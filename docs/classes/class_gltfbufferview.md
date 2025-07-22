github_url
:   hide

# GLTFBufferView {#class_GLTFBufferView}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a glTF buffer view.

::: rst-class
classref-introduction-group
:::

## Description

GLTFBufferView is a data structure representing a glTF `bufferView` that
would be found in the `"bufferViews"` array. A buffer is a blob of
binary data. A buffer view is a slice of a buffer that can be used to
identify and extract data from the buffer.

Most custom uses of buffers only need to use the
`buffer<class_GLTFBufferView_property_buffer>`{.interpreted-text
role="ref"},
`byte_length<class_GLTFBufferView_property_byte_length>`{.interpreted-text
role="ref"}, and
`byte_offset<class_GLTFBufferView_property_byte_offset>`{.interpreted-text
role="ref"}. The
`byte_stride<class_GLTFBufferView_property_byte_stride>`{.interpreted-text
role="ref"} and
`indices<class_GLTFBufferView_property_indices>`{.interpreted-text
role="ref"} properties are for more advanced use cases such as
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

## Property Descriptions

:::: {#class_GLTFBufferView_property_buffer}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **buffer** = `-1`
`🔗<class_GLTFBufferView_property_buffer>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_buffer**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_buffer**()

The index of the buffer this buffer view is referencing. If `-1`, this
buffer view is not referencing any buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFBufferView_property_byte_length}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **byte_length** = `0`
`🔗<class_GLTFBufferView_property_byte_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_byte_length**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_byte_length**()

The length, in bytes, of this buffer view. If `0`, this buffer view is
empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFBufferView_property_byte_offset}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **byte_offset** = `0`
`🔗<class_GLTFBufferView_property_byte_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_byte_offset**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_byte_offset**()

The offset, in bytes, from the start of the buffer to the start of this
buffer view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFBufferView_property_byte_stride}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **byte_stride** = `-1`
`🔗<class_GLTFBufferView_property_byte_stride>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_byte_stride**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_byte_stride**()

The stride, in bytes, between interleaved data. If `-1`, this buffer
view is not interleaved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFBufferView_property_indices}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **indices** = `false`
`🔗<class_GLTFBufferView_property_indices>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_indices**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_indices**()

`true` if the GLTFBufferView\'s OpenGL GPU buffer type is an
`ELEMENT_ARRAY_BUFFER` used for vertex indices (integer constant
`34963`). `false` if the buffer type is any other value. See [Buffers,
BufferViews, and
Accessors](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md)
for possible values. This property is set on import and used on export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFBufferView_property_vertex_attributes}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **vertex_attributes** =
`false`
`🔗<class_GLTFBufferView_property_vertex_attributes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertex_attributes**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_vertex_attributes**()

`true` if the GLTFBufferView\'s OpenGL GPU buffer type is an
`ARRAY_BUFFER` used for vertex attributes (integer constant `34962`).
`false` if the buffer type is any other value. See [Buffers,
BufferViews, and
Accessors](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md)
for possible values. This property is set on import and used on export.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFBufferView_method_load_buffer_view_data}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**load_buffer_view_data**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFBufferView_method_load_buffer_view_data>`{.interpreted-text
role="ref"}

Loads the buffer view data from the buffer referenced by this buffer
view in the given `GLTFState<class_GLTFState>`{.interpreted-text
role="ref"}. Interleaved data with a byte stride is not yet supported by
this method. The data is returned as a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.
