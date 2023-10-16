## PythonExamplesPorter

### General principles

1. Tests (test methods) are base entities for porting. Test methods are methods which are marked with one of the corresponding attribute (**TestAttribute**, **TestCaseAttribute** etc) and situated in test classes (which are also marked with the corresponding attribute - **TestFixtureAttribute**).
1. All other entities (classes, non-test methods in test classes, etc.) will only be ported if they are directly or indirectly used in tests.
1. We must support of ignoring different objects from porting process: files, test classes, test methods.
1. We must support handmade implementations for different entities: classes, methods etc. For handmade implementations of classes we must support ability of mapping of member's names.
1. We must support handmade implementations of arbitrary pieces of code (within one method).
1. We must support different strategies for entities from different external sources (main library/libraries, .NET, other external libraries). For main library/libraries, we will use entities from this library with some names transformations. For entities from .NET, we will use either corresponding entities from python or these entities directly with some names transformations. For all entities from other external libraries (and for some entities from main library/libraries and .NET), we will report about impossibility of using these entities.
1. If we can't using some constructions/statements or entities, then we will stop porting of the parent test method and generate exception (with description of reason) in it.
1. We will implement this solution according to phases (see below).

### Phase 0

1. We will port only simple test methods (marked by **TestAttribute** attribute), which are situated in the top level test classes (marked by **TestFixtureAttribute** attribute). All other entities (other classes and methods in test classes) we will ignore.
1. We will add infrastructure for processing projects and solutions.
1. We will add infrastructure for processing of all top level test classes and their simple test methods.
1. We will add support of ignoring different objects from porting process: files, test classes, test methods.
1. We will add support of handmade implementation of base classes (for test classes) and ability of mapping names of their members.
1. We will add support of base statements: ```if .. else```, ```switch```, ```for```, ```foreach```, ```while```, ```do … while```, variable declarations, method calls.
1. We will add support of base expressions (which are frequently using).
1. We will add support different strategies for entities from different external sources (main library/libraries, .NET, other external libraries).
1. In the current phase, we won't separate collection of source data and generation of destination data - we will implement all functionality in the AST processing methods.

### Phase 1
1. We will fix technical debt after Phase 0.
1. We will add support of frequently used types/methods from system (.NET) and test (NUnit) libraries.
1. We will create utility for demonstrating difference between ported and existing examples (only for fully ported examples).
1. We will create integration tests.
1. We will add support for tests marked by **TestCase** attribute.
1. We will add infrastructure for processing single files.
1. We will add support of some other statements: ```try … catch```, ```try … finally```, ```using``` etc.
1. We will add support of some advanced expressions (which we use periodically): increment/decrement, assignment with modifications, string interpolation etc.
1. We will add support of constructors, methods, properties and fields in the top level test classes (we don't support overloading in constructors and methods).
1. We will add support of other classes/structures (non top level test classes) and inheritance (without support of interfaces).

### Phase 2
1. We will add infrastructure for processing pieces of code.
1. We will add support of periodically and rarely used types/methods from system (.NET) and test (NUnit) libraries.
1. We will add support of handmade classes.
1. We will add support of handmade methods.
1. We will add support for handmade pieces of code.
1. We will add processing of comments.
1. We will add processing of lambda expressions.
1. We will add support of some advanced expressions, which we use rarely or nothing in examples (now).
1. We will investigate ability of using intermediate code (for simplification of possible usage for examples on other languages).

### Phase 3
**Under construction**