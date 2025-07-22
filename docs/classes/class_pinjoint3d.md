github_url
:   hide

# PinJoint3D {#class_PinJoint3D}

**Inherits:** `Joint3D<class_Joint3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A physics joint that attaches two 3D physics bodies at a single point,
allowing them to freely rotate.

::: rst-class
classref-introduction-group
:::

## Description

A physics joint that attaches two 3D physics bodies at a single point,
allowing them to freely rotate. For example, a
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} can be
attached to a `StaticBody3D<class_StaticBody3D>`{.interpreted-text
role="ref"} to create a pendulum or a seesaw.

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

:::: {#enum_PinJoint3D_Param}
::: rst-class
classref-enumeration
:::
::::

enum **Param**: `🔗<enum_PinJoint3D_Param>`{.interpreted-text
role="ref"}

:::: {#class_PinJoint3D_constant_PARAM_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_PinJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_BIAS** = `0`

The force with which the pinned objects stay in positional relation to
each other. The higher, the stronger.

:::: {#class_PinJoint3D_constant_PARAM_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_PinJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_DAMPING** = `1`

The force with which the pinned objects stay in velocity relation to
each other. The higher, the stronger.

:::: {#class_PinJoint3D_constant_PARAM_IMPULSE_CLAMP}
::: rst-class
classref-enumeration-constant
:::
::::

`Param<enum_PinJoint3D_Param>`{.interpreted-text role="ref"}
**PARAM_IMPULSE_CLAMP** = `2`

If above 0, this value is the maximum value for an impulse that this
Joint3D produces.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_PinJoint3D_property_params/bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **params/bias** =
`0.3` `🔗<class_PinJoint3D_property_params/bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_PinJoint3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_PinJoint3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The force with which the pinned objects stay in positional relation to
each other. The higher, the stronger.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PinJoint3D_property_params/damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **params/damping** =
`1.0` `🔗<class_PinJoint3D_property_params/damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_PinJoint3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_PinJoint3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The force with which the pinned objects stay in velocity relation to
each other. The higher, the stronger.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PinJoint3D_property_params/impulse_clamp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**params/impulse_clamp** = `0.0`
`🔗<class_PinJoint3D_property_params/impulse_clamp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(param: `Param<enum_PinJoint3D_Param>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param**(param: `Param<enum_PinJoint3D_Param>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If above 0, this value is the maximum value for an impulse that this
Joint3D produces.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PinJoint3D_method_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_param**(param:
`Param<enum_PinJoint3D_Param>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PinJoint3D_method_get_param>`{.interpreted-text
role="ref"}

Returns the value of the specified parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PinJoint3D_method_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param**(param: `Param<enum_PinJoint3D_Param>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PinJoint3D_method_set_param>`{.interpreted-text role="ref"}

Sets the value of the specified parameter.
