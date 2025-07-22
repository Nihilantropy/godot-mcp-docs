github_url
:   hide

# PolygonPathFinder {#class_PolygonPathFinder}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

::: {.container .contribute}
There is currently no description for this class. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

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

:::: {#class_PolygonPathFinder_method_find_path}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **find_path**(from:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, to:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_PolygonPathFinder_method_find_path>`{.interpreted-text
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

:::: {#class_PolygonPathFinder_method_get_bounds}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_bounds**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PolygonPathFinder_method_get_bounds>`{.interpreted-text
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

:::: {#class_PolygonPathFinder_method_get_closest_point}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_closest_point**(point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PolygonPathFinder_method_get_closest_point>`{.interpreted-text
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

:::: {#class_PolygonPathFinder_method_get_intersections}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **get_intersections**(from:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, to:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PolygonPathFinder_method_get_intersections>`{.interpreted-text
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

:::: {#class_PolygonPathFinder_method_get_point_penalty}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_point_penalty**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PolygonPathFinder_method_get_point_penalty>`{.interpreted-text
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

:::: {#class_PolygonPathFinder_method_is_point_inside}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_point_inside**(point: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PolygonPathFinder_method_is_point_inside>`{.interpreted-text
role="ref"}

Returns `true` if `point` falls inside the polygon area.

::::: tabs
::: code-tab
gdscript

var polygon_path_finder = PolygonPathFinder.new() var points =
\[Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)\] var
connections = \[0, 1, 1, 2, 2, 0\] polygon_path_finder.setup(points,
connections) print(polygon_path_finder.is_point_inside(Vector2(0.2,
0.2))) \# Prints true
print(polygon_path_finder.is_point_inside(Vector2(1.0, 1.0))) \# Prints
false
:::

::: code-tab
csharp

var polygonPathFinder = new PolygonPathFinder(); Vector2\[\] points = \[
new Vector2(0.0f, 0.0f), new Vector2(1.0f, 0.0f), new Vector2(0.0f,
1.0f) \]; int\[\] connections = \[0, 1, 1, 2, 2, 0\];
polygonPathFinder.Setup(points, connections);
GD.Print(polygonPathFinder.IsPointInside(new Vector2(0.2f, 0.2f))); //
Prints True GD.Print(polygonPathFinder.IsPointInside(new Vector2(1.0f,
1.0f))); // Prints False
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PolygonPathFinder_method_set_point_penalty}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_point_penalty**(idx: `int<class_int>`{.interpreted-text
role="ref"}, penalty: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_PolygonPathFinder_method_set_point_penalty>`{.interpreted-text
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

:::: {#class_PolygonPathFinder_method_setup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**setup**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, connections:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_PolygonPathFinder_method_setup>`{.interpreted-text role="ref"}

Sets up **PolygonPathFinder** with an array of points that define the
vertices of the polygon, and an array of indices that determine the
edges of the polygon.

The length of `connections` must be even, returns an error if odd.

::::: tabs
::: code-tab
gdscript

var polygon_path_finder = PolygonPathFinder.new() var points =
\[Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)\] var
connections = \[0, 1, 1, 2, 2, 0\] polygon_path_finder.setup(points,
connections)
:::

::: code-tab
csharp

var polygonPathFinder = new PolygonPathFinder(); Vector2\[\] points = \[
new Vector2(0.0f, 0.0f), new Vector2(1.0f, 0.0f), new Vector2(0.0f,
1.0f) \]; int\[\] connections = \[0, 1, 1, 2, 2, 0\];
polygonPathFinder.Setup(points, connections);
:::
:::::
