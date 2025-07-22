github_url
:   hide

# VisualShaderNodeWorldPositionFromDepth {#class_VisualShaderNodeWorldPositionFromDepth}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node that calculates the position of the pixel in world
space using the depth texture.

::: rst-class
classref-introduction-group
:::

## Description

The WorldPositionFromDepth node reconstructs the depth position of the
pixel in world space. This can be used to obtain world space UVs for
projection mapping like Caustics.
