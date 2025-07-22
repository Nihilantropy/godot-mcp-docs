github_url
:   hide

# RDAttachmentFormat {#class_RDAttachmentFormat}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Attachment format (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

This object is used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.

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

:::: {#class_RDAttachmentFormat_property_format}
::: rst-class
classref-property
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **format** = `36`
`🔗<class_RDAttachmentFormat_property_format>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_format**(value:
  `DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
  role="ref"})
- `DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
  role="ref"} **get_format**()

The attachment\'s data format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDAttachmentFormat_property_samples}
::: rst-class
classref-property
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **samples** = `0`
`🔗<class_RDAttachmentFormat_property_samples>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_samples**(value:
  `TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
  role="ref"})
- `TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
  role="ref"} **get_samples**()

The number of samples used when sampling the attachment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDAttachmentFormat_property_usage_flags}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **usage_flags** = `0`
`🔗<class_RDAttachmentFormat_property_usage_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_usage_flags**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_usage_flags**()

The attachment\'s usage flags, which determine what can be done with it.
