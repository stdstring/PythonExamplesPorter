using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Handmade;
using PythonExamplesPorterApp.Ignored;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Converter
{
    internal class FileConverter
    {
        public FileConverter(AppConfig appConfig,
                             IgnoredEntitiesManager ignoredManager,
                             HandmadeEntitiesManager handmadeManager,
                             ILogger logger)
        {
            _appConfig = appConfig;
            _ignoredManager = ignoredManager;
            _handmadeManager = handmadeManager;
            _logger = logger;
        }

        public void Convert(String relativeFilePath, SyntaxTree tree, SemanticModel model)
        {
            String destRelativePath = PathTransformer.TransformPath(relativeFilePath);
            String destDirectory = Path.Combine(_appConfig.BaseDirectory, _appConfig.ConfigData.BaseConfig!.DestDirectory);
            String destPath = Path.Combine(destDirectory, destRelativePath);
            FileStorage currentFile = new FileStorage(destPath);
            FileConverterSyntaxWalker converter = new FileConverterSyntaxWalker(model, currentFile, _ignoredManager, _handmadeManager, _logger);
            converter.Visit(tree.GetRoot());
            if (currentFile.IsEmpty())
                return;
            Directory.CreateDirectory(destDirectory);
            currentFile.Save();
        }

        private readonly AppConfig _appConfig;
        private readonly IgnoredEntitiesManager _ignoredManager;
        private readonly HandmadeEntitiesManager _handmadeManager;
        private readonly ILogger _logger;
    }

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
            if (!ContainAttribute(attributes, "NUnit.Framework.TestFixtureAttribute"))
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
            if (!ContainAttribute(attributes, "NUnit.Framework.TestAttribute"))
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
            _currentMethod = _currentClass.CreateMethodStorage(destMethodName);
            _currentMethod.SetError("we don't support this functionality yet");
        }

        private Boolean ContainAttribute(SyntaxList<AttributeListSyntax> attributes, String expectedFullName)
        {
            foreach (AttributeListSyntax attributeList in attributes)
            {
                foreach (AttributeSyntax attribute in attributeList.Attributes)
                {
                    ISymbol? symbol = _model.GetSymbolInfo(attribute.Name).Symbol;
                    if (symbol == null)
                        return false;
                    if (symbol.Kind != SymbolKind.Method)
                        return false;
                    INamedTypeSymbol? symbolType = symbol.ContainingType;
                    if (symbolType == null)
                        return false;
                    if (symbolType.Kind != SymbolKind.NamedType)
                        return false;
                    // TODO (std_string) : think about using SymbolDisplayFormat
                    String attributeFullName = symbolType.ToDisplayString();
                    if (String.Equals(expectedFullName, attributeFullName))
                        return true;
                }
            }
            return false;
        }

        private readonly SemanticModel _model;
        private readonly FileStorage _currentFile;
        private readonly IgnoredEntitiesManager _ignoredManager;
        private readonly HandmadeEntitiesManager _handmadeManager;
        private readonly ILogger _logger;
        private ClassStorage? _currentClass;
        private MethodStorage? _currentMethod;
    }
}
