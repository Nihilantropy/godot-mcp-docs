github_url
:   hide

# Texture2D {#class_Texture2D}

**Inherits:** `Texture<class_Texture>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AnimatedTexture<class_AnimatedTexture>`{.interpreted-text role="ref"},
`AtlasTexture<class_AtlasTexture>`{.interpreted-text role="ref"},
`CameraTexture<class_CameraTexture>`{.interpreted-text role="ref"},
`CanvasTexture<class_CanvasTexture>`{.interpreted-text role="ref"},
`CompressedTexture2D<class_CompressedTexture2D>`{.interpreted-text
role="ref"}, `CurveTexture<class_CurveTexture>`{.interpreted-text
role="ref"}, `CurveXYZTexture<class_CurveXYZTexture>`{.interpreted-text
role="ref"}, `ExternalTexture<class_ExternalTexture>`{.interpreted-text
role="ref"},
`GradientTexture1D<class_GradientTexture1D>`{.interpreted-text
role="ref"},
`GradientTexture2D<class_GradientTexture2D>`{.interpreted-text
role="ref"}, `ImageTexture<class_ImageTexture>`{.interpreted-text
role="ref"}, `MeshTexture<class_MeshTexture>`{.interpreted-text
role="ref"}, `NoiseTexture2D<class_NoiseTexture2D>`{.interpreted-text
role="ref"},
`PlaceholderTexture2D<class_PlaceholderTexture2D>`{.interpreted-text
role="ref"},
`PortableCompressedTexture2D<class_PortableCompressedTexture2D>`{.interpreted-text
role="ref"}, `SVGTexture<class_SVGTexture>`{.interpreted-text
role="ref"}, `Texture2DRD<class_Texture2DRD>`{.interpreted-text
role="ref"}, `ViewportTexture<class_ViewportTexture>`{.interpreted-text
role="ref"}

Texture for 2D and 3D.

::: rst-class
classref-introduction-group
:::

## Description

A texture works by registering an image in the video hardware, which
then can be used in 3D models or 2D
`Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"} or GUI
`Control<class_Control>`{.interpreted-text role="ref"}.

Textures are often created by loading them from a file. See
`@GDScript.load()<class_@GDScript_method_load>`{.interpreted-text
role="ref"}.

\*\*Texture2D\*\* is a base for other resources. It cannot be used
directly.

\*\*Note:\*\* The maximum texture size is 16384×16384 pixels due to
graphics hardware limitations. Larger textures may fail to import.

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

:::: {#class_Texture2D_private_method__draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_draw**(to_canvas_item: `RID<class_RID>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, modulate: `Color<class_Color>`{.interpreted-text
role="ref"}, transpose: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2D_private_method__draw>`{.interpreted-text role="ref"}

Called when the entire **Texture2D** is requested to be drawn over a
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}, with the
top-left offset specified in `pos`. `modulate` specifies a multiplier
for the colors being drawn, while `transpose` specifies whether drawing
should be performed in column-major order instead of row-major order
(resulting in 90-degree clockwise rotation).

\*\*Note:\*\* This is only used in 2D rendering, not 3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_private_method__draw_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_draw_rect**(to_canvas_item: `RID<class_RID>`{.interpreted-text
role="ref"}, rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"},
tile: `bool<class_bool>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"}, transpose:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2D_private_method__draw_rect>`{.interpreted-text
role="ref"}

Called when the **Texture2D** is requested to be drawn onto
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}\'s
specified `rect`. `modulate` specifies a multiplier for the colors being
drawn, while `transpose` specifies whether drawing should be performed
in column-major order instead of row-major order (resulting in 90-degree
clockwise rotation).

\*\*Note:\*\* This is only used in 2D rendering, not 3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_private_method__draw_rect_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_draw_rect_region**(to_canvas_item:
`RID<class_RID>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, src_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"}, transpose:
`bool<class_bool>`{.interpreted-text role="ref"}, clip_uv:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2D_private_method__draw_rect_region>`{.interpreted-text
role="ref"}

Called when a part of the **Texture2D** specified by `src_rect`\'s
coordinates is requested to be drawn onto
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}\'s
specified `rect`. `modulate` specifies a multiplier for the colors being
drawn, while `transpose` specifies whether drawing should be performed
in column-major order instead of row-major order (resulting in 90-degree
clockwise rotation).

\*\*Note:\*\* This is only used in 2D rendering, not 3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_private_method__get_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_height**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2D_private_method__get_height>`{.interpreted-text
role="ref"}

Called when the **Texture2D**\'s height is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_private_method__get_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_width**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2D_private_method__get_width>`{.interpreted-text
role="ref"}

Called when the **Texture2D**\'s width is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_private_method__has_alpha}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_has_alpha**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2D_private_method__has_alpha>`{.interpreted-text
role="ref"}

Called when the presence of an alpha channel in the **Texture2D** is
queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_private_method__is_pixel_opaque}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_pixel_opaque**(x: `int<class_int>`{.interpreted-text role="ref"},
y: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2D_private_method__is_pixel_opaque>`{.interpreted-text
role="ref"}

Called when a pixel\'s opaque state in the **Texture2D** is queried at
the specified `(x, y)` position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_method_create_placeholder}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**create_placeholder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2D_method_create_placeholder>`{.interpreted-text
role="ref"}

Creates a placeholder version of this resource
(`PlaceholderTexture2D<class_PlaceholderTexture2D>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_method_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw**(canvas_item: `RID<class_RID>`{.interpreted-text role="ref"},
position: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
modulate: `Color<class_Color>`{.interpreted-text role="ref"} = Color(1,
1, 1, 1), transpose: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture2D_method_draw>`{.interpreted-text
role="ref"}

Draws the texture using a
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} with the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
API at the specified `position`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_method_draw_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_rect**(canvas_item: `RID<class_RID>`{.interpreted-text
role="ref"}, rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"},
tile: `bool<class_bool>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
transpose: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture2D_method_draw_rect>`{.interpreted-text
role="ref"}

Draws the texture using a
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} with the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
API.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_method_draw_rect_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_rect_region**(canvas_item: `RID<class_RID>`{.interpreted-text
role="ref"}, rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"},
src_rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
transpose: `bool<class_bool>`{.interpreted-text role="ref"} = false,
clip_uv: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture2D_method_draw_rect_region>`{.interpreted-text
role="ref"}

Draws a part of the texture using a
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} with the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
API.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_method_get_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture2D_method_get_height>`{.interpreted-text
role="ref"}

Returns the texture height in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_method_get_image}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"} **get_image**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture2D_method_get_image>`{.interpreted-text
role="ref"}

Returns an `Image<class_Image>`{.interpreted-text role="ref"} that is a
copy of data from this **Texture2D** (a new
`Image<class_Image>`{.interpreted-text role="ref"} is created each
time). `Image<class_Image>`{.interpreted-text role="ref"}s can be
accessed and manipulated directly.

\*\*Note:\*\* This will return `null` if this **Texture2D** is invalid.

\*\*Note:\*\* This will fetch the texture data from the GPU, which might
cause performance problems when overused. Avoid calling
`get_image()<class_Texture2D_method_get_image>`{.interpreted-text
role="ref"} every frame, especially on large textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_method_get_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture2D_method_get_size>`{.interpreted-text
role="ref"}

Returns the texture size in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_method_get_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_width**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture2D_method_get_width>`{.interpreted-text
role="ref"}

Returns the texture width in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture2D_method_has_alpha}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_alpha**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture2D_method_has_alpha>`{.interpreted-text
role="ref"}

Returns `true` if this **Texture2D** has an alpha channel.
