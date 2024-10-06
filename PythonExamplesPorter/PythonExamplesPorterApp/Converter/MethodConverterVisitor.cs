using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Comments;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;
using PythonExamplesPorterApp.Utils;

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
            Func<Boolean> beforeGenerateChecker = hasTestCaseAttribute ?
                                                  () => CheckTestCaseMethodDeclaration(node, currentMethod!, methodStorage) :
                                                  () => true;
            Action beforeGenerateAction = hasTestCaseAttribute ?
                                          () => GenerateTestCaseHandler(node, currentMethod!, methodStorage) :
                                          () => {};
            Action afterGenerateAction = hasTestCaseAttribute ?
                                         () => { methodStorage.DecreaseLocalIndentation(StorageDef.IndentationDelta); } :
                                         () => {};
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
            return true;
        }

        private Boolean CheckTestCaseMethodDeclaration(MethodDeclarationSyntax node, IMethodSymbol currentMethod, MethodStorage methodStorage)
        {
            String methodName = node.Identifier.Text;
            IList<IParameterSymbol> parameters = currentMethod.Parameters;
            if (parameters.IsEmpty())
            {
                _appData.Logger.LogError($"Bad {methodName} method: absence of parameters");
                methodStorage.SetError("absence of method's parameters");
                return false;
            }
            Boolean hasParamsArg = parameters.Last().IsParams;
            Boolean hasDefaultValue = parameters.Any(parameter => parameter.HasExplicitDefaultValue);
            Boolean hasRefOutModifier = parameters.Any(parameter => parameter.RefKind != RefKind.None);
            if (hasParamsArg || hasDefaultValue || hasRefOutModifier)
            {
                _appData.Logger.LogError($"Bad {methodName} method: unsupported kind of parameters");
                methodStorage.SetError("unsupported kind of parameters");
                return false;
            }
            return true;
        }

        private void GenerateTestCaseHandler(MethodDeclarationSyntax node, IMethodSymbol currentMethod, MethodStorage methodStorage)
        {
            String[] parameters = currentMethod.Parameters
                .Select(parameter => _appData.NameTransformer.TransformLocalVariableName(parameter.Name))
                .ToArray();
            String parametersDest = String.Join(", ", parameters);
            ExpressionConverter expressionConverter = new ExpressionConverter(_model, _appData, new ExpressionConverterSettings());
            AttributeSyntax[] testCaseAttributes = node.AttributeLists.GetAttributes(_model, "NUnit.Framework.TestCaseAttribute");
            IList<String> valuesList = new List<String>();
            foreach (AttributeSyntax attribute in testCaseAttributes)
            {
                if (attribute.ArgumentList == null)
                    throw new UnsupportedSyntaxException("Bad NUnit.Framework.TestCaseAttribute");
                IReadOnlyList<AttributeArgumentSyntax> arguments = attribute.ArgumentList.Arguments;
                String[] values = new String[arguments.Count];
                for (Int32 argumentIndex = 0; argumentIndex < arguments.Count; ++argumentIndex)
                {
                    ConvertResult expressionResult = expressionConverter.Convert(arguments[argumentIndex].Expression);
                    if (!expressionResult.AfterResults.IsEmpty())
                        throw new UnsupportedSyntaxException("Unexpected attribute's value conversion result");
                    methodStorage.ImportStorage.Append(expressionResult.ImportData);
                    values[argumentIndex] = expressionResult.Result;
                }
                valuesList.Add(values.Length == 1 ? values.First() : $"({String.Join(", ", values)})");
            }
            String valuesDest = $"[{String.Join(", ", valuesList)}]";
            methodStorage.AddBodyLine($"for {parametersDest} in {valuesDest}:");
            methodStorage.IncreaseLocalIndentation(StorageDef.IndentationDelta);
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
            if (node.Body == null)
            {
                _appData.Logger.LogError($"Bad {methodName} method: absence of body");
                methodStorage.SetError("absence of method's body");
                return;
            }

            if (!beforeGenerateChecker())
                return;
            try
            {
                beforeGenerateAction();
                StatementConverterVisitor statementConverter = new StatementConverterVisitor(_model, methodStorage, _appData);
                statementConverter.VisitBlock(node.Body);
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