using System.Text;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.DestStorage;

namespace PythonExamplesPorterApp.Converter
{
    internal record ConvertResult(String Result, IDictionary<String, String> ImportData);

    internal class ExpressionConverter
    {
        public ExpressionConverter(SemanticModel model, ImportStorage importStorage)
        {
            _model = model;
            _importStorage = importStorage;
        }

        public ConvertResult Convert(ExpressionSyntax expression)
        {
            StringBuilder buffer = new StringBuilder();
            IDictionary<String, String> importData = new Dictionary<String, String>();
            ExpressionConverterVisitor visitor = new ExpressionConverterVisitor(_model, _importStorage, buffer, importData);
            visitor.VisitExpression(expression);
            return new ConvertResult(buffer.ToString(), importData);
        }

        private readonly SemanticModel _model;
        private readonly ImportStorage _importStorage;
    }

    internal class ExpressionConverterVisitor : CSharpSyntaxWalker
    {
        public ExpressionConverterVisitor(SemanticModel model, ImportStorage importStorage, StringBuilder buffer, IDictionary<String, String> importData)
        {
            _model = model;
            _importStorage = importStorage;
            _buffer = buffer;
            _importData = importData;
        }

        public void VisitExpression(ExpressionSyntax expression)
        {
            _buffer.Append("<<<some expression>>>");
        }

        private readonly SemanticModel _model;
        private readonly ImportStorage _importStorage;
        private readonly StringBuilder _buffer;
        private readonly IDictionary<String, String> _importData;
    }
}
