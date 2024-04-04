namespace PythonExamplesPorterApp.Comments
{
    internal class CommentsProcessor
    {
        public String[] Process(String[] source)
        {
            return source.Select(ProcessImpl).ToArray();
        }

        public String? Process(String? source)
        {
            return source == null ? null : ProcessImpl(source);
        }

        private String ProcessImpl(String comment)
        {
            const String commentStart = "//";
            if (!String.IsNullOrEmpty(comment) && !comment.StartsWith(commentStart))
                throw new InvalidOperationException("Bad comment");
            return comment.Replace(commentStart, "#");
        }
    }
}
