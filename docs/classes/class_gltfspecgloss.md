github_url
:   hide

# GLTFSpecGloss {#class_GLTFSpecGloss}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Archived glTF extension for specular/glossy materials.

::: rst-class
classref-introduction-group
:::

## Description

KHR_materials_pbrSpecularGlossiness is an archived glTF extension. This
means that it is deprecated and not recommended for new files. However,
it is still supported for loading old files.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}
- [KHR_materials_pbrSpecularGlossiness glTF extension
  spec](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Archived/KHR_materials_pbrSpecularGlossiness)

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

:::: {#class_GLTFSpecGloss_property_diffuse_factor}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **diffuse_factor** =
`Color(1, 1, 1, 1)`
`🔗<class_GLTFSpecGloss_property_diffuse_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_diffuse_factor**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_diffuse_factor**()

The reflected diffuse factor of the material.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSpecGloss_property_diffuse_img}
::: rst-class
classref-property
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"} **diffuse_img**
`🔗<class_GLTFSpecGloss_property_diffuse_img>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_diffuse_img**(value: `Image<class_Image>`{.interpreted-text
  role="ref"})
- `Image<class_Image>`{.interpreted-text role="ref"}
  **get_diffuse_img**()

The diffuse texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSpecGloss_property_gloss_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **gloss_factor** =
`1.0` `🔗<class_GLTFSpecGloss_property_gloss_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gloss_factor**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_gloss_factor**()

The glossiness or smoothness of the material.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSpecGloss_property_spec_gloss_img}
::: rst-class
classref-property
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"} **spec_gloss_img**
`🔗<class_GLTFSpecGloss_property_spec_gloss_img>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spec_gloss_img**(value: `Image<class_Image>`{.interpreted-text
  role="ref"})
- `Image<class_Image>`{.interpreted-text role="ref"}
  **get_spec_gloss_img**()

The specular-glossiness texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSpecGloss_property_specular_factor}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **specular_factor** =
`Color(1, 1, 1, 1)`
`🔗<class_GLTFSpecGloss_property_specular_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_specular_factor**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_specular_factor**()

The specular RGB color of the material. The alpha channel is unused.
