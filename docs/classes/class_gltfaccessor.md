github_url
:   hide

# GLTFAccessor {#class_GLTFAccessor}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a glTF accessor.

::: rst-class
classref-introduction-group
:::

## Description

GLTFAccessor is a data structure representing a glTF `accessor` that
would be found in the `"accessors"` array. A buffer is a blob of binary
data. A buffer view is a slice of a buffer. An accessor is a typed
interpretation of the data in a buffer view.

Most custom data stored in glTF does not need accessors, only buffer
views (see `GLTFBufferView<class_GLTFBufferView>`{.interpreted-text
role="ref"}). Accessors are for more advanced use cases such as
interleaved mesh data encoded for the GPU.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Buffers, BufferViews, and Accessors in Khronos glTF
  specification](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md)
- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
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

## Enumerations

:::: {#enum_GLTFAccessor_GLTFAccessorType}
::: rst-class
classref-enumeration
:::
::::

enum **GLTFAccessorType**:
`🔗<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text role="ref"}

:::: {#class_GLTFAccessor_constant_TYPE_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
role="ref"} **TYPE_SCALAR** = `0`

Accessor type \"SCALAR\". For the glTF object model, this can be used to
map to a single float, int, or bool value, or a float array.

:::: {#class_GLTFAccessor_constant_TYPE_VEC2}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
role="ref"} **TYPE_VEC2** = `1`

Accessor type \"VEC2\". For the glTF object model, this maps to
\"float2\", represented in the glTF JSON as an array of two floats.

:::: {#class_GLTFAccessor_constant_TYPE_VEC3}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
role="ref"} **TYPE_VEC3** = `2`

Accessor type \"VEC3\". For the glTF object model, this maps to
\"float3\", represented in the glTF JSON as an array of three floats.

:::: {#class_GLTFAccessor_constant_TYPE_VEC4}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
role="ref"} **TYPE_VEC4** = `3`

Accessor type \"VEC4\". For the glTF object model, this maps to
\"float4\", represented in the glTF JSON as an array of four floats.

:::: {#class_GLTFAccessor_constant_TYPE_MAT2}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
role="ref"} **TYPE_MAT2** = `4`

Accessor type \"MAT2\". For the glTF object model, this maps to
\"float2x2\", represented in the glTF JSON as an array of four floats.

:::: {#class_GLTFAccessor_constant_TYPE_MAT3}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
role="ref"} **TYPE_MAT3** = `5`

Accessor type \"MAT3\". For the glTF object model, this maps to
\"float3x3\", represented in the glTF JSON as an array of nine floats.

:::: {#class_GLTFAccessor_constant_TYPE_MAT4}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
role="ref"} **TYPE_MAT4** = `6`

Accessor type \"MAT4\". For the glTF object model, this maps to
\"float4x4\", represented in the glTF JSON as an array of sixteen
floats.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_GLTFAccessor_GLTFComponentType}
::: rst-class
classref-enumeration
:::
::::

enum **GLTFComponentType**:
`🔗<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text role="ref"}

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_NONE** = `0`

Component type \"NONE\". This is not a valid component type, and is used
to indicate that the component type is not set.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_SIGNED_BYTE}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_SIGNED_BYTE** = `5120`

Component type \"BYTE\". The value is `0x1400` which comes from OpenGL.
This indicates data is stored in 1-byte or 8-bit signed integers. This
is a core part of the glTF specification.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_UNSIGNED_BYTE}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_UNSIGNED_BYTE** = `5121`

Component type \"UNSIGNED_BYTE\". The value is `0x1401` which comes from
OpenGL. This indicates data is stored in 1-byte or 8-bit unsigned
integers. This is a core part of the glTF specification.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_SIGNED_SHORT}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_SIGNED_SHORT** = `5122`

Component type \"SHORT\". The value is `0x1402` which comes from OpenGL.
This indicates data is stored in 2-byte or 16-bit signed integers. This
is a core part of the glTF specification.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_UNSIGNED_SHORT}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_UNSIGNED_SHORT** = `5123`

Component type \"UNSIGNED_SHORT\". The value is `0x1403` which comes
from OpenGL. This indicates data is stored in 2-byte or 16-bit unsigned
integers. This is a core part of the glTF specification.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_SIGNED_INT}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_SIGNED_INT** = `5124`

Component type \"INT\". The value is `0x1404` which comes from OpenGL.
This indicates data is stored in 4-byte or 32-bit signed integers. This
is NOT a core part of the glTF specification, and may not be supported
by all glTF importers. May be used by some extensions including
`KHR_interactivity`.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_UNSIGNED_INT}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_UNSIGNED_INT** = `5125`

Component type \"UNSIGNED_INT\". The value is `0x1405` which comes from
OpenGL. This indicates data is stored in 4-byte or 32-bit unsigned
integers. This is a core part of the glTF specification.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_SINGLE_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_SINGLE_FLOAT** = `5126`

Component type \"FLOAT\". The value is `0x1406` which comes from OpenGL.
This indicates data is stored in 4-byte or 32-bit floating-point
numbers. This is a core part of the glTF specification.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_DOUBLE_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_DOUBLE_FLOAT** = `5130`

Component type \"DOUBLE\". The value is `0x140A` which comes from
OpenGL. This indicates data is stored in 8-byte or 64-bit floating-point
numbers. This is NOT a core part of the glTF specification, and may not
be supported by all glTF importers. May be used by some extensions
including `KHR_interactivity`.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_HALF_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_HALF_FLOAT** = `5131`

Component type \"HALF_FLOAT\". The value is `0x140B` which comes from
OpenGL. This indicates data is stored in 2-byte or 16-bit floating-point
numbers. This is NOT a core part of the glTF specification, and may not
be supported by all glTF importers. May be used by some extensions
including `KHR_interactivity`.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_SIGNED_LONG}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_SIGNED_LONG** = `5134`

Component type \"LONG\". The value is `0x140E` which comes from OpenGL.
This indicates data is stored in 8-byte or 64-bit signed integers. This
is NOT a core part of the glTF specification, and may not be supported
by all glTF importers. May be used by some extensions including
`KHR_interactivity`.

:::: {#class_GLTFAccessor_constant_COMPONENT_TYPE_UNSIGNED_LONG}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **COMPONENT_TYPE_UNSIGNED_LONG** = `5135`

Component type \"UNSIGNED_LONG\". The value is `0x140F` which comes from
OpenGL. This indicates data is stored in 8-byte or 64-bit unsigned
integers. This is NOT a core part of the glTF specification, and may not
be supported by all glTF importers. May be used by some extensions
including `KHR_interactivity`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GLTFAccessor_property_accessor_type}
::: rst-class
classref-property
:::
::::

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
role="ref"} **accessor_type** = `0`
`🔗<class_GLTFAccessor_property_accessor_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessor_type**(value:
  `GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
  role="ref"})
- `GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
  role="ref"} **get_accessor_type**()

The glTF accessor type, as an enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_buffer_view}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **buffer_view** = `-1`
`🔗<class_GLTFAccessor_property_buffer_view>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_buffer_view**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_buffer_view**()

The index of the buffer view this accessor is referencing. If `-1`, this
accessor is not referencing any buffer view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_byte_offset}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **byte_offset** = `0`
`🔗<class_GLTFAccessor_property_byte_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_byte_offset**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_byte_offset**()

The offset relative to the start of the buffer view in bytes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_component_type}
::: rst-class
classref-property
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **component_type** = `0`
`🔗<class_GLTFAccessor_property_component_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_component_type**(value:
  `GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
  role="ref"})
- `GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
  role="ref"} **get_component_type**()

The glTF component type as an enum. See
`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} for possible values. Within the core glTF specification, a
value of 5125 or \"UNSIGNED_INT\" must not be used for any accessor that
is not referenced by mesh.primitive.indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **count** = `0`
`🔗<class_GLTFAccessor_property_count>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_count**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_count**()

The number of elements referenced by this accessor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_max}
::: rst-class
classref-property
:::
::::

`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"} **max** = `PackedFloat64Array()`
`🔗<class_GLTFAccessor_property_max>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max**(value:
  `PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
  role="ref"})
- `PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
  role="ref"} **get_max**()

Maximum value of each component in this accessor.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_min}
::: rst-class
classref-property
:::
::::

`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"} **min** = `PackedFloat64Array()`
`🔗<class_GLTFAccessor_property_min>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min**(value:
  `PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
  role="ref"})
- `PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
  role="ref"} **get_min**()

Minimum value of each component in this accessor.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_normalized}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **normalized** =
`false` `🔗<class_GLTFAccessor_property_normalized>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_normalized**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_normalized**()

Specifies whether integer data values are normalized before usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_sparse_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sparse_count** = `0`
`🔗<class_GLTFAccessor_property_sparse_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sparse_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_sparse_count**()

Number of deviating accessor values stored in the sparse array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_sparse_indices_buffer_view}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**sparse_indices_buffer_view** = `0`
`🔗<class_GLTFAccessor_property_sparse_indices_buffer_view>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sparse_indices_buffer_view**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_sparse_indices_buffer_view**()

The index of the buffer view with sparse indices. The referenced buffer
view MUST NOT have its target or byteStride properties defined. The
buffer view and the optional byteOffset MUST be aligned to the
componentType byte length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_sparse_indices_byte_offset}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**sparse_indices_byte_offset** = `0`
`🔗<class_GLTFAccessor_property_sparse_indices_byte_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sparse_indices_byte_offset**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_sparse_indices_byte_offset**()

The offset relative to the start of the buffer view in bytes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_sparse_indices_component_type}
::: rst-class
classref-property
:::
::::

`GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
role="ref"} **sparse_indices_component_type** = `0`
`🔗<class_GLTFAccessor_property_sparse_indices_component_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sparse_indices_component_type**(value:
  `GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
  role="ref"})
- `GLTFComponentType<enum_GLTFAccessor_GLTFComponentType>`{.interpreted-text
  role="ref"} **get_sparse_indices_component_type**()

The indices component data type as an enum. Possible values are 5121 for
\"UNSIGNED_BYTE\", 5123 for \"UNSIGNED_SHORT\", and 5125 for
\"UNSIGNED_INT\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_sparse_values_buffer_view}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**sparse_values_buffer_view** = `0`
`🔗<class_GLTFAccessor_property_sparse_values_buffer_view>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sparse_values_buffer_view**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_sparse_values_buffer_view**()

The index of the bufferView with sparse values. The referenced buffer
view MUST NOT have its target or byteStride properties defined.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_sparse_values_byte_offset}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**sparse_values_byte_offset** = `0`
`🔗<class_GLTFAccessor_property_sparse_values_byte_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sparse_values_byte_offset**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_sparse_values_byte_offset**()

The offset relative to the start of the bufferView in bytes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAccessor_property_type}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **type**
`🔗<class_GLTFAccessor_property_type>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_type**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_type**()

**Deprecated:** Use
`accessor_type<class_GLTFAccessor_property_accessor_type>`{.interpreted-text
role="ref"} instead.

The glTF accessor type, as an `int<class_int>`{.interpreted-text
role="ref"}. Possible values are `0` for \"SCALAR\", `1` for \"VEC2\",
`2` for \"VEC3\", `3` for \"VEC4\", `4` for \"MAT2\", `5` for \"MAT3\",
and `6` for \"MAT4\".
