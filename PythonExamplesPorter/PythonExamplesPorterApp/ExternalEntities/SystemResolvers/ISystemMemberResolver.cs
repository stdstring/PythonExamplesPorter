using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal interface ISystemMemberResolver
    {
        public string TypeName { get; }

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation);

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation);
    }
}