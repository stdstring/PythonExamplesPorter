using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemStringMemberResolver : ISystemMemberResolver
    {
        public SystemStringMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.String";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.String");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.String.{memberName}");
                case IMethodSymbol {Name: "Contains"}:
                    return ResolveContainsMethod(data, representation);
                case IMethodSymbol {Name: "Replace"}:
                    return ResolveReplaceMethod(data, representation);
                case IMethodSymbol {Name: "StartsWith"}:
                    return ResolveStartsWithMethod(data, representation);
                case IMethodSymbol {Name: "Trim"}:
                    return ResolveTrimMethod(data, representation);
            }
            return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.String.{memberName}");
        }

        private OperationResult<MemberResolveData> ResolveTrimMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                case []:
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData($"{representation.Target}.strip()"));
                case [var arg]:
                    switch (arg.Expression)
                    {
                        // TODO (std_string) : for some unknown reasons, roslyn resolve String.Trim(Char) method as String.Trim(params Char[]) - investigate this
                        case LiteralExpressionSyntax:
                        {
                            String member = $"{representation.Target}.strip({representation.Arguments.Values[0].Trim('[', ']')})";
                            MemberResolveData memberData = new MemberResolveData(member);
                            return new OperationResult<MemberResolveData>.Ok(memberData);
                        }
                        default:
                            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.String.Trim");
                    }
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.String.Trim");
        }

        private OperationResult<MemberResolveData> ResolveStartsWithMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                // TODO (std_string) : add check of arg type
                case [_]:
                {
                    String member = $"{representation.Target}.startswith({representation.Arguments.Values[0]})";
                    MemberResolveData memberData = new MemberResolveData(member);
                    return new OperationResult<MemberResolveData>.Ok(memberData);
                }
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.String.StartsWith");
        }

        private OperationResult<MemberResolveData> ResolveContainsMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                // TODO (std_string) : add check of arg type
                case [_]:
                {
                    String member = $"({representation.Arguments.Values[0]} in {representation.Target})";
                    MemberResolveData memberData = new MemberResolveData(member);
                    return new OperationResult<MemberResolveData>.Ok(memberData);
                }
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.String.Contains");
        }

        private OperationResult<MemberResolveData> ResolveReplaceMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                // TODO (std_string) : add check of arg type
                case [_, _]:
                {
                    String member = $"{representation.Target}.replace({representation.Arguments.Values[0]}, {representation.Arguments.Values[1]})";
                    MemberResolveData memberData = new MemberResolveData(member);
                    return new OperationResult<MemberResolveData>.Ok(memberData);
                }
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.String.Replace");
        }

        private readonly SemanticModel _model;
    }
}