github_url
:   hide

# PhysicsServer3D {#class_PhysicsServer3D}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`PhysicsServer3DExtension<class_PhysicsServer3DExtension>`{.interpreted-text
role="ref"}

A server interface for low-level 3D physics access.

::: rst-class
classref-introduction-group
:::

## Description

PhysicsServer3D is the server responsible for all 3D physics. It can
directly create and manipulate all physics objects:

- A *space* is a self-contained world for a physics simulation. It
  contains bodies, areas, and joints. Its state can be queried for
  collision and intersection information, and several parameters of the
  simulation can be modified.
- A *shape* is a geometric shape such as a sphere, a box, a cylinder, or
  a polygon. It can be used for collision detection by adding it to a
  body/area, possibly with an extra transformation relative to the
  body/area\'s origin. Bodies/areas can have multiple (transformed)
  shapes added to them, and a single shape can be added to bodies/areas
  multiple times with different local transformations.
- A *body* is a physical object which can be in static, kinematic, or
  rigid mode. Its state (such as position and velocity) can be queried
  and updated. A force integration callback can be set to customize the
  body\'s physics.
- An *area* is a region in space which can be used to detect bodies and
  areas entering and exiting it. A body monitoring callback can be set
  to report entering/exiting body shapes, and similarly an area
  monitoring callback can be set. Gravity and damping can be overridden
  within the area by setting area parameters.
- A *joint* is a constraint, either between two bodies or on one body
  relative to a point. Parameters such as the joint bias and the rest
  length of a spring joint can be adjusted.

Physics objects in **PhysicsServer3D** may be created and manipulated
independently; they do not have to be tied to nodes in the scene tree.

\*\*Note:\*\* All the 3D physics nodes use the physics server
internally. Adding a physics node to the scene tree will cause a
corresponding physics object to be created in the physics server. A
rigid body node registers a callback that updates the node\'s transform
with the transform of the respective body object in the physics server
(every physics update). An area node registers a callback to inform the
area node about overlaps with the respective area object in the physics
server. The raycast node queries the direct state of the relevant space
in the physics server.

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

:::: {#enum_PhysicsServer3D_JointType}
::: rst-class
classref-enumeration
:::
::::

enum **JointType**:
`🔗<enum_PhysicsServer3D_JointType>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_JOINT_TYPE_PIN}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer3D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_PIN** = `0`

The `Joint3D<class_Joint3D>`{.interpreted-text role="ref"} is a
`PinJoint3D<class_PinJoint3D>`{.interpreted-text role="ref"}.

:::: {#class_PhysicsServer3D_constant_JOINT_TYPE_HINGE}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer3D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_HINGE** = `1`

The `Joint3D<class_Joint3D>`{.interpreted-text role="ref"} is a
`HingeJoint3D<class_HingeJoint3D>`{.interpreted-text role="ref"}.

:::: {#class_PhysicsServer3D_constant_JOINT_TYPE_SLIDER}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer3D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_SLIDER** = `2`

The `Joint3D<class_Joint3D>`{.interpreted-text role="ref"} is a
`SliderJoint3D<class_SliderJoint3D>`{.interpreted-text role="ref"}.

:::: {#class_PhysicsServer3D_constant_JOINT_TYPE_CONE_TWIST}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer3D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_CONE_TWIST** = `3`

The `Joint3D<class_Joint3D>`{.interpreted-text role="ref"} is a
`ConeTwistJoint3D<class_ConeTwistJoint3D>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer3D_constant_JOINT_TYPE_6DOF}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer3D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_6DOF** = `4`

The `Joint3D<class_Joint3D>`{.interpreted-text role="ref"} is a
`Generic6DOFJoint3D<class_Generic6DOFJoint3D>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer3D_constant_JOINT_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`JointType<enum_PhysicsServer3D_JointType>`{.interpreted-text
role="ref"} **JOINT_TYPE_MAX** = `5`

Represents the size of the
`JointType<enum_PhysicsServer3D_JointType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_PinJointParam}
::: rst-class
classref-enumeration
:::
::::

enum **PinJointParam**:
`🔗<enum_PhysicsServer3D_PinJointParam>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_PIN_JOINT_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`PinJointParam<enum_PhysicsServer3D_PinJointParam>`{.interpreted-text
role="ref"} **PIN_JOINT_BIAS** = `0`

The strength with which the pinned objects try to stay in positional
relation to each other.

The higher, the stronger.

:::: {#class_PhysicsServer3D_constant_PIN_JOINT_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`PinJointParam<enum_PhysicsServer3D_PinJointParam>`{.interpreted-text
role="ref"} **PIN_JOINT_DAMPING** = `1`

The strength with which the pinned objects try to stay in velocity
relation to each other.

The higher, the stronger.

:::: {#class_PhysicsServer3D_constant_PIN_JOINT_IMPULSE_CLAMP}
::: rst-class
classref-enumeration-constant
:::
::::

`PinJointParam<enum_PhysicsServer3D_PinJointParam>`{.interpreted-text
role="ref"} **PIN_JOINT_IMPULSE_CLAMP** = `2`

If above 0, this value is the maximum value for an impulse that this
Joint3D puts on its ends.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_HingeJointParam}
::: rst-class
classref-enumeration
:::
::::

enum **HingeJointParam**:
`🔗<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"} **HINGE_JOINT_BIAS** = `0`

The speed with which the two bodies get pulled together when they move
in different directions.

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_LIMIT_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"} **HINGE_JOINT_LIMIT_UPPER** = `1`

The maximum rotation across the Hinge.

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_LIMIT_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"} **HINGE_JOINT_LIMIT_LOWER** = `2`

The minimum rotation across the Hinge.

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_LIMIT_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"} **HINGE_JOINT_LIMIT_BIAS** = `3`

The speed with which the rotation across the axis perpendicular to the
hinge gets corrected.

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"} **HINGE_JOINT_LIMIT_SOFTNESS** = `4`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_LIMIT_RELAXATION}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"} **HINGE_JOINT_LIMIT_RELAXATION** = `5`

The lower this value, the more the rotation gets slowed down.

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_MOTOR_TARGET_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"} **HINGE_JOINT_MOTOR_TARGET_VELOCITY** = `6`

Target speed for the motor.

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_MOTOR_MAX_IMPULSE}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"} **HINGE_JOINT_MOTOR_MAX_IMPULSE** = `7`

Maximum acceleration for the motor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_HingeJointFlag}
::: rst-class
classref-enumeration
:::
::::

enum **HingeJointFlag**:
`🔗<enum_PhysicsServer3D_HingeJointFlag>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_FLAG_USE_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointFlag<enum_PhysicsServer3D_HingeJointFlag>`{.interpreted-text
role="ref"} **HINGE_JOINT_FLAG_USE_LIMIT** = `0`

If `true`, the Hinge has a maximum and a minimum rotation.

:::: {#class_PhysicsServer3D_constant_HINGE_JOINT_FLAG_ENABLE_MOTOR}
::: rst-class
classref-enumeration-constant
:::
::::

`HingeJointFlag<enum_PhysicsServer3D_HingeJointFlag>`{.interpreted-text
role="ref"} **HINGE_JOINT_FLAG_ENABLE_MOTOR** = `1`

If `true`, a motor turns the Hinge.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_SliderJointParam}
::: rst-class
classref-enumeration
:::
::::

enum **SliderJointParam**:
`🔗<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_LIMIT_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_LIMIT_UPPER** = `0`

The maximum difference between the pivot points on their X axis before
damping happens.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_LIMIT_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_LIMIT_LOWER** = `1`

The minimum difference between the pivot points on their X axis before
damping happens.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_LIMIT_SOFTNESS** = `2`

A factor applied to the movement across the slider axis once the limits
get surpassed. The lower, the slower the movement.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_LIMIT_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_LIMIT_RESTITUTION** = `3`

The amount of restitution once the limits are surpassed. The lower, the
more velocity-energy gets lost.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_LIMIT_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_LIMIT_DAMPING** = `4`

The amount of damping once the slider limits are surpassed.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_MOTION_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_MOTION_SOFTNESS** = `5`

A factor applied to the movement across the slider axis as long as the
slider is in the limits. The lower, the slower the movement.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_MOTION_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_MOTION_RESTITUTION** = `6`

The amount of restitution inside the slider limits.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_MOTION_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_MOTION_DAMPING** = `7`

The amount of damping inside the slider limits.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_ORTHOGONAL_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_ORTHOGONAL_SOFTNESS** = `8`

A factor applied to the movement across axes orthogonal to the slider.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_ORTHOGONAL_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_ORTHOGONAL_RESTITUTION** = `9`

The amount of restitution when movement is across axes orthogonal to the
slider.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_LINEAR_ORTHOGONAL_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_LINEAR_ORTHOGONAL_DAMPING** = `10`

The amount of damping when movement is across axes orthogonal to the
slider.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_LIMIT_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_LIMIT_UPPER** = `11`

The upper limit of rotation in the slider.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_LIMIT_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_LIMIT_LOWER** = `12`

The lower limit of rotation in the slider.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_LIMIT_SOFTNESS** = `13`

A factor applied to the all rotation once the limit is surpassed.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_LIMIT_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_LIMIT_RESTITUTION** = `14`

The amount of restitution of the rotation when the limit is surpassed.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_LIMIT_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_LIMIT_DAMPING** = `15`

The amount of damping of the rotation when the limit is surpassed.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_MOTION_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_MOTION_SOFTNESS** = `16`

A factor that gets applied to the all rotation in the limits.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_MOTION_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_MOTION_RESTITUTION** = `17`

The amount of restitution of the rotation in the limits.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_MOTION_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_MOTION_DAMPING** = `18`

The amount of damping of the rotation in the limits.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_ORTHOGONAL_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_ORTHOGONAL_SOFTNESS** = `19`

A factor that gets applied to the all rotation across axes orthogonal to
the slider.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_ORTHOGONAL_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_ORTHOGONAL_RESTITUTION** = `20`

The amount of restitution of the rotation across axes orthogonal to the
slider.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_ANGULAR_ORTHOGONAL_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_ANGULAR_ORTHOGONAL_DAMPING** = `21`

The amount of damping of the rotation across axes orthogonal to the
slider.

:::: {#class_PhysicsServer3D_constant_SLIDER_JOINT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} **SLIDER_JOINT_MAX** = `22`

Represents the size of the
`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_ConeTwistJointParam}
::: rst-class
classref-enumeration
:::
::::

enum **ConeTwistJointParam**:
`🔗<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer3D_constant_CONE_TWIST_JOINT_SWING_SPAN}
::: rst-class
classref-enumeration-constant
:::
::::

`ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"} **CONE_TWIST_JOINT_SWING_SPAN** = `0`

Swing is rotation from side to side, around the axis perpendicular to
the twist axis.

The swing span defines, how much rotation will not get corrected along
the swing axis.

Could be defined as looseness in the
`ConeTwistJoint3D<class_ConeTwistJoint3D>`{.interpreted-text
role="ref"}.

If below 0.05, this behavior is locked.

:::: {#class_PhysicsServer3D_constant_CONE_TWIST_JOINT_TWIST_SPAN}
::: rst-class
classref-enumeration-constant
:::
::::

`ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"} **CONE_TWIST_JOINT_TWIST_SPAN** = `1`

Twist is the rotation around the twist axis, this value defined how far
the joint can twist.

Twist is locked if below 0.05.

:::: {#class_PhysicsServer3D_constant_CONE_TWIST_JOINT_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"} **CONE_TWIST_JOINT_BIAS** = `2`

The speed with which the swing or twist will take place.

The higher, the faster.

:::: {#class_PhysicsServer3D_constant_CONE_TWIST_JOINT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"} **CONE_TWIST_JOINT_SOFTNESS** = `3`

The ease with which the Joint3D twists, if it\'s too low, it takes more
force to twist the joint.

:::: {#class_PhysicsServer3D_constant_CONE_TWIST_JOINT_RELAXATION}
::: rst-class
classref-enumeration-constant
:::
::::

`ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"} **CONE_TWIST_JOINT_RELAXATION** = `4`

Defines, how fast the swing- and twist-speed-difference on both sides
gets synced.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_G6DOFJointAxisParam}
::: rst-class
classref-enumeration
:::
::::

enum **G6DOFJointAxisParam**:
`🔗<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_LOWER_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_LOWER_LIMIT** = `0`

The minimum difference between the pivot points\' axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_UPPER_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_UPPER_LIMIT** = `1`

The maximum difference between the pivot points\' axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_LIMIT_SOFTNESS** = `2`

A factor that gets applied to the movement across the axes. The lower,
the slower the movement.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_RESTITUTION** = `3`

The amount of restitution on the axes movement. The lower, the more
velocity-energy gets lost.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_DAMPING** = `4`

The amount of damping that happens at the linear motion across the axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_MOTOR_TARGET_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_MOTOR_TARGET_VELOCITY** = `5`

The velocity that the joint\'s linear motor will attempt to reach.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_MOTOR_FORCE_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_MOTOR_FORCE_LIMIT** = `6`

The maximum force that the linear motor can apply while trying to reach
the target velocity.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_SPRING_STIFFNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_SPRING_STIFFNESS** = `7`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_SPRING_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_SPRING_DAMPING** = `8`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_LINEAR_SPRING_EQUILIBRIUM_POINT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_LINEAR_SPRING_EQUILIBRIUM_POINT** = `9`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_LOWER_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_LOWER_LIMIT** = `10`

The minimum rotation in negative direction to break loose and rotate
around the axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_UPPER_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_UPPER_LIMIT** = `11`

The minimum rotation in positive direction to break loose and rotate
around the axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_LIMIT_SOFTNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_LIMIT_SOFTNESS** = `12`

A factor that gets multiplied onto all rotations across the axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_DAMPING** = `13`

The amount of rotational damping across the axes. The lower, the more
damping occurs.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_RESTITUTION}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_RESTITUTION** = `14`

The amount of rotational restitution across the axes. The lower, the
more restitution occurs.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_FORCE_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_FORCE_LIMIT** = `15`

The maximum amount of force that can occur, when rotating around the
axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_ERP}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_ERP** = `16`

When correcting the crossing of limits in rotation across the axes, this
error tolerance factor defines how much the correction gets slowed down.
The lower, the slower.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_MOTOR_TARGET_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_MOTOR_TARGET_VELOCITY** = `17`

Target speed for the motor at the axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_MOTOR_FORCE_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_MOTOR_FORCE_LIMIT** = `18`

Maximum acceleration for the motor at the axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_SPRING_STIFFNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_SPRING_STIFFNESS** = `19`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_SPRING_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_SPRING_DAMPING** = `20`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_ANGULAR_SPRING_EQUILIBRIUM_POINT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_ANGULAR_SPRING_EQUILIBRIUM_POINT** = `21`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} **G6DOF_JOINT_MAX** = `22`

Represents the size of the
`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_G6DOFJointAxisFlag}
::: rst-class
classref-enumeration
:::
::::

enum **G6DOFJointAxisFlag**:
`🔗<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_FLAG_ENABLE_LINEAR_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"} **G6DOF_JOINT_FLAG_ENABLE_LINEAR_LIMIT** = `0`

If set, linear motion is possible within the given limits.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_FLAG_ENABLE_ANGULAR_LIMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"} **G6DOF_JOINT_FLAG_ENABLE_ANGULAR_LIMIT** = `1`

If set, rotational motion is possible.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_FLAG_ENABLE_ANGULAR_SPRING}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"} **G6DOF_JOINT_FLAG_ENABLE_ANGULAR_SPRING** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_FLAG_ENABLE_LINEAR_SPRING}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"} **G6DOF_JOINT_FLAG_ENABLE_LINEAR_SPRING** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_FLAG_ENABLE_MOTOR}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"} **G6DOF_JOINT_FLAG_ENABLE_MOTOR** = `4`

If set, there is a rotational motor across these axes.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_FLAG_ENABLE_LINEAR_MOTOR}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"} **G6DOF_JOINT_FLAG_ENABLE_LINEAR_MOTOR** = `5`

If set, there is a linear motor on this axis that targets a specific
velocity.

:::: {#class_PhysicsServer3D_constant_G6DOF_JOINT_FLAG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"} **G6DOF_JOINT_FLAG_MAX** = `6`

Represents the size of the
`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_ShapeType}
::: rst-class
classref-enumeration
:::
::::

enum **ShapeType**:
`🔗<enum_PhysicsServer3D_ShapeType>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_SHAPE_WORLD_BOUNDARY}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_WORLD_BOUNDARY** = `0`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is a
`WorldBoundaryShape3D<class_WorldBoundaryShape3D>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer3D_constant_SHAPE_SEPARATION_RAY}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_SEPARATION_RAY** = `1`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is a
`SeparationRayShape3D<class_SeparationRayShape3D>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer3D_constant_SHAPE_SPHERE}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_SPHERE** = `2`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is a
`SphereShape3D<class_SphereShape3D>`{.interpreted-text role="ref"}.

:::: {#class_PhysicsServer3D_constant_SHAPE_BOX}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_BOX** = `3`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is a
`BoxShape3D<class_BoxShape3D>`{.interpreted-text role="ref"}.

:::: {#class_PhysicsServer3D_constant_SHAPE_CAPSULE}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CAPSULE** = `4`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is a
`CapsuleShape3D<class_CapsuleShape3D>`{.interpreted-text role="ref"}.

:::: {#class_PhysicsServer3D_constant_SHAPE_CYLINDER}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CYLINDER** = `5`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is a
`CylinderShape3D<class_CylinderShape3D>`{.interpreted-text role="ref"}.

:::: {#class_PhysicsServer3D_constant_SHAPE_CONVEX_POLYGON}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CONVEX_POLYGON** = `6`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is a
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer3D_constant_SHAPE_CONCAVE_POLYGON}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CONCAVE_POLYGON** = `7`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is a
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer3D_constant_SHAPE_HEIGHTMAP}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_HEIGHTMAP** = `8`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is a
`HeightMapShape3D<class_HeightMapShape3D>`{.interpreted-text
role="ref"}.

:::: {#class_PhysicsServer3D_constant_SHAPE_SOFT_BODY}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_SOFT_BODY** = `9`

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} is used
internally for a soft body. Any attempt to create this kind of shape
results in an error.

:::: {#class_PhysicsServer3D_constant_SHAPE_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **SHAPE_CUSTOM** = `10`

This constant is used internally by the engine. Any attempt to create
this kind of shape results in an error.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_AreaParameter}
::: rst-class
classref-enumeration
:::
::::

enum **AreaParameter**:
`🔗<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_GRAVITY_OVERRIDE_MODE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY_OVERRIDE_MODE** = `0`

Constant to set/get gravity override mode in an area. See
`AreaSpaceOverrideMode<enum_PhysicsServer3D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} for possible values.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_GRAVITY}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY** = `1`

Constant to set/get gravity strength in an area.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_GRAVITY_VECTOR}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY_VECTOR** = `2`

Constant to set/get gravity vector/center in an area.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_GRAVITY_IS_POINT}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY_IS_POINT** = `3`

Constant to set/get whether the gravity vector of an area is a
direction, or a center point.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_GRAVITY_POINT_UNIT_DISTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_GRAVITY_POINT_UNIT_DISTANCE** = `4`

Constant to set/get the distance at which the gravity strength is equal
to the gravity controlled by
`AREA_PARAM_GRAVITY<class_PhysicsServer3D_constant_AREA_PARAM_GRAVITY>`{.interpreted-text
role="ref"}. For example, on a planet 100 meters in radius with a
surface gravity of 4.0 m/s², set the gravity to 4.0 and the unit
distance to 100.0. The gravity will have falloff according to the
inverse square law, so in the example, at 200 meters from the center the
gravity will be 1.0 m/s² (twice the distance, 1/4th the gravity), at 50
meters it will be 16.0 m/s² (half the distance, 4x the gravity), and so
on.

The above is true only when the unit distance is a positive number. When
this is set to 0.0, the gravity will be constant regardless of distance.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_LINEAR_DAMP_OVERRIDE_MODE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_LINEAR_DAMP_OVERRIDE_MODE** = `5`

Constant to set/get linear damping override mode in an area. See
`AreaSpaceOverrideMode<enum_PhysicsServer3D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} for possible values.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_LINEAR_DAMP}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_LINEAR_DAMP** = `6`

Constant to set/get the linear damping factor of an area.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_ANGULAR_DAMP_OVERRIDE_MODE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_ANGULAR_DAMP_OVERRIDE_MODE** = `7`

Constant to set/get angular damping override mode in an area. See
`AreaSpaceOverrideMode<enum_PhysicsServer3D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} for possible values.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_ANGULAR_DAMP}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_ANGULAR_DAMP** = `8`

Constant to set/get the angular damping factor of an area.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_PRIORITY}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_PRIORITY** = `9`

Constant to set/get the priority (order of processing) of an area.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_WIND_FORCE_MAGNITUDE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_WIND_FORCE_MAGNITUDE** = `10`

Constant to set/get the magnitude of area-specific wind force. This wind
force only applies to `SoftBody3D<class_SoftBody3D>`{.interpreted-text
role="ref"} nodes. Other physics bodies are currently not affected by
wind.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_WIND_SOURCE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_WIND_SOURCE** = `11`

Constant to set/get the 3D vector that specifies the origin from which
an area-specific wind blows.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_WIND_DIRECTION}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_WIND_DIRECTION** = `12`

Constant to set/get the 3D vector that specifies the direction in which
an area-specific wind blows.

:::: {#class_PhysicsServer3D_constant_AREA_PARAM_WIND_ATTENUATION_FACTOR}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} **AREA_PARAM_WIND_ATTENUATION_FACTOR** = `13`

Constant to set/get the exponential rate at which wind force decreases
with distance from its origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_AreaSpaceOverrideMode}
::: rst-class
classref-enumeration
:::
::::

enum **AreaSpaceOverrideMode**:
`🔗<enum_PhysicsServer3D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer3D_constant_AREA_SPACE_OVERRIDE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer3D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_DISABLED** = `0`

This area does not affect gravity/damp. These are generally areas that
exist only to detect collisions, and objects entering or exiting them.

:::: {#class_PhysicsServer3D_constant_AREA_SPACE_OVERRIDE_COMBINE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer3D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_COMBINE** = `1`

This area adds its gravity/damp values to whatever has been calculated
so far. This way, many overlapping areas can combine their physics to
make interesting effects.

:::: {#class_PhysicsServer3D_constant_AREA_SPACE_OVERRIDE_COMBINE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer3D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_COMBINE_REPLACE** = `2`

This area adds its gravity/damp values to whatever has been calculated
so far. Then stops taking into account the rest of the areas, even the
default one.

:::: {#class_PhysicsServer3D_constant_AREA_SPACE_OVERRIDE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer3D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_REPLACE** = `3`

This area replaces any gravity/damp, even the default one, and stops
taking into account the rest of the areas.

:::: {#class_PhysicsServer3D_constant_AREA_SPACE_OVERRIDE_REPLACE_COMBINE}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaSpaceOverrideMode<enum_PhysicsServer3D_AreaSpaceOverrideMode>`{.interpreted-text
role="ref"} **AREA_SPACE_OVERRIDE_REPLACE_COMBINE** = `4`

This area replaces any gravity/damp calculated so far, but keeps
calculating the rest of the areas, down to the default one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_BodyMode}
::: rst-class
classref-enumeration
:::
::::

enum **BodyMode**: `🔗<enum_PhysicsServer3D_BodyMode>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer3D_constant_BODY_MODE_STATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyMode<enum_PhysicsServer3D_BodyMode>`{.interpreted-text role="ref"}
**BODY_MODE_STATIC** = `0`

Constant for static bodies. In this mode, a body can be only moved by
user code and doesn\'t collide with other bodies along its path when
moved.

:::: {#class_PhysicsServer3D_constant_BODY_MODE_KINEMATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyMode<enum_PhysicsServer3D_BodyMode>`{.interpreted-text role="ref"}
**BODY_MODE_KINEMATIC** = `1`

Constant for kinematic bodies. In this mode, a body can be only moved by
user code and collides with other bodies along its path.

:::: {#class_PhysicsServer3D_constant_BODY_MODE_RIGID}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyMode<enum_PhysicsServer3D_BodyMode>`{.interpreted-text role="ref"}
**BODY_MODE_RIGID** = `2`

Constant for rigid bodies. In this mode, a body can be pushed by other
bodies and has forces applied.

:::: {#class_PhysicsServer3D_constant_BODY_MODE_RIGID_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyMode<enum_PhysicsServer3D_BodyMode>`{.interpreted-text role="ref"}
**BODY_MODE_RIGID_LINEAR** = `3`

Constant for linear rigid bodies. In this mode, a body can not rotate,
and only its linear velocity is affected by external forces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_BodyParameter}
::: rst-class
classref-enumeration
:::
::::

enum **BodyParameter**:
`🔗<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_BOUNCE}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_BOUNCE** = `0`

Constant to set/get a body\'s bounce factor.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_FRICTION}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_FRICTION** = `1`

Constant to set/get a body\'s friction.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_MASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_MASS** = `2`

Constant to set/get a body\'s mass.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_INERTIA}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_INERTIA** = `3`

Constant to set/get a body\'s inertia.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_CENTER_OF_MASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_CENTER_OF_MASS** = `4`

Constant to set/get a body\'s center of mass position in the body\'s
local coordinate system.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_GRAVITY_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_GRAVITY_SCALE** = `5`

Constant to set/get a body\'s gravity multiplier.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_LINEAR_DAMP_MODE}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_LINEAR_DAMP_MODE** = `6`

Constant to set/get a body\'s linear damping mode. See
`BodyDampMode<enum_PhysicsServer3D_BodyDampMode>`{.interpreted-text
role="ref"} for possible values.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_ANGULAR_DAMP_MODE}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_ANGULAR_DAMP_MODE** = `7`

Constant to set/get a body\'s angular damping mode. See
`BodyDampMode<enum_PhysicsServer3D_BodyDampMode>`{.interpreted-text
role="ref"} for possible values.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_LINEAR_DAMP}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_LINEAR_DAMP** = `8`

Constant to set/get a body\'s linear damping factor.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_ANGULAR_DAMP}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_ANGULAR_DAMP** = `9`

Constant to set/get a body\'s angular damping factor.

:::: {#class_PhysicsServer3D_constant_BODY_PARAM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} **BODY_PARAM_MAX** = `10`

Represents the size of the
`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_BodyDampMode}
::: rst-class
classref-enumeration
:::
::::

enum **BodyDampMode**:
`🔗<enum_PhysicsServer3D_BodyDampMode>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_BODY_DAMP_MODE_COMBINE}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyDampMode<enum_PhysicsServer3D_BodyDampMode>`{.interpreted-text
role="ref"} **BODY_DAMP_MODE_COMBINE** = `0`

The body\'s damping value is added to any value set in areas or the
default value.

:::: {#class_PhysicsServer3D_constant_BODY_DAMP_MODE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyDampMode<enum_PhysicsServer3D_BodyDampMode>`{.interpreted-text
role="ref"} **BODY_DAMP_MODE_REPLACE** = `1`

The body\'s damping value replaces any value set in areas or the default
value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_BodyState}
::: rst-class
classref-enumeration
:::
::::

enum **BodyState**:
`🔗<enum_PhysicsServer3D_BodyState>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_BODY_STATE_TRANSFORM}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_TRANSFORM** = `0`

Constant to set/get the current transform matrix of the body.

:::: {#class_PhysicsServer3D_constant_BODY_STATE_LINEAR_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_LINEAR_VELOCITY** = `1`

Constant to set/get the current linear velocity of the body.

:::: {#class_PhysicsServer3D_constant_BODY_STATE_ANGULAR_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_ANGULAR_VELOCITY** = `2`

Constant to set/get the current angular velocity of the body.

:::: {#class_PhysicsServer3D_constant_BODY_STATE_SLEEPING}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_SLEEPING** = `3`

Constant to sleep/wake up a body, or to get whether it is sleeping.

:::: {#class_PhysicsServer3D_constant_BODY_STATE_CAN_SLEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"} **BODY_STATE_CAN_SLEEP** = `4`

Constant to set/get whether the body can sleep.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_AreaBodyStatus}
::: rst-class
classref-enumeration
:::
::::

enum **AreaBodyStatus**:
`🔗<enum_PhysicsServer3D_AreaBodyStatus>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_AREA_BODY_ADDED}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaBodyStatus<enum_PhysicsServer3D_AreaBodyStatus>`{.interpreted-text
role="ref"} **AREA_BODY_ADDED** = `0`

The value of the first parameter and area callback function receives,
when an object enters one of its shapes.

:::: {#class_PhysicsServer3D_constant_AREA_BODY_REMOVED}
::: rst-class
classref-enumeration-constant
:::
::::

`AreaBodyStatus<enum_PhysicsServer3D_AreaBodyStatus>`{.interpreted-text
role="ref"} **AREA_BODY_REMOVED** = `1`

The value of the first parameter and area callback function receives,
when an object exits one of its shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_ProcessInfo}
::: rst-class
classref-enumeration
:::
::::

enum **ProcessInfo**:
`🔗<enum_PhysicsServer3D_ProcessInfo>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_INFO_ACTIVE_OBJECTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_PhysicsServer3D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_ACTIVE_OBJECTS** = `0`

Constant to get the number of objects that are not sleeping.

:::: {#class_PhysicsServer3D_constant_INFO_COLLISION_PAIRS}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_PhysicsServer3D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_COLLISION_PAIRS** = `1`

Constant to get the number of possible collisions.

:::: {#class_PhysicsServer3D_constant_INFO_ISLAND_COUNT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessInfo<enum_PhysicsServer3D_ProcessInfo>`{.interpreted-text
role="ref"} **INFO_ISLAND_COUNT** = `2`

Constant to get the number of space regions where a collision could
occur.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_SpaceParameter}
::: rst-class
classref-enumeration
:::
::::

enum **SpaceParameter**:
`🔗<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text role="ref"}

:::: {#class_PhysicsServer3D_constant_SPACE_PARAM_CONTACT_RECYCLE_RADIUS}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_CONTACT_RECYCLE_RADIUS** = `0`

Constant to set/get the maximum distance a pair of bodies has to move
before their collision status has to be recalculated.

:::: {#class_PhysicsServer3D_constant_SPACE_PARAM_CONTACT_MAX_SEPARATION}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_CONTACT_MAX_SEPARATION** = `1`

Constant to set/get the maximum distance a shape can be from another
before they are considered separated and the contact is discarded.

:::: {#class_PhysicsServer3D_constant_SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION** = `2`

Constant to set/get the maximum distance a shape can penetrate another
shape before it is considered a collision.

:::: {#class_PhysicsServer3D_constant_SPACE_PARAM_CONTACT_DEFAULT_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_CONTACT_DEFAULT_BIAS** = `3`

Constant to set/get the default solver bias for all physics contacts. A
solver bias is a factor controlling how much two objects \"rebound\",
after overlapping, to avoid leaving them in that state because of
numerical imprecision.

:::: {#class_PhysicsServer3D_constant_SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD** = `4`

Constant to set/get the threshold linear velocity of activity. A body
marked as potentially inactive for both linear and angular velocity will
be put to sleep after the time given.

:::: {#class_PhysicsServer3D_constant_SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD** = `5`

Constant to set/get the threshold angular velocity of activity. A body
marked as potentially inactive for both linear and angular velocity will
be put to sleep after the time given.

:::: {#class_PhysicsServer3D_constant_SPACE_PARAM_BODY_TIME_TO_SLEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_BODY_TIME_TO_SLEEP** = `6`

Constant to set/get the maximum time of activity. A body marked as
potentially inactive for both linear and angular velocity will be put to
sleep after this time.

:::: {#class_PhysicsServer3D_constant_SPACE_PARAM_SOLVER_ITERATIONS}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"} **SPACE_PARAM_SOLVER_ITERATIONS** = `7`

Constant to set/get the number of solver iterations for contacts and
constraints. The greater the number of iterations, the more accurate the
collisions and constraints will be. However, a greater number of
iterations requires more CPU power, which can decrease performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_PhysicsServer3D_BodyAxis}
::: rst-class
classref-enumeration
:::
::::

enum **BodyAxis**: `🔗<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text
role="ref"}

:::: {#class_PhysicsServer3D_constant_BODY_AXIS_LINEAR_X}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"}
**BODY_AXIS_LINEAR_X** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_BODY_AXIS_LINEAR_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"}
**BODY_AXIS_LINEAR_Y** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_BODY_AXIS_LINEAR_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"}
**BODY_AXIS_LINEAR_Z** = `4`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_BODY_AXIS_ANGULAR_X}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"}
**BODY_AXIS_ANGULAR_X** = `8`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_BODY_AXIS_ANGULAR_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"}
**BODY_AXIS_ANGULAR_Y** = `16`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_PhysicsServer3D_constant_BODY_AXIS_ANGULAR_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"}
**BODY_AXIS_ANGULAR_Z** = `32`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
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

:::: {#class_PhysicsServer3D_method_area_add_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_add_shape**(area: `RID<class_RID>`{.interpreted-text role="ref"},
shape: `RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} =
Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PhysicsServer3D_method_area_add_shape>`{.interpreted-text
role="ref"}

Adds a shape to the area, along with a transform matrix. Shapes are
usually referenced by their index, so you should track which shape has a
given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_attach_object_instance_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_attach_object_instance_id**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_attach_object_instance_id>`{.interpreted-text
role="ref"}

Assigns the area to a descendant of
`Object<class_Object>`{.interpreted-text role="ref"}, so it can exist in
the node tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_clear_shapes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_clear_shapes**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_area_clear_shapes>`{.interpreted-text
role="ref"}

Removes all shapes from an area. It does not delete the shapes, so they
can be reassigned later.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **area_create**()
`🔗<class_PhysicsServer3D_method_area_create>`{.interpreted-text
role="ref"}

Creates a 3D area object in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. The
default settings for the created area include a collision layer and mask
set to `1`, and `monitorable` set to `false`.

Use
`area_add_shape()<class_PhysicsServer3D_method_area_add_shape>`{.interpreted-text
role="ref"} to add shapes to it, use
`area_set_transform()<class_PhysicsServer3D_method_area_set_transform>`{.interpreted-text
role="ref"} to set its transform, and use
`area_set_space()<class_PhysicsServer3D_method_area_set_space>`{.interpreted-text
role="ref"} to add the area to a space. If you want the area to be
detectable use
`area_set_monitorable()<class_PhysicsServer3D_method_area_set_monitorable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_get_collision_layer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**area_get_collision_layer**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_area_get_collision_layer>`{.interpreted-text
role="ref"}

Returns the physics layer or layers an area belongs to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_get_collision_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**area_get_collision_mask**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_area_get_collision_mask>`{.interpreted-text
role="ref"}

Returns the physics layer or layers an area can contact with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_get_object_instance_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**area_get_object_instance_id**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_area_get_object_instance_id>`{.interpreted-text
role="ref"}

Gets the instance ID of the object the area is assigned to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_get_param}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**area_get_param**(area: `RID<class_RID>`{.interpreted-text role="ref"},
param:
`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_area_get_param>`{.interpreted-text
role="ref"}

Returns an area parameter value. A list of available parameters is on
the
`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_get_shape}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **area_get_shape**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, shape_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_area_get_shape>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the nth
shape of an area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_get_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**area_get_shape_count**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_area_get_shape_count>`{.interpreted-text
role="ref"}

Returns the number of shapes assigned to an area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_get_shape_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**area_get_shape_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_area_get_shape_transform>`{.interpreted-text
role="ref"}

Returns the transform matrix of a shape within an area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_get_space}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **area_get_space**(area:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_area_get_space>`{.interpreted-text
role="ref"}

Returns the space assigned to the area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_get_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**area_get_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_area_get_transform>`{.interpreted-text
role="ref"}

Returns the transform matrix for an area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_remove_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_remove_shape**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_remove_shape>`{.interpreted-text
role="ref"}

Removes a shape from an area. It does not delete the shape, so it can be
reassigned later.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_area_monitor_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_area_monitor_callback**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_area_monitor_callback>`{.interpreted-text
role="ref"}

Sets the area\'s area monitor callback. This callback will be called
when any other (shape of an) area enters or exits (a shape of) the given
area, and must take the following five parameters:

1.  an integer `status`: either
    `AREA_BODY_ADDED<class_PhysicsServer3D_constant_AREA_BODY_ADDED>`{.interpreted-text
    role="ref"} or
    `AREA_BODY_REMOVED<class_PhysicsServer3D_constant_AREA_BODY_REMOVED>`{.interpreted-text
    role="ref"} depending on whether the other area\'s shape entered or
    exited the area,
2.  an `RID<class_RID>`{.interpreted-text role="ref"} `area_rid`: the
    `RID<class_RID>`{.interpreted-text role="ref"} of the other area
    that entered or exited the area,
3.  an integer `instance_id`: the `ObjectID` attached to the other area,
4.  an integer `area_shape_idx`: the index of the shape of the other
    area that entered or exited the area,
5.  an integer `self_shape_idx`: the index of the shape of the area
    where the other area entered or exited.

By counting (or keeping track of) the shapes that enter and exit, it can
be determined if an area (with all its shapes) is entering for the first
time or exiting for the last time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_collision_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_collision_layer**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_collision_layer>`{.interpreted-text
role="ref"}

Assigns the area to one or many physics layers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_collision_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_collision_mask**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_collision_mask>`{.interpreted-text
role="ref"}

Sets which physics layers the area will monitor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_monitor_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_monitor_callback**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_monitor_callback>`{.interpreted-text
role="ref"}

Sets the area\'s body monitor callback. This callback will be called
when any other (shape of a) body enters or exits (a shape of) the given
area, and must take the following five parameters:

1.  an integer `status`: either
    `AREA_BODY_ADDED<class_PhysicsServer3D_constant_AREA_BODY_ADDED>`{.interpreted-text
    role="ref"} or
    `AREA_BODY_REMOVED<class_PhysicsServer3D_constant_AREA_BODY_REMOVED>`{.interpreted-text
    role="ref"} depending on whether the other body shape entered or
    exited the area,
2.  an `RID<class_RID>`{.interpreted-text role="ref"} `body_rid`: the
    `RID<class_RID>`{.interpreted-text role="ref"} of the body that
    entered or exited the area,
3.  an integer `instance_id`: the `ObjectID` attached to the body,
4.  an integer `body_shape_idx`: the index of the shape of the body that
    entered or exited the area,
5.  an integer `self_shape_idx`: the index of the shape of the area
    where the body entered or exited.

By counting (or keeping track of) the shapes that enter and exit, it can
be determined if a body (with all its shapes) is entering for the first
time or exiting for the last time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_monitorable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_monitorable**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, monitorable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_monitorable>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_area_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_param**(area: `RID<class_RID>`{.interpreted-text role="ref"},
param:
`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_param>`{.interpreted-text
role="ref"}

Sets the value for an area parameter. A list of available parameters is
on the
`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"} constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_ray_pickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_ray_pickable**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_ray_pickable>`{.interpreted-text
role="ref"}

Sets object pickable with rays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_shape**(area: `RID<class_RID>`{.interpreted-text role="ref"},
shape_idx: `int<class_int>`{.interpreted-text role="ref"}, shape:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_shape>`{.interpreted-text
role="ref"}

Substitutes a given area shape by another. The old shape is selected by
its index, the new one by its `RID<class_RID>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_shape_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_shape_disabled**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_shape_disabled>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_area_set_shape_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_shape_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_shape_transform>`{.interpreted-text
role="ref"}

Sets the transform matrix for an area shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_space}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_space**(area: `RID<class_RID>`{.interpreted-text role="ref"},
space: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_space>`{.interpreted-text
role="ref"}

Assigns a space to the area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_area_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**area_set_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_area_set_transform>`{.interpreted-text
role="ref"}

Sets the transform matrix for an area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_add_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, excepted_body:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_add_collision_exception>`{.interpreted-text
role="ref"}

Adds a body to the list of bodies exempt from collisions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_add_constant_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_constant_central_force**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_add_constant_central_force>`{.interpreted-text
role="ref"}

Adds a constant directional force without affecting rotation that keeps
being applied over time until cleared with
`body_set_constant_force(body, Vector3(0, 0, 0))`.

This is equivalent to using
`body_add_constant_force()<class_PhysicsServer3D_method_body_add_constant_force>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_add_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_PhysicsServer3D_method_body_add_constant_force>`{.interpreted-text
role="ref"}

Adds a constant positioned force to the body that keeps being applied
over time until cleared with
`body_set_constant_force(body, Vector3(0, 0, 0))`.

`position` is the offset from the body origin in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_add_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_add_constant_torque>`{.interpreted-text
role="ref"}

Adds a constant rotational force without affecting position that keeps
being applied over time until cleared with
`body_set_constant_torque(body, Vector3(0, 0, 0))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_add_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_add_shape**(body: `RID<class_RID>`{.interpreted-text role="ref"},
shape: `RID<class_RID>`{.interpreted-text role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} =
Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_PhysicsServer3D_method_body_add_shape>`{.interpreted-text
role="ref"}

Adds a shape to the body, along with a transform matrix. Shapes are
usually referenced by their index, so you should track which shape has a
given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_apply_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_central_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_apply_central_force>`{.interpreted-text
role="ref"}

Applies a directional force without affecting rotation. A force is time
dependent and meant to be applied every physics update.

This is equivalent to using
`body_apply_force()<class_PhysicsServer3D_method_body_apply_force>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_central_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_apply_central_impulse>`{.interpreted-text
role="ref"}

Applies a directional impulse without affecting rotation.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

This is equivalent to using
`body_apply_impulse()<class_PhysicsServer3D_method_body_apply_impulse>`{.interpreted-text
role="ref"} at the body\'s center of mass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_apply_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_PhysicsServer3D_method_body_apply_force>`{.interpreted-text
role="ref"}

Applies a positioned force to the body. A force is time dependent and
meant to be applied every physics update.

`position` is the offset from the body origin in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_apply_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"} = Vector3(0, 0, 0))
`🔗<class_PhysicsServer3D_method_body_apply_impulse>`{.interpreted-text
role="ref"}

Applies a positioned impulse to the body.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

`position` is the offset from the body origin in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_apply_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_apply_torque>`{.interpreted-text
role="ref"}

Applies a rotational force without affecting position. A force is time
dependent and meant to be applied every physics update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_apply_torque_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_apply_torque_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_apply_torque_impulse>`{.interpreted-text
role="ref"}

Applies a rotational impulse to the body without affecting the position.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_attach_object_instance_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_attach_object_instance_id**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_attach_object_instance_id>`{.interpreted-text
role="ref"}

Assigns the area to a descendant of
`Object<class_Object>`{.interpreted-text role="ref"}, so it can exist in
the node tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_clear_shapes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_clear_shapes**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_clear_shapes>`{.interpreted-text
role="ref"}

Removes all shapes from a body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **body_create**()
`🔗<class_PhysicsServer3D_method_body_create>`{.interpreted-text
role="ref"}

Creates a 3D body object in the physics server, and returns the
`RID<class_RID>`{.interpreted-text role="ref"} that identifies it. The
default settings for the created area include a collision layer and mask
set to `1`, and body mode set to
`BODY_MODE_RIGID<class_PhysicsServer3D_constant_BODY_MODE_RIGID>`{.interpreted-text
role="ref"}.

Use
`body_add_shape()<class_PhysicsServer3D_method_body_add_shape>`{.interpreted-text
role="ref"} to add shapes to it, use
`body_set_state()<class_PhysicsServer3D_method_body_set_state>`{.interpreted-text
role="ref"} to set its transform, and use
`body_set_space()<class_PhysicsServer3D_method_body_set_space>`{.interpreted-text
role="ref"} to add the body to a space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_collision_layer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_collision_layer**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_collision_layer>`{.interpreted-text
role="ref"}

Returns the physics layer or layers a body belongs to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_collision_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_collision_mask**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_collision_mask>`{.interpreted-text
role="ref"}

Returns the physics layer or layers a body can collide with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_collision_priority}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**body_get_collision_priority**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_collision_priority>`{.interpreted-text
role="ref"}

Returns the body\'s collision priority.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_constant_force}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**body_get_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_constant_force>`{.interpreted-text
role="ref"}

Returns the body\'s total constant positional forces applied during each
physics update.

See
`body_add_constant_force()<class_PhysicsServer3D_method_body_add_constant_force>`{.interpreted-text
role="ref"} and
`body_add_constant_central_force()<class_PhysicsServer3D_method_body_add_constant_central_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_constant_torque}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**body_get_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_constant_torque>`{.interpreted-text
role="ref"}

Returns the body\'s total constant rotational forces applied during each
physics update.

See
`body_add_constant_torque()<class_PhysicsServer3D_method_body_add_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_direct_state}
::: rst-class
classref-method
:::
::::

`PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>`{.interpreted-text
role="ref"} **body_get_direct_state**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_get_direct_state>`{.interpreted-text
role="ref"}

Returns the
`PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>`{.interpreted-text
role="ref"} of the body. Returns `null` if the body is destroyed or
removed from the physics space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_max_contacts_reported}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_max_contacts_reported**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_max_contacts_reported>`{.interpreted-text
role="ref"}

Returns the maximum contacts that can be reported. See
`body_set_max_contacts_reported()<class_PhysicsServer3D_method_body_set_max_contacts_reported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_mode}
::: rst-class
classref-method
:::
::::

`BodyMode<enum_PhysicsServer3D_BodyMode>`{.interpreted-text role="ref"}
**body_get_mode**(body: `RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_mode>`{.interpreted-text
role="ref"}

Returns the body mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_object_instance_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_object_instance_id**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_object_instance_id>`{.interpreted-text
role="ref"}

Gets the instance ID of the object the area is assigned to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_param}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**body_get_param**(body: `RID<class_RID>`{.interpreted-text role="ref"},
param:
`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_param>`{.interpreted-text
role="ref"}

Returns the value of a body parameter. A list of available parameters is
on the
`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_shape}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **body_get_shape**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, shape_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_shape>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the nth
shape of a body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**body_get_shape_count**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_shape_count>`{.interpreted-text
role="ref"}

Returns the number of shapes assigned to a body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_shape_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**body_get_shape_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_shape_transform>`{.interpreted-text
role="ref"}

Returns the transform matrix of a body shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_space}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **body_get_space**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_space>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the space
assigned to a body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_get_state}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**body_get_state**(body: `RID<class_RID>`{.interpreted-text role="ref"},
state: `BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_get_state>`{.interpreted-text
role="ref"}

Returns a body state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_is_axis_locked}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_is_axis_locked**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, axis:
`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_is_axis_locked>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_body_is_continuous_collision_detection_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_is_continuous_collision_detection_enabled**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_is_continuous_collision_detection_enabled>`{.interpreted-text
role="ref"}

If `true`, the continuous collision detection mode is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_is_omitting_force_integration}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_is_omitting_force_integration**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_body_is_omitting_force_integration>`{.interpreted-text
role="ref"}

Returns `true` if the body is omitting the standard force integration.
See
`body_set_omit_force_integration()<class_PhysicsServer3D_method_body_set_omit_force_integration>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_remove_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_remove_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, excepted_body:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_remove_collision_exception>`{.interpreted-text
role="ref"}

Removes a body from the list of bodies exempt from collisions.

Continuous collision detection tries to predict where a moving body will
collide, instead of moving it and correcting its movement if it
collided.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_remove_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_remove_shape**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_remove_shape>`{.interpreted-text
role="ref"}

Removes a shape from a body. The shape is not deleted, so it can be
reused afterwards.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_reset_mass_properties}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_reset_mass_properties**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_reset_mass_properties>`{.interpreted-text
role="ref"}

Restores the default inertia and center of mass based on shapes to
cancel any custom values previously set using
`body_set_param()<class_PhysicsServer3D_method_body_set_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_axis_lock}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_axis_lock**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, axis:
`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"},
lock: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_axis_lock>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_body_set_axis_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_axis_velocity**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, axis_velocity: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_axis_velocity>`{.interpreted-text
role="ref"}

Sets an axis velocity. The velocity in the given vector axis will be set
as the given vector length. This is useful for jumping behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_collision_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_collision_layer**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_collision_layer>`{.interpreted-text
role="ref"}

Sets the physics layer or layers a body belongs to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_collision_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_collision_mask**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_collision_mask>`{.interpreted-text
role="ref"}

Sets the physics layer or layers a body can collide with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_collision_priority}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_collision_priority**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, priority: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_collision_priority>`{.interpreted-text
role="ref"}

Sets the body\'s collision priority.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_constant_force>`{.interpreted-text
role="ref"}

Sets the body\'s total constant positional forces applied during each
physics update.

See
`body_add_constant_force()<class_PhysicsServer3D_method_body_add_constant_force>`{.interpreted-text
role="ref"} and
`body_add_constant_central_force()<class_PhysicsServer3D_method_body_add_constant_central_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_constant_torque>`{.interpreted-text
role="ref"}

Sets the body\'s total constant rotational forces applied during each
physics update.

See
`body_add_constant_torque()<class_PhysicsServer3D_method_body_add_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_enable_continuous_collision_detection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_enable_continuous_collision_detection**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_enable_continuous_collision_detection>`{.interpreted-text
role="ref"}

If `true`, the continuous collision detection mode is enabled.

Continuous collision detection tries to predict where a moving body will
collide, instead of moving it and correcting its movement if it
collided.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_force_integration_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_force_integration_callback**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, callable:
`Callable<class_Callable>`{.interpreted-text role="ref"}, userdata:
`Variant<class_Variant>`{.interpreted-text role="ref"} = null)
`🔗<class_PhysicsServer3D_method_body_set_force_integration_callback>`{.interpreted-text
role="ref"}

Sets the body\'s custom force integration callback function to
`callable`. Use an empty `Callable<class_Callable>`{.interpreted-text
role="ref"} (`Callable()`) to clear the custom callback.

The function `callable` will be called every physics tick, before the
standard force integration (see
`body_set_omit_force_integration()<class_PhysicsServer3D_method_body_set_omit_force_integration>`{.interpreted-text
role="ref"}). It can be used for example to update the body\'s linear
and angular velocity based on contact with other bodies.

If `userdata` is not `null`, the function `callable` must take the
following two parameters:

1.  `state`: a
    `PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>`{.interpreted-text
    role="ref"}, used to retrieve and modify the body\'s state,
2.  `userdata`: a `Variant<class_Variant>`{.interpreted-text
    role="ref"}; its value will be the `userdata` passed into this
    method.

If `userdata` is `null`, then `callable` must take only the `state`
parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_max_contacts_reported}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_max_contacts_reported**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, amount:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_max_contacts_reported>`{.interpreted-text
role="ref"}

Sets the maximum contacts to report. Bodies can keep a log of the
contacts with other bodies. This is enabled by setting the maximum
number of contacts reported to a number greater than 0.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_mode**(body: `RID<class_RID>`{.interpreted-text role="ref"},
mode: `BodyMode<enum_PhysicsServer3D_BodyMode>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_mode>`{.interpreted-text
role="ref"}

Sets the body mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_omit_force_integration}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_omit_force_integration**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_omit_force_integration>`{.interpreted-text
role="ref"}

Sets whether the body omits the standard force integration. If `enable`
is `true`, the body will not automatically use applied forces, torques,
and damping to update the body\'s linear and angular velocity. In this
case,
`body_set_force_integration_callback()<class_PhysicsServer3D_method_body_set_force_integration_callback>`{.interpreted-text
role="ref"} can be used to manually update the linear and angular
velocity instead.

This method is called when the property
`RigidBody3D.custom_integrator<class_RigidBody3D_property_custom_integrator>`{.interpreted-text
role="ref"} is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_param**(body: `RID<class_RID>`{.interpreted-text role="ref"},
param:
`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_param>`{.interpreted-text
role="ref"}

Sets a body parameter. A list of available parameters is on the
`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"} constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_ray_pickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_ray_pickable**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_ray_pickable>`{.interpreted-text
role="ref"}

Sets the body pickable with rays if `enable` is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_shape**(body: `RID<class_RID>`{.interpreted-text role="ref"},
shape_idx: `int<class_int>`{.interpreted-text role="ref"}, shape:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_shape>`{.interpreted-text
role="ref"}

Substitutes a given body shape by another. The old shape is selected by
its index, the new one by its `RID<class_RID>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_shape_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_shape_disabled**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_shape_disabled>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_body_set_shape_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_shape_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_shape_transform>`{.interpreted-text
role="ref"}

Sets the transform matrix for a body shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_space}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_space**(body: `RID<class_RID>`{.interpreted-text role="ref"},
space: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_space>`{.interpreted-text
role="ref"}

Assigns a space to the body (see
`space_create()<class_PhysicsServer3D_method_space_create>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_state}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_state**(body: `RID<class_RID>`{.interpreted-text role="ref"},
state: `BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_state>`{.interpreted-text
role="ref"}

Sets a body state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_set_state_sync_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**body_set_state_sync_callback**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_body_set_state_sync_callback>`{.interpreted-text
role="ref"}

Sets the body\'s state synchronization callback function to `callable`.
Use an empty `Callable<class_Callable>`{.interpreted-text role="ref"}
(`Callable()`) to clear the callback.

The function `callable` will be called every physics frame, assuming
that the body was active during the previous physics tick, and can be
used to fetch the latest state from the physics server.

The function `callable` must take the following parameters:

1.  `state`: a
    `PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>`{.interpreted-text
    role="ref"}, used to retrieve the body\'s state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_body_test_motion}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_test_motion**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, parameters:
`PhysicsTestMotionParameters3D<class_PhysicsTestMotionParameters3D>`{.interpreted-text
role="ref"}, result:
`PhysicsTestMotionResult3D<class_PhysicsTestMotionResult3D>`{.interpreted-text
role="ref"} = null)
`🔗<class_PhysicsServer3D_method_body_test_motion>`{.interpreted-text
role="ref"}

Returns `true` if a collision would result from moving along a motion
vector from a given point in space.
`PhysicsTestMotionParameters3D<class_PhysicsTestMotionParameters3D>`{.interpreted-text
role="ref"} is passed to set motion parameters.
`PhysicsTestMotionResult3D<class_PhysicsTestMotionResult3D>`{.interpreted-text
role="ref"} can be passed to return additional information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_box_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **box_shape_create**()
`🔗<class_PhysicsServer3D_method_box_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_capsule_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**capsule_shape_create**()
`🔗<class_PhysicsServer3D_method_capsule_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_concave_polygon_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**concave_polygon_shape_create**()
`🔗<class_PhysicsServer3D_method_concave_polygon_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_cone_twist_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**cone_twist_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_cone_twist_joint_get_param>`{.interpreted-text
role="ref"}

Gets a cone twist joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_cone_twist_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cone_twist_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_cone_twist_joint_set_param>`{.interpreted-text
role="ref"}

Sets a cone twist joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_convex_polygon_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**convex_polygon_shape_create**()
`🔗<class_PhysicsServer3D_method_convex_polygon_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_custom_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **custom_shape_create**()
`🔗<class_PhysicsServer3D_method_custom_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_cylinder_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**cylinder_shape_create**()
`🔗<class_PhysicsServer3D_method_cylinder_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_free_rid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**free_rid**(rid: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_free_rid>`{.interpreted-text
role="ref"}

Destroys any of the objects created by PhysicsServer3D. If the
`RID<class_RID>`{.interpreted-text role="ref"} passed is not one of the
objects that can be created by PhysicsServer3D, an error will be sent to
the console.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_generic_6dof_joint_get_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**generic_6dof_joint_get_flag**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}, flag:
`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_generic_6dof_joint_get_flag>`{.interpreted-text
role="ref"}

Returns the value of a generic 6DOF joint flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_generic_6dof_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**generic_6dof_joint_get_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}, param:
`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_generic_6dof_joint_get_param>`{.interpreted-text
role="ref"}

Returns the value of a generic 6DOF joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_generic_6dof_joint_set_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**generic_6dof_joint_set_flag**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}, flag:
`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_generic_6dof_joint_set_flag>`{.interpreted-text
role="ref"}

Sets the value of a given generic 6DOF joint flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_generic_6dof_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**generic_6dof_joint_set_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}, param:
`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_generic_6dof_joint_set_param>`{.interpreted-text
role="ref"}

Sets the value of a given generic 6DOF joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_get_process_info}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_process_info**(process_info:
`ProcessInfo<enum_PhysicsServer3D_ProcessInfo>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_get_process_info>`{.interpreted-text
role="ref"}

Returns the value of a physics engine state specified by `process_info`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_heightmap_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**heightmap_shape_create**()
`🔗<class_PhysicsServer3D_method_heightmap_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_hinge_joint_get_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**hinge_joint_get_flag**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, flag:
`HingeJointFlag<enum_PhysicsServer3D_HingeJointFlag>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_hinge_joint_get_flag>`{.interpreted-text
role="ref"}

Gets a hinge joint flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_hinge_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**hinge_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_hinge_joint_get_param>`{.interpreted-text
role="ref"}

Gets a hinge joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_hinge_joint_set_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**hinge_joint_set_flag**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, flag:
`HingeJointFlag<enum_PhysicsServer3D_HingeJointFlag>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_hinge_joint_set_flag>`{.interpreted-text
role="ref"}

Sets a hinge joint flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_hinge_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**hinge_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_hinge_joint_set_param>`{.interpreted-text
role="ref"}

Sets a hinge joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_joint_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_clear**(joint: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_joint_clear>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_joint_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **joint_create**()
`🔗<class_PhysicsServer3D_method_joint_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_joint_disable_collisions_between_bodies}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_disable_collisions_between_bodies**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, disable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_joint_disable_collisions_between_bodies>`{.interpreted-text
role="ref"}

Sets whether the bodies attached to the
`Joint3D<class_Joint3D>`{.interpreted-text role="ref"} will collide with
each other.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_joint_get_solver_priority}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**joint_get_solver_priority**(joint: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_joint_get_solver_priority>`{.interpreted-text
role="ref"}

Gets the priority value of the Joint3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_joint_get_type}
::: rst-class
classref-method
:::
::::

`JointType<enum_PhysicsServer3D_JointType>`{.interpreted-text
role="ref"} **joint_get_type**(joint: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_joint_get_type>`{.interpreted-text
role="ref"}

Returns the type of the Joint3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_joint_is_disabled_collisions_between_bodies}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**joint_is_disabled_collisions_between_bodies**(joint:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_joint_is_disabled_collisions_between_bodies>`{.interpreted-text
role="ref"}

Returns whether the bodies attached to the
`Joint3D<class_Joint3D>`{.interpreted-text role="ref"} will collide with
each other.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_joint_make_cone_twist}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_make_cone_twist**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_A: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, body_B: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_B: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_joint_make_cone_twist>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_joint_make_generic_6dof}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_make_generic_6dof**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_A: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, body_B: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_B: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_joint_make_generic_6dof>`{.interpreted-text
role="ref"}

Make the joint a generic six degrees of freedom (6DOF) joint. Use
`generic_6dof_joint_set_flag()<class_PhysicsServer3D_method_generic_6dof_joint_set_flag>`{.interpreted-text
role="ref"} and
`generic_6dof_joint_set_param()<class_PhysicsServer3D_method_generic_6dof_joint_set_param>`{.interpreted-text
role="ref"} to set the joint\'s flags and parameters respectively.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_joint_make_hinge}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_make_hinge**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
hinge_A: `Transform3D<class_Transform3D>`{.interpreted-text role="ref"},
body_B: `RID<class_RID>`{.interpreted-text role="ref"}, hinge_B:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_joint_make_hinge>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_joint_make_pin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_make_pin**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
local_A: `Vector3<class_Vector3>`{.interpreted-text role="ref"}, body_B:
`RID<class_RID>`{.interpreted-text role="ref"}, local_B:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_joint_make_pin>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_joint_make_slider}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_make_slider**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_A: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, body_B: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_B: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_joint_make_slider>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_joint_set_solver_priority}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**joint_set_solver_priority**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, priority: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_joint_set_solver_priority>`{.interpreted-text
role="ref"}

Sets the priority value of the Joint3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_pin_joint_get_local_a}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**pin_joint_get_local_a**(joint: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_pin_joint_get_local_a>`{.interpreted-text
role="ref"}

Returns position of the joint in the local space of body a of the joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_pin_joint_get_local_b}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**pin_joint_get_local_b**(joint: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_pin_joint_get_local_b>`{.interpreted-text
role="ref"}

Returns position of the joint in the local space of body b of the joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_pin_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**pin_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`PinJointParam<enum_PhysicsServer3D_PinJointParam>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_pin_joint_get_param>`{.interpreted-text
role="ref"}

Gets a pin joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_pin_joint_set_local_a}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**pin_joint_set_local_a**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, local_A: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_pin_joint_set_local_a>`{.interpreted-text
role="ref"}

Sets position of the joint in the local space of body a of the joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_pin_joint_set_local_b}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**pin_joint_set_local_b**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, local_B: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_pin_joint_set_local_b>`{.interpreted-text
role="ref"}

Sets position of the joint in the local space of body b of the joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_pin_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**pin_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`PinJointParam<enum_PhysicsServer3D_PinJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_pin_joint_set_param>`{.interpreted-text
role="ref"}

Sets a pin joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_separation_ray_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**separation_ray_shape_create**()
`🔗<class_PhysicsServer3D_method_separation_ray_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_set_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_active**(active: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_set_active>`{.interpreted-text
role="ref"}

Activates or deactivates the 3D physics engine.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_shape_get_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**shape_get_data**(shape: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_shape_get_data>`{.interpreted-text
role="ref"}

Returns the shape data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_shape_get_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shape_get_margin**(shape: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_shape_get_margin>`{.interpreted-text
role="ref"}

Returns the collision margin for the shape.

\*\*Note:\*\* This is not used in Godot Physics, so will always return
`0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_shape_get_type}
::: rst-class
classref-method
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **shape_get_type**(shape: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_shape_get_type>`{.interpreted-text
role="ref"}

Returns the type of shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_shape_set_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shape_set_data**(shape: `RID<class_RID>`{.interpreted-text
role="ref"}, data: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_shape_set_data>`{.interpreted-text
role="ref"}

Sets the shape data that defines its shape and size. The data to be
passed depends on the kind of shape created
`shape_get_type()<class_PhysicsServer3D_method_shape_get_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_shape_set_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shape_set_margin**(shape: `RID<class_RID>`{.interpreted-text
role="ref"}, margin: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_shape_set_margin>`{.interpreted-text
role="ref"}

Sets the collision margin for the shape.

\*\*Note:\*\* This is not used in Godot Physics.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_slider_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**slider_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_slider_joint_get_param>`{.interpreted-text
role="ref"}

Gets a slider joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_slider_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**slider_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_slider_joint_set_param>`{.interpreted-text
role="ref"}

Gets a slider joint parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_add_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_add_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, body_b:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_add_collision_exception>`{.interpreted-text
role="ref"}

Adds the given body to the list of bodies exempt from collisions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_apply_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_apply_central_force**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_apply_central_force>`{.interpreted-text
role="ref"}

Distributes and applies a force to all points. A force is time dependent
and meant to be applied every physics update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_apply_central_impulse**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_apply_central_impulse>`{.interpreted-text
role="ref"}

Distributes and applies an impulse to all points.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_apply_point_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_apply_point_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, point_index: `int<class_int>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_apply_point_force>`{.interpreted-text
role="ref"}

Applies a force to a point. A force is time dependent and meant to be
applied every physics update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_apply_point_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_apply_point_impulse**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, point_index:
`int<class_int>`{.interpreted-text role="ref"}, impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_apply_point_impulse>`{.interpreted-text
role="ref"}

Applies an impulse to a point.

An impulse is time-independent! Applying an impulse every frame would
result in a framerate-dependent force. For this reason, it should only
be used when simulating one-time impacts (use the \"\_force\" functions
otherwise).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **soft_body_create**()
`🔗<class_PhysicsServer3D_method_soft_body_create>`{.interpreted-text
role="ref"}

Creates a new soft body and returns its internal
`RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_bounds}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"}
**soft_body_get_bounds**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_bounds>`{.interpreted-text
role="ref"}

Returns the bounds of the given soft body in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_collision_layer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**soft_body_get_collision_layer**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_collision_layer>`{.interpreted-text
role="ref"}

Returns the physics layer or layers that the given soft body belongs to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_collision_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**soft_body_get_collision_mask**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_collision_mask>`{.interpreted-text
role="ref"}

Returns the physics layer or layers that the given soft body can collide
with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_damping_coefficient}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**soft_body_get_damping_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_damping_coefficient>`{.interpreted-text
role="ref"}

Returns the damping coefficient of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_drag_coefficient}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**soft_body_get_drag_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_drag_coefficient>`{.interpreted-text
role="ref"}

Returns the drag coefficient of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_linear_stiffness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**soft_body_get_linear_stiffness**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_linear_stiffness>`{.interpreted-text
role="ref"}

Returns the linear stiffness of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_point_global_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**soft_body_get_point_global_position**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, point_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_point_global_position>`{.interpreted-text
role="ref"}

Returns the current position of the given soft body point in global
coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_pressure_coefficient}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**soft_body_get_pressure_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_pressure_coefficient>`{.interpreted-text
role="ref"}

Returns the pressure coefficient of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_shrinking_factor}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**soft_body_get_shrinking_factor**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_shrinking_factor>`{.interpreted-text
role="ref"}

Returns the shrinking factor of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_simulation_precision}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**soft_body_get_simulation_precision**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_simulation_precision>`{.interpreted-text
role="ref"}

Returns the simulation precision of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_space}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**soft_body_get_space**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_space>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the space
assigned to the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_state}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**soft_body_get_state**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, state:
`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_state>`{.interpreted-text
role="ref"}

Returns the given soft body state.

\*\*Note:\*\* Godot\'s default physics implementation does not support
`BODY_STATE_LINEAR_VELOCITY<class_PhysicsServer3D_constant_BODY_STATE_LINEAR_VELOCITY>`{.interpreted-text
role="ref"},
`BODY_STATE_ANGULAR_VELOCITY<class_PhysicsServer3D_constant_BODY_STATE_ANGULAR_VELOCITY>`{.interpreted-text
role="ref"},
`BODY_STATE_SLEEPING<class_PhysicsServer3D_constant_BODY_STATE_SLEEPING>`{.interpreted-text
role="ref"}, or
`BODY_STATE_CAN_SLEEP<class_PhysicsServer3D_constant_BODY_STATE_CAN_SLEEP>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_get_total_mass}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**soft_body_get_total_mass**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_get_total_mass>`{.interpreted-text
role="ref"}

Returns the total mass assigned to the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_is_point_pinned}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**soft_body_is_point_pinned**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, point_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_soft_body_is_point_pinned>`{.interpreted-text
role="ref"}

Returns whether the given soft body point is pinned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_move_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_move_point**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, point_index: `int<class_int>`{.interpreted-text
role="ref"}, global_position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_move_point>`{.interpreted-text
role="ref"}

Moves the given soft body point to a position in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_pin_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_pin_point**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, point_index: `int<class_int>`{.interpreted-text
role="ref"}, pin: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_pin_point>`{.interpreted-text
role="ref"}

Pins or unpins the given soft body point based on the value of `pin`.

\*\*Note:\*\* Pinning a point effectively makes it kinematic, preventing
it from being affected by forces, but you can still move it using
`soft_body_move_point()<class_PhysicsServer3D_method_soft_body_move_point>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_remove_all_pinned_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_remove_all_pinned_points**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_remove_all_pinned_points>`{.interpreted-text
role="ref"}

Unpins all points of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_remove_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_remove_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, body_b:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_remove_collision_exception>`{.interpreted-text
role="ref"}

Removes the given body from the list of bodies exempt from collisions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_collision_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_collision_layer**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, layer:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_collision_layer>`{.interpreted-text
role="ref"}

Sets the physics layer or layers the given soft body belongs to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_collision_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_collision_mask**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_collision_mask>`{.interpreted-text
role="ref"}

Sets the physics layer or layers the given soft body can collide with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_damping_coefficient}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_damping_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, damping_coefficient:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_damping_coefficient>`{.interpreted-text
role="ref"}

Sets the damping coefficient of the given soft body. Higher values will
slow down the body more noticeably when forces are applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_drag_coefficient}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_drag_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, drag_coefficient:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_drag_coefficient>`{.interpreted-text
role="ref"}

Sets the drag coefficient of the given soft body. Higher values increase
this body\'s air resistance.

\*\*Note:\*\* This value is currently unused by Godot\'s default physics
implementation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_linear_stiffness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_linear_stiffness**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, stiffness:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_linear_stiffness>`{.interpreted-text
role="ref"}

Sets the linear stiffness of the given soft body. Higher values will
result in a stiffer body, while lower values will increase the body\'s
ability to bend. The value can be between `0.0` and `1.0` (inclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_mesh**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, mesh: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_mesh>`{.interpreted-text
role="ref"}

Sets the mesh of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_pressure_coefficient}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_pressure_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, pressure_coefficient:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_pressure_coefficient>`{.interpreted-text
role="ref"}

Sets the pressure coefficient of the given soft body. Simulates pressure
build-up from inside this body. Higher values increase the strength of
this effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_ray_pickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_ray_pickable**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_ray_pickable>`{.interpreted-text
role="ref"}

Sets whether the given soft body will be pickable when using object
picking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_shrinking_factor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_shrinking_factor**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, shrinking_factor:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_shrinking_factor>`{.interpreted-text
role="ref"}

Sets the shrinking factor of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_simulation_precision}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_simulation_precision**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, simulation_precision:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_simulation_precision>`{.interpreted-text
role="ref"}

Sets the simulation precision of the given soft body. Increasing this
value will improve the resulting simulation, but can affect performance.
Use with care.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_space}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_space**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, space: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_space>`{.interpreted-text
role="ref"}

Assigns a space to the given soft body (see
`space_create()<class_PhysicsServer3D_method_space_create>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_state}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_state**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, state:
`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"}, variant: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_state>`{.interpreted-text
role="ref"}

Sets the given body state for the given body.

\*\*Note:\*\* Godot\'s default physics implementation does not support
`BODY_STATE_LINEAR_VELOCITY<class_PhysicsServer3D_constant_BODY_STATE_LINEAR_VELOCITY>`{.interpreted-text
role="ref"},
`BODY_STATE_ANGULAR_VELOCITY<class_PhysicsServer3D_constant_BODY_STATE_ANGULAR_VELOCITY>`{.interpreted-text
role="ref"},
`BODY_STATE_SLEEPING<class_PhysicsServer3D_constant_BODY_STATE_SLEEPING>`{.interpreted-text
role="ref"}, or
`BODY_STATE_CAN_SLEEP<class_PhysicsServer3D_constant_BODY_STATE_CAN_SLEEP>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_total_mass}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_total_mass**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, total_mass: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_total_mass>`{.interpreted-text
role="ref"}

Sets the total mass for the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_set_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_set_transform>`{.interpreted-text
role="ref"}

Sets the global transform of the given soft body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_soft_body_update_rendering_server}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**soft_body_update_rendering_server**(body:
`RID<class_RID>`{.interpreted-text role="ref"},
rendering_server_handler:
`PhysicsServer3DRenderingServerHandler<class_PhysicsServer3DRenderingServerHandler>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3D_method_soft_body_update_rendering_server>`{.interpreted-text
role="ref"}

Requests that the physics server updates the rendering server with the
latest positions of the given soft body\'s points through the
`rendering_server_handler` interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_space_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **space_create**()
`🔗<class_PhysicsServer3D_method_space_create>`{.interpreted-text
role="ref"}

Creates a space. A space is a collection of parameters for the physics
engine that can be assigned to an area or a body. It can be assigned to
an area with
`area_set_space()<class_PhysicsServer3D_method_area_set_space>`{.interpreted-text
role="ref"}, or to a body with
`body_set_space()<class_PhysicsServer3D_method_body_set_space>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_space_get_direct_state}
::: rst-class
classref-method
:::
::::

`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`{.interpreted-text
role="ref"} **space_get_direct_state**(space:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_space_get_direct_state>`{.interpreted-text
role="ref"}

Returns the state of a space, a
`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`{.interpreted-text
role="ref"}. This object can be used to make collision/intersection
queries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_space_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**space_get_param**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_space_get_param>`{.interpreted-text
role="ref"}

Returns the value of a space parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_space_is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**space_is_active**(space: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3D_method_space_is_active>`{.interpreted-text
role="ref"}

Returns whether the space is active.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_space_set_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**space_set_active**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, active: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_space_set_active>`{.interpreted-text
role="ref"}

Marks a space as active. It will not have an effect, unless it is
assigned to an area or body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_space_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**space_set_param**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3D_method_space_set_param>`{.interpreted-text
role="ref"}

Sets the value for a space parameter. A list of available parameters is
on the
`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"} constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3D_method_sphere_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **sphere_shape_create**()
`🔗<class_PhysicsServer3D_method_sphere_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3D_method_world_boundary_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**world_boundary_shape_create**()
`🔗<class_PhysicsServer3D_method_world_boundary_shape_create>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
