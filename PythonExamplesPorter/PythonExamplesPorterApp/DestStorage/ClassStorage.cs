using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.DestStorage
{
    internal class ClassStorage
    {
        public ClassStorage(String className, Int32 indentation)
        {
            _className = className;
            _indentation = indentation;
        }

        public void Save(TextWriter writer)
        {
            String baseIndentation = IndentationUtils.Create(_indentation);
            String bodyIndentation = IndentationUtils.Create(_indentation + StorageDef.IndentationDelta);
            foreach (String decorator in _decorators)
                writer.WriteLine($"{baseIndentation}{decorator}");
            String baseClassesPart = _baseClasses.IsEmpty() ? "" : $"({String.Join(",", _baseClasses)})";
            writer.WriteLine($"{baseIndentation}class {_className}{baseClassesPart}:");
            for (Int32 index = 0; index < _methods.Count; ++index)
            {
                if (index > 0)
                    writer.WriteLine();
                _methods[index].Save(writer);
            }
            if (_methods.IsEmpty())
                writer.WriteLine($"{bodyIndentation}pass");
        }

        public void AddDecorator(String decorator)
        {
            _decorators.Add(decorator);
        }

        public void AddBaseClass(String baseClass)
        {
            _baseClasses.Add(baseClass);
        }

        public MethodStorage CreateMethodStorage(String methodName)
        {
            MethodStorage currentMethod = new MethodStorage(methodName, _indentation + StorageDef.IndentationDelta);
            _methods.Add(currentMethod);
            return currentMethod;
        }

        private readonly String _className;
        private readonly Int32 _indentation;
        private readonly IList<String> _decorators = new List<String>();
        private readonly IList<String> _baseClasses = new List<String>();
        private readonly IList<MethodStorage> _methods = new List<MethodStorage>();
    }
}
