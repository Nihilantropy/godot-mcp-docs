github_url
:   hide

# SpringBoneCollision3D {#class_SpringBoneCollision3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`SpringBoneCollisionCapsule3D<class_SpringBoneCollisionCapsule3D>`{.interpreted-text
role="ref"},
`SpringBoneCollisionPlane3D<class_SpringBoneCollisionPlane3D>`{.interpreted-text
role="ref"},
`SpringBoneCollisionSphere3D<class_SpringBoneCollisionSphere3D>`{.interpreted-text
role="ref"}

A base class of the collision that interacts with
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A collision can be a child of
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"}. If it is not a child of
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"}, it has no effect.

The colliding and sliding are done in the
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"}\'s modification process in order of its collision list which
is set by
`SpringBoneSimulator3D.set_collision_path()<class_SpringBoneSimulator3D_method_set_collision_path>`{.interpreted-text
role="ref"}. If
`SpringBoneSimulator3D.are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>`{.interpreted-text
role="ref"} is `true`, the order matches
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}.

If `bone<class_SpringBoneCollision3D_property_bone>`{.interpreted-text
role="ref"} is set, it synchronizes with the bone pose of the ancestor
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}, which is
done in before the
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"}\'s modification process as the pre-process.

\*\*Warning:\*\* A scaled **SpringBoneCollision3D** will likely not
behave as expected. Make sure that the parent
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} and its
bones are not scaled.

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

:::: {#class_SpringBoneCollision3D_property_bone}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bone** = `-1`
`🔗<class_SpringBoneCollision3D_property_bone>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bone**()

The index of the attached bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneCollision3D_property_bone_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **bone_name** =
`""`
`🔗<class_SpringBoneCollision3D_property_bone_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_bone_name**()

The name of the attached bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneCollision3D_property_position_offset}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**position_offset**
`🔗<class_SpringBoneCollision3D_property_position_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position_offset**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_position_offset**()

The offset of the position from
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}\'s
`bone<class_SpringBoneCollision3D_property_bone>`{.interpreted-text
role="ref"} pose position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringBoneCollision3D_property_rotation_offset}
::: rst-class
classref-property
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**rotation_offset**
`🔗<class_SpringBoneCollision3D_property_rotation_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_offset**(value:
  `Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
- `Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
  **get_rotation_offset**()

The offset of the rotation from
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}\'s
`bone<class_SpringBoneCollision3D_property_bone>`{.interpreted-text
role="ref"} pose rotation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SpringBoneCollision3D_method_get_skeleton}
::: rst-class
classref-method
:::
::::

`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
**get_skeleton**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpringBoneCollision3D_method_get_skeleton>`{.interpreted-text
role="ref"}

Get parent `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
node of the parent
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"} if found.
