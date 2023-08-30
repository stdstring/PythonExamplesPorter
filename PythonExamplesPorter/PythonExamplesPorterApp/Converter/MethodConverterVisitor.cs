using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Converter;

internal class MethodConverterVisitor : CSharpSyntaxWalker
{
    public MethodConverterVisitor(SemanticModel model,
        ClassStorage currentClass,
        IgnoredEntitiesManager ignoredManager,
        ILogger logger)
    {
        _model = model;
        _currentClass = currentClass;
        _ignoredManager = ignoredManager;
        _logger = logger;
    }

    public override void VisitMethodDeclaration(MethodDeclarationSyntax node)
    {
        String logHead = $"        We try to process {node.Identifier.Text} method ...";
        IMethodSymbol? currentMethod = _model.GetDeclaredSymbol(node);
        // we don't process method without semantic info
        if (currentMethod == null)
        {
            _logger.LogInfo($"{logHead} skipped due to absence semantic info");
            return;
        }
        // we don't process method without parent
        if (node.Parent == null)
        {
            _logger.LogInfo($"{logHead} skipped due to absence of method's parent");
            return;
        }
        ISymbol? parent = _model.GetDeclaredSymbol(node.Parent);
        if (parent == null)
        {
            _logger.LogInfo($"{logHead} skipped due to absence parent's semantic info");
            return;
        }
        Boolean isPublic = node.Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.PublicKeyword));
        Boolean isStatic = node.Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.StaticKeyword));
        // we don't process nonpublic methods
        if (!isPublic)
        {
            _logger.LogInfo($"{logHead} skipped for nonpublic method");
            return;
        }
        // we don't process static methods
        if (isStatic)
        {
            _logger.LogInfo($"{logHead} skipped for static method");
            return;
        }
        SyntaxList<AttributeListSyntax> attributes = node.AttributeLists;
        // we don't process methods not marked by NUnit.Framework.TestAttribute attribute
        if (!attributes.ContainAttribute(_model, "NUnit.Framework.TestAttribute"))
        {
            _logger.LogInfo($"{logHead} skipped for method non marked by NUnit.Framework.TestAttribute attribute");
            return;
        }
        String methodName = currentMethod.Name;
        String parentFullName = parent.ToDisplayString();
        // we don't process ignored method
        if (_ignoredManager.IsIgnoredMethod($"{parentFullName}.{methodName}"))
        {
            _logger.LogInfo($"{logHead} skipped because ignored method");
            return;
        }
        _logger.LogInfo($"{logHead} processed");
        GenerateMethodDeclaration(node);
        base.VisitMethodDeclaration(node);
    }

    private void GenerateMethodDeclaration(MethodDeclarationSyntax node)
    {
        if (_currentClass == null)
            throw new InvalidOperationException($"Unknown class for method {node.Identifier.Text}");
        String destMethodName = NameTransformer.TransformMethodName(node.Identifier.Text);
        if (!destMethodName.StartsWith("test_"))
            destMethodName = "test_" + destMethodName;
        MethodStorage currentMethod = _currentClass.CreateMethodStorage(destMethodName);
        currentMethod.SetError("we don't support this functionality yet");
    }

    private readonly SemanticModel _model;
    private readonly ClassStorage _currentClass;
    private readonly IgnoredEntitiesManager _ignoredManager;
    private readonly ILogger _logger;
}