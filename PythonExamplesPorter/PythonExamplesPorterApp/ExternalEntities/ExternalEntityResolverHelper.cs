using PythonExamplesPorterApp.Common;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal static class ExternalEntityResolverHelper
    {
        public static OperationResult<MemberResolveData> ResolveInstanceProperty(MemberRepresentation representation, String propertyName)
        {
            MemberResolveData memberData = new MemberResolveData($"{representation.Target}.{propertyName}");
            return new OperationResult<MemberResolveData>.Ok(memberData);
        }
    }
}
