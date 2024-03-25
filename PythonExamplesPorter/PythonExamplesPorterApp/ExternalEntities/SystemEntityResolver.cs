using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal class SystemEntityResolver : IExternalEntityResolver
    {
        public SystemEntityResolver(SemanticModel model, AppData appData)
        {
            _systemStringResolver = new SystemStringMemberResolver(model);
            _systemDrawingColorResolver = new SystemDrawingColorMemberResolver(model, appData);
            _systemDrawingPointResolver = new SystemDrawingPointMemberResolver(model, appData, "Point");
            _systemDrawingPointFResolver = new SystemDrawingPointMemberResolver(model, appData, "PointF");
            _systemDrawingSizeResolver = new SystemDrawingSizeMemberResolver(model, appData, "Size");
            _systemDrawingSizeFResolver = new SystemDrawingSizeMemberResolver(model, appData, "SizeF");
            _systemDrawingRectangleResolver = new SystemDrawingRectangleMemberResolver(model, appData, "Rectangle");
            _systemDrawingRectangleFResolver = new SystemDrawingRectangleMemberResolver(model, appData, "RectangleF");
        }

        public OperationResult<MemberResolveData> ResolveCtor(ITypeSymbol sourceType, IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            switch (sourceTypeFullName)
            {
                case "System.Drawing.PointF":
                    return _systemDrawingPointFResolver.ResolveCtor(argumentsData, argumentsRepresentation);
                case "System.Drawing.Point":
                    return _systemDrawingPointResolver.ResolveCtor(argumentsData, argumentsRepresentation);
                case "System.Drawing.SizeF":
                    return _systemDrawingSizeFResolver.ResolveCtor(argumentsData, argumentsRepresentation);
                case "System.Drawing.Size":
                    return _systemDrawingSizeResolver.ResolveCtor(argumentsData, argumentsRepresentation);
                case "System.Drawing.RectangleF":
                    return _systemDrawingRectangleFResolver.ResolveCtor(argumentsData, argumentsRepresentation);
                case "System.Drawing.Rectangle":
                    return _systemDrawingRectangleResolver.ResolveCtor(argumentsData, argumentsRepresentation);
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported type: {sourceTypeFullName}");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            switch (sourceTypeFullName)
            {
                case "System.String":
                    return _systemStringResolver.ResolveMember(data, representation);
                case "System.Drawing.Color":
                    return _systemDrawingColorResolver.ResolveMember(data, representation);
                case "System.Drawing.PointF":
                    return _systemDrawingPointFResolver.ResolveMember(data, representation);
                case "System.Drawing.Point":
                    return _systemDrawingPointResolver.ResolveMember(data, representation);
                case "System.Drawing.SizeF":
                    return _systemDrawingSizeFResolver.ResolveMember(data, representation);
                case "System.Drawing.Size":
                    return _systemDrawingSizeResolver.ResolveMember(data, representation);
                case "System.Drawing.RectangleF":
                    return _systemDrawingRectangleFResolver.ResolveMember(data, representation);
                case "System.Drawing.Rectangle":
                    return _systemDrawingRectangleResolver.ResolveMember(data, representation);
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported type: {sourceTypeFullName}");
        }

        public OperationResult<CastResolveData> ResolveCast(ExpressionSyntax sourceExpression, ITypeSymbol castTypeSymbol, String sourceRepresentation)
        {
            return new OperationResult<CastResolveData>(false, "Not supported now");
        }

        private readonly SystemStringMemberResolver _systemStringResolver;
        private readonly SystemDrawingColorMemberResolver _systemDrawingColorResolver;
        private readonly SystemDrawingPointMemberResolver _systemDrawingPointResolver;
        private readonly SystemDrawingPointMemberResolver _systemDrawingPointFResolver;
        private readonly SystemDrawingSizeMemberResolver _systemDrawingSizeResolver;
        private readonly SystemDrawingSizeMemberResolver _systemDrawingSizeFResolver;
        private readonly SystemDrawingRectangleMemberResolver _systemDrawingRectangleResolver;
        private readonly SystemDrawingRectangleMemberResolver _systemDrawingRectangleFResolver;
    }

    internal class SystemStringMemberResolver
    {
        public SystemStringMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.String.{memberName}");
                case IMethodSymbol {Name: "Contains"}:
                    return ResolveContainsMethod(data, representation);
                case IMethodSymbol {Name: "Replace"}:
                    return ResolveReplaceMethod(data, representation);
                case IMethodSymbol {Name: "StartsWith"}:
                    return ResolveStartsWithMethod(data, representation);
                case IMethodSymbol {Name: "Trim"}:
                    return ResolveTrimMethod(data, representation);
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.String.{memberName}");
        }

        private OperationResult<MemberResolveData> ResolveTrimMethod(MemberData data, MemberRepresentation representation)
        {
            switch (data.Arguments)
            {
                case []:
                    return new OperationResult<MemberResolveData>(true, "",
                        new MemberResolveData($"{representation.Target}.strip()"));
                case [var arg]:
                    switch (arg.Expression)
                    {
                        // TODO (std_string) : for some unknown reasons, roslyn resolve String.Trim(Char) method as String.Trim(params Char[]) - investigate this
                        case LiteralExpressionSyntax:
                        {
                            String member = $"{representation.Target}.strip({representation.Arguments.Values[0].Trim('[', ']')})";
                            MemberResolveData memberData = new MemberResolveData(member);
                            return new OperationResult<MemberResolveData>(true, "", memberData);
                        }
                        default:
                            return new OperationResult<MemberResolveData>(false, "Unsupported arguments for System.String.Trim");
                    }
            }
            return new OperationResult<MemberResolveData>(false, "Unsupported arguments for System.String.Trim");
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
                    return new OperationResult<MemberResolveData>(true, "", memberData);
                }
            }
            return new OperationResult<MemberResolveData>(false, "Unsupported arguments for System.String.StartsWith");
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
                    return new OperationResult<MemberResolveData>(true, "", memberData);
                }
            }
            return new OperationResult<MemberResolveData>(false, "Unsupported arguments for System.String.Contains");
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
                    return new OperationResult<MemberResolveData>(true, "", memberData);
                }
            }
            return new OperationResult<MemberResolveData>(false, "Unsupported arguments for System.String.Replace");
        }

        private readonly SemanticModel _model;
    }

    internal class SystemDrawingColorMemberResolver
    {
        public SystemDrawingColorMemberResolver(SemanticModel model, AppData appData)
        {
            _model = model;
            _appData = appData;
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.Drawing.Color.{memberName}");
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
                case IMethodSymbol {Name: "FromArgb" }:
                    return ResolveFromArgbMethod(representation);
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.Drawing.Color.{memberName}");
        }

        private OperationResult<MemberResolveData> ResolveColorDefinitionProperty(String sourceColorName)
        {
            // TODO (std_string) : probably some static properties may be not a colors. we need to check this
            String destColorName = _appData.NameTransformer.TransformPropertyName("System.Drawing.Color", sourceColorName);
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
            MemberResolveData colorData = new MemberResolveData($"{prepareResult.moduleName}.Color.{destColorName}", prepareResult.importData);
            return new OperationResult<MemberResolveData>(true, "", colorData);
        }

        private OperationResult<MemberResolveData> ResolveEmptyField()
        {
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
            MemberResolveData colorData = new MemberResolveData($"{prepareResult.moduleName}.Color.empty()", prepareResult.importData);
            return new OperationResult<MemberResolveData>(true, "", colorData);
        }

        private OperationResult<MemberResolveData> ResolveFromArgbMethod(MemberRepresentation representation)
        {
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
            String arguments = String.Join(", ", representation.Arguments.Values);
            MemberResolveData colorData = new MemberResolveData($"{prepareResult.moduleName}.Color.from_argb({arguments})", prepareResult.importData);
            return new OperationResult<MemberResolveData>(true, "", colorData);
        }

        private OperationResult<MemberResolveData> ResolveToArgbMethod(MemberRepresentation representation)
        {
            // the only signature is System.Drawing.Color.ToArgb()
            MemberResolveData memberData = new MemberResolveData($"{representation.Target}.to_argb()");
            return new OperationResult<MemberResolveData>(true, "", memberData);
        }

        private readonly AppData _appData;
        private readonly SemanticModel _model;
    }

    // resolver for System.Drawing.Point and System.Drawing.PointF
    internal class SystemDrawingPointMemberResolver
    {
        public SystemDrawingPointMemberResolver(SemanticModel model, AppData appData, String typeName)
        {
            _model = model;
            _appData = appData;
            _typeName = typeName;
            String[] knownNames = {"Point", "PointF"};
            if (!knownNames.Contains(typeName))
                throw new InvalidOperationException($"Unsupported name of type: {typeName}");
        }

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            // TODO (std_string) : add check of arg type
            switch (argumentsRepresentation.Values)
            {
                case [var x, var y]:
                {
                    (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
                    MemberResolveData ctorData = new MemberResolveData($"{prepareResult.moduleName}.{_typeName}({x}, {y})", prepareResult.importData);
                    return new OperationResult<MemberResolveData>(true, "", ctorData);
                }
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported ctor for System.Drawing.{_typeName}");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.Drawing.{_typeName}.{memberName}");
                case IPropertySymbol {Name: "IsEmpty"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "is_empty");
                case IPropertySymbol {Name: "X"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "x");
                case IPropertySymbol {Name: "Y"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "y");
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.Drawing.{_typeName}.{memberName}");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly String _typeName;
    }

    // resolver for System.Drawing.Rectangle and System.Drawing.RectangleF
    internal class SystemDrawingRectangleMemberResolver
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

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
            // TODO (std_string) : add check of arg type
            switch (argumentsRepresentation.Values)
            {
                case [var location, var size]:
                {
                    MemberResolveData ctorData = new MemberResolveData($"{prepareResult.moduleName}{_typeName}({location}, {size})", prepareResult.importData);
                    return new OperationResult<MemberResolveData>(true, "", ctorData);
                }
                case [var x, var y, var width, var height]:
                {
                    String member = $"{prepareResult.moduleName}.{_typeName}({x}, {y}, {width}, {height})";
                    MemberResolveData ctorData = new MemberResolveData(member, prepareResult.importData);
                    return new OperationResult<MemberResolveData>(true, "", ctorData);
                }
            }
            return new OperationResult<MemberResolveData>(false, $"Not supported now for System.Drawing.{_typeName}");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.Drawing.{_typeName}.{memberName}");
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
            return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.Drawing.{_typeName}.{memberName}");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly String _typeName;
    }

    // resolver for System.Drawing.Size and System.Drawing.SizeF
    internal class SystemDrawingSizeMemberResolver
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

        public OperationResult<MemberResolveData> ResolveCtor(IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            // TODO (std_string) : add check of arg type
            switch (argumentsRepresentation.Values)
            {
                case [var width, var height]:
                {
                    (String moduleName, ImportData importData) prepareResult = _appData.ImportAliasManager.PrepareImport("aspose.pydrawing");
                    MemberResolveData ctorData = new MemberResolveData($"{prepareResult.moduleName}.{_typeName}({width}, {height})", prepareResult.importData);
                    return new OperationResult<MemberResolveData>(true, "", ctorData);
                }
            }
            return new OperationResult<MemberResolveData>(false, $"Not supported now for System.Drawing.{_typeName}");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax memberName = data.Name;
            SymbolInfo memberInfo = _model.GetSymbolInfo(memberName);
            switch (memberInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.Drawing.{_typeName}.{memberName}");
                case IPropertySymbol {Name: "Height"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "height");
                case IPropertySymbol {Name: "IsEmpty"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "is_empty");
                case IPropertySymbol {Name: "Width"}:
                    return ExternalEntityResolverHelper.ResolveInstanceProperty(representation, "width");
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported member: System.Drawing.{_typeName}.{memberName}");
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly String _typeName;
    }
}
