github_url
:   hide

# AnimationNodeTimeSeek {#class_AnimationNodeTimeSeek}

**Inherits:** `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A time-seeking animation node used in
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This animation node can be used to cause a seek command to happen to any
sub-children of the animation graph. Use to play an
`Animation<class_Animation>`{.interpreted-text role="ref"} from the
start or a certain playback position inside the
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

After setting the time and changing the animation playback, the time
seek node automatically goes into sleep mode on the next process frame
by setting its `seek_request` value to `-1.0`.

::::: tabs
::: code-tab
gdscript

\# Play child animation from the start.
animation_tree.set(\"parameters/TimeSeek/seek_request\", 0.0) \#
Alternative syntax (same result as above).
animation_tree\[\"parameters/TimeSeek/seek_request\"\] = 0.0

\# Play child animation from 12 second timestamp.
animation_tree.set(\"parameters/TimeSeek/seek_request\", 12.0) \#
Alternative syntax (same result as above).
animation_tree\[\"parameters/TimeSeek/seek_request\"\] = 12.0
:::

::: code-tab
csharp

// Play child animation from the start.
animationTree.Set(\"parameters/TimeSeek/seek_request\", 0.0);

// Play child animation from 12 second timestamp.
animationTree.Set(\"parameters/TimeSeek/seek_request\", 12.0);
:::
:::::

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

:::: {#class_AnimationNodeTimeSeek_property_explicit_elapse}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **explicit_elapse** =
`true`
`🔗<class_AnimationNodeTimeSeek_property_explicit_elapse>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_explicit_elapse**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_explicit_elapse**()

If `true`, some processes are executed to handle keys between seeks,
such as calculating root motion and finding the nearest discrete key.
