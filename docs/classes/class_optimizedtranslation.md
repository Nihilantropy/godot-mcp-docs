github_url
:   hide

# OptimizedTranslation {#class_OptimizedTranslation}

**Inherits:** `Translation<class_Translation>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

An optimized translation, used by default for CSV Translations.

::: rst-class
classref-introduction-group
:::

## Description

An optimized translation, used by default for CSV Translations. Uses
real-time compressed translations, which results in very small
dictionaries.

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

:::: {#class_OptimizedTranslation_method_generate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**generate**(from: `Translation<class_Translation>`{.interpreted-text
role="ref"})
`🔗<class_OptimizedTranslation_method_generate>`{.interpreted-text
role="ref"}

Generates and sets an optimized translation from the given
`Translation<class_Translation>`{.interpreted-text role="ref"} resource.

\*\*Note:\*\* This method is intended to be used in the editor. It does
nothing when called from an exported project.
