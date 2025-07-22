github_url
:   hide

# TextureRect {#class_TextureRect}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A control that displays a texture.

::: rst-class
classref-introduction-group
:::

## Description

A control that displays a texture, for example an icon inside a GUI. The
texture\'s placement can be controlled with the
`stretch_mode<class_TextureRect_property_stretch_mode>`{.interpreted-text
role="ref"} property. It can scale, tile, or stay centered inside its
bounding rectangle.

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

:::: {#enum_TextureRect_ExpandMode}
::: rst-class
classref-enumeration
:::
::::

enum **ExpandMode**: `🔗<enum_TextureRect_ExpandMode>`{.interpreted-text
role="ref"}

:::: {#class_TextureRect_constant_EXPAND_KEEP_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`ExpandMode<enum_TextureRect_ExpandMode>`{.interpreted-text role="ref"}
**EXPAND_KEEP_SIZE** = `0`

The minimum size will be equal to texture size, i.e. **TextureRect**
can\'t be smaller than the texture.

:::: {#class_TextureRect_constant_EXPAND_IGNORE_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`ExpandMode<enum_TextureRect_ExpandMode>`{.interpreted-text role="ref"}
**EXPAND_IGNORE_SIZE** = `1`

The size of the texture won\'t be considered for minimum size
calculation, so the **TextureRect** can be shrunk down past the texture
size.

:::: {#class_TextureRect_constant_EXPAND_FIT_WIDTH}
::: rst-class
classref-enumeration-constant
:::
::::

`ExpandMode<enum_TextureRect_ExpandMode>`{.interpreted-text role="ref"}
**EXPAND_FIT_WIDTH** = `2`

The height of the texture will be ignored. Minimum width will be equal
to the current height. Useful for horizontal layouts, e.g. inside
`HBoxContainer<class_HBoxContainer>`{.interpreted-text role="ref"}.

:::: {#class_TextureRect_constant_EXPAND_FIT_WIDTH_PROPORTIONAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ExpandMode<enum_TextureRect_ExpandMode>`{.interpreted-text role="ref"}
**EXPAND_FIT_WIDTH_PROPORTIONAL** = `3`

Same as
`EXPAND_FIT_WIDTH<class_TextureRect_constant_EXPAND_FIT_WIDTH>`{.interpreted-text
role="ref"}, but keeps texture\'s aspect ratio.

:::: {#class_TextureRect_constant_EXPAND_FIT_HEIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`ExpandMode<enum_TextureRect_ExpandMode>`{.interpreted-text role="ref"}
**EXPAND_FIT_HEIGHT** = `4`

The width of the texture will be ignored. Minimum height will be equal
to the current width. Useful for vertical layouts, e.g. inside
`VBoxContainer<class_VBoxContainer>`{.interpreted-text role="ref"}.

:::: {#class_TextureRect_constant_EXPAND_FIT_HEIGHT_PROPORTIONAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ExpandMode<enum_TextureRect_ExpandMode>`{.interpreted-text role="ref"}
**EXPAND_FIT_HEIGHT_PROPORTIONAL** = `5`

Same as
`EXPAND_FIT_HEIGHT<class_TextureRect_constant_EXPAND_FIT_HEIGHT>`{.interpreted-text
role="ref"}, but keeps texture\'s aspect ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextureRect_StretchMode}
::: rst-class
classref-enumeration
:::
::::

enum **StretchMode**:
`🔗<enum_TextureRect_StretchMode>`{.interpreted-text role="ref"}

:::: {#class_TextureRect_constant_STRETCH_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_SCALE** = `0`

Scale to fit the node\'s bounding rectangle.

:::: {#class_TextureRect_constant_STRETCH_TILE}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_TILE** = `1`

Tile inside the node\'s bounding rectangle.

:::: {#class_TextureRect_constant_STRETCH_KEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_KEEP** = `2`

The texture keeps its original size and stays in the bounding
rectangle\'s top-left corner.

:::: {#class_TextureRect_constant_STRETCH_KEEP_CENTERED}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_KEEP_CENTERED** = `3`

The texture keeps its original size and stays centered in the node\'s
bounding rectangle.

:::: {#class_TextureRect_constant_STRETCH_KEEP_ASPECT}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_KEEP_ASPECT** = `4`

Scale the texture to fit the node\'s bounding rectangle, but maintain
the texture\'s aspect ratio.

:::: {#class_TextureRect_constant_STRETCH_KEEP_ASPECT_CENTERED}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
role="ref"} **STRETCH_KEEP_ASPECT_CENTERED** = `5`

Scale the texture to fit the node\'s bounding rectangle, center it and
maintain its aspect ratio.

:::: {#class_TextureRect_constant_STRETCH_KEEP_ASPECT_COVERED}
::: rst-class
classref-enumeration-constant
:::
::::

`StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
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

:::: {#class_TextureRect_property_expand_mode}
::: rst-class
classref-property
:::
::::

`ExpandMode<enum_TextureRect_ExpandMode>`{.interpreted-text role="ref"}
**expand_mode** = `0`
`🔗<class_TextureRect_property_expand_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_expand_mode**(value:
  `ExpandMode<enum_TextureRect_ExpandMode>`{.interpreted-text
  role="ref"})
- `ExpandMode<enum_TextureRect_ExpandMode>`{.interpreted-text
  role="ref"} **get_expand_mode**()

**Experimental:** Using
`EXPAND_FIT_WIDTH<class_TextureRect_constant_EXPAND_FIT_WIDTH>`{.interpreted-text
role="ref"},
`EXPAND_FIT_WIDTH_PROPORTIONAL<class_TextureRect_constant_EXPAND_FIT_WIDTH_PROPORTIONAL>`{.interpreted-text
role="ref"},
`EXPAND_FIT_HEIGHT<class_TextureRect_constant_EXPAND_FIT_HEIGHT>`{.interpreted-text
role="ref"}, or
`EXPAND_FIT_HEIGHT_PROPORTIONAL<class_TextureRect_constant_EXPAND_FIT_HEIGHT_PROPORTIONAL>`{.interpreted-text
role="ref"} may result in unstable behavior in some
`Container<class_Container>`{.interpreted-text role="ref"} controls.
This behavior may be re-evaluated and changed in the future.

Defines how minimum size is determined based on the texture\'s size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureRect_property_flip_h}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_h** = `false`
`🔗<class_TextureRect_property_flip_h>`{.interpreted-text role="ref"}

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

:::: {#class_TextureRect_property_flip_v}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_v** = `false`
`🔗<class_TextureRect_property_flip_v>`{.interpreted-text role="ref"}

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

:::: {#class_TextureRect_property_stretch_mode}
::: rst-class
classref-property
:::
::::

`StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
role="ref"} **stretch_mode** = `0`
`🔗<class_TextureRect_property_stretch_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_mode**(value:
  `StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
  role="ref"})
- `StretchMode<enum_TextureRect_StretchMode>`{.interpreted-text
  role="ref"} **get_stretch_mode**()

Controls the texture\'s behavior when resizing the node\'s bounding
rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureRect_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_TextureRect_property_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

The node\'s `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
resource.
