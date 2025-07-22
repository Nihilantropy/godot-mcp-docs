github_url
:   hide

# String {#class_String}

A built-in type for strings.

::: rst-class
classref-introduction-group
:::

## Description

This is the built-in string Variant type (and the one used by GDScript).
Strings may contain any number of Unicode characters, and expose methods
useful for manipulating and generating strings. Strings are
reference-counted and use a copy-on-write approach (every modification
to a string returns a new **String**), so passing them around is cheap
in resources.

Some string methods have corresponding variations. Variations suffixed
with `n` (`countn()<class_String_method_countn>`{.interpreted-text
role="ref"}, `findn()<class_String_method_findn>`{.interpreted-text
role="ref"},
`replacen()<class_String_method_replacen>`{.interpreted-text
role="ref"}, etc.) are **case-insensitive** (they make no distinction
between uppercase and lowercase letters). Method variations prefixed
with `r` (`rfind()<class_String_method_rfind>`{.interpreted-text
role="ref"}, `rsplit()<class_String_method_rsplit>`{.interpreted-text
role="ref"}, etc.) are reversed, and start from the end of the string,
instead of the beginning.

To convert any `Variant<class_Variant>`{.interpreted-text role="ref"} to
or from a string, see
`@GlobalScope.str()<class_@GlobalScope_method_str>`{.interpreted-text
role="ref"},
`@GlobalScope.str_to_var()<class_@GlobalScope_method_str_to_var>`{.interpreted-text
role="ref"}, and
`@GlobalScope.var_to_str()<class_@GlobalScope_method_var_to_str>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In a boolean context, a string will evaluate to `false` if
it is empty (`""`). Otherwise, a string will always evaluate to `true`.

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

- `GDScript format strings <../tutorials/scripting/gdscript/gdscript_format_string>`{.interpreted-text
  role="doc"}

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

:::: {#class_String_constructor_String}
::: rst-class
classref-constructor
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **String**()
`🔗<class_String_constructor_String>`{.interpreted-text role="ref"}

Constructs an empty **String** (`""`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`String<class_String>`{.interpreted-text role="ref"} **String**(from:
`String<class_String>`{.interpreted-text role="ref"})

Constructs a **String** as a copy of the given **String**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`String<class_String>`{.interpreted-text role="ref"} **String**(from:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})

Constructs a new **String** from the given
`NodePath<class_NodePath>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`String<class_String>`{.interpreted-text role="ref"} **String**(from:
`StringName<class_StringName>`{.interpreted-text role="ref"})

Constructs a new **String** from the given
`StringName<class_StringName>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_String_method_begins_with}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **begins_with**(text:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_begins_with>`{.interpreted-text
role="ref"}

Returns `true` if the string begins with the given `text`. See also
`ends_with()<class_String_method_ends_with>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_bigrams}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **bigrams**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_bigrams>`{.interpreted-text
role="ref"}

Returns an array containing the bigrams (pairs of consecutive
characters) of this string.

    print("Get up!".bigrams()) # Prints ["Ge", "et", "t ", " u", "up", "p!"]

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_bin_to_int}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bin_to_int**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_bin_to_int>`{.interpreted-text
role="ref"}

Converts the string representing a binary number into an
`int<class_int>`{.interpreted-text role="ref"}. The string may
optionally be prefixed with `"0b"`, and an additional `-` prefix for
negative numbers.

::::: tabs
::: code-tab
gdscript

print(\"101\".bin_to_int()) \# Prints 5 print(\"0b101\".bin_to_int()) \#
Prints 5 print(\"-0b10\".bin_to_int()) \# Prints -2
:::

::: code-tab
csharp

GD.Print(\"101\".BinToInt()); // Prints 5
GD.Print(\"0b101\".BinToInt()); // Prints 5
GD.Print(\"-0b10\".BinToInt()); // Prints -2
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_c_escape}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **c_escape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_c_escape>`{.interpreted-text
role="ref"}

Returns a copy of the string with special characters escaped using the C
language standard.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_c_unescape}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **c_unescape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_c_unescape>`{.interpreted-text
role="ref"}

Returns a copy of the string with escaped characters replaced by their
meanings. Supported escape sequences are `\'`, `\"`, `\\`, `\a`, `\b`,
`\f`, `\n`, `\r`, `\t`, `\v`.

\*\*Note:\*\* Unlike the GDScript parser, this method doesn\'t support
the `\uXXXX` escape sequence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_capitalize}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **capitalize**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_capitalize>`{.interpreted-text
role="ref"}

Changes the appearance of the string: replaces underscores (`_`) with
spaces, adds spaces before uppercase letters in the middle of a word,
converts all letters to lowercase, then converts the first one and each
one following a space to uppercase.

::::: tabs
::: code-tab
gdscript

\"move_local_x\".capitalize() \# Returns \"Move Local X\"
\"sceneFile_path\".capitalize() \# Returns \"Scene File Path\" \"2D,
FPS, PNG\".capitalize() \# Returns \"2d, Fps, Png\"
:::

::: code-tab
csharp

\"move_local_x\".Capitalize(); // Returns \"Move Local X\"
\"sceneFile_path\".Capitalize(); // Returns \"Scene File Path\" \"2D,
FPS, PNG\".Capitalize(); // Returns \"2d, Fps, Png\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_casecmp_to}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **casecmp_to**(to:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_casecmp_to>`{.interpreted-text
role="ref"}

Performs a case-sensitive comparison to another string. Returns `-1` if
less than, `1` if greater than, or `0` if equal. \"Less than\" and
\"greater than\" are determined by the [Unicode code
points](https://en.wikipedia.org/wiki/List_of_Unicode_characters) of
each string, which roughly matches the alphabetical order.

If the character comparison reaches the end of one string, but the other
string contains more characters, then it will use length as the deciding
factor: `1` will be returned if this string is longer than the `to`
string, or `-1` if shorter. Note that the length of empty strings is
always `0`.

To get a `bool<class_bool>`{.interpreted-text role="ref"} result from a
string comparison, use the `==` operator instead. See also
`nocasecmp_to()<class_String_method_nocasecmp_to>`{.interpreted-text
role="ref"},
`filecasecmp_to()<class_String_method_filecasecmp_to>`{.interpreted-text
role="ref"}, and
`naturalcasecmp_to()<class_String_method_naturalcasecmp_to>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_chr}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **chr**(code:
`int<class_int>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_chr>`{.interpreted-text role="ref"}

Returns a single Unicode character from the integer `code`. You may use
[unicodelookup.com](https://unicodelookup.com/) or
[unicode.org](https://www.unicode.org/charts/) as points of reference.

    print(String.chr(65))     # Prints "A"
    print(String.chr(129302)) # Prints "🤖" (robot face emoji)

See also
`unicode_at()<class_String_method_unicode_at>`{.interpreted-text
role="ref"},
`@GDScript.char()<class_@GDScript_method_char>`{.interpreted-text
role="ref"}, and
`@GDScript.ord()<class_@GDScript_method_ord>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_contains}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **contains**(what:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_contains>`{.interpreted-text
role="ref"}

Returns `true` if the string contains `what`. In GDScript, this
corresponds to the `in` operator.

::::: tabs
::: code-tab
gdscript

print(\"Node\".contains(\"de\")) \# Prints true
print(\"team\".contains(\"I\")) \# Prints false print(\"I\" in \"team\")
\# Prints false
:::

::: code-tab
csharp

GD.Print(\"Node\".Contains(\"de\")); // Prints True
GD.Print(\"team\".Contains(\"I\")); // Prints False
:::
:::::

If you need to know where `what` is within the string, use
`find()<class_String_method_find>`{.interpreted-text role="ref"}. See
also `containsn()<class_String_method_containsn>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_containsn}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **containsn**(what:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_containsn>`{.interpreted-text
role="ref"}

Returns `true` if the string contains `what`, **ignoring case**.

If you need to know where `what` is within the string, use
`findn()<class_String_method_findn>`{.interpreted-text role="ref"}. See
also `contains()<class_String_method_contains>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **count**(what:
`String<class_String>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0, to:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_count>`{.interpreted-text
role="ref"}

Returns the number of occurrences of the substring `what` between `from`
and `to` positions. If `to` is 0, the search continues until the end of
the string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_countn}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **countn**(what:
`String<class_String>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0, to:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_countn>`{.interpreted-text
role="ref"}

Returns the number of occurrences of the substring `what` between `from`
and `to` positions, **ignoring case**. If `to` is 0, the search
continues until the end of the string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_dedent}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **dedent**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_dedent>`{.interpreted-text
role="ref"}

Returns a copy of the string with indentation (leading tabs and spaces)
removed. See also
`indent()<class_String_method_indent>`{.interpreted-text role="ref"} to
add indentation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_ends_with}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ends_with**(text:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_ends_with>`{.interpreted-text
role="ref"}

Returns `true` if the string ends with the given `text`. See also
`begins_with()<class_String_method_begins_with>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_erase}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **erase**(position:
`int<class_int>`{.interpreted-text role="ref"}, chars:
`int<class_int>`{.interpreted-text role="ref"} = 1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_erase>`{.interpreted-text
role="ref"}

Returns a string with `chars` characters erased starting from
`position`. If `chars` goes beyond the string\'s length given the
specified `position`, fewer characters will be erased from the returned
string. Returns an empty string if either `position` or `chars` is
negative. Returns the original string unmodified if `chars` is `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_filecasecmp_to}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **filecasecmp_to**(to:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_filecasecmp_to>`{.interpreted-text
role="ref"}

Like
`naturalcasecmp_to()<class_String_method_naturalcasecmp_to>`{.interpreted-text
role="ref"} but prioritizes strings that begin with periods (`.`) and
underscores (`_`) before any other character. Useful when sorting
folders or file names.

To get a `bool<class_bool>`{.interpreted-text role="ref"} result from a
string comparison, use the `==` operator instead. See also
`filenocasecmp_to()<class_String_method_filenocasecmp_to>`{.interpreted-text
role="ref"},
`naturalcasecmp_to()<class_String_method_naturalcasecmp_to>`{.interpreted-text
role="ref"}, and
`casecmp_to()<class_String_method_casecmp_to>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_filenocasecmp_to}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **filenocasecmp_to**(to:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_filenocasecmp_to>`{.interpreted-text role="ref"}

Like
`naturalnocasecmp_to()<class_String_method_naturalnocasecmp_to>`{.interpreted-text
role="ref"} but prioritizes strings that begin with periods (`.`) and
underscores (`_`) before any other character. Useful when sorting
folders or file names.

To get a `bool<class_bool>`{.interpreted-text role="ref"} result from a
string comparison, use the `==` operator instead. See also
`filecasecmp_to()<class_String_method_filecasecmp_to>`{.interpreted-text
role="ref"},
`naturalnocasecmp_to()<class_String_method_naturalnocasecmp_to>`{.interpreted-text
role="ref"}, and
`nocasecmp_to()<class_String_method_nocasecmp_to>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_find}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find**(what:
`String<class_String>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_find>`{.interpreted-text
role="ref"}

Returns the index of the **first** occurrence of `what` in this string,
or `-1` if there are none. The search\'s start can be specified with
`from`, continuing to the end of the string.

::::: tabs
::: code-tab
gdscript

print(\"Team\".find(\"I\")) \# Prints -1

print(\"Potato\".find(\"t\")) \# Prints 2 print(\"Potato\".find(\"t\",
3)) \# Prints 4 print(\"Potato\".find(\"t\", 5)) \# Prints -1
:::

::: code-tab
csharp

GD.Print(\"Team\".Find(\"I\")); // Prints -1

GD.Print(\"Potato\".Find(\"t\")); // Prints 2
GD.Print(\"Potato\".Find(\"t\", 3)); // Prints 4
GD.Print(\"Potato\".Find(\"t\", 5)); // Prints -1
:::
:::::

\*\*Note:\*\* If you just want to know whether the string contains
`what`, use `contains()<class_String_method_contains>`{.interpreted-text
role="ref"}. In GDScript, you may also use the `in` operator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_findn}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **findn**(what:
`String<class_String>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_findn>`{.interpreted-text
role="ref"}

Returns the index of the **first** **case-insensitive** occurrence of
`what` in this string, or `-1` if there are none. The starting search
index can be specified with `from`, continuing to the end of the string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_format}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **format**(values:
`Variant<class_Variant>`{.interpreted-text role="ref"}, placeholder:
`String<class_String>`{.interpreted-text role="ref"} = \"{\_}\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_format>`{.interpreted-text
role="ref"}

Formats the string by replacing all occurrences of `placeholder` with
the elements of `values`.

`values` can be a `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, an `Array<class_Array>`{.interpreted-text role="ref"}, or
an `Object<class_Object>`{.interpreted-text role="ref"}. Any underscores
in `placeholder` will be replaced with the corresponding keys in
advance. Array elements use their index as keys.

    # Prints "Waiting for Godot is a play by Samuel Beckett, and Godot Engine is named after it."
    var use_array_values = "Waiting for {0} is a play by {1}, and {0} Engine is named after it."
    print(use_array_values.format(["Godot", "Samuel Beckett"]))

    # Prints "User 42 is Godot."
    print("User {id} is {name}.".format({"id": 42, "name": "Godot"}))

Some additional handling is performed when `values` is an
`Array<class_Array>`{.interpreted-text role="ref"}. If `placeholder`
does not contain an underscore, the elements of the `values` array will
be used to replace one occurrence of the placeholder in order; If an
element of `values` is another 2-element array, it\'ll be interpreted as
a key-value pair.

    # Prints "User 42 is Godot."
    print("User {} is {}.".format([42, "Godot"], "{}"))
    print("User {id} is {name}.".format([["id", 42], ["name", "Godot"]]))

When passing an `Object<class_Object>`{.interpreted-text role="ref"},
the property names from
`Object.get_property_list()<class_Object_method_get_property_list>`{.interpreted-text
role="ref"} are used as keys.

    # Prints "Visible true, position (0, 0)"
    var node = Node2D.new()
    print("Visible {visible}, position {position}".format(node))

See also the
`GDScript format string <../tutorials/scripting/gdscript/gdscript_format_string>`{.interpreted-text
role="doc"} tutorial.

\*\*Note:\*\* Each replacement is done sequentially for each element of
`values`, **not** all at once. This means that if any element is
inserted and it contains another placeholder, it may be changed by the
next replacement. While this can be very useful, it often causes
unexpected results. If not necessary, make sure `values`\'s elements do
not contain placeholders.

    print("{0} {1}".format(["{1}", "x"]))           # Prints "x x"
    print("{0} {1}".format(["x", "{0}"]))           # Prints "x {0}"
    print("{a} {b}".format({"a": "{b}", "b": "c"})) # Prints "c c"
    print("{a} {b}".format({"b": "c", "a": "{b}"})) # Prints "{b} c"

\*\*Note:\*\* In C#, it\'s recommended to [interpolate strings with
\"\$\"](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated),
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_get_base_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_base_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_get_base_dir>`{.interpreted-text
role="ref"}

If the string is a valid file path, returns the base directory name.

    var dir_path = "/path/to/file.txt".get_base_dir() # dir_path is "/path/to"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_get_basename}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_basename**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_get_basename>`{.interpreted-text
role="ref"}

If the string is a valid file path, returns the full file path, without
the extension.

    var base = "/path/to/file.txt".get_basename() # base is "/path/to/file"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_get_extension}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_extension**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_get_extension>`{.interpreted-text
role="ref"}

If the string is a valid file name or path, returns the file extension
without the leading period (`.`). Otherwise, returns an empty string.

    var a = "/path/to/file.txt".get_extension() # a is "txt"
    var b = "cool.txt".get_extension()          # b is "txt"
    var c = "cool.font.tres".get_extension()    # c is "tres"
    var d = ".pack1".get_extension()            # d is "pack1"

    var e = "file.txt.".get_extension()  # e is ""
    var f = "file.txt..".get_extension() # f is ""
    var g = "txt".get_extension()        # g is ""
    var h = "".get_extension()           # h is ""

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_get_file}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_file**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_get_file>`{.interpreted-text
role="ref"}

If the string is a valid file path, returns the file name, including the
extension.

    var file = "/path/to/icon.png".get_file() # file is "icon.png"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_get_slice}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_slice**(delimiter: `String<class_String>`{.interpreted-text
role="ref"}, slice: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_get_slice>`{.interpreted-text
role="ref"}

Splits the string using a `delimiter` and returns the substring at index
`slice`. Returns the original string if `delimiter` does not occur in
the string. Returns an empty string if the `slice` does not exist.

This is faster than
`split()<class_String_method_split>`{.interpreted-text role="ref"}, if
you only need one substring.

    print("i/am/example/hi".get_slice("/", 2)) # Prints "example"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_get_slice_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_slice_count**(delimiter: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_get_slice_count>`{.interpreted-text
role="ref"}

Returns the total number of slices when the string is split with the
given `delimiter` (see
`split()<class_String_method_split>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_get_slicec}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_slicec**(delimiter: `int<class_int>`{.interpreted-text
role="ref"}, slice: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_get_slicec>`{.interpreted-text
role="ref"}

Splits the string using a Unicode character with code `delimiter` and
returns the substring at index `slice`. Returns an empty string if the
`slice` does not exist.

This is faster than
`split()<class_String_method_split>`{.interpreted-text role="ref"}, if
you only need one substring.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_hash}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hash**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_hash>`{.interpreted-text
role="ref"}

Returns the 32-bit hash value representing the string\'s contents.

\*\*Note:\*\* Strings with equal hash values are *not* guaranteed to be
the same, as a result of hash collisions. On the contrary, strings with
different hash values are guaranteed to be different.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_hex_decode}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**hex_decode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_hex_decode>`{.interpreted-text
role="ref"}

Decodes a hexadecimal string as a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.

::::: tabs
::: code-tab
gdscript

var text = \"hello world\" var encoded =
text.to_utf8_buffer().hex_encode() \# outputs \"68656c6c6f20776f726c64\"
print(encoded.hex_decode().get_string_from_utf8())
:::

::: code-tab
csharp

var text = \"hello world\"; var encoded =
text.ToUtf8Buffer().HexEncode(); // outputs \"68656c6c6f20776f726c64\"
GD.Print(encoded.HexDecode().GetStringFromUtf8());
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_hex_to_int}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hex_to_int**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_hex_to_int>`{.interpreted-text
role="ref"}

Converts the string representing a hexadecimal number into an
`int<class_int>`{.interpreted-text role="ref"}. The string may be
optionally prefixed with `"0x"`, and an additional `-` prefix for
negative numbers.

::::: tabs
::: code-tab
gdscript

print(\"0xff\".hex_to_int()) \# Prints 255 print(\"ab\".hex_to_int()) \#
Prints 171
:::

::: code-tab
csharp

GD.Print(\"0xff\".HexToInt()); // Prints 255
GD.Print(\"ab\".HexToInt()); // Prints 171
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_humanize_size}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**humanize_size**(size: `int<class_int>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_humanize_size>`{.interpreted-text
role="ref"}

Converts `size` which represents a number of bytes into a human-readable
form.

The result is in [IEC prefix
format](https://en.wikipedia.org/wiki/Binary_prefix#IEC_prefixes), which
may end in either `"B"`, `"KiB"`, `"MiB"`, `"GiB"`, `"TiB"`, `"PiB"`, or
`"EiB"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_indent}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **indent**(prefix:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_indent>`{.interpreted-text
role="ref"}

Indents every line of the string with the given `prefix`. Empty lines
are not indented. See also
`dedent()<class_String_method_dedent>`{.interpreted-text role="ref"} to
remove indentation.

For example, the string can be indented with two tabulations using
`"\t\t"`, or four spaces using `"    "`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_insert}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**insert**(position: `int<class_int>`{.interpreted-text role="ref"},
what: `String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_insert>`{.interpreted-text
role="ref"}

Inserts `what` at the given `position` in the string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_absolute_path}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_absolute_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_absolute_path>`{.interpreted-text role="ref"}

Returns `true` if the string is a path to a file or directory, and its
starting point is explicitly defined. This method is the opposite of
`is_relative_path()<class_String_method_is_relative_path>`{.interpreted-text
role="ref"}.

This includes all paths starting with `"res://"`, `"user://"`, `"C:\"`,
`"/"`, etc.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the string\'s length is `0` (`""`). See also
`length()<class_String_method_length>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_relative_path}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_relative_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_relative_path>`{.interpreted-text role="ref"}

Returns `true` if the string is a path, and its starting point is
dependent on context. The path could begin from the current directory,
or the current `Node<class_Node>`{.interpreted-text role="ref"} (if the
string is derived from a `NodePath<class_NodePath>`{.interpreted-text
role="ref"}), and may sometimes be prefixed with `"./"`. This method is
the opposite of
`is_absolute_path()<class_String_method_is_absolute_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_subsequence_of}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_subsequence_of**(text: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_subsequence_of>`{.interpreted-text
role="ref"}

Returns `true` if all characters of this string can be found in `text`
in their original order. This is not the same as
`contains()<class_String_method_contains>`{.interpreted-text
role="ref"}.

    var text = "Wow, incredible!"

    print("inedible".is_subsequence_of(text)) # Prints true
    print("Word!".is_subsequence_of(text))    # Prints true
    print("Window".is_subsequence_of(text))   # Prints false
    print("".is_subsequence_of(text))         # Prints true

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_subsequence_ofn}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_subsequence_ofn**(text: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_subsequence_ofn>`{.interpreted-text
role="ref"}

Returns `true` if all characters of this string can be found in `text`
in their original order, **ignoring case**. This is not the same as
`containsn()<class_String_method_containsn>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_valid_ascii_identifier}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_ascii_identifier**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_valid_ascii_identifier>`{.interpreted-text
role="ref"}

Returns `true` if this string is a valid ASCII identifier. A valid ASCII
identifier may contain only letters, digits, and underscores (`_`), and
the first character may not be a digit.

    print("node_2d".is_valid_ascii_identifier())    # Prints true
    print("TYPE_FLOAT".is_valid_ascii_identifier()) # Prints true
    print("1st_method".is_valid_ascii_identifier()) # Prints false
    print("MyMethod#2".is_valid_ascii_identifier()) # Prints false

See also
`is_valid_unicode_identifier()<class_String_method_is_valid_unicode_identifier>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_valid_filename}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_valid_filename**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_valid_filename>`{.interpreted-text
role="ref"}

Returns `true` if this string is a valid file name. A valid file name
cannot be empty, begin or end with space characters, or contain
characters that are not allowed (`:` `/` `\` `?` `*` `"` `|` `%` `<`
`>`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_valid_float}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_valid_float**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_is_valid_float>`{.interpreted-text
role="ref"}

Returns `true` if this string represents a valid floating-point number.
A valid float may contain only digits, one decimal point (`.`), and the
exponent letter (`e`). It may also be prefixed with a positive (`+`) or
negative (`-`) sign. Any valid integer is also a valid float (see
`is_valid_int()<class_String_method_is_valid_int>`{.interpreted-text
role="ref"}). See also
`to_float()<class_String_method_to_float>`{.interpreted-text
role="ref"}.

    print("1.7".is_valid_float())   # Prints true
    print("24".is_valid_float())    # Prints true
    print("7e3".is_valid_float())   # Prints true
    print("Hello".is_valid_float()) # Prints false

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_valid_hex_number}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_hex_number**(with_prefix:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_valid_hex_number>`{.interpreted-text
role="ref"}

Returns `true` if this string is a valid hexadecimal number. A valid
hexadecimal number only contains digits or letters `A` to `F` (either
uppercase or lowercase), and may be prefixed with a positive (`+`) or
negative (`-`) sign.

If `with_prefix` is `true`, the hexadecimal number needs to prefixed by
`"0x"` to be considered valid.

    print("A08E".is_valid_hex_number())    # Prints true
    print("-AbCdEf".is_valid_hex_number()) # Prints true
    print("2.5".is_valid_hex_number())     # Prints false

    print("0xDEADC0DE".is_valid_hex_number(true)) # Prints true

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_valid_html_color}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_html_color**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_valid_html_color>`{.interpreted-text
role="ref"}

Returns `true` if this string is a valid color in hexadecimal HTML
notation. The string must be a hexadecimal value (see
`is_valid_hex_number()<class_String_method_is_valid_hex_number>`{.interpreted-text
role="ref"}) of either 3, 4, 6 or 8 digits, and may be prefixed by a
hash sign (`#`). Other HTML notations for colors, such as names or
`hsl()`, are not considered valid. See also
`Color.html()<class_Color_method_html>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_valid_identifier}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_identifier**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_valid_identifier>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`is_valid_ascii_identifier()<class_String_method_is_valid_ascii_identifier>`{.interpreted-text
role="ref"} instead.

Returns `true` if this string is a valid identifier. A valid identifier
may contain only letters, digits and underscores (`_`), and the first
character may not be a digit.

    print("node_2d".is_valid_identifier())    # Prints true
    print("TYPE_FLOAT".is_valid_identifier()) # Prints true
    print("1st_method".is_valid_identifier()) # Prints false
    print("MyMethod#2".is_valid_identifier()) # Prints false

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_valid_int}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_valid_int**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_is_valid_int>`{.interpreted-text
role="ref"}

Returns `true` if this string represents a valid integer. A valid
integer only contains digits, and may be prefixed with a positive (`+`)
or negative (`-`) sign. See also
`to_int()<class_String_method_to_int>`{.interpreted-text role="ref"}.

    print("7".is_valid_int())    # Prints true
    print("1.65".is_valid_int()) # Prints false
    print("Hi".is_valid_int())   # Prints false
    print("+3".is_valid_int())   # Prints true
    print("-12".is_valid_int())  # Prints true

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_valid_ip_address}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_ip_address**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_valid_ip_address>`{.interpreted-text
role="ref"}

Returns `true` if this string represents a well-formatted IPv4 or IPv6
address. This method considers [reserved IP
addresses](https://en.wikipedia.org/wiki/Reserved_IP_addresses) such as
`"0.0.0.0"` and `"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"` as valid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_is_valid_unicode_identifier}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_unicode_identifier**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_is_valid_unicode_identifier>`{.interpreted-text
role="ref"}

Returns `true` if this string is a valid Unicode identifier.

A valid Unicode identifier must begin with a Unicode character of class
`XID_Start` or `"_"`, and may contain Unicode characters of class
`XID_Continue` in the other positions.

    print("node_2d".is_valid_unicode_identifier())      # Prints true
    print("1st_method".is_valid_unicode_identifier())   # Prints false
    print("MyMethod#2".is_valid_unicode_identifier())   # Prints false
    print("állóképesség".is_valid_unicode_identifier()) # Prints true
    print("выносливость".is_valid_unicode_identifier()) # Prints true
    print("体力".is_valid_unicode_identifier())         # Prints true

See also
`is_valid_ascii_identifier()<class_String_method_is_valid_ascii_identifier>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method checks identifiers the same way as GDScript.
See
`TextServer.is_valid_identifier()<class_TextServer_method_is_valid_identifier>`{.interpreted-text
role="ref"} for more advanced checks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_join}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **join**(parts:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_join>`{.interpreted-text
role="ref"}

Returns the concatenation of `parts`\' elements, with each element
separated by the string calling this method. This method is the opposite
of `split()<class_String_method_split>`{.interpreted-text role="ref"}.

::::: tabs
::: code-tab
gdscript

var fruits = \[\"Apple\", \"Orange\", \"Pear\", \"Kiwi\"\]

print(\", \".join(fruits)) \# Prints \"Apple, Orange, Pear, Kiwi\"
print(\"\-\--\".join(fruits)) \# Prints
\"Apple\-\--Orange\-\--Pear\-\--Kiwi\"
:::

::: code-tab
csharp

string\[\] fruits = \[\"Apple\", \"Orange\", \"Pear\", \"Kiwi\"\];

// In C#, this method is static. GD.Print(string.Join(\", \", fruits));
// Prints \"Apple, Orange, Pear, Kiwi\" GD.Print(string.Join(\"\-\--\",
fruits)); // Prints \"Apple\-\--Orange\-\--Pear\-\--Kiwi\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_json_escape}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **json_escape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_json_escape>`{.interpreted-text
role="ref"}

Returns a copy of the string with special characters escaped using the
JSON standard. Because it closely matches the C standard, it is possible
to use `c_unescape()<class_String_method_c_unescape>`{.interpreted-text
role="ref"} to unescape the string, if necessary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_left}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **left**(length:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_left>`{.interpreted-text
role="ref"}

Returns the first `length` characters from the beginning of the string.
If `length` is negative, strips the last `length` characters from the
string\'s end.

    print("Hello World!".left(3))  # Prints "Hel"
    print("Hello World!".left(-4)) # Prints "Hello Wo"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_length}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_length>`{.interpreted-text
role="ref"}

Returns the number of characters in the string. Empty strings (`""`)
always return `0`. See also
`is_empty()<class_String_method_is_empty>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_lpad}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**lpad**(min_length: `int<class_int>`{.interpreted-text role="ref"},
character: `String<class_String>`{.interpreted-text role="ref"} = \" \")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_lpad>`{.interpreted-text
role="ref"}

Formats the string to be at least `min_length` long by adding
`character`s to the left of the string, if necessary. See also
`rpad()<class_String_method_rpad>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_lstrip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **lstrip**(chars:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_lstrip>`{.interpreted-text
role="ref"}

Removes a set of characters defined in `chars` from the string\'s
beginning. See also
`rstrip()<class_String_method_rstrip>`{.interpreted-text role="ref"}.

\*\*Note:\*\* `chars` is not a prefix. Use
`trim_prefix()<class_String_method_trim_prefix>`{.interpreted-text
role="ref"} to remove a single prefix, rather than a set of characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_match}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **match**(expr:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_match>`{.interpreted-text
role="ref"}

Does a simple expression match (also called \"glob\" or \"globbing\"),
where `*` matches zero or more arbitrary characters and `?` matches any
single character except a period (`.`). An empty string or empty
expression always evaluates to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_matchn}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **matchn**(expr:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_matchn>`{.interpreted-text
role="ref"}

Does a simple **case-insensitive** expression match, where `*` matches
zero or more arbitrary characters and `?` matches any single character
except a period (`.`). An empty string or empty expression always
evaluates to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_md5_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**md5_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_md5_buffer>`{.interpreted-text
role="ref"}

Returns the [MD5 hash](https://en.wikipedia.org/wiki/MD5) of the string
as a `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_md5_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **md5_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_md5_text>`{.interpreted-text
role="ref"}

Returns the [MD5 hash](https://en.wikipedia.org/wiki/MD5) of the string
as another **String**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_naturalcasecmp_to}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **naturalcasecmp_to**(to:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_naturalcasecmp_to>`{.interpreted-text
role="ref"}

Performs a **case-sensitive**, *natural order* comparison to another
string. Returns `-1` if less than, `1` if greater than, or `0` if equal.
\"Less than\" or \"greater than\" are determined by the [Unicode code
points](https://en.wikipedia.org/wiki/List_of_Unicode_characters) of
each string, which roughly matches the alphabetical order.

When used for sorting, natural order comparison orders sequences of
numbers by the combined value of each digit as is often expected,
instead of the single digit\'s value. A sorted sequence of numbered
strings will be `["1", "2", "3", ...]`, not
`["1", "10", "2", "3", ...]`.

If the character comparison reaches the end of one string, but the other
string contains more characters, then it will use length as the deciding
factor: `1` will be returned if this string is longer than the `to`
string, or `-1` if shorter. Note that the length of empty strings is
always `0`.

To get a `bool<class_bool>`{.interpreted-text role="ref"} result from a
string comparison, use the `==` operator instead. See also
`naturalnocasecmp_to()<class_String_method_naturalnocasecmp_to>`{.interpreted-text
role="ref"},
`filecasecmp_to()<class_String_method_filecasecmp_to>`{.interpreted-text
role="ref"}, and
`nocasecmp_to()<class_String_method_nocasecmp_to>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_naturalnocasecmp_to}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**naturalnocasecmp_to**(to: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_naturalnocasecmp_to>`{.interpreted-text
role="ref"}

Performs a **case-insensitive**, *natural order* comparison to another
string. Returns `-1` if less than, `1` if greater than, or `0` if equal.
\"Less than\" or \"greater than\" are determined by the [Unicode code
points](https://en.wikipedia.org/wiki/List_of_Unicode_characters) of
each string, which roughly matches the alphabetical order. Internally,
lowercase characters are converted to uppercase for the comparison.

When used for sorting, natural order comparison orders sequences of
numbers by the combined value of each digit as is often expected,
instead of the single digit\'s value. A sorted sequence of numbered
strings will be `["1", "2", "3", ...]`, not
`["1", "10", "2", "3", ...]`.

If the character comparison reaches the end of one string, but the other
string contains more characters, then it will use length as the deciding
factor: `1` will be returned if this string is longer than the `to`
string, or `-1` if shorter. Note that the length of empty strings is
always `0`.

To get a `bool<class_bool>`{.interpreted-text role="ref"} result from a
string comparison, use the `==` operator instead. See also
`naturalcasecmp_to()<class_String_method_naturalcasecmp_to>`{.interpreted-text
role="ref"},
`filenocasecmp_to()<class_String_method_filenocasecmp_to>`{.interpreted-text
role="ref"}, and
`casecmp_to()<class_String_method_casecmp_to>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_nocasecmp_to}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **nocasecmp_to**(to:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_nocasecmp_to>`{.interpreted-text
role="ref"}

Performs a **case-insensitive** comparison to another string. Returns
`-1` if less than, `1` if greater than, or `0` if equal. \"Less than\"
or \"greater than\" are determined by the [Unicode code
points](https://en.wikipedia.org/wiki/List_of_Unicode_characters) of
each string, which roughly matches the alphabetical order. Internally,
lowercase characters are converted to uppercase for the comparison.

If the character comparison reaches the end of one string, but the other
string contains more characters, then it will use length as the deciding
factor: `1` will be returned if this string is longer than the `to`
string, or `-1` if shorter. Note that the length of empty strings is
always `0`.

To get a `bool<class_bool>`{.interpreted-text role="ref"} result from a
string comparison, use the `==` operator instead. See also
`casecmp_to()<class_String_method_casecmp_to>`{.interpreted-text
role="ref"},
`filenocasecmp_to()<class_String_method_filenocasecmp_to>`{.interpreted-text
role="ref"}, and
`naturalnocasecmp_to()<class_String_method_naturalnocasecmp_to>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_num}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **num**(number:
`float<class_float>`{.interpreted-text role="ref"}, decimals:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_num>`{.interpreted-text role="ref"}

Converts a `float<class_float>`{.interpreted-text role="ref"} to a
string representation of a decimal number, with the number of decimal
places specified in `decimals`.

If `decimals` is `-1` as by default, the string representation may only
have up to 14 significant digits, with digits before the decimal point
having priority over digits after.

Trailing zeros are not included in the string. The last digit is
rounded, not truncated.

    String.num(3.141593)     # Returns "3.141593"
    String.num(3.141593, 3)  # Returns "3.142"
    String.num(3.14159300)   # Returns "3.141593"

    # Here, the last digit will be rounded up,
    # which reduces the total digit count, since trailing zeros are removed:
    String.num(42.129999, 5) # Returns "42.13"

    # If `decimals` is not specified, the maximum number of significant digits is 14:
    String.num(-0.0000012345432123454321)     # Returns "-0.00000123454321"
    String.num(-10000.0000012345432123454321) # Returns "-10000.0000012345"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_num_int64}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**num_int64**(number: `int<class_int>`{.interpreted-text role="ref"},
base: `int<class_int>`{.interpreted-text role="ref"} = 10,
capitalize_hex: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_num_int64>`{.interpreted-text
role="ref"}

Converts the given `number` to a string representation, with the given
`base`.

By default, `base` is set to decimal (`10`). Other common bases in
programming include binary (`2`),
[octal](https://en.wikipedia.org/wiki/Octal) (`8`), hexadecimal (`16`).

If `capitalize_hex` is `true`, digits higher than 9 are represented in
uppercase.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_num_scientific}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**num_scientific**(number: `float<class_float>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_num_scientific>`{.interpreted-text
role="ref"}

Converts the given `number` to a string representation, in scientific
notation.

::::: tabs
::: code-tab
gdscript

var n = -5.2e8 print(n) \# Prints -520000000
print(String.num_scientific(n)) \# Prints -5.2e+08
:::

::: code-tab
csharp

// This method is not implemented in C#. // Use
[string.ToString()]{.title-ref} with \"e\" to achieve similar results.
var n = -5.2e8f; GD.Print(n); // Prints -520000000
GD.Print(n.ToString(\"e1\")); // Prints -5.2e+008
:::
:::::

\*\*Note:\*\* In C#, this method is not implemented. To achieve similar
results, see C#\'s [Standard numeric format
strings](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_num_uint64}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**num_uint64**(number: `int<class_int>`{.interpreted-text role="ref"},
base: `int<class_int>`{.interpreted-text role="ref"} = 10,
capitalize_hex: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_num_uint64>`{.interpreted-text
role="ref"}

Converts the given unsigned `int<class_int>`{.interpreted-text
role="ref"} to a string representation, with the given `base`.

By default, `base` is set to decimal (`10`). Other common bases in
programming include binary (`2`),
[octal](https://en.wikipedia.org/wiki/Octal) (`8`), hexadecimal (`16`).

If `capitalize_hex` is `true`, digits higher than 9 are represented in
uppercase.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_pad_decimals}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**pad_decimals**(digits: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_pad_decimals>`{.interpreted-text
role="ref"}

Formats the string representing a number to have an exact number of
`digits` *after* the decimal point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_pad_zeros}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**pad_zeros**(digits: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_pad_zeros>`{.interpreted-text
role="ref"}

Formats the string representing a number to have an exact number of
`digits` *before* the decimal point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_path_join}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **path_join**(path:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_path_join>`{.interpreted-text
role="ref"}

Concatenates `path` at the end of the string as a subpath, adding `/` if
necessary.

\*\*Example:\*\* `"this/is".path_join("path") == "this/is/path"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_remove_char}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**remove_char**(what: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_remove_char>`{.interpreted-text
role="ref"}

Removes all occurrences of the Unicode character with code `what`.
Faster version of
`replace()<class_String_method_replace>`{.interpreted-text role="ref"}
when the key is only one character long and the replacement is `""`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_remove_chars}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**remove_chars**(chars: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_remove_chars>`{.interpreted-text
role="ref"}

Removes any occurrence of the characters in `chars`. See also
`remove_char()<class_String_method_remove_char>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_repeat}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **repeat**(count:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_repeat>`{.interpreted-text
role="ref"}

Repeats this string a number of times. `count` needs to be greater than
`0`. Otherwise, returns an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_replace}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **replace**(what:
`String<class_String>`{.interpreted-text role="ref"}, forwhat:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_replace>`{.interpreted-text
role="ref"}

Replaces all occurrences of `what` inside the string with the given
`forwhat`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_replace_char}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**replace_char**(key: `int<class_int>`{.interpreted-text role="ref"},
with: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_replace_char>`{.interpreted-text
role="ref"}

Replaces all occurrences of the Unicode character with code `key` with
the Unicode character with code `with`. Faster version of
`replace()<class_String_method_replace>`{.interpreted-text role="ref"}
when the key is only one character long. To get a single character use
`"X".unicode_at(0)` (note that some strings, like compound letters and
emoji, can be composed of multiple unicode codepoints, and will not work
with this method, use
`length()<class_String_method_length>`{.interpreted-text role="ref"} to
make sure).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_replace_chars}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**replace_chars**(keys: `String<class_String>`{.interpreted-text
role="ref"}, with: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_replace_chars>`{.interpreted-text
role="ref"}

Replaces any occurrence of the characters in `keys` with the Unicode
character with code `with`. See also
`replace_char()<class_String_method_replace_char>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_replacen}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **replacen**(what:
`String<class_String>`{.interpreted-text role="ref"}, forwhat:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_replacen>`{.interpreted-text
role="ref"}

Replaces all **case-insensitive** occurrences of `what` inside the
string with the given `forwhat`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_reverse}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **reverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_reverse>`{.interpreted-text
role="ref"}

Returns the copy of this string in reverse order. This operation works
on unicode codepoints, rather than sequences of codepoints, and may
break things like compound letters or emojis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_rfind}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rfind**(what:
`String<class_String>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_rfind>`{.interpreted-text
role="ref"}

Returns the index of the **last** occurrence of `what` in this string,
or `-1` if there are none. The search\'s start can be specified with
`from`, continuing to the beginning of the string. This method is the
reverse of `find()<class_String_method_find>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_rfindn}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rfindn**(what:
`String<class_String>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_rfindn>`{.interpreted-text
role="ref"}

Returns the index of the **last** **case-insensitive** occurrence of
`what` in this string, or `-1` if there are none. The starting search
index can be specified with `from`, continuing to the beginning of the
string. This method is the reverse of
`findn()<class_String_method_findn>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_right}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **right**(length:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_right>`{.interpreted-text
role="ref"}

Returns the last `length` characters from the end of the string. If
`length` is negative, strips the first `length` characters from the
string\'s beginning.

    print("Hello World!".right(3))  # Prints "ld!"
    print("Hello World!".right(-4)) # Prints "o World!"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_rpad}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rpad**(min_length: `int<class_int>`{.interpreted-text role="ref"},
character: `String<class_String>`{.interpreted-text role="ref"} = \" \")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_rpad>`{.interpreted-text
role="ref"}

Formats the string to be at least `min_length` long, by adding
`character`s to the right of the string, if necessary. See also
`lpad()<class_String_method_lpad>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_rsplit}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **rsplit**(delimiter:
`String<class_String>`{.interpreted-text role="ref"} = \"\",
allow_empty: `bool<class_bool>`{.interpreted-text role="ref"} = true,
maxsplit: `int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_rsplit>`{.interpreted-text
role="ref"}

Splits the string using a `delimiter` and returns an array of the
substrings, starting from the end of the string. The splits in the
returned array appear in the same order as the original string. If
`delimiter` is an empty string, each substring will be a single
character.

If `allow_empty` is `false`, empty strings between adjacent delimiters
are excluded from the array.

If `maxsplit` is greater than `0`, the number of splits may not exceed
`maxsplit`. By default, the entire string is split, which is mostly
identical to `split()<class_String_method_split>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var some_string = \"One,Two,Three,Four\" var some_array =
some_string.rsplit(\",\", true, 1)

print(some_array.size()) \# Prints 2 print(some_array\[0\]) \# Prints
\"One,Two,Three\" print(some_array\[1\]) \# Prints \"Four\"
:::

::: code-tab
csharp

// In C#, there is no String.RSplit() method.
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_rstrip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **rstrip**(chars:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_rstrip>`{.interpreted-text
role="ref"}

Removes a set of characters defined in `chars` from the string\'s end.
See also `lstrip()<class_String_method_lstrip>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* `chars` is not a suffix. Use
`trim_suffix()<class_String_method_trim_suffix>`{.interpreted-text
role="ref"} to remove a single suffix, rather than a set of characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_sha1_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**sha1_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_sha1_buffer>`{.interpreted-text
role="ref"}

Returns the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash of the
string as a `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_sha1_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **sha1_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_sha1_text>`{.interpreted-text
role="ref"}

Returns the [SHA-1](https://en.wikipedia.org/wiki/SHA-1) hash of the
string as another **String**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_sha256_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**sha256_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_sha256_buffer>`{.interpreted-text
role="ref"}

Returns the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash of the
string as a `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_sha256_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **sha256_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_sha256_text>`{.interpreted-text
role="ref"}

Returns the [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash of the
string as another **String**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_similarity}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **similarity**(text:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_similarity>`{.interpreted-text
role="ref"}

Returns the similarity index ([Sørensen-Dice
coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient))
of this string compared to another. A result of `1.0` means totally
similar, while `0.0` means totally dissimilar.

    print("ABC123".similarity("ABC123")) # Prints 1.0
    print("ABC123".similarity("XYZ456")) # Prints 0.0
    print("ABC123".similarity("123ABC")) # Prints 0.8
    print("ABC123".similarity("abc123")) # Prints 0.4

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_simplify_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **simplify_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_simplify_path>`{.interpreted-text
role="ref"}

If the string is a valid file path, converts the string into a canonical
path. This is the shortest possible path, without `"./"`, and all the
unnecessary `".."` and `"/"`.

    var simple_path = "./path/to///../file".simplify_path()
    print(simple_path) # Prints "path/file"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_split}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **split**(delimiter:
`String<class_String>`{.interpreted-text role="ref"} = \"\",
allow_empty: `bool<class_bool>`{.interpreted-text role="ref"} = true,
maxsplit: `int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_split>`{.interpreted-text
role="ref"}

Splits the string using a `delimiter` and returns an array of the
substrings. If `delimiter` is an empty string, each substring will be a
single character. This method is the opposite of
`join()<class_String_method_join>`{.interpreted-text role="ref"}.

If `allow_empty` is `false`, empty strings between adjacent delimiters
are excluded from the array.

If `maxsplit` is greater than `0`, the number of splits may not exceed
`maxsplit`. By default, the entire string is split.

::::: tabs
::: code-tab
gdscript

var some_array = \"One,Two,Three,Four\".split(\",\", true, 2)

print(some_array.size()) \# Prints 3 print(some_array\[0\]) \# Prints
\"One\" print(some_array\[1\]) \# Prints \"Two\" print(some_array\[2\])
\# Prints \"Three,Four\"
:::

::: code-tab
csharp

// C#\'s [Split()]{.title-ref} does not support the
[maxsplit]{.title-ref} parameter. var someArray =
\"One,Two,Three\".Split(\",\");

GD.Print(someArray\[0\]); // Prints \"One\" GD.Print(someArray\[1\]); //
Prints \"Two\" GD.Print(someArray\[2\]); // Prints \"Three\"
:::
:::::

\*\*Note:\*\* If you only need one substring from the array, consider
using `get_slice()<class_String_method_get_slice>`{.interpreted-text
role="ref"} which is faster. If you need to split strings with more
complex rules, use the `RegEx<class_RegEx>`{.interpreted-text
role="ref"} class instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_split_floats}
::: rst-class
classref-method
:::
::::

`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"} **split_floats**(delimiter:
`String<class_String>`{.interpreted-text role="ref"}, allow_empty:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_split_floats>`{.interpreted-text
role="ref"}

Splits the string into floats by using a `delimiter` and returns a
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"}.

If `allow_empty` is `false`, empty or invalid
`float<class_float>`{.interpreted-text role="ref"} conversions between
adjacent delimiters are excluded.

    var a = "1,2,4.5".split_floats(",")         # a is [1.0, 2.0, 4.5]
    var c = "1| ||4.5".split_floats("|")        # c is [1.0, 0.0, 0.0, 4.5]
    var b = "1| ||4.5".split_floats("|", false) # b is [1.0, 4.5]

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_strip_edges}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**strip_edges**(left: `bool<class_bool>`{.interpreted-text role="ref"} =
true, right: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_strip_edges>`{.interpreted-text
role="ref"}

Strips all non-printable characters from the beginning and the end of
the string. These include spaces, tabulations (`\t`), and newlines (`\n`
`\r`).

If `left` is `false`, ignores the string\'s beginning. Likewise, if
`right` is `false`, ignores the string\'s end.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_strip_escapes}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **strip_escapes**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_strip_escapes>`{.interpreted-text
role="ref"}

Strips all escape characters from the string. These include all
non-printable control characters of the first page of the ASCII table
(values from 0 to 31), such as tabulation (`\t`) and newline (`\n`,
`\r`) characters, but *not* spaces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_substr}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **substr**(from:
`int<class_int>`{.interpreted-text role="ref"}, len:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_substr>`{.interpreted-text
role="ref"}

Returns part of the string from the position `from` with length `len`.
If `len` is `-1` (as by default), returns the rest of the string
starting from the given position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_ascii_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_ascii_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_ascii_buffer>`{.interpreted-text
role="ref"}

Converts the string to an
[ASCII](https://en.wikipedia.org/wiki/ASCII)/Latin-1 encoded
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.
This method is slightly faster than
`to_utf8_buffer()<class_String_method_to_utf8_buffer>`{.interpreted-text
role="ref"}, but replaces all unsupported characters with spaces. This
is the inverse of
`PackedByteArray.get_string_from_ascii()<class_PackedByteArray_method_get_string_from_ascii>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_camel_case}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **to_camel_case**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_camel_case>`{.interpreted-text
role="ref"}

Returns the string converted to `camelCase`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_float}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **to_float**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_float>`{.interpreted-text
role="ref"}

Converts the string representing a decimal number into a
`float<class_float>`{.interpreted-text role="ref"}. This method stops on
the first non-number character, except the first decimal point (`.`) and
the exponent letter (`e`). See also
`is_valid_float()<class_String_method_is_valid_float>`{.interpreted-text
role="ref"}.

    var a = "12.35".to_float()  # a is 12.35
    var b = "1.2.3".to_float()  # b is 1.2
    var c = "12xy3".to_float()  # c is 12.0
    var d = "1e3".to_float()    # d is 1000.0
    var e = "Hello!".to_float() # e is 0.0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_int}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **to_int**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_int>`{.interpreted-text
role="ref"}

Converts the string representing an integer number into an
`int<class_int>`{.interpreted-text role="ref"}. This method removes any
non-number character and stops at the first decimal point (`.`). See
also
`is_valid_int()<class_String_method_is_valid_int>`{.interpreted-text
role="ref"}.

    var a = "123".to_int()    # a is 123
    var b = "x1y2z3".to_int() # b is 123
    var c = "-1.2.3".to_int() # c is -1
    var d = "Hello!".to_int() # d is 0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_kebab_case}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **to_kebab_case**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_kebab_case>`{.interpreted-text
role="ref"}

Returns the string converted to `kebab-case`.

\*\*Note:\*\* Numbers followed by a *single* letter are not separated in
the conversion to keep some words (such as \"2D\") together.

::::: tabs
::: code-tab
gdscript

\"Node2D\".to_kebab_case() \# Returns \"node-2d\" \"2nd
place\".to_kebab_case() \# Returns \"2-nd-place\"
\"Texture3DAssetFolder\".to_kebab_case() \# Returns
\"texture-3d-asset-folder\"
:::

::: code-tab
csharp

\"Node2D\".ToKebabCase(); // Returns \"node-2d\" \"2nd
place\".ToKebabCase(); // Returns \"2-nd-place\"
\"Texture3DAssetFolder\".ToKebabCase(); // Returns
\"texture-3d-asset-folder\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_lower}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **to_lower**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_lower>`{.interpreted-text
role="ref"}

Returns the string converted to `lowercase`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_multibyte_char_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_multibyte_char_buffer**(encoding:
`String<class_String>`{.interpreted-text role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_to_multibyte_char_buffer>`{.interpreted-text
role="ref"}

Converts the string to system multibyte code page encoded
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.
If conversion fails, empty array is returned.

The values permitted for `encoding` are system dependent. If `encoding`
is empty string, system default encoding is used.

- For Windows, see [Code Page
  Identifiers](https://learn.microsoft.com/en-us/windows/win32/Intl/code-page-identifiers)
  .NET names.
- For macOS and Linux/BSD, see `libiconv` library documentation and
  `iconv --list` for a list of supported encodings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_pascal_case}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**to_pascal_case**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_pascal_case>`{.interpreted-text
role="ref"}

Returns the string converted to `PascalCase`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_snake_case}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **to_snake_case**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_snake_case>`{.interpreted-text
role="ref"}

Returns the string converted to `snake_case`.

\*\*Note:\*\* Numbers followed by a *single* letter are not separated in
the conversion to keep some words (such as \"2D\") together.

::::: tabs
::: code-tab
gdscript

\"Node2D\".to_snake_case() \# Returns \"node_2d\" \"2nd
place\".to_snake_case() \# Returns \"2_nd_place\"
\"Texture3DAssetFolder\".to_snake_case() \# Returns
\"texture_3d_asset_folder\"
:::

::: code-tab
csharp

\"Node2D\".ToSnakeCase(); // Returns \"node_2d\" \"2nd
place\".ToSnakeCase(); // Returns \"2_nd_place\"
\"Texture3DAssetFolder\".ToSnakeCase(); // Returns
\"texture_3d_asset_folder\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_upper}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **to_upper**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_upper>`{.interpreted-text
role="ref"}

Returns the string converted to `UPPERCASE`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_utf8_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_utf8_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_utf8_buffer>`{.interpreted-text
role="ref"}

Converts the string to a [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
encoded `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}. This method is slightly slower than
`to_ascii_buffer()<class_String_method_to_ascii_buffer>`{.interpreted-text
role="ref"}, but supports all UTF-8 characters. For most cases, prefer
using this method. This is the inverse of
`PackedByteArray.get_string_from_utf8()<class_PackedByteArray_method_get_string_from_utf8>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_utf16_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_utf16_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_utf16_buffer>`{.interpreted-text
role="ref"}

Converts the string to a [UTF-16](https://en.wikipedia.org/wiki/UTF-16)
encoded `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}. This is the inverse of
`PackedByteArray.get_string_from_utf16()<class_PackedByteArray_method_get_string_from_utf16>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_utf32_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_utf32_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_utf32_buffer>`{.interpreted-text
role="ref"}

Converts the string to a [UTF-32](https://en.wikipedia.org/wiki/UTF-32)
encoded `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}. This is the inverse of
`PackedByteArray.get_string_from_utf32()<class_PackedByteArray_method_get_string_from_utf32>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_to_wchar_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_wchar_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_to_wchar_buffer>`{.interpreted-text
role="ref"}

Converts the string to a [wide
character](https://en.wikipedia.org/wiki/Wide_character) (`wchar_t`,
UTF-16 on Windows, UTF-32 on other platforms) encoded
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.
This is the inverse of
`PackedByteArray.get_string_from_wchar()<class_PackedByteArray_method_get_string_from_wchar>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_trim_prefix}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**trim_prefix**(prefix: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_trim_prefix>`{.interpreted-text
role="ref"}

Removes the given `prefix` from the start of the string, or returns the
string unchanged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_trim_suffix}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**trim_suffix**(suffix: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_trim_suffix>`{.interpreted-text
role="ref"}

Removes the given `suffix` from the end of the string, or returns the
string unchanged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_unicode_at}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **unicode_at**(at:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_unicode_at>`{.interpreted-text
role="ref"}

Returns the character code at position `at`.

See also `chr()<class_String_method_chr>`{.interpreted-text role="ref"},
`@GDScript.char()<class_@GDScript_method_char>`{.interpreted-text
role="ref"}, and
`@GDScript.ord()<class_@GDScript_method_ord>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_uri_decode}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **uri_decode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_uri_decode>`{.interpreted-text
role="ref"}

Decodes the string from its URL-encoded format. This method is meant to
properly decode the parameters in a URL when receiving an HTTP request.
See also
`uri_encode()<class_String_method_uri_encode>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var url = \"\$DOCS_URL/?highlight=Godot%20Engine%3%docs\"
print(url.uri_decode()) \# Prints \"\$DOCS_URL/?highlight=Godot
Engine:docs\"
:::

::: code-tab
csharp

var url = \"\$DOCS_URL/?highlight=Godot%20Engine%3%docs\"
GD.Print(url.URIDecode()) // Prints \"\$DOCS_URL/?highlight=Godot
Engine:docs\"
:::
:::::

\*\*Note:\*\* This method decodes `+` as space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_uri_encode}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **uri_encode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_uri_encode>`{.interpreted-text
role="ref"}

Encodes the string to URL-friendly format. This method is meant to
properly encode the parameters in a URL when sending an HTTP request.
See also
`uri_decode()<class_String_method_uri_decode>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var prefix = \"\$DOCS_URL/?highlight=\" var url = prefix + \"Godot
Engine:docs\".uri_encode()

print(url) \# Prints \"\$DOCS_URL/?highlight=Godot%20Engine%3%docs\"
:::

::: code-tab
csharp

var prefix = \"\$DOCS_URL/?highlight=\"; var url = prefix + \"Godot
Engine:docs\".URIEncode();

GD.Print(url); // Prints \"\$DOCS_URL/?highlight=Godot%20Engine%3%docs\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_uri_file_decode}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**uri_file_decode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_uri_file_decode>`{.interpreted-text
role="ref"}

Decodes the file path from its URL-encoded format. Unlike
`uri_decode()<class_String_method_uri_decode>`{.interpreted-text
role="ref"} this method leaves `+` as is.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_validate_filename}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**validate_filename**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_validate_filename>`{.interpreted-text
role="ref"}

Returns a copy of the string with all characters that are not allowed in
`is_valid_filename()<class_String_method_is_valid_filename>`{.interpreted-text
role="ref"} replaced with underscores.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_validate_node_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**validate_node_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_String_method_validate_node_name>`{.interpreted-text
role="ref"}

Returns a copy of the string with all characters that are not allowed in
`Node.name<class_Node_property_name>`{.interpreted-text role="ref"} (`.`
`:` `@` `/` `"` `%`) replaced with underscores.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_xml_escape}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**xml_escape**(escape_quotes: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_xml_escape>`{.interpreted-text
role="ref"}

Returns a copy of the string with special characters escaped using the
XML standard. If `escape_quotes` is `true`, the single quote (`'`) and
double quote (`"`) characters are also escaped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_method_xml_unescape}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **xml_unescape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_String_method_xml_unescape>`{.interpreted-text
role="ref"}

Returns a copy of the string with escaped characters replaced by their
meanings according to the XML standard.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_String_operator_neq_String}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_String_operator_neq_String>`{.interpreted-text role="ref"}

Returns `true` if both strings do not contain the same sequence of
characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_neq_StringName}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_String_operator_neq_StringName>`{.interpreted-text role="ref"}

Returns `true` if this **String** is not equivalent to the given
`StringName<class_StringName>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_mod_Variant}
::: rst-class
classref-operator
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **operator
%**(right: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_String_operator_mod_Variant>`{.interpreted-text role="ref"}

Formats the **String**, replacing the placeholders with one or more
parameters. To pass multiple parameters, `right` needs to be an
`Array<class_Array>`{.interpreted-text role="ref"}.

    print("I caught %d fishes!" % 2) # Prints "I caught 2 fishes!"

    var my_message = "Travelling to %s, at %2.2f km/h."
    var location = "Deep Valley"
    var speed = 40.3485
    print(my_message % [location, speed]) # Prints "Travelling to Deep Valley, at 40.35 km/h."

For more information, see the
`GDScript format strings <../tutorials/scripting/gdscript/gdscript_format_string>`{.interpreted-text
role="doc"} tutorial.

\*\*Note:\*\* In C#, this operator is not available. Instead, see [how
to interpolate strings with
\"\$\"](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_sum_String}
::: rst-class
classref-operator
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **operator
+**(right: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_String_operator_sum_String>`{.interpreted-text role="ref"}

Appends `right` at the end of this **String**, also known as a string
concatenation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_sum_StringName}
::: rst-class
classref-operator
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **operator
+**(right: `StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_String_operator_sum_StringName>`{.interpreted-text role="ref"}

Appends `right` at the end of this **String**, returning a **String**.
This is also known as a string concatenation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_lt_String}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_String_operator_lt_String>`{.interpreted-text role="ref"}

Returns `true` if the left **String** comes before `right` in [Unicode
order](https://en.wikipedia.org/wiki/List_of_Unicode_characters), which
roughly matches the alphabetical order. Useful for sorting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_lte_String}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_String_operator_lte_String>`{.interpreted-text role="ref"}

Returns `true` if the left **String** comes before `right` in [Unicode
order](https://en.wikipedia.org/wiki/List_of_Unicode_characters), which
roughly matches the alphabetical order, or if both are equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_eq_String}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_String_operator_eq_String>`{.interpreted-text role="ref"}

Returns `true` if both strings contain the same sequence of characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_eq_StringName}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_String_operator_eq_StringName>`{.interpreted-text role="ref"}

Returns `true` if this **String** is equivalent to the given
`StringName<class_StringName>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_gt_String}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_String_operator_gt_String>`{.interpreted-text role="ref"}

Returns `true` if the left **String** comes after `right` in [Unicode
order](https://en.wikipedia.org/wiki/List_of_Unicode_characters), which
roughly matches the alphabetical order. Useful for sorting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_gte_String}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_String_operator_gte_String>`{.interpreted-text role="ref"}

Returns `true` if the left **String** comes after `right` in [Unicode
order](https://en.wikipedia.org/wiki/List_of_Unicode_characters), which
roughly matches the alphabetical order, or if both are equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_String_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_String_operator_idx_int>`{.interpreted-text role="ref"}

Returns a new **String** that only contains the character at `index`.
Indices start from `0`. If `index` is greater or equal to `0`, the
character is fetched starting from the beginning of the string. If
`index` is a negative value, it is fetched starting from the end.
Accessing a string out-of-bounds will cause a run-time error, pausing
the project execution if run from the editor.
