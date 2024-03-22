using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
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
            // we don't process method without semantic info
            if (currentMethod == null)
            {
                _appData.Logger.LogInfo($"{logHead} skipped due to absence semantic info");
                return;
            }
            // we don't process method without parent
            if (node.Parent == null)
            {
                _appData.Logger.LogInfo($"{logHead} skipped due to absence of method's parent");
                return;
            }
            ISymbol? parent = _model.GetDeclaredSymbol(node.Parent);
            if (parent == null)
            {
                _appData.Logger.LogInfo($"{logHead} skipped due to absence parent's semantic info");
                return;
            }
            Boolean isPublic = node.Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.PublicKeyword));
            Boolean isStatic = node.Modifiers.Any(modifier => modifier.IsKind(SyntaxKind.StaticKeyword));
            // we don't process nonpublic methods
            if (!isPublic)
            {
                _appData.Logger.LogInfo($"{logHead} skipped for nonpublic method");
                return;
            }
            // we don't process static methods
            if (isStatic)
            {
                _appData.Logger.LogInfo($"{logHead} skipped for static method");
                return;
            }
            String methodName = currentMethod.Name;
            String parentFullName = parent.ToDisplayString();
            // we don't process ignored method
            if (_appData.IgnoredManager.IsIgnoredMethod($"{parentFullName}.{methodName}"))
            {
                _appData.Logger.LogInfo($"{logHead} skipped because ignored method");
                return;
            }
            switch (node.AttributeLists)
            {
                case var attributes when attributes.ContainAttribute(_model, "NUnit.Framework.TestAttribute"):
                    _appData.Logger.LogInfo($"{logHead} processed");
                    GenerateTestMethodDeclaration(node, CreateTestMethodName(node, parentFullName));
                    break;
                case var attributes when attributes.ContainAttribute(_model, "NUnit.Framework.TestCaseAttribute"):
                    _appData.Logger.LogInfo($"{logHead} processed");
                    GenerateTestCaseMethodDeclaration(node, CreateTestMethodName(node, parentFullName));
                    break;
                default:
                    _appData.Logger.LogInfo($"{logHead} skipped for method non marked by NUnit.Framework.TestAttribute/NUnit.Framework.TestCaseAttribute attributes");
                    return;
            }
        }

        private void GenerateTestMethodDeclaration(MethodDeclarationSyntax node, String testMethodName)
        {
            String methodName = node.Identifier.Text;
            MethodStorage currentMethod = _currentClass.CreateMethodStorage(testMethodName);
            if (node.Body == null)
            {
                _appData.Logger.LogError($"Bad {methodName} method: absence of body");
                currentMethod.SetError("absence of method's body");
                return;
            }
            try
            {
                StatementConverterVisitor statementConverter = new StatementConverterVisitor(_model, currentMethod, _appData);
                statementConverter.VisitBlock(node.Body);
            }
            catch (UnsupportedSyntaxException exc)
            {
                _appData.Logger.LogError(exc.Message);
                currentMethod.SetError(exc.Message);
            }
        }

        private void GenerateTestCaseMethodDeclaration(MethodDeclarationSyntax node, String testMethodName)
        {
            String methodName = node.Identifier.Text;
            MethodStorage currentMethod = _currentClass.CreateMethodStorage(testMethodName);
            switch (node.Body)
            {
                case null:
                    _appData.Logger.LogError($"Bad {methodName} method: absence of body");
                    currentMethod.SetError("absence of method's body");
                    break;
                default:
                    _appData.Logger.LogError($"Unsupported {methodName} method: NUnit.Framework.TestCaseAttribute attributes is not supported now");
                    currentMethod.SetError("Unsupported NUnit.Framework.TestCaseAttribute attributes");
                    break;
            }
        }

        private String CreateTestMethodName(MethodDeclarationSyntax node, String typeName)
        {
            String methodName = node.Identifier.Text;
            if (_currentClass == null)
                throw new InvalidOperationException($"Unknown class for method {methodName}");
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