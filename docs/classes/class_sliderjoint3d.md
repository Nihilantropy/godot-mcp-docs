github_url
:   hide

# SliderJoint3D {#class_SliderJoint3D}

**Inherits:** `Joint3D<class_Joint3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A physics joint that restricts the movement of a 3D physics body along
an axis relative to another physics body.

::: rst-class
classref-introduction-group
:::

## Description

A physics joint that restricts the movement of a 3D physics body along
an axis relative to another physics body. For example, Body A could be a
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"}
representing a piston base, while Body B could be a
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"}
representing the piston head, moving up and down.

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

:::: {#enum_SliderJoint3D_Param}
::: rst-class
classref-enumeration
:::
::::

enum **Param**: `🔗<enum_SliderJoint3D_Param>`{.interpreted-text
role="ref"}

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_LIMIT_UPPER** = `0`

Constant for accessing
`linear_limit/upper_distance<class_SliderJoint3D_property_linear_limit/upper_distance>`{.interpreted-text
role="ref"}. The maximum difference between the pivot points on their X
axis before damping happens.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_LIMIT_LOWER** = `1`

Constant for accessing
`linear_limit/lower_distance<class_SliderJoint3D_property_linear_limit/lower_distance>`{.interpreted-text
role="ref"}. The minimum difference between the pivot points on their X
axis before damping happens.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_LIMIT_SOFTNESS** = `2`

Constant for accessing
`linear_limit/softness<class_SliderJoint3D_property_linear_limit/softness>`{.interpreted-text
role="ref"}. A factor applied to the movement across the slider axis
once the limits get surpassed. The lower, the slower the movement.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_LIMIT_RESTITUTION** = `3`

Constant for accessing
`linear_limit/restitution<class_SliderJoint3D_property_linear_limit/restitution>`{.interpreted-text
role="ref"}. The amount of restitution once the limits are surpassed.
The lower, the more velocity-energy gets lost.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_LIMIT_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_LIMIT_DAMPING** = `4`

Constant for accessing
`linear_limit/damping<class_SliderJoint3D_property_linear_limit/damping>`{.interpreted-text
role="ref"}. The amount of damping once the slider limits are surpassed.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_MOTION_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_MOTION_SOFTNESS** = `5`

Constant for accessing
`linear_motion/softness<class_SliderJoint3D_property_linear_motion/softness>`{.interpreted-text
role="ref"}. A factor applied to the movement across the slider axis as
long as the slider is in the limits. The lower, the slower the movement.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_MOTION_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_MOTION_RESTITUTION** = `6`

Constant for accessing
`linear_motion/restitution<class_SliderJoint3D_property_linear_motion/restitution>`{.interpreted-text
role="ref"}. The amount of restitution inside the slider limits.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_MOTION_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_MOTION_DAMPING** = `7`

Constant for accessing
`linear_motion/damping<class_SliderJoint3D_property_linear_motion/damping>`{.interpreted-text
role="ref"}. The amount of damping inside the slider limits.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_ORTHOGONAL_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_ORTHOGONAL_SOFTNESS** = `8`

Constant for accessing
`linear_ortho/softness<class_SliderJoint3D_property_linear_ortho/softness>`{.interpreted-text
role="ref"}. A factor applied to the movement across axes orthogonal to
the slider.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_ORTHOGONAL_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_ORTHOGONAL_RESTITUTION** = `9`

Constant for accessing
`linear_motion/restitution<class_SliderJoint3D_property_linear_motion/restitution>`{.interpreted-text
role="ref"}. The amount of restitution when movement is across axes
orthogonal to the slider.

:::: {#class_SliderJoint3D_constant_PARAM_LINEAR_ORTHOGONAL_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_LINEAR_ORTHOGONAL_DAMPING** = `10`

Constant for accessing
`linear_motion/damping<class_SliderJoint3D_property_linear_motion/damping>`{.interpreted-text
role="ref"}. The amount of damping when movement is across axes
orthogonal to the slider.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_LIMIT_UPPER** = `11`

Constant for accessing
`angular_limit/upper_angle<class_SliderJoint3D_property_angular_limit/upper_angle>`{.interpreted-text
role="ref"}. The upper limit of rotation in the slider.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_LIMIT_LOWER** = `12`

Constant for accessing
`angular_limit/lower_angle<class_SliderJoint3D_property_angular_limit/lower_angle>`{.interpreted-text
role="ref"}. The lower limit of rotation in the slider.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_LIMIT_SOFTNESS** = `13`

Constant for accessing
`angular_limit/softness<class_SliderJoint3D_property_angular_limit/softness>`{.interpreted-text
role="ref"}. A factor applied to the all rotation once the limit is
surpassed.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_LIMIT_RESTITUTION** = `14`

Constant for accessing
`angular_limit/restitution<class_SliderJoint3D_property_angular_limit/restitution>`{.interpreted-text
role="ref"}. The amount of restitution of the rotation when the limit is
surpassed.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_LIMIT_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_LIMIT_DAMPING** = `15`

Constant for accessing
`angular_limit/damping<class_SliderJoint3D_property_angular_limit/damping>`{.interpreted-text
role="ref"}. The amount of damping of the rotation when the limit is
surpassed.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_MOTION_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_MOTION_SOFTNESS** = `16`

Constant for accessing
`angular_motion/softness<class_SliderJoint3D_property_angular_motion/softness>`{.interpreted-text
role="ref"}. A factor applied to the all rotation in the limits.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_MOTION_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_MOTION_RESTITUTION** = `17`

Constant for accessing
`angular_motion/restitution<class_SliderJoint3D_property_angular_motion/restitution>`{.interpreted-text
role="ref"}. The amount of restitution of the rotation in the limits.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_MOTION_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_MOTION_DAMPING** = `18`

Constant for accessing
`angular_motion/damping<class_SliderJoint3D_property_angular_motion/damping>`{.interpreted-text
role="ref"}. The amount of damping of the rotation in the limits.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_ORTHOGONAL_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_ORTHOGONAL_SOFTNESS** = `19`

Constant for accessing
`angular_ortho/softness<class_SliderJoint3D_property_angular_ortho/softness>`{.interpreted-text
role="ref"}. A factor applied to the all rotation across axes orthogonal
to the slider.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_ORTHOGONAL_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_ORTHOGONAL_RESTITUTION** = `20`

Constant for accessing
`angular_ortho/restitution<class_SliderJoint3D_property_angular_ortho/restitution>`{.interpreted-text
role="ref"}. The amount of restitution of the rotation across axes
orthogonal to the slider.

:::: {#class_SliderJoint3D_constant_PARAM_ANGULAR_ORTHOGONAL_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_ORTHOGONAL_DAMPING** = `21`

Constant for accessing
`angular_ortho/damping<class_SliderJoint3D_property_angular_ortho/damping>`{.interpreted-text
role="ref"}. The amount of damping of the rotation across axes
orthogonal to the slider.

:::: {#class_SliderJoint3D_constant_PARAM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_MAX** = `22`

Represents the size of the
`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SliderJoint3D_property_angular_limit/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/damping** = `0.0`
`🔗<class_SliderJoint3D_property_angular_limit/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of damping of the rotation when the limit is surpassed.

A lower damping value allows a rotation initiated by body A to travel to
body B slower.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_limit/lower_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/lower_angle** = `0.0`
`🔗<class_SliderJoint3D_property_angular_limit/lower_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The lower limit of rotation in the slider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_limit/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/restitution** = `0.7`
`🔗<class_SliderJoint3D_property_angular_limit/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of restitution of the rotation when the limit is surpassed.

Does not affect damping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_limit/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/softness** = `1.0`
`🔗<class_SliderJoint3D_property_angular_limit/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A factor applied to the all rotation once the limit is surpassed.

Makes all rotation slower when between 0 and 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_limit/upper_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_limit/upper_angle** = `0.0`
`🔗<class_SliderJoint3D_property_angular_limit/upper_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The upper limit of rotation in the slider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_motion/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_motion/damping** = `1.0`
`🔗<class_SliderJoint3D_property_angular_motion/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of damping of the rotation in the limits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_motion/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_motion/restitution** = `0.7`
`🔗<class_SliderJoint3D_property_angular_motion/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of restitution of the rotation in the limits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_motion/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_motion/softness** = `1.0`
`🔗<class_SliderJoint3D_property_angular_motion/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A factor applied to the all rotation in the limits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_ortho/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_ortho/damping** = `1.0`
`🔗<class_SliderJoint3D_property_angular_ortho/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of damping of the rotation across axes orthogonal to the
slider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_ortho/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_ortho/restitution** = `0.7`
`🔗<class_SliderJoint3D_property_angular_ortho/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of restitution of the rotation across axes orthogonal to the
slider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_angular_ortho/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_ortho/softness** = `1.0`
`🔗<class_SliderJoint3D_property_angular_ortho/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A factor applied to the all rotation across axes orthogonal to the
slider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_limit/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit/damping** = `1.0`
`🔗<class_SliderJoint3D_property_linear_limit/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of damping that happens once the limit defined by
`linear_limit/lower_distance<class_SliderJoint3D_property_linear_limit/lower_distance>`{.interpreted-text
role="ref"} and
`linear_limit/upper_distance<class_SliderJoint3D_property_linear_limit/upper_distance>`{.interpreted-text
role="ref"} is surpassed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_limit/lower_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit/lower_distance** = `-1.0`
`🔗<class_SliderJoint3D_property_linear_limit/lower_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The minimum difference between the pivot points on their X axis before
damping happens.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_limit/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit/restitution** = `0.7`
`🔗<class_SliderJoint3D_property_linear_limit/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of restitution once the limits are surpassed. The lower, the
more velocity-energy gets lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_limit/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit/softness** = `1.0`
`🔗<class_SliderJoint3D_property_linear_limit/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A factor applied to the movement across the slider axis once the limits
get surpassed. The lower, the slower the movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_limit/upper_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_limit/upper_distance** = `1.0`
`🔗<class_SliderJoint3D_property_linear_limit/upper_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum difference between the pivot points on their X axis before
damping happens.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_motion/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_motion/damping** = `0.0`
`🔗<class_SliderJoint3D_property_linear_motion/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of damping inside the slider limits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_motion/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_motion/restitution** = `0.7`
`🔗<class_SliderJoint3D_property_linear_motion/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of restitution inside the slider limits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_motion/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_motion/softness** = `1.0`
`🔗<class_SliderJoint3D_property_linear_motion/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A factor applied to the movement across the slider axis as long as the
slider is in the limits. The lower, the slower the movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_ortho/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_ortho/damping** = `1.0`
`🔗<class_SliderJoint3D_property_linear_ortho/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of damping when movement is across axes orthogonal to the
slider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_ortho/restitution}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_ortho/restitution** = `0.7`
`🔗<class_SliderJoint3D_property_linear_ortho/restitution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The amount of restitution when movement is across axes orthogonal to the
slider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_property_linear_ortho/softness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**linear_ortho/softness** = `1.0`
`🔗<class_SliderJoint3D_property_linear_ortho/softness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"},
  value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param:
  `Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A factor applied to the movement across axes orthogonal to the slider.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SliderJoint3D_method_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_param**(param:
`Param<enum_SliderJoint3D_Param>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SliderJoint3D_method_get_param>`{.interpreted-text role="ref"}

Returns the value of the given parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SliderJoint3D_method_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param**(param: `Param<enum_SliderJoint3D_Param>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SliderJoint3D_method_set_param>`{.interpreted-text role="ref"}

Assigns `value` to the given parameter.
