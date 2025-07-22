github_url
:   hide

# Polygon2D {#class_Polygon2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D polygon.

::: rst-class
classref-introduction-group
:::

## Description

A Polygon2D is defined by a set of points. Each point is connected to
the next, with the final point being connected to the first, resulting
in a closed polygon. Polygon2Ds can be filled with color (solid or
gradient) or filled with a given texture.

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

## Property Descriptions

:::: {#class_Polygon2D_property_antialiased}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **antialiased** =
`false` `🔗<class_Polygon2D_property_antialiased>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_antialiased**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_antialiased**()

If `true`, polygon edges will be anti-aliased.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(1, 1, 1, 1)`
`🔗<class_Polygon2D_property_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

The polygon\'s fill color. If
`texture<class_Polygon2D_property_texture>`{.interpreted-text
role="ref"} is set, it will be multiplied by this color. It will also be
the default color for vertices not set in
`vertex_colors<class_Polygon2D_property_vertex_colors>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_internal_vertex_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **internal_vertex_count**
= `0`
`🔗<class_Polygon2D_property_internal_vertex_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_internal_vertex_count**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_internal_vertex_count**()

Number of internal vertices, used for UV mapping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_invert_border}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **invert_border** =
`100.0` `🔗<class_Polygon2D_property_invert_border>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_invert_border**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_invert_border**()

Added padding applied to the bounding box when
`invert_enabled<class_Polygon2D_property_invert_enabled>`{.interpreted-text
role="ref"} is set to `true`. Setting this value too small may result in
a \"Bad Polygon\" error.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_invert_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **invert_enabled** =
`false` `🔗<class_Polygon2D_property_invert_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_invert_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_invert_enabled**()

If `true`, the polygon will be inverted, containing the area outside the
defined points and extending to the
`invert_border<class_Polygon2D_property_invert_border>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)` `🔗<class_Polygon2D_property_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_offset**()

The offset applied to each vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_polygon}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **polygon** = `PackedVector2Array()`
`🔗<class_Polygon2D_property_polygon>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_polygon**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_polygon**()

The polygon\'s list of vertices. The final point will be connected to
the first.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_polygons}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **polygons** = `[]`
`🔗<class_Polygon2D_property_polygons>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_polygons**(value: `Array<class_Array>`{.interpreted-text
  role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"} **get_polygons**()

The list of polygons, in case more than one is being represented. Every
individual polygon is stored as a
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
where each `int<class_int>`{.interpreted-text role="ref"} is an index to
a point in `polygon<class_Polygon2D_property_polygon>`{.interpreted-text
role="ref"}. If empty, this property will be ignored, and the resulting
single polygon will be composed of all points in
`polygon<class_Polygon2D_property_polygon>`{.interpreted-text
role="ref"}, using the order they are stored in.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_skeleton}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **skeleton** =
`NodePath("")` `🔗<class_Polygon2D_property_skeleton>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_skeleton**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_skeleton**()

Path to a `Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"}
node used for skeleton-based deformations of this polygon. If empty or
invalid, skeletal deformations will not be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_Polygon2D_property_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

The polygon\'s fill texture. Use
`uv<class_Polygon2D_property_uv>`{.interpreted-text role="ref"} to set
texture coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_texture_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**texture_offset** = `Vector2(0, 0)`
`🔗<class_Polygon2D_property_texture_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_texture_offset**()

Amount to offset the polygon\'s
`texture<class_Polygon2D_property_texture>`{.interpreted-text
role="ref"}. If set to `Vector2(0, 0)`, the texture\'s origin (its
top-left corner) will be placed at the polygon\'s position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_texture_rotation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **texture_rotation**
= `0.0`
`🔗<class_Polygon2D_property_texture_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_rotation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_texture_rotation**()

The texture\'s rotation in radians.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_texture_scale}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **texture_scale**
= `Vector2(1, 1)`
`🔗<class_Polygon2D_property_texture_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_scale**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_texture_scale**()

Amount to multiply the
`uv<class_Polygon2D_property_uv>`{.interpreted-text role="ref"}
coordinates when using
`texture<class_Polygon2D_property_texture>`{.interpreted-text
role="ref"}. Larger values make the texture smaller, and vice versa.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_uv}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **uv** = `PackedVector2Array()`
`🔗<class_Polygon2D_property_uv>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_uv**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_uv**()

Texture coordinates for each vertex of the polygon. There should be one
UV value per polygon vertex. If there are fewer, undefined vertices will
use `Vector2(0, 0)`.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_property_vertex_colors}
::: rst-class
classref-property
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**vertex_colors** = `PackedColorArray()`
`🔗<class_Polygon2D_property_vertex_colors>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertex_colors**(value:
  `PackedColorArray<class_PackedColorArray>`{.interpreted-text
  role="ref"})
- `PackedColorArray<class_PackedColorArray>`{.interpreted-text
  role="ref"} **get_vertex_colors**()

Color for each vertex. Colors are interpolated between vertices,
resulting in smooth gradients. There should be one per polygon vertex.
If there are fewer, undefined vertices will use
`color<class_Polygon2D_property_color>`{.interpreted-text role="ref"}.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Polygon2D_method_add_bone}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_bone**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"}, weights:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}) `🔗<class_Polygon2D_method_add_bone>`{.interpreted-text
role="ref"}

Adds a bone with the specified `path` and `weights`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_method_clear_bones}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_bones**()
`🔗<class_Polygon2D_method_clear_bones>`{.interpreted-text role="ref"}

Removes all bones from this **Polygon2D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_method_erase_bone}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_bone**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Polygon2D_method_erase_bone>`{.interpreted-text role="ref"}

Removes the specified bone from this **Polygon2D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_method_get_bone_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_bone_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Polygon2D_method_get_bone_count>`{.interpreted-text
role="ref"}

Returns the number of bones in this **Polygon2D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_method_get_bone_path}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_bone_path**(index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Polygon2D_method_get_bone_path>`{.interpreted-text role="ref"}

Returns the path to the node associated with the specified bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_method_get_bone_weights}
::: rst-class
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **get_bone_weights**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Polygon2D_method_get_bone_weights>`{.interpreted-text
role="ref"}

Returns the weight values of the specified bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_method_set_bone_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_path**(index: `int<class_int>`{.interpreted-text role="ref"},
path: `NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_Polygon2D_method_set_bone_path>`{.interpreted-text role="ref"}

Sets the path to the node associated with the specified bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Polygon2D_method_set_bone_weights}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bone_weights**(index: `int<class_int>`{.interpreted-text
role="ref"}, weights:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_Polygon2D_method_set_bone_weights>`{.interpreted-text
role="ref"}

Sets the weight values for the specified bone.
