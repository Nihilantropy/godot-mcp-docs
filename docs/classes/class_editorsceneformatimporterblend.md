github_url
:   hide

# EditorSceneFormatImporterBlend {#class_EditorSceneFormatImporterBlend}

**Inherits:**
`EditorSceneFormatImporter<class_EditorSceneFormatImporter>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Importer for Blender\'s `.blend` scene file format.

::: rst-class
classref-introduction-group
:::

## Description

Imports Blender scenes in the `.blend` file format through the glTF 2.0
3D import pipeline. This importer requires Blender to be installed by
the user, so that it can be used to export the scene as glTF 2.0.

The location of the Blender binary is set via the
`EditorSettings.filesystem/import/blender/blender_path<class_EditorSettings_property_filesystem/import/blender/blender_path>`{.interpreted-text
role="ref"} setting.

This importer is only used if
`ProjectSettings.filesystem/import/blender/enabled<class_ProjectSettings_property_filesystem/import/blender/enabled>`{.interpreted-text
role="ref"} is enabled, otherwise `.blend` files present in the project
folder are not imported.

Blend import requires Blender 3.0.

Internally, the EditorSceneFormatImporterBlend uses the Blender glTF
\"Use Original\" mode to reference external textures.
