github_url
:   hide

# ResourceImporterSVG {#class_ResourceImporterSVG}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports an SVG file as a scalable texture for use in 2D or 3D rendering.

::: rst-class
classref-introduction-group
:::

## Description

This importer imports `SVGTexture<class_SVGTexture>`{.interpreted-text
role="ref"} resources. See also
`ResourceImporterTexture<class_ResourceImporterTexture>`{.interpreted-text
role="ref"} and
`ResourceImporterImage<class_ResourceImporterImage>`{.interpreted-text
role="ref"}.

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

:::: {#class_ResourceImporterSVG_property_base_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **base_scale** =
`1.0`
`🔗<class_ResourceImporterSVG_property_base_scale>`{.interpreted-text
role="ref"}

SVG texture scale. `1.0` is the original SVG size. Higher values result
in a larger image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterSVG_property_color_map}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**color_map** = `{}`
`🔗<class_ResourceImporterSVG_property_color_map>`{.interpreted-text
role="ref"}

If set, remaps SVG texture colors according to
`Color<class_Color>`{.interpreted-text
role="ref"}-`Color<class_Color>`{.interpreted-text role="ref"} map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterSVG_property_compress}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **compress** = `true`
`🔗<class_ResourceImporterSVG_property_compress>`{.interpreted-text
role="ref"}

If `true`, uses lossless compression for the SVG source.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterSVG_property_saturation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **saturation** =
`1.0`
`🔗<class_ResourceImporterSVG_property_saturation>`{.interpreted-text
role="ref"}

Overrides texture saturation.
