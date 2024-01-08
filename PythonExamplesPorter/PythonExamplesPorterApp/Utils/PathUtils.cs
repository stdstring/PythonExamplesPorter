using PythonExamplesPorterApp.Config;

namespace PythonExamplesPorterApp.Utils
{
    internal static class PathUtils
    {
        public static String ResolveTargetPath(this TargetPath? targetPath, AppConfig appConfig)
        {
            if (targetPath == null)
                throw new ArgumentNullException(nameof(targetPath));
            if (Path.IsPathFullyQualified(targetPath.Path))
                return NormalizeFullPath(targetPath.Path);
            return targetPath.RelativePathBase switch
            {
                RelativePathBase.App => NormalizeFullPath(Path.Combine(appConfig.AppBaseDirectory, targetPath.Path)),
                RelativePathBase.Config => NormalizeFullPath(Path.Combine(appConfig.ConfigBaseDirectory, targetPath.Path)),
                _ => throw new InvalidOperationException("Bad targetPath.RelativePathBase value")
            };
        }

        public static String NormalizeFullPath(String source)
        {
            return Path.GetFullPath(new Uri(source).LocalPath).TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
        }
    }
}
