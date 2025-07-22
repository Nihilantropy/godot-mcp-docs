github_url
:   hide

# LightOccluder2D {#class_LightOccluder2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Occludes light cast by a Light2D, casting shadows.

::: rst-class
classref-introduction-group
:::

## Description

Occludes light cast by a Light2D, casting shadows. The LightOccluder2D
must be provided with an
`OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
role="ref"} in order for the shadow to be computed.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D lights and shadows <../tutorials/2d/2d_lights_and_shadows>`{.interpreted-text
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

:::: {#class_LightOccluder2D_property_occluder}
::: rst-class
classref-property
:::
::::

`OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
role="ref"} **occluder**
`🔗<class_LightOccluder2D_property_occluder>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_occluder_polygon**(value:
  `OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
  role="ref"})
- `OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
  role="ref"} **get_occluder_polygon**()

The `OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
role="ref"} used to compute the shadow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightOccluder2D_property_occluder_light_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **occluder_light_mask** =
`1`
`🔗<class_LightOccluder2D_property_occluder_light_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_occluder_light_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_occluder_light_mask**()

The LightOccluder2D\'s occluder light mask. The LightOccluder2D will
cast shadows only from Light2D(s) that have the same light mask(s).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LightOccluder2D_property_sdf_collision}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sdf_collision** =
`true`
`🔗<class_LightOccluder2D_property_sdf_collision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_as_sdf_collision**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_set_as_sdf_collision**()

If enabled, the occluder will be part of a real-time generated signed
distance field that can be used in custom shaders.
