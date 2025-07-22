github_url
:   hide

::: {.meta keywords="trigger"}
:::

# Area2D {#class_Area2D}

**Inherits:**
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} **\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A region of 2D space that detects other
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"}s entering or exiting it.

::: rst-class
classref-introduction-group
:::

## Description

**Area2D** is a region of 2D space defined by one or multiple
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text role="ref"}
or `CollisionPolygon2D<class_CollisionPolygon2D>`{.interpreted-text
role="ref"} child nodes. It detects when other
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"}s enter or exit it, and it also keeps track of which
collision objects haven\'t exited it yet (i.e. which one are overlapping
it).

This node can also locally alter or override physics parameters
(gravity, damping) and route audio to custom audio buses.

\*\*Note:\*\* Areas and bodies created with
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}
might not interact as expected with **Area2D**s, and might not emit
signals or track objects correctly.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Area2D <../tutorials/physics/using_area_2d>`{.interpreted-text
  role="doc"}
- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)
- [2D Pong Demo](https://godotengine.org/asset-library/asset/2728)
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

## Signals

:::: {#class_Area2D_signal_area_entered}
::: rst-class
classref-signal
:::
::::

**area_entered**(area: `Area2D<class_Area2D>`{.interpreted-text
role="ref"}) `🔗<class_Area2D_signal_area_entered>`{.interpreted-text
role="ref"}

Emitted when the received `area` enters this area. Requires
`monitoring<class_Area2D_property_monitoring>`{.interpreted-text
role="ref"} to be set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_signal_area_exited}
::: rst-class
classref-signal
:::
::::

**area_exited**(area: `Area2D<class_Area2D>`{.interpreted-text
role="ref"}) `🔗<class_Area2D_signal_area_exited>`{.interpreted-text
role="ref"}

Emitted when the received `area` exits this area. Requires
`monitoring<class_Area2D_property_monitoring>`{.interpreted-text
role="ref"} to be set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_signal_area_shape_entered}
::: rst-class
classref-signal
:::
::::

**area_shape_entered**(area_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, area: `Area2D<class_Area2D>`{.interpreted-text role="ref"},
area_shape_index: `int<class_int>`{.interpreted-text role="ref"},
local_shape_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Area2D_signal_area_shape_entered>`{.interpreted-text
role="ref"}

Emitted when a `Shape2D<class_Shape2D>`{.interpreted-text role="ref"} of
the received `area` enters a shape of this area. Requires
`monitoring<class_Area2D_property_monitoring>`{.interpreted-text
role="ref"} to be set to `true`.

`local_shape_index` and `area_shape_index` contain indices of the
interacting shapes from this area and the other area, respectively.
`area_rid` contains the `RID<class_RID>`{.interpreted-text role="ref"}
of the other area. These values can be used with the
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}.

\*\*Example:\*\* Get the
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text role="ref"}
node from the shape index:

:::: tabs
::: code-tab
gdscript

var other_shape_owner = area.shape_find_owner(area_shape_index) var
other_shape_node = area.shape_owner_get_owner(other_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index) var
local_shape_node = shape_owner_get_owner(local_shape_owner)
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_signal_area_shape_exited}
::: rst-class
classref-signal
:::
::::

**area_shape_exited**(area_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, area: `Area2D<class_Area2D>`{.interpreted-text role="ref"},
area_shape_index: `int<class_int>`{.interpreted-text role="ref"},
local_shape_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Area2D_signal_area_shape_exited>`{.interpreted-text
role="ref"}

Emitted when a `Shape2D<class_Shape2D>`{.interpreted-text role="ref"} of
the received `area` exits a shape of this area. Requires
`monitoring<class_Area2D_property_monitoring>`{.interpreted-text
role="ref"} to be set to `true`.

See also
`area_shape_entered<class_Area2D_signal_area_shape_entered>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_signal_body_entered}
::: rst-class
classref-signal
:::
::::

**body_entered**(body: `Node2D<class_Node2D>`{.interpreted-text
role="ref"}) `🔗<class_Area2D_signal_body_entered>`{.interpreted-text
role="ref"}

Emitted when the received `body` enters this area. `body` can be a
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"} or a
`TileMap<class_TileMap>`{.interpreted-text role="ref"}.
`TileMap<class_TileMap>`{.interpreted-text role="ref"}s are detected if
their `TileSet<class_TileSet>`{.interpreted-text role="ref"} has
collision shapes configured. Requires
`monitoring<class_Area2D_property_monitoring>`{.interpreted-text
role="ref"} to be set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_signal_body_exited}
::: rst-class
classref-signal
:::
::::

**body_exited**(body: `Node2D<class_Node2D>`{.interpreted-text
role="ref"}) `🔗<class_Area2D_signal_body_exited>`{.interpreted-text
role="ref"}

Emitted when the received `body` exits this area. `body` can be a
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"} or a
`TileMap<class_TileMap>`{.interpreted-text role="ref"}.
`TileMap<class_TileMap>`{.interpreted-text role="ref"}s are detected if
their `TileSet<class_TileSet>`{.interpreted-text role="ref"} has
collision shapes configured. Requires
`monitoring<class_Area2D_property_monitoring>`{.interpreted-text
role="ref"} to be set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_signal_body_shape_entered}
::: rst-class
classref-signal
:::
::::

**body_shape_entered**(body_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, body: `Node2D<class_Node2D>`{.interpreted-text role="ref"},
body_shape_index: `int<class_int>`{.interpreted-text role="ref"},
local_shape_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Area2D_signal_body_shape_entered>`{.interpreted-text
role="ref"}

Emitted when a `Shape2D<class_Shape2D>`{.interpreted-text role="ref"} of
the received `body` enters a shape of this area. `body` can be a
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"} or a
`TileMap<class_TileMap>`{.interpreted-text role="ref"}.
`TileMap<class_TileMap>`{.interpreted-text role="ref"}s are detected if
their `TileSet<class_TileSet>`{.interpreted-text role="ref"} has
collision shapes configured. Requires
`monitoring<class_Area2D_property_monitoring>`{.interpreted-text
role="ref"} to be set to `true`.

`local_shape_index` and `body_shape_index` contain indices of the
interacting shapes from this area and the interacting body,
respectively. `body_rid` contains the `RID<class_RID>`{.interpreted-text
role="ref"} of the body. These values can be used with the
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}.

\*\*Example:\*\* Get the
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text role="ref"}
node from the shape index:

:::: tabs
::: code-tab
gdscript

var body_shape_owner = body.shape_find_owner(body_shape_index) var
body_shape_node = body.shape_owner_get_owner(body_shape_owner)

var local_shape_owner = shape_find_owner(local_shape_index) var
local_shape_node = shape_owner_get_owner(local_shape_owner)
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_signal_body_shape_exited}
::: rst-class
classref-signal
:::
::::

**body_shape_exited**(body_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, body: `Node2D<class_Node2D>`{.interpreted-text role="ref"},
body_shape_index: `int<class_int>`{.interpreted-text role="ref"},
local_shape_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Area2D_signal_body_shape_exited>`{.interpreted-text
role="ref"}

Emitted when a `Shape2D<class_Shape2D>`{.interpreted-text role="ref"} of
the received `body` exits a shape of this area. `body` can be a
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"} or a
`TileMap<class_TileMap>`{.interpreted-text role="ref"}.
`TileMap<class_TileMap>`{.interpreted-text role="ref"}s are detected if
their `TileSet<class_TileSet>`{.interpreted-text role="ref"} has
collision shapes configured. Requires
`monitoring<class_Area2D_property_monitoring>`{.interpreted-text
role="ref"} to be set to `true`.

See also
`body_shape_entered<class_Area2D_signal_body_shape_entered>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Area2D_SpaceOverride}
::: rst-class
classref-enumeration
:::
::::

enum **SpaceOverride**:
`🔗<enum_Area2D_SpaceOverride>`{.interpreted-text role="ref"}

:::: {#class_Area2D_constant_SPACE_OVERRIDE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text role="ref"}
**SPACE_OVERRIDE_DISABLED** = `0`

This area does not affect gravity/damping.

:::: {#class_Area2D_constant_SPACE_OVERRIDE_COMBINE}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text role="ref"}
**SPACE_OVERRIDE_COMBINE** = `1`

This area adds its gravity/damping values to whatever has been
calculated so far (in
`priority<class_Area2D_property_priority>`{.interpreted-text role="ref"}
order).

:::: {#class_Area2D_constant_SPACE_OVERRIDE_COMBINE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text role="ref"}
**SPACE_OVERRIDE_COMBINE_REPLACE** = `2`

This area adds its gravity/damping values to whatever has been
calculated so far (in
`priority<class_Area2D_property_priority>`{.interpreted-text role="ref"}
order), ignoring any lower priority areas.

:::: {#class_Area2D_constant_SPACE_OVERRIDE_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text role="ref"}
**SPACE_OVERRIDE_REPLACE** = `3`

This area replaces any gravity/damping, even the defaults, ignoring any
lower priority areas.

:::: {#class_Area2D_constant_SPACE_OVERRIDE_REPLACE_COMBINE}
::: rst-class
classref-enumeration-constant
:::
::::

`SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text role="ref"}
**SPACE_OVERRIDE_REPLACE_COMBINE** = `4`

This area replaces any gravity/damping calculated so far (in
`priority<class_Area2D_property_priority>`{.interpreted-text role="ref"}
order), but keeps calculating the rest of the areas.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Area2D_property_angular_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angular_damp** =
`1.0` `🔗<class_Area2D_property_angular_damp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_damp**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_angular_damp**()

The rate at which objects stop spinning in this area. Represents the
angular velocity lost per second.

See
`ProjectSettings.physics/2d/default_angular_damp<class_ProjectSettings_property_physics/2d/default_angular_damp>`{.interpreted-text
role="ref"} for more details about damping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_angular_damp_space_override}
::: rst-class
classref-property
:::
::::

`SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text role="ref"}
**angular_damp_space_override** = `0`
`🔗<class_Area2D_property_angular_damp_space_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_damp_space_override_mode**(value:
  `SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text
  role="ref"})
- `SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text
  role="ref"} **get_angular_damp_space_override_mode**()

Override mode for angular damping calculations within this area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_audio_bus_name}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**audio_bus_name** = `&"Master"`
`🔗<class_Area2D_property_audio_bus_name>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_audio_bus_name**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_audio_bus_name**()

The name of the area\'s audio bus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_audio_bus_override}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **audio_bus_override**
= `false`
`🔗<class_Area2D_property_audio_bus_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_audio_bus_override**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_overriding_audio_bus**()

If `true`, the area\'s audio bus overrides the default audio bus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_gravity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **gravity** = `980.0`
`🔗<class_Area2D_property_gravity>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_gravity**()

The area\'s gravity intensity (in pixels per second squared). This value
multiplies the gravity direction. This is useful to alter the force of
gravity without altering its direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_gravity_direction}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**gravity_direction** = `Vector2(0, 1)`
`🔗<class_Area2D_property_gravity_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity_direction**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_gravity_direction**()

The area\'s gravity vector (not normalized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_gravity_point}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **gravity_point** =
`false` `🔗<class_Area2D_property_gravity_point>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity_is_point**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_gravity_a_point**()

If `true`, gravity is calculated from a point (set via
`gravity_point_center<class_Area2D_property_gravity_point_center>`{.interpreted-text
role="ref"}). See also
`gravity_space_override<class_Area2D_property_gravity_space_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_gravity_point_center}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**gravity_point_center** = `Vector2(0, 1)`
`🔗<class_Area2D_property_gravity_point_center>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity_point_center**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_gravity_point_center**()

If gravity is a point (see
`gravity_point<class_Area2D_property_gravity_point>`{.interpreted-text
role="ref"}), this will be the point of attraction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_gravity_point_unit_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**gravity_point_unit_distance** = `0.0`
`🔗<class_Area2D_property_gravity_point_unit_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity_point_unit_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_gravity_point_unit_distance**()

The distance at which the gravity strength is equal to
`gravity<class_Area2D_property_gravity>`{.interpreted-text role="ref"}.
For example, on a planet 100 pixels in radius with a surface gravity of
4.0 px/s², set the
`gravity<class_Area2D_property_gravity>`{.interpreted-text role="ref"}
to 4.0 and the unit distance to 100.0. The gravity will have falloff
according to the inverse square law, so in the example, at 200 pixels
from the center the gravity will be 1.0 px/s² (twice the distance, 1/4th
the gravity), at 50 pixels it will be 16.0 px/s² (half the distance, 4x
the gravity), and so on.

The above is true only when the unit distance is a positive number. When
this is set to 0.0, the gravity will be constant regardless of distance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_gravity_space_override}
::: rst-class
classref-property
:::
::::

`SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text role="ref"}
**gravity_space_override** = `0`
`🔗<class_Area2D_property_gravity_space_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity_space_override_mode**(value:
  `SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text
  role="ref"})
- `SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text
  role="ref"} **get_gravity_space_override_mode**()

Override mode for gravity calculations within this area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_linear_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **linear_damp** =
`0.1` `🔗<class_Area2D_property_linear_damp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_damp**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_linear_damp**()

The rate at which objects stop moving in this area. Represents the
linear velocity lost per second.

See
`ProjectSettings.physics/2d/default_linear_damp<class_ProjectSettings_property_physics/2d/default_linear_damp>`{.interpreted-text
role="ref"} for more details about damping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_linear_damp_space_override}
::: rst-class
classref-property
:::
::::

`SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text role="ref"}
**linear_damp_space_override** = `0`
`🔗<class_Area2D_property_linear_damp_space_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_damp_space_override_mode**(value:
  `SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text
  role="ref"})
- `SpaceOverride<enum_Area2D_SpaceOverride>`{.interpreted-text
  role="ref"} **get_linear_damp_space_override_mode**()

Override mode for linear damping calculations within this area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_monitorable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **monitorable** =
`true` `🔗<class_Area2D_property_monitorable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_monitorable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_monitorable**()

If `true`, other monitoring areas can detect this area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_monitoring}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **monitoring** = `true`
`🔗<class_Area2D_property_monitoring>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_monitoring**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_monitoring**()

If `true`, the area detects bodies or areas entering and exiting it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_property_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **priority** = `0`
`🔗<class_Area2D_property_priority>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_priority**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_priority**()

The area\'s priority. Higher priority areas are processed first. The
`World2D<class_World2D>`{.interpreted-text role="ref"}\'s physics is
always processed last, after all areas.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Area2D_method_get_overlapping_areas}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Area2D<class_Area2D>`{.interpreted-text role="ref"}\]
**get_overlapping_areas**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Area2D_method_get_overlapping_areas>`{.interpreted-text
role="ref"}

Returns a list of intersecting **Area2D**s. The overlapping area\'s
`CollisionObject2D.collision_layer<class_CollisionObject2D_property_collision_layer>`{.interpreted-text
role="ref"} must be part of this area\'s
`CollisionObject2D.collision_mask<class_CollisionObject2D_property_collision_mask>`{.interpreted-text
role="ref"} in order to be detected.

For performance reasons (collisions are all processed at the same time)
this list is modified once during the physics step, not immediately
after objects are moved. Consider using signals instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_method_get_overlapping_bodies}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node2D<class_Node2D>`{.interpreted-text role="ref"}\]
**get_overlapping_bodies**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Area2D_method_get_overlapping_bodies>`{.interpreted-text
role="ref"}

Returns a list of intersecting
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}s and
`TileMap<class_TileMap>`{.interpreted-text role="ref"}s. The overlapping
body\'s
`CollisionObject2D.collision_layer<class_CollisionObject2D_property_collision_layer>`{.interpreted-text
role="ref"} must be part of this area\'s
`CollisionObject2D.collision_mask<class_CollisionObject2D_property_collision_mask>`{.interpreted-text
role="ref"} in order to be detected.

For performance reasons (collisions are all processed at the same time)
this list is modified once during the physics step, not immediately
after objects are moved. Consider using signals instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_method_has_overlapping_areas}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_overlapping_areas**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Area2D_method_has_overlapping_areas>`{.interpreted-text
role="ref"}

Returns `true` if intersecting any **Area2D**s, otherwise returns
`false`. The overlapping area\'s
`CollisionObject2D.collision_layer<class_CollisionObject2D_property_collision_layer>`{.interpreted-text
role="ref"} must be part of this area\'s
`CollisionObject2D.collision_mask<class_CollisionObject2D_property_collision_mask>`{.interpreted-text
role="ref"} in order to be detected.

For performance reasons (collisions are all processed at the same time)
the list of overlapping areas is modified once during the physics step,
not immediately after objects are moved. Consider using signals instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_method_has_overlapping_bodies}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_overlapping_bodies**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Area2D_method_has_overlapping_bodies>`{.interpreted-text
role="ref"}

Returns `true` if intersecting any
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}s or
`TileMap<class_TileMap>`{.interpreted-text role="ref"}s, otherwise
returns `false`. The overlapping body\'s
`CollisionObject2D.collision_layer<class_CollisionObject2D_property_collision_layer>`{.interpreted-text
role="ref"} must be part of this area\'s
`CollisionObject2D.collision_mask<class_CollisionObject2D_property_collision_mask>`{.interpreted-text
role="ref"} in order to be detected.

For performance reasons (collisions are all processed at the same time)
the list of overlapping bodies is modified once during the physics step,
not immediately after objects are moved. Consider using signals instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_method_overlaps_area}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **overlaps_area**(area:
`Node<class_Node>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Area2D_method_overlaps_area>`{.interpreted-text
role="ref"}

Returns `true` if the given **Area2D** intersects or overlaps this
**Area2D**, `false` otherwise.

\*\*Note:\*\* The result of this test is not immediate after moving
objects. For performance, the list of overlaps is updated once per frame
and before the physics step. Consider using signals instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Area2D_method_overlaps_body}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **overlaps_body**(body:
`Node<class_Node>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Area2D_method_overlaps_body>`{.interpreted-text
role="ref"}

Returns `true` if the given physics body intersects or overlaps this
**Area2D**, `false` otherwise.

\*\*Note:\*\* The result of this test is not immediate after moving
objects. For performance, list of overlaps is updated once per frame and
before the physics step. Consider using signals instead.

The `body` argument can either be a
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"} or a
`TileMap<class_TileMap>`{.interpreted-text role="ref"} instance. While
TileMaps are not physics bodies themselves, they register their tiles
with collision shapes as a virtual physics body.
