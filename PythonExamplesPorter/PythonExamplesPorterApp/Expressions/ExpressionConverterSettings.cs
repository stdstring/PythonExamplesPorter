namespace PythonExamplesPorterApp.Expressions
{
    internal struct ExpressionConverterSettings
    {
        public ExpressionConverterSettings()
        {
        }

        public ExpressionConverterSettings(ExpressionConverterSettings other)
        {
            AllowIncrementDecrement = other.AllowIncrementDecrement;
            AllowObjectInitializer = other.AllowObjectInitializer;
            QuoteMark = other.QuoteMark;
        }

        public Boolean AllowIncrementDecrement { get; set; }

        public Boolean AllowObjectInitializer { get; set; }

        public Char QuoteMark { get; set; } = '"';

        public readonly ExpressionConverterSettings CreateChild()
        {
            return new ExpressionConverterSettings(this)
            {
                AllowIncrementDecrement = false,
                AllowObjectInitializer = false
            };
        }
    }
}