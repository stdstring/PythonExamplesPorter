using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemDateTimeMemberResolver : ISystemMemberResolver
    {
        internal SystemDateTimeMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.DateTime";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            ImportData import = new ImportData().AddImport("datetime");
            switch (argumentsRepresentation.Values)
            {
                // TODO: add check of arg type
                // year, month, day
                case [_, _, _]:
                // year, month, day, hour, minute, second
                case [_, _, _, _, _, _]:
                {
                    MemberResolveData resolveData = new MemberResolveData($"datetime.datetime({String.Join(",", argumentsRepresentation.Values)})", import);
                    return new OperationResult<MemberResolveData>.Ok(resolveData);
                }
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for ctor System.String.DateTime");
            }
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IPropertySymbol {Name: "Now"}:
                    return ResolveProperty("datetime", "now");
                case IPropertySymbol {Name: "Today"}:
                    return ResolveProperty("date", "today");
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.DateTime.{memberName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveProperty(String className, String methodName)
        {
            MemberResolveData resolveData = new MemberResolveData($"datetime.{className}.{methodName}()", new ImportData().AddImport("datetime"));
            return new OperationResult<MemberResolveData>.Ok(resolveData);
        }

        private readonly SemanticModel _model;
    }
}