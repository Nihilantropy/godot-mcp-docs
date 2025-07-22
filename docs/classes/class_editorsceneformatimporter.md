github_url
:   hide

# EditorSceneFormatImporter {#class_EditorSceneFormatImporter}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`EditorSceneFormatImporterBlend<class_EditorSceneFormatImporterBlend>`{.interpreted-text
role="ref"},
`EditorSceneFormatImporterFBX2GLTF<class_EditorSceneFormatImporterFBX2GLTF>`{.interpreted-text
role="ref"},
`EditorSceneFormatImporterGLTF<class_EditorSceneFormatImporterGLTF>`{.interpreted-text
role="ref"},
`EditorSceneFormatImporterUFBX<class_EditorSceneFormatImporterUFBX>`{.interpreted-text
role="ref"}

Imports scenes from third-parties\' 3D files.

::: rst-class
classref-introduction-group
:::

## Description

**EditorSceneFormatImporter** allows to define an importer script for a
third-party 3D format.

To use **EditorSceneFormatImporter**, register it using the
`EditorPlugin.add_scene_format_importer_plugin()<class_EditorPlugin_method_add_scene_format_importer_plugin>`{.interpreted-text
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

## Constants

:::: {#class_EditorSceneFormatImporter_constant_IMPORT_SCENE}
::: rst-class
classref-constant
:::
::::

**IMPORT_SCENE** = `1`
`🔗<class_EditorSceneFormatImporter_constant_IMPORT_SCENE>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorSceneFormatImporter_constant_IMPORT_ANIMATION}
::: rst-class
classref-constant
:::
::::

**IMPORT_ANIMATION** = `2`
`🔗<class_EditorSceneFormatImporter_constant_IMPORT_ANIMATION>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorSceneFormatImporter_constant_IMPORT_FAIL_ON_MISSING_DEPENDENCIES}
::: rst-class
classref-constant
:::
::::

**IMPORT_FAIL_ON_MISSING_DEPENDENCIES** = `4`
`🔗<class_EditorSceneFormatImporter_constant_IMPORT_FAIL_ON_MISSING_DEPENDENCIES>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorSceneFormatImporter_constant_IMPORT_GENERATE_TANGENT_ARRAYS}
::: rst-class
classref-constant
:::
::::

**IMPORT_GENERATE_TANGENT_ARRAYS** = `8`
`🔗<class_EditorSceneFormatImporter_constant_IMPORT_GENERATE_TANGENT_ARRAYS>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorSceneFormatImporter_constant_IMPORT_USE_NAMED_SKIN_BINDS}
::: rst-class
classref-constant
:::
::::

**IMPORT_USE_NAMED_SKIN_BINDS** = `16`
`🔗<class_EditorSceneFormatImporter_constant_IMPORT_USE_NAMED_SKIN_BINDS>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorSceneFormatImporter_constant_IMPORT_DISCARD_MESHES_AND_MATERIALS}
::: rst-class
classref-constant
:::
::::

**IMPORT_DISCARD_MESHES_AND_MATERIALS** = `32`
`🔗<class_EditorSceneFormatImporter_constant_IMPORT_DISCARD_MESHES_AND_MATERIALS>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorSceneFormatImporter_constant_IMPORT_FORCE_DISABLE_MESH_COMPRESSION}
::: rst-class
classref-constant
:::
::::

**IMPORT_FORCE_DISABLE_MESH_COMPRESSION** = `64`
`🔗<class_EditorSceneFormatImporter_constant_IMPORT_FORCE_DISABLE_MESH_COMPRESSION>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this constant. Please help us by
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

:::: {#class_EditorSceneFormatImporter_private_method__get_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_extensions**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSceneFormatImporter_private_method__get_extensions>`{.interpreted-text
role="ref"}

Return supported file extensions for this scene importer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSceneFormatImporter_private_method__get_import_options}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_get_import_options**(path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSceneFormatImporter_private_method__get_import_options>`{.interpreted-text
role="ref"}

Override to add general import options. These will appear in the main
import dock on the editor. Add options via
`add_import_option()<class_EditorSceneFormatImporter_method_add_import_option>`{.interpreted-text
role="ref"} and
`add_import_option_advanced()<class_EditorSceneFormatImporter_method_add_import_option_advanced>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* All **EditorSceneFormatImporter** and
`EditorScenePostImportPlugin<class_EditorScenePostImportPlugin>`{.interpreted-text
role="ref"} instances will add options for all files. It is good
practice to check the file extension when `path` is non-empty.

When the user is editing project settings, `path` will be empty. It is
recommended to add all options when `path` is empty to allow the user to
customize Import Defaults.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSceneFormatImporter_private_method__get_option_visibility}
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
`🔗<class_EditorSceneFormatImporter_private_method__get_option_visibility>`{.interpreted-text
role="ref"}

Should return `true` to show the given option, `false` to hide the given
option, or `null` to ignore.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSceneFormatImporter_private_method__import_scene}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**\_import_scene**(path: `String<class_String>`{.interpreted-text
role="ref"}, flags: `int<class_int>`{.interpreted-text role="ref"},
options: `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSceneFormatImporter_private_method__import_scene>`{.interpreted-text
role="ref"}

Perform the bulk of the scene import logic here, for example using
`GLTFDocument<class_GLTFDocument>`{.interpreted-text role="ref"} or
`FBXDocument<class_FBXDocument>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSceneFormatImporter_method_add_import_option}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_import_option**(name: `String<class_String>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_EditorSceneFormatImporter_method_add_import_option>`{.interpreted-text
role="ref"}

Add a specific import option (name and default value only). This
function can only be called from
`_get_import_options()<class_EditorSceneFormatImporter_private_method__get_import_options>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSceneFormatImporter_method_add_import_option_advanced}
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
`🔗<class_EditorSceneFormatImporter_method_add_import_option_advanced>`{.interpreted-text
role="ref"}

Add a specific import option. This function can only be called from
`_get_import_options()<class_EditorSceneFormatImporter_private_method__get_import_options>`{.interpreted-text
role="ref"}.
