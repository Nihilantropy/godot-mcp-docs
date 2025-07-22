github_url
:   hide

# RenderSceneDataExtension {#class_RenderSceneDataExtension}

**Inherits:** `RenderSceneData<class_RenderSceneData>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

This class allows for a RenderSceneData implementation to be made in
GDExtension.

::: rst-class
classref-introduction-group
:::

## Description

This class allows for a RenderSceneData implementation to be made in
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

:::: {#class_RenderSceneDataExtension_private_method__get_cam_projection}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**\_get_cam_projection**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneDataExtension_private_method__get_cam_projection>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the camera
`Projection<class_Projection>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneDataExtension_private_method__get_cam_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**\_get_cam_transform**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneDataExtension_private_method__get_cam_transform>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the camera
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneDataExtension_private_method__get_uniform_buffer}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_get_uniform_buffer**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneDataExtension_private_method__get_uniform_buffer>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the
`RID<class_RID>`{.interpreted-text role="ref"} of the uniform buffer
containing the scene data as a UBO.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneDataExtension_private_method__get_view_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_view_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneDataExtension_private_method__get_view_count>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the view count.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneDataExtension_private_method__get_view_eye_offset}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**\_get_view_eye_offset**(view: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneDataExtension_private_method__get_view_eye_offset>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the eye offset for the given
`view`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneDataExtension_private_method__get_view_projection}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**\_get_view_projection**(view: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneDataExtension_private_method__get_view_projection>`{.interpreted-text
role="ref"}

Implement this in GDExtension to return the view
`Projection<class_Projection>`{.interpreted-text role="ref"} for the
given `view`.
