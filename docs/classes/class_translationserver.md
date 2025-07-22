github_url
:   hide

# TranslationServer {#class_TranslationServer}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

The server responsible for language translations.

::: rst-class
classref-introduction-group
:::

## Description

The translation server is the API backend that manages all language
translations.

Translations are stored in
`TranslationDomain<class_TranslationDomain>`{.interpreted-text
role="ref"}s, which can be accessed by name. The most commonly used
translation domain is the main translation domain. It always exists and
can be accessed using an empty
`StringName<class_StringName>`{.interpreted-text role="ref"}. The
translation server provides wrapper methods for accessing the main
translation domain directly, without having to fetch the translation
domain first. Custom translation domains are mainly for advanced usages
like editor plugins. Names starting with `godot.` are reserved for
engine internals.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Internationalizing games <../tutorials/i18n/internationalizing_games>`{.interpreted-text
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

:::: {#class_TranslationServer_property_pseudolocalization_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**pseudolocalization_enabled** = `false`
`🔗<class_TranslationServer_property_pseudolocalization_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pseudolocalization_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_pseudolocalization_enabled**()

If `true`, enables the use of pseudolocalization on the main translation
domain. See
`ProjectSettings.internationalization/pseudolocalization/use_pseudolocalization<class_ProjectSettings_property_internationalization/pseudolocalization/use_pseudolocalization>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TranslationServer_method_add_translation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_translation**(translation:
`Translation<class_Translation>`{.interpreted-text role="ref"})
`🔗<class_TranslationServer_method_add_translation>`{.interpreted-text
role="ref"}

Adds a translation to the main translation domain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_TranslationServer_method_clear>`{.interpreted-text role="ref"}

Removes all translations from the main translation domain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_compare_locales}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**compare_locales**(locale_a: `String<class_String>`{.interpreted-text
role="ref"}, locale_b: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_compare_locales>`{.interpreted-text
role="ref"}

Compares two locales and returns a similarity score between `0` (no
match) and `10` (full match).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_all_countries}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_all_countries**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_get_all_countries>`{.interpreted-text
role="ref"}

Returns an array of known country codes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_all_languages}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_all_languages**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_get_all_languages>`{.interpreted-text
role="ref"}

Returns array of known language codes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_all_scripts}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_all_scripts**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_get_all_scripts>`{.interpreted-text
role="ref"}

Returns an array of known script codes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_country_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_country_name**(country: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_get_country_name>`{.interpreted-text
role="ref"}

Returns a readable country name for the `country` code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_language_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_language_name**(language: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_get_language_name>`{.interpreted-text
role="ref"}

Returns a readable language name for the `language` code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_loaded_locales}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_loaded_locales**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_get_loaded_locales>`{.interpreted-text
role="ref"}

Returns an array of all loaded locales of the project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_locale}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_locale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_get_locale>`{.interpreted-text
role="ref"}

Returns the current locale of the project.

See also `OS.get_locale()<class_OS_method_get_locale>`{.interpreted-text
role="ref"} and
`OS.get_locale_language()<class_OS_method_get_locale_language>`{.interpreted-text
role="ref"} to query the locale of the user system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_locale_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_locale_name**(locale: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_get_locale_name>`{.interpreted-text
role="ref"}

Returns a locale\'s language and its variant (e.g. `"en_US"` would
return `"English (United States)"`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_or_add_domain}
::: rst-class
classref-method
:::
::::

`TranslationDomain<class_TranslationDomain>`{.interpreted-text
role="ref"} **get_or_add_domain**(domain:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_TranslationServer_method_get_or_add_domain>`{.interpreted-text
role="ref"}

Returns the translation domain with the specified name. An empty
translation domain will be created and added if it does not exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_script_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_script_name**(script: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_get_script_name>`{.interpreted-text
role="ref"}

Returns a readable script name for the `script` code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_tool_locale}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tool_locale**()
`🔗<class_TranslationServer_method_get_tool_locale>`{.interpreted-text
role="ref"}

Returns the current locale of the editor.

\*\*Note:\*\* When called from an exported project returns the same
value as
`get_locale()<class_TranslationServer_method_get_locale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_get_translation_object}
::: rst-class
classref-method
:::
::::

`Translation<class_Translation>`{.interpreted-text role="ref"}
**get_translation_object**(locale:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TranslationServer_method_get_translation_object>`{.interpreted-text
role="ref"}

Returns the `Translation<class_Translation>`{.interpreted-text
role="ref"} instance that best matches `locale` in the main translation
domain. Returns `null` if there are no matches.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_has_domain}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_domain**(domain:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_has_domain>`{.interpreted-text
role="ref"}

Returns `true` if a translation domain with the specified name exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_pseudolocalize}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**pseudolocalize**(message:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_pseudolocalize>`{.interpreted-text
role="ref"}

Returns the pseudolocalized string based on the `message` passed in.

\*\*Note:\*\* This method always uses the main translation domain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_reload_pseudolocalization}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reload_pseudolocalization**()
`🔗<class_TranslationServer_method_reload_pseudolocalization>`{.interpreted-text
role="ref"}

Reparses the pseudolocalization options and reloads the translation for
the main translation domain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_remove_domain}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_domain**(domain:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_TranslationServer_method_remove_domain>`{.interpreted-text
role="ref"}

Removes the translation domain with the specified name.

\*\*Note:\*\* Trying to remove the main translation domain is an error.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_remove_translation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_translation**(translation:
`Translation<class_Translation>`{.interpreted-text role="ref"})
`🔗<class_TranslationServer_method_remove_translation>`{.interpreted-text
role="ref"}

Removes the given translation from the main translation domain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_set_locale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_locale**(locale: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TranslationServer_method_set_locale>`{.interpreted-text
role="ref"}

Sets the locale of the project. The `locale` string will be standardized
to match known locales (e.g. `en-US` would be matched to `en_US`).

If translations have been loaded beforehand for the new locale, they
will be applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_standardize_locale}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**standardize_locale**(locale: `String<class_String>`{.interpreted-text
role="ref"}, add_defaults: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_standardize_locale>`{.interpreted-text
role="ref"}

Returns a `locale` string standardized to match known locales (e.g.
`en-US` would be matched to `en_US`). If `add_defaults` is `true`, the
locale may have a default script or country added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_translate}
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
`🔗<class_TranslationServer_method_translate>`{.interpreted-text
role="ref"}

Returns the current locale\'s translation for the given message and
context.

\*\*Note:\*\* This method always uses the main translation domain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TranslationServer_method_translate_plural}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**translate_plural**(message:
`StringName<class_StringName>`{.interpreted-text role="ref"},
plural_message: `StringName<class_StringName>`{.interpreted-text
role="ref"}, n: `int<class_int>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TranslationServer_method_translate_plural>`{.interpreted-text
role="ref"}

Returns the current locale\'s translation for the given message, plural
message and context.

The number `n` is the number or quantity of the plural object. It will
be used to guide the translation system to fetch the correct plural form
for the selected language.

\*\*Note:\*\* This method always uses the main translation domain.
