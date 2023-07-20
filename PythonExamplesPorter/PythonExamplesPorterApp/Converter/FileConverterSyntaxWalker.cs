using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Converter;

internal class FileConverterSyntaxWalker : CSharpSyntaxWalker
{
    public FileConverterSyntaxWalker(SemanticModel model,
        FileStorage currentFile,
        IgnoredEntitiesManager ignoredManager,
        HandmadeEntitiesManager handmadeManager,
        ILogger logger)
    {
        _model = model;
        _currentFile = currentFile;
        _ignoredManager = ignoredManager;
        _handmadeManager = handmadeManager;
        _logger = logger;
    }

    public override void VisitClassDeclaration(ClassDeclarationSyntax node)
    {
        String logHead = $"    We try to process {node.Identifier.Text} class ...";
        INamedTypeSymbol? currentType = _model.GetDeclaredSymbol(node);
        // we don't process class without semantic info
        if (currentType == null)
        {
            _logger.LogInfo($"{logHead} skipped due to absence semantic info");
            return;
        }
        SyntaxNode? parentDecl = node.Parent;
        // we don't process class which aren't nested into namespaces
        if (parentDecl == null)
        {
            _logger.LogInfo($"{logHead} skipped due to absence parent namespace");
            return;
        }
        // we don't process nested class
        if (!parentDecl.IsKind(SyntaxKind.NamespaceDeclaration))
        {
            _logger.LogInfo($"{logHead} skipped for nested class");
            return;
        }
        SyntaxList<AttributeListSyntax> attributes = node.AttributeLists;
        // we don't process classes not marked by NUnit.Framework.TestFixtureAttribute attribute
        if (!attributes.ContainAttribute(_model, "NUnit.Framework.TestFixtureAttribute"))
        {
            _logger.LogInfo($"{logHead} skipped for class non marked by NUnit.Framework.TestFixtureAttribute attribute");
            return;
        }
        // TODO (std_string) : think about using SymbolDisplayFormat
        String currentTypeFullName = currentType.ToDisplayString();
        // we don't process ignored class
        if (_ignoredManager.IsIgnoredType(currentTypeFullName))
        {
            _logger.LogInfo($"{logHead} skipped because ignored class");
            return;
        }
        _logger.LogInfo($"{logHead} processed");
        GenerateClassDeclaration(node, currentType);
        base.VisitClassDeclaration(node);
    }

    private void GenerateClassDeclaration(ClassDeclarationSyntax node, INamedTypeSymbol currentType)
    {
        String? baseClassFullName = GetBaseClassFullName(currentType);
        String destClassName = NameTransformer.TransformClassName(node.Identifier.Text);
        _currentClass = _currentFile.CreateClassStorage(destClassName);
        if (baseClassFullName == null)
        {
            _currentFile.AddImport("unittest");
            _currentClass.AddBaseClass("unittest.TestCase");
        }
        else
        {
            Int32 lastDotIndex = baseClassFullName.LastIndexOf('.');
            String baseClassName = lastDotIndex == -1 ? baseClassFullName : baseClassFullName.Substring(lastDotIndex + 1);
            _currentClass.AddBaseClass(baseClassName);
            _handmadeManager.UseHandmadeType(baseClassFullName);
        }
    }

    private String? GetBaseClassFullName(INamedTypeSymbol currentType)
    {
        INamedTypeSymbol? baseType = currentType.BaseType;
        INamespaceSymbol? baseTypeNamespace = baseType?.ContainingNamespace;
        String? baseTypeNamespaceName = baseTypeNamespace?.Name;
        if (baseType == null)
            return null;
        if (baseTypeNamespaceName == null || baseTypeNamespaceName.StartsWith("System."))
            return null;
        // TODO (std_string) : think about using SymbolDisplayFormat
        return baseType.ToDisplayString();
    }

    public override void VisitMethodDeclaration(MethodDeclarationSyntax node)
    {
        if (_currentClass == null)
            throw new InvalidOperationException($"Unknown class for method {node.Identifier.Text}");
        MethodConverterSyntaxWalker methodConverter = new MethodConverterSyntaxWalker(_model, _currentClass, _ignoredManager, _logger);
        methodConverter.Visit(node);
        //base.VisitMethodDeclaration(node);
    }

    private readonly SemanticModel _model;
    private readonly FileStorage _currentFile;
    private readonly IgnoredEntitiesManager _ignoredManager;
    private readonly HandmadeEntitiesManager _handmadeManager;
    private readonly ILogger _logger;
    private ClassStorage? _currentClass;
}