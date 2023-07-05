using PythonExamplesPorterApp.Config;

namespace PythonExamplesPorterApp.Ignored
{
    internal class IgnoredEntitiesManager
    {
        public IgnoredEntitiesManager(IgnoredEntities? ignoredEntities)
        {
            _ignoredFiles = new HashSet<String>(ignoredEntities?.Files ?? Array.Empty<String>());
            _ignoredTypes = new HashSet<String>(ignoredEntities?.Types ?? Array.Empty<String>());
            _ignoredMethods = new HashSet<String>(ignoredEntities?.Methods ?? Array.Empty<String>());
        }

        public Boolean IsIgnoredFile(String relativePath)
        {
            return _ignoredFiles.Contains(relativePath);
        }

        public Boolean IsIgnoredType(String fullName)
        {
            return _ignoredTypes.Contains(fullName);
        }

        public Boolean IsIgnoredMethod(String fullName)
        {
            return _ignoredMethods.Contains(fullName);
        }

        private readonly ISet<String> _ignoredFiles;
        private readonly ISet<String> _ignoredTypes;
        private readonly ISet<String> _ignoredMethods;
    }
}
