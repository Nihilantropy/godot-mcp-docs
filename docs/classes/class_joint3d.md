github_url
:   hide

# Joint3D {#class_Joint3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`ConeTwistJoint3D<class_ConeTwistJoint3D>`{.interpreted-text
role="ref"},
`Generic6DOFJoint3D<class_Generic6DOFJoint3D>`{.interpreted-text
role="ref"}, `HingeJoint3D<class_HingeJoint3D>`{.interpreted-text
role="ref"}, `PinJoint3D<class_PinJoint3D>`{.interpreted-text
role="ref"}, `SliderJoint3D<class_SliderJoint3D>`{.interpreted-text
role="ref"}

Abstract base class for all 3D physics joints.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for all joints in 3D physics. 3D joints bind
together two physics bodies
(`node_a<class_Joint3D_property_node_a>`{.interpreted-text role="ref"}
and `node_b<class_Joint3D_property_node_b>`{.interpreted-text
role="ref"}) and apply a constraint. If only one body is defined, it is
attached to a fixed `StaticBody3D<class_StaticBody3D>`{.interpreted-text
role="ref"} without collision shapes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Truck Town Demo](https://godotengine.org/asset-library/asset/2752)

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

:::: {#class_Joint3D_property_exclude_nodes_from_collision}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**exclude_nodes_from_collision** = `true`
`🔗<class_Joint3D_property_exclude_nodes_from_collision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exclude_nodes_from_collision**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_exclude_nodes_from_collision**()

If `true`, the two bodies bound together do not collide with each other.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Joint3D_property_node_a}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **node_a** =
`NodePath("")` `🔗<class_Joint3D_property_node_a>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_node_a**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_node_a**()

Path to the first node (A) attached to the joint. The node must inherit
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}.

If left empty and
`node_b<class_Joint3D_property_node_b>`{.interpreted-text role="ref"} is
set, the body is attached to a fixed
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"} without
collision shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Joint3D_property_node_b}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **node_b** =
`NodePath("")` `🔗<class_Joint3D_property_node_b>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_node_b**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_node_b**()

Path to the second node (B) attached to the joint. The node must inherit
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}.

If left empty and
`node_a<class_Joint3D_property_node_a>`{.interpreted-text role="ref"} is
set, the body is attached to a fixed
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"} without
collision shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Joint3D_property_solver_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **solver_priority** = `1`
`🔗<class_Joint3D_property_solver_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_solver_priority**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_solver_priority**()

The priority used to define which solver is executed first for multiple
joints. The lower the value, the higher the priority.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Joint3D_method_get_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Joint3D_method_get_rid>`{.interpreted-text
role="ref"}

Returns the joint\'s internal `RID<class_RID>`{.interpreted-text
role="ref"} from the
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.
