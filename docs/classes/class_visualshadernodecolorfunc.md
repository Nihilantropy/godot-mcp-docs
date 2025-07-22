github_url
:   hide

# VisualShaderNodeColorFunc {#class_VisualShaderNodeColorFunc}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `Color<class_Color>`{.interpreted-text role="ref"} function to be used
within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Accept a `Color<class_Color>`{.interpreted-text role="ref"} to the input
port and transform it according to
`function<class_VisualShaderNodeColorFunc_property_function>`{.interpreted-text
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

## Enumerations

:::: {#enum_VisualShaderNodeColorFunc_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_GRAYSCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_GRAYSCALE** = `0`

Converts the color to grayscale using the following formula:

    vec3 c = input;
    float max1 = max(c.r, c.g);
    float max2 = max(max1, c.b);
    float max3 = max(max1, max2);
    return vec3(max3, max3, max3);

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_HSV2RGB}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_HSV2RGB** = `1`

Converts HSV vector to RGB equivalent.

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_RGB2HSV}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_RGB2HSV** = `2`

Converts RGB vector to HSV equivalent.

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_SEPIA}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SEPIA** = `3`

Applies sepia tone effect using the following formula:

    vec3 c = input;
    float r = (c.r * 0.393) + (c.g * 0.769) + (c.b * 0.189);
    float g = (c.r * 0.349) + (c.g * 0.686) + (c.b * 0.168);
    float b = (c.r * 0.272) + (c.g * 0.534) + (c.b * 0.131);
    return vec3(r, g, b);

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_LINEAR_TO_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_LINEAR_TO_SRGB** = `4`

Converts color from linear color space to sRGB color space using the
following formula:

    vec3 c = clamp(c, vec3(0.0), vec3(1.0));
    const vec3 a = vec3(0.055f);
    return mix((vec3(1.0f) + a) * pow(c.rgb, vec3(1.0f / 2.4f)) - a, 12.92f * c.rgb, lessThan(c.rgb, vec3(0.0031308f)));

The Compatibility renderer uses a simpler formula:

    vec3 c = input;
    return max(vec3(1.055) * pow(c, vec3(0.416666667)) - vec3(0.055), vec3(0.0));

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_SRGB_TO_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SRGB_TO_LINEAR** = `5`

Converts color from sRGB color space to linear color space using the
following formula:

    vec3 c = input;
    return mix(pow((c.rgb + vec3(0.055)) * (1.0 / (1.0 + 0.055)), vec3(2.4)), c.rgb * (1.0 / 12.92), lessThan(c.rgb, vec3(0.04045)));

The Compatibility renderer uses a simpler formula:

    vec3 c = input;
    return c * (c * (c * 0.305306011 + 0.682171111) + 0.012522878);

:::: {#class_VisualShaderNodeColorFunc_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `6`

Represents the size of the
`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeColorFunc_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
role="ref"} **function** = `0`
`🔗<class_VisualShaderNodeColorFunc_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeColorFunc_Function>`{.interpreted-text
  role="ref"} **get_function**()

A function to be applied to the input color.
