using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemIoPathMemberResolver : ISystemMemberResolver
    {
        public SystemIoPathMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.IO.Path";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.IO.Path");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IMethodSymbol {Name: "Combine"}:
                    return ResolveCombineMethod(data, representation);
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.IO.Path.{memberName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveCombineMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                case [_, _]:
                case [_, _, _]:
                case [_, _, _, _]:
                {
                    String member = $"os.path.join({String.Join(", ", representation.Arguments.Values)})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("os")));
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.IO.Path");
            }
        }

        private readonly SemanticModel _model;
    }
}