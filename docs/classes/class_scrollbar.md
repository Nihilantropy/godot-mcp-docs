github_url
:   hide

# ScrollBar {#class_ScrollBar}

**Inherits:** `Range<class_Range>`{.interpreted-text role="ref"} **\<**
`Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `HScrollBar<class_HScrollBar>`{.interpreted-text
role="ref"}, `VScrollBar<class_VScrollBar>`{.interpreted-text
role="ref"}

Abstract base class for scrollbars.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for scrollbars, typically used to navigate through
content that extends beyond the visible area of a control. Scrollbars
are `Range<class_Range>`{.interpreted-text role="ref"}-based controls.

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

## Signals

:::: {#class_ScrollBar_signal_scrolling}
::: rst-class
classref-signal
:::
::::

**scrolling**() `🔗<class_ScrollBar_signal_scrolling>`{.interpreted-text
role="ref"}

Emitted when the scrollbar is being scrolled.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ScrollBar_property_custom_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **custom_step** =
`-1.0` `🔗<class_ScrollBar_property_custom_step>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_step**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_custom_step**()

Overrides the step used when clicking increment and decrement buttons or
when using arrow keys when the **ScrollBar** is focused.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_ScrollBar_theme_icon_decrement}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **decrement**
`🔗<class_ScrollBar_theme_icon_decrement>`{.interpreted-text role="ref"}

Icon used as a button to scroll the **ScrollBar** left/up. Supports
custom step using the
`custom_step<class_ScrollBar_property_custom_step>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_icon_decrement_highlight}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**decrement_highlight**
`🔗<class_ScrollBar_theme_icon_decrement_highlight>`{.interpreted-text
role="ref"}

Displayed when the mouse cursor hovers over the decrement button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_icon_decrement_pressed}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**decrement_pressed**
`🔗<class_ScrollBar_theme_icon_decrement_pressed>`{.interpreted-text
role="ref"}

Displayed when the decrement button is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_icon_increment}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **increment**
`🔗<class_ScrollBar_theme_icon_increment>`{.interpreted-text role="ref"}

Icon used as a button to scroll the **ScrollBar** right/down. Supports
custom step using the
`custom_step<class_ScrollBar_property_custom_step>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_icon_increment_highlight}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**increment_highlight**
`🔗<class_ScrollBar_theme_icon_increment_highlight>`{.interpreted-text
role="ref"}

Displayed when the mouse cursor hovers over the increment button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_icon_increment_pressed}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**increment_pressed**
`🔗<class_ScrollBar_theme_icon_increment_pressed>`{.interpreted-text
role="ref"}

Displayed when the increment button is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_style_grabber}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **grabber**
`🔗<class_ScrollBar_theme_style_grabber>`{.interpreted-text role="ref"}

Used as texture for the grabber, the draggable element representing
current scroll.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_style_grabber_highlight}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**grabber_highlight**
`🔗<class_ScrollBar_theme_style_grabber_highlight>`{.interpreted-text
role="ref"}

Used when the mouse hovers over the grabber.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_style_grabber_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**grabber_pressed**
`🔗<class_ScrollBar_theme_style_grabber_pressed>`{.interpreted-text
role="ref"}

Used when the grabber is being dragged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_style_scroll}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **scroll**
`🔗<class_ScrollBar_theme_style_scroll>`{.interpreted-text role="ref"}

Used as background of this **ScrollBar**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollBar_theme_style_scroll_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**scroll_focus**
`🔗<class_ScrollBar_theme_style_scroll_focus>`{.interpreted-text
role="ref"}

Used as background when the **ScrollBar** has the GUI focus.
