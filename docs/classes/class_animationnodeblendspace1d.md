github_url
:   hide

# AnimationNodeBlendSpace1D {#class_AnimationNodeBlendSpace1D}

**Inherits:**
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A set of `AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s placed on a virtual axis, crossfading between the two
adjacent ones. Used by
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A resource used by
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

\*\*AnimationNodeBlendSpace1D\*\* represents a virtual axis on which any
type of `AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s can be added using
`add_blend_point()<class_AnimationNodeBlendSpace1D_method_add_blend_point>`{.interpreted-text
role="ref"}. Outputs the linear blend of the two
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s adjacent to the current value.

You can set the extents of the axis with
`min_space<class_AnimationNodeBlendSpace1D_property_min_space>`{.interpreted-text
role="ref"} and
`max_space<class_AnimationNodeBlendSpace1D_property_max_space>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
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

:::: {#enum_AnimationNodeBlendSpace1D_BlendMode}
::: rst-class
classref-enumeration
:::
::::

enum **BlendMode**:
`🔗<enum_AnimationNodeBlendSpace1D_BlendMode>`{.interpreted-text
role="ref"}

:::: {#class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_INTERPOLATED}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.

:::: {#class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_DISCRETE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending
position is closest to. Useful for frame-by-frame 2D animations.

:::: {#class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_DISCRETE_CARRY}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>`{.interpreted-text
role="ref"} **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to
`BLEND_MODE_DISCRETE<class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_DISCRETE>`{.interpreted-text
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

:::: {#class_AnimationNodeBlendSpace1D_property_blend_mode}
::: rst-class
classref-property
:::
::::

`BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>`{.interpreted-text
role="ref"} **blend_mode** = `0`
`🔗<class_AnimationNodeBlendSpace1D_property_blend_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_mode**(value:
  `BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>`{.interpreted-text
  role="ref"})
- `BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>`{.interpreted-text
  role="ref"} **get_blend_mode**()

Controls the interpolation between animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_property_max_space}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_space** = `1.0`
`🔗<class_AnimationNodeBlendSpace1D_property_max_space>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_space**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_max_space**()

The blend space\'s axis\'s upper limit for the points\' position. See
`add_blend_point()<class_AnimationNodeBlendSpace1D_method_add_blend_point>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_property_min_space}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **min_space** =
`-1.0`
`🔗<class_AnimationNodeBlendSpace1D_property_min_space>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_space**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_min_space**()

The blend space\'s axis\'s lower limit for the points\' position. See
`add_blend_point()<class_AnimationNodeBlendSpace1D_method_add_blend_point>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_property_snap}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **snap** = `0.1`
`🔗<class_AnimationNodeBlendSpace1D_property_snap>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_snap**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_snap**()

Position increment to snap to when moving a point on the axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_property_sync}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sync** = `false`
`🔗<class_AnimationNodeBlendSpace1D_property_sync>`{.interpreted-text
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

:::: {#class_AnimationNodeBlendSpace1D_property_value_label}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **value_label** =
`"value"`
`🔗<class_AnimationNodeBlendSpace1D_property_value_label>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_value_label**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_value_label**()

Label of the virtual axis of the blend space.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationNodeBlendSpace1D_method_add_blend_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_blend_point**(node:
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, pos: `float<class_float>`{.interpreted-text role="ref"},
at_index: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_AnimationNodeBlendSpace1D_method_add_blend_point>`{.interpreted-text
role="ref"}

Adds a new point that represents a `node` on the virtual axis at a given
position set by `pos`. You can insert it at a specific index using the
`at_index` argument. If you use the default value for `at_index`, the
point is inserted at the end of the blend points array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_method_get_blend_point_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_blend_point_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_count>`{.interpreted-text
role="ref"}

Returns the number of points on the blend axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_method_get_blend_point_node}
::: rst-class
classref-method
:::
::::

`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} **get_blend_point_node**(point:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_node>`{.interpreted-text
role="ref"}

Returns the `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} referenced by the point at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_method_get_blend_point_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_blend_point_position**(point: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_position>`{.interpreted-text
role="ref"}

Returns the position of the point at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_method_remove_blend_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_blend_point**(point: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeBlendSpace1D_method_remove_blend_point>`{.interpreted-text
role="ref"}

Removes the point at index `point` from the blend axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_method_set_blend_point_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_blend_point_node**(point: `int<class_int>`{.interpreted-text
role="ref"}, node:
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNodeBlendSpace1D_method_set_blend_point_node>`{.interpreted-text
role="ref"}

Changes the `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} referenced by the point at index `point`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeBlendSpace1D_method_set_blend_point_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_blend_point_position**(point: `int<class_int>`{.interpreted-text
role="ref"}, pos: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_AnimationNodeBlendSpace1D_method_set_blend_point_position>`{.interpreted-text
role="ref"}

Updates the position of the point at index `point` on the blend axis.
