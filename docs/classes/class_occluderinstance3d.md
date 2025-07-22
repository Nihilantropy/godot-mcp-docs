github_url
:   hide

# OccluderInstance3D {#class_OccluderInstance3D}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Provides occlusion culling for 3D nodes, which improves performance in
closed areas.

::: rst-class
classref-introduction-group
:::

## Description

Occlusion culling can improve rendering performance in closed/semi-open
areas by hiding geometry that is occluded by other objects.

The occlusion culling system is mostly static. **OccluderInstance3D**s
can be moved or hidden at run-time, but doing so will trigger a
background recomputation that can take several frames. It is recommended
to only move **OccluderInstance3D**s sporadically (e.g. for procedural
generation purposes), rather than doing so every frame.

The occlusion culling system works by rendering the occluders on the CPU
in parallel using [Embree](https://www.embree.org/), drawing the result
to a low-resolution buffer then using this to cull 3D nodes
individually. In the 3D editor, you can preview the occlusion culling
buffer by choosing **Perspective \> Display Advanced\... \> Occlusion
Culling Buffer** in the top-left corner of the 3D viewport. The
occlusion culling buffer quality can be adjusted in the Project
Settings.

\*\*Baking:\*\* Select an **OccluderInstance3D** node, then use the
**Bake Occluders** button at the top of the 3D editor. Only opaque
materials will be taken into account; transparent materials
(alpha-blended or alpha-tested) will be ignored by the occluder
generation.

\*\*Note:\*\* Occlusion culling is only effective if
`ProjectSettings.rendering/occlusion_culling/use_occlusion_culling<class_ProjectSettings_property_rendering/occlusion_culling/use_occlusion_culling>`{.interpreted-text
role="ref"} is `true`. Enabling occlusion culling has a cost on the CPU.
Only enable occlusion culling if you actually plan to use it. Large open
scenes with few or no objects blocking the view will generally not
benefit much from occlusion culling. Large open scenes generally benefit
more from mesh LOD and visibility ranges
(`GeometryInstance3D.visibility_range_begin<class_GeometryInstance3D_property_visibility_range_begin>`{.interpreted-text
role="ref"} and
`GeometryInstance3D.visibility_range_end<class_GeometryInstance3D_property_visibility_range_end>`{.interpreted-text
role="ref"}) compared to occlusion culling.

\*\*Note:\*\* Due to memory constraints, occlusion culling is not
supported by default in Web export templates. It can be enabled by
compiling custom Web export templates with `module_raycast_enabled=yes`.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Occlusion culling <../tutorials/3d/occlusion_culling>`{.interpreted-text
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

## Property Descriptions

:::: {#class_OccluderInstance3D_property_bake_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bake_mask** =
`4294967295`
`🔗<class_OccluderInstance3D_property_bake_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bake_mask**()

The visual layers to account for when baking for occluders. Only
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}s
whose
`VisualInstance3D.layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"} match with this
`bake_mask<class_OccluderInstance3D_property_bake_mask>`{.interpreted-text
role="ref"} will be included in the generated occluder mesh. By default,
all objects with *opaque* materials are taken into account for the
occluder baking.

To improve performance and avoid artifacts, it is recommended to exclude
dynamic objects, small objects and fixtures from the baking process by
moving them to a separate visual layer and excluding this layer in
`bake_mask<class_OccluderInstance3D_property_bake_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OccluderInstance3D_property_bake_simplification_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**bake_simplification_distance** = `0.1`
`🔗<class_OccluderInstance3D_property_bake_simplification_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bake_simplification_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_bake_simplification_distance**()

The simplification distance to use for simplifying the generated
occluder polygon (in 3D units). Higher values result in a less detailed
occluder mesh, which improves performance but reduces culling accuracy.

The occluder geometry is rendered on the CPU, so it is important to keep
its geometry as simple as possible. Since the buffer is rendered at a
low resolution, less detailed occluder meshes generally still work well.
The default value is fairly aggressive, so you may have to decrease it
if you run into false negatives (objects being occluded even though they
are visible by the camera). A value of `0.01` will act conservatively,
and will keep geometry *perceptually* unaffected in the occlusion
culling buffer. Depending on the scene, a value of `0.01` may still
simplify the mesh noticeably compared to disabling simplification
entirely.

Setting this to `0.0` disables simplification entirely, but vertices in
the exact same position will still be merged. The mesh will also be
re-indexed to reduce both the number of vertices and indices.

\*\*Note:\*\* This uses the [meshoptimizer](https://meshoptimizer.org/)
library under the hood, similar to LOD generation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OccluderInstance3D_property_occluder}
::: rst-class
classref-property
:::
::::

`Occluder3D<class_Occluder3D>`{.interpreted-text role="ref"}
**occluder**
`🔗<class_OccluderInstance3D_property_occluder>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_occluder**(value:
  `Occluder3D<class_Occluder3D>`{.interpreted-text role="ref"})
- `Occluder3D<class_Occluder3D>`{.interpreted-text role="ref"}
  **get_occluder**()

The occluder resource for this **OccluderInstance3D**. You can generate
an occluder resource by selecting an **OccluderInstance3D** node then
using the **Bake Occluders** button at the top of the editor.

You can also draw your own 2D occluder polygon by adding a new
`PolygonOccluder3D<class_PolygonOccluder3D>`{.interpreted-text
role="ref"} resource to the
`occluder<class_OccluderInstance3D_property_occluder>`{.interpreted-text
role="ref"} property in the Inspector.

Alternatively, you can select a primitive occluder to use:
`QuadOccluder3D<class_QuadOccluder3D>`{.interpreted-text role="ref"},
`BoxOccluder3D<class_BoxOccluder3D>`{.interpreted-text role="ref"} or
`SphereOccluder3D<class_SphereOccluder3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OccluderInstance3D_method_get_bake_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_bake_mask_value**(layer_number: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OccluderInstance3D_method_get_bake_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`bake_mask<class_OccluderInstance3D_property_bake_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OccluderInstance3D_method_set_bake_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bake_mask_value**(layer_number: `int<class_int>`{.interpreted-text
role="ref"}, value: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_OccluderInstance3D_method_set_bake_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`bake_mask<class_OccluderInstance3D_property_bake_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.
