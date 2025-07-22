github_url
:   hide

# BoneMap {#class_BoneMap}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Describes a mapping of bone names for retargeting
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} into common
names defined by a
`SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This class contains a dictionary that uses a list of bone names in
`SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}
as key names.

By assigning the actual `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} bone name as the key value, it maps the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} to the
`SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}.

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

:::: {#class_BoneMap_signal_bone_map_updated}
::: rst-class
classref-signal
:::
::::

**bone_map_updated**()
`🔗<class_BoneMap_signal_bone_map_updated>`{.interpreted-text
role="ref"}

This signal is emitted when change the key value in the **BoneMap**.
This is used to validate mapping and to update **BoneMap** editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneMap_signal_profile_updated}
::: rst-class
classref-signal
:::
::::

**profile_updated**()
`🔗<class_BoneMap_signal_profile_updated>`{.interpreted-text role="ref"}

This signal is emitted when change the value in profile or change the
reference of profile. This is used to update key names in the
**BoneMap** and to redraw the **BoneMap** editor.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_BoneMap_property_profile}
::: rst-class
classref-property
:::
::::

`SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}
**profile** `🔗<class_BoneMap_property_profile>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_profile**(value:
  `SkeletonProfile<class_SkeletonProfile>`{.interpreted-text
  role="ref"})
- `SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}
  **get_profile**()

A `SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}
of the mapping target. Key names in the **BoneMap** are synchronized
with it.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_BoneMap_method_find_profile_bone_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**find_profile_bone_name**(skeleton_bone_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BoneMap_method_find_profile_bone_name>`{.interpreted-text
role="ref"}

Returns a profile bone name having `skeleton_bone_name`. If not found,
an empty `StringName<class_StringName>`{.interpreted-text role="ref"}
will be returned.

In the retargeting process, the returned bone name is the bone name of
the target skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneMap_method_get_skeleton_bone_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_skeleton_bone_name**(profile_bone_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BoneMap_method_get_skeleton_bone_name>`{.interpreted-text
role="ref"}

Returns a skeleton bone name is mapped to `profile_bone_name`.

In the retargeting process, the returned bone name is the bone name of
the source skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneMap_method_set_skeleton_bone_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_skeleton_bone_name**(profile_bone_name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
skeleton_bone_name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_BoneMap_method_set_skeleton_bone_name>`{.interpreted-text
role="ref"}

Maps a skeleton bone name to `profile_bone_name`.

In the retargeting process, the setting bone name is the bone name of
the source skeleton.
