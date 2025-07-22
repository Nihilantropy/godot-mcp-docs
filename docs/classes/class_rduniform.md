github_url
:   hide

# RDUniform {#class_RDUniform}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Shader uniform (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

This object is used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.

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

:::: {#class_RDUniform_property_binding}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **binding** = `0`
`🔗<class_RDUniform_property_binding>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_binding**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_binding**()

The uniform\'s binding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDUniform_property_uniform_type}
::: rst-class
classref-property
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **uniform_type** = `3`
`🔗<class_RDUniform_property_uniform_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_uniform_type**(value:
  `UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
  role="ref"})
- `UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
  role="ref"} **get_uniform_type**()

The uniform\'s data type.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RDUniform_method_add_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **add_id**(id:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RDUniform_method_add_id>`{.interpreted-text role="ref"}

Binds the given id to the uniform. The data associated with the id is
then used when the uniform is passed to a shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDUniform_method_clear_ids}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear_ids**()
`🔗<class_RDUniform_method_clear_ids>`{.interpreted-text role="ref"}

Unbinds all ids currently bound to the uniform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDUniform_method_get_ids}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**get_ids**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RDUniform_method_get_ids>`{.interpreted-text
role="ref"}

Returns an array of all ids currently bound to the uniform.
