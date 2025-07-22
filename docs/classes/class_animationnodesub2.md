github_url
:   hide

# AnimationNodeSub2 {#class_AnimationNodeSub2}

**Inherits:**
`AnimationNodeSync<class_AnimationNodeSync>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Blends two animations subtractively inside of an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A resource to add to an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}. Blends two animations subtractively based on the amount
value.

This animation node is usually used for pre-calculation to cancel out
any extra poses from the animation for the \"add\" animation source in
`AnimationNodeAdd2<class_AnimationNodeAdd2>`{.interpreted-text
role="ref"} or
`AnimationNodeAdd3<class_AnimationNodeAdd3>`{.interpreted-text
role="ref"}.

In general, the blend value should be in the `[0.0, 1.0]` range, but
values outside of this range can be used for amplified or inverted
animations.

\*\*Note:\*\* This calculation is different from using a negative value
in `AnimationNodeAdd2<class_AnimationNodeAdd2>`{.interpreted-text
role="ref"}, since the transformation matrices do not satisfy the
commutative law. **AnimationNodeSub2** multiplies the transformation
matrix of the inverted animation from the left side, while negative
`AnimationNodeAdd2<class_AnimationNodeAdd2>`{.interpreted-text
role="ref"} multiplies it from the right side.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
