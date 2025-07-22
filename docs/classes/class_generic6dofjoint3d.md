github_url
:   hide

# Generic6DOFJoint3D {#class_Generic6DOFJoint3D}

**Inherits:** `Joint3D<class_Joint3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A physics joint that allows for complex movement and rotation between
two 3D physics bodies.

::: rst-class
classref-introduction-group
:::

## Description

The **Generic6DOFJoint3D** (6 Degrees Of Freedom) joint allows for
implementing custom types of joints by locking the rotation and
translation of certain axes.

The first 3 DOF represent the linear motion of the physics bodies and
the last 3 DOF represent the angular motion of the physics bodies. Each
axis can be either locked, or limited.

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

:::: {#enum_Generic6DOFJoint3D_Param}
::: rst-class
classref-enumeration
:::
::::

enum **Param**: `🔗<enum_Generic6DOFJoint3D_Param>`{.interpreted-text
role="ref"}

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_LOWER_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_LOWER_LIMIT** = `0`

The minimum difference between the pivot points\' axes.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_UPPER_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_UPPER_LIMIT** = `1`

The maximum difference between the pivot points\' axes.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_LIMIT_SOFTNESS** = `2`

A factor applied to the movement across the axes. The lower, the slower
the movement.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_RESTITUTION** = `3`

The amount of restitution on the axes\' movement. The lower, the more
momentum gets lost.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_DAMPING** = `4`

The amount of damping that happens at the linear motion across the axes.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_MOTOR_TARGET_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_MOTOR_TARGET_VELOCITY** = `5`

The velocity the linear motor will try to reach.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_MOTOR_FORCE_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_MOTOR_FORCE_LIMIT** = `6`

The maximum force the linear motor will apply while trying to reach the
velocity target.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_SPRING_STIFFNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_SPRING_STIFFNESS** = `7`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_SPRING_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_SPRING_DAMPING** = `8`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_Generic6DOFJoint3D_constant_PARAM_LINEAR_SPRING_EQUILIBRIUM_POINT}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_SPRING_EQUILIBRIUM_POINT** = `9`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_LOWER_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_LOWER_LIMIT** = `10`

The minimum rotation in negative direction to break loose and rotate
around the axes.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_UPPER_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_UPPER_LIMIT** = `11`

The minimum rotation in positive direction to break loose and rotate
around the axes.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_LIMIT_SOFTNESS** = `12`

The speed of all rotations across the axes.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_DAMPING** = `13`

The amount of rotational damping across the axes. The lower, the more
damping occurs.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_RESTITUTION** = `14`

The amount of rotational restitution across the axes. The lower, the
more restitution occurs.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_FORCE_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_FORCE_LIMIT** = `15`

The maximum amount of force that can occur, when rotating around the
axes.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_ERP}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_ERP** = `16`

When rotating across the axes, this error tolerance factor defines how
much the correction gets slowed down. The lower, the slower.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_MOTOR_TARGET_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_MOTOR_TARGET_VELOCITY** = `17`

Target speed for the motor at the axes.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_MOTOR_FORCE_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_MOTOR_FORCE_LIMIT** = `18`

Maximum acceleration for the motor at the axes.

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_SPRING_STIFFNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_SPRING_STIFFNESS** = `19`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_SPRING_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_SPRING_DAMPING** = `20`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_Generic6DOFJoint3D_constant_PARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT** = `21`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_Generic6DOFJoint3D_constant_PARAM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_MAX** = `22`

Represents the size of the
`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Generic6DOFJoint3D_Flag}
::: rst-class
classref-enumeration
:::
::::

enum **Flag**: `🔗<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text
role="ref"}

:::: {#class_Generic6DOFJoint3D_constant_FLAG_ENABLE_LINEAR_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_ENABLE_LINEAR_LIMIT** = `0`

If enabled, linear motion is possible within the given limits.

:::: {#class_Generic6DOFJoint3D_constant_FLAG_ENABLE_ANGULAR_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_ENABLE_ANGULAR_LIMIT** = `1`

If enabled, rotational motion is possible within the given limits.

:::: {#class_Generic6DOFJoint3D_constant_FLAG_ENABLE_LINEAR_SPRING}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_ENABLE_LINEAR_SPRING** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_Generic6DOFJoint3D_constant_FLAG_ENABLE_ANGULAR_SPRING}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_ENABLE_ANGULAR_SPRING** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_Generic6DOFJoint3D_constant_FLAG_ENABLE_MOTOR}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_ENABLE_MOTOR** = `4`

If enabled, there is a rotational motor across these axes.

:::: {#class_Generic6DOFJoint3D_constant_FLAG_ENABLE_LINEAR_MOTOR}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_ENABLE_LINEAR_MOTOR** = `5`

If enabled, there is a linear motor across these axes.

:::: {#class_Generic6DOFJoint3D_constant_FLAG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"}
**FLAG_MAX** = `6`

Represents the size of the
`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Generic6DOFJoint3D_property_angular_limit_x/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_x/damping** = `1.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_x/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of rotational damping across the X axis.

The lower, the longer an impulse from one side takes to travel to the
other side.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_x/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_limit_x/enabled** = `true`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_x/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, rotation across the X axis is limited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_x/erp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_x/erp** = `0.5`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_x/erp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

When rotating across the X axis, this error tolerance factor defines how
much the correction gets slowed down. The lower, the slower.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_x/force_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_x/force_limit** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_x/force_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum amount of force that can occur, when rotating around the X
axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_x/lower_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_x/lower_angle** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_x/lower_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum rotation in negative direction to break loose and rotate
around the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_x/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_x/restitution** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_x/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of rotational restitution across the X axis. The lower, the
more restitution occurs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_x/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_x/softness** = `0.5`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_x/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The speed of all rotations across the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_x/upper_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_x/upper_angle** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_x/upper_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum rotation in positive direction to break loose and rotate
around the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_y/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_y/damping** = `1.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_y/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of rotational damping across the Y axis. The lower, the more
damping occurs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_y/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_limit_y/enabled** = `true`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_y/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, rotation across the Y axis is limited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_y/erp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_y/erp** = `0.5`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_y/erp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

When rotating across the Y axis, this error tolerance factor defines how
much the correction gets slowed down. The lower, the slower.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_y/force_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_y/force_limit** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_y/force_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum amount of force that can occur, when rotating around the Y
axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_y/lower_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_y/lower_angle** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_y/lower_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum rotation in negative direction to break loose and rotate
around the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_y/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_y/restitution** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_y/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of rotational restitution across the Y axis. The lower, the
more restitution occurs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_y/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_y/softness** = `0.5`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_y/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The speed of all rotations across the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_y/upper_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_y/upper_angle** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_y/upper_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum rotation in positive direction to break loose and rotate
around the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_z/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_z/damping** = `1.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_z/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of rotational damping across the Z axis. The lower, the more
damping occurs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_z/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_limit_z/enabled** = `true`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_z/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, rotation across the Z axis is limited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_z/erp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_z/erp** = `0.5`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_z/erp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

When rotating across the Z axis, this error tolerance factor defines how
much the correction gets slowed down. The lower, the slower.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_z/force_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_z/force_limit** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_z/force_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum amount of force that can occur, when rotating around the Z
axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_z/lower_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_z/lower_angle** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_z/lower_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum rotation in negative direction to break loose and rotate
around the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_z/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_z/restitution** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_z/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of rotational restitution across the Z axis. The lower, the
more restitution occurs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_z/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_z/softness** = `0.5`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_z/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The speed of all rotations across the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_limit_z/upper_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit_z/upper_angle** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_limit_z/upper_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum rotation in positive direction to break loose and rotate
around the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_motor_x/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_motor_x/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_angular_motor_x/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, a rotating motor at the X axis is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_motor_x/force_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_motor_x/force_limit** = `300.0`
`🔗<class_Generic6DOFJoint3D_property_angular_motor_x/force_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum acceleration for the motor at the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_motor_x/target_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_motor_x/target_velocity** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_motor_x/target_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Target speed for the motor at the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_motor_y/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_motor_y/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_angular_motor_y/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, a rotating motor at the Y axis is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_motor_y/force_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_motor_y/force_limit** = `300.0`
`🔗<class_Generic6DOFJoint3D_property_angular_motor_y/force_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum acceleration for the motor at the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_motor_y/target_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_motor_y/target_velocity** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_motor_y/target_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Target speed for the motor at the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_motor_z/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_motor_z/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_angular_motor_z/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, a rotating motor at the Z axis is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_motor_z/force_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_motor_z/force_limit** = `300.0`
`🔗<class_Generic6DOFJoint3D_property_angular_motor_z/force_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum acceleration for the motor at the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_motor_z/target_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_motor_z/target_velocity** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_motor_z/target_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Target speed for the motor at the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_x/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_spring_x/damping** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_x/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_x/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_spring_x/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_x/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_x/equilibrium_point}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_spring_x/equilibrium_point** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_x/equilibrium_point>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_x/stiffness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_spring_x/stiffness** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_x/stiffness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_y/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_spring_y/damping** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_y/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_y/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_spring_y/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_y/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_y/equilibrium_point}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_spring_y/equilibrium_point** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_y/equilibrium_point>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_y/stiffness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_spring_y/stiffness** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_y/stiffness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_z/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_spring_z/damping** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_z/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_z/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**angular_spring_z/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_z/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_z/equilibrium_point}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_spring_z/equilibrium_point** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_z/equilibrium_point>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_angular_spring_z/stiffness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_spring_z/stiffness** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_angular_spring_z/stiffness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_x/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_x/damping** = `1.0`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_x/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of damping that happens at the X motion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_x/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**linear_limit_x/enabled** = `true`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_x/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the linear motion across the X axis is limited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_x/lower_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_x/lower_distance** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_x/lower_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum difference between the pivot points\' X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_x/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_x/restitution** = `0.5`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_x/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of restitution on the X axis movement. The lower, the more
momentum gets lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_x/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_x/softness** = `0.7`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_x/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A factor applied to the movement across the X axis. The lower, the
slower the movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_x/upper_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_x/upper_distance** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_x/upper_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum difference between the pivot points\' X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_y/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_y/damping** = `1.0`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_y/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of damping that happens at the Y motion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_y/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**linear_limit_y/enabled** = `true`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_y/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the linear motion across the Y axis is limited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_y/lower_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_y/lower_distance** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_y/lower_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum difference between the pivot points\' Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_y/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_y/restitution** = `0.5`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_y/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of restitution on the Y axis movement. The lower, the more
momentum gets lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_y/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_y/softness** = `0.7`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_y/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A factor applied to the movement across the Y axis. The lower, the
slower the movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_y/upper_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_y/upper_distance** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_y/upper_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum difference between the pivot points\' Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_z/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_z/damping** = `1.0`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_z/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of damping that happens at the Z motion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_z/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**linear_limit_z/enabled** = `true`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_z/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the linear motion across the Z axis is limited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_z/lower_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_z/lower_distance** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_z/lower_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum difference between the pivot points\' Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_z/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_z/restitution** = `0.5`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_z/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of restitution on the Z axis movement. The lower, the more
momentum gets lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_z/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_z/softness** = `0.7`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_z/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A factor applied to the movement across the Z axis. The lower, the
slower the movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_limit_z/upper_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit_z/upper_distance** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_limit_z/upper_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum difference between the pivot points\' Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_motor_x/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**linear_motor_x/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_linear_motor_x/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, then there is a linear motor on the X axis. It will attempt
to reach the target velocity while staying within the force limits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_motor_x/force_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_motor_x/force_limit** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_motor_x/force_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum force the linear motor can apply on the X axis while trying
to reach the target velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_motor_x/target_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_motor_x/target_velocity** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_motor_x/target_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The speed that the linear motor will attempt to reach on the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_motor_y/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**linear_motor_y/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_linear_motor_y/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, then there is a linear motor on the Y axis. It will attempt
to reach the target velocity while staying within the force limits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_motor_y/force_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_motor_y/force_limit** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_motor_y/force_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum force the linear motor can apply on the Y axis while trying
to reach the target velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_motor_y/target_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_motor_y/target_velocity** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_motor_y/target_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The speed that the linear motor will attempt to reach on the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_motor_z/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**linear_motor_z/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_linear_motor_z/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, then there is a linear motor on the Z axis. It will attempt
to reach the target velocity while staying within the force limits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_motor_z/force_limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_motor_z/force_limit** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_motor_z/force_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum force the linear motor can apply on the Z axis while trying
to reach the target velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_motor_z/target_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_motor_z/target_velocity** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_motor_z/target_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The speed that the linear motor will attempt to reach on the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_x/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_spring_x/damping** = `0.01`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_x/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_x/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**linear_spring_x/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_x/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_x**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_x/equilibrium_point}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_spring_x/equilibrium_point** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_x/equilibrium_point>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_x/stiffness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_spring_x/stiffness** = `0.01`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_x/stiffness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_x**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_y/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_spring_y/damping** = `0.01`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_y/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_y/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**linear_spring_y/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_y/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_y**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_y/equilibrium_point}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_spring_y/equilibrium_point** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_y/equilibrium_point>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_y/stiffness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_spring_y/stiffness** = `0.01`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_y/stiffness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_y**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_z/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_spring_z/damping** = `0.01`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_z/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_z/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**linear_spring_z/enabled** = `false`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_z/enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
  value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag_z**(flag:
  `Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_z/equilibrium_point}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_spring_z/equilibrium_point** = `0.0`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_z/equilibrium_point>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_property_linear_spring_z/stiffness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_spring_z/stiffness** = `0.01`
`🔗<class_Generic6DOFJoint3D_property_linear_spring_z/stiffness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_z**(param:
  `Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Generic6DOFJoint3D_method_get_flag_x}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_flag_x**(flag:
`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Generic6DOFJoint3D_method_get_flag_x>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_get_flag_y}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_flag_y**(flag:
`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Generic6DOFJoint3D_method_get_flag_y>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_get_flag_z}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_flag_z**(flag:
`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Generic6DOFJoint3D_method_get_flag_z>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_get_param_x}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_param_x**(param:
`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Generic6DOFJoint3D_method_get_param_x>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_get_param_y}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_param_y**(param:
`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Generic6DOFJoint3D_method_get_param_y>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_get_param_z}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_param_z**(param:
`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Generic6DOFJoint3D_method_get_param_z>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_set_flag_x}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_flag_x**(flag:
`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
value: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Generic6DOFJoint3D_method_set_flag_x>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_set_flag_y}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_flag_y**(flag:
`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
value: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Generic6DOFJoint3D_method_set_flag_y>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_set_flag_z}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_flag_z**(flag:
`Flag<enum_Generic6DOFJoint3D_Flag>`{.interpreted-text role="ref"},
value: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Generic6DOFJoint3D_method_set_flag_z>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_set_param_x}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param_x**(param:
`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Generic6DOFJoint3D_method_set_param_x>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_set_param_y}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param_y**(param:
`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Generic6DOFJoint3D_method_set_param_y>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Generic6DOFJoint3D_method_set_param_z}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param_z**(param:
`Param<enum_Generic6DOFJoint3D_Param>`{.interpreted-text role="ref"},
value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Generic6DOFJoint3D_method_set_param_z>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
