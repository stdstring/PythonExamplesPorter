using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Config;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Converter
{
    internal class FileConverter
    {
        public FileConverter(ConfigData configData, ILogger logger)
        {
            _configData = configData;
            _logger = logger;
        }

        public void Convert(String relativeFilePath, SyntaxTree tree, SemanticModel model)
        {
            String destRelativePath = PathTransformer.TransformPath(relativeFilePath);
            String destPath = Path.Combine(_configData.DestDirectory, destRelativePath);
            FileStorage currentFile = new FileStorage(destPath);
            FileConverterSyntaxWalker converter = new FileConverterSyntaxWalker(model, currentFile, _logger);
            converter.Visit(tree.GetRoot());
            if (currentFile.IsEmpty())
                return;
            String? destDirectory = Path.GetDirectoryName(destPath);
            if (destDirectory != null)
                Directory.CreateDirectory(destDirectory);
            currentFile.Save();
        }

        private readonly ConfigData _configData;
        private readonly ILogger _logger;
    }

    internal class FileConverterSyntaxWalker : CSharpSyntaxWalker
    {
        public FileConverterSyntaxWalker(SemanticModel model, FileStorage currentFile, ILogger logger)
        {
            _logger = logger;
            _model = model;
            _currentFile = currentFile;
        }

        public override void VisitClassDeclaration(ClassDeclarationSyntax node)
        {
            String logHead = $"    We try to process {node.Identifier.Text} class ...";
            SyntaxNode? parentDecl = node.Parent;
            // we don't process class which aren't nested into namespaces
            if (parentDecl == null)
            {
                _logger.LogInfo($"{logHead} skipped for absence parent namespace");
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
            _logger.LogInfo($"{logHead} processed");
            String destClassName = NameTransformer.TransformClassName(node.Identifier.Text);
            _currentClass = _currentFile.CreateClassStorage(destClassName);
            _currentFile.AddImport("unittest");
            _currentClass.AddBaseClass("unittest.TestCase");
            base.VisitClassDeclaration(node);
        }

        public override void VisitMethodDeclaration(MethodDeclarationSyntax node)
        {
            String logHead = $"        We try to process {node.Identifier.Text} method ...";
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
            _logger.LogInfo($"{logHead} processed");
            if (_currentClass == null)
                throw new InvalidOperationException($"Unknown class for method {node.Identifier.Text}");
            String destMethodName = NameTransformer.TransformMethodName(node.Identifier.Text);
            if (!destMethodName.StartsWith("test_"))
                destMethodName = "test_" + destMethodName;
            _currentMethod = _currentClass.CreateMethodStorage(destMethodName);
            _currentMethod.SetError("we don't support this functionality yet");
            base.VisitMethodDeclaration(node);
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

        private readonly ILogger _logger;
        private readonly SemanticModel _model;
        private readonly FileStorage _currentFile;
        private ClassStorage? _currentClass;
        private MethodStorage? _currentMethod;
    }
}
