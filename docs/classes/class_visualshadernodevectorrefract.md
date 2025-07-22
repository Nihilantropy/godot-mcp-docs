github_url
:   hide

# VisualShaderNodeVectorRefract {#class_VisualShaderNodeVectorRefract}

**Inherits:**
`VisualShaderNodeVectorBase<class_VisualShaderNodeVectorBase>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Returns the vector that points in the direction of refraction. For use
within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Translated to `refract(I, N, eta)` in the shader language, where `I` is
the incident vector, `N` is the normal vector and `eta` is the ratio of
the indices of the refraction.
