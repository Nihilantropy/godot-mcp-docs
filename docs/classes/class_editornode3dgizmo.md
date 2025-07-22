github_url
:   hide

# EditorNode3DGizmo {#class_EditorNode3DGizmo}

**Inherits:** `Node3DGizmo<class_Node3DGizmo>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Gizmo for editing `Node3D<class_Node3D>`{.interpreted-text role="ref"}
objects.

::: rst-class
classref-introduction-group
:::

## Description

Gizmo that is used for providing custom visualization and editing
(handles and subgizmos) for `Node3D<class_Node3D>`{.interpreted-text
role="ref"} objects. Can be overridden to create custom gizmos, but for
simple gizmos creating an
`EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>`{.interpreted-text
role="ref"} is usually recommended.

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

:::: {#class_EditorNode3DGizmo_private_method__begin_handle_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_begin_handle_action**(id: `int<class_int>`{.interpreted-text
role="ref"}, secondary: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__begin_handle_action>`{.interpreted-text
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

:::: {#class_EditorNode3DGizmo_private_method__commit_handle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_commit_handle**(id: `int<class_int>`{.interpreted-text role="ref"},
secondary: `bool<class_bool>`{.interpreted-text role="ref"}, restore:
`Variant<class_Variant>`{.interpreted-text role="ref"}, cancel:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__commit_handle>`{.interpreted-text
role="ref"}

Override this method to commit a handle being edited (handles must have
been previously added by
`add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"}). This usually means creating an
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"} action for the
change, using the current handle value as \"do\" and the `restore`
argument as \"undo\".

If the `cancel` argument is `true`, the `restore` value should be
directly set, without any `UndoRedo<class_UndoRedo>`{.interpreted-text
role="ref"} action.

The `secondary` argument is `true` when the committed handle is
secondary (see
`add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__commit_subgizmos}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_commit_subgizmos**(ids:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}, restores: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}\], cancel: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__commit_subgizmos>`{.interpreted-text
role="ref"}

Override this method to commit a group of subgizmos being edited (see
`_subgizmos_intersect_ray()<class_EditorNode3DGizmo_private_method__subgizmos_intersect_ray>`{.interpreted-text
role="ref"} and
`_subgizmos_intersect_frustum()<class_EditorNode3DGizmo_private_method__subgizmos_intersect_frustum>`{.interpreted-text
role="ref"}). This usually means creating an
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"} action for the
change, using the current transforms as \"do\" and the `restores`
transforms as \"undo\".

If the `cancel` argument is `true`, the `restores` transforms should be
directly set, without any `UndoRedo<class_UndoRedo>`{.interpreted-text
role="ref"} action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__get_handle_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_handle_name**(id: `int<class_int>`{.interpreted-text
role="ref"}, secondary: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__get_handle_name>`{.interpreted-text
role="ref"}

Override this method to return the name of an edited handle (handles
must have been previously added by
`add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"}). Handles can be named for reference to the user when
editing.

The `secondary` argument is `true` when the requested handle is
secondary (see
`add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__get_handle_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_get_handle_value**(id: `int<class_int>`{.interpreted-text
role="ref"}, secondary: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__get_handle_value>`{.interpreted-text
role="ref"}

Override this method to return the current value of a handle. This value
will be requested at the start of an edit and used as the `restore`
argument in
`_commit_handle()<class_EditorNode3DGizmo_private_method__commit_handle>`{.interpreted-text
role="ref"}.

The `secondary` argument is `true` when the requested handle is
secondary (see
`add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__get_subgizmo_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**\_get_subgizmo_transform**(id: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__get_subgizmo_transform>`{.interpreted-text
role="ref"}

Override this method to return the current transform of a subgizmo. This
transform will be requested at the start of an edit and used as the
`restore` argument in
`_commit_subgizmos()<class_EditorNode3DGizmo_private_method__commit_subgizmos>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__is_handle_highlighted}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_handle_highlighted**(id: `int<class_int>`{.interpreted-text
role="ref"}, secondary: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__is_handle_highlighted>`{.interpreted-text
role="ref"}

Override this method to return `true` whenever the given handle should
be highlighted in the editor.

The `secondary` argument is `true` when the requested handle is
secondary (see
`add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__redraw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_redraw**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__redraw>`{.interpreted-text
role="ref"}

Override this method to add all the gizmo elements whenever a gizmo
update is requested. It\'s common to call
`clear()<class_EditorNode3DGizmo_method_clear>`{.interpreted-text
role="ref"} at the beginning of this method and then add visual elements
depending on the node\'s properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__set_handle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_handle**(id: `int<class_int>`{.interpreted-text role="ref"},
secondary: `bool<class_bool>`{.interpreted-text role="ref"}, camera:
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}, point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__set_handle>`{.interpreted-text
role="ref"}

Override this method to update the node properties when the user drags a
gizmo handle (previously added with
`add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"}). The provided `point` is the mouse position in screen
coordinates and the `camera` can be used to convert it to raycasts.

The `secondary` argument is `true` when the edited handle is secondary
(see
`add_handles()<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"} for more information).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__set_subgizmo_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_subgizmo_transform**(id: `int<class_int>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__set_subgizmo_transform>`{.interpreted-text
role="ref"}

Override this method to update the node properties during subgizmo
editing (see
`_subgizmos_intersect_ray()<class_EditorNode3DGizmo_private_method__subgizmos_intersect_ray>`{.interpreted-text
role="ref"} and
`_subgizmos_intersect_frustum()<class_EditorNode3DGizmo_private_method__subgizmos_intersect_frustum>`{.interpreted-text
role="ref"}). The `transform` is given in the
`Node3D<class_Node3D>`{.interpreted-text role="ref"}\'s local coordinate
system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__subgizmos_intersect_frustum}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_subgizmos_intersect_frustum**(camera:
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}, frustum:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__subgizmos_intersect_frustum>`{.interpreted-text
role="ref"}

Override this method to allow selecting subgizmos using mouse drag box
selection. Given a `camera` and a `frustum`, this method should return
which subgizmos are contained within the frustum. The `frustum` argument
consists of an array with all the `Plane<class_Plane>`{.interpreted-text
role="ref"}s that make up the selection frustum. The returned value
should contain a list of unique subgizmo identifiers, which can have any
non-negative value and will be used in other virtual methods like
`_get_subgizmo_transform()<class_EditorNode3DGizmo_private_method__get_subgizmo_transform>`{.interpreted-text
role="ref"} or
`_commit_subgizmos()<class_EditorNode3DGizmo_private_method__commit_subgizmos>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_private_method__subgizmos_intersect_ray}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_subgizmos_intersect_ray**(camera:
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}, point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_private_method__subgizmos_intersect_ray>`{.interpreted-text
role="ref"}

Override this method to allow selecting subgizmos using mouse clicks.
Given a `camera` and a `point` in screen coordinates, this method should
return which subgizmo should be selected. The returned value should be a
unique subgizmo identifier, which can have any non-negative value and
will be used in other virtual methods like
`_get_subgizmo_transform()<class_EditorNode3DGizmo_private_method__get_subgizmo_transform>`{.interpreted-text
role="ref"} or
`_commit_subgizmos()<class_EditorNode3DGizmo_private_method__commit_subgizmos>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_add_collision_segments}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_collision_segments**(segments:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"})
`🔗<class_EditorNode3DGizmo_method_add_collision_segments>`{.interpreted-text
role="ref"}

Adds the specified `segments` to the gizmo\'s collision shape for
picking. Call this method during
`_redraw()<class_EditorNode3DGizmo_private_method__redraw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_add_collision_triangles}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_collision_triangles**(triangles:
`TriangleMesh<class_TriangleMesh>`{.interpreted-text role="ref"})
`🔗<class_EditorNode3DGizmo_method_add_collision_triangles>`{.interpreted-text
role="ref"}

Adds collision triangles to the gizmo for picking. A
`TriangleMesh<class_TriangleMesh>`{.interpreted-text role="ref"} can be
generated from a regular `Mesh<class_Mesh>`{.interpreted-text
role="ref"} too. Call this method during
`_redraw()<class_EditorNode3DGizmo_private_method__redraw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_add_handles}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_handles**(handles:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, material: `Material<class_Material>`{.interpreted-text
role="ref"}, ids:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}, billboard: `bool<class_bool>`{.interpreted-text role="ref"}
= false, secondary: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_EditorNode3DGizmo_method_add_handles>`{.interpreted-text
role="ref"}

Adds a list of handles (points) which can be used to edit the properties
of the gizmo\'s `Node3D<class_Node3D>`{.interpreted-text role="ref"}.
The `ids` argument can be used to specify a custom identifier for each
handle, if an empty array is passed, the ids will be assigned
automatically from the `handles` argument order.

The `secondary` argument marks the added handles as secondary, meaning
they will normally have lower selection priority than regular handles.
When the user is holding the shift key secondary handles will switch to
have higher priority than regular handles. This change in priority can
be used to place multiple handles at the same point while still giving
the user control on their selection.

There are virtual methods which will be called upon editing of these
handles. Call this method during
`_redraw()<class_EditorNode3DGizmo_private_method__redraw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_add_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_lines**(lines:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, material: `Material<class_Material>`{.interpreted-text
role="ref"}, billboard: `bool<class_bool>`{.interpreted-text role="ref"}
= false, modulate: `Color<class_Color>`{.interpreted-text role="ref"} =
Color(1, 1, 1, 1))
`🔗<class_EditorNode3DGizmo_method_add_lines>`{.interpreted-text
role="ref"}

Adds lines to the gizmo (as sets of 2 points), with a given material.
The lines are used for visualizing the gizmo. Call this method during
`_redraw()<class_EditorNode3DGizmo_private_method__redraw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_add_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_mesh**(mesh: `Mesh<class_Mesh>`{.interpreted-text role="ref"},
material: `Material<class_Material>`{.interpreted-text role="ref"} =
null, transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), skeleton:
`SkinReference<class_SkinReference>`{.interpreted-text role="ref"} =
null) `🔗<class_EditorNode3DGizmo_method_add_mesh>`{.interpreted-text
role="ref"}

Adds a mesh to the gizmo with the specified `material`, local
`transform` and `skeleton`. Call this method during
`_redraw()<class_EditorNode3DGizmo_private_method__redraw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_add_unscaled_billboard}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_unscaled_billboard**(material:
`Material<class_Material>`{.interpreted-text role="ref"}, default_scale:
`float<class_float>`{.interpreted-text role="ref"} = 1, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1))
`🔗<class_EditorNode3DGizmo_method_add_unscaled_billboard>`{.interpreted-text
role="ref"}

Adds an unscaled billboard for visualization and selection. Call this
method during
`_redraw()<class_EditorNode3DGizmo_private_method__redraw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_EditorNode3DGizmo_method_clear>`{.interpreted-text role="ref"}

Removes everything in the gizmo including meshes, collisions and
handles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_get_node_3d}
::: rst-class
classref-method
:::
::::

`Node3D<class_Node3D>`{.interpreted-text role="ref"} **get_node_3d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_method_get_node_3d>`{.interpreted-text
role="ref"}

Returns the `Node3D<class_Node3D>`{.interpreted-text role="ref"} node
associated with this gizmo.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_get_plugin}
::: rst-class
classref-method
:::
::::

`EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>`{.interpreted-text
role="ref"} **get_plugin**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_method_get_plugin>`{.interpreted-text
role="ref"}

Returns the
`EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>`{.interpreted-text
role="ref"} that owns this gizmo. It\'s useful to retrieve materials
using
`EditorNode3DGizmoPlugin.get_material()<class_EditorNode3DGizmoPlugin_method_get_material>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_get_subgizmo_selection}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_subgizmo_selection**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_method_get_subgizmo_selection>`{.interpreted-text
role="ref"}

Returns a list of the currently selected subgizmos. Can be used to
highlight selected elements during
`_redraw()<class_EditorNode3DGizmo_private_method__redraw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_is_subgizmo_selected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_subgizmo_selected**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorNode3DGizmo_method_is_subgizmo_selected>`{.interpreted-text
role="ref"}

Returns `true` if the given subgizmo is currently selected. Can be used
to highlight selected elements during
`_redraw()<class_EditorNode3DGizmo_private_method__redraw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_set_hidden}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_hidden**(hidden: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorNode3DGizmo_method_set_hidden>`{.interpreted-text
role="ref"}

Sets the gizmo\'s hidden state. If `true`, the gizmo will be hidden. If
`false`, it will be shown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorNode3DGizmo_method_set_node_3d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_node_3d**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_EditorNode3DGizmo_method_set_node_3d>`{.interpreted-text
role="ref"}

Sets the reference `Node3D<class_Node3D>`{.interpreted-text role="ref"}
node for the gizmo. `node` must inherit from
`Node3D<class_Node3D>`{.interpreted-text role="ref"}.
