github_url
:   hide

# RenderSceneBuffers {#class_RenderSceneBuffers}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`RenderSceneBuffersExtension<class_RenderSceneBuffersExtension>`{.interpreted-text
role="ref"},
`RenderSceneBuffersRD<class_RenderSceneBuffersRD>`{.interpreted-text
role="ref"}

Abstract scene buffers object, created for each viewport for which 3D
rendering is done.

::: rst-class
classref-introduction-group
:::

## Description

Abstract scene buffers object, created for each viewport for which 3D
rendering is done. It manages any additional buffers used during
rendering and will discard buffers when the viewport is resized.

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

:::: {#class_RenderSceneBuffers_method_configure}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**configure**(config:
`RenderSceneBuffersConfiguration<class_RenderSceneBuffersConfiguration>`{.interpreted-text
role="ref"})
`🔗<class_RenderSceneBuffers_method_configure>`{.interpreted-text
role="ref"}

This method is called by the rendering server when the associated
viewport\'s configuration is changed. It will discard the old buffers
and recreate the internal buffers used.
