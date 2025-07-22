github_url
:   hide

# ShaderInclude {#class_ShaderInclude}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A snippet of shader code to be included in a
`Shader<class_Shader>`{.interpreted-text role="ref"} with `#include`.

::: rst-class
classref-introduction-group
:::

## Description

A shader include file, saved with the `.gdshaderinc` extension. This
class allows you to define a custom shader snippet that can be included
in a `Shader<class_Shader>`{.interpreted-text role="ref"} by using the
preprocessor directive `#include`, followed by the file path (e.g.
`#include "res://shader_lib.gdshaderinc"`). The snippet doesn\'t have to
be a valid shader on its own.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Shader preprocessor <../tutorials/shaders/shader_reference/shader_preprocessor>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ShaderInclude_property_code}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **code** = `""`
`🔗<class_ShaderInclude_property_code>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_code**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_code**()

Returns the code of the shader include file. The returned text is what
the user has written, not the full generated code used internally.
