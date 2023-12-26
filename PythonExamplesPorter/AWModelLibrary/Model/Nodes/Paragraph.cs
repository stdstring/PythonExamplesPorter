namespace AWords
{
    public class Paragraph : Node
    {
        public Paragraph(String text, IList<Node> children) : base(children)
        {
            _text = text;
        }

        public override NodeType NodeType => NodeType.Paragraph;

        public override String GetText() => _text;

        private readonly String _text;
    }
}
