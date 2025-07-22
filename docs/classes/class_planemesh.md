github_url
:   hide

# PlaneMesh {#class_PlaneMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `QuadMesh<class_QuadMesh>`{.interpreted-text
role="ref"}

Class representing a planar
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Class representing a planar
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}. This
flat mesh does not have a thickness. By default, this mesh is aligned on
the X and Z axes; this default rotation isn\'t suited for use with
billboarded materials. For billboarded materials, change
`orientation<class_PlaneMesh_property_orientation>`{.interpreted-text
role="ref"} to
`FACE_Z<class_PlaneMesh_constant_FACE_Z>`{.interpreted-text role="ref"}.

\*\*Note:\*\* When using a large textured **PlaneMesh** (e.g. as a
floor), you may stumble upon UV jittering issues depending on the camera
angle. To solve this, increase
`subdivide_depth<class_PlaneMesh_property_subdivide_depth>`{.interpreted-text
role="ref"} and
`subdivide_width<class_PlaneMesh_property_subdivide_width>`{.interpreted-text
role="ref"} until you no longer notice UV jittering.

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

:::: {#enum_PlaneMesh_Orientation}
::: rst-class
classref-enumeration
:::
::::

enum **Orientation**: `🔗<enum_PlaneMesh_Orientation>`{.interpreted-text
role="ref"}

:::: {#class_PlaneMesh_constant_FACE_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Orientation<enum_PlaneMesh_Orientation>`{.interpreted-text role="ref"}
**FACE_X** = `0`

**PlaneMesh** will face the positive X-axis.

:::: {#class_PlaneMesh_constant_FACE_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Orientation<enum_PlaneMesh_Orientation>`{.interpreted-text role="ref"}
**FACE_Y** = `1`

**PlaneMesh** will face the positive Y-axis. This matches the behavior
of the **PlaneMesh** in Godot 3.x.

:::: {#class_PlaneMesh_constant_FACE_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`Orientation<enum_PlaneMesh_Orientation>`{.interpreted-text role="ref"}
**FACE_Z** = `2`

**PlaneMesh** will face the positive Z-axis. This matches the behavior
of the QuadMesh in Godot 3.x.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_PlaneMesh_property_center_offset}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **center_offset**
= `Vector3(0, 0, 0)`
`🔗<class_PlaneMesh_property_center_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_center_offset**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_center_offset**()

Offset of the generated plane. Useful for particles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PlaneMesh_property_orientation}
::: rst-class
classref-property
:::
::::

`Orientation<enum_PlaneMesh_Orientation>`{.interpreted-text role="ref"}
**orientation** = `1`
`🔗<class_PlaneMesh_property_orientation>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_orientation**(value:
  `Orientation<enum_PlaneMesh_Orientation>`{.interpreted-text
  role="ref"})
- `Orientation<enum_PlaneMesh_Orientation>`{.interpreted-text
  role="ref"} **get_orientation**()

Direction that the **PlaneMesh** is facing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PlaneMesh_property_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **size** =
`Vector2(2, 2)` `🔗<class_PlaneMesh_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_size**()

Size of the generated plane.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PlaneMesh_property_subdivide_depth}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **subdivide_depth** = `0`
`🔗<class_PlaneMesh_property_subdivide_depth>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subdivide_depth**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_subdivide_depth**()

Number of subdivision along the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PlaneMesh_property_subdivide_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **subdivide_width** = `0`
`🔗<class_PlaneMesh_property_subdivide_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subdivide_width**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_subdivide_width**()

Number of subdivision along the X axis.
