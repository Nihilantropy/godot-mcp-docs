github_url
:   hide

# ResourceImporterTextureAtlas {#class_ResourceImporterTextureAtlas}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports a collection of textures from a PNG image into an optimized
`AtlasTexture<class_AtlasTexture>`{.interpreted-text role="ref"} for 2D
rendering.

::: rst-class
classref-introduction-group
:::

## Description

This imports a collection of textures from a PNG image into an
`AtlasTexture<class_AtlasTexture>`{.interpreted-text role="ref"} or 2D
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}. This can be
used to save memory when importing 2D animations from spritesheets.
Texture atlases are only supported in 2D rendering, not 3D. See also
`ResourceImporterTexture<class_ResourceImporterTexture>`{.interpreted-text
role="ref"} and
`ResourceImporterLayeredTexture<class_ResourceImporterLayeredTexture>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* **ResourceImporterTextureAtlas** does not handle importing
`TileSetAtlasSource<class_TileSetAtlasSource>`{.interpreted-text
role="ref"}, which is created using the
`TileSet<class_TileSet>`{.interpreted-text role="ref"} editor instead.

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

:::: {#class_ResourceImporterTextureAtlas_property_atlas_file}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **atlas_file** =
`""`
`🔗<class_ResourceImporterTextureAtlas_property_atlas_file>`{.interpreted-text
role="ref"}

Path to the atlas spritesheet. This *must* be set to valid path to a PNG
image. Otherwise, the atlas will fail to import.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTextureAtlas_property_crop_to_region}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **crop_to_region** =
`false`
`🔗<class_ResourceImporterTextureAtlas_property_crop_to_region>`{.interpreted-text
role="ref"}

If `true`, discards empty areas from the atlas. This only affects final
sprite positioning, not storage. See also
`trim_alpha_border_from_region<class_ResourceImporterTextureAtlas_property_trim_alpha_border_from_region>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only effective if
`import_mode<class_ResourceImporterTextureAtlas_property_import_mode>`{.interpreted-text
role="ref"} is **Region**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTextureAtlas_property_import_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **import_mode** = `0`
`🔗<class_ResourceImporterTextureAtlas_property_import_mode>`{.interpreted-text
role="ref"}

**Region:** Imports the atlas in an
`AtlasTexture<class_AtlasTexture>`{.interpreted-text role="ref"}
resource, which is rendered as a rectangle. This is fast to render, but
transparent areas still have to be rendered if they can\'t be trimmed
effectively by
`trim_alpha_border_from_region<class_ResourceImporterTextureAtlas_property_trim_alpha_border_from_region>`{.interpreted-text
role="ref"}. This can reduce performance when rendering large sprites on
screen.

\*\*Mesh:\*\* Imports the atlas as an
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"} resource,
keeping the original bitmap visible (but rendered as a polygon). This
can be used to reduce fill rate when rendering large transparent
sprites, at the cost of slower rendering if there are little to no
transparent areas in the sprite.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTextureAtlas_property_trim_alpha_border_from_region}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**trim_alpha_border_from_region** = `true`
`🔗<class_ResourceImporterTextureAtlas_property_trim_alpha_border_from_region>`{.interpreted-text
role="ref"}

If `true`, trims the region to exclude fully transparent pixels using a
clipping rectangle (which is never rotated). This can be used to save
memory. See also
`crop_to_region<class_ResourceImporterTextureAtlas_property_crop_to_region>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only effective if
`import_mode<class_ResourceImporterTextureAtlas_property_import_mode>`{.interpreted-text
role="ref"} is **Region**.
