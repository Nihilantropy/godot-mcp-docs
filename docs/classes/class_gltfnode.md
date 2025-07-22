github_url
:   hide

# GLTFNode {#class_GLTFNode}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

glTF node class.

::: rst-class
classref-introduction-group
:::

## Description

Represents a glTF node. glTF nodes may have names, transforms, children
(other glTF nodes), and more specialized properties (represented by
their own classes).

glTF nodes generally exist inside of
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"} which
represents all data of a glTF file. Most of GLTFNode\'s properties are
indices of other data in the glTF file. You can extend a glTF node with
additional properties by using
`get_additional_data()<class_GLTFNode_method_get_additional_data>`{.interpreted-text
role="ref"} and
`set_additional_data()<class_GLTFNode_method_set_additional_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}
- [glTF scene and node
  spec](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_004_ScenesNodes.md")

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

:::: {#class_GLTFNode_property_camera}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **camera** = `-1`
`🔗<class_GLTFNode_property_camera>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_camera**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_camera**()

If this glTF node is a camera, the index of the
`GLTFCamera<class_GLTFCamera>`{.interpreted-text role="ref"} in the
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"} that
describes the camera\'s properties. If `-1`, this node is not a camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_children}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**children** = `PackedInt32Array()`
`🔗<class_GLTFNode_property_children>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_children**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_children**()

The indices of the child nodes in the
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}. If this glTF
node has no children, this will be an empty array.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_height}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **height** = `-1`
`🔗<class_GLTFNode_property_height>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_height**()

How deep into the node hierarchy this node is. A root node will have a
height of 0, its children will have a height of 1, and so on. If -1, the
height has not been calculated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_light}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **light** = `-1`
`🔗<class_GLTFNode_property_light>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_light**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_light**()

If this glTF node is a light, the index of the
`GLTFLight<class_GLTFLight>`{.interpreted-text role="ref"} in the
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"} that
describes the light\'s properties. If -1, this node is not a light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_mesh}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **mesh** = `-1`
`🔗<class_GLTFNode_property_mesh>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_mesh**()

If this glTF node is a mesh, the index of the
`GLTFMesh<class_GLTFMesh>`{.interpreted-text role="ref"} in the
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"} that
describes the mesh\'s properties. If -1, this node is not a mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_original_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **original_name** =
`""` `🔗<class_GLTFNode_property_original_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_original_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_original_name**()

The original name of the node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_parent}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **parent** = `-1`
`🔗<class_GLTFNode_property_parent>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_parent**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_parent**()

The index of the parent node in the
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"}. If -1, this
node is a root node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_position}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **position** =
`Vector3(0, 0, 0)`
`🔗<class_GLTFNode_property_position>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_position**()

The position of the glTF node relative to its parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_rotation}
::: rst-class
classref-property
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**rotation** = `Quaternion(0, 0, 0, 1)`
`🔗<class_GLTFNode_property_rotation>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation**(value:
  `Quaternion<class_Quaternion>`{.interpreted-text role="ref"})
- `Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
  **get_rotation**()

The rotation of the glTF node relative to its parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_scale}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **scale** =
`Vector3(1, 1, 1)` `🔗<class_GLTFNode_property_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scale**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_scale**()

The scale of the glTF node relative to its parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_skeleton}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **skeleton** = `-1`
`🔗<class_GLTFNode_property_skeleton>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_skeleton**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_skeleton**()

If this glTF node has a skeleton, the index of the
`GLTFSkeleton<class_GLTFSkeleton>`{.interpreted-text role="ref"} in the
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"} that
describes the skeleton\'s properties. If -1, this node does not have a
skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_skin}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **skin** = `-1`
`🔗<class_GLTFNode_property_skin>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_skin**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_skin**()

If this glTF node has a skin, the index of the
`GLTFSkin<class_GLTFSkin>`{.interpreted-text role="ref"} in the
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"} that
describes the skin\'s properties. If -1, this node does not have a skin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **visible** = `true`
`🔗<class_GLTFNode_property_visible>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_visible**()

If `true`, the GLTF node is visible. If `false`, the GLTF node is not
visible. This is translated to the
`Node3D.visible<class_Node3D_property_visible>`{.interpreted-text
role="ref"} property in the Godot scene, and is exported to
`KHR_node_visibility` when `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_property_xform}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} **xform**
= `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_GLTFNode_property_xform>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_xform**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_xform**()

The transform of the glTF node relative to its parent. This property is
usually unused since the position, rotation, and scale properties are
preferred.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFNode_method_append_child_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_child_index**(child_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_GLTFNode_method_append_child_index>`{.interpreted-text
role="ref"}

Appends the given child node index to the
`children<class_GLTFNode_property_children>`{.interpreted-text
role="ref"} array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_method_get_additional_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GLTFNode_method_get_additional_data>`{.interpreted-text
role="ref"}

Gets additional arbitrary data in this **GLTFNode** instance. This can
be used to keep per-node state data in
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

:::: {#class_GLTFNode_method_get_scene_node_path}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_scene_node_path**(gltf_state:
`GLTFState<class_GLTFState>`{.interpreted-text role="ref"},
handle_skeletons: `bool<class_bool>`{.interpreted-text role="ref"} =
true) `🔗<class_GLTFNode_method_get_scene_node_path>`{.interpreted-text
role="ref"}

Returns the `NodePath<class_NodePath>`{.interpreted-text role="ref"}
that this GLTF node will have in the Godot scene tree after being
imported. This is useful when importing glTF object model pointers with
`GLTFObjectModelProperty<class_GLTFObjectModelProperty>`{.interpreted-text
role="ref"}, for handling extensions such as `KHR_animation_pointer` or
`KHR_interactivity`.

If `handle_skeletons` is `true`, paths to skeleton bone glTF nodes will
be resolved properly. For example, a path that would be
`^"A/B/C/Bone1/Bone2/Bone3"` if `false` will become
`^"A/B/C/Skeleton3D:Bone3"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFNode_method_set_additional_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
additional_data: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_GLTFNode_method_set_additional_data>`{.interpreted-text
role="ref"}

Sets additional arbitrary data in this **GLTFNode** instance. This can
be used to keep per-node state data in
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes, which is important because they are stateless.

The first argument should be the
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} name (does not have to match the extension name in the glTF
file), and the second argument can be anything you want.
