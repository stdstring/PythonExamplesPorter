using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.Comments
{
    internal static class CommentsExtractor
    {
        public static String[] ExtractHeaderComments(SyntaxNode node)
        {
            GroupData groupData = GroupCommentParts(node.GetLeadingTrivia());
            IList<IList<String>> groups = groupData.Groups;
            SyntaxToken firstToken = node.GetFirstToken();
            SyntaxToken prevToken = firstToken.GetPreviousToken();
            switch (prevToken.Kind())
            {
                case var _ when groups.Count == 1 && groupData.HasSpaceBack:
                    return Array.Empty<String>();
                case SyntaxKind.OpenBraceToken:
                case var _ when groups.Count == 1:
                case var _ when groupData.HasSpaceFront:
                    return JoinGroups(groups, 0).ToArray();
                default:
                    return JoinGroups(groups, 1).ToArray();
            }
        }

        public static String[] ExtractComments(SyntaxNode node)
        {
            return ExtractComments(node.GetLeadingTrivia());
        }

        public static String[] ExtractComments(SyntaxToken token)
        {
            return ExtractComments(token.LeadingTrivia);
        }

        public static String? ExtractTrailingComment(SyntaxNode node)
        {
            return node.GetTrailingTrivia()
                .Where(entry => entry.IsKind(SyntaxKind.SingleLineCommentTrivia))
                .Select(entry => entry.ToString().Trim())
                .SingleOrDefault();
        }

        public static String[] ExtractFooterComments(SyntaxNode node)
        {
            SyntaxToken lastToken = node.GetLastToken();
            SyntaxToken nextToken = lastToken.GetNextToken();
            GroupData groupData = GroupCommentParts(nextToken.LeadingTrivia);
            IList<IList<String>> groups = groupData.Groups;
            switch (nextToken.Kind())
            {
                case var _ when groups.IsEmpty():
                    return Array.Empty<String>();
                case SyntaxKind.CloseBraceToken:
                    return JoinGroups(groups, 0).ToArray();
                case var _ when groupData.HasSpaceFront:
                    return Array.Empty<String>();
                default:
                    return groups[0].ToArray();
            }
        }

        private static String[] ExtractComments(IReadOnlyList<SyntaxTrivia> triviaList)
        {
            GroupData groupData = GroupCommentParts(triviaList);
            IList<IList<String>> groups = groupData.Groups;
            if (groups.IsEmpty())
                return Array.Empty<String>();
            IList<String> result = JoinGroups(groupData.Groups, 0);
            if (groupData.HasSpaceFront)
                result.Insert(0, "");
            if (groupData.HasSpaceBack)
                result.Add("");
            return result.ToArray();
        }

        private record GroupData(IList<IList<String>> Groups, Boolean HasSpaceFront, Boolean HasSpaceBack);

        private static GroupData GroupCommentParts(IReadOnlyList<SyntaxTrivia> source)
        {
            IList<SyntaxTrivia> preparedSource = source
                .Where(trivia => trivia.IsKind(SyntaxKind.SingleLineCommentTrivia) || trivia.IsKind(SyntaxKind.EndOfLineTrivia))
                .ToList();
            IList<IList<String>> groups = new List<IList<String>>();
            groups.Add(new List<String>());
            for (Int32 index = 0; index < preparedSource.Count; ++index)
            {
                switch (preparedSource[index].Kind())
                {
                    case SyntaxKind.SingleLineCommentTrivia:
                        groups[^1].Add(preparedSource[index].ToString().Trim());
                        break;
                    case SyntaxKind.EndOfLineTrivia when (index > 0) && preparedSource[index - 1].IsKind(SyntaxKind.EndOfLineTrivia) && !groups[^1].IsEmpty():
                        groups.Add(new List<String>());
                        break;
                }
            }
            if (groups[^1].IsEmpty())
                groups.RemoveAt(groups.Count - 1);
            Boolean hasSpaceFront = (preparedSource.Count > 0) && preparedSource[0].IsKind(SyntaxKind.EndOfLineTrivia);
            Boolean hasSpaceBack = (preparedSource.Count > 1) &&
                                   preparedSource[^1].IsKind(SyntaxKind.EndOfLineTrivia) &&
                                   preparedSource[^2].IsKind(SyntaxKind.EndOfLineTrivia);
            return new GroupData(groups, hasSpaceFront, hasSpaceBack);
        }

        private static IList<String> JoinGroups(IList<IList<String>> groups, Int32 start)
        {
            List<String> dest = new List<String>();
            for (Int32 index = start; index < groups.Count; ++index)
            {
                if (index > start)
                    dest.Add("");
                dest.AddRange(groups[index]);
            }
            return dest;
        }
    }
}
