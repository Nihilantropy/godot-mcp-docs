github_url
:   hide

# VisualShaderNodeReroute {#class_VisualShaderNodeReroute}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node that allows rerouting a connection within the visual shader
graph.

::: rst-class
classref-introduction-group
:::

## Description

Automatically adapts its port type to the type of the incoming
connection and ensures valid connections.

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

:::: {#class_VisualShaderNodeReroute_method_get_port_type}
::: rst-class
classref-method
:::
::::

`PortType<enum_VisualShaderNode_PortType>`{.interpreted-text role="ref"}
**get_port_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShaderNodeReroute_method_get_port_type>`{.interpreted-text
role="ref"}

Returns the port type of the reroute node.
