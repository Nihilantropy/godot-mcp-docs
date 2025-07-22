github_url
:   hide

# EditorSceneFormatImporterFBX2GLTF {#class_EditorSceneFormatImporterFBX2GLTF}

**Inherits:**
`EditorSceneFormatImporter<class_EditorSceneFormatImporter>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Importer for the `.fbx` scene file format.

::: rst-class
classref-introduction-group
:::

## Description

Imports Autodesk FBX 3D scenes by way of converting them to glTF 2.0
using the FBX2glTF command line tool.

The location of the FBX2glTF binary is set via the
`EditorSettings.filesystem/import/fbx/fbx2gltf_path<class_EditorSettings_property_filesystem/import/fbx/fbx2gltf_path>`{.interpreted-text
role="ref"} editor setting.

This importer is only used if
`ProjectSettings.filesystem/import/fbx2gltf/enabled<class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled>`{.interpreted-text
role="ref"} is set to `true`.
