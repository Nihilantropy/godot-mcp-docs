github_url
:   hide

# AABB {#class_AABB}

A 3D axis-aligned bounding box.

::: rst-class
classref-introduction-group
:::

## Description

The **AABB** built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type represents an axis-aligned bounding box in a 3D space.
It is defined by its
`position<class_AABB_property_position>`{.interpreted-text role="ref"}
and `size<class_AABB_property_size>`{.interpreted-text role="ref"},
which are `Vector3<class_Vector3>`{.interpreted-text role="ref"}. It is
frequently used for fast overlap tests (see
`intersects()<class_AABB_method_intersects>`{.interpreted-text
role="ref"}). Although **AABB** itself is axis-aligned, it can be
combined with `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} to represent a rotated or skewed bounding box.

It uses floating-point coordinates. The 2D counterpart to **AABB** is
`Rect2<class_Rect2>`{.interpreted-text role="ref"}. There is no version
of **AABB** that uses integer coordinates.

\*\*Note:\*\* Negative values for
`size<class_AABB_property_size>`{.interpreted-text role="ref"} are not
supported. With negative size, most **AABB** methods do not work
correctly. Use `abs()<class_AABB_method_abs>`{.interpreted-text
role="ref"} to get an equivalent **AABB** with a non-negative size.

\*\*Note:\*\* In a boolean context, an **AABB** evaluates to `false` if
both `position<class_AABB_property_position>`{.interpreted-text
role="ref"} and `size<class_AABB_property_size>`{.interpreted-text
role="ref"} are zero (equal to
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}). Otherwise, it always evaluates to `true`.

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Math documentation index <../tutorials/math/index>`{.interpreted-text
  role="doc"}
- `Vector math <../tutorials/math/vector_math>`{.interpreted-text
  role="doc"}
- `Advanced vector math <../tutorials/math/vectors_advanced>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Constructors

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Operators

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AABB_property_end}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **end** =
`Vector3(0, 0, 0)` `🔗<class_AABB_property_end>`{.interpreted-text
role="ref"}

The ending point. This is usually the corner on the top-right and back
of the bounding box, and is equivalent to `position + size`. Setting
this point affects the
`size<class_AABB_property_size>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_property_position}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **position** =
`Vector3(0, 0, 0)` `🔗<class_AABB_property_position>`{.interpreted-text
role="ref"}

The origin point. This is usually the corner on the bottom-left and
forward of the bounding box.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(0, 0, 0)` `🔗<class_AABB_property_size>`{.interpreted-text
role="ref"}

The bounding box\'s width, height, and depth starting from
`position<class_AABB_property_position>`{.interpreted-text role="ref"}.
Setting this value also affects the
`end<class_AABB_property_end>`{.interpreted-text role="ref"} point.

\*\*Note:\*\* It\'s recommended setting the width, height, and depth to
non-negative values. This is because most methods in Godot assume that
the `position<class_AABB_property_position>`{.interpreted-text
role="ref"} is the bottom-left-forward corner, and the
`end<class_AABB_property_end>`{.interpreted-text role="ref"} is the
top-right-back corner. To get an equivalent bounding box with
non-negative size, use `abs()<class_AABB_method_abs>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_AABB_constructor_AABB}
::: rst-class
classref-constructor
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **AABB**()
`🔗<class_AABB_constructor_AABB>`{.interpreted-text role="ref"}

Constructs an **AABB** with its
`position<class_AABB_property_position>`{.interpreted-text role="ref"}
and `size<class_AABB_property_size>`{.interpreted-text role="ref"} set
to `Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`AABB<class_AABB>`{.interpreted-text role="ref"} **AABB**(from:
`AABB<class_AABB>`{.interpreted-text role="ref"})

Constructs an **AABB** as a copy of the given **AABB**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`AABB<class_AABB>`{.interpreted-text role="ref"} **AABB**(position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, size:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})

Constructs an **AABB** by `position` and `size`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AABB_method_abs}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **abs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_abs>`{.interpreted-text role="ref"}

Returns an **AABB** equivalent to this bounding box, with its width,
height, and depth modified to be non-negative values.

::::: tabs
::: code-tab
gdscript

var box = AABB(Vector3(5, 0, 5), Vector3(-20, -10, -5)) var absolute =
box.abs() print(absolute.position) \# Prints (-15.0, -10.0, 0.0)
print(absolute.size) \# Prints (20.0, 10.0, 5.0)
:::

::: code-tab
csharp

var box = new Aabb(new Vector3(5, 0, 5), new Vector3(-20, -10, -5)); var
absolute = box.Abs(); GD.Print(absolute.Position); // Prints (-15, -10,
0) GD.Print(absolute.Size); // Prints (20, 10, 5)
:::
:::::

\*\*Note:\*\* It\'s recommended to use this method when
`size<class_AABB_property_size>`{.interpreted-text role="ref"} is
negative, as most other methods in Godot assume that the
`size<class_AABB_property_size>`{.interpreted-text role="ref"}\'s
components are greater than `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_encloses}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **encloses**(with:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_encloses>`{.interpreted-text
role="ref"}

Returns `true` if this bounding box *completely* encloses the `with`
box. The edges of both boxes are included.

::::: tabs
::: code-tab
gdscript

var a = AABB(Vector3(0, 0, 0), Vector3(4, 4, 4)) var b = AABB(Vector3(1,
1, 1), Vector3(3, 3, 3)) var c = AABB(Vector3(2, 2, 2), Vector3(8, 8,
8))

print(a.encloses(a)) \# Prints true print(a.encloses(b)) \# Prints true
print(a.encloses(c)) \# Prints false
:::

::: code-tab
csharp

var a = new Aabb(new Vector3(0, 0, 0), new Vector3(4, 4, 4)); var b =
new Aabb(new Vector3(1, 1, 1), new Vector3(3, 3, 3)); var c = new
Aabb(new Vector3(2, 2, 2), new Vector3(8, 8, 8));

GD.Print(a.Encloses(a)); // Prints True GD.Print(a.Encloses(b)); //
Prints True GD.Print(a.Encloses(c)); // Prints False
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_expand}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **expand**(to_point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_expand>`{.interpreted-text
role="ref"}

Returns a copy of this bounding box expanded to align the edges with the
given `to_point`, if necessary.

::::: tabs
::: code-tab
gdscript

var box = AABB(Vector3(0, 0, 0), Vector3(5, 2, 5))

box = box.expand(Vector3(10, 0, 0)) print(box.position) \# Prints (0.0,
0.0, 0.0) print(box.size) \# Prints (10.0, 2.0, 5.0)

box = box.expand(Vector3(-5, 0, 5)) print(box.position) \# Prints (-5.0,
0.0, 0.0) print(box.size) \# Prints (15.0, 2.0, 5.0)
:::

::: code-tab
csharp

var box = new Aabb(new Vector3(0, 0, 0), new Vector3(5, 2, 5));

box = box.Expand(new Vector3(10, 0, 0)); GD.Print(box.Position); //
Prints (0, 0, 0) GD.Print(box.Size); // Prints (10, 2, 5)

box = box.Expand(new Vector3(-5, 0, 5)); GD.Print(box.Position); //
Prints (-5, 0, 0) GD.Print(box.Size); // Prints (15, 2, 5)
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_center}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_center**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_get_center>`{.interpreted-text
role="ref"}

Returns the center point of the bounding box. This is the same as
`position + (size / 2.0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_endpoint}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_endpoint**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_get_endpoint>`{.interpreted-text
role="ref"}

Returns the position of one of the 8 vertices that compose this bounding
box. With an `idx` of `0` this is the same as
`position<class_AABB_property_position>`{.interpreted-text role="ref"},
and an `idx` of `7` is the same as
`end<class_AABB_property_end>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_longest_axis}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_longest_axis**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_get_longest_axis>`{.interpreted-text
role="ref"}

Returns the longest normalized axis of this bounding box\'s
`size<class_AABB_property_size>`{.interpreted-text role="ref"}, as a
`Vector3<class_Vector3>`{.interpreted-text role="ref"}
(`Vector3.RIGHT<class_Vector3_constant_RIGHT>`{.interpreted-text
role="ref"}, `Vector3.UP<class_Vector3_constant_UP>`{.interpreted-text
role="ref"}, or
`Vector3.BACK<class_Vector3_constant_BACK>`{.interpreted-text
role="ref"}).

::::: tabs
::: code-tab
gdscript

var box = AABB(Vector3(0, 0, 0), Vector3(2, 4, 8))

print(box.get_longest_axis()) \# Prints (0.0, 0.0, 1.0)
print(box.get_longest_axis_index()) \# Prints 2
print(box.get_longest_axis_size()) \# Prints 8.0
:::

::: code-tab
csharp

var box = new Aabb(new Vector3(0, 0, 0), new Vector3(2, 4, 8));

GD.Print(box.GetLongestAxis()); // Prints (0, 0, 1)
GD.Print(box.GetLongestAxisIndex()); // Prints Z
GD.Print(box.GetLongestAxisSize()); // Prints 8
:::
:::::

See also
`get_longest_axis_index()<class_AABB_method_get_longest_axis_index>`{.interpreted-text
role="ref"} and
`get_longest_axis_size()<class_AABB_method_get_longest_axis_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_longest_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_longest_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AABB_method_get_longest_axis_index>`{.interpreted-text
role="ref"}

Returns the index to the longest axis of this bounding box\'s
`size<class_AABB_property_size>`{.interpreted-text role="ref"} (see
`Vector3.AXIS_X<class_Vector3_constant_AXIS_X>`{.interpreted-text
role="ref"},
`Vector3.AXIS_Y<class_Vector3_constant_AXIS_Y>`{.interpreted-text
role="ref"}, and
`Vector3.AXIS_Z<class_Vector3_constant_AXIS_Z>`{.interpreted-text
role="ref"}).

For an example, see
`get_longest_axis()<class_AABB_method_get_longest_axis>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_longest_axis_size}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_longest_axis_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AABB_method_get_longest_axis_size>`{.interpreted-text
role="ref"}

Returns the longest dimension of this bounding box\'s
`size<class_AABB_property_size>`{.interpreted-text role="ref"}.

For an example, see
`get_longest_axis()<class_AABB_method_get_longest_axis>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_shortest_axis}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_shortest_axis**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_get_shortest_axis>`{.interpreted-text
role="ref"}

Returns the shortest normalized axis of this bounding box\'s
`size<class_AABB_property_size>`{.interpreted-text role="ref"}, as a
`Vector3<class_Vector3>`{.interpreted-text role="ref"}
(`Vector3.RIGHT<class_Vector3_constant_RIGHT>`{.interpreted-text
role="ref"}, `Vector3.UP<class_Vector3_constant_UP>`{.interpreted-text
role="ref"}, or
`Vector3.BACK<class_Vector3_constant_BACK>`{.interpreted-text
role="ref"}).

::::: tabs
::: code-tab
gdscript

var box = AABB(Vector3(0, 0, 0), Vector3(2, 4, 8))

print(box.get_shortest_axis()) \# Prints (1.0, 0.0, 0.0)
print(box.get_shortest_axis_index()) \# Prints 0
print(box.get_shortest_axis_size()) \# Prints 2.0
:::

::: code-tab
csharp

var box = new Aabb(new Vector3(0, 0, 0), new Vector3(2, 4, 8));

GD.Print(box.GetShortestAxis()); // Prints (1, 0, 0)
GD.Print(box.GetShortestAxisIndex()); // Prints X
GD.Print(box.GetShortestAxisSize()); // Prints 2
:::
:::::

See also
`get_shortest_axis_index()<class_AABB_method_get_shortest_axis_index>`{.interpreted-text
role="ref"} and
`get_shortest_axis_size()<class_AABB_method_get_shortest_axis_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_shortest_axis_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_shortest_axis_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AABB_method_get_shortest_axis_index>`{.interpreted-text
role="ref"}

Returns the index to the shortest axis of this bounding box\'s
`size<class_AABB_property_size>`{.interpreted-text role="ref"} (see
`Vector3.AXIS_X<class_Vector3_constant_AXIS_X>`{.interpreted-text
role="ref"},
`Vector3.AXIS_Y<class_Vector3_constant_AXIS_Y>`{.interpreted-text
role="ref"}, and
`Vector3.AXIS_Z<class_Vector3_constant_AXIS_Z>`{.interpreted-text
role="ref"}).

For an example, see
`get_shortest_axis()<class_AABB_method_get_shortest_axis>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_shortest_axis_size}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_shortest_axis_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AABB_method_get_shortest_axis_size>`{.interpreted-text
role="ref"}

Returns the shortest dimension of this bounding box\'s
`size<class_AABB_property_size>`{.interpreted-text role="ref"}.

For an example, see
`get_shortest_axis()<class_AABB_method_get_shortest_axis>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_support}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_support**(direction: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_get_support>`{.interpreted-text
role="ref"}

Returns the vertex\'s position of this bounding box that\'s the farthest
in the given direction. This point is commonly known as the support
point in collision detection algorithms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_get_volume}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_volume**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_get_volume>`{.interpreted-text
role="ref"}

Returns the bounding box\'s volume. This is equivalent to
`size.x * size.y * size.z`. See also
`has_volume()<class_AABB_method_has_volume>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_grow}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **grow**(by:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_grow>`{.interpreted-text role="ref"}

Returns a copy of this bounding box extended on all sides by the given
amount `by`. A negative amount shrinks the box instead.

::::: tabs
::: code-tab
gdscript

var a = AABB(Vector3(4, 4, 4), Vector3(8, 8, 8)).grow(4)
print(a.position) \# Prints (0.0, 0.0, 0.0) print(a.size) \# Prints
(16.0, 16.0, 16.0)

var b = AABB(Vector3(0, 0, 0), Vector3(8, 4, 2)).grow(2)
print(b.position) \# Prints (-2.0, -2.0, -2.0) print(b.size) \# Prints
(12.0, 8.0, 6.0)
:::

::: code-tab
csharp

var a = new Aabb(new Vector3(4, 4, 4), new Vector3(8, 8, 8)).Grow(4);
GD.Print(a.Position); // Prints (0, 0, 0) GD.Print(a.Size); // Prints
(16, 16, 16)

var b = new Aabb(new Vector3(0, 0, 0), new Vector3(8, 4, 2)).Grow(2);
GD.Print(b.Position); // Prints (-2, -2, -2) GD.Print(b.Size); // Prints
(12, 8, 6)
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_has_point}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_point**(point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_has_point>`{.interpreted-text
role="ref"}

Returns `true` if the bounding box contains the given `point`. By
convention, points exactly on the right, top, and front sides are
**not** included.

\*\*Note:\*\* This method is not reliable for **AABB** with a *negative*
`size<class_AABB_property_size>`{.interpreted-text role="ref"}. Use
`abs()<class_AABB_method_abs>`{.interpreted-text role="ref"} first to
get a valid bounding box.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_has_surface}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_surface**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_has_surface>`{.interpreted-text
role="ref"}

Returns `true` if this bounding box has a surface or a length, that is,
at least one component of
`size<class_AABB_property_size>`{.interpreted-text role="ref"} is
greater than `0`. Otherwise, returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_has_volume}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_volume**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_has_volume>`{.interpreted-text
role="ref"}

Returns `true` if this bounding box\'s width, height, and depth are all
positive. See also
`get_volume()<class_AABB_method_get_volume>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_intersection}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **intersection**(with:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_intersection>`{.interpreted-text
role="ref"}

Returns the intersection between this bounding box and `with`. If the
boxes do not intersect, returns an empty **AABB**. If the boxes
intersect at the edge, returns a flat **AABB** with no volume (see
`has_surface()<class_AABB_method_has_surface>`{.interpreted-text
role="ref"} and
`has_volume()<class_AABB_method_has_volume>`{.interpreted-text
role="ref"}).

::::: tabs
::: code-tab
gdscript

var box1 = AABB(Vector3(0, 0, 0), Vector3(5, 2, 8)) var box2 =
AABB(Vector3(2, 0, 2), Vector3(8, 4, 4))

var intersection = box1.intersection(box2) print(intersection.position)
\# Prints (2.0, 0.0, 2.0) print(intersection.size) \# Prints (3.0, 2.0,
4.0)
:::

::: code-tab
csharp

var box1 = new Aabb(new Vector3(0, 0, 0), new Vector3(5, 2, 8)); var
box2 = new Aabb(new Vector3(2, 0, 2), new Vector3(8, 4, 4));

var intersection = box1.Intersection(box2);
GD.Print(intersection.Position); // Prints (2, 0, 2)
GD.Print(intersection.Size); // Prints (3, 2, 4)
:::
:::::

\*\*Note:\*\* If you only need to know whether two bounding boxes are
intersecting, use
`intersects()<class_AABB_method_intersects>`{.interpreted-text
role="ref"}, instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_intersects}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **intersects**(with:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_intersects>`{.interpreted-text
role="ref"}

Returns `true` if this bounding box overlaps with the box `with`. The
edges of both boxes are *always* excluded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_intersects_plane}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**intersects_plane**(plane: `Plane<class_Plane>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_intersects_plane>`{.interpreted-text
role="ref"}

Returns `true` if this bounding box is on both sides of the given
`plane`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_intersects_ray}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**intersects_ray**(from: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, dir: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_intersects_ray>`{.interpreted-text
role="ref"}

Returns the first point where this bounding box and the given ray
intersect, as a `Vector3<class_Vector3>`{.interpreted-text role="ref"}.
If no intersection occurs, returns `null`.

The ray begin at `from`, faces `dir` and extends towards infinity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_intersects_segment}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**intersects_segment**(from: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, to: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AABB_method_intersects_segment>`{.interpreted-text role="ref"}

Returns the first point where this bounding box and the given segment
intersect, as a `Vector3<class_Vector3>`{.interpreted-text role="ref"}.
If no intersection occurs, returns `null`.

The segment begins at `from` and ends at `to`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_equal_approx**(aabb: `AABB<class_AABB>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_is_equal_approx>`{.interpreted-text
role="ref"}

Returns `true` if this bounding box and `aabb` are approximately equal,
by calling
`Vector3.is_equal_approx()<class_Vector3_method_is_equal_approx>`{.interpreted-text
role="ref"} on the
`position<class_AABB_property_position>`{.interpreted-text role="ref"}
and the `size<class_AABB_property_size>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_is_finite}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_is_finite>`{.interpreted-text
role="ref"}

Returns `true` if this bounding box\'s values are finite, by calling
`Vector3.is_finite()<class_Vector3_method_is_finite>`{.interpreted-text
role="ref"} on the
`position<class_AABB_property_position>`{.interpreted-text role="ref"}
and the `size<class_AABB_property_size>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_method_merge}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **merge**(with:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_AABB_method_merge>`{.interpreted-text role="ref"}

Returns an **AABB** that encloses both this bounding box and `with`
around the edges. See also
`encloses()<class_AABB_method_encloses>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_AABB_operator_neq_AABB}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_AABB_operator_neq_AABB>`{.interpreted-text role="ref"}

Returns `true` if the
`position<class_AABB_property_position>`{.interpreted-text role="ref"}
or `size<class_AABB_property_size>`{.interpreted-text role="ref"} of
both bounding boxes are not equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_AABB_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_operator_mul_Transform3D}
::: rst-class
classref-operator
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **operator**\*(right:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_AABB_operator_mul_Transform3D>`{.interpreted-text role="ref"}

Inversely transforms (multiplies) the **AABB** by the given
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
transformation matrix, under the assumption that the transformation
basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is
not).

`aabb * transform` is equivalent to `transform.inverse() * aabb`. See
`Transform3D.inverse()<class_Transform3D_method_inverse>`{.interpreted-text
role="ref"}.

For transforming by inverse of an affine transformation (e.g. with
scaling) `transform.affine_inverse() * aabb` can be used instead. See
`Transform3D.affine_inverse()<class_Transform3D_method_affine_inverse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AABB_operator_eq_AABB}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_AABB_operator_eq_AABB>`{.interpreted-text role="ref"}

Returns `true` if both
`position<class_AABB_property_position>`{.interpreted-text role="ref"}
and `size<class_AABB_property_size>`{.interpreted-text role="ref"} of
the bounding boxes are exactly equal, respectively.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_AABB_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.
