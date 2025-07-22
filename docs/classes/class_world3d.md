github_url
:   hide

# World3D {#class_World3D}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A resource that holds all components of a 3D world, such as a visual
scenario and a physics space.

::: rst-class
classref-introduction-group
:::

## Description

Class that has everything pertaining to a world: A physics space, a
visual scenario, and a sound space. 3D nodes register their resources
into the current 3D world.

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

:::: {#class_World3D_property_camera_attributes}
::: rst-class
classref-property
:::
::::

`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
**camera_attributes**
`🔗<class_World3D_property_camera_attributes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_camera_attributes**(value:
  `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"})
- `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"} **get_camera_attributes**()

The default `CameraAttributes<class_CameraAttributes>`{.interpreted-text
role="ref"} resource to use if none set on the
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_World3D_property_direct_space_state}
::: rst-class
classref-property
:::
::::

`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`{.interpreted-text
role="ref"} **direct_space_state**
`🔗<class_World3D_property_direct_space_state>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`{.interpreted-text
  role="ref"} **get_direct_space_state**()

Direct access to the world\'s physics 3D space state. Used for querying
current and potential collisions. When using multi-threaded physics,
access is limited to
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} in the main thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_World3D_property_environment}
::: rst-class
classref-property
:::
::::

`Environment<class_Environment>`{.interpreted-text role="ref"}
**environment**
`🔗<class_World3D_property_environment>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_environment**(value:
  `Environment<class_Environment>`{.interpreted-text role="ref"})
- `Environment<class_Environment>`{.interpreted-text role="ref"}
  **get_environment**()

The World3D\'s `Environment<class_Environment>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_World3D_property_fallback_environment}
::: rst-class
classref-property
:::
::::

`Environment<class_Environment>`{.interpreted-text role="ref"}
**fallback_environment**
`🔗<class_World3D_property_fallback_environment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fallback_environment**(value:
  `Environment<class_Environment>`{.interpreted-text role="ref"})
- `Environment<class_Environment>`{.interpreted-text role="ref"}
  **get_fallback_environment**()

The World3D\'s fallback environment will be used if
`environment<class_World3D_property_environment>`{.interpreted-text
role="ref"} fails or is missing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_World3D_property_navigation_map}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **navigation_map**
`🔗<class_World3D_property_navigation_map>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `RID<class_RID>`{.interpreted-text role="ref"}
  **get_navigation_map**()

The `RID<class_RID>`{.interpreted-text role="ref"} of this world\'s
navigation map. Used by the
`NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_World3D_property_scenario}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **scenario**
`🔗<class_World3D_property_scenario>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `RID<class_RID>`{.interpreted-text role="ref"} **get_scenario**()

The World3D\'s visual scenario.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_World3D_property_space}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **space**
`🔗<class_World3D_property_space>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `RID<class_RID>`{.interpreted-text role="ref"} **get_space**()

The World3D\'s physics space.
