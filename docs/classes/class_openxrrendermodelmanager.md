github_url
:   hide

# OpenXRRenderModelManager {#class_OpenXRRenderModelManager}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Helper node that will automatically manage displaying render models.

::: rst-class
classref-introduction-group
:::

## Description

This helper node will automatically manage displaying render models. It
will create new
`OpenXRRenderModel<class_OpenXRRenderModel>`{.interpreted-text
role="ref"} nodes as controllers and other hand held devices are
detected, and remove those nodes when they are deactivated.

\*\*Note:\*\* If you want more control over this logic you can
alternatively call
`OpenXRRenderModelExtension.render_model_get_all()<class_OpenXRRenderModelExtension_method_render_model_get_all>`{.interpreted-text
role="ref"} to obtain a list of active render model ids and create
`OpenXRRenderModel<class_OpenXRRenderModel>`{.interpreted-text
role="ref"} instances for each render model id provided.

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

## Signals

:::: {#class_OpenXRRenderModelManager_signal_render_model_added}
::: rst-class
classref-signal
:::
::::

**render_model_added**(render_model:
`OpenXRRenderModel<class_OpenXRRenderModel>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRRenderModelManager_signal_render_model_added>`{.interpreted-text
role="ref"}

Emitted when a render model node is added as a child to this node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelManager_signal_render_model_removed}
::: rst-class
classref-signal
:::
::::

**render_model_removed**(render_model:
`OpenXRRenderModel<class_OpenXRRenderModel>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRRenderModelManager_signal_render_model_removed>`{.interpreted-text
role="ref"}

Emitted when a render model child node is about to be removed from this
node.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_OpenXRRenderModelManager_RenderModelTracker}
::: rst-class
classref-enumeration
:::
::::

enum **RenderModelTracker**:
`🔗<enum_OpenXRRenderModelManager_RenderModelTracker>`{.interpreted-text
role="ref"}

:::: {#class_OpenXRRenderModelManager_constant_RENDER_MODEL_TRACKER_ANY}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderModelTracker<enum_OpenXRRenderModelManager_RenderModelTracker>`{.interpreted-text
role="ref"} **RENDER_MODEL_TRACKER_ANY** = `0`

All active render models are shown regardless of what tracker they
relate to.

:::: {#class_OpenXRRenderModelManager_constant_RENDER_MODEL_TRACKER_NONE_SET}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderModelTracker<enum_OpenXRRenderModelManager_RenderModelTracker>`{.interpreted-text
role="ref"} **RENDER_MODEL_TRACKER_NONE_SET** = `1`

Only active render models are shown that are not related to any tracker
we manage.

:::: {#class_OpenXRRenderModelManager_constant_RENDER_MODEL_TRACKER_LEFT_HAND}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderModelTracker<enum_OpenXRRenderModelManager_RenderModelTracker>`{.interpreted-text
role="ref"} **RENDER_MODEL_TRACKER_LEFT_HAND** = `2`

Only active render models are shown that are related to the left hand
tracker.

:::: {#class_OpenXRRenderModelManager_constant_RENDER_MODEL_TRACKER_RIGHT_HAND}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderModelTracker<enum_OpenXRRenderModelManager_RenderModelTracker>`{.interpreted-text
role="ref"} **RENDER_MODEL_TRACKER_RIGHT_HAND** = `3`

Only active render models are shown that are related to the right hand
tracker.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OpenXRRenderModelManager_property_make_local_to_pose}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**make_local_to_pose** = `""`
`🔗<class_OpenXRRenderModelManager_property_make_local_to_pose>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_make_local_to_pose**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_make_local_to_pose**()

Position render models local to this pose (this will adjust the position
of the render models container node).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRRenderModelManager_property_tracker}
::: rst-class
classref-property
:::
::::

`RenderModelTracker<enum_OpenXRRenderModelManager_RenderModelTracker>`{.interpreted-text
role="ref"} **tracker** = `0`
`🔗<class_OpenXRRenderModelManager_property_tracker>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tracker**(value:
  `RenderModelTracker<enum_OpenXRRenderModelManager_RenderModelTracker>`{.interpreted-text
  role="ref"})
- `RenderModelTracker<enum_OpenXRRenderModelManager_RenderModelTracker>`{.interpreted-text
  role="ref"} **get_tracker**()

Limits render models to the specified tracker. Include: 0 = All render
models, 1 = Render models not related to a tracker, 2 = Render models
related to the left hand tracker, 3 = Render models related to the right
hand tracker.
