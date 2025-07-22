github_url
:   hide

# RootMotionView {#class_RootMotionView}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Editor-only helper for setting up root motion in
`AnimationMixer<class_AnimationMixer>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

*Root motion* refers to an animation technique where a mesh\'s skeleton
is used to give impulse to a character. When working with 3D animations,
a popular technique is for animators to use the root skeleton bone to
give motion to the rest of the skeleton. This allows animating
characters in a way where steps actually match the floor below. It also
allows precise interaction with objects during cinematics. See also
`AnimationMixer<class_AnimationMixer>`{.interpreted-text role="ref"}.

\*\*Note:\*\* **RootMotionView** is only visible in the editor. It will
be hidden automatically in the running project.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Using AnimationTree - Root
  motion](../tutorials/animation/animation_tree.html#root-motion)

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

:::: {#class_RootMotionView_property_animation_path}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**animation_path** = `NodePath("")`
`🔗<class_RootMotionView_property_animation_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_animation_path**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_animation_path**()

Path to an `AnimationMixer<class_AnimationMixer>`{.interpreted-text
role="ref"} node to use as a basis for root motion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RootMotionView_property_cell_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cell_size** = `1.0`
`🔗<class_RootMotionView_property_cell_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cell_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_cell_size**()

The grid\'s cell size in 3D units.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RootMotionView_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(0.5, 0.5, 1, 1)`
`🔗<class_RootMotionView_property_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

The grid\'s color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RootMotionView_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `10.0`
`🔗<class_RootMotionView_property_radius>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The grid\'s radius in 3D units. The grid\'s opacity will fade gradually
as the distance from the origin increases until this
`radius<class_RootMotionView_property_radius>`{.interpreted-text
role="ref"} is reached.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RootMotionView_property_zero_y}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **zero_y** = `true`
`🔗<class_RootMotionView_property_zero_y>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_zero_y**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_zero_y**()

If `true`, the grid\'s points will all be on the same Y coordinate
(*local* Y = 0). If `false`, the points\' original Y coordinate is
preserved.
