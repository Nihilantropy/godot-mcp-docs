github_url
:   hide

# VisualShaderNodeIf {#class_VisualShaderNodeIf}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Outputs a 3D vector based on the result of a floating-point comparison
within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

This visual shader node has six input ports:

- Port **1** and **2** provide the two floating-point numbers `a` and
  `b` that will be compared.
- Port **3** is the tolerance, which allows similar floating-point
  numbers to be considered equal.
- Ports **4**, **5**, and **6** are the possible outputs, returned if
  `a == b`, `a > b`, or `a < b` respectively.
