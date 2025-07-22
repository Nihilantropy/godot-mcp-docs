github_url
:   hide

# TouchScreenButton {#class_TouchScreenButton}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Button for touch screen devices for gameplay use.

::: rst-class
classref-introduction-group
:::

## Description

TouchScreenButton allows you to create on-screen buttons for touch
devices. It\'s intended for gameplay use, such as a unit you have to
touch to move. Unlike `Button<class_Button>`{.interpreted-text
role="ref"}, TouchScreenButton supports multitouch out of the box.
Several TouchScreenButtons can be pressed at the same time with touch
input.

This node inherits from `Node2D<class_Node2D>`{.interpreted-text
role="ref"}. Unlike with `Control<class_Control>`{.interpreted-text
role="ref"} nodes, you cannot set anchors on it. If you want to create
menus or user interfaces, you may want to use
`Button<class_Button>`{.interpreted-text role="ref"} nodes instead. To
make button nodes react to touch events, you can enable
`ProjectSettings.input_devices/pointing/emulate_mouse_from_touch<class_ProjectSettings_property_input_devices/pointing/emulate_mouse_from_touch>`{.interpreted-text
role="ref"} in the Project Settings.

You can configure TouchScreenButton to be visible only on touch devices,
helping you develop your game both for desktop and mobile devices.

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

:::: {#class_TouchScreenButton_signal_pressed}
::: rst-class
classref-signal
:::
::::

**pressed**()
`🔗<class_TouchScreenButton_signal_pressed>`{.interpreted-text
role="ref"}

Emitted when the button is pressed (down).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TouchScreenButton_signal_released}
::: rst-class
classref-signal
:::
::::

**released**()
`🔗<class_TouchScreenButton_signal_released>`{.interpreted-text
role="ref"}

Emitted when the button is released (up).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_TouchScreenButton_VisibilityMode}
::: rst-class
classref-enumeration
:::
::::

enum **VisibilityMode**:
`🔗<enum_TouchScreenButton_VisibilityMode>`{.interpreted-text
role="ref"}

:::: {#class_TouchScreenButton_constant_VISIBILITY_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityMode<enum_TouchScreenButton_VisibilityMode>`{.interpreted-text
role="ref"} **VISIBILITY_ALWAYS** = `0`

Always visible.

:::: {#class_TouchScreenButton_constant_VISIBILITY_TOUCHSCREEN_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibilityMode<enum_TouchScreenButton_VisibilityMode>`{.interpreted-text
role="ref"} **VISIBILITY_TOUCHSCREEN_ONLY** = `1`

Visible on touch screens only.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TouchScreenButton_property_action}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **action** = `""`
`🔗<class_TouchScreenButton_property_action>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_action**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_action**()

The button\'s action. Actions can be handled with
`InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TouchScreenButton_property_bitmask}
::: rst-class
classref-property
:::
::::

`BitMap<class_BitMap>`{.interpreted-text role="ref"} **bitmask**
`🔗<class_TouchScreenButton_property_bitmask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bitmask**(value: `BitMap<class_BitMap>`{.interpreted-text
  role="ref"})
- `BitMap<class_BitMap>`{.interpreted-text role="ref"} **get_bitmask**()

The button\'s bitmask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TouchScreenButton_property_passby_press}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **passby_press** =
`false`
`🔗<class_TouchScreenButton_property_passby_press>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_passby_press**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_passby_press_enabled**()

If `true`, the
`pressed<class_TouchScreenButton_signal_pressed>`{.interpreted-text
role="ref"} and
`released<class_TouchScreenButton_signal_released>`{.interpreted-text
role="ref"} signals are emitted whenever a pressed finger goes in and
out of the button, even if the pressure started outside the active area
of the button.

\*\*Note:\*\* This is a \"pass-by\" (not \"bypass\") press mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TouchScreenButton_property_shape}
::: rst-class
classref-property
:::
::::

`Shape2D<class_Shape2D>`{.interpreted-text role="ref"} **shape**
`🔗<class_TouchScreenButton_property_shape>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape**(value: `Shape2D<class_Shape2D>`{.interpreted-text
  role="ref"})
- `Shape2D<class_Shape2D>`{.interpreted-text role="ref"} **get_shape**()

The button\'s shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TouchScreenButton_property_shape_centered}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shape_centered** =
`true`
`🔗<class_TouchScreenButton_property_shape_centered>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape_centered**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_shape_centered**()

If `true`, the button\'s shape is centered in the provided texture. If
no texture is used, this property has no effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TouchScreenButton_property_shape_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shape_visible** =
`true`
`🔗<class_TouchScreenButton_property_shape_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_shape_visible**()

If `true`, the button\'s shape is visible in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TouchScreenButton_property_texture_normal}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_normal**
`🔗<class_TouchScreenButton_property_texture_normal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_normal**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture_normal**()

The button\'s texture for the normal state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TouchScreenButton_property_texture_pressed}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_pressed**
`🔗<class_TouchScreenButton_property_texture_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_pressed**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture_pressed**()

The button\'s texture for the pressed state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TouchScreenButton_property_visibility_mode}
::: rst-class
classref-property
:::
::::

`VisibilityMode<enum_TouchScreenButton_VisibilityMode>`{.interpreted-text
role="ref"} **visibility_mode** = `0`
`🔗<class_TouchScreenButton_property_visibility_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visibility_mode**(value:
  `VisibilityMode<enum_TouchScreenButton_VisibilityMode>`{.interpreted-text
  role="ref"})
- `VisibilityMode<enum_TouchScreenButton_VisibilityMode>`{.interpreted-text
  role="ref"} **get_visibility_mode**()

The button\'s visibility mode.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TouchScreenButton_method_is_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_pressed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TouchScreenButton_method_is_pressed>`{.interpreted-text
role="ref"}

Returns `true` if this button is currently pressed.
