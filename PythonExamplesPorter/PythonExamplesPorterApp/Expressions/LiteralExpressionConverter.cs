using Microsoft.CodeAnalysis.CSharp.Syntax;
using System.Globalization;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Expressions
{
    internal class LiteralExpressionConverter
    {
        public ConvertResult Convert(LiteralExpressionSyntax expression)
        {
            LiteralConverter literalConverter = new LiteralConverter();
            String text = literalConverter.Convert(expression);
            return new ConvertResult(text, new ImportData());
        }
    }

    internal class LiteralConverter
    {
        public String Convert(LiteralExpressionSyntax expression)
        {
            return expression.Token.Value switch
            {
                null => expression.Token.Text,
                Double value => value.ToString(CultureInfo.InvariantCulture),
                Single value => value.ToString(CultureInfo.InvariantCulture),
                Boolean value => value ? "True" : "False",
                Char value => $"\"{StringUtils.ConvertEscapeSequences(expression.Token.Text.Trim('\''))}\"",
                // TODO (std_string) : there are problems with some unicode symbols - investigate their
                String _ when expression.Token.Text.StartsWith('@') => $"\"\"{StringUtils.ConvertEscapeSequences(expression.Token.Text.Substring(1))}\"\"",
                String => StringUtils.ConvertEscapeSequences(expression.Token.Text),
                var value => value.ToString() ?? expression.Token.Text
            };
        }
    }
}
