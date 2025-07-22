github_url
:   hide

# FogVolume {#class_FogVolume}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A region that contributes to the default volumetric fog from the world
environment.

::: rst-class
classref-introduction-group
:::

## Description

**FogVolume**s are used to add localized fog into the global volumetric
fog effect. **FogVolume**s can also remove volumetric fog from specific
areas if using a `FogMaterial<class_FogMaterial>`{.interpreted-text
role="ref"} with a negative
`FogMaterial.density<class_FogMaterial_property_density>`{.interpreted-text
role="ref"}.

Performance of **FogVolume**s is directly related to their relative size
on the screen and the complexity of their attached
`FogMaterial<class_FogMaterial>`{.interpreted-text role="ref"}. It is
best to keep **FogVolume**s relatively small and simple where possible.

\*\*Note:\*\* **FogVolume**s only have a visible effect if
`Environment.volumetric_fog_enabled<class_Environment_property_volumetric_fog_enabled>`{.interpreted-text
role="ref"} is `true`. If you don\'t want fog to be globally visible
(but only within **FogVolume** nodes), set
`Environment.volumetric_fog_density<class_Environment_property_volumetric_fog_density>`{.interpreted-text
role="ref"} to `0.0`.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Volumetric fog and fog volumes <../tutorials/3d/volumetric_fog>`{.interpreted-text
  role="doc"}

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

## Property Descriptions

:::: {#class_FogVolume_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_FogVolume_property_material>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

The `Material<class_Material>`{.interpreted-text role="ref"} used by the
**FogVolume**. Can be either a built-in
`FogMaterial<class_FogMaterial>`{.interpreted-text role="ref"} or a
custom `ShaderMaterial<class_ShaderMaterial>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FogVolume_property_shape}
::: rst-class
classref-property
:::
::::

`FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
role="ref"} **shape** = `3`
`🔗<class_FogVolume_property_shape>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape**(value:
  `FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
  role="ref"})
- `FogVolumeShape<enum_RenderingServer_FogVolumeShape>`{.interpreted-text
  role="ref"} **get_shape**()

The shape of the **FogVolume**. This can be set to either
`RenderingServer.FOG_VOLUME_SHAPE_ELLIPSOID<class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID>`{.interpreted-text
role="ref"},
`RenderingServer.FOG_VOLUME_SHAPE_CONE<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE>`{.interpreted-text
role="ref"},
`RenderingServer.FOG_VOLUME_SHAPE_CYLINDER<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER>`{.interpreted-text
role="ref"},
`RenderingServer.FOG_VOLUME_SHAPE_BOX<class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX>`{.interpreted-text
role="ref"} or
`RenderingServer.FOG_VOLUME_SHAPE_WORLD<class_RenderingServer_constant_FOG_VOLUME_SHAPE_WORLD>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FogVolume_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(2, 2, 2)` `🔗<class_FogVolume_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The size of the **FogVolume** when
`shape<class_FogVolume_property_shape>`{.interpreted-text role="ref"} is
`RenderingServer.FOG_VOLUME_SHAPE_ELLIPSOID<class_RenderingServer_constant_FOG_VOLUME_SHAPE_ELLIPSOID>`{.interpreted-text
role="ref"},
`RenderingServer.FOG_VOLUME_SHAPE_CONE<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE>`{.interpreted-text
role="ref"},
`RenderingServer.FOG_VOLUME_SHAPE_CYLINDER<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER>`{.interpreted-text
role="ref"} or
`RenderingServer.FOG_VOLUME_SHAPE_BOX<class_RenderingServer_constant_FOG_VOLUME_SHAPE_BOX>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Thin fog volumes may appear to flicker when the camera
moves or rotates. This can be alleviated by increasing
`ProjectSettings.rendering/environment/volumetric_fog/volume_depth<class_ProjectSettings_property_rendering/environment/volumetric_fog/volume_depth>`{.interpreted-text
role="ref"} (at a performance cost) or by decreasing
`Environment.volumetric_fog_length<class_Environment_property_volumetric_fog_length>`{.interpreted-text
role="ref"} (at no performance cost, but at the cost of lower fog
range). Alternatively, the **FogVolume** can be made thicker and use a
lower density in the
`material<class_FogVolume_property_material>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If
`shape<class_FogVolume_property_shape>`{.interpreted-text role="ref"} is
`RenderingServer.FOG_VOLUME_SHAPE_CONE<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CONE>`{.interpreted-text
role="ref"} or
`RenderingServer.FOG_VOLUME_SHAPE_CYLINDER<class_RenderingServer_constant_FOG_VOLUME_SHAPE_CYLINDER>`{.interpreted-text
role="ref"}, the cone/cylinder will be adjusted to fit within the size.
Non-uniform scaling of cone/cylinder shapes via the
`size<class_FogVolume_property_size>`{.interpreted-text role="ref"}
property is not supported, but you can scale the **FogVolume** node
instead.
