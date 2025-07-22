github_url
:   hide

::: {.meta keywords="batch"}
:::

# MultiMesh {#class_MultiMesh}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides high-performance drawing of a mesh multiple times using GPU
instancing.

::: rst-class
classref-introduction-group
:::

## Description

MultiMesh provides low-level mesh instancing. Drawing thousands of
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
nodes can be slow, since each object is submitted to the GPU then drawn
individually.

MultiMesh is much faster as it can draw thousands of instances with a
single draw call, resulting in less API overhead.

As a drawback, if the instances are too far away from each other,
performance may be reduced as every single instance will always render
(they are spatially indexed as one, for the whole object).

Since instances may have any behavior, the AABB used for visibility must
be provided by the user.

\*\*Note:\*\* A MultiMesh is a single object, therefore the same maximum
lights per object restriction applies. This means, that once the maximum
lights are consumed by one or more instances, the rest of the MultiMesh
instances will **not** receive any lighting.

\*\*Note:\*\* Blend Shapes will be ignored if used in a MultiMesh.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using MultiMeshInstance <../tutorials/3d/using_multi_mesh_instance>`{.interpreted-text
  role="doc"}
- `Optimization using MultiMeshes <../tutorials/performance/using_multimesh>`{.interpreted-text
  role="doc"}
- `Animating thousands of fish with MultiMeshInstance <../tutorials/performance/vertex_animation/animating_thousands_of_fish>`{.interpreted-text
  role="doc"}

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

## Enumerations

:::: {#enum_MultiMesh_TransformFormat}
::: rst-class
classref-enumeration
:::
::::

enum **TransformFormat**:
`🔗<enum_MultiMesh_TransformFormat>`{.interpreted-text role="ref"}

:::: {#class_MultiMesh_constant_TRANSFORM_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFormat<enum_MultiMesh_TransformFormat>`{.interpreted-text
role="ref"} **TRANSFORM_2D** = `0`

Use this when using 2D transforms.

:::: {#class_MultiMesh_constant_TRANSFORM_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFormat<enum_MultiMesh_TransformFormat>`{.interpreted-text
role="ref"} **TRANSFORM_3D** = `1`

Use this when using 3D transforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_MultiMesh_PhysicsInterpolationQuality}
::: rst-class
classref-enumeration
:::
::::

enum **PhysicsInterpolationQuality**:
`🔗<enum_MultiMesh_PhysicsInterpolationQuality>`{.interpreted-text
role="ref"}

:::: {#class_MultiMesh_constant_INTERP_QUALITY_FAST}
::: rst-class
classref-enumeration-constant
:::
::::

`PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>`{.interpreted-text
role="ref"} **INTERP_QUALITY_FAST** = `0`

Always interpolate using Basis lerping, which can produce warping
artifacts in some situations.

:::: {#class_MultiMesh_constant_INTERP_QUALITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>`{.interpreted-text
role="ref"} **INTERP_QUALITY_HIGH** = `1`

Attempt to interpolate using Basis slerping (spherical linear
interpolation) where possible, otherwise fall back to lerping.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_MultiMesh_property_buffer}
::: rst-class
classref-property
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **buffer** = `PackedFloat32Array()`
`🔗<class_MultiMesh_property_buffer>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_buffer**(value:
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"})
- `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} **get_buffer**()

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_color_array}
::: rst-class
classref-property
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**color_array**
`🔗<class_MultiMesh_property_color_array>`{.interpreted-text role="ref"}

**Deprecated:** Accessing this property is very slow. Use
`set_instance_color()<class_MultiMesh_method_set_instance_color>`{.interpreted-text
role="ref"} and
`get_instance_color()<class_MultiMesh_method_get_instance_color>`{.interpreted-text
role="ref"} instead.

Array containing each `Color<class_Color>`{.interpreted-text role="ref"}
used by all instances of this mesh.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_custom_aabb}
::: rst-class
classref-property
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **custom_aabb** =
`AABB(0, 0, 0, 0, 0, 0)`
`🔗<class_MultiMesh_property_custom_aabb>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_aabb**(value: `AABB<class_AABB>`{.interpreted-text
  role="ref"})
- `AABB<class_AABB>`{.interpreted-text role="ref"} **get_custom_aabb**()

Custom AABB for this MultiMesh resource. Setting this manually prevents
costly runtime AABB recalculations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_custom_data_array}
::: rst-class
classref-property
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**custom_data_array**
`🔗<class_MultiMesh_property_custom_data_array>`{.interpreted-text
role="ref"}

**Deprecated:** Accessing this property is very slow. Use
`set_instance_custom_data()<class_MultiMesh_method_set_instance_custom_data>`{.interpreted-text
role="ref"} and
`get_instance_custom_data()<class_MultiMesh_method_get_instance_custom_data>`{.interpreted-text
role="ref"} instead.

Array containing each custom data value used by all instances of this
mesh, as a `PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_instance_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **instance_count** = `0`
`🔗<class_MultiMesh_property_instance_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_instance_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_instance_count**()

Number of instances that will get drawn. This clears and (re)sizes the
buffers. Setting data format or flags afterwards will have no effect.

By default, all instances are drawn but you can limit this with
`visible_instance_count<class_MultiMesh_property_visible_instance_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_mesh}
::: rst-class
classref-property
:::
::::

`Mesh<class_Mesh>`{.interpreted-text role="ref"} **mesh**
`🔗<class_MultiMesh_property_mesh>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh**(value: `Mesh<class_Mesh>`{.interpreted-text role="ref"})
- `Mesh<class_Mesh>`{.interpreted-text role="ref"} **get_mesh**()

`Mesh<class_Mesh>`{.interpreted-text role="ref"} resource to be
instanced.

The looks of the individual instances can be modified using
`set_instance_color()<class_MultiMesh_method_set_instance_color>`{.interpreted-text
role="ref"} and
`set_instance_custom_data()<class_MultiMesh_method_set_instance_custom_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_physics_interpolation_quality}
::: rst-class
classref-property
:::
::::

`PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>`{.interpreted-text
role="ref"} **physics_interpolation_quality** = `0`
`🔗<class_MultiMesh_property_physics_interpolation_quality>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_interpolation_quality**(value:
  `PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>`{.interpreted-text
  role="ref"})
- `PhysicsInterpolationQuality<enum_MultiMesh_PhysicsInterpolationQuality>`{.interpreted-text
  role="ref"} **get_physics_interpolation_quality**()

Choose whether to use an interpolation method that favors speed or
quality.

When using low physics tick rates (typically below 20) or high rates of
object rotation, you may get better results from the high quality
setting.

\*\*Note:\*\* Fast quality does not equate to low quality. Except in the
special cases mentioned above, the quality should be comparable to high
quality.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_transform_2d_array}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **transform_2d_array**
`🔗<class_MultiMesh_property_transform_2d_array>`{.interpreted-text
role="ref"}

**Deprecated:** Accessing this property is very slow. Use
`set_instance_transform_2d()<class_MultiMesh_method_set_instance_transform_2d>`{.interpreted-text
role="ref"} and
`get_instance_transform_2d()<class_MultiMesh_method_get_instance_transform_2d>`{.interpreted-text
role="ref"} instead.

Array containing each `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"} value used by all instances of this mesh, as a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}. Each transform is divided into 3
`Vector2<class_Vector2>`{.interpreted-text role="ref"} values
corresponding to the transforms\' `x`, `y`, and `origin`.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_transform_array}
::: rst-class
classref-property
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **transform_array**
`🔗<class_MultiMesh_property_transform_array>`{.interpreted-text
role="ref"}

**Deprecated:** Accessing this property is very slow. Use
`set_instance_transform()<class_MultiMesh_method_set_instance_transform>`{.interpreted-text
role="ref"} and
`get_instance_transform()<class_MultiMesh_method_get_instance_transform>`{.interpreted-text
role="ref"} instead.

Array containing each `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} value used by all instances of this mesh, as a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}. Each transform is divided into 4
`Vector3<class_Vector3>`{.interpreted-text role="ref"} values
corresponding to the transforms\' `x`, `y`, `z`, and `origin`.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_transform_format}
::: rst-class
classref-property
:::
::::

`TransformFormat<enum_MultiMesh_TransformFormat>`{.interpreted-text
role="ref"} **transform_format** = `0`
`🔗<class_MultiMesh_property_transform_format>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform_format**(value:
  `TransformFormat<enum_MultiMesh_TransformFormat>`{.interpreted-text
  role="ref"})
- `TransformFormat<enum_MultiMesh_TransformFormat>`{.interpreted-text
  role="ref"} **get_transform_format**()

Format of transform used to transform mesh, either 2D or 3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_use_colors}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_colors** =
`false` `🔗<class_MultiMesh_property_use_colors>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_colors**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_using_colors**()

If `true`, the **MultiMesh** will use color data (see
`set_instance_color()<class_MultiMesh_method_set_instance_color>`{.interpreted-text
role="ref"}). Can only be set when
`instance_count<class_MultiMesh_property_instance_count>`{.interpreted-text
role="ref"} is `0` or less. This means that you need to call this method
before setting the instance count, or temporarily reset it to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_use_custom_data}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_custom_data** =
`false` `🔗<class_MultiMesh_property_use_custom_data>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_custom_data**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_custom_data**()

If `true`, the **MultiMesh** will use custom data (see
`set_instance_custom_data()<class_MultiMesh_method_set_instance_custom_data>`{.interpreted-text
role="ref"}). Can only be set when
`instance_count<class_MultiMesh_property_instance_count>`{.interpreted-text
role="ref"} is `0` or less. This means that you need to call this method
before setting the instance count, or temporarily reset it to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_property_visible_instance_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**visible_instance_count** = `-1`
`🔗<class_MultiMesh_property_visible_instance_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible_instance_count**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_visible_instance_count**()

Limits the number of instances drawn, -1 draws all instances. Changing
this does not change the sizes of the buffers.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MultiMesh_method_get_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **get_aabb**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_MultiMesh_method_get_aabb>`{.interpreted-text
role="ref"}

Returns the visibility axis-aligned bounding box in local space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_get_instance_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_instance_color**(instance: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiMesh_method_get_instance_color>`{.interpreted-text
role="ref"}

Gets a specific instance\'s color multiplier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_get_instance_custom_data}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_instance_custom_data**(instance:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiMesh_method_get_instance_custom_data>`{.interpreted-text
role="ref"}

Returns the custom data that has been set for a specific instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_get_instance_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_instance_transform**(instance: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiMesh_method_get_instance_transform>`{.interpreted-text
role="ref"}

Returns the `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} of a specific instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_get_instance_transform_2d}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_instance_transform_2d**(instance:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MultiMesh_method_get_instance_transform_2d>`{.interpreted-text
role="ref"}

Returns the `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"} of a specific instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_reset_instance_physics_interpolation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reset_instance_physics_interpolation**(instance:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_MultiMesh_method_reset_instance_physics_interpolation>`{.interpreted-text
role="ref"}

When using *physics interpolation*, this function allows you to prevent
interpolation on an instance in the current physics tick.

This allows you to move instances instantaneously, and should usually be
used when initially placing an instance such as a bullet to prevent
graphical glitches.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_set_buffer_interpolated}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_buffer_interpolated**(buffer_curr:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}, buffer_prev:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_MultiMesh_method_set_buffer_interpolated>`{.interpreted-text
role="ref"}

An alternative to setting the
`buffer<class_MultiMesh_property_buffer>`{.interpreted-text role="ref"}
property, which can be used with *physics interpolation*. This method
takes two arrays, and can set the data for the current and previous tick
in one go. The renderer will automatically interpolate the data at each
frame.

This is useful for situations where the order of instances may change
from physics tick to tick, such as particle systems.

When the order of instances is coherent, the simpler alternative of
setting `buffer<class_MultiMesh_property_buffer>`{.interpreted-text
role="ref"} can still be used with interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_set_instance_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_instance_color**(instance: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_MultiMesh_method_set_instance_color>`{.interpreted-text
role="ref"}

Sets the color of a specific instance by *multiplying* the mesh\'s
existing vertex colors. This allows for different color tinting per
instance.

\*\*Note:\*\* Each component is stored in 32 bits in the Forward+ and
Mobile rendering methods, but is packed into 16 bits in the
Compatibility rendering method.

For the color to take effect, ensure that
`use_colors<class_MultiMesh_property_use_colors>`{.interpreted-text
role="ref"} is `true` on the **MultiMesh** and
`BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>`{.interpreted-text
role="ref"} is `true` on the material. If you intend to set an absolute
color instead of tinting, make sure the material\'s albedo color is set
to pure white (`Color(1, 1, 1)`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_set_instance_custom_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_instance_custom_data**(instance:
`int<class_int>`{.interpreted-text role="ref"}, custom_data:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_MultiMesh_method_set_instance_custom_data>`{.interpreted-text
role="ref"}

Sets custom data for a specific instance. `custom_data` is a
`Color<class_Color>`{.interpreted-text role="ref"} type only to contain
4 floating-point numbers.

\*\*Note:\*\* Each number is stored in 32 bits in the Forward+ and
Mobile rendering methods, but is packed into 16 bits in the
Compatibility rendering method.

For the custom data to be used, ensure that
`use_custom_data<class_MultiMesh_property_use_custom_data>`{.interpreted-text
role="ref"} is `true`.

This custom instance data has to be manually accessed in your custom
shader using `INSTANCE_CUSTOM`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_set_instance_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_instance_transform**(instance: `int<class_int>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_MultiMesh_method_set_instance_transform>`{.interpreted-text
role="ref"}

Sets the `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
for a specific instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MultiMesh_method_set_instance_transform_2d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_instance_transform_2d**(instance:
`int<class_int>`{.interpreted-text role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_MultiMesh_method_set_instance_transform_2d>`{.interpreted-text
role="ref"}

Sets the `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
for a specific instance.
