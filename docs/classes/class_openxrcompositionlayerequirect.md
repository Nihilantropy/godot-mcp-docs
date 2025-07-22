github_url
:   hide

# OpenXRCompositionLayerEquirect {#class_OpenXRCompositionLayerEquirect}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`OpenXRCompositionLayer<class_OpenXRCompositionLayer>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An OpenXR composition layer that is rendered as an internal slice of a
sphere.

::: rst-class
classref-introduction-group
:::

## Description

An OpenXR composition layer that allows rendering a
`SubViewport<class_SubViewport>`{.interpreted-text role="ref"} on an
internal slice of a sphere.

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

:::: {#class_OpenXRCompositionLayerEquirect_property_central_horizontal_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**central_horizontal_angle** = `1.5707964`
`🔗<class_OpenXRCompositionLayerEquirect_property_central_horizontal_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_central_horizontal_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_central_horizontal_angle**()

The central horizontal angle of the sphere. Used to set the width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayerEquirect_property_fallback_segments}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fallback_segments** =
`10`
`🔗<class_OpenXRCompositionLayerEquirect_property_fallback_segments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fallback_segments**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_fallback_segments**()

The number of segments to use in the fallback mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**lower_vertical_angle** = `0.7853982`
`🔗<class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lower_vertical_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_lower_vertical_angle**()

The lower vertical angle of the sphere. Used (together with
`upper_vertical_angle<class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle>`{.interpreted-text
role="ref"}) to set the height.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayerEquirect_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `1.0`
`🔗<class_OpenXRCompositionLayerEquirect_property_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The radius of the sphere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**upper_vertical_angle** = `0.7853982`
`🔗<class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_upper_vertical_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_upper_vertical_angle**()

The upper vertical angle of the sphere. Used (together with
`lower_vertical_angle<class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle>`{.interpreted-text
role="ref"}) to set the height.
