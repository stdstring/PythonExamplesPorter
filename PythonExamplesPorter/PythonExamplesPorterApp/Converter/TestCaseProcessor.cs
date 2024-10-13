using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;
using PythonExamplesPorterApp.Utils;
using System.Xml.Linq;

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
            IReadOnlyList<ParameterSyntax> parameters = _node.ParameterList.Parameters;
            Boolean isLastParams = parameters.Last().Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.ParamsKeyword));
            foreach (AttributeSyntax attribute in _node.AttributeLists.GetAttributes(_model, "NUnit.Framework.TestCaseAttribute"))
            {
                if (attribute.ArgumentList == null)
                    continue;
                IReadOnlyList<AttributeArgumentSyntax> arguments = attribute.ArgumentList.Arguments;
                if (arguments.Any(argument => argument.NameColon != null))
                {
                    _appData.Logger.LogError($"Bad {methodName} method: unsupported usage of argument's names in NUnit.Framework.TestCaseAttribute attribute");
                    _methodStorage.SetError("unsupported usage of argument's names in NUnit.Framework.TestCaseAttribute attribute");
                    return false;
                }
                if ((arguments.Count > parameters.Count) && !isLastParams)
                {
                    _appData.Logger.LogError($"Bad {methodName} method: bad NUnit.Framework.TestCaseAttribute attribute's arguments count");
                    _methodStorage.SetError("bad NUnit.Framework.TestCaseAttribute attribute's arguments count");
                    return false;
                }
            }
            return true;
        }

        public void ProcessBefore()
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
                String[] values = ExtractValues(arguments, expressionConverter);
                valuesList.Add(values.Length == 1 ? values.First() : $"({String.Join(", ", values)})");
            }
            foreach (String line in CreateTestCaseForHeader(String.Join(", ", parameters), valuesList))
                _methodStorage.AddBodyLine(line);
            _methodStorage.IncreaseLocalIndentation(StorageDef.IndentationDelta);
        }

        public void ProcessAfter()
        {
            // TODO (std_string) : think about approach
            if (_node.Body!.Statements.Count == 0)
                _methodStorage.AddBodyLine("pass");
            _methodStorage.DecreaseLocalIndentation(StorageDef.IndentationDelta);
        }

        private String[] ExtractValues(IReadOnlyList<AttributeArgumentSyntax> arguments, ExpressionConverter expressionConverter)
        {
            IReadOnlyList<ParameterSyntax> parameters = _node.ParameterList.Parameters;
            Boolean isLastParams = parameters.Last().Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.ParamsKeyword));
            String[] values = new String[parameters.Count];
            Int32 usualParametersCount = parameters.Count - (isLastParams ? 1 : 0);
            for (Int32 parameterIndex = 0; parameterIndex < usualParametersCount; ++parameterIndex)
            {
                if ((parameterIndex >= arguments.Count) && (parameters[parameterIndex].Default == null))
                    throw new UnsupportedSyntaxException("Bad NUnit.Framework.TestCaseAttribute attribute's arguments count");
                ExpressionSyntax expression = parameterIndex < arguments.Count ? arguments[parameterIndex].Expression : parameters[parameterIndex].Default!.Value;
                ConvertResult expressionResult = expressionConverter.Convert(expression);
                if (!expressionResult.AfterResults.IsEmpty())
                    throw new UnsupportedSyntaxException("Unexpected attribute's value conversion result");
                _methodStorage.ImportStorage.Append(expressionResult.ImportData);
                values[parameterIndex] = expressionResult.Result;
            }
            if (isLastParams)
                values[parameters.Count - 1] = ExtractParamsValue(arguments, parameters.Count - 1, expressionConverter);
            return values;
        }

        private String ExtractParamsValue(IReadOnlyList<AttributeArgumentSyntax> arguments, Int32 argumentIndex, ExpressionConverter expressionConverter)
        {
            IList<String> values = new List<String>();
            for (; argumentIndex < arguments.Count; ++argumentIndex)
            {
                ConvertResult expressionResult = expressionConverter.Convert(arguments[argumentIndex].Expression);
                if (!expressionResult.AfterResults.IsEmpty())
                    throw new UnsupportedSyntaxException("Unexpected attribute's value conversion result");
                _methodStorage.ImportStorage.Append(expressionResult.ImportData);
                values.Add(expressionResult.Result);
            }
            return $"[{String.Join(", ", values)}]";
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