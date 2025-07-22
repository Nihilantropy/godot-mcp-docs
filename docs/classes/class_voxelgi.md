github_url
:   hide

# VoxelGI {#class_VoxelGI}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Real-time global illumination (GI) probe.

::: rst-class
classref-introduction-group
:::

## Description

**VoxelGI**s are used to provide high-quality real-time indirect light
and reflections to scenes. They precompute the effect of objects that
emit light and the effect of static geometry to simulate the behavior of
complex light in real-time. **VoxelGI**s need to be baked before having
a visible effect. However, once baked, dynamic objects will receive
light from them. Furthermore, lights can be fully dynamic or baked.

\*\*Note:\*\* **VoxelGI** is only supported in the Forward+ rendering
method, not Mobile or Compatibility.

\*\*Procedural generation:\*\* **VoxelGI** can be baked in an exported
project, which makes it suitable for procedurally generated or
user-built levels as long as all the geometry is generated in advance.
For games where geometry is generated at any time during gameplay, SDFGI
is more suitable (see
`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}).

\*\*Performance:\*\* **VoxelGI** is relatively demanding on the GPU and
is not suited to low-end hardware such as integrated graphics (consider
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} instead).
To improve performance, adjust
`ProjectSettings.rendering/global_illumination/voxel_gi/quality<class_ProjectSettings_property_rendering/global_illumination/voxel_gi/quality>`{.interpreted-text
role="ref"} and enable
`ProjectSettings.rendering/global_illumination/gi/use_half_resolution<class_ProjectSettings_property_rendering/global_illumination/gi/use_half_resolution>`{.interpreted-text
role="ref"} in the Project Settings. To provide a fallback for low-end
hardware, consider adding an option to disable **VoxelGI** in your
project\'s options menus. A **VoxelGI** node can be disabled by hiding
it.

\*\*Note:\*\* Meshes should have sufficiently thick walls to avoid light
leaks (avoid one-sided walls). For interior levels, enclose your level
geometry in a sufficiently large box and bridge the loops to close the
mesh. To further prevent light leaks, you can also strategically place
temporary `MeshInstance3D<class_MeshInstance3D>`{.interpreted-text
role="ref"} nodes with their
`GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>`{.interpreted-text
role="ref"} set to
`GeometryInstance3D.GI_MODE_STATIC<class_GeometryInstance3D_constant_GI_MODE_STATIC>`{.interpreted-text
role="ref"}. These temporary nodes can then be hidden after baking the
**VoxelGI** node.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Voxel global illumination <../tutorials/3d/global_illumination/using_voxel_gi>`{.interpreted-text
  role="doc"}
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

:::: {#enum_VoxelGI_Subdiv}
::: rst-class
classref-enumeration
:::
::::

enum **Subdiv**: `🔗<enum_VoxelGI_Subdiv>`{.interpreted-text role="ref"}

:::: {#class_VoxelGI_constant_SUBDIV_64}
::: rst-class
classref-enumeration-constant
:::
::::

`Subdiv<enum_VoxelGI_Subdiv>`{.interpreted-text role="ref"}
**SUBDIV_64** = `0`

Use 64 subdivisions. This is the lowest quality setting, but the
fastest. Use it if you can, but especially use it on lower-end hardware.

:::: {#class_VoxelGI_constant_SUBDIV_128}
::: rst-class
classref-enumeration-constant
:::
::::

`Subdiv<enum_VoxelGI_Subdiv>`{.interpreted-text role="ref"}
**SUBDIV_128** = `1`

Use 128 subdivisions. This is the default quality setting.

:::: {#class_VoxelGI_constant_SUBDIV_256}
::: rst-class
classref-enumeration-constant
:::
::::

`Subdiv<enum_VoxelGI_Subdiv>`{.interpreted-text role="ref"}
**SUBDIV_256** = `2`

Use 256 subdivisions.

:::: {#class_VoxelGI_constant_SUBDIV_512}
::: rst-class
classref-enumeration-constant
:::
::::

`Subdiv<enum_VoxelGI_Subdiv>`{.interpreted-text role="ref"}
**SUBDIV_512** = `3`

Use 512 subdivisions. This is the highest quality setting, but the
slowest. On lower-end hardware, this could cause the GPU to stall.

:::: {#class_VoxelGI_constant_SUBDIV_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Subdiv<enum_VoxelGI_Subdiv>`{.interpreted-text role="ref"}
**SUBDIV_MAX** = `4`

Represents the size of the
`Subdiv<enum_VoxelGI_Subdiv>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VoxelGI_property_camera_attributes}
::: rst-class
classref-property
:::
::::

`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
**camera_attributes**
`🔗<class_VoxelGI_property_camera_attributes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_camera_attributes**(value:
  `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"})
- `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"} **get_camera_attributes**()

The `CameraAttributes<class_CameraAttributes>`{.interpreted-text
role="ref"} resource that specifies exposure levels to bake at.
Auto-exposure and non exposure properties will be ignored. Exposure
settings should be used to reduce the dynamic range present when baking.
If exposure is too high, the **VoxelGI** will have banding artifacts or
may have over-exposure artifacts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGI_property_data}
::: rst-class
classref-property
:::
::::

`VoxelGIData<class_VoxelGIData>`{.interpreted-text role="ref"} **data**
`🔗<class_VoxelGI_property_data>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_probe_data**(value:
  `VoxelGIData<class_VoxelGIData>`{.interpreted-text role="ref"})
- `VoxelGIData<class_VoxelGIData>`{.interpreted-text role="ref"}
  **get_probe_data**()

The `VoxelGIData<class_VoxelGIData>`{.interpreted-text role="ref"}
resource that holds the data for this **VoxelGI**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGI_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(20, 20, 20)`
`🔗<class_VoxelGI_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The size of the area covered by the **VoxelGI**. If you make the size
larger without increasing the subdivisions with
`subdiv<class_VoxelGI_property_subdiv>`{.interpreted-text role="ref"},
the size of each cell will increase and result in lower detailed
lighting.

\*\*Note:\*\* Size is clamped to 1.0 unit or more on each axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGI_property_subdiv}
::: rst-class
classref-property
:::
::::

`Subdiv<enum_VoxelGI_Subdiv>`{.interpreted-text role="ref"} **subdiv** =
`1` `🔗<class_VoxelGI_property_subdiv>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subdiv**(value: `Subdiv<enum_VoxelGI_Subdiv>`{.interpreted-text
  role="ref"})
- `Subdiv<enum_VoxelGI_Subdiv>`{.interpreted-text role="ref"}
  **get_subdiv**()

Number of times to subdivide the grid that the **VoxelGI** operates on.
A higher number results in finer detail and thus higher visual quality,
while lower numbers result in better performance.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VoxelGI_method_bake}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**bake**(from_node: `Node<class_Node>`{.interpreted-text role="ref"} =
null, create_visual_debug: `bool<class_bool>`{.interpreted-text
role="ref"} = false) `🔗<class_VoxelGI_method_bake>`{.interpreted-text
role="ref"}

Bakes the effect from all
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"}s marked with
`GeometryInstance3D.GI_MODE_STATIC<class_GeometryInstance3D_constant_GI_MODE_STATIC>`{.interpreted-text
role="ref"} and `Light3D<class_Light3D>`{.interpreted-text role="ref"}s
marked with either
`Light3D.BAKE_STATIC<class_Light3D_constant_BAKE_STATIC>`{.interpreted-text
role="ref"} or
`Light3D.BAKE_DYNAMIC<class_Light3D_constant_BAKE_DYNAMIC>`{.interpreted-text
role="ref"}. If `create_visual_debug` is `true`, after baking the light,
this will generate a `MultiMesh<class_MultiMesh>`{.interpreted-text
role="ref"} that has a cube representing each solid cell with each cube
colored to the cell\'s albedo color. This can be used to visualize the
**VoxelGI**\'s data and debug any issues that may be occurring.

\*\*Note:\*\* `bake()<class_VoxelGI_method_bake>`{.interpreted-text
role="ref"} works from the editor and in exported projects. This makes
it suitable for procedurally generated or user-built levels. Baking a
**VoxelGI** node generally takes from 5 to 20 seconds in most scenes.
Reducing `subdiv<class_VoxelGI_property_subdiv>`{.interpreted-text
role="ref"} can speed up baking.

\*\*Note:\*\*
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"}s and `Light3D<class_Light3D>`{.interpreted-text role="ref"}s
must be fully ready before
`bake()<class_VoxelGI_method_bake>`{.interpreted-text role="ref"} is
called. If you are procedurally creating those and some meshes or lights
are missing from your baked **VoxelGI**, use `call_deferred("bake")`
instead of calling `bake()<class_VoxelGI_method_bake>`{.interpreted-text
role="ref"} directly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGI_method_debug_bake}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**debug_bake**() `🔗<class_VoxelGI_method_debug_bake>`{.interpreted-text
role="ref"}

Calls `bake()<class_VoxelGI_method_bake>`{.interpreted-text role="ref"}
with `create_visual_debug` enabled.
