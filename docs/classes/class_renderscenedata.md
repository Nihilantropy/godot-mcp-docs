github_url
:   hide

# RenderSceneData {#class_RenderSceneData}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`RenderSceneDataExtension<class_RenderSceneDataExtension>`{.interpreted-text
role="ref"},
`RenderSceneDataRD<class_RenderSceneDataRD>`{.interpreted-text
role="ref"}

Abstract render data object, holds scene data related to rendering a
single frame of a viewport.

::: rst-class
classref-introduction-group
:::

## Description

Abstract scene data object, exists for the duration of rendering a
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

:::: {#class_RenderSceneData_method_get_cam_projection}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**get_cam_projection**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneData_method_get_cam_projection>`{.interpreted-text
role="ref"}

Returns the camera projection used to render this frame.

\*\*Note:\*\* If more than one view is rendered, this will return a
combined projection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneData_method_get_cam_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_cam_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneData_method_get_cam_transform>`{.interpreted-text
role="ref"}

Returns the camera transform used to render this frame.

\*\*Note:\*\* If more than one view is rendered, this will return a
centered transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneData_method_get_uniform_buffer}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_uniform_buffer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneData_method_get_uniform_buffer>`{.interpreted-text
role="ref"}

Return the `RID<class_RID>`{.interpreted-text role="ref"} of the uniform
buffer containing the scene data as a UBO.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneData_method_get_view_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_view_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneData_method_get_view_count>`{.interpreted-text
role="ref"}

Returns the number of views being rendered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneData_method_get_view_eye_offset}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_view_eye_offset**(view: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneData_method_get_view_eye_offset>`{.interpreted-text
role="ref"}

Returns the eye offset per view used to render this frame. This is the
offset between our camera transform and the eye transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneData_method_get_view_projection}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**get_view_projection**(view: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneData_method_get_view_projection>`{.interpreted-text
role="ref"}

Returns the view projection per view used to render this frame.

\*\*Note:\*\* If a single view is rendered, this returns the camera
projection. If more than one view is rendered, this will return a
projection for the given view including the eye offset.
