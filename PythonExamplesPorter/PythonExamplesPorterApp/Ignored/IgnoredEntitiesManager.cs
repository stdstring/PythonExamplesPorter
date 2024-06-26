﻿namespace PythonExamplesPorterApp.Ignored
{
    internal class IgnoredEntitiesManager
    {
        public IgnoredEntitiesManager(IgnoredEntities? ignoredEntities)
        {
            _ignoredDirectories = ignoredEntities?.Directories?.Select(dir => dir.EndsWith('\\') ? dir : $"{dir}\\").ToArray() ?? Array.Empty<String>();
            _ignoredFiles = new HashSet<String>(ignoredEntities?.Files ?? Array.Empty<String>());
            _ignoredTypes = new HashSet<String>(ignoredEntities?.Types ?? Array.Empty<String>());
            _ignoredMethods = new HashSet<String>(ignoredEntities?.Methods ?? Array.Empty<String>());
            _ignoredMethodsBody = new HashSet<String>(ignoredEntities?.MethodsBody ?? Array.Empty<String>());
        }

        public Boolean IsIgnoredFile(String relativePath) => _ignoredDirectories.Any(relativePath.StartsWith) ||
                                                             _ignoredFiles.Contains(relativePath);
        public Boolean IsIgnoredType(String fullName) => _ignoredTypes.Contains(fullName);

        public Boolean IsIgnoredMethod(String fullName) => _ignoredMethods.Contains(fullName);

        public Boolean IsIgnoredMethodBody(String fullName) => _ignoredMethodsBody.Contains(fullName);

        private readonly String[] _ignoredDirectories;
        private readonly ISet<String> _ignoredFiles;
        private readonly ISet<String> _ignoredTypes;
        private readonly ISet<String> _ignoredMethods;
        private readonly ISet<String> _ignoredMethodsBody;
    }
}
