github_url
:   hide

# EncodedObjectAsID {#class_EncodedObjectAsID}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Holds a reference to an `Object<class_Object>`{.interpreted-text
role="ref"}\'s instance ID.

::: rst-class
classref-introduction-group
:::

## Description

Utility class which holds a reference to the internal identifier of an
`Object<class_Object>`{.interpreted-text role="ref"} instance, as given
by
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}. This ID can then be used to retrieve the object instance
with
`@GlobalScope.instance_from_id()<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"}.

This class is used internally by the editor inspector and script
debugger, but can also be used in plugins to pass and display objects as
their IDs.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_EncodedObjectAsID_property_object_id}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **object_id** = `0`
`🔗<class_EncodedObjectAsID_property_object_id>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_object_id**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_object_id**()

The `Object<class_Object>`{.interpreted-text role="ref"} identifier
stored in this **EncodedObjectAsID** instance. The object instance can
be retrieved with
`@GlobalScope.instance_from_id()<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"}.
