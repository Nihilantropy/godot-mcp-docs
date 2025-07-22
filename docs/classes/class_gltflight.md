github_url
:   hide

# GLTFLight {#class_GLTFLight}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a glTF light.

::: rst-class
classref-introduction-group
:::

## Description

Represents a light as defined by the `KHR_lights_punctual` glTF
extension.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
  role="doc"}
- [KHR_lights_punctual glTF extension
  spec](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_lights_punctual)

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

:::: {#class_GLTFLight_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(1, 1, 1, 1)`
`🔗<class_GLTFLight_property_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

The `Color<class_Color>`{.interpreted-text role="ref"} of the light in
linear space. Defaults to white. A black color causes the light to have
no effect.

This value is linear to match glTF, but will be converted to nonlinear
sRGB when creating a Godot `Light3D<class_Light3D>`{.interpreted-text
role="ref"} node upon import, or converted to linear when exporting a
Godot `Light3D<class_Light3D>`{.interpreted-text role="ref"} to glTF.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFLight_property_inner_cone_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **inner_cone_angle**
= `0.0`
`🔗<class_GLTFLight_property_inner_cone_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inner_cone_angle**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_inner_cone_angle**()

The inner angle of the cone in a spotlight. Must be less than or equal
to the outer cone angle.

Within this angle, the light is at full brightness. Between the inner
and outer cone angles, there is a transition from full brightness to
zero brightness. When creating a Godot
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}, the
ratio between the inner and outer cone angles is used to calculate the
attenuation of the light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFLight_property_intensity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **intensity** = `1.0`
`🔗<class_GLTFLight_property_intensity>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_intensity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_intensity**()

The intensity of the light. This is expressed in candelas (lumens per
steradian) for point and spot lights, and lux (lumens per m²) for
directional lights. When creating a Godot light, this value is converted
to a unitless multiplier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFLight_property_light_type}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **light_type** =
`""` `🔗<class_GLTFLight_property_light_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_light_type**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_light_type**()

The type of the light. The values accepted by Godot are \"point\",
\"spot\", and \"directional\", which correspond to Godot\'s
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"},
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}, and
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"} respectively.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFLight_property_outer_cone_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **outer_cone_angle**
= `0.7853982`
`🔗<class_GLTFLight_property_outer_cone_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outer_cone_angle**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_outer_cone_angle**()

The outer angle of the cone in a spotlight. Must be greater than or
equal to the inner angle.

At this angle, the light drops off to zero brightness. Between the inner
and outer cone angles, there is a transition from full brightness to
zero brightness. If this angle is a half turn, then the spotlight emits
in all directions. When creating a Godot
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}, the
outer cone angle is used as the angle of the spotlight.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFLight_property_range}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **range** = `inf`
`🔗<class_GLTFLight_property_range>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_range**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_range**()

The range of the light, beyond which the light has no effect. glTF
lights with no range defined behave like physical lights (which have
infinite range). When creating a Godot light, the range is clamped to
`4096.0`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GLTFLight_method_from_dictionary}
::: rst-class
classref-method
:::
::::

`GLTFLight<class_GLTFLight>`{.interpreted-text role="ref"}
**from_dictionary**(dictionary:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFLight_method_from_dictionary>`{.interpreted-text
role="ref"}

Creates a new GLTFLight instance by parsing the given
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFLight_method_from_node}
::: rst-class
classref-method
:::
::::

`GLTFLight<class_GLTFLight>`{.interpreted-text role="ref"}
**from_node**(light_node: `Light3D<class_Light3D>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_GLTFLight_method_from_node>`{.interpreted-text
role="ref"}

Create a new GLTFLight instance from the given Godot
`Light3D<class_Light3D>`{.interpreted-text role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFLight_method_get_additional_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_GLTFLight_method_get_additional_data>`{.interpreted-text
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

:::: {#class_GLTFLight_method_set_additional_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_additional_data**(extension_name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
additional_data: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_GLTFLight_method_set_additional_data>`{.interpreted-text
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

:::: {#class_GLTFLight_method_to_dictionary}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**to_dictionary**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GLTFLight_method_to_dictionary>`{.interpreted-text role="ref"}

Serializes this GLTFLight instance into a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GLTFLight_method_to_node}
::: rst-class
classref-method
:::
::::

`Light3D<class_Light3D>`{.interpreted-text role="ref"} **to_node**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_GLTFLight_method_to_node>`{.interpreted-text
role="ref"}

Converts this GLTFLight instance into a Godot
`Light3D<class_Light3D>`{.interpreted-text role="ref"} node.
