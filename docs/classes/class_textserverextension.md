github_url
:   hide

# TextServerExtension {#class_TextServerExtension}

**Inherits:** `TextServer<class_TextServer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"}, `TextServerDummy<class_TextServerDummy>`{.interpreted-text
role="ref"},
`TextServerFallback<class_TextServerFallback>`{.interpreted-text
role="ref"}

Base class for custom `TextServer<class_TextServer>`{.interpreted-text
role="ref"} implementations (plugins).

::: rst-class
classref-introduction-group
:::

## Description

External `TextServer<class_TextServer>`{.interpreted-text role="ref"}
implementations should inherit from this class.

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

## Method Descriptions

:::: {#class_TextServerExtension_private_method__cleanup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_cleanup**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__cleanup>`{.interpreted-text
role="ref"}

This method is called before text server is unregistered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__create_font}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_create_font**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__create_font>`{.interpreted-text
role="ref"}

Creates a new, empty font cache entry resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__create_font_linked_variation}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_create_font_linked_variation**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__create_font_linked_variation>`{.interpreted-text
role="ref"}

Optional, implement if font supports extra spacing or baseline offset.

Creates a new variation existing font which is reusing the same glyph
cache and font data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__create_shaped_text}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_create_shaped_text**(direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"},
orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__create_shaped_text>`{.interpreted-text
role="ref"}

Creates a new buffer for complex text layout, with the given `direction`
and `orientation`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__draw_hex_code_box}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_draw_hex_code_box**(canvas: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__draw_hex_code_box>`{.interpreted-text
role="ref"}

Draws box displaying character hexadecimal code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_clear_glyphs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_clear_glyphs**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_clear_glyphs>`{.interpreted-text
role="ref"}

Removes all rendered glyph information from the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_clear_kerning_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_clear_kerning_map**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_clear_kerning_map>`{.interpreted-text
role="ref"}

Removes all kerning overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_clear_size_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_clear_size_cache**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_clear_size_cache>`{.interpreted-text
role="ref"}

Removes all font sizes from the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_clear_system_fallback_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_clear_system_fallback_cache**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_clear_system_fallback_cache>`{.interpreted-text
role="ref"}

Frees all automatically loaded system fonts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_clear_textures}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_clear_textures**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_clear_textures>`{.interpreted-text
role="ref"}

Removes all textures from font cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_draw_glyph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_draw_glyph**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, canvas: `RID<class_RID>`{.interpreted-text role="ref"},
size: `int<class_int>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"}, oversampling:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_draw_glyph>`{.interpreted-text
role="ref"}

Draws single glyph into a canvas item at the position, using `font_rid`
at the size `size`. If `oversampling` is greater than zero, it is used
as font oversampling factor, otherwise viewport oversampling settings
are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_draw_glyph_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_draw_glyph_outline**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, canvas:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, outline_size:
`int<class_int>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"}, oversampling:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_draw_glyph_outline>`{.interpreted-text
role="ref"}

Draws single glyph outline of size `outline_size` into a canvas item at
the position, using `font_rid` at the size `size`. If `oversampling` is
greater than zero, it is used as font oversampling factor, otherwise
viewport oversampling settings are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_antialiasing}
::: rst-class
classref-method
:::
::::

`FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
role="ref"} **\_font_get_antialiasing**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_antialiasing>`{.interpreted-text
role="ref"}

Returns font anti-aliasing mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_ascent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_font_get_ascent**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_ascent>`{.interpreted-text
role="ref"}

Returns the font ascent (number of pixels above the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_baseline_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_font_get_baseline_offset**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_baseline_offset>`{.interpreted-text
role="ref"}

Returns extra baseline offset (as a fraction of font height).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_char_from_glyph_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_char_from_glyph_index**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, glyph_index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_char_from_glyph_index>`{.interpreted-text
role="ref"}

Returns character code associated with `glyph_index`, or `0` if
`glyph_index` is invalid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_descent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_font_get_descent**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_descent>`{.interpreted-text
role="ref"}

Returns the font descent (number of pixels below the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_disable_embedded_bitmaps}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_get_disable_embedded_bitmaps**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_disable_embedded_bitmaps>`{.interpreted-text
role="ref"}

Returns whether the font\'s embedded bitmap loading is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_embolden}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_font_get_embolden**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_embolden>`{.interpreted-text
role="ref"}

Returns font embolden strength.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_face_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_face_count**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_face_count>`{.interpreted-text
role="ref"}

Returns number of faces in the TrueType / OpenType collection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_face_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_face_index**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_face_index>`{.interpreted-text
role="ref"}

Returns an active face index in the TrueType / OpenType collection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_fixed_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_fixed_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_fixed_size>`{.interpreted-text
role="ref"}

Returns bitmap font fixed size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_fixed_size_scale_mode}
::: rst-class
classref-method
:::
::::

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
role="ref"} **\_font_get_fixed_size_scale_mode**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_fixed_size_scale_mode>`{.interpreted-text
role="ref"}

Returns bitmap font scaling mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_generate_mipmaps}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_get_generate_mipmaps**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_generate_mipmaps>`{.interpreted-text
role="ref"}

Returns `true` if font texture mipmap generation is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_global_oversampling}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_font_get_global_oversampling**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_global_oversampling>`{.interpreted-text
role="ref"}

Returns the font oversampling factor, shared by all fonts in the
TextServer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_advance}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_font_get_glyph_advance**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_advance>`{.interpreted-text
role="ref"}

Returns glyph advance (offset of the next glyph).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_contours}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_font_get_glyph_contours**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_contours>`{.interpreted-text
role="ref"}

Returns outline contours of the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_glyph_index**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"}, char:
`int<class_int>`{.interpreted-text role="ref"}, variation_selector:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_index>`{.interpreted-text
role="ref"}

Returns the glyph index of a `char`, optionally modified by the
`variation_selector`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_list}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_font_get_glyph_list**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_list>`{.interpreted-text
role="ref"}

Returns list of rendered glyphs in the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_offset}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_font_get_glyph_offset**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_offset>`{.interpreted-text
role="ref"}

Returns glyph offset from the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_font_get_glyph_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_size>`{.interpreted-text
role="ref"}

Returns size of the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_texture_idx}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_glyph_texture_idx**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_texture_idx>`{.interpreted-text
role="ref"}

Returns index of the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_texture_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_font_get_glyph_texture_rid**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_texture_rid>`{.interpreted-text
role="ref"}

Returns resource ID of the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_texture_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_font_get_glyph_texture_size**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_texture_size>`{.interpreted-text
role="ref"}

Returns size of the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_glyph_uv_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**\_font_get_glyph_uv_rect**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_glyph_uv_rect>`{.interpreted-text
role="ref"}

Returns rectangle in the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_hinting}
::: rst-class
classref-method
:::
::::

`Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"}
**\_font_get_hinting**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_hinting>`{.interpreted-text
role="ref"}

Returns the font hinting mode. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_keep_rounding_remainders}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_get_keep_rounding_remainders**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_keep_rounding_remainders>`{.interpreted-text
role="ref"}

Returns glyph position rounding behavior. If set to `true`, when
aligning glyphs to the pixel boundaries rounding remainders are
accumulated to ensure more uniform glyph distribution. This setting has
no effect if subpixel positioning is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_kerning}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_font_get_kerning**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph_pair: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_kerning>`{.interpreted-text
role="ref"}

Returns kerning for the pair of glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_kerning_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**\_font_get_kerning_list**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_kerning_list>`{.interpreted-text
role="ref"}

Returns list of the kerning overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_language_support_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_get_language_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_language_support_override>`{.interpreted-text
role="ref"}

Returns `true` if support override is enabled for the `language`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_language_support_overrides}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_font_get_language_support_overrides**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_language_support_overrides>`{.interpreted-text
role="ref"}

Returns list of language support overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_msdf_pixel_range}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_msdf_pixel_range**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_msdf_pixel_range>`{.interpreted-text
role="ref"}

Returns the width of the range around the shape between the minimum and
maximum representable signed distance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_msdf_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_msdf_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_msdf_size>`{.interpreted-text
role="ref"}

Returns source font size used to generate MSDF textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_font_get_name**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_name>`{.interpreted-text
role="ref"}

Returns font family name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_opentype_feature_overrides}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_font_get_opentype_feature_overrides**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_opentype_feature_overrides>`{.interpreted-text
role="ref"}

Returns font OpenType feature set override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_ot_name_strings}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_font_get_ot_name_strings**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_ot_name_strings>`{.interpreted-text
role="ref"}

Returns `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
with OpenType font name strings (localized font names, version,
description, license information, sample text, etc.).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_oversampling}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_font_get_oversampling**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_oversampling>`{.interpreted-text
role="ref"}

Returns oversampling factor override. If set to a positive value,
overrides the oversampling factor of the viewport this font is used in.
See
`Viewport.oversampling<class_Viewport_property_oversampling>`{.interpreted-text
role="ref"}. This value doesn\'t override the `oversampling` parameter
of `draw_*` methods. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_font_get_scale**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_scale>`{.interpreted-text
role="ref"}

Returns scaling factor of the color bitmap font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_script_support_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_get_script_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, script:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_script_support_override>`{.interpreted-text
role="ref"}

Returns `true` if support override is enabled for the `script`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_script_support_overrides}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_font_get_script_support_overrides**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_script_support_overrides>`{.interpreted-text
role="ref"}

Returns list of script support overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_size_cache_info}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_font_get_size_cache_info**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_size_cache_info>`{.interpreted-text
role="ref"}

Returns font cache information, each entry contains the following
fields: `Vector2i size_px` - font size in pixels,
`float viewport_oversampling` - viewport oversampling factor,
`int glyphs` - number of rendered glyphs, `int textures` - number of
used textures, `int textures_size` - size of texture data in bytes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_size_cache_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**\_font_get_size_cache_list**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_size_cache_list>`{.interpreted-text
role="ref"}

Returns list of the font sizes in the cache. Each size is
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} with font size
and outline size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_spacing}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_spacing**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_spacing>`{.interpreted-text
role="ref"}

Returns the spacing for `spacing` in pixels (not relative to the font
size).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_stretch}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_stretch**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_stretch>`{.interpreted-text
role="ref"}

Returns font stretch amount, compared to a normal width. A percentage
value between `50%` and `200%`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_style}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text
role="ref"}\] **\_font_get_style**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_style>`{.interpreted-text
role="ref"}

Returns font style flags.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_style_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_font_get_style_name**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_style_name>`{.interpreted-text
role="ref"}

Returns font style name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_subpixel_positioning}
::: rst-class
classref-method
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **\_font_get_subpixel_positioning**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_subpixel_positioning>`{.interpreted-text
role="ref"}

Returns font subpixel glyph positioning mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_supported_chars}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_font_get_supported_chars**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_supported_chars>`{.interpreted-text
role="ref"}

Returns a string containing all the characters available in the font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_supported_glyphs}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_font_get_supported_glyphs**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_supported_glyphs>`{.interpreted-text
role="ref"}

Returns an array containing all glyph indices in the font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_texture_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_texture_count**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_texture_count>`{.interpreted-text
role="ref"}

Returns number of textures used by font cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_texture_image}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**\_font_get_texture_image**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, texture_index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_texture_image>`{.interpreted-text
role="ref"}

Returns font cache texture image data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_texture_offsets}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_font_get_texture_offsets**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, texture_index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_texture_offsets>`{.interpreted-text
role="ref"}

Returns array containing glyph packing data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**\_font_get_transform**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_transform>`{.interpreted-text
role="ref"}

Returns 2D transform applied to the font outlines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_underline_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_font_get_underline_position**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_underline_position>`{.interpreted-text
role="ref"}

Returns pixel offset of the underline below the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_underline_thickness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_font_get_underline_thickness**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_underline_thickness>`{.interpreted-text
role="ref"}

Returns thickness of the underline in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_variation_coordinates}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_font_get_variation_coordinates**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_variation_coordinates>`{.interpreted-text
role="ref"}

Returns variation coordinates for the specified font cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_get_weight}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_font_get_weight**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_get_weight>`{.interpreted-text
role="ref"}

Returns weight (boldness) of the font. A value in the `100...999` range,
normal font weight is `400`, bold font weight is `700`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_has_char}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_has_char**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, char: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_has_char>`{.interpreted-text
role="ref"}

Returns `true` if a Unicode `char` is available in the font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_is_allow_system_fallback}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_is_allow_system_fallback**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_is_allow_system_fallback>`{.interpreted-text
role="ref"}

Returns `true` if system fonts can be automatically used as fallbacks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_is_force_autohinter}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_is_force_autohinter**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_is_force_autohinter>`{.interpreted-text
role="ref"}

Returns `true` if auto-hinting is supported and preferred over font
built-in hinting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_is_language_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_is_language_supported**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_is_language_supported>`{.interpreted-text
role="ref"}

Returns `true`, if font supports given language ([ISO
639](https://en.wikipedia.org/wiki/ISO_639-1) code).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_is_modulate_color_glyphs}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_is_modulate_color_glyphs**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_is_modulate_color_glyphs>`{.interpreted-text
role="ref"}

Returns `true`, if color modulation is applied when drawing colored
glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_is_multichannel_signed_distance_field}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_is_multichannel_signed_distance_field**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_is_multichannel_signed_distance_field>`{.interpreted-text
role="ref"}

Returns `true` if glyphs of all sizes are rendered using single
multichannel signed distance field generated from the dynamic font
vector data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_is_script_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_font_is_script_supported**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, script:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_is_script_supported>`{.interpreted-text
role="ref"}

Returns `true`, if font supports given script (ISO 15924 code).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_remove_glyph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_remove_glyph**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_remove_glyph>`{.interpreted-text
role="ref"}

Removes specified rendered glyph information from the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_remove_kerning}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_remove_kerning**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph_pair: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_remove_kerning>`{.interpreted-text
role="ref"}

Removes kerning override for the pair of glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_remove_language_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_remove_language_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_remove_language_support_override>`{.interpreted-text
role="ref"}

Remove language support override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_remove_script_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_remove_script_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, script:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_remove_script_support_override>`{.interpreted-text
role="ref"}

Removes script support override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_remove_size_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_remove_size_cache**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_remove_size_cache>`{.interpreted-text
role="ref"}

Removes specified font size from the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_remove_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_remove_texture**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, texture_index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_remove_texture>`{.interpreted-text
role="ref"}

Removes specified texture from the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_render_glyph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_render_glyph**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_render_glyph>`{.interpreted-text
role="ref"}

Renders specified glyph to the font cache texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_render_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_render_range**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, start: `int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_render_range>`{.interpreted-text
role="ref"}

Renders the range of characters to the font cache texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_allow_system_fallback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_allow_system_fallback**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, allow_system_fallback:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_allow_system_fallback>`{.interpreted-text
role="ref"}

If set to `true`, system fonts can be automatically used as fallbacks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_antialiasing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_antialiasing**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, antialiasing:
`FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_antialiasing>`{.interpreted-text
role="ref"}

Sets font anti-aliasing mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_ascent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_ascent**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
ascent: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_ascent>`{.interpreted-text
role="ref"}

Sets the font ascent (number of pixels above the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_baseline_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_baseline_offset**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, baseline_offset:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_baseline_offset>`{.interpreted-text
role="ref"}

Sets extra baseline offset (as a fraction of font height).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_data**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_data>`{.interpreted-text
role="ref"}

Sets font source data, e.g contents of the dynamic font source file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_data_ptr}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_data_ptr**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, data_ptr: `const uint8_t*`, data_size:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_data_ptr>`{.interpreted-text
role="ref"}

Sets pointer to the font source data, e.g contents of the dynamic font
source file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_descent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_descent**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
descent: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_descent>`{.interpreted-text
role="ref"}

Sets the font descent (number of pixels below the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_disable_embedded_bitmaps}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_disable_embedded_bitmaps**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"},
disable_embedded_bitmaps: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_disable_embedded_bitmaps>`{.interpreted-text
role="ref"}

If set to `true`, embedded font bitmap loading is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_embolden}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_embolden**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, strength: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_embolden>`{.interpreted-text
role="ref"}

Sets font embolden strength. If `strength` is not equal to zero,
emboldens the font outlines. Negative values reduce the outline
thickness.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_face_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_face_index**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, face_index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_face_index>`{.interpreted-text
role="ref"}

Sets an active face index in the TrueType / OpenType collection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_fixed_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_fixed_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, fixed_size: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_fixed_size>`{.interpreted-text
role="ref"}

Sets bitmap font fixed size. If set to value greater than zero, same
cache entry will be used for all font sizes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_fixed_size_scale_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_fixed_size_scale_mode**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, fixed_size_scale_mode:
`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_fixed_size_scale_mode>`{.interpreted-text
role="ref"}

Sets bitmap font scaling mode. This property is used only if
`fixed_size` is greater than zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_force_autohinter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_force_autohinter**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, force_autohinter:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_force_autohinter>`{.interpreted-text
role="ref"}

If set to `true` auto-hinting is preferred over font built-in hinting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_generate_mipmaps}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_generate_mipmaps**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, generate_mipmaps:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_generate_mipmaps>`{.interpreted-text
role="ref"}

If set to `true` font texture mipmap generation is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_global_oversampling}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_global_oversampling**(oversampling:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_global_oversampling>`{.interpreted-text
role="ref"}

Sets oversampling factor, shared by all font in the TextServer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_glyph_advance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_glyph_advance**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"}, advance:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_glyph_advance>`{.interpreted-text
role="ref"}

Sets glyph advance (offset of the next glyph).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_glyph_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_glyph_offset**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"},
offset: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_glyph_offset>`{.interpreted-text
role="ref"}

Sets glyph offset from the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_glyph_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_glyph_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"},
gl_size: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_glyph_size>`{.interpreted-text
role="ref"}

Sets size of the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_glyph_texture_idx}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_glyph_texture_idx**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"}, texture_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_glyph_texture_idx>`{.interpreted-text
role="ref"}

Sets index of the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_glyph_uv_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_glyph_uv_rect**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"}, uv_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_glyph_uv_rect>`{.interpreted-text
role="ref"}

Sets rectangle in the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_hinting}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_hinting**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, hinting:
`Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_hinting>`{.interpreted-text
role="ref"}

Sets font hinting mode. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_keep_rounding_remainders}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_keep_rounding_remainders**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"},
keep_rounding_remainders: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_keep_rounding_remainders>`{.interpreted-text
role="ref"}

Sets glyph position rounding behavior. If set to `true`, when aligning
glyphs to the pixel boundaries rounding remainders are accumulated to
ensure more uniform glyph distribution. This setting has no effect if
subpixel positioning is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_kerning}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_kerning**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph_pair: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
kerning: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_kerning>`{.interpreted-text
role="ref"}

Sets kerning for the pair of glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_language_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_language_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"}, supported:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_language_support_override>`{.interpreted-text
role="ref"}

Adds override for
`_font_is_language_supported()<class_TextServerExtension_private_method__font_is_language_supported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_modulate_color_glyphs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_modulate_color_glyphs**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, modulate:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_modulate_color_glyphs>`{.interpreted-text
role="ref"}

If set to `true`, color modulation is applied when drawing colored
glyphs, otherwise it\'s applied to the monochrome glyphs only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_msdf_pixel_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_msdf_pixel_range**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, msdf_pixel_range:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_msdf_pixel_range>`{.interpreted-text
role="ref"}

Sets the width of the range around the shape between the minimum and
maximum representable signed distance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_msdf_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_msdf_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, msdf_size: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_msdf_size>`{.interpreted-text
role="ref"}

Sets source font size used to generate MSDF textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_multichannel_signed_distance_field}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_multichannel_signed_distance_field**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, msdf:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_multichannel_signed_distance_field>`{.interpreted-text
role="ref"}

If set to `true`, glyphs of all sizes are rendered using single
multichannel signed distance field generated from the dynamic font
vector data. MSDF rendering allows displaying the font at any scaling
factor without blurriness, and without incurring a CPU cost when the
font size changes (since the font no longer needs to be rasterized on
the CPU). As a downside, font hinting is not available with MSDF. The
lack of font hinting may result in less crisp and less readable fonts at
small sizes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_name**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_name>`{.interpreted-text
role="ref"}

Sets the font family name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_opentype_feature_overrides}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_opentype_feature_overrides**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, overrides:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_opentype_feature_overrides>`{.interpreted-text
role="ref"}

Sets font OpenType feature set override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_oversampling}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_oversampling**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, oversampling: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_oversampling>`{.interpreted-text
role="ref"}

If set to a positive value, overrides the oversampling factor of the
viewport this font is used in. See
`Viewport.oversampling<class_Viewport_property_oversampling>`{.interpreted-text
role="ref"}. This value doesn\'t override the `oversampling` parameter
of `draw_*` methods. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_scale**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
scale: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_scale>`{.interpreted-text
role="ref"}

Sets scaling factor of the color bitmap font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_script_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_script_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, script:
`String<class_String>`{.interpreted-text role="ref"}, supported:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_script_support_override>`{.interpreted-text
role="ref"}

Adds override for
`_font_is_script_supported()<class_TextServerExtension_private_method__font_is_script_supported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_spacing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_spacing**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_spacing>`{.interpreted-text
role="ref"}

Sets the spacing for `spacing` to `value` in pixels (not relative to the
font size).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_stretch}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_stretch**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, stretch: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_stretch>`{.interpreted-text
role="ref"}

Sets font stretch amount, compared to a normal width. A percentage value
between `50%` and `200%`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_style}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_style**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, style:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_style>`{.interpreted-text
role="ref"}

Sets the font style flags.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_style_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_style_name**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, name_style: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_style_name>`{.interpreted-text
role="ref"}

Sets the font style name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_subpixel_positioning}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_subpixel_positioning**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, subpixel_positioning:
`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_subpixel_positioning>`{.interpreted-text
role="ref"}

Sets font subpixel glyph positioning mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_texture_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_texture_image**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, texture_index:
`int<class_int>`{.interpreted-text role="ref"}, image:
`Image<class_Image>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_texture_image>`{.interpreted-text
role="ref"}

Sets font cache texture image data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_texture_offsets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_texture_offsets**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, texture_index:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_texture_offsets>`{.interpreted-text
role="ref"}

Sets array containing glyph packing data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_transform**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_transform>`{.interpreted-text
role="ref"}

Sets 2D transform, applied to the font outlines, can be used for
slanting, flipping, and rotating glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_underline_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_underline_position**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, underline_position:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_underline_position>`{.interpreted-text
role="ref"}

Sets pixel offset of the underline below the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_underline_thickness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_underline_thickness**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, underline_thickness:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_underline_thickness>`{.interpreted-text
role="ref"}

Sets thickness of the underline in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_variation_coordinates}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_variation_coordinates**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, variation_coordinates:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_variation_coordinates>`{.interpreted-text
role="ref"}

Sets variation coordinates for the specified font cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_set_weight}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_font_set_weight**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, weight: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_set_weight>`{.interpreted-text
role="ref"}

Sets weight (boldness) of the font. A value in the `100...999` range,
normal font weight is `400`, bold font weight is `700`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_supported_feature_list}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_font_supported_feature_list**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_supported_feature_list>`{.interpreted-text
role="ref"}

Returns the dictionary of the supported OpenType features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__font_supported_variation_list}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_font_supported_variation_list**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__font_supported_variation_list>`{.interpreted-text
role="ref"}

Returns the dictionary of the supported OpenType variation coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__format_number}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_format_number**(number: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__format_number>`{.interpreted-text
role="ref"}

Converts a number from the Western Arabic (0..9) to the numeral systems
used in `language`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__free_rid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_free_rid**(rid: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__free_rid>`{.interpreted-text
role="ref"}

Frees an object created by this
`TextServer<class_TextServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__get_features}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_features**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__get_features>`{.interpreted-text
role="ref"}

Returns text server features, see
`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__get_hex_code_box_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_hex_code_box_size**(size: `int<class_int>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__get_hex_code_box_size>`{.interpreted-text
role="ref"}

Returns size of the replacement character (box with character
hexadecimal code that is drawn in place of invalid characters).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **\_get_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__get_name>`{.interpreted-text
role="ref"}

Returns the name of the server interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__get_support_data}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**\_get_support_data**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__get_support_data>`{.interpreted-text
role="ref"}

Returns default TextServer database (e.g. ICU break iterators and
dictionaries).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__get_support_data_filename}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_support_data_filename**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__get_support_data_filename>`{.interpreted-text
role="ref"}

Returns default TextServer database (e.g. ICU break iterators and
dictionaries) filename.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__get_support_data_info}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_support_data_info**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__get_support_data_info>`{.interpreted-text
role="ref"}

Returns TextServer database (e.g. ICU break iterators and dictionaries)
description.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__has}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_has**(rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__has>`{.interpreted-text
role="ref"}

Returns `true` if `rid` is valid resource owned by this text server.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__has_feature}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_has_feature**(feature:
`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__has_feature>`{.interpreted-text
role="ref"}

Returns `true` if the server supports a feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__is_confusable}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_is_confusable**(string: `String<class_String>`{.interpreted-text
role="ref"}, dict:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__is_confusable>`{.interpreted-text
role="ref"}

Returns index of the first string in `dict` which is visually confusable
with the `string`, or `-1` if none is found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__is_locale_right_to_left}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_locale_right_to_left**(locale:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__is_locale_right_to_left>`{.interpreted-text
role="ref"}

Returns `true` if locale is right-to-left.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__is_valid_identifier}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_valid_identifier**(string:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__is_valid_identifier>`{.interpreted-text
role="ref"}

Returns `true` if `string` is a valid identifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__is_valid_letter}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_valid_letter**(unicode: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__is_valid_letter>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__load_support_data}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_load_support_data**(filename:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__load_support_data>`{.interpreted-text
role="ref"}

Loads optional TextServer database (e.g. ICU break iterators and
dictionaries).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__name_to_tag}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_name_to_tag**(name:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__name_to_tag>`{.interpreted-text
role="ref"}

Converts readable feature, variation, script, or language name to
OpenType tag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__parse_number}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_parse_number**(number: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__parse_number>`{.interpreted-text
role="ref"}

Converts `number` from the numeral systems used in `language` to Western
Arabic (0..9).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__parse_structured_text}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}\]
**\_parse_structured_text**(parser_type:
`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"}, args: `Array<class_Array>`{.interpreted-text role="ref"},
text: `String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__parse_structured_text>`{.interpreted-text
role="ref"}

Default implementation of the BiDi algorithm override function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__percent_sign}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_percent_sign**(language: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__percent_sign>`{.interpreted-text
role="ref"}

Returns percent sign used in the `language`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__reference_oversampling_level}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_reference_oversampling_level**(oversampling:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__reference_oversampling_level>`{.interpreted-text
role="ref"}

Increases the reference count of the specified oversampling level. This
method is called by `Viewport<class_Viewport>`{.interpreted-text
role="ref"}, and should not be used directly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__save_support_data}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_save_support_data**(filename:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__save_support_data>`{.interpreted-text
role="ref"}

Saves optional TextServer database (e.g. ICU break iterators and
dictionaries) to the file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_run_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_get_run_count**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_run_count>`{.interpreted-text
role="ref"}

Returns the number of uniform text runs in the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_run_direction}
::: rst-class
classref-method
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**\_shaped_get_run_direction**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_run_direction>`{.interpreted-text
role="ref"}

Returns the direction of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_run_font_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_shaped_get_run_font_rid**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_run_font_rid>`{.interpreted-text
role="ref"}

Returns the font RID of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_run_font_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_get_run_font_size**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_run_font_size>`{.interpreted-text
role="ref"}

Returns the font size of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_run_language}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_shaped_get_run_language**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_run_language>`{.interpreted-text
role="ref"}

Returns the language of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_run_object}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_shaped_get_run_object**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_run_object>`{.interpreted-text
role="ref"}

Returns the embedded object of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_run_range}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**\_shaped_get_run_range**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_run_range>`{.interpreted-text
role="ref"}

Returns the source text range of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_run_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_shaped_get_run_text**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_run_text>`{.interpreted-text
role="ref"}

Returns the source text of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_span_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_get_span_count**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_span_count>`{.interpreted-text
role="ref"}

Returns number of text spans added using
`_shaped_text_add_string()<class_TextServerExtension_private_method__shaped_text_add_string>`{.interpreted-text
role="ref"} or
`_shaped_text_add_object()<class_TextServerExtension_private_method__shaped_text_add_object>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_span_embedded_object}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_shaped_get_span_embedded_object**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_span_embedded_object>`{.interpreted-text
role="ref"}

Returns text embedded object key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_span_meta}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_shaped_get_span_meta**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_span_meta>`{.interpreted-text
role="ref"}

Returns text span metadata.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_span_object}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_shaped_get_span_object**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_span_object>`{.interpreted-text
role="ref"}

Returns the text span embedded object key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_span_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_shaped_get_span_text**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_span_text>`{.interpreted-text
role="ref"}

Returns the text span source text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_get_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_shaped_get_text**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_get_text>`{.interpreted-text
role="ref"}

Returns the text buffer source text, including object replacement
characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_set_span_update_font}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_set_span_update_font**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, fonts:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\], size:
`int<class_int>`{.interpreted-text role="ref"}, opentype_features:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_set_span_update_font>`{.interpreted-text
role="ref"}

Changes text span font, font size, and OpenType features, without
changing the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_add_object}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shaped_text_add_object**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, key: `Variant<class_Variant>`{.interpreted-text
role="ref"}, size: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, inline_align:
`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"}, length: `int<class_int>`{.interpreted-text role="ref"},
baseline: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_add_object>`{.interpreted-text
role="ref"}

Adds inline object to the text buffer, `key` must be unique. In the
text, object is represented as `length` object replacement characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_add_string}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shaped_text_add_string**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, text: `String<class_String>`{.interpreted-text role="ref"},
fonts: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\], size:
`int<class_int>`{.interpreted-text role="ref"}, opentype_features:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"}, meta:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_add_string>`{.interpreted-text
role="ref"}

Adds text span and font to draw it to the text buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_clear**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_clear>`{.interpreted-text
role="ref"}

Clears text buffer (removes text and inline objects).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_closest_character_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_closest_character_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_closest_character_pos>`{.interpreted-text
role="ref"}

Returns composite character position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_draw**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, canvas: `RID<class_RID>`{.interpreted-text role="ref"},
pos: `Vector2<class_Vector2>`{.interpreted-text role="ref"}, clip_l:
`float<class_float>`{.interpreted-text role="ref"}, clip_r:
`float<class_float>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"}, oversampling:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_draw>`{.interpreted-text
role="ref"}

Draw shaped text into a canvas item at a given position, with `color`.
`pos` specifies the leftmost point of the baseline (for horizontal
layout) or topmost point of the baseline (for vertical layout). If
`oversampling` is greater than zero, it is used as font oversampling
factor, otherwise viewport oversampling settings are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_draw_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_draw_outline**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, canvas:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, clip_l:
`float<class_float>`{.interpreted-text role="ref"}, clip_r:
`float<class_float>`{.interpreted-text role="ref"}, outline_size:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"}, oversampling:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_draw_outline>`{.interpreted-text
role="ref"}

Draw the outline of the shaped text into a canvas item at a given
position, with `color`. `pos` specifies the leftmost point of the
baseline (for horizontal layout) or topmost point of the baseline (for
vertical layout). If `oversampling` is greater than zero, it is used as
font oversampling factor, otherwise viewport oversampling settings are
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_fit_to_width}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_shaped_text_fit_to_width**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, width:
`float<class_float>`{.interpreted-text role="ref"}, justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_fit_to_width>`{.interpreted-text
role="ref"}

Adjusts text width to fit to specified width, returns new text width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_ascent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_shaped_text_get_ascent**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_ascent>`{.interpreted-text
role="ref"}

Returns the text ascent (number of pixels above the baseline for
horizontal layout or to the left of baseline for vertical).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_carets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_get_carets**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, position: `int<class_int>`{.interpreted-text role="ref"},
caret: `CaretInfo*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_carets>`{.interpreted-text
role="ref"}

Returns shapes of the carets corresponding to the character offset
`position` in the text. Returned caret shape is 1 pixel wide rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_character_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_shaped_text_get_character_breaks**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_character_breaks>`{.interpreted-text
role="ref"}

Returns array of the composite character boundaries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_custom_ellipsis}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_get_custom_ellipsis**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_custom_ellipsis>`{.interpreted-text
role="ref"}

Returns ellipsis character used for text clipping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_custom_punctuation}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_shaped_text_get_custom_punctuation**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_custom_punctuation>`{.interpreted-text
role="ref"}

Returns custom punctuation character list, used for word breaking. If
set to empty string, server defaults are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_descent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_shaped_text_get_descent**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_descent>`{.interpreted-text
role="ref"}

Returns the text descent (number of pixels below the baseline for
horizontal layout or to the right of baseline for vertical).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_direction}
::: rst-class
classref-method
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**\_shaped_text_get_direction**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_direction>`{.interpreted-text
role="ref"}

Returns direction of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_dominant_direction_in_range}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_get_dominant_direction_in_range**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, start:
`int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_dominant_direction_in_range>`{.interpreted-text
role="ref"}

Returns dominant direction of in the range of text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyph_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_get_ellipsis_glyph_count**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyph_count>`{.interpreted-text
role="ref"}

Returns number of glyphs in the ellipsis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyphs}
::: rst-class
classref-method
:::
::::

`const Glyph*` **\_shaped_text_get_ellipsis_glyphs**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyphs>`{.interpreted-text
role="ref"}

Returns array of the glyphs in the ellipsis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_ellipsis_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_get_ellipsis_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_ellipsis_pos>`{.interpreted-text
role="ref"}

Returns position of the ellipsis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_glyph_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_get_glyph_count**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_glyph_count>`{.interpreted-text
role="ref"}

Returns number of glyphs in the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_glyphs}
::: rst-class
classref-method
:::
::::

`const Glyph*` **\_shaped_text_get_glyphs**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_glyphs>`{.interpreted-text
role="ref"}

Returns an array of glyphs in the visual order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_grapheme_bounds}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_shaped_text_get_grapheme_bounds**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_grapheme_bounds>`{.interpreted-text
role="ref"}

Returns composite character\'s bounds as offsets from the start of the
line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_inferred_direction}
::: rst-class
classref-method
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**\_shaped_text_get_inferred_direction**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_inferred_direction>`{.interpreted-text
role="ref"}

Returns direction of the text, inferred by the BiDi algorithm.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_line_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_shaped_text_get_line_breaks**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, width:
`float<class_float>`{.interpreted-text role="ref"}, start:
`int<class_int>`{.interpreted-text role="ref"}, break_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_line_breaks>`{.interpreted-text
role="ref"}

Breaks text to the lines and returns character ranges for each line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_line_breaks_adv}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_shaped_text_get_line_breaks_adv**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, width:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}, start: `int<class_int>`{.interpreted-text role="ref"},
once: `bool<class_bool>`{.interpreted-text role="ref"}, break_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_line_breaks_adv>`{.interpreted-text
role="ref"}

Breaks text to the lines and columns. Returns character ranges for each
segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_object_glyph}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_get_object_glyph**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, key:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_object_glyph>`{.interpreted-text
role="ref"}

Returns the glyph index of the inline object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_object_range}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**\_shaped_text_get_object_range**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, key:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_object_range>`{.interpreted-text
role="ref"}

Returns the character range of the inline object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_object_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**\_shaped_text_get_object_rect**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, key:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_object_rect>`{.interpreted-text
role="ref"}

Returns bounding rectangle of the inline object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_objects}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**\_shaped_text_get_objects**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_objects>`{.interpreted-text
role="ref"}

Returns array of inline objects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_orientation}
::: rst-class
classref-method
:::
::::

`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
**\_shaped_text_get_orientation**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_orientation>`{.interpreted-text
role="ref"}

Returns text orientation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_parent}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_shaped_text_get_parent**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_parent>`{.interpreted-text
role="ref"}

Returns the parent buffer from which the substring originates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_preserve_control}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shaped_text_get_preserve_control**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_preserve_control>`{.interpreted-text
role="ref"}

Returns `true` if text buffer is configured to display control
characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_preserve_invalid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shaped_text_get_preserve_invalid**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_preserve_invalid>`{.interpreted-text
role="ref"}

Returns `true` if text buffer is configured to display hexadecimal codes
in place of invalid characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_range}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**\_shaped_text_get_range**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_range>`{.interpreted-text
role="ref"}

Returns substring buffer character range in the parent buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_selection}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **\_shaped_text_get_selection**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, start:
`int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_selection>`{.interpreted-text
role="ref"}

Returns selection rectangles for the specified character range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_shaped_text_get_size**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_size>`{.interpreted-text
role="ref"}

Returns size of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_spacing}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_get_spacing**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_spacing>`{.interpreted-text
role="ref"}

Returns extra spacing added between glyphs or lines in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_trim_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_get_trim_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_trim_pos>`{.interpreted-text
role="ref"}

Returns the position of the overrun trim.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_underline_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_shaped_text_get_underline_position**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_underline_position>`{.interpreted-text
role="ref"}

Returns pixel offset of the underline below the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_underline_thickness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_shaped_text_get_underline_thickness**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_underline_thickness>`{.interpreted-text
role="ref"}

Returns thickness of the underline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_width}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_shaped_text_get_width**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_width>`{.interpreted-text
role="ref"}

Returns width (for horizontal layout) or height (for vertical) of the
text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_get_word_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_shaped_text_get_word_breaks**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, grapheme_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"}\], skip_grapheme_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_get_word_breaks>`{.interpreted-text
role="ref"}

Breaks text into words and returns array of character ranges. Use
`grapheme_flags` to set what characters are used for breaking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_hit_test_grapheme}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_hit_test_grapheme**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, coord:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_hit_test_grapheme>`{.interpreted-text
role="ref"}

Returns grapheme index at the specified pixel offset at the baseline, or
`-1` if none is found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_hit_test_position}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_hit_test_position**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, coord:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_hit_test_position>`{.interpreted-text
role="ref"}

Returns caret character offset at the specified pixel offset at the
baseline. This function always returns a valid position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_is_ready}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shaped_text_is_ready**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_is_ready>`{.interpreted-text
role="ref"}

Returns `true` if buffer is successfully shaped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_next_character_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_next_character_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_next_character_pos>`{.interpreted-text
role="ref"}

Returns composite character end position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_next_grapheme_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_next_grapheme_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_next_grapheme_pos>`{.interpreted-text
role="ref"}

Returns grapheme end position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_overrun_trim_to_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_overrun_trim_to_width**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, width:
`float<class_float>`{.interpreted-text role="ref"}, trim_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_overrun_trim_to_width>`{.interpreted-text
role="ref"}

Trims text if it exceeds the given width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_prev_character_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_prev_character_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_prev_character_pos>`{.interpreted-text
role="ref"}

Returns composite character start position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_prev_grapheme_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_shaped_text_prev_grapheme_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_prev_grapheme_pos>`{.interpreted-text
role="ref"}

Returns grapheme start position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_resize_object}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shaped_text_resize_object**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, key:
`Variant<class_Variant>`{.interpreted-text role="ref"}, size:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, inline_align:
`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"}, baseline: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_resize_object>`{.interpreted-text
role="ref"}

Sets new size and alignment of embedded object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_set_bidi_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_set_bidi_override**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, override:
`Array<class_Array>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_set_bidi_override>`{.interpreted-text
role="ref"}

Overrides BiDi for the structured text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_set_custom_ellipsis}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_set_custom_ellipsis**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, char:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_set_custom_ellipsis>`{.interpreted-text
role="ref"}

Sets ellipsis character used for text clipping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_set_custom_punctuation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_set_custom_punctuation**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, punct:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_set_custom_punctuation>`{.interpreted-text
role="ref"}

Sets custom punctuation character list, used for word breaking. If set
to empty string, server defaults are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_set_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_set_direction**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_set_direction>`{.interpreted-text
role="ref"}

Sets desired text direction. If set to
`TextServer.DIRECTION_AUTO<class_TextServer_constant_DIRECTION_AUTO>`{.interpreted-text
role="ref"}, direction will be detected based on the buffer contents and
current locale.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_set_orientation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_set_orientation**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_set_orientation>`{.interpreted-text
role="ref"}

Sets desired text orientation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_set_preserve_control}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_set_preserve_control**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_set_preserve_control>`{.interpreted-text
role="ref"}

If set to `true` text buffer will display control characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_set_preserve_invalid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_set_preserve_invalid**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_set_preserve_invalid>`{.interpreted-text
role="ref"}

If set to `true` text buffer will display invalid characters as
hexadecimal codes, otherwise nothing is displayed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_set_spacing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shaped_text_set_spacing**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_set_spacing>`{.interpreted-text
role="ref"}

Sets extra spacing added between glyphs or lines in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_shape}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shaped_text_shape**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_shape>`{.interpreted-text
role="ref"}

Shapes buffer if it\'s not shaped. Returns `true` if the string is
shaped successfully.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_sort_logical}
::: rst-class
classref-method
:::
::::

`const Glyph*` **\_shaped_text_sort_logical**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_sort_logical>`{.interpreted-text
role="ref"}

Returns text glyphs in the logical order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_substr}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_shaped_text_substr**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, start: `int<class_int>`{.interpreted-text role="ref"},
length: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_substr>`{.interpreted-text
role="ref"}

Returns text buffer for the substring of the text in the `shaped` text
buffer (including inline objects).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_tab_align}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_shaped_text_tab_align**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, tab_stops:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_tab_align>`{.interpreted-text
role="ref"}

Aligns shaped text to the given tab-stops.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_update_breaks}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shaped_text_update_breaks**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_update_breaks>`{.interpreted-text
role="ref"}

Updates break points in the shaped text. This method is called by
default implementation of text breaking functions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__shaped_text_update_justification_ops}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shaped_text_update_justification_ops**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__shaped_text_update_justification_ops>`{.interpreted-text
role="ref"}

Updates justification points in the shaped text. This method is called
by default implementation of text justification functions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__spoof_check}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_spoof_check**(string: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__spoof_check>`{.interpreted-text
role="ref"}

Returns `true` if `string` is likely to be an attempt at confusing the
reader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__string_get_character_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_string_get_character_breaks**(string:
`String<class_String>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__string_get_character_breaks>`{.interpreted-text
role="ref"}

Returns array of the composite character boundaries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__string_get_word_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**\_string_get_word_breaks**(string:
`String<class_String>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"}, chars_per_line:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__string_get_word_breaks>`{.interpreted-text
role="ref"}

Returns an array of the word break boundaries. Elements in the returned
array are the offsets of the start and end of words. Therefore the
length of the array is always even.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__string_to_lower}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_string_to_lower**(string: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__string_to_lower>`{.interpreted-text
role="ref"}

Returns the string converted to lowercase.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__string_to_title}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_string_to_title**(string: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__string_to_title>`{.interpreted-text
role="ref"}

Returns the string converted to title case.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__string_to_upper}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_string_to_upper**(string: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__string_to_upper>`{.interpreted-text
role="ref"}

Returns the string converted to uppercase.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__strip_diacritics}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_strip_diacritics**(string: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__strip_diacritics>`{.interpreted-text
role="ref"}

Strips diacritics from the string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__tag_to_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_tag_to_name**(tag: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__tag_to_name>`{.interpreted-text
role="ref"}

Converts OpenType tag to readable feature, variation, script, or
language name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServerExtension_private_method__unreference_oversampling_level}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_unreference_oversampling_level**(oversampling:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServerExtension_private_method__unreference_oversampling_level>`{.interpreted-text
role="ref"}

Decreases the reference count of the specified oversampling level, and
frees the font cache for oversampling level when the reference count
reaches zero. This method is called by
`Viewport<class_Viewport>`{.interpreted-text role="ref"}, and should not
be used directly.
