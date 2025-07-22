github_url
:   hide

# CanvasLayer {#class_CanvasLayer}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`ParallaxBackground<class_ParallaxBackground>`{.interpreted-text
role="ref"}

A node used for independent rendering of objects within a 2D scene.

::: rst-class
classref-introduction-group
:::

## Description

`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}-derived
nodes that are direct or indirect children of a **CanvasLayer** will be
drawn in that layer. The layer is a numeric index that defines the draw
order. The default 2D scene renders with index `0`, so a **CanvasLayer**
with index `-1` will be drawn below, and a **CanvasLayer** with index
`1` will be drawn above. This order will hold regardless of the
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} of the nodes within each layer.

\*\*CanvasLayer\*\*s can be hidden and they can also optionally follow
the viewport. This makes them useful for HUDs like health bar overlays
(on layers `1` and higher) or backgrounds (on layers `-1` and lower).

\*\*Note:\*\* Embedded `Window<class_Window>`{.interpreted-text
role="ref"}s are placed on layer `1024`.
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}s on layers
`1025` and higher appear in front of embedded windows.

\*\*Note:\*\* Each **CanvasLayer** is drawn on one specific
`Viewport<class_Viewport>`{.interpreted-text role="ref"} and cannot be
shared between multiple `Viewport<class_Viewport>`{.interpreted-text
role="ref"}s, see
`custom_viewport<class_CanvasLayer_property_custom_viewport>`{.interpreted-text
role="ref"}. When using multiple
`Viewport<class_Viewport>`{.interpreted-text role="ref"}s, for example
in a split-screen game, you need to create an individual **CanvasLayer**
for each `Viewport<class_Viewport>`{.interpreted-text role="ref"} you
want it to be drawn on.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Viewport and canvas transforms <../tutorials/2d/2d_transforms>`{.interpreted-text
  role="doc"}
- `Canvas layers <../tutorials/2d/canvas_layers>`{.interpreted-text
  role="doc"}
- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)

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

:::: {#class_CanvasLayer_signal_visibility_changed}
::: rst-class
classref-signal
:::
::::

**visibility_changed**()
`🔗<class_CanvasLayer_signal_visibility_changed>`{.interpreted-text
role="ref"}

Emitted when visibility of the layer is changed. See
`visible<class_CanvasLayer_property_visible>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CanvasLayer_property_custom_viewport}
::: rst-class
classref-property
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **custom_viewport**
`🔗<class_CanvasLayer_property_custom_viewport>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_viewport**(value: `Node<class_Node>`{.interpreted-text
  role="ref"})
- `Node<class_Node>`{.interpreted-text role="ref"}
  **get_custom_viewport**()

The custom `Viewport<class_Viewport>`{.interpreted-text role="ref"} node
assigned to the **CanvasLayer**. If `null`, uses the default viewport
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_property_follow_viewport_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**follow_viewport_enabled** = `false`
`🔗<class_CanvasLayer_property_follow_viewport_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_follow_viewport**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_following_viewport**()

If enabled, the **CanvasLayer** maintains its position in world space.
If disabled, the **CanvasLayer** stays in a fixed position on the
screen.

Together with
`follow_viewport_scale<class_CanvasLayer_property_follow_viewport_scale>`{.interpreted-text
role="ref"}, this can be used for a pseudo-3D effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_property_follow_viewport_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**follow_viewport_scale** = `1.0`
`🔗<class_CanvasLayer_property_follow_viewport_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_follow_viewport_scale**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_follow_viewport_scale**()

Scales the layer when using
`follow_viewport_enabled<class_CanvasLayer_property_follow_viewport_enabled>`{.interpreted-text
role="ref"}. Layers moving into the foreground should have increasing
scales, while layers moving into the background should have decreasing
scales.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_property_layer}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **layer** = `1`
`🔗<class_CanvasLayer_property_layer>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_layer**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_layer**()

Layer index for draw order. Lower values are drawn behind higher values.

\*\*Note:\*\* If multiple CanvasLayers have the same layer index,
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} children of
one CanvasLayer are drawn behind the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} children of
the other CanvasLayer. Which CanvasLayer is drawn in front is
non-deterministic.

\*\*Note:\*\* The layer index should be between
`RenderingServer.CANVAS_LAYER_MIN<class_RenderingServer_constant_CANVAS_LAYER_MIN>`{.interpreted-text
role="ref"} and
`RenderingServer.CANVAS_LAYER_MAX<class_RenderingServer_constant_CANVAS_LAYER_MAX>`{.interpreted-text
role="ref"} (inclusive). Any other value will wrap around.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)`
`🔗<class_CanvasLayer_property_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_offset**()

The layer\'s base offset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_property_rotation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **rotation** = `0.0`
`🔗<class_CanvasLayer_property_rotation>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_rotation**()

The layer\'s rotation in radians.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_property_scale}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **scale** =
`Vector2(1, 1)` `🔗<class_CanvasLayer_property_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scale**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_scale**()

The layer\'s scale.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_property_transform}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**transform** = `Transform2D(1, 0, 0, 1, 0, 0)`
`🔗<class_CanvasLayer_property_transform>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform**(value:
  `Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_transform**()

The layer\'s transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_property_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **visible** = `true`
`🔗<class_CanvasLayer_property_visible>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_visible**()

If `false`, any `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} under this **CanvasLayer** will be hidden.

Unlike
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"}, visibility of a **CanvasLayer** isn\'t propagated to
underlying layers.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CanvasLayer_method_get_canvas}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_canvas**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CanvasLayer_method_get_canvas>`{.interpreted-text
role="ref"}

Returns the RID of the canvas used by this layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_method_get_final_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_final_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasLayer_method_get_final_transform>`{.interpreted-text
role="ref"}

Returns the transform from the **CanvasLayer**s coordinate system to the
`Viewport<class_Viewport>`{.interpreted-text role="ref"}s coordinate
system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_method_hide}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **hide**()
`🔗<class_CanvasLayer_method_hide>`{.interpreted-text role="ref"}

Hides any `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
under this **CanvasLayer**. This is equivalent to setting
`visible<class_CanvasLayer_property_visible>`{.interpreted-text
role="ref"} to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasLayer_method_show}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **show**()
`🔗<class_CanvasLayer_method_show>`{.interpreted-text role="ref"}

Shows any `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
under this **CanvasLayer**. This is equivalent to setting
`visible<class_CanvasLayer_property_visible>`{.interpreted-text
role="ref"} to `true`.
