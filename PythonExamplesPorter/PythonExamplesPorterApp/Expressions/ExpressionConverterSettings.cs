namespace PythonExamplesPorterApp.Expressions
{
    internal class ExpressionConverterSettings
    {
        public ExpressionConverterSettings()
        {
        }

        public ExpressionConverterSettings(ExpressionConverterSettings other)
        {
            AllowIncrementDecrement = other.AllowIncrementDecrement;
            AllowObjectInitializer = other.AllowObjectInitializer;
        }

        public Boolean AllowIncrementDecrement { get; set; }

        public Boolean AllowObjectInitializer { get; set; }

        public ExpressionConverterSettings CreateChild()
        {
            return new ExpressionConverterSettings(this)
            {
                AllowIncrementDecrement = false,
                AllowObjectInitializer = false
            };
        }
    }
}