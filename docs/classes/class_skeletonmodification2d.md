github_url
:   hide

# SkeletonModification2D {#class_SkeletonModification2D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`SkeletonModification2DCCDIK<class_SkeletonModification2DCCDIK>`{.interpreted-text
role="ref"},
`SkeletonModification2DFABRIK<class_SkeletonModification2DFABRIK>`{.interpreted-text
role="ref"},
`SkeletonModification2DJiggle<class_SkeletonModification2DJiggle>`{.interpreted-text
role="ref"},
`SkeletonModification2DLookAt<class_SkeletonModification2DLookAt>`{.interpreted-text
role="ref"},
`SkeletonModification2DPhysicalBones<class_SkeletonModification2DPhysicalBones>`{.interpreted-text
role="ref"},
`SkeletonModification2DStackHolder<class_SkeletonModification2DStackHolder>`{.interpreted-text
role="ref"},
`SkeletonModification2DTwoBoneIK<class_SkeletonModification2DTwoBoneIK>`{.interpreted-text
role="ref"}

Base class for resources that operate on
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"}s in a
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This resource provides an interface that can be expanded so code that
operates on `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} nodes
in a `Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"} can be
mixed and matched together to create complex interactions.

This is used to provide Godot with a flexible and powerful Inverse
Kinematics solution that can be adapted for many different uses.

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

:::: {#class_SkeletonModification2D_property_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `true`
`🔗<class_SkeletonModification2D_property_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_enabled**()

If `true`, the modification\'s
`_execute()<class_SkeletonModification2D_private_method__execute>`{.interpreted-text
role="ref"} function will be called by the
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2D_property_execution_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **execution_mode** = `0`
`🔗<class_SkeletonModification2D_property_execution_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_execution_mode**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_execution_mode**()

The execution mode for the modification. This tells the modification
stack when to execute the modification. Some modifications have settings
that are only available in certain execution modes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonModification2D_private_method__draw_editor_gizmo}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_draw_editor_gizmo**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2D_private_method__draw_editor_gizmo>`{.interpreted-text
role="ref"}

Used for drawing **editor-only** modification gizmos. This function will
only be called in the Godot editor and can be overridden to draw custom
gizmos.

\*\*Note:\*\* You will need to use the Skeleton2D from
`SkeletonModificationStack2D.get_skeleton()<class_SkeletonModificationStack2D_method_get_skeleton>`{.interpreted-text
role="ref"} and it\'s draw functions, as the **SkeletonModification2D**
resource cannot draw on its own.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2D_private_method__execute}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_execute**(delta: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2D_private_method__execute>`{.interpreted-text
role="ref"}

Executes the given modification. This is where the modification performs
whatever function it is designed to do.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2D_private_method__setup_modification}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_setup_modification**(modification_stack:
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2D_private_method__setup_modification>`{.interpreted-text
role="ref"}

Called when the modification is setup. This is where the modification
performs initialization.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2D_method_clamp_angle}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**clamp_angle**(angle: `float<class_float>`{.interpreted-text
role="ref"}, min: `float<class_float>`{.interpreted-text role="ref"},
max: `float<class_float>`{.interpreted-text role="ref"}, invert:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2D_method_clamp_angle>`{.interpreted-text
role="ref"}

Takes an angle and clamps it so it is within the passed-in `min` and
`max` range. `invert` will inversely clamp the angle, clamping it to the
range outside of the given bounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2D_method_get_editor_draw_gizmo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_editor_draw_gizmo**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2D_method_get_editor_draw_gizmo>`{.interpreted-text
role="ref"}

Returns whether this modification will call
`_draw_editor_gizmo()<class_SkeletonModification2D_private_method__draw_editor_gizmo>`{.interpreted-text
role="ref"} in the Godot editor to draw modification-specific gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2D_method_get_is_setup}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_is_setup**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2D_method_get_is_setup>`{.interpreted-text
role="ref"}

Returns whether this modification has been successfully setup or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2D_method_get_modification_stack}
::: rst-class
classref-method
:::
::::

`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} **get_modification_stack**()
`🔗<class_SkeletonModification2D_method_get_modification_stack>`{.interpreted-text
role="ref"}

Returns the
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} that this modification is bound to. Through the modification
stack, you can access the Skeleton2D the modification is operating on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2D_method_set_editor_draw_gizmo}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_editor_draw_gizmo**(draw_gizmo:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2D_method_set_editor_draw_gizmo>`{.interpreted-text
role="ref"}

Sets whether this modification will call
`_draw_editor_gizmo()<class_SkeletonModification2D_private_method__draw_editor_gizmo>`{.interpreted-text
role="ref"} in the Godot editor to draw modification-specific gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2D_method_set_is_setup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_is_setup**(is_setup: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonModification2D_method_set_is_setup>`{.interpreted-text
role="ref"}

Manually allows you to set the setup state of the modification. This
function should only rarely be used, as the
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} the modification is bound to should handle setting the
modification up.
