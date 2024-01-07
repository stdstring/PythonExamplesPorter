using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Checker;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterApp.Expressions
{
    internal class InvocationExpressionConverter
    {
        public InvocationExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _settings = settings;
        }

        public ConvertResult Convert(InvocationExpressionSyntax expression)
        {
            CheckResult argumentsCheckResult = expression.ArgumentList.GetArguments().CheckForMethod();
            if (!argumentsCheckResult.Result)
                throw new UnsupportedSyntaxException(argumentsCheckResult.Reason);
            switch (expression.Expression)
            {
                case MemberAccessExpressionSyntax memberAccessExpression:
                    MemberAccessExpressionConverter converter = new MemberAccessExpressionConverter(_model, _appData, _settings);
                    return converter.Convert(memberAccessExpression, expression.ArgumentList);
                case IdentifierNameSyntax identifierExpression:
                    throw new UnsupportedSyntaxException($"Unsupported call of method named {identifierExpression.Identifier.ValueText}");
                default:
                    throw new UnsupportedSyntaxException($"Unsupported invocation expression: {expression.Expression.Kind()}");
            }
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExpressionConverterSettings _settings;
    }
}
