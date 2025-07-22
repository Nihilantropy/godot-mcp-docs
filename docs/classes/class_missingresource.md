github_url
:   hide

# MissingResource {#class_MissingResource}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

An internal editor class intended for keeping the data of unrecognized
resources.

::: rst-class
classref-introduction-group
:::

## Description

This is an internal editor class intended for keeping data of resources
of unknown type (most likely this type was supplied by an extension that
is no longer loaded). It can\'t be manually instantiated or placed in a
scene.

\*\*Warning:\*\* Ignore missing resources unless you know what you are
doing. Existing properties on a missing resource can be freely modified
in code, regardless of the type they are intended to be.

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

:::: {#class_MissingResource_property_original_class}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **original_class**
`🔗<class_MissingResource_property_original_class>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_original_class**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_original_class**()

The name of the class this resource was supposed to be (see
`Object.get_class()<class_Object_method_get_class>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MissingResource_property_recording_properties}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**recording_properties**
`🔗<class_MissingResource_property_recording_properties>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_recording_properties**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_recording_properties**()

If set to `true`, allows new properties to be added on top of the
existing ones with
`Object.set()<class_Object_method_set>`{.interpreted-text role="ref"}.
