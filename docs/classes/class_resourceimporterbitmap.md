github_url
:   hide

# ResourceImporterBitMap {#class_ResourceImporterBitMap}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports a `BitMap<class_BitMap>`{.interpreted-text role="ref"} resource
(2D array of boolean values).

::: rst-class
classref-introduction-group
:::

## Description

`BitMap<class_BitMap>`{.interpreted-text role="ref"} resources are
typically used as click masks in
`TextureButton<class_TextureButton>`{.interpreted-text role="ref"} and
`TouchScreenButton<class_TouchScreenButton>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Importing images <../tutorials/assets_pipeline/importing_images>`{.interpreted-text
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

:::: {#class_ResourceImporterBitMap_property_create_from}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **create_from** = `0`
`🔗<class_ResourceImporterBitMap_property_create_from>`{.interpreted-text
role="ref"}

The data source to use for generating the bitmap.

\*\*Black & White:\*\* Pixels whose HSV value is greater than the
`threshold<class_ResourceImporterBitMap_property_threshold>`{.interpreted-text
role="ref"} will be considered as \"enabled\" (bit is `true`). If the
pixel is lower than or equal to the threshold, it will be considered as
\"disabled\" (bit is `false`).

\*\*Alpha:\*\* Pixels whose alpha value is greater than the
`threshold<class_ResourceImporterBitMap_property_threshold>`{.interpreted-text
role="ref"} will be considered as \"enabled\" (bit is `true`). If the
pixel is lower than or equal to the threshold, it will be considered as
\"disabled\" (bit is `false`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterBitMap_property_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **threshold** = `0.5`
`🔗<class_ResourceImporterBitMap_property_threshold>`{.interpreted-text
role="ref"}

The threshold to use to determine which bits should be considered
enabled or disabled. See also
`create_from<class_ResourceImporterBitMap_property_create_from>`{.interpreted-text
role="ref"}.
