github_url
:   hide

# Image {#class_Image}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Image datatype.

::: rst-class
classref-introduction-group
:::

## Description

Native image datatype. Contains image data which can be converted to an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"} and
provides commonly used *image processing* methods. The maximum width and
height for an **Image** are
`MAX_WIDTH<class_Image_constant_MAX_WIDTH>`{.interpreted-text
role="ref"} and
`MAX_HEIGHT<class_Image_constant_MAX_HEIGHT>`{.interpreted-text
role="ref"}.

An **Image** cannot be assigned to a texture property of an object
directly (such as
`Sprite2D.texture<class_Sprite2D_property_texture>`{.interpreted-text
role="ref"}), and has to be converted manually to an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"} first.

\*\*Note:\*\* The maximum image size is 16384×16384 pixels due to
graphics hardware limitations. Larger images may fail to import.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Importing images <../tutorials/assets_pipeline/importing_images>`{.interpreted-text
  role="doc"}
- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}

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

## Enumerations

:::: {#enum_Image_Format}
::: rst-class
classref-enumeration
:::
::::

enum **Format**: `🔗<enum_Image_Format>`{.interpreted-text role="ref"}

:::: {#class_Image_constant_FORMAT_L8}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_L8**
= `0`

Texture format with a single 8-bit depth representing luminance.

:::: {#class_Image_constant_FORMAT_LA8}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_LA8**
= `1`

OpenGL texture format with two values, luminance and alpha each stored
with 8 bits.

:::: {#class_Image_constant_FORMAT_R8}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_R8**
= `2`

OpenGL texture format `RED` with a single component and a bitdepth of 8.

:::: {#class_Image_constant_FORMAT_RG8}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_RG8**
= `3`

OpenGL texture format `RG` with two components and a bitdepth of 8 for
each.

:::: {#class_Image_constant_FORMAT_RGB8}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGB8** = `4`

OpenGL texture format `RGB` with three components, each with a bitdepth
of 8.

\*\*Note:\*\* When creating an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}, an
sRGB to linear color space conversion is performed.

:::: {#class_Image_constant_FORMAT_RGBA8}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGBA8** = `5`

OpenGL texture format `RGBA` with four components, each with a bitdepth
of 8.

\*\*Note:\*\* When creating an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}, an
sRGB to linear color space conversion is performed.

:::: {#class_Image_constant_FORMAT_RGBA4444}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGBA4444** = `6`

OpenGL texture format `RGBA` with four components, each with a bitdepth
of 4.

:::: {#class_Image_constant_FORMAT_RGB565}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGB565** = `7`

OpenGL texture format `RGB` with three components. Red and blue have a
bitdepth of 5, and green has a bitdepth of 6.

:::: {#class_Image_constant_FORMAT_RF}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_RF**
= `8`

OpenGL texture format `GL_R32F` where there\'s one component, a 32-bit
floating-point value.

:::: {#class_Image_constant_FORMAT_RGF}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_RGF**
= `9`

OpenGL texture format `GL_RG32F` where there are two components, each a
32-bit floating-point values.

:::: {#class_Image_constant_FORMAT_RGBF}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGBF** = `10`

OpenGL texture format `GL_RGB32F` where there are three components, each
a 32-bit floating-point values.

:::: {#class_Image_constant_FORMAT_RGBAF}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGBAF** = `11`

OpenGL texture format `GL_RGBA32F` where there are four components, each
a 32-bit floating-point values.

:::: {#class_Image_constant_FORMAT_RH}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_RH**
= `12`

OpenGL texture format `GL_R16F` where there\'s one component, a 16-bit
\"half-precision\" floating-point value.

:::: {#class_Image_constant_FORMAT_RGH}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_RGH**
= `13`

OpenGL texture format `GL_RG16F` where there are two components, each a
16-bit \"half-precision\" floating-point value.

:::: {#class_Image_constant_FORMAT_RGBH}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGBH** = `14`

OpenGL texture format `GL_RGB16F` where there are three components, each
a 16-bit \"half-precision\" floating-point value.

:::: {#class_Image_constant_FORMAT_RGBAH}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGBAH** = `15`

OpenGL texture format `GL_RGBA16F` where there are four components, each
a 16-bit \"half-precision\" floating-point value.

:::: {#class_Image_constant_FORMAT_RGBE9995}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGBE9995** = `16`

A special OpenGL texture format where the three color components have 9
bits of precision and all three share a single 5-bit exponent.

:::: {#class_Image_constant_FORMAT_DXT1}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_DXT1** = `17`

The [S3TC](https://en.wikipedia.org/wiki/S3_Texture_Compression) texture
format that uses Block Compression 1, and is the smallest variation of
S3TC, only providing 1 bit of alpha and color data being premultiplied
with alpha.

\*\*Note:\*\* When creating an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}, an
sRGB to linear color space conversion is performed.

:::: {#class_Image_constant_FORMAT_DXT3}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_DXT3** = `18`

The [S3TC](https://en.wikipedia.org/wiki/S3_Texture_Compression) texture
format that uses Block Compression 2, and color data is interpreted as
not having been premultiplied by alpha. Well suited for images with
sharp alpha transitions between translucent and opaque areas.

\*\*Note:\*\* When creating an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}, an
sRGB to linear color space conversion is performed.

:::: {#class_Image_constant_FORMAT_DXT5}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_DXT5** = `19`

The [S3TC](https://en.wikipedia.org/wiki/S3_Texture_Compression) texture
format also known as Block Compression 3 or BC3 that contains 64 bits of
alpha channel data followed by 64 bits of DXT1-encoded color data. Color
data is not premultiplied by alpha, same as DXT3. DXT5 generally
produces superior results for transparent gradients compared to DXT3.

\*\*Note:\*\* When creating an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}, an
sRGB to linear color space conversion is performed.

:::: {#class_Image_constant_FORMAT_RGTC_R}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGTC_R** = `20`

Texture format that uses [Red Green Texture
Compression](https://www.khronos.org/opengl/wiki/Red_Green_Texture_Compression),
normalizing the red channel data using the same compression algorithm
that DXT5 uses for the alpha channel.

:::: {#class_Image_constant_FORMAT_RGTC_RG}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_RGTC_RG** = `21`

Texture format that uses [Red Green Texture
Compression](https://www.khronos.org/opengl/wiki/Red_Green_Texture_Compression),
normalizing the red and green channel data using the same compression
algorithm that DXT5 uses for the alpha channel.

:::: {#class_Image_constant_FORMAT_BPTC_RGBA}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_BPTC_RGBA** = `22`

Texture format that uses
[BPTC](https://www.khronos.org/opengl/wiki/BPTC_Texture_Compression)
compression with unsigned normalized RGBA components.

\*\*Note:\*\* When creating an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}, an
sRGB to linear color space conversion is performed.

:::: {#class_Image_constant_FORMAT_BPTC_RGBF}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_BPTC_RGBF** = `23`

Texture format that uses
[BPTC](https://www.khronos.org/opengl/wiki/BPTC_Texture_Compression)
compression with signed floating-point RGB components.

:::: {#class_Image_constant_FORMAT_BPTC_RGBFU}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_BPTC_RGBFU** = `24`

Texture format that uses
[BPTC](https://www.khronos.org/opengl/wiki/BPTC_Texture_Compression)
compression with unsigned floating-point RGB components.

:::: {#class_Image_constant_FORMAT_ETC}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_ETC**
= `25`

[Ericsson Texture Compression format
1](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression#ETC1),
also referred to as \"ETC1\", and is part of the OpenGL ES graphics
standard. This format cannot store an alpha channel.

:::: {#class_Image_constant_FORMAT_ETC2_R11}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ETC2_R11** = `26`

[Ericsson Texture Compression format
2](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression#ETC2_and_EAC)
(`R11_EAC` variant), which provides one channel of unsigned data.

:::: {#class_Image_constant_FORMAT_ETC2_R11S}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ETC2_R11S** = `27`

[Ericsson Texture Compression format
2](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression#ETC2_and_EAC)
(`SIGNED_R11_EAC` variant), which provides one channel of signed data.

:::: {#class_Image_constant_FORMAT_ETC2_RG11}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ETC2_RG11** = `28`

[Ericsson Texture Compression format
2](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression#ETC2_and_EAC)
(`RG11_EAC` variant), which provides two channels of unsigned data.

:::: {#class_Image_constant_FORMAT_ETC2_RG11S}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ETC2_RG11S** = `29`

[Ericsson Texture Compression format
2](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression#ETC2_and_EAC)
(`SIGNED_RG11_EAC` variant), which provides two channels of signed data.

:::: {#class_Image_constant_FORMAT_ETC2_RGB8}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ETC2_RGB8** = `30`

[Ericsson Texture Compression format
2](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression#ETC2_and_EAC)
(`RGB8` variant), which is a follow-up of ETC1 and compresses RGB888
data.

\*\*Note:\*\* When creating an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}, an
sRGB to linear color space conversion is performed.

:::: {#class_Image_constant_FORMAT_ETC2_RGBA8}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ETC2_RGBA8** = `31`

[Ericsson Texture Compression format
2](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression#ETC2_and_EAC)
(`RGBA8`variant), which compresses RGBA8888 data with full alpha
support.

\*\*Note:\*\* When creating an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}, an
sRGB to linear color space conversion is performed.

:::: {#class_Image_constant_FORMAT_ETC2_RGB8A1}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ETC2_RGB8A1** = `32`

[Ericsson Texture Compression format
2](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression#ETC2_and_EAC)
(`RGB8_PUNCHTHROUGH_ALPHA1` variant), which compresses RGBA data to make
alpha either fully transparent or fully opaque.

\*\*Note:\*\* When creating an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}, an
sRGB to linear color space conversion is performed.

:::: {#class_Image_constant_FORMAT_ETC2_RA_AS_RG}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ETC2_RA_AS_RG** = `33`

[Ericsson Texture Compression format
2](https://en.wikipedia.org/wiki/Ericsson_Texture_Compression#ETC2_and_EAC)
(`RGBA8` variant), which compresses RA data and interprets it as two
channels (red and green). See also
`FORMAT_ETC2_RGBA8<class_Image_constant_FORMAT_ETC2_RGBA8>`{.interpreted-text
role="ref"}.

:::: {#class_Image_constant_FORMAT_DXT5_RA_AS_RG}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_DXT5_RA_AS_RG** = `34`

The [S3TC](https://en.wikipedia.org/wiki/S3_Texture_Compression) texture
format also known as Block Compression 3 or BC3, which compresses RA
data and interprets it as two channels (red and green). See also
`FORMAT_DXT5<class_Image_constant_FORMAT_DXT5>`{.interpreted-text
role="ref"}.

:::: {#class_Image_constant_FORMAT_ASTC_4x4}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ASTC_4x4** = `35`

[Adaptive Scalable Texture
Compression](https://en.wikipedia.org/wiki/Adaptive_scalable_texture_compression).
This implements the 4×4 (high quality) mode.

:::: {#class_Image_constant_FORMAT_ASTC_4x4_HDR}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ASTC_4x4_HDR** = `36`

Same format as
`FORMAT_ASTC_4x4<class_Image_constant_FORMAT_ASTC_4x4>`{.interpreted-text
role="ref"}, but with the hint to let the GPU know it is used for HDR.

:::: {#class_Image_constant_FORMAT_ASTC_8x8}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ASTC_8x8** = `37`

[Adaptive Scalable Texture
Compression](https://en.wikipedia.org/wiki/Adaptive_scalable_texture_compression).
This implements the 8×8 (low quality) mode.

:::: {#class_Image_constant_FORMAT_ASTC_8x8_HDR}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**FORMAT_ASTC_8x8_HDR** = `38`

Same format as
`FORMAT_ASTC_8x8<class_Image_constant_FORMAT_ASTC_8x8>`{.interpreted-text
role="ref"}, but with the hint to let the GPU know it is used for HDR.

:::: {#class_Image_constant_FORMAT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"} **FORMAT_MAX**
= `39`

Represents the size of the `Format<enum_Image_Format>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Image_Interpolation}
::: rst-class
classref-enumeration
:::
::::

enum **Interpolation**: `🔗<enum_Image_Interpolation>`{.interpreted-text
role="ref"}

:::: {#class_Image_constant_INTERPOLATE_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`Interpolation<enum_Image_Interpolation>`{.interpreted-text role="ref"}
**INTERPOLATE_NEAREST** = `0`

Performs nearest-neighbor interpolation. If the image is resized, it
will be pixelated.

:::: {#class_Image_constant_INTERPOLATE_BILINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Interpolation<enum_Image_Interpolation>`{.interpreted-text role="ref"}
**INTERPOLATE_BILINEAR** = `1`

Performs bilinear interpolation. If the image is resized, it will be
blurry. This mode is faster than
`INTERPOLATE_CUBIC<class_Image_constant_INTERPOLATE_CUBIC>`{.interpreted-text
role="ref"}, but it results in lower quality.

:::: {#class_Image_constant_INTERPOLATE_CUBIC}
::: rst-class
classref-enumeration-constant
:::
::::

`Interpolation<enum_Image_Interpolation>`{.interpreted-text role="ref"}
**INTERPOLATE_CUBIC** = `2`

Performs cubic interpolation. If the image is resized, it will be
blurry. This mode often gives better results compared to
`INTERPOLATE_BILINEAR<class_Image_constant_INTERPOLATE_BILINEAR>`{.interpreted-text
role="ref"}, at the cost of being slower.

:::: {#class_Image_constant_INTERPOLATE_TRILINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Interpolation<enum_Image_Interpolation>`{.interpreted-text role="ref"}
**INTERPOLATE_TRILINEAR** = `3`

Performs bilinear separately on the two most-suited mipmap levels, then
linearly interpolates between them.

It\'s slower than
`INTERPOLATE_BILINEAR<class_Image_constant_INTERPOLATE_BILINEAR>`{.interpreted-text
role="ref"}, but produces higher-quality results with far fewer aliasing
artifacts.

If the image does not have mipmaps, they will be generated and used
internally, but no mipmaps will be generated on the resulting image.

\*\*Note:\*\* If you intend to scale multiple copies of the original
image, it\'s better to call
`generate_mipmaps()<class_Image_method_generate_mipmaps>`{.interpreted-text
role="ref"}\] on it in advance, to avoid wasting processing power in
generating them again and again.

On the other hand, if the image already has mipmaps, they will be used,
and a new set will be generated for the resulting image.

:::: {#class_Image_constant_INTERPOLATE_LANCZOS}
::: rst-class
classref-enumeration-constant
:::
::::

`Interpolation<enum_Image_Interpolation>`{.interpreted-text role="ref"}
**INTERPOLATE_LANCZOS** = `4`

Performs Lanczos interpolation. This is the slowest image resizing mode,
but it typically gives the best results, especially when downscaling
images.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Image_AlphaMode}
::: rst-class
classref-enumeration
:::
::::

enum **AlphaMode**: `🔗<enum_Image_AlphaMode>`{.interpreted-text
role="ref"}

:::: {#class_Image_constant_ALPHA_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaMode<enum_Image_AlphaMode>`{.interpreted-text role="ref"}
**ALPHA_NONE** = `0`

Image does not have alpha.

:::: {#class_Image_constant_ALPHA_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaMode<enum_Image_AlphaMode>`{.interpreted-text role="ref"}
**ALPHA_BIT** = `1`

Image stores alpha in a single bit.

:::: {#class_Image_constant_ALPHA_BLEND}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaMode<enum_Image_AlphaMode>`{.interpreted-text role="ref"}
**ALPHA_BLEND** = `2`

Image uses alpha.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Image_CompressMode}
::: rst-class
classref-enumeration
:::
::::

enum **CompressMode**: `🔗<enum_Image_CompressMode>`{.interpreted-text
role="ref"}

:::: {#class_Image_constant_COMPRESS_S3TC}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressMode<enum_Image_CompressMode>`{.interpreted-text role="ref"}
**COMPRESS_S3TC** = `0`

Use S3TC compression.

:::: {#class_Image_constant_COMPRESS_ETC}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressMode<enum_Image_CompressMode>`{.interpreted-text role="ref"}
**COMPRESS_ETC** = `1`

Use ETC compression.

:::: {#class_Image_constant_COMPRESS_ETC2}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressMode<enum_Image_CompressMode>`{.interpreted-text role="ref"}
**COMPRESS_ETC2** = `2`

Use ETC2 compression.

:::: {#class_Image_constant_COMPRESS_BPTC}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressMode<enum_Image_CompressMode>`{.interpreted-text role="ref"}
**COMPRESS_BPTC** = `3`

Use BPTC compression.

:::: {#class_Image_constant_COMPRESS_ASTC}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressMode<enum_Image_CompressMode>`{.interpreted-text role="ref"}
**COMPRESS_ASTC** = `4`

Use ASTC compression.

:::: {#class_Image_constant_COMPRESS_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressMode<enum_Image_CompressMode>`{.interpreted-text role="ref"}
**COMPRESS_MAX** = `5`

Represents the size of the
`CompressMode<enum_Image_CompressMode>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Image_UsedChannels}
::: rst-class
classref-enumeration
:::
::::

enum **UsedChannels**: `🔗<enum_Image_UsedChannels>`{.interpreted-text
role="ref"}

:::: {#class_Image_constant_USED_CHANNELS_L}
::: rst-class
classref-enumeration-constant
:::
::::

`UsedChannels<enum_Image_UsedChannels>`{.interpreted-text role="ref"}
**USED_CHANNELS_L** = `0`

The image only uses one channel for luminance (grayscale).

:::: {#class_Image_constant_USED_CHANNELS_LA}
::: rst-class
classref-enumeration-constant
:::
::::

`UsedChannels<enum_Image_UsedChannels>`{.interpreted-text role="ref"}
**USED_CHANNELS_LA** = `1`

The image uses two channels for luminance and alpha, respectively.

:::: {#class_Image_constant_USED_CHANNELS_R}
::: rst-class
classref-enumeration-constant
:::
::::

`UsedChannels<enum_Image_UsedChannels>`{.interpreted-text role="ref"}
**USED_CHANNELS_R** = `2`

The image only uses the red channel.

:::: {#class_Image_constant_USED_CHANNELS_RG}
::: rst-class
classref-enumeration-constant
:::
::::

`UsedChannels<enum_Image_UsedChannels>`{.interpreted-text role="ref"}
**USED_CHANNELS_RG** = `3`

The image uses two channels for red and green.

:::: {#class_Image_constant_USED_CHANNELS_RGB}
::: rst-class
classref-enumeration-constant
:::
::::

`UsedChannels<enum_Image_UsedChannels>`{.interpreted-text role="ref"}
**USED_CHANNELS_RGB** = `4`

The image uses three channels for red, green, and blue.

:::: {#class_Image_constant_USED_CHANNELS_RGBA}
::: rst-class
classref-enumeration-constant
:::
::::

`UsedChannels<enum_Image_UsedChannels>`{.interpreted-text role="ref"}
**USED_CHANNELS_RGBA** = `5`

The image uses four channels for red, green, blue, and alpha.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Image_CompressSource}
::: rst-class
classref-enumeration
:::
::::

enum **CompressSource**:
`🔗<enum_Image_CompressSource>`{.interpreted-text role="ref"}

:::: {#class_Image_constant_COMPRESS_SOURCE_GENERIC}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressSource<enum_Image_CompressSource>`{.interpreted-text
role="ref"} **COMPRESS_SOURCE_GENERIC** = `0`

Source texture (before compression) is a regular texture. Default for
all textures.

:::: {#class_Image_constant_COMPRESS_SOURCE_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressSource<enum_Image_CompressSource>`{.interpreted-text
role="ref"} **COMPRESS_SOURCE_SRGB** = `1`

Source texture (before compression) is in sRGB space.

:::: {#class_Image_constant_COMPRESS_SOURCE_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CompressSource<enum_Image_CompressSource>`{.interpreted-text
role="ref"} **COMPRESS_SOURCE_NORMAL** = `2`

Source texture (before compression) is a normal texture (e.g. it can be
compressed into two channels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Image_ASTCFormat}
::: rst-class
classref-enumeration
:::
::::

enum **ASTCFormat**: `🔗<enum_Image_ASTCFormat>`{.interpreted-text
role="ref"}

:::: {#class_Image_constant_ASTC_FORMAT_4x4}
::: rst-class
classref-enumeration-constant
:::
::::

`ASTCFormat<enum_Image_ASTCFormat>`{.interpreted-text role="ref"}
**ASTC_FORMAT_4x4** = `0`

Hint to indicate that the high quality 4×4 ASTC compression format
should be used.

:::: {#class_Image_constant_ASTC_FORMAT_8x8}
::: rst-class
classref-enumeration-constant
:::
::::

`ASTCFormat<enum_Image_ASTCFormat>`{.interpreted-text role="ref"}
**ASTC_FORMAT_8x8** = `1`

Hint to indicate that the low quality 8×8 ASTC compression format should
be used.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Image_constant_MAX_WIDTH}
::: rst-class
classref-constant
:::
::::

**MAX_WIDTH** = `16777216`
`🔗<class_Image_constant_MAX_WIDTH>`{.interpreted-text role="ref"}

The maximal width allowed for **Image** resources.

:::: {#class_Image_constant_MAX_HEIGHT}
::: rst-class
classref-constant
:::
::::

**MAX_HEIGHT** = `16777216`
`🔗<class_Image_constant_MAX_HEIGHT>`{.interpreted-text role="ref"}

The maximal height allowed for **Image** resources.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Image_property_data}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} **data** =
`{ "data": PackedByteArray(), "format": "Lum8", "height": 0, "mipmaps": false, "width": 0 }`
`🔗<class_Image_property_data>`{.interpreted-text role="ref"}

Holds all the image\'s color data in a given format. See
`Format<enum_Image_Format>`{.interpreted-text role="ref"} constants.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Image_method_adjust_bcs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**adjust_bcs**(brightness: `float<class_float>`{.interpreted-text
role="ref"}, contrast: `float<class_float>`{.interpreted-text
role="ref"}, saturation: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Image_method_adjust_bcs>`{.interpreted-text
role="ref"}

Adjusts this image\'s `brightness`, `contrast`, and `saturation` by the
given values. Does not work if the image is compressed (see
`is_compressed()<class_Image_method_is_compressed>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_blend_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**blend_rect**(src: `Image<class_Image>`{.interpreted-text role="ref"},
src_rect: `Rect2i<class_Rect2i>`{.interpreted-text role="ref"}, dst:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_Image_method_blend_rect>`{.interpreted-text role="ref"}

Alpha-blends `src_rect` from `src` image to this image at coordinates
`dst`, clipped accordingly to both image bounds. This image and `src`
image **must** have the same format. `src_rect` with non-positive size
is treated as empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_blend_rect_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**blend_rect_mask**(src: `Image<class_Image>`{.interpreted-text
role="ref"}, mask: `Image<class_Image>`{.interpreted-text role="ref"},
src_rect: `Rect2i<class_Rect2i>`{.interpreted-text role="ref"}, dst:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_Image_method_blend_rect_mask>`{.interpreted-text role="ref"}

Alpha-blends `src_rect` from `src` image to this image using `mask`
image at coordinates `dst`, clipped accordingly to both image bounds.
Alpha channels are required for both `src` and `mask`. `dst` pixels and
`src` pixels will blend if the corresponding mask pixel\'s alpha value
is not 0. This image and `src` image **must** have the same format.
`src` image and `mask` image **must** have the same size (width and
height) but they can have different formats. `src_rect` with
non-positive size is treated as empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_blit_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**blit_rect**(src: `Image<class_Image>`{.interpreted-text role="ref"},
src_rect: `Rect2i<class_Rect2i>`{.interpreted-text role="ref"}, dst:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_Image_method_blit_rect>`{.interpreted-text role="ref"}

Copies `src_rect` from `src` image to this image at coordinates `dst`,
clipped accordingly to both image bounds. This image and `src` image
**must** have the same format. `src_rect` with non-positive size is
treated as empty.

\*\*Note:\*\* The alpha channel data in `src` will overwrite the
corresponding data in this image at the target position. To blend alpha
channels, use
`blend_rect()<class_Image_method_blend_rect>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_blit_rect_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**blit_rect_mask**(src: `Image<class_Image>`{.interpreted-text
role="ref"}, mask: `Image<class_Image>`{.interpreted-text role="ref"},
src_rect: `Rect2i<class_Rect2i>`{.interpreted-text role="ref"}, dst:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_Image_method_blit_rect_mask>`{.interpreted-text role="ref"}

Blits `src_rect` area from `src` image to this image at the coordinates
given by `dst`, clipped accordingly to both image bounds. `src` pixel is
copied onto `dst` if the corresponding `mask` pixel\'s alpha value is
not 0. This image and `src` image **must** have the same format. `src`
image and `mask` image **must** have the same size (width and height)
but they can have different formats. `src_rect` with non-positive size
is treated as empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_bump_map_to_normal_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bump_map_to_normal_map**(bump_scale:
`float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_Image_method_bump_map_to_normal_map>`{.interpreted-text
role="ref"}

Converts a bump map to a normal map. A bump map provides a height offset
per-pixel, while a normal map provides a normal direction per pixel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_clear_mipmaps}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_mipmaps**()
`🔗<class_Image_method_clear_mipmaps>`{.interpreted-text role="ref"}

Removes the image\'s mipmaps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_compress}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**compress**(mode:
`CompressMode<enum_Image_CompressMode>`{.interpreted-text role="ref"},
source: `CompressSource<enum_Image_CompressSource>`{.interpreted-text
role="ref"} = 0, astc_format:
`ASTCFormat<enum_Image_ASTCFormat>`{.interpreted-text role="ref"} = 0)
`🔗<class_Image_method_compress>`{.interpreted-text role="ref"}

Compresses the image to use less memory. Can not directly access pixel
data while the image is compressed. Returns error if the chosen
compression mode is not available.

The `source` parameter helps to pick the best compression method for DXT
and ETC2 formats. It is ignored for ASTC compression.

For ASTC compression, the `astc_format` parameter must be supplied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_compress_from_channels}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**compress_from_channels**(mode:
`CompressMode<enum_Image_CompressMode>`{.interpreted-text role="ref"},
channels: `UsedChannels<enum_Image_UsedChannels>`{.interpreted-text
role="ref"}, astc_format:
`ASTCFormat<enum_Image_ASTCFormat>`{.interpreted-text role="ref"} = 0)
`🔗<class_Image_method_compress_from_channels>`{.interpreted-text
role="ref"}

Compresses the image to use less memory. Can not directly access pixel
data while the image is compressed. Returns error if the chosen
compression mode is not available.

This is an alternative to
`compress()<class_Image_method_compress>`{.interpreted-text role="ref"}
that lets the user supply the channels used in order for the compressor
to pick the best DXT and ETC2 formats. For other formats (non DXT or
ETC2), this argument is ignored.

For ASTC compression, the `astc_format` parameter must be supplied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_compute_image_metrics}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**compute_image_metrics**(compared_image:
`Image<class_Image>`{.interpreted-text role="ref"}, use_luma:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Image_method_compute_image_metrics>`{.interpreted-text
role="ref"}

Compute image metrics on the current image and the compared image.

The dictionary contains `max`, `mean`, `mean_squared`,
`root_mean_squared` and `peak_snr`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_convert}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**convert**(format: `Format<enum_Image_Format>`{.interpreted-text
role="ref"}) `🔗<class_Image_method_convert>`{.interpreted-text
role="ref"}

Converts this image\'s format to the given `format`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_copy_from}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**copy_from**(src: `Image<class_Image>`{.interpreted-text role="ref"})
`🔗<class_Image_method_copy_from>`{.interpreted-text role="ref"}

Copies `src` image to this image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_create}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"} **create**(width:
`int<class_int>`{.interpreted-text role="ref"}, height:
`int<class_int>`{.interpreted-text role="ref"}, use_mipmaps:
`bool<class_bool>`{.interpreted-text role="ref"}, format:
`Format<enum_Image_Format>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_create>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`create_empty()<class_Image_method_create_empty>`{.interpreted-text
role="ref"}.

Creates an empty image of the given size and format. If `use_mipmaps` is
`true`, generates mipmaps for this image. See the
`generate_mipmaps()<class_Image_method_generate_mipmaps>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_create_empty}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**create_empty**(width: `int<class_int>`{.interpreted-text role="ref"},
height: `int<class_int>`{.interpreted-text role="ref"}, use_mipmaps:
`bool<class_bool>`{.interpreted-text role="ref"}, format:
`Format<enum_Image_Format>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_create_empty>`{.interpreted-text
role="ref"}

Creates an empty image of the given size and format. If `use_mipmaps` is
`true`, generates mipmaps for this image. See the
`generate_mipmaps()<class_Image_method_generate_mipmaps>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_create_from_data}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**create_from_data**(width: `int<class_int>`{.interpreted-text
role="ref"}, height: `int<class_int>`{.interpreted-text role="ref"},
use_mipmaps: `bool<class_bool>`{.interpreted-text role="ref"}, format:
`Format<enum_Image_Format>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_create_from_data>`{.interpreted-text
role="ref"}

Creates a new image of the given size and format. Fills the image with
the given raw data. If `use_mipmaps` is `true`, loads the mipmaps for
this image from `data`. See
`generate_mipmaps()<class_Image_method_generate_mipmaps>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_crop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **crop**(width:
`int<class_int>`{.interpreted-text role="ref"}, height:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Image_method_crop>`{.interpreted-text role="ref"}

Crops the image to the given `width` and `height`. If the specified size
is larger than the current size, the extra area is filled with black
pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_decompress}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**decompress**() `🔗<class_Image_method_decompress>`{.interpreted-text
role="ref"}

Decompresses the image if it is VRAM compressed in a supported format.
Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if the format is supported, otherwise
`@GlobalScope.ERR_UNAVAILABLE<class_@GlobalScope_constant_ERR_UNAVAILABLE>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The following formats can be decompressed: DXT, RGTC,
BPTC. The formats ETC1 and ETC2 are not supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_detect_alpha}
::: rst-class
classref-method
:::
::::

`AlphaMode<enum_Image_AlphaMode>`{.interpreted-text role="ref"}
**detect_alpha**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_detect_alpha>`{.interpreted-text
role="ref"}

Returns
`ALPHA_BLEND<class_Image_constant_ALPHA_BLEND>`{.interpreted-text
role="ref"} if the image has data for alpha values. Returns
`ALPHA_BIT<class_Image_constant_ALPHA_BIT>`{.interpreted-text
role="ref"} if all the alpha values are stored in a single bit. Returns
`ALPHA_NONE<class_Image_constant_ALPHA_NONE>`{.interpreted-text
role="ref"} if no data for alpha values is found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_detect_used_channels}
::: rst-class
classref-method
:::
::::

`UsedChannels<enum_Image_UsedChannels>`{.interpreted-text role="ref"}
**detect_used_channels**(source:
`CompressSource<enum_Image_CompressSource>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Image_method_detect_used_channels>`{.interpreted-text
role="ref"}

Returns the color channels used by this image. If the image is
compressed, the original `source` must be specified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_fill}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **fill**(color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Image_method_fill>`{.interpreted-text role="ref"}

Fills the image with `color`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_fill_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fill_rect**(rect: `Rect2i<class_Rect2i>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Image_method_fill_rect>`{.interpreted-text role="ref"}

Fills `rect` with `color`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_fix_alpha_edges}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fix_alpha_edges**()
`🔗<class_Image_method_fix_alpha_edges>`{.interpreted-text role="ref"}

Blends low-alpha pixels with nearby pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_flip_x}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **flip_x**()
`🔗<class_Image_method_flip_x>`{.interpreted-text role="ref"}

Flips the image horizontally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_flip_y}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **flip_y**()
`🔗<class_Image_method_flip_y>`{.interpreted-text role="ref"}

Flips the image vertically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_generate_mipmaps}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**generate_mipmaps**(renormalize: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_Image_method_generate_mipmaps>`{.interpreted-text role="ref"}

Generates mipmaps for the image. Mipmaps are precalculated
lower-resolution copies of the image that are automatically used if the
image needs to be scaled down when rendered. They help improve image
quality and performance when rendering. This method returns an error if
the image is compressed, in a custom format, or if the image\'s
width/height is `0`. Enabling `renormalize` when generating mipmaps for
normal map textures will make sure all resulting vector values are
normalized.

It is possible to check if the image has mipmaps by calling
`has_mipmaps()<class_Image_method_has_mipmaps>`{.interpreted-text
role="ref"} or
`get_mipmap_count()<class_Image_method_get_mipmap_count>`{.interpreted-text
role="ref"}. Calling
`generate_mipmaps()<class_Image_method_generate_mipmaps>`{.interpreted-text
role="ref"} on an image that already has mipmaps will replace existing
mipmaps in the image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_data}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_data**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_data>`{.interpreted-text
role="ref"}

Returns a copy of the image\'s raw data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_data_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_data_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_data_size>`{.interpreted-text
role="ref"}

Returns size (in bytes) of the image\'s raw data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_format}
::: rst-class
classref-method
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**get_format**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_format>`{.interpreted-text
role="ref"}

Returns this image\'s format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_height>`{.interpreted-text
role="ref"}

Returns the image\'s height.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_mipmap_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_mipmap_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_mipmap_count>`{.interpreted-text
role="ref"}

Returns the number of mipmap levels or 0 if the image has no mipmaps.
The largest main level image is not counted as a mipmap level by this
method, so if you want to include it you can add 1 to this count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_mipmap_offset}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_mipmap_offset**(mipmap: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Image_method_get_mipmap_offset>`{.interpreted-text role="ref"}

Returns the offset where the image\'s mipmap with index `mipmap` is
stored in the `data<class_Image_property_data>`{.interpreted-text
role="ref"} dictionary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_pixel}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **get_pixel**(x:
`int<class_int>`{.interpreted-text role="ref"}, y:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_pixel>`{.interpreted-text
role="ref"}

Returns the color of the pixel at `(x, y)`.

This is the same as
`get_pixelv()<class_Image_method_get_pixelv>`{.interpreted-text
role="ref"}, but with two integer arguments instead of a
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} argument.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_pixelv}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **get_pixelv**(point:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_pixelv>`{.interpreted-text
role="ref"}

Returns the color of the pixel at `point`.

This is the same as
`get_pixel()<class_Image_method_get_pixel>`{.interpreted-text
role="ref"}, but with a `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"} argument instead of two integer arguments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_region}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**get_region**(region: `Rect2i<class_Rect2i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_region>`{.interpreted-text
role="ref"}

Returns a new **Image** that is a copy of this **Image**\'s area
specified with `region`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_size}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **get_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_size>`{.interpreted-text
role="ref"}

Returns the image\'s size (width and height).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_used_rect}
::: rst-class
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **get_used_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_used_rect>`{.interpreted-text
role="ref"}

Returns a `Rect2i<class_Rect2i>`{.interpreted-text role="ref"} enclosing
the visible portion of the image, considering each pixel with a non-zero
alpha channel as visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_get_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_width**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_get_width>`{.interpreted-text
role="ref"}

Returns the image\'s width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_has_mipmaps}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_mipmaps**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_has_mipmaps>`{.interpreted-text
role="ref"}

Returns `true` if the image has generated mipmaps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_is_compressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_compressed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_is_compressed>`{.interpreted-text
role="ref"}

Returns `true` if the image is compressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the image has no data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_is_invisible}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_invisible**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_is_invisible>`{.interpreted-text
role="ref"}

Returns `true` if all the image\'s pixels have an alpha value of 0.
Returns `false` if any pixel has an alpha value higher than 0.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_linear_to_srgb}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**linear_to_srgb**()
`🔗<class_Image_method_linear_to_srgb>`{.interpreted-text role="ref"}

Converts the entire image from the linear colorspace to the sRGB
colorspace. Only works on images with
`FORMAT_RGB8<class_Image_constant_FORMAT_RGB8>`{.interpreted-text
role="ref"} or
`FORMAT_RGBA8<class_Image_constant_FORMAT_RGBA8>`{.interpreted-text
role="ref"} formats.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_Image_method_load>`{.interpreted-text role="ref"}

Loads an image from file `path`. See [Supported image
formats](../tutorials/assets_pipeline/importing_images.html#supported-image-formats)
for a list of supported image formats and limitations.

\*\*Warning:\*\* This method should only be used in the editor or in
cases when you need to load external images at run-time, such as images
located at the `user://` directory, and may not work in exported
projects.

See also `ImageTexture<class_ImageTexture>`{.interpreted-text
role="ref"} description for usage examples.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_bmp_from_buffer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_bmp_from_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Image_method_load_bmp_from_buffer>`{.interpreted-text
role="ref"}

Loads an image from the binary contents of a BMP file.

\*\*Note:\*\* Godot\'s BMP module doesn\'t support 16-bit per pixel
images. Only 1-bit, 4-bit, 8-bit, 24-bit, and 32-bit per pixel images
are supported.

\*\*Note:\*\* This method is only available in engine builds with the
BMP module enabled. By default, the BMP module is enabled, but it can be
disabled at build-time using the `module_bmp_enabled=no` SCons option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_dds_from_buffer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_dds_from_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Image_method_load_dds_from_buffer>`{.interpreted-text
role="ref"}

Loads an image from the binary contents of a DDS file.

\*\*Note:\*\* This method is only available in engine builds with the
DDS module enabled. By default, the DDS module is enabled, but it can be
disabled at build-time using the `module_dds_enabled=no` SCons option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_from_file}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**load_from_file**(path: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_load_from_file>`{.interpreted-text
role="ref"}

Creates a new **Image** and loads data from the specified file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_jpg_from_buffer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_jpg_from_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Image_method_load_jpg_from_buffer>`{.interpreted-text
role="ref"}

Loads an image from the binary contents of a JPEG file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_ktx_from_buffer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_ktx_from_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Image_method_load_ktx_from_buffer>`{.interpreted-text
role="ref"}

Loads an image from the binary contents of a
[KTX](https://github.com/KhronosGroup/KTX-Software) file. Unlike most
image formats, KTX can store VRAM-compressed data and embed mipmaps.

\*\*Note:\*\* Godot\'s libktx implementation only supports 2D images.
Cubemaps, texture arrays, and de-padding are not supported.

\*\*Note:\*\* This method is only available in engine builds with the
KTX module enabled. By default, the KTX module is enabled, but it can be
disabled at build-time using the `module_ktx_enabled=no` SCons option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_png_from_buffer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_png_from_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Image_method_load_png_from_buffer>`{.interpreted-text
role="ref"}

Loads an image from the binary contents of a PNG file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_svg_from_buffer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_svg_from_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
scale: `float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_Image_method_load_svg_from_buffer>`{.interpreted-text
role="ref"}

Loads an image from the UTF-8 binary contents of an **uncompressed** SVG
file (**.svg**).

\*\*Note:\*\* Beware when using compressed SVG files (like **.svgz**),
they need to be `decompressed` before loading.

\*\*Note:\*\* This method is only available in engine builds with the
SVG module enabled. By default, the SVG module is enabled, but it can be
disabled at build-time using the `module_svg_enabled=no` SCons option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_svg_from_string}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_svg_from_string**(svg_str:
`String<class_String>`{.interpreted-text role="ref"}, scale:
`float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_Image_method_load_svg_from_string>`{.interpreted-text
role="ref"}

Loads an image from the string contents of an SVG file (**.svg**).

\*\*Note:\*\* This method is only available in engine builds with the
SVG module enabled. By default, the SVG module is enabled, but it can be
disabled at build-time using the `module_svg_enabled=no` SCons option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_tga_from_buffer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_tga_from_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Image_method_load_tga_from_buffer>`{.interpreted-text
role="ref"}

Loads an image from the binary contents of a TGA file.

\*\*Note:\*\* This method is only available in engine builds with the
TGA module enabled. By default, the TGA module is enabled, but it can be
disabled at build-time using the `module_tga_enabled=no` SCons option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_load_webp_from_buffer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_webp_from_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Image_method_load_webp_from_buffer>`{.interpreted-text
role="ref"}

Loads an image from the binary contents of a WebP file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_normal_map_to_xy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**normal_map_to_xy**()
`🔗<class_Image_method_normal_map_to_xy>`{.interpreted-text role="ref"}

Converts the image\'s data to represent coordinates on a 3D plane. This
is used when the image represents a normal map. A normal map can add
lots of detail to a 3D surface without increasing the polygon count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_premultiply_alpha}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**premultiply_alpha**()
`🔗<class_Image_method_premultiply_alpha>`{.interpreted-text role="ref"}

Multiplies color values with alpha values. Resulting color values for a
pixel are `(color * alpha)/256`. See also
`CanvasItemMaterial.blend_mode<class_CanvasItemMaterial_property_blend_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_resize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**resize**(width: `int<class_int>`{.interpreted-text role="ref"},
height: `int<class_int>`{.interpreted-text role="ref"}, interpolation:
`Interpolation<enum_Image_Interpolation>`{.interpreted-text role="ref"}
= 1) `🔗<class_Image_method_resize>`{.interpreted-text role="ref"}

Resizes the image to the given `width` and `height`. New pixels are
calculated using the `interpolation` mode defined via
`Interpolation<enum_Image_Interpolation>`{.interpreted-text role="ref"}
constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_resize_to_po2}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**resize_to_po2**(square: `bool<class_bool>`{.interpreted-text
role="ref"} = false, interpolation:
`Interpolation<enum_Image_Interpolation>`{.interpreted-text role="ref"}
= 1) `🔗<class_Image_method_resize_to_po2>`{.interpreted-text
role="ref"}

Resizes the image to the nearest power of 2 for the width and height. If
`square` is `true`, sets width and height to be the same. New pixels are
calculated using the `interpolation` mode defined via
`Interpolation<enum_Image_Interpolation>`{.interpreted-text role="ref"}
constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_rgbe_to_srgb}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"} **rgbe_to_srgb**()
`🔗<class_Image_method_rgbe_to_srgb>`{.interpreted-text role="ref"}

Converts a standard RGBE (Red Green Blue Exponent) image to an sRGB
image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_rotate_90}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_90**(direction:
`ClockDirection<enum_@GlobalScope_ClockDirection>`{.interpreted-text
role="ref"}) `🔗<class_Image_method_rotate_90>`{.interpreted-text
role="ref"}

Rotates the image in the specified `direction` by `90` degrees. The
width and height of the image must be greater than `1`. If the width and
height are not equal, the image will be resized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_rotate_180}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rotate_180**() `🔗<class_Image_method_rotate_180>`{.interpreted-text
role="ref"}

Rotates the image by `180` degrees. The width and height of the image
must be greater than `1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_dds}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_dds**(path: `String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_save_dds>`{.interpreted-text
role="ref"}

Saves the image as a DDS (DirectDraw Surface) file to `path`. DDS is a
container format that can store textures in various compression formats,
such as DXT1, DXT5, or BC7. This function will return
`@GlobalScope.ERR_UNAVAILABLE<class_@GlobalScope_constant_ERR_UNAVAILABLE>`{.interpreted-text
role="ref"} if Godot was compiled without the DDS module.

\*\*Note:\*\* The DDS module may be disabled in certain builds, which
means `save_dds()<class_Image_method_save_dds>`{.interpreted-text
role="ref"} will return
`@GlobalScope.ERR_UNAVAILABLE<class_@GlobalScope_constant_ERR_UNAVAILABLE>`{.interpreted-text
role="ref"} when it is called from an exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_dds_to_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**save_dds_to_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Image_method_save_dds_to_buffer>`{.interpreted-text
role="ref"}

Saves the image as a DDS (DirectDraw Surface) file to a byte array. DDS
is a container format that can store textures in various compression
formats, such as DXT1, DXT5, or BC7. This function will return an empty
byte array if Godot was compiled without the DDS module.

\*\*Note:\*\* The DDS module may be disabled in certain builds, which
means
`save_dds_to_buffer()<class_Image_method_save_dds_to_buffer>`{.interpreted-text
role="ref"} will return an empty byte array when it is called from an
exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_exr}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_exr**(path: `String<class_String>`{.interpreted-text role="ref"},
grayscale: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_save_exr>`{.interpreted-text
role="ref"}

Saves the image as an EXR file to `path`. If `grayscale` is `true` and
the image has only one channel, it will be saved explicitly as
monochrome rather than one red channel. This function will return
`@GlobalScope.ERR_UNAVAILABLE<class_@GlobalScope_constant_ERR_UNAVAILABLE>`{.interpreted-text
role="ref"} if Godot was compiled without the TinyEXR module.

\*\*Note:\*\* The TinyEXR module is disabled in non-editor builds, which
means `save_exr()<class_Image_method_save_exr>`{.interpreted-text
role="ref"} will return
`@GlobalScope.ERR_UNAVAILABLE<class_@GlobalScope_constant_ERR_UNAVAILABLE>`{.interpreted-text
role="ref"} when it is called from an exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_exr_to_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**save_exr_to_buffer**(grayscale: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Image_method_save_exr_to_buffer>`{.interpreted-text
role="ref"}

Saves the image as an EXR file to a byte array. If `grayscale` is `true`
and the image has only one channel, it will be saved explicitly as
monochrome rather than one red channel. This function will return an
empty byte array if Godot was compiled without the TinyEXR module.

\*\*Note:\*\* The TinyEXR module is disabled in non-editor builds, which
means
`save_exr_to_buffer()<class_Image_method_save_exr_to_buffer>`{.interpreted-text
role="ref"} will return an empty byte array when it is called from an
exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_jpg}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_jpg**(path: `String<class_String>`{.interpreted-text role="ref"},
quality: `float<class_float>`{.interpreted-text role="ref"} = 0.75)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_save_jpg>`{.interpreted-text
role="ref"}

Saves the image as a JPEG file to `path` with the specified `quality`
between `0.01` and `1.0` (inclusive). Higher `quality` values result in
better-looking output at the cost of larger file sizes. Recommended
`quality` values are between `0.75` and `0.90`. Even at quality `1.00`,
JPEG compression remains lossy.

\*\*Note:\*\* JPEG does not save an alpha channel. If the **Image**
contains an alpha channel, the image will still be saved, but the
resulting JPEG file won\'t contain the alpha channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_jpg_to_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**save_jpg_to_buffer**(quality: `float<class_float>`{.interpreted-text
role="ref"} = 0.75)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Image_method_save_jpg_to_buffer>`{.interpreted-text
role="ref"}

Saves the image as a JPEG file to a byte array with the specified
`quality` between `0.01` and `1.0` (inclusive). Higher `quality` values
result in better-looking output at the cost of larger byte array sizes
(and therefore memory usage). Recommended `quality` values are between
`0.75` and `0.90`. Even at quality `1.00`, JPEG compression remains
lossy.

\*\*Note:\*\* JPEG does not save an alpha channel. If the **Image**
contains an alpha channel, the image will still be saved, but the
resulting byte array won\'t contain the alpha channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_png}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_png**(path: `String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_save_png>`{.interpreted-text
role="ref"}

Saves the image as a PNG file to the file at `path`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_png_to_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**save_png_to_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Image_method_save_png_to_buffer>`{.interpreted-text
role="ref"}

Saves the image as a PNG file to a byte array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_webp}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_webp**(path: `String<class_String>`{.interpreted-text
role="ref"}, lossy: `bool<class_bool>`{.interpreted-text role="ref"} =
false, quality: `float<class_float>`{.interpreted-text role="ref"} =
0.75)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Image_method_save_webp>`{.interpreted-text
role="ref"}

Saves the image as a WebP (Web Picture) file to the file at `path`. By
default it will save lossless. If `lossy` is `true`, the image will be
saved lossy, using the `quality` setting between `0.0` and `1.0`
(inclusive). Lossless WebP offers more efficient compression than PNG.

\*\*Note:\*\* The WebP format is limited to a size of 16383×16383
pixels, while PNG can save larger images.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_save_webp_to_buffer}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**save_webp_to_buffer**(lossy: `bool<class_bool>`{.interpreted-text
role="ref"} = false, quality: `float<class_float>`{.interpreted-text
role="ref"} = 0.75)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Image_method_save_webp_to_buffer>`{.interpreted-text
role="ref"}

Saves the image as a WebP (Web Picture) file to a byte array. By default
it will save lossless. If `lossy` is `true`, the image will be saved
lossy, using the `quality` setting between `0.0` and `1.0` (inclusive).
Lossless WebP offers more efficient compression than PNG.

\*\*Note:\*\* The WebP format is limited to a size of 16383×16383
pixels, while PNG can save larger images.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_set_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_data**(width: `int<class_int>`{.interpreted-text role="ref"},
height: `int<class_int>`{.interpreted-text role="ref"}, use_mipmaps:
`bool<class_bool>`{.interpreted-text role="ref"}, format:
`Format<enum_Image_Format>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Image_method_set_data>`{.interpreted-text role="ref"}

Overwrites data of an existing **Image**. Non-static equivalent of
`create_from_data()<class_Image_method_create_from_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_set_pixel}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_pixel**(x: `int<class_int>`{.interpreted-text role="ref"}, y:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Image_method_set_pixel>`{.interpreted-text role="ref"}

Sets the `Color<class_Color>`{.interpreted-text role="ref"} of the pixel
at `(x, y)` to `color`.

::::: tabs
::: code-tab
gdscript

var img_width = 10 var img_height = 5 var img = Image.create(img_width,
img_height, false, Image.FORMAT_RGBA8)

img.set_pixel(1, 2, Color.RED) \# Sets the color at (1, 2) to red.
:::

::: code-tab
csharp

int imgWidth = 10; int imgHeight = 5; var img = Image.Create(imgWidth,
imgHeight, false, Image.Format.Rgba8);

img.SetPixel(1, 2, Colors.Red); // Sets the color at (1, 2) to red.
:::
:::::

This is the same as
`set_pixelv()<class_Image_method_set_pixelv>`{.interpreted-text
role="ref"}, but with a two integer arguments instead of a
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} argument.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_set_pixelv}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_pixelv**(point: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Image_method_set_pixelv>`{.interpreted-text role="ref"}

Sets the `Color<class_Color>`{.interpreted-text role="ref"} of the pixel
at `point` to `color`.

::::: tabs
::: code-tab
gdscript

var img_width = 10 var img_height = 5 var img = Image.create(img_width,
img_height, false, Image.FORMAT_RGBA8)

img.set_pixelv(Vector2i(1, 2), Color.RED) \# Sets the color at (1, 2) to
red.
:::

::: code-tab
csharp

int imgWidth = 10; int imgHeight = 5; var img = Image.Create(imgWidth,
imgHeight, false, Image.Format.Rgba8);

img.SetPixelv(new Vector2I(1, 2), Colors.Red); // Sets the color at (1,
2) to red.
:::
:::::

This is the same as
`set_pixel()<class_Image_method_set_pixel>`{.interpreted-text
role="ref"}, but with a `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"} argument instead of two integer arguments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_shrink_x2}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **shrink_x2**()
`🔗<class_Image_method_shrink_x2>`{.interpreted-text role="ref"}

Shrinks the image by a factor of 2 on each axis (this divides the pixel
count by 4).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Image_method_srgb_to_linear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**srgb_to_linear**()
`🔗<class_Image_method_srgb_to_linear>`{.interpreted-text role="ref"}

Converts the raw data from the sRGB colorspace to a linear scale. Only
works on images with
`FORMAT_RGB8<class_Image_constant_FORMAT_RGB8>`{.interpreted-text
role="ref"} or
`FORMAT_RGBA8<class_Image_constant_FORMAT_RGBA8>`{.interpreted-text
role="ref"} formats.
