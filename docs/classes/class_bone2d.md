github_url
:   hide

# Bone2D {#class_Bone2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A joint used with `Skeleton2D<class_Skeleton2D>`{.interpreted-text
role="ref"} to control and animate other nodes.

::: rst-class
classref-introduction-group
:::

## Description

A hierarchy of **Bone2D**s can be bound to a
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"} to control
and animate other `Node2D<class_Node2D>`{.interpreted-text role="ref"}
nodes.

You can use **Bone2D** and
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"} nodes to
animate 2D meshes created with the
`Polygon2D<class_Polygon2D>`{.interpreted-text role="ref"} UV editor.

Each bone has a `rest<class_Bone2D_property_rest>`{.interpreted-text
role="ref"} transform that you can reset to with
`apply_rest()<class_Bone2D_method_apply_rest>`{.interpreted-text
role="ref"}. These rest poses are relative to the bone\'s parent.

If in the editor, you can set the rest pose of an entire skeleton using
a menu option, from the code, you need to iterate over the bones to set
their individual rest poses.

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

:::: {#class_Bone2D_property_rest}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"} **rest**
= `Transform2D(0, 0, 0, 0, 0, 0)`
`🔗<class_Bone2D_property_rest>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rest**(value: `Transform2D<class_Transform2D>`{.interpreted-text
  role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_rest**()

Rest transform of the bone. You can reset the node\'s transforms to this
value using
`apply_rest()<class_Bone2D_method_apply_rest>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Bone2D_method_apply_rest}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**apply_rest**() `🔗<class_Bone2D_method_apply_rest>`{.interpreted-text
role="ref"}

Resets the bone to the rest pose. This is equivalent to setting
`Node2D.transform<class_Node2D_property_transform>`{.interpreted-text
role="ref"} to `rest<class_Bone2D_property_rest>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Bone2D_method_get_autocalculate_length_and_angle}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_autocalculate_length_and_angle**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Bone2D_method_get_autocalculate_length_and_angle>`{.interpreted-text
role="ref"}

Returns whether this **Bone2D** is going to autocalculate its length and
bone angle using its first **Bone2D** child node, if one exists. If
there are no **Bone2D** children, then it cannot autocalculate these
values and will print a warning.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Bone2D_method_get_bone_angle}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_bone_angle**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Bone2D_method_get_bone_angle>`{.interpreted-text
role="ref"}

Returns the angle of the bone in the **Bone2D**.

\*\*Note:\*\* This is different from the **Bone2D**\'s rotation. The
bone\'s angle is the rotation of the bone shown by the gizmo, which is
unaffected by the **Bone2D**\'s
`Node2D.transform<class_Node2D_property_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Bone2D_method_get_index_in_skeleton}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_index_in_skeleton**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Bone2D_method_get_index_in_skeleton>`{.interpreted-text
role="ref"}

Returns the node\'s index as part of the entire skeleton. See
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Bone2D_method_get_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Bone2D_method_get_length>`{.interpreted-text
role="ref"}

Returns the length of the bone in the **Bone2D** node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Bone2D_method_get_skeleton_rest}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_skeleton_rest**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Bone2D_method_get_skeleton_rest>`{.interpreted-text
role="ref"}

Returns the node\'s `rest<class_Bone2D_property_rest>`{.interpreted-text
role="ref"} `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"} if it doesn\'t have a parent, or its rest pose relative to
its parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Bone2D_method_set_autocalculate_length_and_angle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_autocalculate_length_and_angle**(auto_calculate:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Bone2D_method_set_autocalculate_length_and_angle>`{.interpreted-text
role="ref"}

When set to `true`, the **Bone2D** node will attempt to automatically
calculate the bone angle and length using the first child **Bone2D**
node, if one exists. If none exist, the **Bone2D** cannot automatically
calculate these values and will print a warning.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Bone2D_method_set_bone_angle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_angle**(angle: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Bone2D_method_set_bone_angle>`{.interpreted-text
role="ref"}

Sets the bone angle for the **Bone2D**. This is typically set to the
rotation from the **Bone2D** to a child **Bone2D** node.

\*\*Note:\*\* This is different from the **Bone2D**\'s rotation. The
bone\'s angle is the rotation of the bone shown by the gizmo, which is
unaffected by the **Bone2D**\'s
`Node2D.transform<class_Node2D_property_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Bone2D_method_set_length}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_length**(length: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Bone2D_method_set_length>`{.interpreted-text
role="ref"}

Sets the length of the bone in the **Bone2D**.
