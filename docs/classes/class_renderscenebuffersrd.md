github_url
:   hide

# RenderSceneBuffersRD {#class_RenderSceneBuffersRD}

**Inherits:**
`RenderSceneBuffers<class_RenderSceneBuffers>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Render scene buffer implementation for the RenderingDevice based
renderers.

::: rst-class
classref-introduction-group
:::

## Description

This object manages all 3D rendering buffers for the rendering device
based renderers. An instance of this object is created for every
viewport that has 3D rendering enabled.

All buffers are organized in **contexts**. The default context is called
**render_buffers** and can contain amongst others the color buffer,
depth buffer, velocity buffers, VRS density map and MSAA variants of
these buffers.

Buffers are only guaranteed to exist during rendering of the viewport.

\*\*Note:\*\* This is an internal rendering server object, do not
instantiate this from script.

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

:::: {#class_RenderSceneBuffersRD_method_clear_context}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_context**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_RenderSceneBuffersRD_method_clear_context>`{.interpreted-text
role="ref"}

Frees all buffers related to this context.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_create_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**create_texture**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
data_format:
`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"}, usage_bits: `int<class_int>`{.interpreted-text role="ref"},
texture_samples:
`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, layers: `int<class_int>`{.interpreted-text role="ref"},
mipmaps: `int<class_int>`{.interpreted-text role="ref"}, unique:
`bool<class_bool>`{.interpreted-text role="ref"}, discardable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderSceneBuffersRD_method_create_texture>`{.interpreted-text
role="ref"}

Create a new texture with the given definition and cache this under the
given name. Will return the existing texture if it already exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_create_texture_from_format}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**create_texture_from_format**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, format:
`RDTextureFormat<class_RDTextureFormat>`{.interpreted-text role="ref"},
view: `RDTextureView<class_RDTextureView>`{.interpreted-text
role="ref"}, unique: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_RenderSceneBuffersRD_method_create_texture_from_format>`{.interpreted-text
role="ref"}

Create a new texture using the given format and view and cache this
under the given name. Will return the existing texture if it already
exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_create_texture_view}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**create_texture_view**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, view_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, view:
`RDTextureView<class_RDTextureView>`{.interpreted-text role="ref"})
`🔗<class_RenderSceneBuffersRD_method_create_texture_view>`{.interpreted-text
role="ref"}

Create a new texture view for an existing texture and cache this under
the given `view_name`. Will return the existing texture view if it
already exists. Will error if the source texture doesn\'t exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_color_layer}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_color_layer**(layer: `int<class_int>`{.interpreted-text
role="ref"}, msaa: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_RenderSceneBuffersRD_method_get_color_layer>`{.interpreted-text
role="ref"}

Returns the specified layer from the color texture we are rendering 3D
content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant
of the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_color_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_color_texture**(msaa: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_RenderSceneBuffersRD_method_get_color_texture>`{.interpreted-text
role="ref"}

Returns the color texture we are rendering 3D content to. If multiview
is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant
of the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_depth_layer}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_depth_layer**(layer: `int<class_int>`{.interpreted-text
role="ref"}, msaa: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_RenderSceneBuffersRD_method_get_depth_layer>`{.interpreted-text
role="ref"}

Returns the specified layer from the depth texture we are rendering 3D
content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant
of the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_depth_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_depth_texture**(msaa: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_RenderSceneBuffersRD_method_get_depth_texture>`{.interpreted-text
role="ref"}

Returns the depth texture we are rendering 3D content to. If multiview
is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant
of the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_fsr_sharpness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_fsr_sharpness**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_fsr_sharpness>`{.interpreted-text
role="ref"}

Returns the FSR sharpness value used while rendering the 3D content (if
`get_scaling_3d_mode()<class_RenderSceneBuffersRD_method_get_scaling_3d_mode>`{.interpreted-text
role="ref"} is an FSR mode).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_internal_size}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_internal_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_internal_size>`{.interpreted-text
role="ref"}

Returns the internal size of the render buffer (size before upscaling)
with which textures are created by default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_msaa_3d}
::: rst-class
classref-method
:::
::::

`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"} **get_msaa_3d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_msaa_3d>`{.interpreted-text
role="ref"}

Returns the applied 3D MSAA mode for this viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_render_target}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_render_target**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_render_target>`{.interpreted-text
role="ref"}

Returns the render target associated with this buffers object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_scaling_3d_mode}
::: rst-class
classref-method
:::
::::

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} **get_scaling_3d_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_scaling_3d_mode>`{.interpreted-text
role="ref"}

Returns the scaling mode used for upscaling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_screen_space_aa}
::: rst-class
classref-method
:::
::::

`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
role="ref"} **get_screen_space_aa**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_screen_space_aa>`{.interpreted-text
role="ref"}

Returns the screen-space antialiasing method applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_target_size}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_target_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_target_size>`{.interpreted-text
role="ref"}

Returns the target size of the render buffer (size after upscaling).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_texture**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_texture>`{.interpreted-text
role="ref"}

Returns a cached texture with this name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_texture_format}
::: rst-class
classref-method
:::
::::

`RDTextureFormat<class_RDTextureFormat>`{.interpreted-text role="ref"}
**get_texture_format**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_texture_format>`{.interpreted-text
role="ref"}

Returns the texture format information with which a cached texture was
created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_texture_samples}
::: rst-class
classref-method
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **get_texture_samples**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_texture_samples>`{.interpreted-text
role="ref"}

Returns the number of MSAA samples used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_texture_slice}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_texture_slice**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, layer:
`int<class_int>`{.interpreted-text role="ref"}, mipmap:
`int<class_int>`{.interpreted-text role="ref"}, layers:
`int<class_int>`{.interpreted-text role="ref"}, mipmaps:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderSceneBuffersRD_method_get_texture_slice>`{.interpreted-text
role="ref"}

Returns a specific slice (layer or mipmap) for a cached texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_texture_slice_size}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_texture_slice_size**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, mipmap:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderSceneBuffersRD_method_get_texture_slice_size>`{.interpreted-text
role="ref"}

Returns the texture size of a given slice of a cached texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_texture_slice_view}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_texture_slice_view**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, layer:
`int<class_int>`{.interpreted-text role="ref"}, mipmap:
`int<class_int>`{.interpreted-text role="ref"}, layers:
`int<class_int>`{.interpreted-text role="ref"}, mipmaps:
`int<class_int>`{.interpreted-text role="ref"}, view:
`RDTextureView<class_RDTextureView>`{.interpreted-text role="ref"})
`🔗<class_RenderSceneBuffersRD_method_get_texture_slice_view>`{.interpreted-text
role="ref"}

Returns a specific view of a slice (layer or mipmap) for a cached
texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_use_debanding}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_use_debanding**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_use_debanding>`{.interpreted-text
role="ref"}

Returns `true` if debanding is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_use_taa}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_use_taa**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_use_taa>`{.interpreted-text
role="ref"}

Returns `true` if TAA is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_velocity_layer}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_velocity_layer**(layer: `int<class_int>`{.interpreted-text
role="ref"}, msaa: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_RenderSceneBuffersRD_method_get_velocity_layer>`{.interpreted-text
role="ref"}

Returns the specified layer from the velocity texture we are rendering
3D content to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_velocity_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_velocity_texture**(msaa: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_RenderSceneBuffersRD_method_get_velocity_texture>`{.interpreted-text
role="ref"}

Returns the velocity texture we are rendering 3D content to. If
multiview is used this will be a texture array with all views.

If `msaa` is **true** and MSAA is enabled, this returns the MSAA variant
of the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_get_view_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_view_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_get_view_count>`{.interpreted-text
role="ref"}

Returns the view count for the associated viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersRD_method_has_texture}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_texture**(context:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersRD_method_has_texture>`{.interpreted-text
role="ref"}

Returns `true` if a cached texture exists for this name.
