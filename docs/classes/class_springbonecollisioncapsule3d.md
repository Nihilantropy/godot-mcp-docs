github_url
:   hide

# SpringBoneCollisionCapsule3D {#class_SpringBoneCollisionCapsule3D}

**Inherits:**
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A capsule shape collision that interacts with
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A capsule shape collision that interacts with
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"}.

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

:::: {#class_SpringBoneCollisionCapsule3D_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `0.5`
`🔗<class_SpringBoneCollisionCapsule3D_property_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

The capsule\'s full height, including the hemispheres.

\*\*Note:\*\* The
`height<class_SpringBoneCollisionCapsule3D_property_height>`{.interpreted-text
role="ref"} of a capsule must be at least twice its
`radius<class_SpringBoneCollisionCapsule3D_property_radius>`{.interpreted-text
role="ref"}. Otherwise, the capsule becomes a sphere. If the
`height<class_SpringBoneCollisionCapsule3D_property_height>`{.interpreted-text
role="ref"} is less than twice the
`radius<class_SpringBoneCollisionCapsule3D_property_radius>`{.interpreted-text
role="ref"}, the properties adjust to a valid value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneCollisionCapsule3D_property_inside}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **inside** = `false`
`🔗<class_SpringBoneCollisionCapsule3D_property_inside>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inside**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_inside**()

If `true`, the collision acts to trap the joint within the collision.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneCollisionCapsule3D_property_mid_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mid_height**
`🔗<class_SpringBoneCollisionCapsule3D_property_mid_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mid_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_mid_height**()

The capsule\'s height, excluding the hemispheres. This is the height of
the central cylindrical part in the middle of the capsule, and is the
distance between the centers of the two hemispheres. This is a wrapper
for
`height<class_SpringBoneCollisionCapsule3D_property_height>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneCollisionCapsule3D_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.1`
`🔗<class_SpringBoneCollisionCapsule3D_property_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The capsule\'s radius.

\*\*Note:\*\* The
`radius<class_SpringBoneCollisionCapsule3D_property_radius>`{.interpreted-text
role="ref"} of a capsule cannot be greater than half of its
`height<class_SpringBoneCollisionCapsule3D_property_height>`{.interpreted-text
role="ref"}. Otherwise, the capsule becomes a sphere. If the
`radius<class_SpringBoneCollisionCapsule3D_property_radius>`{.interpreted-text
role="ref"} is greater than half of the
`height<class_SpringBoneCollisionCapsule3D_property_height>`{.interpreted-text
role="ref"}, the properties adjust to a valid value.
