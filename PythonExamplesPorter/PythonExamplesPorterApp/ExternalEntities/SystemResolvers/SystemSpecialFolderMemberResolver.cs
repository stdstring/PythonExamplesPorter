using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemSpecialFolderMemberResolver : ISystemMemberResolver
    {
        public SystemSpecialFolderMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.SpecialFolder";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.SpecialFolder");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IFieldSymbol {Name: "UserProfile"}:
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData("system_helper.environment.SpecialFolder.USER_PROFILE", new ImportData().AddImport("system_helper")));
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.SpecialFolder.{memberName}");
            }
        }

        private readonly SemanticModel _model;
    }
}