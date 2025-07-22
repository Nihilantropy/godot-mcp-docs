github_url
:   hide

# PackedFloat32Array {#class_PackedFloat32Array}

A packed array of 32-bit floating-point values.

::: rst-class
classref-introduction-group
:::

## Description

An array specifically designed to hold 32-bit floating-point values
(float). Packs data tightly, so it saves memory for large array sizes.

If you need to pack 64-bit floats tightly, see
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Packed arrays are always passed by reference. To get a
copy of an array that can be modified independently of the original
array, use
`duplicate()<class_PackedFloat32Array_method_duplicate>`{.interpreted-text
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

:::: {#class_PackedFloat32Array_constructor_PackedFloat32Array}
::: rst-class
classref-constructor
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **PackedFloat32Array**()
`🔗<class_PackedFloat32Array_constructor_PackedFloat32Array>`{.interpreted-text
role="ref"}

Constructs an empty **PackedFloat32Array**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **PackedFloat32Array**(from:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})

Constructs a **PackedFloat32Array** as a copy of the given
**PackedFloat32Array**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **PackedFloat32Array**(from:
`Array<class_Array>`{.interpreted-text role="ref"})

Constructs a new **PackedFloat32Array**. Optionally, you can pass in a
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

:::: {#class_PackedFloat32Array_method_append}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **append**(value:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PackedFloat32Array_method_append>`{.interpreted-text
role="ref"}

Appends an element at the end of the array (alias of
`push_back()<class_PackedFloat32Array_method_push_back>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_append_array}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_array**(array:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedFloat32Array_method_append_array>`{.interpreted-text
role="ref"}

Appends a **PackedFloat32Array** at the end of this array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_bsearch}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bsearch**(value:
`float<class_float>`{.interpreted-text role="ref"}, before:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_PackedFloat32Array_method_bsearch>`{.interpreted-text
role="ref"}

Finds the index of an existing value (or the insertion index that
maintains sorting order, if the value is not yet present in the array)
using binary search. Optionally, a `before` specifier can be passed. If
`false`, the returned index comes after all existing entries of the
value in the array.

\*\*Note:\*\* Calling
`bsearch()<class_PackedFloat32Array_method_bsearch>`{.interpreted-text
role="ref"} on an unsorted array results in unexpected behavior.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this method may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_PackedFloat32Array_method_clear>`{.interpreted-text
role="ref"}

Clears the array. This is equivalent to using
`resize()<class_PackedFloat32Array_method_resize>`{.interpreted-text
role="ref"} with a size of `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **count**(value:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedFloat32Array_method_count>`{.interpreted-text
role="ref"}

Returns the number of times an element is in the array.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this method may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_duplicate}
::: rst-class
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **duplicate**()
`🔗<class_PackedFloat32Array_method_duplicate>`{.interpreted-text
role="ref"}

Creates a copy of the array, and returns it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_erase}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **erase**(value:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PackedFloat32Array_method_erase>`{.interpreted-text
role="ref"}

Removes the first occurrence of a value from the array and returns
`true`. If the value does not exist in the array, nothing happens and
`false` is returned. To remove an element by index, use
`remove_at()<class_PackedFloat32Array_method_remove_at>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this method may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_fill}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **fill**(value:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PackedFloat32Array_method_fill>`{.interpreted-text role="ref"}

Assigns the given value to all elements in the array. This can typically
be used together with
`resize()<class_PackedFloat32Array_method_resize>`{.interpreted-text
role="ref"} to create an array with a given size and initialized
elements.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_find}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find**(value:
`float<class_float>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedFloat32Array_method_find>`{.interpreted-text role="ref"}

Searches the array for a value and returns its index or `-1` if not
found. Optionally, the initial search index can be passed.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this method may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_get}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedFloat32Array_method_get>`{.interpreted-text
role="ref"}

Returns the 32-bit float at the given `index` in the array. If `index`
out-of-bounds or negative, this method fails and returns `0.0`.

This method is similar (but not identical) to the `[]` operator. Most
notably, when this method fails, it doesn\'t pause project execution if
run from the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_has}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has**(value:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedFloat32Array_method_has>`{.interpreted-text
role="ref"}

Returns `true` if the array contains `value`.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this method may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_insert}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **insert**(at_index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PackedFloat32Array_method_insert>`{.interpreted-text
role="ref"}

Inserts a new element at a given position in the array. The position
must be valid, or at the end of the array (`idx == size()`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedFloat32Array_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the array is empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_push_back}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **push_back**(value:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PackedFloat32Array_method_push_back>`{.interpreted-text
role="ref"}

Appends an element at the end of the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_remove_at}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_at**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedFloat32Array_method_remove_at>`{.interpreted-text
role="ref"}

Removes an element from the array by index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_resize}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **resize**(new_size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedFloat32Array_method_resize>`{.interpreted-text
role="ref"}

Sets the size of the array. If the array is grown, reserves elements at
the end of the array. If the array is shrunk, truncates the array to the
new size. Calling
`resize()<class_PackedFloat32Array_method_resize>`{.interpreted-text
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
`size()<class_PackedFloat32Array_method_size>`{.interpreted-text
role="ref"} to find the actual size of the array after resize.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_reverse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reverse**()
`🔗<class_PackedFloat32Array_method_reverse>`{.interpreted-text
role="ref"}

Reverses the order of the elements in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_rfind}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rfind**(value:
`float<class_float>`{.interpreted-text role="ref"}, from:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedFloat32Array_method_rfind>`{.interpreted-text
role="ref"}

Searches the array in reverse order. Optionally, a start search index
can be passed. If negative, the start index is considered relative to
the end of the array.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this method may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **set**(index:
`int<class_int>`{.interpreted-text role="ref"}, value:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PackedFloat32Array_method_set>`{.interpreted-text role="ref"}

Changes the float at the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedFloat32Array_method_size>`{.interpreted-text role="ref"}

Returns the number of elements in the array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_slice}
::: rst-class
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **slice**(begin: `int<class_int>`{.interpreted-text
role="ref"}, end: `int<class_int>`{.interpreted-text role="ref"} =
2147483647)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedFloat32Array_method_slice>`{.interpreted-text
role="ref"}

Returns the slice of the **PackedFloat32Array**, from `begin`
(inclusive) to `end` (exclusive), as a new **PackedFloat32Array**.

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

:::: {#class_PackedFloat32Array_method_sort}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **sort**()
`🔗<class_PackedFloat32Array_method_sort>`{.interpreted-text role="ref"}

Sorts the elements of the array in ascending order.

\*\*Note:\*\*
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} doesn\'t behave the same as other numbers. Therefore, the
results from this method may not be accurate if NaNs are included.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_method_to_byte_array}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**to_byte_array**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedFloat32Array_method_to_byte_array>`{.interpreted-text
role="ref"}

Returns a copy of the data converted to a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
where each element has been encoded as 4 bytes.

The size of the new array will be `float32_array.size() * 4`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_PackedFloat32Array_operator_neq_PackedFloat32Array}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedFloat32Array_operator_neq_PackedFloat32Array>`{.interpreted-text
role="ref"}

Returns `true` if contents of the arrays differ.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_operator_sum_PackedFloat32Array}
::: rst-class
classref-operator
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **operator +**(right:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedFloat32Array_operator_sum_PackedFloat32Array>`{.interpreted-text
role="ref"}

Returns a new **PackedFloat32Array** with contents of `right` added at
the end of this array. For better performance, consider using
`append_array()<class_PackedFloat32Array_method_append_array>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_operator_eq_PackedFloat32Array}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_PackedFloat32Array_operator_eq_PackedFloat32Array>`{.interpreted-text
role="ref"}

Returns `true` if contents of both arrays are the same, i.e. they have
all equal floats at the corresponding indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedFloat32Array_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PackedFloat32Array_operator_idx_int>`{.interpreted-text
role="ref"}

Returns the `float<class_float>`{.interpreted-text role="ref"} at index
`index`. Negative indices can be used to access the elements starting
from the end. Using index out of array\'s bounds will result in an
error.

Note that `float<class_float>`{.interpreted-text role="ref"} type is
64-bit, unlike the values stored in the array.
