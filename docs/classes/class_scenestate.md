github_url
:   hide

# SceneState {#class_SceneState}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides access to a scene file\'s information.

::: rst-class
classref-introduction-group
:::

## Description

Maintains a list of resources, nodes, exported and overridden
properties, and built-in scripts associated with a scene. They cannot be
modified from a **SceneState**, only accessed. Useful for peeking into
what a `PackedScene<class_PackedScene>`{.interpreted-text role="ref"}
contains without instantiating it.

This class cannot be instantiated directly, it is retrieved for a given
scene as the result of
`PackedScene.get_state()<class_PackedScene_method_get_state>`{.interpreted-text
role="ref"}.

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

## Enumerations

:::: {#enum_SceneState_GenEditState}
::: rst-class
classref-enumeration
:::
::::

enum **GenEditState**:
`🔗<enum_SceneState_GenEditState>`{.interpreted-text role="ref"}

:::: {#class_SceneState_constant_GEN_EDIT_STATE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`GenEditState<enum_SceneState_GenEditState>`{.interpreted-text
role="ref"} **GEN_EDIT_STATE_DISABLED** = `0`

If passed to
`PackedScene.instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"}, blocks edits to the scene state.

:::: {#class_SceneState_constant_GEN_EDIT_STATE_INSTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`GenEditState<enum_SceneState_GenEditState>`{.interpreted-text
role="ref"} **GEN_EDIT_STATE_INSTANCE** = `1`

If passed to
`PackedScene.instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"}, provides inherited scene resources to the local scene.

\*\*Note:\*\* Only available in editor builds.

:::: {#class_SceneState_constant_GEN_EDIT_STATE_MAIN}
::: rst-class
classref-enumeration-constant
:::
::::

`GenEditState<enum_SceneState_GenEditState>`{.interpreted-text
role="ref"} **GEN_EDIT_STATE_MAIN** = `2`

If passed to
`PackedScene.instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"}, provides local scene resources to the local scene. Only the
main scene should receive the main edit state.

\*\*Note:\*\* Only available in editor builds.

:::: {#class_SceneState_constant_GEN_EDIT_STATE_MAIN_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`GenEditState<enum_SceneState_GenEditState>`{.interpreted-text
role="ref"} **GEN_EDIT_STATE_MAIN_INHERITED** = `3`

If passed to
`PackedScene.instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"}, it\'s similar to
`GEN_EDIT_STATE_MAIN<class_SceneState_constant_GEN_EDIT_STATE_MAIN>`{.interpreted-text
role="ref"}, but for the case where the scene is being instantiated to
be the base of another one.

\*\*Note:\*\* Only available in editor builds.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SceneState_method_get_base_scene_state}
::: rst-class
classref-method
:::
::::

`SceneState<class_SceneState>`{.interpreted-text role="ref"}
**get_base_scene_state**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_base_scene_state>`{.interpreted-text
role="ref"}

Returns the **SceneState** of the scene that this scene inherits from,
or `null` if it doesn\'t inherit from any scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_connection_binds}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_connection_binds**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_connection_binds>`{.interpreted-text
role="ref"}

Returns the list of bound parameters for the signal at `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_connection_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_connection_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_connection_count>`{.interpreted-text
role="ref"}

Returns the number of signal connections in the scene.

The `idx` argument used to query connection metadata in other
`get_connection_*` methods in the interval
`[0, get_connection_count() - 1]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_connection_flags}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_connection_flags**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_connection_flags>`{.interpreted-text
role="ref"}

Returns the connection flags for the signal at `idx`. See
`ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text role="ref"}
constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_connection_method}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_connection_method**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_connection_method>`{.interpreted-text
role="ref"}

Returns the method connected to the signal at `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_connection_signal}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_connection_signal**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_connection_signal>`{.interpreted-text
role="ref"}

Returns the name of the signal at `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_connection_source}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_connection_source**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_connection_source>`{.interpreted-text
role="ref"}

Returns the path to the node that owns the signal at `idx`, relative to
the root node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_connection_target}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_connection_target**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_connection_target>`{.interpreted-text
role="ref"}

Returns the path to the node that owns the method connected to the
signal at `idx`, relative to the root node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_connection_unbinds}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_connection_unbinds**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_connection_unbinds>`{.interpreted-text
role="ref"}

Returns the number of unbound parameters for the signal at `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_node_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_count>`{.interpreted-text
role="ref"}

Returns the number of nodes in the scene.

The `idx` argument used to query node data in other `get_node_*` methods
in the interval `[0, get_node_count() - 1]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_groups}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_node_groups**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_groups>`{.interpreted-text
role="ref"}

Returns the list of group names associated with the node at `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_node_index**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_index>`{.interpreted-text
role="ref"}

Returns the node\'s index, which is its position relative to its
siblings. This is only relevant and saved in scenes for cases where new
nodes are added to an instantiated or inherited scene among siblings
from the base scene. Despite the name, this index is not related to the
`idx` argument used here and in other methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_instance}
::: rst-class
classref-method
:::
::::

`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}
**get_node_instance**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_instance>`{.interpreted-text
role="ref"}

Returns a `PackedScene<class_PackedScene>`{.interpreted-text role="ref"}
for the node at `idx` (i.e. the whole branch starting at this node, with
its child nodes and resources), or `null` if the node is not an
instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_instance_placeholder}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_node_instance_placeholder**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_instance_placeholder>`{.interpreted-text
role="ref"}

Returns the path to the represented scene file if the node at `idx` is
an `InstancePlaceholder<class_InstancePlaceholder>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_node_name**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_name>`{.interpreted-text
role="ref"}

Returns the name of the node at `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_owner_path}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_node_owner_path**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_owner_path>`{.interpreted-text
role="ref"}

Returns the path to the owner of the node at `idx`, relative to the root
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_path}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_node_path**(idx: `int<class_int>`{.interpreted-text role="ref"},
for_parent: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_path>`{.interpreted-text
role="ref"}

Returns the path to the node at `idx`.

If `for_parent` is `true`, returns the path of the `idx` node\'s parent
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_property_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_node_property_count**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_property_count>`{.interpreted-text
role="ref"}

Returns the number of exported or overridden properties for the node at
`idx`.

The `prop_idx` argument used to query node property data in other
`get_node_property_*` methods in the interval
`[0, get_node_property_count() - 1]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_property_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_node_property_name**(idx: `int<class_int>`{.interpreted-text
role="ref"}, prop_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_property_name>`{.interpreted-text
role="ref"}

Returns the name of the property at `prop_idx` for the node at `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_property_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_node_property_value**(idx: `int<class_int>`{.interpreted-text
role="ref"}, prop_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_property_value>`{.interpreted-text
role="ref"}

Returns the value of the property at `prop_idx` for the node at `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_node_type}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_node_type**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_get_node_type>`{.interpreted-text
role="ref"}

Returns the type of the node at `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_get_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_SceneState_method_get_path>`{.interpreted-text
role="ref"}

Returns the resource path to the represented
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneState_method_is_node_instance_placeholder}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_node_instance_placeholder**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneState_method_is_node_instance_placeholder>`{.interpreted-text
role="ref"}

Returns `true` if the node at `idx` is an
`InstancePlaceholder<class_InstancePlaceholder>`{.interpreted-text
role="ref"}.
