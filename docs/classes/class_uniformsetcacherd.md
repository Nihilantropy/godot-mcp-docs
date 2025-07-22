github_url
:   hide

# UniformSetCacheRD {#class_UniformSetCacheRD}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Uniform set cache manager for Rendering Device based renderers.

::: rst-class
classref-introduction-group
:::

## Description

Uniform set cache manager for Rendering Device based renderers. Provides
a way to create a uniform set and reuse it in subsequent calls for as
long as the uniform set exists. Uniform set will automatically be
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

:::: {#class_UniformSetCacheRD_method_get_cache}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_cache**(shader:
`RID<class_RID>`{.interpreted-text role="ref"}, set:
`int<class_int>`{.interpreted-text role="ref"}, uniforms:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RDUniform<class_RDUniform>`{.interpreted-text
role="ref"}\])
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_UniformSetCacheRD_method_get_cache>`{.interpreted-text
role="ref"}

Creates/returns a cached uniform set based on the provided uniforms for
a given shader.
