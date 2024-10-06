using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemIoFileMemberResolver : ISystemMemberResolver
    {
        public SystemIoFileMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.IO.File";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.IO.File");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IMethodSymbol {Name: "Exists"}:
                    return ResolveExistMethod(representation);
                case IMethodSymbol {Name: "ReadAllBytes"}:
                    return ResolveReadAllBytesMethod(data, representation);
                case IMethodSymbol {Name: "ReadAllText"}:
                    return ResolveReadAllTextMethod(data, representation);
                case IMethodSymbol {Name: "WriteAllBytes"}:
                    return ResolveWriteAllBytesMethod(representation);
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.IO.File.{memberName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveWriteAllBytesMethod(MemberRepresentation representation)
        {
            String member = $"system_helper.io.File.write_all_bytes({representation.Arguments.Values[0]}, {representation.Arguments.Values[1]})";
            return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("system_helper")));
        }

        private OperationResult<MemberResolveData> ResolveExistMethod(MemberRepresentation representation)
        {
            String member = $"system_helper.io.File.exist({representation.Arguments.Values[0]})";
            return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("system_helper")));
        }

        private OperationResult<MemberResolveData> ResolveReadAllBytesMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                case [_]:
                {
                    String member = $"system_helper.io.File.read_all_bytes({representation.Arguments.Values[0]})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("system_helper")));
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.IO.File");
            }
        }

        private OperationResult<MemberResolveData> ResolveReadAllTextMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                case [_]:
                {
                    String member = $"system_helper.io.File.read_all_text({representation.Arguments.Values[0]})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("system_helper")));
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.IO.File");
            }
        }

        private readonly SemanticModel _model;
    }
}