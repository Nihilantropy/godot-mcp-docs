github_url
:   hide

# SkeletonModificationStack2D {#class_SkeletonModificationStack2D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A resource that holds a stack of
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

This resource is used by the Skeleton and holds a stack of
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"}s.

This controls the order of the modifications and how they are applied.
Modification order is especially important for full-body IK setups, as
you need to execute the modifications in the correct order to get the
desired results. For example, you want to execute a modification on the
spine *before* the arms on a humanoid skeleton.

This resource also controls how strongly all of the modifications are
applied to the `Skeleton2D<class_Skeleton2D>`{.interpreted-text
role="ref"}.

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

:::: {#class_SkeletonModificationStack2D_property_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `false`
`🔗<class_SkeletonModificationStack2D_property_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_enabled**()

If `true`, the modification\'s in the stack will be called. This is
handled automatically through the
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_property_modification_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **modification_count** =
`0`
`🔗<class_SkeletonModificationStack2D_property_modification_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modification_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_modification_count**()

The number of modifications in the stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_property_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **strength** = `1.0`
`🔗<class_SkeletonModificationStack2D_property_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_strength**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_strength**()

The interpolation strength of the modifications in stack. A value of `0`
will make it where the modifications are not applied, a strength of
`0.5` will be half applied, and a strength of `1` will allow the
modifications to be fully applied and override the
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"}
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} poses.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonModificationStack2D_method_add_modification}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_modification**(modification:
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonModificationStack2D_method_add_modification>`{.interpreted-text
role="ref"}

Adds the passed-in
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} to the stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_method_delete_modification}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**delete_modification**(mod_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonModificationStack2D_method_delete_modification>`{.interpreted-text
role="ref"}

Deletes the
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} at the index position `mod_idx`, if it exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_method_enable_all_modifications}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**enable_all_modifications**(enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModificationStack2D_method_enable_all_modifications>`{.interpreted-text
role="ref"}

Enables all
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"}s in the stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_method_execute}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**execute**(delta: `float<class_float>`{.interpreted-text role="ref"},
execution_mode: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModificationStack2D_method_execute>`{.interpreted-text
role="ref"}

Executes all of the
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"}s in the stack that use the same execution mode as the
passed-in `execution_mode`, starting from index `0` to
`modification_count<class_SkeletonModificationStack2D_property_modification_count>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The order of the modifications can matter depending on the
modifications. For example, modifications on a spine should operate
before modifications on the arms in order to get proper results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_method_get_is_setup}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_is_setup**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModificationStack2D_method_get_is_setup>`{.interpreted-text
role="ref"}

Returns a boolean that indicates whether the modification stack is setup
and can execute.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_method_get_modification}
::: rst-class
classref-method
:::
::::

`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} **get_modification**(mod_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModificationStack2D_method_get_modification>`{.interpreted-text
role="ref"}

Returns the
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} at the passed-in index, `mod_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_method_get_skeleton}
::: rst-class
classref-method
:::
::::

`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"}
**get_skeleton**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModificationStack2D_method_get_skeleton>`{.interpreted-text
role="ref"}

Returns the `Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"}
node that the SkeletonModificationStack2D is bound to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_method_set_modification}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_modification**(mod_idx: `int<class_int>`{.interpreted-text
role="ref"}, modification:
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonModificationStack2D_method_set_modification>`{.interpreted-text
role="ref"}

Sets the modification at `mod_idx` to the passed-in modification,
`modification`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModificationStack2D_method_setup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **setup**()
`🔗<class_SkeletonModificationStack2D_method_setup>`{.interpreted-text
role="ref"}

Sets up the modification stack so it can execute. This function should
be called by `Skeleton2D<class_Skeleton2D>`{.interpreted-text
role="ref"} and shouldn\'t be manually called unless you know what you
are doing.
