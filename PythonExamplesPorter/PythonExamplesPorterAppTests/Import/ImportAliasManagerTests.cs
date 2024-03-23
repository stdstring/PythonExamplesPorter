using NUnit.Framework;
using PythonExamplesPorterApp.DestStorage;
using PythonExamplesPorterApp.Import;

namespace PythonExamplesPorterAppTests.Import
{
    [TestFixture]
    public class ImportAliasManagerTests
    {
        [TestCaseSource(nameof(PrepareImportTestCases))]
        public void PrepareImport(String sourceModule, String expectedModule, IDictionary<String, String> expectedImport)
        {
            ImportAliasManager manager = new ImportAliasManager(_importAliases);
            (String actualModule, ImportData actualImport) = manager.PrepareImport(sourceModule);
            Assert.AreEqual(expectedModule, actualModule);
            Assert.That(actualImport.ModulesImport, Is.EquivalentTo(expectedImport));
            Assert.IsEmpty(actualImport.EntityImport);
        }

        private static readonly Object[] PrepareImportTestCases = new Object[]
        {
            new Object[]{"aspose.words", "aw", new Dictionary<String, String>{{"aspose.words", "aw"}}},
            new Object[]{"aspose.words.drawing", "aw.drawing", new Dictionary<String, String>{{"aspose.words", "aw"}, {"aspose.words.drawing", ""}}},
            new Object[]{"aspose.words.drawing.charts", "aw.drawing.charts", new Dictionary<String, String>{{"aspose.words", "aw"}, {"aspose.words.drawing.charts", ""}}},
            new Object[]{"aspose.words.fonts", "aw.fonts", new Dictionary<String, String>{{"aspose.words", "aw"}, {"aspose.words.fonts", ""}}},
            new Object[]{"aspose.pydrawing", "drawing", new Dictionary<String, String>{{"aspose.pydrawing", "drawing"}}},
            new Object[]{"aspose.pydrawing.rectangles", "drawing.rectangles", new Dictionary<String, String>{{"aspose.pydrawing", "drawing"}, {"aspose.pydrawing.rectangles", ""}}},
            new Object[]{"aspose.something", "aspose.something", new Dictionary<String, String>{{"aspose.something", ""}}},
            new Object[]{"xxx.yyy", "xxx.yyy", new Dictionary<String, String>{{"xxx.yyy", ""}}},
        };

        private readonly ImportAliasEntries _importAliases = new ImportAliasEntries
        {
            ImportAliases = new[]
            {
                new ImportAliasEntry{Import = "aspose.words", Alias = "aw"},
                new ImportAliasEntry{Import = "aspose.pydrawing", Alias = "drawing"}
            }
        };
    }
}
