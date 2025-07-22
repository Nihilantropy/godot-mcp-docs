github_url
:   hide

# GrooveJoint2D {#class_GrooveJoint2D}

**Inherits:** `Joint2D<class_Joint2D>`{.interpreted-text role="ref"}
**\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A physics joint that restricts the movement of two 2D physics bodies to
a fixed axis.

::: rst-class
classref-introduction-group
:::

## Description

A physics joint that restricts the movement of two 2D physics bodies to
a fixed axis. For example, a
`StaticBody2D<class_StaticBody2D>`{.interpreted-text role="ref"}
representing a piston base can be attached to a
`RigidBody2D<class_RigidBody2D>`{.interpreted-text role="ref"}
representing the piston head, moving up and down.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GrooveJoint2D_property_initial_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **initial_offset** =
`25.0`
`🔗<class_GrooveJoint2D_property_initial_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_initial_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_initial_offset**()

The body B\'s initial anchor position defined by the joint\'s origin and
a local offset
`initial_offset<class_GrooveJoint2D_property_initial_offset>`{.interpreted-text
role="ref"} along the joint\'s Y axis (along the groove).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GrooveJoint2D_property_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length** = `50.0`
`🔗<class_GrooveJoint2D_property_length>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_length**()

The groove\'s length. The groove is from the joint\'s origin towards
`length<class_GrooveJoint2D_property_length>`{.interpreted-text
role="ref"} along the joint\'s local Y axis.
