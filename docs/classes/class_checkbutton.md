github_url
:   hide

# CheckButton {#class_CheckButton}

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

**CheckButton** is a toggle button displayed as a check field. It\'s
similar to `CheckBox<class_CheckBox>`{.interpreted-text role="ref"} in
functionality, but it has a different appearance. To follow established
UX patterns, it\'s recommended to use **CheckButton** when toggling it
has an **immediate** effect on something. For example, it can be used
when pressing it shows or hides advanced settings, without asking the
user to confirm this action.

See also `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
which contains common properties and methods associated with this node.

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

:::: {#class_CheckButton_theme_color_button_checked_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**button_checked_color** = `Color(1, 1, 1, 1)`
`🔗<class_CheckButton_theme_color_button_checked_color>`{.interpreted-text
role="ref"}

The color of the checked icon when the checkbox is pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_color_button_unchecked_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**button_unchecked_color** = `Color(1, 1, 1, 1)`
`🔗<class_CheckButton_theme_color_button_unchecked_color>`{.interpreted-text
role="ref"}

The color of the unchecked icon when the checkbox is not pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_constant_check_v_offset}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **check_v_offset** = `0`
`🔗<class_CheckButton_theme_constant_check_v_offset>`{.interpreted-text
role="ref"}

The vertical offset used when rendering the toggle icons (in pixels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_icon_checked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **checked**
`🔗<class_CheckButton_theme_icon_checked>`{.interpreted-text role="ref"}

The icon to display when the **CheckButton** is checked (for
left-to-right layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_icon_checked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**checked_disabled**
`🔗<class_CheckButton_theme_icon_checked_disabled>`{.interpreted-text
role="ref"}

The icon to display when the **CheckButton** is checked and disabled
(for left-to-right layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_icon_checked_disabled_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**checked_disabled_mirrored**
`🔗<class_CheckButton_theme_icon_checked_disabled_mirrored>`{.interpreted-text
role="ref"}

The icon to display when the **CheckButton** is checked and disabled
(for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_icon_checked_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**checked_mirrored**
`🔗<class_CheckButton_theme_icon_checked_mirrored>`{.interpreted-text
role="ref"}

The icon to display when the **CheckButton** is checked (for
right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_icon_unchecked}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **unchecked**
`🔗<class_CheckButton_theme_icon_unchecked>`{.interpreted-text
role="ref"}

The icon to display when the **CheckButton** is unchecked (for
left-to-right layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_icon_unchecked_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**unchecked_disabled**
`🔗<class_CheckButton_theme_icon_unchecked_disabled>`{.interpreted-text
role="ref"}

The icon to display when the **CheckButton** is unchecked and disabled
(for left-to-right layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_icon_unchecked_disabled_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**unchecked_disabled_mirrored**
`🔗<class_CheckButton_theme_icon_unchecked_disabled_mirrored>`{.interpreted-text
role="ref"}

The icon to display when the **CheckButton** is unchecked and disabled
(for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CheckButton_theme_icon_unchecked_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**unchecked_mirrored**
`🔗<class_CheckButton_theme_icon_unchecked_mirrored>`{.interpreted-text
role="ref"}

The icon to display when the **CheckButton** is unchecked (for
right-to-left layouts).
