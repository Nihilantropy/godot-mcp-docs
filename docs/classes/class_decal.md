github_url
:   hide

::: {.meta keywords="stain"}
:::

# Decal {#class_Decal}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Node that projects a texture onto a
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**Decal**s are used to project a texture onto a
`Mesh<class_Mesh>`{.interpreted-text role="ref"} in the scene. Use
Decals to add detail to a scene without affecting the underlying
`Mesh<class_Mesh>`{.interpreted-text role="ref"}. They are often used to
add weathering to building, add dirt or mud to the ground, or add
variety to props. Decals can be moved at any time, making them suitable
for things like blob shadows or laser sight dots.

They are made of an `AABB<class_AABB>`{.interpreted-text role="ref"} and
a group of `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}s
specifying `Color<class_Color>`{.interpreted-text role="ref"}, normal,
ORM (ambient occlusion, roughness, metallic), and emission. Decals are
projected within their `AABB<class_AABB>`{.interpreted-text role="ref"}
so altering the orientation of the Decal affects the direction in which
they are projected. By default, Decals are projected down (i.e. from
positive Y to negative Y).

The `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}s
associated with the Decal are automatically stored in a texture atlas
which is used for drawing the decals so all decals can be drawn at once.
Godot uses clustered decals, meaning they are stored in cluster data and
drawn when the mesh is drawn, they are not drawn as a post-processing
effect after.

\*\*Note:\*\* Decals cannot affect an underlying material\'s
transparency, regardless of its transparency mode (alpha blend, alpha
scissor, alpha hash, opaque pre-pass). This means translucent or
transparent areas of a material will remain translucent or transparent
even if an opaque decal is applied on them.

\*\*Note:\*\* Decals are only supported in the Forward+ and Mobile
rendering methods, not Compatibility. When using the Mobile rendering
method, only 8 decals can be displayed on each mesh resource. Attempting
to display more than 8 decals on a single mesh resource will result in
decals flickering in and out as the camera moves.

\*\*Note:\*\* When using the Mobile rendering method, decals will only
correctly affect meshes whose visibility AABB intersects with the
decal\'s AABB. If using a shader to deform the mesh in a way that makes
it go outside its AABB,
`GeometryInstance3D.extra_cull_margin<class_GeometryInstance3D_property_extra_cull_margin>`{.interpreted-text
role="ref"} must be increased on the mesh. Otherwise, the decal may not
be visible on the mesh.

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

:::: {#enum_Decal_DecalTexture}
::: rst-class
classref-enumeration
:::
::::

enum **DecalTexture**: `🔗<enum_Decal_DecalTexture>`{.interpreted-text
role="ref"}

:::: {#class_Decal_constant_TEXTURE_ALBEDO}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"}
**TEXTURE_ALBEDO** = `0`

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} corresponding
to
`texture_albedo<class_Decal_property_texture_albedo>`{.interpreted-text
role="ref"}.

:::: {#class_Decal_constant_TEXTURE_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"}
**TEXTURE_NORMAL** = `1`

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} corresponding
to
`texture_normal<class_Decal_property_texture_normal>`{.interpreted-text
role="ref"}.

:::: {#class_Decal_constant_TEXTURE_ORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"}
**TEXTURE_ORM** = `2`

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} corresponding
to `texture_orm<class_Decal_property_texture_orm>`{.interpreted-text
role="ref"}.

:::: {#class_Decal_constant_TEXTURE_EMISSION}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"}
**TEXTURE_EMISSION** = `3`

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} corresponding
to
`texture_emission<class_Decal_property_texture_emission>`{.interpreted-text
role="ref"}.

:::: {#class_Decal_constant_TEXTURE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"}
**TEXTURE_MAX** = `4`

Max size of `DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Decal_property_albedo_mix}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **albedo_mix** =
`1.0` `🔗<class_Decal_property_albedo_mix>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_albedo_mix**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_albedo_mix**()

Blends the albedo `Color<class_Color>`{.interpreted-text role="ref"} of
the decal with albedo `Color<class_Color>`{.interpreted-text role="ref"}
of the underlying mesh. This can be set to `0.0` to create a decal that
only affects normal or ORM. In this case, an albedo texture is still
required as its alpha channel will determine where the normal and ORM
will be overridden. See also
`modulate<class_Decal_property_modulate>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_cull_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **cull_mask** = `1048575`
`🔗<class_Decal_property_cull_mask>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cull_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_cull_mask**()

Specifies which
`VisualInstance3D.layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"} this decal will project on. By default, Decals affect all
layers. This is used so you can specify which types of objects receive
the Decal and which do not. This is especially useful so you can ensure
that dynamic objects don\'t accidentally receive a Decal intended for
the terrain under them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_distance_fade_begin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_fade_begin** = `40.0`
`🔗<class_Decal_property_distance_fade_begin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_distance_fade_begin**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_distance_fade_begin**()

The distance from the camera at which the Decal begins to fade away (in
3D units).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_distance_fade_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**distance_fade_enabled** = `false`
`🔗<class_Decal_property_distance_fade_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_distance_fade**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_distance_fade_enabled**()

If `true`, decals will smoothly fade away when far from the active
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} starting at
`distance_fade_begin<class_Decal_property_distance_fade_begin>`{.interpreted-text
role="ref"}. The Decal will fade out over
`distance_fade_begin<class_Decal_property_distance_fade_begin>`{.interpreted-text
role="ref"} +
`distance_fade_length<class_Decal_property_distance_fade_length>`{.interpreted-text
role="ref"}, after which it will be culled and not sent to the shader at
all. Use this to reduce the number of active Decals in a scene and thus
improve performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_distance_fade_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**distance_fade_length** = `10.0`
`🔗<class_Decal_property_distance_fade_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_distance_fade_length**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_distance_fade_length**()

The distance over which the Decal fades (in 3D units). The Decal becomes
slowly more transparent over this distance and is completely invisible
at the end. Higher values result in a smoother fade-out transition,
which is more suited when the camera moves fast.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_emission_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **emission_energy** =
`1.0` `🔗<class_Decal_property_emission_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_energy**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_emission_energy**()

Energy multiplier for the emission texture. This will make the decal
emit light at a higher or lower intensity, independently of the albedo
color. See also
`modulate<class_Decal_property_modulate>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_lower_fade}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **lower_fade** =
`0.3` `🔗<class_Decal_property_lower_fade>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lower_fade**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_lower_fade**()

Sets the curve over which the decal will fade as the surface gets
further from the center of the `AABB<class_AABB>`{.interpreted-text
role="ref"}. Only positive values are valid (negative values will be
clamped to `0.0`). See also
`upper_fade<class_Decal_property_upper_fade>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_modulate}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **modulate** =
`Color(1, 1, 1, 1)`
`🔗<class_Decal_property_modulate>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modulate**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_modulate**()

Changes the `Color<class_Color>`{.interpreted-text role="ref"} of the
Decal by multiplying the albedo and emission colors with this value. The
alpha component is only taken into account when multiplying the albedo
color, not the emission color. See also
`emission_energy<class_Decal_property_emission_energy>`{.interpreted-text
role="ref"} and
`albedo_mix<class_Decal_property_albedo_mix>`{.interpreted-text
role="ref"} to change the emission and albedo intensity independently of
each other.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_normal_fade}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **normal_fade** =
`0.0` `🔗<class_Decal_property_normal_fade>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_normal_fade**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_normal_fade**()

Fades the Decal if the angle between the Decal\'s
`AABB<class_AABB>`{.interpreted-text role="ref"} and the target surface
becomes too large. A value of `0` projects the Decal regardless of
angle, a value of `1` limits the Decal to surfaces that are nearly
perpendicular.

\*\*Note:\*\* Setting
`normal_fade<class_Decal_property_normal_fade>`{.interpreted-text
role="ref"} to a value greater than `0.0` has a small performance cost
due to the added normal angle computations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(2, 2, 2)` `🔗<class_Decal_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

Sets the size of the `AABB<class_AABB>`{.interpreted-text role="ref"}
used by the decal. All dimensions must be set to a value greater than
zero (they will be clamped to `0.001` if this is not the case). The AABB
goes from `-size/2` to `size/2`.

\*\*Note:\*\* To improve culling efficiency of \"hard surface\" decals,
set their
`upper_fade<class_Decal_property_upper_fade>`{.interpreted-text
role="ref"} and
`lower_fade<class_Decal_property_lower_fade>`{.interpreted-text
role="ref"} to `0.0` and set the Y component of the
`size<class_Decal_property_size>`{.interpreted-text role="ref"} as low
as possible. This will reduce the decals\' AABB size without affecting
their appearance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_texture_albedo}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_albedo**
`🔗<class_Decal_property_texture_albedo>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(type:
  `DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"},
  texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**(type:
  `DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} with the base
`Color<class_Color>`{.interpreted-text role="ref"} of the Decal. Either
this or the
`texture_emission<class_Decal_property_texture_emission>`{.interpreted-text
role="ref"} must be set for the Decal to be visible. Use the alpha
channel like a mask to smoothly blend the edges of the decal with the
underlying object.

\*\*Note:\*\* Unlike
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"}
whose filter mode can be adjusted on a per-material basis, the filter
mode for **Decal** textures is set globally with
`ProjectSettings.rendering/textures/decals/filter<class_ProjectSettings_property_rendering/textures/decals/filter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_texture_emission}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_emission**
`🔗<class_Decal_property_texture_emission>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(type:
  `DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"},
  texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**(type:
  `DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} with the
emission `Color<class_Color>`{.interpreted-text role="ref"} of the
Decal. Either this or the
`texture_albedo<class_Decal_property_texture_albedo>`{.interpreted-text
role="ref"} must be set for the Decal to be visible. Use the alpha
channel like a mask to smoothly blend the edges of the decal with the
underlying object.

\*\*Note:\*\* Unlike
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"}
whose filter mode can be adjusted on a per-material basis, the filter
mode for **Decal** textures is set globally with
`ProjectSettings.rendering/textures/decals/filter<class_ProjectSettings_property_rendering/textures/decals/filter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_texture_normal}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_normal**
`🔗<class_Decal_property_texture_normal>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(type:
  `DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"},
  texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**(type:
  `DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} with the
per-pixel normal map for the decal. Use this to add extra detail to
decals.

\*\*Note:\*\* Unlike
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"}
whose filter mode can be adjusted on a per-material basis, the filter
mode for **Decal** textures is set globally with
`ProjectSettings.rendering/textures/decals/filter<class_ProjectSettings_property_rendering/textures/decals/filter>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Setting this texture alone will not result in a visible
decal, as
`texture_albedo<class_Decal_property_texture_albedo>`{.interpreted-text
role="ref"} must also be set. To create a normal-only decal, load an
albedo texture into
`texture_albedo<class_Decal_property_texture_albedo>`{.interpreted-text
role="ref"} and set
`albedo_mix<class_Decal_property_albedo_mix>`{.interpreted-text
role="ref"} to `0.0`. The albedo texture\'s alpha channel will be used
to determine where the underlying surface\'s normal map should be
overridden (and its intensity).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_texture_orm}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**texture_orm** `🔗<class_Decal_property_texture_orm>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(type:
  `DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"},
  texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**(type:
  `DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} storing
ambient occlusion, roughness, and metallic for the decal. Use this to
add extra detail to decals.

\*\*Note:\*\* Unlike
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"}
whose filter mode can be adjusted on a per-material basis, the filter
mode for **Decal** textures is set globally with
`ProjectSettings.rendering/textures/decals/filter<class_ProjectSettings_property_rendering/textures/decals/filter>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Setting this texture alone will not result in a visible
decal, as
`texture_albedo<class_Decal_property_texture_albedo>`{.interpreted-text
role="ref"} must also be set. To create an ORM-only decal, load an
albedo texture into
`texture_albedo<class_Decal_property_texture_albedo>`{.interpreted-text
role="ref"} and set
`albedo_mix<class_Decal_property_albedo_mix>`{.interpreted-text
role="ref"} to `0.0`. The albedo texture\'s alpha channel will be used
to determine where the underlying surface\'s ORM map should be
overridden (and its intensity).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_property_upper_fade}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **upper_fade** =
`0.3` `🔗<class_Decal_property_upper_fade>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_upper_fade**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_upper_fade**()

Sets the curve over which the decal will fade as the surface gets
further from the center of the `AABB<class_AABB>`{.interpreted-text
role="ref"}. Only positive values are valid (negative values will be
clamped to `0.0`). See also
`lower_fade<class_Decal_property_lower_fade>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Decal_method_get_texture}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_texture**(type:
`DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Decal_method_get_texture>`{.interpreted-text
role="ref"}

Returns the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
associated with the specified
`DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"}.
This is a convenience method, in most cases you should access the
texture directly.

For example, instead of
`albedo_tex = $Decal.get_texture(Decal.TEXTURE_ALBEDO)`, use
`albedo_tex = $Decal.texture_albedo`.

One case where this is better than accessing the texture directly is
when you want to copy one Decal\'s textures to another. For example:

::::: tabs
::: code-tab
gdscript

for i in Decal.TEXTURE_MAX:

:   \$NewDecal.set_texture(i, \$OldDecal.get_texture(i))
:::

::: code-tab
csharp

for (int i = 0; i \< (int)Decal.DecalTexture.Max; i++) {
GetNode\<Decal\>(\"NewDecal\").SetTexture(i,
GetNode\<Decal\>(\"OldDecal\").GetTexture(i)); }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Decal_method_set_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_texture**(type:
`DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"},
texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_Decal_method_set_texture>`{.interpreted-text role="ref"}

Sets the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
associated with the specified
`DecalTexture<enum_Decal_DecalTexture>`{.interpreted-text role="ref"}.
This is a convenience method, in most cases you should access the
texture directly.

For example, instead of
`$Decal.set_texture(Decal.TEXTURE_ALBEDO, albedo_tex)`, use
`$Decal.texture_albedo = albedo_tex`.

One case where this is better than accessing the texture directly is
when you want to copy one Decal\'s textures to another. For example:

::::: tabs
::: code-tab
gdscript

for i in Decal.TEXTURE_MAX:

:   \$NewDecal.set_texture(i, \$OldDecal.get_texture(i))
:::

::: code-tab
csharp

for (int i = 0; i \< (int)Decal.DecalTexture.Max; i++) {
GetNode\<Decal\>(\"NewDecal\").SetTexture(i,
GetNode\<Decal\>(\"OldDecal\").GetTexture(i)); }
:::
:::::
