using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal class NUnitEntityResolver : IExternalEntityResolver
    {
        public NUnitEntityResolver(SemanticModel model)
        {
            _model = model;
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            if (!sourceTypeFullName.Equals("NUnit.Framework.Assert"))
                return new OperationResult<MemberResolveData>(false, $"Unsupported type {sourceTypeFullName}");
            AssertMemberResolver resolver = new AssertMemberResolver(_model);
            return resolver.ResolveMember(data, representation);
        }

        public OperationResult<CastResolveData> ResolveCast(ExpressionSyntax sourceExpression, ITypeSymbol castTypeSymbol, String sourceRepresentation)
        {
            return new OperationResult<CastResolveData>(false, "Not supported now");
        }

        private readonly SemanticModel _model;
    }

    internal class AssertMemberResolver
    {
        public AssertMemberResolver(SemanticModel model)
        {
            _model = model;
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, MemberRepresentation representation)
        {
            SimpleNameSyntax name = data.Name;
            SymbolInfo nameInfo = _model.GetSymbolInfo(name);
            switch (nameInfo.Symbol)
            {
                case null:
                    return new OperationResult<MemberResolveData>(false, $"Unrecognizable member NUnit.Framework.Assert.{name.Identifier}");
                case IMethodSymbol {Name: "AreEqual"}:
                    return ResolveAreEqualMethod(data, representation);
            }
            return new OperationResult<MemberResolveData>(false, $"Unsupported member NUnit.Framework.Assert.{name.Identifier}");
        }

        private OperationResult<MemberResolveData> ResolveAreEqualMethod(MemberData data, MemberRepresentation representation)
        {
            if (data.Arguments.Count < 2)
                return new OperationResult<MemberResolveData>(false, $"Bad arguments count in Assert.AreEqual: {data.Arguments.Count}");
            String firstArg = representation.Arguments.Values[0];
            String secondArg = representation.Arguments.Values[1];
            TypeInfo firstArgInfo = _model.GetTypeInfo(data.Arguments[0].Expression);
            TypeInfo secondArgInfo = _model.GetTypeInfo(data.Arguments[1].Expression);
            Boolean useEqualForCollections = firstArgInfo.Type is IArrayTypeSymbol || secondArgInfo.Type is IArrayTypeSymbol;
            switch (data.Arguments.Count)
            {
                case 2:
                    (String name, String value)[] emptyNamedArguments = Array.Empty<(String name, String value)>();
                    return useEqualForCollections switch
                    {
                        true => GenerateAreEqualEqual("assertSequenceEqual", firstArg, secondArg, emptyNamedArguments),
                        false => GenerateAreEqualEqual("assertEqual", firstArg, secondArg, emptyNamedArguments)
                    };
                case 3:
                    String thirdArg = representation.Arguments.Values[2];
                    ExpressionSyntax lastArgument = data.Arguments.Last().Expression;
                    String? lastArgumentType = _model.GetTypeInfo(lastArgument).Type?.GetTypeFullName();
                    if (lastArgumentType == null)
                        return new OperationResult<MemberResolveData>(false, "Unrecognizable third argument of Assert.AreEqual");
                    String? methodName = lastArgumentType switch
                    {
                        "System.Single" => "assertAlmostEqual",
                        "System.Double" => "assertAlmostEqual",
                        "System.String" when useEqualForCollections => "assertSequenceEqual",
                        "System.String" => "assertEqual",
                        _ => null
                    };
                    if (methodName is null)
                        return new OperationResult<MemberResolveData>(false, "Unsupported third argument of Assert.AreEqual");
                    (String name, String value)[] namedArguments = lastArgumentType! switch
                    {
                        "System.Single" => new[] {(name: "delta", value: thirdArg)},
                        "System.Double" => new[] {(name: "delta", value: thirdArg)},
                        "System.String" => new[] {(name: "msg", value: thirdArg)},
                        _ => Array.Empty<(String name, String value)>()
                    };
                    return GenerateAreEqualEqual(methodName, firstArg, secondArg, namedArguments);
            }
            return new OperationResult<MemberResolveData>(false, "Unsupported arguments for Assert.AreEqual");
        }

        private OperationResult<MemberResolveData> GenerateAreEqualEqual(String methodName, String arg0, String arg1, (String name, String value)[] namedArguments)
        {
            String namedArgumentsPart = String.Join("", namedArguments.Select(arg => $", {arg.name}={arg.value}"));
            String methodCall = $"self.{methodName}({arg0}, {arg1}{namedArgumentsPart})";
            MemberResolveData resolveData = new MemberResolveData(methodCall, "unittest");
            return new OperationResult<MemberResolveData>(true, "", resolveData);
        }

        private readonly SemanticModel _model;
    }
}
