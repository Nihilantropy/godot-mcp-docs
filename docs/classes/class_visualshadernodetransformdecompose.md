github_url
:   hide

# VisualShaderNodeTransformDecompose {#class_VisualShaderNodeTransformDecompose}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Decomposes a `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} into four `Vector3<class_Vector3>`{.interpreted-text
role="ref"}s within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Takes a 4×4 transform matrix and decomposes it into four `vec3` values,
one from each row of the matrix.
