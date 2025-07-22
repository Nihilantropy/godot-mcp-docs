github_url
:   hide

# TextServerManager {#class_TextServerManager}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton for managing
`TextServer<class_TextServer>`{.interpreted-text role="ref"}
implementations.

::: rst-class
classref-introduction-group
:::

## Description

**TextServerManager** is the API backend for loading, enumerating, and
switching `TextServer<class_TextServer>`{.interpreted-text role="ref"}s.

\*\*Note:\*\* Switching text server at runtime is possible, but will
invalidate all fonts and text buffers. Make sure to unload all controls,
fonts, and themes before doing so.

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

:::: {#class_TextServerManager_signal_interface_added}
::: rst-class
classref-signal
:::
::::

**interface_added**(interface_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_TextServerManager_signal_interface_added>`{.interpreted-text
role="ref"}

Emitted when a new interface has been added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerManager_signal_interface_removed}
::: rst-class
classref-signal
:::
::::

**interface_removed**(interface_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_TextServerManager_signal_interface_removed>`{.interpreted-text
role="ref"}

Emitted when an interface is removed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TextServerManager_method_add_interface}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_interface**(interface:
`TextServer<class_TextServer>`{.interpreted-text role="ref"})
`🔗<class_TextServerManager_method_add_interface>`{.interpreted-text
role="ref"}

Registers a `TextServer<class_TextServer>`{.interpreted-text role="ref"}
interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerManager_method_find_interface}
::: rst-class
classref-method
:::
::::

`TextServer<class_TextServer>`{.interpreted-text role="ref"}
**find_interface**(name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerManager_method_find_interface>`{.interpreted-text
role="ref"}

Finds an interface by its `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerManager_method_get_interface}
::: rst-class
classref-method
:::
::::

`TextServer<class_TextServer>`{.interpreted-text role="ref"}
**get_interface**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerManager_method_get_interface>`{.interpreted-text
role="ref"}

Returns the interface registered at a given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerManager_method_get_interface_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_interface_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerManager_method_get_interface_count>`{.interpreted-text
role="ref"}

Returns the number of interfaces currently registered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerManager_method_get_interfaces}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_interfaces**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerManager_method_get_interfaces>`{.interpreted-text
role="ref"}

Returns a list of available interfaces, with the index and name of each
interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerManager_method_get_primary_interface}
::: rst-class
classref-method
:::
::::

`TextServer<class_TextServer>`{.interpreted-text role="ref"}
**get_primary_interface**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerManager_method_get_primary_interface>`{.interpreted-text
role="ref"}

Returns the primary `TextServer<class_TextServer>`{.interpreted-text
role="ref"} interface currently in use.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerManager_method_remove_interface}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_interface**(interface:
`TextServer<class_TextServer>`{.interpreted-text role="ref"})
`🔗<class_TextServerManager_method_remove_interface>`{.interpreted-text
role="ref"}

Removes an interface. All fonts and shaped text caches should be freed
before removing an interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerManager_method_set_primary_interface}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_primary_interface**(index:
`TextServer<class_TextServer>`{.interpreted-text role="ref"})
`🔗<class_TextServerManager_method_set_primary_interface>`{.interpreted-text
role="ref"}

Sets the primary `TextServer<class_TextServer>`{.interpreted-text
role="ref"} interface.
