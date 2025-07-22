github_url
:   hide

# MeshConvexDecompositionSettings {#class_MeshConvexDecompositionSettings}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Parameters to be used with a `Mesh<class_Mesh>`{.interpreted-text
role="ref"} convex decomposition operation.

::: rst-class
classref-introduction-group
:::

## Description

Parameters to be used with a `Mesh<class_Mesh>`{.interpreted-text
role="ref"} convex decomposition operation.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_MeshConvexDecompositionSettings_Mode}
::: rst-class
classref-enumeration
:::
::::

enum **Mode**:
`🔗<enum_MeshConvexDecompositionSettings_Mode>`{.interpreted-text
role="ref"}

:::: {#class_MeshConvexDecompositionSettings_constant_CONVEX_DECOMPOSITION_MODE_VOXEL}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_MeshConvexDecompositionSettings_Mode>`{.interpreted-text
role="ref"} **CONVEX_DECOMPOSITION_MODE_VOXEL** = `0`

Constant for voxel-based approximate convex decomposition.

:::: {#class_MeshConvexDecompositionSettings_constant_CONVEX_DECOMPOSITION_MODE_TETRAHEDRON}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_MeshConvexDecompositionSettings_Mode>`{.interpreted-text
role="ref"} **CONVEX_DECOMPOSITION_MODE_TETRAHEDRON** = `1`

Constant for tetrahedron-based approximate convex decomposition.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_MeshConvexDecompositionSettings_property_convex_hull_approximation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**convex_hull_approximation** = `true`
`🔗<class_MeshConvexDecompositionSettings_property_convex_hull_approximation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_convex_hull_approximation**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_convex_hull_approximation**()

If `true`, uses approximation for computing convex hulls.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_convex_hull_downsampling}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**convex_hull_downsampling** = `4`
`🔗<class_MeshConvexDecompositionSettings_property_convex_hull_downsampling>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_convex_hull_downsampling**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_convex_hull_downsampling**()

Controls the precision of the convex-hull generation process during the
clipping plane selection stage. Ranges from `1` to `16`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_max_concavity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_concavity** =
`1.0`
`🔗<class_MeshConvexDecompositionSettings_property_max_concavity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_concavity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_max_concavity**()

Maximum concavity. Ranges from `0.0` to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_max_convex_hulls}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_convex_hulls** =
`1`
`🔗<class_MeshConvexDecompositionSettings_property_max_convex_hulls>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_convex_hulls**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_convex_hulls**()

The maximum number of convex hulls to produce from the merge operation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_max_num_vertices_per_convex_hull}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**max_num_vertices_per_convex_hull** = `32`
`🔗<class_MeshConvexDecompositionSettings_property_max_num_vertices_per_convex_hull>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_num_vertices_per_convex_hull**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_max_num_vertices_per_convex_hull**()

Controls the maximum number of triangles per convex-hull. Ranges from
`4` to `1024`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_min_volume_per_convex_hull}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**min_volume_per_convex_hull** = `0.0001`
`🔗<class_MeshConvexDecompositionSettings_property_min_volume_per_convex_hull>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_volume_per_convex_hull**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_min_volume_per_convex_hull**()

Controls the adaptive sampling of the generated convex-hulls. Ranges
from `0.0` to `0.01`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_mode}
::: rst-class
classref-property
:::
::::

`Mode<enum_MeshConvexDecompositionSettings_Mode>`{.interpreted-text
role="ref"} **mode** = `0`
`🔗<class_MeshConvexDecompositionSettings_property_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mode**(value:
  `Mode<enum_MeshConvexDecompositionSettings_Mode>`{.interpreted-text
  role="ref"})
- `Mode<enum_MeshConvexDecompositionSettings_Mode>`{.interpreted-text
  role="ref"} **get_mode**()

Mode for the approximate convex decomposition.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_normalize_mesh}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **normalize_mesh** =
`false`
`🔗<class_MeshConvexDecompositionSettings_property_normalize_mesh>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_normalize_mesh**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_normalize_mesh**()

If `true`, normalizes the mesh before applying the convex decomposition.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_plane_downsampling}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **plane_downsampling** =
`4`
`🔗<class_MeshConvexDecompositionSettings_property_plane_downsampling>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_plane_downsampling**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_plane_downsampling**()

Controls the granularity of the search for the \"best\" clipping plane.
Ranges from `1` to `16`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_project_hull_vertices}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**project_hull_vertices** = `true`
`🔗<class_MeshConvexDecompositionSettings_property_project_hull_vertices>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_project_hull_vertices**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_project_hull_vertices**()

If `true`, projects output convex hull vertices onto the original source
mesh to increase floating-point accuracy of the results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_resolution}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **resolution** = `10000`
`🔗<class_MeshConvexDecompositionSettings_property_resolution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_resolution**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_resolution**()

Maximum number of voxels generated during the voxelization stage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_revolution_axes_clipping_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**revolution_axes_clipping_bias** = `0.05`
`🔗<class_MeshConvexDecompositionSettings_property_revolution_axes_clipping_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_revolution_axes_clipping_bias**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_revolution_axes_clipping_bias**()

Controls the bias toward clipping along revolution axes. Ranges from
`0.0` to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshConvexDecompositionSettings_property_symmetry_planes_clipping_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**symmetry_planes_clipping_bias** = `0.05`
`🔗<class_MeshConvexDecompositionSettings_property_symmetry_planes_clipping_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_symmetry_planes_clipping_bias**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_symmetry_planes_clipping_bias**()

Controls the bias toward clipping along symmetry planes. Ranges from
`0.0` to `1.0`.
