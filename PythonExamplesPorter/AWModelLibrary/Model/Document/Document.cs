using System.Text;
using AWords.Loading;
using AWords.Saving;

namespace AWords
{
    public class Document : Node
    {
        public Document() : base(new List<Node>())
        {
        }

        public Document(IList<Node> children) : base(children)
        {
        }

        public override NodeType NodeType => NodeType.Document;

        public override string GetText()
        {
            StringBuilder builder = new StringBuilder();
            foreach (Node child in GetChildrenNodes())
                builder.AppendLine(child.GetText());
            return builder.ToString();
        }

        public void Load(String path)
        {
            Load(path, new LoadOptions());
        }

        public void Load(String path, LoadOptions options)
        {
            Encoding encoding = Encoding.GetEncoding(options.Encoding);
            String[] lines = File.ReadAllLines(path, encoding);
            IList<Node> paragraphNodes = new List<Node>();
            foreach (String line in lines)
            {
                IList<Node> wordNodes = new List<Node>();
                foreach (String word in line.Split(' ', '\t', StringSplitOptions.RemoveEmptyEntries))
                {
                    Node wordNode = new Word(word);
                    wordNodes.Add(wordNode);
                }
                Node paragraphNode = new Paragraph(line, wordNodes);
                paragraphNodes.Add(paragraphNode);
            }
            ChildrenNodes = paragraphNodes;
        }

        public void Save(String path)
        {
            Save(path, new SaveOptions());
        }

        public void Save(String path, SaveOptions options)
        {
            Encoding encoding = Encoding.GetEncoding(options.Encoding);
            using (StreamWriter writer = new StreamWriter(path, false, encoding))
                writer.Write(GetText());
        }
    }
}
