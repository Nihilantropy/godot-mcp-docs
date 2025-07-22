github_url
:   hide

# InputEventKey {#class_InputEventKey}

**Inherits:**
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"} **\<**
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"} **\<** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a key on a keyboard being pressed or released.

::: rst-class
classref-introduction-group
:::

## Description

An input event for keys on a keyboard. Supports key presses, key
releases and `echo<class_InputEventKey_property_echo>`{.interpreted-text
role="ref"} events. It can also be received in
`Node._unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Events received from the keyboard usually have all
properties set. Event mappings should have only one of the
`keycode<class_InputEventKey_property_keycode>`{.interpreted-text
role="ref"},
`physical_keycode<class_InputEventKey_property_physical_keycode>`{.interpreted-text
role="ref"} or
`unicode<class_InputEventKey_property_unicode>`{.interpreted-text
role="ref"} set.

When events are compared, properties are checked in the following
priority -
`keycode<class_InputEventKey_property_keycode>`{.interpreted-text
role="ref"},
`physical_keycode<class_InputEventKey_property_physical_keycode>`{.interpreted-text
role="ref"} and
`unicode<class_InputEventKey_property_unicode>`{.interpreted-text
role="ref"}. Events with the first matching value will be considered
equal.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`{.interpreted-text
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

## Property Descriptions

:::: {#class_InputEventKey_property_echo}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **echo** = `false`
`🔗<class_InputEventKey_property_echo>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_echo**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_echo**()

If `true`, the key was already pressed before this event. An echo event
is a repeated key event sent when the user is holding down the key.

\*\*Note:\*\* The rate at which echo events are sent is typically around
20 events per second (after holding down the key for roughly half a
second). However, the key repeat delay/speed can be changed by the user
or disabled entirely in the operating system settings. To ensure your
project works correctly on all configurations, do not assume the user
has a specific key repeat configuration in your project\'s behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_property_key_label}
::: rst-class
classref-property
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **key_label**
= `0` `🔗<class_InputEventKey_property_key_label>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_key_label**(value:
  `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
- `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
  **get_key_label**()

Represents the localized label printed on the key in the current
keyboard layout, which corresponds to one of the
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} constants or
any valid Unicode character.

For keyboard layouts with a single label on the key, it is equivalent to
`keycode<class_InputEventKey_property_keycode>`{.interpreted-text
role="ref"}.

To get a human-readable representation of the **InputEventKey**, use
`OS.get_keycode_string(event.key_label)` where `event` is the
**InputEventKey**.

``` text
+-----+ +-----+
| Q   | | Q   | - "Q" - keycode
|   Й | |  ض | - "Й" and "ض" - key_label
+-----+ +-----+
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_property_keycode}
::: rst-class
classref-property
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **keycode** =
`0` `🔗<class_InputEventKey_property_keycode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keycode**(value: `Key<enum_@GlobalScope_Key>`{.interpreted-text
  role="ref"})
- `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
  **get_keycode**()

Latin label printed on the key in the current keyboard layout, which
corresponds to one of the `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} constants.

To get a human-readable representation of the **InputEventKey**, use
`OS.get_keycode_string(event.keycode)` where `event` is the
**InputEventKey**.

``` text
+-----+ +-----+
| Q   | | Q   | - "Q" - keycode
|   Й | |  ض | - "Й" and "ض" - key_label
+-----+ +-----+
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_property_location}
::: rst-class
classref-property
:::
::::

`KeyLocation<enum_@GlobalScope_KeyLocation>`{.interpreted-text
role="ref"} **location** = `0`
`🔗<class_InputEventKey_property_location>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_location**(value:
  `KeyLocation<enum_@GlobalScope_KeyLocation>`{.interpreted-text
  role="ref"})
- `KeyLocation<enum_@GlobalScope_KeyLocation>`{.interpreted-text
  role="ref"} **get_location**()

Represents the location of a key which has both left and right versions,
such as `Shift`{.interpreted-text role="kbd"} or `Alt`{.interpreted-text
role="kbd"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_property_physical_keycode}
::: rst-class
classref-property
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**physical_keycode** = `0`
`🔗<class_InputEventKey_property_physical_keycode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physical_keycode**(value:
  `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
- `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
  **get_physical_keycode**()

Represents the physical location of a key on the 101/102-key US QWERTY
keyboard, which corresponds to one of the
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} constants.

To get a human-readable representation of the **InputEventKey**, use
`OS.get_keycode_string()<class_OS_method_get_keycode_string>`{.interpreted-text
role="ref"} in combination with
`DisplayServer.keyboard_get_keycode_from_physical()<class_DisplayServer_method_keyboard_get_keycode_from_physical>`{.interpreted-text
role="ref"}:

::::: tabs
::: code-tab
gdscript

func [input]{#input}(event):

:   

    if event is InputEventKey:

    :   var keycode =
        DisplayServer.keyboard_get_keycode_from_physical(event.physical_keycode)
        print(OS.get_keycode_string(keycode))
:::

::: code-tab
csharp

public override void [Input]{#input}(InputEvent \@event) { if (@event is
InputEventKey inputEventKey) { var keycode =
DisplayServer.KeyboardGetKeycodeFromPhysical(inputEventKey.PhysicalKeycode);
GD.Print(OS.GetKeycodeString(keycode)); } }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_property_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **pressed** = `false`
`🔗<class_InputEventKey_property_pressed>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_pressed**()

If `true`, the key\'s state is pressed. If `false`, the key\'s state is
released.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_property_unicode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **unicode** = `0`
`🔗<class_InputEventKey_property_unicode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_unicode**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_unicode**()

The key Unicode character code (when relevant), shifted by modifier
keys. Unicode character codes for composite characters and complex
scripts may not be available unless IME input mode is active. See
`Window.set_ime_active()<class_Window_method_set_ime_active>`{.interpreted-text
role="ref"} for more information.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_InputEventKey_method_as_text_key_label}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**as_text_key_label**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEventKey_method_as_text_key_label>`{.interpreted-text
role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"}
representation of the event\'s
`key_label<class_InputEventKey_property_key_label>`{.interpreted-text
role="ref"} and modifiers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_method_as_text_keycode}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**as_text_keycode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEventKey_method_as_text_keycode>`{.interpreted-text
role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"}
representation of the event\'s
`keycode<class_InputEventKey_property_keycode>`{.interpreted-text
role="ref"} and modifiers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_method_as_text_location}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**as_text_location**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEventKey_method_as_text_location>`{.interpreted-text
role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"}
representation of the event\'s
`location<class_InputEventKey_property_location>`{.interpreted-text
role="ref"}. This will be a blank string if the event is not specific to
a location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_method_as_text_physical_keycode}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**as_text_physical_keycode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEventKey_method_as_text_physical_keycode>`{.interpreted-text
role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"}
representation of the event\'s
`physical_keycode<class_InputEventKey_property_physical_keycode>`{.interpreted-text
role="ref"} and modifiers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_method_get_key_label_with_modifiers}
::: rst-class
classref-method
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**get_key_label_with_modifiers**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEventKey_method_get_key_label_with_modifiers>`{.interpreted-text
role="ref"}

Returns the localized key label combined with modifier keys such as
`Shift`{.interpreted-text role="kbd"} or `Alt`{.interpreted-text
role="kbd"}. See also
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"}.

To get a human-readable representation of the **InputEventKey** with
modifiers, use
`OS.get_keycode_string(event.get_key_label_with_modifiers())` where
`event` is the **InputEventKey**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_method_get_keycode_with_modifiers}
::: rst-class
classref-method
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**get_keycode_with_modifiers**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEventKey_method_get_keycode_with_modifiers>`{.interpreted-text
role="ref"}

Returns the Latin keycode combined with modifier keys such as
`Shift`{.interpreted-text role="kbd"} or `Alt`{.interpreted-text
role="kbd"}. See also
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"}.

To get a human-readable representation of the **InputEventKey** with
modifiers, use
`OS.get_keycode_string(event.get_keycode_with_modifiers())` where
`event` is the **InputEventKey**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventKey_method_get_physical_keycode_with_modifiers}
::: rst-class
classref-method
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**get_physical_keycode_with_modifiers**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEventKey_method_get_physical_keycode_with_modifiers>`{.interpreted-text
role="ref"}

Returns the physical keycode combined with modifier keys such as
`Shift`{.interpreted-text role="kbd"} or `Alt`{.interpreted-text
role="kbd"}. See also
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"}.

To get a human-readable representation of the **InputEventKey** with
modifiers, use
`OS.get_keycode_string(event.get_physical_keycode_with_modifiers())`
where `event` is the **InputEventKey**.
