github_url
:   hide

# AnimatableBody2D {#class_AnimatableBody2D}

**Inherits:** `StaticBody2D<class_StaticBody2D>`{.interpreted-text
role="ref"} **\<**
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}
**\<** `CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} **\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D physics body that can\'t be moved by external forces. When moved
manually, it affects other bodies in its path.

::: rst-class
classref-introduction-group
:::

## Description

An animatable 2D physics body. It can\'t be moved by external forces or
contacts, but can be moved manually by other means such as code,
`AnimationMixer<class_AnimationMixer>`{.interpreted-text role="ref"}s
(with
`AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>`{.interpreted-text
role="ref"} set to
`AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS>`{.interpreted-text
role="ref"}), and
`RemoteTransform2D<class_RemoteTransform2D>`{.interpreted-text
role="ref"}.

When **AnimatableBody2D** is moved, its linear and angular velocity are
estimated and used to affect other physics bodies in its path. This
makes it useful for moving platforms, doors, and other moving objects.

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

:::: {#class_AnimatableBody2D_property_sync_to_physics}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sync_to_physics** =
`true`
`🔗<class_AnimatableBody2D_property_sync_to_physics>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sync_to_physics**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_sync_to_physics_enabled**()

If `true`, the body\'s movement will be synchronized to the physics
frame. This is useful when animating movement via
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"},
for example on moving platforms. Do **not** use together with
`PhysicsBody2D.move_and_collide()<class_PhysicsBody2D_method_move_and_collide>`{.interpreted-text
role="ref"}.
