github_url
:   hide

# WorldBoundaryShape3D {#class_WorldBoundaryShape3D}

**Inherits:** `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D world boundary (half-space) shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 3D world boundary shape, intended for use in physics.
**WorldBoundaryShape3D** works like an infinite plane that forces all
physics bodies to stay above it. The
`plane<class_WorldBoundaryShape3D_property_plane>`{.interpreted-text
role="ref"}\'s normal determines which direction is considered as
\"above\" and in the editor, the line over the plane represents this
direction. It can for example be used for endless flat floors.

\*\*Note:\*\* When the physics engine is set to **Jolt Physics** in the
project settings
(`ProjectSettings.physics/3d/physics_engine<class_ProjectSettings_property_physics/3d/physics_engine>`{.interpreted-text
role="ref"}), **WorldBoundaryShape3D** has a finite size (centered at
the shape\'s origin). It can be adjusted by changing
`ProjectSettings.physics/jolt_physics_3d/limits/world_boundary_shape_size<class_ProjectSettings_property_physics/jolt_physics_3d/limits/world_boundary_shape_size>`{.interpreted-text
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

:::: {#class_WorldBoundaryShape3D_property_plane}
::: rst-class
classref-property
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"} **plane** =
`Plane(0, 1, 0, 0)`
`🔗<class_WorldBoundaryShape3D_property_plane>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_plane**(value: `Plane<class_Plane>`{.interpreted-text
  role="ref"})
- `Plane<class_Plane>`{.interpreted-text role="ref"} **get_plane**()

The `Plane<class_Plane>`{.interpreted-text role="ref"} used by the
**WorldBoundaryShape3D** for collision.
