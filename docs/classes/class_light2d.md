github_url
:   hide

# Light2D {#class_Light2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`DirectionalLight2D<class_DirectionalLight2D>`{.interpreted-text
role="ref"}, `PointLight2D<class_PointLight2D>`{.interpreted-text
role="ref"}

Casts light in a 2D environment.

::: rst-class
classref-introduction-group
:::

## Description

Casts light in a 2D environment. A light is defined as a color, an
energy value, a mode (see constants), and various other parameters
(range and shadows-related).

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D lights and shadows <../tutorials/2d/2d_lights_and_shadows>`{.interpreted-text
  role="doc"}

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

## Enumerations

:::: {#enum_Light2D_ShadowFilter}
::: rst-class
classref-enumeration
:::
::::

enum **ShadowFilter**: `🔗<enum_Light2D_ShadowFilter>`{.interpreted-text
role="ref"}

:::: {#class_Light2D_constant_SHADOW_FILTER_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowFilter<enum_Light2D_ShadowFilter>`{.interpreted-text role="ref"}
**SHADOW_FILTER_NONE** = `0`

No filter applies to the shadow map. This provides hard shadow edges and
is the fastest to render. See
`shadow_filter<class_Light2D_property_shadow_filter>`{.interpreted-text
role="ref"}.

:::: {#class_Light2D_constant_SHADOW_FILTER_PCF5}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowFilter<enum_Light2D_ShadowFilter>`{.interpreted-text role="ref"}
**SHADOW_FILTER_PCF5** = `1`

Percentage closer filtering (5 samples) applies to the shadow map. This
is slower compared to hard shadow rendering. See
`shadow_filter<class_Light2D_property_shadow_filter>`{.interpreted-text
role="ref"}.

:::: {#class_Light2D_constant_SHADOW_FILTER_PCF13}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowFilter<enum_Light2D_ShadowFilter>`{.interpreted-text role="ref"}
**SHADOW_FILTER_PCF13** = `2`

Percentage closer filtering (13 samples) applies to the shadow map. This
is the slowest shadow filtering mode, and should be used sparingly. See
`shadow_filter<class_Light2D_property_shadow_filter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Light2D_BlendMode}
::: rst-class
classref-enumeration
:::
::::

enum **BlendMode**: `🔗<enum_Light2D_BlendMode>`{.interpreted-text
role="ref"}

:::: {#class_Light2D_constant_BLEND_MODE_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_Light2D_BlendMode>`{.interpreted-text role="ref"}
**BLEND_MODE_ADD** = `0`

Adds the value of pixels corresponding to the Light2D to the values of
pixels under it. This is the common behavior of a light.

:::: {#class_Light2D_constant_BLEND_MODE_SUB}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_Light2D_BlendMode>`{.interpreted-text role="ref"}
**BLEND_MODE_SUB** = `1`

Subtracts the value of pixels corresponding to the Light2D to the values
of pixels under it, resulting in inversed light effect.

:::: {#class_Light2D_constant_BLEND_MODE_MIX}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendMode<enum_Light2D_BlendMode>`{.interpreted-text role="ref"}
**BLEND_MODE_MIX** = `2`

Mix the value of pixels corresponding to the Light2D to the values of
pixels under it by linear interpolation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Light2D_property_blend_mode}
::: rst-class
classref-property
:::
::::

`BlendMode<enum_Light2D_BlendMode>`{.interpreted-text role="ref"}
**blend_mode** = `0`
`🔗<class_Light2D_property_blend_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_mode**(value:
  `BlendMode<enum_Light2D_BlendMode>`{.interpreted-text role="ref"})
- `BlendMode<enum_Light2D_BlendMode>`{.interpreted-text role="ref"}
  **get_blend_mode**()

The Light2D\'s blend mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(1, 1, 1, 1)` `🔗<class_Light2D_property_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

The Light2D\'s `Color<class_Color>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_editor_only}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editor_only** =
`false` `🔗<class_Light2D_property_editor_only>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editor_only**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_editor_only**()

If `true`, Light2D will only appear when editing the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `true`
`🔗<class_Light2D_property_enabled>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_enabled**()

If `true`, Light2D will emit light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **energy** = `1.0`
`🔗<class_Light2D_property_energy>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_energy**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_energy**()

The Light2D\'s energy value. The larger the value, the stronger the
light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_range_item_cull_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **range_item_cull_mask**
= `1`
`🔗<class_Light2D_property_range_item_cull_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_item_cull_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_item_cull_mask**()

The layer mask. Only objects with a matching
`CanvasItem.light_mask<class_CanvasItem_property_light_mask>`{.interpreted-text
role="ref"} will be affected by the Light2D. See also
`shadow_item_cull_mask<class_Light2D_property_shadow_item_cull_mask>`{.interpreted-text
role="ref"}, which affects which objects can cast shadows.

\*\*Note:\*\*
`range_item_cull_mask<class_Light2D_property_range_item_cull_mask>`{.interpreted-text
role="ref"} is ignored by
`DirectionalLight2D<class_DirectionalLight2D>`{.interpreted-text
role="ref"}, which will always light a 2D node regardless of the 2D
node\'s
`CanvasItem.light_mask<class_CanvasItem_property_light_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_range_layer_max}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **range_layer_max** = `0`
`🔗<class_Light2D_property_range_layer_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_layer_range_max**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_layer_range_max**()

Maximum layer value of objects that are affected by the Light2D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_range_layer_min}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **range_layer_min** = `0`
`🔗<class_Light2D_property_range_layer_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_layer_range_min**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_layer_range_min**()

Minimum layer value of objects that are affected by the Light2D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_range_z_max}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **range_z_max** = `1024`
`🔗<class_Light2D_property_range_z_max>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_z_range_max**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_z_range_max**()

Maximum `z` value of objects that are affected by the Light2D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_range_z_min}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **range_z_min** = `-1024`
`🔗<class_Light2D_property_range_z_min>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_z_range_min**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_z_range_min**()

Minimum `z` value of objects that are affected by the Light2D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_shadow_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **shadow_color** =
`Color(0, 0, 0, 0)`
`🔗<class_Light2D_property_shadow_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_shadow_color**()

`Color<class_Color>`{.interpreted-text role="ref"} of shadows cast by
the Light2D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_shadow_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shadow_enabled** =
`false` `🔗<class_Light2D_property_shadow_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_shadow_enabled**()

If `true`, the Light2D will cast shadows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_shadow_filter}
::: rst-class
classref-property
:::
::::

`ShadowFilter<enum_Light2D_ShadowFilter>`{.interpreted-text role="ref"}
**shadow_filter** = `0`
`🔗<class_Light2D_property_shadow_filter>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_filter**(value:
  `ShadowFilter<enum_Light2D_ShadowFilter>`{.interpreted-text
  role="ref"})
- `ShadowFilter<enum_Light2D_ShadowFilter>`{.interpreted-text
  role="ref"} **get_shadow_filter**()

Shadow filter type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_shadow_filter_smooth}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shadow_filter_smooth** = `0.0`
`🔗<class_Light2D_property_shadow_filter_smooth>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_smooth**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_shadow_smooth**()

Smoothing value for shadows. Higher values will result in softer
shadows, at the cost of visible streaks that can appear in shadow
rendering.
`shadow_filter_smooth<class_Light2D_property_shadow_filter_smooth>`{.interpreted-text
role="ref"} only has an effect if
`shadow_filter<class_Light2D_property_shadow_filter>`{.interpreted-text
role="ref"} is
`SHADOW_FILTER_PCF5<class_Light2D_constant_SHADOW_FILTER_PCF5>`{.interpreted-text
role="ref"} or
`SHADOW_FILTER_PCF13<class_Light2D_constant_SHADOW_FILTER_PCF13>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_property_shadow_item_cull_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_item_cull_mask**
= `1`
`🔗<class_Light2D_property_shadow_item_cull_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_item_shadow_cull_mask**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_item_shadow_cull_mask**()

The shadow mask. Used with
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"}
to cast shadows. Only occluders with a matching
`CanvasItem.light_mask<class_CanvasItem_property_light_mask>`{.interpreted-text
role="ref"} will cast shadows. See also
`range_item_cull_mask<class_Light2D_property_range_item_cull_mask>`{.interpreted-text
role="ref"}, which affects which objects can *receive* the light.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Light2D_method_get_height}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Light2D_method_get_height>`{.interpreted-text
role="ref"}

Returns the light\'s height, which is used in 2D normal mapping. See
`PointLight2D.height<class_PointLight2D_property_height>`{.interpreted-text
role="ref"} and
`DirectionalLight2D.height<class_DirectionalLight2D_property_height>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Light2D_method_set_height}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_height**(height: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Light2D_method_set_height>`{.interpreted-text
role="ref"}

Sets the light\'s height, which is used in 2D normal mapping. See
`PointLight2D.height<class_PointLight2D_property_height>`{.interpreted-text
role="ref"} and
`DirectionalLight2D.height<class_DirectionalLight2D_property_height>`{.interpreted-text
role="ref"}.
