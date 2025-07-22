github_url
:   hide

# Sprite2D {#class_Sprite2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

General-purpose sprite node.

::: rst-class
classref-introduction-group
:::

## Description

A node that displays a 2D texture. The texture displayed can be a region
from a larger atlas texture, or a frame from a sprite sheet animation.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Instancing Demo](https://godotengine.org/asset-library/asset/2716)

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

:::: {#class_Sprite2D_signal_frame_changed}
::: rst-class
classref-signal
:::
::::

**frame_changed**()
`🔗<class_Sprite2D_signal_frame_changed>`{.interpreted-text role="ref"}

Emitted when the
`frame<class_Sprite2D_property_frame>`{.interpreted-text role="ref"}
changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_signal_texture_changed}
::: rst-class
classref-signal
:::
::::

**texture_changed**()
`🔗<class_Sprite2D_signal_texture_changed>`{.interpreted-text
role="ref"}

Emitted when the
`texture<class_Sprite2D_property_texture>`{.interpreted-text role="ref"}
changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Sprite2D_property_centered}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **centered** = `true`
`🔗<class_Sprite2D_property_centered>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_centered**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_centered**()

If `true`, texture is centered.

\*\*Note:\*\* For games with a pixel art aesthetic, textures may appear
deformed when centered. This is caused by their position being between
pixels. To prevent this, set this property to `false`, or consider
enabling
`ProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_vertices_to_pixel>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_transforms_to_pixel>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_flip_h}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_h** = `false`
`🔗<class_Sprite2D_property_flip_h>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flip_h**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_flipped_h**()

If `true`, texture is flipped horizontally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_flip_v}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_v** = `false`
`🔗<class_Sprite2D_property_flip_v>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flip_v**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_flipped_v**()

If `true`, texture is flipped vertically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_frame}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **frame** = `0`
`🔗<class_Sprite2D_property_frame>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frame**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_frame**()

Current frame to display from sprite sheet.
`hframes<class_Sprite2D_property_hframes>`{.interpreted-text role="ref"}
or `vframes<class_Sprite2D_property_vframes>`{.interpreted-text
role="ref"} must be greater than 1. This property is automatically
adjusted when
`hframes<class_Sprite2D_property_hframes>`{.interpreted-text role="ref"}
or `vframes<class_Sprite2D_property_vframes>`{.interpreted-text
role="ref"} are changed to keep pointing to the same visual frame (same
column and row). If that\'s impossible, this value is reset to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_frame_coords}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**frame_coords** = `Vector2i(0, 0)`
`🔗<class_Sprite2D_property_frame_coords>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frame_coords**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_frame_coords**()

Coordinates of the frame to display from sprite sheet. This is as an
alias for the `frame<class_Sprite2D_property_frame>`{.interpreted-text
role="ref"} property.
`hframes<class_Sprite2D_property_hframes>`{.interpreted-text role="ref"}
or `vframes<class_Sprite2D_property_vframes>`{.interpreted-text
role="ref"} must be greater than 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_hframes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hframes** = `1`
`🔗<class_Sprite2D_property_hframes>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hframes**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_hframes**()

The number of columns in the sprite sheet. When this property is
changed, `frame<class_Sprite2D_property_frame>`{.interpreted-text
role="ref"} is adjusted so that the same visual frame is maintained
(same row and column). If that\'s impossible,
`frame<class_Sprite2D_property_frame>`{.interpreted-text role="ref"} is
reset to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)` `🔗<class_Sprite2D_property_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_offset**()

The texture\'s drawing offset.

\*\*Note:\*\* When you increase
`offset<class_Sprite2D_property_offset>`{.interpreted-text role="ref"}.y
in Sprite2D, the sprite moves downward on screen (i.e., +Y is down).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_region_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **region_enabled** =
`false` `🔗<class_Sprite2D_property_region_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_region_enabled**()

If `true`, texture is cut from a larger atlas texture. See
`region_rect<class_Sprite2D_property_region_rect>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_region_filter_clip_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**region_filter_clip_enabled** = `false`
`🔗<class_Sprite2D_property_region_filter_clip_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region_filter_clip_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_region_filter_clip_enabled**()

If `true`, the area outside of the
`region_rect<class_Sprite2D_property_region_rect>`{.interpreted-text
role="ref"} is clipped to avoid bleeding of the surrounding texture
pixels.
`region_enabled<class_Sprite2D_property_region_enabled>`{.interpreted-text
role="ref"} must be `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_region_rect}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **region_rect** =
`Rect2(0, 0, 0, 0)`
`🔗<class_Sprite2D_property_region_rect>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region_rect**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"}
  **get_region_rect**()

The region of the atlas texture to display.
`region_enabled<class_Sprite2D_property_region_enabled>`{.interpreted-text
role="ref"} must be `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_Sprite2D_property_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} object to
draw.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_property_vframes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **vframes** = `1`
`🔗<class_Sprite2D_property_vframes>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vframes**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_vframes**()

The number of rows in the sprite sheet. When this property is changed,
`frame<class_Sprite2D_property_frame>`{.interpreted-text role="ref"} is
adjusted so that the same visual frame is maintained (same row and
column). If that\'s impossible,
`frame<class_Sprite2D_property_frame>`{.interpreted-text role="ref"} is
reset to `0`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Sprite2D_method_get_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Sprite2D_method_get_rect>`{.interpreted-text
role="ref"}

Returns a `Rect2<class_Rect2>`{.interpreted-text role="ref"}
representing the Sprite2D\'s boundary in local coordinates.

\*\*Example:\*\* Detect if the Sprite2D was clicked:

::::: tabs
::: code-tab
gdscript

func [input]{#input}(event):

:   

    if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:

    :   

        if get_rect().has_point(to_local(event.position)):

        :   print(\"A click!\")
:::

::: code-tab
csharp

public override void [Input]{#input}(InputEvent \@event) { if (@event is
InputEventMouseButton inputEventMouse) { if (inputEventMouse.Pressed &&
inputEventMouse.ButtonIndex == MouseButton.Left) { if
(GetRect().HasPoint(ToLocal(inputEventMouse.Position))) { GD.Print(\"A
click!\"); } } } }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite2D_method_is_pixel_opaque}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_pixel_opaque**(pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Sprite2D_method_is_pixel_opaque>`{.interpreted-text
role="ref"}

Returns `true`, if the pixel at the given position is opaque and `false`
in other case. The position is in local coordinates.

\*\*Note:\*\* It also returns `false`, if the sprite\'s texture is
`null` or if the given position is invalid.
