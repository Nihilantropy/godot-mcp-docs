github_url
:   hide

# XRVRS {#class_XRVRS}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Helper class for XR interfaces that generates VRS images.

::: rst-class
classref-introduction-group
:::

## Description

This class is used by various XR interfaces to generate VRS textures
that can be used to speed up rendering.

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

:::: {#class_XRVRS_property_vrs_min_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **vrs_min_radius** =
`20.0` `🔗<class_XRVRS_property_vrs_min_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_min_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_vrs_min_radius**()

The minimum radius around the focal point where full quality is
guaranteed if VRS is used as a percentage of screen size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRVRS_property_vrs_render_region}
::: rst-class
classref-property
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**vrs_render_region** = `Rect2i(0, 0, 0, 0)`
`🔗<class_XRVRS_property_vrs_render_region>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_render_region**(value:
  `Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
- `Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
  **get_vrs_render_region**()

The render region that the VRS texture will be scaled to when generated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRVRS_property_vrs_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **vrs_strength** =
`1.0` `🔗<class_XRVRS_property_vrs_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_strength**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_vrs_strength**()

The strength used to calculate the VRS density map. The greater this
value, the more noticeable VRS is.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRVRS_method_make_vrs_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**make_vrs_texture**(target_size:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, eye_foci:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}) `🔗<class_XRVRS_method_make_vrs_texture>`{.interpreted-text
role="ref"}

Generates the VRS texture based on a render `target_size` adjusted by
our VRS tile size. For each eyes focal point passed in `eye_foci` a
layer is created. Focal point should be in NDC.

The result will be cached, requesting a VRS texture with unchanged
parameters and settings will return the cached RID.
