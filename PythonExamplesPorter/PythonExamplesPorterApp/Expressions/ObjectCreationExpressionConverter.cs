using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Checker;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;
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
            _externalEntityResolver = new ExternalEntityResolver(model, appData);
        }

        public ConvertResult Convert(ObjectCreationExpressionSyntax expression)
        {
            ImportData importData = new ImportData();
            CheckResult argumentsCheckResult = expression.ArgumentList.GetArguments().CheckForMethod();
            if (!argumentsCheckResult.Result)
                throw new UnsupportedSyntaxException(argumentsCheckResult.Reason);
            if ((expression.Initializer is {Expressions.Count: > 0}) && !_settings.AllowObjectInitializer)
                throw new UnsupportedSyntaxException("Forbidden object initializer");
            TypeSyntax type = expression.Type;
            OperationResult<TypeResolveData> resolveResult = _externalEntityResolver.ResolveType(type);
            if (!resolveResult.Success)
                throw new UnsupportedSyntaxException(resolveResult.Reason);
            TypeResolveData data = resolveResult.Data!;
            // TODO (std_string) : i return empty type for system type because we need in additional analysis - think about approach
            if (String.IsNullOrEmpty(data.TypeName))
                throw new UnsupportedSyntaxException($"Unsupported type: {type}");
            importData.AddImport(data.ModuleName);
            ArgumentListConverter argumentListConverter = new ArgumentListConverter(_model, _appData, _settings.CreateChild());
            ConvertArgumentsResult arguments = argumentListConverter.Convert(expression, expression.ArgumentList.GetArguments());
            importData.Append(arguments.ImportData);
            String result = $"{data.ModuleName}.{data.TypeName}({String.Join(", ", arguments.Result.GetArguments(true))})";
            IList<String> afterResults = new List<String>();
            if (expression.Initializer is {Expressions.Count: > 0})
                afterResults.AddRange(ConvertObjectInitializerExpressions(expression.Initializer.Expressions, importData));
            return new ConvertResult(result, importData, afterResults);
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
                        OperationResult<ITypeSymbol> expressionType = identifier.GetExpressionTypeSymbol(_model);
                        if (!expressionType.Success)
                            throw new UnsupportedSyntaxException($"Unsupported object initializer expression: {expressionType.Reason}");
                        String sourceTypeFullName = expressionType.Data!.GetTypeFullName();
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
