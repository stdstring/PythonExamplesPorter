using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemEnvironmentMemberResolver : ISystemMemberResolver
    {
        public SystemEnvironmentMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.Environment";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.Environment");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IPropertySymbol {Name: "NewLine"}:
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData("system_helper.environment.Environment.new_line()", new ImportData().AddImport("system_helper")));
                case IMethodSymbol {Name: "GetFolderPath"}:
                    return ResolveGetFolderPathMethod(data, representation);
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Environment.{memberName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveGetFolderPathMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                case [_]:
                {
                    String member = $"system_helper.environment.Environment.get_folder_path({representation.Arguments.Values[0]})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("system_helper")));
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.Environment.GetFolderPath");
            }
        }

        private readonly SemanticModel _model;
    }
}