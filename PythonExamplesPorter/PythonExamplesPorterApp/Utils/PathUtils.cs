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
                return targetPath.Path;
            return targetPath.RelativePathBase switch
            {
                RelativePathBase.App => Path.Combine(appConfig.AppBaseDirectory, targetPath.Path),
                RelativePathBase.Config => Path.Combine(appConfig.ConfigBaseDirectory, targetPath.Path),
                _ => throw new InvalidOperationException("Bad targetPath.RelativePathBase value")
            };
        }
    }
}
