using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemConsoleMemberResolver : ISystemMemberResolver
    {
        internal SystemConsoleMemberResolver(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _settings = settings;
        }

        public string TypeName => "System.Console";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.Console");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IMethodSymbol {Name: "WriteLine"}:
                    return ResolveWriteLineMethod(data);
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Console.{memberName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveWriteLineMethod(MemberData data)
        {
            switch (data.Arguments)
            {
                case []:
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData("print()"));
                case [_]:
                {
                    String member = $"print({ConvertExpressions(data.Arguments)[0]})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member));
                }
                default:
                {
                    if (!(data.Arguments[0].Expression is LiteralExpressionSyntax))
                        return new OperationResult<MemberResolveData>.Error("Unsupported arguments for System.Console.WriteLine");
                    IList<String> convertResult = ConvertExpressions(data.Arguments);
                    String member = $"print({convertResult[0]}.format({String.Join(",", convertResult.ToArray()[1..])}))";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member));
                }
            }
        }

        private IList<String> ConvertExpressions(IReadOnlyList<ArgumentSyntax> arguments)
        {
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData, _settings);
            return arguments.Select(arg => expressionConverter.Convert(arg.Expression).Result).ToList();
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExpressionConverterSettings _settings;
    }
}