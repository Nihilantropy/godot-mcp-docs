github_url
:   hide

# GLTFPhysicsShape {#class_GLTFPhysicsShape}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a glTF physics shape.

::: rst-class
classref-introduction-group
:::

## Description

Represents a physics shape as defined by the `OMI_physics_shape` or
`OMI_collider` glTF extensions. This class is an intermediary between
the glTF data and Godot\'s nodes, and it\'s abstracted in a way that
allows adding support for different glTF physics extensions in the
future.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}
- [OMI_physics_shape glTF
  extension](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_shape)
- [OMI_collider glTF
  extension](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/Archived/OMI_collider)

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

:::: {#class_GLTFPhysicsShape_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `2.0`
`🔗<class_GLTFPhysicsShape_property_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

The height of the shape, in meters. This is only used when the shape
type is `"capsule"` or `"cylinder"`. This value should not be negative,
and for `"capsule"` it should be at least twice the radius.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_property_importer_mesh}
::: rst-class
classref-property
:::
::::

`ImporterMesh<class_ImporterMesh>`{.interpreted-text role="ref"}
**importer_mesh**
`🔗<class_GLTFPhysicsShape_property_importer_mesh>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_importer_mesh**(value:
  `ImporterMesh<class_ImporterMesh>`{.interpreted-text role="ref"})
- `ImporterMesh<class_ImporterMesh>`{.interpreted-text role="ref"}
  **get_importer_mesh**()

The `ImporterMesh<class_ImporterMesh>`{.interpreted-text role="ref"}
resource of the shape. This is only used when the shape type is `"hull"`
(convex hull) or `"trimesh"` (concave trimesh).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_property_is_trigger}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_trigger** =
`false`
`🔗<class_GLTFPhysicsShape_property_is_trigger>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_is_trigger**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_is_trigger**()

If `true`, indicates that this shape is a trigger. For Godot, this means
that the shape should be a child of an
`Area3D<class_Area3D>`{.interpreted-text role="ref"} node.

This is the only variable not used in the
`to_node()<class_GLTFPhysicsShape_method_to_node>`{.interpreted-text
role="ref"} method, it\'s intended to be used alongside when deciding
where to add the generated node as a child.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_property_mesh_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **mesh_index** = `-1`
`🔗<class_GLTFPhysicsShape_property_mesh_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh_index**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_mesh_index**()

The index of the shape\'s mesh in the glTF file. This is only used when
the shape type is `"hull"` (convex hull) or `"trimesh"` (concave
trimesh).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_GLTFPhysicsShape_property_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The radius of the shape, in meters. This is only used when the shape
type is `"capsule"`, `"cylinder"`, or `"sphere"`. This value should not
be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_property_shape_type}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **shape_type** =
`""` `🔗<class_GLTFPhysicsShape_property_shape_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape_type**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_shape_type**()

The type of shape this shape represents. Valid values are `"box"`,
`"capsule"`, `"cylinder"`, `"sphere"`, `"hull"`, and `"trimesh"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(1, 1, 1)`
`🔗<class_GLTFPhysicsShape_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The size of the shape, in meters. This is only used when the shape type
is `"box"`, and it represents the `"diameter"` of the box. This value
should not be negative.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFPhysicsShape_method_from_dictionary}
::: rst-class
classref-method
:::
::::

`GLTFPhysicsShape<class_GLTFPhysicsShape>`{.interpreted-text role="ref"}
**from_dictionary**(dictionary:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFPhysicsShape_method_from_dictionary>`{.interpreted-text
role="ref"}

Creates a new GLTFPhysicsShape instance by parsing the given
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_method_from_node}
::: rst-class
classref-method
:::
::::

`GLTFPhysicsShape<class_GLTFPhysicsShape>`{.interpreted-text role="ref"}
**from_node**(shape_node:
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFPhysicsShape_method_from_node>`{.interpreted-text
role="ref"}

Creates a new GLTFPhysicsShape instance from the given Godot
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_method_from_resource}
::: rst-class
classref-method
:::
::::

`GLTFPhysicsShape<class_GLTFPhysicsShape>`{.interpreted-text role="ref"}
**from_resource**(shape_resource:
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFPhysicsShape_method_from_resource>`{.interpreted-text
role="ref"}

Creates a new GLTFPhysicsShape instance from the given Godot
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_method_to_dictionary}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**to_dictionary**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFPhysicsShape_method_to_dictionary>`{.interpreted-text
role="ref"}

Serializes this GLTFPhysicsShape instance into a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} in the
format defined by `OMI_physics_shape`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_method_to_node}
::: rst-class
classref-method
:::
::::

`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
**to_node**(cache_shapes: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_GLTFPhysicsShape_method_to_node>`{.interpreted-text
role="ref"}

Converts this GLTFPhysicsShape instance into a Godot
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFPhysicsShape_method_to_resource}
::: rst-class
classref-method
:::
::::

`Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**to_resource**(cache_shapes: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_GLTFPhysicsShape_method_to_resource>`{.interpreted-text
role="ref"}

Converts this GLTFPhysicsShape instance into a Godot
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} resource.
