github_url
:   hide

# ResourceImporterCSVTranslation {#class_ResourceImporterCSVTranslation}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports comma-separated values

::: rst-class
classref-introduction-group
:::

## Description

Comma-separated values are a plain text table storage format. The
format\'s simplicity makes it easy to edit in any text editor or
spreadsheet software. This makes it a common choice for game
localization.

\*\*Example CSV file:\*\*

``` text
keys,en,es,ja
GREET,"Hello, friend!","Hola, amigo!",こんにちは
ASK,How are you?,Cómo está?,元気ですか
BYE,Goodbye,Adiós,さようなら
QUOTE,"""Hello"" said the man.","""Hola"" dijo el hombre.",「こんにちは」男は言いました
```

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Importing translations <../tutorials/assets_pipeline/importing_translations>`{.interpreted-text
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

:::: {#class_ResourceImporterCSVTranslation_property_compress}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **compress** = `true`
`🔗<class_ResourceImporterCSVTranslation_property_compress>`{.interpreted-text
role="ref"}

If `true`, creates an
`OptimizedTranslation<class_OptimizedTranslation>`{.interpreted-text
role="ref"} instead of a
`Translation<class_Translation>`{.interpreted-text role="ref"}. This
makes the resulting file smaller at the cost of a small CPU overhead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterCSVTranslation_property_delimiter}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **delimiter** = `0`
`🔗<class_ResourceImporterCSVTranslation_property_delimiter>`{.interpreted-text
role="ref"}

The delimiter to use in the CSV file. The default value matches the
common CSV convention. Tab-separated values are sometimes called TSV
files.
