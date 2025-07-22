github_url
:   hide

# PhysicsDirectBodyState2DExtension {#class_PhysicsDirectBodyState2DExtension}

**Inherits:**
`PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides virtual methods that can be overridden to create custom
`PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
role="ref"} implementations.

::: rst-class
classref-introduction-group
:::

## Description

This class extends
`PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
role="ref"} by providing additional virtual methods that can be
overridden. When these methods are overridden, they will be called
instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of
`PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
role="ref"}.

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

## Method Descriptions

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__add_constant_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_add_constant_central_force**(force:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__add_constant_central_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.add_constant_central_force()<class_PhysicsDirectBodyState2D_method_add_constant_central_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__add_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_add_constant_force**(force:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__add_constant_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.add_constant_force()<class_PhysicsDirectBodyState2D_method_add_constant_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__add_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_add_constant_torque**(torque: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__add_constant_torque>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.add_constant_torque()<class_PhysicsDirectBodyState2D_method_add_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__apply_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_apply_central_force**(force:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_central_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.apply_central_force()<class_PhysicsDirectBodyState2D_method_apply_central_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_apply_central_impulse**(impulse:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_central_impulse>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.apply_central_impulse()<class_PhysicsDirectBodyState2D_method_apply_central_impulse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__apply_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_apply_force**(force: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.apply_force()<class_PhysicsDirectBodyState2D_method_apply_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__apply_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_apply_impulse**(impulse: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_impulse>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.apply_impulse()<class_PhysicsDirectBodyState2D_method_apply_impulse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__apply_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_apply_torque**(torque: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_torque>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.apply_torque()<class_PhysicsDirectBodyState2D_method_apply_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__apply_torque_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_apply_torque_impulse**(impulse:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_torque_impulse>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.apply_torque_impulse()<class_PhysicsDirectBodyState2D_method_apply_torque_impulse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_angular_velocity}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_get_angular_velocity**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_angular_velocity>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.angular_velocity<class_PhysicsDirectBodyState2D_property_angular_velocity>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_center_of_mass}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_center_of_mass**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_center_of_mass>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.center_of_mass<class_PhysicsDirectBodyState2D_property_center_of_mass>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_center_of_mass_local}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_center_of_mass_local**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_center_of_mass_local>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.center_of_mass_local<class_PhysicsDirectBodyState2D_property_center_of_mass_local>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_constant_force}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_constant_force**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_constant_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_constant_force()<class_PhysicsDirectBodyState2D_method_get_constant_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_constant_torque}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_get_constant_torque**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_constant_torque>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_constant_torque()<class_PhysicsDirectBodyState2D_method_get_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_get_contact_collider**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_collider()<class_PhysicsDirectBodyState2D_method_get_contact_collider>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_contact_collider_id**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_id>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_collider_id()<class_PhysicsDirectBodyState2D_method_get_contact_collider_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_object}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**\_get_contact_collider_object**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_object>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_collider_object()<class_PhysicsDirectBodyState2D_method_get_contact_collider_object>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_contact_collider_position**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_position>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_collider_position()<class_PhysicsDirectBodyState2D_method_get_contact_collider_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_shape}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_contact_collider_shape**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_collider_shape()<class_PhysicsDirectBodyState2D_method_get_contact_collider_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_velocity_at_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_contact_collider_velocity_at_position**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_velocity_at_position>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_collider_velocity_at_position()<class_PhysicsDirectBodyState2D_method_get_contact_collider_velocity_at_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_contact_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_count>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_count()<class_PhysicsDirectBodyState2D_method_get_contact_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_impulse}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_contact_impulse**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_impulse>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_impulse()<class_PhysicsDirectBodyState2D_method_get_contact_impulse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_normal}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_contact_local_normal**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_normal>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_local_normal()<class_PhysicsDirectBodyState2D_method_get_contact_local_normal>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_contact_local_position**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_position>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_local_position()<class_PhysicsDirectBodyState2D_method_get_contact_local_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_shape}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_contact_local_shape**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_local_shape()<class_PhysicsDirectBodyState2D_method_get_contact_local_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_velocity_at_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_contact_local_velocity_at_position**(contact_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_velocity_at_position>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_contact_local_velocity_at_position()<class_PhysicsDirectBodyState2D_method_get_contact_local_velocity_at_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_inverse_inertia}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_get_inverse_inertia**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_inverse_inertia>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.inverse_inertia<class_PhysicsDirectBodyState2D_property_inverse_inertia>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_inverse_mass}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_get_inverse_mass**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_inverse_mass>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.inverse_mass<class_PhysicsDirectBodyState2D_property_inverse_mass>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_linear_velocity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_linear_velocity**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_linear_velocity>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.linear_velocity<class_PhysicsDirectBodyState2D_property_linear_velocity>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_space_state}
::: rst-class
classref-method
:::
::::

`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"} **\_get_space_state**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_space_state>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_space_state()<class_PhysicsDirectBodyState2D_method_get_space_state>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_step}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **\_get_step**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_step>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.step<class_PhysicsDirectBodyState2D_property_step>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_total_angular_damp}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_get_total_angular_damp**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_total_angular_damp>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.total_angular_damp<class_PhysicsDirectBodyState2D_property_total_angular_damp>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_total_gravity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_total_gravity**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_total_gravity>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.total_gravity<class_PhysicsDirectBodyState2D_property_total_gravity>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_total_linear_damp}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_get_total_linear_damp**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_total_linear_damp>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.total_linear_damp<class_PhysicsDirectBodyState2D_property_total_linear_damp>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**\_get_transform**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_transform>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.transform<class_PhysicsDirectBodyState2D_property_transform>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__get_velocity_at_local_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_velocity_at_local_position**(local_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_velocity_at_local_position>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.get_velocity_at_local_position()<class_PhysicsDirectBodyState2D_method_get_velocity_at_local_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__integrate_forces}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_integrate_forces**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__integrate_forces>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.integrate_forces()<class_PhysicsDirectBodyState2D_method_integrate_forces>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__is_sleeping}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_is_sleeping**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__is_sleeping>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.sleeping<class_PhysicsDirectBodyState2D_property_sleeping>`{.interpreted-text
role="ref"} and its respective getter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__set_angular_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_angular_velocity**(velocity:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_angular_velocity>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.angular_velocity<class_PhysicsDirectBodyState2D_property_angular_velocity>`{.interpreted-text
role="ref"} and its respective setter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__set_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_constant_force**(force:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_constant_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.set_constant_force()<class_PhysicsDirectBodyState2D_method_set_constant_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__set_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_constant_torque**(torque: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_constant_torque>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsDirectBodyState2D.set_constant_torque()<class_PhysicsDirectBodyState2D_method_set_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__set_linear_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_linear_velocity**(velocity:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_linear_velocity>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.linear_velocity<class_PhysicsDirectBodyState2D_property_linear_velocity>`{.interpreted-text
role="ref"} and its respective setter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__set_sleep_state}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_sleep_state**(enabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_sleep_state>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.sleeping<class_PhysicsDirectBodyState2D_property_sleeping>`{.interpreted-text
role="ref"} and its respective setter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectBodyState2DExtension_private_method__set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_transform**(transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_transform>`{.interpreted-text
role="ref"}

Implement to override the behavior of
`PhysicsDirectBodyState2D.transform<class_PhysicsDirectBodyState2D_property_transform>`{.interpreted-text
role="ref"} and its respective setter.
