github_url
:   hide

# Node2D {#class_Node2D}

**Inherits:** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AnimatedSprite2D<class_AnimatedSprite2D>`{.interpreted-text
role="ref"}, `AudioListener2D<class_AudioListener2D>`{.interpreted-text
role="ref"},
`AudioStreamPlayer2D<class_AudioStreamPlayer2D>`{.interpreted-text
role="ref"}, `BackBufferCopy<class_BackBufferCopy>`{.interpreted-text
role="ref"}, `Bone2D<class_Bone2D>`{.interpreted-text role="ref"},
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"},
`CanvasGroup<class_CanvasGroup>`{.interpreted-text role="ref"},
`CanvasModulate<class_CanvasModulate>`{.interpreted-text role="ref"},
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"},
`CollisionPolygon2D<class_CollisionPolygon2D>`{.interpreted-text
role="ref"},
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text
role="ref"}, `CPUParticles2D<class_CPUParticles2D>`{.interpreted-text
role="ref"}, `GPUParticles2D<class_GPUParticles2D>`{.interpreted-text
role="ref"}, `Joint2D<class_Joint2D>`{.interpreted-text role="ref"},
`Light2D<class_Light2D>`{.interpreted-text role="ref"},
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"},
`Line2D<class_Line2D>`{.interpreted-text role="ref"},
`Marker2D<class_Marker2D>`{.interpreted-text role="ref"},
`MeshInstance2D<class_MeshInstance2D>`{.interpreted-text role="ref"},
`MultiMeshInstance2D<class_MultiMeshInstance2D>`{.interpreted-text
role="ref"},
`NavigationLink2D<class_NavigationLink2D>`{.interpreted-text
role="ref"},
`NavigationObstacle2D<class_NavigationObstacle2D>`{.interpreted-text
role="ref"},
`NavigationRegion2D<class_NavigationRegion2D>`{.interpreted-text
role="ref"}, `Parallax2D<class_Parallax2D>`{.interpreted-text
role="ref"}, `ParallaxLayer<class_ParallaxLayer>`{.interpreted-text
role="ref"}, `Path2D<class_Path2D>`{.interpreted-text role="ref"},
`PathFollow2D<class_PathFollow2D>`{.interpreted-text role="ref"},
`Polygon2D<class_Polygon2D>`{.interpreted-text role="ref"},
`RayCast2D<class_RayCast2D>`{.interpreted-text role="ref"},
`RemoteTransform2D<class_RemoteTransform2D>`{.interpreted-text
role="ref"}, `ShapeCast2D<class_ShapeCast2D>`{.interpreted-text
role="ref"}, `Skeleton2D<class_Skeleton2D>`{.interpreted-text
role="ref"}, `Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"},
`TileMap<class_TileMap>`{.interpreted-text role="ref"},
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"},
`TouchScreenButton<class_TouchScreenButton>`{.interpreted-text
role="ref"},
`VisibleOnScreenNotifier2D<class_VisibleOnScreenNotifier2D>`{.interpreted-text
role="ref"}

A 2D game object, inherited by all 2D-related nodes. Has a position,
rotation, scale, and skew.

::: rst-class
classref-introduction-group
:::

## Description

A 2D game object, with a transform (position, rotation, and scale). All
2D nodes, including physics objects and sprites, inherit from Node2D.
Use Node2D as a parent node to move, scale and rotate children in a 2D
project. Also gives control of the node\'s render order.

\*\*Note:\*\* Since both **Node2D** and
`Control<class_Control>`{.interpreted-text role="ref"} inherit from
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}, they share
several concepts from the class such as the
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} and
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} properties.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Custom drawing in 2D <../tutorials/2d/custom_drawing_in_2d>`{.interpreted-text
  role="doc"}
- [All 2D
  Demos](https://github.com/godotengine/godot-demo-projects/tree/master/2d)

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

:::: {#class_Node2D_property_global_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**global_position**
`🔗<class_Node2D_property_global_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_position**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_global_position**()

Global position. See also
`position<class_Node2D_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_global_rotation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **global_rotation**
`🔗<class_Node2D_property_global_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_rotation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_global_rotation**()

Global rotation in radians. See also
`rotation<class_Node2D_property_rotation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_global_rotation_degrees}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**global_rotation_degrees**
`🔗<class_Node2D_property_global_rotation_degrees>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_rotation_degrees**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_global_rotation_degrees**()

Helper property to access
`global_rotation<class_Node2D_property_global_rotation>`{.interpreted-text
role="ref"} in degrees instead of radians. See also
`rotation_degrees<class_Node2D_property_rotation_degrees>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_global_scale}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **global_scale**
`🔗<class_Node2D_property_global_scale>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_scale**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_global_scale**()

Global scale. See also
`scale<class_Node2D_property_scale>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_global_skew}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **global_skew**
`🔗<class_Node2D_property_global_skew>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_skew**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_global_skew**()

Global skew in radians. See also
`skew<class_Node2D_property_skew>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_global_transform}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**global_transform**
`🔗<class_Node2D_property_global_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_transform**(value:
  `Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_global_transform**()

Global `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}.
See also `transform<class_Node2D_property_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **position** =
`Vector2(0, 0)` `🔗<class_Node2D_property_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_position**()

Position, relative to the node\'s parent. See also
`global_position<class_Node2D_property_global_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_rotation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **rotation** = `0.0`
`🔗<class_Node2D_property_rotation>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_rotation**()

Rotation in radians, relative to the node\'s parent. See also
`global_rotation<class_Node2D_property_global_rotation>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is edited in the inspector in degrees. If
you want to use degrees in a script, use
`rotation_degrees<class_Node2D_property_rotation_degrees>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_rotation_degrees}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **rotation_degrees**
`🔗<class_Node2D_property_rotation_degrees>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_degrees**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_rotation_degrees**()

Helper property to access
`rotation<class_Node2D_property_rotation>`{.interpreted-text role="ref"}
in degrees instead of radians. See also
`global_rotation_degrees<class_Node2D_property_global_rotation_degrees>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_scale}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **scale** =
`Vector2(1, 1)` `🔗<class_Node2D_property_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scale**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_scale**()

The node\'s scale, relative to the node\'s parent. Unscaled value:
`(1, 1)`. See also
`global_scale<class_Node2D_property_global_scale>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Negative X scales in 2D are not decomposable from the
transformation matrix. Due to the way scale is represented with
transformation matrices in Godot, negative scales on the X axis will be
changed to negative scales on the Y axis and a rotation of 180 degrees
when decomposed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_skew}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **skew** = `0.0`
`🔗<class_Node2D_property_skew>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_skew**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_skew**()

If set to a non-zero value, slants the node in one direction or another.
This can be used for pseudo-3D effects. See also
`global_skew<class_Node2D_property_global_skew>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Skew is performed on the X axis only, and *between*
rotation and scaling.

\*\*Note:\*\* This property is edited in the inspector in degrees. If
you want to use degrees in a script, use
`skew = deg_to_rad(value_in_degrees)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_property_transform}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**transform** `🔗<class_Node2D_property_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform**(value:
  `Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_transform**()

The node\'s `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}, relative to the node\'s parent. See also
`global_transform<class_Node2D_property_global_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Node2D_method_apply_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_scale**(ratio: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_Node2D_method_apply_scale>`{.interpreted-text
role="ref"}

Multiplies the current scale by the `ratio` vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_get_angle_to}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_angle_to**(point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node2D_method_get_angle_to>`{.interpreted-text
role="ref"}

Returns the angle between the node and the `point` in radians.

\`Illustration of the returned angle.
\<https://raw.githubusercontent.com/godotengine/godot-docs/master/img/node2d_get_angle_to.png\>\`\_\_

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_get_relative_transform_to_parent}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_relative_transform_to_parent**(parent:
`Node<class_Node>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node2D_method_get_relative_transform_to_parent>`{.interpreted-text
role="ref"}

Returns the `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"} relative to this node\'s parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_global_translate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_translate**(offset: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_Node2D_method_global_translate>`{.interpreted-text role="ref"}

Adds the `offset` vector to the node\'s global position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_look_at}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**look_at**(point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_Node2D_method_look_at>`{.interpreted-text
role="ref"}

Rotates the node so that its local +X axis points towards the `point`,
which is expected to use global coordinates.

`point` should not be the same as the node\'s position, otherwise the
node always looks to the right.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_move_local_x}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_local_x**(delta: `float<class_float>`{.interpreted-text
role="ref"}, scaled: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_Node2D_method_move_local_x>`{.interpreted-text
role="ref"}

Applies a local translation on the node\'s X axis based on the
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}\'s `delta`. If `scaled` is `false`, normalizes the movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_move_local_y}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_local_y**(delta: `float<class_float>`{.interpreted-text
role="ref"}, scaled: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_Node2D_method_move_local_y>`{.interpreted-text
role="ref"}

Applies a local translation on the node\'s Y axis based on the
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}\'s `delta`. If `scaled` is `false`, normalizes the movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_rotate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate**(radians: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Node2D_method_rotate>`{.interpreted-text role="ref"}

Applies a rotation to the node, in radians, starting from its current
rotation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_to_global}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**to_global**(local_point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node2D_method_to_global>`{.interpreted-text
role="ref"}

Transforms the provided local position into a position in global
coordinate space. The input is expected to be local relative to the
**Node2D** it is called on. e.g. Applying this method to the positions
of child nodes will correctly transform their positions into the global
coordinate space, but applying it to a node\'s own position will give an
incorrect result, as it will incorporate the node\'s own transformation
into its global position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_to_local}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**to_local**(global_point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node2D_method_to_local>`{.interpreted-text
role="ref"}

Transforms the provided global position into a position in local
coordinate space. The output will be local relative to the **Node2D** it
is called on. e.g. It is appropriate for determining the positions of
child nodes, but it is not appropriate for determining its own position
relative to its parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node2D_method_translate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**translate**(offset: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_Node2D_method_translate>`{.interpreted-text
role="ref"}

Translates the node by the given `offset` in local coordinates.
