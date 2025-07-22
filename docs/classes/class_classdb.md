github_url
:   hide

# ClassDB {#class_ClassDB}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A class information repository.

::: rst-class
classref-introduction-group
:::

## Description

Provides access to metadata stored for every available class.

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

## Enumerations

:::: {#enum_ClassDB_APIType}
::: rst-class
classref-enumeration
:::
::::

enum **APIType**: `🔗<enum_ClassDB_APIType>`{.interpreted-text
role="ref"}

:::: {#class_ClassDB_constant_API_CORE}
::: rst-class
classref-enumeration-constant
:::
::::

`APIType<enum_ClassDB_APIType>`{.interpreted-text role="ref"}
**API_CORE** = `0`

Native Core class type.

:::: {#class_ClassDB_constant_API_EDITOR}
::: rst-class
classref-enumeration-constant
:::
::::

`APIType<enum_ClassDB_APIType>`{.interpreted-text role="ref"}
**API_EDITOR** = `1`

Native Editor class type.

:::: {#class_ClassDB_constant_API_EXTENSION}
::: rst-class
classref-enumeration-constant
:::
::::

`APIType<enum_ClassDB_APIType>`{.interpreted-text role="ref"}
**API_EXTENSION** = `2`

GDExtension class type.

:::: {#class_ClassDB_constant_API_EDITOR_EXTENSION}
::: rst-class
classref-enumeration-constant
:::
::::

`APIType<enum_ClassDB_APIType>`{.interpreted-text role="ref"}
**API_EDITOR_EXTENSION** = `3`

GDExtension Editor class type.

:::: {#class_ClassDB_constant_API_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`APIType<enum_ClassDB_APIType>`{.interpreted-text role="ref"}
**API_NONE** = `4`

Unknown class type.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ClassDB_method_can_instantiate}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**can_instantiate**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_can_instantiate>`{.interpreted-text role="ref"}

Returns `true` if objects can be instantiated from the specified
`class`, otherwise returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_call_static}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**class_call_static**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_call_static>`{.interpreted-text
role="ref"}

Calls a static method on a class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_exists}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **class_exists**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ClassDB_method_class_exists>`{.interpreted-text
role="ref"}

Returns whether the specified `class` is available or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_api_type}
::: rst-class
classref-method
:::
::::

`APIType<enum_ClassDB_APIType>`{.interpreted-text role="ref"}
**class_get_api_type**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_api_type>`{.interpreted-text
role="ref"}

Returns the API type of the specified `class`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_enum_constants}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **class_get_enum_constants**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, enum:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_enum_constants>`{.interpreted-text
role="ref"}

Returns an array with all the keys in `enum` of `class` or its ancestry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_enum_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **class_get_enum_list**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_enum_list>`{.interpreted-text
role="ref"}

Returns an array with all the enums of `class` or its ancestry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_integer_constant}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**class_get_integer_constant**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_integer_constant>`{.interpreted-text
role="ref"}

Returns the value of the integer constant `name` of `class` or its
ancestry. Always returns 0 when the constant could not be found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_integer_constant_enum}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**class_get_integer_constant_enum**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_integer_constant_enum>`{.interpreted-text
role="ref"}

Returns which enum the integer constant `name` of `class` or its
ancestry belongs to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_integer_constant_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **class_get_integer_constant_list**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_integer_constant_list>`{.interpreted-text
role="ref"}

Returns an array with the names all the integer constants of `class` or
its ancestry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_method_argument_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**class_get_method_argument_count**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, method:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_method_argument_count>`{.interpreted-text
role="ref"}

Returns the number of arguments of the method `method` of `class` or its
ancestry if `no_inheritance` is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_method_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **class_get_method_list**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_method_list>`{.interpreted-text
role="ref"}

Returns an array with all the methods of `class` or its ancestry if
`no_inheritance` is `false`. Every element of the array is a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following keys: `args`, `default_args`, `flags`, `id`, `name`,
`return: (class_name, hint, hint_string, name, type, usage)`.

\*\*Note:\*\* In exported release builds the debug info is not
available, so the returned dictionaries will contain only method names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_property}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**class_get_property**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, property: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_property>`{.interpreted-text
role="ref"}

Returns the value of `property` of `object` or its ancestry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_property_default_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**class_get_property_default_value**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_property_default_value>`{.interpreted-text
role="ref"}

Returns the default value of `property` of `class` or its ancestor
classes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_property_getter}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**class_get_property_getter**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_ClassDB_method_class_get_property_getter>`{.interpreted-text
role="ref"}

Returns the getter method name of `property` of `class`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_property_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **class_get_property_list**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_property_list>`{.interpreted-text
role="ref"}

Returns an array with all the properties of `class` or its ancestry if
`no_inheritance` is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_property_setter}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**class_get_property_setter**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_ClassDB_method_class_get_property_setter>`{.interpreted-text
role="ref"}

Returns the setter method name of `property` of `class`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_signal}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**class_get_signal**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, signal:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_signal>`{.interpreted-text
role="ref"}

Returns the `signal` data of `class` or its ancestry. The returned value
is a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with
the following keys: `args`, `default_args`, `flags`, `id`, `name`,
`return: (class_name, hint, hint_string, name, type, usage)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_get_signal_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **class_get_signal_list**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_get_signal_list>`{.interpreted-text
role="ref"}

Returns an array with all the signals of `class` or its ancestry if
`no_inheritance` is `false`. Every element of the array is a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} as
described in
`class_get_signal()<class_ClassDB_method_class_get_signal>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_has_enum}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**class_has_enum**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ClassDB_method_class_has_enum>`{.interpreted-text
role="ref"}

Returns whether `class` or its ancestry has an enum called `name` or
not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_has_integer_constant}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**class_has_integer_constant**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_has_integer_constant>`{.interpreted-text
role="ref"}

Returns whether `class` or its ancestry has an integer constant called
`name` or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_has_method}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**class_has_method**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, method:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_has_method>`{.interpreted-text
role="ref"}

Returns whether `class` (or its ancestry if `no_inheritance` is `false`)
has a method called `method` or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_has_signal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**class_has_signal**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, signal:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_has_signal>`{.interpreted-text
role="ref"}

Returns whether `class` or its ancestry has a signal called `signal` or
not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_class_set_property}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**class_set_property**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, property: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_class_set_property>`{.interpreted-text
role="ref"}

Sets `property` value of `object` to `value`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_get_class_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_class_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ClassDB_method_get_class_list>`{.interpreted-text
role="ref"}

Returns the names of all the classes available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_get_inheriters_from_class}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_inheriters_from_class**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_get_inheriters_from_class>`{.interpreted-text
role="ref"}

Returns the names of all the classes that directly or indirectly inherit
from `class`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_get_parent_class}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_parent_class**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_get_parent_class>`{.interpreted-text
role="ref"}

Returns the parent class of `class`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_instantiate}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**instantiate**(class: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ClassDB_method_instantiate>`{.interpreted-text
role="ref"}

Creates an instance of `class`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_is_class_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_class_enabled**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_is_class_enabled>`{.interpreted-text
role="ref"}

Returns whether this `class` is enabled or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_is_class_enum_bitfield}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_class_enum_bitfield**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, enum:
`StringName<class_StringName>`{.interpreted-text role="ref"},
no_inheritance: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_is_class_enum_bitfield>`{.interpreted-text
role="ref"}

Returns whether `class` (or its ancestor classes if `no_inheritance` is
`false`) has an enum called `enum` that is a bitfield.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ClassDB_method_is_parent_class}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_parent_class**(class:
`StringName<class_StringName>`{.interpreted-text role="ref"}, inherits:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ClassDB_method_is_parent_class>`{.interpreted-text role="ref"}

Returns whether `inherits` is an ancestor of `class` or not.
