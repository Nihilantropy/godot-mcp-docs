github_url
:   hide

::: {.meta keywords="tilemap"}
:::

# GridMapEditorPlugin {#class_GridMapEditorPlugin}

**Inherits:** `EditorPlugin<class_EditorPlugin>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Editor for `GridMap<class_GridMap>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-introduction-group
:::

## Description

GridMapEditorPlugin provides access to the
`GridMap<class_GridMap>`{.interpreted-text role="ref"} editor
functionality.

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

:::: {#class_GridMapEditorPlugin_method_clear_selection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_selection**()
`🔗<class_GridMapEditorPlugin_method_clear_selection>`{.interpreted-text
role="ref"}

Deselects any currently selected cells.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMapEditorPlugin_method_get_current_grid_map}
::: rst-class
classref-method
:::
::::

`GridMap<class_GridMap>`{.interpreted-text role="ref"}
**get_current_grid_map**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMapEditorPlugin_method_get_current_grid_map>`{.interpreted-text
role="ref"}

Returns the `GridMap<class_GridMap>`{.interpreted-text role="ref"} node
currently edited by the grid map editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMapEditorPlugin_method_get_selected_cells}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_selected_cells**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMapEditorPlugin_method_get_selected_cells>`{.interpreted-text
role="ref"}

Returns an array of `Vector3i<class_Vector3i>`{.interpreted-text
role="ref"}s with the selected cells\' coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMapEditorPlugin_method_get_selected_palette_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selected_palette_item**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMapEditorPlugin_method_get_selected_palette_item>`{.interpreted-text
role="ref"}

Returns the index of the selected
`MeshLibrary<class_MeshLibrary>`{.interpreted-text role="ref"} item in
the grid map editor\'s palette or `-1` if no item is selected.

\*\*Note:\*\* The indices might not be in the same order as they appear
in the editor\'s interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMapEditorPlugin_method_get_selection}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **get_selection**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMapEditorPlugin_method_get_selection>`{.interpreted-text
role="ref"}

Returns the cell coordinate bounds of the current selection. Use
`has_selection()<class_GridMapEditorPlugin_method_has_selection>`{.interpreted-text
role="ref"} to check if there is an active selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMapEditorPlugin_method_has_selection}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_selection**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMapEditorPlugin_method_has_selection>`{.interpreted-text
role="ref"}

Returns `true` if there are selected cells.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMapEditorPlugin_method_set_selected_palette_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_selected_palette_item**(item: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GridMapEditorPlugin_method_set_selected_palette_item>`{.interpreted-text
role="ref"}

Selects the `MeshLibrary<class_MeshLibrary>`{.interpreted-text
role="ref"} item with the given index in the grid map editor\'s palette.
If a negative index is given, no item will be selected. If a value
greater than the last index is given, the last item will be selected.

\*\*Note:\*\* The indices might not be in the same order as they appear
in the editor\'s interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridMapEditorPlugin_method_set_selection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_selection**(begin: `Vector3i<class_Vector3i>`{.interpreted-text
role="ref"}, end: `Vector3i<class_Vector3i>`{.interpreted-text
role="ref"})
`🔗<class_GridMapEditorPlugin_method_set_selection>`{.interpreted-text
role="ref"}

Selects the cells inside the given bounds from `begin` to `end`.
