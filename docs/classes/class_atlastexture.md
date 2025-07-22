github_url
:   hide

# AtlasTexture {#class_AtlasTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A texture that crops out part of another Texture2D.

::: rst-class
classref-introduction-group
:::

## Description

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} resource that
draws only part of its
`atlas<class_AtlasTexture_property_atlas>`{.interpreted-text role="ref"}
texture, as defined by the
`region<class_AtlasTexture_property_region>`{.interpreted-text
role="ref"}. An additional
`margin<class_AtlasTexture_property_margin>`{.interpreted-text
role="ref"} can also be set, which is useful for small adjustments.

Multiple **AtlasTexture** resources can be cropped from the same
`atlas<class_AtlasTexture_property_atlas>`{.interpreted-text
role="ref"}. Packing many smaller textures into a singular large texture
helps to optimize video memory costs and render calls.

\*\*Note:\*\* **AtlasTexture** cannot be used in an
`AnimatedTexture<class_AnimatedTexture>`{.interpreted-text role="ref"},
and will not tile properly in nodes such as
`TextureRect<class_TextureRect>`{.interpreted-text role="ref"} or
`Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"}. To tile an
**AtlasTexture**, modify its
`region<class_AtlasTexture_property_region>`{.interpreted-text
role="ref"} instead.

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

:::: {#class_AtlasTexture_property_atlas}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **atlas**
`🔗<class_AtlasTexture_property_atlas>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_atlas**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_atlas**()

The texture that contains the atlas. Can be any type inheriting from
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, including
another **AtlasTexture**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AtlasTexture_property_filter_clip}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **filter_clip** =
`false` `🔗<class_AtlasTexture_property_filter_clip>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filter_clip**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_filter_clip**()

If `true`, the area outside of the
`region<class_AtlasTexture_property_region>`{.interpreted-text
role="ref"} is clipped to avoid bleeding of the surrounding texture
pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AtlasTexture_property_margin}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **margin** =
`Rect2(0, 0, 0, 0)`
`🔗<class_AtlasTexture_property_margin>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margin**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_margin**()

The margin around the
`region<class_AtlasTexture_property_region>`{.interpreted-text
role="ref"}. Useful for small adjustments. If the
`Rect2.size<class_Rect2_property_size>`{.interpreted-text role="ref"} of
this property (\"w\" and \"h\" in the editor) is set, the drawn texture
is resized to fit within the margin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AtlasTexture_property_region}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **region** =
`Rect2(0, 0, 0, 0)`
`🔗<class_AtlasTexture_property_region>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_region**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_region**()

The region used to draw the
`atlas<class_AtlasTexture_property_atlas>`{.interpreted-text
role="ref"}. If either dimension of the region\'s size is `0`, the value
from `atlas<class_AtlasTexture_property_atlas>`{.interpreted-text
role="ref"} size will be used for that axis instead.
