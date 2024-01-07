using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;

namespace PythonExamplesPorterApp.Expressions
{
    internal class MemberAccessExpressionConverter
    {
        public MemberAccessExpressionConverter(SemanticModel model, AppData appData, ExpressionConverterSettings settings)
        {
            _model = model;
            _appData = appData;
            _settings = settings;
            _expressionConverter = new ExpressionConverter(model, appData, settings);
            _externalEntityResolver = new ExternalEntityResolver(model, appData);
        }

        public ConvertResult Convert(MemberAccessExpressionSyntax expression)
        {
            return Convert(expression, null);
        }

        public ConvertResult Convert(MemberAccessExpressionSyntax expression, ArgumentListSyntax? argumentList)
        {
            ImportData importData = new ImportData();
            ArgumentListConverter argumentListConverter = new ArgumentListConverter(_model, _appData, _settings.CreateChild());
            ConvertArgumentsResult arguments = argumentListConverter.Convert(expression, argumentList.GetArguments());
            importData.Append(arguments.ImportData);
            ExpressionSyntax target = expression.Expression;
            SymbolInfo targetInfo = _model.GetSymbolInfo(target);
            switch (targetInfo.Symbol)
            {
                // TODO (std_string) : for some types of expression we receive null, but this is not error of recognition. Think about this
                case INamespaceSymbol:
                    return _expressionConverter.Convert(expression.Name);
                default:
                    //String targetDest = ConvertExpression(expressionConverter, target);
                    ConvertResult targetDest = _expressionConverter.Convert(target);
                    importData.Append(targetDest.ImportData);
                    SimpleNameSyntax name = expression.Name;
                    MemberData memberData = new MemberData(target, name, argumentList.GetArguments());
                    MemberRepresentation memberRepresentation = new MemberRepresentation(targetDest.Result, arguments.Result);
                    OperationResult<MemberResolveData> resolveResult = _externalEntityResolver.ResolveMember(memberData, memberRepresentation);
                    if (!resolveResult.Success)
                        throw new UnsupportedSyntaxException(resolveResult.Reason);
                    MemberResolveData memberResolveData = resolveResult.Data!;
                    //Buffer.Append(memberResolveData.Member);
                    importData.AddImport(memberResolveData.ModuleName);
                    return new ConvertResult(memberResolveData.Member, importData);
            }
        }

        private readonly SemanticModel _model;
        private readonly AppData _appData;
        private readonly ExpressionConverterSettings _settings;
        private readonly ExpressionConverter _expressionConverter;
        private readonly ExternalEntityResolver _externalEntityResolver;
    }
}
