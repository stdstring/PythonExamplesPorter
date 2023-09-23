using System.Text;

namespace PythonExamplesPorterApp.Converter
{
    internal static class NameTransformer
    {
        public static String TransformFileObjectName(String fileObjectName)
        {
            return ConvertPascalCaseIntoSnakeCase(fileObjectName);
        }

        public static String TransformNamespaceName(String namespaceName)
        {
            return namespaceName.ToLower();
        }

        public static String TransformClassName(String className)
        {
            return className;
        }

        public static String TransformMethodName(String methodName)
        {
            return ConvertPascalCaseIntoSnakeCase(methodName);
        }

        public static String TransformLocalVariableName(String variableName)
        {
            return ConvertPascalCaseIntoSnakeCase(variableName);
        }

        private static String ConvertPascalCaseIntoSnakeCase(String name)
        {
            StringBuilder builder = new StringBuilder();
            foreach (char ch in name)
            {
                if (Char.IsUpper(ch) && builder.Length > 0)
                    builder.Append('_');
                builder.Append(Char.ToLower(ch));
            }
            return builder.ToString();
        }
    }
}
