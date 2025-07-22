github_url
:   hide

# GLTFTextureSampler {#class_GLTFTextureSampler}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a glTF texture sampler

::: rst-class
classref-introduction-group
:::

## Description

Represents a texture sampler as defined by the base glTF spec. Texture
samplers in glTF specify how to sample data from the texture\'s base
image, when rendering the texture on an object.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}

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

:::: {#class_GLTFTextureSampler_property_mag_filter}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **mag_filter** = `9729`
`🔗<class_GLTFTextureSampler_property_mag_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mag_filter**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_mag_filter**()

Texture\'s magnification filter, used when texture appears larger on
screen than the source image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFTextureSampler_property_min_filter}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **min_filter** = `9987`
`🔗<class_GLTFTextureSampler_property_min_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_filter**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_min_filter**()

Texture\'s minification filter, used when the texture appears smaller on
screen than the source image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFTextureSampler_property_wrap_s}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **wrap_s** = `10497`
`🔗<class_GLTFTextureSampler_property_wrap_s>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wrap_s**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_wrap_s**()

Wrapping mode to use for S-axis (horizontal) texture coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFTextureSampler_property_wrap_t}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **wrap_t** = `10497`
`🔗<class_GLTFTextureSampler_property_wrap_t>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wrap_t**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_wrap_t**()

Wrapping mode to use for T-axis (vertical) texture coordinates.
