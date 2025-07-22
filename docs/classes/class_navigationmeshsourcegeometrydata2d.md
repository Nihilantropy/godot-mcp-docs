github_url
:   hide

# NavigationMeshSourceGeometryData2D {#class_NavigationMeshSourceGeometryData2D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Container for parsed source geometry data used in navigation mesh
baking.

::: rst-class
classref-introduction-group
:::

## Description

Container for parsed source geometry data used in navigation mesh
baking.

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

:::: {#class_NavigationMeshSourceGeometryData2D_method_add_obstruction_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_obstruction_outline**(shape_outline:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMeshSourceGeometryData2D_method_add_obstruction_outline>`{.interpreted-text
role="ref"}

Adds the outline points of a shape as obstructed area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_add_projected_obstruction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_projected_obstruction**(vertices:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, carve: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationMeshSourceGeometryData2D_method_add_projected_obstruction>`{.interpreted-text
role="ref"}

Adds a projected obstruction shape to the source geometry. If `carve` is
`true` the carved shape will not be affected by additional offsets (e.g.
agent radius) of the navigation mesh baking process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_add_traversable_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_traversable_outline**(shape_outline:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMeshSourceGeometryData2D_method_add_traversable_outline>`{.interpreted-text
role="ref"}

Adds the outline points of a shape as traversable area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_append_obstruction_outlines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_obstruction_outlines**(obstruction_outlines:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\])
`🔗<class_NavigationMeshSourceGeometryData2D_method_append_obstruction_outlines>`{.interpreted-text
role="ref"}

Appends another array of `obstruction_outlines` at the end of the
existing obstruction outlines array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_append_traversable_outlines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_traversable_outlines**(traversable_outlines:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\])
`🔗<class_NavigationMeshSourceGeometryData2D_method_append_traversable_outlines>`{.interpreted-text
role="ref"}

Appends another array of `traversable_outlines` at the end of the
existing traversable outlines array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_NavigationMeshSourceGeometryData2D_method_clear>`{.interpreted-text
role="ref"}

Clears the internal data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_clear_projected_obstructions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_projected_obstructions**()
`🔗<class_NavigationMeshSourceGeometryData2D_method_clear_projected_obstructions>`{.interpreted-text
role="ref"}

Clears all projected obstructions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_get_bounds}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_bounds**()
`🔗<class_NavigationMeshSourceGeometryData2D_method_get_bounds>`{.interpreted-text
role="ref"}

Returns an axis-aligned bounding box that covers all the stored geometry
data. The bounds are calculated when calling this function with the
result cached until further geometry changes are made.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_get_obstruction_outlines}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **get_obstruction_outlines**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationMeshSourceGeometryData2D_method_get_obstruction_outlines>`{.interpreted-text
role="ref"}

Returns all the obstructed area outlines arrays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_get_projected_obstructions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_projected_obstructions**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationMeshSourceGeometryData2D_method_get_projected_obstructions>`{.interpreted-text
role="ref"}

Returns the projected obstructions as an
`Array<class_Array>`{.interpreted-text role="ref"} of dictionaries. Each
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} contains
the following entries:

- `vertices` - A
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} that defines the outline points of the projected shape.
- `carve` - A `bool<class_bool>`{.interpreted-text role="ref"} that
  defines how the projected shape affects the navigation mesh baking. If
  `true` the projected shape will not be affected by addition offsets,
  e.g. agent radius.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_get_traversable_outlines}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **get_traversable_outlines**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationMeshSourceGeometryData2D_method_get_traversable_outlines>`{.interpreted-text
role="ref"}

Returns all the traversable area outlines arrays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_has_data}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_data**()
`🔗<class_NavigationMeshSourceGeometryData2D_method_has_data>`{.interpreted-text
role="ref"}

Returns `true` when parsed source geometry data exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_merge}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**merge**(other_geometry:
`NavigationMeshSourceGeometryData2D<class_NavigationMeshSourceGeometryData2D>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMeshSourceGeometryData2D_method_merge>`{.interpreted-text
role="ref"}

Adds the geometry data of another **NavigationMeshSourceGeometryData2D**
to the navigation mesh baking data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_set_obstruction_outlines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_obstruction_outlines**(obstruction_outlines:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\])
`🔗<class_NavigationMeshSourceGeometryData2D_method_set_obstruction_outlines>`{.interpreted-text
role="ref"}

Sets all the obstructed area outlines arrays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_set_projected_obstructions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_projected_obstructions**(projected_obstructions:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_NavigationMeshSourceGeometryData2D_method_set_projected_obstructions>`{.interpreted-text
role="ref"}

Sets the projected obstructions with an Array of Dictionaries with the
following key value pairs:

:::: tabs
::: code-tab
gdscript

\"vertices\" : PackedFloat32Array \"carve\" : bool
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData2D_method_set_traversable_outlines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_traversable_outlines**(traversable_outlines:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\])
`🔗<class_NavigationMeshSourceGeometryData2D_method_set_traversable_outlines>`{.interpreted-text
role="ref"}

Sets all the traversable area outlines arrays.
