github_url
:   hide

# OggPacketSequence {#class_OggPacketSequence}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A sequence of Ogg packets.

::: rst-class
classref-introduction-group
:::

## Description

A sequence of Ogg packets.

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

:::: {#class_OggPacketSequence_property_granule_positions}
::: rst-class
classref-property
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**granule_positions** = `PackedInt64Array()`
`🔗<class_OggPacketSequence_property_granule_positions>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_packet_granule_positions**(value:
  `PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
  role="ref"})
- `PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
  role="ref"} **get_packet_granule_positions**()

Contains the granule positions for each page in this packet sequence.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OggPacketSequence_property_packet_data}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Array<class_Array>`{.interpreted-text role="ref"}\]
**packet_data** = `[]`
`🔗<class_OggPacketSequence_property_packet_data>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_packet_data**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`Array<class_Array>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`Array<class_Array>`{.interpreted-text role="ref"}\]
  **get_packet_data**()

Contains the raw packets that make up this OggPacketSequence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OggPacketSequence_property_sampling_rate}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sampling_rate** =
`0.0`
`🔗<class_OggPacketSequence_property_sampling_rate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sampling_rate**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sampling_rate**()

Holds sample rate information about this sequence. Must be set by
another class that actually understands the codec.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OggPacketSequence_method_get_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OggPacketSequence_method_get_length>`{.interpreted-text
role="ref"}

The length of this stream, in seconds.
