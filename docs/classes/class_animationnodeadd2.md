github_url
:   hide

# AnimationNodeAdd2 {#class_AnimationNodeAdd2}

**Inherits:**
`AnimationNodeSync<class_AnimationNodeSync>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Blends two animations additively inside of an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A resource to add to an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}. Blends two animations additively based on the amount value.

If the amount is greater than `1.0`, the animation connected to \"in\"
port is blended with the amplified animation connected to \"add\" port.

If the amount is less than `0.0`, the animation connected to \"in\" port
is blended with the inverted animation connected to \"add\" port.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
