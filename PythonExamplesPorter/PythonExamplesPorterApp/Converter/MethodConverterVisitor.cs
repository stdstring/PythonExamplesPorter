using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Comments;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;

namespace PythonExamplesPorterApp.Converter
{
    internal class MethodConverterVisitor : CSharpSyntaxWalker
    {
        public MethodConverterVisitor(SemanticModel model, ClassStorage currentClass, AppData appData)
        {
            _model = model;
            _currentClass = currentClass;
            _appData = appData;
        }

        public override void VisitMethodDeclaration(MethodDeclarationSyntax node)
        {
            String logHead = $"        We try to process {node.Identifier.Text} method ...";
            IMethodSymbol? currentMethod = _model.GetDeclaredSymbol(node);
            if (!CheckVisitMethodDeclaration(node, currentMethod, logHead))
                return;
            ISymbol parent = _model.GetDeclaredSymbol(node.Parent!)!;
            String parentFullName = parent.ToDisplayString();
            String testMethodName = CreateTestMethodName(node, parentFullName);
            MethodStorage methodStorage = _currentClass.CreateMethodStorage(testMethodName);
            CommentsProcessor commentsProcessor = new CommentsProcessor(_appData.NameTransformer);
            methodStorage.AppendHeaderData(commentsProcessor.Process(CommentsExtractor.ExtractHeaderComments(node)));
            methodStorage.AppendFooterData(commentsProcessor.Process(CommentsExtractor.ExtractFooterComments(node)));
            methodStorage.SetTrailingData(commentsProcessor.Process(CommentsExtractor.ExtractTrailingComment(node)));
            Boolean hasTestCaseAttribute = node.AttributeLists.ContainAttribute(_model, "NUnit.Framework.TestCaseAttribute");
            Func<Boolean> beforeGenerateChecker = () => true;
            Action beforeGenerateAction = () => {};
            Action afterGenerateAction = () => {};
            if (hasTestCaseAttribute)
            {
                TestCaseProcessor testCaseProcessor = new TestCaseProcessor(_model, _appData, node, currentMethod!, methodStorage);
                beforeGenerateChecker = testCaseProcessor.CheckMethodDeclaration;
                beforeGenerateAction = testCaseProcessor.ProcessBefore;
                afterGenerateAction = testCaseProcessor.ProcessAfter;
            }
            _appData.Logger.LogInfo($"{logHead} processed");
            GenerateTestMethodDeclaration(node, parentFullName, methodStorage, beforeGenerateChecker, beforeGenerateAction, afterGenerateAction);
        }

        private Boolean CheckVisitMethodDeclaration(MethodDeclarationSyntax node, IMethodSymbol? currentMethod, String logHead)
        {
            if (currentMethod == null)
            {
                _appData.Logger.LogInfo($"{logHead} skipped due to absence semantic info");
                return false;
            }
            // we don't process method without parent
            if (node.Parent == null)
            {
                _appData.Logger.LogInfo($"{logHead} skipped due to absence of method's parent");
                return false;
            }
            ISymbol? parent = _model.GetDeclaredSymbol(node.Parent);
            if (parent == null)
            {
                _appData.Logger.LogInfo($"{logHead} skipped due to absence parent's semantic info");
                return false;
            }
            Boolean isPublic = node.Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.PublicKeyword));
            Boolean isStatic = node.Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.StaticKeyword));
            // we don't process nonpublic methods
            if (!isPublic)
            {
                _appData.Logger.LogInfo($"{logHead} skipped for nonpublic method");
                return false;
            }
            // we don't process static methods
            if (isStatic)
            {
                _appData.Logger.LogInfo($"{logHead} skipped for static method");
                return false;
            }
            String methodName = currentMethod.Name;
            String parentFullName = parent.ToDisplayString();
            // we don't process ignored method
            if (_appData.IgnoredManager.IsIgnoredMethod($"{parentFullName}.{methodName}"))
            {
                _appData.Logger.LogInfo($"{logHead} skipped because ignored method");
                return false;
            }
            if (!node.AttributeLists.ContainAttribute(_model, "NUnit.Framework.TestAttribute") &&
                !node.AttributeLists.ContainAttribute(_model, "NUnit.Framework.TestCaseAttribute"))
            {
                _appData.Logger.LogInfo($"{logHead} skipped for method non marked by NUnit.Framework.TestAttribute/NUnit.Framework.TestCaseAttribute attributes");
                return false;
            }
            if (node.Body == null)
            {
                _appData.Logger.LogError($"Bad {methodName} method: absence of body");
                return false;
            }
            return true;
        }

        private void GenerateTestMethodDeclaration(MethodDeclarationSyntax node,
                                                   String parentFullName,
                                                   MethodStorage methodStorage,
                                                   Func<Boolean> beforeGenerateChecker,
                                                   Action beforeGenerateAction,
                                                   Action afterGenerateAction)
        {
            String methodName = node.Identifier.Text;
            if (_appData.IgnoredManager.IsIgnoredMethodBody($"{parentFullName}.{methodName}"))
            {
                _appData.Logger.LogInfo($"Ignored {methodName} method body");
                methodStorage.SetError("ignored method body");
                return;
            }
            if (!beforeGenerateChecker())
                return;
            try
            {
                beforeGenerateAction();
                StatementConverterVisitor statementConverter = new StatementConverterVisitor(_model, methodStorage, _appData);
                statementConverter.VisitBlock(node.Body!);
                afterGenerateAction();
            }
            catch (UnsupportedSyntaxException exc)
            {
                _appData.Logger.LogError(exc.Message);
                methodStorage.SetError(exc.Message);
            }
        }

        private String CreateTestMethodName(MethodDeclarationSyntax node, String typeName)
        {
            String methodName = node.Identifier.Text;
            String destMethodName = _appData.NameTransformer.TransformMethodName(typeName, methodName);
            if (!destMethodName.StartsWith("test_"))
                destMethodName = "test_" + destMethodName;
            return destMethodName;
        }

        private readonly SemanticModel _model;
        private readonly ClassStorage _currentClass;
        private readonly AppData _appData;
    }
}