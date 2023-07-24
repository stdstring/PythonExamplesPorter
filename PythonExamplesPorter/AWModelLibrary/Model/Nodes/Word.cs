namespace AWords
{
    public class Word : Node
    {
        public Word(String text) : base(new List<Node>())
        {
            _text = text;
        }

        public override NodeType NodeType => NodeType.Word;

        public override String GetText() => _text;

        private readonly String _text;
    }
}
