github_url
:   hide

# VisualShaderNodeFloatParameter {#class_VisualShaderNodeFloatParameter}

**Inherits:**
`VisualShaderNodeParameter<class_VisualShaderNodeParameter>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A scalar float parameter to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Translated to `uniform float` in the shader language.

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

:::: {#enum_VisualShaderNodeFloatParameter_Hint}
::: rst-class
classref-enumeration
:::
::::

enum **Hint**:
`🔗<enum_VisualShaderNodeFloatParameter_Hint>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeFloatParameter_constant_HINT_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Hint<enum_VisualShaderNodeFloatParameter_Hint>`{.interpreted-text
role="ref"} **HINT_NONE** = `0`

No hint used.

:::: {#class_VisualShaderNodeFloatParameter_constant_HINT_RANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Hint<enum_VisualShaderNodeFloatParameter_Hint>`{.interpreted-text
role="ref"} **HINT_RANGE** = `1`

A range hint for scalar value, which limits possible input values
between
`min<class_VisualShaderNodeFloatParameter_property_min>`{.interpreted-text
role="ref"} and
`max<class_VisualShaderNodeFloatParameter_property_max>`{.interpreted-text
role="ref"}. Translated to `hint_range(min, max)` in shader code.

:::: {#class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP}
::: rst-class
classref-enumeration-constant
:::
::::

`Hint<enum_VisualShaderNodeFloatParameter_Hint>`{.interpreted-text
role="ref"} **HINT_RANGE_STEP** = `2`

A range hint for scalar value with step, which limits possible input
values between
`min<class_VisualShaderNodeFloatParameter_property_min>`{.interpreted-text
role="ref"} and
`max<class_VisualShaderNodeFloatParameter_property_max>`{.interpreted-text
role="ref"}, with a step (increment) of
`step<class_VisualShaderNodeFloatParameter_property_step>`{.interpreted-text
role="ref"}). Translated to `hint_range(min, max, step)` in shader code.

:::: {#class_VisualShaderNodeFloatParameter_constant_HINT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Hint<enum_VisualShaderNodeFloatParameter_Hint>`{.interpreted-text
role="ref"} **HINT_MAX** = `3`

Represents the size of the
`Hint<enum_VisualShaderNodeFloatParameter_Hint>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeFloatParameter_property_default_value}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **default_value** =
`0.0`
`🔗<class_VisualShaderNodeFloatParameter_property_default_value>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_value**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_default_value**()

A default value to be assigned within the shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFloatParameter_property_default_value_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**default_value_enabled** = `false`
`🔗<class_VisualShaderNodeFloatParameter_property_default_value_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_value_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_default_value_enabled**()

Enables usage of the
`default_value<class_VisualShaderNodeFloatParameter_property_default_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFloatParameter_property_hint}
::: rst-class
classref-property
:::
::::

`Hint<enum_VisualShaderNodeFloatParameter_Hint>`{.interpreted-text
role="ref"} **hint** = `0`
`🔗<class_VisualShaderNodeFloatParameter_property_hint>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hint**(value:
  `Hint<enum_VisualShaderNodeFloatParameter_Hint>`{.interpreted-text
  role="ref"})
- `Hint<enum_VisualShaderNodeFloatParameter_Hint>`{.interpreted-text
  role="ref"} **get_hint**()

A hint applied to the uniform, which controls the values it can take
when set through the Inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFloatParameter_property_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max** = `1.0`
`🔗<class_VisualShaderNodeFloatParameter_property_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_max**()

Minimum value for range hints. Used if
`hint<class_VisualShaderNodeFloatParameter_property_hint>`{.interpreted-text
role="ref"} is set to
`HINT_RANGE<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE>`{.interpreted-text
role="ref"} or
`HINT_RANGE_STEP<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFloatParameter_property_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **min** = `0.0`
`🔗<class_VisualShaderNodeFloatParameter_property_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_min**()

Maximum value for range hints. Used if
`hint<class_VisualShaderNodeFloatParameter_property_hint>`{.interpreted-text
role="ref"} is set to
`HINT_RANGE<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE>`{.interpreted-text
role="ref"} or
`HINT_RANGE_STEP<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeFloatParameter_property_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **step** = `0.1`
`🔗<class_VisualShaderNodeFloatParameter_property_step>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_step**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_step**()

Step (increment) value for the range hint with step. Used if
`hint<class_VisualShaderNodeFloatParameter_property_hint>`{.interpreted-text
role="ref"} is set to
`HINT_RANGE_STEP<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP>`{.interpreted-text
role="ref"}.
