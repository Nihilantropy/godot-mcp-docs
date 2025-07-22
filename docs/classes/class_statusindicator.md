github_url
:   hide

::: {.meta keywords="tray"}
:::

# StatusIndicator {#class_StatusIndicator}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Application status indicator (aka notification area icon).

\*\*Note:\*\* Status indicator is implemented on macOS and Windows.

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

:::: {#class_StatusIndicator_signal_pressed}
::: rst-class
classref-signal
:::
::::

**pressed**(mouse_button: `int<class_int>`{.interpreted-text
role="ref"}, mouse_position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_StatusIndicator_signal_pressed>`{.interpreted-text role="ref"}

Emitted when the status indicator is pressed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_StatusIndicator_property_icon}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **icon**
`🔗<class_StatusIndicator_property_icon>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_icon**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_icon**()

Status indicator icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StatusIndicator_property_menu}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **menu** =
`NodePath("")`
`🔗<class_StatusIndicator_property_menu>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_menu**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_menu**()

Status indicator native popup menu. If this is set, the
`pressed<class_StatusIndicator_signal_pressed>`{.interpreted-text
role="ref"} signal is not emitted.

\*\*Note:\*\* Native popup is only supported if
`NativeMenu<class_NativeMenu>`{.interpreted-text role="ref"} supports
`NativeMenu.FEATURE_POPUP_MENU<class_NativeMenu_constant_FEATURE_POPUP_MENU>`{.interpreted-text
role="ref"} feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StatusIndicator_property_tooltip}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **tooltip** = `""`
`🔗<class_StatusIndicator_property_tooltip>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tooltip**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_tooltip**()

Status indicator tooltip.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StatusIndicator_property_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **visible** = `true`
`🔗<class_StatusIndicator_property_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_visible**()

If `true`, the status indicator is visible.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_StatusIndicator_method_get_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StatusIndicator_method_get_rect>`{.interpreted-text
role="ref"}

Returns the status indicator rectangle in screen coordinates. If this
status indicator is not visible, returns an empty
`Rect2<class_Rect2>`{.interpreted-text role="ref"}.
