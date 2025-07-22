github_url
:   hide

# OpenXRExtensionWrapper {#class_OpenXRExtensionWrapper}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`OpenXRExtensionWrapperExtension<class_OpenXRExtensionWrapperExtension>`{.interpreted-text
role="ref"},
`OpenXRFutureExtension<class_OpenXRFutureExtension>`{.interpreted-text
role="ref"},
`OpenXRRenderModelExtension<class_OpenXRRenderModelExtension>`{.interpreted-text
role="ref"}

Allows implementing OpenXR extensions with GDExtension.

::: rst-class
classref-introduction-group
:::

## Description

**OpenXRExtensionWrapper** allows implementing OpenXR extensions with
GDExtension. The extension should be registered with
`register_extension_wrapper()<class_OpenXRExtensionWrapper_method_register_extension_wrapper>`{.interpreted-text
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

:::: {#class_OpenXRExtensionWrapper_private_method__get_composition_layer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_composition_layer**(index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__get_composition_layer>`{.interpreted-text
role="ref"}

Returns a pointer to an `XrCompositionLayerBaseHeader` struct to provide
the given composition layer.

This will only be called if the extension previously registered itself
with
`OpenXRAPIExtension.register_composition_layer_provider()<class_OpenXRAPIExtension_method_register_composition_layer_provider>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__get_composition_layer_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_composition_layer_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__get_composition_layer_count>`{.interpreted-text
role="ref"}

Returns the number of composition layers this extension wrapper provides
via
`_get_composition_layer()<class_OpenXRExtensionWrapper_private_method__get_composition_layer>`{.interpreted-text
role="ref"}.

This will only be called if the extension previously registered itself
with
`OpenXRAPIExtension.register_composition_layer_provider()<class_OpenXRAPIExtension_method_register_composition_layer_provider>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__get_composition_layer_order}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_composition_layer_order**(index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__get_composition_layer_order>`{.interpreted-text
role="ref"}

Returns an integer that will be used to sort the given composition layer
provided via
`_get_composition_layer()<class_OpenXRExtensionWrapper_private_method__get_composition_layer>`{.interpreted-text
role="ref"}. Lower numbers will move the layer to the front of the list,
and higher numbers to the end. The default projection layer has an order
of `0`, so layers provided by this method should probably be above or
below (but not exactly) `0`.

This will only be called if the extension previously registered itself
with
`OpenXRAPIExtension.register_composition_layer_provider()<class_OpenXRAPIExtension_method_register_composition_layer_provider>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__get_requested_extensions}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_get_requested_extensions**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__get_requested_extensions>`{.interpreted-text
role="ref"}

Returns a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
of OpenXR extensions related to this extension. The
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} should
contain the name of the extension, mapped to a `bool *` cast to an
integer:

- If the `bool *` is a `nullptr` this extension is mandatory.
- If the `bool *` points to a boolean, the boolean will be updated to
  `true` if the extension is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__get_suggested_tracker_names}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_suggested_tracker_names**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__get_suggested_tracker_names>`{.interpreted-text
role="ref"}

Returns a `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} of positional tracker names that are used within the
extension wrapper.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\]
**\_get_viewport_composition_layer_extension_properties**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties>`{.interpreted-text
role="ref"}

Gets an array of `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}s that represent properties, just like
`Object._get_property_list()<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"}, that will be added to
`OpenXRCompositionLayer<class_OpenXRCompositionLayer>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_property_defaults}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_get_viewport_composition_layer_extension_property_defaults**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_property_defaults>`{.interpreted-text
role="ref"}

Gets a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
containing the default values for the properties returned by
`_get_viewport_composition_layer_extension_properties()<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_before_instance_created}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_before_instance_created**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_before_instance_created>`{.interpreted-text
role="ref"}

Called before the OpenXR instance is created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_event_polled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_on_event_polled**(event: `const void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_event_polled>`{.interpreted-text
role="ref"}

Called when there is an OpenXR event to process. When implementing,
return `true` if the event was handled, return `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_instance_created}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_instance_created**(instance: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_instance_created>`{.interpreted-text
role="ref"}

Called right after the OpenXR instance is created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_instance_destroyed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_instance_destroyed**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_instance_destroyed>`{.interpreted-text
role="ref"}

Called right before the OpenXR instance is destroyed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_main_swapchains_created}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_main_swapchains_created**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_main_swapchains_created>`{.interpreted-text
role="ref"}

Called right after the main swapchains are (re)created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_post_draw_viewport}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_post_draw_viewport**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_post_draw_viewport>`{.interpreted-text
role="ref"}

Called right after the given viewport is rendered.

\*\*Note:\*\* The draw commands might only be queued at this point, not
executed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_pre_draw_viewport}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_pre_draw_viewport**(viewport: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_pre_draw_viewport>`{.interpreted-text
role="ref"}

Called right before the given viewport is rendered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_pre_render}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_pre_render**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_pre_render>`{.interpreted-text
role="ref"}

Called right before the XR viewports begin their rendering step.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_process**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_process>`{.interpreted-text
role="ref"}

Called as part of the OpenXR process handling. This happens right before
general and physics processing steps of the main loop. During this step
controller data is queried and made available to game logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_register_metadata}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_register_metadata**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_register_metadata>`{.interpreted-text
role="ref"}

Allows extensions to register additional controller metadata. This
function is called even when the OpenXR API is not constructed as the
metadata needs to be available to the editor.

Extensions should also provide metadata regardless of whether they are
supported on the host system. The controller data is used to setup
action maps for users who may have access to the relevant hardware.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_session_created}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_session_created**(session: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_session_created>`{.interpreted-text
role="ref"}

Called right after the OpenXR session is created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_session_destroyed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_session_destroyed**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_session_destroyed>`{.interpreted-text
role="ref"}

Called right before the OpenXR session is destroyed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_state_exiting}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_state_exiting**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_state_exiting>`{.interpreted-text
role="ref"}

Called when the OpenXR session state is changed to exiting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_state_focused}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_state_focused**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_state_focused>`{.interpreted-text
role="ref"}

Called when the OpenXR session state is changed to focused. This state
is the active state when the game runs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_state_idle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_state_idle**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_state_idle>`{.interpreted-text
role="ref"}

Called when the OpenXR session state is changed to idle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_state_loss_pending}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_state_loss_pending**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_state_loss_pending>`{.interpreted-text
role="ref"}

Called when the OpenXR session state is changed to loss pending.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_state_ready}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_state_ready**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_state_ready>`{.interpreted-text
role="ref"}

Called when the OpenXR session state is changed to ready. This means
OpenXR is ready to set up the session.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_state_stopping}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_state_stopping**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_state_stopping>`{.interpreted-text
role="ref"}

Called when the OpenXR session state is changed to stopping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_state_synchronized}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_state_synchronized**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_state_synchronized>`{.interpreted-text
role="ref"}

Called when the OpenXR session state is changed to synchronized. OpenXR
also returns to this state when the application loses focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_state_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_state_visible**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_state_visible>`{.interpreted-text
role="ref"}

Called when the OpenXR session state is changed to visible. This means
OpenXR is now ready to receive frames.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_sync_actions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_sync_actions**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_sync_actions>`{.interpreted-text
role="ref"}

Called when OpenXR has performed its action sync.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__on_viewport_composition_layer_destroyed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_on_viewport_composition_layer_destroyed**(layer: `const void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__on_viewport_composition_layer_destroyed>`{.interpreted-text
role="ref"}

Called when a composition layer created via
`OpenXRCompositionLayer<class_OpenXRCompositionLayer>`{.interpreted-text
role="ref"} is destroyed.

`layer` is a pointer to an `XrCompositionLayerBaseHeader` struct.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_android_surface_swapchain_create_info_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_android_surface_swapchain_create_info_and_get_next_pointer**(property_values:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"},
next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_android_surface_swapchain_create_info_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures to Android surface swapchains created by
`OpenXRCompositionLayer<class_OpenXRCompositionLayer>`{.interpreted-text
role="ref"}.

`property_values` contains the values of the properties returned by
`_get_viewport_composition_layer_extension_properties()<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_frame_end_info_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_frame_end_info_and_get_next_pointer**(next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_frame_end_info_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures to `XrFrameEndInfo`.

This will only be called if the extension previously registered itself
with
`OpenXRAPIExtension.register_frame_info_extension()<class_OpenXRAPIExtension_method_register_frame_info_extension>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_frame_wait_info_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_frame_wait_info_and_get_next_pointer**(next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_frame_wait_info_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures to `XrFrameWaitInfo`.

This will only be called if the extension previously registered itself
with
`OpenXRAPIExtension.register_frame_info_extension()<class_OpenXRAPIExtension_method_register_frame_info_extension>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_hand_joint_locations_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_hand_joint_locations_and_get_next_pointer**(hand_index:
`int<class_int>`{.interpreted-text role="ref"}, next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_hand_joint_locations_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures when each hand tracker is created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_instance_create_info_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_instance_create_info_and_get_next_pointer**(next_pointer:
`void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_instance_create_info_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures when the OpenXR instance is created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_projection_views_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_projection_views_and_get_next_pointer**(view_index:
`int<class_int>`{.interpreted-text role="ref"}, next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_projection_views_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures to the projection view of the given
`view_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_reference_space_create_info_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_reference_space_create_info_and_get_next_pointer**(reference_space_type:
`int<class_int>`{.interpreted-text role="ref"}, next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_reference_space_create_info_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures to `XrReferenceSpaceCreateInfo`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_session_create_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_session_create_and_get_next_pointer**(next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_session_create_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures when the OpenXR session is created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_swapchain_create_info_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_swapchain_create_info_and_get_next_pointer**(next_pointer:
`void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_swapchain_create_info_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures when creating OpenXR swapchains.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_system_properties_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_system_properties_and_get_next_pointer**(next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_system_properties_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures when querying OpenXR system abilities.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_view_locate_info_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_view_locate_info_and_get_next_pointer**(next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_view_locate_info_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures to `XrViewLocateInfo`.

This will only be called if the extension previously registered itself
with
`OpenXRAPIExtension.register_frame_info_extension()<class_OpenXRAPIExtension_method_register_frame_info_extension>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_private_method__set_viewport_composition_layer_and_get_next_pointer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_set_viewport_composition_layer_and_get_next_pointer**(layer:
`const void*`, property_values:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"},
next_pointer: `void*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRExtensionWrapper_private_method__set_viewport_composition_layer_and_get_next_pointer>`{.interpreted-text
role="ref"}

Adds additional data structures to composition layers created by
`OpenXRCompositionLayer<class_OpenXRCompositionLayer>`{.interpreted-text
role="ref"}.

`property_values` contains the values of the properties returned by
`_get_viewport_composition_layer_extension_properties()<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties>`{.interpreted-text
role="ref"}.

`layer` is a pointer to an `XrCompositionLayerBaseHeader` struct.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_method_get_openxr_api}
::: rst-class
classref-method
:::
::::

`OpenXRAPIExtension<class_OpenXRAPIExtension>`{.interpreted-text
role="ref"} **get_openxr_api**()
`🔗<class_OpenXRExtensionWrapper_method_get_openxr_api>`{.interpreted-text
role="ref"}

Returns the created
`OpenXRAPIExtension<class_OpenXRAPIExtension>`{.interpreted-text
role="ref"}, which can be used to access the OpenXR API.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRExtensionWrapper_method_register_extension_wrapper}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_extension_wrapper**()
`🔗<class_OpenXRExtensionWrapper_method_register_extension_wrapper>`{.interpreted-text
role="ref"}

Registers the extension. This should happen at core module
initialization level.
