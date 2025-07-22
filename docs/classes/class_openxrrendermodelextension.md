github_url
:   hide

# OpenXRRenderModelExtension {#class_OpenXRRenderModelExtension}

**Inherits:**
`OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

This class implements the OpenXR Render Model Extension.

::: rst-class
classref-introduction-group
:::

## Description

This class implements the OpenXR Render Model Extension, if enabled it
will maintain a list of active render models and provides an interface
to the render model data.

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

:::: {#class_OpenXRRenderModelExtension_signal_render_model_added}
::: rst-class
classref-signal
:::
::::

**render_model_added**(render_model: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRRenderModelExtension_signal_render_model_added>`{.interpreted-text
role="ref"}

Emitted when a new render model is added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_signal_render_model_removed}
::: rst-class
classref-signal
:::
::::

**render_model_removed**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_OpenXRRenderModelExtension_signal_render_model_removed>`{.interpreted-text
role="ref"}

Emitted when a render model is removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_signal_render_model_top_level_path_changed}
::: rst-class
classref-signal
:::
::::

**render_model_top_level_path_changed**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_OpenXRRenderModelExtension_signal_render_model_top_level_path_changed>`{.interpreted-text
role="ref"}

Emitted when the top level path associated with a render model changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRRenderModelExtension_method_is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_active**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModelExtension_method_is_active>`{.interpreted-text
role="ref"}

Returns `true` if OpenXR\'s render model extension is supported and
enabled.

\*\*Note:\*\* This only returns a valid value after OpenXR has been
initialized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**render_model_create**(render_model_id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_OpenXRRenderModelExtension_method_render_model_create>`{.interpreted-text
role="ref"}

Creates a render model object within OpenXR using a render model id.

\*\*Note:\*\* This function is exposed for dependent OpenXR extensions
that provide render model ids to be used with the render model
extension.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_destroy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**render_model_destroy**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_OpenXRRenderModelExtension_method_render_model_destroy>`{.interpreted-text
role="ref"}

Destroys a render model object within OpenXR that was previously created
with
`render_model_create()<class_OpenXRRenderModelExtension_method_render_model_create>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This function is exposed for dependent OpenXR extensions
that provide render model ids to be used with the render model
extension.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_get_all}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**render_model_get_all**()
`🔗<class_OpenXRRenderModelExtension_method_render_model_get_all>`{.interpreted-text
role="ref"}

Returns an array of all currently active render models registered with
this extension.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**render_model_get_animatable_node_count**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_count>`{.interpreted-text
role="ref"}

Returns the number of animatable nodes this render model has.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**render_model_get_animatable_node_name**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_name>`{.interpreted-text
role="ref"}

Returns the name of the given animatable node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**render_model_get_animatable_node_transform**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_transform>`{.interpreted-text
role="ref"}

Returns the current local transform for an animatable node. This is
updated every frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_get_confidence}
::: rst-class
classref-method
:::
::::

`TrackingConfidence<enum_XRPose_TrackingConfidence>`{.interpreted-text
role="ref"} **render_model_get_confidence**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModelExtension_method_render_model_get_confidence>`{.interpreted-text
role="ref"}

Returns the tracking confidence of the tracking data for the render
model.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_get_root_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**render_model_get_root_transform**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModelExtension_method_render_model_get_root_transform>`{.interpreted-text
role="ref"}

Returns the root transform of a render model. This is the tracked
position relative to our
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_get_subaction_paths}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **render_model_get_subaction_paths**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_OpenXRRenderModelExtension_method_render_model_get_subaction_paths>`{.interpreted-text
role="ref"}

Returns a list of active subaction paths for this `render_model`.

\*\*Note:\*\* If different devices are bound to your actions than
available in suggested interaction bindings, this information shows
paths related to the interaction bindings being mimicked by that device.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_get_top_level_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**render_model_get_top_level_path**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModelExtension_method_render_model_get_top_level_path>`{.interpreted-text
role="ref"}

Returns the top level path associated with this `render_model`. If
provided this identifies whether the render model is associated with the
player\'s hands or other body part.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_is_animatable_node_visible}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**render_model_is_animatable_node_visible**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModelExtension_method_render_model_is_animatable_node_visible>`{.interpreted-text
role="ref"}

Returns `true` if this animatable node should be visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelExtension_method_render_model_new_scene_instance}
::: rst-class
classref-method
:::
::::

`Node3D<class_Node3D>`{.interpreted-text role="ref"}
**render_model_new_scene_instance**(render_model:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModelExtension_method_render_model_new_scene_instance>`{.interpreted-text
role="ref"}

Returns an instance of a subscene that contains all
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
nodes that allow you to visualize the render model.
