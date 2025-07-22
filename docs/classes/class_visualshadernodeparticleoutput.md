github_url
:   hide

# VisualShaderNodeParticleOutput {#class_VisualShaderNodeParticleOutput}

**Inherits:**
`VisualShaderNodeOutput<class_VisualShaderNodeOutput>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Visual shader node that defines output values for particle emitting.

::: rst-class
classref-introduction-group
:::

## Description

This node defines how particles are emitted. It allows to customize e.g.
position and velocity. Available ports are different depending on which
function this node is inside (start, process, collision) and whether
custom data is enabled.
