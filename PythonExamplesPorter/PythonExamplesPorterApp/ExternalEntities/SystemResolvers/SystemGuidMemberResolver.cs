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
                    MemberResolveData resolveData = new MemberResolveData("uuid.uuid4()", new ImportData().AddImport("uuid"));
                    return new OperationResult<MemberResolveData>.Ok(resolveData);
                case IMethodSymbol {Name: "Parse"}:
                    return ResolveParseMethod(data, representation);
                case IMethodSymbol {Name: "ToString"}:
                    return ResolveToStringMethod(data, representation);
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Guid.{memberName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveToStringMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                case []:
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData($"str({representation.Target})"));
                case [_]:
                {
                    switch (representation.Arguments.Values[0].Replace("\"", ""))
                    {
                        case "D":
                            return new OperationResult<MemberResolveData>.Ok(new MemberResolveData($"str({representation.Target})"));
                        case "B":
                        {
                            String member = "'{' + " + $"str({representation.Target})" + " + '}'";
                            return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member));
                        }
                        default:
                            return new OperationResult<MemberResolveData>.Error("Unsupported arguments type for System.Guid.ToString");
                    }
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.Guid.ToString");
            }
        }

        private OperationResult<MemberResolveData> ResolveParseMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                case [_]:
                {
                    String member = $"uuid.UUID({representation.Arguments.Values[0]})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member, new ImportData().AddImport("uuid")));
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.Guid");
            }
        }

        private readonly SemanticModel _model;
    }
}