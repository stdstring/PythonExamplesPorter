using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities.SystemResolvers
{
    internal class SystemDrawingColorMemberResolver : ISystemMemberResolver
    {
        public SystemDrawingColorMemberResolver(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
        }

        public string TypeName => "System.Drawing.Color";

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error($"Unsupported ctor for System.Drawing.Color");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Drawing.Color.{memberName}");
                case IPropertySymbol {IsStatic: true, Name: var name}:
                    return ResolveColorDefinitionProperty(name);
                case IFieldSymbol {Name: "Empty"}:
                    return ResolveEmptyField();
                case IPropertySymbol {Name: "A"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "a");
                case IPropertySymbol {Name: "R"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "r");
                case IPropertySymbol {Name: "G"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "g");
                case IPropertySymbol {Name: "B"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "b");
                case IMethodSymbol {Name: "ToArgb"}:
                    return ResolveToArgbMethod(representation);
                case IMethodSymbol {Name: "FromArgb"}:
                    return ResolveFromArgbMethod(representation);
            }
            return new OperationResult<MemberResolveData>.Error($"Unsupported member: System.Drawing.Color.{memberName}");
        }

        private OperationResult<MemberResolveData> ResolveColorDefinitionProperty(String sourceColorName)
        {
            // TODO (std_string) : probably some static properties may be not a colors. we need to check this
            String destColorName = _appData.NameTransformer.TransformPropertyName("System.Drawing.Color", sourceColorName);
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
            MemberResolveData colorData = new MemberResolveData($"{prepareResult.moduleName}.Color.{destColorName}", prepareResult.importData);
            return new OperationResult<MemberResolveData>.Ok(colorData);
        }

        private OperationResult<MemberResolveData> ResolveEmptyField()
        {
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
            MemberResolveData colorData = new MemberResolveData($"{prepareResult.moduleName}.Color.empty()", prepareResult.importData);
            return new OperationResult<MemberResolveData>.Ok(colorData);
        }

        private OperationResult<MemberResolveData> ResolveFromArgbMethod(MemberRepresentation representation)
        {
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
            String arguments = String.Join(", ", representation.Arguments.Values);
            MemberResolveData colorData = new MemberResolveData($"{prepareResult.moduleName}.Color.from_argb({arguments})", prepareResult.importData);
            return new OperationResult<MemberResolveData>.Ok(colorData);
        }

        private OperationResult<MemberResolveData> ResolveToArgbMethod(MemberRepresentation representation)
        {
            // the only signature is System.Drawing.Color.ToArgb()
            MemberResolveData memberData = new MemberResolveData($"{representation.Target}.to_argb()");
            return new OperationResult<MemberResolveData>.Ok(memberData);
        }

        private readonly AppData _appData;
        private readonly SemanticModel _model;
    }
}