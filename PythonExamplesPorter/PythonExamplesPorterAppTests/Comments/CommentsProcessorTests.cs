using NUnit.Framework;
using PythonExamplesPorterApp.Comments;
using PythonExamplesPorterApp.Names;

namespace PythonExamplesPorterAppTests.Comments
{
    [TestFixture]
    internal class CommentsProcessorTests
    {
        public CommentsProcessorTests()
        {
            INameTransformStrategy transformStrategy = new SeparatedDigitsExceptSinglesNameConverter();
            IHandmadeNameManager manager = HandmadeNameManagerFactory.Create(_handmadeAliases);
            _nameTransformer = new NameTransformer(transformStrategy, manager);
        }

        [TestCase("", null)]
        [TestCase("//", "#")]
        [TestCase("////////", "####")]
        [TestCase("// Some simple comment", "# Some simple comment")]
        [TestCase("// OtherType", "# OtherType")]
        [TestCase("// OtherType.CreateDocument", "# OtherType.CreateDocument")]
        [TestCase("// OtherType.CreateDocument(int[])", "# OtherType.CreateDocument(int[])")]
        [TestCase("//ExStart", "#ExStart")]
        [TestCase("//ExStart: IDDQD", "#ExStart: IDDQD")]
        [TestCase("//ExStart: OtherType", "#ExStart: OtherType")]
        [TestCase("//ExStart: OtherType.CreateDocument", "#ExStart: OtherType.CreateDocument")]
        [TestCase("//ExStart: OtherType.CreateDocument(int[])", "#ExStart: OtherType.CreateDocument(int[])")]
        [TestCase("//ExEnd", "#ExEnd")]
        [TestCase("//ExEnd: IDDQD", "#ExEnd: IDDQD")]
        [TestCase("//ExEnd: OtherType", "#ExEnd: OtherType")]
        [TestCase("//ExEnd: OtherType.CreateDocument", "#ExEnd: OtherType.CreateDocument")]
        [TestCase("//ExEnd: OtherType.CreateDocument(int[])", "#ExEnd: OtherType.CreateDocument(int[])")]
        [TestCase("//ExSkip", "#ExSkip")]
        [TestCase("//ExSummary: blablabla", "#ExSummary: blablabla")]
        [TestCase("//ExSummary: blablabla OtherType", "#ExSummary: blablabla OtherType")]
        [TestCase("//ExSummary: blablabla OtherType.CreateDocument", "#ExSummary: blablabla OtherType.CreateDocument")]
        [TestCase("//ExSummary: blablabla OtherType.CreateDocument(int[])", "#ExSummary: blablabla OtherType.CreateDocument(int[])")]
        [TestCase("//ExFor:OtherType", "#ExFor:OtherType")]
        [TestCase("//ExFor:OtherType.SomeProp", "#ExFor:OtherType.some_prop")]
        [TestCase("//ExFor:OtherType.HRef", "#ExFor:OtherType.href")]
        [TestCase("//ExFor:OtherType.CreateDocument", "#ExFor:OtherType.create_document")]
        [TestCase("//ExFor:OtherType.CreateDocument(int)", "#ExFor:OtherType.create_document(int)")]
        [TestCase("//ExFor:OtherType.CreateDocument(int,string)", "#ExFor:OtherType.create_document(int,str)")]
        [TestCase("//ExFor:OtherType.CreateDocument(int,string,char)", "#ExFor:OtherType.create_document(int,str,str)")]
        [TestCase("//ExFor:OtherType.CreateDocument(int,string,char,Document)", "#ExFor:OtherType.create_document(int,str,str,Document)")]
        [TestCase("//ExFor:OtherType.SomeMethod()", "#ExFor:OtherType.some_method()")]
        [TestCase("//ExFor:OtherType.SomeMethod(bool,Boolean,System.Boolean)", "#ExFor:OtherType.some_method(bool,bool,bool)")]
        [TestCase("//ExFor:OtherType.SomeMethod(long,Int64,System.Int64)", "#ExFor:OtherType.some_method(int,int,int)")]
        [TestCase("//ExFor:OtherType.SomeMethod(ulong,UInt64,System.UInt64)", "#ExFor:OtherType.some_method(int,int,int)")]
        [TestCase("//ExFor:OtherType.SomeMethod(int,Int32,System.Int32)", "#ExFor:OtherType.some_method(int,int,int)")]
        [TestCase("//ExFor:OtherType.SomeMethod(uint,UInt32,System.UInt32)", "#ExFor:OtherType.some_method(int,int,int)")]
        [TestCase("//ExFor:OtherType.SomeMethod(short,Int16,System.Int16)", "#ExFor:OtherType.some_method(int,int,int)")]
        [TestCase("//ExFor:OtherType.SomeMethod(ushort,UInt16,System.UInt16)", "#ExFor:OtherType.some_method(int,int,int)")]
        [TestCase("//ExFor:OtherType.SomeMethod(byte,Byte,System.Byte)", "#ExFor:OtherType.some_method(int,int,int)")]
        [TestCase("//ExFor:OtherType.SomeMethod(sbyte,SByte,System.SByte)", "#ExFor:OtherType.some_method(int,int,int)")]
        [TestCase("//ExFor:OtherType.SomeMethod(byte[],Byte[],System.Byte[])", "#ExFor:OtherType.some_method(bytes,bytes,bytes)")]
        [TestCase("//ExFor:OtherType.SomeMethod(sbyte[],SByte[],System.SByte[])", "#ExFor:OtherType.some_method(bytes,bytes,bytes)")]
        [TestCase("//ExFor:OtherType.SomeMethod(float,Single,System.Single)", "#ExFor:OtherType.some_method(float,float,float)")]
        [TestCase("//ExFor:OtherType.SomeMethod(double,Double,System.Double)", "#ExFor:OtherType.some_method(float,float,float)")]
        [TestCase("//ExFor:OtherType.SomeMethod(decimal,Decimal,System.Decimal)", "#ExFor:OtherType.some_method(float,float,float)")]
        [TestCase("//ExFor:OtherType.SomeMethod(char,Char,System.Char)", "#ExFor:OtherType.some_method(str,str,str)")]
        [TestCase("//ExFor:OtherType.SomeMethod(string,String,System.String)", "#ExFor:OtherType.some_method(str,str,str)")]
        [TestCase("//ExFor:OtherType.SomeMethod(DateTime,System.DateTime)", "#ExFor:OtherType.some_method(datetime,datetime)")]
        [TestCase("//ExFor:OtherType.SomeMethod(object,Object,System.Object)", "#ExFor:OtherType.some_method(object,object,object)")]
        [TestCase("//ExFor:OtherType.SomeMethod(byte[],int[],double[],string[],Document[])", "#ExFor:OtherType.some_method(bytes,List[int],List[float],List[str],List[Document])")]
        [TestCase("//ExFor:CompositeNode.RemoveChild``1(``0)", "#ExFor:CompositeNode.remove_child")]
        [TestCase("//ExFor:CompositeNode.InsertAfter``1(``0, Node)", "#ExFor:CompositeNode.insert_after")]
        [TestCase("//ExFor:CompositeNode.InsertAfter``1(Node, ``0)", "#ExFor:CompositeNode.insert_after")]
        [TestCase("//ExFor:BaseWebExtensionCollection`1.Remove(Int32)", "#ExFor:BaseWebExtensionCollection.remove")]
        [TestCase("//ExFor:OtherType.#ctor", "#ExFor:OtherType.__init__")]
        [TestCase("//ExFor:OtherType.#ctor()", "#ExFor:OtherType.__init__()")]
        [TestCase("//ExFor:OtherType.#ctor(int,string)", "#ExFor:OtherType.__init__(int,str)")]
        [TestCase("//ExFor:OtherType.Item", "#ExFor:OtherType.__getitem__")]
        [TestCase("//ExFor:OtherType.Item(int)", "#ExFor:OtherType.__getitem__(int)")]
        [TestCase("//ExFor:OtherType.GetEnumerator", "#ExFor:OtherType.__iter__")]
        [TestCase("//ExFor:OtherType.Equals", "#ExFor:OtherType.__eq__")]
        [TestCase("//ExFor:OtherType.Equals(Int32)", "#ExFor:OtherType.__eq__(int)")]
        [TestCase("//ExFor:OtherType.GetHashCode", "#ExFor:OtherType.__hash__")]
        [TestCase("//ExFor:OtherType.ToString", "#ExFor:OtherType.__str__")]
        [TestCase("//ExFor:SomeType.SomeProperty", "#ExFor:SomeType.prop666")]
        [TestCase("//ExFor:SomeType.SomeMethod()", "#ExFor:SomeType.do_it999()")]
        [TestCase("//ExFor:SomeType.SomeMethod(int)", "#ExFor:SomeType.do_it999(int)")]
        [TestCase("//ExFor:SomeType.SomeGenericMethod``1()", "#ExFor:SomeType.make_work")]
        [TestCase("//ExFor:SomeType.SomeGenericMethod``1(``0)", "#ExFor:SomeType.make_work")]
        [TestCase("//ExFor:SomeType.SomeGenericMethod``1(``0,int)", "#ExFor:SomeType.make_work")]
        [TestCase("//ExFor: OtherType", "#ExFor:OtherType")]
        public void ProcessComment(String source, String? expected)
        {
            CommentsProcessor commentsProcessor = new CommentsProcessor(_nameTransformer);
            Assert.That(commentsProcessor.Process(source), Is.EqualTo(expected));
        }

        private readonly NameTransformer _nameTransformer;

        private readonly HandmadeNameAliases _handmadeAliases = new HandmadeNameAliases
        {
            Namespaces = new[]
            {
                new NamespaceNameEntry
                {
                    Types = new []
                    {
                        new TypeNameEntry
                        {
                            Members = new []
                            {
                                new MemberAliasMapping{Name = "HRef", Alias="href"},
                                new MemberAliasMapping{Name = "XPath", Alias="xpath"},
                            }
                        },
                        new TypeNameEntry
                        {
                            Condition = new NameConditions{EqualCondition = "SomeType"},
                            Members = new []
                            {
                                new MemberAliasMapping{Name = "SomeProperty", Alias="prop666"},
                                new MemberAliasMapping{Name = "SomeMethod", Alias="do_it999"},
                                new MemberAliasMapping{Name = "SomeGenericMethod", Alias="make_work"}
                            }
                        }
                    }
                }
            }
        };
    }
}
