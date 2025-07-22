github_url
:   hide

# Array {#class_Array}

A built-in data structure that holds a sequence of elements.

::: rst-class
classref-introduction-group
:::

## Description

An array data structure that can contain a sequence of elements of any
`Variant<class_Variant>`{.interpreted-text role="ref"} type. Elements
are accessed by a numerical index starting at `0`. Negative indices are
used to count from the back (`-1` is the last element, `-2` is the
second to last, etc.).

::::: tabs
::: code-tab
gdscript

var array = \[\"First\", 2, 3, \"Last\"\] print(array\[0\]) \# Prints
\"First\" print(array\[2\]) \# Prints 3 print(array\[-1\]) \# Prints
\"Last\"

array\[1\] = \"Second\" print(array\[1\]) \# Prints \"Second\"
print(array\[-3\]) \# Prints \"Second\"
:::

::: code-tab
csharp

Godot.Collections.Array array = \[\"First\", 2, 3, \"Last\"\];
GD.Print(array\[0\]); // Prints \"First\" GD.Print(array\[2\]); //
Prints 3 GD.Print(array\[\^1\]); // Prints \"Last\"

array\[1\] = \"Second\"; GD.Print(array\[1\]); // Prints \"Second\"
GD.Print(array\[\^3\]); // Prints \"Second\"
:::
:::::

\*\*Note:\*\* Arrays are always passed by **reference**. To get a copy
of an array that can be modified independently of the original array,
use `duplicate()<class_Array_method_duplicate>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Erasing elements while iterating over arrays is **not**
supported and will result in unpredictable behavior.

\*\*Differences between packed arrays, typed arrays, and untyped
arrays:\*\* Packed arrays are generally faster to iterate on and modify
compared to a typed array of the same type (e.g.
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
versus `Array[int]`). Also, packed arrays consume less memory. As a
downside, packed arrays are less flexible as they don\'t offer as many
convenience methods such as
`map()<class_Array_method_map>`{.interpreted-text role="ref"}. Typed
arrays are in turn faster to iterate on and modify than untyped arrays.

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

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

:::: {#class_Array_constructor_Array}
::: rst-class
classref-constructor
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**()
`🔗<class_Array_constructor_Array>`{.interpreted-text role="ref"}

Constructs an empty **Array**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(base:
`Array<class_Array>`{.interpreted-text role="ref"}, type:
`int<class_int>`{.interpreted-text role="ref"}, class_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, script:
`Variant<class_Variant>`{.interpreted-text role="ref"})

Creates a typed array from the `base` array. A typed array can only
contain elements of the given type, or that inherit from the given
class, as described by this constructor\'s parameters:

- `type` is the built-in `Variant<class_Variant>`{.interpreted-text
  role="ref"} type, as one the
  `Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
  role="ref"} constants.
- `class_name` is the built-in class name (see
  `Object.get_class()<class_Object_method_get_class>`{.interpreted-text
  role="ref"}).
- `script` is the associated script. It must be a
  `Script<class_Script>`{.interpreted-text role="ref"} instance or
  `null`.

If `type` is not
`@GlobalScope.TYPE_OBJECT<class_@GlobalScope_constant_TYPE_OBJECT>`{.interpreted-text
role="ref"}, `class_name` must be an empty
`StringName<class_StringName>`{.interpreted-text role="ref"} and
`script` must be `null`.

    class_name Sword
    extends Node

    class Stats:
        pass

    func _ready():
        var a = Array([], TYPE_INT, "", null)               # Array[int]
        var b = Array([], TYPE_OBJECT, "Node", null)        # Array[Node]
        var c = Array([], TYPE_OBJECT, "Node", Sword)       # Array[Sword]
        var d = Array([], TYPE_OBJECT, "RefCounted", Stats) # Array[Stats]

The `base` array\'s elements are converted when necessary. If this is
not possible or `base` is already typed, this constructor fails and
returns an empty **Array**.

In GDScript, this constructor is usually not necessary, as it is
possible to create a typed array through static typing:

    var numbers: Array[float] = []
    var children: Array[Node] = [$Node, $Sprite2D, $RigidBody3D]

    var integers: Array[int] = [0.2, 4.5, -2.0]
    print(integers) # Prints [0, 4, -2]

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`Array<class_Array>`{.interpreted-text role="ref"})

Returns the same array as `from`. If you need a copy of the array, use
`duplicate()<class_Array_method_duplicate>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})

Constructs an array from a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"})

Constructs an array from a
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})

Constructs an array from a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"})

Constructs an array from a
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})

Constructs an array from a
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"})

Constructs an array from a
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})

Constructs an array from a
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})

Constructs an array from a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"})

Constructs an array from a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Array<class_Array>`{.interpreted-text role="ref"} **Array**(from:
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"})

Constructs an array from a
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Array_method_all}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **all**(method:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_all>`{.interpreted-text role="ref"}

Calls the given `Callable<class_Callable>`{.interpreted-text role="ref"}
on each element in the array and returns `true` if the
`Callable<class_Callable>`{.interpreted-text role="ref"} returns `true`
for *all* elements in the array. If the
`Callable<class_Callable>`{.interpreted-text role="ref"} returns `false`
for one array element or more, this method returns `false`.

The `method` should take one `Variant<class_Variant>`{.interpreted-text
role="ref"} parameter (the current array element) and return a
`bool<class_bool>`{.interpreted-text role="ref"}.

::::: tabs
::: code-tab
gdscript

func greater_than_5(number):

:   return number \> 5

func [ready]{#ready}():

:   print(\[6, 10, 6\].all(greater_than_5)) \# Prints true (3/3 elements
    evaluate to true). print(\[4, 10, 4\].all(greater_than_5)) \# Prints
    false (1/3 elements evaluate to true). print(\[4, 4,
    4\].all(greater_than_5)) \# Prints false (0/3 elements evaluate to
    true). print(\[\].all(greater_than_5)) \# Prints true (0/0 elements
    evaluate to true).

    \# Same as the first line above, but using a lambda function.
    print(\[6, 10, 6\].all(func(element): return element \> 5)) \#
    Prints true
:::

::: code-tab
csharp

private static bool GreaterThan5(int number) { return number \> 5; }

public override void [Ready]{#ready}() { // Prints True (3/3 elements
evaluate to true). GD.Print(new Godot.Collections.Array\>int\< { 6, 10,
6 }.All(GreaterThan5)); // Prints False (1/3 elements evaluate to true).
GD.Print(new Godot.Collections.Array\>int\< { 4, 10, 4
}.All(GreaterThan5)); // Prints False (0/3 elements evaluate to true).
GD.Print(new Godot.Collections.Array\>int\< { 4, 4, 4
}.All(GreaterThan5)); // Prints True (0/0 elements evaluate to true).
GD.Print(new Godot.Collections.Array\>int\< { }.All(GreaterThan5));

> // Same as the first line above, but using a lambda function.
> GD.Print(new Godot.Collections.Array\>int\< { 6, 10, 6 }.All(element
> =\> element \> 5)); // Prints True

}
:::
:::::

See also `any()<class_Array_method_any>`{.interpreted-text role="ref"},
`filter()<class_Array_method_filter>`{.interpreted-text role="ref"},
`map()<class_Array_method_map>`{.interpreted-text role="ref"} and
`reduce()<class_Array_method_reduce>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Unlike relying on the size of an array returned by
`filter()<class_Array_method_filter>`{.interpreted-text role="ref"},
this method will return as early as possible to improve performance
(especially with large arrays).

\*\*Note:\*\* For an empty array, this method
[always](https://en.wikipedia.org/wiki/Vacuous_truth) returns `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_any}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **any**(method:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_any>`{.interpreted-text role="ref"}

Calls the given `Callable<class_Callable>`{.interpreted-text role="ref"}
on each element in the array and returns `true` if the
`Callable<class_Callable>`{.interpreted-text role="ref"} returns `true`
for *one or more* elements in the array. If the
`Callable<class_Callable>`{.interpreted-text role="ref"} returns `false`
for all elements in the array, this method returns `false`.

The `method` should take one `Variant<class_Variant>`{.interpreted-text
role="ref"} parameter (the current array element) and return a
`bool<class_bool>`{.interpreted-text role="ref"}.

    func greater_than_5(number):
        return number > 5

    func _ready():
        print([6, 10, 6].any(greater_than_5)) # Prints true (3 elements evaluate to true).
        print([4, 10, 4].any(greater_than_5)) # Prints true (1 elements evaluate to true).
        print([4, 4, 4].any(greater_than_5))  # Prints false (0 elements evaluate to true).
        print([].any(greater_than_5))         # Prints false (0 elements evaluate to true).

        # Same as the first line above, but using a lambda function.
        print([6, 10, 6].any(func(number): return number > 5)) # Prints true

See also `all()<class_Array_method_all>`{.interpreted-text role="ref"},
`filter()<class_Array_method_filter>`{.interpreted-text role="ref"},
`map()<class_Array_method_map>`{.interpreted-text role="ref"} and
`reduce()<class_Array_method_reduce>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Unlike relying on the size of an array returned by
`filter()<class_Array_method_filter>`{.interpreted-text role="ref"},
this method will return as early as possible to improve performance
(especially with large arrays).

\*\*Note:\*\* For an empty array, this method always returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_append}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append**(value: `Variant<class_Variant>`{.interpreted-text
role="ref"}) `🔗<class_Array_method_append>`{.interpreted-text
role="ref"}

Appends `value` at the end of the array (alias of
`push_back()<class_Array_method_push_back>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_append_array}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_array**(array: `Array<class_Array>`{.interpreted-text
role="ref"}) `🔗<class_Array_method_append_array>`{.interpreted-text
role="ref"}

Appends another `array` at the end of this array.

    var numbers = [1, 2, 3]
    var extra = [4, 5, 6]
    numbers.append_array(extra)
    print(numbers) # Prints [1, 2, 3, 4, 5, 6]

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_assign}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**assign**(array: `Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Array_method_assign>`{.interpreted-text role="ref"}

Assigns elements of another `array` into the array. Resizes the array to
match `array`. Performs type conversions if the array is typed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_back}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **back**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_back>`{.interpreted-text role="ref"}

Returns the last element of the array. If the array is empty, fails and
returns `null`. See also
`front()<class_Array_method_front>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Unlike with the `[]` operator (`array[-1]`), an error is
generated without stopping project execution.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_bsearch}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bsearch**(value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, before:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_bsearch>`{.interpreted-text
role="ref"}

Returns the index of `value` in the sorted array. If it cannot be found,
returns where `value` should be inserted to keep the array sorted. The
algorithm used is [binary
search](https://en.wikipedia.org/wiki/Binary_search_algorithm).

If `before` is `true` (as by default), the returned index comes before
all existing elements equal to `value` in the array.

    var numbers = [2, 4, 8, 10]
    var idx = numbers.bsearch(7)

    numbers.insert(idx, 7)
    print(numbers) # Prints [2, 4, 7, 8, 10]

    var fruits = ["Apple", "Lemon", "Lemon", "Orange"]
    print(fruits.bsearch("Lemon", true))  # Prints 1, points at the first "Lemon".
    print(fruits.bsearch("Lemon", false)) # Prints 3, points at "Orange".

\*\*Note:\*\* Calling
`bsearch()<class_Array_method_bsearch>`{.interpreted-text role="ref"} on
an *unsorted* array will result in unexpected behavior. Use
`sort()<class_Array_method_sort>`{.interpreted-text role="ref"} before
calling this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_bsearch_custom}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bsearch_custom**(value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, func:
`Callable<class_Callable>`{.interpreted-text role="ref"}, before:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_bsearch_custom>`{.interpreted-text
role="ref"}

Returns the index of `value` in the sorted array. If it cannot be found,
returns where `value` should be inserted to keep the array sorted (using
`func` for the comparisons). The algorithm used is [binary
search](https://en.wikipedia.org/wiki/Binary_search_algorithm).

Similar to
`sort_custom()<class_Array_method_sort_custom>`{.interpreted-text
role="ref"}, `func` is called as many times as necessary, receiving one
array element and `value` as arguments. The function should return
`true` if the array element should be *behind* `value`, otherwise it
should return `false`.

If `before` is `true` (as by default), the returned index comes before
all existing elements equal to `value` in the array.

    func sort_by_amount(a, b):
        if a[1] < b[1]:
            return true
        return false

    func _ready():
        var my_items = [["Tomato", 2], ["Kiwi", 5], ["Rice", 9]]

        var apple = ["Apple", 5]
        # "Apple" is inserted before "Kiwi".
        my_items.insert(my_items.bsearch_custom(apple, sort_by_amount, true), apple)

        var banana = ["Banana", 5]
        # "Banana" is inserted after "Kiwi".
        my_items.insert(my_items.bsearch_custom(banana, sort_by_amount, false), banana)

        # Prints [["Tomato", 2], ["Apple", 5], ["Kiwi", 5], ["Banana", 5], ["Rice", 9]]
        print(my_items)

\*\*Note:\*\* Calling
`bsearch_custom()<class_Array_method_bsearch_custom>`{.interpreted-text
role="ref"} on an *unsorted* array will result in unexpected behavior.
Use `sort_custom()<class_Array_method_sort_custom>`{.interpreted-text
role="ref"} with `func` before calling this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_Array_method_clear>`{.interpreted-text role="ref"}

Removes all elements from the array. This is equivalent to using
`resize()<class_Array_method_resize>`{.interpreted-text role="ref"} with
a size of `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **count**(value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_count>`{.interpreted-text
role="ref"}

Returns the number of times an element is in the array.

To count how many elements in an array satisfy a condition, see
`reduce()<class_Array_method_reduce>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_duplicate}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **duplicate**(deep:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_duplicate>`{.interpreted-text
role="ref"}

Returns a new copy of the array.

By default, a **shallow** copy is returned: all nested **Array**,
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}, and
`Resource<class_Resource>`{.interpreted-text role="ref"} elements are
shared with the original array. Modifying any of those in one array will
also affect them in the other.

If `deep` is `true`, a **deep** copy is returned: all nested arrays and
dictionaries are also duplicated (recursively). Any
`Resource<class_Resource>`{.interpreted-text role="ref"} is still shared
with the original array, though.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_duplicate_deep}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**duplicate_deep**(deep_subresources_mode:
`int<class_int>`{.interpreted-text role="ref"} = 1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_duplicate_deep>`{.interpreted-text
role="ref"}

Duplicates this array, deeply, like
`duplicate()<class_Array_method_duplicate>`{.interpreted-text
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

:::: {#class_Array_method_erase}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase**(value: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Array_method_erase>`{.interpreted-text role="ref"}

Finds and removes the first occurrence of `value` from the array. If
`value` does not exist in the array, nothing happens. To remove an
element by index, use
`remove_at()<class_Array_method_remove_at>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* This method shifts every element\'s index after the
removed `value` back, which may have a noticeable performance cost,
especially on larger arrays.

\*\*Note:\*\* Erasing elements while iterating over arrays is **not**
supported and will result in unpredictable behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_fill}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **fill**(value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Array_method_fill>`{.interpreted-text role="ref"}

Assigns the given `value` to all elements in the array.

This method can often be combined with
`resize()<class_Array_method_resize>`{.interpreted-text role="ref"} to
create an array with a given size and initialized elements:

::::: tabs
::: code-tab
gdscript

var array = \[\] array.resize(5) array.fill(2) print(array) \# Prints
\[2, 2, 2, 2, 2\]
:::

::: code-tab
csharp

Godot.Collections.Array array = \[\]; array.Resize(5); array.Fill(2);
GD.Print(array); // Prints \[2, 2, 2, 2, 2\]
:::
:::::

\*\*Note:\*\* If `value` is a `Variant<class_Variant>`{.interpreted-text
role="ref"} passed by reference
(`Object<class_Object>`{.interpreted-text role="ref"}-derived,
**Array**, `Dictionary<class_Dictionary>`{.interpreted-text role="ref"},
etc.), the array will be filled with references to the same `value`,
which are not duplicates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_filter}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **filter**(method:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_filter>`{.interpreted-text
role="ref"}

Calls the given `Callable<class_Callable>`{.interpreted-text role="ref"}
on each element in the array and returns a new, filtered **Array**.

The `method` receives one of the array elements as an argument, and
should return `true` to add the element to the filtered array, or
`false` to exclude it.

    func is_even(number):
        return number % 2 == 0

    func _ready():
        print([1, 4, 5, 8].filter(is_even)) # Prints [4, 8]

        # Same as above, but using a lambda function.
        print([1, 4, 5, 8].filter(func(number): return number % 2 == 0))

See also `any()<class_Array_method_any>`{.interpreted-text role="ref"},
`all()<class_Array_method_all>`{.interpreted-text role="ref"},
`map()<class_Array_method_map>`{.interpreted-text role="ref"} and
`reduce()<class_Array_method_reduce>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_find}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find**(what:
`Variant<class_Variant>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_find>`{.interpreted-text role="ref"}

Returns the index of the **first** occurrence of `what` in this array,
or `-1` if there are none. The search\'s start can be specified with
`from`, continuing to the end of the array.

\*\*Note:\*\* If you just want to know whether the array contains
`what`, use `has()<class_Array_method_has>`{.interpreted-text
role="ref"} (`Contains` in C#). In GDScript, you may also use the `in`
operator.

\*\*Note:\*\* For performance reasons, the search is affected by
`what`\'s
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"}. For example, `7` (`int<class_int>`{.interpreted-text
role="ref"}) and `7.0` (`float<class_float>`{.interpreted-text
role="ref"}) are not considered equal for this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_find_custom}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find_custom**(method:
`Callable<class_Callable>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_find_custom>`{.interpreted-text
role="ref"}

Returns the index of the **first** element in the array that causes
`method` to return `true`, or `-1` if there are none. The search\'s
start can be specified with `from`, continuing to the end of the array.

`method` is a callable that takes an element of the array, and returns a
`bool<class_bool>`{.interpreted-text role="ref"}.

\*\*Note:\*\* If you just want to know whether the array contains
*anything* that satisfies `method`, use
`any()<class_Array_method_any>`{.interpreted-text role="ref"}.

:::: tabs
::: code-tab
gdscript

func is_even(number):

:   return number % 2 == 0

func [ready]{#ready}():

:   print(\[1, 3, 4, 7\].find_custom(is_even.bind())) \# Prints 2
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_front}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **front**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_front>`{.interpreted-text
role="ref"}

Returns the first element of the array. If the array is empty, fails and
returns `null`. See also
`back()<class_Array_method_back>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Unlike with the `[]` operator (`array[0]`), an error is
generated without stopping project execution.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_get}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **get**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_get>`{.interpreted-text role="ref"}

Returns the element at the given `index` in the array. If `index`
out-of-bounds or negative, this method fails and returns `null`.

This method is similar (but not identical) to the `[]` operator. Most
notably, when this method fails, it doesn\'t pause project execution if
run from the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_get_typed_builtin}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_typed_builtin**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Array_method_get_typed_builtin>`{.interpreted-text role="ref"}

Returns the built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type of the typed array as a
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} constant. If the array is not typed, returns
`@GlobalScope.TYPE_NIL<class_@GlobalScope_constant_TYPE_NIL>`{.interpreted-text
role="ref"}. See also
`is_typed()<class_Array_method_is_typed>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_get_typed_class_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_typed_class_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Array_method_get_typed_class_name>`{.interpreted-text
role="ref"}

Returns the **built-in** class name of the typed array, if the built-in
`Variant<class_Variant>`{.interpreted-text role="ref"} type
`@GlobalScope.TYPE_OBJECT<class_@GlobalScope_constant_TYPE_OBJECT>`{.interpreted-text
role="ref"}. Otherwise, returns an empty
`StringName<class_StringName>`{.interpreted-text role="ref"}. See also
`is_typed()<class_Array_method_is_typed>`{.interpreted-text role="ref"}
and
`Object.get_class()<class_Object_method_get_class>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_get_typed_script}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_typed_script**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_get_typed_script>`{.interpreted-text
role="ref"}

Returns the `Script<class_Script>`{.interpreted-text role="ref"}
instance associated with this typed array, or `null` if it does not
exist. See also
`is_typed()<class_Array_method_is_typed>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_has}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has**(value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_has>`{.interpreted-text role="ref"}

Returns `true` if the array contains the given `value`.

::::: tabs
::: code-tab
gdscript

print(\[\"inside\", 7\].has(\"inside\")) \# Prints true
print(\[\"inside\", 7\].has(\"outside\")) \# Prints false
print(\[\"inside\", 7\].has(7)) \# Prints true print(\[\"inside\",
7\].has(\"7\")) \# Prints false
:::

::: code-tab
csharp

Godot.Collections.Array arr = \[\"inside\", 7\]; // By C# convention,
this method is renamed to [Contains]{.title-ref}.
GD.Print(arr.Contains(\"inside\")); // Prints True
GD.Print(arr.Contains(\"outside\")); // Prints False
GD.Print(arr.Contains(7)); // Prints True GD.Print(arr.Contains(\"7\"));
// Prints False
:::
:::::

In GDScript, this is equivalent to the `in` operator:

    if 4 in [2, 4, 6, 8]:
        print("4 is here!") # Will be printed.

\*\*Note:\*\* For performance reasons, the search is affected by the
`value`\'s
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"}. For example, `7` (`int<class_int>`{.interpreted-text
role="ref"}) and `7.0` (`float<class_float>`{.interpreted-text
role="ref"}) are not considered equal for this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_hash}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hash**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_hash>`{.interpreted-text role="ref"}

Returns a hashed 32-bit integer value representing the array and its
contents.

\*\*Note:\*\* Arrays with equal hash values are *not* guaranteed to be
the same, as a result of hash collisions. On the countrary, arrays with
different hash values are guaranteed to be different.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_insert}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **insert**(position:
`int<class_int>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Array_method_insert>`{.interpreted-text role="ref"}

Inserts a new element (`value`) at a given index (`position`) in the
array. `position` should be between `0` and the array\'s
`size()<class_Array_method_size>`{.interpreted-text role="ref"}. If
negative, `position` is considered relative to the end of the array.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the other
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} constants
if this method fails.

\*\*Note:\*\* Every element\'s index after `position` needs to be
shifted forward, which may have a noticeable performance cost,
especially on larger arrays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the array is empty (`[]`). See also
`size()<class_Array_method_size>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_is_read_only}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_read_only**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_is_read_only>`{.interpreted-text
role="ref"}

Returns `true` if the array is read-only. See
`make_read_only()<class_Array_method_make_read_only>`{.interpreted-text
role="ref"}.

In GDScript, arrays are automatically read-only if declared with the
`const` keyword.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_is_same_typed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_same_typed**(array: `Array<class_Array>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_is_same_typed>`{.interpreted-text
role="ref"}

Returns `true` if this array is typed the same as the given `array`. See
also `is_typed()<class_Array_method_is_typed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_is_typed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_typed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_is_typed>`{.interpreted-text
role="ref"}

Returns `true` if the array is typed. Typed arrays can only contain
elements of a specific type, as defined by the typed array constructor.
The methods of a typed array are still expected to return a generic
`Variant<class_Variant>`{.interpreted-text role="ref"}.

In GDScript, it is possible to define a typed array with static typing:

    var numbers: Array[float] = [0.2, 4.2, -2.0]
    print(numbers.is_typed()) # Prints true

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_make_read_only}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_read_only**()
`🔗<class_Array_method_make_read_only>`{.interpreted-text role="ref"}

Makes the array read-only. The array\'s elements cannot be overridden
with different values, and their order cannot change. Does not apply to
nested elements, such as dictionaries.

In GDScript, arrays are automatically read-only if declared with the
`const` keyword.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_map}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **map**(method:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_map>`{.interpreted-text role="ref"}

Calls the given `Callable<class_Callable>`{.interpreted-text role="ref"}
for each element in the array and returns a new array filled with values
returned by the `method`.

The `method` should take one `Variant<class_Variant>`{.interpreted-text
role="ref"} parameter (the current array element) and can return any
`Variant<class_Variant>`{.interpreted-text role="ref"}.

    func double(number):
        return number * 2

    func _ready():
        print([1, 2, 3].map(double)) # Prints [2, 4, 6]

        # Same as above, but using a lambda function.
        print([1, 2, 3].map(func(element): return element * 2))

See also `filter()<class_Array_method_filter>`{.interpreted-text
role="ref"}, `reduce()<class_Array_method_reduce>`{.interpreted-text
role="ref"}, `any()<class_Array_method_any>`{.interpreted-text
role="ref"} and `all()<class_Array_method_all>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_max}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **max**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_max>`{.interpreted-text role="ref"}

Returns the maximum value contained in the array, if all elements can be
compared. Otherwise, returns `null`. See also
`min()<class_Array_method_min>`{.interpreted-text role="ref"}.

To find the maximum value using a custom comparator, you can use
`reduce()<class_Array_method_reduce>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_min}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **min**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_min>`{.interpreted-text role="ref"}

Returns the minimum value contained in the array, if all elements can be
compared. Otherwise, returns `null`. See also
`max()<class_Array_method_max>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_pick_random}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **pick_random**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_pick_random>`{.interpreted-text
role="ref"}

Returns a random element from the array. Generates an error and returns
`null` if the array is empty.

::::: tabs
::: code-tab
gdscript

\# May print 1, 2, 3.25, or \"Hi\". print(\[1, 2, 3.25,
\"Hi\"\].pick_random())
:::

::: code-tab
csharp

Godot.Collections.Array array = \[1, 2, 3.25f, \"Hi\"\];
GD.Print(array.PickRandom()); // May print 1, 2, 3.25, or \"Hi\".
:::
:::::

\*\*Note:\*\* Like many similar functions in the engine (such as
`@GlobalScope.randi()<class_@GlobalScope_method_randi>`{.interpreted-text
role="ref"} or `shuffle()<class_Array_method_shuffle>`{.interpreted-text
role="ref"}), this method uses a common, global random seed. To get a
predictable outcome from this method, see
`@GlobalScope.seed()<class_@GlobalScope_method_seed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_pop_at}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**pop_at**(position: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Array_method_pop_at>`{.interpreted-text role="ref"}

Removes and returns the element of the array at index `position`. If
negative, `position` is considered relative to the end of the array.
Returns `null` if the array is empty. If `position` is out of bounds, an
error message is also generated.

\*\*Note:\*\* This method shifts every element\'s index after `position`
back, which may have a noticeable performance cost, especially on larger
arrays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_pop_back}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **pop_back**()
`🔗<class_Array_method_pop_back>`{.interpreted-text role="ref"}

Removes and returns the last element of the array. Returns `null` if the
array is empty, without generating an error. See also
`pop_front()<class_Array_method_pop_front>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_pop_front}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **pop_front**()
`🔗<class_Array_method_pop_front>`{.interpreted-text role="ref"}

Removes and returns the first element of the array. Returns `null` if
the array is empty, without generating an error. See also
`pop_back()<class_Array_method_pop_back>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This method shifts every other element\'s index back,
which may have a noticeable performance cost, especially on larger
arrays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_push_back}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_back**(value: `Variant<class_Variant>`{.interpreted-text
role="ref"}) `🔗<class_Array_method_push_back>`{.interpreted-text
role="ref"}

Appends an element at the end of the array. See also
`push_front()<class_Array_method_push_front>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_push_front}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_front**(value: `Variant<class_Variant>`{.interpreted-text
role="ref"}) `🔗<class_Array_method_push_front>`{.interpreted-text
role="ref"}

Adds an element at the beginning of the array. See also
`push_back()<class_Array_method_push_back>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method shifts every other element\'s index forward,
which may have a noticeable performance cost, especially on larger
arrays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_reduce}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**reduce**(method: `Callable<class_Callable>`{.interpreted-text
role="ref"}, accum: `Variant<class_Variant>`{.interpreted-text
role="ref"} = null)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_reduce>`{.interpreted-text
role="ref"}

Calls the given `Callable<class_Callable>`{.interpreted-text role="ref"}
for each element in array, accumulates the result in `accum`, then
returns it.

The `method` takes two arguments: the current value of `accum` and the
current array element. If `accum` is `null` (as by default), the
iteration will start from the second element, with the first one used as
initial value of `accum`.

    func sum(accum, number):
        return accum + number

    func _ready():
        print([1, 2, 3].reduce(sum, 0))  # Prints 6
        print([1, 2, 3].reduce(sum, 10)) # Prints 16

        # Same as above, but using a lambda function.
        print([1, 2, 3].reduce(func(accum, number): return accum + number, 10))

If `max()<class_Array_method_max>`{.interpreted-text role="ref"} is not
desirable, this method may also be used to implement a custom
comparator:

    func _ready():
        var arr = [Vector2i(5, 0), Vector2i(3, 4), Vector2i(1, 2)]

        var longest_vec = arr.reduce(func(max, vec): return vec if is_length_greater(vec, max) else max)
        print(longest_vec) # Prints (3, 4)

    func is_length_greater(a, b):
        return a.length() > b.length()

This method can also be used to count how many elements in an array
satisfy a certain condition, similar to
`count()<class_Array_method_count>`{.interpreted-text role="ref"}:

    func is_even(number):
        return number % 2 == 0

    func _ready():
        var arr = [1, 2, 3, 4, 5]
        # If the current element is even, increment count, otherwise leave count the same.
        var even_count = arr.reduce(func(count, next): return count + 1 if is_even(next) else count, 0)
        print(even_count) # Prints 2

See also `map()<class_Array_method_map>`{.interpreted-text role="ref"},
`filter()<class_Array_method_filter>`{.interpreted-text role="ref"},
`any()<class_Array_method_any>`{.interpreted-text role="ref"}, and
`all()<class_Array_method_all>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_remove_at}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_at**(position: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Array_method_remove_at>`{.interpreted-text role="ref"}

Removes the element from the array at the given index (`position`). If
the index is out of bounds, this method fails. If the index is negative,
`position` is considered relative to the end of the array.

If you need to return the removed element, use
`pop_at()<class_Array_method_pop_at>`{.interpreted-text role="ref"}. To
remove an element by value, use
`erase()<class_Array_method_erase>`{.interpreted-text role="ref"}
instead.

\*\*Note:\*\* This method shifts every element\'s index after `position`
back, which may have a noticeable performance cost, especially on larger
arrays.

\*\*Note:\*\* The `position` cannot be negative. To remove an element
relative to the end of the array, use
`arr.remove_at(arr.size() - (i + 1))`. To remove the last element from
the array, use `arr.resize(arr.size() - 1)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_resize}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **resize**(size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Array_method_resize>`{.interpreted-text role="ref"}

Sets the array\'s number of elements to `size`. If `size` is smaller
than the array\'s current size, the elements at the end are removed. If
`size` is greater, new default elements (usually `null`) are added,
depending on the array\'s type.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the following
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} constants
if this method fails:
`@GlobalScope.ERR_LOCKED<class_@GlobalScope_constant_ERR_LOCKED>`{.interpreted-text
role="ref"} if the array is read-only,
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} if the size is negative, or
`@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>`{.interpreted-text
role="ref"} if allocations fail. Use
`size()<class_Array_method_size>`{.interpreted-text role="ref"} to find
the actual size of the array after resize.

\*\*Note:\*\* Calling this method once and assigning the new values is
faster than calling
`append()<class_Array_method_append>`{.interpreted-text role="ref"} for
every new element.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_reverse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reverse**()
`🔗<class_Array_method_reverse>`{.interpreted-text role="ref"}

Reverses the order of all elements in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_rfind}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rfind**(what:
`Variant<class_Variant>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_rfind>`{.interpreted-text
role="ref"}

Returns the index of the **last** occurrence of `what` in this array, or
`-1` if there are none. The search\'s start can be specified with
`from`, continuing to the beginning of the array. This method is the
reverse of `find()<class_Array_method_find>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_rfind_custom}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rfind_custom**(method:
`Callable<class_Callable>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_rfind_custom>`{.interpreted-text
role="ref"}

Returns the index of the **last** element of the array that causes
`method` to return `true`, or `-1` if there are none. The search\'s
start can be specified with `from`, continuing to the beginning of the
array. This method is the reverse of
`find_custom()<class_Array_method_find_custom>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **set**(index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Array_method_set>`{.interpreted-text role="ref"}

Sets the value of the element at the given `index` to the given `value`.
This will not change the size of the array, it only changes the value at
an index already in the array. This is the same as using the `[]`
operator (`array[index] = value`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_shuffle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **shuffle**()
`🔗<class_Array_method_shuffle>`{.interpreted-text role="ref"}

Shuffles all elements of the array in a random order.

\*\*Note:\*\* Like many similar functions in the engine (such as
`@GlobalScope.randi()<class_@GlobalScope_method_randi>`{.interpreted-text
role="ref"} or
`pick_random()<class_Array_method_pick_random>`{.interpreted-text
role="ref"}), this method uses a common, global random seed. To get a
predictable outcome from this method, see
`@GlobalScope.seed()<class_@GlobalScope_method_seed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_size>`{.interpreted-text role="ref"}

Returns the number of elements in the array. Empty arrays (`[]`) always
return `0`. See also
`is_empty()<class_Array_method_is_empty>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_slice}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **slice**(begin:
`int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"} = 2147483647, step:
`int<class_int>`{.interpreted-text role="ref"} = 1, deep:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Array_method_slice>`{.interpreted-text
role="ref"}

Returns a new **Array** containing this array\'s elements, from index
`begin` (inclusive) to `end` (exclusive), every `step` elements.

If either `begin` or `end` are negative, their value is relative to the
end of the array.

If `step` is negative, this method iterates through the array in
reverse, returning a slice ordered backwards. For this to work, `begin`
must be greater than `end`.

If `deep` is `true`, all nested **Array** and
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} elements in
the slice are duplicated from the original, recursively. See also
`duplicate()<class_Array_method_duplicate>`{.interpreted-text
role="ref"}.

    var letters = ["A", "B", "C", "D", "E", "F"]

    print(letters.slice(0, 2))  # Prints ["A", "B"]
    print(letters.slice(2, -2)) # Prints ["C", "D"]
    print(letters.slice(-2, 6)) # Prints ["E", "F"]

    print(letters.slice(0, 6, 2))  # Prints ["A", "C", "E"]
    print(letters.slice(4, 1, -1)) # Prints ["E", "D", "C"]

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_sort}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **sort**()
`🔗<class_Array_method_sort>`{.interpreted-text role="ref"}

Sorts the array in ascending order. The final order is dependent on the
\"less than\" (`<`) comparison between elements.

::::: tabs
::: code-tab
gdscript

var numbers = \[10, 5, 2.5, 8\] numbers.sort() print(numbers) \# Prints
\[2.5, 5, 8, 10\]
:::

::: code-tab
csharp

Godot.Collections.Array numbers = \[10, 5, 2.5, 8\]; numbers.Sort();
GD.Print(numbers); // Prints \[2.5, 5, 8, 10\]
:::
:::::

\*\*Note:\*\* The sorting algorithm used is not
[stable](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability).
This means that equivalent elements (such as `2` and `2.0`) may have
their order changed when calling
`sort()<class_Array_method_sort>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_method_sort_custom}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**sort_custom**(func: `Callable<class_Callable>`{.interpreted-text
role="ref"}) `🔗<class_Array_method_sort_custom>`{.interpreted-text
role="ref"}

Sorts the array using a custom
`Callable<class_Callable>`{.interpreted-text role="ref"}.

`func` is called as many times as necessary, receiving two array
elements as arguments. The function should return `true` if the first
element should be moved *before* the second one, otherwise it should
return `false`.

    func sort_ascending(a, b):
        if a[1] < b[1]:
            return true
        return false

    func _ready():
        var my_items = [["Tomato", 5], ["Apple", 9], ["Rice", 4]]
        my_items.sort_custom(sort_ascending)
        print(my_items) # Prints [["Rice", 4], ["Tomato", 5], ["Apple", 9]]

        # Sort descending, using a lambda function.
        my_items.sort_custom(func(a, b): return a[1] > b[1])
        print(my_items) # Prints [["Apple", 9], ["Tomato", 5], ["Rice", 4]]

It may also be necessary to use this method to sort strings by natural
order, with
`String.naturalnocasecmp_to()<class_String_method_naturalnocasecmp_to>`{.interpreted-text
role="ref"}, as in the following example:

    var files = ["newfile1", "newfile2", "newfile10", "newfile11"]
    files.sort_custom(func(a, b): return a.naturalnocasecmp_to(b) < 0)
    print(files) # Prints ["newfile1", "newfile2", "newfile10", "newfile11"]

\*\*Note:\*\* In C#, this method is not supported.

\*\*Note:\*\* The sorting algorithm used is not
[stable](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability).
This means that values considered equal may have their order changed
when calling this method.

\*\*Note:\*\* You should not randomize the return value of `func`, as
the heapsort algorithm expects a consistent result. Randomizing the
return value will result in unexpected behavior.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Array_operator_neq_Array}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Array_operator_neq_Array>`{.interpreted-text role="ref"}

Returns `true` if the array\'s size or its elements are different than
`right`\'s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_operator_sum_Array}
::: rst-class
classref-operator
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **operator +**(right:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Array_operator_sum_Array>`{.interpreted-text role="ref"}

Appends the `right` array to the left operand, creating a new **Array**.
This is also known as an array concatenation.

::::: tabs
::: code-tab
gdscript

var array1 = \[\"One\", 2\] var array2 = \[3, \"Four\"\] print(array1 +
array2) \# Prints \[\"One\", 2, 3, \"Four\"\]
:::

::: code-tab
csharp

// Note that concatenation is not possible with C#\'s native Array type.
Godot.Collections.Array array1 = \[\"One\", 2\]; Godot.Collections.Array
array2 = \[3, \"Four\"\]; GD.Print(array1 + array2); // Prints
\[\"One\", 2, 3, \"Four\"\]
:::
:::::

\*\*Note:\*\* For existing arrays,
`append_array()<class_Array_method_append_array>`{.interpreted-text
role="ref"} is much more efficient than concatenation and assignment
with the `+=` operator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_operator_lt_Array}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Array_operator_lt_Array>`{.interpreted-text role="ref"}

Compares the elements of both arrays in order, starting from index `0`
and ending on the last index in common between both arrays. For each
pair of elements, returns `true` if this array\'s element is less than
`right`\'s, `false` if this element is greater. Otherwise, continues to
the next pair.

If all searched elements are equal, returns `true` if this array\'s size
is less than `right`\'s, otherwise returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_operator_lte_Array}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Array_operator_lte_Array>`{.interpreted-text role="ref"}

Compares the elements of both arrays in order, starting from index `0`
and ending on the last index in common between both arrays. For each
pair of elements, returns `true` if this array\'s element is less than
`right`\'s, `false` if this element is greater. Otherwise, continues to
the next pair.

If all searched elements are equal, returns `true` if this array\'s size
is less or equal to `right`\'s, otherwise returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_operator_eq_Array}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Array_operator_eq_Array>`{.interpreted-text role="ref"}

Compares the left operand **Array** against the `right` **Array**.
Returns `true` if the sizes and contents of the arrays are equal,
`false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_operator_gt_Array}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Array_operator_gt_Array>`{.interpreted-text role="ref"}

Compares the elements of both arrays in order, starting from index `0`
and ending on the last index in common between both arrays. For each
pair of elements, returns `true` if this array\'s element is greater
than `right`\'s, `false` if this element is less. Otherwise, continues
to the next pair.

If all searched elements are equal, returns `true` if this array\'s size
is greater than `right`\'s, otherwise returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_operator_gte_Array}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Array_operator_gte_Array>`{.interpreted-text role="ref"}

Compares the elements of both arrays in order, starting from index `0`
and ending on the last index in common between both arrays. For each
pair of elements, returns `true` if this array\'s element is greater
than `right`\'s, `false` if this element is less. Otherwise, continues
to the next pair.

If all searched elements are equal, returns `true` if this array\'s size
is greater or equal to `right`\'s, otherwise returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Array_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Array_operator_idx_int>`{.interpreted-text role="ref"}

Returns the `Variant<class_Variant>`{.interpreted-text role="ref"}
element at the specified `index`. Arrays start at index 0. If `index` is
greater or equal to `0`, the element is fetched starting from the
beginning of the array. If `index` is a negative value, the element is
fetched starting from the end. Accessing an array out-of-bounds will
cause a run-time error, pausing the project execution if run from the
editor.
