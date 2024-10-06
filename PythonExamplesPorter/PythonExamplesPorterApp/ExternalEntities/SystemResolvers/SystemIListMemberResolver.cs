using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemIListMemberResolver : ISystemMemberResolver
    {
        public SystemIListMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.Collections.Generic.IList";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.Collections.Generic.IList");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IPropertySymbol {Name: "Count"}:
                {
                    String member = $"len({representation.Target})";
                    return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member));
                }
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Collections.Generic.IList.{memberName}");
            }
        }

        private readonly SemanticModel _model;
    }
}