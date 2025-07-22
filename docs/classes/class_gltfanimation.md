github_url
:   hide

# GLTFAnimation {#class_GLTFAnimation}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

::: {.container .contribute}
There is currently no description for this class. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

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

## Property Descriptions

:::: {#class_GLTFAnimation_property_loop}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **loop** = `false`
`🔗<class_GLTFAnimation_property_loop>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_loop**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAnimation_property_original_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **original_name** =
`""` `🔗<class_GLTFAnimation_property_original_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_original_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_original_name**()

The original name of the animation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFAnimation_method_get_additional_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GLTFAnimation_method_get_additional_data>`{.interpreted-text
role="ref"}

Gets additional arbitrary data in this **GLTFAnimation** instance. This
can be used to keep per-node state data in
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes, which is important because they are stateless.

The argument should be the
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} name (does not have to match the extension name in the glTF
file), and the return value can be anything you set. If nothing was set,
the return value is `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFAnimation_method_set_additional_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
additional_data: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_GLTFAnimation_method_set_additional_data>`{.interpreted-text
role="ref"}

Sets additional arbitrary data in this **GLTFAnimation** instance. This
can be used to keep per-node state data in
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes, which is important because they are stateless.

The first argument should be the
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} name (does not have to match the extension name in the glTF
file), and the second argument can be anything you want.
