github_url
:   hide

# GLTFSkeleton {#class_GLTFSkeleton}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

::: {.container .contribute}
There is currently no description for this class. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
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

:::: {#class_GLTFSkeleton_property_joints}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**joints** = `PackedInt32Array()`
`🔗<class_GLTFSkeleton_property_joints>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_joints**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_joints**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSkeleton_property_roots}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**roots** = `PackedInt32Array()`
`🔗<class_GLTFSkeleton_property_roots>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_roots**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_roots**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFSkeleton_method_get_bone_attachment}
::: rst-class
classref-method
:::
::::

`BoneAttachment3D<class_BoneAttachment3D>`{.interpreted-text role="ref"}
**get_bone_attachment**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GLTFSkeleton_method_get_bone_attachment>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSkeleton_method_get_bone_attachment_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_bone_attachment_count**()
`🔗<class_GLTFSkeleton_method_get_bone_attachment_count>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSkeleton_method_get_godot_bone_node}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_godot_bone_node**()
`🔗<class_GLTFSkeleton_method_get_godot_bone_node>`{.interpreted-text
role="ref"}

Returns a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
that maps skeleton bone indices to the indices of glTF nodes. This
property is unused during import, and only set during export. In a glTF
file, a bone is a node, so Godot converts skeleton bones to glTF nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSkeleton_method_get_godot_skeleton}
::: rst-class
classref-method
:::
::::

`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
**get_godot_skeleton**()
`🔗<class_GLTFSkeleton_method_get_godot_skeleton>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSkeleton_method_get_unique_names}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
**get_unique_names**()
`🔗<class_GLTFSkeleton_method_get_unique_names>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSkeleton_method_set_godot_bone_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_godot_bone_node**(godot_bone_node:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_GLTFSkeleton_method_set_godot_bone_node>`{.interpreted-text
role="ref"}

Sets a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"} that
maps skeleton bone indices to the indices of glTF nodes. This property
is unused during import, and only set during export. In a glTF file, a
bone is a node, so Godot converts skeleton bones to glTF nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFSkeleton_method_set_unique_names}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_unique_names**(unique_names:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\])
`🔗<class_GLTFSkeleton_method_set_unique_names>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
