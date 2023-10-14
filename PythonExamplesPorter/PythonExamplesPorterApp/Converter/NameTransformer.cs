﻿using System.Text;

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

        public static String TransformPropertyName(String propertyName)
        {
            return ConvertPascalCaseIntoSnakeCase(propertyName);
        }

        public static String TransformFieldName(String fieldName)
        {
            return ConvertPascalCaseIntoSnakeCase(fieldName);
        }

        public static String TransformEnumValueName(String fieldName)
        {
            return ConvertPascalCaseIntoSnakeCase(fieldName).ToUpper();
        }

        public static String TransformLocalVariableName(String variableName)
        {
            return ConvertPascalCaseIntoSnakeCase(variableName);
        }

        private static String ConvertPascalCaseIntoSnakeCase(String name)
        {
            StringBuilder builder = new StringBuilder();
            builder.Append(Char.ToLower(name[0]));
            for (Int32 index = 1; index < name.Length; ++index)
            {
                if (Char.IsUpper(name[index]) && !Char.IsUpper(name[index - 1]))
                    builder.Append('_');
                builder.Append(Char.ToLower(name[index]));
            }
            return builder.ToString();
        }
    }
}
