using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemIoDirectoryMemberResolver : ISystemMemberResolver
    {
        public SystemIoDirectoryMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.IO.Directory";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.IO.Directory");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IMethodSymbol {Name: "CreateDirectory"}:
                    return ResolveCreateDirectoryMethod(data, representation);
                case IMethodSymbol {Name: "GetFiles"}:
                    return ResolveGetFilesMethod(data, representation);
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.IO.Directory.{memberName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveCreateDirectoryMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                case [_]:
                {
                    String member = $"system_helper.io.Directory.create_directory({representation.Arguments.Values[0]})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("system_helper")));
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.IO.Directory.CreateDirectory");
            }
        }

        private OperationResult<MemberResolveData> ResolveGetFilesMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                // path, searchPattern, searchOption
                case [_, _, _]:
                {
                    String member = $"system_helper.io.Directory.get_files({representation.Arguments.Values[0]}, {representation.Arguments.Values[1]}, {representation.Arguments.Values[2]})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("system_helper")));
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.IO.Directory.GetFiles");
            }
        }

        private readonly SemanticModel _model;
    }
}