github_url
:   hide

# PhysicsMaterial {#class_PhysicsMaterial}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Holds physics-related properties of a surface, namely its roughness and
bounciness.

::: rst-class
classref-introduction-group
:::

## Description

Holds physics-related properties of a surface, namely its roughness and
bounciness. This class is used to apply these properties to a physics
body.

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

:::: {#class_PhysicsMaterial_property_absorbent}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **absorbent** = `false`
`🔗<class_PhysicsMaterial_property_absorbent>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_absorbent**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_absorbent**()

If `true`, subtracts the bounciness from the colliding object\'s
bounciness instead of adding it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsMaterial_property_bounce}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bounce** = `0.0`
`🔗<class_PhysicsMaterial_property_bounce>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bounce**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_bounce**()

The body\'s bounciness. Values range from `0` (no bounce) to `1` (full
bounciness).

\*\*Note:\*\* Even with
`bounce<class_PhysicsMaterial_property_bounce>`{.interpreted-text
role="ref"} set to `1.0`, some energy will be lost over time due to
linear and angular damping. To have a physics body that preserves all
its energy over time, set
`bounce<class_PhysicsMaterial_property_bounce>`{.interpreted-text
role="ref"} to `1.0`, the body\'s linear damp mode to **Replace** (if
applicable), its linear damp to `0.0`, its angular damp mode to
**Replace** (if applicable), and its angular damp to `0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsMaterial_property_friction}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **friction** = `1.0`
`🔗<class_PhysicsMaterial_property_friction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_friction**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_friction**()

The body\'s friction. Values range from `0` (frictionless) to `1`
(maximum friction).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsMaterial_property_rough}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **rough** = `false`
`🔗<class_PhysicsMaterial_property_rough>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rough**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_rough**()

If `true`, the physics engine will use the friction of the object marked
as \"rough\" when two objects collide. If `false`, the physics engine
will use the lowest friction of all colliding objects instead. If `true`
for both colliding objects, the physics engine will use the highest
friction.
