github_url
:   hide

# CheckBox {#class_CheckBox}

**Inherits:** `Button<class_Button>`{.interpreted-text role="ref"}
**\<** `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A button that represents a binary choice.

::: rst-class
classref-introduction-group
:::

## Description

**CheckBox** allows the user to choose one of only two possible options.
It\'s similar to `CheckButton<class_CheckButton>`{.interpreted-text
role="ref"} in functionality, but it has a different appearance. To
follow established UX patterns, it\'s recommended to use **CheckBox**
when toggling it has **no** immediate effect on something. For example,
it could be used when toggling it will only do something once a
confirmation button is pressed.

See also `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
which contains common properties and methods associated with this node.

When
`BaseButton.button_group<class_BaseButton_property_button_group>`{.interpreted-text
role="ref"} specifies a
`ButtonGroup<class_ButtonGroup>`{.interpreted-text role="ref"},
**CheckBox** changes its appearance to that of a radio button and uses
the various `radio_*` theme properties.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Theme Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_CheckBox_theme_color_checkbox_checked_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**checkbox_checked_color** = `Color(1, 1, 1, 1)`
`🔗<class_CheckBox_theme_color_checkbox_checked_color>`{.interpreted-text
role="ref"}

The color of the checked icon when the checkbox is pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_color_checkbox_unchecked_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**checkbox_unchecked_color** = `Color(1, 1, 1, 1)`
`🔗<class_CheckBox_theme_color_checkbox_unchecked_color>`{.interpreted-text
role="ref"}

The color of the unchecked icon when the checkbox is not pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_constant_check_v_offset}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **check_v_offset** = `0`
`🔗<class_CheckBox_theme_constant_check_v_offset>`{.interpreted-text
role="ref"}

The vertical offset used when rendering the check icons (in pixels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_icon_checked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **checked**
`🔗<class_CheckBox_theme_icon_checked>`{.interpreted-text role="ref"}

The check icon to display when the **CheckBox** is checked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_icon_checked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**checked_disabled**
`🔗<class_CheckBox_theme_icon_checked_disabled>`{.interpreted-text
role="ref"}

The check icon to display when the **CheckBox** is checked and is
disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_icon_radio_checked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radio_checked**
`🔗<class_CheckBox_theme_icon_radio_checked>`{.interpreted-text
role="ref"}

The check icon to display when the **CheckBox** is configured as a radio
button and is checked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_icon_radio_checked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radio_checked_disabled**
`🔗<class_CheckBox_theme_icon_radio_checked_disabled>`{.interpreted-text
role="ref"}

The check icon to display when the **CheckBox** is configured as a radio
button, is disabled, and is unchecked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_icon_radio_unchecked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radio_unchecked**
`🔗<class_CheckBox_theme_icon_radio_unchecked>`{.interpreted-text
role="ref"}

The check icon to display when the **CheckBox** is configured as a radio
button and is unchecked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_icon_radio_unchecked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radio_unchecked_disabled**
`🔗<class_CheckBox_theme_icon_radio_unchecked_disabled>`{.interpreted-text
role="ref"}

The check icon to display when the **CheckBox** is configured as a radio
button, is disabled, and is unchecked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_icon_unchecked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **unchecked**
`🔗<class_CheckBox_theme_icon_unchecked>`{.interpreted-text role="ref"}

The check icon to display when the **CheckBox** is unchecked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckBox_theme_icon_unchecked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**unchecked_disabled**
`🔗<class_CheckBox_theme_icon_unchecked_disabled>`{.interpreted-text
role="ref"}

The check icon to display when the **CheckBox** is unchecked and is
disabled.
