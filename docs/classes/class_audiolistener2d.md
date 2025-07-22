github_url
:   hide

::: {.meta keywords="sound"}
:::

# AudioListener2D {#class_AudioListener2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Overrides the location sounds are heard from.

::: rst-class
classref-introduction-group
:::

## Description

Once added to the scene tree and enabled using
`make_current()<class_AudioListener2D_method_make_current>`{.interpreted-text
role="ref"}, this node will override the location sounds are heard from.
Only one **AudioListener2D** can be current. Using
`make_current()<class_AudioListener2D_method_make_current>`{.interpreted-text
role="ref"} will disable the previous **AudioListener2D**.

If there is no active **AudioListener2D** in the current
`Viewport<class_Viewport>`{.interpreted-text role="ref"}, center of the
screen will be used as a hearing point for the audio.
**AudioListener2D** needs to be inside
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} to function.

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

## Method Descriptions

:::: {#class_AudioListener2D_method_clear_current}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_current**()
`🔗<class_AudioListener2D_method_clear_current>`{.interpreted-text
role="ref"}

Disables the **AudioListener2D**. If it\'s not set as current, this
method will have no effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioListener2D_method_is_current}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_current**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioListener2D_method_is_current>`{.interpreted-text
role="ref"}

Returns `true` if this **AudioListener2D** is currently active.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioListener2D_method_make_current}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_current**()
`🔗<class_AudioListener2D_method_make_current>`{.interpreted-text
role="ref"}

Makes the **AudioListener2D** active, setting it as the hearing point
for the sounds. If there is already another active **AudioListener2D**,
it will be disabled.

This method will have no effect if the **AudioListener2D** is not added
to `SceneTree<class_SceneTree>`{.interpreted-text role="ref"}.
