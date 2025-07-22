github_url
:   hide

# FramebufferCacheRD {#class_FramebufferCacheRD}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Framebuffer cache manager for Rendering Device based renderers.

::: rst-class
classref-introduction-group
:::

## Description

Framebuffer cache manager for Rendering Device based renderers. Provides
a way to create a framebuffer and reuse it in subsequent calls for as
long as the used textures exists. Framebuffers will automatically be
cleaned up when dependent objects are freed.

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

:::: {#class_FramebufferCacheRD_method_get_cache_multipass}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_cache_multipass**(textures: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\], passes:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RDFramebufferPass<class_RDFramebufferPass>`{.interpreted-text
role="ref"}\], views: `int<class_int>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_FramebufferCacheRD_method_get_cache_multipass>`{.interpreted-text
role="ref"}

Creates, or obtains a cached, framebuffer. `textures` lists textures
accessed. `passes` defines the subpasses and texture allocation, if left
empty a single pass is created and textures are allocated depending on
their usage flags. `views` defines the number of views used when
rendering.
