using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Converter
{
    internal class TestCaseProcessor
    {
        public TestCaseProcessor(SemanticModel model,AppData appData, MethodDeclarationSyntax node, IMethodSymbol currentMethod, MethodStorage methodStorage)
        {
            _model = model;
            _appData = appData;
            _node = node;
            _currentMethod = currentMethod;
            _methodStorage = methodStorage;
        }

        public Boolean CheckMethodDeclaration()
        {
            String methodName = _node.Identifier.Text;
            IList<IParameterSymbol> parameters = _currentMethod.Parameters;
            if (parameters.IsEmpty())
            {
                _appData.Logger.LogError($"Bad {methodName} method: absence of parameters");
                _methodStorage.SetError("absence of method's parameters");
                return false;
            }
            Boolean hasParamsArg = parameters.Last().IsParams;
            Boolean hasDefaultValue = parameters.Any(parameter => parameter.HasExplicitDefaultValue);
            Boolean hasRefOutModifier = parameters.Any(parameter => parameter.RefKind != RefKind.None);
            if (hasParamsArg || hasDefaultValue || hasRefOutModifier)
            {
                _appData.Logger.LogError($"Bad {methodName} method: unsupported kind of parameters");
                _methodStorage.SetError("unsupported kind of parameters");
                return false;
            }
            return true;
        }

        public void Process()
        {
            String[] parameters = _currentMethod.Parameters
                .Select(parameter => _appData.NameTransformer.TransformLocalVariableName(parameter.Name))
                .ToArray();
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData, new ExpressionConverterSettings());
            AttributeSyntax[] testCaseAttributes = _node.AttributeLists.GetAttributes(_model, "NUnit.Framework.TestCaseAttribute");
            IList<String> valuesList = new List<String>();
            foreach (AttributeSyntax attribute in testCaseAttributes)
            {
                if (attribute.ArgumentList == null)
                    throw new UnsupportedSyntaxException("Bad NUnit.Framework.TestCaseAttribute");
                IReadOnlyList<AttributeArgumentSyntax> arguments = attribute.ArgumentList.Arguments;
                String[] values = new String[arguments.Count];
                for (Int32 argumentIndex = 0; argumentIndex < arguments.Count; ++argumentIndex)
                {
                    ConvertResult expressionResult = expressionConverter.Convert(arguments[argumentIndex].Expression);
                    if (!expressionResult.AfterResults.IsEmpty())
                        throw new UnsupportedSyntaxException("Unexpected attribute's value conversion result");
                    _methodStorage.ImportStorage.Append(expressionResult.ImportData);
                    values[argumentIndex] = expressionResult.Result;
                }
                valuesList.Add(values.Length == 1 ? values.First() : $"({String.Join(", ", values)})");
            }
            foreach (String line in CreateTestCaseForHeader(String.Join(", ", parameters), valuesList))
                _methodStorage.AddBodyLine(line);
            _methodStorage.IncreaseLocalIndentation(StorageDef.IndentationDelta);
        }

        private IList<String> CreateTestCaseForHeader(String parameters, IList<String> valuesList)
        {
            // TODO (std_string) : think about place
            const Int32 maxLength = 80;
            String allInOneLine = $"for {parameters} in [{String.Join(", ", valuesList)}]:";
            if (allInOneLine.Length <= maxLength)
                return new[] { allInOneLine };
            IList<String> lines = new List<String>();
            String forStart = $"for {parameters} in [";
            String valuePrefix = new String(' ', forStart.Length);
            Int32 lastIndex = valuesList.Count - 1;
            for (Int32 index = 0; index < valuesList.Count; ++index)
            {
                String line = $"{(index == 0 ? forStart : valuePrefix)}{valuesList[index]}{(index < lastIndex ? "," : "]:")}";
                lines.Add(line);
            }
            return lines;
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly MethodDeclarationSyntax _node;
        private readonly IMethodSymbol _currentMethod;
        private readonly MethodStorage _methodStorage;
    }
}