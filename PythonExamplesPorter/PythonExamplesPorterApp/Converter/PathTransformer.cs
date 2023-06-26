namespace PythonExamplesPorterApp.Converter
{
    internal static class PathTransformer
    {
        public static String TransformPath(String sourcePath)
        {
            String[] parts = sourcePath.Split(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
            String[] result = new String[parts.Length];
            for (Int32 index = 0; index < parts.Length; ++index)
                result[index] = index < parts.Length - 1
                    ? NameTransformer.TransformFileObjectName(parts[index])
                    : $"{NameTransformer.TransformFileObjectName(Path.GetFileNameWithoutExtension(parts[index]))}.py";
            return String.Join(Path.DirectorySeparatorChar, result);
        }
    }
}