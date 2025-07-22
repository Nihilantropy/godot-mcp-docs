github_url
:   hide

# Joint2D {#class_Joint2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`DampedSpringJoint2D<class_DampedSpringJoint2D>`{.interpreted-text
role="ref"}, `GrooveJoint2D<class_GrooveJoint2D>`{.interpreted-text
role="ref"}, `PinJoint2D<class_PinJoint2D>`{.interpreted-text
role="ref"}

Abstract base class for all 2D physics joints.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for all joints in 2D physics. 2D joints bind
together two physics bodies
(`node_a<class_Joint2D_property_node_a>`{.interpreted-text role="ref"}
and `node_b<class_Joint2D_property_node_b>`{.interpreted-text
role="ref"}) and apply a constraint.

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

:::: {#class_Joint2D_property_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bias** = `0.0`
`🔗<class_Joint2D_property_bias>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bias**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_bias**()

When `node_a<class_Joint2D_property_node_a>`{.interpreted-text
role="ref"} and
`node_b<class_Joint2D_property_node_b>`{.interpreted-text role="ref"}
move in different directions the
`bias<class_Joint2D_property_bias>`{.interpreted-text role="ref"}
controls how fast the joint pulls them back to their original position.
The lower the `bias<class_Joint2D_property_bias>`{.interpreted-text
role="ref"} the more the two bodies can pull on the joint.

When set to `0`, the default value from
`ProjectSettings.physics/2d/solver/default_constraint_bias<class_ProjectSettings_property_physics/2d/solver/default_constraint_bias>`{.interpreted-text
role="ref"} is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Joint2D_property_disable_collision}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **disable_collision** =
`true` `🔗<class_Joint2D_property_disable_collision>`{.interpreted-text
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

:::: {#class_Joint2D_property_node_a}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **node_a** =
`NodePath("")` `🔗<class_Joint2D_property_node_a>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_node_a**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_node_a**()

Path to the first body (A) attached to the joint. The node must inherit
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Joint2D_property_node_b}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **node_b** =
`NodePath("")` `🔗<class_Joint2D_property_node_b>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_node_b**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_node_b**()

Path to the second body (B) attached to the joint. The node must inherit
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Joint2D_method_get_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Joint2D_method_get_rid>`{.interpreted-text
role="ref"}

Returns the joint\'s internal `RID<class_RID>`{.interpreted-text
role="ref"} from the
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}.
