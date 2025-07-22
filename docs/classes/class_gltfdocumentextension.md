github_url
:   hide

# GLTFDocumentExtension {#class_GLTFDocumentExtension}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`GLTFDocumentExtensionConvertImporterMesh<class_GLTFDocumentExtensionConvertImporterMesh>`{.interpreted-text
role="ref"}

`GLTFDocument<class_GLTFDocument>`{.interpreted-text role="ref"}
extension class.

::: rst-class
classref-introduction-group
:::

## Description

Extends the functionality of the
`GLTFDocument<class_GLTFDocument>`{.interpreted-text role="ref"} class
by allowing you to run arbitrary code at various stages of glTF import
or export.

To use, make a new class extending GLTFDocumentExtension, override any
methods you need, make an instance of your class, and register it using
`GLTFDocument.register_gltf_document_extension()<class_GLTFDocument_method_register_gltf_document_extension>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Like GLTFDocument itself, all GLTFDocumentExtension
classes must be stateless in order to function properly. If you need to
store data, use the `set_additional_data` and `get_additional_data`
methods in `GLTFState<class_GLTFState>`{.interpreted-text role="ref"} or
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
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

## Method Descriptions

:::: {#class_GLTFDocumentExtension_private_method__convert_scene_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_convert_scene_node**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, gltf_node:
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}, scene_node:
`Node<class_Node>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__convert_scene_node>`{.interpreted-text
role="ref"}

Part of the export process. This method is run after
`_export_preflight()<class_GLTFDocumentExtension_private_method__export_preflight>`{.interpreted-text
role="ref"} and before
`_export_post_convert()<class_GLTFDocumentExtension_private_method__export_post_convert>`{.interpreted-text
role="ref"}.

Runs when converting the data from a Godot scene node. This method can
be used to process the Godot scene node data into a format that can be
used by
`_export_node()<class_GLTFDocumentExtension_private_method__export_node>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__export_node}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_node**(state: `GLTFState<class_GLTFState>`{.interpreted-text
role="ref"}, gltf_node: `GLTFNode<class_GLTFNode>`{.interpreted-text
role="ref"}, json: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, node: `Node<class_Node>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__export_node>`{.interpreted-text
role="ref"}

Part of the export process. This method is run after
`_get_saveable_image_formats()<class_GLTFDocumentExtension_private_method__get_saveable_image_formats>`{.interpreted-text
role="ref"} and before
`_export_post()<class_GLTFDocumentExtension_private_method__export_post>`{.interpreted-text
role="ref"}. If this **GLTFDocumentExtension** is used for exporting
images, this runs after
`_serialize_texture_json()<class_GLTFDocumentExtension_private_method__serialize_texture_json>`{.interpreted-text
role="ref"}.

This method can be used to modify the final JSON of each node. Data
should be primarily stored in `gltf_node` prior to serializing the JSON,
but the original Godot `Node<class_Node>`{.interpreted-text role="ref"}
is also provided if available. `node` may be `null` if not available,
such as when exporting glTF data not generated from a Godot scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__export_object_model_property}
::: rst-class
classref-method
:::
::::

`GLTFObjectModelProperty<class_GLTFObjectModelProperty>`{.interpreted-text
role="ref"} **\_export_object_model_property**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, node_path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"}, godot_node:
`Node<class_Node>`{.interpreted-text role="ref"}, gltf_node_index:
`int<class_int>`{.interpreted-text role="ref"}, target_object:
`Object<class_Object>`{.interpreted-text role="ref"}, target_depth:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__export_object_model_property>`{.interpreted-text
role="ref"}

Part of the export process. Allows GLTFDocumentExtension classes to
provide mappings for properties of nodes in the Godot scene tree, to
JSON pointers to glTF properties, as defined by the glTF object model.

Returns a
`GLTFObjectModelProperty<class_GLTFObjectModelProperty>`{.interpreted-text
role="ref"} instance that defines how the property should be mapped. If
your extension can\'t handle the property, return `null` or an instance
without any JSON pointers (see
`GLTFObjectModelProperty.has_json_pointers()<class_GLTFObjectModelProperty_method_has_json_pointers>`{.interpreted-text
role="ref"}). You should use
`GLTFObjectModelProperty.set_types()<class_GLTFObjectModelProperty_method_set_types>`{.interpreted-text
role="ref"} to set the types, and set the JSON pointer(s) using the
`GLTFObjectModelProperty.json_pointers<class_GLTFObjectModelProperty_property_json_pointers>`{.interpreted-text
role="ref"} property.

The parameters provide context for the property, including the NodePath,
the Godot node, the GLTF node index, and the target object. The
`target_object` will be equal to `godot_node` if no sub-object can be
found, otherwise it will point to a sub-object. For example, if the path
is `^"A/B/C/MeshInstance3D:mesh:surface_0/material:emission_intensity"`,
it will get the node, then the mesh, and then the material, so
`target_object` will be the `Material<class_Material>`{.interpreted-text
role="ref"} resource, and `target_depth` will be 2 because 2 levels were
traversed to get to the target.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__export_post}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_post**(state: `GLTFState<class_GLTFState>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__export_post>`{.interpreted-text
role="ref"}

Part of the export process. This method is run last, after all other
parts of the export process.

This method can be used to modify the final JSON of the generated glTF
file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__export_post_convert}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_post_convert**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, root:
`Node<class_Node>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__export_post_convert>`{.interpreted-text
role="ref"}

Part of the export process. This method is run after
`_convert_scene_node()<class_GLTFDocumentExtension_private_method__convert_scene_node>`{.interpreted-text
role="ref"} and before
`_export_preserialize()<class_GLTFDocumentExtension_private_method__export_preserialize>`{.interpreted-text
role="ref"}.

This method can be used to modify the converted node data structures
before serialization with any additional data from the scene tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__export_preflight}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_preflight**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, root:
`Node<class_Node>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__export_preflight>`{.interpreted-text
role="ref"}

Part of the export process. This method is run first, before all other
parts of the export process.

The return value is used to determine if this **GLTFDocumentExtension**
instance should be used for exporting a given glTF file. If
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"}, the export will use this **GLTFDocumentExtension**
instance. If not overridden,
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__export_preserialize}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_export_preserialize**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__export_preserialize>`{.interpreted-text
role="ref"}

Part of the export process. This method is run after
`_export_post_convert()<class_GLTFDocumentExtension_private_method__export_post_convert>`{.interpreted-text
role="ref"} and before
`_get_saveable_image_formats()<class_GLTFDocumentExtension_private_method__get_saveable_image_formats>`{.interpreted-text
role="ref"}.

This method can be used to alter the state before performing
serialization. It runs every time when generating a buffer with
`GLTFDocument.generate_buffer()<class_GLTFDocument_method_generate_buffer>`{.interpreted-text
role="ref"} or writing to the file system with
`GLTFDocument.write_to_filesystem()<class_GLTFDocument_method_write_to_filesystem>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__generate_scene_node}
::: rst-class
classref-method
:::
::::

`Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\_generate_scene_node**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, gltf_node:
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}, scene_parent:
`Node<class_Node>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__generate_scene_node>`{.interpreted-text
role="ref"}

Part of the import process. This method is run after
`_import_pre_generate()<class_GLTFDocumentExtension_private_method__import_pre_generate>`{.interpreted-text
role="ref"} and before
`_import_node()<class_GLTFDocumentExtension_private_method__import_node>`{.interpreted-text
role="ref"}.

Runs when generating a Godot scene node from a GLTFNode. The returned
node will be added to the scene tree. Multiple nodes can be generated in
this step if they are added as a child of the returned node.

\*\*Note:\*\* The `scene_parent` parameter may be `null` if this is the
single root node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__get_image_file_extension}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_image_file_extension**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__get_image_file_extension>`{.interpreted-text
role="ref"}

Returns the file extension to use for saving image data into, for
example, `".png"`. If defined, when this extension is used to handle
images, and the images are saved to a separate file, the image bytes
will be copied to a file with this extension. If this is set, there
should be a `ResourceImporter<class_ResourceImporter>`{.interpreted-text
role="ref"} class able to import the file. If not defined or empty,
Godot will save the image into a PNG file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__get_saveable_image_formats}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_saveable_image_formats**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__get_saveable_image_formats>`{.interpreted-text
role="ref"}

Part of the export process. This method is run after
`_convert_scene_node()<class_GLTFDocumentExtension_private_method__convert_scene_node>`{.interpreted-text
role="ref"} and before
`_export_node()<class_GLTFDocumentExtension_private_method__export_node>`{.interpreted-text
role="ref"}.

Returns an array of the image formats that can be saved/exported by this
extension. This extension will only be selected as the image exporter if
the `GLTFDocument<class_GLTFDocument>`{.interpreted-text role="ref"}\'s
`GLTFDocument.image_format<class_GLTFDocument_property_image_format>`{.interpreted-text
role="ref"} is in this array. If this **GLTFDocumentExtension** is
selected as the image exporter, one of the
`_save_image_at_path()<class_GLTFDocumentExtension_private_method__save_image_at_path>`{.interpreted-text
role="ref"} or
`_serialize_image_to_bytes()<class_GLTFDocumentExtension_private_method__serialize_image_to_bytes>`{.interpreted-text
role="ref"} methods will run next, otherwise
`_export_node()<class_GLTFDocumentExtension_private_method__export_node>`{.interpreted-text
role="ref"} will run next. If the format name contains `"Lossy"`, the
lossy quality slider will be displayed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__get_supported_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_supported_extensions**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__get_supported_extensions>`{.interpreted-text
role="ref"}

Part of the import process. This method is run after
`_import_preflight()<class_GLTFDocumentExtension_private_method__import_preflight>`{.interpreted-text
role="ref"} and before
`_parse_node_extensions()<class_GLTFDocumentExtension_private_method__parse_node_extensions>`{.interpreted-text
role="ref"}.

Returns an array of the glTF extensions supported by this
GLTFDocumentExtension class. This is used to validate if a glTF file
with required extensions can be loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__import_node}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_import_node**(state: `GLTFState<class_GLTFState>`{.interpreted-text
role="ref"}, gltf_node: `GLTFNode<class_GLTFNode>`{.interpreted-text
role="ref"}, json: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, node: `Node<class_Node>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__import_node>`{.interpreted-text
role="ref"}

Part of the import process. This method is run after
`_generate_scene_node()<class_GLTFDocumentExtension_private_method__generate_scene_node>`{.interpreted-text
role="ref"} and before
`_import_post()<class_GLTFDocumentExtension_private_method__import_post>`{.interpreted-text
role="ref"}.

This method can be used to make modifications to each of the generated
Godot scene nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__import_object_model_property}
::: rst-class
classref-method
:::
::::

`GLTFObjectModelProperty<class_GLTFObjectModelProperty>`{.interpreted-text
role="ref"} **\_import_object_model_property**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"},
split_json_pointer:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, partial_paths: `Array<class_Array>`{.interpreted-text
role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__import_object_model_property>`{.interpreted-text
role="ref"}

Part of the import process. Allows GLTFDocumentExtension classes to
provide mappings for JSON pointers to glTF properties, as defined by the
glTF object model, to properties of nodes in the Godot scene tree.

Returns a
`GLTFObjectModelProperty<class_GLTFObjectModelProperty>`{.interpreted-text
role="ref"} instance that defines how the property should be mapped. If
your extension can\'t handle the property, return `null` or an instance
without any NodePaths (see
`GLTFObjectModelProperty.has_node_paths()<class_GLTFObjectModelProperty_method_has_node_paths>`{.interpreted-text
role="ref"}). You should use
`GLTFObjectModelProperty.set_types()<class_GLTFObjectModelProperty_method_set_types>`{.interpreted-text
role="ref"} to set the types, and
`GLTFObjectModelProperty.append_path_to_property()<class_GLTFObjectModelProperty_method_append_path_to_property>`{.interpreted-text
role="ref"} function is useful for most simple cases.

In many cases, `partial_paths` will contain the start of a path,
allowing the extension to complete the path. For example, for
`/nodes/3/extensions/MY_ext/prop`, Godot will pass you a NodePath that
leads to node 3, so the GLTFDocumentExtension class only needs to
resolve the last `MY_ext/prop` part of the path. In this example, the
extension should check
`split.size() > 4 and split[0] == "nodes" and split[2] == "extensions" and split[3] == "MY_ext"`
at the start of the function to check if this JSON pointer applies to
it, then it can use `partial_paths` and handle `split[4]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__import_post}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_import_post**(state: `GLTFState<class_GLTFState>`{.interpreted-text
role="ref"}, root: `Node<class_Node>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__import_post>`{.interpreted-text
role="ref"}

Part of the import process. This method is run last, after all other
parts of the import process.

This method can be used to modify the final Godot scene generated by the
import process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__import_post_parse}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_import_post_parse**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__import_post_parse>`{.interpreted-text
role="ref"}

Part of the import process. This method is run after
`_parse_node_extensions()<class_GLTFDocumentExtension_private_method__parse_node_extensions>`{.interpreted-text
role="ref"} and before
`_import_pre_generate()<class_GLTFDocumentExtension_private_method__import_pre_generate>`{.interpreted-text
role="ref"}.

This method can be used to modify any of the data imported so far after
parsing each node, but before generating the scene or any of its nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__import_pre_generate}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_import_pre_generate**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__import_pre_generate>`{.interpreted-text
role="ref"}

Part of the import process. This method is run after
`_import_post_parse()<class_GLTFDocumentExtension_private_method__import_post_parse>`{.interpreted-text
role="ref"} and before
`_generate_scene_node()<class_GLTFDocumentExtension_private_method__generate_scene_node>`{.interpreted-text
role="ref"}.

This method can be used to modify or read from any of the processed data
structures, before generating the nodes and then running the final
per-node import step.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__import_preflight}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_import_preflight**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, extensions:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__import_preflight>`{.interpreted-text
role="ref"}

Part of the import process. This method is run first, before all other
parts of the import process.

The return value is used to determine if this **GLTFDocumentExtension**
instance should be used for importing a given glTF file. If
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"}, the import will use this **GLTFDocumentExtension**
instance. If not overridden,
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__parse_image_data}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_parse_image_data**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, image_data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
mime_type: `String<class_String>`{.interpreted-text role="ref"},
ret_image: `Image<class_Image>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__parse_image_data>`{.interpreted-text
role="ref"}

Part of the import process. This method is run after
`_parse_node_extensions()<class_GLTFDocumentExtension_private_method__parse_node_extensions>`{.interpreted-text
role="ref"} and before
`_parse_texture_json()<class_GLTFDocumentExtension_private_method__parse_texture_json>`{.interpreted-text
role="ref"}.

Runs when parsing image data from a glTF file. The data could be sourced
from a separate file, a URI, or a buffer, and then is passed as a byte
array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__parse_node_extensions}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_parse_node_extensions**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, gltf_node:
`GLTFNode<class_GLTFNode>`{.interpreted-text role="ref"}, extensions:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__parse_node_extensions>`{.interpreted-text
role="ref"}

Part of the import process. This method is run after
`_get_supported_extensions()<class_GLTFDocumentExtension_private_method__get_supported_extensions>`{.interpreted-text
role="ref"} and before
`_import_post_parse()<class_GLTFDocumentExtension_private_method__import_post_parse>`{.interpreted-text
role="ref"}.

Runs when parsing the node extensions of a GLTFNode. This method can be
used to process the extension JSON data into a format that can be used
by
`_generate_scene_node()<class_GLTFDocumentExtension_private_method__generate_scene_node>`{.interpreted-text
role="ref"}. The return value should be a member of the
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__parse_texture_json}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_parse_texture_json**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"},
texture_json: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, ret_gltf_texture:
`GLTFTexture<class_GLTFTexture>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__parse_texture_json>`{.interpreted-text
role="ref"}

Part of the import process. This method is run after
`_parse_image_data()<class_GLTFDocumentExtension_private_method__parse_image_data>`{.interpreted-text
role="ref"} and before
`_generate_scene_node()<class_GLTFDocumentExtension_private_method__generate_scene_node>`{.interpreted-text
role="ref"}.

Runs when parsing the texture JSON from the glTF textures array. This
can be used to set the source image index to use as the texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__save_image_at_path}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_save_image_at_path**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, image:
`Image<class_Image>`{.interpreted-text role="ref"}, file_path:
`String<class_String>`{.interpreted-text role="ref"}, image_format:
`String<class_String>`{.interpreted-text role="ref"}, lossy_quality:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__save_image_at_path>`{.interpreted-text
role="ref"}

Part of the export process. This method is run after
`_get_saveable_image_formats()<class_GLTFDocumentExtension_private_method__get_saveable_image_formats>`{.interpreted-text
role="ref"} and before
`_serialize_texture_json()<class_GLTFDocumentExtension_private_method__serialize_texture_json>`{.interpreted-text
role="ref"}.

This method is run when saving images separately from the glTF file.
When images are embedded,
`_serialize_image_to_bytes()<class_GLTFDocumentExtension_private_method__serialize_image_to_bytes>`{.interpreted-text
role="ref"} runs instead. Note that these methods only run when this
**GLTFDocumentExtension** is selected as the image exporter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__serialize_image_to_bytes}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**\_serialize_image_to_bytes**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}, image:
`Image<class_Image>`{.interpreted-text role="ref"}, image_dict:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"},
image_format: `String<class_String>`{.interpreted-text role="ref"},
lossy_quality: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__serialize_image_to_bytes>`{.interpreted-text
role="ref"}

Part of the export process. This method is run after
`_get_saveable_image_formats()<class_GLTFDocumentExtension_private_method__get_saveable_image_formats>`{.interpreted-text
role="ref"} and before
`_serialize_texture_json()<class_GLTFDocumentExtension_private_method__serialize_texture_json>`{.interpreted-text
role="ref"}.

This method is run when embedding images in the glTF file. When images
are saved separately,
`_save_image_at_path()<class_GLTFDocumentExtension_private_method__save_image_at_path>`{.interpreted-text
role="ref"} runs instead. Note that these methods only run when this
**GLTFDocumentExtension** is selected as the image exporter.

This method must set the image MIME type in the `image_dict` with the
`"mimeType"` key. For example, for a PNG image, it would be set to
`"image/png"`. The return value must be a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
containing the image data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFDocumentExtension_private_method__serialize_texture_json}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_serialize_texture_json**(state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"},
texture_json: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, gltf_texture:
`GLTFTexture<class_GLTFTexture>`{.interpreted-text role="ref"},
image_format: `String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFDocumentExtension_private_method__serialize_texture_json>`{.interpreted-text
role="ref"}

Part of the export process. This method is run after
`_save_image_at_path()<class_GLTFDocumentExtension_private_method__save_image_at_path>`{.interpreted-text
role="ref"} or
`_serialize_image_to_bytes()<class_GLTFDocumentExtension_private_method__serialize_image_to_bytes>`{.interpreted-text
role="ref"}, and before
`_export_node()<class_GLTFDocumentExtension_private_method__export_node>`{.interpreted-text
role="ref"}. Note that this method only runs when this
**GLTFDocumentExtension** is selected as the image exporter.

This method can be used to set up the extensions for the texture JSON by
editing `texture_json`. The extension must also be added as used
extension with
`GLTFState.add_used_extension()<class_GLTFState_method_add_used_extension>`{.interpreted-text
role="ref"}, be sure to set `required` to `true` if you are not
providing a fallback.
