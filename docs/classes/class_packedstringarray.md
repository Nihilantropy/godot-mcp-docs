github_url
:   hide

# PackedStringArray {#class_PackedStringArray}

A packed array of `String<class_String>`{.interpreted-text role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

An array specifically designed to hold
`String<class_String>`{.interpreted-text role="ref"}s. Packs data
tightly, so it saves memory for large array sizes.

If you want to join the strings in the array, use
`String.join()<class_String_method_join>`{.interpreted-text role="ref"}.

    var string_array = PackedStringArray(["hello", "world"])
    var string = " ".join(string_array)
    print(string) # "hello world"

\*\*Differences between packed arrays, typed arrays, and untyped
arrays:\*\* Packed arrays are generally faster to iterate on and modify
compared to a typed array of the same type (e.g. **PackedStringArray**
versus `Array[String]`). Also, packed arrays consume less memory. As a
downside, packed arrays are less flexible as they don\'t offer as many
convenience methods such as
`Array.map()<class_Array_method_map>`{.interpreted-text role="ref"}.
Typed arrays are in turn faster to iterate on and modify than untyped
arrays.

\*\*Note:\*\* Packed arrays are always passed by reference. To get a
copy of an array that can be modified independently of the original
array, use
`duplicate()<class_PackedStringArray_method_duplicate>`{.interpreted-text
role="ref"}. This is *not* the case for built-in properties and methods.
In these cases the returned packed array is a copy, and changing it will
*not* affect the original value. To update a built-in property of this
type, modify the returned array and then assign it to the property
again.

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

:::: {#class_PackedStringArray_constructor_PackedStringArray}
::: rst-class
classref-constructor
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **PackedStringArray**()
`🔗<class_PackedStringArray_constructor_PackedStringArray>`{.interpreted-text
role="ref"}

Constructs an empty **PackedStringArray**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **PackedStringArray**(from:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})

Constructs a **PackedStringArray** as a copy of the given
**PackedStringArray**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **PackedStringArray**(from:
`Array<class_Array>`{.interpreted-text role="ref"})

Constructs a new **PackedStringArray**. Optionally, you can pass in a
generic `Array<class_Array>`{.interpreted-text role="ref"} that will be
converted.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PackedStringArray_method_append}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **append**(value:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PackedStringArray_method_append>`{.interpreted-text
role="ref"}

Appends an element at the end of the array (alias of
`push_back()<class_PackedStringArray_method_push_back>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_append_array}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_array**(array:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_PackedStringArray_method_append_array>`{.interpreted-text
role="ref"}

Appends a **PackedStringArray** at the end of this array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_bsearch}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bsearch**(value:
`String<class_String>`{.interpreted-text role="ref"}, before:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_PackedStringArray_method_bsearch>`{.interpreted-text
role="ref"}

Finds the index of an existing value (or the insertion index that
maintains sorting order, if the value is not yet present in the array)
using binary search. Optionally, a `before` specifier can be passed. If
`false`, the returned index comes after all existing entries of the
value in the array.

\*\*Note:\*\* Calling
`bsearch()<class_PackedStringArray_method_bsearch>`{.interpreted-text
role="ref"} on an unsorted array results in unexpected behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_PackedStringArray_method_clear>`{.interpreted-text role="ref"}

Clears the array. This is equivalent to using
`resize()<class_PackedStringArray_method_resize>`{.interpreted-text
role="ref"} with a size of `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **count**(value:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedStringArray_method_count>`{.interpreted-text role="ref"}

Returns the number of times an element is in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_duplicate}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **duplicate**()
`🔗<class_PackedStringArray_method_duplicate>`{.interpreted-text
role="ref"}

Creates a copy of the array, and returns it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_erase}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **erase**(value:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PackedStringArray_method_erase>`{.interpreted-text role="ref"}

Removes the first occurrence of a value from the array and returns
`true`. If the value does not exist in the array, nothing happens and
`false` is returned. To remove an element by index, use
`remove_at()<class_PackedStringArray_method_remove_at>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_fill}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **fill**(value:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PackedStringArray_method_fill>`{.interpreted-text role="ref"}

Assigns the given value to all elements in the array. This can typically
be used together with
`resize()<class_PackedStringArray_method_resize>`{.interpreted-text
role="ref"} to create an array with a given size and initialized
elements.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_find}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find**(value:
`String<class_String>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedStringArray_method_find>`{.interpreted-text
role="ref"}

Searches the array for a value and returns its index or `-1` if not
found. Optionally, the initial search index can be passed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_get}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedStringArray_method_get>`{.interpreted-text
role="ref"}

Returns the `String<class_String>`{.interpreted-text role="ref"} at the
given `index` in the array. Returns an empty string and prints an error
if the access is out of bounds. Negative indices are not supported; they
will always consider the value to be out of bounds and return an empty
string.

This is similar to using the `[]` operator (`array[index]`), except that
operator supports negative indices and causes a debugger break if
out-of-bounds access is performed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_has}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has**(value:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedStringArray_method_has>`{.interpreted-text
role="ref"}

Returns `true` if the array contains `value`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_insert}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **insert**(at_index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PackedStringArray_method_insert>`{.interpreted-text
role="ref"}

Inserts a new element at a given position in the array. The position
must be valid, or at the end of the array (`idx == size()`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedStringArray_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the array is empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_push_back}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **push_back**(value:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PackedStringArray_method_push_back>`{.interpreted-text
role="ref"}

Appends a string element at end of the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_remove_at}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_at**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedStringArray_method_remove_at>`{.interpreted-text
role="ref"}

Removes an element from the array by index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_resize}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **resize**(new_size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedStringArray_method_resize>`{.interpreted-text
role="ref"}

Sets the size of the array. If the array is grown, reserves elements at
the end of the array. If the array is shrunk, truncates the array to the
new size. Calling
`resize()<class_PackedStringArray_method_resize>`{.interpreted-text
role="ref"} once and assigning the new values is faster than adding new
elements one by one.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the following
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} constants
if this method fails:
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} if the size is negative, or
`@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>`{.interpreted-text
role="ref"} if allocations fail. Use
`size()<class_PackedStringArray_method_size>`{.interpreted-text
role="ref"} to find the actual size of the array after resize.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_reverse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reverse**()
`🔗<class_PackedStringArray_method_reverse>`{.interpreted-text
role="ref"}

Reverses the order of the elements in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_rfind}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rfind**(value:
`String<class_String>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedStringArray_method_rfind>`{.interpreted-text role="ref"}

Searches the array in reverse order. Optionally, a start search index
can be passed. If negative, the start index is considered relative to
the end of the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **set**(index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PackedStringArray_method_set>`{.interpreted-text role="ref"}

Changes the `String<class_String>`{.interpreted-text role="ref"} at the
given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedStringArray_method_size>`{.interpreted-text
role="ref"}

Returns the number of elements in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_slice}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **slice**(begin: `int<class_int>`{.interpreted-text
role="ref"}, end: `int<class_int>`{.interpreted-text role="ref"} =
2147483647)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedStringArray_method_slice>`{.interpreted-text role="ref"}

Returns the slice of the **PackedStringArray**, from `begin` (inclusive)
to `end` (exclusive), as a new **PackedStringArray**.

The absolute value of `begin` and `end` will be clamped to the array
size, so the default value for `end` makes it slice to the size of the
array by default (i.e. `arr.slice(1)` is a shorthand for
`arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the
end of the array (i.e. `arr.slice(0, -2)` is a shorthand for
`arr.slice(0, arr.size() - 2)`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_sort}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **sort**()
`🔗<class_PackedStringArray_method_sort>`{.interpreted-text role="ref"}

Sorts the elements of the array in ascending order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_method_to_byte_array}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_byte_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedStringArray_method_to_byte_array>`{.interpreted-text
role="ref"}

Returns a `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"} with each string encoded as UTF-8. Strings are `null`
terminated.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_PackedStringArray_operator_neq_PackedStringArray}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_PackedStringArray_operator_neq_PackedStringArray>`{.interpreted-text
role="ref"}

Returns `true` if contents of the arrays differ.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_operator_sum_PackedStringArray}
::: rst-class
classref-operator
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **operator +**(right:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_PackedStringArray_operator_sum_PackedStringArray>`{.interpreted-text
role="ref"}

Returns a new **PackedStringArray** with contents of `right` added at
the end of this array. For better performance, consider using
`append_array()<class_PackedStringArray_method_append_array>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_operator_eq_PackedStringArray}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_PackedStringArray_operator_eq_PackedStringArray>`{.interpreted-text
role="ref"}

Returns `true` if contents of both arrays are the same, i.e. they have
all equal `String<class_String>`{.interpreted-text role="ref"}s at the
corresponding indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedStringArray_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedStringArray_operator_idx_int>`{.interpreted-text
role="ref"}

Returns the `String<class_String>`{.interpreted-text role="ref"} at
index `index`. Negative indices can be used to access the elements
starting from the end. Using index out of array\'s bounds will result in
an error.
