github_url
:   hide

# TileSetScenesCollectionSource {#class_TileSetScenesCollectionSource}

**Inherits:** `TileSetSource<class_TileSetSource>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Exposes a set of scenes as tiles for a
`TileSet<class_TileSet>`{.interpreted-text role="ref"} resource.

::: rst-class
classref-introduction-group
:::

## Description

When placed on a `TileMapLayer<class_TileMapLayer>`{.interpreted-text
role="ref"}, tiles from **TileSetScenesCollectionSource** will
automatically instantiate an associated scene at the cell\'s position in
the TileMapLayer.

Scenes are instantiated as children of the
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"} after
it enters the tree, at the end of the frame (their creation is
deferred). If you add/remove a scene tile in the
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"} that is
already inside the tree, the
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"} will
automatically instantiate/free the scene accordingly.

\*\*Note:\*\* Scene tiles all occupy one tile slot and instead use
alternate tile ID to identify scene index.
`TileSetSource.get_tiles_count()<class_TileSetSource_method_get_tiles_count>`{.interpreted-text
role="ref"} will always return `1`. Use
`get_scene_tiles_count()<class_TileSetScenesCollectionSource_method_get_scene_tiles_count>`{.interpreted-text
role="ref"} to get a number of scenes in a
**TileSetScenesCollectionSource**.

Use this code if you want to find the scene path at a given tile in
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"}:

::::: tabs
::: code-tab
gdscript

var source_id = tile_map_layer.get_cell_source_id(Vector2i(x, y)) if
source_id \> -1: var scene_source =
tile_map_layer.tile_set.get_source(source_id) if scene_source is
TileSetScenesCollectionSource: var alt_id =
tile_map_layer.get_cell_alternative_tile(Vector2i(x, y)) \# The assigned
PackedScene. var scene = scene_source.get_scene_tile_scene(alt_id)
:::

::: code-tab
csharp

int sourceId = tileMapLayer.GetCellSourceId(new Vector2I(x, y)); if
(sourceId \> -1) { TileSetSource source =
tileMapLayer.TileSet.GetSource(sourceId); if (source is
TileSetScenesCollectionSource sceneSource) { int altId =
tileMapLayer.GetCellAlternativeTile(new Vector2I(x, y)); // The assigned
PackedScene. PackedScene scene = sceneSource.GetSceneTileScene(altId); }
}
:::
:::::

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

:::: {#class_TileSetScenesCollectionSource_method_create_scene_tile}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**create_scene_tile**(packed_scene:
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"},
id_override: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_TileSetScenesCollectionSource_method_create_scene_tile>`{.interpreted-text
role="ref"}

Creates a scene-based tile out of the given scene.

Returns a newly generated unique ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_get_next_scene_tile_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_next_scene_tile_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetScenesCollectionSource_method_get_next_scene_tile_id>`{.interpreted-text
role="ref"}

Returns the scene ID a following call to
`create_scene_tile()<class_TileSetScenesCollectionSource_method_create_scene_tile>`{.interpreted-text
role="ref"} would return.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_get_scene_tile_display_placeholder}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_scene_tile_display_placeholder**(id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetScenesCollectionSource_method_get_scene_tile_display_placeholder>`{.interpreted-text
role="ref"}

Returns whether the scene tile with `id` displays a placeholder in the
editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_get_scene_tile_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_scene_tile_id**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileSetScenesCollectionSource_method_get_scene_tile_id>`{.interpreted-text
role="ref"}

Returns the scene tile ID of the scene tile at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_get_scene_tile_scene}
::: rst-class
classref-method
:::
::::

`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}
**get_scene_tile_scene**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TileSetScenesCollectionSource_method_get_scene_tile_scene>`{.interpreted-text
role="ref"}

Returns the `PackedScene<class_PackedScene>`{.interpreted-text
role="ref"} resource of scene tile with `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_get_scene_tiles_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_scene_tiles_count**()
`🔗<class_TileSetScenesCollectionSource_method_get_scene_tiles_count>`{.interpreted-text
role="ref"}

Returns the number or scene tiles this TileSet source has.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_has_scene_tile_id}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_scene_tile_id**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileSetScenesCollectionSource_method_has_scene_tile_id>`{.interpreted-text
role="ref"}

Returns whether this TileSet source has a scene tile with `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_remove_scene_tile}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_scene_tile**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TileSetScenesCollectionSource_method_remove_scene_tile>`{.interpreted-text
role="ref"}

Remove the scene tile with `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_set_scene_tile_display_placeholder}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_scene_tile_display_placeholder**(id:
`int<class_int>`{.interpreted-text role="ref"}, display_placeholder:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TileSetScenesCollectionSource_method_set_scene_tile_display_placeholder>`{.interpreted-text
role="ref"}

Sets whether or not the scene tile with `id` should display a
placeholder in the editor. This might be useful for scenes that are not
visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_set_scene_tile_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_scene_tile_id**(id: `int<class_int>`{.interpreted-text
role="ref"}, new_id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TileSetScenesCollectionSource_method_set_scene_tile_id>`{.interpreted-text
role="ref"}

Changes a scene tile\'s ID from `id` to `new_id`. This will fail if
there is already a tile with an ID equal to `new_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TileSetScenesCollectionSource_method_set_scene_tile_scene}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_scene_tile_scene**(id: `int<class_int>`{.interpreted-text
role="ref"}, packed_scene:
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"})
`🔗<class_TileSetScenesCollectionSource_method_set_scene_tile_scene>`{.interpreted-text
role="ref"}

Assigns a `PackedScene<class_PackedScene>`{.interpreted-text role="ref"}
resource to the scene tile with `id`. This will fail if the scene does
not extend `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"},
as positioning properties are needed to place the scene on the
`TileMapLayer<class_TileMapLayer>`{.interpreted-text role="ref"}.
