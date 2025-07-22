github_url
:   hide

# VisualShaderNodeRandomRange {#class_VisualShaderNodeRandomRange}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node that generates a pseudo-random scalar.

::: rst-class
classref-introduction-group
:::

## Description

Random range node will output a pseudo-random scalar value in the
specified range, based on the seed. The value is always the same for the
given seed and range, so you should provide a changing input, e.g. by
using time.
