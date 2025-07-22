github_url
:   hide

# VisualShaderNodeVectorDecompose {#class_VisualShaderNodeVectorDecompose}

**Inherits:**
`VisualShaderNodeVectorBase<class_VisualShaderNodeVectorBase>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Decomposes a `Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"} or 4D vector
(represented as a `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"}) into scalars within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Takes a `vec2`, `vec3` or `vec4` and decomposes it into scalar values
that can be used as separate outputs.
