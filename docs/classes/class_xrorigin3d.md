github_url
:   hide

# XROrigin3D {#class_XROrigin3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

The origin point in AR/VR.

::: rst-class
classref-introduction-group
:::

## Description

This is a special node within the AR/VR system that maps the physical
location of the center of our tracking space to the virtual location
within our game world.

Multiple origin points can be added to the scene tree, but only one can
used at a time. All the `XRCamera3D<class_XRCamera3D>`{.interpreted-text
role="ref"}, `XRController3D<class_XRController3D>`{.interpreted-text
role="ref"}, and `XRAnchor3D<class_XRAnchor3D>`{.interpreted-text
role="ref"} nodes should be direct children of this node for spatial
tracking to work correctly.

It is the position of this node that you update when your character
needs to move through your game world while we\'re not moving in the
real world. Movement in the real world is always in relation to this
origin point.

For example, if your character is driving a car, the **XROrigin3D** node
should be a child node of this car. Or, if you\'re implementing a
teleport system to move your character, you should change the position
of this node.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `XR documentation index <../tutorials/xr/index>`{.interpreted-text
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

:::: {#class_XROrigin3D_property_current}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **current** = `false`
`🔗<class_XROrigin3D_property_current>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_current**()

If `true`, this origin node is currently being used by the
`XRServer<class_XRServer>`{.interpreted-text role="ref"}. Only one
origin point can be used at a time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XROrigin3D_property_world_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **world_scale** =
`1.0` `🔗<class_XROrigin3D_property_world_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_world_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_world_scale**()

The scale of the game world compared to the real world. This is the same
as
`XRServer.world_scale<class_XRServer_property_world_scale>`{.interpreted-text
role="ref"}. By default, most AR/VR platforms assume that 1 game unit
corresponds to 1 real world meter.
