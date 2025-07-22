github_url
:   hide

# GLTFTexture {#class_GLTFTexture}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

GLTFTexture represents a texture in a glTF file.

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

:::: {#class_GLTFTexture_property_sampler}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sampler** = `-1`
`🔗<class_GLTFTexture_property_sampler>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sampler**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_sampler**()

ID of the texture sampler to use when sampling the image. If -1, then
the default texture sampler is used (linear filtering, and repeat
wrapping in both axes).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFTexture_property_src_image}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **src_image** = `-1`
`🔗<class_GLTFTexture_property_src_image>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_src_image**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_src_image**()

The index of the image associated with this texture, see
`GLTFState.get_images()<class_GLTFState_method_get_images>`{.interpreted-text
role="ref"}. If -1, then this texture does not have an image assigned.
