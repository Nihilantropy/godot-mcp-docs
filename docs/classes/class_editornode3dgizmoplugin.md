github_url
:   hide

# EditorNode3DGizmoPlugin {#class_EditorNode3DGizmoPlugin}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A class used by the editor to define Node3D gizmo types.

::: rst-class
classref-introduction-group
:::

## Description

**EditorNode3DGizmoPlugin** allows you to define a new type of Gizmo.
There are two main ways to do so: extending **EditorNode3DGizmoPlugin**
for the simpler gizmos, or creating a new
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} type. See the tutorial in the documentation for more info.

To use **EditorNode3DGizmoPlugin**, register it using the
`EditorPlugin.add_node_3d_gizmo_plugin()<class_EditorPlugin_method_add_node_3d_gizmo_plugin>`{.interpreted-text
role="ref"} method first.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Node3D gizmo plugins <../tutorials/plugins/editor/3d_gizmos>`{.interpreted-text
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

## Method Descriptions

:::: {#class_EditorNode3DGizmoPlugin_private_method__begin_handle_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_begin_handle_action**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, handle_id: `int<class_int>`{.interpreted-text role="ref"},
secondary: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__begin_handle_action>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__can_be_hidden}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_can_be_hidden**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__can_be_hidden>`{.interpreted-text
role="ref"}

Override this method to define whether the gizmos handled by this plugin
can be hidden or not. Returns `true` if not overridden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__commit_handle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_commit_handle**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, handle_id: `int<class_int>`{.interpreted-text role="ref"},
secondary: `bool<class_bool>`{.interpreted-text role="ref"}, restore:
`Variant<class_Variant>`{.interpreted-text role="ref"}, cancel:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__commit_handle>`{.interpreted-text
role="ref"}

Override this method to commit a handle being edited (handles must have
been previously added by
`EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} during
`_redraw()<class_EditorNode3DGizmoPlugin_private_method__redraw>`{.interpreted-text
role="ref"}). This usually means creating an
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"} action for the
change, using the current handle value as \"do\" and the `restore`
argument as \"undo\".

If the `cancel` argument is `true`, the `restore` value should be
directly set, without any `UndoRedo<class_UndoRedo>`{.interpreted-text
role="ref"} action.

The `secondary` argument is `true` when the committed handle is
secondary (see
`EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information).

Called for this plugin\'s active gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_commit_subgizmos**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, ids:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}, restores: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}\], cancel: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos>`{.interpreted-text
role="ref"}

Override this method to commit a group of subgizmos being edited (see
`_subgizmos_intersect_ray()<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_ray>`{.interpreted-text
role="ref"} and
`_subgizmos_intersect_frustum()<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_frustum>`{.interpreted-text
role="ref"}). This usually means creating an
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"} action for the
change, using the current transforms as \"do\" and the `restores`
transforms as \"undo\".

If the `cancel` argument is `true`, the `restores` transforms should be
directly set, without any `UndoRedo<class_UndoRedo>`{.interpreted-text
role="ref"} action. As with all subgizmo methods, transforms are given
in local space respect to the gizmo\'s Node3D. Called for this plugin\'s
active gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__create_gizmo}
::: rst-class
classref-method
:::
::::

`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} **\_create_gizmo**(for_node_3d:
`Node3D<class_Node3D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__create_gizmo>`{.interpreted-text
role="ref"}

Override this method to return a custom
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} for the 3D nodes of your choice, return `null` for the rest
of nodes. See also
`_has_gizmo()<class_EditorNode3DGizmoPlugin_private_method__has_gizmo>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__get_gizmo_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_gizmo_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__get_gizmo_name>`{.interpreted-text
role="ref"}

Override this method to provide the name that will appear in the gizmo
visibility menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__get_handle_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_handle_name**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, handle_id: `int<class_int>`{.interpreted-text role="ref"},
secondary: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__get_handle_name>`{.interpreted-text
role="ref"}

Override this method to provide gizmo\'s handle names. The `secondary`
argument is `true` when the requested handle is secondary (see
`EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information). Called for this plugin\'s active
gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__get_handle_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_get_handle_value**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, handle_id: `int<class_int>`{.interpreted-text role="ref"},
secondary: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__get_handle_value>`{.interpreted-text
role="ref"}

Override this method to return the current value of a handle. This value
will be requested at the start of an edit and used as the `restore`
argument in
`_commit_handle()<class_EditorNode3DGizmoPlugin_private_method__commit_handle>`{.interpreted-text
role="ref"}.

The `secondary` argument is `true` when the requested handle is
secondary (see
`EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information).

Called for this plugin\'s active gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__get_priority}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_priority**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__get_priority>`{.interpreted-text
role="ref"}

Override this method to set the gizmo\'s priority. Gizmos with higher
priority will have precedence when processing inputs like handles or
subgizmos selection.

All built-in editor gizmos return a priority of `-1`. If not overridden,
this method will return `0`, which means custom gizmos will
automatically get higher priority than built-in gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__get_subgizmo_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**\_get_subgizmo_transform**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, subgizmo_id: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__get_subgizmo_transform>`{.interpreted-text
role="ref"}

Override this method to return the current transform of a subgizmo. As
with all subgizmo methods, the transform should be in local space
respect to the gizmo\'s Node3D. This transform will be requested at the
start of an edit and used in the `restore` argument in
`_commit_subgizmos()<class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos>`{.interpreted-text
role="ref"}. Called for this plugin\'s active gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__has_gizmo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_has_gizmo**(for_node_3d: `Node3D<class_Node3D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__has_gizmo>`{.interpreted-text
role="ref"}

Override this method to define which Node3D nodes have a gizmo from this
plugin. Whenever a `Node3D<class_Node3D>`{.interpreted-text role="ref"}
node is added to a scene this method is called, if it returns `true` the
node gets a generic
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} assigned and is added to this plugin\'s list of active
gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__is_handle_highlighted}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_handle_highlighted**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, handle_id: `int<class_int>`{.interpreted-text role="ref"},
secondary: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__is_handle_highlighted>`{.interpreted-text
role="ref"}

Override this method to return `true` whenever to given handle should be
highlighted in the editor. The `secondary` argument is `true` when the
requested handle is secondary (see
`EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information). Called for this plugin\'s active
gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__is_selectable_when_hidden}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_selectable_when_hidden**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__is_selectable_when_hidden>`{.interpreted-text
role="ref"}

Override this method to define whether Node3D with this gizmo should be
selectable even when the gizmo is hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__redraw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_redraw**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__redraw>`{.interpreted-text
role="ref"}

Override this method to add all the gizmo elements whenever a gizmo
update is requested. It\'s common to call
`EditorNode3DGizmo.clear()<class_EditorNode3DGizmo_method_clear>`{.interpreted-text
role="ref"} at the beginning of this method and then add visual elements
depending on the node\'s properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__set_handle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_handle**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, handle_id: `int<class_int>`{.interpreted-text role="ref"},
secondary: `bool<class_bool>`{.interpreted-text role="ref"}, camera:
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}, screen_pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__set_handle>`{.interpreted-text
role="ref"}

Override this method to update the node\'s properties when the user
drags a gizmo handle (previously added with
`EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"}). The provided `screen_pos` is the mouse position in screen
coordinates and the `camera` can be used to convert it to raycasts.

The `secondary` argument is `true` when the edited handle is secondary
(see
`EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information).

Called for this plugin\'s active gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__set_subgizmo_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_subgizmo_transform**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, subgizmo_id: `int<class_int>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__set_subgizmo_transform>`{.interpreted-text
role="ref"}

Override this method to update the node properties during subgizmo
editing (see
`_subgizmos_intersect_ray()<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_ray>`{.interpreted-text
role="ref"} and
`_subgizmos_intersect_frustum()<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_frustum>`{.interpreted-text
role="ref"}). The `transform` is given in the Node3D\'s local coordinate
system. Called for this plugin\'s active gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_frustum}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_subgizmos_intersect_frustum**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, camera: `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"}, frustum_planes: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_frustum>`{.interpreted-text
role="ref"}

Override this method to allow selecting subgizmos using mouse drag box
selection. Given a `camera` and `frustum_planes`, this method should
return which subgizmos are contained within the frustums. The
`frustum_planes` argument consists of an array with all the
`Plane<class_Plane>`{.interpreted-text role="ref"}s that make up the
selection frustum. The returned value should contain a list of unique
subgizmo identifiers, these identifiers can have any non-negative value
and will be used in other virtual methods like
`_get_subgizmo_transform()<class_EditorNode3DGizmoPlugin_private_method__get_subgizmo_transform>`{.interpreted-text
role="ref"} or
`_commit_subgizmos()<class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos>`{.interpreted-text
role="ref"}. Called for this plugin\'s active gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_ray}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_subgizmos_intersect_ray**(gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}, camera: `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"}, screen_pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_ray>`{.interpreted-text
role="ref"}

Override this method to allow selecting subgizmos using mouse clicks.
Given a `camera` and a `screen_pos` in screen coordinates, this method
should return which subgizmo should be selected. The returned value
should be a unique subgizmo identifier, which can have any non-negative
value and will be used in other virtual methods like
`_get_subgizmo_transform()<class_EditorNode3DGizmoPlugin_private_method__get_subgizmo_transform>`{.interpreted-text
role="ref"} or
`_commit_subgizmos()<class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos>`{.interpreted-text
role="ref"}. Called for this plugin\'s active gizmos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_method_add_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_material**(name: `String<class_String>`{.interpreted-text
role="ref"}, material:
`StandardMaterial3D<class_StandardMaterial3D>`{.interpreted-text
role="ref"})
`🔗<class_EditorNode3DGizmoPlugin_method_add_material>`{.interpreted-text
role="ref"}

Adds a new material to the internal material list for the plugin. It can
then be accessed with
`get_material()<class_EditorNode3DGizmoPlugin_method_get_material>`{.interpreted-text
role="ref"}. Should not be overridden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_method_create_handle_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_handle_material**(name:
`String<class_String>`{.interpreted-text role="ref"}, billboard:
`bool<class_bool>`{.interpreted-text role="ref"} = false, texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} = null)
`🔗<class_EditorNode3DGizmoPlugin_method_create_handle_material>`{.interpreted-text
role="ref"}

Creates a handle material with its variants (selected and/or editable)
and adds them to the internal material list. They can then be accessed
with
`get_material()<class_EditorNode3DGizmoPlugin_method_get_material>`{.interpreted-text
role="ref"} and used in
`EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"}. Should not be overridden.

You can optionally provide a texture to use instead of the default icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_method_create_icon_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_icon_material**(name: `String<class_String>`{.interpreted-text
role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}, on_top: `bool<class_bool>`{.interpreted-text role="ref"} =
false, color: `Color<class_Color>`{.interpreted-text role="ref"} =
Color(1, 1, 1, 1))
`🔗<class_EditorNode3DGizmoPlugin_method_create_icon_material>`{.interpreted-text
role="ref"}

Creates an icon material with its variants (selected and/or editable)
and adds them to the internal material list. They can then be accessed
with
`get_material()<class_EditorNode3DGizmoPlugin_method_get_material>`{.interpreted-text
role="ref"} and used in
`EditorNode3DGizmo.add_unscaled_billboard()<class_EditorNode3DGizmo_method_add_unscaled_billboard>`{.interpreted-text
role="ref"}. Should not be overridden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_method_create_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_material**(name: `String<class_String>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"},
billboard: `bool<class_bool>`{.interpreted-text role="ref"} = false,
on_top: `bool<class_bool>`{.interpreted-text role="ref"} = false,
use_vertex_color: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_EditorNode3DGizmoPlugin_method_create_material>`{.interpreted-text
role="ref"}

Creates an unshaded material with its variants (selected and/or
editable) and adds them to the internal material list. They can then be
accessed with
`get_material()<class_EditorNode3DGizmoPlugin_method_get_material>`{.interpreted-text
role="ref"} and used in
`EditorNode3DGizmo.add_mesh()<class_EditorNode3DGizmo_method_add_mesh>`{.interpreted-text
role="ref"} and
`EditorNode3DGizmo.add_lines()<class_EditorNode3DGizmo_method_add_lines>`{.interpreted-text
role="ref"}. Should not be overridden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmoPlugin_method_get_material}
::: rst-class
classref-method
:::
::::

`StandardMaterial3D<class_StandardMaterial3D>`{.interpreted-text
role="ref"} **get_material**(name:
`String<class_String>`{.interpreted-text role="ref"}, gizmo:
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} = null)
`🔗<class_EditorNode3DGizmoPlugin_method_get_material>`{.interpreted-text
role="ref"}

Gets material from the internal list of materials. If an
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} is provided, it will try to get the corresponding variant
(selected and/or editable).
