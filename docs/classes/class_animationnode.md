github_url
:   hide

# AnimationNode {#class_AnimationNode}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AnimationNodeExtension<class_AnimationNodeExtension>`{.interpreted-text
role="ref"},
`AnimationNodeOutput<class_AnimationNodeOutput>`{.interpreted-text
role="ref"},
`AnimationNodeSync<class_AnimationNodeSync>`{.interpreted-text
role="ref"},
`AnimationNodeTimeScale<class_AnimationNodeTimeScale>`{.interpreted-text
role="ref"},
`AnimationNodeTimeSeek<class_AnimationNodeTimeSeek>`{.interpreted-text
role="ref"},
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}

Base class for `AnimationTree<class_AnimationTree>`{.interpreted-text
role="ref"} nodes. Not related to scene nodes.

::: rst-class
classref-introduction-group
:::

## Description

Base resource for `AnimationTree<class_AnimationTree>`{.interpreted-text
role="ref"} nodes. In general, it\'s not used directly, but you can
create custom ones with custom blending formulas.

Inherit this when creating animation nodes mainly for use in
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}, otherwise
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} should be used instead.

You can access the time information as read-only parameter which is
processed and stored in the previous frame for all nodes except
`AnimationNodeOutput<class_AnimationNodeOutput>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If multiple inputs exist in the **AnimationNode**, which
time information takes precedence depends on the type of
**AnimationNode**.

    var current_length = $AnimationTree["parameters/AnimationNodeName/current_length"]
    var current_position = $AnimationTree["parameters/AnimationNodeName/current_position"]
    var current_delta = $AnimationTree["parameters/AnimationNodeName/current_delta"]

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

:::: {#class_AnimationNode_signal_animation_node_removed}
::: rst-class
classref-signal
:::
::::

**animation_node_removed**(object_id: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_AnimationNode_signal_animation_node_removed>`{.interpreted-text
role="ref"}

Emitted by nodes that inherit from this class and that have an internal
tree when one of their animation nodes removes. The animation nodes that
emit this signal are
`AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>`{.interpreted-text
role="ref"},
`AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>`{.interpreted-text
role="ref"},
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"}, and
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_signal_animation_node_renamed}
::: rst-class
classref-signal
:::
::::

**animation_node_renamed**(object_id: `int<class_int>`{.interpreted-text
role="ref"}, old_name: `String<class_String>`{.interpreted-text
role="ref"}, new_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNode_signal_animation_node_renamed>`{.interpreted-text
role="ref"}

Emitted by nodes that inherit from this class and that have an internal
tree when one of their animation node names changes. The animation nodes
that emit this signal are
`AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>`{.interpreted-text
role="ref"},
`AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>`{.interpreted-text
role="ref"},
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"}, and
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_signal_tree_changed}
::: rst-class
classref-signal
:::
::::

**tree_changed**()
`🔗<class_AnimationNode_signal_tree_changed>`{.interpreted-text
role="ref"}

Emitted by nodes that inherit from this class and that have an internal
tree when one of their animation nodes changes. The animation nodes that
emit this signal are
`AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>`{.interpreted-text
role="ref"},
`AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>`{.interpreted-text
role="ref"},
`AnimationNodeStateMachine<class_AnimationNodeStateMachine>`{.interpreted-text
role="ref"},
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"} and
`AnimationNodeTransition<class_AnimationNodeTransition>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AnimationNode_FilterAction}
::: rst-class
classref-enumeration
:::
::::

enum **FilterAction**:
`🔗<enum_AnimationNode_FilterAction>`{.interpreted-text role="ref"}

:::: {#class_AnimationNode_constant_FILTER_IGNORE}
::: rst-class
classref-enumeration-constant
:::
::::

`FilterAction<enum_AnimationNode_FilterAction>`{.interpreted-text
role="ref"} **FILTER_IGNORE** = `0`

Do not use filtering.

:::: {#class_AnimationNode_constant_FILTER_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`FilterAction<enum_AnimationNode_FilterAction>`{.interpreted-text
role="ref"} **FILTER_PASS** = `1`

Paths matching the filter will be allowed to pass.

:::: {#class_AnimationNode_constant_FILTER_STOP}
::: rst-class
classref-enumeration-constant
:::
::::

`FilterAction<enum_AnimationNode_FilterAction>`{.interpreted-text
role="ref"} **FILTER_STOP** = `2`

Paths matching the filter will be discarded.

:::: {#class_AnimationNode_constant_FILTER_BLEND}
::: rst-class
classref-enumeration-constant
:::
::::

`FilterAction<enum_AnimationNode_FilterAction>`{.interpreted-text
role="ref"} **FILTER_BLEND** = `3`

Paths matching the filter will be blended (by the blend value).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationNode_property_filter_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **filter_enabled**
`🔗<class_AnimationNode_property_filter_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filter_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_filter_enabled**()

If `true`, filtering is enabled.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationNode_private_method__get_caption}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **\_get_caption**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_private_method__get_caption>`{.interpreted-text
role="ref"}

When inheriting from
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, implement this virtual method to override the text caption
for this animation node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_private_method__get_child_by_name}
::: rst-class
classref-method
:::
::::

`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\_get_child_by_name**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_private_method__get_child_by_name>`{.interpreted-text
role="ref"}

When inheriting from
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, implement this virtual method to return a child animation
node by its `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_private_method__get_child_nodes}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_get_child_nodes**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_private_method__get_child_nodes>`{.interpreted-text
role="ref"}

When inheriting from
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, implement this virtual method to return all child animation
nodes in order as a `name: node` dictionary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_private_method__get_parameter_default_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_get_parameter_default_value**(parameter:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_private_method__get_parameter_default_value>`{.interpreted-text
role="ref"}

When inheriting from
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, implement this virtual method to return the default value
of a `parameter`. Parameters are custom local memory used for your
animation nodes, given a resource can be reused in multiple trees.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_private_method__get_parameter_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**\_get_parameter_list**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_private_method__get_parameter_list>`{.interpreted-text
role="ref"}

When inheriting from
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, implement this virtual method to return a list of the
properties on this animation node. Parameters are custom local memory
used for your animation nodes, given a resource can be reused in
multiple trees. Format is similar to
`Object.get_property_list()<class_Object_method_get_property_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_private_method__has_filter}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_has_filter**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_private_method__has_filter>`{.interpreted-text
role="ref"}

When inheriting from
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, implement this virtual method to return whether the blend
tree editor should display filter editing on this animation node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_private_method__is_parameter_read_only}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_parameter_read_only**(parameter:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_private_method__is_parameter_read_only>`{.interpreted-text
role="ref"}

When inheriting from
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, implement this virtual method to return whether the
`parameter` is read-only. Parameters are custom local memory used for
your animation nodes, given a resource can be reused in multiple trees.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_private_method__process}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **\_process**(time:
`float<class_float>`{.interpreted-text role="ref"}, seek:
`bool<class_bool>`{.interpreted-text role="ref"}, is_external_seeking:
`bool<class_bool>`{.interpreted-text role="ref"}, test_only:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_private_method__process>`{.interpreted-text
role="ref"}

**Deprecated:** Currently this is mostly useless as there is a lack of
many APIs to extend AnimationNode by GDScript. It is planned that a more
flexible API using structures will be provided in the future.

When inheriting from
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"}, implement this virtual method to run some code when this
animation node is processed. The `time` parameter is a relative delta,
unless `seek` is `true`, in which case it is absolute.

Here, call the
`blend_input()<class_AnimationNode_method_blend_input>`{.interpreted-text
role="ref"},
`blend_node()<class_AnimationNode_method_blend_node>`{.interpreted-text
role="ref"} or
`blend_animation()<class_AnimationNode_method_blend_animation>`{.interpreted-text
role="ref"} functions. You can also use
`get_parameter()<class_AnimationNode_method_get_parameter>`{.interpreted-text
role="ref"} and
`set_parameter()<class_AnimationNode_method_set_parameter>`{.interpreted-text
role="ref"} to modify local memory.

This function should return the delta.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_add_input}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **add_input**(name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_AnimationNode_method_add_input>`{.interpreted-text role="ref"}

Adds an input to the animation node. This is only useful for animation
nodes created for use in an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}. If the addition fails, returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_blend_animation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**blend_animation**(animation:
`StringName<class_StringName>`{.interpreted-text role="ref"}, time:
`float<class_float>`{.interpreted-text role="ref"}, delta:
`float<class_float>`{.interpreted-text role="ref"}, seeked:
`bool<class_bool>`{.interpreted-text role="ref"}, is_external_seeking:
`bool<class_bool>`{.interpreted-text role="ref"}, blend:
`float<class_float>`{.interpreted-text role="ref"}, looped_flag:
`LoopedFlag<enum_Animation_LoopedFlag>`{.interpreted-text role="ref"} =
0) `🔗<class_AnimationNode_method_blend_animation>`{.interpreted-text
role="ref"}

Blends an animation by `blend` amount (name must be valid in the linked
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}).
A `time` and `delta` may be passed, as well as whether `seeked`
happened.

A `looped_flag` is used by internal processing immediately after the
loop.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_blend_input}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**blend_input**(input_index: `int<class_int>`{.interpreted-text
role="ref"}, time: `float<class_float>`{.interpreted-text role="ref"},
seek: `bool<class_bool>`{.interpreted-text role="ref"},
is_external_seeking: `bool<class_bool>`{.interpreted-text role="ref"},
blend: `float<class_float>`{.interpreted-text role="ref"}, filter:
`FilterAction<enum_AnimationNode_FilterAction>`{.interpreted-text
role="ref"} = 0, sync: `bool<class_bool>`{.interpreted-text role="ref"}
= true, test_only: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_AnimationNode_method_blend_input>`{.interpreted-text
role="ref"}

Blends an input. This is only useful for animation nodes created for an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}. The `time` parameter is a relative delta, unless `seek` is
`true`, in which case it is absolute. A filter mode may be optionally
passed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_blend_node}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **blend_node**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, node:
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"},
time: `float<class_float>`{.interpreted-text role="ref"}, seek:
`bool<class_bool>`{.interpreted-text role="ref"}, is_external_seeking:
`bool<class_bool>`{.interpreted-text role="ref"}, blend:
`float<class_float>`{.interpreted-text role="ref"}, filter:
`FilterAction<enum_AnimationNode_FilterAction>`{.interpreted-text
role="ref"} = 0, sync: `bool<class_bool>`{.interpreted-text role="ref"}
= true, test_only: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_AnimationNode_method_blend_node>`{.interpreted-text
role="ref"}

Blend another animation node (in case this animation node contains child
animation nodes). This function is only useful if you inherit from
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} instead, otherwise editors will not display your animation
node for addition.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_find_input}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **find_input**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_method_find_input>`{.interpreted-text
role="ref"}

Returns the input index which corresponds to `name`. If not found,
returns `-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_get_input_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_input_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_method_get_input_count>`{.interpreted-text
role="ref"}

Amount of inputs in this animation node, only useful for animation nodes
that go into
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_get_input_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_input_name**(input: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_method_get_input_name>`{.interpreted-text
role="ref"}

Gets the name of an input by index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_get_parameter}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_parameter**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_method_get_parameter>`{.interpreted-text
role="ref"}

Gets the value of a parameter. Parameters are custom local memory used
for your animation nodes, given a resource can be reused in multiple
trees.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_get_processing_animation_tree_instance_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_processing_animation_tree_instance_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_method_get_processing_animation_tree_instance_id>`{.interpreted-text
role="ref"}

Returns the object id of the
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"} that
owns this node.

\*\*Note:\*\* This method should only be called from within the
`AnimationNodeExtension._process_animation_node()<class_AnimationNodeExtension_private_method__process_animation_node>`{.interpreted-text
role="ref"} method, and will return an invalid id otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_is_path_filtered}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_path_filtered**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_method_is_path_filtered>`{.interpreted-text
role="ref"}

Returns `true` if the given path is filtered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_is_process_testing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_process_testing**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationNode_method_is_process_testing>`{.interpreted-text
role="ref"}

Returns `true` if this animation node is being processed in test-only
mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_remove_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_input**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_AnimationNode_method_remove_input>`{.interpreted-text
role="ref"}

Removes an input, call this only when inactive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_set_filter_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_filter_path**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AnimationNode_method_set_filter_path>`{.interpreted-text
role="ref"}

Adds or removes a path for the filter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_set_input_name}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**set_input_name**(input: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_AnimationNode_method_set_input_name>`{.interpreted-text
role="ref"}

Sets the name of the input at the given `input` index. If the setting
fails, returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNode_method_set_parameter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_parameter**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_AnimationNode_method_set_parameter>`{.interpreted-text
role="ref"}

Sets a custom parameter. These are used as local memory, because
resources can be reused across the tree or scenes.
