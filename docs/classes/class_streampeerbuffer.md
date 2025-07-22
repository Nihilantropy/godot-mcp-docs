github_url
:   hide

# StreamPeerBuffer {#class_StreamPeerBuffer}

**Inherits:** `StreamPeer<class_StreamPeer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A stream peer used to handle binary data streams.

::: rst-class
classref-introduction-group
:::

## Description

A data buffer stream peer that uses a byte array as the stream. This
object can be used to handle binary data from network sessions. To
handle binary data stored in files,
`FileAccess<class_FileAccess>`{.interpreted-text role="ref"} can be used
directly.

A **StreamPeerBuffer** object keeps an internal cursor which is the
offset in bytes to the start of the buffer. Get and put operations are
performed at the cursor position and will move the cursor accordingly.

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

:::: {#class_StreamPeerBuffer_property_data_array}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**data_array** = `PackedByteArray()`
`🔗<class_StreamPeerBuffer_property_data_array>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_data_array**(value:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_data_array**()

The underlying data buffer. Setting this value resets the cursor.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_StreamPeerBuffer_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_StreamPeerBuffer_method_clear>`{.interpreted-text role="ref"}

Clears the
`data_array<class_StreamPeerBuffer_property_data_array>`{.interpreted-text
role="ref"} and resets the cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerBuffer_method_duplicate}
::: rst-class
classref-method
:::
::::

`StreamPeerBuffer<class_StreamPeerBuffer>`{.interpreted-text role="ref"}
**duplicate**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeerBuffer_method_duplicate>`{.interpreted-text
role="ref"}

Returns a new **StreamPeerBuffer** with the same
`data_array<class_StreamPeerBuffer_property_data_array>`{.interpreted-text
role="ref"} content.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerBuffer_method_get_position}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeerBuffer_method_get_position>`{.interpreted-text
role="ref"}

Returns the current cursor position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerBuffer_method_get_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StreamPeerBuffer_method_get_size>`{.interpreted-text
role="ref"}

Returns the size of
`data_array<class_StreamPeerBuffer_property_data_array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerBuffer_method_resize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**resize**(size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeerBuffer_method_resize>`{.interpreted-text role="ref"}

Resizes the
`data_array<class_StreamPeerBuffer_property_data_array>`{.interpreted-text
role="ref"}. This *doesn\'t* update the cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StreamPeerBuffer_method_seek}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**seek**(position: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_StreamPeerBuffer_method_seek>`{.interpreted-text role="ref"}

Moves the cursor to the specified position. `position` must be a valid
index of
`data_array<class_StreamPeerBuffer_property_data_array>`{.interpreted-text
role="ref"}.
