github_url
:   hide

# OpenXRBindingModifier {#class_OpenXRBindingModifier}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>`{.interpreted-text
role="ref"},
`OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>`{.interpreted-text
role="ref"}

Binding modifier base class.

::: rst-class
classref-introduction-group
:::

## Description

Binding modifier base class. Subclasses implement various modifiers that
alter how an OpenXR runtime processes inputs.

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

:::: {#class_OpenXRBindingModifier_private_method__get_description}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_description**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRBindingModifier_private_method__get_description>`{.interpreted-text
role="ref"}

Return the description of this class that is used for the title bar of
the binding modifier editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRBindingModifier_private_method__get_ip_modification}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**\_get_ip_modification**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRBindingModifier_private_method__get_ip_modification>`{.interpreted-text
role="ref"}

Returns the data that is sent to OpenXR when submitting the suggested
interacting bindings this modifier is a part of.

\*\*Note:\*\* This must be data compatible with an
`XrBindingModificationBaseHeaderKHR` structure.
