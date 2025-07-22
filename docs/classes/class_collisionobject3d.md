github_url
:   hide

# CollisionObject3D {#class_CollisionObject3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `Area3D<class_Area3D>`{.interpreted-text role="ref"},
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}

Abstract base class for 3D physics objects.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for 3D physics objects. **CollisionObject3D** can
hold any number of `Shape3D<class_Shape3D>`{.interpreted-text
role="ref"}s for collision. Each shape must be assigned to a *shape
owner*. Shape owners are not nodes and do not appear in the editor, but
are accessible through code using the `shape_owner_*` methods.

\*\*Warning:\*\* With a non-uniform scale, this node will likely not
behave as expected. It is advised to keep its scale the same on all axes
and adjust its collision shape(s) instead.

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

:::: {#class_CollisionObject3D_signal_input_event}
::: rst-class
classref-signal
:::
::::

**input_event**(camera: `Node<class_Node>`{.interpreted-text
role="ref"}, event: `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}, event_position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, normal: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CollisionObject3D_signal_input_event>`{.interpreted-text
role="ref"}

Emitted when the object receives an unhandled
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"}.
`event_position` is the location in world space of the mouse pointer on
the surface of the shape with index `shape_idx` and `normal` is the
normal vector of the surface at that point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_signal_mouse_entered}
::: rst-class
classref-signal
:::
::::

**mouse_entered**()
`🔗<class_CollisionObject3D_signal_mouse_entered>`{.interpreted-text
role="ref"}

Emitted when the mouse pointer enters any of this object\'s shapes.
Requires
`input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>`{.interpreted-text
role="ref"} to be `true` and at least one
`collision_layer<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"} bit to be set.

\*\*Note:\*\* Due to the lack of continuous collision detection, this
signal may not be emitted in the expected order if the mouse moves fast
enough and the **CollisionObject3D**\'s area is small. This signal may
also not be emitted if another **CollisionObject3D** is overlapping the
**CollisionObject3D** in question.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_signal_mouse_exited}
::: rst-class
classref-signal
:::
::::

**mouse_exited**()
`🔗<class_CollisionObject3D_signal_mouse_exited>`{.interpreted-text
role="ref"}

Emitted when the mouse pointer exits all this object\'s shapes. Requires
`input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>`{.interpreted-text
role="ref"} to be `true` and at least one
`collision_layer<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"} bit to be set.

\*\*Note:\*\* Due to the lack of continuous collision detection, this
signal may not be emitted in the expected order if the mouse moves fast
enough and the **CollisionObject3D**\'s area is small. This signal may
also not be emitted if another **CollisionObject3D** is overlapping the
**CollisionObject3D** in question.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_CollisionObject3D_DisableMode}
::: rst-class
classref-enumeration
:::
::::

enum **DisableMode**:
`🔗<enum_CollisionObject3D_DisableMode>`{.interpreted-text role="ref"}

:::: {#class_CollisionObject3D_constant_DISABLE_MODE_REMOVE}
::: rst-class
classref-enumeration-constant
:::
::::

`DisableMode<enum_CollisionObject3D_DisableMode>`{.interpreted-text
role="ref"} **DISABLE_MODE_REMOVE** = `0`

When
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} is set to
`Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}, remove from the physics simulation to stop all physics
interactions with this **CollisionObject3D**.

Automatically re-added to the physics simulation when the
`Node<class_Node>`{.interpreted-text role="ref"} is processed again.

:::: {#class_CollisionObject3D_constant_DISABLE_MODE_MAKE_STATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`DisableMode<enum_CollisionObject3D_DisableMode>`{.interpreted-text
role="ref"} **DISABLE_MODE_MAKE_STATIC** = `1`

When
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} is set to
`Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}, make the body static. Doesn\'t affect
`Area3D<class_Area3D>`{.interpreted-text role="ref"}.
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}
can\'t be affected by forces or other bodies while static.

Automatically set `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text
role="ref"} back to its original mode when the
`Node<class_Node>`{.interpreted-text role="ref"} is processed again.

:::: {#class_CollisionObject3D_constant_DISABLE_MODE_KEEP_ACTIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`DisableMode<enum_CollisionObject3D_DisableMode>`{.interpreted-text
role="ref"} **DISABLE_MODE_KEEP_ACTIVE** = `2`

When
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} is set to
`Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}, do not affect the physics simulation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CollisionObject3D_property_collision_layer}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_layer** = `1`
`🔗<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_layer**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_layer**()

The physics layers this CollisionObject3D **is in**. Collision objects
can exist in one or more of 32 different layers. See also
`collision_mask<class_CollisionObject3D_property_collision_mask>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Object A can detect a contact with object B only if object
B is in any of the layers that object A scans. See [Collision layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_property_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** = `1`
`🔗<class_CollisionObject3D_property_collision_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_mask**()

The physics layers this CollisionObject3D **scans**. Collision objects
can scan one or more of 32 different layers. See also
`collision_layer<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Object A can detect a contact with object B only if object
B is in any of the layers that object A scans. See [Collision layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_property_collision_priority}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**collision_priority** = `1.0`
`🔗<class_CollisionObject3D_property_collision_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_priority**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_collision_priority**()

The priority used to solve colliding when occurring penetration. The
higher the priority is, the lower the penetration into the object will
be. This can for example be used to prevent the player from breaking
through the boundaries of a level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_property_disable_mode}
::: rst-class
classref-property
:::
::::

`DisableMode<enum_CollisionObject3D_DisableMode>`{.interpreted-text
role="ref"} **disable_mode** = `0`
`🔗<class_CollisionObject3D_property_disable_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disable_mode**(value:
  `DisableMode<enum_CollisionObject3D_DisableMode>`{.interpreted-text
  role="ref"})
- `DisableMode<enum_CollisionObject3D_DisableMode>`{.interpreted-text
  role="ref"} **get_disable_mode**()

Defines the behavior in physics when
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} is set to
`Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_property_input_capture_on_drag}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_capture_on_drag** = `false`
`🔗<class_CollisionObject3D_property_input_capture_on_drag>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_capture_input_on_drag**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_capture_input_on_drag**()

If `true`, the **CollisionObject3D** will continue to receive input
events as the mouse is dragged across its shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_property_input_ray_pickable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **input_ray_pickable**
= `true`
`🔗<class_CollisionObject3D_property_input_ray_pickable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ray_pickable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_ray_pickable**()

If `true`, this object is pickable. A pickable object can detect the
mouse pointer entering/leaving, and if the mouse is inside it, report
input events. Requires at least one
`collision_layer<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"} bit to be set.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CollisionObject3D_private_method__input_event}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_input_event**(camera: `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"}, event: `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}, event_position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, normal: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_private_method__input_event>`{.interpreted-text
role="ref"}

Receives unhandled `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}s. `event_position` is the location in world space of the
mouse pointer on the surface of the shape with index `shape_idx` and
`normal` is the normal vector of the surface at that point. Connect to
the
`input_event<class_CollisionObject3D_signal_input_event>`{.interpreted-text
role="ref"} signal to easily pick up these events.

\*\*Note:\*\*
`_input_event()<class_CollisionObject3D_private_method__input_event>`{.interpreted-text
role="ref"} requires
`input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>`{.interpreted-text
role="ref"} to be `true` and at least one
`collision_layer<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"} bit to be set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_private_method__mouse_enter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_mouse_enter**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_private_method__mouse_enter>`{.interpreted-text
role="ref"}

Called when the mouse pointer enters any of this object\'s shapes.
Requires
`input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>`{.interpreted-text
role="ref"} to be `true` and at least one
`collision_layer<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"} bit to be set. Note that moving between different shapes
within a single **CollisionObject3D** won\'t cause this function to be
called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_private_method__mouse_exit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_mouse_exit**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_private_method__mouse_exit>`{.interpreted-text
role="ref"}

Called when the mouse pointer exits all this object\'s shapes. Requires
`input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>`{.interpreted-text
role="ref"} to be `true` and at least one
`collision_layer<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"} bit to be set. Note that moving between different shapes
within a single **CollisionObject3D** won\'t cause this function to be
called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_create_shape_owner}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**create_shape_owner**(owner: `Object<class_Object>`{.interpreted-text
role="ref"})
`🔗<class_CollisionObject3D_method_create_shape_owner>`{.interpreted-text
role="ref"}

Creates a new shape owner for the given object. Returns `owner_id` of
the new owner for future reference.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_get_collision_layer_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_get_collision_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_layer<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_get_collision_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_get_collision_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_mask<class_CollisionObject3D_property_collision_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_get_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_get_rid>`{.interpreted-text
role="ref"}

Returns the object\'s `RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_get_shape_owners}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_shape_owners**()
`🔗<class_CollisionObject3D_method_get_shape_owners>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`owner_id` identifiers. You can use these ids in other methods that take
`owner_id` as an argument.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_is_shape_owner_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_shape_owner_disabled**(owner_id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_is_shape_owner_disabled>`{.interpreted-text
role="ref"}

If `true`, the shape owner and its shapes are disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_remove_shape_owner}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_shape_owner**(owner_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_CollisionObject3D_method_remove_shape_owner>`{.interpreted-text
role="ref"}

Removes the given shape owner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_set_collision_layer_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CollisionObject3D_method_set_collision_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_layer<class_CollisionObject3D_property_collision_layer>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_set_collision_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CollisionObject3D_method_set_collision_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_mask<class_CollisionObject3D_property_collision_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_find_owner}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shape_find_owner**(shape_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_shape_find_owner>`{.interpreted-text
role="ref"}

Returns the `owner_id` of the given shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_add_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shape_owner_add_shape**(owner_id: `int<class_int>`{.interpreted-text
role="ref"}, shape: `Shape3D<class_Shape3D>`{.interpreted-text
role="ref"})
`🔗<class_CollisionObject3D_method_shape_owner_add_shape>`{.interpreted-text
role="ref"}

Adds a `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} to the
shape owner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_clear_shapes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shape_owner_clear_shapes**(owner_id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CollisionObject3D_method_shape_owner_clear_shapes>`{.interpreted-text
role="ref"}

Removes all shapes from the shape owner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_get_owner}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**shape_owner_get_owner**(owner_id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_shape_owner_get_owner>`{.interpreted-text
role="ref"}

Returns the parent object of the given shape owner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_get_shape}
::: rst-class
classref-method
:::
::::

`Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**shape_owner_get_shape**(owner_id: `int<class_int>`{.interpreted-text
role="ref"}, shape_id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_shape_owner_get_shape>`{.interpreted-text
role="ref"}

Returns the `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} with
the given ID from the given shape owner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_get_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shape_owner_get_shape_count**(owner_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_shape_owner_get_shape_count>`{.interpreted-text
role="ref"}

Returns the number of shapes the given shape owner contains.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_get_shape_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shape_owner_get_shape_index**(owner_id:
`int<class_int>`{.interpreted-text role="ref"}, shape_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_shape_owner_get_shape_index>`{.interpreted-text
role="ref"}

Returns the child index of the
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} with the given ID
from the given shape owner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_get_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**shape_owner_get_transform**(owner_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CollisionObject3D_method_shape_owner_get_transform>`{.interpreted-text
role="ref"}

Returns the shape owner\'s
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_remove_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shape_owner_remove_shape**(owner_id:
`int<class_int>`{.interpreted-text role="ref"}, shape_id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CollisionObject3D_method_shape_owner_remove_shape>`{.interpreted-text
role="ref"}

Removes a shape from the given shape owner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_set_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shape_owner_set_disabled**(owner_id:
`int<class_int>`{.interpreted-text role="ref"}, disabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CollisionObject3D_method_shape_owner_set_disabled>`{.interpreted-text
role="ref"}

If `true`, disables the given shape owner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionObject3D_method_shape_owner_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shape_owner_set_transform**(owner_id:
`int<class_int>`{.interpreted-text role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_CollisionObject3D_method_shape_owner_set_transform>`{.interpreted-text
role="ref"}

Sets the `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
of the given shape owner.
