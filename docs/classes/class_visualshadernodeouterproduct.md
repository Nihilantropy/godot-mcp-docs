github_url
:   hide

# VisualShaderNodeOuterProduct {#class_VisualShaderNodeOuterProduct}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Calculates an outer product of two vectors within the visual shader
graph.

::: rst-class
classref-introduction-group
:::

## Description

`OuterProduct` treats the first parameter `c` as a column vector (matrix
with one column) and the second parameter `r` as a row vector (matrix
with one row) and does a linear algebraic matrix multiply `c * r`,
yielding a matrix whose number of rows is the number of components in
`c` and whose number of columns is the number of components in `r`.
