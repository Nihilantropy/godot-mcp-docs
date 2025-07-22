github_url
:   hide

# Marshalls {#class_Marshalls}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Data transformation (marshaling) and encoding helpers.

::: rst-class
classref-introduction-group
:::

## Description

Provides data transformation and encoding utility functions.

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

:::: {#class_Marshalls_method_base64_to_raw}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**base64_to_raw**(base64_str: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_Marshalls_method_base64_to_raw>`{.interpreted-text role="ref"}

Returns a decoded
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
corresponding to the Base64-encoded string `base64_str`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Marshalls_method_base64_to_utf8}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**base64_to_utf8**(base64_str: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_Marshalls_method_base64_to_utf8>`{.interpreted-text
role="ref"}

Returns a decoded string corresponding to the Base64-encoded string
`base64_str`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Marshalls_method_base64_to_variant}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**base64_to_variant**(base64_str:
`String<class_String>`{.interpreted-text role="ref"}, allow_objects:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Marshalls_method_base64_to_variant>`{.interpreted-text
role="ref"}

Returns a decoded `Variant<class_Variant>`{.interpreted-text role="ref"}
corresponding to the Base64-encoded string `base64_str`. If
`allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the
`@GlobalScope.bytes_to_var()<class_@GlobalScope_method_bytes_to_var>`{.interpreted-text
role="ref"} method.

\*\*Warning:\*\* Deserialized objects can contain code which gets
executed. Do not use this option if the serialized object comes from
untrusted sources to avoid potential security threats such as remote
code execution.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Marshalls_method_raw_to_base64}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**raw_to_base64**(array:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Marshalls_method_raw_to_base64>`{.interpreted-text role="ref"}

Returns a Base64-encoded string of a given
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Marshalls_method_utf8_to_base64}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**utf8_to_base64**(utf8_str: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_Marshalls_method_utf8_to_base64>`{.interpreted-text
role="ref"}

Returns a Base64-encoded string of the UTF-8 string `utf8_str`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Marshalls_method_variant_to_base64}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**variant_to_base64**(variant:
`Variant<class_Variant>`{.interpreted-text role="ref"}, full_objects:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Marshalls_method_variant_to_base64>`{.interpreted-text
role="ref"}

Returns a Base64-encoded string of the
`Variant<class_Variant>`{.interpreted-text role="ref"} `variant`. If
`full_objects` is `true`, encoding objects is allowed (and can
potentially include code).

Internally, this uses the same encoding mechanism as the
`@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>`{.interpreted-text
role="ref"} method.
