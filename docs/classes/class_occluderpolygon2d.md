github_url
:   hide

# OccluderPolygon2D {#class_OccluderPolygon2D}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Defines a 2D polygon for LightOccluder2D.

::: rst-class
classref-introduction-group
:::

## Description

Editor facility that helps you draw a 2D polygon used as resource for
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"}.

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

## Enumerations

:::: {#enum_OccluderPolygon2D_CullMode}
::: rst-class
classref-enumeration
:::
::::

enum **CullMode**:
`🔗<enum_OccluderPolygon2D_CullMode>`{.interpreted-text role="ref"}

:::: {#class_OccluderPolygon2D_constant_CULL_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`CullMode<enum_OccluderPolygon2D_CullMode>`{.interpreted-text
role="ref"} **CULL_DISABLED** = `0`

Culling is disabled. See
`cull_mode<class_OccluderPolygon2D_property_cull_mode>`{.interpreted-text
role="ref"}.

:::: {#class_OccluderPolygon2D_constant_CULL_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`CullMode<enum_OccluderPolygon2D_CullMode>`{.interpreted-text
role="ref"} **CULL_CLOCKWISE** = `1`

Culling is performed in the clockwise direction. See
`cull_mode<class_OccluderPolygon2D_property_cull_mode>`{.interpreted-text
role="ref"}.

:::: {#class_OccluderPolygon2D_constant_CULL_COUNTER_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`CullMode<enum_OccluderPolygon2D_CullMode>`{.interpreted-text
role="ref"} **CULL_COUNTER_CLOCKWISE** = `2`

Culling is performed in the counterclockwise direction. See
`cull_mode<class_OccluderPolygon2D_property_cull_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OccluderPolygon2D_property_closed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **closed** = `true`
`🔗<class_OccluderPolygon2D_property_closed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_closed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_closed**()

If `true`, closes the polygon. A closed OccluderPolygon2D occludes the
light coming from any direction. An opened OccluderPolygon2D occludes
the light only at its outline\'s direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OccluderPolygon2D_property_cull_mode}
::: rst-class
classref-property
:::
::::

`CullMode<enum_OccluderPolygon2D_CullMode>`{.interpreted-text
role="ref"} **cull_mode** = `0`
`🔗<class_OccluderPolygon2D_property_cull_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cull_mode**(value:
  `CullMode<enum_OccluderPolygon2D_CullMode>`{.interpreted-text
  role="ref"})
- `CullMode<enum_OccluderPolygon2D_CullMode>`{.interpreted-text
  role="ref"} **get_cull_mode**()

The culling mode to use.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OccluderPolygon2D_property_polygon}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **polygon** = `PackedVector2Array()`
`🔗<class_OccluderPolygon2D_property_polygon>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_polygon**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_polygon**()

A `Vector2<class_Vector2>`{.interpreted-text role="ref"} array with the
index for polygon\'s vertices positions.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.
