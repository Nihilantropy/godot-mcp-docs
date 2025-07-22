github_url
:   hide

# Shape3D {#class_Shape3D}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `BoxShape3D<class_BoxShape3D>`{.interpreted-text
role="ref"}, `CapsuleShape3D<class_CapsuleShape3D>`{.interpreted-text
role="ref"},
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"},
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"}, `CylinderShape3D<class_CylinderShape3D>`{.interpreted-text
role="ref"},
`HeightMapShape3D<class_HeightMapShape3D>`{.interpreted-text
role="ref"},
`SeparationRayShape3D<class_SeparationRayShape3D>`{.interpreted-text
role="ref"}, `SphereShape3D<class_SphereShape3D>`{.interpreted-text
role="ref"},
`WorldBoundaryShape3D<class_WorldBoundaryShape3D>`{.interpreted-text
role="ref"}

Abstract base class for 3D shapes used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for all 3D shapes, intended for use in physics.

\*\*Performance:\*\* Primitive shapes, especially
`SphereShape3D<class_SphereShape3D>`{.interpreted-text role="ref"}, are
fast to check collisions against.
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"} and
`HeightMapShape3D<class_HeightMapShape3D>`{.interpreted-text role="ref"}
are slower, and
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} is the slowest.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`{.interpreted-text
  role="doc"}

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

:::: {#class_Shape3D_property_custom_solver_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**custom_solver_bias** = `0.0`
`🔗<class_Shape3D_property_custom_solver_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_solver_bias**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_custom_solver_bias**()

The shape\'s custom solver bias. Defines how much bodies react to
enforce contact separation when this shape is involved.

When set to `0`, the default value from
`ProjectSettings.physics/3d/solver/default_contact_bias<class_ProjectSettings_property_physics/3d/solver/default_contact_bias>`{.interpreted-text
role="ref"} is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Shape3D_property_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **margin** = `0.04`
`🔗<class_Shape3D_property_margin>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_margin**()

The collision margin for the shape. This is not used in Godot Physics.

Collision margins allow collision detection to be more efficient by
adding an extra shell around shapes. Collision algorithms are more
expensive when objects overlap by more than their margin, so a higher
value for margins is better for performance, at the cost of accuracy
around edges as it makes them less sharp.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Shape3D_method_get_debug_mesh}
::: rst-class
classref-method
:::
::::

`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}
**get_debug_mesh**()
`🔗<class_Shape3D_method_get_debug_mesh>`{.interpreted-text role="ref"}

Returns the `ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}
used to draw the debug collision for this **Shape3D**.
