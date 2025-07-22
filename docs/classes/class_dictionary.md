github_url
:   hide

# Dictionary {#class_Dictionary}

A built-in data structure that holds key-value pairs.

::: rst-class
classref-introduction-group
:::

## Description

Dictionaries are associative containers that contain values referenced
by unique keys. Dictionaries will preserve the insertion order when
adding new entries. In other programming languages, this data structure
is often referred to as a hash map or an associative array.

You can define a dictionary by placing a comma-separated list of
`key: value` pairs inside curly braces `{}`.

Creating a dictionary:

::::: tabs
::: code-tab
gdscript

var my_dict = {} \# Creates an empty dictionary.

var dict_variable_key = \"Another key name\" var dict_variable_value =
\"value2\" var another_dict = { \"Some key name\": \"value1\",
dict_variable_key: dict_variable_value, }

var points_dict = { \"White\": 50, \"Yellow\": 75, \"Orange\": 100 }

\# Alternative Lua-style syntax. \# Doesn\'t require quotes around keys,
but only string constants can be used as key names. \# Additionally, key
names must start with a letter or an underscore. \# Here,
[some_key]{.title-ref} is a string literal, not a variable! another_dict
= { some_key = 42, }
:::

::: code-tab
csharp

var myDict = new Godot.Collections.Dictionary(); // Creates an empty
dictionary. var pointsDict = new Godot.Collections.Dictionary { {
\"White\", 50 }, { \"Yellow\", 75 }, { \"Orange\", 100 }, };
:::
:::::

You can access a dictionary\'s value by referencing its corresponding
key. In the above example, `points_dict["White"]` will return `50`. You
can also write `points_dict.White`, which is equivalent. However,
you\'ll have to use the bracket syntax if the key you\'re accessing the
dictionary with isn\'t a fixed string (such as a number or variable).

::::: tabs
::: code-tab
gdscript

\@export_enum(\"White\", \"Yellow\", \"Orange\") var my_color: String
var points_dict = { \"White\": 50, \"Yellow\": 75, \"Orange\": 100 }
func [ready]{#ready}(): \# We can\'t use dot syntax here as
[my_color]{.title-ref} is a variable. var points =
points_dict\[my_color\]
:::

::: code-tab
csharp

\[Export(PropertyHint.Enum, \"White,Yellow,Orange\")\] public string
MyColor { get; set; } private Godot.Collections.Dictionary
[pointsDict]{#pointsdict} = new Godot.Collections.Dictionary { {
\"White\", 50 }, { \"Yellow\", 75 }, { \"Orange\", 100 }, };

public override void [Ready]{#ready}() { int points =
(int)\_pointsDict\[MyColor\]; }
:::
:::::

In the above code, `points` will be assigned the value that is paired
with the appropriate color selected in `my_color`.

Dictionaries can contain more complex data:

::::: tabs
::: code-tab
gdscript

var my_dict = {

:   \"First Array\": \[1, 2, 3, 4\] \# Assigns an Array to a String key.

}
:::

::: code-tab
csharp

var myDict = new Godot.Collections.Dictionary { { \"First Array\", new
Godot.Collections.Array { 1, 2, 3, 4 } } };
:::
:::::

To add a key to an existing dictionary, access it like an existing key
and assign to it:

::::: tabs
::: code-tab
gdscript

var points_dict = { \"White\": 50, \"Yellow\": 75, \"Orange\": 100 }
points_dict\[\"Blue\"\] = 150 \# Add \"Blue\" as a key and assign 150 as
its value.
:::

::: code-tab
csharp

var pointsDict = new Godot.Collections.Dictionary { { \"White\", 50 }, {
\"Yellow\", 75 }, { \"Orange\", 100 }, }; pointsDict\[\"Blue\"\] = 150;
// Add \"Blue\" as a key and assign 150 as its value.
:::
:::::

Finally, dictionaries can contain different types of keys and values in
the same dictionary:

::::: tabs
::: code-tab
gdscript

\# This is a valid dictionary. \# To access the string \"Nested value\"
below, use [my_dict.sub_dict.sub_key]{.title-ref} or
[my_dict\[\"sub_dict\"\]\[\"sub_key\"\]]{.title-ref}. \# Indexing styles
can be mixed and matched depending on your needs. var my_dict = {
\"String Key\": 5, 4: \[1, 2, 3\], 7: \"Hello\", \"sub_dict\": {
\"sub_key\": \"Nested value\" }, }
:::

::: code-tab
csharp

// This is a valid dictionary. // To access the string \"Nested value\"
below, use
[((Godot.Collections.Dictionary)myDict\[\"sub_dict\"\])\[\"sub_key\"\]]{.title-ref}.
var myDict = new Godot.Collections.Dictionary { { \"String Key\", 5 }, {
4, new Godot.Collections.Array { 1, 2, 3 } }, { 7, \"Hello\" }, {
\"sub_dict\", new Godot.Collections.Dictionary { { \"sub_key\", \"Nested
value\" } } }, };
:::
:::::

The keys of a dictionary can be iterated with the `for` keyword:

::::: tabs
::: code-tab
gdscript

var groceries = { \"Orange\": 20, \"Apple\": 2, \"Banana\": 4 } for
fruit in groceries: var amount = groceries\[fruit\]
:::

::: code-tab
csharp

var groceries = new Godot.Collections.Dictionary { { \"Orange\", 20 }, {
\"Apple\", 2 }, { \"Banana\", 4 } }; foreach (var (fruit, amount) in
groceries) { // [fruit]{.title-ref} is the key, [amount]{.title-ref} is
the value. }
:::
:::::

\*\*Note:\*\* Dictionaries are always passed by reference. To get a copy
of a dictionary which can be modified independently of the original
dictionary, use
`duplicate()<class_Dictionary_method_duplicate>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Erasing elements while iterating over dictionaries is
**not** supported and will result in unpredictable behavior.

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

- [GDScript basics:
  Dictionary](../tutorials/scripting/gdscript/gdscript_basics.html#dictionary)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)
- [Operating System Testing
  Demo](https://godotengine.org/asset-library/asset/2789)

::: rst-class
classref-reftable-group
:::

## Constructors

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Operators

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Dictionary_constructor_Dictionary}
::: rst-class
classref-constructor
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**Dictionary**()
`🔗<class_Dictionary_constructor_Dictionary>`{.interpreted-text
role="ref"}

Constructs an empty **Dictionary**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**Dictionary**(base: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, key_type: `int<class_int>`{.interpreted-text role="ref"},
key_class_name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, key_script: `Variant<class_Variant>`{.interpreted-text
role="ref"}, value_type: `int<class_int>`{.interpreted-text role="ref"},
value_class_name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value_script: `Variant<class_Variant>`{.interpreted-text
role="ref"})

Creates a typed dictionary from the `base` dictionary. A typed
dictionary can only contain keys and values of the given types, or that
inherit from the given classes, as described by this constructor\'s
parameters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**Dictionary**(from: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"})

Returns the same dictionary as `from`. If you need a copy of the
dictionary, use
`duplicate()<class_Dictionary_method_duplicate>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Dictionary_method_assign}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**assign**(dictionary: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}) `🔗<class_Dictionary_method_assign>`{.interpreted-text
role="ref"}

Assigns elements of another `dictionary` into the dictionary. Resizes
the dictionary to match `dictionary`. Performs type conversions if the
dictionary is typed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_Dictionary_method_clear>`{.interpreted-text role="ref"}

Clears the dictionary, removing all entries from it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_duplicate}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**duplicate**(deep: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_duplicate>`{.interpreted-text
role="ref"}

Returns a new copy of the dictionary.

By default, a **shallow** copy is returned: all nested
`Array<class_Array>`{.interpreted-text role="ref"}, **Dictionary**, and
`Resource<class_Resource>`{.interpreted-text role="ref"} keys and values
are shared with the original dictionary. Modifying any of those in one
dictionary will also affect them in the other.

If `deep` is `true`, a **deep** copy is returned: all nested arrays and
dictionaries are also duplicated (recursively). Any
`Resource<class_Resource>`{.interpreted-text role="ref"} is still shared
with the original dictionary, though.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_duplicate_deep}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**duplicate_deep**(deep_subresources_mode:
`int<class_int>`{.interpreted-text role="ref"} = 1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_duplicate_deep>`{.interpreted-text
role="ref"}

Duplicates this dictionary, deeply, like
`duplicate()<class_Dictionary_method_duplicate>`{.interpreted-text
role="ref"}`(true)`, with extra control over how subresources are
handled.

`deep_subresources_mode` must be one of the values from
`DeepDuplicateMode<enum_Resource_DeepDuplicateMode>`{.interpreted-text
role="ref"}. By default, only internal resources will be duplicated
(recursively).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_erase}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **erase**(key:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Dictionary_method_erase>`{.interpreted-text role="ref"}

Removes the dictionary entry by key, if it exists. Returns `true` if the
given `key` existed in the dictionary, otherwise `false`.

\*\*Note:\*\* Do not erase entries while iterating over the dictionary.
You can iterate over the
`keys()<class_Dictionary_method_keys>`{.interpreted-text role="ref"}
array instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_find_key}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**find_key**(value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_find_key>`{.interpreted-text
role="ref"}

Finds and returns the first key whose associated value is equal to
`value`, or `null` if it is not found.

\*\*Note:\*\* `null` is also a valid key. If inside the dictionary,
`find_key()<class_Dictionary_method_find_key>`{.interpreted-text
role="ref"} may give misleading results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_get}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **get**(key:
`Variant<class_Variant>`{.interpreted-text role="ref"}, default:
`Variant<class_Variant>`{.interpreted-text role="ref"} = null)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_get>`{.interpreted-text
role="ref"}

Returns the corresponding value for the given `key` in the dictionary.
If the `key` does not exist, returns `default`, or `null` if the
parameter is omitted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_get_or_add}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_or_add**(key: `Variant<class_Variant>`{.interpreted-text
role="ref"}, default: `Variant<class_Variant>`{.interpreted-text
role="ref"} = null)
`🔗<class_Dictionary_method_get_or_add>`{.interpreted-text role="ref"}

Gets a value and ensures the key is set. If the `key` exists in the
dictionary, this behaves like
`get()<class_Dictionary_method_get>`{.interpreted-text role="ref"}.
Otherwise, the `default` value is inserted into the dictionary and
returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_get_typed_key_builtin}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_typed_key_builtin**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_get_typed_key_builtin>`{.interpreted-text
role="ref"}

Returns the built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type of the typed dictionary\'s keys as a
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} constant. If the keys are not typed, returns
`@GlobalScope.TYPE_NIL<class_@GlobalScope_constant_TYPE_NIL>`{.interpreted-text
role="ref"}. See also
`is_typed_key()<class_Dictionary_method_is_typed_key>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_get_typed_key_class_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_typed_key_class_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_get_typed_key_class_name>`{.interpreted-text
role="ref"}

Returns the **built-in** class name of the typed dictionary\'s keys, if
the built-in `Variant<class_Variant>`{.interpreted-text role="ref"} type
is
`@GlobalScope.TYPE_OBJECT<class_@GlobalScope_constant_TYPE_OBJECT>`{.interpreted-text
role="ref"}. Otherwise, returns an empty
`StringName<class_StringName>`{.interpreted-text role="ref"}. See also
`is_typed_key()<class_Dictionary_method_is_typed_key>`{.interpreted-text
role="ref"} and
`Object.get_class()<class_Object_method_get_class>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_get_typed_key_script}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_typed_key_script**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_get_typed_key_script>`{.interpreted-text
role="ref"}

Returns the `Script<class_Script>`{.interpreted-text role="ref"}
instance associated with this typed dictionary\'s keys, or `null` if it
does not exist. See also
`is_typed_key()<class_Dictionary_method_is_typed_key>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_get_typed_value_builtin}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_typed_value_builtin**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_get_typed_value_builtin>`{.interpreted-text
role="ref"}

Returns the built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type of the typed dictionary\'s values as a
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} constant. If the values are not typed, returns
`@GlobalScope.TYPE_NIL<class_@GlobalScope_constant_TYPE_NIL>`{.interpreted-text
role="ref"}. See also
`is_typed_value()<class_Dictionary_method_is_typed_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_get_typed_value_class_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_typed_value_class_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_get_typed_value_class_name>`{.interpreted-text
role="ref"}

Returns the **built-in** class name of the typed dictionary\'s values,
if the built-in `Variant<class_Variant>`{.interpreted-text role="ref"}
type is
`@GlobalScope.TYPE_OBJECT<class_@GlobalScope_constant_TYPE_OBJECT>`{.interpreted-text
role="ref"}. Otherwise, returns an empty
`StringName<class_StringName>`{.interpreted-text role="ref"}. See also
`is_typed_value()<class_Dictionary_method_is_typed_value>`{.interpreted-text
role="ref"} and
`Object.get_class()<class_Object_method_get_class>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_get_typed_value_script}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_typed_value_script**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_get_typed_value_script>`{.interpreted-text
role="ref"}

Returns the `Script<class_Script>`{.interpreted-text role="ref"}
instance associated with this typed dictionary\'s values, or `null` if
it does not exist. See also
`is_typed_value()<class_Dictionary_method_is_typed_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_has}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has**(key:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_has>`{.interpreted-text
role="ref"}

Returns `true` if the dictionary contains an entry with the given `key`.

::::: tabs
::: code-tab
gdscript

var my_dict = {

:   \"Godot\" : 4, 210 : null,

}

print(my_dict.has(\"Godot\")) \# Prints true print(my_dict.has(210)) \#
Prints true print(my_dict.has(4)) \# Prints false
:::

::: code-tab
csharp

var myDict = new Godot.Collections.Dictionary { { \"Godot\", 4 }, { 210,
default }, };

GD.Print(myDict.ContainsKey(\"Godot\")); // Prints True
GD.Print(myDict.ContainsKey(210)); // Prints True
GD.Print(myDict.ContainsKey(4)); // Prints False
:::
:::::

In GDScript, this is equivalent to the `in` operator:

    if "Godot" in { "Godot": 4 }:
        print("The key is here!") # Will be printed.

\*\*Note:\*\* This method returns `true` as long as the `key` exists,
even if its corresponding value is `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_has_all}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_all**(keys:
`Array<class_Array>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_has_all>`{.interpreted-text
role="ref"}

Returns `true` if the dictionary contains all keys in the given `keys`
array.

    var data = { "width": 10, "height": 20 }
    data.has_all(["height", "width"]) # Returns true

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_hash}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hash**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_hash>`{.interpreted-text
role="ref"}

Returns a hashed 32-bit integer value representing the dictionary
contents.

::::: tabs
::: code-tab
gdscript

var dict1 = { \"A\": 10, \"B\": 2 } var dict2 = { \"A\": 10, \"B\": 2 }

print(dict1.hash() == dict2.hash()) \# Prints true
:::

::: code-tab
csharp

var dict1 = new Godot.Collections.Dictionary { { \"A\", 10 }, { \"B\", 2
} }; var dict2 = new Godot.Collections.Dictionary { { \"A\", 10 }, {
\"B\", 2 } };

// Godot.Collections.Dictionary has no Hash() method. Use GD.Hash()
instead. GD.Print(GD.Hash(dict1) == GD.Hash(dict2)); // Prints True
:::
:::::

\*\*Note:\*\* Dictionaries with the same entries but in a different
order will not have the same hash.

\*\*Note:\*\* Dictionaries with equal hash values are *not* guaranteed
to be the same, because of hash collisions. On the contrary,
dictionaries with different hash values are guaranteed to be different.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the dictionary is empty (its size is `0`). See also
`size()<class_Dictionary_method_size>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_is_read_only}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_read_only**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_is_read_only>`{.interpreted-text role="ref"}

Returns `true` if the dictionary is read-only. See
`make_read_only()<class_Dictionary_method_make_read_only>`{.interpreted-text
role="ref"}. Dictionaries are automatically read-only if declared with
`const` keyword.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_is_same_typed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_same_typed**(dictionary:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_is_same_typed>`{.interpreted-text
role="ref"}

Returns `true` if the dictionary is typed the same as `dictionary`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_is_same_typed_key}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_same_typed_key**(dictionary:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_is_same_typed_key>`{.interpreted-text
role="ref"}

Returns `true` if the dictionary\'s keys are typed the same as
`dictionary`\'s keys.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_is_same_typed_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_same_typed_value**(dictionary:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_is_same_typed_value>`{.interpreted-text
role="ref"}

Returns `true` if the dictionary\'s values are typed the same as
`dictionary`\'s values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_is_typed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_typed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_is_typed>`{.interpreted-text
role="ref"}

Returns `true` if the dictionary is typed. Typed dictionaries can only
store keys/values of their associated type and provide type safety for
the `[]` operator. Methods of typed dictionary still return
`Variant<class_Variant>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_is_typed_key}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_typed_key**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_is_typed_key>`{.interpreted-text role="ref"}

Returns `true` if the dictionary\'s keys are typed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_is_typed_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_typed_value**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_is_typed_value>`{.interpreted-text
role="ref"}

Returns `true` if the dictionary\'s values are typed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_keys}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **keys**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_keys>`{.interpreted-text
role="ref"}

Returns the list of keys in the dictionary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_make_read_only}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_read_only**()
`🔗<class_Dictionary_method_make_read_only>`{.interpreted-text
role="ref"}

Makes the dictionary read-only, i.e. disables modification of the
dictionary\'s contents. Does not apply to nested content, e.g. content
of nested dictionaries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_merge}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**merge**(dictionary: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, overwrite: `bool<class_bool>`{.interpreted-text role="ref"}
= false) `🔗<class_Dictionary_method_merge>`{.interpreted-text
role="ref"}

Adds entries from `dictionary` to this dictionary. By default, duplicate
keys are not copied over, unless `overwrite` is `true`.

::::: tabs
::: code-tab
gdscript

var dict = { \"item\": \"sword\", \"quantity\": 2 } var other_dict = {
\"quantity\": 15, \"color\": \"silver\" }

\# Overwriting of existing keys is disabled by default.
dict.merge(other_dict) print(dict) \# { \"item\": \"sword\",
\"quantity\": 2, \"color\": \"silver\" }

\# With overwriting of existing keys enabled. dict.merge(other_dict,
true) print(dict) \# { \"item\": \"sword\", \"quantity\": 15, \"color\":
\"silver\" }
:::

::: code-tab
csharp

var dict = new Godot.Collections.Dictionary { \[\"item\"\] = \"sword\",
\[\"quantity\"\] = 2, };

var otherDict = new Godot.Collections.Dictionary { \[\"quantity\"\] =
15, \[\"color\"\] = \"silver\", };

// Overwriting of existing keys is disabled by default.
dict.Merge(otherDict); GD.Print(dict); // { \"item\": \"sword\",
\"quantity\": 2, \"color\": \"silver\" }

// With overwriting of existing keys enabled. dict.Merge(otherDict,
true); GD.Print(dict); // { \"item\": \"sword\", \"quantity\": 15,
\"color\": \"silver\" }
:::
:::::

\*\*Note:\*\* `merge()<class_Dictionary_method_merge>`{.interpreted-text
role="ref"} is *not* recursive. Nested dictionaries are considered as
keys that can be overwritten or not depending on the value of
`overwrite`, but they will never be merged together.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_merged}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**merged**(dictionary: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, overwrite: `bool<class_bool>`{.interpreted-text role="ref"}
= false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_merged>`{.interpreted-text
role="ref"}

Returns a copy of this dictionary merged with the other `dictionary`. By
default, duplicate keys are not copied over, unless `overwrite` is
`true`. See also
`merge()<class_Dictionary_method_merge>`{.interpreted-text role="ref"}.

This method is useful for quickly making dictionaries with default
values:

    var base = { "fruit": "apple", "vegetable": "potato" }
    var extra = { "fruit": "orange", "dressing": "vinegar" }
    # Prints { "fruit": "orange", "vegetable": "potato", "dressing": "vinegar" }
    print(extra.merged(base))
    # Prints { "fruit": "apple", "vegetable": "potato", "dressing": "vinegar" }
    print(extra.merged(base, true))

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_recursive_equal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**recursive_equal**(dictionary:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"},
recursion_count: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Dictionary_method_recursive_equal>`{.interpreted-text
role="ref"}

Returns `true` if the two dictionaries contain the same keys and values,
inner **Dictionary** and `Array<class_Array>`{.interpreted-text
role="ref"} keys and values are compared recursively.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_set}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **set**(key:
`Variant<class_Variant>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Dictionary_method_set>`{.interpreted-text role="ref"}

Sets the value of the element at the given `key` to the given `value`.
This is the same as using the `[]` operator (`array[index] = value`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_size>`{.interpreted-text
role="ref"}

Returns the number of entries in the dictionary. Empty dictionaries
(`{ }`) always return `0`. See also
`is_empty()<class_Dictionary_method_is_empty>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_sort}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **sort**()
`🔗<class_Dictionary_method_sort>`{.interpreted-text role="ref"}

Sorts the dictionary in ascending order, by key. The final order is
dependent on the \"less than\" (`<`) comparison between keys.

:::: tabs
::: code-tab
gdscript

var numbers = { \"c\": 2, \"a\": 0, \"b\": 1 } numbers.sort()
print(numbers) \# Prints { \"a\": 0, \"b\": 1, \"c\": 2 }
:::
::::

This method ensures that the dictionary\'s entries are ordered
consistently when
`keys()<class_Dictionary_method_keys>`{.interpreted-text role="ref"} or
`values()<class_Dictionary_method_values>`{.interpreted-text role="ref"}
are called, or when the dictionary needs to be converted to a string
through
`@GlobalScope.str()<class_@GlobalScope_method_str>`{.interpreted-text
role="ref"} or
`JSON.stringify()<class_JSON_method_stringify>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_method_values}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **values**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Dictionary_method_values>`{.interpreted-text
role="ref"}

Returns the list of values in this dictionary.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Dictionary_operator_neq_Dictionary}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_Dictionary_operator_neq_Dictionary>`{.interpreted-text
role="ref"}

Returns `true` if the two dictionaries do not contain the same keys and
values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_operator_eq_Dictionary}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_Dictionary_operator_eq_Dictionary>`{.interpreted-text
role="ref"}

Returns `true` if the two dictionaries contain the same keys and values.
The order of the entries does not matter.

\*\*Note:\*\* In C#, by convention, this operator compares by
**reference**. If you need to compare by value, iterate over both
dictionaries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Dictionary_operator_idx_Variant}
::: rst-class
classref-operator
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **operator
\[\]**(key: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Dictionary_operator_idx_Variant>`{.interpreted-text
role="ref"}

Returns the corresponding value for the given `key` in the dictionary.
If the entry does not exist, fails and returns `null`. For safe access,
use `get()<class_Dictionary_method_get>`{.interpreted-text role="ref"}
or `has()<class_Dictionary_method_has>`{.interpreted-text role="ref"}.
