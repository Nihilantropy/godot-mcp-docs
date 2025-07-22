github_url
:   hide

# RenderingServer {#class_RenderingServer}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Server for anything visible.

::: rst-class
classref-introduction-group
:::

## Description

The rendering server is the API backend for everything visible. The
whole scene system mounts on it to display. The rendering server is
completely opaque: the internals are entirely implementation-specific
and cannot be accessed.

The rendering server can be used to bypass the
scene/`Node<class_Node>`{.interpreted-text role="ref"} system entirely.
This can improve performance in cases where the scene system is the
bottleneck, but won\'t improve performance otherwise (for instance, if
the GPU is already fully utilized).

Resources are created using the `*_create` functions. These functions
return `RID<class_RID>`{.interpreted-text role="ref"}s which are not
references to the objects themselves, but opaque *pointers* towards
these objects.

All objects are drawn to a viewport. You can use the
`Viewport<class_Viewport>`{.interpreted-text role="ref"} attached to the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} or you can
create one yourself with
`viewport_create()<class_RenderingServer_method_viewport_create>`{.interpreted-text
role="ref"}. When using a custom scenario or canvas, the scenario or
canvas needs to be attached to the viewport using
`viewport_set_scenario()<class_RenderingServer_method_viewport_set_scenario>`{.interpreted-text
role="ref"} or
`viewport_attach_canvas()<class_RenderingServer_method_viewport_attach_canvas>`{.interpreted-text
role="ref"}.

\*\*Scenarios:\*\* In 3D, all visual objects must be associated with a
scenario. The scenario is a visual representation of the world. If
accessing the rendering server from a running game, the scenario can be
accessed from the scene tree from any
`Node3D<class_Node3D>`{.interpreted-text role="ref"} node with
`Node3D.get_world_3d()<class_Node3D_method_get_world_3d>`{.interpreted-text
role="ref"}. Otherwise, a scenario can be created with
`scenario_create()<class_RenderingServer_method_scenario_create>`{.interpreted-text
role="ref"}.

Similarly, in 2D, a canvas is needed to draw all canvas items.

\*\*3D:\*\* In 3D, all visible objects are comprised of a resource and
an instance. A resource can be a mesh, a particle system, a light, or
any other 3D object. In order to be visible resources must be attached
to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"}. The instance must also be attached to the scenario using
`instance_set_scenario()<class_RenderingServer_method_instance_set_scenario>`{.interpreted-text
role="ref"} in order to be visible. RenderingServer methods that don\'t
have a prefix are usually 3D-specific (but not always).

\*\*2D:\*\* In 2D, all visible objects are some form of canvas item. In
order to be visible, a canvas item needs to be the child of a canvas
attached to a viewport, or it needs to be the child of another canvas
item that is eventually attached to the canvas. 2D-specific
RenderingServer methods generally start with `canvas_*`.

\*\*Headless mode:\*\* Starting the engine with the `--headless`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"} disables all rendering and window management functions. Most
functions from **RenderingServer** will return dummy values in this
case.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Optimization using Servers <../tutorials/performance/using_servers>`{.interpreted-text
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

## Signals

:::: {#class_RenderingServer_signal_frame_post_draw}
::: rst-class
classref-signal
:::
::::

**frame_post_draw**()
`🔗<class_RenderingServer_signal_frame_post_draw>`{.interpreted-text
role="ref"}

Emitted at the end of the frame, after the RenderingServer has finished
updating all the Viewports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_signal_frame_pre_draw}
::: rst-class
classref-signal
:::
::::

**frame_pre_draw**()
`🔗<class_RenderingServer_signal_frame_pre_draw>`{.interpreted-text
role="ref"}

Emitted at the beginning of the frame, before the RenderingServer
updates all the Viewports.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_RenderingServer_TextureType}
::: rst-class
classref-enumeration
:::
::::

enum **TextureType**:
`🔗<enum_RenderingServer_TextureType>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_TEXTURE_TYPE_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingServer_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_2D** = `0`

2D texture.

:::: {#class_RenderingServer_constant_TEXTURE_TYPE_LAYERED}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingServer_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_LAYERED** = `1`

Layered texture.

:::: {#class_RenderingServer_constant_TEXTURE_TYPE_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingServer_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_3D** = `2`

3D texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_TextureLayeredType}
::: rst-class
classref-enumeration
:::
::::

enum **TextureLayeredType**:
`🔗<enum_RenderingServer_TextureLayeredType>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_TEXTURE_LAYERED_2D_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureLayeredType<enum_RenderingServer_TextureLayeredType>`{.interpreted-text
role="ref"} **TEXTURE_LAYERED_2D_ARRAY** = `0`

Array of 2-dimensional textures (see
`Texture2DArray<class_Texture2DArray>`{.interpreted-text role="ref"}).

:::: {#class_RenderingServer_constant_TEXTURE_LAYERED_CUBEMAP}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureLayeredType<enum_RenderingServer_TextureLayeredType>`{.interpreted-text
role="ref"} **TEXTURE_LAYERED_CUBEMAP** = `1`

Cubemap texture (see `Cubemap<class_Cubemap>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_TEXTURE_LAYERED_CUBEMAP_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureLayeredType<enum_RenderingServer_TextureLayeredType>`{.interpreted-text
role="ref"} **TEXTURE_LAYERED_CUBEMAP_ARRAY** = `2`

Array of cubemap textures (see
`CubemapArray<class_CubemapArray>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CubeMapLayer}
::: rst-class
classref-enumeration
:::
::::

enum **CubeMapLayer**:
`🔗<enum_RenderingServer_CubeMapLayer>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_CUBEMAP_LAYER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`CubeMapLayer<enum_RenderingServer_CubeMapLayer>`{.interpreted-text
role="ref"} **CUBEMAP_LAYER_LEFT** = `0`

Left face of a `Cubemap<class_Cubemap>`{.interpreted-text role="ref"}.

:::: {#class_RenderingServer_constant_CUBEMAP_LAYER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`CubeMapLayer<enum_RenderingServer_CubeMapLayer>`{.interpreted-text
role="ref"} **CUBEMAP_LAYER_RIGHT** = `1`

Right face of a `Cubemap<class_Cubemap>`{.interpreted-text role="ref"}.

:::: {#class_RenderingServer_constant_CUBEMAP_LAYER_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`CubeMapLayer<enum_RenderingServer_CubeMapLayer>`{.interpreted-text
role="ref"} **CUBEMAP_LAYER_BOTTOM** = `2`

Bottom face of a `Cubemap<class_Cubemap>`{.interpreted-text role="ref"}.

:::: {#class_RenderingServer_constant_CUBEMAP_LAYER_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`CubeMapLayer<enum_RenderingServer_CubeMapLayer>`{.interpreted-text
role="ref"} **CUBEMAP_LAYER_TOP** = `3`

Top face of a `Cubemap<class_Cubemap>`{.interpreted-text role="ref"}.

:::: {#class_RenderingServer_constant_CUBEMAP_LAYER_FRONT}
::: rst-class
classref-enumeration-constant
:::
::::

`CubeMapLayer<enum_RenderingServer_CubeMapLayer>`{.interpreted-text
role="ref"} **CUBEMAP_LAYER_FRONT** = `4`

Front face of a `Cubemap<class_Cubemap>`{.interpreted-text role="ref"}.

:::: {#class_RenderingServer_constant_CUBEMAP_LAYER_BACK}
::: rst-class
classref-enumeration-constant
:::
::::

`CubeMapLayer<enum_RenderingServer_CubeMapLayer>`{.interpreted-text
role="ref"} **CUBEMAP_LAYER_BACK** = `5`

Back face of a `Cubemap<class_Cubemap>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ShaderMode}
::: rst-class
classref-enumeration
:::
::::

enum **ShaderMode**:
`🔗<enum_RenderingServer_ShaderMode>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_SHADER_SPATIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderMode<enum_RenderingServer_ShaderMode>`{.interpreted-text
role="ref"} **SHADER_SPATIAL** = `0`

Shader is a 3D shader.

:::: {#class_RenderingServer_constant_SHADER_CANVAS_ITEM}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderMode<enum_RenderingServer_ShaderMode>`{.interpreted-text
role="ref"} **SHADER_CANVAS_ITEM** = `1`

Shader is a 2D shader.

:::: {#class_RenderingServer_constant_SHADER_PARTICLES}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderMode<enum_RenderingServer_ShaderMode>`{.interpreted-text
role="ref"} **SHADER_PARTICLES** = `2`

Shader is a particle shader (can be used in both 2D and 3D).

:::: {#class_RenderingServer_constant_SHADER_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderMode<enum_RenderingServer_ShaderMode>`{.interpreted-text
role="ref"} **SHADER_SKY** = `3`

Shader is a 3D sky shader.

:::: {#class_RenderingServer_constant_SHADER_FOG}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderMode<enum_RenderingServer_ShaderMode>`{.interpreted-text
role="ref"} **SHADER_FOG** = `4`

Shader is a 3D fog shader.

:::: {#class_RenderingServer_constant_SHADER_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderMode<enum_RenderingServer_ShaderMode>`{.interpreted-text
role="ref"} **SHADER_MAX** = `5`

Represents the size of the
`ShaderMode<enum_RenderingServer_ShaderMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ArrayType}
::: rst-class
classref-enumeration
:::
::::

enum **ArrayType**:
`🔗<enum_RenderingServer_ArrayType>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_ARRAY_VERTEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_VERTEX** = `0`

Array is a vertex position array.

:::: {#class_RenderingServer_constant_ARRAY_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_NORMAL** = `1`

Array is a normal array.

:::: {#class_RenderingServer_constant_ARRAY_TANGENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_TANGENT** = `2`

Array is a tangent array.

:::: {#class_RenderingServer_constant_ARRAY_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_COLOR** = `3`

Array is a vertex color array.

:::: {#class_RenderingServer_constant_ARRAY_TEX_UV}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_TEX_UV** = `4`

Array is a UV coordinates array.

:::: {#class_RenderingServer_constant_ARRAY_TEX_UV2}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_TEX_UV2** = `5`

Array is a UV coordinates array for the second set of UV coordinates.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM0}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM0** = `6`

Array is a custom data array for the first set of custom data.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM1}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM1** = `7`

Array is a custom data array for the second set of custom data.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM2}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM2** = `8`

Array is a custom data array for the third set of custom data.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM3}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM3** = `9`

Array is a custom data array for the fourth set of custom data.

:::: {#class_RenderingServer_constant_ARRAY_BONES}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_BONES** = `10`

Array contains bone information.

:::: {#class_RenderingServer_constant_ARRAY_WEIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_WEIGHTS** = `11`

Array is weight information.

:::: {#class_RenderingServer_constant_ARRAY_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_INDEX** = `12`

Array is an index array.

:::: {#class_RenderingServer_constant_ARRAY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} **ARRAY_MAX** = `13`

Represents the size of the
`ArrayType<enum_RenderingServer_ArrayType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ArrayCustomFormat}
::: rst-class
classref-enumeration
:::
::::

enum **ArrayCustomFormat**:
`🔗<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_RGBA8_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGBA8_UNORM** = `0`

Custom data array contains 8-bit-per-channel red/green/blue/alpha color
data. Values are normalized, unsigned floating-point in the `[0.0, 1.0]`
range.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_RGBA8_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGBA8_SNORM** = `1`

Custom data array contains 8-bit-per-channel red/green/blue/alpha color
data. Values are normalized, signed floating-point in the `[-1.0, 1.0]`
range.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_RG_HALF}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RG_HALF** = `2`

Custom data array contains 16-bit-per-channel red/green color data.
Values are floating-point in half precision.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_RGBA_HALF}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGBA_HALF** = `3`

Custom data array contains 16-bit-per-channel red/green/blue/alpha color
data. Values are floating-point in half precision.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_R_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_R_FLOAT** = `4`

Custom data array contains 32-bit-per-channel red color data. Values are
floating-point in single precision.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_RG_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RG_FLOAT** = `5`

Custom data array contains 32-bit-per-channel red/green color data.
Values are floating-point in single precision.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_RGB_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGB_FLOAT** = `6`

Custom data array contains 32-bit-per-channel red/green/blue color data.
Values are floating-point in single precision.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_RGBA_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGBA_FLOAT** = `7`

Custom data array contains 32-bit-per-channel red/green/blue/alpha color
data. Values are floating-point in single precision.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_MAX** = `8`

Represents the size of the
`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ArrayFormat}
::: rst-class
classref-enumeration
:::
::::

flags **ArrayFormat**:
`🔗<enum_RenderingServer_ArrayFormat>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_VERTEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_VERTEX** = `1`

Flag used to mark a vertex position array.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_NORMAL** = `2`

Flag used to mark a normal array.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_TANGENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_TANGENT** = `4`

Flag used to mark a tangent array.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_COLOR** = `8`

Flag used to mark a vertex color array.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_TEX_UV}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_TEX_UV** = `16`

Flag used to mark a UV coordinates array.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_TEX_UV2}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_TEX_UV2** = `32`

Flag used to mark a UV coordinates array for the second UV coordinates.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM0}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM0** = `64`

Flag used to mark an array of custom per-vertex data for the first set
of custom data.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM1}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM1** = `128`

Flag used to mark an array of custom per-vertex data for the second set
of custom data.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM2}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM2** = `256`

Flag used to mark an array of custom per-vertex data for the third set
of custom data.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM3}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM3** = `512`

Flag used to mark an array of custom per-vertex data for the fourth set
of custom data.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_BONES}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_BONES** = `1024`

Flag used to mark a bone information array.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_WEIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_WEIGHTS** = `2048`

Flag used to mark a weights array.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_INDEX** = `4096`

Flag used to mark an index array.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_BLEND_SHAPE_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_BLEND_SHAPE_MASK** = `7`

Mask of mesh channels permitted in blend shapes.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM_BASE}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM_BASE** = `13`

Shift of first custom channel.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM_BITS}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM_BITS** = `3`

Number of format bits per custom channel. See
`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM0_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM0_SHIFT** = `13`

Amount to shift
`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} for custom channel index 0.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM1_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM1_SHIFT** = `16`

Amount to shift
`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} for custom channel index 1.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM2_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM2_SHIFT** = `19`

Amount to shift
`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} for custom channel index 2.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM3_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM3_SHIFT** = `22`

Amount to shift
`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"} for custom channel index 3.

:::: {#class_RenderingServer_constant_ARRAY_FORMAT_CUSTOM_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FORMAT_CUSTOM_MASK** = `7`

Mask of custom format bits per custom channel. Must be shifted by one of
the SHIFT constants. See
`ArrayCustomFormat<enum_RenderingServer_ArrayCustomFormat>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_ARRAY_COMPRESS_FLAGS_BASE}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_COMPRESS_FLAGS_BASE** = `25`

Shift of first compress flag. Compress flags should be passed to
`ArrayMesh.add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"} and
`SurfaceTool.commit()<class_SurfaceTool_method_commit>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_USE_2D_VERTICES}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_USE_2D_VERTICES** = `33554432`

Flag used to mark that the array contains 2D vertices.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_USE_DYNAMIC_UPDATE** = `67108864`

Flag used to mark that the mesh data will use `GL_DYNAMIC_DRAW` on GLES.
Unused on Vulkan.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_USE_8_BONE_WEIGHTS** = `134217728`

Flag used to mark that the array uses 8 bone weights instead of 4.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY** = `268435456`

Flag used to mark that the mesh does not have a vertex array and instead
will infer vertex positions in the shader using indices and other
information.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_COMPRESS_ATTRIBUTES}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_COMPRESS_ATTRIBUTES** = `536870912`

Flag used to mark that a mesh is using compressed attributes (vertices,
normals, tangents, UVs). When this form of compression is enabled,
vertex positions will be packed into an RGBA16UNORM attribute and scaled
in the vertex shader. The normal and tangent will be packed into an
RG16UNORM representing an axis, and a 16-bit float stored in the
A-channel of the vertex. UVs will use 16-bit normalized floats instead
of full 32-bit signed floats. When using this compression mode you must
use either vertices, normals, and tangents or only vertices. You cannot
use normals without tangents. Importers will automatically enable this
compression if they can.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_BASE}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_FORMAT_VERSION_BASE** = `35`

Flag used to mark the start of the bits used to store the mesh version.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_FORMAT_VERSION_SHIFT** = `35`

Flag used to shift a mesh format int to bring the version into the
lowest digits.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_1}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_FORMAT_VERSION_1** = `0`

Flag used to record the format used by prior mesh versions before the
introduction of a version.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_2}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_FORMAT_VERSION_2** = `34359738368`

Flag used to record the second iteration of the mesh version flag. The
primary difference between this and
`ARRAY_FLAG_FORMAT_VERSION_1<class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_1>`{.interpreted-text
role="ref"} is that this version supports
`ARRAY_FLAG_COMPRESS_ATTRIBUTES<class_RenderingServer_constant_ARRAY_FLAG_COMPRESS_ATTRIBUTES>`{.interpreted-text
role="ref"} and in this version vertex positions are de-interleaved from
normals and tangents.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_FORMAT_CURRENT_VERSION}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_FORMAT_CURRENT_VERSION** = `34359738368`

Flag used to record the current version that the engine expects.
Currently this is the same as
`ARRAY_FLAG_FORMAT_VERSION_2<class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_2>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"} **ARRAY_FLAG_FORMAT_VERSION_MASK** = `255`

Flag used to isolate the bits used for mesh version after using
`ARRAY_FLAG_FORMAT_VERSION_SHIFT<class_RenderingServer_constant_ARRAY_FLAG_FORMAT_VERSION_SHIFT>`{.interpreted-text
role="ref"} to shift them into place.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_PrimitiveType}
::: rst-class
classref-enumeration
:::
::::

enum **PrimitiveType**:
`🔗<enum_RenderingServer_PrimitiveType>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_PRIMITIVE_POINTS}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_RenderingServer_PrimitiveType>`{.interpreted-text
role="ref"} **PRIMITIVE_POINTS** = `0`

Primitive to draw consists of points.

:::: {#class_RenderingServer_constant_PRIMITIVE_LINES}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_RenderingServer_PrimitiveType>`{.interpreted-text
role="ref"} **PRIMITIVE_LINES** = `1`

Primitive to draw consists of lines.

:::: {#class_RenderingServer_constant_PRIMITIVE_LINE_STRIP}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_RenderingServer_PrimitiveType>`{.interpreted-text
role="ref"} **PRIMITIVE_LINE_STRIP** = `2`

Primitive to draw consists of a line strip from start to end.

:::: {#class_RenderingServer_constant_PRIMITIVE_TRIANGLES}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_RenderingServer_PrimitiveType>`{.interpreted-text
role="ref"} **PRIMITIVE_TRIANGLES** = `3`

Primitive to draw consists of triangles.

:::: {#class_RenderingServer_constant_PRIMITIVE_TRIANGLE_STRIP}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_RenderingServer_PrimitiveType>`{.interpreted-text
role="ref"} **PRIMITIVE_TRIANGLE_STRIP** = `4`

Primitive to draw consists of a triangle strip (the last 3 vertices are
always combined to make a triangle).

:::: {#class_RenderingServer_constant_PRIMITIVE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_RenderingServer_PrimitiveType>`{.interpreted-text
role="ref"} **PRIMITIVE_MAX** = `5`

Represents the size of the
`PrimitiveType<enum_RenderingServer_PrimitiveType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_BlendShapeMode}
::: rst-class
classref-enumeration
:::
::::

enum **BlendShapeMode**:
`🔗<enum_RenderingServer_BlendShapeMode>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_BLEND_SHAPE_MODE_NORMALIZED}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeMode<enum_RenderingServer_BlendShapeMode>`{.interpreted-text
role="ref"} **BLEND_SHAPE_MODE_NORMALIZED** = `0`

Blend shapes are normalized.

:::: {#class_RenderingServer_constant_BLEND_SHAPE_MODE_RELATIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeMode<enum_RenderingServer_BlendShapeMode>`{.interpreted-text
role="ref"} **BLEND_SHAPE_MODE_RELATIVE** = `1`

Blend shapes are relative to base weight.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_MultimeshTransformFormat}
::: rst-class
classref-enumeration
:::
::::

enum **MultimeshTransformFormat**:
`🔗<enum_RenderingServer_MultimeshTransformFormat>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_MULTIMESH_TRANSFORM_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`MultimeshTransformFormat<enum_RenderingServer_MultimeshTransformFormat>`{.interpreted-text
role="ref"} **MULTIMESH_TRANSFORM_2D** = `0`

Use `Transform2D<class_Transform2D>`{.interpreted-text role="ref"} to
store MultiMesh transform.

:::: {#class_RenderingServer_constant_MULTIMESH_TRANSFORM_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`MultimeshTransformFormat<enum_RenderingServer_MultimeshTransformFormat>`{.interpreted-text
role="ref"} **MULTIMESH_TRANSFORM_3D** = `1`

Use `Transform3D<class_Transform3D>`{.interpreted-text role="ref"} to
store MultiMesh transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_MultimeshPhysicsInterpolationQuality}
::: rst-class
classref-enumeration
:::
::::

enum **MultimeshPhysicsInterpolationQuality**:
`🔗<enum_RenderingServer_MultimeshPhysicsInterpolationQuality>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_MULTIMESH_INTERP_QUALITY_FAST}
::: rst-class
classref-enumeration-constant
:::
::::

`MultimeshPhysicsInterpolationQuality<enum_RenderingServer_MultimeshPhysicsInterpolationQuality>`{.interpreted-text
role="ref"} **MULTIMESH_INTERP_QUALITY_FAST** = `0`

MultiMesh physics interpolation favors speed over quality.

:::: {#class_RenderingServer_constant_MULTIMESH_INTERP_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`MultimeshPhysicsInterpolationQuality<enum_RenderingServer_MultimeshPhysicsInterpolationQuality>`{.interpreted-text
role="ref"} **MULTIMESH_INTERP_QUALITY_HIGH** = `1`

MultiMesh physics interpolation favors quality over speed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_LightProjectorFilter}
::: rst-class
classref-enumeration
:::
::::

enum **LightProjectorFilter**:
`🔗<enum_RenderingServer_LightProjectorFilter>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`LightProjectorFilter<enum_RenderingServer_LightProjectorFilter>`{.interpreted-text
role="ref"} **LIGHT_PROJECTOR_FILTER_NEAREST** = `0`

Nearest-neighbor filter for light projectors (use for pixel art light
projectors). No mipmaps are used for rendering, which means light
projectors at a distance will look sharp but grainy. This has roughly
the same performance cost as using mipmaps.

:::: {#class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`LightProjectorFilter<enum_RenderingServer_LightProjectorFilter>`{.interpreted-text
role="ref"} **LIGHT_PROJECTOR_FILTER_LINEAR** = `1`

Linear filter for light projectors (use for non-pixel art light
projectors). No mipmaps are used for rendering, which means light
projectors at a distance will look smooth but blurry. This has roughly
the same performance cost as using mipmaps.

:::: {#class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`LightProjectorFilter<enum_RenderingServer_LightProjectorFilter>`{.interpreted-text
role="ref"} **LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS** = `2`

Nearest-neighbor filter for light projectors (use for pixel art light
projectors). Isotropic mipmaps are used for rendering, which means light
projectors at a distance will look smooth but blurry. This has roughly
the same performance cost as not using mipmaps.

:::: {#class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`LightProjectorFilter<enum_RenderingServer_LightProjectorFilter>`{.interpreted-text
role="ref"} **LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS** = `3`

Linear filter for light projectors (use for non-pixel art light
projectors). Isotropic mipmaps are used for rendering, which means light
projectors at a distance will look smooth but blurry. This has roughly
the same performance cost as not using mipmaps.

:::: {#class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`LightProjectorFilter<enum_RenderingServer_LightProjectorFilter>`{.interpreted-text
role="ref"} **LIGHT_PROJECTOR_FILTER_NEAREST_MIPMAPS_ANISOTROPIC** = `4`

Nearest-neighbor filter for light projectors (use for pixel art light
projectors). Anisotropic mipmaps are used for rendering, which means
light projectors at a distance will look smooth and sharp when viewed
from oblique angles. This looks better compared to isotropic mipmaps,
but is slower. The level of anisotropic filtering is defined by
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`LightProjectorFilter<enum_RenderingServer_LightProjectorFilter>`{.interpreted-text
role="ref"} **LIGHT_PROJECTOR_FILTER_LINEAR_MIPMAPS_ANISOTROPIC** = `5`

Linear filter for light projectors (use for non-pixel art light
projectors). Anisotropic mipmaps are used for rendering, which means
light projectors at a distance will look smooth and sharp when viewed
from oblique angles. This looks better compared to isotropic mipmaps,
but is slower. The level of anisotropic filtering is defined by
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_LightType}
::: rst-class
classref-enumeration
:::
::::

enum **LightType**:
`🔗<enum_RenderingServer_LightType>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_LIGHT_DIRECTIONAL}
::: rst-class
classref-enumeration-constant
:::
::::

`LightType<enum_RenderingServer_LightType>`{.interpreted-text
role="ref"} **LIGHT_DIRECTIONAL** = `0`

Directional (sun/moon) light (see
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_LIGHT_OMNI}
::: rst-class
classref-enumeration-constant
:::
::::

`LightType<enum_RenderingServer_LightType>`{.interpreted-text
role="ref"} **LIGHT_OMNI** = `1`

Omni light (see `OmniLight3D<class_OmniLight3D>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_LIGHT_SPOT}
::: rst-class
classref-enumeration-constant
:::
::::

`LightType<enum_RenderingServer_LightType>`{.interpreted-text
role="ref"} **LIGHT_SPOT** = `2`

Spot light (see `SpotLight3D<class_SpotLight3D>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_LightParam}
::: rst-class
classref-enumeration
:::
::::

enum **LightParam**:
`🔗<enum_RenderingServer_LightParam>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_LIGHT_PARAM_ENERGY}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_ENERGY** = `0`

The light\'s energy multiplier.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_INDIRECT_ENERGY}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_INDIRECT_ENERGY** = `1`

The light\'s indirect energy multiplier (final indirect energy is
`LIGHT_PARAM_ENERGY<class_RenderingServer_constant_LIGHT_PARAM_ENERGY>`{.interpreted-text
role="ref"} \*
`LIGHT_PARAM_INDIRECT_ENERGY<class_RenderingServer_constant_LIGHT_PARAM_INDIRECT_ENERGY>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY** = `2`

The light\'s volumetric fog energy multiplier (final volumetric fog
energy is
`LIGHT_PARAM_ENERGY<class_RenderingServer_constant_LIGHT_PARAM_ENERGY>`{.interpreted-text
role="ref"} \*
`LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY<class_RenderingServer_constant_LIGHT_PARAM_VOLUMETRIC_FOG_ENERGY>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SPECULAR}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SPECULAR** = `3`

The light\'s influence on specularity.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_RANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_RANGE** = `4`

The light\'s range.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SIZE** = `5`

The size of the light when using spot light or omni light. The angular
size of the light when using directional light.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_ATTENUATION}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_ATTENUATION** = `6`

The light\'s attenuation.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SPOT_ANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SPOT_ANGLE** = `7`

The spotlight\'s angle.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SPOT_ATTENUATION}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SPOT_ATTENUATION** = `8`

The spotlight\'s attenuation.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_MAX_DISTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_MAX_DISTANCE** = `9`

The maximum distance for shadow splits. Increasing this value will make
directional shadows visible from further away, at the cost of lower
overall shadow detail and performance (since more objects need to be
included in the directional shadow rendering).

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_SPLIT_1_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_SPLIT_1_OFFSET** = `10`

Proportion of shadow atlas occupied by the first split.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_SPLIT_2_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_SPLIT_2_OFFSET** = `11`

Proportion of shadow atlas occupied by the second split.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_SPLIT_3_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_SPLIT_3_OFFSET** = `12`

Proportion of shadow atlas occupied by the third split. The fourth split
occupies the rest.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_FADE_START}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_FADE_START** = `13`

Proportion of shadow max distance where the shadow will start to fade
out.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_NORMAL_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_NORMAL_BIAS** = `14`

Normal bias used to offset shadow lookup by object normal. Can be used
to fix self-shadowing artifacts.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_BIAS** = `15`

Bias for the shadow lookup to fix self-shadowing artifacts.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_PANCAKE_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_PANCAKE_SIZE** = `16`

Sets the size of the directional shadow pancake. The pancake offsets the
start of the shadow\'s camera frustum to provide a higher effective
depth resolution for the shadow. However, a high pancake size can cause
artifacts in the shadows of large objects that are close to the edge of
the frustum. Reducing the pancake size can help. Setting the size to `0`
turns off the pancaking effect.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_OPACITY}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_OPACITY** = `17`

The light\'s shadow opacity. Values lower than `1.0` make the light
appear through shadows. This can be used to fake global illumination at
a low performance cost.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_SHADOW_BLUR}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_SHADOW_BLUR** = `18`

Blurs the edges of the shadow. Can be used to hide pixel artifacts in
low resolution shadow maps. A high value can make shadows appear grainy
and can cause other unwanted artifacts. Try to keep as near default as
possible.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_TRANSMITTANCE_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_TRANSMITTANCE_BIAS** = `19`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_LIGHT_PARAM_INTENSITY}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_INTENSITY** = `20`

Constant representing the intensity of the light, measured in Lumens
when dealing with a `SpotLight3D<class_SpotLight3D>`{.interpreted-text
role="ref"} or `OmniLight3D<class_OmniLight3D>`{.interpreted-text
role="ref"}, or measured in Lux with a
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}. Only used when
`ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>`{.interpreted-text
role="ref"} is `true`.

:::: {#class_RenderingServer_constant_LIGHT_PARAM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} **LIGHT_PARAM_MAX** = `21`

Represents the size of the
`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_LightBakeMode}
::: rst-class
classref-enumeration
:::
::::

enum **LightBakeMode**:
`🔗<enum_RenderingServer_LightBakeMode>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_LIGHT_BAKE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`LightBakeMode<enum_RenderingServer_LightBakeMode>`{.interpreted-text
role="ref"} **LIGHT_BAKE_DISABLED** = `0`

Light is ignored when baking. This is the fastest mode, but the light
will be taken into account when baking global illumination. This mode
should generally be used for dynamic lights that change quickly, as the
effect of global illumination is less noticeable on those lights.

:::: {#class_RenderingServer_constant_LIGHT_BAKE_STATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`LightBakeMode<enum_RenderingServer_LightBakeMode>`{.interpreted-text
role="ref"} **LIGHT_BAKE_STATIC** = `1`

Light is taken into account in static baking
(`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"},
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}, SDFGI
(`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"})). The light can be moved around or modified, but its global
illumination will not update in real-time. This is suitable for subtle
changes (such as flickering torches), but generally not large changes
such as toggling a light on and off.

:::: {#class_RenderingServer_constant_LIGHT_BAKE_DYNAMIC}
::: rst-class
classref-enumeration-constant
:::
::::

`LightBakeMode<enum_RenderingServer_LightBakeMode>`{.interpreted-text
role="ref"} **LIGHT_BAKE_DYNAMIC** = `2`

Light is taken into account in dynamic baking
(`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} and SDFGI
(`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}) only). The light can be moved around or modified with
global illumination updating in real-time. The light\'s global
illumination appearance will be slightly different compared to
`LIGHT_BAKE_STATIC<class_RenderingServer_constant_LIGHT_BAKE_STATIC>`{.interpreted-text
role="ref"}. This has a greater performance cost compared to
`LIGHT_BAKE_STATIC<class_RenderingServer_constant_LIGHT_BAKE_STATIC>`{.interpreted-text
role="ref"}. When using SDFGI, the update speed of dynamic lights is
affected by
`ProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_update_lights>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_LightOmniShadowMode}
::: rst-class
classref-enumeration
:::
::::

enum **LightOmniShadowMode**:
`🔗<enum_RenderingServer_LightOmniShadowMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_LIGHT_OMNI_SHADOW_DUAL_PARABOLOID}
::: rst-class
classref-enumeration-constant
:::
::::

`LightOmniShadowMode<enum_RenderingServer_LightOmniShadowMode>`{.interpreted-text
role="ref"} **LIGHT_OMNI_SHADOW_DUAL_PARABOLOID** = `0`

Use a dual paraboloid shadow map for omni lights.

:::: {#class_RenderingServer_constant_LIGHT_OMNI_SHADOW_CUBE}
::: rst-class
classref-enumeration-constant
:::
::::

`LightOmniShadowMode<enum_RenderingServer_LightOmniShadowMode>`{.interpreted-text
role="ref"} **LIGHT_OMNI_SHADOW_CUBE** = `1`

Use a cubemap shadow map for omni lights. Slower but better quality than
dual paraboloid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_LightDirectionalShadowMode}
::: rst-class
classref-enumeration
:::
::::

enum **LightDirectionalShadowMode**:
`🔗<enum_RenderingServer_LightDirectionalShadowMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_LIGHT_DIRECTIONAL_SHADOW_ORTHOGONAL}
::: rst-class
classref-enumeration-constant
:::
::::

`LightDirectionalShadowMode<enum_RenderingServer_LightDirectionalShadowMode>`{.interpreted-text
role="ref"} **LIGHT_DIRECTIONAL_SHADOW_ORTHOGONAL** = `0`

Use orthogonal shadow projection for directional light.

:::: {#class_RenderingServer_constant_LIGHT_DIRECTIONAL_SHADOW_PARALLEL_2_SPLITS}
::: rst-class
classref-enumeration-constant
:::
::::

`LightDirectionalShadowMode<enum_RenderingServer_LightDirectionalShadowMode>`{.interpreted-text
role="ref"} **LIGHT_DIRECTIONAL_SHADOW_PARALLEL_2_SPLITS** = `1`

Use 2 splits for shadow projection when using directional light.

:::: {#class_RenderingServer_constant_LIGHT_DIRECTIONAL_SHADOW_PARALLEL_4_SPLITS}
::: rst-class
classref-enumeration-constant
:::
::::

`LightDirectionalShadowMode<enum_RenderingServer_LightDirectionalShadowMode>`{.interpreted-text
role="ref"} **LIGHT_DIRECTIONAL_SHADOW_PARALLEL_4_SPLITS** = `2`

Use 4 splits for shadow projection when using directional light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_LightDirectionalSkyMode}
::: rst-class
classref-enumeration
:::
::::

enum **LightDirectionalSkyMode**:
`🔗<enum_RenderingServer_LightDirectionalSkyMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_AND_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`LightDirectionalSkyMode<enum_RenderingServer_LightDirectionalSkyMode>`{.interpreted-text
role="ref"} **LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_AND_SKY** = `0`

Use DirectionalLight3D in both sky rendering and scene lighting.

:::: {#class_RenderingServer_constant_LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`LightDirectionalSkyMode<enum_RenderingServer_LightDirectionalSkyMode>`{.interpreted-text
role="ref"} **LIGHT_DIRECTIONAL_SKY_MODE_LIGHT_ONLY** = `1`

Only use DirectionalLight3D in scene lighting.

:::: {#class_RenderingServer_constant_LIGHT_DIRECTIONAL_SKY_MODE_SKY_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`LightDirectionalSkyMode<enum_RenderingServer_LightDirectionalSkyMode>`{.interpreted-text
role="ref"} **LIGHT_DIRECTIONAL_SKY_MODE_SKY_ONLY** = `2`

Only use DirectionalLight3D in sky rendering.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ShadowQuality}
::: rst-class
classref-enumeration
:::
::::

enum **ShadowQuality**:
`🔗<enum_RenderingServer_ShadowQuality>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_SHADOW_QUALITY_HARD}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"} **SHADOW_QUALITY_HARD** = `0`

Lowest shadow filtering quality (fastest). Soft shadows are not
available with this quality setting, which means the
`Light3D.shadow_blur<class_Light3D_property_shadow_blur>`{.interpreted-text
role="ref"} property is ignored if
`Light3D.light_size<class_Light3D_property_light_size>`{.interpreted-text
role="ref"} and
`Light3D.light_angular_distance<class_Light3D_property_light_angular_distance>`{.interpreted-text
role="ref"} is `0.0`.

\*\*Note:\*\* The variable shadow blur performed by
`Light3D.light_size<class_Light3D_property_light_size>`{.interpreted-text
role="ref"} and
`Light3D.light_angular_distance<class_Light3D_property_light_angular_distance>`{.interpreted-text
role="ref"} is still effective when using hard shadow filtering. In this
case,
`Light3D.shadow_blur<class_Light3D_property_shadow_blur>`{.interpreted-text
role="ref"} *is* taken into account. However, the results will not be
blurred, instead the blur amount is treated as a maximum radius for the
penumbra.

:::: {#class_RenderingServer_constant_SHADOW_QUALITY_SOFT_VERY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"} **SHADOW_QUALITY_SOFT_VERY_LOW** = `1`

Very low shadow filtering quality (faster). When using this quality
setting,
`Light3D.shadow_blur<class_Light3D_property_shadow_blur>`{.interpreted-text
role="ref"} is automatically multiplied by 0.75× to avoid introducing
too much noise. This division only applies to lights whose
`Light3D.light_size<class_Light3D_property_light_size>`{.interpreted-text
role="ref"} or
`Light3D.light_angular_distance<class_Light3D_property_light_angular_distance>`{.interpreted-text
role="ref"} is `0.0`).

:::: {#class_RenderingServer_constant_SHADOW_QUALITY_SOFT_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"} **SHADOW_QUALITY_SOFT_LOW** = `2`

Low shadow filtering quality (fast).

:::: {#class_RenderingServer_constant_SHADOW_QUALITY_SOFT_MEDIUM}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"} **SHADOW_QUALITY_SOFT_MEDIUM** = `3`

Medium low shadow filtering quality (average).

:::: {#class_RenderingServer_constant_SHADOW_QUALITY_SOFT_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"} **SHADOW_QUALITY_SOFT_HIGH** = `4`

High low shadow filtering quality (slow). When using this quality
setting,
`Light3D.shadow_blur<class_Light3D_property_shadow_blur>`{.interpreted-text
role="ref"} is automatically multiplied by 1.5× to better make use of
the high sample count. This increased blur also improves the stability
of dynamic object shadows. This multiplier only applies to lights whose
`Light3D.light_size<class_Light3D_property_light_size>`{.interpreted-text
role="ref"} or
`Light3D.light_angular_distance<class_Light3D_property_light_angular_distance>`{.interpreted-text
role="ref"} is `0.0`).

:::: {#class_RenderingServer_constant_SHADOW_QUALITY_SOFT_ULTRA}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"} **SHADOW_QUALITY_SOFT_ULTRA** = `5`

Highest low shadow filtering quality (slowest). When using this quality
setting,
`Light3D.shadow_blur<class_Light3D_property_shadow_blur>`{.interpreted-text
role="ref"} is automatically multiplied by 2× to better make use of the
high sample count. This increased blur also improves the stability of
dynamic object shadows. This multiplier only applies to lights whose
`Light3D.light_size<class_Light3D_property_light_size>`{.interpreted-text
role="ref"} or
`Light3D.light_angular_distance<class_Light3D_property_light_angular_distance>`{.interpreted-text
role="ref"} is `0.0`).

:::: {#class_RenderingServer_constant_SHADOW_QUALITY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"} **SHADOW_QUALITY_MAX** = `6`

Represents the size of the
`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ReflectionProbeUpdateMode}
::: rst-class
classref-enumeration
:::
::::

enum **ReflectionProbeUpdateMode**:
`🔗<enum_RenderingServer_ReflectionProbeUpdateMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_REFLECTION_PROBE_UPDATE_ONCE}
::: rst-class
classref-enumeration-constant
:::
::::

`ReflectionProbeUpdateMode<enum_RenderingServer_ReflectionProbeUpdateMode>`{.interpreted-text
role="ref"} **REFLECTION_PROBE_UPDATE_ONCE** = `0`

Reflection probe will update reflections once and then stop.

:::: {#class_RenderingServer_constant_REFLECTION_PROBE_UPDATE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`ReflectionProbeUpdateMode<enum_RenderingServer_ReflectionProbeUpdateMode>`{.interpreted-text
role="ref"} **REFLECTION_PROBE_UPDATE_ALWAYS** = `1`

Reflection probe will update each frame. This mode is necessary to
capture moving objects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ReflectionProbeAmbientMode}
::: rst-class
classref-enumeration
:::
::::

enum **ReflectionProbeAmbientMode**:
`🔗<enum_RenderingServer_ReflectionProbeAmbientMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_REFLECTION_PROBE_AMBIENT_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ReflectionProbeAmbientMode<enum_RenderingServer_ReflectionProbeAmbientMode>`{.interpreted-text
role="ref"} **REFLECTION_PROBE_AMBIENT_DISABLED** = `0`

Do not apply any ambient lighting inside the reflection probe\'s box
defined by its size.

:::: {#class_RenderingServer_constant_REFLECTION_PROBE_AMBIENT_ENVIRONMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ReflectionProbeAmbientMode<enum_RenderingServer_ReflectionProbeAmbientMode>`{.interpreted-text
role="ref"} **REFLECTION_PROBE_AMBIENT_ENVIRONMENT** = `1`

Apply automatically-sourced environment lighting inside the reflection
probe\'s box defined by its size.

:::: {#class_RenderingServer_constant_REFLECTION_PROBE_AMBIENT_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`ReflectionProbeAmbientMode<enum_RenderingServer_ReflectionProbeAmbientMode>`{.interpreted-text
role="ref"} **REFLECTION_PROBE_AMBIENT_COLOR** = `2`

Apply custom ambient lighting inside the reflection probe\'s box defined
by its size. See
`reflection_probe_set_ambient_color()<class_RenderingServer_method_reflection_probe_set_ambient_color>`{.interpreted-text
role="ref"} and
`reflection_probe_set_ambient_energy()<class_RenderingServer_method_reflection_probe_set_ambient_energy>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_DecalTexture}
::: rst-class
classref-enumeration
:::
::::

enum **DecalTexture**:
`🔗<enum_RenderingServer_DecalTexture>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_DECAL_TEXTURE_ALBEDO}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_RenderingServer_DecalTexture>`{.interpreted-text
role="ref"} **DECAL_TEXTURE_ALBEDO** = `0`

Albedo texture slot in a decal
(`Decal.texture_albedo<class_Decal_property_texture_albedo>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_DECAL_TEXTURE_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_RenderingServer_DecalTexture>`{.interpreted-text
role="ref"} **DECAL_TEXTURE_NORMAL** = `1`

Normal map texture slot in a decal
(`Decal.texture_normal<class_Decal_property_texture_normal>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_DECAL_TEXTURE_ORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_RenderingServer_DecalTexture>`{.interpreted-text
role="ref"} **DECAL_TEXTURE_ORM** = `2`

Occlusion/Roughness/Metallic texture slot in a decal
(`Decal.texture_orm<class_Decal_property_texture_orm>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_DECAL_TEXTURE_EMISSION}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_RenderingServer_DecalTexture>`{.interpreted-text
role="ref"} **DECAL_TEXTURE_EMISSION** = `3`

Emission texture slot in a decal
(`Decal.texture_emission<class_Decal_property_texture_emission>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_DECAL_TEXTURE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_RenderingServer_DecalTexture>`{.interpreted-text
role="ref"} **DECAL_TEXTURE_MAX** = `4`

Represents the size of the
`DecalTexture<enum_RenderingServer_DecalTexture>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_DecalFilter}
::: rst-class
classref-enumeration
:::
::::

enum **DecalFilter**:
`🔗<enum_RenderingServer_DecalFilter>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_DECAL_FILTER_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalFilter<enum_RenderingServer_DecalFilter>`{.interpreted-text
role="ref"} **DECAL_FILTER_NEAREST** = `0`

Nearest-neighbor filter for decals (use for pixel art decals). No
mipmaps are used for rendering, which means decals at a distance will
look sharp but grainy. This has roughly the same performance cost as
using mipmaps.

:::: {#class_RenderingServer_constant_DECAL_FILTER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalFilter<enum_RenderingServer_DecalFilter>`{.interpreted-text
role="ref"} **DECAL_FILTER_LINEAR** = `1`

Linear filter for decals (use for non-pixel art decals). No mipmaps are
used for rendering, which means decals at a distance will look smooth
but blurry. This has roughly the same performance cost as using mipmaps.

:::: {#class_RenderingServer_constant_DECAL_FILTER_NEAREST_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalFilter<enum_RenderingServer_DecalFilter>`{.interpreted-text
role="ref"} **DECAL_FILTER_NEAREST_MIPMAPS** = `2`

Nearest-neighbor filter for decals (use for pixel art decals). Isotropic
mipmaps are used for rendering, which means decals at a distance will
look smooth but blurry. This has roughly the same performance cost as
not using mipmaps.

:::: {#class_RenderingServer_constant_DECAL_FILTER_LINEAR_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalFilter<enum_RenderingServer_DecalFilter>`{.interpreted-text
role="ref"} **DECAL_FILTER_LINEAR_MIPMAPS** = `3`

Linear filter for decals (use for non-pixel art decals). Isotropic
mipmaps are used for rendering, which means decals at a distance will
look smooth but blurry. This has roughly the same performance cost as
not using mipmaps.

:::: {#class_RenderingServer_constant_DECAL_FILTER_NEAREST_MIPMAPS_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalFilter<enum_RenderingServer_DecalFilter>`{.interpreted-text
role="ref"} **DECAL_FILTER_NEAREST_MIPMAPS_ANISOTROPIC** = `4`

Nearest-neighbor filter for decals (use for pixel art decals).
Anisotropic mipmaps are used for rendering, which means decals at a
distance will look smooth and sharp when viewed from oblique angles.
This looks better compared to isotropic mipmaps, but is slower. The
level of anisotropic filtering is defined by
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_DECAL_FILTER_LINEAR_MIPMAPS_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalFilter<enum_RenderingServer_DecalFilter>`{.interpreted-text
role="ref"} **DECAL_FILTER_LINEAR_MIPMAPS_ANISOTROPIC** = `5`

Linear filter for decals (use for non-pixel art decals). Anisotropic
mipmaps are used for rendering, which means decals at a distance will
look smooth and sharp when viewed from oblique angles. This looks better
compared to isotropic mipmaps, but is slower. The level of anisotropic
filtering is defined by
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_VoxelGIQuality}
::: rst-class
classref-enumeration
:::
::::

enum **VoxelGIQuality**:
`🔗<enum_RenderingServer_VoxelGIQuality>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_VOXEL_GI_QUALITY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`VoxelGIQuality<enum_RenderingServer_VoxelGIQuality>`{.interpreted-text
role="ref"} **VOXEL_GI_QUALITY_LOW** = `0`

Low `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} rendering
quality using 4 cones.

:::: {#class_RenderingServer_constant_VOXEL_GI_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`VoxelGIQuality<enum_RenderingServer_VoxelGIQuality>`{.interpreted-text
role="ref"} **VOXEL_GI_QUALITY_HIGH** = `1`

High `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} rendering
quality using 6 cones.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ParticlesMode}
::: rst-class
classref-enumeration
:::
::::

enum **ParticlesMode**:
`🔗<enum_RenderingServer_ParticlesMode>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_PARTICLES_MODE_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesMode<enum_RenderingServer_ParticlesMode>`{.interpreted-text
role="ref"} **PARTICLES_MODE_2D** = `0`

2D particles.

:::: {#class_RenderingServer_constant_PARTICLES_MODE_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesMode<enum_RenderingServer_ParticlesMode>`{.interpreted-text
role="ref"} **PARTICLES_MODE_3D** = `1`

3D particles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ParticlesTransformAlign}
::: rst-class
classref-enumeration
:::
::::

enum **ParticlesTransformAlign**:
`🔗<enum_RenderingServer_ParticlesTransformAlign>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_PARTICLES_TRANSFORM_ALIGN_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesTransformAlign<enum_RenderingServer_ParticlesTransformAlign>`{.interpreted-text
role="ref"} **PARTICLES_TRANSFORM_ALIGN_DISABLED** = `0`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesTransformAlign<enum_RenderingServer_ParticlesTransformAlign>`{.interpreted-text
role="ref"} **PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_TRANSFORM_ALIGN_Y_TO_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesTransformAlign<enum_RenderingServer_ParticlesTransformAlign>`{.interpreted-text
role="ref"} **PARTICLES_TRANSFORM_ALIGN_Y_TO_VELOCITY** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD_Y_TO_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesTransformAlign<enum_RenderingServer_ParticlesTransformAlign>`{.interpreted-text
role="ref"} **PARTICLES_TRANSFORM_ALIGN_Z_BILLBOARD_Y_TO_VELOCITY** =
`3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ParticlesDrawOrder}
::: rst-class
classref-enumeration
:::
::::

enum **ParticlesDrawOrder**:
`🔗<enum_RenderingServer_ParticlesDrawOrder>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_PARTICLES_DRAW_ORDER_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesDrawOrder<enum_RenderingServer_ParticlesDrawOrder>`{.interpreted-text
role="ref"} **PARTICLES_DRAW_ORDER_INDEX** = `0`

Draw particles in the order that they appear in the particles array.

:::: {#class_RenderingServer_constant_PARTICLES_DRAW_ORDER_LIFETIME}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesDrawOrder<enum_RenderingServer_ParticlesDrawOrder>`{.interpreted-text
role="ref"} **PARTICLES_DRAW_ORDER_LIFETIME** = `1`

Sort particles based on their lifetime. In other words, the particle
with the highest lifetime is drawn at the front.

:::: {#class_RenderingServer_constant_PARTICLES_DRAW_ORDER_REVERSE_LIFETIME}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesDrawOrder<enum_RenderingServer_ParticlesDrawOrder>`{.interpreted-text
role="ref"} **PARTICLES_DRAW_ORDER_REVERSE_LIFETIME** = `2`

Sort particles based on the inverse of their lifetime. In other words,
the particle with the lowest lifetime is drawn at the front.

:::: {#class_RenderingServer_constant_PARTICLES_DRAW_ORDER_VIEW_DEPTH}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesDrawOrder<enum_RenderingServer_ParticlesDrawOrder>`{.interpreted-text
role="ref"} **PARTICLES_DRAW_ORDER_VIEW_DEPTH** = `3`

Sort particles based on their distance to the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ParticlesCollisionType}
::: rst-class
classref-enumeration
:::
::::

enum **ParticlesCollisionType**:
`🔗<enum_RenderingServer_ParticlesCollisionType>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_SPHERE_ATTRACT}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionType<enum_RenderingServer_ParticlesCollisionType>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_TYPE_SPHERE_ATTRACT** = `0`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_BOX_ATTRACT}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionType<enum_RenderingServer_ParticlesCollisionType>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_TYPE_BOX_ATTRACT** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_VECTOR_FIELD_ATTRACT}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionType<enum_RenderingServer_ParticlesCollisionType>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_TYPE_VECTOR_FIELD_ATTRACT** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_SPHERE_COLLIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionType<enum_RenderingServer_ParticlesCollisionType>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_TYPE_SPHERE_COLLIDE** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_BOX_COLLIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionType<enum_RenderingServer_ParticlesCollisionType>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_TYPE_BOX_COLLIDE** = `4`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_SDF_COLLIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionType<enum_RenderingServer_ParticlesCollisionType>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_TYPE_SDF_COLLIDE** = `5`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_TYPE_HEIGHTFIELD_COLLIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionType<enum_RenderingServer_ParticlesCollisionType>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_TYPE_HEIGHTFIELD_COLLIDE** = `6`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ParticlesCollisionHeightfieldResolution}
::: rst-class
classref-enumeration
:::
::::

enum **ParticlesCollisionHeightfieldResolution**:
`🔗<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_256}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionHeightfieldResolution<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_256** = `0`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_512}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionHeightfieldResolution<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_512** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_1024}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionHeightfieldResolution<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_1024** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_2048}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionHeightfieldResolution<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_2048** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_4096}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionHeightfieldResolution<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_4096** = `4`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_8192}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionHeightfieldResolution<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_8192** = `5`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticlesCollisionHeightfieldResolution<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"} **PARTICLES_COLLISION_HEIGHTFIELD_RESOLUTION_MAX** = `6`

Represents the size of the
`ParticlesCollisionHeightfieldResolution<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_FogVolumeShape}
::: rst-class
classref-enumeration
:::
::::

enum **FogVolumeShape**:
`🔗<enum_RenderingServer_FogVolumeShape>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID}
::: rst-class
classref-enumeration-constant
:::
::::

`FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
role="ref"} **FOG_VOLUME_SHAPE_ELLIPSOID** = `0`

`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} will be
shaped like an ellipsoid (stretched sphere).

:::: {#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE}
::: rst-class
classref-enumeration-constant
:::
::::

`FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
role="ref"} **FOG_VOLUME_SHAPE_CONE** = `1`

`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} will be
shaped like a cone pointing upwards (in local coordinates). The cone\'s
angle is set automatically to fill the size. The cone will be adjusted
to fit within the size. Rotate the
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} node to
reorient the cone. Non-uniform scaling via size is not supported (scale
the `FogVolume<class_FogVolume>`{.interpreted-text role="ref"} node
instead).

:::: {#class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER}
::: rst-class
classref-enumeration-constant
:::
::::

`FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
role="ref"} **FOG_VOLUME_SHAPE_CYLINDER** = `2`

`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} will be
shaped like an upright cylinder (in local coordinates). Rotate the
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} node to
reorient the cylinder. The cylinder will be adjusted to fit within the
size. Non-uniform scaling via size is not supported (scale the
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} node
instead).

:::: {#class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX}
::: rst-class
classref-enumeration-constant
:::
::::

`FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
role="ref"} **FOG_VOLUME_SHAPE_BOX** = `3`

`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} will be
shaped like a box.

:::: {#class_RenderingServer_constant_FOG_VOLUME_SHAPE_WORLD}
::: rst-class
classref-enumeration-constant
:::
::::

`FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
role="ref"} **FOG_VOLUME_SHAPE_WORLD** = `4`

`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} will have no
shape, will cover the whole world and will not be culled.

:::: {#class_RenderingServer_constant_FOG_VOLUME_SHAPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
role="ref"} **FOG_VOLUME_SHAPE_MAX** = `5`

Represents the size of the
`FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportScaling3DMode}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportScaling3DMode**:
`🔗<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_BILINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} **VIEWPORT_SCALING_3D_MODE_BILINEAR** = `0`

Use bilinear scaling for the viewport\'s 3D buffer. The amount of
scaling can be set using
`Viewport.scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}. Values less than `1.0` will result in undersampling while
values greater than `1.0` will result in supersampling. A value of `1.0`
disables scaling.

:::: {#class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_FSR}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} **VIEWPORT_SCALING_3D_MODE_FSR** = `1`

Use AMD FidelityFX Super Resolution 1.0 upscaling for the viewport\'s 3D
buffer. The amount of scaling can be set using
`Viewport.scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}. Values less than `1.0` will result in the viewport being
upscaled using FSR. Values greater than `1.0` are not supported and
bilinear downsampling will be used instead. A value of `1.0` disables
scaling.

:::: {#class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_FSR2}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} **VIEWPORT_SCALING_3D_MODE_FSR2** = `2`

Use AMD FidelityFX Super Resolution 2.2 upscaling for the viewport\'s 3D
buffer. The amount of scaling can be set using
`Viewport.scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}. Values less than `1.0` will result in the viewport being
upscaled using FSR2. Values greater than `1.0` are not supported and
bilinear downsampling will be used instead. A value of `1.0` will use
FSR2 at native resolution as a TAA solution.

:::: {#class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_METALFX_SPATIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} **VIEWPORT_SCALING_3D_MODE_METALFX_SPATIAL** = `3`

Use MetalFX spatial upscaling for the viewport\'s 3D buffer. The amount
of scaling can be set using
`Viewport.scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}. Values less than `1.0` will result in the viewport being
upscaled using MetalFX. Values greater than `1.0` are not supported and
bilinear downsampling will be used instead. A value of `1.0` disables
scaling.

\*\*Note:\*\* Only supported when the Metal rendering driver is in use,
which limits this scaling mode to macOS and iOS.

:::: {#class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_METALFX_TEMPORAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} **VIEWPORT_SCALING_3D_MODE_METALFX_TEMPORAL** = `4`

Use MetalFX temporal upscaling for the viewport\'s 3D buffer. The amount
of scaling can be set using
`Viewport.scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}. Values less than `1.0` will result in the viewport being
upscaled using MetalFX. Values greater than `1.0` are not supported and
bilinear downsampling will be used instead. A value of `1.0` will use
MetalFX at native resolution as a TAA solution.

\*\*Note:\*\* Only supported when the Metal rendering driver is in use,
which limits this scaling mode to macOS and iOS.

:::: {#class_RenderingServer_constant_VIEWPORT_SCALING_3D_MODE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} **VIEWPORT_SCALING_3D_MODE_MAX** = `5`

Represents the size of the
`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportUpdateMode}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportUpdateMode**:
`🔗<enum_RenderingServer_ViewportUpdateMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_UPDATE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportUpdateMode<enum_RenderingServer_ViewportUpdateMode>`{.interpreted-text
role="ref"} **VIEWPORT_UPDATE_DISABLED** = `0`

Do not update the viewport\'s render target.

:::: {#class_RenderingServer_constant_VIEWPORT_UPDATE_ONCE}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportUpdateMode<enum_RenderingServer_ViewportUpdateMode>`{.interpreted-text
role="ref"} **VIEWPORT_UPDATE_ONCE** = `1`

Update the viewport\'s render target once, then switch to
`VIEWPORT_UPDATE_DISABLED<class_RenderingServer_constant_VIEWPORT_UPDATE_DISABLED>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_VIEWPORT_UPDATE_WHEN_VISIBLE}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportUpdateMode<enum_RenderingServer_ViewportUpdateMode>`{.interpreted-text
role="ref"} **VIEWPORT_UPDATE_WHEN_VISIBLE** = `2`

Update the viewport\'s render target only when it is visible. This is
the default value.

:::: {#class_RenderingServer_constant_VIEWPORT_UPDATE_WHEN_PARENT_VISIBLE}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportUpdateMode<enum_RenderingServer_ViewportUpdateMode>`{.interpreted-text
role="ref"} **VIEWPORT_UPDATE_WHEN_PARENT_VISIBLE** = `3`

Update the viewport\'s render target only when its parent is visible.

:::: {#class_RenderingServer_constant_VIEWPORT_UPDATE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportUpdateMode<enum_RenderingServer_ViewportUpdateMode>`{.interpreted-text
role="ref"} **VIEWPORT_UPDATE_ALWAYS** = `4`

Always update the viewport\'s render target.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportClearMode}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportClearMode**:
`🔗<enum_RenderingServer_ViewportClearMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_CLEAR_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportClearMode<enum_RenderingServer_ViewportClearMode>`{.interpreted-text
role="ref"} **VIEWPORT_CLEAR_ALWAYS** = `0`

Always clear the viewport\'s render target before drawing.

:::: {#class_RenderingServer_constant_VIEWPORT_CLEAR_NEVER}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportClearMode<enum_RenderingServer_ViewportClearMode>`{.interpreted-text
role="ref"} **VIEWPORT_CLEAR_NEVER** = `1`

Never clear the viewport\'s render target.

:::: {#class_RenderingServer_constant_VIEWPORT_CLEAR_ONLY_NEXT_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportClearMode<enum_RenderingServer_ViewportClearMode>`{.interpreted-text
role="ref"} **VIEWPORT_CLEAR_ONLY_NEXT_FRAME** = `2`

Clear the viewport\'s render target on the next frame, then switch to
`VIEWPORT_CLEAR_NEVER<class_RenderingServer_constant_VIEWPORT_CLEAR_NEVER>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportEnvironmentMode}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportEnvironmentMode**:
`🔗<enum_RenderingServer_ViewportEnvironmentMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportEnvironmentMode<enum_RenderingServer_ViewportEnvironmentMode>`{.interpreted-text
role="ref"} **VIEWPORT_ENVIRONMENT_DISABLED** = `0`

Disable rendering of 3D environment over 2D canvas.

:::: {#class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportEnvironmentMode<enum_RenderingServer_ViewportEnvironmentMode>`{.interpreted-text
role="ref"} **VIEWPORT_ENVIRONMENT_ENABLED** = `1`

Enable rendering of 3D environment over 2D canvas.

:::: {#class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_INHERIT}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportEnvironmentMode<enum_RenderingServer_ViewportEnvironmentMode>`{.interpreted-text
role="ref"} **VIEWPORT_ENVIRONMENT_INHERIT** = `2`

Inherit enable/disable value from parent. If the topmost parent is also
set to
`VIEWPORT_ENVIRONMENT_INHERIT<class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_INHERIT>`{.interpreted-text
role="ref"}, then this has the same behavior as
`VIEWPORT_ENVIRONMENT_ENABLED<class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_ENABLED>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportEnvironmentMode<enum_RenderingServer_ViewportEnvironmentMode>`{.interpreted-text
role="ref"} **VIEWPORT_ENVIRONMENT_MAX** = `3`

Represents the size of the
`ViewportEnvironmentMode<enum_RenderingServer_ViewportEnvironmentMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportSDFOversize}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportSDFOversize**:
`🔗<enum_RenderingServer_ViewportSDFOversize>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_100_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportSDFOversize<enum_RenderingServer_ViewportSDFOversize>`{.interpreted-text
role="ref"} **VIEWPORT_SDF_OVERSIZE_100_PERCENT** = `0`

Do not oversize the 2D signed distance field. Occluders may disappear
when touching the viewport\'s edges, and
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
collision may stop working earlier than intended. This has the lowest
GPU requirements.

:::: {#class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_120_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportSDFOversize<enum_RenderingServer_ViewportSDFOversize>`{.interpreted-text
role="ref"} **VIEWPORT_SDF_OVERSIZE_120_PERCENT** = `1`

2D signed distance field covers 20% of the viewport\'s size outside the
viewport on each side (top, right, bottom, left).

:::: {#class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_150_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportSDFOversize<enum_RenderingServer_ViewportSDFOversize>`{.interpreted-text
role="ref"} **VIEWPORT_SDF_OVERSIZE_150_PERCENT** = `2`

2D signed distance field covers 50% of the viewport\'s size outside the
viewport on each side (top, right, bottom, left).

:::: {#class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_200_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportSDFOversize<enum_RenderingServer_ViewportSDFOversize>`{.interpreted-text
role="ref"} **VIEWPORT_SDF_OVERSIZE_200_PERCENT** = `3`

2D signed distance field covers 100% of the viewport\'s size outside the
viewport on each side (top, right, bottom, left). This has the highest
GPU requirements.

:::: {#class_RenderingServer_constant_VIEWPORT_SDF_OVERSIZE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportSDFOversize<enum_RenderingServer_ViewportSDFOversize>`{.interpreted-text
role="ref"} **VIEWPORT_SDF_OVERSIZE_MAX** = `4`

Represents the size of the
`ViewportSDFOversize<enum_RenderingServer_ViewportSDFOversize>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportSDFScale}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportSDFScale**:
`🔗<enum_RenderingServer_ViewportSDFScale>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_SDF_SCALE_100_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportSDFScale<enum_RenderingServer_ViewportSDFScale>`{.interpreted-text
role="ref"} **VIEWPORT_SDF_SCALE_100_PERCENT** = `0`

Full resolution 2D signed distance field scale. This has the highest GPU
requirements.

:::: {#class_RenderingServer_constant_VIEWPORT_SDF_SCALE_50_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportSDFScale<enum_RenderingServer_ViewportSDFScale>`{.interpreted-text
role="ref"} **VIEWPORT_SDF_SCALE_50_PERCENT** = `1`

Half resolution 2D signed distance field scale on each axis (25% of the
viewport pixel count).

:::: {#class_RenderingServer_constant_VIEWPORT_SDF_SCALE_25_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportSDFScale<enum_RenderingServer_ViewportSDFScale>`{.interpreted-text
role="ref"} **VIEWPORT_SDF_SCALE_25_PERCENT** = `2`

Quarter resolution 2D signed distance field scale on each axis (6.25% of
the viewport pixel count). This has the lowest GPU requirements.

:::: {#class_RenderingServer_constant_VIEWPORT_SDF_SCALE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportSDFScale<enum_RenderingServer_ViewportSDFScale>`{.interpreted-text
role="ref"} **VIEWPORT_SDF_SCALE_MAX** = `3`

Represents the size of the
`ViewportSDFScale<enum_RenderingServer_ViewportSDFScale>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportMSAA}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportMSAA**:
`🔗<enum_RenderingServer_ViewportMSAA>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_MSAA_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"} **VIEWPORT_MSAA_DISABLED** = `0`

Multisample antialiasing for 3D is disabled. This is the default value,
and also the fastest setting.

:::: {#class_RenderingServer_constant_VIEWPORT_MSAA_2X}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"} **VIEWPORT_MSAA_2X** = `1`

Multisample antialiasing uses 2 samples per pixel for 3D. This has a
moderate impact on performance.

:::: {#class_RenderingServer_constant_VIEWPORT_MSAA_4X}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"} **VIEWPORT_MSAA_4X** = `2`

Multisample antialiasing uses 4 samples per pixel for 3D. This has a
high impact on performance.

:::: {#class_RenderingServer_constant_VIEWPORT_MSAA_8X}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"} **VIEWPORT_MSAA_8X** = `3`

Multisample antialiasing uses 8 samples per pixel for 3D. This has a
very high impact on performance. Likely unsupported on low-end and older
hardware.

:::: {#class_RenderingServer_constant_VIEWPORT_MSAA_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"} **VIEWPORT_MSAA_MAX** = `4`

Represents the size of the
`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportAnisotropicFiltering}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportAnisotropicFiltering**:
`🔗<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_ANISOTROPY_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"} **VIEWPORT_ANISOTROPY_DISABLED** = `0`

Anisotropic filtering is disabled.

:::: {#class_RenderingServer_constant_VIEWPORT_ANISOTROPY_2X}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"} **VIEWPORT_ANISOTROPY_2X** = `1`

Use 2× anisotropic filtering.

:::: {#class_RenderingServer_constant_VIEWPORT_ANISOTROPY_4X}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"} **VIEWPORT_ANISOTROPY_4X** = `2`

Use 4× anisotropic filtering. This is the default value.

:::: {#class_RenderingServer_constant_VIEWPORT_ANISOTROPY_8X}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"} **VIEWPORT_ANISOTROPY_8X** = `3`

Use 8× anisotropic filtering.

:::: {#class_RenderingServer_constant_VIEWPORT_ANISOTROPY_16X}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"} **VIEWPORT_ANISOTROPY_16X** = `4`

Use 16× anisotropic filtering.

:::: {#class_RenderingServer_constant_VIEWPORT_ANISOTROPY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"} **VIEWPORT_ANISOTROPY_MAX** = `5`

Represents the size of the
`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportScreenSpaceAA}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportScreenSpaceAA**:
`🔗<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_SCREEN_SPACE_AA_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
role="ref"} **VIEWPORT_SCREEN_SPACE_AA_DISABLED** = `0`

Do not perform any antialiasing in the full screen post-process.

:::: {#class_RenderingServer_constant_VIEWPORT_SCREEN_SPACE_AA_FXAA}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
role="ref"} **VIEWPORT_SCREEN_SPACE_AA_FXAA** = `1`

Use fast approximate antialiasing. FXAA is a popular screen-space
antialiasing method, which is fast but will make the image look blurry,
especially at lower resolutions. It can still work relatively well at
large resolutions such as 1440p and 4K.

:::: {#class_RenderingServer_constant_VIEWPORT_SCREEN_SPACE_AA_SMAA}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
role="ref"} **VIEWPORT_SCREEN_SPACE_AA_SMAA** = `2`

Use subpixel morphological antialiasing. SMAA may produce clearer
results than FXAA, but at a slightly higher performance cost.

:::: {#class_RenderingServer_constant_VIEWPORT_SCREEN_SPACE_AA_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
role="ref"} **VIEWPORT_SCREEN_SPACE_AA_MAX** = `3`

Represents the size of the
`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportOcclusionCullingBuildQuality}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportOcclusionCullingBuildQuality**:
`🔗<enum_RenderingServer_ViewportOcclusionCullingBuildQuality>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_OCCLUSION_BUILD_QUALITY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportOcclusionCullingBuildQuality<enum_RenderingServer_ViewportOcclusionCullingBuildQuality>`{.interpreted-text
role="ref"} **VIEWPORT_OCCLUSION_BUILD_QUALITY_LOW** = `0`

Low occlusion culling BVH build quality (as defined by Embree). Results
in the lowest CPU usage, but least effective culling.

:::: {#class_RenderingServer_constant_VIEWPORT_OCCLUSION_BUILD_QUALITY_MEDIUM}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportOcclusionCullingBuildQuality<enum_RenderingServer_ViewportOcclusionCullingBuildQuality>`{.interpreted-text
role="ref"} **VIEWPORT_OCCLUSION_BUILD_QUALITY_MEDIUM** = `1`

Medium occlusion culling BVH build quality (as defined by Embree).

:::: {#class_RenderingServer_constant_VIEWPORT_OCCLUSION_BUILD_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportOcclusionCullingBuildQuality<enum_RenderingServer_ViewportOcclusionCullingBuildQuality>`{.interpreted-text
role="ref"} **VIEWPORT_OCCLUSION_BUILD_QUALITY_HIGH** = `2`

High occlusion culling BVH build quality (as defined by Embree). Results
in the highest CPU usage, but most effective culling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportRenderInfo}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportRenderInfo**:
`🔗<enum_RenderingServer_ViewportRenderInfo>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_RENDER_INFO_OBJECTS_IN_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportRenderInfo<enum_RenderingServer_ViewportRenderInfo>`{.interpreted-text
role="ref"} **VIEWPORT_RENDER_INFO_OBJECTS_IN_FRAME** = `0`

Number of objects drawn in a single frame.

:::: {#class_RenderingServer_constant_VIEWPORT_RENDER_INFO_PRIMITIVES_IN_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportRenderInfo<enum_RenderingServer_ViewportRenderInfo>`{.interpreted-text
role="ref"} **VIEWPORT_RENDER_INFO_PRIMITIVES_IN_FRAME** = `1`

Number of points, lines, or triangles drawn in a single frame.

:::: {#class_RenderingServer_constant_VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportRenderInfo<enum_RenderingServer_ViewportRenderInfo>`{.interpreted-text
role="ref"} **VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME** = `2`

Number of draw calls during this frame.

:::: {#class_RenderingServer_constant_VIEWPORT_RENDER_INFO_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportRenderInfo<enum_RenderingServer_ViewportRenderInfo>`{.interpreted-text
role="ref"} **VIEWPORT_RENDER_INFO_MAX** = `3`

Represents the size of the
`ViewportRenderInfo<enum_RenderingServer_ViewportRenderInfo>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportRenderInfoType}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportRenderInfoType**:
`🔗<enum_RenderingServer_ViewportRenderInfoType>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_RENDER_INFO_TYPE_VISIBLE}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportRenderInfoType<enum_RenderingServer_ViewportRenderInfoType>`{.interpreted-text
role="ref"} **VIEWPORT_RENDER_INFO_TYPE_VISIBLE** = `0`

Visible render pass (excluding shadows).

:::: {#class_RenderingServer_constant_VIEWPORT_RENDER_INFO_TYPE_SHADOW}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportRenderInfoType<enum_RenderingServer_ViewportRenderInfoType>`{.interpreted-text
role="ref"} **VIEWPORT_RENDER_INFO_TYPE_SHADOW** = `1`

Shadow render pass. Objects will be rendered several times depending on
the number of amounts of lights with shadows and the number of
directional shadow splits.

:::: {#class_RenderingServer_constant_VIEWPORT_RENDER_INFO_TYPE_CANVAS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportRenderInfoType<enum_RenderingServer_ViewportRenderInfoType>`{.interpreted-text
role="ref"} **VIEWPORT_RENDER_INFO_TYPE_CANVAS** = `2`

Canvas item rendering. This includes all 2D rendering.

:::: {#class_RenderingServer_constant_VIEWPORT_RENDER_INFO_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportRenderInfoType<enum_RenderingServer_ViewportRenderInfoType>`{.interpreted-text
role="ref"} **VIEWPORT_RENDER_INFO_TYPE_MAX** = `3`

Represents the size of the
`ViewportRenderInfoType<enum_RenderingServer_ViewportRenderInfoType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportDebugDraw}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportDebugDraw**:
`🔗<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_DISABLED** = `0`

Debug draw is disabled. Default setting.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_UNSHADED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_UNSHADED** = `1`

Objects are displayed without light information.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_LIGHTING}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_LIGHTING** = `2`

Objects are displayed with only light information.

\*\*Note:\*\* When using this debug draw mode, custom shaders are
ignored since all materials in the scene temporarily use a debug
material. This means the result from custom shader functions (such as
vertex displacement) won\'t be visible anymore when using this debug
draw mode.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_OVERDRAW}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_OVERDRAW** = `3`

Objects are displayed semi-transparent with additive blending so you can
see where they are drawing over top of one another. A higher overdraw
(represented by brighter colors) means you are wasting performance on
drawing pixels that are being hidden behind others.

\*\*Note:\*\* When using this debug draw mode, custom shaders are
ignored since all materials in the scene temporarily use a debug
material. This means the result from custom shader functions (such as
vertex displacement) won\'t be visible anymore when using this debug
draw mode.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_WIREFRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_WIREFRAME** = `4`

Debug draw draws objects in wireframe.

\*\*Note:\*\*
`set_debug_generate_wireframes()<class_RenderingServer_method_set_debug_generate_wireframes>`{.interpreted-text
role="ref"} must be called before loading any meshes for wireframes to
be visible when using the Compatibility renderer.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_NORMAL_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_NORMAL_BUFFER** = `5`

Normal buffer is drawn instead of regular scene so you can see the
per-pixel normals that will be used by post-processing effects.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_VOXEL_GI_ALBEDO}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_VOXEL_GI_ALBEDO** = `6`

Objects are displayed with only the albedo value from
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}s. Requires at
least one visible `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}
node that has been baked to have a visible effect.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_VOXEL_GI_LIGHTING}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_VOXEL_GI_LIGHTING** = `7`

Objects are displayed with only the lighting value from
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}s. Requires at
least one visible `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}
node that has been baked to have a visible effect.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_VOXEL_GI_EMISSION}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_VOXEL_GI_EMISSION** = `8`

Objects are displayed with only the emission color from
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}s. Requires at
least one visible `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}
node that has been baked to have a visible effect.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SHADOW_ATLAS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_SHADOW_ATLAS** = `9`

Draws the shadow atlas that stores shadows from
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"}s and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}s in the
upper left quadrant of the `Viewport<class_Viewport>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS** = `10`

Draws the shadow atlas that stores shadows from
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s in the upper left quadrant of the
`Viewport<class_Viewport>`{.interpreted-text role="ref"}.

The slice of the camera frustum related to the shadow map cascade is
superimposed to visualize coverage. The color of each slice matches the
colors used for
`VIEWPORT_DEBUG_DRAW_PSSM_SPLITS<class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_PSSM_SPLITS>`{.interpreted-text
role="ref"}. When shadow cascades are blended the overlap is taken into
account when drawing the frustum slices.

The last cascade shows all frustum slices to illustrate the coverage of
all slices.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SCENE_LUMINANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_SCENE_LUMINANCE** = `11`

Draws the estimated scene luminance. This is a 1×1 texture that is
generated when autoexposure is enabled to control the scene\'s exposure.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SSAO}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_SSAO** = `12`

Draws the screen space ambient occlusion texture instead of the scene so
that you can clearly see how it is affecting objects. In order for this
display mode to work, you must have
`Environment.ssao_enabled<class_Environment_property_ssao_enabled>`{.interpreted-text
role="ref"} set in your
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SSIL}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_SSIL** = `13`

Draws the screen space indirect lighting texture instead of the scene so
that you can clearly see how it is affecting objects. In order for this
display mode to work, you must have
`Environment.ssil_enabled<class_Environment_property_ssil_enabled>`{.interpreted-text
role="ref"} set in your
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_PSSM_SPLITS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_PSSM_SPLITS** = `14`

Colors each PSSM split for the
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s in the scene a different color so you can see where the
splits are. In order (from closest to furthest from the camera), they
are colored red, green, blue, and yellow.

\*\*Note:\*\* When using this debug draw mode, custom shaders are
ignored since all materials in the scene temporarily use a debug
material. This means the result from custom shader functions (such as
vertex displacement) won\'t be visible anymore when using this debug
draw mode.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_DECAL_ATLAS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_DECAL_ATLAS** = `15`

Draws the decal atlas that stores decal textures from
`Decal<class_Decal>`{.interpreted-text role="ref"}s.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SDFGI}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_SDFGI** = `16`

Draws SDFGI cascade data. This is the data structure that is used to
bounce lighting against and create reflections.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_SDFGI_PROBES}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_SDFGI_PROBES** = `17`

Draws SDFGI probe data. This is the data structure that is used to give
indirect lighting dynamic objects moving within the scene.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_GI_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_GI_BUFFER** = `18`

Draws the global illumination buffer from
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} or SDFGI.
Requires `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} (at
least one visible baked VoxelGI node) or SDFGI
(`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}) to be enabled to have a visible effect.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_DISABLE_LOD}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_DISABLE_LOD** = `19`

Disable mesh LOD. All meshes are drawn with full detail, which can be
used to compare performance.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_CLUSTER_OMNI_LIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_CLUSTER_OMNI_LIGHTS** = `20`

Draws the `OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"}
cluster. Clustering determines where lights are positioned in
screen-space, which allows the engine to only process these portions of
the screen for lighting.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_CLUSTER_SPOT_LIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_CLUSTER_SPOT_LIGHTS** = `21`

Draws the `SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}
cluster. Clustering determines where lights are positioned in
screen-space, which allows the engine to only process these portions of
the screen for lighting.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_CLUSTER_DECALS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_CLUSTER_DECALS** = `22`

Draws the `Decal<class_Decal>`{.interpreted-text role="ref"} cluster.
Clustering determines where decals are positioned in screen-space, which
allows the engine to only process these portions of the screen for
decals.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_CLUSTER_REFLECTION_PROBES}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_CLUSTER_REFLECTION_PROBES** = `23`

Draws the `ReflectionProbe<class_ReflectionProbe>`{.interpreted-text
role="ref"} cluster. Clustering determines where reflection probes are
positioned in screen-space, which allows the engine to only process
these portions of the screen for reflection probes.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_OCCLUDERS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_OCCLUDERS** = `24`

Draws the occlusion culling buffer. This low-resolution occlusion
culling buffer is rasterized on the CPU and is used to check whether
instances are occluded by other objects.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_MOTION_VECTORS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_MOTION_VECTORS** = `25`

Draws the motion vectors buffer. This is used by temporal antialiasing
to correct for motion that occurs during gameplay.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_RenderingServer_constant_VIEWPORT_DEBUG_DRAW_INTERNAL_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"} **VIEWPORT_DEBUG_DRAW_INTERNAL_BUFFER** = `26`

Internal buffer is drawn instead of regular scene so you can see the
per-pixel output that will be used by post-processing effects.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportVRSMode}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportVRSMode**:
`🔗<enum_RenderingServer_ViewportVRSMode>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_VRS_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportVRSMode<enum_RenderingServer_ViewportVRSMode>`{.interpreted-text
role="ref"} **VIEWPORT_VRS_DISABLED** = `0`

Variable rate shading is disabled.

:::: {#class_RenderingServer_constant_VIEWPORT_VRS_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportVRSMode<enum_RenderingServer_ViewportVRSMode>`{.interpreted-text
role="ref"} **VIEWPORT_VRS_TEXTURE** = `1`

Variable rate shading uses a texture. Note, for stereoscopic use a
texture atlas with a texture for each view.

:::: {#class_RenderingServer_constant_VIEWPORT_VRS_XR}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportVRSMode<enum_RenderingServer_ViewportVRSMode>`{.interpreted-text
role="ref"} **VIEWPORT_VRS_XR** = `2`

Variable rate shading texture is supplied by the primary
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"}. Note
that this may override the update mode.

:::: {#class_RenderingServer_constant_VIEWPORT_VRS_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportVRSMode<enum_RenderingServer_ViewportVRSMode>`{.interpreted-text
role="ref"} **VIEWPORT_VRS_MAX** = `3`

Represents the size of the
`ViewportVRSMode<enum_RenderingServer_ViewportVRSMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ViewportVRSUpdateMode}
::: rst-class
classref-enumeration
:::
::::

enum **ViewportVRSUpdateMode**:
`🔗<enum_RenderingServer_ViewportVRSUpdateMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportVRSUpdateMode<enum_RenderingServer_ViewportVRSUpdateMode>`{.interpreted-text
role="ref"} **VIEWPORT_VRS_UPDATE_DISABLED** = `0`

The input texture for variable rate shading will not be processed.

:::: {#class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_ONCE}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportVRSUpdateMode<enum_RenderingServer_ViewportVRSUpdateMode>`{.interpreted-text
role="ref"} **VIEWPORT_VRS_UPDATE_ONCE** = `1`

The input texture for variable rate shading will be processed once.

:::: {#class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportVRSUpdateMode<enum_RenderingServer_ViewportVRSUpdateMode>`{.interpreted-text
role="ref"} **VIEWPORT_VRS_UPDATE_ALWAYS** = `2`

The input texture for variable rate shading will be processed each
frame.

:::: {#class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ViewportVRSUpdateMode<enum_RenderingServer_ViewportVRSUpdateMode>`{.interpreted-text
role="ref"} **VIEWPORT_VRS_UPDATE_MAX** = `3`

Represents the size of the
`ViewportVRSUpdateMode<enum_RenderingServer_ViewportVRSUpdateMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_SkyMode}
::: rst-class
classref-enumeration
:::
::::

enum **SkyMode**: `🔗<enum_RenderingServer_SkyMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_SKY_MODE_AUTOMATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`SkyMode<enum_RenderingServer_SkyMode>`{.interpreted-text role="ref"}
**SKY_MODE_AUTOMATIC** = `0`

Automatically selects the appropriate process mode based on your sky
shader. If your shader uses `TIME` or `POSITION`, this will use
`SKY_MODE_REALTIME<class_RenderingServer_constant_SKY_MODE_REALTIME>`{.interpreted-text
role="ref"}. If your shader uses any of the `LIGHT_*` variables or any
custom uniforms, this uses
`SKY_MODE_INCREMENTAL<class_RenderingServer_constant_SKY_MODE_INCREMENTAL>`{.interpreted-text
role="ref"}. Otherwise, this defaults to
`SKY_MODE_QUALITY<class_RenderingServer_constant_SKY_MODE_QUALITY>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_SKY_MODE_QUALITY}
::: rst-class
classref-enumeration-constant
:::
::::

`SkyMode<enum_RenderingServer_SkyMode>`{.interpreted-text role="ref"}
**SKY_MODE_QUALITY** = `1`

Uses high quality importance sampling to process the radiance map. In
general, this results in much higher quality than
`SKY_MODE_REALTIME<class_RenderingServer_constant_SKY_MODE_REALTIME>`{.interpreted-text
role="ref"} but takes much longer to generate. This should not be used
if you plan on changing the sky at runtime. If you are finding that the
reflection is not blurry enough and is showing sparkles or fireflies,
try increasing
`ProjectSettings.rendering/reflections/sky_reflections/ggx_samples<class_ProjectSettings_property_rendering/reflections/sky_reflections/ggx_samples>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_SKY_MODE_INCREMENTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`SkyMode<enum_RenderingServer_SkyMode>`{.interpreted-text role="ref"}
**SKY_MODE_INCREMENTAL** = `2`

Uses the same high quality importance sampling to process the radiance
map as
`SKY_MODE_QUALITY<class_RenderingServer_constant_SKY_MODE_QUALITY>`{.interpreted-text
role="ref"}, but updates over several frames. The number of frames is
determined by
`ProjectSettings.rendering/reflections/sky_reflections/roughness_layers<class_ProjectSettings_property_rendering/reflections/sky_reflections/roughness_layers>`{.interpreted-text
role="ref"}. Use this when you need highest quality radiance maps, but
have a sky that updates slowly.

:::: {#class_RenderingServer_constant_SKY_MODE_REALTIME}
::: rst-class
classref-enumeration-constant
:::
::::

`SkyMode<enum_RenderingServer_SkyMode>`{.interpreted-text role="ref"}
**SKY_MODE_REALTIME** = `3`

Uses the fast filtering algorithm to process the radiance map. In
general this results in lower quality, but substantially faster run
times. If you need better quality, but still need to update the sky
every frame, consider turning on
`ProjectSettings.rendering/reflections/sky_reflections/fast_filter_high_quality<class_ProjectSettings_property_rendering/reflections/sky_reflections/fast_filter_high_quality>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The fast filtering algorithm is limited to 256×256
cubemaps, so
`sky_set_radiance_size()<class_RenderingServer_method_sky_set_radiance_size>`{.interpreted-text
role="ref"} must be set to `256`. Otherwise, a warning is printed and
the overridden radiance size is ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CompositorEffectFlags}
::: rst-class
classref-enumeration
:::
::::

enum **CompositorEffectFlags**:
`🔗<enum_RenderingServer_CompositorEffectFlags>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectFlags<enum_RenderingServer_CompositorEffectFlags>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_COLOR** = `1`

The rendering effect requires the color buffer to be resolved if MSAA is
enabled.

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_DEPTH}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectFlags<enum_RenderingServer_CompositorEffectFlags>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_FLAG_ACCESS_RESOLVED_DEPTH** = `2`

The rendering effect requires the depth buffer to be resolved if MSAA is
enabled.

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_NEEDS_MOTION_VECTORS}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectFlags<enum_RenderingServer_CompositorEffectFlags>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_FLAG_NEEDS_MOTION_VECTORS** = `4`

The rendering effect requires motion vectors to be produced.

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_NEEDS_ROUGHNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectFlags<enum_RenderingServer_CompositorEffectFlags>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_FLAG_NEEDS_ROUGHNESS** = `8`

The rendering effect requires normals and roughness g-buffer to be
produced (Forward+ only).

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_FLAG_NEEDS_SEPARATE_SPECULAR}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectFlags<enum_RenderingServer_CompositorEffectFlags>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_FLAG_NEEDS_SEPARATE_SPECULAR** = `16`

The rendering effect requires specular data to be separated out
(Forward+ only).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CompositorEffectCallbackType}
::: rst-class
classref-enumeration
:::
::::

enum **CompositorEffectCallbackType**:
`🔗<enum_RenderingServer_CompositorEffectCallbackType>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_OPAQUE}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectCallbackType<enum_RenderingServer_CompositorEffectCallbackType>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_OPAQUE** = `0`

The callback is called before our opaque rendering pass, but after depth
prepass (if applicable).

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_OPAQUE}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectCallbackType<enum_RenderingServer_CompositorEffectCallbackType>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_OPAQUE** = `1`

The callback is called after our opaque rendering pass, but before our
sky is rendered.

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectCallbackType<enum_RenderingServer_CompositorEffectCallbackType>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_SKY** = `2`

The callback is called after our sky is rendered, but before our back
buffers are created (and if enabled, before subsurface scattering and/or
screen space reflections).

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_TRANSPARENT}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectCallbackType<enum_RenderingServer_CompositorEffectCallbackType>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_CALLBACK_TYPE_PRE_TRANSPARENT** = `3`

The callback is called before our transparent rendering pass, but after
our sky is rendered and we\'ve created our back buffers.

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_TRANSPARENT}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectCallbackType<enum_RenderingServer_CompositorEffectCallbackType>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_CALLBACK_TYPE_POST_TRANSPARENT** = `4`

The callback is called after our transparent rendering pass, but before
any built-in post-processing effects and output to our render target.

:::: {#class_RenderingServer_constant_COMPOSITOR_EFFECT_CALLBACK_TYPE_ANY}
::: rst-class
classref-enumeration-constant
:::
::::

`CompositorEffectCallbackType<enum_RenderingServer_CompositorEffectCallbackType>`{.interpreted-text
role="ref"} **COMPOSITOR_EFFECT_CALLBACK_TYPE_ANY** = `-1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentBG}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentBG**:
`🔗<enum_RenderingServer_EnvironmentBG>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_ENV_BG_CLEAR_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBG<enum_RenderingServer_EnvironmentBG>`{.interpreted-text
role="ref"} **ENV_BG_CLEAR_COLOR** = `0`

Use the clear color as background.

:::: {#class_RenderingServer_constant_ENV_BG_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBG<enum_RenderingServer_EnvironmentBG>`{.interpreted-text
role="ref"} **ENV_BG_COLOR** = `1`

Use a specified color as the background.

:::: {#class_RenderingServer_constant_ENV_BG_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBG<enum_RenderingServer_EnvironmentBG>`{.interpreted-text
role="ref"} **ENV_BG_SKY** = `2`

Use a sky resource for the background.

:::: {#class_RenderingServer_constant_ENV_BG_CANVAS}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBG<enum_RenderingServer_EnvironmentBG>`{.interpreted-text
role="ref"} **ENV_BG_CANVAS** = `3`

Use a specified canvas layer as the background. This can be useful for
instantiating a 2D scene in a 3D world.

:::: {#class_RenderingServer_constant_ENV_BG_KEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBG<enum_RenderingServer_EnvironmentBG>`{.interpreted-text
role="ref"} **ENV_BG_KEEP** = `4`

Do not clear the background, use whatever was rendered last frame as the
background.

:::: {#class_RenderingServer_constant_ENV_BG_CAMERA_FEED}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBG<enum_RenderingServer_EnvironmentBG>`{.interpreted-text
role="ref"} **ENV_BG_CAMERA_FEED** = `5`

Displays a camera feed in the background.

:::: {#class_RenderingServer_constant_ENV_BG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBG<enum_RenderingServer_EnvironmentBG>`{.interpreted-text
role="ref"} **ENV_BG_MAX** = `6`

Represents the size of the
`EnvironmentBG<enum_RenderingServer_EnvironmentBG>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentAmbientSource}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentAmbientSource**:
`🔗<enum_RenderingServer_EnvironmentAmbientSource>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_AMBIENT_SOURCE_BG}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentAmbientSource<enum_RenderingServer_EnvironmentAmbientSource>`{.interpreted-text
role="ref"} **ENV_AMBIENT_SOURCE_BG** = `0`

Gather ambient light from whichever source is specified as the
background.

:::: {#class_RenderingServer_constant_ENV_AMBIENT_SOURCE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentAmbientSource<enum_RenderingServer_EnvironmentAmbientSource>`{.interpreted-text
role="ref"} **ENV_AMBIENT_SOURCE_DISABLED** = `1`

Disable ambient light.

:::: {#class_RenderingServer_constant_ENV_AMBIENT_SOURCE_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentAmbientSource<enum_RenderingServer_EnvironmentAmbientSource>`{.interpreted-text
role="ref"} **ENV_AMBIENT_SOURCE_COLOR** = `2`

Specify a specific `Color<class_Color>`{.interpreted-text role="ref"}
for ambient light.

:::: {#class_RenderingServer_constant_ENV_AMBIENT_SOURCE_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentAmbientSource<enum_RenderingServer_EnvironmentAmbientSource>`{.interpreted-text
role="ref"} **ENV_AMBIENT_SOURCE_SKY** = `3`

Gather ambient light from the `Sky<class_Sky>`{.interpreted-text
role="ref"} regardless of what the background is.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentReflectionSource}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentReflectionSource**:
`🔗<enum_RenderingServer_EnvironmentReflectionSource>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_REFLECTION_SOURCE_BG}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentReflectionSource<enum_RenderingServer_EnvironmentReflectionSource>`{.interpreted-text
role="ref"} **ENV_REFLECTION_SOURCE_BG** = `0`

Use the background for reflections.

:::: {#class_RenderingServer_constant_ENV_REFLECTION_SOURCE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentReflectionSource<enum_RenderingServer_EnvironmentReflectionSource>`{.interpreted-text
role="ref"} **ENV_REFLECTION_SOURCE_DISABLED** = `1`

Disable reflections.

:::: {#class_RenderingServer_constant_ENV_REFLECTION_SOURCE_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentReflectionSource<enum_RenderingServer_EnvironmentReflectionSource>`{.interpreted-text
role="ref"} **ENV_REFLECTION_SOURCE_SKY** = `2`

Use the `Sky<class_Sky>`{.interpreted-text role="ref"} for reflections
regardless of what the background is.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentGlowBlendMode}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentGlowBlendMode**:
`🔗<enum_RenderingServer_EnvironmentGlowBlendMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_ADDITIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentGlowBlendMode<enum_RenderingServer_EnvironmentGlowBlendMode>`{.interpreted-text
role="ref"} **ENV_GLOW_BLEND_MODE_ADDITIVE** = `0`

Additive glow blending mode. Mostly used for particles, glows (bloom),
lens flare, bright sources.

:::: {#class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_SCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentGlowBlendMode<enum_RenderingServer_EnvironmentGlowBlendMode>`{.interpreted-text
role="ref"} **ENV_GLOW_BLEND_MODE_SCREEN** = `1`

Screen glow blending mode. Increases brightness, used frequently with
bloom.

:::: {#class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_SOFTLIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentGlowBlendMode<enum_RenderingServer_EnvironmentGlowBlendMode>`{.interpreted-text
role="ref"} **ENV_GLOW_BLEND_MODE_SOFTLIGHT** = `2`

Soft light glow blending mode. Modifies contrast, exposes shadows and
highlights (vivid bloom).

:::: {#class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentGlowBlendMode<enum_RenderingServer_EnvironmentGlowBlendMode>`{.interpreted-text
role="ref"} **ENV_GLOW_BLEND_MODE_REPLACE** = `3`

Replace glow blending mode. Replaces all pixels\' color by the glow
value. This can be used to simulate a full-screen blur effect by
tweaking the glow parameters to match the original image\'s brightness.

:::: {#class_RenderingServer_constant_ENV_GLOW_BLEND_MODE_MIX}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentGlowBlendMode<enum_RenderingServer_EnvironmentGlowBlendMode>`{.interpreted-text
role="ref"} **ENV_GLOW_BLEND_MODE_MIX** = `4`

Mixes the glow with the underlying color to avoid increasing brightness
as much while still maintaining a glow effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentFogMode}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentFogMode**:
`🔗<enum_RenderingServer_EnvironmentFogMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_FOG_MODE_EXPONENTIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentFogMode<enum_RenderingServer_EnvironmentFogMode>`{.interpreted-text
role="ref"} **ENV_FOG_MODE_EXPONENTIAL** = `0`

Use a physically-based fog model defined primarily by fog density.

:::: {#class_RenderingServer_constant_ENV_FOG_MODE_DEPTH}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentFogMode<enum_RenderingServer_EnvironmentFogMode>`{.interpreted-text
role="ref"} **ENV_FOG_MODE_DEPTH** = `1`

Use a simple fog model defined by start and end positions and a custom
curve. While not physically accurate, this model can be useful when you
need more artistic control.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentToneMapper}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentToneMapper**:
`🔗<enum_RenderingServer_EnvironmentToneMapper>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_TONE_MAPPER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentToneMapper<enum_RenderingServer_EnvironmentToneMapper>`{.interpreted-text
role="ref"} **ENV_TONE_MAPPER_LINEAR** = `0`

Does not modify color data, resulting in a linear tonemapping curve
which unnaturally clips bright values, causing bright lighting to look
blown out. The simplest and fastest tonemapper.

:::: {#class_RenderingServer_constant_ENV_TONE_MAPPER_REINHARD}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentToneMapper<enum_RenderingServer_EnvironmentToneMapper>`{.interpreted-text
role="ref"} **ENV_TONE_MAPPER_REINHARD** = `1`

A simple tonemapping curve that rolls off bright values to prevent
clipping. This results in an image that can appear dull and low
contrast. Slower than
`ENV_TONE_MAPPER_LINEAR<class_RenderingServer_constant_ENV_TONE_MAPPER_LINEAR>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When
`Environment.tonemap_white<class_Environment_property_tonemap_white>`{.interpreted-text
role="ref"} is left at the default value of `1.0`,
`ENV_TONE_MAPPER_REINHARD<class_RenderingServer_constant_ENV_TONE_MAPPER_REINHARD>`{.interpreted-text
role="ref"} produces an identical image to
`ENV_TONE_MAPPER_LINEAR<class_RenderingServer_constant_ENV_TONE_MAPPER_LINEAR>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_ENV_TONE_MAPPER_FILMIC}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentToneMapper<enum_RenderingServer_EnvironmentToneMapper>`{.interpreted-text
role="ref"} **ENV_TONE_MAPPER_FILMIC** = `2`

Uses a film-like tonemapping curve to prevent clipping of bright values
and provide better contrast than
`ENV_TONE_MAPPER_REINHARD<class_RenderingServer_constant_ENV_TONE_MAPPER_REINHARD>`{.interpreted-text
role="ref"}. Slightly slower than
`ENV_TONE_MAPPER_REINHARD<class_RenderingServer_constant_ENV_TONE_MAPPER_REINHARD>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_ENV_TONE_MAPPER_ACES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentToneMapper<enum_RenderingServer_EnvironmentToneMapper>`{.interpreted-text
role="ref"} **ENV_TONE_MAPPER_ACES** = `3`

Uses a high-contrast film-like tonemapping curve and desaturates bright
values for a more realistic appearance. Slightly slower than
`ENV_TONE_MAPPER_FILMIC<class_RenderingServer_constant_ENV_TONE_MAPPER_FILMIC>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This tonemapping operator is called \"ACES Fitted\" in
Godot 3.x.

:::: {#class_RenderingServer_constant_ENV_TONE_MAPPER_AGX}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentToneMapper<enum_RenderingServer_EnvironmentToneMapper>`{.interpreted-text
role="ref"} **ENV_TONE_MAPPER_AGX** = `4`

Uses a film-like tonemapping curve and desaturates bright values for a
more realistic appearance. Better than other tonemappers at maintaining
the hue of colors as they become brighter. The slowest tonemapping
option.

\*\*Note:\*\*
`Environment.tonemap_white<class_Environment_property_tonemap_white>`{.interpreted-text
role="ref"} is fixed at a value of `16.29`, which makes
`ENV_TONE_MAPPER_AGX<class_RenderingServer_constant_ENV_TONE_MAPPER_AGX>`{.interpreted-text
role="ref"} unsuitable for use with the Mobile rendering method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentSSRRoughnessQuality}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentSSRRoughnessQuality**:
`🔗<enum_RenderingServer_EnvironmentSSRRoughnessQuality>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_SSR_ROUGHNESS_QUALITY_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSRRoughnessQuality<enum_RenderingServer_EnvironmentSSRRoughnessQuality>`{.interpreted-text
role="ref"} **ENV_SSR_ROUGHNESS_QUALITY_DISABLED** = `0`

Lowest quality of roughness filter for screen-space reflections. Rough
materials will not have blurrier screen-space reflections compared to
smooth (non-rough) materials. This is the fastest option.

:::: {#class_RenderingServer_constant_ENV_SSR_ROUGHNESS_QUALITY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSRRoughnessQuality<enum_RenderingServer_EnvironmentSSRRoughnessQuality>`{.interpreted-text
role="ref"} **ENV_SSR_ROUGHNESS_QUALITY_LOW** = `1`

Low quality of roughness filter for screen-space reflections.

:::: {#class_RenderingServer_constant_ENV_SSR_ROUGHNESS_QUALITY_MEDIUM}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSRRoughnessQuality<enum_RenderingServer_EnvironmentSSRRoughnessQuality>`{.interpreted-text
role="ref"} **ENV_SSR_ROUGHNESS_QUALITY_MEDIUM** = `2`

Medium quality of roughness filter for screen-space reflections.

:::: {#class_RenderingServer_constant_ENV_SSR_ROUGHNESS_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSRRoughnessQuality<enum_RenderingServer_EnvironmentSSRRoughnessQuality>`{.interpreted-text
role="ref"} **ENV_SSR_ROUGHNESS_QUALITY_HIGH** = `3`

High quality of roughness filter for screen-space reflections. This is
the slowest option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentSSAOQuality}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentSSAOQuality**:
`🔗<enum_RenderingServer_EnvironmentSSAOQuality>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_SSAO_QUALITY_VERY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSAOQuality<enum_RenderingServer_EnvironmentSSAOQuality>`{.interpreted-text
role="ref"} **ENV_SSAO_QUALITY_VERY_LOW** = `0`

Lowest quality of screen-space ambient occlusion.

:::: {#class_RenderingServer_constant_ENV_SSAO_QUALITY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSAOQuality<enum_RenderingServer_EnvironmentSSAOQuality>`{.interpreted-text
role="ref"} **ENV_SSAO_QUALITY_LOW** = `1`

Low quality screen-space ambient occlusion.

:::: {#class_RenderingServer_constant_ENV_SSAO_QUALITY_MEDIUM}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSAOQuality<enum_RenderingServer_EnvironmentSSAOQuality>`{.interpreted-text
role="ref"} **ENV_SSAO_QUALITY_MEDIUM** = `2`

Medium quality screen-space ambient occlusion.

:::: {#class_RenderingServer_constant_ENV_SSAO_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSAOQuality<enum_RenderingServer_EnvironmentSSAOQuality>`{.interpreted-text
role="ref"} **ENV_SSAO_QUALITY_HIGH** = `3`

High quality screen-space ambient occlusion.

:::: {#class_RenderingServer_constant_ENV_SSAO_QUALITY_ULTRA}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSAOQuality<enum_RenderingServer_EnvironmentSSAOQuality>`{.interpreted-text
role="ref"} **ENV_SSAO_QUALITY_ULTRA** = `4`

Highest quality screen-space ambient occlusion. Uses the adaptive target
setting which can be dynamically adjusted to smoothly balance
performance and visual quality.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentSSILQuality}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentSSILQuality**:
`🔗<enum_RenderingServer_EnvironmentSSILQuality>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_SSIL_QUALITY_VERY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSILQuality<enum_RenderingServer_EnvironmentSSILQuality>`{.interpreted-text
role="ref"} **ENV_SSIL_QUALITY_VERY_LOW** = `0`

Lowest quality of screen-space indirect lighting.

:::: {#class_RenderingServer_constant_ENV_SSIL_QUALITY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSILQuality<enum_RenderingServer_EnvironmentSSILQuality>`{.interpreted-text
role="ref"} **ENV_SSIL_QUALITY_LOW** = `1`

Low quality screen-space indirect lighting.

:::: {#class_RenderingServer_constant_ENV_SSIL_QUALITY_MEDIUM}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSILQuality<enum_RenderingServer_EnvironmentSSILQuality>`{.interpreted-text
role="ref"} **ENV_SSIL_QUALITY_MEDIUM** = `2`

High quality screen-space indirect lighting.

:::: {#class_RenderingServer_constant_ENV_SSIL_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSILQuality<enum_RenderingServer_EnvironmentSSILQuality>`{.interpreted-text
role="ref"} **ENV_SSIL_QUALITY_HIGH** = `3`

High quality screen-space indirect lighting.

:::: {#class_RenderingServer_constant_ENV_SSIL_QUALITY_ULTRA}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSSILQuality<enum_RenderingServer_EnvironmentSSILQuality>`{.interpreted-text
role="ref"} **ENV_SSIL_QUALITY_ULTRA** = `4`

Highest quality screen-space indirect lighting. Uses the adaptive target
setting which can be dynamically adjusted to smoothly balance
performance and visual quality.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentSDFGIYScale}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentSDFGIYScale**:
`🔗<enum_RenderingServer_EnvironmentSDFGIYScale>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_SDFGI_Y_SCALE_50_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIYScale<enum_RenderingServer_EnvironmentSDFGIYScale>`{.interpreted-text
role="ref"} **ENV_SDFGI_Y_SCALE_50_PERCENT** = `0`

Use 50% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be
twice as short as they are wide. This allows providing increased GI
detail and reduced light leaking with thin floors and ceilings. This is
usually the best choice for scenes that don\'t feature much verticality.

:::: {#class_RenderingServer_constant_ENV_SDFGI_Y_SCALE_75_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIYScale<enum_RenderingServer_EnvironmentSDFGIYScale>`{.interpreted-text
role="ref"} **ENV_SDFGI_Y_SCALE_75_PERCENT** = `1`

Use 75% scale for SDFGI on the Y (vertical) axis. This is a balance
between the 50% and 100% SDFGI Y scales.

:::: {#class_RenderingServer_constant_ENV_SDFGI_Y_SCALE_100_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIYScale<enum_RenderingServer_EnvironmentSDFGIYScale>`{.interpreted-text
role="ref"} **ENV_SDFGI_Y_SCALE_100_PERCENT** = `2`

Use 100% scale for SDFGI on the Y (vertical) axis. SDFGI cells will be
as tall as they are wide. This is usually the best choice for highly
vertical scenes. The downside is that light leaking may become more
noticeable with thin floors and ceilings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentSDFGIRayCount}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentSDFGIRayCount**:
`🔗<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_4}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"} **ENV_SDFGI_RAY_COUNT_4** = `0`

Throw 4 rays per frame when converging SDFGI. This has the lowest GPU
requirements, but creates the most noisy result.

:::: {#class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_8}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"} **ENV_SDFGI_RAY_COUNT_8** = `1`

Throw 8 rays per frame when converging SDFGI.

:::: {#class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_16}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"} **ENV_SDFGI_RAY_COUNT_16** = `2`

Throw 16 rays per frame when converging SDFGI.

:::: {#class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_32}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"} **ENV_SDFGI_RAY_COUNT_32** = `3`

Throw 32 rays per frame when converging SDFGI.

:::: {#class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_64}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"} **ENV_SDFGI_RAY_COUNT_64** = `4`

Throw 64 rays per frame when converging SDFGI.

:::: {#class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_96}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"} **ENV_SDFGI_RAY_COUNT_96** = `5`

Throw 96 rays per frame when converging SDFGI. This has high GPU
requirements.

:::: {#class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_128}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"} **ENV_SDFGI_RAY_COUNT_128** = `6`

Throw 128 rays per frame when converging SDFGI. This has very high GPU
requirements, but creates the least noisy result.

:::: {#class_RenderingServer_constant_ENV_SDFGI_RAY_COUNT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"} **ENV_SDFGI_RAY_COUNT_MAX** = `7`

Represents the size of the
`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentSDFGIFramesToConverge}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentSDFGIFramesToConverge**:
`🔗<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_5_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToConverge<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"} **ENV_SDFGI_CONVERGE_IN_5_FRAMES** = `0`

Converge SDFGI over 5 frames. This is the most responsive, but creates
the most noisy result with a given ray count.

:::: {#class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_10_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToConverge<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"} **ENV_SDFGI_CONVERGE_IN_10_FRAMES** = `1`

Configure SDFGI to fully converge over 10 frames.

:::: {#class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_15_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToConverge<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"} **ENV_SDFGI_CONVERGE_IN_15_FRAMES** = `2`

Configure SDFGI to fully converge over 15 frames.

:::: {#class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_20_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToConverge<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"} **ENV_SDFGI_CONVERGE_IN_20_FRAMES** = `3`

Configure SDFGI to fully converge over 20 frames.

:::: {#class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_25_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToConverge<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"} **ENV_SDFGI_CONVERGE_IN_25_FRAMES** = `4`

Configure SDFGI to fully converge over 25 frames.

:::: {#class_RenderingServer_constant_ENV_SDFGI_CONVERGE_IN_30_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToConverge<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"} **ENV_SDFGI_CONVERGE_IN_30_FRAMES** = `5`

Configure SDFGI to fully converge over 30 frames. This is the least
responsive, but creates the least noisy result with a given ray count.

:::: {#class_RenderingServer_constant_ENV_SDFGI_CONVERGE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToConverge<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"} **ENV_SDFGI_CONVERGE_MAX** = `6`

Represents the size of the
`EnvironmentSDFGIFramesToConverge<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentSDFGIFramesToUpdateLight**:
`🔗<enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_1_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToUpdateLight<enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight>`{.interpreted-text
role="ref"} **ENV_SDFGI_UPDATE_LIGHT_IN_1_FRAME** = `0`

Update indirect light from dynamic lights in SDFGI over 1 frame. This is
the most responsive, but has the highest GPU requirements.

:::: {#class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_2_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToUpdateLight<enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight>`{.interpreted-text
role="ref"} **ENV_SDFGI_UPDATE_LIGHT_IN_2_FRAMES** = `1`

Update indirect light from dynamic lights in SDFGI over 2 frames.

:::: {#class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_4_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToUpdateLight<enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight>`{.interpreted-text
role="ref"} **ENV_SDFGI_UPDATE_LIGHT_IN_4_FRAMES** = `2`

Update indirect light from dynamic lights in SDFGI over 4 frames.

:::: {#class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_8_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToUpdateLight<enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight>`{.interpreted-text
role="ref"} **ENV_SDFGI_UPDATE_LIGHT_IN_8_FRAMES** = `3`

Update indirect light from dynamic lights in SDFGI over 8 frames.

:::: {#class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_IN_16_FRAMES}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToUpdateLight<enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight>`{.interpreted-text
role="ref"} **ENV_SDFGI_UPDATE_LIGHT_IN_16_FRAMES** = `4`

Update indirect light from dynamic lights in SDFGI over 16 frames. This
is the least responsive, but has the lowest GPU requirements.

:::: {#class_RenderingServer_constant_ENV_SDFGI_UPDATE_LIGHT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentSDFGIFramesToUpdateLight<enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight>`{.interpreted-text
role="ref"} **ENV_SDFGI_UPDATE_LIGHT_MAX** = `5`

Represents the size of the
`EnvironmentSDFGIFramesToUpdateLight<enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_SubSurfaceScatteringQuality}
::: rst-class
classref-enumeration
:::
::::

enum **SubSurfaceScatteringQuality**:
`🔗<enum_RenderingServer_SubSurfaceScatteringQuality>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_SUB_SURFACE_SCATTERING_QUALITY_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`SubSurfaceScatteringQuality<enum_RenderingServer_SubSurfaceScatteringQuality>`{.interpreted-text
role="ref"} **SUB_SURFACE_SCATTERING_QUALITY_DISABLED** = `0`

Disables subsurface scattering entirely, even on materials that have
`BaseMaterial3D.subsurf_scatter_enabled<class_BaseMaterial3D_property_subsurf_scatter_enabled>`{.interpreted-text
role="ref"} set to `true`. This has the lowest GPU requirements.

:::: {#class_RenderingServer_constant_SUB_SURFACE_SCATTERING_QUALITY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`SubSurfaceScatteringQuality<enum_RenderingServer_SubSurfaceScatteringQuality>`{.interpreted-text
role="ref"} **SUB_SURFACE_SCATTERING_QUALITY_LOW** = `1`

Low subsurface scattering quality.

:::: {#class_RenderingServer_constant_SUB_SURFACE_SCATTERING_QUALITY_MEDIUM}
::: rst-class
classref-enumeration-constant
:::
::::

`SubSurfaceScatteringQuality<enum_RenderingServer_SubSurfaceScatteringQuality>`{.interpreted-text
role="ref"} **SUB_SURFACE_SCATTERING_QUALITY_MEDIUM** = `2`

Medium subsurface scattering quality.

:::: {#class_RenderingServer_constant_SUB_SURFACE_SCATTERING_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`SubSurfaceScatteringQuality<enum_RenderingServer_SubSurfaceScatteringQuality>`{.interpreted-text
role="ref"} **SUB_SURFACE_SCATTERING_QUALITY_HIGH** = `3`

High subsurface scattering quality. This has the highest GPU
requirements.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_DOFBokehShape}
::: rst-class
classref-enumeration
:::
::::

enum **DOFBokehShape**:
`🔗<enum_RenderingServer_DOFBokehShape>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_DOF_BOKEH_BOX}
::: rst-class
classref-enumeration-constant
:::
::::

`DOFBokehShape<enum_RenderingServer_DOFBokehShape>`{.interpreted-text
role="ref"} **DOF_BOKEH_BOX** = `0`

Calculate the DOF blur using a box filter. The fastest option, but
results in obvious lines in blur pattern.

:::: {#class_RenderingServer_constant_DOF_BOKEH_HEXAGON}
::: rst-class
classref-enumeration-constant
:::
::::

`DOFBokehShape<enum_RenderingServer_DOFBokehShape>`{.interpreted-text
role="ref"} **DOF_BOKEH_HEXAGON** = `1`

Calculates DOF blur using a hexagon shaped filter.

:::: {#class_RenderingServer_constant_DOF_BOKEH_CIRCLE}
::: rst-class
classref-enumeration-constant
:::
::::

`DOFBokehShape<enum_RenderingServer_DOFBokehShape>`{.interpreted-text
role="ref"} **DOF_BOKEH_CIRCLE** = `2`

Calculates DOF blur using a circle shaped filter. Best quality and most
realistic, but slowest. Use only for areas where a lot of performance
can be dedicated to post-processing (e.g. cutscenes).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_DOFBlurQuality}
::: rst-class
classref-enumeration
:::
::::

enum **DOFBlurQuality**:
`🔗<enum_RenderingServer_DOFBlurQuality>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_DOF_BLUR_QUALITY_VERY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`DOFBlurQuality<enum_RenderingServer_DOFBlurQuality>`{.interpreted-text
role="ref"} **DOF_BLUR_QUALITY_VERY_LOW** = `0`

Lowest quality DOF blur. This is the fastest setting, but you may be
able to see filtering artifacts.

:::: {#class_RenderingServer_constant_DOF_BLUR_QUALITY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`DOFBlurQuality<enum_RenderingServer_DOFBlurQuality>`{.interpreted-text
role="ref"} **DOF_BLUR_QUALITY_LOW** = `1`

Low quality DOF blur.

:::: {#class_RenderingServer_constant_DOF_BLUR_QUALITY_MEDIUM}
::: rst-class
classref-enumeration-constant
:::
::::

`DOFBlurQuality<enum_RenderingServer_DOFBlurQuality>`{.interpreted-text
role="ref"} **DOF_BLUR_QUALITY_MEDIUM** = `2`

Medium quality DOF blur.

:::: {#class_RenderingServer_constant_DOF_BLUR_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`DOFBlurQuality<enum_RenderingServer_DOFBlurQuality>`{.interpreted-text
role="ref"} **DOF_BLUR_QUALITY_HIGH** = `3`

Highest quality DOF blur. Results in the smoothest looking blur by
taking the most samples, but is also significantly slower.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_InstanceType}
::: rst-class
classref-enumeration
:::
::::

enum **InstanceType**:
`🔗<enum_RenderingServer_InstanceType>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_INSTANCE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_NONE** = `0`

The instance does not have a type.

:::: {#class_RenderingServer_constant_INSTANCE_MESH}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_MESH** = `1`

The instance is a mesh.

:::: {#class_RenderingServer_constant_INSTANCE_MULTIMESH}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_MULTIMESH** = `2`

The instance is a multimesh.

:::: {#class_RenderingServer_constant_INSTANCE_PARTICLES}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_PARTICLES** = `3`

The instance is a particle emitter.

:::: {#class_RenderingServer_constant_INSTANCE_PARTICLES_COLLISION}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_PARTICLES_COLLISION** = `4`

The instance is a GPUParticles collision shape.

:::: {#class_RenderingServer_constant_INSTANCE_LIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_LIGHT** = `5`

The instance is a light.

:::: {#class_RenderingServer_constant_INSTANCE_REFLECTION_PROBE}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_REFLECTION_PROBE** = `6`

The instance is a reflection probe.

:::: {#class_RenderingServer_constant_INSTANCE_DECAL}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_DECAL** = `7`

The instance is a decal.

:::: {#class_RenderingServer_constant_INSTANCE_VOXEL_GI}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_VOXEL_GI** = `8`

The instance is a VoxelGI.

:::: {#class_RenderingServer_constant_INSTANCE_LIGHTMAP}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_LIGHTMAP** = `9`

The instance is a lightmap.

:::: {#class_RenderingServer_constant_INSTANCE_OCCLUDER}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_OCCLUDER** = `10`

The instance is an occlusion culling occluder.

:::: {#class_RenderingServer_constant_INSTANCE_VISIBLITY_NOTIFIER}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_VISIBLITY_NOTIFIER** = `11`

The instance is a visible on-screen notifier.

:::: {#class_RenderingServer_constant_INSTANCE_FOG_VOLUME}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_FOG_VOLUME** = `12`

The instance is a fog volume.

:::: {#class_RenderingServer_constant_INSTANCE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_MAX** = `13`

Represents the size of the
`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} enum.

:::: {#class_RenderingServer_constant_INSTANCE_GEOMETRY_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceType<enum_RenderingServer_InstanceType>`{.interpreted-text
role="ref"} **INSTANCE_GEOMETRY_MASK** = `14`

A combination of the flags of geometry instances (mesh, multimesh,
immediate and particles).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_InstanceFlags}
::: rst-class
classref-enumeration
:::
::::

enum **InstanceFlags**:
`🔗<enum_RenderingServer_InstanceFlags>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_INSTANCE_FLAG_USE_BAKED_LIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceFlags<enum_RenderingServer_InstanceFlags>`{.interpreted-text
role="ref"} **INSTANCE_FLAG_USE_BAKED_LIGHT** = `0`

Allows the instance to be used in baked lighting.

:::: {#class_RenderingServer_constant_INSTANCE_FLAG_USE_DYNAMIC_GI}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceFlags<enum_RenderingServer_InstanceFlags>`{.interpreted-text
role="ref"} **INSTANCE_FLAG_USE_DYNAMIC_GI** = `1`

Allows the instance to be used with dynamic global illumination.

:::: {#class_RenderingServer_constant_INSTANCE_FLAG_DRAW_NEXT_FRAME_IF_VISIBLE}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceFlags<enum_RenderingServer_InstanceFlags>`{.interpreted-text
role="ref"} **INSTANCE_FLAG_DRAW_NEXT_FRAME_IF_VISIBLE** = `2`

When set, manually requests to draw geometry on next frame.

:::: {#class_RenderingServer_constant_INSTANCE_FLAG_IGNORE_OCCLUSION_CULLING}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceFlags<enum_RenderingServer_InstanceFlags>`{.interpreted-text
role="ref"} **INSTANCE_FLAG_IGNORE_OCCLUSION_CULLING** = `3`

Always draw, even if the instance would be culled by occlusion culling.
Does not affect view frustum culling.

:::: {#class_RenderingServer_constant_INSTANCE_FLAG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`InstanceFlags<enum_RenderingServer_InstanceFlags>`{.interpreted-text
role="ref"} **INSTANCE_FLAG_MAX** = `4`

Represents the size of the
`InstanceFlags<enum_RenderingServer_InstanceFlags>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_ShadowCastingSetting}
::: rst-class
classref-enumeration
:::
::::

enum **ShadowCastingSetting**:
`🔗<enum_RenderingServer_ShadowCastingSetting>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_SHADOW_CASTING_SETTING_OFF}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>`{.interpreted-text
role="ref"} **SHADOW_CASTING_SETTING_OFF** = `0`

Disable shadows from this instance.

:::: {#class_RenderingServer_constant_SHADOW_CASTING_SETTING_ON}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>`{.interpreted-text
role="ref"} **SHADOW_CASTING_SETTING_ON** = `1`

Cast shadows from this instance.

:::: {#class_RenderingServer_constant_SHADOW_CASTING_SETTING_DOUBLE_SIDED}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>`{.interpreted-text
role="ref"} **SHADOW_CASTING_SETTING_DOUBLE_SIDED** = `2`

Disable backface culling when rendering the shadow of the object. This
is slightly slower but may result in more correct shadows.

:::: {#class_RenderingServer_constant_SHADOW_CASTING_SETTING_SHADOWS_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>`{.interpreted-text
role="ref"} **SHADOW_CASTING_SETTING_SHADOWS_ONLY** = `3`

Only render the shadows from the object. The object itself will not be
drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_VisibilityRangeFadeMode}
::: rst-class
classref-enumeration
:::
::::

enum **VisibilityRangeFadeMode**:
`🔗<enum_RenderingServer_VisibilityRangeFadeMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_VISIBILITY_RANGE_FADE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityRangeFadeMode<enum_RenderingServer_VisibilityRangeFadeMode>`{.interpreted-text
role="ref"} **VISIBILITY_RANGE_FADE_DISABLED** = `0`

Disable visibility range fading for the given instance.

:::: {#class_RenderingServer_constant_VISIBILITY_RANGE_FADE_SELF}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityRangeFadeMode<enum_RenderingServer_VisibilityRangeFadeMode>`{.interpreted-text
role="ref"} **VISIBILITY_RANGE_FADE_SELF** = `1`

Fade-out the given instance when it approaches its visibility range
limits.

:::: {#class_RenderingServer_constant_VISIBILITY_RANGE_FADE_DEPENDENCIES}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityRangeFadeMode<enum_RenderingServer_VisibilityRangeFadeMode>`{.interpreted-text
role="ref"} **VISIBILITY_RANGE_FADE_DEPENDENCIES** = `2`

Fade-in the given instance\'s dependencies when reaching its visibility
range limits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_BakeChannels}
::: rst-class
classref-enumeration
:::
::::

enum **BakeChannels**:
`🔗<enum_RenderingServer_BakeChannels>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_BAKE_CHANNEL_ALBEDO_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeChannels<enum_RenderingServer_BakeChannels>`{.interpreted-text
role="ref"} **BAKE_CHANNEL_ALBEDO_ALPHA** = `0`

Index of `Image<class_Image>`{.interpreted-text role="ref"} in array of
`Image<class_Image>`{.interpreted-text role="ref"}s returned by
`bake_render_uv2()<class_RenderingServer_method_bake_render_uv2>`{.interpreted-text
role="ref"}. Image uses
`Image.FORMAT_RGBA8<class_Image_constant_FORMAT_RGBA8>`{.interpreted-text
role="ref"} and contains albedo color in the `.rgb` channels and alpha
in the `.a` channel.

:::: {#class_RenderingServer_constant_BAKE_CHANNEL_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeChannels<enum_RenderingServer_BakeChannels>`{.interpreted-text
role="ref"} **BAKE_CHANNEL_NORMAL** = `1`

Index of `Image<class_Image>`{.interpreted-text role="ref"} in array of
`Image<class_Image>`{.interpreted-text role="ref"}s returned by
`bake_render_uv2()<class_RenderingServer_method_bake_render_uv2>`{.interpreted-text
role="ref"}. Image uses
`Image.FORMAT_RGBA8<class_Image_constant_FORMAT_RGBA8>`{.interpreted-text
role="ref"} and contains the per-pixel normal of the object in the
`.rgb` channels and nothing in the `.a` channel. The per-pixel normal is
encoded as `normal * 0.5 + 0.5`.

:::: {#class_RenderingServer_constant_BAKE_CHANNEL_ORM}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeChannels<enum_RenderingServer_BakeChannels>`{.interpreted-text
role="ref"} **BAKE_CHANNEL_ORM** = `2`

Index of `Image<class_Image>`{.interpreted-text role="ref"} in array of
`Image<class_Image>`{.interpreted-text role="ref"}s returned by
`bake_render_uv2()<class_RenderingServer_method_bake_render_uv2>`{.interpreted-text
role="ref"}. Image uses
`Image.FORMAT_RGBA8<class_Image_constant_FORMAT_RGBA8>`{.interpreted-text
role="ref"} and contains ambient occlusion (from material and decals
only) in the `.r` channel, roughness in the `.g` channel, metallic in
the `.b` channel and sub surface scattering amount in the `.a` channel.

:::: {#class_RenderingServer_constant_BAKE_CHANNEL_EMISSION}
::: rst-class
classref-enumeration-constant
:::
::::

`BakeChannels<enum_RenderingServer_BakeChannels>`{.interpreted-text
role="ref"} **BAKE_CHANNEL_EMISSION** = `3`

Index of `Image<class_Image>`{.interpreted-text role="ref"} in array of
`Image<class_Image>`{.interpreted-text role="ref"}s returned by
`bake_render_uv2()<class_RenderingServer_method_bake_render_uv2>`{.interpreted-text
role="ref"}. Image uses
`Image.FORMAT_RGBAH<class_Image_constant_FORMAT_RGBAH>`{.interpreted-text
role="ref"} and contains emission color in the `.rgb` channels and
nothing in the `.a` channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CanvasTextureChannel}
::: rst-class
classref-enumeration
:::
::::

enum **CanvasTextureChannel**:
`🔗<enum_RenderingServer_CanvasTextureChannel>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_CANVAS_TEXTURE_CHANNEL_DIFFUSE}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasTextureChannel<enum_RenderingServer_CanvasTextureChannel>`{.interpreted-text
role="ref"} **CANVAS_TEXTURE_CHANNEL_DIFFUSE** = `0`

Diffuse canvas texture
(`CanvasTexture.diffuse_texture<class_CanvasTexture_property_diffuse_texture>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_CANVAS_TEXTURE_CHANNEL_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasTextureChannel<enum_RenderingServer_CanvasTextureChannel>`{.interpreted-text
role="ref"} **CANVAS_TEXTURE_CHANNEL_NORMAL** = `1`

Normal map canvas texture
(`CanvasTexture.normal_texture<class_CanvasTexture_property_normal_texture>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_CANVAS_TEXTURE_CHANNEL_SPECULAR}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasTextureChannel<enum_RenderingServer_CanvasTextureChannel>`{.interpreted-text
role="ref"} **CANVAS_TEXTURE_CHANNEL_SPECULAR** = `2`

Specular map canvas texture
(`CanvasTexture.specular_texture<class_CanvasTexture_property_specular_texture>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_NinePatchAxisMode}
::: rst-class
classref-enumeration
:::
::::

enum **NinePatchAxisMode**:
`🔗<enum_RenderingServer_NinePatchAxisMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_NINE_PATCH_STRETCH}
::: rst-class
classref-enumeration-constant
:::
::::

`NinePatchAxisMode<enum_RenderingServer_NinePatchAxisMode>`{.interpreted-text
role="ref"} **NINE_PATCH_STRETCH** = `0`

The nine patch gets stretched where needed.

:::: {#class_RenderingServer_constant_NINE_PATCH_TILE}
::: rst-class
classref-enumeration-constant
:::
::::

`NinePatchAxisMode<enum_RenderingServer_NinePatchAxisMode>`{.interpreted-text
role="ref"} **NINE_PATCH_TILE** = `1`

The nine patch gets filled with tiles where needed.

:::: {#class_RenderingServer_constant_NINE_PATCH_TILE_FIT}
::: rst-class
classref-enumeration-constant
:::
::::

`NinePatchAxisMode<enum_RenderingServer_NinePatchAxisMode>`{.interpreted-text
role="ref"} **NINE_PATCH_TILE_FIT** = `2`

The nine patch gets filled with tiles where needed and stretches them a
bit if needed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CanvasItemTextureFilter}
::: rst-class
classref-enumeration
:::
::::

enum **CanvasItemTextureFilter**:
`🔗<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_FILTER_DEFAULT** = `0`

Uses the default filter mode for this
`Viewport<class_Viewport>`{.interpreted-text role="ref"}.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_FILTER_NEAREST** = `1`

The texture filter reads from the nearest pixel only. This makes the
texture look pixelated from up close, and grainy from a distance (due to
mipmaps not being sampled).

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_FILTER_LINEAR** = `2`

The texture filter blends between the nearest 4 pixels. This makes the
texture look smooth from up close, and grainy from a distance (due to
mipmaps not being sampled).

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS** = `3`

The texture filter reads from the nearest pixel and blends between the
nearest 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`). This makes the texture look pixelated from up
close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale
(e.g. due to `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
zoom or sprite scaling), as mipmaps are important to smooth out pixels
that are smaller than on-screen pixels.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS** = `4`

The texture filter blends between the nearest 4 pixels and between the
nearest 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`). This makes the texture look smooth from up
close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale
(e.g. due to `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
zoom or sprite scaling), as mipmaps are important to smooth out pixels
that are smaller than on-screen pixels.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"}
**CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC** = `5`

The texture filter reads from the nearest pixel and blends between 2
mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`) based on the angle between the surface and the
camera view. This makes the texture look pixelated from up close, and
smooth from a distance. Anisotropic filtering improves texture quality
on surfaces that are almost in line with the camera, but is slightly
slower. The anisotropic filtering level can be changed by adjusting
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This texture filter is rarely useful in 2D projects.
`CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS<class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS>`{.interpreted-text
role="ref"} is usually more appropriate in this case.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"}
**CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC** = `6`

The texture filter blends between the nearest 4 pixels and blends
between 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`) based on the angle between the surface and the
camera view. This makes the texture look smooth from up close, and
smooth from a distance. Anisotropic filtering improves texture quality
on surfaces that are almost in line with the camera, but is slightly
slower. The anisotropic filtering level can be changed by adjusting
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This texture filter is rarely useful in 2D projects.
`CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS<class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS>`{.interpreted-text
role="ref"} is usually more appropriate in this case.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_FILTER_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_FILTER_MAX** = `7`

Max value for
`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CanvasItemTextureRepeat}
::: rst-class
classref-enumeration
:::
::::

enum **CanvasItemTextureRepeat**:
`🔗<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureRepeat<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_REPEAT_DEFAULT** = `0`

Uses the default repeat mode for this
`Viewport<class_Viewport>`{.interpreted-text role="ref"}.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureRepeat<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_REPEAT_DISABLED** = `1`

Disables textures repeating. Instead, when reading UVs outside the 0-1
range, the value will be clamped to the edge of the texture, resulting
in a stretched out look at the borders of the texture.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureRepeat<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_REPEAT_ENABLED** = `2`

Enables the texture to repeat when UV coordinates are outside the 0-1
range. If using one of the linear filtering modes, this can result in
artifacts at the edges of a texture when the sampler filters across the
edges of the texture.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_MIRROR}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureRepeat<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_REPEAT_MIRROR** = `3`

Flip the texture when repeating so that the edge lines up instead of
abruptly changing.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_TEXTURE_REPEAT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasItemTextureRepeat<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **CANVAS_ITEM_TEXTURE_REPEAT_MAX** = `4`

Max value for
`CanvasItemTextureRepeat<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CanvasGroupMode}
::: rst-class
classref-enumeration
:::
::::

enum **CanvasGroupMode**:
`🔗<enum_RenderingServer_CanvasGroupMode>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_CANVAS_GROUP_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasGroupMode<enum_RenderingServer_CanvasGroupMode>`{.interpreted-text
role="ref"} **CANVAS_GROUP_MODE_DISABLED** = `0`

Child draws over parent and is not clipped.

:::: {#class_RenderingServer_constant_CANVAS_GROUP_MODE_CLIP_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasGroupMode<enum_RenderingServer_CanvasGroupMode>`{.interpreted-text
role="ref"} **CANVAS_GROUP_MODE_CLIP_ONLY** = `1`

Parent is used for the purposes of clipping only. Child is clipped to
the parent\'s visible area, parent is not drawn.

:::: {#class_RenderingServer_constant_CANVAS_GROUP_MODE_CLIP_AND_DRAW}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasGroupMode<enum_RenderingServer_CanvasGroupMode>`{.interpreted-text
role="ref"} **CANVAS_GROUP_MODE_CLIP_AND_DRAW** = `2`

Parent is used for clipping child, but parent is also drawn underneath
child as normal before clipping child to its visible area.

:::: {#class_RenderingServer_constant_CANVAS_GROUP_MODE_TRANSPARENT}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasGroupMode<enum_RenderingServer_CanvasGroupMode>`{.interpreted-text
role="ref"} **CANVAS_GROUP_MODE_TRANSPARENT** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CanvasLightMode}
::: rst-class
classref-enumeration
:::
::::

enum **CanvasLightMode**:
`🔗<enum_RenderingServer_CanvasLightMode>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_CANVAS_LIGHT_MODE_POINT}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasLightMode<enum_RenderingServer_CanvasLightMode>`{.interpreted-text
role="ref"} **CANVAS_LIGHT_MODE_POINT** = `0`

2D point light (see `PointLight2D<class_PointLight2D>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_CANVAS_LIGHT_MODE_DIRECTIONAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasLightMode<enum_RenderingServer_CanvasLightMode>`{.interpreted-text
role="ref"} **CANVAS_LIGHT_MODE_DIRECTIONAL** = `1`

2D directional (sun/moon) light (see
`DirectionalLight2D<class_DirectionalLight2D>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CanvasLightBlendMode}
::: rst-class
classref-enumeration
:::
::::

enum **CanvasLightBlendMode**:
`🔗<enum_RenderingServer_CanvasLightBlendMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_CANVAS_LIGHT_BLEND_MODE_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasLightBlendMode<enum_RenderingServer_CanvasLightBlendMode>`{.interpreted-text
role="ref"} **CANVAS_LIGHT_BLEND_MODE_ADD** = `0`

Adds light color additive to the canvas.

:::: {#class_RenderingServer_constant_CANVAS_LIGHT_BLEND_MODE_SUB}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasLightBlendMode<enum_RenderingServer_CanvasLightBlendMode>`{.interpreted-text
role="ref"} **CANVAS_LIGHT_BLEND_MODE_SUB** = `1`

Adds light color subtractive to the canvas.

:::: {#class_RenderingServer_constant_CANVAS_LIGHT_BLEND_MODE_MIX}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasLightBlendMode<enum_RenderingServer_CanvasLightBlendMode>`{.interpreted-text
role="ref"} **CANVAS_LIGHT_BLEND_MODE_MIX** = `2`

The light adds color depending on transparency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CanvasLightShadowFilter}
::: rst-class
classref-enumeration
:::
::::

enum **CanvasLightShadowFilter**:
`🔗<enum_RenderingServer_CanvasLightShadowFilter>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_CANVAS_LIGHT_FILTER_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasLightShadowFilter<enum_RenderingServer_CanvasLightShadowFilter>`{.interpreted-text
role="ref"} **CANVAS_LIGHT_FILTER_NONE** = `0`

Do not apply a filter to canvas light shadows.

:::: {#class_RenderingServer_constant_CANVAS_LIGHT_FILTER_PCF5}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasLightShadowFilter<enum_RenderingServer_CanvasLightShadowFilter>`{.interpreted-text
role="ref"} **CANVAS_LIGHT_FILTER_PCF5** = `1`

Use PCF5 filtering to filter canvas light shadows.

:::: {#class_RenderingServer_constant_CANVAS_LIGHT_FILTER_PCF13}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasLightShadowFilter<enum_RenderingServer_CanvasLightShadowFilter>`{.interpreted-text
role="ref"} **CANVAS_LIGHT_FILTER_PCF13** = `2`

Use PCF13 filtering to filter canvas light shadows.

:::: {#class_RenderingServer_constant_CANVAS_LIGHT_FILTER_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasLightShadowFilter<enum_RenderingServer_CanvasLightShadowFilter>`{.interpreted-text
role="ref"} **CANVAS_LIGHT_FILTER_MAX** = `3`

Max value of the
`CanvasLightShadowFilter<enum_RenderingServer_CanvasLightShadowFilter>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_CanvasOccluderPolygonCullMode}
::: rst-class
classref-enumeration
:::
::::

enum **CanvasOccluderPolygonCullMode**:
`🔗<enum_RenderingServer_CanvasOccluderPolygonCullMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_CANVAS_OCCLUDER_POLYGON_CULL_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasOccluderPolygonCullMode<enum_RenderingServer_CanvasOccluderPolygonCullMode>`{.interpreted-text
role="ref"} **CANVAS_OCCLUDER_POLYGON_CULL_DISABLED** = `0`

Culling of the canvas occluder is disabled.

:::: {#class_RenderingServer_constant_CANVAS_OCCLUDER_POLYGON_CULL_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasOccluderPolygonCullMode<enum_RenderingServer_CanvasOccluderPolygonCullMode>`{.interpreted-text
role="ref"} **CANVAS_OCCLUDER_POLYGON_CULL_CLOCKWISE** = `1`

Culling of the canvas occluder is clockwise.

:::: {#class_RenderingServer_constant_CANVAS_OCCLUDER_POLYGON_CULL_COUNTER_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`CanvasOccluderPolygonCullMode<enum_RenderingServer_CanvasOccluderPolygonCullMode>`{.interpreted-text
role="ref"} **CANVAS_OCCLUDER_POLYGON_CULL_COUNTER_CLOCKWISE** = `2`

Culling of the canvas occluder is counterclockwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_GlobalShaderParameterType}
::: rst-class
classref-enumeration
:::
::::

enum **GlobalShaderParameterType**:
`🔗<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_BOOL}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_BOOL** = `0`

Boolean global shader parameter (`global uniform bool ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_BVEC2}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_BVEC2** = `1`

2-dimensional boolean vector global shader parameter
(`global uniform bvec2 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_BVEC3}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_BVEC3** = `2`

3-dimensional boolean vector global shader parameter
(`global uniform bvec3 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_BVEC4}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_BVEC4** = `3`

4-dimensional boolean vector global shader parameter
(`global uniform bvec4 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_INT}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_INT** = `4`

Integer global shader parameter (`global uniform int ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_IVEC2}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_IVEC2** = `5`

2-dimensional integer vector global shader parameter
(`global uniform ivec2 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_IVEC3}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_IVEC3** = `6`

3-dimensional integer vector global shader parameter
(`global uniform ivec3 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_IVEC4}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_IVEC4** = `7`

4-dimensional integer vector global shader parameter
(`global uniform ivec4 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_RECT2I}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_RECT2I** = `8`

2-dimensional integer rectangle global shader parameter
(`global uniform ivec4 ...`). Equivalent to
`GLOBAL_VAR_TYPE_IVEC4<class_RenderingServer_constant_GLOBAL_VAR_TYPE_IVEC4>`{.interpreted-text
role="ref"} in shader code, but exposed as a
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} in the editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_UINT** = `9`

Unsigned integer global shader parameter (`global uniform uint ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_UVEC2}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_UVEC2** = `10`

2-dimensional unsigned integer vector global shader parameter
(`global uniform uvec2 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_UVEC3}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_UVEC3** = `11`

3-dimensional unsigned integer vector global shader parameter
(`global uniform uvec3 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_UVEC4}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_UVEC4** = `12`

4-dimensional unsigned integer vector global shader parameter
(`global uniform uvec4 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_FLOAT** = `13`

Single-precision floating-point global shader parameter
(`global uniform float ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC2}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_VEC2** = `14`

2-dimensional floating-point vector global shader parameter
(`global uniform vec2 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC3}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_VEC3** = `15`

3-dimensional floating-point vector global shader parameter
(`global uniform vec3 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC4}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_VEC4** = `16`

4-dimensional floating-point vector global shader parameter
(`global uniform vec4 ...`).

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_COLOR** = `17`

Color global shader parameter (`global uniform vec4 ...`). Equivalent to
`GLOBAL_VAR_TYPE_VEC4<class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC4>`{.interpreted-text
role="ref"} in shader code, but exposed as a
`Color<class_Color>`{.interpreted-text role="ref"} in the editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_RECT2}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_RECT2** = `18`

2-dimensional floating-point rectangle global shader parameter
(`global uniform vec4 ...`). Equivalent to
`GLOBAL_VAR_TYPE_VEC4<class_RenderingServer_constant_GLOBAL_VAR_TYPE_VEC4>`{.interpreted-text
role="ref"} in shader code, but exposed as a
`Rect2<class_Rect2>`{.interpreted-text role="ref"} in the editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_MAT2}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_MAT2** = `19`

2×2 matrix global shader parameter (`global uniform mat2 ...`). Exposed
as a `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"} in the editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_MAT3}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_MAT3** = `20`

3×3 matrix global shader parameter (`global uniform mat3 ...`). Exposed
as a `Basis<class_Basis>`{.interpreted-text role="ref"} in the editor
UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_MAT4}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_MAT4** = `21`

4×4 matrix global shader parameter (`global uniform mat4 ...`). Exposed
as a `Projection<class_Projection>`{.interpreted-text role="ref"} in the
editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_TRANSFORM_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_TRANSFORM_2D** = `22`

2-dimensional transform global shader parameter
(`global uniform mat2x3 ...`). Exposed as a
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"} in the
editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_TRANSFORM}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_TRANSFORM** = `23`

3-dimensional transform global shader parameter
(`global uniform mat3x4 ...`). Exposed as a
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} in the
editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLER2D}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_SAMPLER2D** = `24`

2D sampler global shader parameter (`global uniform sampler2D ...`).
Exposed as a `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
in the editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLER2DARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_SAMPLER2DARRAY** = `25`

2D sampler array global shader parameter
(`global uniform sampler2DArray ...`). Exposed as a
`Texture2DArray<class_Texture2DArray>`{.interpreted-text role="ref"} in
the editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLER3D}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_SAMPLER3D** = `26`

3D sampler global shader parameter (`global uniform sampler3D ...`).
Exposed as a `Texture3D<class_Texture3D>`{.interpreted-text role="ref"}
in the editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLERCUBE}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_SAMPLERCUBE** = `27`

Cubemap sampler global shader parameter
(`global uniform samplerCube ...`). Exposed as a
`Cubemap<class_Cubemap>`{.interpreted-text role="ref"} in the editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_SAMPLEREXT}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_SAMPLEREXT** = `28`

External sampler global shader parameter
(`global uniform samplerExternalOES ...`). Exposed as an
`ExternalTexture<class_ExternalTexture>`{.interpreted-text role="ref"}
in the editor UI.

:::: {#class_RenderingServer_constant_GLOBAL_VAR_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **GLOBAL_VAR_TYPE_MAX** = `29`

Represents the size of the
`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_RenderingInfo}
::: rst-class
classref-enumeration
:::
::::

enum **RenderingInfo**:
`🔗<enum_RenderingServer_RenderingInfo>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_RENDERING_INFO_TOTAL_OBJECTS_IN_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_TOTAL_OBJECTS_IN_FRAME** = `0`

Number of objects rendered in the current 3D scene. This varies
depending on camera position and rotation.

:::: {#class_RenderingServer_constant_RENDERING_INFO_TOTAL_PRIMITIVES_IN_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_TOTAL_PRIMITIVES_IN_FRAME** = `1`

Number of points, lines, or triangles rendered in the current 3D scene.
This varies depending on camera position and rotation.

:::: {#class_RenderingServer_constant_RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME** = `2`

Number of draw calls performed to render in the current 3D scene. This
varies depending on camera position and rotation.

:::: {#class_RenderingServer_constant_RENDERING_INFO_TEXTURE_MEM_USED}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_TEXTURE_MEM_USED** = `3`

Texture memory used (in bytes).

:::: {#class_RenderingServer_constant_RENDERING_INFO_BUFFER_MEM_USED}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_BUFFER_MEM_USED** = `4`

Buffer memory used (in bytes). This includes vertex data, uniform
buffers, and many miscellaneous buffer types used internally.

:::: {#class_RenderingServer_constant_RENDERING_INFO_VIDEO_MEM_USED}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_VIDEO_MEM_USED** = `5`

Video memory used (in bytes). When using the Forward+ or Mobile
renderers, this is always greater than the sum of
`RENDERING_INFO_TEXTURE_MEM_USED<class_RenderingServer_constant_RENDERING_INFO_TEXTURE_MEM_USED>`{.interpreted-text
role="ref"} and
`RENDERING_INFO_BUFFER_MEM_USED<class_RenderingServer_constant_RENDERING_INFO_BUFFER_MEM_USED>`{.interpreted-text
role="ref"}, since there is miscellaneous data not accounted for by
those two metrics. When using the Compatibility renderer, this is equal
to the sum of
`RENDERING_INFO_TEXTURE_MEM_USED<class_RenderingServer_constant_RENDERING_INFO_TEXTURE_MEM_USED>`{.interpreted-text
role="ref"} and
`RENDERING_INFO_BUFFER_MEM_USED<class_RenderingServer_constant_RENDERING_INFO_BUFFER_MEM_USED>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_CANVAS}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_PIPELINE_COMPILATIONS_CANVAS** = `6`

Number of pipeline compilations that were triggered by the 2D canvas
renderer.

:::: {#class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_MESH}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_PIPELINE_COMPILATIONS_MESH** = `7`

Number of pipeline compilations that were triggered by loading meshes.
These compilations will show up as longer loading times the first time a
user runs the game and the pipeline is required.

:::: {#class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_SURFACE}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_PIPELINE_COMPILATIONS_SURFACE** = `8`

Number of pipeline compilations that were triggered by building the
surface cache before rendering the scene. These compilations will show
up as a stutter when loading a scene the first time a user runs the game
and the pipeline is required.

:::: {#class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_DRAW}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_PIPELINE_COMPILATIONS_DRAW** = `9`

Number of pipeline compilations that were triggered while drawing the
scene. These compilations will show up as stutters during gameplay the
first time a user runs the game and the pipeline is required.

:::: {#class_RenderingServer_constant_RENDERING_INFO_PIPELINE_COMPILATIONS_SPECIALIZATION}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"} **RENDERING_INFO_PIPELINE_COMPILATIONS_SPECIALIZATION** =
`10`

Number of pipeline compilations that were triggered to optimize the
current scene. These compilations are done in the background and should
not cause any stutters whatsoever.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_PipelineSource}
::: rst-class
classref-enumeration
:::
::::

enum **PipelineSource**:
`🔗<enum_RenderingServer_PipelineSource>`{.interpreted-text role="ref"}

:::: {#class_RenderingServer_constant_PIPELINE_SOURCE_CANVAS}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineSource<enum_RenderingServer_PipelineSource>`{.interpreted-text
role="ref"} **PIPELINE_SOURCE_CANVAS** = `0`

Pipeline compilation that was triggered by the 2D canvas renderer.

:::: {#class_RenderingServer_constant_PIPELINE_SOURCE_MESH}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineSource<enum_RenderingServer_PipelineSource>`{.interpreted-text
role="ref"} **PIPELINE_SOURCE_MESH** = `1`

Pipeline compilation that was triggered by loading a mesh.

:::: {#class_RenderingServer_constant_PIPELINE_SOURCE_SURFACE}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineSource<enum_RenderingServer_PipelineSource>`{.interpreted-text
role="ref"} **PIPELINE_SOURCE_SURFACE** = `2`

Pipeline compilation that was triggered by building the surface cache
before rendering the scene.

:::: {#class_RenderingServer_constant_PIPELINE_SOURCE_DRAW}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineSource<enum_RenderingServer_PipelineSource>`{.interpreted-text
role="ref"} **PIPELINE_SOURCE_DRAW** = `3`

Pipeline compilation that was triggered while drawing the scene.

:::: {#class_RenderingServer_constant_PIPELINE_SOURCE_SPECIALIZATION}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineSource<enum_RenderingServer_PipelineSource>`{.interpreted-text
role="ref"} **PIPELINE_SOURCE_SPECIALIZATION** = `4`

Pipeline compilation that was triggered to optimize the current scene.

:::: {#class_RenderingServer_constant_PIPELINE_SOURCE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineSource<enum_RenderingServer_PipelineSource>`{.interpreted-text
role="ref"} **PIPELINE_SOURCE_MAX** = `5`

Represents the size of the
`PipelineSource<enum_RenderingServer_PipelineSource>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingServer_Features}
::: rst-class
classref-enumeration
:::
::::

enum **Features**: `🔗<enum_RenderingServer_Features>`{.interpreted-text
role="ref"}

:::: {#class_RenderingServer_constant_FEATURE_SHADERS}
::: rst-class
classref-enumeration-constant
:::
::::

`Features<enum_RenderingServer_Features>`{.interpreted-text role="ref"}
**FEATURE_SHADERS** = `0`

**Deprecated:** This constant has not been used since Godot 3.0.

:::: {#class_RenderingServer_constant_FEATURE_MULTITHREADED}
::: rst-class
classref-enumeration-constant
:::
::::

`Features<enum_RenderingServer_Features>`{.interpreted-text role="ref"}
**FEATURE_MULTITHREADED** = `1`

**Deprecated:** This constant has not been used since Godot 3.0.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_RenderingServer_constant_NO_INDEX_ARRAY}
::: rst-class
classref-constant
:::
::::

**NO_INDEX_ARRAY** = `-1`
`🔗<class_RenderingServer_constant_NO_INDEX_ARRAY>`{.interpreted-text
role="ref"}

Marks an error that shows that the index array is empty.

:::: {#class_RenderingServer_constant_ARRAY_WEIGHTS_SIZE}
::: rst-class
classref-constant
:::
::::

**ARRAY_WEIGHTS_SIZE** = `4`
`🔗<class_RenderingServer_constant_ARRAY_WEIGHTS_SIZE>`{.interpreted-text
role="ref"}

Number of weights/bones per vertex.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_Z_MIN}
::: rst-class
classref-constant
:::
::::

**CANVAS_ITEM_Z_MIN** = `-4096`
`🔗<class_RenderingServer_constant_CANVAS_ITEM_Z_MIN>`{.interpreted-text
role="ref"}

The minimum Z-layer for canvas items.

:::: {#class_RenderingServer_constant_CANVAS_ITEM_Z_MAX}
::: rst-class
classref-constant
:::
::::

**CANVAS_ITEM_Z_MAX** = `4096`
`🔗<class_RenderingServer_constant_CANVAS_ITEM_Z_MAX>`{.interpreted-text
role="ref"}

The maximum Z-layer for canvas items.

:::: {#class_RenderingServer_constant_CANVAS_LAYER_MIN}
::: rst-class
classref-constant
:::
::::

**CANVAS_LAYER_MIN** = `-2147483648`
`🔗<class_RenderingServer_constant_CANVAS_LAYER_MIN>`{.interpreted-text
role="ref"}

The minimum canvas layer.

:::: {#class_RenderingServer_constant_CANVAS_LAYER_MAX}
::: rst-class
classref-constant
:::
::::

**CANVAS_LAYER_MAX** = `2147483647`
`🔗<class_RenderingServer_constant_CANVAS_LAYER_MAX>`{.interpreted-text
role="ref"}

The maximum canvas layer.

:::: {#class_RenderingServer_constant_MAX_GLOW_LEVELS}
::: rst-class
classref-constant
:::
::::

**MAX_GLOW_LEVELS** = `7`
`🔗<class_RenderingServer_constant_MAX_GLOW_LEVELS>`{.interpreted-text
role="ref"}

The maximum number of glow levels that can be used with the glow
post-processing effect.

:::: {#class_RenderingServer_constant_MAX_CURSORS}
::: rst-class
classref-constant
:::
::::

**MAX_CURSORS** = `8`
`🔗<class_RenderingServer_constant_MAX_CURSORS>`{.interpreted-text
role="ref"}

**Deprecated:** This constant is not used by the engine.

:::: {#class_RenderingServer_constant_MAX_2D_DIRECTIONAL_LIGHTS}
::: rst-class
classref-constant
:::
::::

**MAX_2D_DIRECTIONAL_LIGHTS** = `8`
`🔗<class_RenderingServer_constant_MAX_2D_DIRECTIONAL_LIGHTS>`{.interpreted-text
role="ref"}

The maximum number of directional lights that can be rendered at a given
time in 2D.

:::: {#class_RenderingServer_constant_MAX_MESH_SURFACES}
::: rst-class
classref-constant
:::
::::

**MAX_MESH_SURFACES** = `256`
`🔗<class_RenderingServer_constant_MAX_MESH_SURFACES>`{.interpreted-text
role="ref"}

The maximum number of surfaces a mesh can have.

:::: {#class_RenderingServer_constant_MATERIAL_RENDER_PRIORITY_MIN}
::: rst-class
classref-constant
:::
::::

**MATERIAL_RENDER_PRIORITY_MIN** = `-128`
`🔗<class_RenderingServer_constant_MATERIAL_RENDER_PRIORITY_MIN>`{.interpreted-text
role="ref"}

The minimum renderpriority of all materials.

:::: {#class_RenderingServer_constant_MATERIAL_RENDER_PRIORITY_MAX}
::: rst-class
classref-constant
:::
::::

**MATERIAL_RENDER_PRIORITY_MAX** = `127`
`🔗<class_RenderingServer_constant_MATERIAL_RENDER_PRIORITY_MAX>`{.interpreted-text
role="ref"}

The maximum renderpriority of all materials.

:::: {#class_RenderingServer_constant_ARRAY_CUSTOM_COUNT}
::: rst-class
classref-constant
:::
::::

**ARRAY_CUSTOM_COUNT** = `4`
`🔗<class_RenderingServer_constant_ARRAY_CUSTOM_COUNT>`{.interpreted-text
role="ref"}

The number of custom data arrays available
(`ARRAY_CUSTOM0<class_RenderingServer_constant_ARRAY_CUSTOM0>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM1<class_RenderingServer_constant_ARRAY_CUSTOM1>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM2<class_RenderingServer_constant_ARRAY_CUSTOM2>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM3<class_RenderingServer_constant_ARRAY_CUSTOM3>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_POSITION}
::: rst-class
classref-constant
:::
::::

**PARTICLES_EMIT_FLAG_POSITION** = `1`
`🔗<class_RenderingServer_constant_PARTICLES_EMIT_FLAG_POSITION>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_ROTATION_SCALE}
::: rst-class
classref-constant
:::
::::

**PARTICLES_EMIT_FLAG_ROTATION_SCALE** = `2`
`🔗<class_RenderingServer_constant_PARTICLES_EMIT_FLAG_ROTATION_SCALE>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_VELOCITY}
::: rst-class
classref-constant
:::
::::

**PARTICLES_EMIT_FLAG_VELOCITY** = `4`
`🔗<class_RenderingServer_constant_PARTICLES_EMIT_FLAG_VELOCITY>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_COLOR}
::: rst-class
classref-constant
:::
::::

**PARTICLES_EMIT_FLAG_COLOR** = `8`
`🔗<class_RenderingServer_constant_PARTICLES_EMIT_FLAG_COLOR>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingServer_constant_PARTICLES_EMIT_FLAG_CUSTOM}
::: rst-class
classref-constant
:::
::::

**PARTICLES_EMIT_FLAG_CUSTOM** = `16`
`🔗<class_RenderingServer_constant_PARTICLES_EMIT_FLAG_CUSTOM>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_RenderingServer_property_render_loop_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **render_loop_enabled**
`🔗<class_RenderingServer_property_render_loop_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_render_loop_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_render_loop_enabled**()

If `false`, disables rendering completely, but the engine logic is still
being processed. You can call
`force_draw()<class_RenderingServer_method_force_draw>`{.interpreted-text
role="ref"} to draw a frame even with rendering disabled.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RenderingServer_method_bake_render_uv2}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\]
**bake_render_uv2**(base: `RID<class_RID>`{.interpreted-text
role="ref"}, material_overrides: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\],
image_size: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_bake_render_uv2>`{.interpreted-text
role="ref"}

Bakes the material data of the Mesh passed in the `base` parameter with
optional `material_overrides` to a set of
`Image<class_Image>`{.interpreted-text role="ref"}s of size
`image_size`. Returns an array of `Image<class_Image>`{.interpreted-text
role="ref"}s containing material properties as specified in
`BakeChannels<enum_RenderingServer_BakeChannels>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_call_on_render_thread}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**call_on_render_thread**(callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_call_on_render_thread>`{.interpreted-text
role="ref"}

As the RenderingServer actual logic may run on a separate thread,
accessing its internals from the main (or any other) thread will result
in errors. To make it easier to run code that can safely access the
rendering internals (such as
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}
and similar RD classes), push a callable via this function so it will be
executed on the render thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_attributes_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**camera_attributes_create**()
`🔗<class_RenderingServer_method_camera_attributes_create>`{.interpreted-text
role="ref"}

Creates a camera attributes object and adds it to the RenderingServer.
It can be accessed with the RID that is returned. This RID will be used
in all `camera_attributes_` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`CameraAttributes<class_CameraAttributes>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_attributes_set_auto_exposure}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_attributes_set_auto_exposure**(camera_attributes:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"}, min_sensitivity:
`float<class_float>`{.interpreted-text role="ref"}, max_sensitivity:
`float<class_float>`{.interpreted-text role="ref"}, speed:
`float<class_float>`{.interpreted-text role="ref"}, scale:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_attributes_set_auto_exposure>`{.interpreted-text
role="ref"}

Sets the parameters to use with the auto-exposure effect. These
parameters take on the same meaning as their counterparts in
`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
and
`CameraAttributesPractical<class_CameraAttributesPractical>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_attributes_set_dof_blur}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_attributes_set_dof_blur**(camera_attributes:
`RID<class_RID>`{.interpreted-text role="ref"}, far_enable:
`bool<class_bool>`{.interpreted-text role="ref"}, far_distance:
`float<class_float>`{.interpreted-text role="ref"}, far_transition:
`float<class_float>`{.interpreted-text role="ref"}, near_enable:
`bool<class_bool>`{.interpreted-text role="ref"}, near_distance:
`float<class_float>`{.interpreted-text role="ref"}, near_transition:
`float<class_float>`{.interpreted-text role="ref"}, amount:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_attributes_set_dof_blur>`{.interpreted-text
role="ref"}

Sets the parameters to use with the DOF blur effect. These parameters
take on the same meaning as their counterparts in
`CameraAttributesPractical<class_CameraAttributesPractical>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_attributes_set_dof_blur_bokeh_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_attributes_set_dof_blur_bokeh_shape**(shape:
`DOFBokehShape<enum_RenderingServer_DOFBokehShape>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_camera_attributes_set_dof_blur_bokeh_shape>`{.interpreted-text
role="ref"}

Sets the shape of the DOF bokeh pattern to `shape`. Different shapes may
be used to achieve artistic effect, or to meet performance targets.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_attributes_set_dof_blur_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_attributes_set_dof_blur_quality**(quality:
`DOFBlurQuality<enum_RenderingServer_DOFBlurQuality>`{.interpreted-text
role="ref"}, use_jitter: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_camera_attributes_set_dof_blur_quality>`{.interpreted-text
role="ref"}

Sets the quality level of the DOF blur effect to `quality`. `use_jitter`
can be used to jitter samples taken during the blur pass to hide
artifacts at the cost of looking more fuzzy.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_attributes_set_exposure}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_attributes_set_exposure**(camera_attributes:
`RID<class_RID>`{.interpreted-text role="ref"}, multiplier:
`float<class_float>`{.interpreted-text role="ref"}, normalization:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_attributes_set_exposure>`{.interpreted-text
role="ref"}

Sets the exposure values that will be used by the renderers. The
normalization amount is used to bake a given Exposure Value (EV) into
rendering calculations to reduce the dynamic range of the scene.

The normalization factor can be calculated from exposure value (EV100)
as follows:

    func get_exposure_normalization(ev100: float):
        return 1.0 / (pow(2.0, ev100) * 1.2)

The exposure value can be calculated from aperture (in f-stops), shutter
speed (in seconds), and sensitivity (in ISO) as follows:

    func get_exposure(aperture: float, shutter_speed: float, sensitivity: float):
        return log((aperture * aperture) / shutter_speed * (100.0 / sensitivity)) / log(2)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **camera_create**()
`🔗<class_RenderingServer_method_camera_create>`{.interpreted-text
role="ref"}

Creates a 3D camera and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`camera_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent node is
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_set_camera_attributes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_set_camera_attributes**(camera:
`RID<class_RID>`{.interpreted-text role="ref"}, effects:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_set_camera_attributes>`{.interpreted-text
role="ref"}

Sets the camera_attributes created with
`camera_attributes_create()<class_RenderingServer_method_camera_attributes_create>`{.interpreted-text
role="ref"} to the given camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_set_compositor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_set_compositor**(camera: `RID<class_RID>`{.interpreted-text
role="ref"}, compositor: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_set_compositor>`{.interpreted-text
role="ref"}

Sets the compositor used by this camera. Equivalent to
`Camera3D.compositor<class_Camera3D_property_compositor>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_set_cull_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_set_cull_mask**(camera: `RID<class_RID>`{.interpreted-text
role="ref"}, layers: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_set_cull_mask>`{.interpreted-text
role="ref"}

Sets the cull mask associated with this camera. The cull mask describes
which 3D layers are rendered by this camera. Equivalent to
`Camera3D.cull_mask<class_Camera3D_property_cull_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_set_environment}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_set_environment**(camera: `RID<class_RID>`{.interpreted-text
role="ref"}, env: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_set_environment>`{.interpreted-text
role="ref"}

Sets the environment used by this camera. Equivalent to
`Camera3D.environment<class_Camera3D_property_environment>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_set_frustum}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_set_frustum**(camera: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `float<class_float>`{.interpreted-text role="ref"},
offset: `Vector2<class_Vector2>`{.interpreted-text role="ref"}, z_near:
`float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_set_frustum>`{.interpreted-text
role="ref"}

Sets camera to use frustum projection. This mode allows adjusting the
`offset` argument to create \"tilted frustum\" effects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_set_orthogonal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_set_orthogonal**(camera: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `float<class_float>`{.interpreted-text role="ref"},
z_near: `float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_set_orthogonal>`{.interpreted-text
role="ref"}

Sets camera to use orthogonal projection, also known as orthographic
projection. Objects remain the same size on the screen no matter how far
away they are.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_set_perspective}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_set_perspective**(camera: `RID<class_RID>`{.interpreted-text
role="ref"}, fovy_degrees: `float<class_float>`{.interpreted-text
role="ref"}, z_near: `float<class_float>`{.interpreted-text role="ref"},
z_far: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_set_perspective>`{.interpreted-text
role="ref"}

Sets camera to use perspective projection. Objects on the screen becomes
smaller when they are far away.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_set_transform**(camera: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_set_transform>`{.interpreted-text
role="ref"}

Sets `Transform3D<class_Transform3D>`{.interpreted-text role="ref"} of
camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_camera_set_use_vertical_aspect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**camera_set_use_vertical_aspect**(camera:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_camera_set_use_vertical_aspect>`{.interpreted-text
role="ref"}

If `true`, preserves the horizontal aspect ratio which is equivalent to
`Camera3D.KEEP_WIDTH<class_Camera3D_constant_KEEP_WIDTH>`{.interpreted-text
role="ref"}. If `false`, preserves the vertical aspect ratio which is
equivalent to
`Camera3D.KEEP_HEIGHT<class_Camera3D_constant_KEEP_HEIGHT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **canvas_create**()
`🔗<class_RenderingServer_method_canvas_create>`{.interpreted-text
role="ref"}

Creates a canvas and returns the assigned
`RID<class_RID>`{.interpreted-text role="ref"}. It can be accessed with
the RID that is returned. This RID will be used in all `canvas_*`
RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

Canvas has no `Resource<class_Resource>`{.interpreted-text role="ref"}
or `Node<class_Node>`{.interpreted-text role="ref"} equivalent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_animation_slice}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_animation_slice**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, animation_length:
`float<class_float>`{.interpreted-text role="ref"}, slice_begin:
`float<class_float>`{.interpreted-text role="ref"}, slice_end:
`float<class_float>`{.interpreted-text role="ref"}, offset:
`float<class_float>`{.interpreted-text role="ref"} = 0.0)
`🔗<class_RenderingServer_method_canvas_item_add_animation_slice>`{.interpreted-text
role="ref"}

Subsequent drawing commands will be ignored unless they fall within the
specified animation slice. This is a faster way to implement animations
that loop on background rather than redrawing constantly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_circle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_circle**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, radius: `float<class_float>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"}, antialiased:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_RenderingServer_method_canvas_item_add_circle>`{.interpreted-text
role="ref"}

Draws a circle on the `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} pointed to by the `item` `RID<class_RID>`{.interpreted-text
role="ref"}. See also
`CanvasItem.draw_circle()<class_CanvasItem_method_draw_circle>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_clip_ignore}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_clip_ignore**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, ignore: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_add_clip_ignore>`{.interpreted-text
role="ref"}

If `ignore` is `true`, ignore clipping on items drawn with this canvas
item until this is called again with `ignore` set to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_lcd_texture_rect_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_lcd_texture_rect_region**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, texture:
`RID<class_RID>`{.interpreted-text role="ref"}, src_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_add_lcd_texture_rect_region>`{.interpreted-text
role="ref"}

See also
`CanvasItem.draw_lcd_texture_rect_region()<class_CanvasItem_method_draw_lcd_texture_rect_region>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_line**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, from: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, to: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"}, width:
`float<class_float>`{.interpreted-text role="ref"} = -1.0, antialiased:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_RenderingServer_method_canvas_item_add_line>`{.interpreted-text
role="ref"}

Draws a line on the `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} pointed to by the `item` `RID<class_RID>`{.interpreted-text
role="ref"}. See also
`CanvasItem.draw_line()<class_CanvasItem_method_draw_line>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_mesh**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, mesh: `RID<class_RID>`{.interpreted-text role="ref"},
transform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"} = Transform2D(1, 0, 0, 1, 0, 0), modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
texture: `RID<class_RID>`{.interpreted-text role="ref"} = RID())
`🔗<class_RenderingServer_method_canvas_item_add_mesh>`{.interpreted-text
role="ref"}

Draws a mesh created with
`mesh_create()<class_RenderingServer_method_mesh_create>`{.interpreted-text
role="ref"} with given `transform`, `modulate` color, and `texture`.
This is used internally by
`MeshInstance2D<class_MeshInstance2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_msdf_texture_rect_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_msdf_texture_rect_region**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, texture:
`RID<class_RID>`{.interpreted-text role="ref"}, src_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
outline_size: `int<class_int>`{.interpreted-text role="ref"} = 0,
px_range: `float<class_float>`{.interpreted-text role="ref"} = 1.0,
scale: `float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_RenderingServer_method_canvas_item_add_msdf_texture_rect_region>`{.interpreted-text
role="ref"}

See also
`CanvasItem.draw_msdf_texture_rect_region()<class_CanvasItem_method_draw_msdf_texture_rect_region>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_multiline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_multiline**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, width: `float<class_float>`{.interpreted-text role="ref"} =
-1.0, antialiased: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_RenderingServer_method_canvas_item_add_multiline>`{.interpreted-text
role="ref"}

Draws a 2D multiline on the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed to
by the `item` `RID<class_RID>`{.interpreted-text role="ref"}. See also
`CanvasItem.draw_multiline()<class_CanvasItem_method_draw_multiline>`{.interpreted-text
role="ref"} and
`CanvasItem.draw_multiline_colors()<class_CanvasItem_method_draw_multiline_colors>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_multimesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_multimesh**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, mesh: `RID<class_RID>`{.interpreted-text role="ref"},
texture: `RID<class_RID>`{.interpreted-text role="ref"} = RID())
`🔗<class_RenderingServer_method_canvas_item_add_multimesh>`{.interpreted-text
role="ref"}

Draws a 2D `MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"} on
the `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed
to by the `item` `RID<class_RID>`{.interpreted-text role="ref"}. See
also
`CanvasItem.draw_multimesh()<class_CanvasItem_method_draw_multimesh>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_nine_patch}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_nine_patch**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"},
source: `Rect2<class_Rect2>`{.interpreted-text role="ref"}, texture:
`RID<class_RID>`{.interpreted-text role="ref"}, topleft:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, bottomright:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, x_axis_mode:
`NinePatchAxisMode<enum_RenderingServer_NinePatchAxisMode>`{.interpreted-text
role="ref"} = 0, y_axis_mode:
`NinePatchAxisMode<enum_RenderingServer_NinePatchAxisMode>`{.interpreted-text
role="ref"} = 0, draw_center: `bool<class_bool>`{.interpreted-text
role="ref"} = true, modulate: `Color<class_Color>`{.interpreted-text
role="ref"} = Color(1, 1, 1, 1))
`🔗<class_RenderingServer_method_canvas_item_add_nine_patch>`{.interpreted-text
role="ref"}

Draws a nine-patch rectangle on the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed to
by the `item` `RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_particles}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_particles**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, particles: `RID<class_RID>`{.interpreted-text role="ref"},
texture: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_add_particles>`{.interpreted-text
role="ref"}

Draws particles on the `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} pointed to by the `item` `RID<class_RID>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_polygon**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, uvs:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} = PackedVector2Array(), texture:
`RID<class_RID>`{.interpreted-text role="ref"} = RID())
`🔗<class_RenderingServer_method_canvas_item_add_polygon>`{.interpreted-text
role="ref"}

Draws a 2D polygon on the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed to
by the `item` `RID<class_RID>`{.interpreted-text role="ref"}. If you
need more flexibility (such as being able to use bones), use
`canvas_item_add_triangle_array()<class_RenderingServer_method_canvas_item_add_triangle_array>`{.interpreted-text
role="ref"} instead. See also
`CanvasItem.draw_polygon()<class_CanvasItem_method_draw_polygon>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If you frequently redraw the same polygon with a large
number of vertices, consider pre-calculating the triangulation with
`Geometry2D.triangulate_polygon()<class_Geometry2D_method_triangulate_polygon>`{.interpreted-text
role="ref"} and using
`CanvasItem.draw_mesh()<class_CanvasItem_method_draw_mesh>`{.interpreted-text
role="ref"},
`CanvasItem.draw_multimesh()<class_CanvasItem_method_draw_multimesh>`{.interpreted-text
role="ref"}, or
`canvas_item_add_triangle_array()<class_RenderingServer_method_canvas_item_add_triangle_array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_polyline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_polyline**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, width: `float<class_float>`{.interpreted-text role="ref"} =
-1.0, antialiased: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_RenderingServer_method_canvas_item_add_polyline>`{.interpreted-text
role="ref"}

Draws a 2D polyline on the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed to
by the `item` `RID<class_RID>`{.interpreted-text role="ref"}. See also
`CanvasItem.draw_polyline()<class_CanvasItem_method_draw_polyline>`{.interpreted-text
role="ref"} and
`CanvasItem.draw_polyline_colors()<class_CanvasItem_method_draw_polyline_colors>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_primitive}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_primitive**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, uvs:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, texture: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_add_primitive>`{.interpreted-text
role="ref"}

Draws a 2D primitive on the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed to
by the `item` `RID<class_RID>`{.interpreted-text role="ref"}. See also
`CanvasItem.draw_primitive()<class_CanvasItem_method_draw_primitive>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_rect**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"}, antialiased:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_RenderingServer_method_canvas_item_add_rect>`{.interpreted-text
role="ref"}

Draws a rectangle on the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed to
by the `item` `RID<class_RID>`{.interpreted-text role="ref"}. See also
`CanvasItem.draw_rect()<class_CanvasItem_method_draw_rect>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_set_transform**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_add_set_transform>`{.interpreted-text
role="ref"}

Sets a `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
that will be used to transform subsequent canvas item commands.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_texture_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_texture_rect**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, texture:
`RID<class_RID>`{.interpreted-text role="ref"}, tile:
`bool<class_bool>`{.interpreted-text role="ref"} = false, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
transpose: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_RenderingServer_method_canvas_item_add_texture_rect>`{.interpreted-text
role="ref"}

Draws a 2D textured rectangle on the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed to
by the `item` `RID<class_RID>`{.interpreted-text role="ref"}. See also
`CanvasItem.draw_texture_rect()<class_CanvasItem_method_draw_texture_rect>`{.interpreted-text
role="ref"} and
`Texture2D.draw_rect()<class_Texture2D_method_draw_rect>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_texture_rect_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_texture_rect_region**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, texture:
`RID<class_RID>`{.interpreted-text role="ref"}, src_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
transpose: `bool<class_bool>`{.interpreted-text role="ref"} = false,
clip_uv: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_RenderingServer_method_canvas_item_add_texture_rect_region>`{.interpreted-text
role="ref"}

Draws the specified region of a 2D textured rectangle on the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed to
by the `item` `RID<class_RID>`{.interpreted-text role="ref"}. See also
`CanvasItem.draw_texture_rect_region()<class_CanvasItem_method_draw_texture_rect_region>`{.interpreted-text
role="ref"} and
`Texture2D.draw_rect_region()<class_Texture2D_method_draw_rect_region>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_add_triangle_array}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_add_triangle_array**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, indices:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}, points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, uvs:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} = PackedVector2Array(), bones:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
= PackedInt32Array(), weights:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} = PackedFloat32Array(), texture:
`RID<class_RID>`{.interpreted-text role="ref"} = RID(), count:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_RenderingServer_method_canvas_item_add_triangle_array>`{.interpreted-text
role="ref"}

Draws a triangle array on the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} pointed to
by the `item` `RID<class_RID>`{.interpreted-text role="ref"}. This is
internally used by `Line2D<class_Line2D>`{.interpreted-text role="ref"}
and `StyleBoxFlat<class_StyleBoxFlat>`{.interpreted-text role="ref"} for
rendering.
`canvas_item_add_triangle_array()<class_RenderingServer_method_canvas_item_add_triangle_array>`{.interpreted-text
role="ref"} is highly flexible, but more complex to use than
`canvas_item_add_polygon()<class_RenderingServer_method_canvas_item_add_polygon>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If `count` is set to a non-negative value, only the first
`count * 3` indices (corresponding to `count` triangles) will be drawn.
Otherwise, all indices are drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_attach_skeleton}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_attach_skeleton**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, skeleton: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_attach_skeleton>`{.interpreted-text
role="ref"}

Attaches a skeleton to the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}. Removes
the previous skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_clear**(item: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_item_clear>`{.interpreted-text
role="ref"}

Clears the `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
and removes all commands in it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **canvas_item_create**()
`🔗<class_RenderingServer_method_canvas_item_create>`{.interpreted-text
role="ref"}

Creates a new CanvasItem instance and returns its
`RID<class_RID>`{.interpreted-text role="ref"}. It can be accessed with
the RID that is returned. This RID will be used in all `canvas_item_*`
RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent node is
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_get_instance_shader_parameter}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**canvas_item_get_instance_shader_parameter**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, parameter:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_canvas_item_get_instance_shader_parameter>`{.interpreted-text
role="ref"}

Returns the value of the per-instance shader uniform from the specified
canvas item instance. Equivalent to
`CanvasItem.get_instance_shader_parameter()<class_CanvasItem_method_get_instance_shader_parameter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_get_instance_shader_parameter_default_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**canvas_item_get_instance_shader_parameter_default_value**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, parameter:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_canvas_item_get_instance_shader_parameter_default_value>`{.interpreted-text
role="ref"}

Returns the default value of the per-instance shader uniform from the
specified canvas item instance. Equivalent to
`CanvasItem.get_instance_shader_parameter()<class_CanvasItem_method_get_instance_shader_parameter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_get_instance_shader_parameter_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\]
**canvas_item_get_instance_shader_parameter_list**(instance:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_canvas_item_get_instance_shader_parameter_list>`{.interpreted-text
role="ref"}

Returns a dictionary of per-instance shader uniform names of the
per-instance shader uniform from the specified canvas item instance.

The returned dictionary is in PropertyInfo format, with the keys `name`,
`class_name`, `type`, `hint`, `hint_string`, and `usage`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_reset_physics_interpolation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_reset_physics_interpolation**(item:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_reset_physics_interpolation>`{.interpreted-text
role="ref"}

Prevents physics interpolation for the current physics tick.

This is useful when moving a canvas item to a new location, to give an
instantaneous change rather than interpolation from the previous
location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_canvas_group_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_canvas_group_mode**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`CanvasGroupMode<enum_RenderingServer_CanvasGroupMode>`{.interpreted-text
role="ref"}, clear_margin: `float<class_float>`{.interpreted-text
role="ref"} = 5.0, fit_empty: `bool<class_bool>`{.interpreted-text
role="ref"} = false, fit_margin: `float<class_float>`{.interpreted-text
role="ref"} = 0.0, blur_mipmaps: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_RenderingServer_method_canvas_item_set_canvas_group_mode>`{.interpreted-text
role="ref"}

Sets the canvas group mode used during 2D rendering for the canvas item
specified by the `item` RID. For faster but more limited clipping, use
`canvas_item_set_clip()<class_RenderingServer_method_canvas_item_set_clip>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* The equivalent node functionality is found in
`CanvasGroup<class_CanvasGroup>`{.interpreted-text role="ref"} and
`CanvasItem.clip_children<class_CanvasItem_property_clip_children>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_clip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_clip**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, clip: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_clip>`{.interpreted-text
role="ref"}

If `clip` is `true`, makes the canvas item specified by the `item` RID
not draw anything outside of its rect\'s coordinates. This clipping is
fast, but works only with axis-aligned rectangles. This means that
rotation is ignored by the clipping rectangle. For more advanced
clipping shapes, use
`canvas_item_set_canvas_group_mode()<class_RenderingServer_method_canvas_item_set_canvas_group_mode>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* The equivalent node functionality is found in
`Label.clip_text<class_Label_property_clip_text>`{.interpreted-text
role="ref"}, `RichTextLabel<class_RichTextLabel>`{.interpreted-text
role="ref"} (always enabled) and more.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_copy_to_backbuffer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_copy_to_backbuffer**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_copy_to_backbuffer>`{.interpreted-text
role="ref"}

Sets the `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} to
copy a rect to the backbuffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_custom_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_custom_rect**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, use_custom_rect: `bool<class_bool>`{.interpreted-text
role="ref"}, rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"} =
Rect2(0, 0, 0, 0))
`🔗<class_RenderingServer_method_canvas_item_set_custom_rect>`{.interpreted-text
role="ref"}

If `use_custom_rect` is `true`, sets the custom visibility rectangle
(used for culling) to `rect` for the canvas item specified by `item`.
Setting a custom visibility rect can reduce CPU load when drawing lots
of 2D instances. If `use_custom_rect` is `false`, automatically computes
a visibility rectangle based on the canvas item\'s draw commands.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_default_texture_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_default_texture_filter**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, filter:
`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_default_texture_filter>`{.interpreted-text
role="ref"}

Sets the default texture filter mode for the canvas item specified by
the `item` RID. Equivalent to
`CanvasItem.texture_filter<class_CanvasItem_property_texture_filter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_default_texture_repeat}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_default_texture_repeat**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, repeat:
`CanvasItemTextureRepeat<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_default_texture_repeat>`{.interpreted-text
role="ref"}

Sets the default texture repeat mode for the canvas item specified by
the `item` RID. Equivalent to
`CanvasItem.texture_repeat<class_CanvasItem_property_texture_repeat>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_distance_field_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_distance_field_mode**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_distance_field_mode>`{.interpreted-text
role="ref"}

If `enabled` is `true`, enables multichannel signed distance field
rendering mode for the canvas item specified by the `item` RID. This is
meant to be used for font rendering, or with specially generated images
using [msdfgen](https://github.com/Chlumsky/msdfgen).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_draw_behind_parent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_draw_behind_parent**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_draw_behind_parent>`{.interpreted-text
role="ref"}

If `enabled` is `true`, draws the canvas item specified by the `item`
RID behind its parent. Equivalent to
`CanvasItem.show_behind_parent<class_CanvasItem_property_show_behind_parent>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_draw_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_draw_index**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_draw_index>`{.interpreted-text
role="ref"}

Sets the index for the `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_instance_shader_parameter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_instance_shader_parameter**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, parameter:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_instance_shader_parameter>`{.interpreted-text
role="ref"}

Sets the per-instance shader uniform on the specified canvas item
instance. Equivalent to
`CanvasItem.set_instance_shader_parameter()<class_CanvasItem_method_set_instance_shader_parameter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_interpolated}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_interpolated**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, interpolated:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_interpolated>`{.interpreted-text
role="ref"}

If `interpolated` is `true`, turns on physics interpolation for the
canvas item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_light_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_light_mask**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_light_mask>`{.interpreted-text
role="ref"}

Sets the light `mask` for the canvas item specified by the `item` RID.
Equivalent to
`CanvasItem.light_mask<class_CanvasItem_property_light_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_material**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, material: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_material>`{.interpreted-text
role="ref"}

Sets a new `material` to the canvas item specified by the `item` RID.
Equivalent to
`CanvasItem.material<class_CanvasItem_property_material>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_modulate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_modulate**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_modulate>`{.interpreted-text
role="ref"}

Multiplies the color of the canvas item specified by the `item` RID,
while affecting its children. See also
`canvas_item_set_self_modulate()<class_RenderingServer_method_canvas_item_set_self_modulate>`{.interpreted-text
role="ref"}. Equivalent to
`CanvasItem.modulate<class_CanvasItem_property_modulate>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_parent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_parent**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, parent: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_parent>`{.interpreted-text
role="ref"}

Sets a parent `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} to the `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"}. The item will inherit transform, modulation and visibility
from its parent, like `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} nodes in the scene tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_self_modulate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_self_modulate**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_self_modulate>`{.interpreted-text
role="ref"}

Multiplies the color of the canvas item specified by the `item` RID,
without affecting its children. See also
`canvas_item_set_modulate()<class_RenderingServer_method_canvas_item_set_modulate>`{.interpreted-text
role="ref"}. Equivalent to
`CanvasItem.self_modulate<class_CanvasItem_property_self_modulate>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_sort_children_by_y}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_sort_children_by_y**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_sort_children_by_y>`{.interpreted-text
role="ref"}

If `enabled` is `true`, child nodes with the lowest Y position are drawn
before those with a higher Y position. Y-sorting only affects children
that inherit from the canvas item specified by the `item` RID, not the
canvas item itself. Equivalent to
`CanvasItem.y_sort_enabled<class_CanvasItem_property_y_sort_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_transform**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_transform>`{.interpreted-text
role="ref"}

Sets the `transform` of the canvas item specified by the `item` RID.
This affects where and how the item will be drawn. Child canvas items\'
transforms are multiplied by their parent\'s transform. Equivalent to
`Node2D.transform<class_Node2D_property_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_use_parent_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_use_parent_material**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_use_parent_material>`{.interpreted-text
role="ref"}

Sets if the `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
uses its parent\'s material.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_visibility_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_visibility_layer**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, visibility_layer:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_visibility_layer>`{.interpreted-text
role="ref"}

Sets the rendering visibility layer associated with this
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}. Only
`Viewport<class_Viewport>`{.interpreted-text role="ref"} nodes with a
matching rendering mask will render this
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_visibility_notifier}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_visibility_notifier**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"}, area:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, enter_callable:
`Callable<class_Callable>`{.interpreted-text role="ref"}, exit_callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_visibility_notifier>`{.interpreted-text
role="ref"}

Sets the given `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} as visibility notifier. `area` defines the area of detecting
visibility. `enter_callable` is called when the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} enters the
screen, `exit_callable` is called when the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} exits the
screen. If `enable` is `false`, the item will no longer function as
notifier.

This method can be used to manually mimic
`VisibleOnScreenNotifier2D<class_VisibleOnScreenNotifier2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_visible**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, visible: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_visible>`{.interpreted-text
role="ref"}

Sets the visibility of the
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_z_as_relative_to_parent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_z_as_relative_to_parent**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_z_as_relative_to_parent>`{.interpreted-text
role="ref"}

If this is enabled, the Z index of the parent will be added to the
children\'s Z index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_set_z_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_set_z_index**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, z_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_set_z_index>`{.interpreted-text
role="ref"}

Sets the `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}\'s
Z index, i.e. its draw order (lower indexes are drawn first).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_item_transform_physics_interpolation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_item_transform_physics_interpolation**(item:
`RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_item_transform_physics_interpolation>`{.interpreted-text
role="ref"}

Transforms both the current and previous stored transform for a canvas
item.

This allows transforming a canvas item without creating a \"glitch\" in
the interpolation, which is particularly useful for large worlds
utilizing a shifting origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_attach_to_canvas}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_attach_to_canvas**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, canvas:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_attach_to_canvas>`{.interpreted-text
role="ref"}

Attaches the canvas light to the canvas. Removes it from its previous
canvas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **canvas_light_create**()
`🔗<class_RenderingServer_method_canvas_light_create>`{.interpreted-text
role="ref"}

Creates a canvas light and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`canvas_light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent node is
`Light2D<class_Light2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_attach_to_canvas}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_occluder_attach_to_canvas**(occluder:
`RID<class_RID>`{.interpreted-text role="ref"}, canvas:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_occluder_attach_to_canvas>`{.interpreted-text
role="ref"}

Attaches a light occluder to the canvas. Removes it from its previous
canvas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**canvas_light_occluder_create**()
`🔗<class_RenderingServer_method_canvas_light_occluder_create>`{.interpreted-text
role="ref"}

Creates a light occluder and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`canvas_light_occluder_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent node is
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_reset_physics_interpolation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_occluder_reset_physics_interpolation**(occluder:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_occluder_reset_physics_interpolation>`{.interpreted-text
role="ref"}

Prevents physics interpolation for the current physics tick.

This is useful when moving an occluder to a new location, to give an
instantaneous change rather than interpolation from the previous
location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_set_as_sdf_collision}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_occluder_set_as_sdf_collision**(occluder:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_occluder_set_as_sdf_collision>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_set_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_occluder_set_enabled**(occluder:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_occluder_set_enabled>`{.interpreted-text
role="ref"}

Enables or disables light occluder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_set_interpolated}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_occluder_set_interpolated**(occluder:
`RID<class_RID>`{.interpreted-text role="ref"}, interpolated:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_occluder_set_interpolated>`{.interpreted-text
role="ref"}

If `interpolated` is `true`, turns on physics interpolation for the
light occluder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_set_light_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_occluder_set_light_mask**(occluder:
`RID<class_RID>`{.interpreted-text role="ref"}, mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_occluder_set_light_mask>`{.interpreted-text
role="ref"}

The light mask. See
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"}
for more information on light masks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_set_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_occluder_set_polygon**(occluder:
`RID<class_RID>`{.interpreted-text role="ref"}, polygon:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_occluder_set_polygon>`{.interpreted-text
role="ref"}

Sets a light occluder\'s polygon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_occluder_set_transform**(occluder:
`RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_occluder_set_transform>`{.interpreted-text
role="ref"}

Sets a light occluder\'s
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_occluder_transform_physics_interpolation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_occluder_transform_physics_interpolation**(occluder:
`RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_occluder_transform_physics_interpolation>`{.interpreted-text
role="ref"}

Transforms both the current and previous stored transform for a light
occluder.

This allows transforming an occluder without creating a \"glitch\" in
the interpolation, which is particularly useful for large worlds
utilizing a shifting origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_reset_physics_interpolation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_reset_physics_interpolation**(light:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_reset_physics_interpolation>`{.interpreted-text
role="ref"}

Prevents physics interpolation for the current physics tick.

This is useful when moving a canvas item to a new location, to give an
instantaneous change rather than interpolation from the previous
location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_blend_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_blend_mode**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`CanvasLightBlendMode<enum_RenderingServer_CanvasLightBlendMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_blend_mode>`{.interpreted-text
role="ref"}

Sets the blend mode for the given canvas light to `mode`. Equivalent to
`Light2D.blend_mode<class_Light2D_property_blend_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_color**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_color>`{.interpreted-text
role="ref"}

Sets the color for a light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_enabled**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_enabled>`{.interpreted-text
role="ref"}

Enables or disables a canvas light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_energy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_energy**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, energy: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_energy>`{.interpreted-text
role="ref"}

Sets a canvas light\'s energy.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_height}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_height**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, height: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_height>`{.interpreted-text
role="ref"}

Sets a canvas light\'s height.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_interpolated}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_interpolated**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, interpolated:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_interpolated>`{.interpreted-text
role="ref"}

If `interpolated` is `true`, turns on physics interpolation for the
canvas light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_item_cull_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_item_cull_mask**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_item_cull_mask>`{.interpreted-text
role="ref"}

The light mask. See
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"}
for more information on light masks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_item_shadow_cull_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_item_shadow_cull_mask**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_item_shadow_cull_mask>`{.interpreted-text
role="ref"}

The binary mask used to determine which layers this canvas light\'s
shadows affects. See
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"}
for more information on light masks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_layer_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_layer_range**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, min_layer:
`int<class_int>`{.interpreted-text role="ref"}, max_layer:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_layer_range>`{.interpreted-text
role="ref"}

The layer range that gets rendered with this light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_mode**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, mode:
`CanvasLightMode<enum_RenderingServer_CanvasLightMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_mode>`{.interpreted-text
role="ref"}

Sets the mode of the canvas light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_shadow_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_shadow_color**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_shadow_color>`{.interpreted-text
role="ref"}

Sets the color of the canvas light\'s shadow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_shadow_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_shadow_enabled**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_shadow_enabled>`{.interpreted-text
role="ref"}

Enables or disables the canvas light\'s shadow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_shadow_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_shadow_filter**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, filter:
`CanvasLightShadowFilter<enum_RenderingServer_CanvasLightShadowFilter>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_shadow_filter>`{.interpreted-text
role="ref"}

Sets the canvas light\'s shadow\'s filter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_shadow_smooth}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_shadow_smooth**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, smooth:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_shadow_smooth>`{.interpreted-text
role="ref"}

Smoothens the shadow. The lower, the smoother.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_texture**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, texture: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_texture>`{.interpreted-text
role="ref"}

Sets the texture to be used by a
`PointLight2D<class_PointLight2D>`{.interpreted-text role="ref"}.
Equivalent to
`PointLight2D.texture<class_PointLight2D_property_texture>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_texture_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_texture_offset**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, offset:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_texture_offset>`{.interpreted-text
role="ref"}

Sets the offset of a
`PointLight2D<class_PointLight2D>`{.interpreted-text role="ref"}\'s
texture. Equivalent to
`PointLight2D.offset<class_PointLight2D_property_offset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_texture_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_texture_scale**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, scale:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_texture_scale>`{.interpreted-text
role="ref"}

Sets the scale factor of a
`PointLight2D<class_PointLight2D>`{.interpreted-text role="ref"}\'s
texture. Equivalent to
`PointLight2D.texture_scale<class_PointLight2D_property_texture_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_transform**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_transform>`{.interpreted-text
role="ref"}

Sets the canvas light\'s
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_set_z_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_set_z_range**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, min_z: `int<class_int>`{.interpreted-text role="ref"},
max_z: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_set_z_range>`{.interpreted-text
role="ref"}

Sets the Z range of objects that will be affected by this light.
Equivalent to
`Light2D.range_z_min<class_Light2D_property_range_z_min>`{.interpreted-text
role="ref"} and
`Light2D.range_z_max<class_Light2D_property_range_z_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_light_transform_physics_interpolation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_light_transform_physics_interpolation**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_light_transform_physics_interpolation>`{.interpreted-text
role="ref"}

Transforms both the current and previous stored transform for a canvas
light.

This allows transforming a light without creating a \"glitch\" in the
interpolation, which is particularly useful for large worlds utilizing a
shifting origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_occluder_polygon_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**canvas_occluder_polygon_create**()
`🔗<class_RenderingServer_method_canvas_occluder_polygon_create>`{.interpreted-text
role="ref"}

Creates a new light occluder polygon and adds it to the RenderingServer.
It can be accessed with the RID that is returned. This RID will be used
in all `canvas_occluder_polygon_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`OccluderPolygon2D<class_OccluderPolygon2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_occluder_polygon_set_cull_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_occluder_polygon_set_cull_mode**(occluder_polygon:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`CanvasOccluderPolygonCullMode<enum_RenderingServer_CanvasOccluderPolygonCullMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_occluder_polygon_set_cull_mode>`{.interpreted-text
role="ref"}

Sets an occluder polygon\'s cull mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_occluder_polygon_set_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_occluder_polygon_set_shape**(occluder_polygon:
`RID<class_RID>`{.interpreted-text role="ref"}, shape:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, closed: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_occluder_polygon_set_shape>`{.interpreted-text
role="ref"}

Sets the shape of the occluder polygon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_set_disable_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_set_disable_scale**(disable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_set_disable_scale>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_set_item_mirroring}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_set_item_mirroring**(canvas: `RID<class_RID>`{.interpreted-text
role="ref"}, item: `RID<class_RID>`{.interpreted-text role="ref"},
mirroring: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_set_item_mirroring>`{.interpreted-text
role="ref"}

A copy of the canvas item will be drawn with a local offset of the
`mirroring`.

\*\*Note:\*\* This is equivalent to calling
`canvas_set_item_repeat()<class_RenderingServer_method_canvas_set_item_repeat>`{.interpreted-text
role="ref"} like `canvas_set_item_repeat(item, mirroring, 1)`, with an
additional check ensuring `canvas` is a parent of `item`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_set_item_repeat}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_set_item_repeat**(item: `RID<class_RID>`{.interpreted-text
role="ref"}, repeat_size: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, repeat_times: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_set_item_repeat>`{.interpreted-text
role="ref"}

A copy of the canvas item will be drawn with a local offset of the
`repeat_size` by the number of times of the `repeat_times`. As the
`repeat_times` increases, the copies will spread away from the origin
texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_set_modulate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_set_modulate**(canvas: `RID<class_RID>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_set_modulate>`{.interpreted-text
role="ref"}

Modulates all colors in the given canvas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_set_shadow_texture_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_set_shadow_texture_size**(size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_set_shadow_texture_size>`{.interpreted-text
role="ref"}

Sets the
`ProjectSettings.rendering/2d/shadow_atlas/size<class_ProjectSettings_property_rendering/2d/shadow_atlas/size>`{.interpreted-text
role="ref"} to use for `Light2D<class_Light2D>`{.interpreted-text
role="ref"} shadow rendering (in pixels). The value is rounded up to the
nearest power of 2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_texture_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**canvas_texture_create**()
`🔗<class_RenderingServer_method_canvas_texture_create>`{.interpreted-text
role="ref"}

Creates a canvas texture and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`canvas_texture_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method. See also
`texture_2d_create()<class_RenderingServer_method_texture_2d_create>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The equivalent resource is
`CanvasTexture<class_CanvasTexture>`{.interpreted-text role="ref"} and
is only meant to be used in 2D rendering, not 3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_texture_set_channel}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_texture_set_channel**(canvas_texture:
`RID<class_RID>`{.interpreted-text role="ref"}, channel:
`CanvasTextureChannel<enum_RenderingServer_CanvasTextureChannel>`{.interpreted-text
role="ref"}, texture: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_texture_set_channel>`{.interpreted-text
role="ref"}

Sets the `channel`\'s `texture` for the canvas texture specified by the
`canvas_texture` RID. Equivalent to
`CanvasTexture.diffuse_texture<class_CanvasTexture_property_diffuse_texture>`{.interpreted-text
role="ref"},
`CanvasTexture.normal_texture<class_CanvasTexture_property_normal_texture>`{.interpreted-text
role="ref"} and
`CanvasTexture.specular_texture<class_CanvasTexture_property_specular_texture>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_texture_set_shading_parameters}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_texture_set_shading_parameters**(canvas_texture:
`RID<class_RID>`{.interpreted-text role="ref"}, base_color:
`Color<class_Color>`{.interpreted-text role="ref"}, shininess:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_canvas_texture_set_shading_parameters>`{.interpreted-text
role="ref"}

Sets the `base_color` and `shininess` to use for the canvas texture
specified by the `canvas_texture` RID. Equivalent to
`CanvasTexture.specular_color<class_CanvasTexture_property_specular_color>`{.interpreted-text
role="ref"} and
`CanvasTexture.specular_shininess<class_CanvasTexture_property_specular_shininess>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_texture_set_texture_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_texture_set_texture_filter**(canvas_texture:
`RID<class_RID>`{.interpreted-text role="ref"}, filter:
`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_texture_set_texture_filter>`{.interpreted-text
role="ref"}

Sets the texture `filter` mode to use for the canvas texture specified
by the `canvas_texture` RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_canvas_texture_set_texture_repeat}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**canvas_texture_set_texture_repeat**(canvas_texture:
`RID<class_RID>`{.interpreted-text role="ref"}, repeat:
`CanvasItemTextureRepeat<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_canvas_texture_set_texture_repeat>`{.interpreted-text
role="ref"}

Sets the texture `repeat` mode to use for the canvas texture specified
by the `canvas_texture` RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_compositor_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **compositor_create**()
`🔗<class_RenderingServer_method_compositor_create>`{.interpreted-text
role="ref"}

Creates a new compositor and adds it to the RenderingServer. It can be
accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_compositor_effect_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**compositor_effect_create**()
`🔗<class_RenderingServer_method_compositor_effect_create>`{.interpreted-text
role="ref"}

Creates a new rendering effect and adds it to the RenderingServer. It
can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_compositor_effect_set_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compositor_effect_set_callback**(effect:
`RID<class_RID>`{.interpreted-text role="ref"}, callback_type:
`CompositorEffectCallbackType<enum_RenderingServer_CompositorEffectCallbackType>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_compositor_effect_set_callback>`{.interpreted-text
role="ref"}

Sets the callback type (`callback_type`) and callback method(`callback`)
for this rendering effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_compositor_effect_set_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compositor_effect_set_enabled**(effect:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_compositor_effect_set_enabled>`{.interpreted-text
role="ref"}

Enables/disables this rendering effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_compositor_effect_set_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compositor_effect_set_flag**(effect:
`RID<class_RID>`{.interpreted-text role="ref"}, flag:
`CompositorEffectFlags<enum_RenderingServer_CompositorEffectFlags>`{.interpreted-text
role="ref"}, set: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_compositor_effect_set_flag>`{.interpreted-text
role="ref"}

Sets the flag (`flag`) for this rendering effect to `true` or `false`
(`set`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_compositor_set_compositor_effects}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compositor_set_compositor_effects**(compositor:
`RID<class_RID>`{.interpreted-text role="ref"}, effects:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\])
`🔗<class_RenderingServer_method_compositor_set_compositor_effects>`{.interpreted-text
role="ref"}

Sets the compositor effects for the specified compositor RID. `effects`
should be an array containing RIDs created with
`compositor_effect_create()<class_RenderingServer_method_compositor_effect_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_create_local_rendering_device}
::: rst-class
classref-method
:::
::::

`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}
**create_local_rendering_device**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_create_local_rendering_device>`{.interpreted-text
role="ref"}

Creates a RenderingDevice that can be used to do draw and compute
operations on a separate thread. Cannot draw to the screen nor share
data with the global RenderingDevice.

\*\*Note:\*\* When using the OpenGL rendering driver or when running in
headless mode, this function always returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_debug_canvas_item_get_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**debug_canvas_item_get_rect**(item: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_debug_canvas_item_get_rect>`{.interpreted-text
role="ref"}

Returns the bounding rectangle for a canvas item in local space, as
calculated by the renderer. This bound is used internally for culling.

\*\*Warning:\*\* This function is intended for debugging in the editor,
and will pass through and return a zero
`Rect2<class_Rect2>`{.interpreted-text role="ref"} in exported projects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **decal_create**()
`🔗<class_RenderingServer_method_decal_create>`{.interpreted-text
role="ref"}

Creates a decal and adds it to the RenderingServer. It can be accessed
with the RID that is returned. This RID will be used in all `decal_*`
RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

To place in a scene, attach this decal to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"} using the returned RID.

\*\*Note:\*\* The equivalent node is
`Decal<class_Decal>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_set_albedo_mix}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decal_set_albedo_mix**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, albedo_mix: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_decal_set_albedo_mix>`{.interpreted-text
role="ref"}

Sets the `albedo_mix` in the decal specified by the `decal` RID.
Equivalent to
`Decal.albedo_mix<class_Decal_property_albedo_mix>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_set_cull_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decal_set_cull_mask**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_decal_set_cull_mask>`{.interpreted-text
role="ref"}

Sets the cull `mask` in the decal specified by the `decal` RID.
Equivalent to
`Decal.cull_mask<class_Decal_property_cull_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_set_distance_fade}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decal_set_distance_fade**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"},
begin: `float<class_float>`{.interpreted-text role="ref"}, length:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_decal_set_distance_fade>`{.interpreted-text
role="ref"}

Sets the distance fade parameters in the decal specified by the `decal`
RID. Equivalent to
`Decal.distance_fade_enabled<class_Decal_property_distance_fade_enabled>`{.interpreted-text
role="ref"},
`Decal.distance_fade_begin<class_Decal_property_distance_fade_begin>`{.interpreted-text
role="ref"} and
`Decal.distance_fade_length<class_Decal_property_distance_fade_length>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_set_emission_energy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decal_set_emission_energy**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, energy: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_decal_set_emission_energy>`{.interpreted-text
role="ref"}

Sets the emission `energy` in the decal specified by the `decal` RID.
Equivalent to
`Decal.emission_energy<class_Decal_property_emission_energy>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_set_fade}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decal_set_fade**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, above: `float<class_float>`{.interpreted-text role="ref"},
below: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_decal_set_fade>`{.interpreted-text
role="ref"}

Sets the upper fade (`above`) and lower fade (`below`) in the decal
specified by the `decal` RID. Equivalent to
`Decal.upper_fade<class_Decal_property_upper_fade>`{.interpreted-text
role="ref"} and
`Decal.lower_fade<class_Decal_property_lower_fade>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_set_modulate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decal_set_modulate**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_decal_set_modulate>`{.interpreted-text
role="ref"}

Sets the color multiplier in the decal specified by the `decal` RID to
`color`. Equivalent to
`Decal.modulate<class_Decal_property_modulate>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_set_normal_fade}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decal_set_normal_fade**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, fade: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_decal_set_normal_fade>`{.interpreted-text
role="ref"}

Sets the normal `fade` in the decal specified by the `decal` RID.
Equivalent to
`Decal.normal_fade<class_Decal_property_normal_fade>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_set_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decal_set_size**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_decal_set_size>`{.interpreted-text
role="ref"}

Sets the `size` of the decal specified by the `decal` RID. Equivalent to
`Decal.size<class_Decal_property_size>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decal_set_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decal_set_texture**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, type:
`DecalTexture<enum_RenderingServer_DecalTexture>`{.interpreted-text
role="ref"}, texture: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_decal_set_texture>`{.interpreted-text
role="ref"}

Sets the `texture` in the given texture `type` slot for the specified
decal. Equivalent to
`Decal.set_texture()<class_Decal_method_set_texture>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_decals_set_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**decals_set_filter**(filter:
`DecalFilter<enum_RenderingServer_DecalFilter>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_decals_set_filter>`{.interpreted-text
role="ref"}

Sets the texture `filter` mode to use when rendering decals. This
parameter is global and cannot be set on a per-decal basis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_directional_light_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**directional_light_create**()
`🔗<class_RenderingServer_method_directional_light_create>`{.interpreted-text
role="ref"}

Creates a directional light and adds it to the RenderingServer. It can
be accessed with the RID that is returned. This RID can be used in most
`light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

To place in a scene, attach this directional light to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"} using the returned RID.

\*\*Note:\*\* The equivalent node is
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_directional_shadow_atlas_set_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**directional_shadow_atlas_set_size**(size:
`int<class_int>`{.interpreted-text role="ref"}, is_16bits:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_directional_shadow_atlas_set_size>`{.interpreted-text
role="ref"}

Sets the `size` of the directional light shadows in 3D. See also
`ProjectSettings.rendering/lights_and_shadows/directional_shadow/size<class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/size>`{.interpreted-text
role="ref"}. This parameter is global and cannot be set on a
per-viewport basis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_directional_soft_shadow_filter_set_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**directional_soft_shadow_filter_set_quality**(quality:
`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_directional_soft_shadow_filter_set_quality>`{.interpreted-text
role="ref"}

Sets the filter `quality` for directional light shadows in 3D. See also
`ProjectSettings.rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality<class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality>`{.interpreted-text
role="ref"}. This parameter is global and cannot be set on a
per-viewport basis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_bake_panorama}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**environment_bake_panorama**(environment:
`RID<class_RID>`{.interpreted-text role="ref"}, bake_irradiance:
`bool<class_bool>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_bake_panorama>`{.interpreted-text
role="ref"}

Generates and returns an `Image<class_Image>`{.interpreted-text
role="ref"} containing the radiance map for the specified `environment`
RID\'s sky. This supports built-in sky material and custom sky shaders.
If `bake_irradiance` is `true`, the irradiance map is saved instead of
the radiance map. The radiance map is used to render reflected light,
while the irradiance map is used to render ambient light. See also
`sky_bake_panorama()<class_RenderingServer_method_sky_bake_panorama>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The image is saved in linear color space without any
tonemapping performed, which means it will look too dark if viewed
directly in an image editor.

\*\*Note:\*\* `size` should be a 2:1 aspect ratio for the generated
panorama to have square pixels. For radiance maps, there is no point in
using a height greater than
`Sky.radiance_size<class_Sky_property_radiance_size>`{.interpreted-text
role="ref"}, as it won\'t increase detail. Irradiance maps only contain
low-frequency data, so there is usually no point in going past a size of
128×64 pixels when saving an irradiance map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **environment_create**()
`🔗<class_RenderingServer_method_environment_create>`{.interpreted-text
role="ref"}

Creates an environment and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`environment_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`Environment<class_Environment>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_glow_set_use_bicubic_upscale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_glow_set_use_bicubic_upscale**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_glow_set_use_bicubic_upscale>`{.interpreted-text
role="ref"}

If `enable` is `true`, enables bicubic upscaling for glow which improves
quality at the cost of performance. Equivalent to
`ProjectSettings.rendering/environment/glow/upscale_mode<class_ProjectSettings_property_rendering/environment/glow/upscale_mode>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This setting is only effective when using the Forward+ or
Mobile rendering methods, as Compatibility uses a different glow
implementation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_adjustment}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_adjustment**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"},
brightness: `float<class_float>`{.interpreted-text role="ref"},
contrast: `float<class_float>`{.interpreted-text role="ref"},
saturation: `float<class_float>`{.interpreted-text role="ref"},
use_1d_color_correction: `bool<class_bool>`{.interpreted-text
role="ref"}, color_correction: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_adjustment>`{.interpreted-text
role="ref"}

Sets the values to be used with the \"adjustments\" post-process effect.
See `Environment<class_Environment>`{.interpreted-text role="ref"} for
more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_ambient_light}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_ambient_light**(env:
`RID<class_RID>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"}, ambient:
`EnvironmentAmbientSource<enum_RenderingServer_EnvironmentAmbientSource>`{.interpreted-text
role="ref"} = 0, energy: `float<class_float>`{.interpreted-text
role="ref"} = 1.0, sky_contribution:
`float<class_float>`{.interpreted-text role="ref"} = 0.0,
reflection_source:
`EnvironmentReflectionSource<enum_RenderingServer_EnvironmentReflectionSource>`{.interpreted-text
role="ref"} = 0)
`🔗<class_RenderingServer_method_environment_set_ambient_light>`{.interpreted-text
role="ref"}

Sets the values to be used for ambient light rendering. See
`Environment<class_Environment>`{.interpreted-text role="ref"} for more
details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_background}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_background**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, bg:
`EnvironmentBG<enum_RenderingServer_EnvironmentBG>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_background>`{.interpreted-text
role="ref"}

Sets the environment\'s background mode. Equivalent to
`Environment.background_mode<class_Environment_property_background_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_bg_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_bg_color**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_bg_color>`{.interpreted-text
role="ref"}

Color displayed for clear areas of the scene. Only effective if using
the
`ENV_BG_COLOR<class_RenderingServer_constant_ENV_BG_COLOR>`{.interpreted-text
role="ref"} background mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_bg_energy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_bg_energy**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, multiplier: `float<class_float>`{.interpreted-text
role="ref"}, exposure_value: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_bg_energy>`{.interpreted-text
role="ref"}

Sets the intensity of the background color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_camera_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_camera_id**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_camera_id>`{.interpreted-text
role="ref"}

Sets the camera ID to be used as environment background.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_canvas_max_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_canvas_max_layer**(env:
`RID<class_RID>`{.interpreted-text role="ref"}, max_layer:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_canvas_max_layer>`{.interpreted-text
role="ref"}

Sets the maximum layer to use if using Canvas background mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_fog}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_fog**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"},
light_color: `Color<class_Color>`{.interpreted-text role="ref"},
light_energy: `float<class_float>`{.interpreted-text role="ref"},
sun_scatter: `float<class_float>`{.interpreted-text role="ref"},
density: `float<class_float>`{.interpreted-text role="ref"}, height:
`float<class_float>`{.interpreted-text role="ref"}, height_density:
`float<class_float>`{.interpreted-text role="ref"}, aerial_perspective:
`float<class_float>`{.interpreted-text role="ref"}, sky_affect:
`float<class_float>`{.interpreted-text role="ref"}, fog_mode:
`EnvironmentFogMode<enum_RenderingServer_EnvironmentFogMode>`{.interpreted-text
role="ref"} = 0)
`🔗<class_RenderingServer_method_environment_set_fog>`{.interpreted-text
role="ref"}

Configures fog for the specified environment RID. See `fog_*` properties
in `Environment<class_Environment>`{.interpreted-text role="ref"} for
more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_fog_depth}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_fog_depth**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, curve: `float<class_float>`{.interpreted-text role="ref"},
begin: `float<class_float>`{.interpreted-text role="ref"}, end:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_fog_depth>`{.interpreted-text
role="ref"}

Configures fog depth for the specified environment RID. Only has an
effect when the fog mode of the environment is
`ENV_FOG_MODE_DEPTH<class_RenderingServer_constant_ENV_FOG_MODE_DEPTH>`{.interpreted-text
role="ref"}. See `fog_depth_*` properties in
`Environment<class_Environment>`{.interpreted-text role="ref"} for more
information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_glow}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_glow**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"},
levels: `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}, intensity: `float<class_float>`{.interpreted-text
role="ref"}, strength: `float<class_float>`{.interpreted-text
role="ref"}, mix: `float<class_float>`{.interpreted-text role="ref"},
bloom_threshold: `float<class_float>`{.interpreted-text role="ref"},
blend_mode:
`EnvironmentGlowBlendMode<enum_RenderingServer_EnvironmentGlowBlendMode>`{.interpreted-text
role="ref"}, hdr_bleed_threshold: `float<class_float>`{.interpreted-text
role="ref"}, hdr_bleed_scale: `float<class_float>`{.interpreted-text
role="ref"}, hdr_luminance_cap: `float<class_float>`{.interpreted-text
role="ref"}, glow_map_strength: `float<class_float>`{.interpreted-text
role="ref"}, glow_map: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_glow>`{.interpreted-text
role="ref"}

Configures glow for the specified environment RID. See `glow_*`
properties in `Environment<class_Environment>`{.interpreted-text
role="ref"} for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_sdfgi}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_sdfgi**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"},
cascades: `int<class_int>`{.interpreted-text role="ref"}, min_cell_size:
`float<class_float>`{.interpreted-text role="ref"}, y_scale:
`EnvironmentSDFGIYScale<enum_RenderingServer_EnvironmentSDFGIYScale>`{.interpreted-text
role="ref"}, use_occlusion: `bool<class_bool>`{.interpreted-text
role="ref"}, bounce_feedback: `float<class_float>`{.interpreted-text
role="ref"}, read_sky: `bool<class_bool>`{.interpreted-text role="ref"},
energy: `float<class_float>`{.interpreted-text role="ref"}, normal_bias:
`float<class_float>`{.interpreted-text role="ref"}, probe_bias:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_sdfgi>`{.interpreted-text
role="ref"}

Configures signed distance field global illumination for the specified
environment RID. See `sdfgi_*` properties in
`Environment<class_Environment>`{.interpreted-text role="ref"} for more
information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_sdfgi_frames_to_converge}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_sdfgi_frames_to_converge**(frames:
`EnvironmentSDFGIFramesToConverge<enum_RenderingServer_EnvironmentSDFGIFramesToConverge>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_sdfgi_frames_to_converge>`{.interpreted-text
role="ref"}

Sets the number of frames to use for converging signed distance field
global illumination. Equivalent to
`ProjectSettings.rendering/global_illumination/sdfgi/frames_to_converge<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_converge>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_sdfgi_frames_to_update_light}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_sdfgi_frames_to_update_light**(frames:
`EnvironmentSDFGIFramesToUpdateLight<enum_RenderingServer_EnvironmentSDFGIFramesToUpdateLight>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_sdfgi_frames_to_update_light>`{.interpreted-text
role="ref"}

Sets the update speed for dynamic lights\' indirect lighting when
computing signed distance field global illumination. Equivalent to
`ProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_update_lights>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_sdfgi_ray_count}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_sdfgi_ray_count**(ray_count:
`EnvironmentSDFGIRayCount<enum_RenderingServer_EnvironmentSDFGIRayCount>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_sdfgi_ray_count>`{.interpreted-text
role="ref"}

Sets the number of rays to throw per frame when computing signed
distance field global illumination. Equivalent to
`ProjectSettings.rendering/global_illumination/sdfgi/probe_ray_count<class_ProjectSettings_property_rendering/global_illumination/sdfgi/probe_ray_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_sky}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_sky**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, sky: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_sky>`{.interpreted-text
role="ref"}

Sets the `Sky<class_Sky>`{.interpreted-text role="ref"} to be used as
the environment\'s background when using *BGMode* sky. Equivalent to
`Environment.sky<class_Environment_property_sky>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_sky_custom_fov}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_sky_custom_fov**(env:
`RID<class_RID>`{.interpreted-text role="ref"}, scale:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_sky_custom_fov>`{.interpreted-text
role="ref"}

Sets a custom field of view for the background
`Sky<class_Sky>`{.interpreted-text role="ref"}. Equivalent to
`Environment.sky_custom_fov<class_Environment_property_sky_custom_fov>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_sky_orientation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_sky_orientation**(env:
`RID<class_RID>`{.interpreted-text role="ref"}, orientation:
`Basis<class_Basis>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_sky_orientation>`{.interpreted-text
role="ref"}

Sets the rotation of the background `Sky<class_Sky>`{.interpreted-text
role="ref"} expressed as a `Basis<class_Basis>`{.interpreted-text
role="ref"}. Equivalent to
`Environment.sky_rotation<class_Environment_property_sky_rotation>`{.interpreted-text
role="ref"}, where the rotation vector is used to construct the
`Basis<class_Basis>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_ssao}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_ssao**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"},
radius: `float<class_float>`{.interpreted-text role="ref"}, intensity:
`float<class_float>`{.interpreted-text role="ref"}, power:
`float<class_float>`{.interpreted-text role="ref"}, detail:
`float<class_float>`{.interpreted-text role="ref"}, horizon:
`float<class_float>`{.interpreted-text role="ref"}, sharpness:
`float<class_float>`{.interpreted-text role="ref"}, light_affect:
`float<class_float>`{.interpreted-text role="ref"}, ao_channel_affect:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_ssao>`{.interpreted-text
role="ref"}

Sets the variables to be used with the screen-space ambient occlusion
(SSAO) post-process effect. See
`Environment<class_Environment>`{.interpreted-text role="ref"} for more
details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_ssao_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_ssao_quality**(quality:
`EnvironmentSSAOQuality<enum_RenderingServer_EnvironmentSSAOQuality>`{.interpreted-text
role="ref"}, half_size: `bool<class_bool>`{.interpreted-text
role="ref"}, adaptive_target: `float<class_float>`{.interpreted-text
role="ref"}, blur_passes: `int<class_int>`{.interpreted-text
role="ref"}, fadeout_from: `float<class_float>`{.interpreted-text
role="ref"}, fadeout_to: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_ssao_quality>`{.interpreted-text
role="ref"}

Sets the quality level of the screen-space ambient occlusion (SSAO)
post-process effect. See
`Environment<class_Environment>`{.interpreted-text role="ref"} for more
details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_ssil_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_ssil_quality**(quality:
`EnvironmentSSILQuality<enum_RenderingServer_EnvironmentSSILQuality>`{.interpreted-text
role="ref"}, half_size: `bool<class_bool>`{.interpreted-text
role="ref"}, adaptive_target: `float<class_float>`{.interpreted-text
role="ref"}, blur_passes: `int<class_int>`{.interpreted-text
role="ref"}, fadeout_from: `float<class_float>`{.interpreted-text
role="ref"}, fadeout_to: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_ssil_quality>`{.interpreted-text
role="ref"}

Sets the quality level of the screen-space indirect lighting (SSIL)
post-process effect. See
`Environment<class_Environment>`{.interpreted-text role="ref"} for more
details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_ssr}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_ssr**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"},
max_steps: `int<class_int>`{.interpreted-text role="ref"}, fade_in:
`float<class_float>`{.interpreted-text role="ref"}, fade_out:
`float<class_float>`{.interpreted-text role="ref"}, depth_tolerance:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_ssr>`{.interpreted-text
role="ref"}

Sets the variables to be used with the screen-space reflections (SSR)
post-process effect. See
`Environment<class_Environment>`{.interpreted-text role="ref"} for more
details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_ssr_roughness_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_ssr_roughness_quality**(quality:
`EnvironmentSSRRoughnessQuality<enum_RenderingServer_EnvironmentSSRRoughnessQuality>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_ssr_roughness_quality>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_tonemap}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_tonemap**(env: `RID<class_RID>`{.interpreted-text
role="ref"}, tone_mapper:
`EnvironmentToneMapper<enum_RenderingServer_EnvironmentToneMapper>`{.interpreted-text
role="ref"}, exposure: `float<class_float>`{.interpreted-text
role="ref"}, white: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_tonemap>`{.interpreted-text
role="ref"}

Sets the variables to be used with the \"tonemap\" post-process effect.
See `Environment<class_Environment>`{.interpreted-text role="ref"} for
more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_volumetric_fog}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_volumetric_fog**(env:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"}, density:
`float<class_float>`{.interpreted-text role="ref"}, albedo:
`Color<class_Color>`{.interpreted-text role="ref"}, emission:
`Color<class_Color>`{.interpreted-text role="ref"}, emission_energy:
`float<class_float>`{.interpreted-text role="ref"}, anisotropy:
`float<class_float>`{.interpreted-text role="ref"}, length:
`float<class_float>`{.interpreted-text role="ref"}, p_detail_spread:
`float<class_float>`{.interpreted-text role="ref"}, gi_inject:
`float<class_float>`{.interpreted-text role="ref"},
temporal_reprojection: `bool<class_bool>`{.interpreted-text role="ref"},
temporal_reprojection_amount: `float<class_float>`{.interpreted-text
role="ref"}, ambient_inject: `float<class_float>`{.interpreted-text
role="ref"}, sky_affect: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_environment_set_volumetric_fog>`{.interpreted-text
role="ref"}

Sets the variables to be used with the volumetric fog post-process
effect. See `Environment<class_Environment>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_volumetric_fog_filter_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_volumetric_fog_filter_active**(active:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_volumetric_fog_filter_active>`{.interpreted-text
role="ref"}

Enables filtering of the volumetric fog scattering buffer. This results
in much smoother volumes with very few under-sampling artifacts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_environment_set_volumetric_fog_volume_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**environment_set_volumetric_fog_volume_size**(size:
`int<class_int>`{.interpreted-text role="ref"}, depth:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_environment_set_volumetric_fog_volume_size>`{.interpreted-text
role="ref"}

Sets the resolution of the volumetric fog\'s froxel buffer. `size` is
modified by the screen\'s aspect ratio and then used to set the width
and height of the buffer. While `depth` is directly used to set the
depth of the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_fog_volume_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **fog_volume_create**()
`🔗<class_RenderingServer_method_fog_volume_create>`{.interpreted-text
role="ref"}

Creates a new fog volume and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`fog_volume_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent node is
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_fog_volume_set_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fog_volume_set_material**(fog_volume:
`RID<class_RID>`{.interpreted-text role="ref"}, material:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_fog_volume_set_material>`{.interpreted-text
role="ref"}

Sets the `Material<class_Material>`{.interpreted-text role="ref"} of the
fog volume. Can be either a
`FogMaterial<class_FogMaterial>`{.interpreted-text role="ref"} or a
custom `ShaderMaterial<class_ShaderMaterial>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_fog_volume_set_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fog_volume_set_shape**(fog_volume: `RID<class_RID>`{.interpreted-text
role="ref"}, shape:
`FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_fog_volume_set_shape>`{.interpreted-text
role="ref"}

Sets the shape of the fog volume to either
`FOG_VOLUME_SHAPE_ELLIPSOID<class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID>`{.interpreted-text
role="ref"},
`FOG_VOLUME_SHAPE_CONE<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE>`{.interpreted-text
role="ref"},
`FOG_VOLUME_SHAPE_CYLINDER<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER>`{.interpreted-text
role="ref"},
`FOG_VOLUME_SHAPE_BOX<class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX>`{.interpreted-text
role="ref"} or
`FOG_VOLUME_SHAPE_WORLD<class_RenderingServer_constant_FOG_VOLUME_SHAPE_WORLD>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_fog_volume_set_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fog_volume_set_size**(fog_volume: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_fog_volume_set_size>`{.interpreted-text
role="ref"}

Sets the size of the fog volume when shape is
`FOG_VOLUME_SHAPE_ELLIPSOID<class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID>`{.interpreted-text
role="ref"},
`FOG_VOLUME_SHAPE_CONE<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE>`{.interpreted-text
role="ref"},
`FOG_VOLUME_SHAPE_CYLINDER<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER>`{.interpreted-text
role="ref"} or
`FOG_VOLUME_SHAPE_BOX<class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_force_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_draw**(swap_buffers: `bool<class_bool>`{.interpreted-text
role="ref"} = true, frame_step: `float<class_float>`{.interpreted-text
role="ref"} = 0.0)
`🔗<class_RenderingServer_method_force_draw>`{.interpreted-text
role="ref"}

Forces redrawing of all viewports at once. Must be called from the main
thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_force_sync}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_sync**()
`🔗<class_RenderingServer_method_force_sync>`{.interpreted-text
role="ref"}

Forces a synchronization between the CPU and GPU, which may be required
in certain cases. Only call this when needed, as CPU-GPU synchronization
has a performance cost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_free_rid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**free_rid**(rid: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"}

Tries to free an object in the RenderingServer. To avoid memory leaks,
this should be called after using an object as memory management does
not occur automatically when using RenderingServer directly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_current_rendering_driver_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_current_rendering_driver_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_get_current_rendering_driver_name>`{.interpreted-text
role="ref"}

Returns the name of the current rendering driver. This can be `vulkan`,
`d3d12`, `metal`, `opengl3`, `opengl3_es`, or `opengl3_angle`. See also
`get_current_rendering_method()<class_RenderingServer_method_get_current_rendering_method>`{.interpreted-text
role="ref"}.

The rendering driver is determined by
`ProjectSettings.rendering/rendering_device/driver<class_ProjectSettings_property_rendering/rendering_device/driver>`{.interpreted-text
role="ref"}, the `--rendering-driver` command line argument that
overrides this project setting, or an automatic fallback that is applied
depending on the hardware.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_current_rendering_method}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_current_rendering_method**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_get_current_rendering_method>`{.interpreted-text
role="ref"}

Returns the name of the current rendering method. This can be
`forward_plus`, `mobile`, or `gl_compatibility`. See also
`get_current_rendering_driver_name()<class_RenderingServer_method_get_current_rendering_driver_name>`{.interpreted-text
role="ref"}.

The rendering method is determined by
`ProjectSettings.rendering/renderer/rendering_method<class_ProjectSettings_property_rendering/renderer/rendering_method>`{.interpreted-text
role="ref"}, the `--rendering-method` command line argument that
overrides this project setting, or an automatic fallback that is applied
depending on the hardware.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_default_clear_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_default_clear_color**()
`🔗<class_RenderingServer_method_get_default_clear_color>`{.interpreted-text
role="ref"}

Returns the default clear color which is used when a specific clear
color has not been selected. See also
`set_default_clear_color()<class_RenderingServer_method_set_default_clear_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_frame_setup_time_cpu}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_frame_setup_time_cpu**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_get_frame_setup_time_cpu>`{.interpreted-text
role="ref"}

Returns the time taken to setup rendering on the CPU in milliseconds.
This value is shared across all viewports and does *not* require
`viewport_set_measure_render_time()<class_RenderingServer_method_viewport_set_measure_render_time>`{.interpreted-text
role="ref"} to be enabled on a viewport to be queried. See also
`viewport_get_measured_render_time_cpu()<class_RenderingServer_method_viewport_get_measured_render_time_cpu>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_rendering_device}
::: rst-class
classref-method
:::
::::

`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}
**get_rendering_device**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_get_rendering_device>`{.interpreted-text
role="ref"}

Returns the global RenderingDevice.

\*\*Note:\*\* When using the OpenGL rendering driver or when running in
headless mode, this function always returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_rendering_info}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_rendering_info**(info:
`RenderingInfo<enum_RenderingServer_RenderingInfo>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_get_rendering_info>`{.interpreted-text
role="ref"}

Returns a statistic about the rendering engine which can be used for
performance profiling. See also
`viewport_get_render_info()<class_RenderingServer_method_viewport_get_render_info>`{.interpreted-text
role="ref"}, which returns information specific to a viewport.

\*\*Note:\*\* Only 3D rendering is currently taken into account by some
of these values, such as the number of draw calls.

\*\*Note:\*\* Rendering information is not available until at least 2
frames have been rendered by the engine. If rendering information is not
available,
`get_rendering_info()<class_RenderingServer_method_get_rendering_info>`{.interpreted-text
role="ref"} returns `0`. To print rendering information in `_ready()`
successfully, use the following:

    func _ready():
        for _i in 2:
            await get_tree().process_frame

        print(RenderingServer.get_rendering_info(RENDERING_INFO_TOTAL_DRAW_CALLS_IN_FRAME))

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_shader_parameter_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_shader_parameter_list**(shader:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_get_shader_parameter_list>`{.interpreted-text
role="ref"}

Returns the parameters of a shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_test_cube}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_test_cube**()
`🔗<class_RenderingServer_method_get_test_cube>`{.interpreted-text
role="ref"}

Returns the RID of the test cube. This mesh will be created and returned
on the first call to
`get_test_cube()<class_RenderingServer_method_get_test_cube>`{.interpreted-text
role="ref"}, then it will be cached for subsequent calls. See also
`make_sphere_mesh()<class_RenderingServer_method_make_sphere_mesh>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_test_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_test_texture**()
`🔗<class_RenderingServer_method_get_test_texture>`{.interpreted-text
role="ref"}

Returns the RID of a 256×256 texture with a testing pattern on it (in
`Image.FORMAT_RGB8<class_Image_constant_FORMAT_RGB8>`{.interpreted-text
role="ref"} format). This texture will be created and returned on the
first call to
`get_test_texture()<class_RenderingServer_method_get_test_texture>`{.interpreted-text
role="ref"}, then it will be cached for subsequent calls. See also
`get_white_texture()<class_RenderingServer_method_get_white_texture>`{.interpreted-text
role="ref"}.

\*\*Example:\*\* Get the test texture and apply it to a
`Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"} node:

    var texture_rid = RenderingServer.get_test_texture()
    var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
    $Sprite2D.texture = texture

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_video_adapter_api_version}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_video_adapter_api_version**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_get_video_adapter_api_version>`{.interpreted-text
role="ref"}

Returns the version of the graphics video adapter *currently in use*
(e.g. \"1.2.189\" for Vulkan, \"3.3.0 NVIDIA 510.60.02\" for OpenGL).
This version may be different from the actual latest version supported
by the hardware, as Godot may not always request the latest version. See
also
`OS.get_video_adapter_driver_info()<class_OS_method_get_video_adapter_driver_info>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When running a headless or server binary, this function
returns an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_video_adapter_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_video_adapter_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_get_video_adapter_name>`{.interpreted-text
role="ref"}

Returns the name of the video adapter (e.g. \"GeForce GTX
1080/PCIe/SSE2\").

\*\*Note:\*\* When running a headless or server binary, this function
returns an empty string.

\*\*Note:\*\* On the web platform, some browsers such as Firefox may
report a different, fixed GPU name such as \"GeForce GTX 980\"
(regardless of the user\'s actual GPU model). This is done to make
fingerprinting more difficult.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_video_adapter_type}
::: rst-class
classref-method
:::
::::

`DeviceType<enum_RenderingDevice_DeviceType>`{.interpreted-text
role="ref"} **get_video_adapter_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_get_video_adapter_type>`{.interpreted-text
role="ref"}

Returns the type of the video adapter. Since dedicated graphics cards
from a given generation will *usually* be significantly faster than
integrated graphics made in the same generation, the device type can be
used as a basis for automatic graphics settings adjustment. However,
this is not always true, so make sure to provide users with a way to
manually override graphics settings.

\*\*Note:\*\* When using the OpenGL rendering driver or when running in
headless mode, this function always returns
`RenderingDevice.DEVICE_TYPE_OTHER<class_RenderingDevice_constant_DEVICE_TYPE_OTHER>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_video_adapter_vendor}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_video_adapter_vendor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_get_video_adapter_vendor>`{.interpreted-text
role="ref"}

Returns the vendor of the video adapter (e.g. \"NVIDIA Corporation\").

\*\*Note:\*\* When running a headless or server binary, this function
returns an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_get_white_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_white_texture**()
`🔗<class_RenderingServer_method_get_white_texture>`{.interpreted-text
role="ref"}

Returns the ID of a 4×4 white texture (in
`Image.FORMAT_RGB8<class_Image_constant_FORMAT_RGB8>`{.interpreted-text
role="ref"} format). This texture will be created and returned on the
first call to
`get_white_texture()<class_RenderingServer_method_get_white_texture>`{.interpreted-text
role="ref"}, then it will be cached for subsequent calls. See also
`get_test_texture()<class_RenderingServer_method_get_test_texture>`{.interpreted-text
role="ref"}.

\*\*Example:\*\* Get the white texture and apply it to a
`Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"} node:

    var texture_rid = RenderingServer.get_white_texture()
    var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
    $Sprite2D.texture = texture

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_gi_set_use_half_resolution}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**gi_set_use_half_resolution**(half_resolution:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_gi_set_use_half_resolution>`{.interpreted-text
role="ref"}

If `half_resolution` is `true`, renders
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} and SDFGI
(`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}) buffers at halved resolution on each axis (e.g. 960×540
when the viewport size is 1920×1080). This improves performance
significantly when VoxelGI or SDFGI is enabled, at the cost of artifacts
that may be visible on polygon edges. The loss in quality becomes less
noticeable as the viewport resolution increases.
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} rendering
is not affected by this setting. Equivalent to
`ProjectSettings.rendering/global_illumination/gi/use_half_resolution<class_ProjectSettings_property_rendering/global_illumination/gi/use_half_resolution>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_global_shader_parameter_add}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_shader_parameter_add**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, type:
`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"}, default_value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_global_shader_parameter_add>`{.interpreted-text
role="ref"}

Creates a new global shader uniform.

\*\*Note:\*\* Global shader parameter names are case-sensitive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_global_shader_parameter_get}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**global_shader_parameter_get**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_global_shader_parameter_get>`{.interpreted-text
role="ref"}

Returns the value of the global shader uniform specified by `name`.

\*\*Note:\*\*
`global_shader_parameter_get()<class_RenderingServer_method_global_shader_parameter_get>`{.interpreted-text
role="ref"} has a large performance penalty as the rendering thread
needs to synchronize with the calling thread, which is slow. Do not use
this method during gameplay to avoid stuttering. If you need to read
values in a script after setting them, consider creating an autoload
where you store the values you need to query at the same time you\'re
setting them as global parameters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_global_shader_parameter_get_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **global_shader_parameter_get_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_global_shader_parameter_get_list>`{.interpreted-text
role="ref"}

Returns the list of global shader uniform names.

\*\*Note:\*\*
`global_shader_parameter_get()<class_RenderingServer_method_global_shader_parameter_get>`{.interpreted-text
role="ref"} has a large performance penalty as the rendering thread
needs to synchronize with the calling thread, which is slow. Do not use
this method during gameplay to avoid stuttering. If you need to read
values in a script after setting them, consider creating an autoload
where you store the values you need to query at the same time you\'re
setting them as global parameters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_global_shader_parameter_get_type}
::: rst-class
classref-method
:::
::::

`GlobalShaderParameterType<enum_RenderingServer_GlobalShaderParameterType>`{.interpreted-text
role="ref"} **global_shader_parameter_get_type**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_global_shader_parameter_get_type>`{.interpreted-text
role="ref"}

Returns the type associated to the global shader uniform specified by
`name`.

\*\*Note:\*\*
`global_shader_parameter_get()<class_RenderingServer_method_global_shader_parameter_get>`{.interpreted-text
role="ref"} has a large performance penalty as the rendering thread
needs to synchronize with the calling thread, which is slow. Do not use
this method during gameplay to avoid stuttering. If you need to read
values in a script after setting them, consider creating an autoload
where you store the values you need to query at the same time you\'re
setting them as global parameters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_global_shader_parameter_remove}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_shader_parameter_remove**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_global_shader_parameter_remove>`{.interpreted-text
role="ref"}

Removes the global shader uniform specified by `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_global_shader_parameter_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_shader_parameter_set**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_global_shader_parameter_set>`{.interpreted-text
role="ref"}

Sets the global shader uniform `name` to `value`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_global_shader_parameter_set_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**global_shader_parameter_set_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_global_shader_parameter_set_override>`{.interpreted-text
role="ref"}

Overrides the global shader uniform `name` with `value`. Equivalent to
the
`ShaderGlobalsOverride<class_ShaderGlobalsOverride>`{.interpreted-text
role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_has_changed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_changed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_has_changed>`{.interpreted-text
role="ref"}

Returns `true` if changes have been made to the RenderingServer\'s data.
`force_draw()<class_RenderingServer_method_force_draw>`{.interpreted-text
role="ref"} is usually called if this happens.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_has_feature}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_feature**(feature:
`Features<enum_RenderingServer_Features>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_has_feature>`{.interpreted-text
role="ref"}

**Deprecated:** This method has not been used since Godot 3.0.

This method does nothing and always returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_has_os_feature}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_os_feature**(feature: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_has_os_feature>`{.interpreted-text
role="ref"}

Returns `true` if the OS supports a certain `feature`. Features might be
`s3tc`, `etc`, and `etc2`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_attach_object_instance_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_attach_object_instance_id**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_attach_object_instance_id>`{.interpreted-text
role="ref"}

Attaches a unique Object ID to instance. Object ID must be attached to
instance for proper culling with
`instances_cull_aabb()<class_RenderingServer_method_instances_cull_aabb>`{.interpreted-text
role="ref"},
`instances_cull_convex()<class_RenderingServer_method_instances_cull_convex>`{.interpreted-text
role="ref"}, and
`instances_cull_ray()<class_RenderingServer_method_instances_cull_ray>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_attach_skeleton}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_attach_skeleton**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, skeleton:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_attach_skeleton>`{.interpreted-text
role="ref"}

Attaches a skeleton to an instance. Removes the previous skeleton from
the instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **instance_create**()
`🔗<class_RenderingServer_method_instance_create>`{.interpreted-text
role="ref"}

Creates a visual instance and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`instance_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

An instance is a way of placing a 3D object in the scenario. Objects
like particles, meshes, reflection probes and decals need to be
associated with an instance to be visible in the scenario using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The equivalent node is
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_create2}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**instance_create2**(base: `RID<class_RID>`{.interpreted-text
role="ref"}, scenario: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_create2>`{.interpreted-text
role="ref"}

Creates a visual instance, adds it to the RenderingServer, and sets both
base and scenario. It can be accessed with the RID that is returned.
This RID will be used in all `instance_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method. This is a shorthand for using
`instance_create()<class_RenderingServer_method_instance_create>`{.interpreted-text
role="ref"} and setting the base and scenario manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_get_shader_parameter}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**instance_geometry_get_shader_parameter**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, parameter:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_instance_geometry_get_shader_parameter>`{.interpreted-text
role="ref"}

Returns the value of the per-instance shader uniform from the specified
3D geometry instance. Equivalent to
`GeometryInstance3D.get_instance_shader_parameter()<class_GeometryInstance3D_method_get_instance_shader_parameter>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Per-instance shader parameter names are case-sensitive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_get_shader_parameter_default_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**instance_geometry_get_shader_parameter_default_value**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, parameter:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_instance_geometry_get_shader_parameter_default_value>`{.interpreted-text
role="ref"}

Returns the default value of the per-instance shader uniform from the
specified 3D geometry instance. Equivalent to
`GeometryInstance3D.get_instance_shader_parameter()<class_GeometryInstance3D_method_get_instance_shader_parameter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_get_shader_parameter_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **instance_geometry_get_shader_parameter_list**(instance:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_instance_geometry_get_shader_parameter_list>`{.interpreted-text
role="ref"}

Returns a dictionary of per-instance shader uniform names of the
per-instance shader uniform from the specified 3D geometry instance. The
returned dictionary is in PropertyInfo format, with the keys `name`,
`class_name`, `type`, `hint`, `hint_string` and `usage`. Equivalent to
`GeometryInstance3D.get_instance_shader_parameter()<class_GeometryInstance3D_method_get_instance_shader_parameter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_set_cast_shadows_setting}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_geometry_set_cast_shadows_setting**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, shadow_casting_setting:
`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_instance_geometry_set_cast_shadows_setting>`{.interpreted-text
role="ref"}

Sets the shadow casting setting. Equivalent to
`GeometryInstance3D.cast_shadow<class_GeometryInstance3D_property_cast_shadow>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_set_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_geometry_set_flag**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, flag:
`InstanceFlags<enum_RenderingServer_InstanceFlags>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_geometry_set_flag>`{.interpreted-text
role="ref"}

Sets the `flag` for a given `instance` to `enabled`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_set_lightmap}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_geometry_set_lightmap**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, lightmap:
`RID<class_RID>`{.interpreted-text role="ref"}, lightmap_uv_scale:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, lightmap_slice:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_geometry_set_lightmap>`{.interpreted-text
role="ref"}

Sets the lightmap GI instance to use for the specified 3D geometry
instance. The lightmap UV scale for the specified instance (equivalent
to
`GeometryInstance3D.gi_lightmap_scale<class_GeometryInstance3D_property_gi_lightmap_scale>`{.interpreted-text
role="ref"}) and lightmap atlas slice must also be specified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_set_lod_bias}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_geometry_set_lod_bias**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, lod_bias:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_geometry_set_lod_bias>`{.interpreted-text
role="ref"}

Sets the level of detail bias to use when rendering the specified 3D
geometry instance. Higher values result in higher detail from further
away. Equivalent to
`GeometryInstance3D.lod_bias<class_GeometryInstance3D_property_lod_bias>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_set_material_overlay}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_geometry_set_material_overlay**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, material:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_geometry_set_material_overlay>`{.interpreted-text
role="ref"}

Sets a material that will be rendered for all surfaces on top of active
materials for the mesh associated with this instance. Equivalent to
`GeometryInstance3D.material_overlay<class_GeometryInstance3D_property_material_overlay>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_set_material_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_geometry_set_material_override**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, material:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_geometry_set_material_override>`{.interpreted-text
role="ref"}

Sets a material that will override the material for all surfaces on the
mesh associated with this instance. Equivalent to
`GeometryInstance3D.material_override<class_GeometryInstance3D_property_material_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_set_shader_parameter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_geometry_set_shader_parameter**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, parameter:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_geometry_set_shader_parameter>`{.interpreted-text
role="ref"}

Sets the per-instance shader uniform on the specified 3D geometry
instance. Equivalent to
`GeometryInstance3D.set_instance_shader_parameter()<class_GeometryInstance3D_method_set_instance_shader_parameter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_set_transparency}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_geometry_set_transparency**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, transparency:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_geometry_set_transparency>`{.interpreted-text
role="ref"}

Sets the transparency for the given geometry instance. Equivalent to
`GeometryInstance3D.transparency<class_GeometryInstance3D_property_transparency>`{.interpreted-text
role="ref"}.

A transparency of `0.0` is fully opaque, while `1.0` is fully
transparent. Values greater than `0.0` (exclusive) will force the
geometry\'s materials to go through the transparent pipeline, which is
slower to render and can exhibit rendering issues due to incorrect
transparency sorting. However, unlike using a transparent material,
setting `transparency` to a value greater than `0.0` (exclusive) will
*not* disable shadow rendering.

In spatial shaders, `1.0 - transparency` is set as the default value of
the `ALPHA` built-in.

\*\*Note:\*\* `transparency` is clamped between `0.0` and `1.0`, so this
property cannot be used to make transparent materials more opaque than
they originally are.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_geometry_set_visibility_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_geometry_set_visibility_range**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, min:
`float<class_float>`{.interpreted-text role="ref"}, max:
`float<class_float>`{.interpreted-text role="ref"}, min_margin:
`float<class_float>`{.interpreted-text role="ref"}, max_margin:
`float<class_float>`{.interpreted-text role="ref"}, fade_mode:
`VisibilityRangeFadeMode<enum_RenderingServer_VisibilityRangeFadeMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_instance_geometry_set_visibility_range>`{.interpreted-text
role="ref"}

Sets the visibility range values for the given geometry instance.
Equivalent to
`GeometryInstance3D.visibility_range_begin<class_GeometryInstance3D_property_visibility_range_begin>`{.interpreted-text
role="ref"} and related properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_base}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_base**(instance: `RID<class_RID>`{.interpreted-text
role="ref"}, base: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"}

Sets the base of the instance. A base can be any of the 3D objects that
are created in the RenderingServer that can be displayed. For example,
any of the light types, mesh, multimesh, particle system, reflection
probe, decal, lightmap, voxel GI and visibility notifiers are all types
that can be set as the base of an instance in order to be displayed in
the scenario.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_blend_shape_weight}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_blend_shape_weight**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, shape:
`int<class_int>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_blend_shape_weight>`{.interpreted-text
role="ref"}

Sets the weight for a given blend shape associated with this instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_custom_aabb}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_custom_aabb**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, aabb:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_custom_aabb>`{.interpreted-text
role="ref"}

Sets a custom AABB to use when culling objects from the view frustum.
Equivalent to setting
`GeometryInstance3D.custom_aabb<class_GeometryInstance3D_property_custom_aabb>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_extra_visibility_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_extra_visibility_margin**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, margin:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_extra_visibility_margin>`{.interpreted-text
role="ref"}

Sets a margin to increase the size of the AABB when culling objects from
the view frustum. This allows you to avoid culling objects that fall
outside the view frustum. Equivalent to
`GeometryInstance3D.extra_cull_margin<class_GeometryInstance3D_property_extra_cull_margin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_ignore_culling}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_ignore_culling**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_ignore_culling>`{.interpreted-text
role="ref"}

If `true`, ignores both frustum and occlusion culling on the specified
3D geometry instance. This is not the same as
`GeometryInstance3D.ignore_occlusion_culling<class_GeometryInstance3D_property_ignore_occlusion_culling>`{.interpreted-text
role="ref"}, which only ignores occlusion culling and leaves frustum
culling intact.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_layer_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_layer_mask**(instance: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_layer_mask>`{.interpreted-text
role="ref"}

Sets the render layers that this instance will be drawn to. Equivalent
to
`VisualInstance3D.layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_pivot_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_pivot_data**(instance: `RID<class_RID>`{.interpreted-text
role="ref"}, sorting_offset: `float<class_float>`{.interpreted-text
role="ref"}, use_aabb_center: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_instance_set_pivot_data>`{.interpreted-text
role="ref"}

Sets the sorting offset and switches between using the bounding box or
instance origin for depth sorting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_scenario}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_scenario**(instance: `RID<class_RID>`{.interpreted-text
role="ref"}, scenario: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_scenario>`{.interpreted-text
role="ref"}

Sets the scenario that the instance is in. The scenario is the 3D world
that the objects will be displayed in.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_surface_override_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_surface_override_material**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, surface:
`int<class_int>`{.interpreted-text role="ref"}, material:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_surface_override_material>`{.interpreted-text
role="ref"}

Sets the override material of a specific surface. Equivalent to
`MeshInstance3D.set_surface_override_material()<class_MeshInstance3D_method_set_surface_override_material>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_transform**(instance: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_transform>`{.interpreted-text
role="ref"}

Sets the world space transform of the instance. Equivalent to
`Node3D.global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_visibility_parent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_visibility_parent**(instance:
`RID<class_RID>`{.interpreted-text role="ref"}, parent:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_visibility_parent>`{.interpreted-text
role="ref"}

Sets the visibility parent for the given instance. Equivalent to
`Node3D.visibility_parent<class_Node3D_property_visibility_parent>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_set_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_set_visible**(instance: `RID<class_RID>`{.interpreted-text
role="ref"}, visible: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_instance_set_visible>`{.interpreted-text
role="ref"}

Sets whether an instance is drawn or not. Equivalent to
`Node3D.visible<class_Node3D_property_visible>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instance_teleport}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**instance_teleport**(instance: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_instance_teleport>`{.interpreted-text
role="ref"}

Resets motion vectors and other interpolated values. Use this *after*
teleporting a mesh from one position to another to avoid ghosting
artifacts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instances_cull_aabb}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**instances_cull_aabb**(aabb: `AABB<class_AABB>`{.interpreted-text
role="ref"}, scenario: `RID<class_RID>`{.interpreted-text role="ref"} =
RID())
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_instances_cull_aabb>`{.interpreted-text
role="ref"}

Returns an array of object IDs intersecting with the provided AABB. Only
3D nodes that inherit from
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
are considered, such as
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"} or
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}. Use
`@GlobalScope.instance_from_id()<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"} to obtain the actual nodes. A scenario RID must be provided,
which is available in the `World3D<class_World3D>`{.interpreted-text
role="ref"} you want to query. This forces an update for all resources
queued to update.

\*\*Warning:\*\* This function is primarily intended for editor usage.
For in-game use cases, prefer physics collision.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instances_cull_convex}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**instances_cull_convex**(convex: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\],
scenario: `RID<class_RID>`{.interpreted-text role="ref"} = RID())
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_instances_cull_convex>`{.interpreted-text
role="ref"}

Returns an array of object IDs intersecting with the provided convex
shape. Only 3D nodes that inherit from
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
are considered, such as
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"} or
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}. Use
`@GlobalScope.instance_from_id()<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"} to obtain the actual nodes. A scenario RID must be provided,
which is available in the `World3D<class_World3D>`{.interpreted-text
role="ref"} you want to query. This forces an update for all resources
queued to update.

\*\*Warning:\*\* This function is primarily intended for editor usage.
For in-game use cases, prefer physics collision.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_instances_cull_ray}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**instances_cull_ray**(from: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, to: `Vector3<class_Vector3>`{.interpreted-text role="ref"},
scenario: `RID<class_RID>`{.interpreted-text role="ref"} = RID())
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_instances_cull_ray>`{.interpreted-text
role="ref"}

Returns an array of object IDs intersecting with the provided 3D ray.
Only 3D nodes that inherit from
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
are considered, such as
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"} or
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}. Use
`@GlobalScope.instance_from_id()<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"} to obtain the actual nodes. A scenario RID must be provided,
which is available in the `World3D<class_World3D>`{.interpreted-text
role="ref"} you want to query. This forces an update for all resources
queued to update.

\*\*Warning:\*\* This function is primarily intended for editor usage.
For in-game use cases, prefer physics collision.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_is_on_render_thread}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_on_render_thread**()
`🔗<class_RenderingServer_method_is_on_render_thread>`{.interpreted-text
role="ref"}

Returns `true` if our code is currently executing on the rendering
thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_directional_set_blend_splits}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_directional_set_blend_splits**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_directional_set_blend_splits>`{.interpreted-text
role="ref"}

If `true`, this directional light will blend between shadow map splits
resulting in a smoother transition between them. Equivalent to
`DirectionalLight3D.directional_shadow_blend_splits<class_DirectionalLight3D_property_directional_shadow_blend_splits>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_directional_set_shadow_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_directional_set_shadow_mode**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`LightDirectionalShadowMode<enum_RenderingServer_LightDirectionalShadowMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_light_directional_set_shadow_mode>`{.interpreted-text
role="ref"}

Sets the shadow mode for this directional light. Equivalent to
`DirectionalLight3D.directional_shadow_mode<class_DirectionalLight3D_property_directional_shadow_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_directional_set_sky_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_directional_set_sky_mode**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`LightDirectionalSkyMode<enum_RenderingServer_LightDirectionalSkyMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_light_directional_set_sky_mode>`{.interpreted-text
role="ref"}

If `true`, this light will not be used for anything except sky shaders.
Use this for lights that impact your sky shader that you may want to
hide from affecting the rest of the scene. For example, you may want to
enable this when the sun in your sky shader falls below the horizon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_omni_set_shadow_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_omni_set_shadow_mode**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, mode:
`LightOmniShadowMode<enum_RenderingServer_LightOmniShadowMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_light_omni_set_shadow_mode>`{.interpreted-text
role="ref"}

Sets whether to use a dual paraboloid or a cubemap for the shadow map.
Dual paraboloid is faster but may suffer from artifacts. Equivalent to
`OmniLight3D.omni_shadow_mode<class_OmniLight3D_property_omni_shadow_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_projectors_set_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_projectors_set_filter**(filter:
`LightProjectorFilter<enum_RenderingServer_LightProjectorFilter>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_light_projectors_set_filter>`{.interpreted-text
role="ref"}

Sets the texture filter mode to use when rendering light projectors.
This parameter is global and cannot be set on a per-light basis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_bake_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_bake_mode**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, bake_mode:
`LightBakeMode<enum_RenderingServer_LightBakeMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_light_set_bake_mode>`{.interpreted-text
role="ref"}

Sets the bake mode to use for the specified 3D light. Equivalent to
`Light3D.light_bake_mode<class_Light3D_property_light_bake_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_color**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_color>`{.interpreted-text
role="ref"}

Sets the color of the light. Equivalent to
`Light3D.light_color<class_Light3D_property_light_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_cull_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_cull_mask**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_cull_mask>`{.interpreted-text
role="ref"}

Sets the cull mask for this 3D light. Lights only affect objects in the
selected layers. Equivalent to
`Light3D.light_cull_mask<class_Light3D_property_light_cull_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_distance_fade}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_distance_fade**(decal: `RID<class_RID>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"},
begin: `float<class_float>`{.interpreted-text role="ref"}, shadow:
`float<class_float>`{.interpreted-text role="ref"}, length:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_distance_fade>`{.interpreted-text
role="ref"}

Sets the distance fade for this 3D light. This acts as a form of level
of detail (LOD) and can be used to improve performance. Equivalent to
`Light3D.distance_fade_enabled<class_Light3D_property_distance_fade_enabled>`{.interpreted-text
role="ref"},
`Light3D.distance_fade_begin<class_Light3D_property_distance_fade_begin>`{.interpreted-text
role="ref"},
`Light3D.distance_fade_shadow<class_Light3D_property_distance_fade_shadow>`{.interpreted-text
role="ref"}, and
`Light3D.distance_fade_length<class_Light3D_property_distance_fade_length>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_max_sdfgi_cascade}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_max_sdfgi_cascade**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, cascade:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_max_sdfgi_cascade>`{.interpreted-text
role="ref"}

Sets the maximum SDFGI cascade in which the 3D light\'s indirect
lighting is rendered. Higher values allow the light to be rendered in
SDFGI further away from the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_negative}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_negative**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_negative>`{.interpreted-text
role="ref"}

If `true`, the 3D light will subtract light instead of adding light.
Equivalent to
`Light3D.light_negative<class_Light3D_property_light_negative>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_param**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`LightParam<enum_RenderingServer_LightParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_param>`{.interpreted-text
role="ref"}

Sets the specified 3D light parameter. Equivalent to
`Light3D.set_param()<class_Light3D_method_set_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_projector}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_projector**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, texture: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_projector>`{.interpreted-text
role="ref"}

Sets the projector texture to use for the specified 3D light. Equivalent
to
`Light3D.light_projector<class_Light3D_property_light_projector>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_reverse_cull_face_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_reverse_cull_face_mode**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_reverse_cull_face_mode>`{.interpreted-text
role="ref"}

If `true`, reverses the backface culling of the mesh. This can be useful
when you have a flat mesh that has a light behind it. If you need to
cast a shadow on both sides of the mesh, set the mesh to use
double-sided shadows with
`instance_geometry_set_cast_shadows_setting()<class_RenderingServer_method_instance_geometry_set_cast_shadows_setting>`{.interpreted-text
role="ref"}. Equivalent to
`Light3D.shadow_reverse_cull_face<class_Light3D_property_shadow_reverse_cull_face>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_shadow}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_shadow**(light: `RID<class_RID>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_shadow>`{.interpreted-text
role="ref"}

If `true`, light will cast shadows. Equivalent to
`Light3D.shadow_enabled<class_Light3D_property_shadow_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_light_set_shadow_caster_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**light_set_shadow_caster_mask**(light:
`RID<class_RID>`{.interpreted-text role="ref"}, mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_light_set_shadow_caster_mask>`{.interpreted-text
role="ref"}

Sets the shadow caster mask for this 3D light. Shadows will only be cast
using objects in the selected layers. Equivalent to
`Light3D.shadow_caster_mask<class_Light3D_property_shadow_caster_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **lightmap_create**()
`🔗<class_RenderingServer_method_lightmap_create>`{.interpreted-text
role="ref"}

Creates a new lightmap global illumination instance and adds it to the
RenderingServer. It can be accessed with the RID that is returned. This
RID will be used in all `lightmap_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent node is
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_get_probe_capture_bsp_tree}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**lightmap_get_probe_capture_bsp_tree**(lightmap:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_lightmap_get_probe_capture_bsp_tree>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_get_probe_capture_points}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **lightmap_get_probe_capture_points**(lightmap:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_lightmap_get_probe_capture_points>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_get_probe_capture_sh}
::: rst-class
classref-method
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**lightmap_get_probe_capture_sh**(lightmap:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_lightmap_get_probe_capture_sh>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_get_probe_capture_tetrahedra}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**lightmap_get_probe_capture_tetrahedra**(lightmap:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_lightmap_get_probe_capture_tetrahedra>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_set_baked_exposure_normalization}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**lightmap_set_baked_exposure_normalization**(lightmap:
`RID<class_RID>`{.interpreted-text role="ref"}, baked_exposure:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_lightmap_set_baked_exposure_normalization>`{.interpreted-text
role="ref"}

Used to inform the renderer what exposure normalization value was used
while baking the lightmap. This value will be used and modulated at run
time to ensure that the lightmap maintains a consistent level of
exposure even if the scene-wide exposure normalization is changed at run
time. For more information see
`camera_attributes_set_exposure()<class_RenderingServer_method_camera_attributes_set_exposure>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_set_probe_bounds}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**lightmap_set_probe_bounds**(lightmap:
`RID<class_RID>`{.interpreted-text role="ref"}, bounds:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_lightmap_set_probe_bounds>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_set_probe_capture_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**lightmap_set_probe_capture_data**(lightmap:
`RID<class_RID>`{.interpreted-text role="ref"}, points:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, point_sh:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, tetrahedra:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}, bsp_tree:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_lightmap_set_probe_capture_data>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_set_probe_capture_update_speed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**lightmap_set_probe_capture_update_speed**(speed:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_lightmap_set_probe_capture_update_speed>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_set_probe_interior}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**lightmap_set_probe_interior**(lightmap:
`RID<class_RID>`{.interpreted-text role="ref"}, interior:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_lightmap_set_probe_interior>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmap_set_textures}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**lightmap_set_textures**(lightmap: `RID<class_RID>`{.interpreted-text
role="ref"}, light: `RID<class_RID>`{.interpreted-text role="ref"},
uses_sh: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_lightmap_set_textures>`{.interpreted-text
role="ref"}

Set the textures on the given `lightmap` GI instance to the texture
array pointed to by the `light` RID. If the lightmap texture was baked
with
`LightmapGI.directional<class_LightmapGI_property_directional>`{.interpreted-text
role="ref"} set to `true`, then `uses_sh` must also be `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_lightmaps_set_bicubic_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**lightmaps_set_bicubic_filter**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_lightmaps_set_bicubic_filter>`{.interpreted-text
role="ref"}

Toggles whether a bicubic filter should be used when lightmaps are
sampled. This smoothens their appearance at a performance cost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_make_sphere_mesh}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**make_sphere_mesh**(latitudes: `int<class_int>`{.interpreted-text
role="ref"}, longitudes: `int<class_int>`{.interpreted-text role="ref"},
radius: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_make_sphere_mesh>`{.interpreted-text
role="ref"}

Returns a mesh of a sphere with the given number of horizontal
subdivisions, vertical subdivisions and radius. See also
`get_test_cube()<class_RenderingServer_method_get_test_cube>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_material_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **material_create**()
`🔗<class_RenderingServer_method_material_create>`{.interpreted-text
role="ref"}

Creates an empty material and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`material_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`Material<class_Material>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_material_get_param}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**material_get_param**(material: `RID<class_RID>`{.interpreted-text
role="ref"}, parameter: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_material_get_param>`{.interpreted-text
role="ref"}

Returns the value of a certain material\'s parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_material_set_next_pass}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**material_set_next_pass**(material: `RID<class_RID>`{.interpreted-text
role="ref"}, next_material: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_material_set_next_pass>`{.interpreted-text
role="ref"}

Sets an object\'s next material.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_material_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**material_set_param**(material: `RID<class_RID>`{.interpreted-text
role="ref"}, parameter: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_material_set_param>`{.interpreted-text
role="ref"}

Sets a material\'s parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_material_set_render_priority}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**material_set_render_priority**(material:
`RID<class_RID>`{.interpreted-text role="ref"}, priority:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_material_set_render_priority>`{.interpreted-text
role="ref"}

Sets a material\'s render priority.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_material_set_shader}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**material_set_shader**(shader_material:
`RID<class_RID>`{.interpreted-text role="ref"}, shader:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_material_set_shader>`{.interpreted-text
role="ref"}

Sets a shader material\'s shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_add_surface}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_add_surface**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"}, surface: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_mesh_add_surface>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_add_surface_from_arrays}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_add_surface_from_arrays**(mesh:
`RID<class_RID>`{.interpreted-text role="ref"}, primitive:
`PrimitiveType<enum_RenderingServer_PrimitiveType>`{.interpreted-text
role="ref"}, arrays: `Array<class_Array>`{.interpreted-text role="ref"},
blend_shapes: `Array<class_Array>`{.interpreted-text role="ref"} = \[\],
lods: `Dictionary<class_Dictionary>`{.interpreted-text role="ref"} = {},
compress_format:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_RenderingServer_method_mesh_add_surface_from_arrays>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_clear**(mesh: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_mesh_clear>`{.interpreted-text
role="ref"}

Removes all surfaces from a mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **mesh_create**()
`🔗<class_RenderingServer_method_mesh_create>`{.interpreted-text
role="ref"}

Creates a new mesh and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`mesh_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

To place in a scene, attach this mesh to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"} using the returned RID.

\*\*Note:\*\* The equivalent resource is
`Mesh<class_Mesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_create_from_surfaces}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**mesh_create_from_surfaces**(surfaces:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\], blend_shape_count: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_RenderingServer_method_mesh_create_from_surfaces>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_get_blend_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**mesh_get_blend_shape_count**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_get_blend_shape_count>`{.interpreted-text
role="ref"}

Returns a mesh\'s blend shape count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_get_blend_shape_mode}
::: rst-class
classref-method
:::
::::

`BlendShapeMode<enum_RenderingServer_BlendShapeMode>`{.interpreted-text
role="ref"} **mesh_get_blend_shape_mode**(mesh:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_get_blend_shape_mode>`{.interpreted-text
role="ref"}

Returns a mesh\'s blend shape mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_get_custom_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"}
**mesh_get_custom_aabb**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_get_custom_aabb>`{.interpreted-text
role="ref"}

Returns a mesh\'s custom aabb.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_get_surface}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**mesh_get_surface**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"}, surface: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_mesh_get_surface>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_get_surface_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**mesh_get_surface_count**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_get_surface_count>`{.interpreted-text
role="ref"}

Returns a mesh\'s number of surfaces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_set_blend_shape_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_set_blend_shape_mode**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"}, mode:
`BlendShapeMode<enum_RenderingServer_BlendShapeMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_mesh_set_blend_shape_mode>`{.interpreted-text
role="ref"}

Sets a mesh\'s blend shape mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_set_custom_aabb}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_set_custom_aabb**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"}, aabb: `AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_mesh_set_custom_aabb>`{.interpreted-text
role="ref"}

Sets a mesh\'s custom aabb.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_set_shadow_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_set_shadow_mesh**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"}, shadow_mesh: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_mesh_set_shadow_mesh>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_get_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**mesh_surface_get_arrays**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"}, surface: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_surface_get_arrays>`{.interpreted-text
role="ref"}

Returns a mesh\'s surface\'s buffer arrays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_get_blend_shape_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Array<class_Array>`{.interpreted-text role="ref"}\]
**mesh_surface_get_blend_shape_arrays**(mesh:
`RID<class_RID>`{.interpreted-text role="ref"}, surface:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_surface_get_blend_shape_arrays>`{.interpreted-text
role="ref"}

Returns a mesh\'s surface\'s arrays for blend shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_get_format_attribute_stride}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**mesh_surface_get_format_attribute_stride**(format:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"}\], vertex_count: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_surface_get_format_attribute_stride>`{.interpreted-text
role="ref"}

Returns the stride of the attribute buffer for a mesh with given
`format`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_get_format_index_stride}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**mesh_surface_get_format_index_stride**(format:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"}\], vertex_count: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_surface_get_format_index_stride>`{.interpreted-text
role="ref"}

Returns the stride of the index buffer for a mesh with the given
`format`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_get_format_normal_tangent_stride}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**mesh_surface_get_format_normal_tangent_stride**(format:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"}\], vertex_count: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_surface_get_format_normal_tangent_stride>`{.interpreted-text
role="ref"}

Returns the stride of the combined normals and tangents for a mesh with
given `format`. Note importantly that, while normals and tangents are in
the vertex buffer with vertices, they are only interleaved with each
other and so have a different stride than vertex positions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_get_format_offset}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**mesh_surface_get_format_offset**(format:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"}\], vertex_count: `int<class_int>`{.interpreted-text
role="ref"}, array_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_surface_get_format_offset>`{.interpreted-text
role="ref"}

Returns the offset of a given attribute by `array_index` in the start of
its respective buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_get_format_skin_stride}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**mesh_surface_get_format_skin_stride**(format:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"}\], vertex_count: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_surface_get_format_skin_stride>`{.interpreted-text
role="ref"}

Returns the stride of the skin buffer for a mesh with given `format`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_get_format_vertex_stride}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**mesh_surface_get_format_vertex_stride**(format:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ArrayFormat<enum_RenderingServer_ArrayFormat>`{.interpreted-text
role="ref"}\], vertex_count: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_surface_get_format_vertex_stride>`{.interpreted-text
role="ref"}

Returns the stride of the vertex positions for a mesh with given
`format`. Note importantly that vertex positions are stored
consecutively and are not interleaved with the other attributes in the
vertex buffer (normals and tangents).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_get_material}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**mesh_surface_get_material**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"}, surface: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_mesh_surface_get_material>`{.interpreted-text
role="ref"}

Returns a mesh\'s surface\'s material.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_remove}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_surface_remove**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"}, surface: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_mesh_surface_remove>`{.interpreted-text
role="ref"}

Removes the surface at the given index from the Mesh, shifting surfaces
with higher index down by one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_set_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_surface_set_material**(mesh: `RID<class_RID>`{.interpreted-text
role="ref"}, surface: `int<class_int>`{.interpreted-text role="ref"},
material: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_mesh_surface_set_material>`{.interpreted-text
role="ref"}

Sets a mesh\'s surface\'s material.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_update_attribute_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_surface_update_attribute_region**(mesh:
`RID<class_RID>`{.interpreted-text role="ref"}, surface:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`int<class_int>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_mesh_surface_update_attribute_region>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_update_index_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_surface_update_index_region**(mesh:
`RID<class_RID>`{.interpreted-text role="ref"}, surface:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`int<class_int>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_mesh_surface_update_index_region>`{.interpreted-text
role="ref"}

Updates the index buffer of the mesh surface with the given `data`. The
expected data are 16 or 32-bit unsigned integers, which can be
determined with
`mesh_surface_get_format_index_stride()<class_RenderingServer_method_mesh_surface_get_format_index_stride>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_update_skin_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_surface_update_skin_region**(mesh:
`RID<class_RID>`{.interpreted-text role="ref"}, surface:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`int<class_int>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_mesh_surface_update_skin_region>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_mesh_surface_update_vertex_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mesh_surface_update_vertex_region**(mesh:
`RID<class_RID>`{.interpreted-text role="ref"}, surface:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`int<class_int>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_mesh_surface_update_vertex_region>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_allocate_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_allocate_data**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, instances:
`int<class_int>`{.interpreted-text role="ref"}, transform_format:
`MultimeshTransformFormat<enum_RenderingServer_MultimeshTransformFormat>`{.interpreted-text
role="ref"}, color_format: `bool<class_bool>`{.interpreted-text
role="ref"} = false, custom_data_format:
`bool<class_bool>`{.interpreted-text role="ref"} = false, use_indirect:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_RenderingServer_method_multimesh_allocate_data>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **multimesh_create**()
`🔗<class_RenderingServer_method_multimesh_create>`{.interpreted-text
role="ref"}

Creates a new multimesh on the RenderingServer and returns an
`RID<class_RID>`{.interpreted-text role="ref"} handle. This RID will be
used in all `multimesh_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

To place in a scene, attach this multimesh to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"} using the returned RID.

\*\*Note:\*\* The equivalent resource is
`MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_get_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"}
**multimesh_get_aabb**(multimesh: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_get_aabb>`{.interpreted-text
role="ref"}

Calculates and returns the axis-aligned bounding box that encloses all
instances within the multimesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_get_buffer}
::: rst-class
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **multimesh_get_buffer**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_get_buffer>`{.interpreted-text
role="ref"}

Returns the MultiMesh data (such as instance transforms, colors, etc.).
See
`multimesh_set_buffer()<class_RenderingServer_method_multimesh_set_buffer>`{.interpreted-text
role="ref"} for details on the returned data.

\*\*Note:\*\* If the buffer is in the engine\'s internal cache, it will
have to be fetched from GPU memory and possibly decompressed. This means
`multimesh_get_buffer()<class_RenderingServer_method_multimesh_get_buffer>`{.interpreted-text
role="ref"} is potentially a slow operation and should be avoided
whenever possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_get_buffer_rd_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**multimesh_get_buffer_rd_rid**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_get_buffer_rd_rid>`{.interpreted-text
role="ref"}

Returns the `RenderingDevice<class_RenderingDevice>`{.interpreted-text
role="ref"} `RID<class_RID>`{.interpreted-text role="ref"} handle of the
`MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"}, which can be
used as any other buffer on the Rendering Device.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_get_command_buffer_rd_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**multimesh_get_command_buffer_rd_rid**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_get_command_buffer_rd_rid>`{.interpreted-text
role="ref"}

Returns the `RenderingDevice<class_RenderingDevice>`{.interpreted-text
role="ref"} `RID<class_RID>`{.interpreted-text role="ref"} handle of the
`MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"} command
buffer. This `RID<class_RID>`{.interpreted-text role="ref"} is only
valid if `use_indirect` is set to `true` when allocating data through
`multimesh_allocate_data()<class_RenderingServer_method_multimesh_allocate_data>`{.interpreted-text
role="ref"}. It can be used to directly modify the instance count via
buffer.

The data structure is dependent on both how many surfaces the mesh
contains and whether it is indexed or not, the buffer has 5 integers in
it, with the last unused if the mesh is not indexed.

Each of the values in the buffer correspond to these options:

``` text
Indexed:
  0 - indexCount;
  1 - instanceCount;
  2 - firstIndex;
  3 - vertexOffset;
  4 - firstInstance;
Non Indexed:
  0 - vertexCount;
  1 - instanceCount;
  2 - firstVertex;
  3 - firstInstance;
  4 - unused;
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_get_custom_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"}
**multimesh_get_custom_aabb**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_get_custom_aabb>`{.interpreted-text
role="ref"}

Returns the custom AABB defined for this MultiMesh resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_get_instance_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**multimesh_get_instance_count**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_get_instance_count>`{.interpreted-text
role="ref"}

Returns the number of instances allocated for this multimesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_get_mesh}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**multimesh_get_mesh**(multimesh: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_get_mesh>`{.interpreted-text
role="ref"}

Returns the RID of the mesh that will be used in drawing this multimesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_get_visible_instances}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**multimesh_get_visible_instances**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_get_visible_instances>`{.interpreted-text
role="ref"}

Returns the number of visible instances for this multimesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_instance_get_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**multimesh_instance_get_color**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_instance_get_color>`{.interpreted-text
role="ref"}

Returns the color by which the specified instance will be modulated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_instance_get_custom_data}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**multimesh_instance_get_custom_data**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_instance_get_custom_data>`{.interpreted-text
role="ref"}

Returns the custom data associated with the specified instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_instance_get_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**multimesh_instance_get_transform**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_instance_get_transform>`{.interpreted-text
role="ref"}

Returns the `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} of the specified instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_instance_get_transform_2d}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**multimesh_instance_get_transform_2d**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_multimesh_instance_get_transform_2d>`{.interpreted-text
role="ref"}

Returns the `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"} of the specified instance. For use when the multimesh is set
to use 2D transforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_instance_reset_physics_interpolation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_instance_reset_physics_interpolation**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_multimesh_instance_reset_physics_interpolation>`{.interpreted-text
role="ref"}

Prevents physics interpolation for the specified instance during the
current physics tick.

This is useful when moving an instance to a new location, to give an
instantaneous change rather than interpolation from the previous
location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_instance_set_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_instance_set_color**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_multimesh_instance_set_color>`{.interpreted-text
role="ref"}

Sets the color by which this instance will be modulated. Equivalent to
`MultiMesh.set_instance_color()<class_MultiMesh_method_set_instance_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_instance_set_custom_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_instance_set_custom_data**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, custom_data:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_multimesh_instance_set_custom_data>`{.interpreted-text
role="ref"}

Sets the custom data for this instance. Custom data is passed as a
`Color<class_Color>`{.interpreted-text role="ref"}, but is interpreted
as a `vec4` in the shader. Equivalent to
`MultiMesh.set_instance_custom_data()<class_MultiMesh_method_set_instance_custom_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_instance_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_instance_set_transform**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_multimesh_instance_set_transform>`{.interpreted-text
role="ref"}

Sets the `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
for this instance. Equivalent to
`MultiMesh.set_instance_transform()<class_MultiMesh_method_set_instance_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_instance_set_transform_2d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_instance_set_transform_2d**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_multimesh_instance_set_transform_2d>`{.interpreted-text
role="ref"}

Sets the `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
for this instance. For use when multimesh is used in 2D. Equivalent to
`MultiMesh.set_instance_transform_2d()<class_MultiMesh_method_set_instance_transform_2d>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_set_buffer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_set_buffer**(multimesh: `RID<class_RID>`{.interpreted-text
role="ref"}, buffer:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_multimesh_set_buffer>`{.interpreted-text
role="ref"}

Set the entire data to use for drawing the `multimesh` at once to
`buffer` (such as instance transforms and colors). `buffer`\'s size must
match the number of instances multiplied by the per-instance data size
(which depends on the enabled MultiMesh fields). Otherwise, an error
message is printed and nothing is rendered. See also
`multimesh_get_buffer()<class_RenderingServer_method_multimesh_get_buffer>`{.interpreted-text
role="ref"}.

The per-instance data size and expected data order is:

``` text
2D:
  - Position: 8 floats (8 floats for Transform2D)
  - Position + Vertex color: 12 floats (8 floats for Transform2D, 4 floats for Color)
  - Position + Custom data: 12 floats (8 floats for Transform2D, 4 floats of custom data)
  - Position + Vertex color + Custom data: 16 floats (8 floats for Transform2D, 4 floats for Color, 4 floats of custom data)
3D:
  - Position: 12 floats (12 floats for Transform3D)
  - Position + Vertex color: 16 floats (12 floats for Transform3D, 4 floats for Color)
  - Position + Custom data: 16 floats (12 floats for Transform3D, 4 floats of custom data)
  - Position + Vertex color + Custom data: 20 floats (12 floats for Transform3D, 4 floats for Color, 4 floats of custom data)
```

Instance transforms are in row-major order. Specifically:

- For `Transform2D<class_Transform2D>`{.interpreted-text role="ref"} the
  float-order is:
  `(x.x, y.x, padding_float, origin.x, x.y, y.y, padding_float, origin.y)`.
- For `Transform3D<class_Transform3D>`{.interpreted-text role="ref"} the
  float-order is:
  `(basis.x.x, basis.y.x, basis.z.x, origin.x, basis.x.y, basis.y.y, basis.z.y, origin.y, basis.x.z, basis.y.z, basis.z.z, origin.z)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_set_buffer_interpolated}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_set_buffer_interpolated**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, buffer:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}, buffer_previous:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_multimesh_set_buffer_interpolated>`{.interpreted-text
role="ref"}

Alternative version of
`multimesh_set_buffer()<class_RenderingServer_method_multimesh_set_buffer>`{.interpreted-text
role="ref"} for use with physics interpolation.

Takes both an array of current data and an array of data for the
previous physics tick.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_set_custom_aabb}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_set_custom_aabb**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, aabb:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_multimesh_set_custom_aabb>`{.interpreted-text
role="ref"}

Sets the custom AABB for this MultiMesh resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_set_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_set_mesh**(multimesh: `RID<class_RID>`{.interpreted-text
role="ref"}, mesh: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_multimesh_set_mesh>`{.interpreted-text
role="ref"}

Sets the mesh to be drawn by the multimesh. Equivalent to
`MultiMesh.mesh<class_MultiMesh_property_mesh>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_set_physics_interpolated}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_set_physics_interpolated**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, interpolated:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_multimesh_set_physics_interpolated>`{.interpreted-text
role="ref"}

Turns on and off physics interpolation for this MultiMesh resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_set_physics_interpolation_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_set_physics_interpolation_quality**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, quality:
`MultimeshPhysicsInterpolationQuality<enum_RenderingServer_MultimeshPhysicsInterpolationQuality>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_multimesh_set_physics_interpolation_quality>`{.interpreted-text
role="ref"}

Sets the physics interpolation quality for the
`MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"}.

A value of
`MULTIMESH_INTERP_QUALITY_FAST<class_RenderingServer_constant_MULTIMESH_INTERP_QUALITY_FAST>`{.interpreted-text
role="ref"} gives fast but low quality interpolation, a value of
`MULTIMESH_INTERP_QUALITY_HIGH<class_RenderingServer_constant_MULTIMESH_INTERP_QUALITY_HIGH>`{.interpreted-text
role="ref"} gives slower but higher quality interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_multimesh_set_visible_instances}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**multimesh_set_visible_instances**(multimesh:
`RID<class_RID>`{.interpreted-text role="ref"}, visible:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_multimesh_set_visible_instances>`{.interpreted-text
role="ref"}

Sets the number of instances visible at a given time. If -1, all
instances that have been allocated are drawn. Equivalent to
`MultiMesh.visible_instance_count<class_MultiMesh_property_visible_instance_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_occluder_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **occluder_create**()
`🔗<class_RenderingServer_method_occluder_create>`{.interpreted-text
role="ref"}

Creates an occluder instance and adds it to the RenderingServer. It can
be accessed with the RID that is returned. This RID will be used in all
`occluder_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`Occluder3D<class_Occluder3D>`{.interpreted-text role="ref"} (not to be
confused with the
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"} node).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_occluder_set_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**occluder_set_mesh**(occluder: `RID<class_RID>`{.interpreted-text
role="ref"}, vertices:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, indices:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_occluder_set_mesh>`{.interpreted-text
role="ref"}

Sets the mesh data for the given occluder RID, which controls the shape
of the occlusion culling that will be performed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_omni_light_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **omni_light_create**()
`🔗<class_RenderingServer_method_omni_light_create>`{.interpreted-text
role="ref"}

Creates a new omni light and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID can be used in most
`light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

To place in a scene, attach this omni light to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"} using the returned RID.

\*\*Note:\*\* The equivalent node is
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**particles_collision_create**()
`🔗<class_RenderingServer_method_particles_collision_create>`{.interpreted-text
role="ref"}

Creates a new 3D GPU particle collision or attractor and adds it to the
RenderingServer. It can be accessed with the RID that is returned. This
RID can be used in most `particles_collision_*` RenderingServer
functions.

\*\*Note:\*\* The equivalent nodes are
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} and
`GPUParticlesAttractor3D<class_GPUParticlesAttractor3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_height_field_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_height_field_update**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_collision_height_field_update>`{.interpreted-text
role="ref"}

Requests an update for the 3D GPU particle collision heightfield. This
may be automatically called by the 3D GPU particle collision heightfield
depending on its
`GPUParticlesCollisionHeightField3D.update_mode<class_GPUParticlesCollisionHeightField3D_property_update_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_attractor_attenuation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_attractor_attenuation**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, curve:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_attractor_attenuation>`{.interpreted-text
role="ref"}

Sets the attenuation `curve` for the 3D GPU particles attractor
specified by the `particles_collision` RID. Only used for attractors,
not colliders. Equivalent to
`GPUParticlesAttractor3D.attenuation<class_GPUParticlesAttractor3D_property_attenuation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_attractor_directionality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_attractor_directionality**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, amount:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_attractor_directionality>`{.interpreted-text
role="ref"}

Sets the directionality `amount` for the 3D GPU particles attractor
specified by the `particles_collision` RID. Only used for attractors,
not colliders. Equivalent to
`GPUParticlesAttractor3D.directionality<class_GPUParticlesAttractor3D_property_directionality>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_attractor_strength}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_attractor_strength**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, strength:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_attractor_strength>`{.interpreted-text
role="ref"}

Sets the `strength` for the 3D GPU particles attractor specified by the
`particles_collision` RID. Only used for attractors, not colliders.
Equivalent to
`GPUParticlesAttractor3D.strength<class_GPUParticlesAttractor3D_property_strength>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_box_extents}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_box_extents**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, extents:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_box_extents>`{.interpreted-text
role="ref"}

Sets the `extents` for the 3D GPU particles collision by the
`particles_collision` RID. Equivalent to
`GPUParticlesCollisionBox3D.size<class_GPUParticlesCollisionBox3D_property_size>`{.interpreted-text
role="ref"},
`GPUParticlesCollisionSDF3D.size<class_GPUParticlesCollisionSDF3D_property_size>`{.interpreted-text
role="ref"},
`GPUParticlesCollisionHeightField3D.size<class_GPUParticlesCollisionHeightField3D_property_size>`{.interpreted-text
role="ref"},
`GPUParticlesAttractorBox3D.size<class_GPUParticlesAttractorBox3D_property_size>`{.interpreted-text
role="ref"} or
`GPUParticlesAttractorVectorField3D.size<class_GPUParticlesAttractorVectorField3D_property_size>`{.interpreted-text
role="ref"} depending on the `particles_collision` type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_collision_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_collision_type**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, type:
`ParticlesCollisionType<enum_RenderingServer_ParticlesCollisionType>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_collision_type>`{.interpreted-text
role="ref"}

Sets the collision or attractor shape `type` for the 3D GPU particles
collision or attractor specified by the `particles_collision` RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_cull_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_cull_mask**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_cull_mask>`{.interpreted-text
role="ref"}

Sets the cull `mask` for the 3D GPU particles collision or attractor
specified by the `particles_collision` RID. Equivalent to
`GPUParticlesCollision3D.cull_mask<class_GPUParticlesCollision3D_property_cull_mask>`{.interpreted-text
role="ref"} or
`GPUParticlesAttractor3D.cull_mask<class_GPUParticlesAttractor3D_property_cull_mask>`{.interpreted-text
role="ref"} depending on the `particles_collision` type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_field_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_field_texture**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, texture:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_field_texture>`{.interpreted-text
role="ref"}

Sets the signed distance field `texture` for the 3D GPU particles
collision specified by the `particles_collision` RID. Equivalent to
`GPUParticlesCollisionSDF3D.texture<class_GPUParticlesCollisionSDF3D_property_texture>`{.interpreted-text
role="ref"} or
`GPUParticlesAttractorVectorField3D.texture<class_GPUParticlesAttractorVectorField3D_property_texture>`{.interpreted-text
role="ref"} depending on the `particles_collision` type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_height_field_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_height_field_mask**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_height_field_mask>`{.interpreted-text
role="ref"}

Sets the heightfield `mask` for the 3D GPU particles heightfield
collision specified by the `particles_collision` RID. Equivalent to
`GPUParticlesCollisionHeightField3D.heightfield_mask<class_GPUParticlesCollisionHeightField3D_property_heightfield_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_height_field_resolution}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_height_field_resolution**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, resolution:
`ParticlesCollisionHeightfieldResolution<enum_RenderingServer_ParticlesCollisionHeightfieldResolution>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_height_field_resolution>`{.interpreted-text
role="ref"}

Sets the heightmap `resolution` for the 3D GPU particles heightfield
collision specified by the `particles_collision` RID. Equivalent to
`GPUParticlesCollisionHeightField3D.resolution<class_GPUParticlesCollisionHeightField3D_property_resolution>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_collision_set_sphere_radius}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_collision_set_sphere_radius**(particles_collision:
`RID<class_RID>`{.interpreted-text role="ref"}, radius:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_collision_set_sphere_radius>`{.interpreted-text
role="ref"}

Sets the `radius` for the 3D GPU particles sphere collision or attractor
specified by the `particles_collision` RID. Equivalent to
`GPUParticlesCollisionSphere3D.radius<class_GPUParticlesCollisionSphere3D_property_radius>`{.interpreted-text
role="ref"} or
`GPUParticlesAttractorSphere3D.radius<class_GPUParticlesAttractorSphere3D_property_radius>`{.interpreted-text
role="ref"} depending on the `particles_collision` type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **particles_create**()
`🔗<class_RenderingServer_method_particles_create>`{.interpreted-text
role="ref"}

Creates a GPU-based particle system and adds it to the RenderingServer.
It can be accessed with the RID that is returned. This RID will be used
in all `particles_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

To place in a scene, attach these particles to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"} using the returned RID.

\*\*Note:\*\* The equivalent nodes are
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"} and
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}.

\*\*Note:\*\* All `particles_*` methods only apply to GPU-based
particles, not CPU-based particles.
`CPUParticles2D<class_CPUParticles2D>`{.interpreted-text role="ref"} and
`CPUParticles3D<class_CPUParticles3D>`{.interpreted-text role="ref"} do
not have equivalent RenderingServer functions available, as these use
`MultiMeshInstance2D<class_MultiMeshInstance2D>`{.interpreted-text
role="ref"} and
`MultiMeshInstance3D<class_MultiMeshInstance3D>`{.interpreted-text
role="ref"} under the hood (see `multimesh_*` methods).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_emit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_emit**(particles: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"},
velocity: `Vector3<class_Vector3>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"}, custom:
`Color<class_Color>`{.interpreted-text role="ref"}, emit_flags:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_emit>`{.interpreted-text
role="ref"}

Manually emits particles from the `particles` instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_get_current_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"}
**particles_get_current_aabb**(particles:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_get_current_aabb>`{.interpreted-text
role="ref"}

Calculates and returns the axis-aligned bounding box that contains all
the particles. Equivalent to
`GPUParticles3D.capture_aabb()<class_GPUParticles3D_method_capture_aabb>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_get_emitting}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**particles_get_emitting**(particles: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_particles_get_emitting>`{.interpreted-text
role="ref"}

Returns `true` if particles are currently set to emitting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_is_inactive}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**particles_is_inactive**(particles: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_particles_is_inactive>`{.interpreted-text
role="ref"}

Returns `true` if particles are not emitting and particles are set to
inactive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_request_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_request_process**(particles:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_request_process>`{.interpreted-text
role="ref"}

Add particle system to list of particle systems that need to be updated.
Update will take place on the next frame, or on the next call to
`instances_cull_aabb()<class_RenderingServer_method_instances_cull_aabb>`{.interpreted-text
role="ref"},
`instances_cull_convex()<class_RenderingServer_method_instances_cull_convex>`{.interpreted-text
role="ref"}, or
`instances_cull_ray()<class_RenderingServer_method_instances_cull_ray>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_request_process_time}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_request_process_time**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_request_process_time>`{.interpreted-text
role="ref"}

Requests particles to process for extra process time during a single
frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_restart}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_restart**(particles: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_particles_restart>`{.interpreted-text
role="ref"}

Reset the particles on the next update. Equivalent to
`GPUParticles3D.restart()<class_GPUParticles3D_method_restart>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_amount}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_amount**(particles: `RID<class_RID>`{.interpreted-text
role="ref"}, amount: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_amount>`{.interpreted-text
role="ref"}

Sets the number of particles to be drawn and allocates the memory for
them. Equivalent to
`GPUParticles3D.amount<class_GPUParticles3D_property_amount>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_amount_ratio}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_amount_ratio**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, ratio:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_amount_ratio>`{.interpreted-text
role="ref"}

Sets the amount ratio for particles to be emitted. Equivalent to
`GPUParticles3D.amount_ratio<class_GPUParticles3D_property_amount_ratio>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_collision_base_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_collision_base_size**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_collision_base_size>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_custom_aabb}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_custom_aabb**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, aabb:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_custom_aabb>`{.interpreted-text
role="ref"}

Sets a custom axis-aligned bounding box for the particle system.
Equivalent to
`GPUParticles3D.visibility_aabb<class_GPUParticles3D_property_visibility_aabb>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_draw_order}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_draw_order**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, order:
`ParticlesDrawOrder<enum_RenderingServer_ParticlesDrawOrder>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_particles_set_draw_order>`{.interpreted-text
role="ref"}

Sets the draw order of the particles. Equivalent to
`GPUParticles3D.draw_order<class_GPUParticles3D_property_draw_order>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_draw_pass_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_draw_pass_mesh**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, pass:
`int<class_int>`{.interpreted-text role="ref"}, mesh:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_draw_pass_mesh>`{.interpreted-text
role="ref"}

Sets the mesh to be used for the specified draw pass. Equivalent to
`GPUParticles3D.draw_pass_1<class_GPUParticles3D_property_draw_pass_1>`{.interpreted-text
role="ref"},
`GPUParticles3D.draw_pass_2<class_GPUParticles3D_property_draw_pass_2>`{.interpreted-text
role="ref"},
`GPUParticles3D.draw_pass_3<class_GPUParticles3D_property_draw_pass_3>`{.interpreted-text
role="ref"}, and
`GPUParticles3D.draw_pass_4<class_GPUParticles3D_property_draw_pass_4>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_draw_passes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_draw_passes**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, count:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_draw_passes>`{.interpreted-text
role="ref"}

Sets the number of draw passes to use. Equivalent to
`GPUParticles3D.draw_passes<class_GPUParticles3D_property_draw_passes>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_emission_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_emission_transform**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_emission_transform>`{.interpreted-text
role="ref"}

Sets the `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
that will be used by the particles when they first emit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_emitter_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_emitter_velocity**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, velocity:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_emitter_velocity>`{.interpreted-text
role="ref"}

Sets the velocity of a particle node, that will be used by
`ParticleProcessMaterial.inherit_velocity_ratio<class_ParticleProcessMaterial_property_inherit_velocity_ratio>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_emitting}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_emitting**(particles: `RID<class_RID>`{.interpreted-text
role="ref"}, emitting: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_emitting>`{.interpreted-text
role="ref"}

If `true`, particles will emit over time. Setting to `false` does not
reset the particles, but only stops their emission. Equivalent to
`GPUParticles3D.emitting<class_GPUParticles3D_property_emitting>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_explosiveness_ratio}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_explosiveness_ratio**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, ratio:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_explosiveness_ratio>`{.interpreted-text
role="ref"}

Sets the explosiveness ratio. Equivalent to
`GPUParticles3D.explosiveness<class_GPUParticles3D_property_explosiveness>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_fixed_fps}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_fixed_fps**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, fps:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_fixed_fps>`{.interpreted-text
role="ref"}

Sets the frame rate that the particle system rendering will be fixed to.
Equivalent to
`GPUParticles3D.fixed_fps<class_GPUParticles3D_property_fixed_fps>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_fractional_delta}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_fractional_delta**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_fractional_delta>`{.interpreted-text
role="ref"}

If `true`, uses fractional delta which smooths the movement of the
particles. Equivalent to
`GPUParticles3D.fract_delta<class_GPUParticles3D_property_fract_delta>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_interp_to_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_interp_to_end**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, factor:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_interp_to_end>`{.interpreted-text
role="ref"}

Sets the value that informs a
`ParticleProcessMaterial<class_ParticleProcessMaterial>`{.interpreted-text
role="ref"} to rush all particles towards the end of their lifetime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_interpolate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_interpolate**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_interpolate>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_lifetime}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_lifetime**(particles: `RID<class_RID>`{.interpreted-text
role="ref"}, lifetime: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_particles_set_lifetime>`{.interpreted-text
role="ref"}

Sets the lifetime of each particle in the system. Equivalent to
`GPUParticles3D.lifetime<class_GPUParticles3D_property_lifetime>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_mode**(particles: `RID<class_RID>`{.interpreted-text
role="ref"}, mode:
`ParticlesMode<enum_RenderingServer_ParticlesMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_particles_set_mode>`{.interpreted-text
role="ref"}

Sets whether the GPU particles specified by the `particles` RID should
be rendered in 2D or 3D according to `mode`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_one_shot}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_one_shot**(particles: `RID<class_RID>`{.interpreted-text
role="ref"}, one_shot: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_one_shot>`{.interpreted-text
role="ref"}

If `true`, particles will emit once and then stop. Equivalent to
`GPUParticles3D.one_shot<class_GPUParticles3D_property_one_shot>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_pre_process_time}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_pre_process_time**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_pre_process_time>`{.interpreted-text
role="ref"}

Sets the preprocess time for the particles\' animation. This lets you
delay starting an animation until after the particles have begun
emitting. Equivalent to
`GPUParticles3D.preprocess<class_GPUParticles3D_property_preprocess>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_process_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_process_material**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, material:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_process_material>`{.interpreted-text
role="ref"}

Sets the material for processing the particles.

\*\*Note:\*\* This is not the material used to draw the materials.
Equivalent to
`GPUParticles3D.process_material<class_GPUParticles3D_property_process_material>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_randomness_ratio}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_randomness_ratio**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, ratio:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_randomness_ratio>`{.interpreted-text
role="ref"}

Sets the emission randomness ratio. This randomizes the emission of
particles within their phase. Equivalent to
`GPUParticles3D.randomness<class_GPUParticles3D_property_randomness>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_speed_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_speed_scale**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, scale:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_speed_scale>`{.interpreted-text
role="ref"}

Sets the speed scale of the particle system. Equivalent to
`GPUParticles3D.speed_scale<class_GPUParticles3D_property_speed_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_subemitter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_subemitter**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, subemitter_particles:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_subemitter>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_trail_bind_poses}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_trail_bind_poses**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, bind_poses:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}\])
`🔗<class_RenderingServer_method_particles_set_trail_bind_poses>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_trails}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_trails**(particles: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"},
length_sec: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_trails>`{.interpreted-text
role="ref"}

If `enable` is `true`, enables trails for the `particles` with the
specified `length_sec` in seconds. Equivalent to
`GPUParticles3D.trail_enabled<class_GPUParticles3D_property_trail_enabled>`{.interpreted-text
role="ref"} and
`GPUParticles3D.trail_lifetime<class_GPUParticles3D_property_trail_lifetime>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_transform_align}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_transform_align**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, align:
`ParticlesTransformAlign<enum_RenderingServer_ParticlesTransformAlign>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_particles_set_transform_align>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_particles_set_use_local_coordinates}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**particles_set_use_local_coordinates**(particles:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_particles_set_use_local_coordinates>`{.interpreted-text
role="ref"}

If `true`, particles use local coordinates. If `false` they use global
coordinates. Equivalent to
`GPUParticles3D.local_coords<class_GPUParticles3D_property_local_coords>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_positional_soft_shadow_filter_set_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**positional_soft_shadow_filter_set_quality**(quality:
`ShadowQuality<enum_RenderingServer_ShadowQuality>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_positional_soft_shadow_filter_set_quality>`{.interpreted-text
role="ref"}

Sets the filter quality for omni and spot light shadows in 3D. See also
`ProjectSettings.rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality>`{.interpreted-text
role="ref"}. This parameter is global and cannot be set on a
per-viewport basis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**reflection_probe_create**()
`🔗<class_RenderingServer_method_reflection_probe_create>`{.interpreted-text
role="ref"}

Creates a reflection probe and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`reflection_probe_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

To place in a scene, attach this reflection probe to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"} using the returned RID.

\*\*Note:\*\* The equivalent node is
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_ambient_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_ambient_color**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_ambient_color>`{.interpreted-text
role="ref"}

Sets the reflection probe\'s custom ambient light color. Equivalent to
`ReflectionProbe.ambient_color<class_ReflectionProbe_property_ambient_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_ambient_energy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_ambient_energy**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, energy:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_ambient_energy>`{.interpreted-text
role="ref"}

Sets the reflection probe\'s custom ambient light energy. Equivalent to
`ReflectionProbe.ambient_color_energy<class_ReflectionProbe_property_ambient_color_energy>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_ambient_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_ambient_mode**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`ReflectionProbeAmbientMode<enum_RenderingServer_ReflectionProbeAmbientMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_ambient_mode>`{.interpreted-text
role="ref"}

Sets the reflection probe\'s ambient light mode. Equivalent to
`ReflectionProbe.ambient_mode<class_ReflectionProbe_property_ambient_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_as_interior}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_as_interior**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_as_interior>`{.interpreted-text
role="ref"}

If `true`, reflections will ignore sky contribution. Equivalent to
`ReflectionProbe.interior<class_ReflectionProbe_property_interior>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_blend_distance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_blend_distance**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, blend_distance:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_blend_distance>`{.interpreted-text
role="ref"}

Sets the distance in meters over which a probe blends into the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_cull_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_cull_mask**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, layers:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_cull_mask>`{.interpreted-text
role="ref"}

Sets the render cull mask for this reflection probe. Only instances with
a matching layer will be reflected by this probe. Equivalent to
`ReflectionProbe.cull_mask<class_ReflectionProbe_property_cull_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_enable_box_projection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_enable_box_projection**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_enable_box_projection>`{.interpreted-text
role="ref"}

If `true`, uses box projection. This can make reflections look more
correct in certain situations. Equivalent to
`ReflectionProbe.box_projection<class_ReflectionProbe_property_box_projection>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_enable_shadows}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_enable_shadows**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_enable_shadows>`{.interpreted-text
role="ref"}

If `true`, computes shadows in the reflection probe. This makes the
reflection much slower to compute. Equivalent to
`ReflectionProbe.enable_shadows<class_ReflectionProbe_property_enable_shadows>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_intensity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_intensity**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, intensity:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_intensity>`{.interpreted-text
role="ref"}

Sets the intensity of the reflection probe. Intensity modulates the
strength of the reflection. Equivalent to
`ReflectionProbe.intensity<class_ReflectionProbe_property_intensity>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_max_distance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_max_distance**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, distance:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_max_distance>`{.interpreted-text
role="ref"}

Sets the max distance away from the probe an object can be before it is
culled. Equivalent to
`ReflectionProbe.max_distance<class_ReflectionProbe_property_max_distance>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_mesh_lod_threshold}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_mesh_lod_threshold**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, pixels:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_mesh_lod_threshold>`{.interpreted-text
role="ref"}

Sets the mesh level of detail to use in the reflection probe rendering.
Higher values will use less detailed versions of meshes that have LOD
variations generated, which can improve performance. Equivalent to
`ReflectionProbe.mesh_lod_threshold<class_ReflectionProbe_property_mesh_lod_threshold>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_origin_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_origin_offset**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, offset:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_origin_offset>`{.interpreted-text
role="ref"}

Sets the origin offset to be used when this reflection probe is in box
project mode. Equivalent to
`ReflectionProbe.origin_offset<class_ReflectionProbe_property_origin_offset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_reflection_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_reflection_mask**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, layers:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_reflection_mask>`{.interpreted-text
role="ref"}

Sets the render reflection mask for this reflection probe. Only
instances with a matching layer will have reflections applied from this
probe. Equivalent to
`ReflectionProbe.reflection_mask<class_ReflectionProbe_property_reflection_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_resolution}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_resolution**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, resolution:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_resolution>`{.interpreted-text
role="ref"}

Sets the resolution to use when rendering the specified reflection
probe. The `resolution` is specified for each cubemap face: for
instance, specifying `512` will allocate 6 faces of 512×512 each (plus
mipmaps for roughness levels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_size**(probe: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_size>`{.interpreted-text
role="ref"}

Sets the size of the area that the reflection probe will capture.
Equivalent to
`ReflectionProbe.size<class_ReflectionProbe_property_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_reflection_probe_set_update_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reflection_probe_set_update_mode**(probe:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`ReflectionProbeUpdateMode<enum_RenderingServer_ReflectionProbeUpdateMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_reflection_probe_set_update_mode>`{.interpreted-text
role="ref"}

Sets how often the reflection probe updates. Can either be once or every
frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_request_frame_drawn_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**request_frame_drawn_callback**(callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_request_frame_drawn_callback>`{.interpreted-text
role="ref"}

Schedules a callback to the given callable after a frame has been drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_scenario_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **scenario_create**()
`🔗<class_RenderingServer_method_scenario_create>`{.interpreted-text
role="ref"}

Creates a scenario and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`scenario_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

The scenario is the 3D world that all the visual instances exist in.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_scenario_set_camera_attributes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scenario_set_camera_attributes**(scenario:
`RID<class_RID>`{.interpreted-text role="ref"}, effects:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_scenario_set_camera_attributes>`{.interpreted-text
role="ref"}

Sets the camera attributes (`effects`) that will be used with this
scenario. See also
`CameraAttributes<class_CameraAttributes>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_scenario_set_compositor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scenario_set_compositor**(scenario: `RID<class_RID>`{.interpreted-text
role="ref"}, compositor: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_scenario_set_compositor>`{.interpreted-text
role="ref"}

Sets the compositor (`compositor`) that will be used with this scenario.
See also `Compositor<class_Compositor>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_scenario_set_environment}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scenario_set_environment**(scenario:
`RID<class_RID>`{.interpreted-text role="ref"}, environment:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_scenario_set_environment>`{.interpreted-text
role="ref"}

Sets the environment that will be used with this scenario. See also
`Environment<class_Environment>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_scenario_set_fallback_environment}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scenario_set_fallback_environment**(scenario:
`RID<class_RID>`{.interpreted-text role="ref"}, environment:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_scenario_set_fallback_environment>`{.interpreted-text
role="ref"}

Sets the fallback environment to be used by this scenario. The fallback
environment is used if no environment is set. Internally, this is used
by the editor to provide a default environment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_screen_space_roughness_limiter_set_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**screen_space_roughness_limiter_set_active**(enable:
`bool<class_bool>`{.interpreted-text role="ref"}, amount:
`float<class_float>`{.interpreted-text role="ref"}, limit:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_screen_space_roughness_limiter_set_active>`{.interpreted-text
role="ref"}

Sets the screen-space roughness limiter parameters, such as whether it
should be enabled and its thresholds. Equivalent to
`ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/enabled<class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/enabled>`{.interpreted-text
role="ref"},
`ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/amount<class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/amount>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/anti_aliasing/screen_space_roughness_limiter/limit<class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/limit>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_set_boot_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_boot_image**(image: `Image<class_Image>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"},
scale: `bool<class_bool>`{.interpreted-text role="ref"}, use_filter:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_RenderingServer_method_set_boot_image>`{.interpreted-text
role="ref"}

Sets a boot image. The color defines the background color. If `scale` is
`true`, the image will be scaled to fit the screen size. If `use_filter`
is `true`, the image will be scaled with linear interpolation. If
`use_filter` is `false`, the image will be scaled with nearest-neighbor
interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_set_debug_generate_wireframes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_debug_generate_wireframes**(generate:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_set_debug_generate_wireframes>`{.interpreted-text
role="ref"}

If `generate` is `true`, generates debug wireframes for all meshes that
are loaded when using the Compatibility renderer. By default, the engine
does not generate debug wireframes at runtime, since they slow down
loading of assets and take up VRAM.

\*\*Note:\*\* You must call this method before loading any meshes when
using the Compatibility renderer, otherwise wireframes will not be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_set_default_clear_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_default_clear_color**(color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_set_default_clear_color>`{.interpreted-text
role="ref"}

Sets the default clear color which is used when a specific clear color
has not been selected. See also
`get_default_clear_color()<class_RenderingServer_method_get_default_clear_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_shader_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **shader_create**()
`🔗<class_RenderingServer_method_shader_create>`{.interpreted-text
role="ref"}

Creates an empty shader and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`shader_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`Shader<class_Shader>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_shader_get_code}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**shader_get_code**(shader: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_shader_get_code>`{.interpreted-text
role="ref"}

Returns a shader\'s source code as a string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_shader_get_default_texture_parameter}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**shader_get_default_texture_parameter**(shader:
`RID<class_RID>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_shader_get_default_texture_parameter>`{.interpreted-text
role="ref"}

Returns a default texture from a shader searched by name.

\*\*Note:\*\* If the sampler array is used use `index` to access the
specified texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_shader_get_parameter_default}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**shader_get_parameter_default**(shader:
`RID<class_RID>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_shader_get_parameter_default>`{.interpreted-text
role="ref"}

Returns the default value for the specified shader uniform. This is
usually the value written in the shader source code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_shader_set_code}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shader_set_code**(shader: `RID<class_RID>`{.interpreted-text
role="ref"}, code: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_shader_set_code>`{.interpreted-text
role="ref"}

Sets the shader\'s source code (which triggers recompilation after being
changed).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_shader_set_default_texture_parameter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shader_set_default_texture_parameter**(shader:
`RID<class_RID>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, texture:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_RenderingServer_method_shader_set_default_texture_parameter>`{.interpreted-text
role="ref"}

Sets a shader\'s default texture. Overwrites the texture given by name.

\*\*Note:\*\* If the sampler array is used use `index` to access the
specified texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_shader_set_path_hint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shader_set_path_hint**(shader: `RID<class_RID>`{.interpreted-text
role="ref"}, path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_shader_set_path_hint>`{.interpreted-text
role="ref"}

Sets the path hint for the specified shader. This should generally match
the `Shader<class_Shader>`{.interpreted-text role="ref"} resource\'s
`Resource.resource_path<class_Resource_property_resource_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_skeleton_allocate_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**skeleton_allocate_data**(skeleton: `RID<class_RID>`{.interpreted-text
role="ref"}, bones: `int<class_int>`{.interpreted-text role="ref"},
is_2d_skeleton: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_RenderingServer_method_skeleton_allocate_data>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_skeleton_bone_get_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**skeleton_bone_get_transform**(skeleton:
`RID<class_RID>`{.interpreted-text role="ref"}, bone:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_skeleton_bone_get_transform>`{.interpreted-text
role="ref"}

Returns the `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} set for a specific bone of this skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_skeleton_bone_get_transform_2d}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**skeleton_bone_get_transform_2d**(skeleton:
`RID<class_RID>`{.interpreted-text role="ref"}, bone:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_skeleton_bone_get_transform_2d>`{.interpreted-text
role="ref"}

Returns the `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"} set for a specific bone of this skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_skeleton_bone_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**skeleton_bone_set_transform**(skeleton:
`RID<class_RID>`{.interpreted-text role="ref"}, bone:
`int<class_int>`{.interpreted-text role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_skeleton_bone_set_transform>`{.interpreted-text
role="ref"}

Sets the `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
for a specific bone of this skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_skeleton_bone_set_transform_2d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**skeleton_bone_set_transform_2d**(skeleton:
`RID<class_RID>`{.interpreted-text role="ref"}, bone:
`int<class_int>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_skeleton_bone_set_transform_2d>`{.interpreted-text
role="ref"}

Sets the `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
for a specific bone of this skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_skeleton_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **skeleton_create**()
`🔗<class_RenderingServer_method_skeleton_create>`{.interpreted-text
role="ref"}

Creates a skeleton and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`skeleton_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_skeleton_get_bone_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**skeleton_get_bone_count**(skeleton: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_skeleton_get_bone_count>`{.interpreted-text
role="ref"}

Returns the number of bones allocated for this skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_skeleton_set_base_transform_2d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**skeleton_set_base_transform_2d**(skeleton:
`RID<class_RID>`{.interpreted-text role="ref"}, base_transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_skeleton_set_base_transform_2d>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_sky_bake_panorama}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**sky_bake_panorama**(sky: `RID<class_RID>`{.interpreted-text
role="ref"}, energy: `float<class_float>`{.interpreted-text role="ref"},
bake_irradiance: `bool<class_bool>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_sky_bake_panorama>`{.interpreted-text
role="ref"}

Generates and returns an `Image<class_Image>`{.interpreted-text
role="ref"} containing the radiance map for the specified `sky` RID.
This supports built-in sky material and custom sky shaders. If
`bake_irradiance` is `true`, the irradiance map is saved instead of the
radiance map. The radiance map is used to render reflected light, while
the irradiance map is used to render ambient light. See also
`environment_bake_panorama()<class_RenderingServer_method_environment_bake_panorama>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The image is saved in linear color space without any
tonemapping performed, which means it will look too dark if viewed
directly in an image editor. `energy` values above `1.0` can be used to
brighten the resulting image.

\*\*Note:\*\* `size` should be a 2:1 aspect ratio for the generated
panorama to have square pixels. For radiance maps, there is no point in
using a height greater than
`Sky.radiance_size<class_Sky_property_radiance_size>`{.interpreted-text
role="ref"}, as it won\'t increase detail. Irradiance maps only contain
low-frequency data, so there is usually no point in going past a size of
128×64 pixels when saving an irradiance map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_sky_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **sky_create**()
`🔗<class_RenderingServer_method_sky_create>`{.interpreted-text
role="ref"}

Creates an empty sky and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`sky_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_sky_set_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**sky_set_material**(sky: `RID<class_RID>`{.interpreted-text
role="ref"}, material: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_sky_set_material>`{.interpreted-text
role="ref"}

Sets the material that the sky uses to render the background, ambient
and reflection maps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_sky_set_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**sky_set_mode**(sky: `RID<class_RID>`{.interpreted-text role="ref"},
mode: `SkyMode<enum_RenderingServer_SkyMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_sky_set_mode>`{.interpreted-text
role="ref"}

Sets the process `mode` of the sky specified by the `sky` RID.
Equivalent to
`Sky.process_mode<class_Sky_property_process_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_sky_set_radiance_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**sky_set_radiance_size**(sky: `RID<class_RID>`{.interpreted-text
role="ref"}, radiance_size: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_sky_set_radiance_size>`{.interpreted-text
role="ref"}

Sets the `radiance_size` of the sky specified by the `sky` RID (in
pixels). Equivalent to
`Sky.radiance_size<class_Sky_property_radiance_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_spot_light_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **spot_light_create**()
`🔗<class_RenderingServer_method_spot_light_create>`{.interpreted-text
role="ref"}

Creates a spot light and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID can be used in most
`light_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

To place in a scene, attach this spot light to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"} using the returned RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_sub_surface_scattering_set_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**sub_surface_scattering_set_quality**(quality:
`SubSurfaceScatteringQuality<enum_RenderingServer_SubSurfaceScatteringQuality>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_sub_surface_scattering_set_quality>`{.interpreted-text
role="ref"}

Sets
`ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_quality<class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_quality>`{.interpreted-text
role="ref"} to use when rendering materials that have subsurface
scattering enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_sub_surface_scattering_set_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**sub_surface_scattering_set_scale**(scale:
`float<class_float>`{.interpreted-text role="ref"}, depth_scale:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_sub_surface_scattering_set_scale>`{.interpreted-text
role="ref"}

Sets the
`ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_scale<class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_scale>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale<class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale>`{.interpreted-text
role="ref"} to use when rendering materials that have subsurface
scattering enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_2d_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_2d_create**(image: `Image<class_Image>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_texture_2d_create>`{.interpreted-text
role="ref"}

Creates a 2-dimensional texture and adds it to the RenderingServer. It
can be accessed with the RID that is returned. This RID will be used in
all `texture_2d_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Not to be confused with
`RenderingDevice.texture_create()<class_RenderingDevice_method_texture_create>`{.interpreted-text
role="ref"}, which creates the graphics API\'s own texture type as
opposed to the Godot-specific
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_2d_get}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**texture_2d_get**(texture: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_texture_2d_get>`{.interpreted-text
role="ref"}

Returns an `Image<class_Image>`{.interpreted-text role="ref"} instance
from the given `texture` `RID<class_RID>`{.interpreted-text role="ref"}.

\*\*Example:\*\* Get the test texture from
`get_test_texture()<class_RenderingServer_method_get_test_texture>`{.interpreted-text
role="ref"} and apply it to a
`Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"} node:

    var texture_rid = RenderingServer.get_test_texture()
    var texture = ImageTexture.create_from_image(RenderingServer.texture_2d_get(texture_rid))
    $Sprite2D.texture = texture

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_2d_layer_get}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**texture_2d_layer_get**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_texture_2d_layer_get>`{.interpreted-text
role="ref"}

Returns an `Image<class_Image>`{.interpreted-text role="ref"} instance
from the given `texture` `RID<class_RID>`{.interpreted-text role="ref"}
and `layer`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_2d_layered_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_2d_layered_create**(layers:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\],
layered_type:
`TextureLayeredType<enum_RenderingServer_TextureLayeredType>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_texture_2d_layered_create>`{.interpreted-text
role="ref"}

Creates a 2-dimensional layered texture and adds it to the
RenderingServer. It can be accessed with the RID that is returned. This
RID will be used in all `texture_2d_layered_*` RenderingServer
functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_2d_layered_placeholder_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_2d_layered_placeholder_create**(layered_type:
`TextureLayeredType<enum_RenderingServer_TextureLayeredType>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_texture_2d_layered_placeholder_create>`{.interpreted-text
role="ref"}

Creates a placeholder for a 2-dimensional layered texture and adds it to
the RenderingServer. It can be accessed with the RID that is returned.
This RID will be used in all `texture_2d_layered_*` RenderingServer
functions, although it does nothing when used. See also
`texture_2d_placeholder_create()<class_RenderingServer_method_texture_2d_placeholder_create>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The equivalent resource is
`PlaceholderTextureLayered<class_PlaceholderTextureLayered>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_2d_placeholder_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_2d_placeholder_create**()
`🔗<class_RenderingServer_method_texture_2d_placeholder_create>`{.interpreted-text
role="ref"}

Creates a placeholder for a 2-dimensional layered texture and adds it to
the RenderingServer. It can be accessed with the RID that is returned.
This RID will be used in all `texture_2d_layered_*` RenderingServer
functions, although it does nothing when used. See also
`texture_2d_layered_placeholder_create()<class_RenderingServer_method_texture_2d_layered_placeholder_create>`{.interpreted-text
role="ref"}.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`PlaceholderTexture2D<class_PlaceholderTexture2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_2d_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**texture_2d_update**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, image: `Image<class_Image>`{.interpreted-text role="ref"},
layer: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_texture_2d_update>`{.interpreted-text
role="ref"}

Updates the texture specified by the `texture`
`RID<class_RID>`{.interpreted-text role="ref"} with the data in `image`.
A `layer` must also be specified, which should be `0` when updating a
single-layer texture (`Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* The `image` must have the same width, height and format as
the current `texture` data. Otherwise, an error will be printed and the
original texture won\'t be modified. If you need to use different width,
height or format, use
`texture_replace()<class_RenderingServer_method_texture_replace>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_3d_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_3d_create**(format:
`Format<enum_Image_Format>`{.interpreted-text role="ref"}, width:
`int<class_int>`{.interpreted-text role="ref"}, height:
`int<class_int>`{.interpreted-text role="ref"}, depth:
`int<class_int>`{.interpreted-text role="ref"}, mipmaps:
`bool<class_bool>`{.interpreted-text role="ref"}, data:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\])
`🔗<class_RenderingServer_method_texture_3d_create>`{.interpreted-text
role="ref"}

**Note:** The equivalent resource is
`Texture3D<class_Texture3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_3d_get}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\]
**texture_3d_get**(texture: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_texture_3d_get>`{.interpreted-text
role="ref"}

Returns 3D texture data as an array of
`Image<class_Image>`{.interpreted-text role="ref"}s for the specified
texture `RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_3d_placeholder_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_3d_placeholder_create**()
`🔗<class_RenderingServer_method_texture_3d_placeholder_create>`{.interpreted-text
role="ref"}

Creates a placeholder for a 3-dimensional texture and adds it to the
RenderingServer. It can be accessed with the RID that is returned. This
RID will be used in all `texture_3d_*` RenderingServer functions,
although it does nothing when used.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent resource is
`PlaceholderTexture3D<class_PlaceholderTexture3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_3d_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**texture_3d_update**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, data: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\])
`🔗<class_RenderingServer_method_texture_3d_update>`{.interpreted-text
role="ref"}

Updates the texture specified by the `texture`
`RID<class_RID>`{.interpreted-text role="ref"}\'s data with the data in
`data`. All the texture\'s layers must be replaced at once.

\*\*Note:\*\* The `texture` must have the same width, height, depth and
format as the current texture data. Otherwise, an error will be printed
and the original texture won\'t be modified. If you need to use
different width, height, depth or format, use
`texture_replace()<class_RenderingServer_method_texture_replace>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_create_from_native_handle}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_create_from_native_handle**(type:
`TextureType<enum_RenderingServer_TextureType>`{.interpreted-text
role="ref"}, format: `Format<enum_Image_Format>`{.interpreted-text
role="ref"}, native_handle: `int<class_int>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"},
height: `int<class_int>`{.interpreted-text role="ref"}, depth:
`int<class_int>`{.interpreted-text role="ref"}, layers:
`int<class_int>`{.interpreted-text role="ref"} = 1, layered_type:
`TextureLayeredType<enum_RenderingServer_TextureLayeredType>`{.interpreted-text
role="ref"} = 0)
`🔗<class_RenderingServer_method_texture_create_from_native_handle>`{.interpreted-text
role="ref"}

Creates a texture based on a native handle that was created outside of
Godot\'s renderer.

\*\*Note:\*\* If using only the rendering device renderer, it\'s
recommend to use
`RenderingDevice.texture_create_from_extension()<class_RenderingDevice_method_texture_create_from_extension>`{.interpreted-text
role="ref"} together with
`texture_rd_create()<class_RenderingServer_method_texture_rd_create>`{.interpreted-text
role="ref"}, rather than this method. It will give you much more control
over the texture\'s format and usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_get_format}
::: rst-class
classref-method
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**texture_get_format**(texture: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_texture_get_format>`{.interpreted-text
role="ref"}

Returns the format for the texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_get_native_handle}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**texture_get_native_handle**(texture:
`RID<class_RID>`{.interpreted-text role="ref"}, srgb:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_texture_get_native_handle>`{.interpreted-text
role="ref"}

Returns the internal graphics handle for this texture object. For use
when communicating with third-party APIs mostly with GDExtension.

\*\*Note:\*\* This function returns a `uint64_t` which internally maps
to a `GLuint` (OpenGL) or `VkImage` (Vulkan).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_get_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**texture_get_path**(texture: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_texture_get_path>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_get_rd_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_get_rd_texture**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, srgb: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_texture_get_rd_texture>`{.interpreted-text
role="ref"}

Returns a texture `RID<class_RID>`{.interpreted-text role="ref"} that
can be used with
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_proxy_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_proxy_create**(base: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_texture_proxy_create>`{.interpreted-text
role="ref"}

**Deprecated:** ProxyTexture was removed in Godot 4.

This method does nothing and always returns an invalid
`RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_proxy_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**texture_proxy_update**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, proxy_to: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_texture_proxy_update>`{.interpreted-text
role="ref"}

**Deprecated:** ProxyTexture was removed in Godot 4.

This method does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_rd_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_rd_create**(rd_texture: `RID<class_RID>`{.interpreted-text
role="ref"}, layer_type:
`TextureLayeredType<enum_RenderingServer_TextureLayeredType>`{.interpreted-text
role="ref"} = 0)
`🔗<class_RenderingServer_method_texture_rd_create>`{.interpreted-text
role="ref"}

Creates a new texture object based on a texture created directly on the
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.
If the texture contains layers, `layer_type` is used to define the layer
type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_replace}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**texture_replace**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, by_texture: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_texture_replace>`{.interpreted-text
role="ref"}

Replaces `texture`\'s texture data by the texture specified by the
`by_texture` RID, without changing `texture`\'s RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_set_force_redraw_if_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**texture_set_force_redraw_if_visible**(texture:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_texture_set_force_redraw_if_visible>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_set_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**texture_set_path**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_texture_set_path>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_texture_set_size_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**texture_set_size_override**(texture:
`RID<class_RID>`{.interpreted-text role="ref"}, width:
`int<class_int>`{.interpreted-text role="ref"}, height:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_texture_set_size_override>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_attach_camera}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_attach_camera**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, camera: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_attach_camera>`{.interpreted-text
role="ref"}

Sets a viewport\'s camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_attach_canvas}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_attach_canvas**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, canvas: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_attach_canvas>`{.interpreted-text
role="ref"}

Sets a viewport\'s canvas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_attach_to_screen}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_attach_to_screen**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"} = Rect2(0, 0, 0, 0),
screen: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_RenderingServer_method_viewport_attach_to_screen>`{.interpreted-text
role="ref"}

Copies the viewport to a region of the screen specified by `rect`. If
`viewport_set_render_direct_to_screen()<class_RenderingServer_method_viewport_set_render_direct_to_screen>`{.interpreted-text
role="ref"} is `true`, then the viewport does not use a framebuffer and
the contents of the viewport are rendered directly to screen. However,
note that the root viewport is drawn last, therefore it will draw over
the screen. Accordingly, you must set the root viewport to an area that
does not cover the area that you have attached this viewport to.

For example, you can set the root viewport to not render at all with the
following code:

:::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   RenderingServer.viewport_attach_to_screen(get_viewport().get_viewport_rid(),
    Rect2())
    RenderingServer.viewport_attach_to_screen(\$Viewport.get_viewport_rid(),
    Rect2(0, 0, 600, 600))
:::
::::

Using this can result in significant optimization, especially on
lower-end devices. However, it comes at the cost of having to manage
your viewports manually. For further optimization, see
`viewport_set_render_direct_to_screen()<class_RenderingServer_method_viewport_set_render_direct_to_screen>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **viewport_create**()
`🔗<class_RenderingServer_method_viewport_create>`{.interpreted-text
role="ref"}

Creates an empty viewport and adds it to the RenderingServer. It can be
accessed with the RID that is returned. This RID will be used in all
`viewport_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent node is
`Viewport<class_Viewport>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_get_measured_render_time_cpu}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**viewport_get_measured_render_time_cpu**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_viewport_get_measured_render_time_cpu>`{.interpreted-text
role="ref"}

Returns the CPU time taken to render the last frame in milliseconds.
This *only* includes time spent in rendering-related operations;
scripts\' `_process` functions and other engine subsystems are not
included in this readout. To get a complete readout of CPU time spent to
render the scene, sum the render times of all viewports that are drawn
every frame plus
`get_frame_setup_time_cpu()<class_RenderingServer_method_get_frame_setup_time_cpu>`{.interpreted-text
role="ref"}. Unlike
`Engine.get_frames_per_second()<class_Engine_method_get_frames_per_second>`{.interpreted-text
role="ref"}, this method will accurately reflect CPU utilization even if
framerate is capped via V-Sync or
`Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
role="ref"}. See also
`viewport_get_measured_render_time_gpu()<class_RenderingServer_method_viewport_get_measured_render_time_gpu>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Requires measurements to be enabled on the specified
`viewport` using
`viewport_set_measure_render_time()<class_RenderingServer_method_viewport_set_measure_render_time>`{.interpreted-text
role="ref"}. Otherwise, this method returns `0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_get_measured_render_time_gpu}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**viewport_get_measured_render_time_gpu**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_viewport_get_measured_render_time_gpu>`{.interpreted-text
role="ref"}

Returns the GPU time taken to render the last frame in milliseconds. To
get a complete readout of GPU time spent to render the scene, sum the
render times of all viewports that are drawn every frame. Unlike
`Engine.get_frames_per_second()<class_Engine_method_get_frames_per_second>`{.interpreted-text
role="ref"}, this method accurately reflects GPU utilization even if
framerate is capped via V-Sync or
`Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
role="ref"}. See also
`viewport_get_measured_render_time_cpu()<class_RenderingServer_method_viewport_get_measured_render_time_cpu>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Requires measurements to be enabled on the specified
`viewport` using
`viewport_set_measure_render_time()<class_RenderingServer_method_viewport_set_measure_render_time>`{.interpreted-text
role="ref"}. Otherwise, this method returns `0.0`.

\*\*Note:\*\* When GPU utilization is low enough during a certain period
of time, GPUs will decrease their power state (which in turn decreases
core and memory clock speeds). This can cause the reported GPU time to
increase if GPU utilization is kept low enough by a framerate cap
(compared to what it would be at the GPU\'s highest power state). Keep
this in mind when benchmarking using
`viewport_get_measured_render_time_gpu()<class_RenderingServer_method_viewport_get_measured_render_time_gpu>`{.interpreted-text
role="ref"}. This behavior can be overridden in the graphics driver
settings at the cost of higher power usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_get_render_info}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**viewport_get_render_info**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, type:
`ViewportRenderInfoType<enum_RenderingServer_ViewportRenderInfoType>`{.interpreted-text
role="ref"}, info:
`ViewportRenderInfo<enum_RenderingServer_ViewportRenderInfo>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_get_render_info>`{.interpreted-text
role="ref"}

Returns a statistic about the rendering engine which can be used for
performance profiling. This is separated into render pass `type`s, each
of them having the same `info`s you can query (different passes will
return different values).

See also
`get_rendering_info()<class_RenderingServer_method_get_rendering_info>`{.interpreted-text
role="ref"}, which returns global information across all viewports.

\*\*Note:\*\* Viewport rendering information is not available until at
least 2 frames have been rendered by the engine. If rendering
information is not available,
`viewport_get_render_info()<class_RenderingServer_method_viewport_get_render_info>`{.interpreted-text
role="ref"} returns `0`. To print rendering information in `_ready()`
successfully, use the following:

    func _ready():
        for _i in 2:
            await get_tree().process_frame

        print(
                RenderingServer.viewport_get_render_info(get_viewport().get_viewport_rid(),
                RenderingServer.VIEWPORT_RENDER_INFO_TYPE_VISIBLE,
                RenderingServer.VIEWPORT_RENDER_INFO_DRAW_CALLS_IN_FRAME)
        )

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_get_render_target}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**viewport_get_render_target**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_viewport_get_render_target>`{.interpreted-text
role="ref"}

Returns the render target for the viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_get_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**viewport_get_texture**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_viewport_get_texture>`{.interpreted-text
role="ref"}

Returns the viewport\'s last rendered frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_get_update_mode}
::: rst-class
classref-method
:::
::::

`ViewportUpdateMode<enum_RenderingServer_ViewportUpdateMode>`{.interpreted-text
role="ref"} **viewport_get_update_mode**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_viewport_get_update_mode>`{.interpreted-text
role="ref"}

Returns the viewport\'s update mode.

\*\*Warning:\*\* Calling this from any thread other than the rendering
thread will be detrimental to performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_remove_canvas}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_remove_canvas**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, canvas: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_remove_canvas>`{.interpreted-text
role="ref"}

Detaches a viewport from a canvas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_active**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, active: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_active>`{.interpreted-text
role="ref"}

If `true`, sets the viewport active, else sets it inactive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_anisotropic_filtering_level}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_anisotropic_filtering_level**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"},
anisotropic_filtering_level:
`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_anisotropic_filtering_level>`{.interpreted-text
role="ref"}

Sets the maximum number of samples to take when using anisotropic
filtering on textures (as a power of two). A higher sample count will
result in sharper textures at oblique angles, but is more expensive to
compute. A value of `0` forcibly disables anisotropic filtering, even on
materials where it is enabled.

The anisotropic filtering level also affects decals and light projectors
if they are configured to use anisotropic filtering. See
`ProjectSettings.rendering/textures/decals/filter<class_ProjectSettings_property_rendering/textures/decals/filter>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/textures/light_projectors/filter<class_ProjectSettings_property_rendering/textures/light_projectors/filter>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In 3D, for this setting to have an effect, set
`BaseMaterial3D.texture_filter<class_BaseMaterial3D_property_texture_filter>`{.interpreted-text
role="ref"} to
`BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC<class_BaseMaterial3D_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} or
`BaseMaterial3D.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC<class_BaseMaterial3D_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} on materials.

\*\*Note:\*\* In 2D, for this setting to have an effect, set
`CanvasItem.texture_filter<class_CanvasItem_property_texture_filter>`{.interpreted-text
role="ref"} to
`CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC<class_CanvasItem_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} or
`CanvasItem.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC<class_CanvasItem_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} on the `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} node displaying the texture (or in
`CanvasTexture<class_CanvasTexture>`{.interpreted-text role="ref"}).
However, anisotropic filtering is rarely useful in 2D, so only enable it
for textures in 2D if it makes a meaningful visual difference.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_canvas_cull_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_canvas_cull_mask**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, canvas_cull_mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_canvas_cull_mask>`{.interpreted-text
role="ref"}

Sets the rendering mask associated with this
`Viewport<class_Viewport>`{.interpreted-text role="ref"}. Only
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} nodes with
a matching rendering visibility layer will be rendered by this
`Viewport<class_Viewport>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_canvas_stacking}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_canvas_stacking**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, canvas:
`RID<class_RID>`{.interpreted-text role="ref"}, layer:
`int<class_int>`{.interpreted-text role="ref"}, sublayer:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_canvas_stacking>`{.interpreted-text
role="ref"}

Sets the stacking order for a viewport\'s canvas.

`layer` is the actual canvas layer, while `sublayer` specifies the
stacking order of the canvas among those in the same layer.

\*\*Note:\*\* `layer` should be between
`CANVAS_LAYER_MIN<class_RenderingServer_constant_CANVAS_LAYER_MIN>`{.interpreted-text
role="ref"} and
`CANVAS_LAYER_MAX<class_RenderingServer_constant_CANVAS_LAYER_MAX>`{.interpreted-text
role="ref"} (inclusive). Any other value will wrap around.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_canvas_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_canvas_transform**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, canvas:
`RID<class_RID>`{.interpreted-text role="ref"}, offset:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_canvas_transform>`{.interpreted-text
role="ref"}

Sets the transformation of a viewport\'s canvas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_clear_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_clear_mode**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, clear_mode:
`ViewportClearMode<enum_RenderingServer_ViewportClearMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_clear_mode>`{.interpreted-text
role="ref"}

Sets the clear mode of a viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_debug_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_debug_draw**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, draw:
`ViewportDebugDraw<enum_RenderingServer_ViewportDebugDraw>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_debug_draw>`{.interpreted-text
role="ref"}

Sets the debug draw mode of a viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_default_canvas_item_texture_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_default_canvas_item_texture_filter**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, filter:
`CanvasItemTextureFilter<enum_RenderingServer_CanvasItemTextureFilter>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_default_canvas_item_texture_filter>`{.interpreted-text
role="ref"}

Sets the default texture filtering mode for the specified `viewport`
RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_default_canvas_item_texture_repeat}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_default_canvas_item_texture_repeat**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, repeat:
`CanvasItemTextureRepeat<enum_RenderingServer_CanvasItemTextureRepeat>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_default_canvas_item_texture_repeat>`{.interpreted-text
role="ref"}

Sets the default texture repeat mode for the specified `viewport` RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_disable_2d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_disable_2d**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, disable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_disable_2d>`{.interpreted-text
role="ref"}

If `true`, the viewport\'s canvas (i.e. 2D and GUI elements) is not
rendered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_disable_3d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_disable_3d**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, disable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_disable_3d>`{.interpreted-text
role="ref"}

If `true`, the viewport\'s 3D elements are not rendered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_environment_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_environment_mode**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`ViewportEnvironmentMode<enum_RenderingServer_ViewportEnvironmentMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_environment_mode>`{.interpreted-text
role="ref"}

Sets the viewport\'s environment mode which allows enabling or disabling
rendering of 3D environment over 2D canvas. When disabled, 2D will not
be affected by the environment. When enabled, 2D will be affected by the
environment if the environment background mode is
`ENV_BG_CANVAS<class_RenderingServer_constant_ENV_BG_CANVAS>`{.interpreted-text
role="ref"}. The default behavior is to inherit the setting from the
viewport\'s parent. If the topmost parent is also set to
`VIEWPORT_ENVIRONMENT_INHERIT<class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_INHERIT>`{.interpreted-text
role="ref"}, then the behavior will be the same as if it was set to
`VIEWPORT_ENVIRONMENT_ENABLED<class_RenderingServer_constant_VIEWPORT_ENVIRONMENT_ENABLED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_fsr_sharpness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_fsr_sharpness**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, sharpness:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_fsr_sharpness>`{.interpreted-text
role="ref"}

Determines how sharp the upscaled image will be when using the FSR
upscaling mode. Sharpness halves with every whole number. Values go from
0.0 (sharpest) to 2.0. Values above 2.0 won\'t make a visible
difference.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_global_canvas_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_global_canvas_transform**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_global_canvas_transform>`{.interpreted-text
role="ref"}

Sets the viewport\'s global transformation matrix.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_measure_render_time}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_measure_render_time**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_measure_render_time>`{.interpreted-text
role="ref"}

Sets the measurement for the given `viewport` RID (obtained using
`Viewport.get_viewport_rid()<class_Viewport_method_get_viewport_rid>`{.interpreted-text
role="ref"}). Once enabled,
`viewport_get_measured_render_time_cpu()<class_RenderingServer_method_viewport_get_measured_render_time_cpu>`{.interpreted-text
role="ref"} and
`viewport_get_measured_render_time_gpu()<class_RenderingServer_method_viewport_get_measured_render_time_gpu>`{.interpreted-text
role="ref"} will return values greater than `0.0` when queried with the
given `viewport`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_msaa_2d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_msaa_2d**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, msaa:
`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_msaa_2d>`{.interpreted-text
role="ref"}

Sets the multisample antialiasing mode for 2D/Canvas on the specified
`viewport` RID. Equivalent to
`ProjectSettings.rendering/anti_aliasing/quality/msaa_2d<class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_2d>`{.interpreted-text
role="ref"} or
`Viewport.msaa_2d<class_Viewport_property_msaa_2d>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_msaa_3d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_msaa_3d**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, msaa:
`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_msaa_3d>`{.interpreted-text
role="ref"}

Sets the multisample antialiasing mode for 3D on the specified
`viewport` RID. Equivalent to
`ProjectSettings.rendering/anti_aliasing/quality/msaa_3d<class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_3d>`{.interpreted-text
role="ref"} or
`Viewport.msaa_3d<class_Viewport_property_msaa_3d>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_occlusion_culling_build_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_occlusion_culling_build_quality**(quality:
`ViewportOcclusionCullingBuildQuality<enum_RenderingServer_ViewportOcclusionCullingBuildQuality>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_occlusion_culling_build_quality>`{.interpreted-text
role="ref"}

Sets the
`ProjectSettings.rendering/occlusion_culling/bvh_build_quality<class_ProjectSettings_property_rendering/occlusion_culling/bvh_build_quality>`{.interpreted-text
role="ref"} to use for occlusion culling. This parameter is global and
cannot be set on a per-viewport basis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_occlusion_rays_per_thread}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_occlusion_rays_per_thread**(rays_per_thread:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_occlusion_rays_per_thread>`{.interpreted-text
role="ref"}

Sets the
`ProjectSettings.rendering/occlusion_culling/occlusion_rays_per_thread<class_ProjectSettings_property_rendering/occlusion_culling/occlusion_rays_per_thread>`{.interpreted-text
role="ref"} to use for occlusion culling. This parameter is global and
cannot be set on a per-viewport basis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_parent_viewport}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_parent_viewport**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, parent_viewport:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_parent_viewport>`{.interpreted-text
role="ref"}

Sets the viewport\'s parent to the viewport specified by the
`parent_viewport` RID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_positional_shadow_atlas_quadrant_subdivision}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_positional_shadow_atlas_quadrant_subdivision**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, quadrant:
`int<class_int>`{.interpreted-text role="ref"}, subdivision:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_positional_shadow_atlas_quadrant_subdivision>`{.interpreted-text
role="ref"}

Sets the number of subdivisions to use in the specified shadow atlas
`quadrant` for omni and spot shadows. See also
`Viewport.set_positional_shadow_atlas_quadrant_subdiv()<class_Viewport_method_set_positional_shadow_atlas_quadrant_subdiv>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_positional_shadow_atlas_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_positional_shadow_atlas_size**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, use_16_bits:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_RenderingServer_method_viewport_set_positional_shadow_atlas_size>`{.interpreted-text
role="ref"}

Sets the `size` of the shadow atlas\'s images (used for omni and spot
lights) on the viewport specified by the `viewport` RID. The value is
rounded up to the nearest power of 2. If `use_16_bits` is `true`, use 16
bits for the omni/spot shadow depth map. Enabling this results in
shadows having less precision and may result in shadow acne, but can
lead to performance improvements on some devices.

\*\*Note:\*\* If this is set to `0`, no positional shadows will be
visible at all. This can improve performance significantly on low-end
systems by reducing both the CPU and GPU load (as fewer draw calls are
needed to draw the scene without shadows).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_render_direct_to_screen}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_render_direct_to_screen**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_render_direct_to_screen>`{.interpreted-text
role="ref"}

If `true`, render the contents of the viewport directly to screen. This
allows a low-level optimization where you can skip drawing a viewport to
the root viewport. While this optimization can result in a significant
increase in speed (especially on older devices), it comes at a cost of
usability. When this is enabled, you cannot read from the viewport or
from the screen_texture. You also lose the benefit of certain window
settings, such as the various stretch modes. Another consequence to be
aware of is that in 2D the rendering happens in window coordinates, so
if you have a viewport that is double the size of the window, and you
set this, then only the portion that fits within the window will be
drawn, no automatic scaling is possible, even if your game scene is
significantly larger than the window size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_scaling_3d_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_scaling_3d_mode**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, scaling_3d_mode:
`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_scaling_3d_mode>`{.interpreted-text
role="ref"}

Sets the 3D resolution scaling mode. Bilinear scaling renders at
different resolution to either undersample or supersample the viewport.
FidelityFX Super Resolution 1.0, abbreviated to FSR, is an upscaling
technology that produces high quality images at fast framerates by using
a spatially aware upscaling algorithm. FSR is slightly more expensive
than bilinear, but it produces significantly higher image quality. FSR
should be used where possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_scaling_3d_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_scaling_3d_scale**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, scale:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_scaling_3d_scale>`{.interpreted-text
role="ref"}

Scales the 3D render buffer based on the viewport size uses an image
filter specified in
`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} to scale the output image to the full viewport size. Values
lower than `1.0` can be used to speed up 3D rendering at the cost of
quality (undersampling). Values greater than `1.0` are only valid for
bilinear mode and can be used to improve 3D rendering quality at a high
performance cost (supersampling). See also
`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"} for multi-sample antialiasing, which is significantly
cheaper but only smoothens the edges of polygons.

When using FSR upscaling, AMD recommends exposing the following values
as preset options to users \"Ultra Quality: 0.77\", \"Quality: 0.67\",
\"Balanced: 0.59\", \"Performance: 0.5\" instead of exposing the entire
scale.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_scenario}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_scenario**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, scenario: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_scenario>`{.interpreted-text
role="ref"}

Sets a viewport\'s scenario. The scenario contains information about
environment information, reflection atlas, etc.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_screen_space_aa}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_screen_space_aa**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_screen_space_aa>`{.interpreted-text
role="ref"}

Sets the viewport\'s screen-space antialiasing mode. Equivalent to
`ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa<class_ProjectSettings_property_rendering/anti_aliasing/quality/screen_space_aa>`{.interpreted-text
role="ref"} or
`Viewport.screen_space_aa<class_Viewport_property_screen_space_aa>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_sdf_oversize_and_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_sdf_oversize_and_scale**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, oversize:
`ViewportSDFOversize<enum_RenderingServer_ViewportSDFOversize>`{.interpreted-text
role="ref"}, scale:
`ViewportSDFScale<enum_RenderingServer_ViewportSDFScale>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_sdf_oversize_and_scale>`{.interpreted-text
role="ref"}

Sets the viewport\'s 2D signed distance field
`ProjectSettings.rendering/2d/sdf/oversize<class_ProjectSettings_property_rendering/2d/sdf/oversize>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/2d/sdf/scale<class_ProjectSettings_property_rendering/2d/sdf/scale>`{.interpreted-text
role="ref"}. This is used when sampling the signed distance field in
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} shaders as
well as `GPUParticles2D<class_GPUParticles2D>`{.interpreted-text
role="ref"} collision. This is *not* used by SDFGI in 3D rendering.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_size**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"},
height: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_size>`{.interpreted-text
role="ref"}

Sets the viewport\'s width and height in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_snap_2d_transforms_to_pixel}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_snap_2d_transforms_to_pixel**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_snap_2d_transforms_to_pixel>`{.interpreted-text
role="ref"}

If `true`, canvas item transforms (i.e. origin position) are snapped to
the nearest pixel when rendering. This can lead to a crisper appearance
at the cost of less smooth movement, especially when
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"} smoothing is
enabled. Equivalent to
`ProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_transforms_to_pixel>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_snap_2d_vertices_to_pixel}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_snap_2d_vertices_to_pixel**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_snap_2d_vertices_to_pixel>`{.interpreted-text
role="ref"}

If `true`, canvas item vertices (i.e. polygon points) are snapped to the
nearest pixel when rendering. This can lead to a crisper appearance at
the cost of less smooth movement, especially when
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"} smoothing is
enabled. Equivalent to
`ProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_vertices_to_pixel>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_texture_mipmap_bias}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_texture_mipmap_bias**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, mipmap_bias:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_texture_mipmap_bias>`{.interpreted-text
role="ref"}

Affects the final texture sharpness by reading from a lower or higher
mipmap (also called \"texture LOD bias\"). Negative values make
mipmapped textures sharper but grainier when viewed at a distance, while
positive values make mipmapped textures blurrier (even when up close).
To get sharper textures at a distance without introducing too much
graininess, set this between `-0.75` and `0.0`. Enabling temporal
antialiasing
(`ProjectSettings.rendering/anti_aliasing/quality/use_taa<class_ProjectSettings_property_rendering/anti_aliasing/quality/use_taa>`{.interpreted-text
role="ref"}) can help reduce the graininess visible when using negative
mipmap bias.

\*\*Note:\*\* When the 3D scaling mode is set to FSR 1.0, this value is
used to adjust the automatic mipmap bias which is calculated internally
based on the scale factor. The formula for this is
`-log2(1.0 / scale) + mipmap_bias`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_transparent_background}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_transparent_background**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_transparent_background>`{.interpreted-text
role="ref"}

If `true`, the viewport renders its background as transparent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_update_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_update_mode**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, update_mode:
`ViewportUpdateMode<enum_RenderingServer_ViewportUpdateMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_update_mode>`{.interpreted-text
role="ref"}

Sets when the viewport should be updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_use_debanding}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_use_debanding**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_use_debanding>`{.interpreted-text
role="ref"}

Equivalent to
`Viewport.use_debanding<class_Viewport_property_use_debanding>`{.interpreted-text
role="ref"}. See also
`ProjectSettings.rendering/anti_aliasing/quality/use_debanding<class_ProjectSettings_property_rendering/anti_aliasing/quality/use_debanding>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_use_hdr_2d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_use_hdr_2d**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_use_hdr_2d>`{.interpreted-text
role="ref"}

If `true`, 2D rendering will use a high dynamic range (HDR) format
framebuffer matching the bit depth of the 3D framebuffer. When using the
Forward+ renderer this will be an `RGBA16` framebuffer, while when using
the Mobile renderer it will be an `RGB10_A2` framebuffer. Additionally,
2D rendering will take place in linear color space and will be converted
to sRGB space immediately before blitting to the screen (if the Viewport
is attached to the screen). Practically speaking, this means that the
end result of the Viewport will not be clamped into the `0-1` range and
can be used in 3D rendering without color space adjustments. This allows
2D rendering to take advantage of effects requiring high dynamic range
(e.g. 2D glow) as well as substantially improves the appearance of
effects requiring highly detailed gradients. This setting has the same
effect as
`Viewport.use_hdr_2d<class_Viewport_property_use_hdr_2d>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This setting will have no effect when using the
Compatibility renderer, which always renders in low dynamic range for
performance reasons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_use_occlusion_culling}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_use_occlusion_culling**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_use_occlusion_culling>`{.interpreted-text
role="ref"}

If `true`, enables occlusion culling on the specified viewport.
Equivalent to
`ProjectSettings.rendering/occlusion_culling/use_occlusion_culling<class_ProjectSettings_property_rendering/occlusion_culling/use_occlusion_culling>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_use_taa}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_use_taa**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_use_taa>`{.interpreted-text
role="ref"}

If `true`, use temporal antialiasing. Equivalent to
`ProjectSettings.rendering/anti_aliasing/quality/use_taa<class_ProjectSettings_property_rendering/anti_aliasing/quality/use_taa>`{.interpreted-text
role="ref"} or
`Viewport.use_taa<class_Viewport_property_use_taa>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_use_xr}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_use_xr**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, use_xr: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_use_xr>`{.interpreted-text
role="ref"}

If `true`, the viewport uses augmented or virtual reality technologies.
See `XRInterface<class_XRInterface>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_vrs_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_vrs_mode**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"}, mode:
`ViewportVRSMode<enum_RenderingServer_ViewportVRSMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_vrs_mode>`{.interpreted-text
role="ref"}

Sets the Variable Rate Shading (VRS) mode for the viewport. If the GPU
does not support VRS, this property is ignored. Equivalent to
`ProjectSettings.rendering/vrs/mode<class_ProjectSettings_property_rendering/vrs/mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_vrs_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_vrs_texture**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, texture:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_viewport_set_vrs_texture>`{.interpreted-text
role="ref"}

The texture to use when the VRS mode is set to
`VIEWPORT_VRS_TEXTURE<class_RenderingServer_constant_VIEWPORT_VRS_TEXTURE>`{.interpreted-text
role="ref"}. Equivalent to
`ProjectSettings.rendering/vrs/texture<class_ProjectSettings_property_rendering/vrs/texture>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_viewport_set_vrs_update_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**viewport_set_vrs_update_mode**(viewport:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`ViewportVRSUpdateMode<enum_RenderingServer_ViewportVRSUpdateMode>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_viewport_set_vrs_update_mode>`{.interpreted-text
role="ref"}

Sets the update mode for Variable Rate Shading (VRS) for the viewport.
VRS requires the input texture to be converted to the format usable by
the VRS method supported by the hardware. The update mode defines how
often this happens. If the GPU does not support VRS, or VRS is not
enabled, this property is ignored.

If set to
`VIEWPORT_VRS_UPDATE_ONCE<class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_ONCE>`{.interpreted-text
role="ref"}, the input texture is copied once and the mode is changed to
`VIEWPORT_VRS_UPDATE_DISABLED<class_RenderingServer_constant_VIEWPORT_VRS_UPDATE_DISABLED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_visibility_notifier_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**visibility_notifier_create**()
`🔗<class_RenderingServer_method_visibility_notifier_create>`{.interpreted-text
role="ref"}

Creates a new 3D visibility notifier object and adds it to the
RenderingServer. It can be accessed with the RID that is returned. This
RID will be used in all `visibility_notifier_*` RenderingServer
functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

To place in a scene, attach this notifier to an instance using
`instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"} using the returned RID.

\*\*Note:\*\* The equivalent node is
`VisibleOnScreenNotifier3D<class_VisibleOnScreenNotifier3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_visibility_notifier_set_aabb}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**visibility_notifier_set_aabb**(notifier:
`RID<class_RID>`{.interpreted-text role="ref"}, aabb:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_visibility_notifier_set_aabb>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_visibility_notifier_set_callbacks}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**visibility_notifier_set_callbacks**(notifier:
`RID<class_RID>`{.interpreted-text role="ref"}, enter_callable:
`Callable<class_Callable>`{.interpreted-text role="ref"}, exit_callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_visibility_notifier_set_callbacks>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_allocate_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_allocate_data**(voxel_gi: `RID<class_RID>`{.interpreted-text
role="ref"}, to_cell_xform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}, aabb:
`AABB<class_AABB>`{.interpreted-text role="ref"}, octree_size:
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}, octree_cells:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
data_cells: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}, distance_field:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
level_counts:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_allocate_data>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **voxel_gi_create**()
`🔗<class_RenderingServer_method_voxel_gi_create>`{.interpreted-text
role="ref"}

Creates a new voxel-based global illumination object and adds it to the
RenderingServer. It can be accessed with the RID that is returned. This
RID will be used in all `voxel_gi_*` RenderingServer functions.

Once finished with your RID, you will want to free the RID using the
RenderingServer\'s
`free_rid()<class_RenderingServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The equivalent node is
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_get_data_cells}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**voxel_gi_get_data_cells**(voxel_gi: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_voxel_gi_get_data_cells>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_get_distance_field}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**voxel_gi_get_distance_field**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_voxel_gi_get_distance_field>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_get_level_counts}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**voxel_gi_get_level_counts**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_voxel_gi_get_level_counts>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_get_octree_cells}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**voxel_gi_get_octree_cells**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_voxel_gi_get_octree_cells>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_get_octree_size}
::: rst-class
classref-method
:::
::::

`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}
**voxel_gi_get_octree_size**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_voxel_gi_get_octree_size>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_get_to_cell_xform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**voxel_gi_get_to_cell_xform**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingServer_method_voxel_gi_get_to_cell_xform>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_set_baked_exposure_normalization}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_set_baked_exposure_normalization**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"}, baked_exposure:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_set_baked_exposure_normalization>`{.interpreted-text
role="ref"}

Used to inform the renderer what exposure normalization value was used
while baking the voxel gi. This value will be used and modulated at run
time to ensure that the voxel gi maintains a consistent level of
exposure even if the scene-wide exposure normalization is changed at run
time. For more information see
`camera_attributes_set_exposure()<class_RenderingServer_method_camera_attributes_set_exposure>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_set_bias}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_set_bias**(voxel_gi: `RID<class_RID>`{.interpreted-text
role="ref"}, bias: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_set_bias>`{.interpreted-text
role="ref"}

Sets the
`VoxelGIData.bias<class_VoxelGIData_property_bias>`{.interpreted-text
role="ref"} value to use on the specified `voxel_gi`\'s
`RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_set_dynamic_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_set_dynamic_range**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"}, range:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_set_dynamic_range>`{.interpreted-text
role="ref"}

Sets the
`VoxelGIData.dynamic_range<class_VoxelGIData_property_dynamic_range>`{.interpreted-text
role="ref"} value to use on the specified `voxel_gi`\'s
`RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_set_energy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_set_energy**(voxel_gi: `RID<class_RID>`{.interpreted-text
role="ref"}, energy: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_set_energy>`{.interpreted-text
role="ref"}

Sets the
`VoxelGIData.energy<class_VoxelGIData_property_energy>`{.interpreted-text
role="ref"} value to use on the specified `voxel_gi`\'s
`RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_set_interior}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_set_interior**(voxel_gi: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_set_interior>`{.interpreted-text
role="ref"}

Sets the
`VoxelGIData.interior<class_VoxelGIData_property_interior>`{.interpreted-text
role="ref"} value to use on the specified `voxel_gi`\'s
`RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_set_normal_bias}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_set_normal_bias**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"}, bias:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_set_normal_bias>`{.interpreted-text
role="ref"}

Sets the
`VoxelGIData.normal_bias<class_VoxelGIData_property_normal_bias>`{.interpreted-text
role="ref"} value to use on the specified `voxel_gi`\'s
`RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_set_propagation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_set_propagation**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"}, amount:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_set_propagation>`{.interpreted-text
role="ref"}

Sets the
`VoxelGIData.propagation<class_VoxelGIData_property_propagation>`{.interpreted-text
role="ref"} value to use on the specified `voxel_gi`\'s
`RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_set_quality}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_set_quality**(quality:
`VoxelGIQuality<enum_RenderingServer_VoxelGIQuality>`{.interpreted-text
role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_set_quality>`{.interpreted-text
role="ref"}

Sets the
`ProjectSettings.rendering/global_illumination/voxel_gi/quality<class_ProjectSettings_property_rendering/global_illumination/voxel_gi/quality>`{.interpreted-text
role="ref"} value to use when rendering. This parameter is global and
cannot be set on a per-VoxelGI basis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingServer_method_voxel_gi_set_use_two_bounces}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**voxel_gi_set_use_two_bounces**(voxel_gi:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderingServer_method_voxel_gi_set_use_two_bounces>`{.interpreted-text
role="ref"}

Sets the
`VoxelGIData.use_two_bounces<class_VoxelGIData_property_use_two_bounces>`{.interpreted-text
role="ref"} value to use on the specified `voxel_gi`\'s
`RID<class_RID>`{.interpreted-text role="ref"}.
