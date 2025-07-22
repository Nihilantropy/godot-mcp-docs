github_url
:   hide

# PanoramaSkyMaterial {#class_PanoramaSkyMaterial}

**Inherits:** `Material<class_Material>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A material that provides a special texture to a
`Sky<class_Sky>`{.interpreted-text role="ref"}, usually an HDR panorama.

::: rst-class
classref-introduction-group
:::

## Description

A resource referenced in a `Sky<class_Sky>`{.interpreted-text
role="ref"} that is used to draw a background. **PanoramaSkyMaterial**
functions similar to skyboxes in other engines, except it uses an
equirectangular sky map instead of a
`Cubemap<class_Cubemap>`{.interpreted-text role="ref"}.

Using an HDR panorama is strongly recommended for accurate, high-quality
reflections. Godot supports the Radiance HDR (`.hdr`) and OpenEXR
(`.exr`) image formats for this purpose.

You can use [this
tool](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html)
to convert a cubemap to an equirectangular sky map.

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

:::: {#class_PanoramaSkyMaterial_property_energy_multiplier}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **energy_multiplier**
= `1.0`
`🔗<class_PanoramaSkyMaterial_property_energy_multiplier>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_energy_multiplier**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_energy_multiplier**()

The sky\'s overall brightness multiplier. Higher values result in a
brighter sky.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PanoramaSkyMaterial_property_filter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **filter** = `true`
`🔗<class_PanoramaSkyMaterial_property_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filtering_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_filtering_enabled**()

A boolean value to determine if the background texture should be
filtered or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PanoramaSkyMaterial_property_panorama}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **panorama**
`🔗<class_PanoramaSkyMaterial_property_panorama>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_panorama**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_panorama**()

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} to be applied
to the **PanoramaSkyMaterial**.
