github_url
:   hide

# SkeletonModification2DLookAt {#class_SkeletonModification2DLookAt}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A modification that rotates a `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} node to look at a target.

::: rst-class
classref-introduction-group
:::

## Description

This
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} rotates a bone to look a target. This is extremely helpful
for moving character\'s head to look at the player, rotating a turret to
look at a target, or any other case where you want to make a bone rotate
towards something quickly and easily.

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

## Property Descriptions

:::: {#class_SkeletonModification2DLookAt_property_bone2d_node}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **bone2d_node**
= `NodePath("")`
`🔗<class_SkeletonModification2DLookAt_property_bone2d_node>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone2d_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_bone2d_node**()

The `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node that the
modification will operate on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_property_bone_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bone_index** = `-1`
`🔗<class_SkeletonModification2DLookAt_property_bone_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_index**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bone_index**()

The index of the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"}
node that the modification will operate on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_property_target_nodepath}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**target_nodepath** = `NodePath("")`
`🔗<class_SkeletonModification2DLookAt_property_target_nodepath>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_target_node**()

The NodePath to the node that is the target for the LookAt modification.
This node is what the modification will rotate the
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} to.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonModification2DLookAt_method_get_additional_rotation}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_additional_rotation**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DLookAt_method_get_additional_rotation>`{.interpreted-text
role="ref"}

Returns the amount of additional rotation that is applied after the
LookAt modification executes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_method_get_constraint_angle_invert}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_constraint_angle_invert**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DLookAt_method_get_constraint_angle_invert>`{.interpreted-text
role="ref"}

Returns whether the constraints to this modification are inverted or
not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_method_get_constraint_angle_max}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_constraint_angle_max**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DLookAt_method_get_constraint_angle_max>`{.interpreted-text
role="ref"}

Returns the constraint\'s maximum allowed angle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_method_get_constraint_angle_min}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_constraint_angle_min**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DLookAt_method_get_constraint_angle_min>`{.interpreted-text
role="ref"}

Returns the constraint\'s minimum allowed angle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_method_get_enable_constraint}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_enable_constraint**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DLookAt_method_get_enable_constraint>`{.interpreted-text
role="ref"}

Returns `true` if the LookAt modification is using constraints.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_method_set_additional_rotation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_additional_rotation**(rotation:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DLookAt_method_set_additional_rotation>`{.interpreted-text
role="ref"}

Sets the amount of additional rotation that is to be applied after
executing the modification. This allows for offsetting the results by
the inputted rotation amount.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_method_set_constraint_angle_invert}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_constraint_angle_invert**(invert:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DLookAt_method_set_constraint_angle_invert>`{.interpreted-text
role="ref"}

When `true`, the modification will use an inverted joint constraint.

An inverted joint constraint only constraints the
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} to the angles
*outside of* the inputted minimum and maximum angles. For this reason,
it is referred to as an inverted joint constraint, as it constraints the
joint to the outside of the inputted values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_method_set_constraint_angle_max}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_constraint_angle_max**(angle_max:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DLookAt_method_set_constraint_angle_max>`{.interpreted-text
role="ref"}

Sets the constraint\'s maximum allowed angle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_method_set_constraint_angle_min}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_constraint_angle_min**(angle_min:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DLookAt_method_set_constraint_angle_min>`{.interpreted-text
role="ref"}

Sets the constraint\'s minimum allowed angle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DLookAt_method_set_enable_constraint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_enable_constraint**(enable_constraint:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DLookAt_method_set_enable_constraint>`{.interpreted-text
role="ref"}

Sets whether this modification will use constraints or not. When `true`,
constraints will be applied when solving the LookAt modification.
