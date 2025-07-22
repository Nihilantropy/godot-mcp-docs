github_url
:   hide

# EditorFeatureProfile {#class_EditorFeatureProfile}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

An editor feature profile which can be used to disable specific
features.

::: rst-class
classref-introduction-group
:::

## Description

An editor feature profile can be used to disable specific features of
the Godot editor. When disabled, the features won\'t appear in the
editor, which makes the editor less cluttered. This is useful in
education settings to reduce confusion or when working in a team. For
example, artists and level designers could use a feature profile that
disables the script editor to avoid accidentally making changes to files
they aren\'t supposed to edit.

To manage editor feature profiles visually, use **Editor \> Manage
Feature Profiles\...** at the top of the editor window.

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

## Enumerations

:::: {#enum_EditorFeatureProfile_Feature}
::: rst-class
classref-enumeration
:::
::::

enum **Feature**:
`🔗<enum_EditorFeatureProfile_Feature>`{.interpreted-text role="ref"}

:::: {#class_EditorFeatureProfile_constant_FEATURE_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_3D** = `0`

The 3D editor. If this feature is disabled, the 3D editor won\'t display
but 3D nodes will still display in the Create New Node dialog.

:::: {#class_EditorFeatureProfile_constant_FEATURE_SCRIPT}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_SCRIPT** = `1`

The Script tab, which contains the script editor and class reference
browser. If this feature is disabled, the Script tab won\'t display.

:::: {#class_EditorFeatureProfile_constant_FEATURE_ASSET_LIB}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_ASSET_LIB** = `2`

The AssetLib tab. If this feature is disabled, the AssetLib tab won\'t
display.

:::: {#class_EditorFeatureProfile_constant_FEATURE_SCENE_TREE}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_SCENE_TREE** = `3`

Scene tree editing. If this feature is disabled, the Scene tree dock
will still be visible but will be read-only.

:::: {#class_EditorFeatureProfile_constant_FEATURE_NODE_DOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_NODE_DOCK** = `4`

The Node dock. If this feature is disabled, signals and groups won\'t be
visible and modifiable from the editor.

:::: {#class_EditorFeatureProfile_constant_FEATURE_FILESYSTEM_DOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_FILESYSTEM_DOCK** = `5`

The FileSystem dock. If this feature is disabled, the FileSystem dock
won\'t be visible.

:::: {#class_EditorFeatureProfile_constant_FEATURE_IMPORT_DOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_IMPORT_DOCK** = `6`

The Import dock. If this feature is disabled, the Import dock won\'t be
visible.

:::: {#class_EditorFeatureProfile_constant_FEATURE_HISTORY_DOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_HISTORY_DOCK** = `7`

The History dock. If this feature is disabled, the History dock won\'t
be visible.

:::: {#class_EditorFeatureProfile_constant_FEATURE_GAME}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_GAME** = `8`

The Game tab, which allows embedding the game window and selecting nodes
by clicking inside of it. If this feature is disabled, the Game tab
won\'t display.

:::: {#class_EditorFeatureProfile_constant_FEATURE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} **FEATURE_MAX** = `9`

Represents the size of the
`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorFeatureProfile_method_get_feature_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_feature_name**(feature:
`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"})
`🔗<class_EditorFeatureProfile_method_get_feature_name>`{.interpreted-text
role="ref"}

Returns the specified `feature`\'s human-readable name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_is_class_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_class_disabled**(class_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFeatureProfile_method_is_class_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the class specified by `class_name` is disabled. When
disabled, the class won\'t appear in the Create New Node dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_is_class_editor_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_class_editor_disabled**(class_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFeatureProfile_method_is_class_editor_disabled>`{.interpreted-text
role="ref"}

Returns `true` if editing for the class specified by `class_name` is
disabled. When disabled, the class will still appear in the Create New
Node dialog but the Inspector will be read-only when selecting a node
that extends the class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_is_class_property_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_class_property_disabled**(class_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFeatureProfile_method_is_class_property_disabled>`{.interpreted-text
role="ref"}

Returns `true` if `property` is disabled in the class specified by
`class_name`. When a property is disabled, it won\'t appear in the
Inspector when selecting a node that extends the class specified by
`class_name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_is_feature_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_feature_disabled**(feature:
`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFeatureProfile_method_is_feature_disabled>`{.interpreted-text
role="ref"}

Returns `true` if the `feature` is disabled. When a feature is disabled,
it will disappear from the editor entirely.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_load_from_file}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_from_file**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorFeatureProfile_method_load_from_file>`{.interpreted-text
role="ref"}

Loads an editor feature profile from a file. The file must follow the
JSON format obtained by using the feature profile manager\'s **Export**
button or the
`save_to_file()<class_EditorFeatureProfile_method_save_to_file>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* Feature profiles created via the user interface are loaded
from the `feature_profiles` directory, as a file with the `.profile`
extension. The editor configuration folder can be found by using
`EditorPaths.get_config_dir()<class_EditorPaths_method_get_config_dir>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_save_to_file}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_to_file**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorFeatureProfile_method_save_to_file>`{.interpreted-text
role="ref"}

Saves the editor feature profile to a file in JSON format. It can then
be imported using the feature profile manager\'s **Import** button or
the
`load_from_file()<class_EditorFeatureProfile_method_load_from_file>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* Feature profiles created via the user interface are saved
in the `feature_profiles` directory, as a file with the `.profile`
extension. The editor configuration folder can be found by using
`EditorPaths.get_config_dir()<class_EditorPaths_method_get_config_dir>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_set_disable_class}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_disable_class**(class_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, disable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorFeatureProfile_method_set_disable_class>`{.interpreted-text
role="ref"}

If `disable` is `true`, disables the class specified by `class_name`.
When disabled, the class won\'t appear in the Create New Node dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_set_disable_class_editor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_disable_class_editor**(class_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, disable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorFeatureProfile_method_set_disable_class_editor>`{.interpreted-text
role="ref"}

If `disable` is `true`, disables editing for the class specified by
`class_name`. When disabled, the class will still appear in the Create
New Node dialog but the Inspector will be read-only when selecting a
node that extends the class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_set_disable_class_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_disable_class_property**(class_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, disable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorFeatureProfile_method_set_disable_class_property>`{.interpreted-text
role="ref"}

If `disable` is `true`, disables editing for `property` in the class
specified by `class_name`. When a property is disabled, it won\'t appear
in the Inspector when selecting a node that extends the class specified
by `class_name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFeatureProfile_method_set_disable_feature}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_disable_feature**(feature:
`Feature<enum_EditorFeatureProfile_Feature>`{.interpreted-text
role="ref"}, disable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorFeatureProfile_method_set_disable_feature>`{.interpreted-text
role="ref"}

If `disable` is `true`, disables the editor feature specified in
`feature`. When a feature is disabled, it will disappear from the editor
entirely.
