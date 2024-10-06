using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using PythonExamplesPorterApp.Common;
using PythonExamplesPorterApp.Converter;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Expressions;

namespace PythonExamplesPorterApp.ExternalEntities
{
    internal class NUnitEntityResolver : IExternalEntityResolver
    {
        public NUnitEntityResolver(SemanticModel model)
        {
            _model = model;
        }

        public OperationResult<MemberResolveData> ResolveCtor(ITypeSymbol sourceType, IReadOnlyList<ArgumentSyntax> argumentsData, ConvertedArguments argumentsRepresentation)
        {
            return new OperationResult<MemberResolveData>.Error("Not supported now for NUnit types");
        }

        public OperationResult<MemberResolveData> ResolveMember(MemberData data, ITypeSymbol sourceType, MemberRepresentation representation)
        {
            String sourceTypeFullName = sourceType.GetTypeFullName();
            if (!sourceTypeFullName.Equals("NUnit.Framework.Assert"))
                return new OperationResult<MemberResolveData>.Error($"Unsupported type {sourceTypeFullName}");
            AssertMemberResolver resolver = new AssertMemberResolver(_model);
            return resolver.ResolveMember(data, representation);
        }

        public OperationResult<CastResolveData> ResolveCast(ExpressionSyntax sourceExpression, ITypeSymbol castTypeSymbol, String sourceRepresentation)
        {
            return new OperationResult<CastResolveData>.Error("Not supported now");
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
                    return new OperationResult<MemberResolveData>.Error($"Unrecognizable member NUnit.Framework.Assert.{name.Identifier}");
                case IMethodSymbol {Name: "AreEqual"}:
                    return ResolveAreEqualMethod(data, representation);
                case IMethodSymbol {Name: "AreNotEqual"}:
                    return ResolveAreNotEqualMethod(data, representation);
                case IMethodSymbol {Name: "AreNotSame"}:
                    return ResolveAreNotSameMethod(data, representation);
                case IMethodSymbol {Name: "False"}:
                case IMethodSymbol {Name: "IsFalse"}:
                case IMethodSymbol {Name: "IsEmpty"}:
                    return ResolveFalseMethod(data, representation);
                case IMethodSymbol {Name: "IsNull"}:
                case IMethodSymbol {Name: "Null"}:
                    return ResolveNullMethod(data, representation);
                case IMethodSymbol {Name: "NotNull"}:
                case IMethodSymbol {Name: "IsNotNull"}:
                    return ResolveNotNullMethod(data, representation);
                case IMethodSymbol {Name: "IsTrue"}:
                case IMethodSymbol {Name: "IsNotEmpty"}:
                case IMethodSymbol {Name: "True"}:
                    return ResolveTrueMethod(data, representation);
                case IMethodSymbol {Name: "Less"}:
                    return ResolveLessMethod(data, representation);
            }
            return new OperationResult<MemberResolveData>.Error($"Unsupported member NUnit.Framework.Assert.{name.Identifier}");
        }

        private OperationResult<MemberResolveData> ResolveLessMethod(MemberData data, MemberRepresentation representation)
        {
            if (data.Arguments.Count < 2)
                return new OperationResult<MemberResolveData>.Error($"Bad arguments count in Assert.Less: {data.Arguments.Count}");
            switch (data.Arguments.Count)
            {
                case 2:
                    return GenerateMethodCall("assertLess", representation.Arguments.Values, Array.Empty<(String name, String value)>());
                default:
                    return new OperationResult<MemberResolveData>.Error("Unsupported arguments for Assert.Less");
            }
        }

        private OperationResult<MemberResolveData> ResolveAreEqualMethod(MemberData data, MemberRepresentation representation)
        {
            if (data.Arguments.Count < 2)
                return new OperationResult<MemberResolveData>.Error($"Bad arguments count in Assert.AreEqual: {data.Arguments.Count}");
            String arg0 = representation.Arguments.Values[0];
            String arg1 = representation.Arguments.Values[1];
            TypeInfo arg0Info = _model.GetTypeInfo(data.Arguments[0].Expression);
            TypeInfo arg1Info = _model.GetTypeInfo(data.Arguments[1].Expression);
            Boolean useEqualForCollections = arg0Info.Type is IArrayTypeSymbol || arg1Info.Type is IArrayTypeSymbol;
            String[] mainArgs = useEqualForCollections switch
            {
                true => new[]{PrepareArgumentForSequenceEqual(arg0, arg0Info), PrepareArgumentForSequenceEqual(arg1, arg1Info)},
                false => new[]{arg0, arg1}
            };
            switch (data.Arguments.Count)
            {
                case 2:
                    (String name, String value)[] emptyNamedArgs = Array.Empty<(String name, String value)>();
                    return useEqualForCollections switch
                    {
                        true => GenerateMethodCall("assertSequenceEqual", mainArgs, emptyNamedArgs),
                        false => GenerateMethodCall("assertEqual", mainArgs, emptyNamedArgs)
                    };
                case 3:
                    String arg2 = representation.Arguments.Values[2];
                    ExpressionSyntax arg2Expression = data.Arguments.Last().Expression;
                    String? arg2ExpressionType = _model.GetTypeInfo(arg2Expression).Type?.GetTypeFullName();
                    if (arg2ExpressionType == null)
                        return new OperationResult<MemberResolveData>.Error("Unrecognizable third argument of Assert.AreEqual");
                    String? methodName = arg2ExpressionType switch
                    {
                        "System.Single" => "assertAlmostEqual",
                        "System.Double" => "assertAlmostEqual",
                        "System.String" when useEqualForCollections => "assertSequenceEqual",
                        "System.String" => "assertEqual",
                        _ => null
                    };
                    if (methodName is null)
                        return new OperationResult<MemberResolveData>.Error("Unsupported third argument of Assert.AreEqual");
                    (String name, String value)[] namedArgs = arg2ExpressionType! switch
                    {
                        "System.Single" => new[]{(name: "delta", value: arg2)},
                        "System.Double" => new[]{(name: "delta", value: arg2)},
                        "System.String" => new[]{(name: "msg", value: arg2)},
                        _ => Array.Empty<(String name, String value)>()
                    };
                    return GenerateMethodCall(methodName, mainArgs, namedArgs);
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for Assert.AreEqual");
        }

        private String PrepareArgumentForSequenceEqual(String argRepresentation, TypeInfo argInfo)
        {
            return argInfo.Type switch
            {
                null => argRepresentation,
                var type when type.AllInterfaces.All(i => i.MetadataName != "ICollection" && i.MetadataName != "ICollection`1") => $"list({argRepresentation})",
                _ => argRepresentation,
            };
        }

        private OperationResult<MemberResolveData> ResolveAreNotEqualMethod(MemberData data, MemberRepresentation representation)
        {
            if (data.Arguments.Count < 2)
                return new OperationResult<MemberResolveData>.Error($"Bad arguments count in Assert.AreNotEqual: {data.Arguments.Count}");
            // TODO (std_string) : add check of arg type
            String[] args = {representation.Arguments.Values[0], representation.Arguments.Values[1]};
            switch (data.Arguments.Count)
            {
                case 2:
                    return GenerateMethodCall("assertNotEqual", args, Array.Empty<(String name, String value)>());
                case 3:
                    return GenerateMethodCall("assertNotEqual", args, new[]{(name: "msg", value: representation.Arguments.Values[2])});
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for Assert.AreNotEqual");
        }

        // TODO (std_string) : think about porting Assert.AreNotSame as assertNotEqual method
        private OperationResult<MemberResolveData> ResolveAreNotSameMethod(MemberData data, MemberRepresentation representation)
        {
            if (data.Arguments.Count < 2)
                return new OperationResult<MemberResolveData>.Error($"Bad arguments count in Assert.AreNotSame: {data.Arguments.Count}");
            // TODO (std_string) : add check of arg type
            String[] args = {representation.Arguments.Values[0], representation.Arguments.Values[1]};
            switch (data.Arguments.Count)
            {
                case 2:
                    return GenerateMethodCall("assertNotEqual", args, Array.Empty<(String name, String value)>());
                case 3:
                    return GenerateMethodCall("assertNotEqual", args, new[]{(name: "msg", value: representation.Arguments.Values[2])});
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for Assert.AreNotSame");
        }

        private OperationResult<MemberResolveData> ResolveFalseMethod(MemberData data, MemberRepresentation representation)
        {
            if (data.Arguments.Count < 1)
                return new OperationResult<MemberResolveData>.Error($"Bad arguments count in Assert.False/Assert.IsFalse/Assert.IsEmpty: {data.Arguments.Count}");
            // TODO (std_string) : add check of arg type
            String[] args = {representation.Arguments.Values[0]};
            switch (data.Arguments.Count)
            {
                case 1:
                    return GenerateMethodCall("assertFalse", args, Array.Empty<(String name, String value)>());
                case 2:
                    return GenerateMethodCall("assertFalse", args, new[]{(name: "msg", value: representation.Arguments.Values[1])});
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for Assert.False/Assert.IsFalse/Assert.IsEmpty");
        }

        private OperationResult<MemberResolveData> ResolveNullMethod(MemberData data, MemberRepresentation representation)
        {
            if (data.Arguments.Count < 1)
                return new OperationResult<MemberResolveData>.Error($"Bad arguments count in Assert.Null/Assert.IsNull: {data.Arguments.Count}");
            // TODO (std_string) : add check of arg type
            String[] args = {representation.Arguments.Values[0]};
            switch (data.Arguments.Count)
            {
                case 1:
                    return GenerateMethodCall("assertIsNone", args, Array.Empty<(String name, String value)>());
                case 2:
                    return GenerateMethodCall("assertIsNone", args, new[]{(name: "msg", value: representation.Arguments.Values[1])});
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for Assert.Null/Assert.IsNull");
        }

        private OperationResult<MemberResolveData> ResolveNotNullMethod(MemberData data, MemberRepresentation representation)
        {
            if (data.Arguments.Count < 1)
                return new OperationResult<MemberResolveData>.Error($"Bad arguments count in Assert.NotNull/Assert.IsNotNull: {data.Arguments.Count}");
            // TODO (std_string) : add check of arg type
            String[] args = {representation.Arguments.Values[0]};
            switch (data.Arguments.Count)
            {
                case 1:
                    return GenerateMethodCall("assertIsNotNone", args, Array.Empty<(String name, String value)>());
                case 2:
                    return GenerateMethodCall("assertIsNotNone", args, new[]{(name: "msg", value: representation.Arguments.Values[1])});
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for Assert.NotNull/Assert.IsNotNull");
        }

        private OperationResult<MemberResolveData> ResolveTrueMethod(MemberData data, MemberRepresentation representation)
        {
            if (data.Arguments.Count < 1)
                return new OperationResult<MemberResolveData>.Error($"Bad arguments count in Assert.True/Assert.IsTrue/Assert.IsNotEmpty: {data.Arguments.Count}");
            // TODO (std_string) : add check of arg type
            String[] args = {representation.Arguments.Values[0]};
            switch (data.Arguments.Count)
            {
                case 1:
                    return GenerateMethodCall("assertTrue", args, Array.Empty<(String name, String value)>());
                case 2:
                    return GenerateMethodCall("assertTrue", args, new[]{(name: "msg", value: representation.Arguments.Values[1])});
            }
            return new OperationResult<MemberResolveData>.Error("Unsupported arguments for Assert.True/Assert.IsTrue/Assert.IsNotEmpty");
        }

        private OperationResult<MemberResolveData> GenerateMethodCall(String methodName, String[] args, (String name, String value)[] namedArgs)
        {
            String argsPart = String.Join(", ", args);
            String namedArgsPart = String.Join("", namedArgs.Select(arg => $", {arg.name}={arg.value}"));
            String methodCall = $"self.{methodName}({argsPart}{namedArgsPart})";
            MemberResolveData resolveData = new MemberResolveData(methodCall, new ImportData().AddImport("unittest"));
            return new OperationResult<MemberResolveData>.Ok(resolveData);
        }

        private readonly SemanticModel _model;
    }
}