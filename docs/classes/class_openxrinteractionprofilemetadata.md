github_url
:   hide

# OpenXRInteractionProfileMetadata {#class_OpenXRInteractionProfileMetadata}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Meta class registering supported devices in OpenXR.

::: rst-class
classref-introduction-group
:::

## Description

This class allows OpenXR core and extensions to register metadata
relating to supported interaction devices such as controllers, trackers,
haptic devices, etc. It is primarily used by the action map editor and
to sanitize any action map by removing extension-dependent entries when
applicable.

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

:::: {#class_OpenXRInteractionProfileMetadata_method_register_interaction_profile}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_interaction_profile**(display_name:
`String<class_String>`{.interpreted-text role="ref"}, openxr_path:
`String<class_String>`{.interpreted-text role="ref"},
openxr_extension_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRInteractionProfileMetadata_method_register_interaction_profile>`{.interpreted-text
role="ref"}

Registers an interaction profile using its OpenXR designation (e.g.
`/interaction_profiles/khr/simple_controller` is the profile for
OpenXR\'s simple controller profile).

`display_name` is the description shown to the user. `openxr_path` is
the interaction profile path being registered. `openxr_extension_name`
optionally restricts this profile to the given extension being
enabled/available. If the extension is not available, the profile and
all related entries used in an action map are filtered out.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInteractionProfileMetadata_method_register_io_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_io_path**(interaction_profile:
`String<class_String>`{.interpreted-text role="ref"}, display_name:
`String<class_String>`{.interpreted-text role="ref"}, toplevel_path:
`String<class_String>`{.interpreted-text role="ref"}, openxr_path:
`String<class_String>`{.interpreted-text role="ref"},
openxr_extension_name: `String<class_String>`{.interpreted-text
role="ref"}, action_type:
`ActionType<enum_OpenXRAction_ActionType>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRInteractionProfileMetadata_method_register_io_path>`{.interpreted-text
role="ref"}

Registers an input/output path for the given `interaction_profile`. The
profile should previously have been registered using
`register_interaction_profile()<class_OpenXRInteractionProfileMetadata_method_register_interaction_profile>`{.interpreted-text
role="ref"}. `display_name` is the description shown to the user.
`toplevel_path` specifies the bind path this input/output can be bound
to (e.g. `/user/hand/left` or `/user/hand/right`). `openxr_path` is the
action input/output being registered (e.g.
`/user/hand/left/input/aim/pose`). `openxr_extension_name` restricts
this input/output to an enabled/available extension, this doesn\'t need
to repeat the extension on the profile but relates to overlapping
extension (e.g. `XR_EXT_palm_pose` that introduces
`…/input/palm_ext/pose` input paths). `action_type` defines the type of
input or output provided by OpenXR.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInteractionProfileMetadata_method_register_profile_rename}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_profile_rename**(old_name:
`String<class_String>`{.interpreted-text role="ref"}, new_name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_OpenXRInteractionProfileMetadata_method_register_profile_rename>`{.interpreted-text
role="ref"}

Allows for renaming old interaction profile paths to new paths to
maintain backwards compatibility with older action maps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInteractionProfileMetadata_method_register_top_level_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_top_level_path**(display_name:
`String<class_String>`{.interpreted-text role="ref"}, openxr_path:
`String<class_String>`{.interpreted-text role="ref"},
openxr_extension_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRInteractionProfileMetadata_method_register_top_level_path>`{.interpreted-text
role="ref"}

Registers a top level path to which profiles can be bound. For instance
`/user/hand/left` refers to the bind point for the player\'s left hand.
Extensions can register additional top level paths, for instance a
haptic vest extension might register `/user/body/vest`.

`display_name` is the name shown to the user. `openxr_path` is the top
level path being registered. `openxr_extension_name` is optional and
ensures the top level path is only used if the specified extension is
available/enabled.

When a top level path ends up being bound by OpenXR, an
`XRPositionalTracker<class_XRPositionalTracker>`{.interpreted-text
role="ref"} is instantiated to manage the state of the device.
