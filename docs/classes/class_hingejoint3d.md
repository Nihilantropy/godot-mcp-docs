github_url
:   hide

# HingeJoint3D {#class_HingeJoint3D}

**Inherits:** `Joint3D<class_Joint3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A physics joint that restricts the rotation of a 3D physics body around
an axis relative to another physics body.

::: rst-class
classref-introduction-group
:::

## Description

A physics joint that restricts the rotation of a 3D physics body around
an axis relative to another physics body. For example, Body A can be a
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"}
representing a door hinge that a
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} rotates
around.

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

:::: {#enum_HingeJoint3D_Param}
::: rst-class
classref-enumeration
:::
::::

enum **Param**: `🔗<enum_HingeJoint3D_Param>`{.interpreted-text
role="ref"}

:::: {#class_HingeJoint3D_constant_PARAM_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_BIAS** = `0`

The speed with which the two bodies get pulled together when they move
in different directions.

:::: {#class_HingeJoint3D_constant_PARAM_LIMIT_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LIMIT_UPPER** = `1`

The maximum rotation. Only active if
`angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>`{.interpreted-text
role="ref"} is `true`.

:::: {#class_HingeJoint3D_constant_PARAM_LIMIT_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LIMIT_LOWER** = `2`

The minimum rotation. Only active if
`angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>`{.interpreted-text
role="ref"} is `true`.

:::: {#class_HingeJoint3D_constant_PARAM_LIMIT_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LIMIT_BIAS** = `3`

The speed with which the rotation across the axis perpendicular to the
hinge gets corrected.

:::: {#class_HingeJoint3D_constant_PARAM_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LIMIT_SOFTNESS** = `4`

**Deprecated:** This property is never used by the engine and is kept
for compatibility purpose.

:::: {#class_HingeJoint3D_constant_PARAM_LIMIT_RELAXATION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LIMIT_RELAXATION** = `5`

The lower this value, the more the rotation gets slowed down.

:::: {#class_HingeJoint3D_constant_PARAM_MOTOR_TARGET_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_MOTOR_TARGET_VELOCITY** = `6`

Target speed for the motor.

:::: {#class_HingeJoint3D_constant_PARAM_MOTOR_MAX_IMPULSE}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_MOTOR_MAX_IMPULSE** = `7`

Maximum acceleration for the motor.

:::: {#class_HingeJoint3D_constant_PARAM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_MAX** = `8`

Represents the size of the
`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_HingeJoint3D_Flag}
::: rst-class
classref-enumeration
:::
::::

enum **Flag**: `🔗<enum_HingeJoint3D_Flag>`{.interpreted-text
role="ref"}

:::: {#class_HingeJoint3D_constant_FLAG_USE_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_HingeJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_USE_LIMIT** = `0`

If `true`, the hinges maximum and minimum rotation, defined by
`angular_limit/lower<class_HingeJoint3D_property_angular_limit/lower>`{.interpreted-text
role="ref"} and
`angular_limit/upper<class_HingeJoint3D_property_angular_limit/upper>`{.interpreted-text
role="ref"} has effects.

:::: {#class_HingeJoint3D_constant_FLAG_ENABLE_MOTOR}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_HingeJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_ENABLE_MOTOR** = `1`

When activated, a motor turns the hinge.

:::: {#class_HingeJoint3D_constant_FLAG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_HingeJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_MAX** = `2`

Represents the size of the
`Flag<enum_HingeJoint3D_Flag>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_HingeJoint3D_property_angular_limit/bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/bias** = `0.3`
`🔗<class_HingeJoint3D_property_angular_limit/bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}, value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The speed with which the rotation across the axis perpendicular to the
hinge gets corrected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_property_angular_limit/enable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_limit/enable** = `false`
`🔗<class_HingeJoint3D_property_angular_limit/enable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flag<enum_HingeJoint3D_Flag>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flag<enum_HingeJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the hinges maximum and minimum rotation, defined by
`angular_limit/lower<class_HingeJoint3D_property_angular_limit/lower>`{.interpreted-text
role="ref"} and
`angular_limit/upper<class_HingeJoint3D_property_angular_limit/upper>`{.interpreted-text
role="ref"} has effects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_property_angular_limit/lower}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/lower** = `-1.5707964`
`🔗<class_HingeJoint3D_property_angular_limit/lower>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}, value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum rotation. Only active if
`angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_property_angular_limit/relaxation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/relaxation** = `1.0`
`🔗<class_HingeJoint3D_property_angular_limit/relaxation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}, value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The lower this value, the more the rotation gets slowed down.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_property_angular_limit/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/softness** = `0.9`
`🔗<class_HingeJoint3D_property_angular_limit/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}, value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

**Deprecated:** This property is never set by the engine and is kept for
compatibility purposes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_property_angular_limit/upper}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/upper** = `1.5707964`
`🔗<class_HingeJoint3D_property_angular_limit/upper>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}, value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum rotation. Only active if
`angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_property_motor/enable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **motor/enable** =
`false` `🔗<class_HingeJoint3D_property_motor/enable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flag<enum_HingeJoint3D_Flag>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flag<enum_HingeJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

When activated, a motor turns the hinge.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_property_motor/max_impulse}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **motor/max_impulse**
= `1.0`
`🔗<class_HingeJoint3D_property_motor/max_impulse>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}, value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum acceleration for the motor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_property_motor/target_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**motor/target_velocity** = `1.0`
`🔗<class_HingeJoint3D_property_motor/target_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}, value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Target speed for the motor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_property_params/bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **params/bias** =
`0.3` `🔗<class_HingeJoint3D_property_params/bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"}, value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The speed with which the two bodies get pulled together when they move
in different directions.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_HingeJoint3D_method_get_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
`Flag<enum_HingeJoint3D_Flag>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_HingeJoint3D_method_get_flag>`{.interpreted-text
role="ref"}

Returns the value of the specified flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_method_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_param**(param:
`Param<enum_HingeJoint3D_Param>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_HingeJoint3D_method_get_param>`{.interpreted-text
role="ref"}

Returns the value of the specified parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_method_set_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_flag**(flag: `Flag<enum_HingeJoint3D_Flag>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_HingeJoint3D_method_set_flag>`{.interpreted-text role="ref"}

If `true`, enables the specified flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HingeJoint3D_method_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param**(param: `Param<enum_HingeJoint3D_Param>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_HingeJoint3D_method_set_param>`{.interpreted-text role="ref"}

Sets the value of the specified parameter.
