using PythonExamplesPorterApp.Utils;

namespace PythonExamplesPorterApp.DestStorage
{
    internal class MethodStorage
    {
        public MethodStorage(String methodName, Int32 indentation)
        {
            _methodName = methodName;
            _indentation = indentation;
        }

        public void Save(TextWriter writer)
        {
            String baseIndentation = IndentationUtils.Create(_indentation);
            String bodyIndentation = IndentationUtils.Create(_indentation + StorageDef.IndentationDelta);
            foreach (String decorator in _decorators)
                writer.WriteLine($"{baseIndentation}{decorator}");
            writer.WriteLine($"{baseIndentation}def {_methodName}(self):");
            if (_errorReason != null)
            {
                writer.WriteLine($"{bodyIndentation}raise NotImplementedError(\"{_errorReason}\")");
                return;
            }
            foreach (String bodyLine in _body)
                writer.WriteLine($"{bodyIndentation}{bodyLine}");
            if (_body.IsEmpty())
                writer.WriteLine($"{bodyIndentation}pass");
        }

        public void AddDecorator(String decorator)
        {
            _decorators.Add(decorator);
        }

        public void AddBodyLine(String bodyLine)
        {
            if (_errorReason != null)
                throw new InvalidOperationException($"Method {_methodName} raises {_errorReason} error");
            _body.Add(bodyLine);
        }

        public void SetError(String errorReason)
        {
            _errorReason = errorReason;
        }

        public Boolean HasError => _errorReason != null;

        private readonly String _methodName;
        private readonly Int32 _indentation;
        private readonly IList<String> _decorators = new List<String>();
        private readonly IList<String> _body = new List<String>();
        private String? _errorReason;
    }
}
