github_url
:   hide

# ColorPalette {#class_ColorPalette}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A resource class for managing a palette of colors, which can be loaded
and saved using `ColorPicker<class_ColorPicker>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

The **ColorPalette** resource is designed to store and manage a
collection of colors. This resource is useful in scenarios where a
predefined set of colors is required, such as for creating themes,
designing user interfaces, or managing game assets. The built-in
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"} control
can also make use of **ColorPalette** without additional code.

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

:::: {#class_ColorPalette_property_colors}
::: rst-class
classref-property
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**colors** = `PackedColorArray()`
`🔗<class_ColorPalette_property_colors>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_colors**(value:
  `PackedColorArray<class_PackedColorArray>`{.interpreted-text
  role="ref"})
- `PackedColorArray<class_PackedColorArray>`{.interpreted-text
  role="ref"} **get_colors**()

A `PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"} containing the colors in the palette.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
for more details.
