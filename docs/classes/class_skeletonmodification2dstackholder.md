github_url
:   hide

# SkeletonModification2DStackHolder {#class_SkeletonModification2DStackHolder}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A modification that holds and executes a
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} holds a reference to a
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"}, allowing you to use multiple modification stacks on a
single `Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"}.

\*\*Note:\*\* The modifications in the held
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} will only be executed if their execution mode matches the
execution mode of the SkeletonModification2DStackHolder.

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

:::: {#class_SkeletonModification2DStackHolder_method_get_held_modification_stack}
::: rst-class
classref-method
:::
::::

`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} **get_held_modification_stack**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DStackHolder_method_get_held_modification_stack>`{.interpreted-text
role="ref"}

Returns the
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} that this modification is holding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DStackHolder_method_set_held_modification_stack}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_held_modification_stack**(held_modification_stack:
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonModification2DStackHolder_method_set_held_modification_stack>`{.interpreted-text
role="ref"}

Sets the
`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`{.interpreted-text
role="ref"} that this modification is holding. This modification stack
will then be executed when this modification is executed.
