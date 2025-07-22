github_url
:   hide

# PathFollow2D {#class_PathFollow2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Point sampler for a `Path2D<class_Path2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This node takes its parent `Path2D<class_Path2D>`{.interpreted-text
role="ref"}, and returns the coordinates of a point within it, given a
distance from the first vertex.

It is useful for making other nodes follow a path, without coding the
movement pattern. For that, the nodes must be children of this node. The
descendant nodes will then move accordingly when setting the
`progress<class_PathFollow2D_property_progress>`{.interpreted-text
role="ref"} in this node.

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

:::: {#class_PathFollow2D_property_cubic_interp}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cubic_interp** =
`true` `🔗<class_PathFollow2D_property_cubic_interp>`{.interpreted-text
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

The points along the `Curve2D<class_Curve2D>`{.interpreted-text
role="ref"} of the `Path2D<class_Path2D>`{.interpreted-text role="ref"}
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

:::: {#class_PathFollow2D_property_h_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **h_offset** = `0.0`
`🔗<class_PathFollow2D_property_h_offset>`{.interpreted-text role="ref"}

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

:::: {#class_PathFollow2D_property_loop}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **loop** = `true`
`🔗<class_PathFollow2D_property_loop>`{.interpreted-text role="ref"}

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

:::: {#class_PathFollow2D_property_progress}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **progress** = `0.0`
`🔗<class_PathFollow2D_property_progress>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_progress**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_progress**()

The distance along the path, in pixels. Changing this value sets this
node\'s position to a point within the path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow2D_property_progress_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **progress_ratio** =
`0.0` `🔗<class_PathFollow2D_property_progress_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_progress_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_progress_ratio**()

The distance along the path as a number in the range 0.0 (for the first
vertex) to 1.0 (for the last). This is just another way of expressing
the progress within the path, as the offset supplied is multiplied
internally by the path\'s length.

It can be set or get only if the **PathFollow2D** is the child of a
`Path2D<class_Path2D>`{.interpreted-text role="ref"} which is part of
the scene tree, and that this `Path2D<class_Path2D>`{.interpreted-text
role="ref"} has a `Curve2D<class_Curve2D>`{.interpreted-text role="ref"}
with a non-zero length. Otherwise, trying to set this field will print
an error, and getting this field will return `0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow2D_property_rotates}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **rotates** = `true`
`🔗<class_PathFollow2D_property_rotates>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotates**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_rotating**()

If `true`, this node rotates to follow the path, with the +X direction
facing forward on the path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PathFollow2D_property_v_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **v_offset** = `0.0`
`🔗<class_PathFollow2D_property_v_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_v_offset**()

The node\'s offset perpendicular to the curve.
