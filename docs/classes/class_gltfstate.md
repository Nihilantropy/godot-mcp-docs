github_url
:   hide

# GLTFState {#class_GLTFState}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `FBXState<class_FBXState>`{.interpreted-text
role="ref"}

Represents all data of a glTF file.

::: rst-class
classref-introduction-group
:::

## Description

Contains all nodes and resources of a glTF file. This is used by
`GLTFDocument<class_GLTFDocument>`{.interpreted-text role="ref"} as data
storage, which allows
`GLTFDocument<class_GLTFDocument>`{.interpreted-text role="ref"} and all
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes to remain stateless.

GLTFState can be populated by
`GLTFDocument<class_GLTFDocument>`{.interpreted-text role="ref"} reading
a file or by converting a Godot scene. Then the data can either be used
to create a Godot scene or save to a glTF file. The code that converts
to/from a Godot scene can be intercepted at arbitrary points by
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes. This allows for custom data to be stored in the
glTF file or for custom data to be converted to/from Godot nodes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}
- [glTF asset header
  schema](https://github.com/KhronosGroup/glTF/blob/main/specification/2.0/schema/asset.schema.json)

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

## Constants

:::: {#class_GLTFState_constant_HANDLE_BINARY_DISCARD_TEXTURES}
::: rst-class
classref-constant
:::
::::

**HANDLE_BINARY_DISCARD_TEXTURES** = `0`
`🔗<class_GLTFState_constant_HANDLE_BINARY_DISCARD_TEXTURES>`{.interpreted-text
role="ref"}

Discards all embedded textures and uses untextured materials.

:::: {#class_GLTFState_constant_HANDLE_BINARY_EXTRACT_TEXTURES}
::: rst-class
classref-constant
:::
::::

**HANDLE_BINARY_EXTRACT_TEXTURES** = `1`
`🔗<class_GLTFState_constant_HANDLE_BINARY_EXTRACT_TEXTURES>`{.interpreted-text
role="ref"}

Extracts embedded textures to be reimported and compressed. Editor only.
Acts as uncompressed at runtime.

:::: {#class_GLTFState_constant_HANDLE_BINARY_EMBED_AS_BASISU}
::: rst-class
classref-constant
:::
::::

**HANDLE_BINARY_EMBED_AS_BASISU** = `2`
`🔗<class_GLTFState_constant_HANDLE_BINARY_EMBED_AS_BASISU>`{.interpreted-text
role="ref"}

Embeds textures VRAM compressed with Basis Universal into the generated
scene.

:::: {#class_GLTFState_constant_HANDLE_BINARY_EMBED_AS_UNCOMPRESSED}
::: rst-class
classref-constant
:::
::::

**HANDLE_BINARY_EMBED_AS_UNCOMPRESSED** = `3`
`🔗<class_GLTFState_constant_HANDLE_BINARY_EMBED_AS_UNCOMPRESSED>`{.interpreted-text
role="ref"}

Embeds textures compressed losslessly into the generated scene, matching
old behavior.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GLTFState_property_bake_fps}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bake_fps** = `30.0`
`🔗<class_GLTFState_property_bake_fps>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_fps**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_bake_fps**()

The baking fps of the animation for either import or export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_base_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **base_path** =
`""` `🔗<class_GLTFState_property_base_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_base_path**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_base_path**()

The folder path associated with this glTF data. This is used to find
other files the glTF file references, like images or binary buffers.
This will be set during import when appending from a file, and will be
set during export when writing to a file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_buffers}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}\] **buffers** = `[]`
`🔗<class_GLTFState_property_buffers>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_buffers**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"}\] **get_buffers**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_copyright}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **copyright** =
`""` `🔗<class_GLTFState_property_copyright>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_copyright**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_copyright**()

The copyright string in the asset header of the glTF file. This is set
during import if present and export if non-empty. See the glTF asset
header documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_create_animations}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **create_animations** =
`true`
`🔗<class_GLTFState_property_create_animations>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_create_animations**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_create_animations**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_filename}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **filename** = `""`
`🔗<class_GLTFState_property_filename>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filename**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_filename**()

The file name associated with this glTF data. If it ends with `.gltf`,
this is text-based glTF, otherwise this is binary GLB. This will be set
during import when appending from a file, and will be set during export
when writing to a file. If writing to a buffer, this will be an empty
string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_glb_data}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**glb_data** = `PackedByteArray()`
`🔗<class_GLTFState_property_glb_data>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glb_data**(value:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_glb_data**()

The binary buffer attached to a .glb file.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_import_as_skeleton_bones}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**import_as_skeleton_bones** = `false`
`🔗<class_GLTFState_property_import_as_skeleton_bones>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_import_as_skeleton_bones**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_import_as_skeleton_bones**()

If `true`, forces all GLTFNodes in the document to be bones of a single
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} Godot node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_json}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} **json** =
`{}` `🔗<class_GLTFState_property_json>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_json**(value: `Dictionary<class_Dictionary>`{.interpreted-text
  role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_json**()

The original raw JSON document corresponding to this GLTFState.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_major_version}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **major_version** = `0`
`🔗<class_GLTFState_property_major_version>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_major_version**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_major_version**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_minor_version}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **minor_version** = `0`
`🔗<class_GLTFState_property_minor_version>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_minor_version**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_minor_version**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_root_nodes}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**root_nodes** = `PackedInt32Array()`
`🔗<class_GLTFState_property_root_nodes>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_nodes**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_root_nodes**()

The root nodes of the glTF file. Typically, a glTF file will only have
one scene, and therefore one root node. However, a glTF file may have
multiple scenes and therefore multiple root nodes, which will be
generated as siblings of each other and as children of the root node of
the generated Godot scene.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_scene_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **scene_name** =
`""` `🔗<class_GLTFState_property_scene_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scene_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_scene_name**()

The name of the scene. When importing, if not specified, this will be
the file name. When exporting, if specified, the scene name will be
saved to the glTF file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_property_use_named_skin_binds}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_named_skin_binds** = `false`
`🔗<class_GLTFState_property_use_named_skin_binds>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_named_skin_binds**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_named_skin_binds**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
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

:::: {#class_GLTFState_method_add_used_extension}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_used_extension**(extension_name:
`String<class_String>`{.interpreted-text role="ref"}, required:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GLTFState_method_add_used_extension>`{.interpreted-text
role="ref"}

Appends an extension to the list of extensions used by this glTF file
during serialization. If `required` is `true`, the extension will also
be added to the list of required extensions. Do not run this in
`GLTFDocumentExtension._export_post()<class_GLTFDocumentExtension_private_method__export_post>`{.interpreted-text
role="ref"}, as that stage is too late to add extensions. The final list
is sorted alphabetically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_append_data_to_buffers}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**append_data_to_buffers**(data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
deduplication: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GLTFState_method_append_data_to_buffers>`{.interpreted-text
role="ref"}

Appends the given byte array `data` to the buffers and creates a
`GLTFBufferView<class_GLTFBufferView>`{.interpreted-text role="ref"} for
it. The index of the destination
`GLTFBufferView<class_GLTFBufferView>`{.interpreted-text role="ref"} is
returned. If `deduplication` is `true`, the buffers are first searched
for duplicate data, otherwise new bytes are always appended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_append_gltf_node}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**append_gltf_node**(gltf_node:
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"},
godot_scene_node: `Node<class_Node>`{.interpreted-text role="ref"},
parent_node_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GLTFState_method_append_gltf_node>`{.interpreted-text
role="ref"}

Appends the given `GLTFNode<class_GLTFNode>`{.interpreted-text
role="ref"} to the state, and returns its new index. This can be used to
export one Godot node as multiple glTF nodes, or inject new glTF nodes
at import time. On import, this must be called before
`GLTFDocumentExtension._generate_scene_node()<class_GLTFDocumentExtension_private_method__generate_scene_node>`{.interpreted-text
role="ref"} finishes for the parent node. On export, this must be called
before
`GLTFDocumentExtension._export_node()<class_GLTFDocumentExtension_private_method__export_node>`{.interpreted-text
role="ref"} runs for the parent node.

The `godot_scene_node` parameter is the Godot scene node that
corresponds to this glTF node. This is highly recommended to be set to a
valid node, but may be `null` if there is no corresponding Godot scene
node. One Godot scene node may be used for multiple glTF nodes, so if
exporting multiple glTF nodes for one Godot scene node, use the same
Godot scene node for each.

The `parent_node_index` parameter is the index of the parent
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"} in the state.
If `-1`, the node will be a root node, otherwise the new node will be
added to the parent\'s list of children. The index will also be written
to the
`GLTFNode.parent<class_GLTFNode_property_parent>`{.interpreted-text
role="ref"} property of the new node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_accessors}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFAccessor<class_GLTFAccessor>`{.interpreted-text
role="ref"}\] **get_accessors**()
`🔗<class_GLTFState_method_get_accessors>`{.interpreted-text role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_additional_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GLTFState_method_get_additional_data>`{.interpreted-text
role="ref"}

Gets additional arbitrary data in this **GLTFState** instance. This can
be used to keep per-file state data in
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes, which is important because they are stateless.

The argument should be the
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} name (does not have to match the extension name in the glTF
file), and the return value can be anything you set. If nothing was set,
the return value is `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_animation_player}
::: rst-class
classref-method
:::
::::

`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
**get_animation_player**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GLTFState_method_get_animation_player>`{.interpreted-text
role="ref"}

Returns the `AnimationPlayer<class_AnimationPlayer>`{.interpreted-text
role="ref"} node with the given index. These nodes are only used during
the export process when converting Godot
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
nodes to glTF animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_animation_players_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_animation_players_count**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GLTFState_method_get_animation_players_count>`{.interpreted-text
role="ref"}

Returns the number of
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
nodes in this **GLTFState**. These nodes are only used during the export
process when converting Godot
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
nodes to glTF animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_animations}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFAnimation<class_GLTFAnimation>`{.interpreted-text
role="ref"}\] **get_animations**()
`🔗<class_GLTFState_method_get_animations>`{.interpreted-text
role="ref"}

Returns an array of all
`GLTFAnimation<class_GLTFAnimation>`{.interpreted-text role="ref"}s in
the glTF file. When importing, these will be generated as animations in
an `AnimationPlayer<class_AnimationPlayer>`{.interpreted-text
role="ref"} node. When exporting, these will be generated from Godot
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_buffer_views}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFBufferView<class_GLTFBufferView>`{.interpreted-text
role="ref"}\] **get_buffer_views**()
`🔗<class_GLTFState_method_get_buffer_views>`{.interpreted-text
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

:::: {#class_GLTFState_method_get_cameras}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFCamera<class_GLTFCamera>`{.interpreted-text
role="ref"}\] **get_cameras**()
`🔗<class_GLTFState_method_get_cameras>`{.interpreted-text role="ref"}

Returns an array of all `GLTFCamera<class_GLTFCamera>`{.interpreted-text
role="ref"}s in the glTF file. These are the cameras that the
`GLTFNode.camera<class_GLTFNode_property_camera>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_handle_binary_image}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_handle_binary_image**()
`🔗<class_GLTFState_method_get_handle_binary_image>`{.interpreted-text
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

:::: {#class_GLTFState_method_get_images}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}\] **get_images**()
`🔗<class_GLTFState_method_get_images>`{.interpreted-text role="ref"}

Gets the images of the glTF file as an array of
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}s. These are
the images that the
`GLTFTexture.src_image<class_GLTFTexture_property_src_image>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_lights}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFLight<class_GLTFLight>`{.interpreted-text
role="ref"}\] **get_lights**()
`🔗<class_GLTFState_method_get_lights>`{.interpreted-text role="ref"}

Returns an array of all `GLTFLight<class_GLTFLight>`{.interpreted-text
role="ref"}s in the glTF file. These are the lights that the
`GLTFNode.light<class_GLTFNode_property_light>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_materials}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Material<class_Material>`{.interpreted-text role="ref"}\]
**get_materials**()
`🔗<class_GLTFState_method_get_materials>`{.interpreted-text role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_meshes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFMesh<class_GLTFMesh>`{.interpreted-text role="ref"}\]
**get_meshes**()
`🔗<class_GLTFState_method_get_meshes>`{.interpreted-text role="ref"}

Returns an array of all `GLTFMesh<class_GLTFMesh>`{.interpreted-text
role="ref"}es in the glTF file. These are the meshes that the
`GLTFNode.mesh<class_GLTFNode_property_mesh>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_node_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_node_index**(scene_node: `Node<class_Node>`{.interpreted-text
role="ref"})
`🔗<class_GLTFState_method_get_node_index>`{.interpreted-text
role="ref"}

Returns the index of the `GLTFNode<class_GLTFNode>`{.interpreted-text
role="ref"} corresponding to this Godot scene node. This is the inverse
of
`get_scene_node()<class_GLTFState_method_get_scene_node>`{.interpreted-text
role="ref"}. Useful during the export process.

\*\*Note:\*\* Not every Godot scene node will have a corresponding
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}, and not every
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"} will have a
scene node generated. If there is no
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"} index for this
scene node, `-1` is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_nodes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}\]
**get_nodes**() `🔗<class_GLTFState_method_get_nodes>`{.interpreted-text
role="ref"}

Returns an array of all `GLTFNode<class_GLTFNode>`{.interpreted-text
role="ref"}s in the glTF file. These are the nodes that
`GLTFNode.children<class_GLTFNode_property_children>`{.interpreted-text
role="ref"} and
`root_nodes<class_GLTFState_property_root_nodes>`{.interpreted-text
role="ref"} refer to. This includes nodes that may not be generated in
the Godot scene, or nodes that may generate multiple Godot scene nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_scene_node}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **get_scene_node**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GLTFState_method_get_scene_node>`{.interpreted-text
role="ref"}

Returns the Godot scene node that corresponds to the same index as the
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"} it was
generated from. This is the inverse of
`get_node_index()<class_GLTFState_method_get_node_index>`{.interpreted-text
role="ref"}. Useful during the import process.

\*\*Note:\*\* Not every `GLTFNode<class_GLTFNode>`{.interpreted-text
role="ref"} will have a scene node generated, and not every generated
scene node will have a corresponding
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}. If there is no
scene node for this `GLTFNode<class_GLTFNode>`{.interpreted-text
role="ref"} index, `null` is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_skeletons}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFSkeleton<class_GLTFSkeleton>`{.interpreted-text
role="ref"}\] **get_skeletons**()
`🔗<class_GLTFState_method_get_skeletons>`{.interpreted-text role="ref"}

Returns an array of all
`GLTFSkeleton<class_GLTFSkeleton>`{.interpreted-text role="ref"}s in the
glTF file. These are the skeletons that the
`GLTFNode.skeleton<class_GLTFNode_property_skeleton>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_skins}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFSkin<class_GLTFSkin>`{.interpreted-text role="ref"}\]
**get_skins**() `🔗<class_GLTFState_method_get_skins>`{.interpreted-text
role="ref"}

Returns an array of all `GLTFSkin<class_GLTFSkin>`{.interpreted-text
role="ref"}s in the glTF file. These are the skins that the
`GLTFNode.skin<class_GLTFNode_property_skin>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_texture_samplers}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFTextureSampler<class_GLTFTextureSampler>`{.interpreted-text
role="ref"}\] **get_texture_samplers**()
`🔗<class_GLTFState_method_get_texture_samplers>`{.interpreted-text
role="ref"}

Retrieves the array of texture samplers that are used by the textures
contained in the glTF.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_textures}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFTexture<class_GLTFTexture>`{.interpreted-text
role="ref"}\] **get_textures**()
`🔗<class_GLTFState_method_get_textures>`{.interpreted-text role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_unique_animation_names}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
**get_unique_animation_names**()
`🔗<class_GLTFState_method_get_unique_animation_names>`{.interpreted-text
role="ref"}

Returns an array of unique animation names. This is only used during the
import process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_get_unique_names}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
**get_unique_names**()
`🔗<class_GLTFState_method_get_unique_names>`{.interpreted-text
role="ref"}

Returns an array of unique node names. This is used in both the import
process and export process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_accessors}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_accessors**(accessors: `Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFAccessor<class_GLTFAccessor>`{.interpreted-text
role="ref"}\])
`🔗<class_GLTFState_method_set_accessors>`{.interpreted-text role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_additional_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
additional_data: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_GLTFState_method_set_additional_data>`{.interpreted-text
role="ref"}

Sets additional arbitrary data in this **GLTFState** instance. This can
be used to keep per-file state data in
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes, which is important because they are stateless.

The first argument should be the
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} name (does not have to match the extension name in the glTF
file), and the second argument can be anything you want.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_animations}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_animations**(animations: `Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFAnimation<class_GLTFAnimation>`{.interpreted-text
role="ref"}\])
`🔗<class_GLTFState_method_set_animations>`{.interpreted-text
role="ref"}

Sets the `GLTFAnimation<class_GLTFAnimation>`{.interpreted-text
role="ref"}s in the state. When importing, these will be generated as
animations in an
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
node. When exporting, these will be generated from Godot
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_buffer_views}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_buffer_views**(buffer_views:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFBufferView<class_GLTFBufferView>`{.interpreted-text
role="ref"}\])
`🔗<class_GLTFState_method_set_buffer_views>`{.interpreted-text
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

:::: {#class_GLTFState_method_set_cameras}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cameras**(cameras: `Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFCamera<class_GLTFCamera>`{.interpreted-text
role="ref"}\])
`🔗<class_GLTFState_method_set_cameras>`{.interpreted-text role="ref"}

Sets the `GLTFCamera<class_GLTFCamera>`{.interpreted-text role="ref"}s
in the state. These are the cameras that the
`GLTFNode.camera<class_GLTFNode_property_camera>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_handle_binary_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_handle_binary_image**(method: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GLTFState_method_set_handle_binary_image>`{.interpreted-text
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

:::: {#class_GLTFState_method_set_images}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_images**(images: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}\]) `🔗<class_GLTFState_method_set_images>`{.interpreted-text
role="ref"}

Sets the images in the state stored as an array of
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}s. This can be
used during export. These are the images that the
`GLTFTexture.src_image<class_GLTFTexture_property_src_image>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_lights}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_lights**(lights: `Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFLight<class_GLTFLight>`{.interpreted-text
role="ref"}\]) `🔗<class_GLTFState_method_set_lights>`{.interpreted-text
role="ref"}

Sets the `GLTFLight<class_GLTFLight>`{.interpreted-text role="ref"}s in
the state. These are the lights that the
`GLTFNode.light<class_GLTFNode_property_light>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_materials}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_materials**(materials: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Material<class_Material>`{.interpreted-text role="ref"}\])
`🔗<class_GLTFState_method_set_materials>`{.interpreted-text role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_meshes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_meshes**(meshes: `Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFMesh<class_GLTFMesh>`{.interpreted-text role="ref"}\])
`🔗<class_GLTFState_method_set_meshes>`{.interpreted-text role="ref"}

Sets the `GLTFMesh<class_GLTFMesh>`{.interpreted-text role="ref"}es in
the state. These are the meshes that the
`GLTFNode.mesh<class_GLTFNode_property_mesh>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_nodes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_nodes**(nodes: `Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}\])
`🔗<class_GLTFState_method_set_nodes>`{.interpreted-text role="ref"}

Sets the `GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}s in
the state. These are the nodes that
`GLTFNode.children<class_GLTFNode_property_children>`{.interpreted-text
role="ref"} and
`root_nodes<class_GLTFState_property_root_nodes>`{.interpreted-text
role="ref"} refer to. Some of the nodes set here may not be generated in
the Godot scene, or may generate multiple Godot scene nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_skeletons}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_skeletons**(skeletons: `Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFSkeleton<class_GLTFSkeleton>`{.interpreted-text
role="ref"}\])
`🔗<class_GLTFState_method_set_skeletons>`{.interpreted-text role="ref"}

Sets the `GLTFSkeleton<class_GLTFSkeleton>`{.interpreted-text
role="ref"}s in the state. These are the skeletons that the
`GLTFNode.skeleton<class_GLTFNode_property_skeleton>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_skins}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_skins**(skins: `Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFSkin<class_GLTFSkin>`{.interpreted-text role="ref"}\])
`🔗<class_GLTFState_method_set_skins>`{.interpreted-text role="ref"}

Sets the `GLTFSkin<class_GLTFSkin>`{.interpreted-text role="ref"}s in
the state. These are the skins that the
`GLTFNode.skin<class_GLTFNode_property_skin>`{.interpreted-text
role="ref"} index refers to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_texture_samplers}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_texture_samplers**(texture_samplers:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFTextureSampler<class_GLTFTextureSampler>`{.interpreted-text
role="ref"}\])
`🔗<class_GLTFState_method_set_texture_samplers>`{.interpreted-text
role="ref"}

Sets the array of texture samplers that are used by the textures
contained in the glTF.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_textures}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_textures**(textures: `Array<class_Array>`{.interpreted-text
role="ref"}\[`GLTFTexture<class_GLTFTexture>`{.interpreted-text
role="ref"}\])
`🔗<class_GLTFState_method_set_textures>`{.interpreted-text role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_unique_animation_names}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_unique_animation_names**(unique_animation_names:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\])
`🔗<class_GLTFState_method_set_unique_animation_names>`{.interpreted-text
role="ref"}

Sets the unique animation names in the state. This is only used during
the import process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFState_method_set_unique_names}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_unique_names**(unique_names:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\])
`🔗<class_GLTFState_method_set_unique_names>`{.interpreted-text
role="ref"}

Sets the unique node names in the state. This is used in both the import
process and export process.
