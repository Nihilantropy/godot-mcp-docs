github_url
:   hide

# CharacterBody2D {#class_CharacterBody2D}

**Inherits:** `PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text
role="ref"} **\<**
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} **\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D physics body specialized for characters moved by script.

::: rst-class
classref-introduction-group
:::

## Description

**CharacterBody2D** is a specialized class for physics bodies that are
meant to be user-controlled. They are not affected by physics at all,
but they affect other physics bodies in their path. They are mainly used
to provide high-level API to move objects with wall and slope detection
(`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"} method) in addition to the general collision detection
provided by
`PhysicsBody2D.move_and_collide()<class_PhysicsBody2D_method_move_and_collide>`{.interpreted-text
role="ref"}. This makes it useful for highly configurable physics bodies
that must move in specific ways and collide with the world, as is often
the case with user-controlled characters.

For game objects that don\'t require complex movement or collision
detection, such as moving platforms,
`AnimatableBody2D<class_AnimatableBody2D>`{.interpreted-text role="ref"}
is simpler to configure.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Kinematic character (2D) <../tutorials/physics/kinematic_character_2d>`{.interpreted-text
  role="doc"}
- `Using CharacterBody2D <../tutorials/physics/using_character_body_2d>`{.interpreted-text
  role="doc"}
- [2D Kinematic Character
  Demo](https://godotengine.org/asset-library/asset/2719)
- [2D Platformer Demo](https://godotengine.org/asset-library/asset/2727)

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

:::: {#enum_CharacterBody2D_MotionMode}
::: rst-class
classref-enumeration
:::
::::

enum **MotionMode**:
`🔗<enum_CharacterBody2D_MotionMode>`{.interpreted-text role="ref"}

:::: {#class_CharacterBody2D_constant_MOTION_MODE_GROUNDED}
::: rst-class
classref-enumeration-constant
:::
::::

`MotionMode<enum_CharacterBody2D_MotionMode>`{.interpreted-text
role="ref"} **MOTION_MODE_GROUNDED** = `0`

Apply when notions of walls, ceiling and floor are relevant. In this
mode the body motion will react to slopes (acceleration/slowdown). This
mode is suitable for sided games like platformers.

:::: {#class_CharacterBody2D_constant_MOTION_MODE_FLOATING}
::: rst-class
classref-enumeration-constant
:::
::::

`MotionMode<enum_CharacterBody2D_MotionMode>`{.interpreted-text
role="ref"} **MOTION_MODE_FLOATING** = `1`

Apply when there is no notion of floor or ceiling. All collisions will
be reported as `on_wall`. In this mode, when you slide, the speed will
always be constant. This mode is suitable for top-down games.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CharacterBody2D_PlatformOnLeave}
::: rst-class
classref-enumeration
:::
::::

enum **PlatformOnLeave**:
`🔗<enum_CharacterBody2D_PlatformOnLeave>`{.interpreted-text role="ref"}

:::: {#class_CharacterBody2D_constant_PLATFORM_ON_LEAVE_ADD_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`PlatformOnLeave<enum_CharacterBody2D_PlatformOnLeave>`{.interpreted-text
role="ref"} **PLATFORM_ON_LEAVE_ADD_VELOCITY** = `0`

Add the last platform velocity to the
`velocity<class_CharacterBody2D_property_velocity>`{.interpreted-text
role="ref"} when you leave a moving platform.

:::: {#class_CharacterBody2D_constant_PLATFORM_ON_LEAVE_ADD_UPWARD_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`PlatformOnLeave<enum_CharacterBody2D_PlatformOnLeave>`{.interpreted-text
role="ref"} **PLATFORM_ON_LEAVE_ADD_UPWARD_VELOCITY** = `1`

Add the last platform velocity to the
`velocity<class_CharacterBody2D_property_velocity>`{.interpreted-text
role="ref"} when you leave a moving platform, but any downward motion is
ignored. It\'s useful to keep full jump height even when the platform is
moving down.

:::: {#class_CharacterBody2D_constant_PLATFORM_ON_LEAVE_DO_NOTHING}
::: rst-class
classref-enumeration-constant
:::
::::

`PlatformOnLeave<enum_CharacterBody2D_PlatformOnLeave>`{.interpreted-text
role="ref"} **PLATFORM_ON_LEAVE_DO_NOTHING** = `2`

Do nothing when leaving a platform.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CharacterBody2D_property_floor_block_on_wall}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **floor_block_on_wall**
= `true`
`🔗<class_CharacterBody2D_property_floor_block_on_wall>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_floor_block_on_wall_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_floor_block_on_wall_enabled**()

If `true`, the body will be able to move on the floor only. This option
avoids to be able to walk on walls, it will however allow to slide down
along them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_floor_constant_speed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**floor_constant_speed** = `false`
`🔗<class_CharacterBody2D_property_floor_constant_speed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_floor_constant_speed_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_floor_constant_speed_enabled**()

If `false` (by default), the body will move faster on downward slopes
and slower on upward slopes.

If `true`, the body will always move at the same speed on the ground no
matter the slope. Note that you need to use
`floor_snap_length<class_CharacterBody2D_property_floor_snap_length>`{.interpreted-text
role="ref"} to stick along a downward slope at constant speed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_floor_max_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **floor_max_angle** =
`0.7853982`
`🔗<class_CharacterBody2D_property_floor_max_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_floor_max_angle**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_floor_max_angle**()

Maximum angle (in radians) where a slope is still considered a floor (or
a ceiling), rather than a wall, when calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. The default value equals 45 degrees.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_floor_snap_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **floor_snap_length**
= `1.0`
`🔗<class_CharacterBody2D_property_floor_snap_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_floor_snap_length**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_floor_snap_length**()

Sets a snapping distance. When set to a value different from `0.0`, the
body is kept attached to slopes when calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. The snapping vector is determined by the given distance
along the opposite direction of the
`up_direction<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"}.

As long as the snapping vector is in contact with the ground and the
body moves against
`up_direction<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"}, the body will remain attached to the surface. Snapping is
not applied if the body moves along
`up_direction<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"}, meaning it contains vertical rising velocity, so it will be
able to detach from the ground when jumping or when the body is pushed
up by something. If you want to apply a snap without taking into account
the velocity, use
`apply_floor_snap()<class_CharacterBody2D_method_apply_floor_snap>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_floor_stop_on_slope}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **floor_stop_on_slope**
= `true`
`🔗<class_CharacterBody2D_property_floor_stop_on_slope>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_floor_stop_on_slope_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_floor_stop_on_slope_enabled**()

If `true`, the body will not slide on slopes when calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"} when the body is standing still.

If `false`, the body will slide on floor\'s slopes when
`velocity<class_CharacterBody2D_property_velocity>`{.interpreted-text
role="ref"} applies a downward force.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_max_slides}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_slides** = `4`
`🔗<class_CharacterBody2D_property_max_slides>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_slides**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_slides**()

Maximum number of times the body can change direction before it stops
when calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. Must be greater than zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_motion_mode}
::: rst-class
classref-property
:::
::::

`MotionMode<enum_CharacterBody2D_MotionMode>`{.interpreted-text
role="ref"} **motion_mode** = `0`
`🔗<class_CharacterBody2D_property_motion_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_motion_mode**(value:
  `MotionMode<enum_CharacterBody2D_MotionMode>`{.interpreted-text
  role="ref"})
- `MotionMode<enum_CharacterBody2D_MotionMode>`{.interpreted-text
  role="ref"} **get_motion_mode**()

Sets the motion mode which defines the behavior of
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_platform_floor_layers}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **platform_floor_layers**
= `4294967295`
`🔗<class_CharacterBody2D_property_platform_floor_layers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_platform_floor_layers**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_platform_floor_layers**()

Collision layers that will be included for detecting floor bodies that
will act as moving platforms to be followed by the **CharacterBody2D**.
By default, all floor bodies are detected and propagate their velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_platform_on_leave}
::: rst-class
classref-property
:::
::::

`PlatformOnLeave<enum_CharacterBody2D_PlatformOnLeave>`{.interpreted-text
role="ref"} **platform_on_leave** = `0`
`🔗<class_CharacterBody2D_property_platform_on_leave>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_platform_on_leave**(value:
  `PlatformOnLeave<enum_CharacterBody2D_PlatformOnLeave>`{.interpreted-text
  role="ref"})
- `PlatformOnLeave<enum_CharacterBody2D_PlatformOnLeave>`{.interpreted-text
  role="ref"} **get_platform_on_leave**()

Sets the behavior to apply when you leave a moving platform. By default,
to be physically accurate, when you leave the last platform velocity is
applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_platform_wall_layers}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **platform_wall_layers**
= `0`
`🔗<class_CharacterBody2D_property_platform_wall_layers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_platform_wall_layers**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_platform_wall_layers**()

Collision layers that will be included for detecting wall bodies that
will act as moving platforms to be followed by the **CharacterBody2D**.
By default, all wall bodies are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_safe_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **safe_margin** =
`0.08`
`🔗<class_CharacterBody2D_property_safe_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_safe_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_safe_margin**()

Extra margin used for collision recovery when calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}.

If the body is at least this close to another body, it will consider
them to be colliding and will be pushed away before performing the
actual motion.

A higher value means it\'s more flexible for detecting collision, which
helps with consistently detecting walls and floors.

A lower value forces the collision algorithm to use more exact
detection, so it can be used in cases that specifically require
precision, e.g at very low scale to avoid visible jittering, or for
stability with a stack of character bodies.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_slide_on_ceiling}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **slide_on_ceiling** =
`true`
`🔗<class_CharacterBody2D_property_slide_on_ceiling>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_slide_on_ceiling_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_slide_on_ceiling_enabled**()

If `true`, during a jump against the ceiling, the body will slide, if
`false` it will be stopped and will fall vertically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_up_direction}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **up_direction**
= `Vector2(0, -1)`
`🔗<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_up_direction**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_up_direction**()

Vector pointing upwards, used to determine what is a wall and what is a
floor (or a ceiling) when calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. Defaults to
`Vector2.UP<class_Vector2_constant_UP>`{.interpreted-text role="ref"}.
As the vector will be normalized it can\'t be equal to
`Vector2.ZERO<class_Vector2_constant_ZERO>`{.interpreted-text
role="ref"}, if you want all collisions to be reported as walls,
consider using
`MOTION_MODE_FLOATING<class_CharacterBody2D_constant_MOTION_MODE_FLOATING>`{.interpreted-text
role="ref"} as
`motion_mode<class_CharacterBody2D_property_motion_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_velocity}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **velocity** =
`Vector2(0, 0)`
`🔗<class_CharacterBody2D_property_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_velocity**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_velocity**()

Current velocity vector in pixels per second, used and modified during
calls to
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_property_wall_min_slide_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**wall_min_slide_angle** = `0.2617994`
`🔗<class_CharacterBody2D_property_wall_min_slide_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wall_min_slide_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_wall_min_slide_angle**()

Minimum angle (in radians) where the body is allowed to slide when it
encounters a wall. The default value equals 15 degrees. This property
only affects movement when
`motion_mode<class_CharacterBody2D_property_motion_mode>`{.interpreted-text
role="ref"} is
`MOTION_MODE_FLOATING<class_CharacterBody2D_constant_MOTION_MODE_FLOATING>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CharacterBody2D_method_apply_floor_snap}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_floor_snap**()
`🔗<class_CharacterBody2D_method_apply_floor_snap>`{.interpreted-text
role="ref"}

Allows to manually apply a snap to the floor regardless of the body\'s
velocity. This function does nothing when
`is_on_floor()<class_CharacterBody2D_method_is_on_floor>`{.interpreted-text
role="ref"} returns `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_floor_angle}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_floor_angle**(up_direction:
`Vector2<class_Vector2>`{.interpreted-text role="ref"} = Vector2(0, -1))
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_get_floor_angle>`{.interpreted-text
role="ref"}

Returns the floor\'s collision angle at the last collision point
according to `up_direction`, which is
`Vector2.UP<class_Vector2_constant_UP>`{.interpreted-text role="ref"} by
default. This value is always positive and only valid after calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"} and when
`is_on_floor()<class_CharacterBody2D_method_is_on_floor>`{.interpreted-text
role="ref"} returns `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_floor_normal}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_floor_normal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_get_floor_normal>`{.interpreted-text
role="ref"}

Returns the collision normal of the floor at the last collision point.
Only valid after calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"} and when
`is_on_floor()<class_CharacterBody2D_method_is_on_floor>`{.interpreted-text
role="ref"} returns `true`.

\*\*Warning:\*\* The collision normal is not always the same as the
surface normal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_last_motion}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_last_motion**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_get_last_motion>`{.interpreted-text
role="ref"}

Returns the last motion applied to the **CharacterBody2D** during the
last call to
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. The movement can be split into multiple motions when
sliding occurs, and this method return the last one, which is useful to
retrieve the current direction of the movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_last_slide_collision}
::: rst-class
classref-method
:::
::::

`KinematicCollision2D<class_KinematicCollision2D>`{.interpreted-text
role="ref"} **get_last_slide_collision**()
`🔗<class_CharacterBody2D_method_get_last_slide_collision>`{.interpreted-text
role="ref"}

Returns a
`KinematicCollision2D<class_KinematicCollision2D>`{.interpreted-text
role="ref"}, which contains information about the latest collision that
occurred during the last call to
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_platform_velocity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_platform_velocity**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_get_platform_velocity>`{.interpreted-text
role="ref"}

Returns the linear velocity of the platform at the last collision point.
Only valid after calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_position_delta}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_position_delta**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_get_position_delta>`{.interpreted-text
role="ref"}

Returns the travel (position delta) that occurred during the last call
to
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_real_velocity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_real_velocity**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_get_real_velocity>`{.interpreted-text
role="ref"}

Returns the current real velocity since the last call to
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. For example, when you climb a slope, you will move
diagonally even though the velocity is horizontal. This method returns
the diagonal movement, as opposed to
`velocity<class_CharacterBody2D_property_velocity>`{.interpreted-text
role="ref"} which returns the requested velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_slide_collision}
::: rst-class
classref-method
:::
::::

`KinematicCollision2D<class_KinematicCollision2D>`{.interpreted-text
role="ref"} **get_slide_collision**(slide_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CharacterBody2D_method_get_slide_collision>`{.interpreted-text
role="ref"}

Returns a
`KinematicCollision2D<class_KinematicCollision2D>`{.interpreted-text
role="ref"}, which contains information about a collision that occurred
during the last call to
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. Since the body can collide several times in a single call
to
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}, you must specify the index of the collision in the range 0
to
(`get_slide_collision_count()<class_CharacterBody2D_method_get_slide_collision_count>`{.interpreted-text
role="ref"} - 1).

\*\*Example:\*\* Iterate through the collisions with a `for` loop:

::::: tabs
::: code-tab
gdscript

for i in get_slide_collision_count():

:   var collision = get_slide_collision(i) print(\"Collided with: \",
    collision.get_collider().name)
:::

::: code-tab
csharp

for (int i = 0; i \< GetSlideCollisionCount(); i++) {
KinematicCollision2D collision = GetSlideCollision(i);
GD.Print(\"Collided with: \", (collision.GetCollider() as Node).Name); }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_slide_collision_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_slide_collision_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_get_slide_collision_count>`{.interpreted-text
role="ref"}

Returns the number of times the body collided and changed direction
during the last call to
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_get_wall_normal}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_wall_normal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_get_wall_normal>`{.interpreted-text
role="ref"}

Returns the collision normal of the wall at the last collision point.
Only valid after calling
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"} and when
`is_on_wall()<class_CharacterBody2D_method_is_on_wall>`{.interpreted-text
role="ref"} returns `true`.

\*\*Warning:\*\* The collision normal is not always the same as the
surface normal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_is_on_ceiling}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_on_ceiling**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_is_on_ceiling>`{.interpreted-text
role="ref"}

Returns `true` if the body collided with the ceiling on the last call of
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. Otherwise, returns `false`. The
`up_direction<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"} and
`floor_max_angle<class_CharacterBody2D_property_floor_max_angle>`{.interpreted-text
role="ref"} are used to determine whether a surface is \"ceiling\" or
not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_is_on_ceiling_only}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_on_ceiling_only**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_is_on_ceiling_only>`{.interpreted-text
role="ref"}

Returns `true` if the body collided only with the ceiling on the last
call of
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. Otherwise, returns `false`. The
`up_direction<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"} and
`floor_max_angle<class_CharacterBody2D_property_floor_max_angle>`{.interpreted-text
role="ref"} are used to determine whether a surface is \"ceiling\" or
not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_is_on_floor}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_on_floor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_is_on_floor>`{.interpreted-text
role="ref"}

Returns `true` if the body collided with the floor on the last call of
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. Otherwise, returns `false`. The
`up_direction<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"} and
`floor_max_angle<class_CharacterBody2D_property_floor_max_angle>`{.interpreted-text
role="ref"} are used to determine whether a surface is \"floor\" or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_is_on_floor_only}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_on_floor_only**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_is_on_floor_only>`{.interpreted-text
role="ref"}

Returns `true` if the body collided only with the floor on the last call
of
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. Otherwise, returns `false`. The
`up_direction<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"} and
`floor_max_angle<class_CharacterBody2D_property_floor_max_angle>`{.interpreted-text
role="ref"} are used to determine whether a surface is \"floor\" or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_is_on_wall}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_on_wall**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_is_on_wall>`{.interpreted-text
role="ref"}

Returns `true` if the body collided with a wall on the last call of
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. Otherwise, returns `false`. The
`up_direction<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"} and
`floor_max_angle<class_CharacterBody2D_property_floor_max_angle>`{.interpreted-text
role="ref"} are used to determine whether a surface is \"wall\" or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_is_on_wall_only}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_on_wall_only**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CharacterBody2D_method_is_on_wall_only>`{.interpreted-text
role="ref"}

Returns `true` if the body collided only with a wall on the last call of
`move_and_slide()<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}. Otherwise, returns `false`. The
`up_direction<class_CharacterBody2D_property_up_direction>`{.interpreted-text
role="ref"} and
`floor_max_angle<class_CharacterBody2D_property_floor_max_angle>`{.interpreted-text
role="ref"} are used to determine whether a surface is \"wall\" or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharacterBody2D_method_move_and_slide}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **move_and_slide**()
`🔗<class_CharacterBody2D_method_move_and_slide>`{.interpreted-text
role="ref"}

Moves the body based on
`velocity<class_CharacterBody2D_property_velocity>`{.interpreted-text
role="ref"}. If the body collides with another, it will slide along the
other body (by default only on floor) rather than stop immediately. If
the other body is a **CharacterBody2D** or
`RigidBody2D<class_RigidBody2D>`{.interpreted-text role="ref"}, it will
also be affected by the motion of the other body. You can use this to
make moving and rotating platforms, or to make nodes push other nodes.

Modifies
`velocity<class_CharacterBody2D_property_velocity>`{.interpreted-text
role="ref"} if a slide collision occurred. To get the latest collision
call
`get_last_slide_collision()<class_CharacterBody2D_method_get_last_slide_collision>`{.interpreted-text
role="ref"}, for detailed information about collisions that occurred,
use
`get_slide_collision()<class_CharacterBody2D_method_get_slide_collision>`{.interpreted-text
role="ref"}.

When the body touches a moving platform, the platform\'s velocity is
automatically added to the body motion. If a collision occurs due to the
platform\'s motion, it will always be first in the slide collisions.

The general behavior and available properties change according to the
`motion_mode<class_CharacterBody2D_property_motion_mode>`{.interpreted-text
role="ref"}.

Returns `true` if the body collided, otherwise, returns `false`.
