github_url
:   hide

# VisualShaderNodeIntParameter {#class_VisualShaderNodeIntParameter}

**Inherits:**
`VisualShaderNodeParameter<class_VisualShaderNodeParameter>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node for shader parameter (uniform) of type
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A
`VisualShaderNodeParameter<class_VisualShaderNodeParameter>`{.interpreted-text
role="ref"} of type `int<class_int>`{.interpreted-text role="ref"}.
Offers additional customization for range of accepted values.

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

:::: {#enum_VisualShaderNodeIntParameter_Hint}
::: rst-class
classref-enumeration
:::
::::

enum **Hint**:
`🔗<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeIntParameter_constant_HINT_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Hint<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
role="ref"} **HINT_NONE** = `0`

The parameter will not constrain its value.

:::: {#class_VisualShaderNodeIntParameter_constant_HINT_RANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Hint<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
role="ref"} **HINT_RANGE** = `1`

The parameter\'s value must be within the specified
`min<class_VisualShaderNodeIntParameter_property_min>`{.interpreted-text
role="ref"}/`max<class_VisualShaderNodeIntParameter_property_max>`{.interpreted-text
role="ref"} range.

:::: {#class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP}
::: rst-class
classref-enumeration-constant
:::
::::

`Hint<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
role="ref"} **HINT_RANGE_STEP** = `2`

The parameter\'s value must be within the specified range, with the
given
`step<class_VisualShaderNodeIntParameter_property_step>`{.interpreted-text
role="ref"} between values.

:::: {#class_VisualShaderNodeIntParameter_constant_HINT_ENUM}
::: rst-class
classref-enumeration-constant
:::
::::

`Hint<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
role="ref"} **HINT_ENUM** = `3`

The parameter uses an enum to associate preset values to names in the
editor.

:::: {#class_VisualShaderNodeIntParameter_constant_HINT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Hint<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
role="ref"} **HINT_MAX** = `4`

Represents the size of the
`Hint<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeIntParameter_property_default_value}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **default_value** = `0`
`🔗<class_VisualShaderNodeIntParameter_property_default_value>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_value**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_default_value**()

Default value of this parameter, which will be used if not set
externally.
`default_value_enabled<class_VisualShaderNodeIntParameter_property_default_value_enabled>`{.interpreted-text
role="ref"} must be enabled; defaults to `0` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeIntParameter_property_default_value_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**default_value_enabled** = `false`
`🔗<class_VisualShaderNodeIntParameter_property_default_value_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_value_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_default_value_enabled**()

If `true`, the node will have a custom default value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeIntParameter_property_enum_names}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **enum_names** = `PackedStringArray()`
`🔗<class_VisualShaderNodeIntParameter_property_enum_names>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enum_names**(value:
  `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"})
- `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} **get_enum_names**()

The names used for the enum select in the editor.
`hint<class_VisualShaderNodeIntParameter_property_hint>`{.interpreted-text
role="ref"} must be
`HINT_ENUM<class_VisualShaderNodeIntParameter_constant_HINT_ENUM>`{.interpreted-text
role="ref"} for this to take effect.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeIntParameter_property_hint}
::: rst-class
classref-property
:::
::::

`Hint<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
role="ref"} **hint** = `0`
`🔗<class_VisualShaderNodeIntParameter_property_hint>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hint**(value:
  `Hint<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
  role="ref"})
- `Hint<enum_VisualShaderNodeIntParameter_Hint>`{.interpreted-text
  role="ref"} **get_hint**()

Range hint of this node. Use it to customize valid parameter range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeIntParameter_property_max}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max** = `100`
`🔗<class_VisualShaderNodeIntParameter_property_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max**()

The maximum value this parameter can take.
`hint<class_VisualShaderNodeIntParameter_property_hint>`{.interpreted-text
role="ref"} must be either
`HINT_RANGE<class_VisualShaderNodeIntParameter_constant_HINT_RANGE>`{.interpreted-text
role="ref"} or
`HINT_RANGE_STEP<class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP>`{.interpreted-text
role="ref"} for this to take effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeIntParameter_property_min}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **min** = `0`
`🔗<class_VisualShaderNodeIntParameter_property_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_min**()

The minimum value this parameter can take.
`hint<class_VisualShaderNodeIntParameter_property_hint>`{.interpreted-text
role="ref"} must be either
`HINT_RANGE<class_VisualShaderNodeIntParameter_constant_HINT_RANGE>`{.interpreted-text
role="ref"} or
`HINT_RANGE_STEP<class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP>`{.interpreted-text
role="ref"} for this to take effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeIntParameter_property_step}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **step** = `1`
`🔗<class_VisualShaderNodeIntParameter_property_step>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_step**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_step**()

The step between parameter\'s values. Forces the parameter to be a
multiple of the given value.
`hint<class_VisualShaderNodeIntParameter_property_hint>`{.interpreted-text
role="ref"} must be
`HINT_RANGE_STEP<class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP>`{.interpreted-text
role="ref"} for this to take effect.
