github_url
:   hide

# Translation {#class_Translation}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`OptimizedTranslation<class_OptimizedTranslation>`{.interpreted-text
role="ref"}

A language translation that maps a collection of strings to their
individual translations.

::: rst-class
classref-introduction-group
:::

## Description

**Translation**s are resources that can be loaded and unloaded on
demand. They map a collection of strings to their individual
translations, and they also provide convenience methods for
pluralization.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Internationalizing games <../tutorials/i18n/internationalizing_games>`{.interpreted-text
  role="doc"}
- `Localization using gettext <../tutorials/i18n/localization_using_gettext>`{.interpreted-text
  role="doc"}
- `Locales <../tutorials/i18n/locales>`{.interpreted-text role="doc"}

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

:::: {#class_Translation_property_locale}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **locale** = `"en"`
`🔗<class_Translation_property_locale>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_locale**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_locale**()

The locale of the translation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Translation_private_method__get_message}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**\_get_message**(src_message:
`StringName<class_StringName>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Translation_private_method__get_message>`{.interpreted-text
role="ref"}

Virtual method to override
`get_message()<class_Translation_method_get_message>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Translation_private_method__get_plural_message}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**\_get_plural_message**(src_message:
`StringName<class_StringName>`{.interpreted-text role="ref"},
src_plural_message: `StringName<class_StringName>`{.interpreted-text
role="ref"}, n: `int<class_int>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Translation_private_method__get_plural_message>`{.interpreted-text
role="ref"}

Virtual method to override
`get_plural_message()<class_Translation_method_get_plural_message>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Translation_method_add_message}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_message**(src_message:
`StringName<class_StringName>`{.interpreted-text role="ref"},
xlated_message: `StringName<class_StringName>`{.interpreted-text
role="ref"}, context: `StringName<class_StringName>`{.interpreted-text
role="ref"} = &\"\")
`🔗<class_Translation_method_add_message>`{.interpreted-text role="ref"}

Adds a message if nonexistent, followed by its translation.

An additional context could be used to specify the translation context
or differentiate polysemic words.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Translation_method_add_plural_message}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_plural_message**(src_message:
`StringName<class_StringName>`{.interpreted-text role="ref"},
xlated_messages:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, context: `StringName<class_StringName>`{.interpreted-text
role="ref"} = &\"\")
`🔗<class_Translation_method_add_plural_message>`{.interpreted-text
role="ref"}

Adds a message involving plural translation if nonexistent, followed by
its translation.

An additional context could be used to specify the translation context
or differentiate polysemic words.

\*\*Note:\*\* Plurals are only supported in
`gettext-based translations (PO) <../tutorials/i18n/localization_using_gettext>`{.interpreted-text
role="doc"}, not CSV.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Translation_method_erase_message}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_message**(src_message:
`StringName<class_StringName>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\")
`🔗<class_Translation_method_erase_message>`{.interpreted-text
role="ref"}

Erases a message.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Translation_method_get_message}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_message**(src_message:
`StringName<class_StringName>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Translation_method_get_message>`{.interpreted-text role="ref"}

Returns a message\'s translation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Translation_method_get_message_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_message_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Translation_method_get_message_count>`{.interpreted-text
role="ref"}

Returns the number of existing messages.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Translation_method_get_message_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_message_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Translation_method_get_message_list>`{.interpreted-text
role="ref"}

Returns all the messages (keys).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Translation_method_get_plural_message}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_plural_message**(src_message:
`StringName<class_StringName>`{.interpreted-text role="ref"},
src_plural_message: `StringName<class_StringName>`{.interpreted-text
role="ref"}, n: `int<class_int>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Translation_method_get_plural_message>`{.interpreted-text
role="ref"}

Returns a message\'s translation involving plurals.

The number `n` is the number or quantity of the plural object. It will
be used to guide the translation system to fetch the correct plural form
for the selected language.

\*\*Note:\*\* Plurals are only supported in
`gettext-based translations (PO) <../tutorials/i18n/localization_using_gettext>`{.interpreted-text
role="doc"}, not CSV.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Translation_method_get_translated_message_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_translated_message_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Translation_method_get_translated_message_list>`{.interpreted-text
role="ref"}

Returns all the messages (translated text).
