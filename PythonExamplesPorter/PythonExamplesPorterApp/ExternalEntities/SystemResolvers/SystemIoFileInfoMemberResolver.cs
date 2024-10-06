using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemIoFileInfoMemberResolver : ISystemMemberResolver
    {
        public SystemIoFileInfoMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public string TypeName => "System.IO.FileInfo";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            String member = $"system_helper.io.FileInfo({argumentsRepresentation.Values[0]})";
            MemberResolveData resolveData = new MemberResolveData(member, new ImportData().AddImport("system_helper"));
            return new OperationResult<MemberResolveData>.Ok(resolveData);
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case IPropertySymbol {Name: "Length"}:
                    return ResolveLengthProperty(data, representation);
                default:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.IO.FileInfo.{memberName}");
            }
        }

        private OperationResult<MemberResolveData> ResolveLengthProperty(MemberData data, MemberRepresentation representation)
        {
            String member = $"{representation.Target}.length()";
            return new OperationResult<MemberResolveData>.Ok(new MemberResolveData(member));
        }

        private readonly SemanticModel _model;
    }
}