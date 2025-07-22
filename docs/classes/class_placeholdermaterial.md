github_url
:   hide

# PlaceholderMaterial {#class_PlaceholderMaterial}

**Inherits:** `Material<class_Material>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Placeholder class for a material.

::: rst-class
classref-introduction-group
:::

## Description

This class is used when loading a project that uses a
`Material<class_Material>`{.interpreted-text role="ref"} subclass in 2
conditions:

- When running the project exported in dedicated server mode, only the
  texture\'s dimensions are kept (as they may be relied upon for
  gameplay purposes or positioning of other elements). This allows
  reducing the exported PCK\'s size significantly.
- When this subclass is missing due to using a different engine version
  or build (e.g. modules disabled).
