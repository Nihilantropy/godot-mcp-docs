github_url
:   hide

# AnimationTree {#class_AnimationTree}

**Inherits:** `AnimationMixer<class_AnimationMixer>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A node used for advanced animation transitions in an
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A node used for advanced animation transitions in an
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}.

\*\*Note:\*\* When linked with an
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"},
several properties and methods of the corresponding
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
will not function as expected. Playback and transitions should be
handled using only the **AnimationTree** and its constituent
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}(s).
The `AnimationPlayer<class_AnimationPlayer>`{.interpreted-text
role="ref"} node should be used solely for adding, deleting, and editing
animations.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

:::: {#class_AnimationTree_signal_animation_player_changed}
::: rst-class
classref-signal
:::
::::

**animation_player_changed**()
`🔗<class_AnimationTree_signal_animation_player_changed>`{.interpreted-text
role="ref"}

Emitted when the
`anim_player<class_AnimationTree_property_anim_player>`{.interpreted-text
role="ref"} is changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AnimationTree_AnimationProcessCallback}
::: rst-class
classref-enumeration
:::
::::

enum **AnimationProcessCallback**:
`🔗<enum_AnimationTree_AnimationProcessCallback>`{.interpreted-text
role="ref"}

:::: {#class_AnimationTree_constant_ANIMATION_PROCESS_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>`{.interpreted-text
role="ref"} **ANIMATION_PROCESS_PHYSICS** = `0`

**Deprecated:** See
`AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS>`{.interpreted-text
role="ref"}.

:::: {#class_AnimationTree_constant_ANIMATION_PROCESS_IDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>`{.interpreted-text
role="ref"} **ANIMATION_PROCESS_IDLE** = `1`

**Deprecated:** See
`AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_IDLE<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_IDLE>`{.interpreted-text
role="ref"}.

:::: {#class_AnimationTree_constant_ANIMATION_PROCESS_MANUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>`{.interpreted-text
role="ref"} **ANIMATION_PROCESS_MANUAL** = `2`

**Deprecated:** See
`AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_MANUAL<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_MANUAL>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationTree_property_advance_expression_base_node}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**advance_expression_base_node** = `NodePath(".")`
`🔗<class_AnimationTree_property_advance_expression_base_node>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_advance_expression_base_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_advance_expression_base_node**()

The path to the `Node<class_Node>`{.interpreted-text role="ref"} used to
evaluate the `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} `Expression<class_Expression>`{.interpreted-text role="ref"}
if one is not explicitly specified internally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationTree_property_anim_player}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **anim_player**
= `NodePath("")`
`🔗<class_AnimationTree_property_anim_player>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_animation_player**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_animation_player**()

The path to the
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
used for animating.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationTree_property_tree_root}
::: rst-class
classref-property
:::
::::

`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} **tree_root**
`🔗<class_AnimationTree_property_tree_root>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tree_root**(value:
  `AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
  role="ref"})
- `AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
  role="ref"} **get_tree_root**()

The root animation node of this **AnimationTree**. See
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationTree_method_get_process_callback}
::: rst-class
classref-method
:::
::::

`AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>`{.interpreted-text
role="ref"} **get_process_callback**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationTree_method_get_process_callback>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>`{.interpreted-text
role="ref"} instead.

Returns the process notification in which to update animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationTree_method_set_process_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_process_callback**(mode:
`AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>`{.interpreted-text
role="ref"})
`🔗<class_AnimationTree_method_set_process_callback>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>`{.interpreted-text
role="ref"} instead.

Sets the process notification in which to update animations.
