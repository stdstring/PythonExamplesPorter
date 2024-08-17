using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using NUnit.Framework;
using PythonExamplesPorterApp.Comments;
using PythonExamplesPorterAppTests.TestUtils;

namespace PythonExamplesPorterAppTests.Comments
{
    [TestFixture]
    public class CommentsExtractorTests
    {
        [Test]
        public void ExtractForMethods()
        {
            const String source = "namespace ApiExamples\r\n" +
                                  "{\r\n" +
                                  "    public class ExProblem\r\n" +
                                  "    {\r\n" +
                                  "        // Comment 1.1\r\n" +
                                  "        // Comment 1.2\r\n" +
                                  "        public void Method1()\r\n" +
                                  "        {\r\n" +
                                  "        } // Comment 2\r\n" +
                                  "        // Comment 3.1\r\n" +
                                  "        // Comment 3.2\r\n" +
                                  "\r\n" +
                                  "        // Comment 4.1\r\n" +
                                  "        // Comment 4.2\r\n" +
                                  "        // Comment 4.3\r\n" +
                                  "\r\n" +
                                  "        // Comment 5\r\n" +
                                  "        public void Method2()\r\n" +
                                  "        {\r\n" +
                                  "        }\r\n" +
                                  "        // Comment 6.1\r\n" +
                                  "        // Comment 6.2\r\n" +
                                  "    }\r\n" +
                                  "}";
            SemanticModel model = PreparationHelper.Prepare(source, "CommentsExtractorTests");
            SyntaxNode[] descendantNodes = model.SyntaxTree.GetRoot().DescendantNodes().ToArray();
            MethodDeclarationSyntax[] methods = descendantNodes.OfType<MethodDeclarationSyntax>().ToArray();
            CheckComments(methods.First(method => method.Identifier.ToString().Equals("Method1")),
                          new []{"// Comment 1.1", "// Comment 1.2"},
                          "// Comment 2",
                          new []{"// Comment 3.1", "// Comment 3.2"});
            CheckComments(methods.First(method => method.Identifier.ToString().Equals("Method2")),
                          new []{"// Comment 4.1", "// Comment 4.2", "// Comment 4.3", "", "// Comment 5"},
                          null,
                          new []{"// Comment 6.1", "// Comment 6.2"});
        }

        [Test]
        public void ExtractForStatementsInBody()
        {
            const String source = "namespace ApiExamples\r\n" +
                                  "{\r\n" +
                                  "    public class ExProblem\r\n" +
                                  "    {\r\n" +
                                  "        public void Method1()\r\n" +
                                  "        {\r\n" +
                                  "            // Comment 1\r\n" +
                                  "            int i1 = 100;\r\n" +
                                  "            // Comment 2\r\n" +
                                  "            int i2 = 100;\r\n" +
                                  "            // Comment 3\r\n" +
                                  "\r\n" +
                                  "            int i3 = 100;\r\n" +
                                  "\r\n" +
                                  "            // Comment 4\r\n" +
                                  "            int i4 = 100;\r\n" +
                                  "\r\n" +
                                  "            // Comment 5\r\n" +
                                  "\r\n" +
                                  "            int i5 = 100;\r\n" +
                                  "            // Comment 6\r\n" +
                                  "        }\r\n" +
                                  "\r\n" +
                                  "        public void Method2()\r\n" +
                                  "        {\r\n" +
                                  "\r\n" +
                                  "            // Comment 1\r\n" +
                                  "            int i1 = 100;\r\n" +
                                  "            int i2 = 100;\r\n" +
                                  "            // Comment 2\r\n" +
                                  "\r\n" +
                                  "        }\r\n" +
                                  "\r\n" +
                                  "        public void Method3()\r\n" +
                                  "        {\r\n" +
                                  "            // Comment 1\r\n" +
                                  "\r\n" +
                                  "            int i1 = 100;\r\n" +
                                  "            int i2 = 100;\r\n" +
                                  "\r\n" +
                                  "            // Comment 2\r\n" +
                                  "        }\r\n" +
                                  "\r\n" +
                                  "        public void Method4()\r\n" +
                                  "        {\r\n" +
                                  "\r\n" +
                                  "            // Comment 1\r\n" +
                                  "\r\n" +
                                  "            int i1 = 100;\r\n" +
                                  "            int i2 = 100;\r\n" +
                                  "\r\n" +
                                  "            // Comment 2\r\n" +
                                  "\r\n" +
                                  "        }\r\n" +
                                  "    }\r\n" +
                                  "}";
            SemanticModel model = PreparationHelper.Prepare(source, "CommentsExtractorTests");
            SyntaxNode[] descendantNodes = model.SyntaxTree.GetRoot().DescendantNodes().ToArray();
            MethodDeclarationSyntax[] methods = descendantNodes.OfType<MethodDeclarationSyntax>().ToArray();
            MethodDeclarationSyntax method1 = methods.First(method => method.Identifier.ToString().Equals("Method1"));
            StatementSyntax[] method1Statements = method1.Body.MustCheck().Statements.ToArray();
            Assert.That(method1Statements.Length, Is.EqualTo(5));
            CheckComments(method1Statements[0], new []{"// Comment 1"}, null);
            CheckComments(method1Statements[1], new []{"// Comment 2"}, null);
            CheckComments(method1Statements[2], new []{"// Comment 3", ""}, null);
            CheckComments(method1Statements[3], new []{"", "// Comment 4"}, null);
            CheckComments(method1Statements[4], new []{"", "// Comment 5", ""}, null);
            CheckComments(method1Statements[4].GetLastToken().GetNextToken(), new []{"// Comment 6"});
            MethodDeclarationSyntax method2 = methods.First(method => method.Identifier.ToString().Equals("Method2"));
            StatementSyntax[] method2Statements = method2.Body.MustCheck().Statements.ToArray();
            Assert.That(method2Statements.Length, Is.EqualTo(2));
            CheckComments(method2Statements[0], new []{"", "// Comment 1"}, null);
            CheckComments(method2Statements[1], Array.Empty<String>(), null);
            CheckComments(method2Statements[1].GetLastToken().GetNextToken(), new[] {"// Comment 2", ""});
            MethodDeclarationSyntax method3 = methods.First(method => method.Identifier.ToString().Equals("Method3"));
            StatementSyntax[] method3Statements = method3.Body.MustCheck().Statements.ToArray();
            Assert.That(method3Statements.Length, Is.EqualTo(2));
            CheckComments(method3Statements[0], new[] {"// Comment 1", ""}, null);
            CheckComments(method3Statements[1], Array.Empty<String>(), null);
            CheckComments(method3Statements[1].GetLastToken().GetNextToken(), new[] {"", "// Comment 2"});
            MethodDeclarationSyntax method4 = methods.First(method => method.Identifier.ToString().Equals("Method4"));
            StatementSyntax[] method4Statements = method4.Body.MustCheck().Statements.ToArray();
            Assert.That(method4Statements.Length, Is.EqualTo(2));
            CheckComments(method4Statements[0], new[] {"", "// Comment 1", ""}, null);
            CheckComments(method4Statements[1], Array.Empty<String>(), null);
            CheckComments(method4Statements[1].GetLastToken().GetNextToken(), new[] {"", "// Comment 2", ""});
        }

        [Test]
        public void ExtractTrailingCommentsForStatementsInBody()
        {
            const String source = "namespace ApiExamples\r\n" +
                                  "{\r\n" +
                                  "    public class ExProblem\r\n" +
                                  "    {\r\n" +
                                  "        public void Method1()\r\n" +
                                  "        {\r\n" +
                                  "            int i1 = 100; // Comment 1\r\n" +
                                  "            if (i1 > 0) // Comment 2 (missed)\r\n" +
                                  "                i1 = 200; // Comment 3\r\n" +
                                  "            if (i1 > 0) // Comment 4 (missed)\r\n" +
                                  "            {\r\n" +
                                  "                i1 = 666; // Comment 5\r\n" +
                                  "            } // Comment 6\r\n" +
                                  "        }\r\n" +
                                  "    }\r\n" +
                                  "}";
            SemanticModel model = PreparationHelper.Prepare(source, "CommentsExtractorTests");
            SyntaxNode[] descendantNodes = model.SyntaxTree.GetRoot().DescendantNodes().ToArray();
            MethodDeclarationSyntax[] methods = descendantNodes.OfType<MethodDeclarationSyntax>().ToArray();
            MethodDeclarationSyntax method1 = methods.First(method => method.Identifier.ToString().Equals("Method1"));
            StatementSyntax[] method1Statements = method1.Body.MustCheck().DescendantNodes().OfType<StatementSyntax>().ToArray();
            // (std_string) : we will never retrieve comments "// Comment 2 (missed)" and "// Comment 4 (missed)",
            // if we will work only with StatementSyntax nodes
            Assert.That(method1Statements.Length, Is.EqualTo(6));
            CheckComments(method1Statements[0], Array.Empty<String>(), "// Comment 1");
            CheckComments(method1Statements[1], Array.Empty<String>(), "// Comment 3");
            CheckComments(method1Statements[2], Array.Empty<String>(), "// Comment 3");
            CheckComments(method1Statements[3], Array.Empty<String>(), "// Comment 6");
            CheckComments(method1Statements[4], Array.Empty<String>(), "// Comment 6");
            CheckComments(method1Statements[5], Array.Empty<String>(), "// Comment 5");
        }

        private void CheckComments(MethodDeclarationSyntax method, String[] expectedHeader, String? expectedTrailing, String[] expectedFooter)
        {
            Assert.That(CommentsExtractor.ExtractHeaderComments(method), Is.EquivalentTo(expectedHeader));
            Assert.That(CommentsExtractor.ExtractTrailingComment(method), Is.EqualTo(expectedTrailing));
            Assert.That(CommentsExtractor.ExtractFooterComments(method), Is.EquivalentTo(expectedFooter));
        }

        private void CheckComments(StatementSyntax statement, String[] expectedHeader, String? expectedTrailing)
        {
            Assert.That(CommentsExtractor.ExtractComments(statement), Is.EquivalentTo(expectedHeader));
            Assert.That(CommentsExtractor.ExtractTrailingComment(statement), Is.EqualTo(expectedTrailing));
        }

        private void CheckComments(SyntaxToken token, String[] expectedHeader)
        {
            Assert.That(CommentsExtractor.ExtractComments(token), Is.EquivalentTo(expectedHeader));
        }
    }
}
