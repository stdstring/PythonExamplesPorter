using Microsoft.CodeAnalysis.CSharp.Syntax;
using System.Globalization;
using PythonExamplesPorterApp.DestStorage;

namespace PythonExamplesPorterApp.Expressions
{
    internal class LiteralExpressionConverter
    {
        public ConvertResult Convert(LiteralExpressionSyntax expression)
        {
            String text = expression.Token.Value switch
            {
                null => expression.Token.Text,
                Double value => value.ToString(CultureInfo.InvariantCulture),
                Single value => value.ToString(CultureInfo.InvariantCulture),
                Boolean value => value ? "True" : "False",
                // TODO (std_string) : there are problems with some unicode symbols - investigate their
                String _ when expression.Token.Text.StartsWith('@') => $"\"\"{expression.Token.Text.Substring(1)}\"\"",
                String => expression.Token.Text,
                var value => value.ToString() ?? expression.Token.Text
            };
            return new ConvertResult(text, new ImportData());
        }
    }
}
