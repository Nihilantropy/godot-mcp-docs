github_url
:   hide

# VisualShaderNodeVaryingSetter {#class_VisualShaderNodeVaryingSetter}

**Inherits:**
`VisualShaderNodeVarying<class_VisualShaderNodeVarying>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node that sets a value of a varying.

::: rst-class
classref-introduction-group
:::

## Description

Inputs a value to a varying defined in the shader. You need to first
create a varying that can be used in the given function, e.g. varying
setter in Fragment shader requires a varying with mode set to
`VisualShader.VARYING_MODE_FRAG_TO_LIGHT<class_VisualShader_constant_VARYING_MODE_FRAG_TO_LIGHT>`{.interpreted-text
role="ref"}.
