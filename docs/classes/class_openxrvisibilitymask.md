github_url
:   hide

# OpenXRVisibilityMask {#class_OpenXRVisibilityMask}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Draws a stereo correct visibility mask.

::: rst-class
classref-introduction-group
:::

## Description

The visibility mask allows us to black out the part of the render result
that is invisible due to lens distortion.

As this is rendered first, it prevents fragments with expensive lighting
calculations to be processed as they are discarded through z-checking.
