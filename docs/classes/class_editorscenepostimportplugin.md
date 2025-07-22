github_url
:   hide

# EditorScenePostImportPlugin {#class_EditorScenePostImportPlugin}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Plugin to control and modifying the process of importing a scene.

::: rst-class
classref-introduction-group
:::

## Description

This plugin type exists to modify the process of importing scenes,
allowing to change the content as well as add importer options at every
stage of the process.

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

:::: {#enum_EditorScenePostImportPlugin_InternalImportCategory}
::: rst-class
classref-enumeration
:::
::::

enum **InternalImportCategory**:
`🔗<enum_EditorScenePostImportPlugin_InternalImportCategory>`{.interpreted-text
role="ref"}

:::: {#class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_NODE}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>`{.interpreted-text
role="ref"} **INTERNAL_IMPORT_CATEGORY_NODE** = `0`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_MESH_3D_NODE}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>`{.interpreted-text
role="ref"} **INTERNAL_IMPORT_CATEGORY_MESH_3D_NODE** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_MESH}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>`{.interpreted-text
role="ref"} **INTERNAL_IMPORT_CATEGORY_MESH** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_MATERIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>`{.interpreted-text
role="ref"} **INTERNAL_IMPORT_CATEGORY_MATERIAL** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_ANIMATION}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>`{.interpreted-text
role="ref"} **INTERNAL_IMPORT_CATEGORY_ANIMATION** = `4`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_ANIMATION_NODE}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>`{.interpreted-text
role="ref"} **INTERNAL_IMPORT_CATEGORY_ANIMATION_NODE** = `5`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_SKELETON_3D_NODE}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>`{.interpreted-text
role="ref"} **INTERNAL_IMPORT_CATEGORY_SKELETON_3D_NODE** = `6`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorScenePostImportPlugin_constant_INTERNAL_IMPORT_CATEGORY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>`{.interpreted-text
role="ref"} **INTERNAL_IMPORT_CATEGORY_MAX** = `7`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorScenePostImportPlugin_private_method__get_import_options}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_get_import_options**(path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImportPlugin_private_method__get_import_options>`{.interpreted-text
role="ref"}

Override to add general import options. These will appear in the main
import dock on the editor. Add options via
`add_import_option()<class_EditorScenePostImportPlugin_method_add_import_option>`{.interpreted-text
role="ref"} and
`add_import_option_advanced()<class_EditorScenePostImportPlugin_method_add_import_option_advanced>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_private_method__get_internal_import_options}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_get_internal_import_options**(category:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>`{.interpreted-text
role="ref"}

Override to add internal import options. These will appear in the 3D
scene import dialog. Add options via
`add_import_option()<class_EditorScenePostImportPlugin_method_add_import_option>`{.interpreted-text
role="ref"} and
`add_import_option_advanced()<class_EditorScenePostImportPlugin_method_add_import_option_advanced>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_private_method__get_internal_option_update_view_required}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_get_internal_option_update_view_required**(category:
`int<class_int>`{.interpreted-text role="ref"}, option:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImportPlugin_private_method__get_internal_option_update_view_required>`{.interpreted-text
role="ref"}

Should return `true` if the 3D view of the import dialog needs to update
when changing the given option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_private_method__get_internal_option_visibility}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_get_internal_option_visibility**(category:
`int<class_int>`{.interpreted-text role="ref"}, for_animation:
`bool<class_bool>`{.interpreted-text role="ref"}, option:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImportPlugin_private_method__get_internal_option_visibility>`{.interpreted-text
role="ref"}

Should return `true` to show the given option, `false` to hide the given
option, or `null` to ignore.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_private_method__get_option_visibility}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_get_option_visibility**(path:
`String<class_String>`{.interpreted-text role="ref"}, for_animation:
`bool<class_bool>`{.interpreted-text role="ref"}, option:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImportPlugin_private_method__get_option_visibility>`{.interpreted-text
role="ref"}

Should return `true` to show the given option, `false` to hide the given
option, or `null` to ignore.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_private_method__internal_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_internal_process**(category: `int<class_int>`{.interpreted-text
role="ref"}, base_node: `Node<class_Node>`{.interpreted-text
role="ref"}, node: `Node<class_Node>`{.interpreted-text role="ref"},
resource: `Resource<class_Resource>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImportPlugin_private_method__internal_process>`{.interpreted-text
role="ref"}

Process a specific node or resource for a given category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_private_method__post_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_post_process**(scene: `Node<class_Node>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImportPlugin_private_method__post_process>`{.interpreted-text
role="ref"}

Post-process the scene. This function is called after the final scene
has been configured.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_private_method__pre_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_pre_process**(scene: `Node<class_Node>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImportPlugin_private_method__pre_process>`{.interpreted-text
role="ref"}

Pre-process the scene. This function is called right after the scene
format loader loaded the scene and no changes have been made.

Pre-process may be used to adjust internal import options in the
`"nodes"`, `"meshes"`, `"animations"` or `"materials"` keys inside
`get_option_value("_subresources")`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_method_add_import_option}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_import_option**(name: `String<class_String>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_EditorScenePostImportPlugin_method_add_import_option>`{.interpreted-text
role="ref"}

Add a specific import option (name and default value only). This
function can only be called from
`_get_import_options()<class_EditorScenePostImportPlugin_private_method__get_import_options>`{.interpreted-text
role="ref"} and
`_get_internal_import_options()<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_method_add_import_option_advanced}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_import_option_advanced**(type:
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"},
default_value: `Variant<class_Variant>`{.interpreted-text role="ref"},
hint: `PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} = 0, hint_string: `String<class_String>`{.interpreted-text
role="ref"} = \"\", usage_flags: `int<class_int>`{.interpreted-text
role="ref"} = 6)
`🔗<class_EditorScenePostImportPlugin_method_add_import_option_advanced>`{.interpreted-text
role="ref"}

Add a specific import option. This function can only be called from
`_get_import_options()<class_EditorScenePostImportPlugin_private_method__get_import_options>`{.interpreted-text
role="ref"} and
`_get_internal_import_options()<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImportPlugin_method_get_option_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_option_value**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImportPlugin_method_get_option_value>`{.interpreted-text
role="ref"}

Query the value of an option. This function can only be called from
those querying visibility, or processing.
