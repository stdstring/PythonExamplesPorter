using System.Text;
using PythonExamplesPorterApp.Names;

namespace PythonExamplesPorterApp.Comments
{
    internal class CommentsProcessor
    {
        public CommentsProcessor(NameTransformer nameTransformer)
        {
            _nameTransformer = nameTransformer;
        }

        public String[] Process(String[] source)
        {
            return source.Select(ProcessImpl).Where(comment => !String.IsNullOrEmpty(comment)).ToArray();
        }

        public String? Process(String? source)
        {
            if (source == null)
                return null;
            String comment = ProcessImpl(source);
            return String.IsNullOrEmpty(comment) ? null : comment;
        }

        private String ProcessImpl(String comment)
        {
            const String commentStart = "//";
            if (!String.IsNullOrEmpty(comment) && !comment.StartsWith(commentStart))
                throw new InvalidOperationException("Bad comment");
            String convertedComment = comment.Replace(commentStart, "#");
            switch (convertedComment)
            {
                case var _ when convertedComment.StartsWith("#ExFor:"):
                    return ProcessExForComment(convertedComment);
                case var _ when convertedComment.StartsWith("#GistId:"):
                    return String.Empty;
                default:
                    return convertedComment;
            }
        }

        // TODO (std_string) : we use here very simple approach without real searching of types
        private String ProcessExForComment(String comment)
        {
            Boolean CanTransformAsMethod(String typeName, String memberName, String argumentList) =>
                !String.IsNullOrEmpty(argumentList) && !typeName.Contains(GenericTypeSpec) && !memberName.Contains(GenericTypeSpec);
            StringBuilder builder = new StringBuilder();
            builder.Append(ExForPrefix);
            comment = comment.Substring(ExForPrefix.Length).Trim();
            Int32 argumentStart = comment.IndexOf('(');
            String argumentList = argumentStart == -1 ? "" : comment.Substring(argumentStart);
            String mainBody = argumentStart == -1 ? comment : comment.Substring(0, argumentStart);
            switch (mainBody.Split('.'))
            {
                case [_] when !String.IsNullOrEmpty(argumentList):
                    throw new InvalidOperationException($"Bad ExFor comment: {comment}");
                case [var typeName]:
                    builder.Append(TransformTypeName(typeName));
                    break;
                case [var typeName, var memberName] when CanTransformAsMethod(typeName, memberName, argumentList):
                    builder.Append($"{TransformTypeName(typeName)}.{TransformMemberName(typeName, memberName, true)}({TransformArgumentList(argumentList)})");
                    break;
                case [var typeName, var memberName]:
                    builder.Append($"{TransformTypeName(typeName)}.{TransformMemberName(typeName, memberName, false)}");
                    break;
                default:
                    throw new InvalidOperationException($"Bad ExFor comment: {comment}");
            }
            return builder.ToString();
        }

        private String TransformTypeName(String typeName)
        {
            return typeName.IndexOf(GenericTypeSpec) switch
            {
                -1 => _nameTransformer.TransformTypeName(typeName),
                var genericSpecStart => _nameTransformer.TransformTypeName(typeName.Substring(0, genericSpecStart))
            };
        }

        private String TransformMemberName(String typeName, String memberName, Boolean hasArguments)
        {
            Int32 genericSpecStart = memberName.IndexOf(GenericTypeSpec);
            return memberName switch
            {
                "#ctor" => "__init__",
                "Item" => "__getitem__",
                "GetEnumerator" => "__iter__",
                "Equals" => "__eq__",
                "ToString" => "__str__",
                "GetHashCode" => "__hash__",
                _ when genericSpecStart != -1 =>
                    _nameTransformer.TransformMethodName(typeName, memberName.Substring(0, genericSpecStart)),
                _ when hasArguments => _nameTransformer.TransformMethodName(typeName, memberName),
                _ when !hasArguments => _nameTransformer.TransformPropertyName(typeName, memberName),
                _ => throw new InvalidOperationException($"Unexpected member name: {memberName}")
            };
        }

        private String TransformArgumentList(String argumentList)
        {
            String[] destArguments = argumentList.TrimStart('(').TrimEnd(')').Split(',').Select(TransformArgument).ToArray();
            return string.Join(',', destArguments);
        }

        private String TransformArgument(String argument)
        {
            const String arraySuffix = "[]";
            return argument.Trim() switch
            {
                var value when KnownTypeNames.ContainsKey(value) => KnownTypeNames[value],
                var value when value.EndsWith(arraySuffix) =>
                    $"List[{TransformArgument(value.Substring(0, value.Length - arraySuffix.Length))}]",
                var value when value.Contains('.') => throw new InvalidOperationException($"Unexpected argument: {value}"),
                var value => TransformTypeName(value)
            };
        }

        private const String ExForPrefix = "#ExFor:";
        private const Char GenericTypeSpec = '`';

        private readonly NameTransformer _nameTransformer;

        private static readonly IDictionary<String, String> KnownTypeNames = new Dictionary<String, String>
        {
            // bool type
            {"bool", "bool"},
            {"Boolean", "bool"},
            {"System.Boolean", "bool"},
            // integer numbers types
            {"long", "int"},
            {"Int64", "int"},
            {"System.Int64", "int"},
            {"ulong", "int"},
            {"UInt64", "int"},
            {"System.UInt64", "int"},
            {"int", "int"},
            {"Int32", "int"},
            {"System.Int32", "int"},
            {"uint", "int"},
            {"UInt32", "int"},
            {"System.UInt32", "int"},
            {"short", "int"},
            {"Int16", "int"},
            {"System.Int16", "int"},
            {"ushort", "int"},
            {"UInt16", "int"},
            {"System.UInt16", "int"},
            {"byte", "int"},
            {"Byte", "int"},
            {"System.Byte", "int"},
            {"sbyte", "int"},
            {"SByte", "int"},
            {"System.SByte", "int"},
            // byte arrays
            {"byte[]", "bytes"},
            {"Byte[]", "bytes"},
            {"System.Byte[]", "bytes"},
            {"sbyte[]", "bytes"},
            {"SByte[]", "bytes"},
            {"System.SByte[]", "bytes"},
            // real numbers types
            {"float", "float"},
            {"Single", "float"},
            {"System.Single", "float"},
            {"double", "float"},
            {"Double", "float"},
            {"System.Double", "float"},
            {"decimal", "float"},
            {"Decimal", "float"},
            {"System.Decimal", "float"},
            // char, string types
            {"char", "str"},
            {"Char", "str"},
            {"System.Char", "str"},
            {"string", "str"},
            {"String", "str"},
            {"System.String", "str"},
            // DateTime type
            {"DateTime", "datetime"},
            {"System.DateTime", "datetime"},
            // object type
            {"object", "object"},
            {"Object", "object"},
            {"System.Object", "object"},
        };
    }
}
