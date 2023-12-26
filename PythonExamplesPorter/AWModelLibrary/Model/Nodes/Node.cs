namespace AWords
{
    public abstract class Node
    {
        public virtual NodeType NodeType => NodeType.Unknown;

        //public Node? Parent => _parent;

        public IEnumerable<Node> Children => ChildrenNodes;

        public Int32 Count => ChildrenNodes.Count;

        public IList<Node> GetChildrenNodes() => ChildrenNodes.ToList();

        public abstract String GetText();

        protected Node(IList<Node> children)
        {
            ChildrenNodes = children;
        }

        //private readonly Node? _parent;
        //private readonly IList<Node> _children;
        protected IList<Node> ChildrenNodes;
    }
}
