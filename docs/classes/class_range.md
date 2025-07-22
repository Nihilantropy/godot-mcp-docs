github_url
:   hide

# Range {#class_Range}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`EditorSpinSlider<class_EditorSpinSlider>`{.interpreted-text
role="ref"}, `ProgressBar<class_ProgressBar>`{.interpreted-text
role="ref"}, `ScrollBar<class_ScrollBar>`{.interpreted-text role="ref"},
`Slider<class_Slider>`{.interpreted-text role="ref"},
`SpinBox<class_SpinBox>`{.interpreted-text role="ref"},
`TextureProgressBar<class_TextureProgressBar>`{.interpreted-text
role="ref"}

Abstract base class for controls that represent a number within a range.

::: rst-class
classref-introduction-group
:::

## Description

Range is an abstract base class for controls that represent a number
within a range, using a configured
`step<class_Range_property_step>`{.interpreted-text role="ref"} and
`page<class_Range_property_page>`{.interpreted-text role="ref"} size.
See e.g. `ScrollBar<class_ScrollBar>`{.interpreted-text role="ref"} and
`Slider<class_Slider>`{.interpreted-text role="ref"} for examples of
higher-level nodes using Range.

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

## Signals

:::: {#class_Range_signal_changed}
::: rst-class
classref-signal
:::
::::

**changed**() `🔗<class_Range_signal_changed>`{.interpreted-text
role="ref"}

Emitted when
`min_value<class_Range_property_min_value>`{.interpreted-text
role="ref"},
`max_value<class_Range_property_max_value>`{.interpreted-text
role="ref"}, `page<class_Range_property_page>`{.interpreted-text
role="ref"}, or `step<class_Range_property_step>`{.interpreted-text
role="ref"} change.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_signal_value_changed}
::: rst-class
classref-signal
:::
::::

**value_changed**(value: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Range_signal_value_changed>`{.interpreted-text
role="ref"}

Emitted when `value<class_Range_property_value>`{.interpreted-text
role="ref"} changes. When used on a
`Slider<class_Slider>`{.interpreted-text role="ref"}, this is called
continuously while dragging (potentially every frame). If you are
performing an expensive operation in a function connected to
`value_changed<class_Range_signal_value_changed>`{.interpreted-text
role="ref"}, consider using a *debouncing*
`Timer<class_Timer>`{.interpreted-text role="ref"} to call the function
less often.

\*\*Note:\*\* Unlike signals such as
`LineEdit.text_changed<class_LineEdit_signal_text_changed>`{.interpreted-text
role="ref"},
`value_changed<class_Range_signal_value_changed>`{.interpreted-text
role="ref"} is also emitted when `value` is set directly via code.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Range_property_allow_greater}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_greater** =
`false` `🔗<class_Range_property_allow_greater>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_greater**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_greater_allowed**()

If `true`, `value<class_Range_property_value>`{.interpreted-text
role="ref"} may be greater than
`max_value<class_Range_property_max_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_property_allow_lesser}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_lesser** =
`false` `🔗<class_Range_property_allow_lesser>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_lesser**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_lesser_allowed**()

If `true`, `value<class_Range_property_value>`{.interpreted-text
role="ref"} may be less than
`min_value<class_Range_property_min_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_property_exp_edit}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **exp_edit** = `false`
`🔗<class_Range_property_exp_edit>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exp_ratio**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_ratio_exp**()

If `true`, and
`min_value<class_Range_property_min_value>`{.interpreted-text
role="ref"} is greater or equal to `0`,
`value<class_Range_property_value>`{.interpreted-text role="ref"} will
be represented exponentially rather than linearly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_property_max_value}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_value** =
`100.0` `🔗<class_Range_property_max_value>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_max**()

Maximum value. Range is clamped if
`value<class_Range_property_value>`{.interpreted-text role="ref"} is
greater than
`max_value<class_Range_property_max_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_property_min_value}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **min_value** = `0.0`
`🔗<class_Range_property_min_value>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_min**()

Minimum value. Range is clamped if
`value<class_Range_property_value>`{.interpreted-text role="ref"} is
less than `min_value<class_Range_property_min_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_property_page}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **page** = `0.0`
`🔗<class_Range_property_page>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_page**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_page**()

Page size. Used mainly for
`ScrollBar<class_ScrollBar>`{.interpreted-text role="ref"}. A
`ScrollBar<class_ScrollBar>`{.interpreted-text role="ref"}\'s grabber
length is the `ScrollBar<class_ScrollBar>`{.interpreted-text
role="ref"}\'s size multiplied by
`page<class_Range_property_page>`{.interpreted-text role="ref"} over the
difference between
`min_value<class_Range_property_min_value>`{.interpreted-text
role="ref"} and
`max_value<class_Range_property_max_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_property_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ratio**
`🔗<class_Range_property_ratio>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_as_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_as_ratio**()

The value mapped between 0 and 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_property_rounded}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **rounded** = `false`
`🔗<class_Range_property_rounded>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_rounded_values**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_rounded_values**()

If `true`, `value<class_Range_property_value>`{.interpreted-text
role="ref"} will always be rounded to the nearest integer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_property_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **step** = `0.01`
`🔗<class_Range_property_step>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_step**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_step**()

If greater than 0, `value<class_Range_property_value>`{.interpreted-text
role="ref"} will always be rounded to a multiple of this property\'s
value. If `rounded<class_Range_property_rounded>`{.interpreted-text
role="ref"} is also `true`,
`value<class_Range_property_value>`{.interpreted-text role="ref"} will
first be rounded to a multiple of this property\'s value, then rounded
to the nearest integer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_property_value}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **value** = `0.0`
`🔗<class_Range_property_value>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_value**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_value**()

Range\'s current value. Changing this property (even via code) will
trigger
`value_changed<class_Range_signal_value_changed>`{.interpreted-text
role="ref"} signal. Use
`set_value_no_signal()<class_Range_method_set_value_no_signal>`{.interpreted-text
role="ref"} if you want to avoid it.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Range_private_method__value_changed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_value_changed**(new_value: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Range_private_method__value_changed>`{.interpreted-text
role="ref"}

Called when the **Range**\'s value is changed (following the same
conditions as
`value_changed<class_Range_signal_value_changed>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_method_set_value_no_signal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_value_no_signal**(value: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_Range_method_set_value_no_signal>`{.interpreted-text
role="ref"}

Sets the **Range**\'s current value to the specified `value`, without
emitting the
`value_changed<class_Range_signal_value_changed>`{.interpreted-text
role="ref"} signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_method_share}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **share**(with:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_Range_method_share>`{.interpreted-text role="ref"}

Binds two **Range**s together along with any ranges previously grouped
with either of them. When any of range\'s member variables change, it
will share the new value with all other ranges in its group.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Range_method_unshare}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **unshare**()
`🔗<class_Range_method_unshare>`{.interpreted-text role="ref"}

Stops the **Range** from sharing its member variables with any other.
