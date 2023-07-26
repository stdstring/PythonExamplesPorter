using System.Reflection;

namespace ApiExamples
{
    public class ApiExampleBase
    {
        internal static String AssemblyDir { get; }

        internal static String CodeBaseDir { get; }

        internal static String LicenseDir { get; }

        internal static String ArtifactsDir { get; }

        internal static String GoldsDir { get; }

        internal static String RootDataDir { get; }

        internal static String OutputDir { get; }

        private static String GetAssemblyDir(Assembly assembly)
        {
            Uri uri = new Uri(assembly.Location);
            return Path.GetDirectoryName(uri.LocalPath) + Path.DirectorySeparatorChar;
        }

        private static String GetCodeBaseDir(Assembly assembly)
        {
            Uri uri = new Uri(assembly.Location);
            Int32 projectDirIndex = uri.LocalPath.IndexOf("AWModelLibrary.Examples", StringComparison.Ordinal);
            String mainFolder = Path.GetDirectoryName(uri.LocalPath)?.Substring(0, projectDirIndex) ?? "";
            return mainFolder;
        }

        static ApiExampleBase()
        {
            AssemblyDir = GetAssemblyDir(Assembly.GetExecutingAssembly());
            CodeBaseDir = GetCodeBaseDir(Assembly.GetExecutingAssembly());
            ArtifactsDir = new Uri(new Uri(CodeBaseDir), @"AWModelLibrary.Examples.Data/Artifacts/").LocalPath;
            LicenseDir = new Uri(new Uri(CodeBaseDir), @"AWModelLibrary.Examples.Data/License/").LocalPath;
            GoldsDir = new Uri(new Uri(CodeBaseDir), @"AWModelLibrary.Examples.Data/Golds/").LocalPath;
            RootDataDir = new Uri(new Uri(CodeBaseDir), @"AWModelLibrary.Examples.Data/").LocalPath;
            OutputDir = new Uri(new Uri(CodeBaseDir), @"AWModelLibrary.Examples.Data/Output/").LocalPath;
        }
    }
}
