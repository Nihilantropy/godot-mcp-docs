github_url
:   hide

# RenderDataExtension {#class_RenderDataExtension}

**Inherits:** `RenderData<class_RenderData>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

This class allows for a RenderData implementation to be made in
GDExtension.

::: rst-class
classref-introduction-group
:::

## Description

This class allows for a RenderData implementation to be made in
GDExtension.

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

:::: {#class_RenderDataExtension_private_method__get_camera_attributes}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_get_camera_attributes**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderDataExtension_private_method__get_camera_attributes>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the
`RID<class_RID>`{.interpreted-text role="ref"} for the implementation\'s
camera attributes object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderDataExtension_private_method__get_environment}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_get_environment**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderDataExtension_private_method__get_environment>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the
`RID<class_RID>`{.interpreted-text role="ref"} of the implementation\'s
environment object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderDataExtension_private_method__get_render_scene_buffers}
::: rst-class
classref-method
:::
::::

`RenderSceneBuffers<class_RenderSceneBuffers>`{.interpreted-text
role="ref"} **\_get_render_scene_buffers**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderDataExtension_private_method__get_render_scene_buffers>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the implementation\'s
`RenderSceneBuffers<class_RenderSceneBuffers>`{.interpreted-text
role="ref"} object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderDataExtension_private_method__get_render_scene_data}
::: rst-class
classref-method
:::
::::

`RenderSceneData<class_RenderSceneData>`{.interpreted-text role="ref"}
**\_get_render_scene_data**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderDataExtension_private_method__get_render_scene_data>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the implementation\'s
`RenderSceneDataExtension<class_RenderSceneDataExtension>`{.interpreted-text
role="ref"} object.
