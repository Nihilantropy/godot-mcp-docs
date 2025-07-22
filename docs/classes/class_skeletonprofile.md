github_url
:   hide

# SkeletonProfile {#class_SkeletonProfile}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>`{.interpreted-text
role="ref"}

Base class for a profile of a virtual skeleton used as a target for
retargeting.

::: rst-class
classref-introduction-group
:::

## Description

This resource is used in
`EditorScenePostImport<class_EditorScenePostImport>`{.interpreted-text
role="ref"}. Some parameters are referring to bones in
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"},
`Skin<class_Skin>`{.interpreted-text role="ref"},
`Animation<class_Animation>`{.interpreted-text role="ref"}, and some
other nodes are rewritten based on the parameters of
**SkeletonProfile**.

\*\*Note:\*\* These parameters need to be set only when creating a
custom profile. In
`SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>`{.interpreted-text
role="ref"}, they are defined internally as read-only values.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Retargeting 3D Skeletons <../tutorials/assets_pipeline/retargeting_3d_skeletons>`{.interpreted-text
  role="doc"}

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

:::: {#class_SkeletonProfile_signal_profile_updated}
::: rst-class
classref-signal
:::
::::

**profile_updated**()
`🔗<class_SkeletonProfile_signal_profile_updated>`{.interpreted-text
role="ref"}

This signal is emitted when change the value in profile. This is used to
update key name in the `BoneMap<class_BoneMap>`{.interpreted-text
role="ref"} and to redraw the `BoneMap<class_BoneMap>`{.interpreted-text
role="ref"} editor.

\*\*Note:\*\* This signal is not connected directly to editor to
simplify the reference, instead it is passed on to editor through the
`BoneMap<class_BoneMap>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_SkeletonProfile_TailDirection}
::: rst-class
classref-enumeration
:::
::::

enum **TailDirection**:
`🔗<enum_SkeletonProfile_TailDirection>`{.interpreted-text role="ref"}

:::: {#class_SkeletonProfile_constant_TAIL_DIRECTION_AVERAGE_CHILDREN}
::: rst-class
classref-enumeration-constant
:::
::::

`TailDirection<enum_SkeletonProfile_TailDirection>`{.interpreted-text
role="ref"} **TAIL_DIRECTION_AVERAGE_CHILDREN** = `0`

Direction to the average coordinates of bone children.

:::: {#class_SkeletonProfile_constant_TAIL_DIRECTION_SPECIFIC_CHILD}
::: rst-class
classref-enumeration-constant
:::
::::

`TailDirection<enum_SkeletonProfile_TailDirection>`{.interpreted-text
role="ref"} **TAIL_DIRECTION_SPECIFIC_CHILD** = `1`

Direction to the coordinates of specified bone child.

:::: {#class_SkeletonProfile_constant_TAIL_DIRECTION_END}
::: rst-class
classref-enumeration-constant
:::
::::

`TailDirection<enum_SkeletonProfile_TailDirection>`{.interpreted-text
role="ref"} **TAIL_DIRECTION_END** = `2`

Direction is not calculated.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SkeletonProfile_property_bone_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bone_size** = `0`
`🔗<class_SkeletonProfile_property_bone_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bone_size**()

The amount of bones in retargeting section\'s
`BoneMap<class_BoneMap>`{.interpreted-text role="ref"} editor. For
example,
`SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>`{.interpreted-text
role="ref"} has 56 bones.

The size of elements in `BoneMap<class_BoneMap>`{.interpreted-text
role="ref"} updates when changing this property in it\'s assigned
**SkeletonProfile**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_property_group_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **group_size** = `0`
`🔗<class_SkeletonProfile_property_group_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_group_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_group_size**()

The amount of groups of bones in retargeting section\'s
`BoneMap<class_BoneMap>`{.interpreted-text role="ref"} editor. For
example,
`SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>`{.interpreted-text
role="ref"} has 4 groups.

This property exists to separate the bone list into several sections in
the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_property_root_bone}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**root_bone** = `&""`
`🔗<class_SkeletonProfile_property_root_bone>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_bone**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_root_bone**()

A bone name that will be used as the root bone in
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}. This
should be the bone of the parent of hips that exists at the world
origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_property_scale_base_bone}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**scale_base_bone** = `&""`
`🔗<class_SkeletonProfile_property_scale_base_bone>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scale_base_bone**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_scale_base_bone**()

A bone name which will use model\'s height as the coefficient for
normalization. For example,
`SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>`{.interpreted-text
role="ref"} defines it as `Hips`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonProfile_method_find_bone}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find_bone**(bone_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_find_bone>`{.interpreted-text
role="ref"}

Returns the bone index that matches `bone_name` as its name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_get_bone_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_bone_name**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_get_bone_name>`{.interpreted-text
role="ref"}

Returns the name of the bone at `bone_idx` that will be the key name in
the `BoneMap<class_BoneMap>`{.interpreted-text role="ref"}.

In the retargeting process, the returned bone name is the bone name of
the target skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_get_bone_parent}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_bone_parent**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_get_bone_parent>`{.interpreted-text
role="ref"}

Returns the name of the bone which is the parent to the bone at
`bone_idx`. The result is empty if the bone has no parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_get_bone_tail}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_bone_tail**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_get_bone_tail>`{.interpreted-text
role="ref"}

Returns the name of the bone which is the tail of the bone at
`bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_get_group}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_group**(bone_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_get_group>`{.interpreted-text
role="ref"}

Returns the group of the bone at `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_get_group_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_group_name**(group_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_get_group_name>`{.interpreted-text
role="ref"}

Returns the name of the group at `group_idx` that will be the drawing
group in the `BoneMap<class_BoneMap>`{.interpreted-text role="ref"}
editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_get_handle_offset}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_handle_offset**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_get_handle_offset>`{.interpreted-text
role="ref"}

Returns the offset of the bone at `bone_idx` that will be the button
position in the `BoneMap<class_BoneMap>`{.interpreted-text role="ref"}
editor.

This is the offset with origin at the top left corner of the square.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_get_reference_pose}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_reference_pose**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_get_reference_pose>`{.interpreted-text
role="ref"}

Returns the reference pose transform for bone `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_get_tail_direction}
::: rst-class
classref-method
:::
::::

`TailDirection<enum_SkeletonProfile_TailDirection>`{.interpreted-text
role="ref"} **get_tail_direction**(bone_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_get_tail_direction>`{.interpreted-text
role="ref"}

Returns the tail direction of the bone at `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_get_texture}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_texture**(group_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_get_texture>`{.interpreted-text
role="ref"}

Returns the texture of the group at `group_idx` that will be the drawing
group background image in the `BoneMap<class_BoneMap>`{.interpreted-text
role="ref"} editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_is_required}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_required**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonProfile_method_is_required>`{.interpreted-text
role="ref"}

Returns whether the bone at `bone_idx` is required for retargeting.

This value is used by the bone map editor. If this method returns
`true`, and no bone is assigned, the handle color will be red on the
bone map editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_bone_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_name**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, bone_name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonProfile_method_set_bone_name>`{.interpreted-text
role="ref"}

Sets the name of the bone at `bone_idx` that will be the key name in the
`BoneMap<class_BoneMap>`{.interpreted-text role="ref"}.

In the retargeting process, the setting bone name is the bone name of
the target skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_bone_parent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_parent**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, bone_parent:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_SkeletonProfile_method_set_bone_parent>`{.interpreted-text
role="ref"}

Sets the bone with name `bone_parent` as the parent of the bone at
`bone_idx`. If an empty string is passed, then the bone has no parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_bone_tail}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_tail**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, bone_tail: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonProfile_method_set_bone_tail>`{.interpreted-text
role="ref"}

Sets the bone with name `bone_tail` as the tail of the bone at
`bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_group**(bone_idx: `int<class_int>`{.interpreted-text role="ref"},
group: `StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_SkeletonProfile_method_set_group>`{.interpreted-text
role="ref"}

Sets the group of the bone at `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_group_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_group_name**(group_idx: `int<class_int>`{.interpreted-text
role="ref"}, group_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_SkeletonProfile_method_set_group_name>`{.interpreted-text
role="ref"}

Sets the name of the group at `group_idx` that will be the drawing group
in the `BoneMap<class_BoneMap>`{.interpreted-text role="ref"} editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_handle_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_handle_offset**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, handle_offset: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonProfile_method_set_handle_offset>`{.interpreted-text
role="ref"}

Sets the offset of the bone at `bone_idx` that will be the button
position in the `BoneMap<class_BoneMap>`{.interpreted-text role="ref"}
editor.

This is the offset with origin at the top left corner of the square.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_reference_pose}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_reference_pose**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, bone_name:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_SkeletonProfile_method_set_reference_pose>`{.interpreted-text
role="ref"}

Sets the reference pose transform for bone `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_required}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_required**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, required: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonProfile_method_set_required>`{.interpreted-text
role="ref"}

Sets the required status for bone `bone_idx` to `required`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_tail_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tail_direction**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, tail_direction:
`TailDirection<enum_SkeletonProfile_TailDirection>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonProfile_method_set_tail_direction>`{.interpreted-text
role="ref"}

Sets the tail direction of the bone at `bone_idx`.

\*\*Note:\*\* This only specifies the method of calculation. The actual
coordinates required should be stored in an external skeleton, so the
calculation itself needs to be done externally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonProfile_method_set_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_texture**(group_idx: `int<class_int>`{.interpreted-text
role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonProfile_method_set_texture>`{.interpreted-text
role="ref"}

Sets the texture of the group at `group_idx` that will be the drawing
group background image in the `BoneMap<class_BoneMap>`{.interpreted-text
role="ref"} editor.
