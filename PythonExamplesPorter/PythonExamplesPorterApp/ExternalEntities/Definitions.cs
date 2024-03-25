using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal record TypeResolveData(String TypeName, String ModuleName, ImportData ImportData);

    internal record MemberData(ExpressionSyntax Target, SimpleNameSyntax Name, IReadOnlyList<ArgumentSyntax> Arguments);

    internal record MemberRepresentation(String Target, ConvertedArguments Arguments);

    internal record MemberResolveData(String Member, ImportData ImportData)
    {
        public MemberResolveData(String member) : this(member, new ImportData())
        {
        }
    }

    internal record CastResolveData(String Cast, ImportData ImportData)
    {
        public CastResolveData(String cast) : this(cast, new ImportData())
        {
        }
    }

    internal interface IExternalEntityResolver
    {
        OperationResult<MemberResolveData> ResolveCtor(ITypeSymbol sourceType, IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation);
        OperationResult<MemberResolveData> ResolveMember(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation);
        OperationResult<CastResolveData> ResolveCast(ExpressionSyntax sourceExpression, ITypeSymbol castTypeSymbol, String sourceRepresentation);
    }
}
