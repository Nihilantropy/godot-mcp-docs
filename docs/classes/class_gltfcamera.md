github_url
:   hide

# GLTFCamera {#class_GLTFCamera}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a glTF camera.

::: rst-class
classref-introduction-group
:::

## Description

Represents a camera as defined by the base glTF spec.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}
- [glTF camera detailed
  specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera)
- [glTF camera spec and example
  file](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_015_SimpleCameras.md)

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

:::: {#class_GLTFCamera_property_depth_far}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth_far** =
`4000.0` `🔗<class_GLTFCamera_property_depth_far>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_far**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_depth_far**()

The distance to the far culling boundary for this camera relative to its
local Z axis, in meters. This maps to glTF\'s `zfar` property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFCamera_property_depth_near}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth_near** =
`0.05` `🔗<class_GLTFCamera_property_depth_near>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_near**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_depth_near**()

The distance to the near culling boundary for this camera relative to
its local Z axis, in meters. This maps to glTF\'s `znear` property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFCamera_property_fov}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fov** = `1.3089969`
`🔗<class_GLTFCamera_property_fov>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fov**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_fov**()

The FOV of the camera. This class and glTF define the camera FOV in
radians, while Godot uses degrees. This maps to glTF\'s `yfov` property.
This value is only used for perspective cameras, when
`perspective<class_GLTFCamera_property_perspective>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFCamera_property_perspective}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **perspective** =
`true` `🔗<class_GLTFCamera_property_perspective>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_perspective**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_perspective**()

If `true`, the camera is in perspective mode. Otherwise, the camera is
in orthographic/orthogonal mode. This maps to glTF\'s camera `type`
property. See
`Camera3D.projection<class_Camera3D_property_projection>`{.interpreted-text
role="ref"} and the glTF spec for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFCamera_property_size_mag}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **size_mag** = `0.5`
`🔗<class_GLTFCamera_property_size_mag>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size_mag**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_size_mag**()

The size of the camera. This class and glTF define the camera size
magnitude as a radius in meters, while Godot defines it as a diameter in
meters. This maps to glTF\'s `ymag` property. This value is only used
for orthographic/orthogonal cameras, when
`perspective<class_GLTFCamera_property_perspective>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFCamera_method_from_dictionary}
::: rst-class
classref-method
:::
::::

`GLTFCamera<class_GLTFCamera>`{.interpreted-text role="ref"}
**from_dictionary**(dictionary:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFCamera_method_from_dictionary>`{.interpreted-text
role="ref"}

Creates a new GLTFCamera instance by parsing the given
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFCamera_method_from_node}
::: rst-class
classref-method
:::
::::

`GLTFCamera<class_GLTFCamera>`{.interpreted-text role="ref"}
**from_node**(camera_node: `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_GLTFCamera_method_from_node>`{.interpreted-text
role="ref"}

Create a new GLTFCamera instance from the given Godot
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFCamera_method_to_dictionary}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**to_dictionary**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFCamera_method_to_dictionary>`{.interpreted-text
role="ref"}

Serializes this GLTFCamera instance into a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFCamera_method_to_node}
::: rst-class
classref-method
:::
::::

`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} **to_node**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_GLTFCamera_method_to_node>`{.interpreted-text
role="ref"}

Converts this GLTFCamera instance into a Godot
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} node.
