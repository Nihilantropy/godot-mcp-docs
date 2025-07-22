github_url
:   hide

# Mesh {#class_Mesh}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `ArrayMesh<class_ArrayMesh>`{.interpreted-text
role="ref"}, `ImmediateMesh<class_ImmediateMesh>`{.interpreted-text
role="ref"}, `PlaceholderMesh<class_PlaceholderMesh>`{.interpreted-text
role="ref"}, `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"}

A `Resource<class_Resource>`{.interpreted-text role="ref"} that contains
vertex array-based geometry.

::: rst-class
classref-introduction-group
:::

## Description

Mesh is a type of `Resource<class_Resource>`{.interpreted-text
role="ref"} that contains vertex array-based geometry, divided in
*surfaces*. Each surface contains a completely separate array and a
material used to draw it. Design wise, a mesh with multiple surfaces is
preferred to a single surface, because objects created in 3D editing
software commonly contain multiple materials. The maximum number of
surfaces per mesh is
`RenderingServer.MAX_MESH_SURFACES<class_RenderingServer_constant_MAX_MESH_SURFACES>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Material Testers
  Demo](https://godotengine.org/asset-library/asset/2742)
- [3D Kinematic Character
  Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

:::: {#enum_Mesh_PrimitiveType}
::: rst-class
classref-enumeration
:::
::::

enum **PrimitiveType**: `🔗<enum_Mesh_PrimitiveType>`{.interpreted-text
role="ref"}

:::: {#class_Mesh_constant_PRIMITIVE_POINTS}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"}
**PRIMITIVE_POINTS** = `0`

Render array as points (one vertex equals one point).

:::: {#class_Mesh_constant_PRIMITIVE_LINES}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"}
**PRIMITIVE_LINES** = `1`

Render array as lines (every two vertices a line is created).

:::: {#class_Mesh_constant_PRIMITIVE_LINE_STRIP}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"}
**PRIMITIVE_LINE_STRIP** = `2`

Render array as line strip.

:::: {#class_Mesh_constant_PRIMITIVE_TRIANGLES}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"}
**PRIMITIVE_TRIANGLES** = `3`

Render array as triangles (every three vertices a triangle is created).

:::: {#class_Mesh_constant_PRIMITIVE_TRIANGLE_STRIP}
::: rst-class
classref-enumeration-constant
:::
::::

`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"}
**PRIMITIVE_TRIANGLE_STRIP** = `4`

Render array as triangle strips.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Mesh_ArrayType}
::: rst-class
classref-enumeration
:::
::::

enum **ArrayType**: `🔗<enum_Mesh_ArrayType>`{.interpreted-text
role="ref"}

:::: {#class_Mesh_constant_ARRAY_VERTEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_VERTEX** = `0`

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"},
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, or `Array<class_Array>`{.interpreted-text role="ref"} of
vertex positions.

:::: {#class_Mesh_constant_ARRAY_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_NORMAL** = `1`

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} of vertex normals.

\*\*Note:\*\* The array has to consist of normal vectors, otherwise they
will be normalized by the engine, potentially causing visual
discrepancies.

:::: {#class_Mesh_constant_ARRAY_TANGENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_TANGENT** = `2`

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} of vertex tangents. Each element in groups of 4 floats,
first 3 floats determine the tangent, and the last the binormal
direction as -1 or 1.

:::: {#class_Mesh_constant_ARRAY_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_COLOR** = `3`

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
of vertex colors.

:::: {#class_Mesh_constant_ARRAY_TEX_UV}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_TEX_UV** = `4`

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for UV coordinates.

:::: {#class_Mesh_constant_ARRAY_TEX_UV2}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_TEX_UV2** = `5`

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for second UV coordinates.

:::: {#class_Mesh_constant_ARRAY_CUSTOM0}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_CUSTOM0** = `6`

Contains custom color channel 0.
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
if
`(format >> Mesh.ARRAY_FORMAT_CUSTOM0_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK`
is
`ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>`{.interpreted-text
role="ref"}, or
`ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>`{.interpreted-text
role="ref"}.
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} otherwise.

:::: {#class_Mesh_constant_ARRAY_CUSTOM1}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_CUSTOM1** = `7`

Contains custom color channel 1.
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
if
`(format >> Mesh.ARRAY_FORMAT_CUSTOM1_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK`
is
`ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>`{.interpreted-text
role="ref"}, or
`ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>`{.interpreted-text
role="ref"}.
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} otherwise.

:::: {#class_Mesh_constant_ARRAY_CUSTOM2}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_CUSTOM2** = `8`

Contains custom color channel 2.
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
if
`(format >> Mesh.ARRAY_FORMAT_CUSTOM2_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK`
is
`ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>`{.interpreted-text
role="ref"}, or
`ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>`{.interpreted-text
role="ref"}.
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} otherwise.

:::: {#class_Mesh_constant_ARRAY_CUSTOM3}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_CUSTOM3** = `9`

Contains custom color channel 3.
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
if
`(format >> Mesh.ARRAY_FORMAT_CUSTOM3_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK`
is
`ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>`{.interpreted-text
role="ref"},
`ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>`{.interpreted-text
role="ref"}, or
`ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>`{.interpreted-text
role="ref"}.
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} otherwise.

:::: {#class_Mesh_constant_ARRAY_BONES}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_BONES** = `10`

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} or
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
of bone indices. Contains either 4 or 8 numbers per vertex depending on
the presence of the
`ARRAY_FLAG_USE_8_BONE_WEIGHTS<class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS>`{.interpreted-text
role="ref"} flag.

:::: {#class_Mesh_constant_ARRAY_WEIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_WEIGHTS** = `11`

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} or
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"} of bone weights in the range `0.0` to `1.0` (inclusive).
Contains either 4 or 8 numbers per vertex depending on the presence of
the
`ARRAY_FLAG_USE_8_BONE_WEIGHTS<class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS>`{.interpreted-text
role="ref"} flag.

:::: {#class_Mesh_constant_ARRAY_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_INDEX** = `12`

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
of integers used as indices referencing vertices, colors, normals,
tangents, and textures. All of those arrays must have the same number of
elements as the vertex array. No index can be beyond the vertex array
size. When this index array is present, it puts the function into
\"index mode,\" where the index selects the *i*\'th vertex, normal,
tangent, color, UV, etc. This means if you want to have different
normals or colors along an edge, you have to duplicate the vertices.

For triangles, the index array is interpreted as triples, referring to
the vertices of each triangle. For lines, the index array is in pairs
indicating the start and end of each line.

:::: {#class_Mesh_constant_ARRAY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"}
**ARRAY_MAX** = `13`

Represents the size of the
`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Mesh_ArrayCustomFormat}
::: rst-class
classref-enumeration
:::
::::

enum **ArrayCustomFormat**:
`🔗<enum_Mesh_ArrayCustomFormat>`{.interpreted-text role="ref"}

:::: {#class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGBA8_UNORM** = `0`

Indicates this custom channel contains unsigned normalized byte colors
from 0 to 1, encoded as
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.

:::: {#class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGBA8_SNORM** = `1`

Indicates this custom channel contains signed normalized byte colors
from -1 to 1, encoded as
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.

:::: {#class_Mesh_constant_ARRAY_CUSTOM_RG_HALF}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RG_HALF** = `2`

Indicates this custom channel contains half precision float colors,
encoded as `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}. Only red and green channels are used.

:::: {#class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGBA_HALF** = `3`

Indicates this custom channel contains half precision float colors,
encoded as `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}.

:::: {#class_Mesh_constant_ARRAY_CUSTOM_R_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_R_FLOAT** = `4`

Indicates this custom channel contains full float colors, in a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}. Only the red channel is used.

:::: {#class_Mesh_constant_ARRAY_CUSTOM_RG_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RG_FLOAT** = `5`

Indicates this custom channel contains full float colors, in a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}. Only red and green channels are used.

:::: {#class_Mesh_constant_ARRAY_CUSTOM_RGB_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGB_FLOAT** = `6`

Indicates this custom channel contains full float colors, in a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}. Only red, green and blue channels are used.

:::: {#class_Mesh_constant_ARRAY_CUSTOM_RGBA_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_RGBA_FLOAT** = `7`

Indicates this custom channel contains full float colors, in a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}.

:::: {#class_Mesh_constant_ARRAY_CUSTOM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} **ARRAY_CUSTOM_MAX** = `8`

Represents the size of the
`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Mesh_ArrayFormat}
::: rst-class
classref-enumeration
:::
::::

flags **ArrayFormat**: `🔗<enum_Mesh_ArrayFormat>`{.interpreted-text
role="ref"}

:::: {#class_Mesh_constant_ARRAY_FORMAT_VERTEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_VERTEX** = `1`

Mesh array contains vertices. All meshes require a vertex array so this
should always be present.

:::: {#class_Mesh_constant_ARRAY_FORMAT_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_NORMAL** = `2`

Mesh array contains normals.

:::: {#class_Mesh_constant_ARRAY_FORMAT_TANGENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_TANGENT** = `4`

Mesh array contains tangents.

:::: {#class_Mesh_constant_ARRAY_FORMAT_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_COLOR** = `8`

Mesh array contains colors.

:::: {#class_Mesh_constant_ARRAY_FORMAT_TEX_UV}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_TEX_UV** = `16`

Mesh array contains UVs.

:::: {#class_Mesh_constant_ARRAY_FORMAT_TEX_UV2}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_TEX_UV2** = `32`

Mesh array contains second UV.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM0}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM0** = `64`

Mesh array contains custom channel index 0.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM1}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM1** = `128`

Mesh array contains custom channel index 1.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM2}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM2** = `256`

Mesh array contains custom channel index 2.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM3}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM3** = `512`

Mesh array contains custom channel index 3.

:::: {#class_Mesh_constant_ARRAY_FORMAT_BONES}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_BONES** = `1024`

Mesh array contains bones.

:::: {#class_Mesh_constant_ARRAY_FORMAT_WEIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_WEIGHTS** = `2048`

Mesh array contains bone weights.

:::: {#class_Mesh_constant_ARRAY_FORMAT_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_INDEX** = `4096`

Mesh array uses indices.

:::: {#class_Mesh_constant_ARRAY_FORMAT_BLEND_SHAPE_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_BLEND_SHAPE_MASK** = `7`

Mask of mesh channels permitted in blend shapes.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM_BASE}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM_BASE** = `13`

Shift of first custom channel.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM_BITS}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM_BITS** = `3`

Number of format bits per custom channel. See
`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"}.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM0_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM0_SHIFT** = `13`

Amount to shift
`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} for custom channel index 0.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM1_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM1_SHIFT** = `16`

Amount to shift
`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} for custom channel index 1.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM2_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM2_SHIFT** = `19`

Amount to shift
`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} for custom channel index 2.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM3_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM3_SHIFT** = `22`

Amount to shift
`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} for custom channel index 3.

:::: {#class_Mesh_constant_ARRAY_FORMAT_CUSTOM_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FORMAT_CUSTOM_MASK** = `7`

Mask of custom format bits per custom channel. Must be shifted by one of
the SHIFT constants. See
`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"}.

:::: {#class_Mesh_constant_ARRAY_COMPRESS_FLAGS_BASE}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_COMPRESS_FLAGS_BASE** = `25`

Shift of first compress flag. Compress flags should be passed to
`ArrayMesh.add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"} and
`SurfaceTool.commit()<class_SurfaceTool_method_commit>`{.interpreted-text
role="ref"}.

:::: {#class_Mesh_constant_ARRAY_FLAG_USE_2D_VERTICES}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FLAG_USE_2D_VERTICES** = `33554432`

Flag used to mark that the array contains 2D vertices.

:::: {#class_Mesh_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FLAG_USE_DYNAMIC_UPDATE** = `67108864`

Flag used to mark that the mesh data will use `GL_DYNAMIC_DRAW` on GLES.
Unused on Vulkan.

:::: {#class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FLAG_USE_8_BONE_WEIGHTS** = `134217728`

Flag used to mark that the mesh contains up to 8 bone influences per
vertex. This flag indicates that
`ARRAY_BONES<class_Mesh_constant_ARRAY_BONES>`{.interpreted-text
role="ref"} and
`ARRAY_WEIGHTS<class_Mesh_constant_ARRAY_WEIGHTS>`{.interpreted-text
role="ref"} elements will have double length.

:::: {#class_Mesh_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY** = `268435456`

Flag used to mark that the mesh intentionally contains no vertex array.

:::: {#class_Mesh_constant_ARRAY_FLAG_COMPRESS_ATTRIBUTES}
::: rst-class
classref-enumeration-constant
:::
::::

`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
**ARRAY_FLAG_COMPRESS_ATTRIBUTES** = `536870912`

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

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Mesh_BlendShapeMode}
::: rst-class
classref-enumeration
:::
::::

enum **BlendShapeMode**:
`🔗<enum_Mesh_BlendShapeMode>`{.interpreted-text role="ref"}

:::: {#class_Mesh_constant_BLEND_SHAPE_MODE_NORMALIZED}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeMode<enum_Mesh_BlendShapeMode>`{.interpreted-text role="ref"}
**BLEND_SHAPE_MODE_NORMALIZED** = `0`

Blend shapes are normalized.

:::: {#class_Mesh_constant_BLEND_SHAPE_MODE_RELATIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeMode<enum_Mesh_BlendShapeMode>`{.interpreted-text role="ref"}
**BLEND_SHAPE_MODE_RELATIVE** = `1`

Blend shapes are relative to base weight.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Mesh_property_lightmap_size_hint}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**lightmap_size_hint** = `Vector2i(0, 0)`
`🔗<class_Mesh_property_lightmap_size_hint>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lightmap_size_hint**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_lightmap_size_hint**()

Sets a hint to be used for lightmap resolution.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Mesh_private_method__get_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **\_get_aabb**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Mesh_private_method__get_aabb>`{.interpreted-text
role="ref"}

Virtual method to override the `AABB<class_AABB>`{.interpreted-text
role="ref"} for a custom class extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__get_blend_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_blend_shape_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__get_blend_shape_count>`{.interpreted-text
role="ref"}

Virtual method to override the number of blend shapes for a custom class
extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__get_blend_shape_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**\_get_blend_shape_name**(index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__get_blend_shape_name>`{.interpreted-text
role="ref"}

Virtual method to override the retrieval of blend shape names for a
custom class extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__get_surface_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_surface_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__get_surface_count>`{.interpreted-text
role="ref"}

Virtual method to override the surface count for a custom class
extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__set_blend_shape_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_blend_shape_name**(index: `int<class_int>`{.interpreted-text
role="ref"}, name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__set_blend_shape_name>`{.interpreted-text
role="ref"}

Virtual method to override the names of blend shapes for a custom class
extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__surface_get_array_index_len}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_surface_get_array_index_len**(index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__surface_get_array_index_len>`{.interpreted-text
role="ref"}

Virtual method to override the surface array index length for a custom
class extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__surface_get_array_len}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_surface_get_array_len**(index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__surface_get_array_len>`{.interpreted-text
role="ref"}

Virtual method to override the surface array length for a custom class
extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__surface_get_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**\_surface_get_arrays**(index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__surface_get_arrays>`{.interpreted-text
role="ref"}

Virtual method to override the surface arrays for a custom class
extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__surface_get_blend_shape_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Array<class_Array>`{.interpreted-text role="ref"}\]
**\_surface_get_blend_shape_arrays**(index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__surface_get_blend_shape_arrays>`{.interpreted-text
role="ref"}

Virtual method to override the blend shape arrays for a custom class
extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__surface_get_format}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_surface_get_format**(index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__surface_get_format>`{.interpreted-text
role="ref"}

Virtual method to override the surface format for a custom class
extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__surface_get_lods}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_surface_get_lods**(index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__surface_get_lods>`{.interpreted-text
role="ref"}

Virtual method to override the surface LODs for a custom class extending
**Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__surface_get_material}
::: rst-class
classref-method
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"}
**\_surface_get_material**(index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__surface_get_material>`{.interpreted-text
role="ref"}

Virtual method to override the surface material for a custom class
extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__surface_get_primitive_type}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_surface_get_primitive_type**(index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__surface_get_primitive_type>`{.interpreted-text
role="ref"}

Virtual method to override the surface primitive type for a custom class
extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_private_method__surface_set_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_surface_set_material**(index: `int<class_int>`{.interpreted-text
role="ref"}, material: `Material<class_Material>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_private_method__surface_set_material>`{.interpreted-text
role="ref"}

Virtual method to override the setting of a `material` at the given
`index` for a custom class extending **Mesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_create_convex_shape}
::: rst-class
classref-method
:::
::::

`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"} **create_convex_shape**(clean:
`bool<class_bool>`{.interpreted-text role="ref"} = true, simplify:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_method_create_convex_shape>`{.interpreted-text
role="ref"}

Calculate a
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"} from the mesh.

If `clean` is `true` (default), duplicate and interior vertices are
removed automatically. You can set it to `false` to make the process
faster if not needed.

If `simplify` is `true`, the geometry can be further simplified to
reduce the number of vertices. Disabled by default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_create_outline}
::: rst-class
classref-method
:::
::::

`Mesh<class_Mesh>`{.interpreted-text role="ref"}
**create_outline**(margin: `float<class_float>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Mesh_method_create_outline>`{.interpreted-text
role="ref"}

Calculate an outline mesh at a defined offset (margin) from the original
mesh.

\*\*Note:\*\* This method typically returns the vertices in reverse
order (e.g. clockwise to counterclockwise).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_create_placeholder}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**create_placeholder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_method_create_placeholder>`{.interpreted-text role="ref"}

Creates a placeholder version of this resource
(`PlaceholderMesh<class_PlaceholderMesh>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_create_trimesh_shape}
::: rst-class
classref-method
:::
::::

`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} **create_trimesh_shape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_method_create_trimesh_shape>`{.interpreted-text
role="ref"}

Calculate a
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} from the mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_generate_triangle_mesh}
::: rst-class
classref-method
:::
::::

`TriangleMesh<class_TriangleMesh>`{.interpreted-text role="ref"}
**generate_triangle_mesh**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_method_generate_triangle_mesh>`{.interpreted-text
role="ref"}

Generate a `TriangleMesh<class_TriangleMesh>`{.interpreted-text
role="ref"} from the mesh. Considers only surfaces using one of these
primitive types:
`PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`{.interpreted-text
role="ref"},
`PRIMITIVE_TRIANGLE_STRIP<class_Mesh_constant_PRIMITIVE_TRIANGLE_STRIP>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_get_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **get_aabb**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Mesh_method_get_aabb>`{.interpreted-text
role="ref"}

Returns the smallest `AABB<class_AABB>`{.interpreted-text role="ref"}
enclosing this mesh in local space. Not affected by `custom_aabb`.

\*\*Note:\*\* This is only implemented for
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"} and
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_get_faces}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_faces**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Mesh_method_get_faces>`{.interpreted-text
role="ref"}

Returns all the vertices that make up the faces of the mesh. Each three
vertices represent one triangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_get_surface_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_surface_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Mesh_method_get_surface_count>`{.interpreted-text
role="ref"}

Returns the number of surfaces that the **Mesh** holds. This is
equivalent to
`MeshInstance3D.get_surface_override_material_count()<class_MeshInstance3D_method_get_surface_override_material_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_surface_get_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**surface_get_arrays**(surf_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_method_surface_get_arrays>`{.interpreted-text role="ref"}

Returns the arrays for the vertices, normals, UVs, etc. that make up the
requested surface (see
`ArrayMesh.add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_surface_get_blend_shape_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Array<class_Array>`{.interpreted-text role="ref"}\]
**surface_get_blend_shape_arrays**(surf_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_method_surface_get_blend_shape_arrays>`{.interpreted-text
role="ref"}

Returns the blend shape arrays for the requested surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_surface_get_material}
::: rst-class
classref-method
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"}
**surface_get_material**(surf_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Mesh_method_surface_get_material>`{.interpreted-text
role="ref"}

Returns a `Material<class_Material>`{.interpreted-text role="ref"} in a
given surface. Surface is rendered using this material.

\*\*Note:\*\* This returns the material within the **Mesh** resource,
not the `Material<class_Material>`{.interpreted-text role="ref"}
associated to the
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}\'s
Surface Material Override properties. To get the
`Material<class_Material>`{.interpreted-text role="ref"} associated to
the `MeshInstance3D<class_MeshInstance3D>`{.interpreted-text
role="ref"}\'s Surface Material Override properties, use
`MeshInstance3D.get_surface_override_material()<class_MeshInstance3D_method_get_surface_override_material>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mesh_method_surface_set_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_set_material**(surf_idx: `int<class_int>`{.interpreted-text
role="ref"}, material: `Material<class_Material>`{.interpreted-text
role="ref"})
`🔗<class_Mesh_method_surface_set_material>`{.interpreted-text
role="ref"}

Sets a `Material<class_Material>`{.interpreted-text role="ref"} for a
given surface. Surface will be rendered using this material.

\*\*Note:\*\* This assigns the material within the **Mesh** resource,
not the `Material<class_Material>`{.interpreted-text role="ref"}
associated to the
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}\'s
Surface Material Override properties. To set the
`Material<class_Material>`{.interpreted-text role="ref"} associated to
the `MeshInstance3D<class_MeshInstance3D>`{.interpreted-text
role="ref"}\'s Surface Material Override properties, use
`MeshInstance3D.set_surface_override_material()<class_MeshInstance3D_method_set_surface_override_material>`{.interpreted-text
role="ref"} instead.
