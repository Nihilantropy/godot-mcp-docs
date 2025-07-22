github_url
:   hide

# World2D {#class_World2D}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A resource that holds all components of a 2D world, such as a canvas and
a physics space.

::: rst-class
classref-introduction-group
:::

## Description

Class that has everything pertaining to a 2D world: A physics space, a
canvas, and a sound space. 2D nodes register their resources into the
current 2D world.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Ray-casting <../tutorials/physics/ray-casting>`{.interpreted-text
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

:::: {#class_World2D_property_canvas}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **canvas**
`🔗<class_World2D_property_canvas>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `RID<class_RID>`{.interpreted-text role="ref"} **get_canvas**()

The `RID<class_RID>`{.interpreted-text role="ref"} of this world\'s
canvas resource. Used by the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
for 2D drawing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_World2D_property_direct_space_state}
::: rst-class
classref-property
:::
::::

`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"} **direct_space_state**
`🔗<class_World2D_property_direct_space_state>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
  role="ref"} **get_direct_space_state**()

Direct access to the world\'s physics 2D space state. Used for querying
current and potential collisions. When using multi-threaded physics,
access is limited to
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} in the main thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_World2D_property_navigation_map}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **navigation_map**
`🔗<class_World2D_property_navigation_map>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `RID<class_RID>`{.interpreted-text role="ref"}
  **get_navigation_map**()

The `RID<class_RID>`{.interpreted-text role="ref"} of this world\'s
navigation map. Used by the
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_World2D_property_space}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **space**
`🔗<class_World2D_property_space>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `RID<class_RID>`{.interpreted-text role="ref"} **get_space**()

The `RID<class_RID>`{.interpreted-text role="ref"} of this world\'s
physics space resource. Used by the
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}
for 2D physics, treating it as both a space and an area.
