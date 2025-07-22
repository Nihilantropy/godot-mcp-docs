github_url
:   hide

# Line2D {#class_Line2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D polyline that can optionally be textured.

::: rst-class
classref-introduction-group
:::

## Description

This node draws a 2D polyline, i.e. a shape consisting of several points
connected by segments. **Line2D** is not a mathematical polyline, i.e.
the segments are not infinitely thin. It is intended for rendering and
it can be colored and optionally textured.

\*\*Warning:\*\* Certain configurations may be impossible to draw
nicely, such as very sharp angles. In these situations, the node uses
fallback drawing logic to look decent.

\*\*Note:\*\* **Line2D** is drawn using a 2D mesh.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Matrix Transform
  Demo](https://godotengine.org/asset-library/asset/2787)
- [2.5D Game Demo](https://godotengine.org/asset-library/asset/2783)

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

:::: {#enum_Line2D_LineJointMode}
::: rst-class
classref-enumeration
:::
::::

enum **LineJointMode**:
`🔗<enum_Line2D_LineJointMode>`{.interpreted-text role="ref"}

:::: {#class_Line2D_constant_LINE_JOINT_SHARP}
::: rst-class
classref-enumeration-constant
:::
::::

`LineJointMode<enum_Line2D_LineJointMode>`{.interpreted-text role="ref"}
**LINE_JOINT_SHARP** = `0`

Makes the polyline\'s joints pointy, connecting the sides of the two
segments by extending them until they intersect. If the rotation of a
joint is too big (based on
`sharp_limit<class_Line2D_property_sharp_limit>`{.interpreted-text
role="ref"}), the joint falls back to
`LINE_JOINT_BEVEL<class_Line2D_constant_LINE_JOINT_BEVEL>`{.interpreted-text
role="ref"} to prevent very long miters.

:::: {#class_Line2D_constant_LINE_JOINT_BEVEL}
::: rst-class
classref-enumeration-constant
:::
::::

`LineJointMode<enum_Line2D_LineJointMode>`{.interpreted-text role="ref"}
**LINE_JOINT_BEVEL** = `1`

Makes the polyline\'s joints bevelled/chamfered, connecting the sides of
the two segments with a simple line.

:::: {#class_Line2D_constant_LINE_JOINT_ROUND}
::: rst-class
classref-enumeration-constant
:::
::::

`LineJointMode<enum_Line2D_LineJointMode>`{.interpreted-text role="ref"}
**LINE_JOINT_ROUND** = `2`

Makes the polyline\'s joints rounded, connecting the sides of the two
segments with an arc. The detail of this arc depends on
`round_precision<class_Line2D_property_round_precision>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Line2D_LineCapMode}
::: rst-class
classref-enumeration
:::
::::

enum **LineCapMode**: `🔗<enum_Line2D_LineCapMode>`{.interpreted-text
role="ref"}

:::: {#class_Line2D_constant_LINE_CAP_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`LineCapMode<enum_Line2D_LineCapMode>`{.interpreted-text role="ref"}
**LINE_CAP_NONE** = `0`

Draws no line cap.

:::: {#class_Line2D_constant_LINE_CAP_BOX}
::: rst-class
classref-enumeration-constant
:::
::::

`LineCapMode<enum_Line2D_LineCapMode>`{.interpreted-text role="ref"}
**LINE_CAP_BOX** = `1`

Draws the line cap as a box, slightly extending the first/last segment.

:::: {#class_Line2D_constant_LINE_CAP_ROUND}
::: rst-class
classref-enumeration-constant
:::
::::

`LineCapMode<enum_Line2D_LineCapMode>`{.interpreted-text role="ref"}
**LINE_CAP_ROUND** = `2`

Draws the line cap as a semicircle attached to the first/last segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Line2D_LineTextureMode}
::: rst-class
classref-enumeration
:::
::::

enum **LineTextureMode**:
`🔗<enum_Line2D_LineTextureMode>`{.interpreted-text role="ref"}

:::: {#class_Line2D_constant_LINE_TEXTURE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`LineTextureMode<enum_Line2D_LineTextureMode>`{.interpreted-text
role="ref"} **LINE_TEXTURE_NONE** = `0`

Takes the left pixels of the texture and renders them over the whole
polyline.

:::: {#class_Line2D_constant_LINE_TEXTURE_TILE}
::: rst-class
classref-enumeration-constant
:::
::::

`LineTextureMode<enum_Line2D_LineTextureMode>`{.interpreted-text
role="ref"} **LINE_TEXTURE_TILE** = `1`

Tiles the texture over the polyline.
`CanvasItem.texture_repeat<class_CanvasItem_property_texture_repeat>`{.interpreted-text
role="ref"} of the **Line2D** node must be
`CanvasItem.TEXTURE_REPEAT_ENABLED<class_CanvasItem_constant_TEXTURE_REPEAT_ENABLED>`{.interpreted-text
role="ref"} or
`CanvasItem.TEXTURE_REPEAT_MIRROR<class_CanvasItem_constant_TEXTURE_REPEAT_MIRROR>`{.interpreted-text
role="ref"} for it to work properly.

:::: {#class_Line2D_constant_LINE_TEXTURE_STRETCH}
::: rst-class
classref-enumeration-constant
:::
::::

`LineTextureMode<enum_Line2D_LineTextureMode>`{.interpreted-text
role="ref"} **LINE_TEXTURE_STRETCH** = `2`

Stretches the texture across the polyline.
`CanvasItem.texture_repeat<class_CanvasItem_property_texture_repeat>`{.interpreted-text
role="ref"} of the **Line2D** node must be
`CanvasItem.TEXTURE_REPEAT_DISABLED<class_CanvasItem_constant_TEXTURE_REPEAT_DISABLED>`{.interpreted-text
role="ref"} for best results.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Line2D_property_antialiased}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **antialiased** =
`false` `🔗<class_Line2D_property_antialiased>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_antialiased**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_antialiased**()

If `true`, the polyline\'s border will be anti-aliased.

\*\*Note:\*\* **Line2D** is not accelerated by batching when being
anti-aliased.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_begin_cap_mode}
::: rst-class
classref-property
:::
::::

`LineCapMode<enum_Line2D_LineCapMode>`{.interpreted-text role="ref"}
**begin_cap_mode** = `0`
`🔗<class_Line2D_property_begin_cap_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_begin_cap_mode**(value:
  `LineCapMode<enum_Line2D_LineCapMode>`{.interpreted-text role="ref"})
- `LineCapMode<enum_Line2D_LineCapMode>`{.interpreted-text role="ref"}
  **get_begin_cap_mode**()

The style of the beginning of the polyline, if
`closed<class_Line2D_property_closed>`{.interpreted-text role="ref"} is
`false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_closed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **closed** = `false`
`🔗<class_Line2D_property_closed>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_closed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_closed**()

If `true` and the polyline has more than 2 points, the last point and
the first one will be connected by a segment.

\*\*Note:\*\* The shape of the closing segment is not guaranteed to be
seamless if a
`width_curve<class_Line2D_property_width_curve>`{.interpreted-text
role="ref"} is provided.

\*\*Note:\*\* The joint between the closing segment and the first
segment is drawn first and it samples the
`gradient<class_Line2D_property_gradient>`{.interpreted-text role="ref"}
and the
`width_curve<class_Line2D_property_width_curve>`{.interpreted-text
role="ref"} at the beginning. This is an implementation detail that
might change in a future version.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_default_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **default_color** =
`Color(1, 1, 1, 1)`
`🔗<class_Line2D_property_default_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_default_color**()

The color of the polyline. Will not be used if a gradient is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_end_cap_mode}
::: rst-class
classref-property
:::
::::

`LineCapMode<enum_Line2D_LineCapMode>`{.interpreted-text role="ref"}
**end_cap_mode** = `0`
`🔗<class_Line2D_property_end_cap_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_end_cap_mode**(value:
  `LineCapMode<enum_Line2D_LineCapMode>`{.interpreted-text role="ref"})
- `LineCapMode<enum_Line2D_LineCapMode>`{.interpreted-text role="ref"}
  **get_end_cap_mode**()

The style of the end of the polyline, if
`closed<class_Line2D_property_closed>`{.interpreted-text role="ref"} is
`false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_gradient}
::: rst-class
classref-property
:::
::::

`Gradient<class_Gradient>`{.interpreted-text role="ref"} **gradient**
`🔗<class_Line2D_property_gradient>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gradient**(value: `Gradient<class_Gradient>`{.interpreted-text
  role="ref"})
- `Gradient<class_Gradient>`{.interpreted-text role="ref"}
  **get_gradient**()

The gradient is drawn through the whole line from start to finish. The
`default_color<class_Line2D_property_default_color>`{.interpreted-text
role="ref"} will not be used if this property is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_joint_mode}
::: rst-class
classref-property
:::
::::

`LineJointMode<enum_Line2D_LineJointMode>`{.interpreted-text role="ref"}
**joint_mode** = `0`
`🔗<class_Line2D_property_joint_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_joint_mode**(value:
  `LineJointMode<enum_Line2D_LineJointMode>`{.interpreted-text
  role="ref"})
- `LineJointMode<enum_Line2D_LineJointMode>`{.interpreted-text
  role="ref"} **get_joint_mode**()

The style of the connections between segments of the polyline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_points}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **points** = `PackedVector2Array()`
`🔗<class_Line2D_property_points>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_points**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_points**()

The points of the polyline, interpreted in local 2D coordinates.
Segments are drawn between the adjacent points in this array.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_round_precision}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **round_precision** = `8`
`🔗<class_Line2D_property_round_precision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_round_precision**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_round_precision**()

The smoothness used for rounded joints and caps. Higher values result in
smoother corners, but are more demanding to render and update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_sharp_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sharp_limit** =
`2.0` `🔗<class_Line2D_property_sharp_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sharp_limit**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sharp_limit**()

Determines the miter limit of the polyline. Normally, when
`joint_mode<class_Line2D_property_joint_mode>`{.interpreted-text
role="ref"} is set to
`LINE_JOINT_SHARP<class_Line2D_constant_LINE_JOINT_SHARP>`{.interpreted-text
role="ref"}, sharp angles fall back to using the logic of
`LINE_JOINT_BEVEL<class_Line2D_constant_LINE_JOINT_BEVEL>`{.interpreted-text
role="ref"} joints to prevent very long miters. Higher values of this
property mean that the fallback to a bevel joint will happen at sharper
angles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_Line2D_property_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

The texture used for the polyline. Uses
`texture_mode<class_Line2D_property_texture_mode>`{.interpreted-text
role="ref"} for drawing style.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_texture_mode}
::: rst-class
classref-property
:::
::::

`LineTextureMode<enum_Line2D_LineTextureMode>`{.interpreted-text
role="ref"} **texture_mode** = `0`
`🔗<class_Line2D_property_texture_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_mode**(value:
  `LineTextureMode<enum_Line2D_LineTextureMode>`{.interpreted-text
  role="ref"})
- `LineTextureMode<enum_Line2D_LineTextureMode>`{.interpreted-text
  role="ref"} **get_texture_mode**()

The style to render the
`texture<class_Line2D_property_texture>`{.interpreted-text role="ref"}
of the polyline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **width** = `10.0`
`🔗<class_Line2D_property_width>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_width**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_width**()

The polyline\'s width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_property_width_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **width_curve**
`🔗<class_Line2D_property_width_curve>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"} **get_curve**()

The polyline\'s width curve. The width of the polyline over its length
will be equivalent to the value of the width curve over its domain. The
width curve should be a unit `Curve<class_Curve>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Line2D_method_add_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_point**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_Line2D_method_add_point>`{.interpreted-text role="ref"}

Adds a point with the specified `position` relative to the polyline\'s
own position. If no `index` is provided, the new point will be added to
the end of the points array.

If `index` is given, the new point is inserted before the existing point
identified by index `index`. The indices of the points after the new
point get increased by 1. The provided `index` must not exceed the
number of existing points in the polyline. See
`get_point_count()<class_Line2D_method_get_point_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_method_clear_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_points**()
`🔗<class_Line2D_method_clear_points>`{.interpreted-text role="ref"}

Removes all points from the polyline, making it empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_method_get_point_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_point_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Line2D_method_get_point_count>`{.interpreted-text
role="ref"}

Returns the number of points in the polyline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_method_get_point_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_point_position**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Line2D_method_get_point_position>`{.interpreted-text
role="ref"}

Returns the position of the point at index `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_method_remove_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_point**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Line2D_method_remove_point>`{.interpreted-text role="ref"}

Removes the point at index `index` from the polyline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Line2D_method_set_point_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_position**(index: `int<class_int>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_Line2D_method_set_point_position>`{.interpreted-text
role="ref"}

Overwrites the position of the point at the given `index` with the
supplied `position`.
