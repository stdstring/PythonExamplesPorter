using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal record TypeResolveData(String TypeName, String ModuleName);

    internal record MemberData(ExpressionSyntax Target, SimpleNameSyntax Name, IReadOnlyList<ArgumentSyntax> Arguments);

    internal record MemberRepresentation(String Target, ConvertedArguments Arguments);

    // TODO (std_string) : think about using ImportData instead of single module name
    internal record MemberResolveData(String Member, String ModuleName)
    {
        public MemberResolveData(String member) : this(member, "")
        {
        }
    }

    internal record CastResolveData(String Cast, String ModuleName)
    {
        public CastResolveData(String cast) : this(cast, "")
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
