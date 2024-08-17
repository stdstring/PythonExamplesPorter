using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Comments;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Converter
{
    internal class FileConverterVisitor : CSharpSyntaxWalker
    {
        public FileConverterVisitor(SemanticModel model, FileStorage currentFile, AppData appData)
        {
            _model = model;
            _currentFile = currentFile;
            _appData = appData;
        }

        public override void VisitClassDeclaration(ClassDeclarationSyntax node)
        {
            String logHead = $"    We try to process {node.Identifier.Text} class ...";
            INamedTypeSymbol? currentType = _model.GetDeclaredSymbol(node);
            if (!CheckVisitClassDeclaration(node, currentType, logHead))
                return;
            _appData.Logger.LogInfo($"{logHead} processed");
            String destClassName = _appData.NameTransformer.TransformTypeName(node.Identifier.Text);
            _currentClass = _currentFile.CreateClassStorage(destClassName);
            CommentsProcessor commentsProcessor = new CommentsProcessor(_appData.NameTransformer);
            _currentClass.AppendHeaderData(commentsProcessor.Process(CommentsExtractor.ExtractHeaderComments(node)));
            _currentClass.AppendFooterData(commentsProcessor.Process(CommentsExtractor.ExtractFooterComments(node)));
            _currentClass.SetTrailingData(commentsProcessor.Process(CommentsExtractor.ExtractTrailingComment(node)));
            GenerateClassDeclaration(currentType!);
            base.VisitClassDeclaration(node);
        }

        private Boolean CheckVisitClassDeclaration(ClassDeclarationSyntax node, INamedTypeSymbol? currentType, String logHead)
        {
            // we don't process class without semantic info
            if (currentType == null)
            {
                _appData.Logger.LogInfo($"{logHead} skipped due to absence semantic info");
                return false;
            }
            SyntaxNode? parentDecl = node.Parent;
            // we don't process class which aren't nested into namespaces
            if (parentDecl == null)
            {
                _appData.Logger.LogInfo($"{logHead} skipped due to absence parent namespace");
                return false;
            }
            // we don't process nested class
            if (!parentDecl.IsKind(SyntaxKind.NamespaceDeclaration))
            {
                _appData.Logger.LogInfo($"{logHead} skipped for nested class");
                return false;
            }
            // TODO (std_string) : think about using SymbolDisplayFormat
            String currentTypeFullName = currentType.ToDisplayString();
            // we don't process ignored class
            if (_appData.IgnoredManager.IsIgnoredType(currentTypeFullName))
            {
                _appData.Logger.LogInfo($"{logHead} skipped because ignored class");
                return false;
            }
            // we don't process handmade class
            if (_appData.HandmadeManager.IsHandmadeType(currentTypeFullName))
            {
                _appData.Logger.LogInfo($"{logHead} skipped because handmade class");
                return false;
            }
            IReadOnlyList<AttributeListSyntax> attributes = node.AttributeLists;
            // we don't process classes not marked by NUnit.Framework.TestFixtureAttribute attribute
            if (!attributes.ContainAttribute(_model, "NUnit.Framework.TestFixtureAttribute"))
            {
                _appData.Logger.LogInfo($"{logHead} skipped for class non marked by NUnit.Framework.TestFixtureAttribute attribute");
                return false;
            }

            return true;
        }

        private void GenerateClassDeclaration(INamedTypeSymbol currentType)
        {
            String? baseClassFullName = GetBaseClassFullName(currentType);
            if (baseClassFullName == null)
            {
                _currentFile.ImportStorage.AddImport("unittest");
                _currentClass!.AddBaseClass("unittest.TestCase");
            }
            else
            {
                Int32 lastDotIndex = baseClassFullName.LastIndexOf('.');
                String sourceBaseClassName = lastDotIndex == -1 ? baseClassFullName : baseClassFullName.Substring(lastDotIndex + 1);
                String baseClassName = _appData.NameTransformer.TransformTypeName(sourceBaseClassName);
                _currentClass!.AddBaseClass(baseClassName);
                _appData.HandmadeManager.UseHandmadeType(baseClassFullName);
                String moduleName = _appData.HandmadeManager.CalcHandmadeTypeModuleName(baseClassFullName);
                _currentFile.ImportStorage.AddEntity(moduleName, baseClassName);
            }
        }

        // TODO (std_string) : think about processing of unsupported base classes
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
            MethodConverterVisitor methodConverter = new MethodConverterVisitor(_model, _currentClass.Must("Unknown class"), _appData);
            methodConverter.Visit(node);
        }

        private readonly SemanticModel _model;
        private readonly FileStorage _currentFile;
        private readonly AppData _appData;
        private ClassStorage? _currentClass;
    }
}