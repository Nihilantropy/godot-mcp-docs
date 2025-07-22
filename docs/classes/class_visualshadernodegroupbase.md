github_url
:   hide

# VisualShaderNodeGroupBase {#class_VisualShaderNodeGroupBase}

**Inherits:**
`VisualShaderNodeResizableBase<class_VisualShaderNodeResizableBase>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeExpression<class_VisualShaderNodeExpression>`{.interpreted-text
role="ref"}

Base class for a family of nodes with variable number of input and
output ports within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Currently, has no direct usage, use the derived classes instead.

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

## Method Descriptions

:::: {#class_VisualShaderNodeGroupBase_method_add_input_port}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_input_port**(id: `int<class_int>`{.interpreted-text role="ref"},
type: `int<class_int>`{.interpreted-text role="ref"}, name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_add_input_port>`{.interpreted-text
role="ref"}

Adds an input port with the specified `type` (see
`PortType<enum_VisualShaderNode_PortType>`{.interpreted-text
role="ref"}) and `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_add_output_port}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_output_port**(id: `int<class_int>`{.interpreted-text role="ref"},
type: `int<class_int>`{.interpreted-text role="ref"}, name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_add_output_port>`{.interpreted-text
role="ref"}

Adds an output port with the specified `type` (see
`PortType<enum_VisualShaderNode_PortType>`{.interpreted-text
role="ref"}) and `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_clear_input_ports}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_input_ports**()
`🔗<class_VisualShaderNodeGroupBase_method_clear_input_ports>`{.interpreted-text
role="ref"}

Removes all previously specified input ports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_clear_output_ports}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_output_ports**()
`🔗<class_VisualShaderNodeGroupBase_method_clear_output_ports>`{.interpreted-text
role="ref"}

Removes all previously specified output ports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_get_free_input_port_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_free_input_port_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeGroupBase_method_get_free_input_port_id>`{.interpreted-text
role="ref"}

Returns a free input port ID which can be used in
`add_input_port()<class_VisualShaderNodeGroupBase_method_add_input_port>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_get_free_output_port_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_free_output_port_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeGroupBase_method_get_free_output_port_id>`{.interpreted-text
role="ref"}

Returns a free output port ID which can be used in
`add_output_port()<class_VisualShaderNodeGroupBase_method_add_output_port>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_get_input_port_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_input_port_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeGroupBase_method_get_input_port_count>`{.interpreted-text
role="ref"}

Returns the number of input ports in use. Alternative for
`get_free_input_port_id()<class_VisualShaderNodeGroupBase_method_get_free_input_port_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_get_inputs}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_inputs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeGroupBase_method_get_inputs>`{.interpreted-text
role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"}
description of the input ports as a colon-separated list using the
format `id,type,name;` (see
`add_input_port()<class_VisualShaderNodeGroupBase_method_add_input_port>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_get_output_port_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_output_port_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeGroupBase_method_get_output_port_count>`{.interpreted-text
role="ref"}

Returns the number of output ports in use. Alternative for
`get_free_output_port_id()<class_VisualShaderNodeGroupBase_method_get_free_output_port_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_get_outputs}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_outputs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeGroupBase_method_get_outputs>`{.interpreted-text
role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"}
description of the output ports as a colon-separated list using the
format `id,type,name;` (see
`add_output_port()<class_VisualShaderNodeGroupBase_method_add_output_port>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_has_input_port}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_input_port**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeGroupBase_method_has_input_port>`{.interpreted-text
role="ref"}

Returns `true` if the specified input port exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_has_output_port}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_output_port**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeGroupBase_method_has_output_port>`{.interpreted-text
role="ref"}

Returns `true` if the specified output port exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_is_valid_port_name}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_port_name**(name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeGroupBase_method_is_valid_port_name>`{.interpreted-text
role="ref"}

Returns `true` if the specified port name does not override an existed
port name and is valid within the shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_remove_input_port}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_input_port**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_remove_input_port>`{.interpreted-text
role="ref"}

Removes the specified input port.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_remove_output_port}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_output_port**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_remove_output_port>`{.interpreted-text
role="ref"}

Removes the specified output port.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_set_input_port_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_input_port_name**(id: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_set_input_port_name>`{.interpreted-text
role="ref"}

Renames the specified input port.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_set_input_port_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_input_port_type**(id: `int<class_int>`{.interpreted-text
role="ref"}, type: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_set_input_port_type>`{.interpreted-text
role="ref"}

Sets the specified input port\'s type (see
`PortType<enum_VisualShaderNode_PortType>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_set_inputs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_inputs**(inputs: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_set_inputs>`{.interpreted-text
role="ref"}

Defines all input ports using a `String<class_String>`{.interpreted-text
role="ref"} formatted as a colon-separated list: `id,type,name;` (see
`add_input_port()<class_VisualShaderNodeGroupBase_method_add_input_port>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_set_output_port_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_output_port_name**(id: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_set_output_port_name>`{.interpreted-text
role="ref"}

Renames the specified output port.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_set_output_port_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_output_port_type**(id: `int<class_int>`{.interpreted-text
role="ref"}, type: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_set_output_port_type>`{.interpreted-text
role="ref"}

Sets the specified output port\'s type (see
`PortType<enum_VisualShaderNode_PortType>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeGroupBase_method_set_outputs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_outputs**(outputs: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_VisualShaderNodeGroupBase_method_set_outputs>`{.interpreted-text
role="ref"}

Defines all output ports using a
`String<class_String>`{.interpreted-text role="ref"} formatted as a
colon-separated list: `id,type,name;` (see
`add_output_port()<class_VisualShaderNodeGroupBase_method_add_output_port>`{.interpreted-text
role="ref"}).
