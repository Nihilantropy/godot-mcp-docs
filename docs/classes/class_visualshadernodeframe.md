github_url
:   hide

# VisualShaderNodeFrame {#class_VisualShaderNodeFrame}

**Inherits:**
`VisualShaderNodeResizableBase<class_VisualShaderNodeResizableBase>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeComment<class_VisualShaderNodeComment>`{.interpreted-text
role="ref"}

A frame other visual shader nodes can be attached to for better
organization.

::: rst-class
classref-introduction-group
:::

## Description

A rectangular frame that can be used to group visual shader nodes
together to improve organization.

Nodes attached to the frame will move with it when it is dragged and it
can automatically resize to enclose all attached nodes.

Its title, description and color can be customized.

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

:::: {#class_VisualShaderNodeFrame_property_attached_nodes}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**attached_nodes** = `PackedInt32Array()`
`🔗<class_VisualShaderNodeFrame_property_attached_nodes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attached_nodes**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_attached_nodes**()

The list of nodes attached to the frame.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFrame_property_autoshrink}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **autoshrink** = `true`
`🔗<class_VisualShaderNodeFrame_property_autoshrink>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoshrink_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_autoshrink_enabled**()

If `true`, the frame will automatically resize to enclose all attached
nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFrame_property_tint_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **tint_color** =
`Color(0.3, 0.3, 0.3, 0.75)`
`🔗<class_VisualShaderNodeFrame_property_tint_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tint_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_tint_color**()

The color of the frame when
`tint_color_enabled<class_VisualShaderNodeFrame_property_tint_color_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFrame_property_tint_color_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **tint_color_enabled**
= `false`
`🔗<class_VisualShaderNodeFrame_property_tint_color_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tint_color_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_tint_color_enabled**()

If `true`, the frame will be tinted with the color specified in
`tint_color<class_VisualShaderNodeFrame_property_tint_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFrame_property_title}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **title** =
`"Title"`
`🔗<class_VisualShaderNodeFrame_property_title>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_title**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_title**()

The title of the node.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VisualShaderNodeFrame_method_add_attached_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_attached_node**(node: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_VisualShaderNodeFrame_method_add_attached_node>`{.interpreted-text
role="ref"}

Adds a node to the list of nodes attached to the frame. Should not be
called directly, use the
`VisualShader.attach_node_to_frame()<class_VisualShader_method_attach_node_to_frame>`{.interpreted-text
role="ref"} method instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFrame_method_remove_attached_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_attached_node**(node: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_VisualShaderNodeFrame_method_remove_attached_node>`{.interpreted-text
role="ref"}

Removes a node from the list of nodes attached to the frame. Should not
be called directly, use the
`VisualShader.detach_node_from_frame()<class_VisualShader_method_detach_node_from_frame>`{.interpreted-text
role="ref"} method instead.
