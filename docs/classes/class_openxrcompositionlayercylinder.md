github_url
:   hide

# OpenXRCompositionLayerCylinder {#class_OpenXRCompositionLayerCylinder}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`OpenXRCompositionLayer<class_OpenXRCompositionLayer>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An OpenXR composition layer that is rendered as an internal slice of a
cylinder.

::: rst-class
classref-introduction-group
:::

## Description

An OpenXR composition layer that allows rendering a
`SubViewport<class_SubViewport>`{.interpreted-text role="ref"} on an
internal slice of a cylinder.

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

:::: {#class_OpenXRCompositionLayerCylinder_property_aspect_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **aspect_ratio** =
`1.0`
`🔗<class_OpenXRCompositionLayerCylinder_property_aspect_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_aspect_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_aspect_ratio**()

The aspect ratio of the slice. Used to set the height relative to the
width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayerCylinder_property_central_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **central_angle** =
`1.5707964`
`🔗<class_OpenXRCompositionLayerCylinder_property_central_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_central_angle**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_central_angle**()

The central angle of the cylinder. Used to set the width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayerCylinder_property_fallback_segments}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fallback_segments** =
`10`
`🔗<class_OpenXRCompositionLayerCylinder_property_fallback_segments>`{.interpreted-text
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

:::: {#class_OpenXRCompositionLayerCylinder_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `1.0`
`🔗<class_OpenXRCompositionLayerCylinder_property_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The radius of the cylinder.
