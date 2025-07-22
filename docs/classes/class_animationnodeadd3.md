github_url
:   hide

# AnimationNodeAdd3 {#class_AnimationNodeAdd3}

**Inherits:**
`AnimationNodeSync<class_AnimationNodeSync>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Blends two of three animations additively inside of an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A resource to add to an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}. Blends two animations out of three additively out of three
based on the amount value.

This animation node has three inputs:

- The base animation to add to
- A \"-add\" animation to blend with when the blend amount is negative
- A \"+add\" animation to blend with when the blend amount is positive

If the absolute value of the amount is greater than `1.0`, the animation
connected to \"in\" port is blended with the amplified animation
connected to \"-add\"/\"+add\" port.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)
