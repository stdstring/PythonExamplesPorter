using PythonExamplesPorterApp.Common;

namespace PythonExamplesPorterApp.Names
{
    internal class NameTransformer
    {
        public NameTransformer(INameTransformStrategy transformStrategy, IHandmadeNameManager manager)
        {
            _transformStrategy = transformStrategy;
            _manager = manager;
        }

        public String TransformFileObjectName(String fileObjectName)
        {
            return _transformStrategy.ConvertPascalCaseIntoSnakeCase(fileObjectName);
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
            OperationResult<String> handmadeResult = _manager.Search(typeName, methodName);
            return handmadeResult.Success
                ? handmadeResult.Data!
                : _transformStrategy.ConvertPascalCaseIntoSnakeCase(methodName);
        }

        public String TransformPropertyName(String typeName, String propertyName)
        {
            OperationResult<String> handmadeResult = _manager.Search(typeName, propertyName);
            return handmadeResult.Success
            ? handmadeResult.Data!
                : _transformStrategy.ConvertPascalCaseIntoSnakeCase(propertyName);
        }

        public String TransformFieldName(String typeName, String fieldName)
        {
            OperationResult<String> handmadeResult = _manager.Search(typeName, fieldName);
            return handmadeResult.Success
                ? handmadeResult.Data!
                : _transformStrategy.ConvertPascalCaseIntoSnakeCase(fieldName);
        }

        public String TransformEnumValueName(String typeName, String enumValueName)
        {
            OperationResult<String> handmadeResult = _manager.Search(typeName, enumValueName);
            String destName = handmadeResult.Success ? handmadeResult.Data! : _transformStrategy.ConvertPascalCaseIntoSnakeCase(enumValueName);
            return destName.ToUpper();
        }

        public String TransformLocalVariableName(String variableName)
        {
            return _transformStrategy.ConvertPascalCaseIntoSnakeCase(variableName);
        }

        private readonly INameTransformStrategy _transformStrategy;
        private readonly IHandmadeNameManager _manager;
    }
}
