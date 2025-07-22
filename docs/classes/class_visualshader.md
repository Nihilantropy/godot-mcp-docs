github_url
:   hide

# VisualShader {#class_VisualShader}

**Inherits:** `Shader<class_Shader>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A custom shader program with a visual editor.

::: rst-class
classref-introduction-group
:::

## Description

This class provides a graph-like visual editor for creating a
`Shader<class_Shader>`{.interpreted-text role="ref"}. Although
**VisualShader**s do not require coding, they share the same logic with
script shaders. They use
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text
role="ref"}s that can be connected to each other to control the flow of
the shader. The visual shader graph is converted to a script shader
behind the scenes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using VisualShaders <../tutorials/shaders/visual_shaders>`{.interpreted-text
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

## Enumerations

:::: {#enum_VisualShader_Type}
::: rst-class
classref-enumeration
:::
::::

enum **Type**: `🔗<enum_VisualShader_Type>`{.interpreted-text
role="ref"}

:::: {#class_VisualShader_constant_TYPE_VERTEX}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_VERTEX** = `0`

A vertex shader, operating on vertices.

:::: {#class_VisualShader_constant_TYPE_FRAGMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_FRAGMENT** = `1`

A fragment shader, operating on fragments (pixels).

:::: {#class_VisualShader_constant_TYPE_LIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_LIGHT** = `2`

A shader for light calculations.

:::: {#class_VisualShader_constant_TYPE_START}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_START** = `3`

A function for the \"start\" stage of particle shader.

:::: {#class_VisualShader_constant_TYPE_PROCESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_PROCESS** = `4`

A function for the \"process\" stage of particle shader.

:::: {#class_VisualShader_constant_TYPE_COLLIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_COLLIDE** = `5`

A function for the \"collide\" stage (particle collision handler) of
particle shader.

:::: {#class_VisualShader_constant_TYPE_START_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_START_CUSTOM** = `6`

A function for the \"start\" stage of particle shader, with customized
output.

:::: {#class_VisualShader_constant_TYPE_PROCESS_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_PROCESS_CUSTOM** = `7`

A function for the \"process\" stage of particle shader, with customized
output.

:::: {#class_VisualShader_constant_TYPE_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_SKY** = `8`

A shader for 3D environment\'s sky.

:::: {#class_VisualShader_constant_TYPE_FOG}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_FOG** = `9`

A compute shader that runs for each froxel of the volumetric fog map.

:::: {#class_VisualShader_constant_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}
**TYPE_MAX** = `10`

Represents the size of the
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShader_VaryingMode}
::: rst-class
classref-enumeration
:::
::::

enum **VaryingMode**:
`🔗<enum_VisualShader_VaryingMode>`{.interpreted-text role="ref"}

:::: {#class_VisualShader_constant_VARYING_MODE_VERTEX_TO_FRAG_LIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingMode<enum_VisualShader_VaryingMode>`{.interpreted-text
role="ref"} **VARYING_MODE_VERTEX_TO_FRAG_LIGHT** = `0`

Varying is passed from `Vertex` function to `Fragment` and `Light`
functions.

:::: {#class_VisualShader_constant_VARYING_MODE_FRAG_TO_LIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingMode<enum_VisualShader_VaryingMode>`{.interpreted-text
role="ref"} **VARYING_MODE_FRAG_TO_LIGHT** = `1`

Varying is passed from `Fragment` function to `Light` function.

:::: {#class_VisualShader_constant_VARYING_MODE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingMode<enum_VisualShader_VaryingMode>`{.interpreted-text
role="ref"} **VARYING_MODE_MAX** = `2`

Represents the size of the
`VaryingMode<enum_VisualShader_VaryingMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShader_VaryingType}
::: rst-class
classref-enumeration
:::
::::

enum **VaryingType**:
`🔗<enum_VisualShader_VaryingType>`{.interpreted-text role="ref"}

:::: {#class_VisualShader_constant_VARYING_TYPE_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **VARYING_TYPE_FLOAT** = `0`

Varying is of type `float<class_float>`{.interpreted-text role="ref"}.

:::: {#class_VisualShader_constant_VARYING_TYPE_INT}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **VARYING_TYPE_INT** = `1`

Varying is of type `int<class_int>`{.interpreted-text role="ref"}.

:::: {#class_VisualShader_constant_VARYING_TYPE_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **VARYING_TYPE_UINT** = `2`

Varying is of type unsigned `int<class_int>`{.interpreted-text
role="ref"}.

:::: {#class_VisualShader_constant_VARYING_TYPE_VECTOR_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **VARYING_TYPE_VECTOR_2D** = `3`

Varying is of type `Vector2<class_Vector2>`{.interpreted-text
role="ref"}.

:::: {#class_VisualShader_constant_VARYING_TYPE_VECTOR_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **VARYING_TYPE_VECTOR_3D** = `4`

Varying is of type `Vector3<class_Vector3>`{.interpreted-text
role="ref"}.

:::: {#class_VisualShader_constant_VARYING_TYPE_VECTOR_4D}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **VARYING_TYPE_VECTOR_4D** = `5`

Varying is of type `Vector4<class_Vector4>`{.interpreted-text
role="ref"}.

:::: {#class_VisualShader_constant_VARYING_TYPE_BOOLEAN}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **VARYING_TYPE_BOOLEAN** = `6`

Varying is of type `bool<class_bool>`{.interpreted-text role="ref"}.

:::: {#class_VisualShader_constant_VARYING_TYPE_TRANSFORM}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **VARYING_TYPE_TRANSFORM** = `7`

Varying is of type `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}.

:::: {#class_VisualShader_constant_VARYING_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} **VARYING_TYPE_MAX** = `8`

Represents the size of the
`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_VisualShader_constant_NODE_ID_INVALID}
::: rst-class
classref-constant
:::
::::

**NODE_ID_INVALID** = `-1`
`🔗<class_VisualShader_constant_NODE_ID_INVALID>`{.interpreted-text
role="ref"}

Indicates an invalid **VisualShader** node.

:::: {#class_VisualShader_constant_NODE_ID_OUTPUT}
::: rst-class
classref-constant
:::
::::

**NODE_ID_OUTPUT** = `0`
`🔗<class_VisualShader_constant_NODE_ID_OUTPUT>`{.interpreted-text
role="ref"}

Indicates an output node of **VisualShader**.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShader_property_graph_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **graph_offset**
`🔗<class_VisualShader_property_graph_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_graph_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_graph_offset**()

**Deprecated:** This property does nothing and always equals to zero.

Deprecated.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VisualShader_method_add_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_node**(type: `Type<enum_VisualShader_Type>`{.interpreted-text
role="ref"}, node:
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_VisualShader_method_add_node>`{.interpreted-text role="ref"}

Adds the specified `node` to the shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_add_varying}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_varying**(name: `String<class_String>`{.interpreted-text
role="ref"}, mode:
`VaryingMode<enum_VisualShader_VaryingMode>`{.interpreted-text
role="ref"}, type:
`VaryingType<enum_VisualShader_VaryingType>`{.interpreted-text
role="ref"})
`🔗<class_VisualShader_method_add_varying>`{.interpreted-text
role="ref"}

Adds a new varying value node to the shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_attach_node_to_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**attach_node_to_frame**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"}, frame:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_VisualShader_method_attach_node_to_frame>`{.interpreted-text
role="ref"}

Attaches the given node to the given frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_can_connect_nodes}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**can_connect_nodes**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}, from_node:
`int<class_int>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`int<class_int>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShader_method_can_connect_nodes>`{.interpreted-text
role="ref"}

Returns `true` if the specified nodes and ports can be connected
together.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_connect_nodes}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**connect_nodes**(type: `Type<enum_VisualShader_Type>`{.interpreted-text
role="ref"}, from_node: `int<class_int>`{.interpreted-text role="ref"},
from_port: `int<class_int>`{.interpreted-text role="ref"}, to_node:
`int<class_int>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_VisualShader_method_connect_nodes>`{.interpreted-text
role="ref"}

Connects the specified nodes and ports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_connect_nodes_forced}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**connect_nodes_forced**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}, from_node:
`int<class_int>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`int<class_int>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_VisualShader_method_connect_nodes_forced>`{.interpreted-text
role="ref"}

Connects the specified nodes and ports, even if they can\'t be
connected. Such connection is invalid and will not function properly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_detach_node_from_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**detach_node_from_frame**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_VisualShader_method_detach_node_from_frame>`{.interpreted-text
role="ref"}

Detaches the given node from the frame it is attached to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_disconnect_nodes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect_nodes**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}, from_node:
`int<class_int>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`int<class_int>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_VisualShader_method_disconnect_nodes>`{.interpreted-text
role="ref"}

Connects the specified nodes and ports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_get_node}
::: rst-class
classref-method
:::
::::

`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**get_node**(type: `Type<enum_VisualShader_Type>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_VisualShader_method_get_node>`{.interpreted-text
role="ref"}

Returns the shader node instance with specified `type` and `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_get_node_connections}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_node_connections**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShader_method_get_node_connections>`{.interpreted-text
role="ref"}

Returns the list of connected nodes with the specified type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_get_node_list}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_node_list**(type: `Type<enum_VisualShader_Type>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShader_method_get_node_list>`{.interpreted-text
role="ref"}

Returns the list of all nodes in the shader with the specified type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_get_node_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_node_position**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShader_method_get_node_position>`{.interpreted-text
role="ref"}

Returns the position of the specified node within the shader graph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_get_valid_node_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_valid_node_id**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShader_method_get_valid_node_id>`{.interpreted-text
role="ref"}

Returns next valid node ID that can be added to the shader graph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_has_varying}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_varying**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShader_method_has_varying>`{.interpreted-text
role="ref"}

Returns `true` if the shader has a varying with the given `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_is_node_connection}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_node_connection**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}, from_node:
`int<class_int>`{.interpreted-text role="ref"}, from_port:
`int<class_int>`{.interpreted-text role="ref"}, to_node:
`int<class_int>`{.interpreted-text role="ref"}, to_port:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualShader_method_is_node_connection>`{.interpreted-text
role="ref"}

Returns `true` if the specified node and port connection exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_remove_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_node**(type: `Type<enum_VisualShader_Type>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_VisualShader_method_remove_node>`{.interpreted-text
role="ref"}

Removes the specified node from the shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_remove_varying}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_varying**(name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_VisualShader_method_remove_varying>`{.interpreted-text
role="ref"}

Removes a varying value node with the given `name`. Prints an error if a
node with this name is not found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_replace_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**replace_node**(type: `Type<enum_VisualShader_Type>`{.interpreted-text
role="ref"}, id: `int<class_int>`{.interpreted-text role="ref"},
new_class: `StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_VisualShader_method_replace_node>`{.interpreted-text
role="ref"}

Replaces the specified node with a node of new class type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_set_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_mode**(mode: `Mode<enum_Shader_Mode>`{.interpreted-text
role="ref"}) `🔗<class_VisualShader_method_set_mode>`{.interpreted-text
role="ref"}

Sets the mode of this shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShader_method_set_node_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_node_position**(type:
`Type<enum_VisualShader_Type>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"}, position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_VisualShader_method_set_node_position>`{.interpreted-text
role="ref"}

Sets the position of the specified node.
