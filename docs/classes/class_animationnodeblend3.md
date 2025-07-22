github_url
:   hide

# AnimationNodeBlend3 {#class_AnimationNodeBlend3}

**Inherits:**
`AnimationNodeSync<class_AnimationNodeSync>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Blends two of three animations linearly inside of an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A resource to add to an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}. Blends two animations out of three linearly out of three
based on the amount value.

This animation node has three inputs:

- The base animation to blend with
- A \"-blend\" animation to blend with when the blend amount is negative
  value
- A \"+blend\" animation to blend with when the blend amount is positive
  value

In general, the blend value should be in the `[-1.0, 1.0]` range. Values
outside of this range can blend amplified animations, however,
`AnimationNodeAdd3<class_AnimationNodeAdd3>`{.interpreted-text
role="ref"} works better for this purpose.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
