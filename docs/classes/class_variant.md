github_url
:   hide

# Variant {#class_Variant}

The most important data type in Godot.

::: rst-class
classref-introduction-group
:::

## Description

In computer programming, a Variant class is a class that is designed to
store a variety of other types. Dynamic programming languages like PHP,
Lua, JavaScript and GDScript like to use them to store variables\' data
on the backend. With these Variants, properties are able to change value
types freely.

::::: tabs
::: code-tab
gdscript

var foo = 2 \# foo is dynamically an integer foo = \"Now foo is a
string!\" foo = RefCounted.new() \# foo is an Object var bar: int = 2 \#
bar is a statically typed integer. \# bar = \"Uh oh! I can\'t make
statically typed variables become a different type!\"
:::

::: code-tab
csharp

// C# is statically typed. Once a variable has a type it cannot be
changed. You can use the [var]{.title-ref} keyword to let the compiler
infer the type automatically. var foo = 2; // Foo is a 32-bit integer
(int). Be cautious, integers in GDScript are 64-bit and the direct C#
equivalent is [long]{.title-ref}. // foo = \"foo was and will always be
an integer. It cannot be turned into a string!\"; var boo = \"Boo is a
string!\"; var ref = new RefCounted(); // var is especially useful when
used together with a constructor.

// Godot also provides a Variant type that works like a union of all the
Variant-compatible types. Variant fooVar = 2; // fooVar is dynamically
an integer (stored as a [long]{.title-ref} in the Variant type). fooVar
= \"Now fooVar is a string!\"; fooVar = new RefCounted(); // fooVar is a
GodotObject.
:::
:::::

Godot tracks all scripting API variables within Variants. Without even
realizing it, you use Variants all the time. When a particular language
enforces its own rules for keeping data typed, then that language is
applying its own custom logic over the base Variant scripting API.

- GDScript automatically wrap values in them. It keeps all data in plain
  Variants by default and then optionally enforces custom static typing
  rules on variable types.
- C# is statically typed, but uses its own implementation of the Variant
  type in place of Godot\'s **Variant** class when it needs to represent
  a dynamic value. C# Variant can be assigned any compatible type
  implicitly but converting requires an explicit cast.

The global
`@GlobalScope.typeof()<class_@GlobalScope_method_typeof>`{.interpreted-text
role="ref"} function returns the enumerated value of the Variant type
stored in the current variable (see
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"}).

::::: tabs
::: code-tab
gdscript

var foo = 2 match typeof(foo): TYPE_NIL: print(\"foo is null\")
TYPE_INT: print(\"foo is an integer\") TYPE_OBJECT: \# Note that Objects
are their own special category. \# To get the name of the underlying
Object type, you need the [get_class()]{.title-ref} method. print(\"foo
is a(n) %s\" % foo.get_class()) \# inject the class name into a
formatted string. \# Note that this does not get the script\'s
[class_name]{.title-ref} global identifier. \# If the
[class_name]{.title-ref} is needed, use
[foo.get_script().get_global_name()]{.title-ref} instead.
:::

::: code-tab
csharp

Variant foo = 2; switch (foo.VariantType) { case Variant.Type.Nil:
GD.Print(\"foo is null\"); break; case Variant.Type.Int: GD.Print(\"foo
is an integer\"); break; case Variant.Type.Object: // Note that Objects
are their own special category. // You can convert a Variant to a
GodotObject and use reflection to get its name. GD.Print(\$\"foo is a(n)
{foo.AsGodotObject().GetType().Name}\"); break; }
:::
:::::

A Variant takes up only 20 bytes and can store almost any engine
datatype inside of it. Variants are rarely used to hold information for
long periods of time. Instead, they are used mainly for communication,
editing, serialization and moving data around.

Godot has specifically invested in making its Variant class as flexible
as possible; so much so that it is used for a multitude of operations to
facilitate communication between all of Godot\'s systems.

A Variant:

- Can store almost any datatype.
- Can perform operations between many variants. GDScript uses Variant as
  its atomic/native datatype.
- Can be hashed, so it can be compared quickly to other variants.
- Can be used to convert safely between datatypes.
- Can be used to abstract calling methods and their arguments. Godot
  exports all its functions through variants.
- Can be used to defer calls or move data between threads.
- Can be serialized as binary and stored to disk, or transferred via
  network.
- Can be serialized to text and use it for printing values and editable
  settings.
- Can work as an exported property, so the editor can edit it
  universally.
- Can be used for dictionaries, arrays, parsers, etc.

\*\*Containers (Array and Dictionary):\*\* Both are implemented using
variants. A `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
can match any datatype used as key to any other datatype. An
`Array<class_Array>`{.interpreted-text role="ref"} just holds an array
of Variants. Of course, a Variant can also hold a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} and an
`Array<class_Array>`{.interpreted-text role="ref"} inside, making it
even more flexible.

Modifications to a container will modify all references to it. A
`Mutex<class_Mutex>`{.interpreted-text role="ref"} should be created to
lock it if multi-threaded access is desired.

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Variant class introduction <../contributing/development/core_and_modules/variant_class>`{.interpreted-text
  role="doc"}
