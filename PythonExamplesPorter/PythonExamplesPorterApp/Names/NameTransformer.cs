using PythonExamplesPorterApp.Common;

namespace PythonExamplesPorterApp.Names
{
    internal class NameTransformer
    {
        public NameTransformer(INameTransformStrategy transformStrategy, IHandmadeNameManager manager)
        {
            _transformStrategy = transformStrategy;
            _simpleFileObjectStrategy = new SimpleFileObjectConverter();
            _manager = manager;
        }

        public String TransformFileObjectName(String fileObjectName)
        {
            return _simpleFileObjectStrategy.ConvertPascalCaseIntoSnakeCase(fileObjectName);
        }

        public String TransformNamespaceName(String namespaceName)
        {
            return namespaceName.ToLower();
        }

        public String TransformTypeName(String typeName)
        {
            return typeName;
        }

        public String TransformMethodName(String typeName, String methodName)
        {
            return TransformImpl(typeName, methodName);
        }

        public String TransformPropertyName(String typeName, String propertyName)
        {
            return TransformImpl(typeName, propertyName);
        }

        public String TransformFieldName(String typeName, String fieldName)
        {
            return TransformImpl(typeName, fieldName);
        }

        public String TransformStaticReadonlyFieldName(String typeName, String fieldName)
        {
            return TransformImpl(typeName, fieldName).ToUpper();
        }

        public String TransformEnumValueName(String typeName, String enumValueName)
        {
            return TransformImpl(typeName, enumValueName).ToUpper();
        }

        public String TransformLocalVariableName(String variableName)
        {
            return _transformStrategy.ConvertPascalCaseIntoSnakeCase(variableName);
        }

        private String TransformImpl(String typeName, String memberName)
        {
            return _manager.Search(typeName, memberName) switch
            {
                OperationResult<String>.Ok(Data: var result) => result,
                OperationResult<String>.Error => _transformStrategy.ConvertPascalCaseIntoSnakeCase(memberName),
                _ => throw new InvalidOperationException("Unexpected control flow branch")
            };
        }

        private readonly INameTransformStrategy _transformStrategy;
        private readonly INameTransformStrategy _simpleFileObjectStrategy;
        private readonly IHandmadeNameManager _manager;
    }
}
