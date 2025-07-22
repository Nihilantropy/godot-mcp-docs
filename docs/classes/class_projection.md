github_url
:   hide

# Projection {#class_Projection}

A 4×4 matrix for 3D projective transformations.

::: rst-class
classref-introduction-group
:::

## Description

A 4×4 matrix used for 3D projective transformations. It can represent
transformations such as translation, rotation, scaling, shearing, and
perspective division. It consists of four
`Vector4<class_Vector4>`{.interpreted-text role="ref"} columns.

For purely linear transformations (translation, rotation, and scale), it
is recommended to use `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, as it is more performant and requires less memory.

Used internally as `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"}\'s projection matrix.

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

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

## Enumerations

:::: {#enum_Projection_Planes}
::: rst-class
classref-enumeration
:::
::::

enum **Planes**: `🔗<enum_Projection_Planes>`{.interpreted-text
role="ref"}

:::: {#class_Projection_constant_PLANE_NEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Planes<enum_Projection_Planes>`{.interpreted-text role="ref"}
**PLANE_NEAR** = `0`

The index value of the projection\'s near clipping plane.

:::: {#class_Projection_constant_PLANE_FAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Planes<enum_Projection_Planes>`{.interpreted-text role="ref"}
**PLANE_FAR** = `1`

The index value of the projection\'s far clipping plane.

:::: {#class_Projection_constant_PLANE_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Planes<enum_Projection_Planes>`{.interpreted-text role="ref"}
**PLANE_LEFT** = `2`

The index value of the projection\'s left clipping plane.

:::: {#class_Projection_constant_PLANE_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`Planes<enum_Projection_Planes>`{.interpreted-text role="ref"}
**PLANE_TOP** = `3`

The index value of the projection\'s top clipping plane.

:::: {#class_Projection_constant_PLANE_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Planes<enum_Projection_Planes>`{.interpreted-text role="ref"}
**PLANE_RIGHT** = `4`

The index value of the projection\'s right clipping plane.

:::: {#class_Projection_constant_PLANE_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`Planes<enum_Projection_Planes>`{.interpreted-text role="ref"}
**PLANE_BOTTOM** = `5`

The index value of the projection bottom clipping plane.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Projection_constant_IDENTITY}
::: rst-class
classref-constant
:::
::::

**IDENTITY** =
`Projection(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)`
`🔗<class_Projection_constant_IDENTITY>`{.interpreted-text role="ref"}

A **Projection** with no transformation defined. When applied to other
data structures, no transformation is performed.

:::: {#class_Projection_constant_ZERO}
::: rst-class
classref-constant
:::
::::

**ZERO** = `Projection(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)`
`🔗<class_Projection_constant_ZERO>`{.interpreted-text role="ref"}

A **Projection** with all values initialized to 0. When applied to other
data structures, they will be zeroed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Projection_property_w}
::: rst-class
classref-property
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **w** =
`Vector4(0, 0, 0, 1)`
`🔗<class_Projection_property_w>`{.interpreted-text role="ref"}

The projection matrix\'s W vector (column 3). Equivalent to array index
`3`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_property_x}
::: rst-class
classref-property
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **x** =
`Vector4(1, 0, 0, 0)`
`🔗<class_Projection_property_x>`{.interpreted-text role="ref"}

The projection matrix\'s X vector (column 0). Equivalent to array index
`0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_property_y}
::: rst-class
classref-property
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **y** =
`Vector4(0, 1, 0, 0)`
`🔗<class_Projection_property_y>`{.interpreted-text role="ref"}

The projection matrix\'s Y vector (column 1). Equivalent to array index
`1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_property_z}
::: rst-class
classref-property
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **z** =
`Vector4(0, 0, 1, 0)`
`🔗<class_Projection_property_z>`{.interpreted-text role="ref"}

The projection matrix\'s Z vector (column 2). Equivalent to array index
`2`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Projection_constructor_Projection}
::: rst-class
classref-constructor
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**Projection**()
`🔗<class_Projection_constructor_Projection>`{.interpreted-text
role="ref"}

Constructs a default-initialized **Projection** identical to
`IDENTITY<class_Projection_constant_IDENTITY>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In C#, this constructs a **Projection** identical to
`ZERO<class_Projection_constant_ZERO>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**Projection**(from: `Projection<class_Projection>`{.interpreted-text
role="ref"})

Constructs a **Projection** as a copy of the given **Projection**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**Projection**(from: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})

Constructs a Projection as a copy of the given
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**Projection**(x_axis: `Vector4<class_Vector4>`{.interpreted-text
role="ref"}, y_axis: `Vector4<class_Vector4>`{.interpreted-text
role="ref"}, z_axis: `Vector4<class_Vector4>`{.interpreted-text
role="ref"}, w_axis: `Vector4<class_Vector4>`{.interpreted-text
role="ref"})

Constructs a Projection from four
`Vector4<class_Vector4>`{.interpreted-text role="ref"} values (matrix
columns).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Projection_method_create_depth_correction}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_depth_correction**(flip_y: `bool<class_bool>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_depth_correction>`{.interpreted-text
role="ref"}

Creates a new **Projection** that projects positions from a depth range
of `-1` to `1` to one that ranges from `0` to `1`, and flips the
projected positions vertically, according to `flip_y`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_create_fit_aabb}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_fit_aabb**(aabb: `AABB<class_AABB>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_fit_aabb>`{.interpreted-text
role="ref"}

Creates a new **Projection** that scales a given projection to fit
around a given `AABB<class_AABB>`{.interpreted-text role="ref"} in
projection space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_create_for_hmd}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_for_hmd**(eye: `int<class_int>`{.interpreted-text role="ref"},
aspect: `float<class_float>`{.interpreted-text role="ref"},
intraocular_dist: `float<class_float>`{.interpreted-text role="ref"},
display_width: `float<class_float>`{.interpreted-text role="ref"},
display_to_lens: `float<class_float>`{.interpreted-text role="ref"},
oversample: `float<class_float>`{.interpreted-text role="ref"}, z_near:
`float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_for_hmd>`{.interpreted-text
role="ref"}

Creates a new **Projection** for projecting positions onto a
head-mounted display with the given X:Y aspect ratio, distance between
eyes, display width, distance to lens, oversampling factor, and depth
clipping planes.

`eye` creates the projection for the left eye when set to 1, or the
right eye when set to 2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_create_frustum}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_frustum**(left: `float<class_float>`{.interpreted-text
role="ref"}, right: `float<class_float>`{.interpreted-text role="ref"},
bottom: `float<class_float>`{.interpreted-text role="ref"}, top:
`float<class_float>`{.interpreted-text role="ref"}, z_near:
`float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_frustum>`{.interpreted-text
role="ref"}

Creates a new **Projection** that projects positions in a frustum with
the given clipping planes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_create_frustum_aspect}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_frustum_aspect**(size: `float<class_float>`{.interpreted-text
role="ref"}, aspect: `float<class_float>`{.interpreted-text role="ref"},
offset: `Vector2<class_Vector2>`{.interpreted-text role="ref"}, z_near:
`float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"}, flip_fov:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_frustum_aspect>`{.interpreted-text
role="ref"}

Creates a new **Projection** that projects positions in a frustum with
the given size, X:Y aspect ratio, offset, and clipping planes.

`flip_fov` determines whether the projection\'s field of view is flipped
over its diagonal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_create_light_atlas_rect}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_light_atlas_rect**(rect: `Rect2<class_Rect2>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_light_atlas_rect>`{.interpreted-text
role="ref"}

Creates a new **Projection** that projects positions into the given
`Rect2<class_Rect2>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_create_orthogonal}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_orthogonal**(left: `float<class_float>`{.interpreted-text
role="ref"}, right: `float<class_float>`{.interpreted-text role="ref"},
bottom: `float<class_float>`{.interpreted-text role="ref"}, top:
`float<class_float>`{.interpreted-text role="ref"}, z_near:
`float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_orthogonal>`{.interpreted-text
role="ref"}

Creates a new **Projection** that projects positions using an orthogonal
projection with the given clipping planes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_create_orthogonal_aspect}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_orthogonal_aspect**(size:
`float<class_float>`{.interpreted-text role="ref"}, aspect:
`float<class_float>`{.interpreted-text role="ref"}, z_near:
`float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"}, flip_fov:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_orthogonal_aspect>`{.interpreted-text
role="ref"}

Creates a new **Projection** that projects positions using an orthogonal
projection with the given size, X:Y aspect ratio, and clipping planes.

`flip_fov` determines whether the projection\'s field of view is flipped
over its diagonal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_create_perspective}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_perspective**(fovy: `float<class_float>`{.interpreted-text
role="ref"}, aspect: `float<class_float>`{.interpreted-text role="ref"},
z_near: `float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"}, flip_fov:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_perspective>`{.interpreted-text
role="ref"}

Creates a new **Projection** that projects positions using a perspective
projection with the given Y-axis field of view (in degrees), X:Y aspect
ratio, and clipping planes.

`flip_fov` determines whether the projection\'s field of view is flipped
over its diagonal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_create_perspective_hmd}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**create_perspective_hmd**(fovy: `float<class_float>`{.interpreted-text
role="ref"}, aspect: `float<class_float>`{.interpreted-text role="ref"},
z_near: `float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"}, flip_fov:
`bool<class_bool>`{.interpreted-text role="ref"}, eye:
`int<class_int>`{.interpreted-text role="ref"}, intraocular_dist:
`float<class_float>`{.interpreted-text role="ref"}, convergence_dist:
`float<class_float>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_create_perspective_hmd>`{.interpreted-text
role="ref"}

Creates a new **Projection** that projects positions using a perspective
projection with the given Y-axis field of view (in degrees), X:Y aspect
ratio, and clipping distances. The projection is adjusted for a
head-mounted display with the given distance between eyes and distance
to a point that can be focused on.

`eye` creates the projection for the left eye when set to 1, or the
right eye when set to 2.

`flip_fov` determines whether the projection\'s field of view is flipped
over its diagonal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_determinant}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **determinant**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Projection_method_determinant>`{.interpreted-text
role="ref"}

Returns a scalar value that is the signed factor by which areas are
scaled by this matrix. If the sign is negative, the matrix flips the
orientation of the area.

The determinant can be used to calculate the invertibility of a matrix
or solve linear systems of equations involving the matrix, among other
applications.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_flipped_y}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**flipped_y**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Projection_method_flipped_y>`{.interpreted-text
role="ref"}

Returns a copy of this **Projection** with the signs of the values of
the Y column flipped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_aspect}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_aspect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Projection_method_get_aspect>`{.interpreted-text
role="ref"}

Returns the X:Y aspect ratio of this **Projection**\'s viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_far_plane_half_extents}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_far_plane_half_extents**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_get_far_plane_half_extents>`{.interpreted-text
role="ref"}

Returns the dimensions of the far clipping plane of the projection,
divided by two.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_fov}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_fov**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Projection_method_get_fov>`{.interpreted-text
role="ref"}

Returns the horizontal field of view of the projection (in degrees).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_fovy}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_fovy**(fovx:
`float<class_float>`{.interpreted-text role="ref"}, aspect:
`float<class_float>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Projection_method_get_fovy>`{.interpreted-text
role="ref"}

Returns the vertical field of view of the projection (in degrees)
associated with the given horizontal field of view (in degrees) and
aspect ratio.

\*\*Note:\*\* Unlike most methods of **Projection**, `aspect` is
expected to be 1 divided by the X:Y aspect ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_lod_multiplier}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_lod_multiplier**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_get_lod_multiplier>`{.interpreted-text
role="ref"}

Returns the factor by which the visible level of detail is scaled by
this **Projection**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_pixels_per_meter}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_pixels_per_meter**(for_pixel_width:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_get_pixels_per_meter>`{.interpreted-text
role="ref"}

Returns `for_pixel_width` divided by the viewport\'s width measured in
meters on the near plane, after this **Projection** is applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_projection_plane}
::: rst-class
classref-method
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"}
**get_projection_plane**(plane: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_get_projection_plane>`{.interpreted-text
role="ref"}

Returns the clipping plane of this **Projection** whose index is given
by `plane`.

`plane` should be equal to one of
`PLANE_NEAR<class_Projection_constant_PLANE_NEAR>`{.interpreted-text
role="ref"},
`PLANE_FAR<class_Projection_constant_PLANE_FAR>`{.interpreted-text
role="ref"},
`PLANE_LEFT<class_Projection_constant_PLANE_LEFT>`{.interpreted-text
role="ref"},
`PLANE_TOP<class_Projection_constant_PLANE_TOP>`{.interpreted-text
role="ref"},
`PLANE_RIGHT<class_Projection_constant_PLANE_RIGHT>`{.interpreted-text
role="ref"}, or
`PLANE_BOTTOM<class_Projection_constant_PLANE_BOTTOM>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_viewport_half_extents}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_viewport_half_extents**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_get_viewport_half_extents>`{.interpreted-text
role="ref"}

Returns the dimensions of the viewport plane that this **Projection**
projects positions onto, divided by two.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_z_far}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_z_far**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Projection_method_get_z_far>`{.interpreted-text
role="ref"}

Returns the distance for this **Projection** beyond which positions are
clipped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_get_z_near}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_z_near**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Projection_method_get_z_near>`{.interpreted-text
role="ref"}

Returns the distance for this **Projection** before which positions are
clipped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_inverse}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**inverse**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Projection_method_inverse>`{.interpreted-text
role="ref"}

Returns a **Projection** that performs the inverse of this
**Projection**\'s projective transformation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_is_orthogonal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_orthogonal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_is_orthogonal>`{.interpreted-text
role="ref"}

Returns `true` if this **Projection** performs an orthogonal projection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_jitter_offseted}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**jitter_offseted**(offset: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_jitter_offseted>`{.interpreted-text
role="ref"}

Returns a **Projection** with the X and Y values from the given
`Vector2<class_Vector2>`{.interpreted-text role="ref"} added to the
first and second values of the final column respectively.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_method_perspective_znear_adjusted}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**perspective_znear_adjusted**(new_znear:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Projection_method_perspective_znear_adjusted>`{.interpreted-text
role="ref"}

Returns a **Projection** with the near clipping distance adjusted to be
`new_znear`.

\*\*Note:\*\* The original **Projection** must be a perspective
projection.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Projection_operator_neq_Projection}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Projection<class_Projection>`{.interpreted-text role="ref"})
`🔗<class_Projection_operator_neq_Projection>`{.interpreted-text
role="ref"}

Returns `true` if the projections are not equal.

\*\*Note:\*\* Due to floating-point precision errors, this may return
`true`, even if the projections are virtually equal. An
`is_equal_approx` method may be added in a future version of Godot.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_operator_mul_Projection}
::: rst-class
classref-operator
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**operator**\*(right: `Projection<class_Projection>`{.interpreted-text
role="ref"})
`🔗<class_Projection_operator_mul_Projection>`{.interpreted-text
role="ref"}

Returns a **Projection** that applies the combined transformations of
this **Projection** and `right`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_operator_mul_Vector4}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"}
**operator**\*(right: `Vector4<class_Vector4>`{.interpreted-text
role="ref"})
`🔗<class_Projection_operator_mul_Vector4>`{.interpreted-text
role="ref"}

Projects (multiplies) the given
`Vector4<class_Vector4>`{.interpreted-text role="ref"} by this
**Projection** matrix.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_operator_eq_Projection}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Projection<class_Projection>`{.interpreted-text role="ref"})
`🔗<class_Projection_operator_eq_Projection>`{.interpreted-text
role="ref"}

Returns `true` if the projections are equal.

\*\*Note:\*\* Due to floating-point precision errors, this may return
`false`, even if the projections are virtually equal. An
`is_equal_approx` method may be added in a future version of Godot.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Projection_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`Vector4<class_Vector4>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Projection_operator_idx_int>`{.interpreted-text role="ref"}

Returns the column of the **Projection** with the given index.

Indices are in the following order: x, y, z, w.
