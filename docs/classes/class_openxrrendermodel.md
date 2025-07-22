github_url
:   hide

# OpenXRRenderModel {#class_OpenXRRenderModel}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

This node will display an OpenXR render model.

::: rst-class
classref-introduction-group
:::

## Description

This node will display an OpenXR render model by accessing the
associated GLTF and processes all animation data (if supported by the XR
runtime).

Render models were introduced to allow showing the correct model for the
controller (or other device) the user has in hand, since the OpenXR
action map does not provide information about the hardware used by the
user. Note that while the controller (or device) can be somewhat
inferred by the bound action map profile, this is a dangerous approach
as the user may be using hardware not known at time of development and
OpenXR will simply simulate an available interaction profile.

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

:::: {#class_OpenXRRenderModel_signal_render_model_top_level_path_changed}
::: rst-class
classref-signal
:::
::::

**render_model_top_level_path_changed**()
`🔗<class_OpenXRRenderModel_signal_render_model_top_level_path_changed>`{.interpreted-text
role="ref"}

Emitted when the top level path of this render model has changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OpenXRRenderModel_property_render_model}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **render_model** =
`RID()`
`🔗<class_OpenXRRenderModel_property_render_model>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_render_model**(value: `RID<class_RID>`{.interpreted-text
  role="ref"})
- `RID<class_RID>`{.interpreted-text role="ref"} **get_render_model**()

The render model RID for the render model to load, as returned by
`OpenXRRenderModelExtension.render_model_create()<class_OpenXRRenderModelExtension_method_render_model_create>`{.interpreted-text
role="ref"} or
`OpenXRRenderModelExtension.render_model_get_all()<class_OpenXRRenderModelExtension_method_render_model_get_all>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRRenderModel_method_get_top_level_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_top_level_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRRenderModel_method_get_top_level_path>`{.interpreted-text
role="ref"}

Returns the top level path related to this render model.
