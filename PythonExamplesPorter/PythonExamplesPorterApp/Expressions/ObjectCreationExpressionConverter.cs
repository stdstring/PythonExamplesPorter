using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Checker;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.ExternalEntities;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Expressions
{
    internal class ObjectCreationExpressionConverter
    {
        public ObjectCreationExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _settings = settings;
            _expressionConverter = new ExpressionConverter(model, appData, settings);
            _externalEntityResolver = new ExternalEntityResolver(model, appData, settings);
        }

        public ConvertResult Convert(ObjectCreationExpressionSyntax expression)
        {
            ImportData importData = new ImportData();
            IReadOnlyList<ArgumentSyntax> arguments = expression.ArgumentList.GetArguments();
            CheckResult argumentsCheckResult = arguments.CheckForMethod();
            if (!argumentsCheckResult.Result)
                throw new UnsupportedSyntaxException(argumentsCheckResult.Reason);
            if ((expression.Initializer is {Expressions.Count: > 0}) && !_settings.AllowObjectInitializer)
                throw new UnsupportedSyntaxException("Forbidden object initializer");
            TypeSyntax type = expression.Type;
            ArgumentListConverter argumentListConverter = new ArgumentListConverter(_model, _appData, _settings.CreateChild());
            ConvertArgumentsResult convertedArguments = argumentListConverter.Convert(expression, arguments);
            importData.Append(convertedArguments.ImportData);
            MemberResolveData resolveData = _externalEntityResolver.ResolveCtor(type, arguments, convertedArguments.Result).MustSuccess();
            importData.Append(resolveData.ImportData);
            IList<String> afterResults = new List<String>();
            if (expression.Initializer is {Expressions.Count: > 0})
                afterResults.AddRange(ConvertObjectInitializerExpressions(expression.Initializer.Expressions, importData));
            return new ConvertResult(resolveData.Member, importData, afterResults);
        }

        private IList<String> ConvertObjectInitializerExpressions(IReadOnlyList<ExpressionSyntax> initializerExpressions, ImportData importData)
        {
            IList<String> destExpressions = new List<String>();
            // TODO (std_string) : this is simple approach. Think about smarter one
            foreach (ExpressionSyntax expression in initializerExpressions)
            {
                switch (expression)
                {
                    case AssignmentExpressionSyntax {Left: IdentifierNameSyntax identifier} expr when expr.Kind() == SyntaxKind.SimpleAssignmentExpression:
                        // TODO (std_string) : check identifier: is this field, property or something else
                        ITypeSymbol expressionType = identifier.GetExpressionTypeSymbol(_model)
                            .MustSuccess("Unsupported object initializer expression: {0}");
                        String sourceTypeFullName = expressionType.GetTypeFullName();
                        String name = _appData.NameTransformer.TransformPropertyName(sourceTypeFullName, identifier.Identifier.Text);
                        ConvertResult expressionResult = _expressionConverter.Convert(expr.Right);
                        importData.Append(expressionResult.ImportData);
                        destExpressions.Add($"{name} = {expressionResult.Result}");
                        foreach (String child in expressionResult.AfterResults)
                            destExpressions.Add($"{name}.{child}");
                        break;
                    default:
                        throw new UnsupportedSyntaxException($"Unsupported object initializer expression: {expression}");
                }
            }
            return destExpressions;
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExpressionConverterSettings _settings;
        private readonly ExpressionConverter _expressionConverter;
        private readonly ExternalEntityResolver _externalEntityResolver;
    }
}
