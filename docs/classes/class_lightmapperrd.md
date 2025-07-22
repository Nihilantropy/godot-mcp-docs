github_url
:   hide

# LightmapperRD {#class_LightmapperRD}

**Inherits:** `Lightmapper<class_Lightmapper>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

The built-in GPU-based lightmapper for use with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

LightmapperRD (\"RD\" stands for
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"})
is the built-in GPU-based lightmapper for use with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}. On most
dedicated GPUs, it can bake lightmaps much faster than most CPU-based
lightmappers. LightmapperRD uses compute shaders to bake lightmaps, so
it does not require CUDA or OpenCL libraries to be installed to be
usable.

\*\*Note:\*\* Only usable when using the RenderingDevice backend
(Forward+ or Mobile renderers), not Compatibility.
