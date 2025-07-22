github_url
:   hide

# EditorExportPlatformExtension {#class_EditorExportPlatformExtension}

**Inherits:**
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Base class for custom
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} implementations (plugins).

::: rst-class
classref-introduction-group
:::

## Description

External
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} implementations should inherit from this class.

To use
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, register it using the
`EditorPlugin.add_export_platform()<class_EditorPlugin_method_add_export_platform>`{.interpreted-text
role="ref"} method first.

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

## Method Descriptions

:::: {#class_EditorExportPlatformExtension_private_method__can_export}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_can_export**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__can_export>`{.interpreted-text
role="ref"}

Returns `true`, if specified `preset` is valid and can be exported. Use
`set_config_error()<class_EditorExportPlatformExtension_method_set_config_error>`{.interpreted-text
role="ref"} and
`set_config_missing_templates()<class_EditorExportPlatformExtension_method_set_config_missing_templates>`{.interpreted-text
role="ref"} to set error details.

Usual implementation can call
`_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`{.interpreted-text
role="ref"} and
`_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>`{.interpreted-text
role="ref"} to determine if export is possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__cleanup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_cleanup**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__cleanup>`{.interpreted-text
role="ref"}

Called by the editor before platform is unregistered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__export_pack}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_pack**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__export_pack>`{.interpreted-text
role="ref"}

Creates a PCK archive at `path` for the specified `preset`.

This method is called when \"Export PCK/ZIP\" button is pressed in the
export dialog, with \"Export as Patch\" disabled, and PCK is selected as
a file type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__export_pack_patch}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_pack_patch**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, patches:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__export_pack_patch>`{.interpreted-text
role="ref"}

Creates a patch PCK archive at `path` for the specified `preset`,
containing only the files that have changed since the last patch.

This method is called when \"Export PCK/ZIP\" button is pressed in the
export dialog, with \"Export as Patch\" enabled, and PCK is selected as
a file type.

\*\*Note:\*\* The patches provided in `patches` have already been loaded
when this method is called and are merely provided as context. When
empty the patches defined in the export preset have been loaded instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__export_project}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_project**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__export_project>`{.interpreted-text
role="ref"}

Creates a full project at `path` for the specified `preset`.

This method is called when \"Export\" button is pressed in the export
dialog.

This method implementation can call
`EditorExportPlatform.save_pack()<class_EditorExportPlatform_method_save_pack>`{.interpreted-text
role="ref"} or
`EditorExportPlatform.save_zip()<class_EditorExportPlatform_method_save_zip>`{.interpreted-text
role="ref"} to use default PCK/ZIP export process, or calls
`EditorExportPlatform.export_project_files()<class_EditorExportPlatform_method_export_project_files>`{.interpreted-text
role="ref"} and implement custom callback for processing each exported
file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__export_zip}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_zip**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__export_zip>`{.interpreted-text
role="ref"}

Create a ZIP archive at `path` for the specified `preset`.

This method is called when \"Export PCK/ZIP\" button is pressed in the
export dialog, with \"Export as Patch\" disabled, and ZIP is selected as
a file type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__export_zip_patch}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_zip_patch**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, patches:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__export_zip_patch>`{.interpreted-text
role="ref"}

Create a ZIP archive at `path` for the specified `preset`, containing
only the files that have changed since the last patch.

This method is called when \"Export PCK/ZIP\" button is pressed in the
export dialog, with \"Export as Patch\" enabled, and ZIP is selected as
a file type.

\*\*Note:\*\* The patches provided in `patches` have already been loaded
when this method is called and are merely provided as context. When
empty the patches defined in the export preset have been loaded instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_binary_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_binary_extensions**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_binary_extensions>`{.interpreted-text
role="ref"}

Returns array of supported binary extensions for the full project
export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_debug_protocol}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_debug_protocol**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_debug_protocol>`{.interpreted-text
role="ref"}

Returns protocol used for remote debugging. Default implementation
return `tcp://`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_device_architecture}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_device_architecture**(device: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_device_architecture>`{.interpreted-text
role="ref"}

Returns device architecture for one-click deploy.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_export_option_visibility}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_get_export_option_visibility**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, option: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_export_option_visibility>`{.interpreted-text
role="ref"}

Validates `option` and returns visibility for the specified `preset`.
Default implementation return `true` for all options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_export_option_warning}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_export_option_warning**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, option: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_export_option_warning>`{.interpreted-text
role="ref"}

Validates `option` and returns warning message for the specified
`preset`. Default implementation return empty string for all options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_export_options}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_get_export_options**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_export_options>`{.interpreted-text
role="ref"}

Returns a property list, as an `Array<class_Array>`{.interpreted-text
role="ref"} of dictionaries. Each
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} must at
least contain the `name: StringName` and `type: Variant.Type` entries.

Additionally, the following keys are supported:

- `hint: PropertyHint`
- `hint_string: String`
- `usage: PropertyUsageFlags`
- `class_name: StringName`
- `default_value: Variant`, default value of the property.
- `update_visibility: bool`, if set to `true`,
  `_get_export_option_visibility()<class_EditorExportPlatformExtension_private_method__get_export_option_visibility>`{.interpreted-text
  role="ref"} is called for each property when this property is changed.
- `required: bool`, if set to `true`, this property warnings are
  critical, and should be resolved to make export possible. This value
  is a hint for the
  `_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`{.interpreted-text
  role="ref"} implementation, and not used by the engine directly.

See also
`Object._get_property_list()<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_logo}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\_get_logo**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_logo>`{.interpreted-text
role="ref"}

Returns the platform logo displayed in the export dialog. The logo
should be 32×32 pixels, adjusted for the current editor scale (see
`EditorInterface.get_editor_scale()<class_EditorInterface_method_get_editor_scale>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **\_get_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_name>`{.interpreted-text
role="ref"}

Returns export platform name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_option_icon}
::: rst-class
classref-method
:::
::::

`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}
**\_get_option_icon**(device: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_option_icon>`{.interpreted-text
role="ref"}

Returns the item icon for the specified `device` in the one-click deploy
menu. The icon should be 16×16 pixels, adjusted for the current editor
scale (see
`EditorInterface.get_editor_scale()<class_EditorInterface_method_get_editor_scale>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_option_label}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_option_label**(device: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_option_label>`{.interpreted-text
role="ref"}

Returns one-click deploy menu item label for the specified `device`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_option_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_option_tooltip**(device: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_option_tooltip>`{.interpreted-text
role="ref"}

Returns one-click deploy menu item tooltip for the specified `device`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_options_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_options_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_options_count>`{.interpreted-text
role="ref"}

Returns the number of devices (or other options) available in the
one-click deploy menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_options_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_options_tooltip**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_options_tooltip>`{.interpreted-text
role="ref"}

Returns tooltip of the one-click deploy menu button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_os_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **\_get_os_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_os_name>`{.interpreted-text
role="ref"}

Returns target OS name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_platform_features}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_platform_features**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_platform_features>`{.interpreted-text
role="ref"}

Returns array of platform specific features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_preset_features}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_preset_features**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_preset_features>`{.interpreted-text
role="ref"}

Returns array of platform specific features for the specified `preset`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__get_run_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\_get_run_icon**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__get_run_icon>`{.interpreted-text
role="ref"}

Returns the icon of the one-click deploy menu button. The icon should be
16×16 pixels, adjusted for the current editor scale (see
`EditorInterface.get_editor_scale()<class_EditorInterface_method_get_editor_scale>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__has_valid_export_configuration}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_has_valid_export_configuration**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`{.interpreted-text
role="ref"}

Returns `true` if export configuration is valid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__has_valid_project_configuration}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_has_valid_project_configuration**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>`{.interpreted-text
role="ref"}

Returns `true` if project configuration is valid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__is_executable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_executable**(path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__is_executable>`{.interpreted-text
role="ref"}

Returns `true` if specified file is a valid executable (native
executable or script) for the target platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__poll_export}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_poll_export**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__poll_export>`{.interpreted-text
role="ref"}

Returns `true` if one-click deploy options are changed and editor
interface should be updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__run}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_run**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, device: `int<class_int>`{.interpreted-text role="ref"},
debug_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__run>`{.interpreted-text
role="ref"}

This method is called when `device` one-click deploy menu option is
selected.

Implementation should export project to a temporary location, upload and
run it on the specific `device`, or perform another action associated
with the menu item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_private_method__should_update_export_options}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_should_update_export_options**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_private_method__should_update_export_options>`{.interpreted-text
role="ref"}

Returns `true` if export options list is changed and presets should be
updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_method_get_config_error}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_config_error**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_method_get_config_error>`{.interpreted-text
role="ref"}

Returns current configuration error message text. This method should be
called only from the
`_can_export()<class_EditorExportPlatformExtension_private_method__can_export>`{.interpreted-text
role="ref"},
`_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`{.interpreted-text
role="ref"}, or
`_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>`{.interpreted-text
role="ref"} implementations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_method_get_config_missing_templates}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_config_missing_templates**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_method_get_config_missing_templates>`{.interpreted-text
role="ref"}

Returns `true` is export templates are missing from the current
configuration. This method should be called only from the
`_can_export()<class_EditorExportPlatformExtension_private_method__can_export>`{.interpreted-text
role="ref"},
`_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`{.interpreted-text
role="ref"}, or
`_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>`{.interpreted-text
role="ref"} implementations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_method_set_config_error}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_config_error**(error_text:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_method_set_config_error>`{.interpreted-text
role="ref"}

Sets current configuration error message text. This method should be
called only from the
`_can_export()<class_EditorExportPlatformExtension_private_method__can_export>`{.interpreted-text
role="ref"},
`_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`{.interpreted-text
role="ref"}, or
`_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>`{.interpreted-text
role="ref"} implementations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformExtension_method_set_config_missing_templates}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_config_missing_templates**(missing_templates:
`bool<class_bool>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatformExtension_method_set_config_missing_templates>`{.interpreted-text
role="ref"}

Set to `true` is export templates are missing from the current
configuration. This method should be called only from the
`_can_export()<class_EditorExportPlatformExtension_private_method__can_export>`{.interpreted-text
role="ref"},
`_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`{.interpreted-text
role="ref"}, or
`_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>`{.interpreted-text
role="ref"} implementations.
