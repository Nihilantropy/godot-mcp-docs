github_url
:   hide

# CurveXYZTexture {#class_CurveXYZTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 1D texture where the red, green, and blue color channels correspond to
points on 3 curves.

::: rst-class
classref-introduction-group
:::

## Description

A 1D texture where the red, green, and blue color channels correspond to
points on 3 unit `Curve<class_Curve>`{.interpreted-text role="ref"}
resources. Compared to using separate
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}s, this
further simplifies the task of saving curves as image files.

If you only need to store one curve within a single texture, use
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}
instead. See also
`GradientTexture1D<class_GradientTexture1D>`{.interpreted-text
role="ref"} and
`GradientTexture2D<class_GradientTexture2D>`{.interpreted-text
role="ref"}.

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

:::: {#class_CurveXYZTexture_property_curve_x}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **curve_x**
`🔗<class_CurveXYZTexture_property_curve_x>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve_x**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"} **get_curve_x**()

The `Curve<class_Curve>`{.interpreted-text role="ref"} that is rendered
onto the texture\'s red channel. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CurveXYZTexture_property_curve_y}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **curve_y**
`🔗<class_CurveXYZTexture_property_curve_y>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve_y**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"} **get_curve_y**()

The `Curve<class_Curve>`{.interpreted-text role="ref"} that is rendered
onto the texture\'s green channel. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CurveXYZTexture_property_curve_z}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **curve_z**
`🔗<class_CurveXYZTexture_property_curve_z>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve_z**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"} **get_curve_z**()

The `Curve<class_Curve>`{.interpreted-text role="ref"} that is rendered
onto the texture\'s blue channel. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CurveXYZTexture_property_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **width** = `256`
`🔗<class_CurveXYZTexture_property_width>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_width**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_width**()

The width of the texture (in pixels). Higher values make it possible to
represent high-frequency data better (such as sudden direction changes),
at the cost of increased generation time and memory usage.
