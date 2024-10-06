using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemTimeSpanMemberResolver : ISystemMemberResolver
    {
        public SystemTimeSpanMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.TimeSpan";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.TimeSpan");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IMethodSymbol {Name: "FromMinutes"}:
                    return ResolveFromMethod(data, representation, "minutes");
                case IMethodSymbol {Name: "FromSeconds"}:
                    return ResolveFromMethod(data, representation, "seconds");
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.TimeSpan.{memberName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveFromMethod(MemberData data, MemberRepresentation representation, String arg)
        {
            switch (data.Arguments)
            {
                case [_]:
                {
                    String member = $"datetime.timedelta({arg}={representation.Arguments.Values[0]})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("datetime")));
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.TimeSpan");
            }
        }

        private readonly SemanticModel _model;
    }
}