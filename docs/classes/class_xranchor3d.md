github_url
:   hide

# XRAnchor3D {#class_XRAnchor3D}

**Inherits:** `XRNode3D<class_XRNode3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An anchor point in AR space.

::: rst-class
classref-introduction-group
:::

## Description

The **XRAnchor3D** point is an
`XRNode3D<class_XRNode3D>`{.interpreted-text role="ref"} that maps a
real world location identified by the AR platform to a position within
the game world. For example, as long as plane detection in ARKit is on,
ARKit will identify and update the position of planes (tables, floors,
etc.) and create anchors for them.

This node is mapped to one of the anchors through its unique ID. When
you receive a signal that a new anchor is available, you should add this
node to your scene for that anchor. You can predefine nodes and set the
ID; the nodes will simply remain on `(0, 0, 0)` until a plane is
recognized.

Keep in mind that, as long as plane detection is enabled, the size,
placing and orientation of an anchor will be updated as the detection
logic learns more about the real world out there especially if only part
of the surface is in view.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `XR documentation index <../tutorials/xr/index>`{.interpreted-text
  role="doc"}

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

## Method Descriptions

:::: {#class_XRAnchor3D_method_get_plane}
::: rst-class
classref-method
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"} **get_plane**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_XRAnchor3D_method_get_plane>`{.interpreted-text
role="ref"}

Returns a plane aligned with our anchor; handy for intersection testing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRAnchor3D_method_get_size}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_XRAnchor3D_method_get_size>`{.interpreted-text
role="ref"}

Returns the estimated size of the plane that was detected. Say when the
anchor relates to a table in the real world, this is the estimated size
of the surface of that table.
