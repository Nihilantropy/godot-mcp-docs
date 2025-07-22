github_url
:   hide

# MissingNode {#class_MissingNode}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An internal editor class intended for keeping the data of unrecognized
nodes.

::: rst-class
classref-introduction-group
:::

## Description

This is an internal editor class intended for keeping data of nodes of
unknown type (most likely this type was supplied by an extension that is
no longer loaded). It can\'t be manually instantiated or placed in a
scene.

\*\*Warning:\*\* Ignore missing nodes unless you know what you are
doing. Existing properties on a missing node can be freely modified in
code, regardless of the type they are intended to be.

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

:::: {#class_MissingNode_property_original_class}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **original_class**
`🔗<class_MissingNode_property_original_class>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_original_class**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_original_class**()

The name of the class this node was supposed to be (see
`Object.get_class()<class_Object_method_get_class>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MissingNode_property_original_scene}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **original_scene**
`🔗<class_MissingNode_property_original_scene>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_original_scene**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_original_scene**()

Returns the path of the scene this node was instance of originally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MissingNode_property_recording_properties}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**recording_properties**
`🔗<class_MissingNode_property_recording_properties>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_recording_properties**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_recording_properties**()

If `true`, allows new properties to be set along with existing ones. If
`false`, only existing properties\' values can be set, and new
properties cannot be added.
