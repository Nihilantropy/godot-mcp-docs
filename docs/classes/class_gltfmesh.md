github_url
:   hide

# GLTFMesh {#class_GLTFMesh}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

GLTFMesh represents a glTF mesh.

::: rst-class
classref-introduction-group
:::

## Description

GLTFMesh handles 3D mesh data imported from glTF files. It includes
properties for blend channels, blend weights, instance materials, and
the mesh itself.

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

:::: {#class_GLTFMesh_property_blend_weights}
::: rst-class
classref-property
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **blend_weights** = `PackedFloat32Array()`
`🔗<class_GLTFMesh_property_blend_weights>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_weights**(value:
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"})
- `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} **get_blend_weights**()

An array of floats representing the blend weights of the mesh.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFMesh_property_instance_materials}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Material<class_Material>`{.interpreted-text role="ref"}\]
**instance_materials** = `[]`
`🔗<class_GLTFMesh_property_instance_materials>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_instance_materials**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`Material<class_Material>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`Material<class_Material>`{.interpreted-text
  role="ref"}\] **get_instance_materials**()

An array of Material objects representing the materials used in the
mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFMesh_property_mesh}
::: rst-class
classref-property
:::
::::

`ImporterMesh<class_ImporterMesh>`{.interpreted-text role="ref"}
**mesh** `🔗<class_GLTFMesh_property_mesh>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh**(value:
  `ImporterMesh<class_ImporterMesh>`{.interpreted-text role="ref"})
- `ImporterMesh<class_ImporterMesh>`{.interpreted-text role="ref"}
  **get_mesh**()

The `ImporterMesh<class_ImporterMesh>`{.interpreted-text role="ref"}
object representing the mesh itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFMesh_property_original_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **original_name** =
`""` `🔗<class_GLTFMesh_property_original_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_original_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_original_name**()

The original name of the mesh.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFMesh_method_get_additional_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GLTFMesh_method_get_additional_data>`{.interpreted-text
role="ref"}

Gets additional arbitrary data in this **GLTFMesh** instance. This can
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

:::: {#class_GLTFMesh_method_set_additional_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
additional_data: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_GLTFMesh_method_set_additional_data>`{.interpreted-text
role="ref"}

Sets additional arbitrary data in this **GLTFMesh** instance. This can
be used to keep per-node state data in
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes, which is important because they are stateless.

The first argument should be the
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} name (does not have to match the extension name in the glTF
file), and the second argument can be anything you want.
