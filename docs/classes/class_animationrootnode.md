github_url
:   hide

# AnimationRootNode {#class_AnimationRootNode}

**Inherits:** `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AnimationNodeAnimation<class_AnimationNodeAnimation>`{.interpreted-text
role="ref"},
`AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>`{.interpreted-text
role="ref"},
`AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>`{.interpreted-text
role="ref"},
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"},
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"}

Base class for `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"}s that hold one or multiple composite animations. Usually
used for
`AnimationTree.tree_root<class_AnimationTree_property_tree_root>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**AnimationRootNode** is a base class for
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}s that
hold a complete animation. A complete animation refers to the output of
an `AnimationNodeOutput<class_AnimationNodeOutput>`{.interpreted-text
role="ref"} in an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"} or the output of another **AnimationRootNode**. Used for
`AnimationTree.tree_root<class_AnimationTree_property_tree_root>`{.interpreted-text
role="ref"} or in other **AnimationRootNode**s.

Examples of built-in root nodes include
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"} (allows blending nodes between each other using various
modes),
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"} (allows to configure blending and transitions between nodes
using a state machine pattern),
`AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>`{.interpreted-text
role="ref"} (allows linear blending between **three**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}s),
`AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>`{.interpreted-text
role="ref"} (allows linear blending only between **two**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}s).

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
