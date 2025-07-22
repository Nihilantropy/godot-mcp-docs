github_url
:   hide

# ShaderIncludeDB {#class_ShaderIncludeDB}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Internal database of built in shader include files.

::: rst-class
classref-introduction-group
:::

## Description

This object contains shader fragments from Godot\'s internal shaders.
These can be used when access to internal uniform buffers and/or
internal functions is required for instance when composing compositor
effects or compute shaders. Only fragments for the current rendering
device are loaded.

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

:::: {#class_ShaderIncludeDB_method_get_built_in_include_file}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_built_in_include_file**(filename:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_ShaderIncludeDB_method_get_built_in_include_file>`{.interpreted-text
role="ref"}

Returns the code for the built-in shader fragment. You can also access
this in your shader code through `#include "filename"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShaderIncludeDB_method_has_built_in_include_file}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_built_in_include_file**(filename:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_ShaderIncludeDB_method_has_built_in_include_file>`{.interpreted-text
role="ref"}

Returns `true` if an include file with this name exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShaderIncludeDB_method_list_built_in_include_files}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **list_built_in_include_files**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_ShaderIncludeDB_method_list_built_in_include_files>`{.interpreted-text
role="ref"}

Returns a list of built-in include files that are currently registered.
