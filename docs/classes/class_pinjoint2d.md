github_url
:   hide

# PinJoint2D {#class_PinJoint2D}

**Inherits:** `Joint2D<class_Joint2D>`{.interpreted-text role="ref"}
**\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A physics joint that attaches two 2D physics bodies at a single point,
allowing them to freely rotate.

::: rst-class
classref-introduction-group
:::

## Description

A physics joint that attaches two 2D physics bodies at a single point,
allowing them to freely rotate. For example, a
`RigidBody2D<class_RigidBody2D>`{.interpreted-text role="ref"} can be
attached to a `StaticBody2D<class_StaticBody2D>`{.interpreted-text
role="ref"} to create a pendulum or a seesaw.

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

:::: {#class_PinJoint2D_property_angular_limit_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_limit_enabled** = `false`
`🔗<class_PinJoint2D_property_angular_limit_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_limit_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_angular_limit_enabled**()

If `true`, the pin maximum and minimum rotation, defined by
`angular_limit_lower<class_PinJoint2D_property_angular_limit_lower>`{.interpreted-text
role="ref"} and
`angular_limit_upper<class_PinJoint2D_property_angular_limit_upper>`{.interpreted-text
role="ref"} are applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PinJoint2D_property_angular_limit_lower}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_lower** = `0.0`
`🔗<class_PinJoint2D_property_angular_limit_lower>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_limit_lower**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_angular_limit_lower**()

The minimum rotation. Only active if
`angular_limit_enabled<class_PinJoint2D_property_angular_limit_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PinJoint2D_property_angular_limit_upper}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_upper** = `0.0`
`🔗<class_PinJoint2D_property_angular_limit_upper>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_limit_upper**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_angular_limit_upper**()

The maximum rotation. Only active if
`angular_limit_enabled<class_PinJoint2D_property_angular_limit_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PinJoint2D_property_motor_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **motor_enabled** =
`false` `🔗<class_PinJoint2D_property_motor_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_motor_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_motor_enabled**()

When activated, a motor turns the pin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PinJoint2D_property_motor_target_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**motor_target_velocity** = `0.0`
`🔗<class_PinJoint2D_property_motor_target_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_motor_target_velocity**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_motor_target_velocity**()

Target speed for the motor. In radians per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PinJoint2D_property_softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **softness** = `0.0`
`🔗<class_PinJoint2D_property_softness>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_softness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_softness**()

The higher this value, the more the bond to the pinned partner can flex.
