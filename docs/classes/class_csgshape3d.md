github_url
:   hide

# CSGShape3D {#class_CSGShape3D}

**Inherits:**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `CSGCombiner3D<class_CSGCombiner3D>`{.interpreted-text
role="ref"}, `CSGPrimitive3D<class_CSGPrimitive3D>`{.interpreted-text
role="ref"}

The CSG base class.

::: rst-class
classref-introduction-group
:::

## Description

This is the CSG base class that provides CSG operation support to the
various CSG nodes in Godot.

\*\*Performance:\*\* CSG nodes are only intended for prototyping as they
have a significant CPU performance cost. Consider baking final CSG
operation results into static geometry that replaces the CSG nodes.

Individual CSG root node results can be baked to nodes with static
resources with the editor menu that appears when a CSG root node is
selected.

Individual CSG root nodes can also be baked to static resources with
scripts by calling
`bake_static_mesh()<class_CSGShape3D_method_bake_static_mesh>`{.interpreted-text
role="ref"} for the visual mesh or
`bake_collision_shape()<class_CSGShape3D_method_bake_collision_shape>`{.interpreted-text
role="ref"} for the physics collision.

Entire scenes of CSG nodes can be baked to static geometry and exported
with the editor glTF scene exporter: **Scene \> Export As\... \> glTF
2.0 Scene\...**

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Prototyping levels with CSG <../tutorials/3d/csg_tools>`{.interpreted-text
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

## Enumerations

:::: {#enum_CSGShape3D_Operation}
::: rst-class
classref-enumeration
:::
::::

enum **Operation**: `🔗<enum_CSGShape3D_Operation>`{.interpreted-text
role="ref"}

:::: {#class_CSGShape3D_constant_OPERATION_UNION}
::: rst-class
classref-enumeration-constant
:::
::::

`Operation<enum_CSGShape3D_Operation>`{.interpreted-text role="ref"}
**OPERATION_UNION** = `0`

Geometry of both primitives is merged, intersecting geometry is removed.

:::: {#class_CSGShape3D_constant_OPERATION_INTERSECTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Operation<enum_CSGShape3D_Operation>`{.interpreted-text role="ref"}
**OPERATION_INTERSECTION** = `1`

Only intersecting geometry remains, the rest is removed.

:::: {#class_CSGShape3D_constant_OPERATION_SUBTRACTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Operation<enum_CSGShape3D_Operation>`{.interpreted-text role="ref"}
**OPERATION_SUBTRACTION** = `2`

The second shape is subtracted from the first, leaving a dent with its
shape.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CSGShape3D_property_calculate_tangents}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **calculate_tangents**
= `true`
`🔗<class_CSGShape3D_property_calculate_tangents>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_calculate_tangents**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_calculating_tangents**()

Calculate tangents for the CSG shape which allows the use of normal and
height maps. This is only applied on the root shape, this setting is
ignored on any child. Setting this to `false` can speed up shape
generation slightly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_property_collision_layer}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_layer** = `1`
`🔗<class_CSGShape3D_property_collision_layer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_layer**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_layer**()

The physics layers this area is in.

Collidable objects can exist in any of 32 different layers. These layers
work like a tagging system, and are not visual. A collidable can use
these layers to select with which objects it can collide, using the
collision_mask property.

A contact is detected if object A is in any of the layers that object B
scans, or object B is in any layer scanned by object A. See [Collision
layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_property_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** = `1`
`🔗<class_CSGShape3D_property_collision_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_mask**()

The physics layers this CSG shape scans for collisions. Only effective
if
`use_collision<class_CSGShape3D_property_use_collision>`{.interpreted-text
role="ref"} is `true`. See [Collision layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_property_collision_priority}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**collision_priority** = `1.0`
`🔗<class_CSGShape3D_property_collision_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_priority**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_collision_priority**()

The priority used to solve colliding when occurring penetration. Only
effective if
`use_collision<class_CSGShape3D_property_use_collision>`{.interpreted-text
role="ref"} is `true`. The higher the priority is, the lower the
penetration into the object will be. This can for example be used to
prevent the player from breaking through the boundaries of a level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_property_operation}
::: rst-class
classref-property
:::
::::

`Operation<enum_CSGShape3D_Operation>`{.interpreted-text role="ref"}
**operation** = `0`
`🔗<class_CSGShape3D_property_operation>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_operation**(value:
  `Operation<enum_CSGShape3D_Operation>`{.interpreted-text role="ref"})
- `Operation<enum_CSGShape3D_Operation>`{.interpreted-text role="ref"}
  **get_operation**()

The operation that is performed on this shape. This is ignored for the
first CSG child node as the operation is between this node and the
previous child of this nodes parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_property_snap}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **snap**
`🔗<class_CSGShape3D_property_snap>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_snap**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_snap**()

**Deprecated:** The CSG library no longer uses snapping.

This property does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_property_use_collision}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_collision** =
`false` `🔗<class_CSGShape3D_property_use_collision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_collision**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_collision**()

Adds a collision shape to the physics engine for our CSG shape. This
will always act like a static body. Note that the collision shape is
still active even if the CSG shape itself is hidden. See also
`collision_mask<class_CSGShape3D_property_collision_mask>`{.interpreted-text
role="ref"} and
`collision_priority<class_CSGShape3D_property_collision_priority>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CSGShape3D_method_bake_collision_shape}
::: rst-class
classref-method
:::
::::

`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} **bake_collision_shape**()
`🔗<class_CSGShape3D_method_bake_collision_shape>`{.interpreted-text
role="ref"}

Returns a baked physics
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} of this node\'s CSG operation result. Returns an empty shape
if the node is not a CSG root node or has no valid geometry.

\*\*Performance:\*\* If the CSG operation results in a very detailed
geometry with many faces physics performance will be very slow. Concave
shapes should in general only be used for static level geometry and not
with dynamic objects that are moving.

\*\*Note:\*\* CSG mesh data updates are deferred, which means they are
updated with a delay of one rendered frame. To avoid getting an empty
shape or outdated mesh data, make sure to call
`await get_tree().process_frame` before using
`bake_collision_shape()<class_CSGShape3D_method_bake_collision_shape>`{.interpreted-text
role="ref"} in
`Node._ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} or after changing properties on the **CSGShape3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_method_bake_static_mesh}
::: rst-class
classref-method
:::
::::

`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}
**bake_static_mesh**()
`🔗<class_CSGShape3D_method_bake_static_mesh>`{.interpreted-text
role="ref"}

Returns a baked static `ArrayMesh<class_ArrayMesh>`{.interpreted-text
role="ref"} of this node\'s CSG operation result. Materials from
involved CSG nodes are added as extra mesh surfaces. Returns an empty
mesh if the node is not a CSG root node or has no valid geometry.

\*\*Note:\*\* CSG mesh data updates are deferred, which means they are
updated with a delay of one rendered frame. To avoid getting an empty
mesh or outdated mesh data, make sure to call
`await get_tree().process_frame` before using
`bake_static_mesh()<class_CSGShape3D_method_bake_static_mesh>`{.interpreted-text
role="ref"} in
`Node._ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} or after changing properties on the **CSGShape3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_method_get_collision_layer_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CSGShape3D_method_get_collision_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_layer<class_CSGShape3D_property_collision_layer>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_method_get_collision_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CSGShape3D_method_get_collision_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_mask<class_CSGShape3D_property_collision_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_method_get_meshes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_meshes**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CSGShape3D_method_get_meshes>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} with two
elements, the first is the
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} of this
node and the second is the root `Mesh<class_Mesh>`{.interpreted-text
role="ref"} of this node. Only works when this node is the root shape.

\*\*Note:\*\* CSG mesh data updates are deferred, which means they are
updated with a delay of one rendered frame. To avoid getting an empty
shape or outdated mesh data, make sure to call
`await get_tree().process_frame` before using
`get_meshes()<class_CSGShape3D_method_get_meshes>`{.interpreted-text
role="ref"} in
`Node._ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} or after changing properties on the **CSGShape3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_method_is_root_shape}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_root_shape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CSGShape3D_method_is_root_shape>`{.interpreted-text
role="ref"}

Returns `true` if this is a root shape and is thus the object that is
rendered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_method_set_collision_layer_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CSGShape3D_method_set_collision_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_layer<class_CSGShape3D_property_collision_layer>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGShape3D_method_set_collision_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CSGShape3D_method_set_collision_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_mask<class_CSGShape3D_property_collision_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.
