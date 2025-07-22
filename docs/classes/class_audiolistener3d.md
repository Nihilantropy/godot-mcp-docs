github_url
:   hide

::: {.meta keywords="sound"}
:::

# AudioListener3D {#class_AudioListener3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Overrides the location sounds are heard from.

::: rst-class
classref-introduction-group
:::

## Description

Once added to the scene tree and enabled using
`make_current()<class_AudioListener3D_method_make_current>`{.interpreted-text
role="ref"}, this node will override the location sounds are heard from.
This can be used to listen from a location different from the
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}.

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

:::: {#class_AudioListener3D_method_clear_current}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_current**()
`🔗<class_AudioListener3D_method_clear_current>`{.interpreted-text
role="ref"}

Disables the listener to use the current camera\'s listener instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioListener3D_method_get_listener_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_listener_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioListener3D_method_get_listener_transform>`{.interpreted-text
role="ref"}

Returns the listener\'s global orthonormalized
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioListener3D_method_is_current}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_current**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioListener3D_method_is_current>`{.interpreted-text
role="ref"}

Returns `true` if the listener was made current using
`make_current()<class_AudioListener3D_method_make_current>`{.interpreted-text
role="ref"}, `false` otherwise.

\*\*Note:\*\* There may be more than one AudioListener3D marked as
\"current\" in the scene tree, but only the one that was made current
last will be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioListener3D_method_make_current}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_current**()
`🔗<class_AudioListener3D_method_make_current>`{.interpreted-text
role="ref"}

Enables the listener. This will override the current camera\'s listener.
