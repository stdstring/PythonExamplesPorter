using System.Text;

namespace PythonExamplesPorterApp.Utils
{
    internal static class StringUtils
    {
        public static String Escape(String source)
        {
            StringBuilder dest = new StringBuilder();
            foreach (Char ch in source)
            {
                switch (ch)
                {
                    case '"':
                        dest.Append("\\\"");
                        break;
                    case '\r':
                        dest.Append("\\\\r");
                        break;
                    case '\n':
                        dest.Append("\\\\n");
                        break;
                    case '\t':
                        dest.Append("\\\\t");
                        break;
                    case '\\':
                        dest.Append("\\\\");
                        break;
                    default:
                        dest.Append(ch);
                        break;
                }
            }
            return dest.ToString();
        }
    }
}
