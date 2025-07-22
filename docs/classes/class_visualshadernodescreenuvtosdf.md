github_url
:   hide

# VisualShaderNodeScreenUVToSDF {#class_VisualShaderNodeScreenUVToSDF}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A function to convert screen UV to an SDF (signed-distance field), to be
used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Translates to `screen_uv_to_sdf(uv)` in the shader language. If the UV
port isn\'t connected, `SCREEN_UV` is used instead.
