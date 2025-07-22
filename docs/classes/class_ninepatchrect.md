github_url
:   hide

# NinePatchRect {#class_NinePatchRect}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A control that displays a texture by keeping its corners intact, but
tiling its edges and center.

::: rst-class
classref-introduction-group
:::

## Description

Also known as 9-slice panels, **NinePatchRect** produces clean panels of
any size based on a small texture. To do so, it splits the texture in a
3×3 grid. When you scale the node, it tiles the texture\'s edges
horizontally or vertically, tiles the center on both axes, and leaves
the corners unchanged.

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

:::: {#class_NinePatchRect_signal_texture_changed}
::: rst-class
classref-signal
:::
::::

**texture_changed**()
`🔗<class_NinePatchRect_signal_texture_changed>`{.interpreted-text
role="ref"}

Emitted when the node\'s texture changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_NinePatchRect_AxisStretchMode}
::: rst-class
classref-enumeration
:::
::::

enum **AxisStretchMode**:
`🔗<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text role="ref"}

:::: {#class_NinePatchRect_constant_AXIS_STRETCH_MODE_STRETCH}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisStretchMode<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text
role="ref"} **AXIS_STRETCH_MODE_STRETCH** = `0`

Stretches the center texture across the NinePatchRect. This may cause
the texture to be distorted.

:::: {#class_NinePatchRect_constant_AXIS_STRETCH_MODE_TILE}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisStretchMode<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text
role="ref"} **AXIS_STRETCH_MODE_TILE** = `1`

Repeats the center texture across the NinePatchRect. This won\'t cause
any visible distortion. The texture must be seamless for this to work
without displaying artifacts between edges.

:::: {#class_NinePatchRect_constant_AXIS_STRETCH_MODE_TILE_FIT}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisStretchMode<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text
role="ref"} **AXIS_STRETCH_MODE_TILE_FIT** = `2`

Repeats the center texture across the NinePatchRect, but will also
stretch the texture to make sure each tile is visible in full. This may
cause the texture to be distorted, but less than
`AXIS_STRETCH_MODE_STRETCH<class_NinePatchRect_constant_AXIS_STRETCH_MODE_STRETCH>`{.interpreted-text
role="ref"}. The texture must be seamless for this to work without
displaying artifacts between edges.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_NinePatchRect_property_axis_stretch_horizontal}
::: rst-class
classref-property
:::
::::

`AxisStretchMode<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text
role="ref"} **axis_stretch_horizontal** = `0`
`🔗<class_NinePatchRect_property_axis_stretch_horizontal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_h_axis_stretch_mode**(value:
  `AxisStretchMode<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text
  role="ref"})
- `AxisStretchMode<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text
  role="ref"} **get_h_axis_stretch_mode**()

The stretch mode to use for horizontal stretching/tiling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NinePatchRect_property_axis_stretch_vertical}
::: rst-class
classref-property
:::
::::

`AxisStretchMode<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text
role="ref"} **axis_stretch_vertical** = `0`
`🔗<class_NinePatchRect_property_axis_stretch_vertical>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_axis_stretch_mode**(value:
  `AxisStretchMode<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text
  role="ref"})
- `AxisStretchMode<enum_NinePatchRect_AxisStretchMode>`{.interpreted-text
  role="ref"} **get_v_axis_stretch_mode**()

The stretch mode to use for vertical stretching/tiling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NinePatchRect_property_draw_center}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_center** =
`true` `🔗<class_NinePatchRect_property_draw_center>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_center**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_draw_center_enabled**()

If `true`, draw the panel\'s center. Else, only draw the 9-slice\'s
borders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NinePatchRect_property_patch_margin_bottom}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **patch_margin_bottom** =
`0`
`🔗<class_NinePatchRect_property_patch_margin_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_patch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_patch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The height of the 9-slice\'s bottom row. A margin of 16 means the
9-slice\'s bottom corners and side will have a height of 16 pixels. You
can set all 4 margin values individually to create panels with
non-uniform borders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NinePatchRect_property_patch_margin_left}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **patch_margin_left** =
`0`
`🔗<class_NinePatchRect_property_patch_margin_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_patch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_patch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The width of the 9-slice\'s left column. A margin of 16 means the
9-slice\'s left corners and side will have a width of 16 pixels. You can
set all 4 margin values individually to create panels with non-uniform
borders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NinePatchRect_property_patch_margin_right}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **patch_margin_right** =
`0`
`🔗<class_NinePatchRect_property_patch_margin_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_patch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_patch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The width of the 9-slice\'s right column. A margin of 16 means the
9-slice\'s right corners and side will have a width of 16 pixels. You
can set all 4 margin values individually to create panels with
non-uniform borders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NinePatchRect_property_patch_margin_top}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **patch_margin_top** =
`0`
`🔗<class_NinePatchRect_property_patch_margin_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_patch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_patch_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The height of the 9-slice\'s top row. A margin of 16 means the
9-slice\'s top corners and side will have a height of 16 pixels. You can
set all 4 margin values individually to create panels with non-uniform
borders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NinePatchRect_property_region_rect}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **region_rect** =
`Rect2(0, 0, 0, 0)`
`🔗<class_NinePatchRect_property_region_rect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region_rect**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"}
  **get_region_rect**()

Rectangular region of the texture to sample from. If you\'re working
with an atlas, use this property to define the area the 9-slice should
use. All other properties are relative to this one. If the rect is
empty, NinePatchRect will use the whole texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NinePatchRect_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_NinePatchRect_property_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

The node\'s texture resource.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NinePatchRect_method_get_patch_margin}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_patch_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NinePatchRect_method_get_patch_margin>`{.interpreted-text
role="ref"}

Returns the size of the margin on the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NinePatchRect_method_set_patch_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_patch_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_NinePatchRect_method_set_patch_margin>`{.interpreted-text
role="ref"}

Sets the size of the margin on the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"} to `value`
pixels.
