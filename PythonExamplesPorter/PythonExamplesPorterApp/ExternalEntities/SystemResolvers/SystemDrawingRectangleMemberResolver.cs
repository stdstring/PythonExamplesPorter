using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    // resolver for System.Drawing.Rectangle and System.Drawing.RectangleF
    internal class SystemDrawingRectangleMemberResolver : ISystemMemberResolver
    {
        public SystemDrawingRectangleMemberResolver(SemanticModel model, AppData appData, String typeName)
        {
            _model = model;
            _appData = appData;
            _typeName = typeName;
            String[] knownNames = {"Rectangle", "RectangleF"};
            if (!knownNames.Contains(typeName))
                throw new InvalidOperationException($"Unsupported name of type: {typeName}");
        }

        public string TypeName => $"System.Drawing.{_typeName}";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
            // TODO (std_string) : add check of arg type
            switch (argumentsRepresentation.Values)
            {
                case [var location, var size]:
                {
                    MemberResolveData ctorData = new MemberResolveData($"{prepareResult.moduleName}{_typeName}({location}, {size})", prepareResult.importData);
                    return new OperationResult<MemberResolveData>.Ok(ctorData);
                }
                case [var x, var y, var width, var height]:
                {
                    String member = $"{prepareResult.moduleName}.{_typeName}({x}, {y}, {width}, {height})";
                    MemberResolveData ctorData = new MemberResolveData(member, prepareResult.importData);
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
                case IPropertySymbol {Name: "Bottom"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "bottom");
                case IPropertySymbol {Name: "Height"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "height");
                case IPropertySymbol {Name: "IsEmpty"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "is_empty");
                case IPropertySymbol {Name: "Left"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "left");
                case IPropertySymbol {Name: "Location"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "location");
                case IPropertySymbol {Name: "Right"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "right");
                case IPropertySymbol {Name: "Size"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "size");
                case IPropertySymbol {Name: "Top"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "top");
                case IPropertySymbol {Name: "Width"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "width");
                case IPropertySymbol {Name: "X"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "x");
                case IPropertySymbol {Name: "Y"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "y");
            }
            return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Drawing.{_typeName}.{memberName}");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly String _typeName;
    }
}