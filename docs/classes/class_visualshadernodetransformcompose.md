github_url
:   hide

# VisualShaderNodeTransformCompose {#class_VisualShaderNodeTransformCompose}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Composes a `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} from four `Vector3<class_Vector3>`{.interpreted-text
role="ref"}s within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Creates a 4×4 transform matrix using four vectors of type `vec3`. Each
vector is one row in the matrix and the last column is a
`vec4(0, 0, 0, 1)`.
