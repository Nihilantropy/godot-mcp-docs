github_url
:   hide

# ResourceImporterTexture {#class_ResourceImporterTexture}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports an image for use in 2D or 3D rendering.

::: rst-class
classref-introduction-group
:::

## Description

This importer imports
`CompressedTexture2D<class_CompressedTexture2D>`{.interpreted-text
role="ref"} resources. If you need to process the image in scripts in a
more convenient way, use
`ResourceImporterImage<class_ResourceImporterImage>`{.interpreted-text
role="ref"} instead. See also
`ResourceImporterLayeredTexture<class_ResourceImporterLayeredTexture>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Importing images <../tutorials/assets_pipeline/importing_images>`{.interpreted-text
  role="doc"}

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

:::: {#class_ResourceImporterTexture_property_compress/channel_pack}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **compress/channel_pack**
= `0`
`🔗<class_ResourceImporterTexture_property_compress/channel_pack>`{.interpreted-text
role="ref"}

Controls how color channels should be used in the imported texture.

\*\*sRGB Friendly:\*\* Prevents the RG color format from being used, as
it does not support sRGB color.

\*\*Optimized:\*\* Allows the RG color format to be used if the texture
does not use the blue channel. This reduces memory usage if the
texture\'s blue channel can be discarded (all pixels must have a blue
value of `0`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_compress/hdr_compression}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**compress/hdr_compression** = `1`
`🔗<class_ResourceImporterTexture_property_compress/hdr_compression>`{.interpreted-text
role="ref"}

Controls how VRAM compression should be performed for HDR images.

\*\*Disabled:\*\* Never use VRAM compression for HDR textures,
regardless of whether they\'re opaque or transparent. Instead, the
texture is converted to RGBE9995 (9-bits per channel + 5-bit exponent =
32 bits per pixel) to reduce memory usage compared to a half-float or
single-precision float image format.

\*\*Opaque Only:\*\* Only uses VRAM compression for opaque HDR textures.
This is due to a limitation of HDR formats, as there is no
VRAM-compressed HDR format that supports transparency at the same time.

\*\*Always:\*\* Force VRAM compression even for HDR textures with an
alpha channel. To perform this, the alpha channel is discarded on
import.

\*\*Note:\*\* Only effective on Radiance HDR (`.hdr`) and OpenEXR
(`.exr`) images.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_compress/high_quality}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**compress/high_quality** = `false`
`🔗<class_ResourceImporterTexture_property_compress/high_quality>`{.interpreted-text
role="ref"}

If `true`, uses BPTC compression on desktop platforms and ASTC
compression on mobile platforms. When using BPTC, BC7 is used for SDR
textures and BC6H is used for HDR textures.

If `false`, uses the faster but lower-quality S3TC compression on
desktop platforms and ETC2 on mobile/web platforms. When using S3TC,
DXT1 (BC1) is used for opaque textures and DXT5 (BC3) is used for
transparent or normal map (RGTC) textures.

BPTC and ASTC support VRAM compression for HDR textures, but S3TC and
ETC2 do not (see
`compress/hdr_compression<class_ResourceImporterTexture_property_compress/hdr_compression>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_compress/lossy_quality}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**compress/lossy_quality** = `0.7`
`🔗<class_ResourceImporterTexture_property_compress/lossy_quality>`{.interpreted-text
role="ref"}

The quality to use when using the **Lossy** compression mode. Higher
values result in better quality, at the cost of larger file sizes. Lossy
quality does not affect memory usage of the imported texture, only its
file size on disk.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_compress/mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **compress/mode** = `0`
`🔗<class_ResourceImporterTexture_property_compress/mode>`{.interpreted-text
role="ref"}

The compression mode to use. Each compression mode provides a different
tradeoff:

\*\*Lossless\*\*: Original quality, high memory usage, high size on
disk, fast import.

\*\*Lossy:\*\* Reduced quality, high memory usage, low size on disk,
fast import.

\*\*VRAM Compressed:\*\* Reduced quality, low memory usage, low size on
disk, slowest import. Only use for textures in 3D scenes, not for 2D
elements.

\*\*VRAM Uncompressed:\*\* Original quality, high memory usage, highest
size on disk, fastest import.

\*\*Basis Universal:\*\* Reduced quality, low memory usage, lowest size
on disk, slow import. Only use for textures in 3D scenes, not for 2D
elements.

See [Compress
mode](../tutorials/assets_pipeline/importing_images.html#compress-mode)
in the manual for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_compress/normal_map}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **compress/normal_map** =
`0`
`🔗<class_ResourceImporterTexture_property_compress/normal_map>`{.interpreted-text
role="ref"}

When using a texture as normal map, only the red and green channels are
required. Given regular texture compression algorithms produce artifacts
that don\'t look that nice in normal maps, the RGTC compression format
is the best fit for this data. Forcing this option to Enable will make
Godot import the image as RGTC compressed. By default, it\'s set to
Detect. This means that if the texture is ever detected to be used as a
normal map, it will be changed to Enable and reimported automatically.

Note that RGTC compression affects the resulting normal map image. You
will have to adjust custom shaders that use the normal map\'s blue
channel to take this into account. Built-in material shaders already
ignore the blue channel in a normal map (regardless of the actual normal
map\'s contents).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_compress/rdo_quality_loss}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**compress/rdo_quality_loss** = `0.0`
`🔗<class_ResourceImporterTexture_property_compress/rdo_quality_loss>`{.interpreted-text
role="ref"}

If greater than or equal to `0.01`, enables Rate-Distortion Optimization
(RDO) to reduce file size. Higher values result in smaller file sizes
but lower quality.

\*\*Note:\*\* Enabling RDO makes encoding times significantly longer,
especially when the image is large.

See also
`ProjectSettings.rendering/textures/basis_universal/rdo_dict_size<class_ProjectSettings_property_rendering/textures/basis_universal/rdo_dict_size>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/textures/basis_universal/zstd_supercompression_level<class_ProjectSettings_property_rendering/textures/basis_universal/zstd_supercompression_level>`{.interpreted-text
role="ref"} if you want to reduce the file size further.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_compress/uastc_level}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **compress/uastc_level**
= `0`
`🔗<class_ResourceImporterTexture_property_compress/uastc_level>`{.interpreted-text
role="ref"}

The UASTC encoding level. Higher values result in better quality but
make encoding times longer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_detect_3d/compress_to}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **detect_3d/compress_to**
= `1`
`🔗<class_ResourceImporterTexture_property_detect_3d/compress_to>`{.interpreted-text
role="ref"}

This changes the
`compress/mode<class_ResourceImporterTexture_property_compress/mode>`{.interpreted-text
role="ref"} option that is used when a texture is detected as being used
in 3D.

Changing this import option only has an effect if a texture is detected
as being used in 3D. Changing this to **Disabled** then reimporting will
not change the existing compress mode on a texture (if it\'s detected to
be used in 3D), but choosing **VRAM Compressed** or **Basis Universal**
will.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_editor/convert_colors_with_editor_theme}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editor/convert_colors_with_editor_theme** = `false`
`🔗<class_ResourceImporterTexture_property_editor/convert_colors_with_editor_theme>`{.interpreted-text
role="ref"}

If `true`, converts the imported image\'s colors to match
`EditorSettings.interface/theme/icon_and_font_color<class_EditorSettings_property_interface/theme/icon_and_font_color>`{.interpreted-text
role="ref"}. This assumes the image uses the exact same colors as
`Godot's own color palette for editor icons <../contributing/development/editor/creating_icons>`{.interpreted-text
role="doc"}, with the source file designed for a dark editor theme. This
should be enabled for editor plugin icons and custom class icons, but
should be left disabled otherwise.

\*\*Note:\*\* Only available for SVG images.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_editor/scale_with_editor_scale}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editor/scale_with_editor_scale** = `false`
`🔗<class_ResourceImporterTexture_property_editor/scale_with_editor_scale>`{.interpreted-text
role="ref"}

If `true`, scales the imported image to match
`EditorSettings.interface/editor/custom_display_scale<class_EditorSettings_property_interface/editor/custom_display_scale>`{.interpreted-text
role="ref"}. This should be enabled for editor plugin icons and custom
class icons, but should be left disabled otherwise.

\*\*Note:\*\* Only available for SVG images.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_mipmaps/generate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **mipmaps/generate** =
`false`
`🔗<class_ResourceImporterTexture_property_mipmaps/generate>`{.interpreted-text
role="ref"}

If `true`, smaller versions of the texture are generated on import. For
example, a 64×64 texture will generate 6 mipmaps (32×32, 16×16, 8×8,
4×4, 2×2, 1×1). This has several benefits:

- Textures will not become grainy in the distance (in 3D), or if scaled
  down due to `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
  zoom or `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
  scale (in 2D).
- Performance will improve if the texture is displayed in the distance,
  since sampling smaller versions of the original texture is faster and
  requires less memory bandwidth.

The downside of mipmaps is that they increase memory usage by roughly
33%.

It\'s recommended to enable mipmaps in 3D. However, in 2D, this should
only be enabled if your project visibly benefits from having mipmaps
enabled. If the camera never zooms out significantly, there won\'t be a
benefit to enabling mipmaps but memory usage will increase.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_mipmaps/limit}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **mipmaps/limit** = `-1`
`🔗<class_ResourceImporterTexture_property_mipmaps/limit>`{.interpreted-text
role="ref"}

Unimplemented. This currently has no effect when changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/channel_remap/alpha}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**process/channel_remap/alpha** = `3`
`🔗<class_ResourceImporterTexture_property_process/channel_remap/alpha>`{.interpreted-text
role="ref"}

Specifies the data source of the output image\'s alpha channel.

\*\*Red:\*\* Use the values from the source image\'s red channel.

\*\*Green:\*\* Use the values from the source image\'s green channel.

\*\*Blue:\*\* Use the values from the source image\'s blue channel.

\*\*Alpha:\*\* Use the values from the source image\'s alpha channel.

\*\*Red Inverted:\*\* Use inverted values from the source image\'s red
channel (`1.0 - R`).

\*\*Green Inverted:\*\* Use inverted values from the source image\'s
green channel (`1.0 - G`).

\*\*Blue Inverted:\*\* Use inverted values from the source image\'s blue
channel (`1.0 - B`).

\*\*Alpha Inverted:\*\* Use inverted values from the source image\'s
alpha channel (`1.0 - A`).

\*\*Unused:\*\* Set the color channel\'s value to the default (`1.0` for
alpha, `0.0` for red, green or blue).

\*\*Zero:\*\* Set the color channel\'s value to `0.0`.

\*\*One:\*\* Set the color channel\'s value to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/channel_remap/blue}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**process/channel_remap/blue** = `2`
`🔗<class_ResourceImporterTexture_property_process/channel_remap/blue>`{.interpreted-text
role="ref"}

Specifies the data source of the output image\'s blue channel.

\*\*Red:\*\* Use the values from the source image\'s red channel.

\*\*Green:\*\* Use the values from the source image\'s green channel.

\*\*Blue:\*\* Use the values from the source image\'s blue channel.

\*\*Alpha:\*\* Use the values from the source image\'s alpha channel.

\*\*Red Inverted:\*\* Use inverted values from the source image\'s red
channel (`1.0 - R`).

\*\*Green Inverted:\*\* Use inverted values from the source image\'s
green channel (`1.0 - G`).

\*\*Blue Inverted:\*\* Use inverted values from the source image\'s blue
channel (`1.0 - B`).

\*\*Alpha Inverted:\*\* Use inverted values from the source image\'s
alpha channel (`1.0 - A`).

\*\*Unused:\*\* Set the color channel\'s value to the default (`1.0` for
alpha, `0.0` for red, green or blue).

\*\*Zero:\*\* Set the color channel\'s value to `0.0`.

\*\*One:\*\* Set the color channel\'s value to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/channel_remap/green}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**process/channel_remap/green** = `1`
`🔗<class_ResourceImporterTexture_property_process/channel_remap/green>`{.interpreted-text
role="ref"}

Specifies the data source of the output image\'s green channel.

\*\*Red:\*\* Use the values from the source image\'s red channel.

\*\*Green:\*\* Use the values from the source image\'s green channel.

\*\*Blue:\*\* Use the values from the source image\'s blue channel.

\*\*Alpha:\*\* Use the values from the source image\'s alpha channel.

\*\*Red Inverted:\*\* Use inverted values from the source image\'s red
channel (`1.0 - R`).

\*\*Green Inverted:\*\* Use inverted values from the source image\'s
green channel (`1.0 - G`).

\*\*Blue Inverted:\*\* Use inverted values from the source image\'s blue
channel (`1.0 - B`).

\*\*Alpha Inverted:\*\* Use inverted values from the source image\'s
alpha channel (`1.0 - A`).

\*\*Unused:\*\* Set the color channel\'s value to the default (`1.0` for
alpha, `0.0` for red, green or blue).

\*\*Zero:\*\* Set the color channel\'s value to `0.0`.

\*\*One:\*\* Set the color channel\'s value to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/channel_remap/red}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**process/channel_remap/red** = `0`
`🔗<class_ResourceImporterTexture_property_process/channel_remap/red>`{.interpreted-text
role="ref"}

Specifies the data source of the output image\'s red channel.

\*\*Red:\*\* Use the values from the source image\'s red channel.

\*\*Green:\*\* Use the values from the source image\'s green channel.

\*\*Blue:\*\* Use the values from the source image\'s blue channel.

\*\*Alpha:\*\* Use the values from the source image\'s alpha channel.

\*\*Red Inverted:\*\* Use inverted values from the source image\'s red
channel (`1.0 - R`).

\*\*Green Inverted:\*\* Use inverted values from the source image\'s
green channel (`1.0 - G`).

\*\*Blue Inverted:\*\* Use inverted values from the source image\'s blue
channel (`1.0 - B`).

\*\*Alpha Inverted:\*\* Use inverted values from the source image\'s
alpha channel (`1.0 - A`).

\*\*Unused:\*\* Set the color channel\'s value to the default (`1.0` for
alpha, `0.0` for red, green or blue).

\*\*Zero:\*\* Set the color channel\'s value to `0.0`.

\*\*One:\*\* Set the color channel\'s value to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/fix_alpha_border}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**process/fix_alpha_border** = `true`
`🔗<class_ResourceImporterTexture_property_process/fix_alpha_border>`{.interpreted-text
role="ref"}

If `true`, puts pixels of the same surrounding color in transition from
transparent to opaque areas. For textures displayed with bilinear
filtering, this helps to reduce the outline effect when exporting images
from an image editor.

It\'s recommended to leave this enabled (as it is by default), unless
this causes issues for a particular image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/hdr_as_srgb}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **process/hdr_as_srgb**
= `false`
`🔗<class_ResourceImporterTexture_property_process/hdr_as_srgb>`{.interpreted-text
role="ref"}

Some HDR images you can find online may be broken and contain sRGB color
data (instead of linear color data). It is advised not to use those
files. If you absolutely have to, enabling
`process/hdr_as_srgb<class_ResourceImporterTexture_property_process/hdr_as_srgb>`{.interpreted-text
role="ref"} will make them look correct.

\*\*Warning:\*\* Enabling
`process/hdr_as_srgb<class_ResourceImporterTexture_property_process/hdr_as_srgb>`{.interpreted-text
role="ref"} on well-formatted HDR images will cause the resulting image
to look too dark, so leave this on `false` if unsure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/hdr_clamp_exposure}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**process/hdr_clamp_exposure** = `false`
`🔗<class_ResourceImporterTexture_property_process/hdr_clamp_exposure>`{.interpreted-text
role="ref"}

If `true`, clamps exposure in the imported high dynamic range images
using a smart clamping formula (without introducing *visible* clipping).

Some HDR panorama images you can find online may contain extremely
bright pixels, due to being taken from real life sources without any
clipping.

While these HDR panorama images are accurate to real life, this can
cause the radiance map generated by Godot to contain sparkles when used
as a background sky. This can be seen in material reflections (even on
rough materials in extreme cases). Enabling
`process/hdr_clamp_exposure<class_ResourceImporterTexture_property_process/hdr_clamp_exposure>`{.interpreted-text
role="ref"} can resolve this.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/normal_map_invert_y}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**process/normal_map_invert_y** = `false`
`🔗<class_ResourceImporterTexture_property_process/normal_map_invert_y>`{.interpreted-text
role="ref"}

**Deprecated:** The same result can be achieved by setting
`process/channel_remap/green<class_ResourceImporterTexture_property_process/channel_remap/green>`{.interpreted-text
role="ref"} to `Green Inverted`.

If `true`, convert the normal map from Y- (DirectX-style) to Y+
(OpenGL-style) by inverting its green color channel. This is the normal
map convention expected by Godot.

More information about normal maps (including a coordinate order table
for popular engines) can be found
[here](http://wiki.polycount.com/wiki/Normal_Map_Technical_Details).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/premult_alpha}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**process/premult_alpha** = `false`
`🔗<class_ResourceImporterTexture_property_process/premult_alpha>`{.interpreted-text
role="ref"}

An alternative to fixing darkened borders with
`process/fix_alpha_border<class_ResourceImporterTexture_property_process/fix_alpha_border>`{.interpreted-text
role="ref"} is to use premultiplied alpha. By enabling this option, the
texture will be converted to this format. A premultiplied alpha texture
requires specific materials to be displayed correctly:

- In 2D, a
  `CanvasItemMaterial<class_CanvasItemMaterial>`{.interpreted-text
  role="ref"} will need to be created and configured to use the
  `CanvasItemMaterial.BLEND_MODE_PREMULT_ALPHA<class_CanvasItemMaterial_constant_BLEND_MODE_PREMULT_ALPHA>`{.interpreted-text
  role="ref"} blend mode on
  `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}s that use
  this texture. In custom `@canvas_item` shaders,
  `render_mode blend_premul_alpha;` should be used.
- In 3D, a `BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text
  role="ref"} will need to be created and configured to use the
  `BaseMaterial3D.BLEND_MODE_PREMULT_ALPHA<class_BaseMaterial3D_constant_BLEND_MODE_PREMULT_ALPHA>`{.interpreted-text
  role="ref"} blend mode on materials that use this texture. In custom
  `spatial` shaders, `render_mode blend_premul_alpha;` should be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_process/size_limit}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **process/size_limit** =
`0`
`🔗<class_ResourceImporterTexture_property_process/size_limit>`{.interpreted-text
role="ref"}

If set to a value greater than `0`, the size of the texture is limited
on import to a value smaller than or equal to the value specified here.
For non-square textures, the size limit affects the longer dimension,
with the shorter dimension scaled to preserve aspect ratio. Resizing is
performed using cubic interpolation.

This can be used to reduce memory usage without affecting the source
images, or avoid issues with textures not displaying on mobile/web
platforms (as these usually can\'t display textures larger than
4096×4096).

\*\*Note:\*\* Even if this is set to `0`, import size is limited to the
following dimensions for technical reasons. Depending on
`compress/mode<class_ResourceImporterTexture_property_compress/mode>`{.interpreted-text
role="ref"}, textures will be downsampled on import if necessary:

- **Lossy:** 16383 pixels width or height, whichever is larger;
- **Basis Universal:** 16384 pixels width or height, whichever is
  larger;
- **All other modes:** 32768 pixels width or height, whichever is
  larger.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_roughness/mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **roughness/mode** = `0`
`🔗<class_ResourceImporterTexture_property_roughness/mode>`{.interpreted-text
role="ref"}

The color channel to consider as a roughness map in this texture. Only
effective if
`roughness/src_normal<class_ResourceImporterTexture_property_roughness/src_normal>`{.interpreted-text
role="ref"} is not empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_roughness/src_normal}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**roughness/src_normal** = `""`
`🔗<class_ResourceImporterTexture_property_roughness/src_normal>`{.interpreted-text
role="ref"}

The path to the texture to consider as a normal map for roughness
filtering on import. Specifying this can help decrease specular aliasing
slightly in 3D.

Roughness filtering on import is only used in 3D rendering, not 2D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterTexture_property_svg/scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **svg/scale** = `1.0`
`🔗<class_ResourceImporterTexture_property_svg/scale>`{.interpreted-text
role="ref"}

The scale the SVG should be rendered at, with `1.0` being the original
design size. Higher values result in a larger image. Note that unlike
font oversampling, this affects the size the SVG is rendered at in 2D.
See also
`editor/scale_with_editor_scale<class_ResourceImporterTexture_property_editor/scale_with_editor_scale>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only available for SVG images.
