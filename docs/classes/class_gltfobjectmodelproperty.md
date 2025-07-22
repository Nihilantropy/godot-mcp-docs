github_url
:   hide

# GLTFObjectModelProperty {#class_GLTFObjectModelProperty}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Describes how to access a property as defined in the glTF object model.

::: rst-class
classref-introduction-group
:::

## Description

GLTFObjectModelProperty defines a mapping between a property in the glTF
object model and a NodePath in the Godot scene tree. This can be used to
animate properties in a glTF file using the `KHR_animation_pointer`
extension, or to access them through an engine-agnostic script such as a
behavior graph as defined by the `KHR_interactivity` extension.

The glTF property is identified by JSON pointer(s) stored in
`json_pointers<class_GLTFObjectModelProperty_property_json_pointers>`{.interpreted-text
role="ref"}, while the Godot property it maps to is defined by
`node_paths<class_GLTFObjectModelProperty_property_node_paths>`{.interpreted-text
role="ref"}. In most cases
`json_pointers<class_GLTFObjectModelProperty_property_json_pointers>`{.interpreted-text
role="ref"} and
`node_paths<class_GLTFObjectModelProperty_property_node_paths>`{.interpreted-text
role="ref"} will each only have one item, but in some cases a single
glTF JSON pointer will map to multiple Godot properties, or a single
Godot property will be mapped to multiple glTF JSON pointers, or it
might be a many-to-many relationship.

`Expression<class_Expression>`{.interpreted-text role="ref"} objects can
be used to define conversions between the data, such as when glTF
defines an angle in radians and Godot uses degrees. The
`object_model_type<class_GLTFObjectModelProperty_property_object_model_type>`{.interpreted-text
role="ref"} property defines the type of data stored in the glTF file as
defined by the object model, see
`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} for possible values.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [GLTF Object
  Model](https://github.com/KhronosGroup/glTF/blob/main/specification/2.0/ObjectModel.adoc)
- [KHR_animation_pointer GLTF
  extension](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_animation_pointer)

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

## Enumerations

:::: {#enum_GLTFObjectModelProperty_GLTFObjectModelType}
::: rst-class
classref-enumeration
:::
::::

enum **GLTFObjectModelType**:
`🔗<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"}

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_UNKNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_UNKNOWN** = `0`

Unknown or not set object model type. If the object model type is set to
this value, the real type still needs to be determined.

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_BOOL}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_BOOL** = `1`

Object model type \"bool\". Represented in the glTF JSON as a boolean,
and encoded in a `GLTFAccessor<class_GLTFAccessor>`{.interpreted-text
role="ref"} as \"SCALAR\". When encoded in an accessor, a value of `0`
is `false`, and any other value is `true`.

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_FLOAT** = `2`

Object model type \"float\". Represented in the glTF JSON as a number,
and encoded in a `GLTFAccessor<class_GLTFAccessor>`{.interpreted-text
role="ref"} as \"SCALAR\".

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_FLOAT_ARRAY** = `3`

Object model type \"float\[\]\". Represented in the glTF JSON as an
array of numbers, and encoded in a
`GLTFAccessor<class_GLTFAccessor>`{.interpreted-text role="ref"} as
\"SCALAR\".

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT2}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_FLOAT2** = `4`

Object model type \"float2\". Represented in the glTF JSON as an array
of two numbers, and encoded in a
`GLTFAccessor<class_GLTFAccessor>`{.interpreted-text role="ref"} as
\"VEC2\".

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT3}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_FLOAT3** = `5`

Object model type \"float3\". Represented in the glTF JSON as an array
of three numbers, and encoded in a
`GLTFAccessor<class_GLTFAccessor>`{.interpreted-text role="ref"} as
\"VEC3\".

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT4}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_FLOAT4** = `6`

Object model type \"float4\". Represented in the glTF JSON as an array
of four numbers, and encoded in a
`GLTFAccessor<class_GLTFAccessor>`{.interpreted-text role="ref"} as
\"VEC4\".

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT2X2}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_FLOAT2X2** = `7`

Object model type \"float2x2\". Represented in the glTF JSON as an array
of four numbers, and encoded in a
`GLTFAccessor<class_GLTFAccessor>`{.interpreted-text role="ref"} as
\"MAT2\".

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT3X3}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_FLOAT3X3** = `8`

Object model type \"float3x3\". Represented in the glTF JSON as an array
of nine numbers, and encoded in a
`GLTFAccessor<class_GLTFAccessor>`{.interpreted-text role="ref"} as
\"MAT3\".

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_FLOAT4X4}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_FLOAT4X4** = `9`

Object model type \"float4x4\". Represented in the glTF JSON as an array
of sixteen numbers, and encoded in a
`GLTFAccessor<class_GLTFAccessor>`{.interpreted-text role="ref"} as
\"MAT4\".

:::: {#class_GLTFObjectModelProperty_constant_GLTF_OBJECT_MODEL_TYPE_INT}
::: rst-class
classref-enumeration-constant
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **GLTF_OBJECT_MODEL_TYPE_INT** = `10`

Object model type \"int\". Represented in the glTF JSON as a number, and
encoded in a `GLTFAccessor<class_GLTFAccessor>`{.interpreted-text
role="ref"} as \"SCALAR\". The range of values is limited to signed
integers. For `KHR_interactivity`, only 32-bit integers are supported.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GLTFObjectModelProperty_property_gltf_to_godot_expression}
::: rst-class
classref-property
:::
::::

`Expression<class_Expression>`{.interpreted-text role="ref"}
**gltf_to_godot_expression**
`🔗<class_GLTFObjectModelProperty_property_gltf_to_godot_expression>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gltf_to_godot_expression**(value:
  `Expression<class_Expression>`{.interpreted-text role="ref"})
- `Expression<class_Expression>`{.interpreted-text role="ref"}
  **get_gltf_to_godot_expression**()

If set, this `Expression<class_Expression>`{.interpreted-text
role="ref"} will be used to convert the property value from the glTF
object model to the value expected by the Godot property. This is useful
when the glTF object model uses a different unit system, or when the
data needs to be transformed in some way. If `null`, the value will be
copied as-is.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_property_godot_to_gltf_expression}
::: rst-class
classref-property
:::
::::

`Expression<class_Expression>`{.interpreted-text role="ref"}
**godot_to_gltf_expression**
`🔗<class_GLTFObjectModelProperty_property_godot_to_gltf_expression>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_godot_to_gltf_expression**(value:
  `Expression<class_Expression>`{.interpreted-text role="ref"})
- `Expression<class_Expression>`{.interpreted-text role="ref"}
  **get_godot_to_gltf_expression**()

If set, this `Expression<class_Expression>`{.interpreted-text
role="ref"} will be used to convert the property value from the Godot
property to the value expected by the glTF object model. This is useful
when the glTF object model uses a different unit system, or when the
data needs to be transformed in some way. If `null`, the value will be
copied as-is.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_property_json_pointers}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}\] **json_pointers** = `[]`
`🔗<class_GLTFObjectModelProperty_property_json_pointers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_json_pointers**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"}\] **get_json_pointers**()

The glTF object model JSON pointers used to identify the property in the
glTF object model. In most cases, there will be only one item in this
array, but specific cases may require multiple pointers. The items are
themselves arrays which represent the JSON pointer split into its
components.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_property_node_paths}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text role="ref"}\]
**node_paths** = `[]`
`🔗<class_GLTFObjectModelProperty_property_node_paths>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_node_paths**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\] **get_node_paths**()

An array of `NodePath<class_NodePath>`{.interpreted-text role="ref"}s
that point to a property, or multiple properties, in the Godot scene
tree. On import, this will either be set by
`GLTFDocument<class_GLTFDocument>`{.interpreted-text role="ref"}, or by
a `GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} class. For simple cases, use
`append_path_to_property()<class_GLTFObjectModelProperty_method_append_path_to_property>`{.interpreted-text
role="ref"} to add properties to this array.

In most cases
`node_paths<class_GLTFObjectModelProperty_property_node_paths>`{.interpreted-text
role="ref"} will only have one item, but in some cases a single glTF
JSON pointer will map to multiple Godot properties. For example, a
`GLTFCamera<class_GLTFCamera>`{.interpreted-text role="ref"} or
`GLTFLight<class_GLTFLight>`{.interpreted-text role="ref"} used on
multiple glTF nodes will be represented by multiple Godot nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_property_object_model_type}
::: rst-class
classref-property
:::
::::

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} **object_model_type** = `0`
`🔗<class_GLTFObjectModelProperty_property_object_model_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_object_model_type**(value:
  `GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
  role="ref"})
- `GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
  role="ref"} **get_object_model_type**()

The type of data stored in the glTF file as defined by the object model.
This is a superset of the available accessor types, and determines the
accessor type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_property_variant_type}
::: rst-class
classref-property
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **variant_type** = `0`
`🔗<class_GLTFObjectModelProperty_property_variant_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_variant_type**(value:
  `Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
  role="ref"})
- `Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
  role="ref"} **get_variant_type**()

The type of data stored in the Godot property. This is the type of the
property that the
`node_paths<class_GLTFObjectModelProperty_property_node_paths>`{.interpreted-text
role="ref"} point to.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFObjectModelProperty_method_append_node_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_node_path**(node_path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_GLTFObjectModelProperty_method_append_node_path>`{.interpreted-text
role="ref"}

Appends a `NodePath<class_NodePath>`{.interpreted-text role="ref"} to
`node_paths<class_GLTFObjectModelProperty_property_node_paths>`{.interpreted-text
role="ref"}. This can be used by
`GLTFDocumentExtension<class_GLTFDocumentExtension>`{.interpreted-text
role="ref"} classes to define how a glTF object model property maps to a
Godot property, or multiple Godot properties. Prefer using
`append_path_to_property()<class_GLTFObjectModelProperty_method_append_path_to_property>`{.interpreted-text
role="ref"} for simple cases. Be sure to also call
`set_types()<class_GLTFObjectModelProperty_method_set_types>`{.interpreted-text
role="ref"} once (the order does not matter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_method_append_path_to_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_path_to_property**(node_path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"}, prop_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GLTFObjectModelProperty_method_append_path_to_property>`{.interpreted-text
role="ref"}

High-level wrapper over
`append_node_path()<class_GLTFObjectModelProperty_method_append_node_path>`{.interpreted-text
role="ref"} that handles the most common cases. It constructs a new
`NodePath<class_NodePath>`{.interpreted-text role="ref"} using
`node_path` as a base and appends `prop_name` to the subpath. Be sure to
also call
`set_types()<class_GLTFObjectModelProperty_method_set_types>`{.interpreted-text
role="ref"} once (the order does not matter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_method_get_accessor_type}
::: rst-class
classref-method
:::
::::

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>`{.interpreted-text
role="ref"} **get_accessor_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFObjectModelProperty_method_get_accessor_type>`{.interpreted-text
role="ref"}

The GLTF accessor type associated with this property\'s
`object_model_type<class_GLTFObjectModelProperty_property_object_model_type>`{.interpreted-text
role="ref"}. See
`GLTFAccessor.accessor_type<class_GLTFAccessor_property_accessor_type>`{.interpreted-text
role="ref"} for possible values, and see
`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"} for how the object model type maps to accessor types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_method_has_json_pointers}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_json_pointers**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFObjectModelProperty_method_has_json_pointers>`{.interpreted-text
role="ref"}

Returns `true` if
`json_pointers<class_GLTFObjectModelProperty_property_json_pointers>`{.interpreted-text
role="ref"} is not empty. This is used during export to determine if a
**GLTFObjectModelProperty** can handle converting a Godot property to a
glTF object model property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_method_has_node_paths}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_node_paths**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFObjectModelProperty_method_has_node_paths>`{.interpreted-text
role="ref"}

Returns `true` if
`node_paths<class_GLTFObjectModelProperty_property_node_paths>`{.interpreted-text
role="ref"} is not empty. This is used during import to determine if a
**GLTFObjectModelProperty** can handle converting a glTF object model
property to a Godot property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFObjectModelProperty_method_set_types}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_types**(variant_type:
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"}, obj_model_type:
`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`{.interpreted-text
role="ref"})
`🔗<class_GLTFObjectModelProperty_method_set_types>`{.interpreted-text
role="ref"}

Sets the
`variant_type<class_GLTFObjectModelProperty_property_variant_type>`{.interpreted-text
role="ref"} and
`object_model_type<class_GLTFObjectModelProperty_property_object_model_type>`{.interpreted-text
role="ref"} properties. This is a convenience method to set both
properties at once, since they are almost always known at the same time.
This method should be called once. Calling it again with the same values
will have no effect.
