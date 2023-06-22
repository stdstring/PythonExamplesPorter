using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Logger;

namespace PythonExamplesPorterApp.Converter
{
    internal class FileConverter
    {
        public FileConverter(ILogger logger)
        {
            _logger = logger;
        }

        public void Convert(String relativeFilePath, SyntaxTree tree, SemanticModel model)
        {
            FileConverterSyntaxWalker converter = new FileConverterSyntaxWalker(model, _logger);
            converter.Visit(tree.GetRoot());
        }

        private readonly ILogger _logger;
    }

    internal class FileConverterSyntaxWalker : CSharpSyntaxWalker
    {
        public FileConverterSyntaxWalker(SemanticModel model, ILogger logger)
        {
            _logger = logger;
            _model = model;
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
    }
}
