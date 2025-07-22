github_url
:   hide

# AnimationLibrary {#class_AnimationLibrary}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Container for `Animation<class_Animation>`{.interpreted-text role="ref"}
resources.

::: rst-class
classref-introduction-group
:::

## Description

An animation library stores a set of animations accessible through
`StringName<class_StringName>`{.interpreted-text role="ref"} keys, for
use with `AnimationPlayer<class_AnimationPlayer>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Animation tutorial index <../tutorials/animation/index>`{.interpreted-text
  role="doc"}

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

## Signals

:::: {#class_AnimationLibrary_signal_animation_added}
::: rst-class
classref-signal
:::
::::

**animation_added**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationLibrary_signal_animation_added>`{.interpreted-text
role="ref"}

Emitted when an `Animation<class_Animation>`{.interpreted-text
role="ref"} is added, under the key `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationLibrary_signal_animation_changed}
::: rst-class
classref-signal
:::
::::

**animation_changed**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationLibrary_signal_animation_changed>`{.interpreted-text
role="ref"}

Emitted when there\'s a change in one of the animations, e.g. tracks are
added, moved or have changed paths. `name` is the key of the animation
that was changed.

See also
`Resource.changed<class_Resource_signal_changed>`{.interpreted-text
role="ref"}, which this acts as a relay for.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationLibrary_signal_animation_removed}
::: rst-class
classref-signal
:::
::::

**animation_removed**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationLibrary_signal_animation_removed>`{.interpreted-text
role="ref"}

Emitted when an `Animation<class_Animation>`{.interpreted-text
role="ref"} stored with the key `name` is removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationLibrary_signal_animation_renamed}
::: rst-class
classref-signal
:::
::::

**animation_renamed**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, to_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationLibrary_signal_animation_renamed>`{.interpreted-text
role="ref"}

Emitted when the key for an
`Animation<class_Animation>`{.interpreted-text role="ref"} is changed,
from `name` to `to_name`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationLibrary_method_add_animation}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**add_animation**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, animation: `Animation<class_Animation>`{.interpreted-text
role="ref"})
`🔗<class_AnimationLibrary_method_add_animation>`{.interpreted-text
role="ref"}

Adds the `animation` to the library, accessible by the key `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationLibrary_method_get_animation}
::: rst-class
classref-method
:::
::::

`Animation<class_Animation>`{.interpreted-text role="ref"}
**get_animation**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationLibrary_method_get_animation>`{.interpreted-text
role="ref"}

Returns the `Animation<class_Animation>`{.interpreted-text role="ref"}
with the key `name`. If the animation does not exist, `null` is returned
and an error is logged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationLibrary_method_get_animation_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_animation_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationLibrary_method_get_animation_list>`{.interpreted-text
role="ref"}

Returns the keys for the `Animation<class_Animation>`{.interpreted-text
role="ref"}s stored in the library.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationLibrary_method_get_animation_list_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_animation_list_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationLibrary_method_get_animation_list_size>`{.interpreted-text
role="ref"}

Returns the key count for the
`Animation<class_Animation>`{.interpreted-text role="ref"}s stored in
the library.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationLibrary_method_has_animation}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_animation**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationLibrary_method_has_animation>`{.interpreted-text
role="ref"}

Returns `true` if the library stores an
`Animation<class_Animation>`{.interpreted-text role="ref"} with `name`
as the key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationLibrary_method_remove_animation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_animation**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationLibrary_method_remove_animation>`{.interpreted-text
role="ref"}

Removes the `Animation<class_Animation>`{.interpreted-text role="ref"}
with the key `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationLibrary_method_rename_animation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_animation**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, newname:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationLibrary_method_rename_animation>`{.interpreted-text
role="ref"}

Changes the key of the `Animation<class_Animation>`{.interpreted-text
role="ref"} associated with the key `name` to `newname`.
