using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis.CSharp;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterApp.Expressions
{
    internal class InitializerExpressionConverter
    {
        public InitializerExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _settings = settings;
        }

        public ConvertResult Convert(InitializerExpressionSyntax expression)
        {
            switch (expression.Kind())
            {
                case SyntaxKind.ArrayInitializerExpression:
                    ArrayCreationConverter converter = new ArrayCreationConverter(_model, _appData, _settings.CreateChild());
                    return converter.Convert(expression);
                default:
                    throw new UnsupportedSyntaxException($"Unsupported initializer expression: {expression.Kind()}");
            }
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExpressionConverterSettings _settings;
    }
}
