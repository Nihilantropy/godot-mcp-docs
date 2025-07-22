github_url
:   hide

# DampedSpringJoint2D {#class_DampedSpringJoint2D}

**Inherits:** `Joint2D<class_Joint2D>`{.interpreted-text role="ref"}
**\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A physics joint that connects two 2D physics bodies with a spring-like
force.

::: rst-class
classref-introduction-group
:::

## Description

A physics joint that connects two 2D physics bodies with a spring-like
force. This behaves like a spring that always wants to stretch to a
given length.

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

:::: {#class_DampedSpringJoint2D_property_damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **damping** = `1.0`
`🔗<class_DampedSpringJoint2D_property_damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_damping**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_damping**()

The spring joint\'s damping ratio. A value between `0` and `1`. When the
two bodies move into different directions the system tries to align them
to the spring axis again. A high
`damping<class_DampedSpringJoint2D_property_damping>`{.interpreted-text
role="ref"} value forces the attached bodies to align faster.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DampedSpringJoint2D_property_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length** = `50.0`
`🔗<class_DampedSpringJoint2D_property_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_length**()

The spring joint\'s maximum length. The two attached bodies cannot
stretch it past this value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DampedSpringJoint2D_property_rest_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **rest_length** =
`0.0`
`🔗<class_DampedSpringJoint2D_property_rest_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rest_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_rest_length**()

When the bodies attached to the spring joint move they stretch or squash
it. The joint always tries to resize towards this length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DampedSpringJoint2D_property_stiffness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **stiffness** =
`20.0`
`🔗<class_DampedSpringJoint2D_property_stiffness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stiffness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_stiffness**()

The higher the value, the less the bodies attached to the joint will
deform it. The joint applies an opposing force to the bodies, the
product of the stiffness multiplied by the size difference from its
resting length.
