github_url
:   hide

# Skeleton3D {#class_Skeleton3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node containing a bone hierarchy, used to create a 3D skeletal
animation.

::: rst-class
classref-introduction-group
:::

## Description

**Skeleton3D** provides an interface for managing a hierarchy of bones,
including pose, rest and animation (see
`Animation<class_Animation>`{.interpreted-text role="ref"}). It can also
use ragdoll physics.

The overall transform of a bone with respect to the skeleton is
determined by bone pose. Bone rest defines the initial transform of the
bone pose.

Note that \"global pose\" below refers to the overall transform of the
bone with respect to skeleton, so it is not the actual global/world
transform of the bone.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

:::: {#class_Skeleton3D_signal_bone_enabled_changed}
::: rst-class
classref-signal
:::
::::

**bone_enabled_changed**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_signal_bone_enabled_changed>`{.interpreted-text
role="ref"}

Emitted when the bone at `bone_idx` is toggled with
`set_bone_enabled()<class_Skeleton3D_method_set_bone_enabled>`{.interpreted-text
role="ref"}. Use
`is_bone_enabled()<class_Skeleton3D_method_is_bone_enabled>`{.interpreted-text
role="ref"} to check the new value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_signal_bone_list_changed}
::: rst-class
classref-signal
:::
::::

**bone_list_changed**()
`🔗<class_Skeleton3D_signal_bone_list_changed>`{.interpreted-text
role="ref"}

Emitted when the list of bones changes, such as when calling
`add_bone()<class_Skeleton3D_method_add_bone>`{.interpreted-text
role="ref"},
`set_bone_parent()<class_Skeleton3D_method_set_bone_parent>`{.interpreted-text
role="ref"},
`unparent_bone_and_rest()<class_Skeleton3D_method_unparent_bone_and_rest>`{.interpreted-text
role="ref"}, or
`clear_bones()<class_Skeleton3D_method_clear_bones>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_signal_pose_updated}
::: rst-class
classref-signal
:::
::::

**pose_updated**()
`🔗<class_Skeleton3D_signal_pose_updated>`{.interpreted-text role="ref"}

Emitted when the pose is updated.

\*\*Note:\*\* During the update process, this signal is not fired, so
modification by
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} is not detected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_signal_rest_updated}
::: rst-class
classref-signal
:::
::::

**rest_updated**()
`🔗<class_Skeleton3D_signal_rest_updated>`{.interpreted-text role="ref"}

Emitted when the rest is updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_signal_show_rest_only_changed}
::: rst-class
classref-signal
:::
::::

**show_rest_only_changed**()
`🔗<class_Skeleton3D_signal_show_rest_only_changed>`{.interpreted-text
role="ref"}

Emitted when the value of
`show_rest_only<class_Skeleton3D_property_show_rest_only>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_signal_skeleton_updated}
::: rst-class
classref-signal
:::
::::

**skeleton_updated**()
`🔗<class_Skeleton3D_signal_skeleton_updated>`{.interpreted-text
role="ref"}

Emitted when the final pose has been calculated will be applied to the
skin in the update process.

This means that all
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} processing is complete. In order to detect the completion of
the processing of each
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"}, use
`SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Skeleton3D_ModifierCallbackModeProcess}
::: rst-class
classref-enumeration
:::
::::

enum **ModifierCallbackModeProcess**:
`🔗<enum_Skeleton3D_ModifierCallbackModeProcess>`{.interpreted-text
role="ref"}

:::: {#class_Skeleton3D_constant_MODIFIER_CALLBACK_MODE_PROCESS_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>`{.interpreted-text
role="ref"} **MODIFIER_CALLBACK_MODE_PROCESS_PHYSICS** = `0`

Set a flag to process modification during physics frames (see
`Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}).

:::: {#class_Skeleton3D_constant_MODIFIER_CALLBACK_MODE_PROCESS_IDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>`{.interpreted-text
role="ref"} **MODIFIER_CALLBACK_MODE_PROCESS_IDLE** = `1`

Set a flag to process modification during process frames (see
`Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`{.interpreted-text
role="ref"}).

:::: {#class_Skeleton3D_constant_MODIFIER_CALLBACK_MODE_PROCESS_MANUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>`{.interpreted-text
role="ref"} **MODIFIER_CALLBACK_MODE_PROCESS_MANUAL** = `2`

Do not process modification. Use
`advance()<class_Skeleton3D_method_advance>`{.interpreted-text
role="ref"} to process the modification manually.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Skeleton3D_constant_NOTIFICATION_UPDATE_SKELETON}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_UPDATE_SKELETON** = `50`
`🔗<class_Skeleton3D_constant_NOTIFICATION_UPDATE_SKELETON>`{.interpreted-text
role="ref"}

Notification received when this skeleton\'s pose needs to be updated. In
that case, this is called only once per frame in a deferred process.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Skeleton3D_property_animate_physical_bones}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**animate_physical_bones** = `true`
`🔗<class_Skeleton3D_property_animate_physical_bones>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_animate_physical_bones**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_animate_physical_bones**()

**Deprecated:** This property may be changed or removed in future
versions.

If you follow the recommended workflow and explicitly have
`PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>`{.interpreted-text
role="ref"} as a child of **Skeleton3D**, you can control whether it is
affected by raycasting without running
`physical_bones_start_simulation()<class_Skeleton3D_method_physical_bones_start_simulation>`{.interpreted-text
role="ref"}, by its
`SkeletonModifier3D.active<class_SkeletonModifier3D_property_active>`{.interpreted-text
role="ref"}.

However, for old (deprecated) configurations, **Skeleton3D** has an
internal virtual
`PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>`{.interpreted-text
role="ref"} for compatibility. This property controls the internal
virtual
`PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>`{.interpreted-text
role="ref"}\'s
`SkeletonModifier3D.active<class_SkeletonModifier3D_property_active>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_property_modifier_callback_mode_process}
::: rst-class
classref-property
:::
::::

`ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>`{.interpreted-text
role="ref"} **modifier_callback_mode_process** = `1`
`🔗<class_Skeleton3D_property_modifier_callback_mode_process>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modifier_callback_mode_process**(value:
  `ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>`{.interpreted-text
  role="ref"})
- `ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>`{.interpreted-text
  role="ref"} **get_modifier_callback_mode_process**()

Sets the processing timing for the Modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_property_motion_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **motion_scale** =
`1.0` `🔗<class_Skeleton3D_property_motion_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_motion_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_motion_scale**()

Multiplies the 3D position track animation.

\*\*Note:\*\* Unless this value is `1.0`, the key value in animation
will not match the actual position value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_property_show_rest_only}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_rest_only** =
`false` `🔗<class_Skeleton3D_property_show_rest_only>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_rest_only**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_show_rest_only**()

If `true`, forces the bones in their default rest pose, regardless of
their values. In the editor, this also prevents the bones from being
edited.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Skeleton3D_method_add_bone}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_bone**(name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_Skeleton3D_method_add_bone>`{.interpreted-text role="ref"}

Adds a new bone with the given name. Returns the new bone\'s index, or
`-1` if this method fails.

\*\*Note:\*\* Bone names should be unique, non empty, and cannot include
the `:` and `/` characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_advance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**advance**(delta: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Skeleton3D_method_advance>`{.interpreted-text role="ref"}

Manually advance the child
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"}s by the specified time (in seconds).

\*\*Note:\*\* The `delta` is temporarily accumulated in the
**Skeleton3D**, and the deferred process uses the accumulated value to
process the modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_clear_bones}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_bones**()
`🔗<class_Skeleton3D_method_clear_bones>`{.interpreted-text role="ref"}

Clear all the bones in this skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_clear_bones_global_pose_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_bones_global_pose_override**()
`🔗<class_Skeleton3D_method_clear_bones_global_pose_override>`{.interpreted-text
role="ref"}

**Deprecated:** This method may be changed or removed in future
versions.

Removes the global pose override on all bones in the skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_create_skin_from_rest_transforms}
::: rst-class
classref-method
:::
::::

`Skin<class_Skin>`{.interpreted-text role="ref"}
**create_skin_from_rest_transforms**()
`🔗<class_Skeleton3D_method_create_skin_from_rest_transforms>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_find_bone}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find_bone**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Skeleton3D_method_find_bone>`{.interpreted-text
role="ref"}

Returns the bone index that matches `name` as its name. Returns `-1` if
no bone with this name exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_force_update_all_bone_transforms}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_update_all_bone_transforms**()
`🔗<class_Skeleton3D_method_force_update_all_bone_transforms>`{.interpreted-text
role="ref"}

**Deprecated:** This method should only be called internally.

Force updates the bone transforms/poses for all bones in the skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_force_update_bone_child_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_update_bone_child_transform**(bone_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Skeleton3D_method_force_update_bone_child_transform>`{.interpreted-text
role="ref"}

Force updates the bone transform for the bone at `bone_idx` and all of
its children.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_children}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_bone_children**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_children>`{.interpreted-text
role="ref"}

Returns an array containing the bone indexes of all the child node of
the passed in bone, `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_bone_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_count>`{.interpreted-text
role="ref"}

Returns the number of bones in the skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_global_pose}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_bone_global_pose**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_global_pose>`{.interpreted-text
role="ref"}

Returns the overall transform of the specified bone, with respect to the
skeleton. Being relative to the skeleton frame, this is not the actual
\"global\" transform of the bone.

\*\*Note:\*\* This is the global pose you set to the skeleton in the
process, the final global pose can get overridden by modifiers in the
deferred process, if you want to access the final global pose, use
`SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_global_pose_no_override}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_bone_global_pose_no_override**(bone_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_global_pose_no_override>`{.interpreted-text
role="ref"}

**Deprecated:** This method may be changed or removed in future
versions.

Returns the overall transform of the specified bone, with respect to the
skeleton, but without any global pose overrides. Being relative to the
skeleton frame, this is not the actual \"global\" transform of the bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_global_pose_override}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_bone_global_pose_override**(bone_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_global_pose_override>`{.interpreted-text
role="ref"}

**Deprecated:** This method may be changed or removed in future
versions.

Returns the global pose override transform for `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_global_rest}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_bone_global_rest**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_global_rest>`{.interpreted-text
role="ref"}

Returns the global rest transform for `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_meta}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_bone_meta**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, key: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_meta>`{.interpreted-text
role="ref"}

Returns the metadata for the bone at index `bone_idx` with `key`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_meta_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_bone_meta_list**(bone_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_meta_list>`{.interpreted-text
role="ref"}

Returns the list of all metadata keys for the bone at index `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_bone_name**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_name>`{.interpreted-text
role="ref"}

Returns the name of the bone at index `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_parent}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_bone_parent**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_parent>`{.interpreted-text
role="ref"}

Returns the bone index which is the parent of the bone at `bone_idx`. If
-1, then bone has no parent.

\*\*Note:\*\* The parent bone returned will always be less than
`bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_pose}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_bone_pose**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_pose>`{.interpreted-text
role="ref"}

Returns the pose transform of the specified bone.

\*\*Note:\*\* This is the pose you set to the skeleton in the process,
the final pose can get overridden by modifiers in the deferred process,
if you want to access the final pose, use
`SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_pose_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_bone_pose_position**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_pose_position>`{.interpreted-text
role="ref"}

Returns the pose position of the bone at `bone_idx`. The returned
`Vector3<class_Vector3>`{.interpreted-text role="ref"} is in the local
coordinate space of the **Skeleton3D** node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_pose_rotation}
::: rst-class
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**get_bone_pose_rotation**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_pose_rotation>`{.interpreted-text
role="ref"}

Returns the pose rotation of the bone at `bone_idx`. The returned
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} is local to
the bone with respect to the rotation of any parent bones.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_pose_scale}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_bone_pose_scale**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_pose_scale>`{.interpreted-text
role="ref"}

Returns the pose scale of the bone at `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_bone_rest}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_bone_rest**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_bone_rest>`{.interpreted-text
role="ref"}

Returns the rest transform for a bone `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_concatenated_bone_names}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_concatenated_bone_names**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_concatenated_bone_names>`{.interpreted-text
role="ref"}

Returns all bone names concatenated with commas (`,`) as a single
`StringName<class_StringName>`{.interpreted-text role="ref"}.

It is useful to set it as a hint for the enum property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_parentless_bones}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_parentless_bones**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_get_parentless_bones>`{.interpreted-text
role="ref"}

Returns an array with all of the bones that are parentless. Another way
to look at this is that it returns the indexes of all the bones that are
not dependent or modified by other bones in the Skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_get_version}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_version**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Skeleton3D_method_get_version>`{.interpreted-text
role="ref"}

Returns the number of times the bone hierarchy has changed within this
skeleton, including renames.

The Skeleton version is not serialized: only use within a single
instance of Skeleton3D.

Use for invalidating caches in IK solvers and other nodes which process
bones.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_has_bone_meta}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_bone_meta**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, key: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_has_bone_meta>`{.interpreted-text
role="ref"}

Returns `true` if the bone at index `bone_idx` has metadata with the key
`key`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_is_bone_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_bone_enabled**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Skeleton3D_method_is_bone_enabled>`{.interpreted-text
role="ref"}

Returns whether the bone pose for the bone at `bone_idx` is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_localize_rests}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**localize_rests**()
`🔗<class_Skeleton3D_method_localize_rests>`{.interpreted-text
role="ref"}

Returns all bones in the skeleton to their rest poses.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_physical_bones_add_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**physical_bones_add_collision_exception**(exception:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_Skeleton3D_method_physical_bones_add_collision_exception>`{.interpreted-text
role="ref"}

**Deprecated:** This method may be changed or removed in future
versions.

Adds a collision exception to the physical bone.

Works just like the `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_physical_bones_remove_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**physical_bones_remove_collision_exception**(exception:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_Skeleton3D_method_physical_bones_remove_collision_exception>`{.interpreted-text
role="ref"}

**Deprecated:** This method may be changed or removed in future
versions.

Removes a collision exception to the physical bone.

Works just like the `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_physical_bones_start_simulation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**physical_bones_start_simulation**(bones:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] = \[\])
`🔗<class_Skeleton3D_method_physical_bones_start_simulation>`{.interpreted-text
role="ref"}

**Deprecated:** This method may be changed or removed in future
versions.

Tells the `PhysicalBone3D<class_PhysicalBone3D>`{.interpreted-text
role="ref"} nodes in the Skeleton to start simulating and reacting to
the physics world.

Optionally, a list of bone names can be passed-in, allowing only the
passed-in bones to be simulated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_physical_bones_stop_simulation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**physical_bones_stop_simulation**()
`🔗<class_Skeleton3D_method_physical_bones_stop_simulation>`{.interpreted-text
role="ref"}

**Deprecated:** This method may be changed or removed in future
versions.

Tells the `PhysicalBone3D<class_PhysicalBone3D>`{.interpreted-text
role="ref"} nodes in the Skeleton to stop simulating.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_register_skin}
::: rst-class
classref-method
:::
::::

`SkinReference<class_SkinReference>`{.interpreted-text role="ref"}
**register_skin**(skin: `Skin<class_Skin>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_register_skin>`{.interpreted-text
role="ref"}

Binds the given Skin to the Skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_reset_bone_pose}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reset_bone_pose**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_reset_bone_pose>`{.interpreted-text
role="ref"}

Sets the bone pose to rest for `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_reset_bone_poses}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reset_bone_poses**()
`🔗<class_Skeleton3D_method_reset_bone_poses>`{.interpreted-text
role="ref"}

Sets all bone poses to rests.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_enabled**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"} =
true) `🔗<class_Skeleton3D_method_set_bone_enabled>`{.interpreted-text
role="ref"}

Disables the pose for the bone at `bone_idx` if `false`, enables the
bone pose if `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_global_pose}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_global_pose**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, pose: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_set_bone_global_pose>`{.interpreted-text
role="ref"}

Sets the global pose transform, `pose`, for the bone at `bone_idx`.

\*\*Note:\*\* If other bone poses have been changed, this method
executes a dirty poses recalculation and will cause performance to
deteriorate. If you know that multiple global poses will be applied,
consider using
`set_bone_pose()<class_Skeleton3D_method_set_bone_pose>`{.interpreted-text
role="ref"} with precalculation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_global_pose_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_global_pose_override**(bone_idx:
`int<class_int>`{.interpreted-text role="ref"}, pose:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}, amount:
`float<class_float>`{.interpreted-text role="ref"}, persistent:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Skeleton3D_method_set_bone_global_pose_override>`{.interpreted-text
role="ref"}

**Deprecated:** This method may be changed or removed in future
versions.

Sets the global pose transform, `pose`, for the bone at `bone_idx`.

`amount` is the interpolation strength that will be used when applying
the pose, and `persistent` determines if the applied pose will remain.

\*\*Note:\*\* The pose transform needs to be a global pose! To convert a
world transform from a `Node3D<class_Node3D>`{.interpreted-text
role="ref"} to a global bone pose, multiply the
`Transform3D.affine_inverse()<class_Transform3D_method_affine_inverse>`{.interpreted-text
role="ref"} of the node\'s
`Node3D.global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} by the desired world transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_meta}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_meta**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, key: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_set_bone_meta>`{.interpreted-text
role="ref"}

Sets the metadata for the bone at index `bone_idx`, setting the `key`
meta to `value`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_name**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_Skeleton3D_method_set_bone_name>`{.interpreted-text
role="ref"}

Sets the bone name, `name`, for the bone at `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_parent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_parent**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, parent_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Skeleton3D_method_set_bone_parent>`{.interpreted-text
role="ref"}

Sets the bone index `parent_idx` as the parent of the bone at
`bone_idx`. If -1, then bone has no parent.

\*\*Note:\*\* `parent_idx` must be less than `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_pose}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_pose**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, pose: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_set_bone_pose>`{.interpreted-text
role="ref"}

Sets the pose transform, `pose`, for the bone at `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_pose_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_pose_position**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_set_bone_pose_position>`{.interpreted-text
role="ref"}

Sets the pose position of the bone at `bone_idx` to `position`.
`position` is a `Vector3<class_Vector3>`{.interpreted-text role="ref"}
describing a position local to the **Skeleton3D** node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_pose_rotation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_pose_rotation**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, rotation: `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_set_bone_pose_rotation>`{.interpreted-text
role="ref"}

Sets the pose rotation of the bone at `bone_idx` to `rotation`.
`rotation` is a `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"} describing a rotation in the bone\'s local coordinate space
with respect to the rotation of any parent bones.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_pose_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_pose_scale**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, scale: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_set_bone_pose_scale>`{.interpreted-text
role="ref"}

Sets the pose scale of the bone at `bone_idx` to `scale`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_set_bone_rest}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_rest**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"}, rest: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_set_bone_rest>`{.interpreted-text
role="ref"}

Sets the rest transform for bone `bone_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Skeleton3D_method_unparent_bone_and_rest}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unparent_bone_and_rest**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Skeleton3D_method_unparent_bone_and_rest>`{.interpreted-text
role="ref"}

Unparents the bone at `bone_idx` and sets its rest position to that of
its parent prior to being reset.
