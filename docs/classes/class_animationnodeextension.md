github_url
:   hide

# AnimationNodeExtension {#class_AnimationNodeExtension}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Base class for extending
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}s from GDScript, C#, or C++.

::: rst-class
classref-introduction-group
:::

## Description

**AnimationNodeExtension** exposes the APIs of
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} to allow users to extend it from GDScript, C#, or C++. This
class is not meant to be used directly, but to be extended by other
classes. It is used to create custom nodes for the
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}
system.

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

:::: {#class_AnimationNodeExtension_private_method__process_animation_node}
::: rst-class
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **\_process_animation_node**(playback_info:
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"}, test_only: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeExtension_private_method__process_animation_node>`{.interpreted-text
role="ref"}

A version of the
`AnimationNode._process()<class_AnimationNode_private_method__process>`{.interpreted-text
role="ref"} method that is meant to be overridden by custom nodes. It
returns a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} with the processed animation data.

The `PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"} parameter contains the playback information, containing the
following values encoded as floating point numbers (in order): playback
time and delta, start and end times, whether a seek was requested
(encoded as a float greater than `0`), whether the seek request was
externally requested (encoded as a float greater than `0`), the current
`LoopedFlag<enum_Animation_LoopedFlag>`{.interpreted-text role="ref"}
(encoded as a float), and the current blend weight.

The function must return a
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} of the node\'s time info, containing the following values
(in order): animation length, time position, delta,
`LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"}
(encoded as a float), whether the animation is about to end (encoded as
a float greater than `0`) and whether the animation is infinite (encoded
as a float greater than `0`). All values must be included in the
returned array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeExtension_method_get_remaining_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_remaining_time**(node_info:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}, break_loop: `bool<class_bool>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeExtension_method_get_remaining_time>`{.interpreted-text
role="ref"}

Returns the animation\'s remaining time for the given node info. For
looping animations, it will only return the remaining time if
`break_loop` is `true`, a large integer value will be returned
otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeExtension_method_is_looping}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_looping**(node_info:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNodeExtension_method_is_looping>`{.interpreted-text
role="ref"}

Returns `true` if the animation for the given `node_info` is looping.
