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
            SyntaxNode? parentDecl = node.Parent;
            // we don't process class which aren't nested into namespaces
            if (parentDecl == null)
                return;
            // we don't process nested class
            if (!parentDecl.IsKind(SyntaxKind.NamespaceDeclaration))
                return;
            SyntaxList<AttributeListSyntax> attributes = node.AttributeLists;
            // we don't process classes not marked by NUnit.Framework.TestFixtureAttribute attribute
            if (!ContainAttribute(attributes, "NUnit.Framework.TestFixtureAttribute"))
                return;
            _logger.LogInfo($"    We can process {node.Identifier.Text} class");
            base.VisitClassDeclaration(node);
        }

        public override void VisitMethodDeclaration(MethodDeclarationSyntax node)
        {
            Boolean isPublic = node.Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.PublicKeyword));
            Boolean isStatic = node.Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.StaticKeyword));
            // we don't process nonpublic methods
            if (!isPublic)
                return;
            // we don't process static methods
            if (isStatic)
                return;
            SyntaxList<AttributeListSyntax> attributes = node.AttributeLists;
            // we don't process methods not marked by NUnit.Framework.TestAttribute attribute
            if (!ContainAttribute(attributes, "NUnit.Framework.TestAttribute"))
                return;
            _logger.LogInfo($"        We can process {node.Identifier.Text} method");
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
