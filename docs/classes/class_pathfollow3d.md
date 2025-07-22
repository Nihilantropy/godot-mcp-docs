github_url
:   hide

# PathFollow3D {#class_PathFollow3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Point sampler for a `Path3D<class_Path3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This node takes its parent `Path3D<class_Path3D>`{.interpreted-text
role="ref"}, and returns the coordinates of a point within it, given a
distance from the first vertex.

It is useful for making other nodes follow a path, without coding the
movement pattern. For that, the nodes must be children of this node. The
descendant nodes will then move accordingly when setting the
`progress<class_PathFollow3D_property_progress>`{.interpreted-text
role="ref"} in this node.

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

:::: {#enum_PathFollow3D_RotationMode}
::: rst-class
classref-enumeration
:::
::::

enum **RotationMode**:
`🔗<enum_PathFollow3D_RotationMode>`{.interpreted-text role="ref"}

:::: {#class_PathFollow3D_constant_ROTATION_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
role="ref"} **ROTATION_NONE** = `0`

Forbids the PathFollow3D to rotate.

:::: {#class_PathFollow3D_constant_ROTATION_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
role="ref"} **ROTATION_Y** = `1`

Allows the PathFollow3D to rotate in the Y axis only.

:::: {#class_PathFollow3D_constant_ROTATION_XY}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
role="ref"} **ROTATION_XY** = `2`

Allows the PathFollow3D to rotate in both the X, and Y axes.

:::: {#class_PathFollow3D_constant_ROTATION_XYZ}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
role="ref"} **ROTATION_XYZ** = `3`

Allows the PathFollow3D to rotate in any axis.

:::: {#class_PathFollow3D_constant_ROTATION_ORIENTED}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
role="ref"} **ROTATION_ORIENTED** = `4`

Uses the up vector information in a
`Curve3D<class_Curve3D>`{.interpreted-text role="ref"} to enforce
orientation. This rotation mode requires the
`Path3D<class_Path3D>`{.interpreted-text role="ref"}\'s
`Curve3D.up_vector_enabled<class_Curve3D_property_up_vector_enabled>`{.interpreted-text
role="ref"} property to be set to `true`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_PathFollow3D_property_cubic_interp}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cubic_interp** =
`true` `🔗<class_PathFollow3D_property_cubic_interp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cubic_interpolation**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_cubic_interpolation**()

If `true`, the position between two cached points is interpolated
cubically, and linearly otherwise.

The points along the `Curve3D<class_Curve3D>`{.interpreted-text
role="ref"} of the `Path3D<class_Path3D>`{.interpreted-text role="ref"}
are precomputed before use, for faster calculations. The point at the
requested offset is then calculated interpolating between two adjacent
cached points. This may present a problem if the curve makes sharp
turns, as the cached points may not follow the curve closely enough.

There are two answers to this problem: either increase the number of
cached points and increase memory consumption, or make a cubic
interpolation between two points at the cost of (slightly) slower
calculations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow3D_property_h_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **h_offset** = `0.0`
`🔗<class_PathFollow3D_property_h_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_h_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_h_offset**()

The node\'s offset along the curve.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow3D_property_loop}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **loop** = `true`
`🔗<class_PathFollow3D_property_loop>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_loop**()

If `true`, any offset outside the path\'s length will wrap around,
instead of stopping at the ends. Use it for cyclic paths.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow3D_property_progress}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **progress** = `0.0`
`🔗<class_PathFollow3D_property_progress>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_progress**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_progress**()

The distance from the first vertex, measured in 3D units along the path.
Changing this value sets this node\'s position to a point within the
path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow3D_property_progress_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **progress_ratio** =
`0.0` `🔗<class_PathFollow3D_property_progress_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_progress_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_progress_ratio**()

The distance from the first vertex, considering 0.0 as the first vertex
and 1.0 as the last. This is just another way of expressing the progress
within the path, as the progress supplied is multiplied internally by
the path\'s length.

It can be set or get only if the **PathFollow3D** is the child of a
`Path3D<class_Path3D>`{.interpreted-text role="ref"} which is part of
the scene tree, and that this `Path3D<class_Path3D>`{.interpreted-text
role="ref"} has a `Curve3D<class_Curve3D>`{.interpreted-text role="ref"}
with a non-zero length. Otherwise, trying to set this field will print
an error, and getting this field will return `0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow3D_property_rotation_mode}
::: rst-class
classref-property
:::
::::

`RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
role="ref"} **rotation_mode** = `3`
`🔗<class_PathFollow3D_property_rotation_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_mode**(value:
  `RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
  role="ref"})
- `RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
  role="ref"} **get_rotation_mode**()

Allows or forbids rotation on one or more axes, depending on the
`RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
role="ref"} constants being used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow3D_property_tilt_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **tilt_enabled** =
`true` `🔗<class_PathFollow3D_property_tilt_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tilt_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_tilt_enabled**()

If `true`, the tilt property of
`Curve3D<class_Curve3D>`{.interpreted-text role="ref"} takes effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow3D_property_use_model_front}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_model_front** =
`false`
`🔗<class_PathFollow3D_property_use_model_front>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_model_front**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_model_front**()

If `true`, the node moves on the travel path with orienting the +Z axis
as forward. See also
`Vector3.FORWARD<class_Vector3_constant_FORWARD>`{.interpreted-text
role="ref"} and
`Vector3.MODEL_FRONT<class_Vector3_constant_MODEL_FRONT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow3D_property_v_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **v_offset** = `0.0`
`🔗<class_PathFollow3D_property_v_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_v_offset**()

The node\'s offset perpendicular to the curve.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PathFollow3D_method_correct_posture}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**correct_posture**(transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"},
rotation_mode:
`RotationMode<enum_PathFollow3D_RotationMode>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_PathFollow3D_method_correct_posture>`{.interpreted-text
role="ref"}

Correct the `transform`. `rotation_mode` implicitly specifies how
posture (forward, up and sideway direction) is calculated.
