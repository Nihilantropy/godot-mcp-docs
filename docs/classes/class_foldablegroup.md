github_url
:   hide

::: {.meta keywords="expandable, collapsible, collapse"}
:::

# FoldableGroup {#class_FoldableGroup}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A group of foldable containers that doesn\'t allow more than one
container to be expanded at a time.

::: rst-class
classref-introduction-group
:::

## Description

A group of
`FoldableContainer<class_FoldableContainer>`{.interpreted-text
role="ref"}-derived nodes. Only one container can be expanded at a time.

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

## Signals

:::: {#class_FoldableGroup_signal_expanded}
::: rst-class
classref-signal
:::
::::

**expanded**(container:
`FoldableContainer<class_FoldableContainer>`{.interpreted-text
role="ref"}) `🔗<class_FoldableGroup_signal_expanded>`{.interpreted-text
role="ref"}

Emitted when one of the containers of the group is expanded.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_FoldableGroup_property_allow_folding_all}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **allow_folding_all** =
`false`
`🔗<class_FoldableGroup_property_allow_folding_all>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_folding_all**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_allow_folding_all**()

If `true`, it is possible to fold all containers in this FoldableGroup.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_FoldableGroup_method_get_containers}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`FoldableContainer<class_FoldableContainer>`{.interpreted-text
role="ref"}\] **get_containers**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FoldableGroup_method_get_containers>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`FoldableContainer<class_FoldableContainer>`{.interpreted-text
role="ref"}s that have this as their FoldableGroup (see
`FoldableContainer.foldable_group<class_FoldableContainer_property_foldable_group>`{.interpreted-text
role="ref"}). This is equivalent to
`ButtonGroup<class_ButtonGroup>`{.interpreted-text role="ref"} but for
FoldableContainers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FoldableGroup_method_get_expanded_container}
::: rst-class
classref-method
:::
::::

`FoldableContainer<class_FoldableContainer>`{.interpreted-text
role="ref"} **get_expanded_container**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FoldableGroup_method_get_expanded_container>`{.interpreted-text
role="ref"}

Returns the current expanded container.
