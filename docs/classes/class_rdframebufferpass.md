github_url
:   hide

# RDFramebufferPass {#class_RDFramebufferPass}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Framebuffer pass attachment description (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

This class contains the list of attachment descriptions for a
framebuffer pass. Each points with an index to a previously supplied
list of texture attachments.

Multipass framebuffers can optimize some configurations in mobile. On
desktop, they provide little to no advantage.

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

## Constants

:::: {#class_RDFramebufferPass_constant_ATTACHMENT_UNUSED}
::: rst-class
classref-constant
:::
::::

**ATTACHMENT_UNUSED** = `-1`
`🔗<class_RDFramebufferPass_constant_ATTACHMENT_UNUSED>`{.interpreted-text
role="ref"}

Attachment is unused.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_RDFramebufferPass_property_color_attachments}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**color_attachments** = `PackedInt32Array()`
`🔗<class_RDFramebufferPass_property_color_attachments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_attachments**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_color_attachments**()

Color attachments in order starting from 0. If this attachment is not
used by the shader, pass ATTACHMENT_UNUSED to skip.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDFramebufferPass_property_depth_attachment}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **depth_attachment** =
`-1`
`🔗<class_RDFramebufferPass_property_depth_attachment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_attachment**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_depth_attachment**()

Depth attachment. ATTACHMENT_UNUSED should be used if no depth buffer is
required for this pass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDFramebufferPass_property_input_attachments}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**input_attachments** = `PackedInt32Array()`
`🔗<class_RDFramebufferPass_property_input_attachments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_input_attachments**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_input_attachments**()

Used for multipass framebuffers (more than one render pass). Converts an
attachment to an input. Make sure to also supply it properly in the
`RDUniform<class_RDUniform>`{.interpreted-text role="ref"} for the
uniform set.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDFramebufferPass_property_preserve_attachments}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**preserve_attachments** = `PackedInt32Array()`
`🔗<class_RDFramebufferPass_property_preserve_attachments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_preserve_attachments**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_preserve_attachments**()

Attachments to preserve in this pass (otherwise they are erased).

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDFramebufferPass_property_resolve_attachments}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**resolve_attachments** = `PackedInt32Array()`
`🔗<class_RDFramebufferPass_property_resolve_attachments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_resolve_attachments**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_resolve_attachments**()

If the color attachments are multisampled, non-multisampled resolve
attachments can be provided.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.
