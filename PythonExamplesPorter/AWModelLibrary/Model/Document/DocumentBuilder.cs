namespace AWords
{
    public class DocumentBuilder
    {
        public DocumentBuilder()
        {
            _paragraphs = new List<Node>();
        }

        public void AddParagraph(String text)
        {
            AddParagraph(CreateParagraph(text));
        }

        public void AddParagraph(Paragraph paragraph)
        {
            _paragraphs.Add(paragraph);
        }

        public void RemoveParagraph(Paragraph paragraph)
        {
            _paragraphs.Remove(paragraph);
        }

        public IList<Paragraph> GetParagraphs()
        {
            return _paragraphs.OfType<Paragraph>().ToList();
        }

        public void Clear()
        {
            _paragraphs.Clear();
        }

        public Document Create()
        {
            return new Document(_paragraphs);
        }

        private static Paragraph CreateParagraph(String text)
        {
            IList<Node> words = text
                .Split(' ', '\t', StringSplitOptions.RemoveEmptyEntries)
                .Select(part => new Word(part))
                .OfType<Node>()
                .ToList();
            return new Paragraph(text, words);
        }

        private readonly IList<Node> _paragraphs;
    }
}
