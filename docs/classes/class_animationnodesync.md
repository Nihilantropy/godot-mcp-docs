github_url
:   hide

# AnimationNodeSync {#class_AnimationNodeSync}

**Inherits:** `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AnimationNodeAdd2<class_AnimationNodeAdd2>`{.interpreted-text
role="ref"},
`AnimationNodeAdd3<class_AnimationNodeAdd3>`{.interpreted-text
role="ref"},
`AnimationNodeBlend2<class_AnimationNodeBlend2>`{.interpreted-text
role="ref"},
`AnimationNodeBlend3<class_AnimationNodeBlend3>`{.interpreted-text
role="ref"},
`AnimationNodeOneShot<class_AnimationNodeOneShot>`{.interpreted-text
role="ref"},
`AnimationNodeSub2<class_AnimationNodeSub2>`{.interpreted-text
role="ref"},
`AnimationNodeTransition<class_AnimationNodeTransition>`{.interpreted-text
role="ref"}

Base class for `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"}s with multiple input ports that must be synchronized.

::: rst-class
classref-introduction-group
:::

## Description

An animation node used to combine, mix, or blend two or more animations
together while keeping them synchronized within an
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationNodeSync_property_sync}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sync** = `false`
`🔗<class_AnimationNodeSync_property_sync>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_sync**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_using_sync**()

If `false`, the blended animations\' frame are stopped when the blend
value is `0`.

If `true`, forcing the blended animations to advance frame.
