github_url
:   hide

# VisualShaderNodeVaryingGetter {#class_VisualShaderNodeVaryingGetter}

**Inherits:**
`VisualShaderNodeVarying<class_VisualShaderNodeVarying>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node that gets a value of a varying.

::: rst-class
classref-introduction-group
:::

## Description

Outputs a value of a varying defined in the shader. You need to first
create a varying that can be used in the given function, e.g. varying
getter in Fragment shader requires a varying with mode set to
`VisualShader.VARYING_MODE_VERTEX_TO_FRAG_LIGHT<class_VisualShader_constant_VARYING_MODE_VERTEX_TO_FRAG_LIGHT>`{.interpreted-text
role="ref"}.
