github_url
:   hide

# FBXDocument {#class_FBXDocument}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `GLTFDocument<class_GLTFDocument>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Handles FBX documents.

::: rst-class
classref-introduction-group
:::

## Description

The FBXDocument handles FBX documents. It provides methods to append
data from buffers or files, generate scenes, and register/unregister
document extensions.

When exporting FBX from Blender, use the \"FBX Units Scale\" option. The
\"FBX Units Scale\" option sets the correct scale factor and avoids
manual adjustments when re-importing into Blender, such as through glTF
export.
