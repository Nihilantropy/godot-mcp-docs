github_url
:   hide

# SVGTexture {#class_SVGTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A scalable `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
based on an SVG image.

::: rst-class
classref-introduction-group
:::

## Description

A scalable `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
based on an SVG image. **SVGTexture**s are automatically re-rasterized
to match font oversampling.

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

:::: {#class_SVGTexture_property_base_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **base_scale** =
`1.0` `🔗<class_SVGTexture_property_base_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_base_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_base_scale**()

SVG texture scale. `1.0` is the original SVG size. Higher values result
in a larger image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SVGTexture_property_color_map}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**color_map** = `{}`
`🔗<class_SVGTexture_property_color_map>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_map**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_color_map**()

If set, remaps SVG texture colors according to
`Color<class_Color>`{.interpreted-text
role="ref"}-`Color<class_Color>`{.interpreted-text role="ref"} map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SVGTexture_property_saturation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **saturation** =
`1.0` `🔗<class_SVGTexture_property_saturation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_saturation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_saturation**()

Overrides texture saturation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SVGTexture_method_create_from_string}
::: rst-class
classref-method
:::
::::

`SVGTexture<class_SVGTexture>`{.interpreted-text role="ref"}
**create_from_string**(source: `String<class_String>`{.interpreted-text
role="ref"}, scale: `float<class_float>`{.interpreted-text role="ref"} =
1.0, saturation: `float<class_float>`{.interpreted-text role="ref"} =
1.0, color_map: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} = {})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_SVGTexture_method_create_from_string>`{.interpreted-text
role="ref"}

Creates a new **SVGTexture** and initializes it by allocating and
setting the SVG data from string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SVGTexture_method_get_source}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_source**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_SVGTexture_method_get_source>`{.interpreted-text
role="ref"}

Returns SVG source code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SVGTexture_method_set_size_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_size_override**(size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_SVGTexture_method_set_size_override>`{.interpreted-text
role="ref"}

Resizes the texture to the specified dimensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SVGTexture_method_set_source}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_source**(source: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_SVGTexture_method_set_source>`{.interpreted-text
role="ref"}

Sets SVG source code.
