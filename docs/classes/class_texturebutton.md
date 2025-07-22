github_url
:   hide

# TextureButton {#class_TextureButton}

**Inherits:** `BaseButton<class_BaseButton>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Texture-based button. Supports Pressed, Hover, Disabled and Focused
states.

::: rst-class
classref-introduction-group
:::

## Description

**TextureButton** has the same functionality as
`Button<class_Button>`{.interpreted-text role="ref"}, except it uses
sprites instead of Godot\'s `Theme<class_Theme>`{.interpreted-text
role="ref"} resource. It is faster to create, but it doesn\'t support
localization like more complex
`Control<class_Control>`{.interpreted-text role="ref"}s.

See also `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
which contains common properties and methods associated with this node.

\*\*Note:\*\* Setting a texture for the \"normal\" state
(`texture_normal<class_TextureButton_property_texture_normal>`{.interpreted-text
role="ref"}) is recommended. If
`texture_normal<class_TextureButton_property_texture_normal>`{.interpreted-text
role="ref"} is not set, the **TextureButton** will still receive input
events and be clickable, but the user will not be able to see it unless
they activate another one of its states with a texture assigned (e.g.,
hover over it to show
`texture_hover<class_TextureButton_property_texture_hover>`{.interpreted-text
role="ref"}).

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

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

## Enumerations

:::: {#enum_TextureButton_StretchMode}
::: rst-class
classref-enumeration
:::
::::

enum **StretchMode**:
`🔗<enum_TextureButton_StretchMode>`{.interpreted-text role="ref"}

:::: {#class_TextureButton_constant_STRETCH_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_SCALE** = `0`

Scale to fit the node\'s bounding rectangle.

:::: {#class_TextureButton_constant_STRETCH_TILE}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_TILE** = `1`

Tile inside the node\'s bounding rectangle.

:::: {#class_TextureButton_constant_STRETCH_KEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_KEEP** = `2`

The texture keeps its original size and stays in the bounding
rectangle\'s top-left corner.

:::: {#class_TextureButton_constant_STRETCH_KEEP_CENTERED}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_KEEP_CENTERED** = `3`

The texture keeps its original size and stays centered in the node\'s
bounding rectangle.

:::: {#class_TextureButton_constant_STRETCH_KEEP_ASPECT}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_KEEP_ASPECT** = `4`

Scale the texture to fit the node\'s bounding rectangle, but maintain
the texture\'s aspect ratio.

:::: {#class_TextureButton_constant_STRETCH_KEEP_ASPECT_CENTERED}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_KEEP_ASPECT_CENTERED** = `5`

Scale the texture to fit the node\'s bounding rectangle, center it, and
maintain its aspect ratio.

:::: {#class_TextureButton_constant_STRETCH_KEEP_ASPECT_COVERED}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_KEEP_ASPECT_COVERED** = `6`

Scale the texture so that the shorter side fits the bounding rectangle.
The other side clips to the node\'s limits.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TextureButton_property_flip_h}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_h** = `false`
`🔗<class_TextureButton_property_flip_h>`{.interpreted-text role="ref"}

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

:::: {#class_TextureButton_property_flip_v}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_v** = `false`
`🔗<class_TextureButton_property_flip_v>`{.interpreted-text role="ref"}

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

:::: {#class_TextureButton_property_ignore_texture_size}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ignore_texture_size**
= `false`
`🔗<class_TextureButton_property_ignore_texture_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ignore_texture_size**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_ignore_texture_size**()

If `true`, the size of the texture won\'t be considered for minimum size
calculation, so the **TextureButton** can be shrunk down past the
texture size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureButton_property_stretch_mode}
::: rst-class
classref-property
:::
::::

`StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
role="ref"} **stretch_mode** = `2`
`🔗<class_TextureButton_property_stretch_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_mode**(value:
  `StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
  role="ref"})
- `StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
  role="ref"} **get_stretch_mode**()

Controls the texture\'s behavior when you resize the node\'s bounding
rectangle. See the
`StretchMode<enum_TextureButton_StretchMode>`{.interpreted-text
role="ref"} constants for available options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureButton_property_texture_click_mask}
::: rst-class
classref-property
:::
::::

`BitMap<class_BitMap>`{.interpreted-text role="ref"}
**texture_click_mask**
`🔗<class_TextureButton_property_texture_click_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_click_mask**(value: `BitMap<class_BitMap>`{.interpreted-text
  role="ref"})
- `BitMap<class_BitMap>`{.interpreted-text role="ref"}
  **get_click_mask**()

Pure black and white `BitMap<class_BitMap>`{.interpreted-text
role="ref"} image to use for click detection. On the mask, white pixels
represent the button\'s clickable area. Use it to create buttons with
curved shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureButton_property_texture_disabled}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_disabled**
`🔗<class_TextureButton_property_texture_disabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_disabled**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture_disabled**()

Texture to display when the node is disabled. See
`BaseButton.disabled<class_BaseButton_property_disabled>`{.interpreted-text
role="ref"}. If not assigned, the **TextureButton** displays
`texture_normal<class_TextureButton_property_texture_normal>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureButton_property_texture_focused}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_focused**
`🔗<class_TextureButton_property_texture_focused>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_focused**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture_focused**()

Texture to *overlay on the base texture* when the node has mouse or
keyboard focus. Because
`texture_focused<class_TextureButton_property_texture_focused>`{.interpreted-text
role="ref"} is displayed on top of the base texture, a partially
transparent texture should be used to ensure the base texture remains
visible. A texture that represents an outline or an underline works well
for this purpose. To disable the focus visual effect, assign a fully
transparent texture of any size. Note that disabling the focus visual
effect will harm keyboard/controller navigation usability, so this is
not recommended for accessibility reasons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureButton_property_texture_hover}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_hover**
`🔗<class_TextureButton_property_texture_hover>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_hover**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture_hover**()

Texture to display when the mouse hovers over the node. If not assigned,
the **TextureButton** displays
`texture_normal<class_TextureButton_property_texture_normal>`{.interpreted-text
role="ref"} instead when hovered over.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureButton_property_texture_normal}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_normal**
`🔗<class_TextureButton_property_texture_normal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_normal**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture_normal**()

Texture to display by default, when the node is **not** in the disabled,
hover or pressed state. This texture is still displayed in the focused
state, with
`texture_focused<class_TextureButton_property_texture_focused>`{.interpreted-text
role="ref"} drawn on top.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureButton_property_texture_pressed}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_pressed**
`🔗<class_TextureButton_property_texture_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_pressed**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture_pressed**()

Texture to display on mouse down over the node, if the node has keyboard
focus and the player presses the Enter key or if the player presses the
`BaseButton.shortcut<class_BaseButton_property_shortcut>`{.interpreted-text
role="ref"} key. If not assigned, the **TextureButton** displays
`texture_hover<class_TextureButton_property_texture_hover>`{.interpreted-text
role="ref"} instead when pressed.
