github_url
:   hide

# SpriteBase3D {#class_SpriteBase3D}

**Inherits:**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AnimatedSprite3D<class_AnimatedSprite3D>`{.interpreted-text
role="ref"}, `Sprite3D<class_Sprite3D>`{.interpreted-text role="ref"}

2D sprite node in 3D environment.

::: rst-class
classref-introduction-group
:::

## Description

A node that displays 2D texture information in a 3D environment. See
also `Sprite3D<class_Sprite3D>`{.interpreted-text role="ref"} where many
other properties are defined.

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

:::: {#enum_SpriteBase3D_DrawFlags}
::: rst-class
classref-enumeration
:::
::::

enum **DrawFlags**: `🔗<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
role="ref"}

:::: {#class_SpriteBase3D_constant_FLAG_TRANSPARENT}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_TRANSPARENT** = `0`

If set, the texture\'s transparency and the opacity are used to make
those parts of the sprite invisible.

:::: {#class_SpriteBase3D_constant_FLAG_SHADED}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_SHADED** = `1`

If set, lights in the environment affect the sprite.

:::: {#class_SpriteBase3D_constant_FLAG_DOUBLE_SIDED}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_DOUBLE_SIDED** = `2`

If set, texture can be seen from the back as well. If not, the texture
is invisible when looking at it from behind.

:::: {#class_SpriteBase3D_constant_FLAG_DISABLE_DEPTH_TEST}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_DISABLE_DEPTH_TEST** = `3`

Disables the depth test, so this object is drawn on top of all others.
However, objects drawn after it in the draw order may cover it.

:::: {#class_SpriteBase3D_constant_FLAG_FIXED_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_FIXED_SIZE** = `4`

Label is scaled by depth so that it always appears the same size on
screen.

:::: {#class_SpriteBase3D_constant_FLAG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text role="ref"}
**FLAG_MAX** = `5`

Represents the size of the
`DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_SpriteBase3D_AlphaCutMode}
::: rst-class
classref-enumeration
:::
::::

enum **AlphaCutMode**:
`🔗<enum_SpriteBase3D_AlphaCutMode>`{.interpreted-text role="ref"}

:::: {#class_SpriteBase3D_constant_ALPHA_CUT_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>`{.interpreted-text
role="ref"} **ALPHA_CUT_DISABLED** = `0`

This mode performs standard alpha blending. It can display translucent
areas, but transparency sorting issues may be visible when multiple
transparent materials are overlapping.

:::: {#class_SpriteBase3D_constant_ALPHA_CUT_DISCARD}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>`{.interpreted-text
role="ref"} **ALPHA_CUT_DISCARD** = `1`

This mode only allows fully transparent or fully opaque pixels. Harsh
edges will be visible unless some form of screen-space antialiasing is
enabled (see
`ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa<class_ProjectSettings_property_rendering/anti_aliasing/quality/screen_space_aa>`{.interpreted-text
role="ref"}). On the bright side, this mode doesn\'t suffer from
transparency sorting issues when multiple transparent materials are
overlapping. This mode is also known as *alpha testing* or *1-bit
transparency*.

:::: {#class_SpriteBase3D_constant_ALPHA_CUT_OPAQUE_PREPASS}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>`{.interpreted-text
role="ref"} **ALPHA_CUT_OPAQUE_PREPASS** = `2`

This mode draws fully opaque pixels in the depth prepass. This is slower
than
`ALPHA_CUT_DISABLED<class_SpriteBase3D_constant_ALPHA_CUT_DISABLED>`{.interpreted-text
role="ref"} or
`ALPHA_CUT_DISCARD<class_SpriteBase3D_constant_ALPHA_CUT_DISCARD>`{.interpreted-text
role="ref"}, but it allows displaying translucent areas and smooth edges
while using proper sorting.

:::: {#class_SpriteBase3D_constant_ALPHA_CUT_HASH}
::: rst-class
classref-enumeration-constant
:::
::::

`AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>`{.interpreted-text
role="ref"} **ALPHA_CUT_HASH** = `3`

This mode draws cuts off all values below a spatially-deterministic
threshold, the rest will remain opaque.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SpriteBase3D_property_alpha_antialiasing_edge}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**alpha_antialiasing_edge** = `0.0`
`🔗<class_SpriteBase3D_property_alpha_antialiasing_edge>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_antialiasing_edge**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_alpha_antialiasing_edge**()

Threshold at which antialiasing will be applied on the alpha channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_alpha_antialiasing_mode}
::: rst-class
classref-property
:::
::::

`AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>`{.interpreted-text
role="ref"} **alpha_antialiasing_mode** = `0`
`🔗<class_SpriteBase3D_property_alpha_antialiasing_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_antialiasing**(value:
  `AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>`{.interpreted-text
  role="ref"})
- `AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>`{.interpreted-text
  role="ref"} **get_alpha_antialiasing**()

The type of alpha antialiasing to apply.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_alpha_cut}
::: rst-class
classref-property
:::
::::

`AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>`{.interpreted-text
role="ref"} **alpha_cut** = `0`
`🔗<class_SpriteBase3D_property_alpha_cut>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_cut_mode**(value:
  `AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>`{.interpreted-text
  role="ref"})
- `AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>`{.interpreted-text
  role="ref"} **get_alpha_cut_mode**()

The alpha cutting mode to use for the sprite.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_alpha_hash_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **alpha_hash_scale**
= `1.0`
`🔗<class_SpriteBase3D_property_alpha_hash_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_hash_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_alpha_hash_scale**()

The hashing scale for Alpha Hash. Recommended values between `0` and
`2`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_alpha_scissor_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**alpha_scissor_threshold** = `0.5`
`🔗<class_SpriteBase3D_property_alpha_scissor_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_scissor_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_alpha_scissor_threshold**()

Threshold at which the alpha scissor will discard values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_axis}
::: rst-class
classref-property
:::
::::

`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"} **axis** = `2`
`🔗<class_SpriteBase3D_property_axis>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_axis**(value: `Axis<enum_Vector3_Axis>`{.interpreted-text
  role="ref"})
- `Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"} **get_axis**()

The direction in which the front of the texture faces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_billboard}
::: rst-class
classref-property
:::
::::

`BillboardMode<enum_BaseMaterial3D_BillboardMode>`{.interpreted-text
role="ref"} **billboard** = `0`
`🔗<class_SpriteBase3D_property_billboard>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_billboard_mode**(value:
  `BillboardMode<enum_BaseMaterial3D_BillboardMode>`{.interpreted-text
  role="ref"})
- `BillboardMode<enum_BaseMaterial3D_BillboardMode>`{.interpreted-text
  role="ref"} **get_billboard_mode**()

The billboard mode to use for the sprite.

\*\*Note:\*\* When billboarding is enabled and the material also casts
shadows, billboards will face **the** camera in the scene when rendering
shadows. In scenes with multiple cameras, the intended shadow cannot be
determined and this will result in undefined behavior. See [GitHub Pull
Request #72638](https://github.com/godotengine/godot/pull/72638) for
details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_centered}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **centered** = `true`
`🔗<class_SpriteBase3D_property_centered>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_centered**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_centered**()

If `true`, texture will be centered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_double_sided}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **double_sided** =
`true` `🔗<class_SpriteBase3D_property_double_sided>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, texture can be seen from the back as well, if `false`, it is
invisible when looking at it from behind.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_fixed_size}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **fixed_size** =
`false` `🔗<class_SpriteBase3D_property_fixed_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the texture is rendered at the same size regardless of
distance. The texture\'s size on screen is the same as if the camera was
`1.0` units away from the texture\'s origin, regardless of the actual
distance from the camera. The
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}\'s field of
view (or `Camera3D.size<class_Camera3D_property_size>`{.interpreted-text
role="ref"} when in orthogonal/frustum mode) still affects the size the
sprite is drawn at.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_flip_h}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_h** = `false`
`🔗<class_SpriteBase3D_property_flip_h>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flip_h**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_flipped_h**()

If `true`, texture is flipped horizontally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_flip_v}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_v** = `false`
`🔗<class_SpriteBase3D_property_flip_v>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flip_v**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_flipped_v**()

If `true`, texture is flipped vertically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_modulate}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **modulate** =
`Color(1, 1, 1, 1)`
`🔗<class_SpriteBase3D_property_modulate>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modulate**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_modulate**()

A color value used to *multiply* the texture\'s colors. Can be used for
mood-coloring or to simulate the color of ambient light.

\*\*Note:\*\* Unlike
`CanvasItem.modulate<class_CanvasItem_property_modulate>`{.interpreted-text
role="ref"} for 2D, colors with values above `1.0` (overbright) are not
supported.

\*\*Note:\*\* If a
`GeometryInstance3D.material_override<class_GeometryInstance3D_property_material_override>`{.interpreted-text
role="ref"} is defined on the **SpriteBase3D**, the material override
must be configured to take vertex colors into account for albedo.
Otherwise, the color defined in
`modulate<class_SpriteBase3D_property_modulate>`{.interpreted-text
role="ref"} will be ignored. For a
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"},
`BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>`{.interpreted-text
role="ref"} must be `true`. For a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"},
`ALBEDO *= COLOR.rgb;` must be inserted in the shader\'s `fragment()`
function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_no_depth_test}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **no_depth_test** =
`false`
`🔗<class_SpriteBase3D_property_no_depth_test>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, depth testing is disabled and the object will be drawn in
render order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)`
`🔗<class_SpriteBase3D_property_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_offset**()

The texture\'s drawing offset.

\*\*Note:\*\* When you increase
`offset<class_SpriteBase3D_property_offset>`{.interpreted-text
role="ref"}.y in Sprite3D, the sprite moves upward in world space (i.e.,
+Y is up).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_pixel_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pixel_size** =
`0.01` `🔗<class_SpriteBase3D_property_pixel_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pixel_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pixel_size**()

The size of one pixel\'s width on the sprite to scale it in 3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_render_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **render_priority** = `0`
`🔗<class_SpriteBase3D_property_render_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_render_priority**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_render_priority**()

Sets the render priority for the sprite. Higher priority objects will be
sorted in front of lower priority objects.

\*\*Note:\*\* This only applies if
`alpha_cut<class_SpriteBase3D_property_alpha_cut>`{.interpreted-text
role="ref"} is set to
`ALPHA_CUT_DISABLED<class_SpriteBase3D_constant_ALPHA_CUT_DISABLED>`{.interpreted-text
role="ref"} (default value).

\*\*Note:\*\* This only applies to sorting of transparent objects. This
will not impact how transparent objects are sorted relative to opaque
objects. This is because opaque objects are not sorted, while
transparent objects are sorted from back to front (subject to priority).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_shaded}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **shaded** = `false`
`🔗<class_SpriteBase3D_property_shaded>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the `Light3D<class_Light3D>`{.interpreted-text role="ref"} in
the `Environment<class_Environment>`{.interpreted-text role="ref"} has
effects on the sprite.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_texture_filter}
::: rst-class
classref-property
:::
::::

`TextureFilter<enum_BaseMaterial3D_TextureFilter>`{.interpreted-text
role="ref"} **texture_filter** = `3`
`🔗<class_SpriteBase3D_property_texture_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_filter**(value:
  `TextureFilter<enum_BaseMaterial3D_TextureFilter>`{.interpreted-text
  role="ref"})
- `TextureFilter<enum_BaseMaterial3D_TextureFilter>`{.interpreted-text
  role="ref"} **get_texture_filter**()

Filter flags for the texture.

\*\*Note:\*\* Linear filtering may cause artifacts around the edges,
which are especially noticeable on opaque textures. To prevent this, use
textures with transparent or identical colors around the edges.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_property_transparent}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **transparent** =
`true` `🔗<class_SpriteBase3D_property_transparent>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_flag**(flag:
  `DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the texture\'s transparency and the opacity are used to make
those parts of the sprite invisible.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SpriteBase3D_method_generate_triangle_mesh}
::: rst-class
classref-method
:::
::::

`TriangleMesh<class_TriangleMesh>`{.interpreted-text role="ref"}
**generate_triangle_mesh**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteBase3D_method_generate_triangle_mesh>`{.interpreted-text
role="ref"}

Returns a `TriangleMesh<class_TriangleMesh>`{.interpreted-text
role="ref"} with the sprite\'s vertices following its current
configuration (such as its
`axis<class_SpriteBase3D_property_axis>`{.interpreted-text role="ref"}
and
`pixel_size<class_SpriteBase3D_property_pixel_size>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_method_get_draw_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_draw_flag**(flag:
`DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteBase3D_method_get_draw_flag>`{.interpreted-text
role="ref"}

Returns the value of the specified flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_method_get_item_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_item_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteBase3D_method_get_item_rect>`{.interpreted-text
role="ref"}

Returns the rectangle representing this sprite.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteBase3D_method_set_draw_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_draw_flag**(flag:
`DrawFlags<enum_SpriteBase3D_DrawFlags>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SpriteBase3D_method_set_draw_flag>`{.interpreted-text
role="ref"}

If `true`, the specified flag will be enabled.
