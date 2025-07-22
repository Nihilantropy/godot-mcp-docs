github_url
:   hide

# ConeTwistJoint3D {#class_ConeTwistJoint3D}

**Inherits:** `Joint3D<class_Joint3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A physics joint that connects two 3D physics bodies in a way that
simulates a ball-and-socket joint.

::: rst-class
classref-introduction-group
:::

## Description

A physics joint that connects two 3D physics bodies in a way that
simulates a ball-and-socket joint. The twist axis is initiated as the X
axis of the **ConeTwistJoint3D**. Once the physics bodies swing, the
twist axis is calculated as the middle of the X axes of the joint in the
local space of the two physics bodies. Useful for limbs like shoulders
and hips, lamps hanging off a ceiling, etc.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_ConeTwistJoint3D_Param}
::: rst-class
classref-enumeration
:::
::::

enum **Param**: `🔗<enum_ConeTwistJoint3D_Param>`{.interpreted-text
role="ref"}

:::: {#class_ConeTwistJoint3D_constant_PARAM_SWING_SPAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_SWING_SPAN** = `0`

Swing is rotation from side to side, around the axis perpendicular to
the twist axis.

The swing span defines, how much rotation will not get corrected along
the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.

:::: {#class_ConeTwistJoint3D_constant_PARAM_TWIST_SPAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_TWIST_SPAN** = `1`

Twist is the rotation around the twist axis, this value defined how far
the joint can twist.

Twist is locked if below 0.05.

:::: {#class_ConeTwistJoint3D_constant_PARAM_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_BIAS** = `2`

The speed with which the swing or twist will take place.

The higher, the faster.

:::: {#class_ConeTwistJoint3D_constant_PARAM_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_SOFTNESS** = `3`

The ease with which the joint starts to twist. If it\'s too low, it
takes more force to start twisting the joint.

:::: {#class_ConeTwistJoint3D_constant_PARAM_RELAXATION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_RELAXATION** = `4`

Defines, how fast the swing- and twist-speed-difference on both sides
gets synced.

:::: {#class_ConeTwistJoint3D_constant_PARAM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_MAX** = `5`

Represents the size of the
`Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ConeTwistJoint3D_property_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bias** = `0.3`
`🔗<class_ConeTwistJoint3D_property_bias>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The speed with which the swing or twist will take place.

The higher, the faster.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConeTwistJoint3D_property_relaxation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **relaxation** =
`1.0` `🔗<class_ConeTwistJoint3D_property_relaxation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Defines, how fast the swing- and twist-speed-difference on both sides
gets synced.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConeTwistJoint3D_property_softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **softness** = `0.8`
`🔗<class_ConeTwistJoint3D_property_softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The ease with which the joint starts to twist. If it\'s too low, it
takes more force to start twisting the joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConeTwistJoint3D_property_swing_span}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **swing_span** =
`0.7853982`
`🔗<class_ConeTwistJoint3D_property_swing_span>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Swing is rotation from side to side, around the axis perpendicular to
the twist axis.

The swing span defines, how much rotation will not get corrected along
the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConeTwistJoint3D_property_twist_span}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **twist_span** =
`3.1415927`
`🔗<class_ConeTwistJoint3D_property_twist_span>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Twist is the rotation around the twist axis, this value defined how far
the joint can twist.

Twist is locked if below 0.05.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ConeTwistJoint3D_method_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_param**(param:
`Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConeTwistJoint3D_method_get_param>`{.interpreted-text
role="ref"}

Returns the value of the specified parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConeTwistJoint3D_method_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param**(param:
`Param<enum_ConeTwistJoint3D_Param>`{.interpreted-text role="ref"},
value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_ConeTwistJoint3D_method_set_param>`{.interpreted-text
role="ref"}

Sets the value of the specified parameter.
