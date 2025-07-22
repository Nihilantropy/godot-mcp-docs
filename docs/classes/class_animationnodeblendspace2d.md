github_url
:   hide

# AnimationNodeBlendSpace2D {#class_AnimationNodeBlendSpace2D}

**Inherits:**
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A set of `AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s placed on 2D coordinates, crossfading between the three
adjacent ones. Used by
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A resource used by
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

\*\*AnimationNodeBlendSpace2D\*\* represents a virtual 2D space on which
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s are placed. Outputs the linear blend of the three adjacent
animations using a `Vector2<class_Vector2>`{.interpreted-text
role="ref"} weight. Adjacent in this context means the three
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s making up the triangle that contains the current value.

You can add vertices to the blend space with
`add_blend_point()<class_AnimationNodeBlendSpace2D_method_add_blend_point>`{.interpreted-text
role="ref"} and automatically triangulate it by setting
`auto_triangles<class_AnimationNodeBlendSpace2D_property_auto_triangles>`{.interpreted-text
role="ref"} to `true`. Otherwise, use
`add_triangle()<class_AnimationNodeBlendSpace2D_method_add_triangle>`{.interpreted-text
role="ref"} and
`remove_triangle()<class_AnimationNodeBlendSpace2D_method_remove_triangle>`{.interpreted-text
role="ref"} to triangulate the blend space by hand.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

## Signals

:::: {#class_AnimationNodeBlendSpace2D_signal_triangles_updated}
::: rst-class
classref-signal
:::
::::

**triangles_updated**()
`🔗<class_AnimationNodeBlendSpace2D_signal_triangles_updated>`{.interpreted-text
role="ref"}

Emitted every time the blend space\'s triangles are created, removed, or
when one of their vertices changes position.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AnimationNodeBlendSpace2D_BlendMode}
::: rst-class
classref-enumeration
:::
::::

enum **BlendMode**:
`🔗<enum_AnimationNodeBlendSpace2D_BlendMode>`{.interpreted-text
role="ref"}

:::: {#class_AnimationNodeBlendSpace2D_constant_BLEND_MODE_INTERPOLATED}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.

:::: {#class_AnimationNodeBlendSpace2D_constant_BLEND_MODE_DISCRETE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending
position is closest to. Useful for frame-by-frame 2D animations.

:::: {#class_AnimationNodeBlendSpace2D_constant_BLEND_MODE_DISCRETE_CARRY}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to
`BLEND_MODE_DISCRETE<class_AnimationNodeBlendSpace2D_constant_BLEND_MODE_DISCRETE>`{.interpreted-text
role="ref"}, but starts the new animation at the last animation\'s
playback position.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationNodeBlendSpace2D_property_auto_triangles}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **auto_triangles** =
`true`
`🔗<class_AnimationNodeBlendSpace2D_property_auto_triangles>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_triangles**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_auto_triangles**()

If `true`, the blend space is triangulated automatically. The mesh
updates every time you add or remove points with
`add_blend_point()<class_AnimationNodeBlendSpace2D_method_add_blend_point>`{.interpreted-text
role="ref"} and
`remove_blend_point()<class_AnimationNodeBlendSpace2D_method_remove_blend_point>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_property_blend_mode}
::: rst-class
classref-property
:::
::::

`BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>`{.interpreted-text
role="ref"} **blend_mode** = `0`
`🔗<class_AnimationNodeBlendSpace2D_property_blend_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_mode**(value:
  `BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>`{.interpreted-text
  role="ref"})
- `BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>`{.interpreted-text
  role="ref"} **get_blend_mode**()

Controls the interpolation between animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_property_max_space}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **max_space** =
`Vector2(1, 1)`
`🔗<class_AnimationNodeBlendSpace2D_property_max_space>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_space**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_max_space**()

The blend space\'s X and Y axes\' upper limit for the points\' position.
See
`add_blend_point()<class_AnimationNodeBlendSpace2D_method_add_blend_point>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_property_min_space}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **min_space** =
`Vector2(-1, -1)`
`🔗<class_AnimationNodeBlendSpace2D_property_min_space>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_space**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_min_space**()

The blend space\'s X and Y axes\' lower limit for the points\' position.
See
`add_blend_point()<class_AnimationNodeBlendSpace2D_method_add_blend_point>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_property_snap}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **snap** =
`Vector2(0.1, 0.1)`
`🔗<class_AnimationNodeBlendSpace2D_property_snap>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_snap**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_snap**()

Position increment to snap to when moving a point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_property_sync}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sync** = `false`
`🔗<class_AnimationNodeBlendSpace2D_property_sync>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_sync**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_using_sync**()

If `false`, the blended animations\' frame are stopped when the blend
value is `0`.

If `true`, forcing the blended animations to advance frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_property_x_label}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **x_label** = `"x"`
`🔗<class_AnimationNodeBlendSpace2D_property_x_label>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_x_label**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_x_label**()

Name of the blend space\'s X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_property_y_label}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **y_label** = `"y"`
`🔗<class_AnimationNodeBlendSpace2D_property_y_label>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_y_label**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_y_label**()

Name of the blend space\'s Y axis.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationNodeBlendSpace2D_method_add_blend_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_blend_point**(node:
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, at_index: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`🔗<class_AnimationNodeBlendSpace2D_method_add_blend_point>`{.interpreted-text
role="ref"}

Adds a new point that represents a `node` at the position set by `pos`.
You can insert it at a specific index using the `at_index` argument. If
you use the default value for `at_index`, the point is inserted at the
end of the blend points array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_add_triangle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_triangle**(x: `int<class_int>`{.interpreted-text role="ref"}, y:
`int<class_int>`{.interpreted-text role="ref"}, z:
`int<class_int>`{.interpreted-text role="ref"}, at_index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_AnimationNodeBlendSpace2D_method_add_triangle>`{.interpreted-text
role="ref"}

Creates a new triangle using three points `x`, `y`, and `z`. Triangles
can overlap. You can insert the triangle at a specific index using the
`at_index` argument. If you use the default value for `at_index`, the
point is inserted at the end of the blend points array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_get_blend_point_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_blend_point_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendSpace2D_method_get_blend_point_count>`{.interpreted-text
role="ref"}

Returns the number of points in the blend space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_get_blend_point_node}
::: rst-class
classref-method
:::
::::

`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} **get_blend_point_node**(point:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendSpace2D_method_get_blend_point_node>`{.interpreted-text
role="ref"}

Returns the
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} referenced by the point at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_get_blend_point_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_blend_point_position**(point: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendSpace2D_method_get_blend_point_position>`{.interpreted-text
role="ref"}

Returns the position of the point at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_get_triangle_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_triangle_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendSpace2D_method_get_triangle_count>`{.interpreted-text
role="ref"}

Returns the number of triangles in the blend space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_get_triangle_point}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_triangle_point**(triangle: `int<class_int>`{.interpreted-text
role="ref"}, point: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeBlendSpace2D_method_get_triangle_point>`{.interpreted-text
role="ref"}

Returns the position of the point at index `point` in the triangle of
index `triangle`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_remove_blend_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_blend_point**(point: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeBlendSpace2D_method_remove_blend_point>`{.interpreted-text
role="ref"}

Removes the point at index `point` from the blend space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_remove_triangle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_triangle**(triangle: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeBlendSpace2D_method_remove_triangle>`{.interpreted-text
role="ref"}

Removes the triangle at index `triangle` from the blend space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_set_blend_point_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_blend_point_node**(point: `int<class_int>`{.interpreted-text
role="ref"}, node:
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeBlendSpace2D_method_set_blend_point_node>`{.interpreted-text
role="ref"}

Changes the `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} referenced by the point at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace2D_method_set_blend_point_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_blend_point_position**(point: `int<class_int>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeBlendSpace2D_method_set_blend_point_position>`{.interpreted-text
role="ref"}

Updates the position of the point at index `point` in the blend space.
