github_url
:   hide

# Sprite3D {#class_Sprite3D}

**Inherits:** `SpriteBase3D<class_SpriteBase3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

2D sprite node in a 3D world.

::: rst-class
classref-introduction-group
:::

## Description

A node that displays a 2D texture in a 3D environment. The texture
displayed can be a region from a larger atlas texture, or a frame from a
sprite sheet animation. See also
`SpriteBase3D<class_SpriteBase3D>`{.interpreted-text role="ref"} where
properties such as the billboard mode are defined.

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

## Signals

:::: {#class_Sprite3D_signal_frame_changed}
::: rst-class
classref-signal
:::
::::

**frame_changed**()
`🔗<class_Sprite3D_signal_frame_changed>`{.interpreted-text role="ref"}

Emitted when the
`frame<class_Sprite3D_property_frame>`{.interpreted-text role="ref"}
changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite3D_signal_texture_changed}
::: rst-class
classref-signal
:::
::::

**texture_changed**()
`🔗<class_Sprite3D_signal_texture_changed>`{.interpreted-text
role="ref"}

Emitted when the
`texture<class_Sprite3D_property_texture>`{.interpreted-text role="ref"}
changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Sprite3D_property_frame}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **frame** = `0`
`🔗<class_Sprite3D_property_frame>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frame**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_frame**()

Current frame to display from sprite sheet.
`hframes<class_Sprite3D_property_hframes>`{.interpreted-text role="ref"}
or `vframes<class_Sprite3D_property_vframes>`{.interpreted-text
role="ref"} must be greater than 1. This property is automatically
adjusted when
`hframes<class_Sprite3D_property_hframes>`{.interpreted-text role="ref"}
or `vframes<class_Sprite3D_property_vframes>`{.interpreted-text
role="ref"} are changed to keep pointing to the same visual frame (same
column and row). If that\'s impossible, this value is reset to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite3D_property_frame_coords}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**frame_coords** = `Vector2i(0, 0)`
`🔗<class_Sprite3D_property_frame_coords>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frame_coords**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_frame_coords**()

Coordinates of the frame to display from sprite sheet. This is as an
alias for the `frame<class_Sprite3D_property_frame>`{.interpreted-text
role="ref"} property.
`hframes<class_Sprite3D_property_hframes>`{.interpreted-text role="ref"}
or `vframes<class_Sprite3D_property_vframes>`{.interpreted-text
role="ref"} must be greater than 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite3D_property_hframes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hframes** = `1`
`🔗<class_Sprite3D_property_hframes>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hframes**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_hframes**()

The number of columns in the sprite sheet. When this property is
changed, `frame<class_Sprite3D_property_frame>`{.interpreted-text
role="ref"} is adjusted so that the same visual frame is maintained
(same row and column). If that\'s impossible,
`frame<class_Sprite3D_property_frame>`{.interpreted-text role="ref"} is
reset to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite3D_property_region_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **region_enabled** =
`false` `🔗<class_Sprite3D_property_region_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_region_enabled**()

If `true`, the sprite will use
`region_rect<class_Sprite3D_property_region_rect>`{.interpreted-text
role="ref"} and display only the specified part of its texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite3D_property_region_rect}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **region_rect** =
`Rect2(0, 0, 0, 0)`
`🔗<class_Sprite3D_property_region_rect>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region_rect**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"}
  **get_region_rect**()

The region of the atlas texture to display.
`region_enabled<class_Sprite3D_property_region_enabled>`{.interpreted-text
role="ref"} must be `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite3D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_Sprite3D_property_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} object to
draw. If
`GeometryInstance3D.material_override<class_GeometryInstance3D_property_material_override>`{.interpreted-text
role="ref"} is used, this will be overridden. The size information is
still used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Sprite3D_property_vframes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **vframes** = `1`
`🔗<class_Sprite3D_property_vframes>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vframes**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_vframes**()

The number of rows in the sprite sheet. When this property is changed,
`frame<class_Sprite3D_property_frame>`{.interpreted-text role="ref"} is
adjusted so that the same visual frame is maintained (same row and
column). If that\'s impossible,
`frame<class_Sprite3D_property_frame>`{.interpreted-text role="ref"} is
reset to `0`.
