github_url
:   hide

# RenderData {#class_RenderData}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`RenderDataExtension<class_RenderDataExtension>`{.interpreted-text
role="ref"}, `RenderDataRD<class_RenderDataRD>`{.interpreted-text
role="ref"}

Abstract render data object, holds frame data related to rendering a
single frame of a viewport.

::: rst-class
classref-introduction-group
:::

## Description

Abstract render data object, exists for the duration of rendering a
single viewport.

\*\*Note:\*\* This is an internal rendering server object, do not
instantiate this from script.

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

:::: {#class_RenderData_method_get_camera_attributes}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_camera_attributes**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderData_method_get_camera_attributes>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the camera
attributes object in the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
being used to render this viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderData_method_get_environment}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_environment**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderData_method_get_environment>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the
environment object in the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
being used to render this viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderData_method_get_render_scene_buffers}
::: rst-class
classref-method
:::
::::

`RenderSceneBuffers<class_RenderSceneBuffers>`{.interpreted-text
role="ref"} **get_render_scene_buffers**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderData_method_get_render_scene_buffers>`{.interpreted-text
role="ref"}

Returns the
`RenderSceneBuffers<class_RenderSceneBuffers>`{.interpreted-text
role="ref"} object managing the scene buffers for rendering this
viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderData_method_get_render_scene_data}
::: rst-class
classref-method
:::
::::

`RenderSceneData<class_RenderSceneData>`{.interpreted-text role="ref"}
**get_render_scene_data**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderData_method_get_render_scene_data>`{.interpreted-text
role="ref"}

Returns the `RenderSceneData<class_RenderSceneData>`{.interpreted-text
role="ref"} object managing this frames scene data.
