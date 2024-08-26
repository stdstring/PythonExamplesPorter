using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    // resolver for System.Drawing.Size and System.Drawing.SizeF
    internal class SystemDrawingSizeMemberResolver : ISystemMemberResolver
    {
        public SystemDrawingSizeMemberResolver(SemanticModel model, AppData appData, String typeName)
        {
            _model = model;
            _appData = appData;
            _typeName = typeName;
            String[] knownNames = {"Size", "SizeF"};
            if (!knownNames.Contains(typeName))
                throw new InvalidOperationException($"Unsupported name of type: {typeName}");
        }

        public string TypeName => $"System.Drawing.{_typeName}";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            // TODO (std_string) : add check of arg type
            switch (argumentsRepresentation.Values)
            {
                case [var width, var height]:
                {
                    (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
                    MemberResolveData ctorData = new MemberResolveData($"{prepareResult.moduleName}.{_typeName}({width}, {height})", prepareResult.importData);
                    return new OperationResult<MemberResolveData>.Ok(ctorData);
                }
            }
            return new OperationResult<MemberResolveData>.Error($"Not supported now for System.Drawing.{_typeName}");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Drawing.{_typeName}.{memberName}");
                case IPropertySymbol {Name: "Height"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "height");
                case IPropertySymbol {Name: "IsEmpty"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "is_empty");
                case IPropertySymbol {Name: "Width"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "width");
            }
            return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Drawing.{_typeName}.{memberName}");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly String _typeName;
    }
}