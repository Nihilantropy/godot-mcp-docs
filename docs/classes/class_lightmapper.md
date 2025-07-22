github_url
:   hide

# Lightmapper {#class_Lightmapper}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `LightmapperRD<class_LightmapperRD>`{.interpreted-text
role="ref"}

Abstract class extended by lightmappers, for use in
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This class should be extended by custom lightmapper classes.
Lightmappers can then be used with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} to provide
fast baked global illumination in 3D.

Godot contains a built-in GPU-based lightmapper
`LightmapperRD<class_LightmapperRD>`{.interpreted-text role="ref"} that
uses compute shaders, but custom lightmappers can be implemented by C++
modules.
