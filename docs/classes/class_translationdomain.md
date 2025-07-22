github_url
:   hide

# TranslationDomain {#class_TranslationDomain}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A self-contained collection of
`Translation<class_Translation>`{.interpreted-text role="ref"}
resources.

::: rst-class
classref-introduction-group
:::

## Description

**TranslationDomain** is a self-contained collection of
`Translation<class_Translation>`{.interpreted-text role="ref"}
resources. Translations can be added to or removed from it.

If you\'re working with the main translation domain, it is more
convenient to use the wrap methods on
`TranslationServer<class_TranslationServer>`{.interpreted-text
role="ref"}.

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

:::: {#class_TranslationDomain_property_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `true`
`🔗<class_TranslationDomain_property_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_enabled**()

If `true`, translation is enabled. Otherwise,
`translate()<class_TranslationDomain_method_translate>`{.interpreted-text
role="ref"} and
`translate_plural()<class_TranslationDomain_method_translate_plural>`{.interpreted-text
role="ref"} will return the input message unchanged regardless of the
current locale.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_property_pseudolocalization_accents_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**pseudolocalization_accents_enabled** = `true`
`🔗<class_TranslationDomain_property_pseudolocalization_accents_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_accents_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_pseudolocalization_accents_enabled**()

Replace all characters with their accented variants during
pseudolocalization.

\*\*Note:\*\* Updating this property does not automatically update texts
in the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} notification manually after you have finished modifying
pseudolocalization related options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_property_pseudolocalization_double_vowels_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**pseudolocalization_double_vowels_enabled** = `false`
`🔗<class_TranslationDomain_property_pseudolocalization_double_vowels_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_double_vowels_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_pseudolocalization_double_vowels_enabled**()

Double vowels in strings during pseudolocalization to simulate the
lengthening of text due to localization.

\*\*Note:\*\* Updating this property does not automatically update texts
in the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} notification manually after you have finished modifying
pseudolocalization related options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_property_pseudolocalization_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**pseudolocalization_enabled** = `false`
`🔗<class_TranslationDomain_property_pseudolocalization_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_pseudolocalization_enabled**()

If `true`, enables pseudolocalization for the project. This can be used
to spot untranslatable strings or layout issues that may occur once the
project is localized to languages that have longer strings than the
source language.

\*\*Note:\*\* Updating this property does not automatically update texts
in the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} notification manually after you have finished modifying
pseudolocalization related options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_property_pseudolocalization_expansion_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**pseudolocalization_expansion_ratio** = `0.0`
`🔗<class_TranslationDomain_property_pseudolocalization_expansion_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_expansion_ratio**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pseudolocalization_expansion_ratio**()

The expansion ratio to use during pseudolocalization. A value of `0.3`
is sufficient for most practical purposes, and will increase the length
of each string by 30%.

\*\*Note:\*\* Updating this property does not automatically update texts
in the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} notification manually after you have finished modifying
pseudolocalization related options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_property_pseudolocalization_fake_bidi_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**pseudolocalization_fake_bidi_enabled** = `false`
`🔗<class_TranslationDomain_property_pseudolocalization_fake_bidi_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_fake_bidi_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_pseudolocalization_fake_bidi_enabled**()

If `true`, emulate bidirectional (right-to-left) text when
pseudolocalization is enabled. This can be used to spot issues with RTL
layout and UI mirroring that will crop up if the project is localized to
RTL languages such as Arabic or Hebrew.

\*\*Note:\*\* Updating this property does not automatically update texts
in the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} notification manually after you have finished modifying
pseudolocalization related options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_property_pseudolocalization_override_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**pseudolocalization_override_enabled** = `false`
`🔗<class_TranslationDomain_property_pseudolocalization_override_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_override_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_pseudolocalization_override_enabled**()

Replace all characters in the string with `*`. Useful for finding
non-localizable strings.

\*\*Note:\*\* Updating this property does not automatically update texts
in the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} notification manually after you have finished modifying
pseudolocalization related options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_property_pseudolocalization_prefix}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**pseudolocalization_prefix** = `"["`
`🔗<class_TranslationDomain_property_pseudolocalization_prefix>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_prefix**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_pseudolocalization_prefix**()

Prefix that will be prepended to the pseudolocalized string.

\*\*Note:\*\* Updating this property does not automatically update texts
in the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} notification manually after you have finished modifying
pseudolocalization related options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_property_pseudolocalization_skip_placeholders_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**pseudolocalization_skip_placeholders_enabled** = `true`
`🔗<class_TranslationDomain_property_pseudolocalization_skip_placeholders_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_skip_placeholders_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_pseudolocalization_skip_placeholders_enabled**()

Skip placeholders for string formatting like `%s` or `%f` during
pseudolocalization. Useful to identify strings which need additional
control characters to display correctly.

\*\*Note:\*\* Updating this property does not automatically update texts
in the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} notification manually after you have finished modifying
pseudolocalization related options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_property_pseudolocalization_suffix}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**pseudolocalization_suffix** = `"]"`
`🔗<class_TranslationDomain_property_pseudolocalization_suffix>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_suffix**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_pseudolocalization_suffix**()

Suffix that will be appended to the pseudolocalized string.

\*\*Note:\*\* Updating this property does not automatically update texts
in the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} notification manually after you have finished modifying
pseudolocalization related options.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TranslationDomain_method_add_translation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_translation**(translation:
`Translation<class_Translation>`{.interpreted-text role="ref"})
`🔗<class_TranslationDomain_method_add_translation>`{.interpreted-text
role="ref"}

Adds a translation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_TranslationDomain_method_clear>`{.interpreted-text role="ref"}

Removes all translations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_method_get_locale_override}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_locale_override**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationDomain_method_get_locale_override>`{.interpreted-text
role="ref"}

Returns the locale override of the domain. Returns an empty string if
locale override is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_method_get_translation_object}
::: rst-class
classref-method
:::
::::

`Translation<class_Translation>`{.interpreted-text role="ref"}
**get_translation_object**(locale:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationDomain_method_get_translation_object>`{.interpreted-text
role="ref"}

Returns the `Translation<class_Translation>`{.interpreted-text
role="ref"} instance that best matches `locale`. Returns `null` if there
are no matches.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_method_pseudolocalize}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**pseudolocalize**(message:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationDomain_method_pseudolocalize>`{.interpreted-text
role="ref"}

Returns the pseudolocalized string based on the `message` passed in.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_method_remove_translation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_translation**(translation:
`Translation<class_Translation>`{.interpreted-text role="ref"})
`🔗<class_TranslationDomain_method_remove_translation>`{.interpreted-text
role="ref"}

Removes the given translation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_method_set_locale_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_locale_override**(locale: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TranslationDomain_method_set_locale_override>`{.interpreted-text
role="ref"}

Sets the locale override of the domain.

If `locale` is an empty string, locale override is disabled. Otherwise,
`locale` will be standardized to match known locales (e.g. `en-US` would
be matched to `en_US`).

\*\*Note:\*\* Calling this method does not automatically update texts in
the scene tree. Please propagate the
`MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"} signal manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_method_translate}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**translate**(message: `StringName<class_StringName>`{.interpreted-text
role="ref"}, context: `StringName<class_StringName>`{.interpreted-text
role="ref"} = &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationDomain_method_translate>`{.interpreted-text
role="ref"}

Returns the current locale\'s translation for the given message and
context.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationDomain_method_translate_plural}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**translate_plural**(message:
`StringName<class_StringName>`{.interpreted-text role="ref"},
message_plural: `StringName<class_StringName>`{.interpreted-text
role="ref"}, n: `int<class_int>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationDomain_method_translate_plural>`{.interpreted-text
role="ref"}

Returns the current locale\'s translation for the given message, plural
message and context.

The number `n` is the number or quantity of the plural object. It will
be used to guide the translation system to fetch the correct plural form
for the selected language.
