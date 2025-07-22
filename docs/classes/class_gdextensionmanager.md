github_url
:   hide

# GDExtensionManager {#class_GDExtensionManager}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Provides access to GDExtension functionality.

::: rst-class
classref-introduction-group
:::

## Description

The GDExtensionManager loads, initializes, and keeps track of all
available `GDExtension<class_GDExtension>`{.interpreted-text role="ref"}
libraries in the project.

\*\*Note:\*\* Do not worry about GDExtension unless you know what you
are doing.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `GDExtension overview <../tutorials/scripting/gdextension/what_is_gdextension>`{.interpreted-text
  role="doc"}
- `GDExtension example in C++ <../tutorials/scripting/cpp/gdextension_cpp_example>`{.interpreted-text
  role="doc"}

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

:::: {#class_GDExtensionManager_signal_extension_loaded}
::: rst-class
classref-signal
:::
::::

**extension_loaded**(extension:
`GDExtension<class_GDExtension>`{.interpreted-text role="ref"})
`🔗<class_GDExtensionManager_signal_extension_loaded>`{.interpreted-text
role="ref"}

Emitted after the editor has finished loading a new extension.

\*\*Note:\*\* This signal is only emitted in editor builds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GDExtensionManager_signal_extension_unloading}
::: rst-class
classref-signal
:::
::::

**extension_unloading**(extension:
`GDExtension<class_GDExtension>`{.interpreted-text role="ref"})
`🔗<class_GDExtensionManager_signal_extension_unloading>`{.interpreted-text
role="ref"}

Emitted before the editor starts unloading an extension.

\*\*Note:\*\* This signal is only emitted in editor builds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GDExtensionManager_signal_extensions_reloaded}
::: rst-class
classref-signal
:::
::::

**extensions_reloaded**()
`🔗<class_GDExtensionManager_signal_extensions_reloaded>`{.interpreted-text
role="ref"}

Emitted after the editor has finished reloading one or more extensions.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_GDExtensionManager_LoadStatus}
::: rst-class
classref-enumeration
:::
::::

enum **LoadStatus**:
`🔗<enum_GDExtensionManager_LoadStatus>`{.interpreted-text role="ref"}

:::: {#class_GDExtensionManager_constant_LOAD_STATUS_OK}
::: rst-class
classref-enumeration-constant
:::
::::

`LoadStatus<enum_GDExtensionManager_LoadStatus>`{.interpreted-text
role="ref"} **LOAD_STATUS_OK** = `0`

The extension has loaded successfully.

:::: {#class_GDExtensionManager_constant_LOAD_STATUS_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`LoadStatus<enum_GDExtensionManager_LoadStatus>`{.interpreted-text
role="ref"} **LOAD_STATUS_FAILED** = `1`

The extension has failed to load, possibly because it does not exist or
has missing dependencies.

:::: {#class_GDExtensionManager_constant_LOAD_STATUS_ALREADY_LOADED}
::: rst-class
classref-enumeration-constant
:::
::::

`LoadStatus<enum_GDExtensionManager_LoadStatus>`{.interpreted-text
role="ref"} **LOAD_STATUS_ALREADY_LOADED** = `2`

The extension has already been loaded.

:::: {#class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED}
::: rst-class
classref-enumeration-constant
:::
::::

`LoadStatus<enum_GDExtensionManager_LoadStatus>`{.interpreted-text
role="ref"} **LOAD_STATUS_NOT_LOADED** = `3`

The extension has not been loaded.

:::: {#class_GDExtensionManager_constant_LOAD_STATUS_NEEDS_RESTART}
::: rst-class
classref-enumeration-constant
:::
::::

`LoadStatus<enum_GDExtensionManager_LoadStatus>`{.interpreted-text
role="ref"} **LOAD_STATUS_NEEDS_RESTART** = `4`

The extension requires the application to restart to fully load.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GDExtensionManager_method_get_extension}
::: rst-class
classref-method
:::
::::

`GDExtension<class_GDExtension>`{.interpreted-text role="ref"}
**get_extension**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_GDExtensionManager_method_get_extension>`{.interpreted-text
role="ref"}

Returns the `GDExtension<class_GDExtension>`{.interpreted-text
role="ref"} at the given file `path`, or `null` if it has not been
loaded or does not exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GDExtensionManager_method_get_loaded_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_loaded_extensions**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GDExtensionManager_method_get_loaded_extensions>`{.interpreted-text
role="ref"}

Returns the file paths of all currently loaded extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GDExtensionManager_method_is_extension_loaded}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_extension_loaded**(path: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GDExtensionManager_method_is_extension_loaded>`{.interpreted-text
role="ref"}

Returns `true` if the extension at the given file `path` has already
been loaded successfully. See also
`get_loaded_extensions()<class_GDExtensionManager_method_get_loaded_extensions>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GDExtensionManager_method_load_extension}
::: rst-class
classref-method
:::
::::

`LoadStatus<enum_GDExtensionManager_LoadStatus>`{.interpreted-text
role="ref"} **load_extension**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_GDExtensionManager_method_load_extension>`{.interpreted-text
role="ref"}

Loads an extension by absolute file path. The `path` needs to point to a
valid `GDExtension<class_GDExtension>`{.interpreted-text role="ref"}.
Returns
`LOAD_STATUS_OK<class_GDExtensionManager_constant_LOAD_STATUS_OK>`{.interpreted-text
role="ref"} if successful.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GDExtensionManager_method_reload_extension}
::: rst-class
classref-method
:::
::::

`LoadStatus<enum_GDExtensionManager_LoadStatus>`{.interpreted-text
role="ref"} **reload_extension**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_GDExtensionManager_method_reload_extension>`{.interpreted-text
role="ref"}

Reloads the extension at the given file path. The `path` needs to point
to a valid `GDExtension<class_GDExtension>`{.interpreted-text
role="ref"}, otherwise this method may return either
`LOAD_STATUS_NOT_LOADED<class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED>`{.interpreted-text
role="ref"} or
`LOAD_STATUS_FAILED<class_GDExtensionManager_constant_LOAD_STATUS_FAILED>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* You can only reload extensions in the editor. In release
builds, this method always fails and returns
`LOAD_STATUS_FAILED<class_GDExtensionManager_constant_LOAD_STATUS_FAILED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GDExtensionManager_method_unload_extension}
::: rst-class
classref-method
:::
::::

`LoadStatus<enum_GDExtensionManager_LoadStatus>`{.interpreted-text
role="ref"} **unload_extension**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_GDExtensionManager_method_unload_extension>`{.interpreted-text
role="ref"}

Unloads an extension by file path. The `path` needs to point to an
already loaded `GDExtension<class_GDExtension>`{.interpreted-text
role="ref"}, otherwise this method returns
`LOAD_STATUS_NOT_LOADED<class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED>`{.interpreted-text
role="ref"}.
