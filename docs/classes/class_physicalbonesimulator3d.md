github_url
:   hide

# PhysicalBoneSimulator3D {#class_PhysicalBoneSimulator3D}

**Inherits:**
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Node that can be the parent of
`PhysicalBone3D<class_PhysicalBone3D>`{.interpreted-text role="ref"} and
can apply the simulation results to
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Node that can be the parent of
`PhysicalBone3D<class_PhysicalBone3D>`{.interpreted-text role="ref"} and
can apply the simulation results to
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}.

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

## Method Descriptions

:::: {#class_PhysicalBoneSimulator3D_method_is_simulating_physics}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_simulating_physics**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicalBoneSimulator3D_method_is_simulating_physics>`{.interpreted-text
role="ref"}

Returns a boolean that indicates whether the **PhysicalBoneSimulator3D**
is running and simulating.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBoneSimulator3D_method_physical_bones_add_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**physical_bones_add_collision_exception**(exception:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicalBoneSimulator3D_method_physical_bones_add_collision_exception>`{.interpreted-text
role="ref"}

Adds a collision exception to the physical bone.

Works just like the `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBoneSimulator3D_method_physical_bones_remove_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**physical_bones_remove_collision_exception**(exception:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_PhysicalBoneSimulator3D_method_physical_bones_remove_collision_exception>`{.interpreted-text
role="ref"}

Removes a collision exception to the physical bone.

Works just like the `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBoneSimulator3D_method_physical_bones_start_simulation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**physical_bones_start_simulation**(bones:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] = \[\])
`🔗<class_PhysicalBoneSimulator3D_method_physical_bones_start_simulation>`{.interpreted-text
role="ref"}

Tells the `PhysicalBone3D<class_PhysicalBone3D>`{.interpreted-text
role="ref"} nodes in the Skeleton to start simulating and reacting to
the physics world.

Optionally, a list of bone names can be passed-in, allowing only the
passed-in bones to be simulated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBoneSimulator3D_method_physical_bones_stop_simulation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**physical_bones_stop_simulation**()
`🔗<class_PhysicalBoneSimulator3D_method_physical_bones_stop_simulation>`{.interpreted-text
role="ref"}

Tells the `PhysicalBone3D<class_PhysicalBone3D>`{.interpreted-text
role="ref"} nodes in the Skeleton to stop simulating.
