using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemGuidMemberResolver : ISystemMemberResolver
    {
        internal SystemGuidMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.Guid";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.Guid");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IMethodSymbol {Name: "NewGuid"}:
                {
                    MemberResolveData resolveData = new MemberResolveData("uuid.uuid4()", new ImportData().AddImport("uuid"));
                    return new OperationResult<MemberResolveData>.Ok(resolveData);
                }
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Guid.{memberName}");
            }
        }

        private readonly SemanticModel _model;
    }
}