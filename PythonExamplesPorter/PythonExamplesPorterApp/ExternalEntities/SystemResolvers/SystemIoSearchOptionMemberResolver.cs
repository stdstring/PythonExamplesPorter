using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemIoSearchOptionMemberResolver : ISystemMemberResolver
    {
        public SystemIoSearchOptionMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.IO.SearchOption";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.IO.SearchOption");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IFieldSymbol {Name: "AllDirectories"}:
                    _model.GetSymbolInfo(memberName);
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData("system_helper.io.SearchOption.All_DIRECTORIES", new ImportData().AddImport("system_helper")));
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.IO.SearchOption.{memberName}");
            }
        }

        private readonly SemanticModel _model;
    }
}