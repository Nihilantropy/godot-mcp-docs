github_url
:   hide

# RegExMatch {#class_RegExMatch}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Contains the results of a `RegEx<class_RegEx>`{.interpreted-text
role="ref"} search.

::: rst-class
classref-introduction-group
:::

## Description

Contains the results of a single `RegEx<class_RegEx>`{.interpreted-text
role="ref"} match returned by
`RegEx.search()<class_RegEx_method_search>`{.interpreted-text
role="ref"} and
`RegEx.search_all()<class_RegEx_method_search_all>`{.interpreted-text
role="ref"}. It can be used to find the position and range of the match
and its capturing groups, and it can extract its substring for you.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_RegExMatch_property_names}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} **names** =
`{}` `🔗<class_RegExMatch_property_names>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_names**()

A dictionary of named groups and its corresponding group number. Only
groups that were matched are included. If multiple groups have the same
name, that name would refer to the first matching one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RegExMatch_property_strings}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **strings** = `PackedStringArray()`
`🔗<class_RegExMatch_property_strings>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} **get_strings**()

An `Array<class_Array>`{.interpreted-text role="ref"} of the match and
its capturing groups.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RegExMatch_property_subject}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **subject** = `""`
`🔗<class_RegExMatch_property_subject>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `String<class_String>`{.interpreted-text role="ref"} **get_subject**()

The source string used with the search pattern to find this matching
result.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RegExMatch_method_get_end}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_end**(name:
`Variant<class_Variant>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RegExMatch_method_get_end>`{.interpreted-text
role="ref"}

Returns the end position of the match within the source string. The end
position of capturing groups can be retrieved by providing its group
number as an integer or its string name (if it\'s a named group). The
default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn\'t exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RegExMatch_method_get_group_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_group_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RegExMatch_method_get_group_count>`{.interpreted-text
role="ref"}

Returns the number of capturing groups.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RegExMatch_method_get_start}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_start**(name:
`Variant<class_Variant>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RegExMatch_method_get_start>`{.interpreted-text
role="ref"}

Returns the starting position of the match within the source string. The
starting position of capturing groups can be retrieved by providing its
group number as an integer or its string name (if it\'s a named group).
The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn\'t exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RegExMatch_method_get_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_string**(name: `Variant<class_Variant>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RegExMatch_method_get_string>`{.interpreted-text
role="ref"}

Returns the substring of the match from the source string. Capturing
groups can be retrieved by providing its group number as an integer or
its string name (if it\'s a named group). The default value of 0 refers
to the whole pattern.

Returns an empty string if the group did not match or doesn\'t exist.
