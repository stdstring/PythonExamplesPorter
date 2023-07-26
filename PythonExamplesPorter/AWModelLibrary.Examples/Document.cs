using NUnit.Framework;

namespace ApiExamples
{
    [TestFixture]
    public class Document : ApiExampleBase
    {
        [Test]
        public void Create()
        {
        }

        [Test]
        public void Load()
        {
        }

        [Test]
        public void Save()
        {
        }

        // ignored method
        [Test]
        public void AdvancedCreate()
        {
            // do something
        }
    }

    // ignored class
    [TestFixture]
    public class DocumentAdvanced : ApiExampleBase
    {
        [Test]
        public void Create()
        {
            // do something
        }
    }
}
