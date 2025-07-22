github_url
:   hide

# CanvasItem {#class_CanvasItem}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `Control<class_Control>`{.interpreted-text
role="ref"}, `Node2D<class_Node2D>`{.interpreted-text role="ref"}

Abstract base class for everything in 2D space.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for everything in 2D space. Canvas items are laid
out in a tree; children inherit and extend their parent\'s transform.
**CanvasItem** is extended by `Control<class_Control>`{.interpreted-text
role="ref"} for GUI-related nodes, and by
`Node2D<class_Node2D>`{.interpreted-text role="ref"} for 2D game
objects.

Any **CanvasItem** can draw. For this,
`queue_redraw()<class_CanvasItem_method_queue_redraw>`{.interpreted-text
role="ref"} is called by the engine, then
`NOTIFICATION_DRAW<class_CanvasItem_constant_NOTIFICATION_DRAW>`{.interpreted-text
role="ref"} will be received on idle time to request a redraw. Because
of this, canvas items don\'t need to be redrawn on every frame,
improving the performance significantly. Several functions for drawing
on the **CanvasItem** are provided (see `draw_*` functions). However,
they can only be used inside
`_draw()<class_CanvasItem_private_method__draw>`{.interpreted-text
role="ref"}, its corresponding
`Object._notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"} or methods connected to the
`draw<class_CanvasItem_signal_draw>`{.interpreted-text role="ref"}
signal.

Canvas items are drawn in tree order on their canvas layer. By default,
children are on top of their parents, so a root **CanvasItem** will be
drawn behind everything. This behavior can be changed on a per-item
basis.

A **CanvasItem** can be hidden, which will also hide its children. By
adjusting various other properties of a **CanvasItem**, you can also
modulate its color (via
`modulate<class_CanvasItem_property_modulate>`{.interpreted-text
role="ref"} or
`self_modulate<class_CanvasItem_property_self_modulate>`{.interpreted-text
role="ref"}), change its Z-index, blend mode, and more.

Note that properties like transform, modulation, and visibility are only
propagated to *direct* **CanvasItem** child nodes. If there is a
non-**CanvasItem** node in between, like
`Node<class_Node>`{.interpreted-text role="ref"} or
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"},
the **CanvasItem** nodes below will have an independent position and
`modulate<class_CanvasItem_property_modulate>`{.interpreted-text
role="ref"} chain. See also
`top_level<class_CanvasItem_property_top_level>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Viewport and canvas transforms <../tutorials/2d/2d_transforms>`{.interpreted-text
  role="doc"}
- `Custom drawing in 2D <../tutorials/2d/custom_drawing_in_2d>`{.interpreted-text
  role="doc"}
- [Audio Spectrum Visualizer
  Demo](https://godotengine.org/asset-library/asset/2762)

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

## Signals

:::: {#class_CanvasItem_signal_draw}
::: rst-class
classref-signal
:::
::::

**draw**() `🔗<class_CanvasItem_signal_draw>`{.interpreted-text
role="ref"}

Emitted when the **CanvasItem** must redraw, *after* the related
`NOTIFICATION_DRAW<class_CanvasItem_constant_NOTIFICATION_DRAW>`{.interpreted-text
role="ref"} notification, and *before*
`_draw()<class_CanvasItem_private_method__draw>`{.interpreted-text
role="ref"} is called.

\*\*Note:\*\* Deferred connections do not allow drawing through the
`draw_*` methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_signal_hidden}
::: rst-class
classref-signal
:::
::::

**hidden**() `🔗<class_CanvasItem_signal_hidden>`{.interpreted-text
role="ref"}

Emitted when this node becomes hidden, i.e. it\'s no longer visible in
the tree (see
`is_visible_in_tree()<class_CanvasItem_method_is_visible_in_tree>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_signal_item_rect_changed}
::: rst-class
classref-signal
:::
::::

**item_rect_changed**()
`🔗<class_CanvasItem_signal_item_rect_changed>`{.interpreted-text
role="ref"}

Emitted when the **CanvasItem**\'s boundaries (position or size) change,
or when an action took place that may have affected these boundaries
(e.g. changing
`Sprite2D.texture<class_Sprite2D_property_texture>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_signal_visibility_changed}
::: rst-class
classref-signal
:::
::::

**visibility_changed**()
`🔗<class_CanvasItem_signal_visibility_changed>`{.interpreted-text
role="ref"}

Emitted when the **CanvasItem**\'s visibility changes, either because
its own `visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property changed or because its visibility in the tree
changed (see
`is_visible_in_tree()<class_CanvasItem_method_is_visible_in_tree>`{.interpreted-text
role="ref"}).

This signal is emitted *after* the related
`NOTIFICATION_VISIBILITY_CHANGED<class_CanvasItem_constant_NOTIFICATION_VISIBILITY_CHANGED>`{.interpreted-text
role="ref"} notification.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_CanvasItem_TextureFilter}
::: rst-class
classref-enumeration
:::
::::

enum **TextureFilter**:
`🔗<enum_CanvasItem_TextureFilter>`{.interpreted-text role="ref"}

:::: {#class_CanvasItem_constant_TEXTURE_FILTER_PARENT_NODE}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **TEXTURE_FILTER_PARENT_NODE** = `0`

The **CanvasItem** will inherit the filter from its parent.

:::: {#class_CanvasItem_constant_TEXTURE_FILTER_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **TEXTURE_FILTER_NEAREST** = `1`

The texture filter reads from the nearest pixel only. This makes the
texture look pixelated from up close, and grainy from a distance (due to
mipmaps not being sampled).

:::: {#class_CanvasItem_constant_TEXTURE_FILTER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **TEXTURE_FILTER_LINEAR** = `2`

The texture filter blends between the nearest 4 pixels. This makes the
texture look smooth from up close, and grainy from a distance (due to
mipmaps not being sampled).

:::: {#class_CanvasItem_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **TEXTURE_FILTER_NEAREST_WITH_MIPMAPS** = `3`

The texture filter reads from the nearest pixel and blends between the
nearest 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`). This makes the texture look pixelated from up
close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale
(e.g. due to `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
zoom or sprite scaling), as mipmaps are important to smooth out pixels
that are smaller than on-screen pixels.

:::: {#class_CanvasItem_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **TEXTURE_FILTER_LINEAR_WITH_MIPMAPS** = `4`

The texture filter blends between the nearest 4 pixels and between the
nearest 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`). This makes the texture look smooth from up
close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale
(e.g. due to `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
zoom or sprite scaling), as mipmaps are important to smooth out pixels
that are smaller than on-screen pixels.

:::: {#class_CanvasItem_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC** = `5`

The texture filter reads from the nearest pixel and blends between 2
mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`) based on the angle between the surface and the
camera view. This makes the texture look pixelated from up close, and
smooth from a distance. Anisotropic filtering improves texture quality
on surfaces that are almost in line with the camera, but is slightly
slower. The anisotropic filtering level can be changed by adjusting
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This texture filter is rarely useful in 2D projects.
`TEXTURE_FILTER_NEAREST_WITH_MIPMAPS<class_CanvasItem_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS>`{.interpreted-text
role="ref"} is usually more appropriate in this case.

:::: {#class_CanvasItem_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC** = `6`

The texture filter blends between the nearest 4 pixels and blends
between 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`) based on the angle between the surface and the
camera view. This makes the texture look smooth from up close, and
smooth from a distance. Anisotropic filtering improves texture quality
on surfaces that are almost in line with the camera, but is slightly
slower. The anisotropic filtering level can be changed by adjusting
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This texture filter is rarely useful in 2D projects.
`TEXTURE_FILTER_LINEAR_WITH_MIPMAPS<class_CanvasItem_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS>`{.interpreted-text
role="ref"} is usually more appropriate in this case.

:::: {#class_CanvasItem_constant_TEXTURE_FILTER_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **TEXTURE_FILTER_MAX** = `7`

Represents the size of the
`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CanvasItem_TextureRepeat}
::: rst-class
classref-enumeration
:::
::::

enum **TextureRepeat**:
`🔗<enum_CanvasItem_TextureRepeat>`{.interpreted-text role="ref"}

:::: {#class_CanvasItem_constant_TEXTURE_REPEAT_PARENT_NODE}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
role="ref"} **TEXTURE_REPEAT_PARENT_NODE** = `0`

The **CanvasItem** will inherit the filter from its parent.

:::: {#class_CanvasItem_constant_TEXTURE_REPEAT_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
role="ref"} **TEXTURE_REPEAT_DISABLED** = `1`

The texture does not repeat. Sampling the texture outside its extents
will result in \"stretching\" of the edge pixels. You can avoid this by
ensuring a 1-pixel fully transparent border on each side of the texture.

:::: {#class_CanvasItem_constant_TEXTURE_REPEAT_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
role="ref"} **TEXTURE_REPEAT_ENABLED** = `2`

The texture repeats when exceeding the texture\'s size.

:::: {#class_CanvasItem_constant_TEXTURE_REPEAT_MIRROR}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
role="ref"} **TEXTURE_REPEAT_MIRROR** = `3`

The texture repeats when the exceeding the texture\'s size in a \"2×2
tiled mode\". Repeated textures at even positions are mirrored.

:::: {#class_CanvasItem_constant_TEXTURE_REPEAT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
role="ref"} **TEXTURE_REPEAT_MAX** = `4`

Represents the size of the
`TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CanvasItem_ClipChildrenMode}
::: rst-class
classref-enumeration
:::
::::

enum **ClipChildrenMode**:
`🔗<enum_CanvasItem_ClipChildrenMode>`{.interpreted-text role="ref"}

:::: {#class_CanvasItem_constant_CLIP_CHILDREN_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ClipChildrenMode<enum_CanvasItem_ClipChildrenMode>`{.interpreted-text
role="ref"} **CLIP_CHILDREN_DISABLED** = `0`

Children are drawn over this node and are not clipped.

:::: {#class_CanvasItem_constant_CLIP_CHILDREN_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`ClipChildrenMode<enum_CanvasItem_ClipChildrenMode>`{.interpreted-text
role="ref"} **CLIP_CHILDREN_ONLY** = `1`

This node is used as a mask and is **not** drawn. The mask is based on
this node\'s alpha channel: Opaque pixels are kept, transparent pixels
are discarded, and semi-transparent pixels are blended in according to
their opacity. Children are clipped to this node\'s drawn area.

:::: {#class_CanvasItem_constant_CLIP_CHILDREN_AND_DRAW}
::: rst-class
classref-enumeration-constant
:::
::::

`ClipChildrenMode<enum_CanvasItem_ClipChildrenMode>`{.interpreted-text
role="ref"} **CLIP_CHILDREN_AND_DRAW** = `2`

This node is used as a mask and is also drawn. The mask is based on this
node\'s alpha channel: Opaque pixels are kept, transparent pixels are
discarded, and semi-transparent pixels are blended in according to their
opacity. Children are clipped to the parent\'s drawn area.

:::: {#class_CanvasItem_constant_CLIP_CHILDREN_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ClipChildrenMode<enum_CanvasItem_ClipChildrenMode>`{.interpreted-text
role="ref"} **CLIP_CHILDREN_MAX** = `3`

Represents the size of the
`ClipChildrenMode<enum_CanvasItem_ClipChildrenMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_CanvasItem_constant_NOTIFICATION_TRANSFORM_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_TRANSFORM_CHANGED** = `2000`
`🔗<class_CanvasItem_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"}

Notification received when this node\'s global transform changes, if
`is_transform_notification_enabled()<class_CanvasItem_method_is_transform_notification_enabled>`{.interpreted-text
role="ref"} is `true`. See also
`set_notify_transform()<class_CanvasItem_method_set_notify_transform>`{.interpreted-text
role="ref"} and
`get_transform()<class_CanvasItem_method_get_transform>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Many canvas items such as
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"} or
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} automatically enable this in order to function correctly.

:::: {#class_CanvasItem_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_LOCAL_TRANSFORM_CHANGED** = `35`
`🔗<class_CanvasItem_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"}

Notification received when this node\'s transform changes, if
`is_local_transform_notification_enabled()<class_CanvasItem_method_is_local_transform_notification_enabled>`{.interpreted-text
role="ref"} is `true`. This is not received when a parent
`Node2D<class_Node2D>`{.interpreted-text role="ref"}\'s transform
changes. See also
`set_notify_local_transform()<class_CanvasItem_method_set_notify_local_transform>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Many canvas items such as
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"} or
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text role="ref"}
automatically enable this in order to function correctly.

:::: {#class_CanvasItem_constant_NOTIFICATION_DRAW}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_DRAW** = `30`
`🔗<class_CanvasItem_constant_NOTIFICATION_DRAW>`{.interpreted-text
role="ref"}

The **CanvasItem** is requested to draw (see
`_draw()<class_CanvasItem_private_method__draw>`{.interpreted-text
role="ref"}).

:::: {#class_CanvasItem_constant_NOTIFICATION_VISIBILITY_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_VISIBILITY_CHANGED** = `31`
`🔗<class_CanvasItem_constant_NOTIFICATION_VISIBILITY_CHANGED>`{.interpreted-text
role="ref"}

Notification received when this node\'s visibility changes (see
`visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} and
`is_visible_in_tree()<class_CanvasItem_method_is_visible_in_tree>`{.interpreted-text
role="ref"}).

This notification is received *before* the related
`visibility_changed<class_CanvasItem_signal_visibility_changed>`{.interpreted-text
role="ref"} signal.

:::: {#class_CanvasItem_constant_NOTIFICATION_ENTER_CANVAS}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_ENTER_CANVAS** = `32`
`🔗<class_CanvasItem_constant_NOTIFICATION_ENTER_CANVAS>`{.interpreted-text
role="ref"}

The **CanvasItem** has entered the canvas.

:::: {#class_CanvasItem_constant_NOTIFICATION_EXIT_CANVAS}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_EXIT_CANVAS** = `33`
`🔗<class_CanvasItem_constant_NOTIFICATION_EXIT_CANVAS>`{.interpreted-text
role="ref"}

The **CanvasItem** has exited the canvas.

:::: {#class_CanvasItem_constant_NOTIFICATION_WORLD_2D_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WORLD_2D_CHANGED** = `36`
`🔗<class_CanvasItem_constant_NOTIFICATION_WORLD_2D_CHANGED>`{.interpreted-text
role="ref"}

Notification received when this **CanvasItem** is registered to a new
`World2D<class_World2D>`{.interpreted-text role="ref"} (see
`get_world_2d()<class_CanvasItem_method_get_world_2d>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CanvasItem_property_clip_children}
::: rst-class
classref-property
:::
::::

`ClipChildrenMode<enum_CanvasItem_ClipChildrenMode>`{.interpreted-text
role="ref"} **clip_children** = `0`
`🔗<class_CanvasItem_property_clip_children>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_clip_children_mode**(value:
  `ClipChildrenMode<enum_CanvasItem_ClipChildrenMode>`{.interpreted-text
  role="ref"})
- `ClipChildrenMode<enum_CanvasItem_ClipChildrenMode>`{.interpreted-text
  role="ref"} **get_clip_children_mode**()

The mode in which this node clips its children, acting as a mask.

\*\*Note:\*\* Clipping nodes cannot be nested or placed within a
`CanvasGroup<class_CanvasGroup>`{.interpreted-text role="ref"}. If an
ancestor of this node clips its children or is a
`CanvasGroup<class_CanvasGroup>`{.interpreted-text role="ref"}, then
this node\'s clip mode should be set to
`CLIP_CHILDREN_DISABLED<class_CanvasItem_constant_CLIP_CHILDREN_DISABLED>`{.interpreted-text
role="ref"} to avoid unexpected behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_light_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **light_mask** = `1`
`🔗<class_CanvasItem_property_light_mask>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_light_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_light_mask**()

The rendering layers in which this **CanvasItem** responds to
`Light2D<class_Light2D>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_CanvasItem_property_material>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

The material applied to this **CanvasItem**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_modulate}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **modulate** =
`Color(1, 1, 1, 1)`
`🔗<class_CanvasItem_property_modulate>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modulate**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_modulate**()

The color applied to this **CanvasItem**. This property does affect
child **CanvasItem**s, unlike
`self_modulate<class_CanvasItem_property_self_modulate>`{.interpreted-text
role="ref"} which only affects the node itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_self_modulate}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **self_modulate** =
`Color(1, 1, 1, 1)`
`🔗<class_CanvasItem_property_self_modulate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_self_modulate**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_self_modulate**()

The color applied to this **CanvasItem**. This property does **not**
affect child **CanvasItem**s, unlike
`modulate<class_CanvasItem_property_modulate>`{.interpreted-text
role="ref"} which affects both the node itself and its children.

\*\*Note:\*\* Internal children are also not affected by this property
(see the `include_internal` parameter in
`Node.add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}). For built-in nodes this includes sliders in
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"}, and the
tab bar in `TabContainer<class_TabContainer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_show_behind_parent}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_behind_parent**
= `false`
`🔗<class_CanvasItem_property_show_behind_parent>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_behind_parent**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_draw_behind_parent_enabled**()

If `true`, this node draws behind its parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_texture_filter}
::: rst-class
classref-property
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **texture_filter** = `0`
`🔗<class_CanvasItem_property_texture_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_filter**(value:
  `TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
  role="ref"})
- `TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
  role="ref"} **get_texture_filter**()

The filtering mode used to render this **CanvasItem**\'s texture(s).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_texture_repeat}
::: rst-class
classref-property
:::
::::

`TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
role="ref"} **texture_repeat** = `0`
`🔗<class_CanvasItem_property_texture_repeat>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_repeat**(value:
  `TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
  role="ref"})
- `TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
  role="ref"} **get_texture_repeat**()

The repeating mode used to render this **CanvasItem**\'s texture(s). It
affects what happens when the texture is sampled outside its extents,
for example by setting a
`Sprite2D.region_rect<class_Sprite2D_property_region_rect>`{.interpreted-text
role="ref"} that is larger than the texture or assigning
`Polygon2D<class_Polygon2D>`{.interpreted-text role="ref"} UV points
outside the texture.

\*\*Note:\*\* `TextureRect<class_TextureRect>`{.interpreted-text
role="ref"} is not affected by
`texture_repeat<class_CanvasItem_property_texture_repeat>`{.interpreted-text
role="ref"}, as it uses its own texture repeating implementation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_top_level}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **top_level** = `false`
`🔗<class_CanvasItem_property_top_level>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_as_top_level**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_set_as_top_level**()

If `true`, this **CanvasItem** will *not* inherit its transform from
parent **CanvasItem**s. Its draw order will also be changed to make it
draw on top of other **CanvasItem**s that do not have
`top_level<class_CanvasItem_property_top_level>`{.interpreted-text
role="ref"} set to `true`. The **CanvasItem** will effectively act as if
it was placed as a child of a bare `Node<class_Node>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_use_parent_material}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_parent_material**
= `false`
`🔗<class_CanvasItem_property_use_parent_material>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_parent_material**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_parent_material**()

If `true`, the parent **CanvasItem**\'s
`material<class_CanvasItem_property_material>`{.interpreted-text
role="ref"} is used as this node\'s material.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_visibility_layer}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **visibility_layer** =
`1` `🔗<class_CanvasItem_property_visibility_layer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visibility_layer**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_visibility_layer**()

The rendering layer in which this **CanvasItem** is rendered by
`Viewport<class_Viewport>`{.interpreted-text role="ref"} nodes. A
`Viewport<class_Viewport>`{.interpreted-text role="ref"} will render a
**CanvasItem** if it and all its parents share a layer with the
`Viewport<class_Viewport>`{.interpreted-text role="ref"}\'s canvas cull
mask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **visible** = `true`
`🔗<class_CanvasItem_property_visible>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_visible**()

If `true`, this **CanvasItem** may be drawn. Whether this **CanvasItem**
is actually drawn depends on the visibility of all of its **CanvasItem**
ancestors. In other words: this **CanvasItem** will be drawn when
`is_visible_in_tree()<class_CanvasItem_method_is_visible_in_tree>`{.interpreted-text
role="ref"} returns `true` and all **CanvasItem** ancestors share at
least one
`visibility_layer<class_CanvasItem_property_visibility_layer>`{.interpreted-text
role="ref"} with this **CanvasItem**.

\*\*Note:\*\* For controls that inherit
`Popup<class_Popup>`{.interpreted-text role="ref"}, the correct way to
make them visible is to call one of the multiple `popup*()` functions
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_y_sort_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **y_sort_enabled** =
`false` `🔗<class_CanvasItem_property_y_sort_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_y_sort_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_y_sort_enabled**()

If `true`, this and child **CanvasItem** nodes with a higher Y position
are rendered in front of nodes with a lower Y position. If `false`, this
and child **CanvasItem** nodes are rendered normally in scene tree
order.

With Y-sorting enabled on a parent node (\'A\') but disabled on a child
node (\'B\'), the child node (\'B\') is sorted but its children (\'C1\',
\'C2\', etc.) render together on the same Y position as the child node
(\'B\'). This allows you to organize the render order of a scene without
changing the scene tree.

Nodes sort relative to each other only if they are on the same
`z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_z_as_relative}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **z_as_relative** =
`true` `🔗<class_CanvasItem_property_z_as_relative>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_z_as_relative**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_z_relative**()

If `true`, this node\'s final Z index is relative to its parent\'s Z
index.

For example, if
`z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} is `2` and its parent\'s final Z index is `3`, then this
node\'s final Z index will be `5` (`2 + 3`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_property_z_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **z_index** = `0`
`🔗<class_CanvasItem_property_z_index>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_z_index**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_z_index**()

The order in which this node is drawn. A node with a higher Z index will
display in front of others. Must be between
`RenderingServer.CANVAS_ITEM_Z_MIN<class_RenderingServer_constant_CANVAS_ITEM_Z_MIN>`{.interpreted-text
role="ref"} and
`RenderingServer.CANVAS_ITEM_Z_MAX<class_RenderingServer_constant_CANVAS_ITEM_Z_MAX>`{.interpreted-text
role="ref"} (inclusive).

\*\*Note:\*\* The Z index does **not** affect the order in which
**CanvasItem** nodes are processed or the way input events are handled.
This is especially important to keep in mind for
`Control<class_Control>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CanvasItem_private_method__draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_draw**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_private_method__draw>`{.interpreted-text
role="ref"}

Called when **CanvasItem** has been requested to redraw (after
`queue_redraw()<class_CanvasItem_method_queue_redraw>`{.interpreted-text
role="ref"} is called, either manually or by the engine).

Corresponds to the
`NOTIFICATION_DRAW<class_CanvasItem_constant_NOTIFICATION_DRAW>`{.interpreted-text
role="ref"} notification in
`Object._notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_animation_slice}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_animation_slice**(animation_length:
`float<class_float>`{.interpreted-text role="ref"}, slice_begin:
`float<class_float>`{.interpreted-text role="ref"}, slice_end:
`float<class_float>`{.interpreted-text role="ref"}, offset:
`float<class_float>`{.interpreted-text role="ref"} = 0.0)
`🔗<class_CanvasItem_method_draw_animation_slice>`{.interpreted-text
role="ref"}

Subsequent drawing commands will be ignored unless they fall within the
specified animation slice. This is a faster way to implement animations
that loop on background rather than redrawing constantly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_arc}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_arc**(center: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, radius: `float<class_float>`{.interpreted-text role="ref"},
start_angle: `float<class_float>`{.interpreted-text role="ref"},
end_angle: `float<class_float>`{.interpreted-text role="ref"},
point_count: `int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"}, width:
`float<class_float>`{.interpreted-text role="ref"} = -1.0, antialiased:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CanvasItem_method_draw_arc>`{.interpreted-text role="ref"}

Draws an unfilled arc between the given angles with a uniform `color`
and `width` and optional antialiasing (supported only for positive
`width`). The larger the value of `point_count`, the smoother the curve.
See also
`draw_circle()<class_CanvasItem_method_draw_circle>`{.interpreted-text
role="ref"}.

If `width` is negative, it will be ignored and the arc will be drawn
using
`RenderingServer.PRIMITIVE_LINE_STRIP<class_RenderingServer_constant_PRIMITIVE_LINE_STRIP>`{.interpreted-text
role="ref"}. This means that when the CanvasItem is scaled, the arc will
remain thin. If this behavior is not desired, then pass a positive
`width` like `1.0`.

The arc is drawn from `start_angle` towards the value of `end_angle` so
in clockwise direction if `start_angle < end_angle` and
counter-clockwise otherwise. Passing the same angles but in reversed
order will produce the same arc. If absolute difference of `start_angle`
and `end_angle` is greater than
`@GDScript.TAU<class_@GDScript_constant_TAU>`{.interpreted-text
role="ref"} radians, then a full circle arc is drawn (i.e. arc will not
overlap itself).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_char}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_char**(font: `Font<class_Font>`{.interpreted-text role="ref"},
pos: `Vector2<class_Vector2>`{.interpreted-text role="ref"}, char:
`String<class_String>`{.interpreted-text role="ref"}, font_size:
`int<class_int>`{.interpreted-text role="ref"} = 16, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CanvasItem_method_draw_char>`{.interpreted-text
role="ref"}

Draws a string first character using a custom font. If `oversampling` is
greater than zero, it is used as font oversampling factor, otherwise
viewport oversampling settings are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_char_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_char_outline**(font: `Font<class_Font>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, char: `String<class_String>`{.interpreted-text role="ref"},
font_size: `int<class_int>`{.interpreted-text role="ref"} = 16, size:
`int<class_int>`{.interpreted-text role="ref"} = -1, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_draw_char_outline>`{.interpreted-text
role="ref"}

Draws a string first character outline using a custom font. If
`oversampling` is greater than zero, it is used as font oversampling
factor, otherwise viewport oversampling settings are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_circle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_circle**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, radius: `float<class_float>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"}, filled:
`bool<class_bool>`{.interpreted-text role="ref"} = true, width:
`float<class_float>`{.interpreted-text role="ref"} = -1.0, antialiased:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CanvasItem_method_draw_circle>`{.interpreted-text role="ref"}

Draws a circle. See also
`draw_arc()<class_CanvasItem_method_draw_arc>`{.interpreted-text
role="ref"},
`draw_polyline()<class_CanvasItem_method_draw_polyline>`{.interpreted-text
role="ref"}, and
`draw_polygon()<class_CanvasItem_method_draw_polygon>`{.interpreted-text
role="ref"}.

If `filled` is `true`, the circle will be filled with the `color`
specified. If `filled` is `false`, the circle will be drawn as a stroke
with the `color` and `width` specified.

If `width` is negative, then two-point primitives will be drawn instead
of a four-point ones. This means that when the CanvasItem is scaled, the
lines will remain thin. If this behavior is not desired, then pass a
positive `width` like `1.0`.

If `antialiased` is `true`, half transparent \"feathers\" will be
attached to the boundary, making outlines smooth.

\*\*Note:\*\* `width` is only effective if `filled` is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_colored_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_colored_polygon**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"},
uvs: `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} = PackedVector2Array(), texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} = null)
`🔗<class_CanvasItem_method_draw_colored_polygon>`{.interpreted-text
role="ref"}

Draws a colored polygon of any number of points, convex or concave.
Unlike
`draw_polygon()<class_CanvasItem_method_draw_polygon>`{.interpreted-text
role="ref"}, a single color must be specified for the whole polygon.

\*\*Note:\*\* If you frequently redraw the same polygon with a large
number of vertices, consider pre-calculating the triangulation with
`Geometry2D.triangulate_polygon()<class_Geometry2D_method_triangulate_polygon>`{.interpreted-text
role="ref"} and using
`draw_mesh()<class_CanvasItem_method_draw_mesh>`{.interpreted-text
role="ref"},
`draw_multimesh()<class_CanvasItem_method_draw_multimesh>`{.interpreted-text
role="ref"}, or
`RenderingServer.canvas_item_add_triangle_array()<class_RenderingServer_method_canvas_item_add_triangle_array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_dashed_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_dashed_line**(from: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, to: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"}, width:
`float<class_float>`{.interpreted-text role="ref"} = -1.0, dash:
`float<class_float>`{.interpreted-text role="ref"} = 2.0, aligned:
`bool<class_bool>`{.interpreted-text role="ref"} = true, antialiased:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CanvasItem_method_draw_dashed_line>`{.interpreted-text
role="ref"}

Draws a dashed line from a 2D point to another, with a given color and
width. See also
`draw_line()<class_CanvasItem_method_draw_line>`{.interpreted-text
role="ref"},
`draw_multiline()<class_CanvasItem_method_draw_multiline>`{.interpreted-text
role="ref"}, and
`draw_polyline()<class_CanvasItem_method_draw_polyline>`{.interpreted-text
role="ref"}.

If `width` is negative, then a two-point primitives will be drawn
instead of a four-point ones. This means that when the CanvasItem is
scaled, the line parts will remain thin. If this behavior is not
desired, then pass a positive `width` like `1.0`.

`dash` is the length of each dash in pixels, with the gap between each
dash being the same length. If `aligned` is `true`, the length of the
first and last dashes may be shortened or lengthened to allow the line
to begin and end at the precise points defined by `from` and `to`. Both
ends are always symmetrical when `aligned` is `true`. If `aligned` is
`false`, all dashes will have the same length, but the line may appear
incomplete at the end due to the dash length not dividing evenly into
the line length. Only full dashes are drawn when `aligned` is `false`.

If `antialiased` is `true`, half transparent \"feathers\" will be
attached to the boundary, making outlines smooth.

\*\*Note:\*\* `antialiased` is only effective if `width` is greater than
`0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_end_animation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_end_animation**()
`🔗<class_CanvasItem_method_draw_end_animation>`{.interpreted-text
role="ref"}

After submitting all animations slices via
`draw_animation_slice()<class_CanvasItem_method_draw_animation_slice>`{.interpreted-text
role="ref"}, this function can be used to revert drawing to its default
state (all subsequent drawing commands will be visible). If you don\'t
care about this particular use case, usage of this function after
submitting the slices is not required.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_lcd_texture_rect_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_lcd_texture_rect_region**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, src_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1))
`🔗<class_CanvasItem_method_draw_lcd_texture_rect_region>`{.interpreted-text
role="ref"}

Draws a textured rectangle region of the font texture with LCD subpixel
anti-aliasing at a given position, optionally modulated by a color.

Texture is drawn using the following blend operation, blend mode of the
`CanvasItemMaterial<class_CanvasItemMaterial>`{.interpreted-text
role="ref"} is ignored:

    dst.r = texture.r * modulate.r * modulate.a + dst.r * (1.0 - texture.r * modulate.a);
    dst.g = texture.g * modulate.g * modulate.a + dst.g * (1.0 - texture.g * modulate.a);
    dst.b = texture.b * modulate.b * modulate.a + dst.b * (1.0 - texture.b * modulate.a);
    dst.a = modulate.a + dst.a * (1.0 - modulate.a);

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_line**(from: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, to: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"}, width:
`float<class_float>`{.interpreted-text role="ref"} = -1.0, antialiased:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CanvasItem_method_draw_line>`{.interpreted-text role="ref"}

Draws a line from a 2D point to another, with a given color and width.
It can be optionally antialiased. See also
`draw_dashed_line()<class_CanvasItem_method_draw_dashed_line>`{.interpreted-text
role="ref"},
`draw_multiline()<class_CanvasItem_method_draw_multiline>`{.interpreted-text
role="ref"}, and
`draw_polyline()<class_CanvasItem_method_draw_polyline>`{.interpreted-text
role="ref"}.

If `width` is negative, then a two-point primitive will be drawn instead
of a four-point one. This means that when the CanvasItem is scaled, the
line will remain thin. If this behavior is not desired, then pass a
positive `width` like `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_mesh**(mesh: `Mesh<class_Mesh>`{.interpreted-text role="ref"},
texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"},
transform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"} = Transform2D(1, 0, 0, 1, 0, 0), modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1))
`🔗<class_CanvasItem_method_draw_mesh>`{.interpreted-text role="ref"}

Draws a `Mesh<class_Mesh>`{.interpreted-text role="ref"} in 2D, using
the provided texture. See
`MeshInstance2D<class_MeshInstance2D>`{.interpreted-text role="ref"} for
related documentation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_msdf_texture_rect_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_msdf_texture_rect_region**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, src_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
outline: `float<class_float>`{.interpreted-text role="ref"} = 0.0,
pixel_range: `float<class_float>`{.interpreted-text role="ref"} = 4.0,
scale: `float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_CanvasItem_method_draw_msdf_texture_rect_region>`{.interpreted-text
role="ref"}

Draws a textured rectangle region of the multichannel signed distance
field texture at a given position, optionally modulated by a color. See
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} for more information and caveats about MSDF font rendering.

If `outline` is positive, each alpha channel value of pixel in region is
set to maximum value of true distance in the `outline` radius.

Value of the `pixel_range` should the same that was used during distance
field texture generation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_multiline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_multiline**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"},
width: `float<class_float>`{.interpreted-text role="ref"} = -1.0,
antialiased: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CanvasItem_method_draw_multiline>`{.interpreted-text
role="ref"}

Draws multiple disconnected lines with a uniform `width` and `color`.
Each line is defined by two consecutive points from `points` array, i.e.
i-th segment consists of `points[2 * i]`, `points[2 * i + 1]` endpoints.
When drawing large amounts of lines, this is faster than using
individual
`draw_line()<class_CanvasItem_method_draw_line>`{.interpreted-text
role="ref"} calls. To draw interconnected lines, use
`draw_polyline()<class_CanvasItem_method_draw_polyline>`{.interpreted-text
role="ref"} instead.

If `width` is negative, then two-point primitives will be drawn instead
of a four-point ones. This means that when the CanvasItem is scaled, the
lines will remain thin. If this behavior is not desired, then pass a
positive `width` like `1.0`.

\*\*Note:\*\* `antialiased` is only effective if `width` is greater than
`0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_multiline_colors}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_multiline_colors**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, width: `float<class_float>`{.interpreted-text role="ref"} =
-1.0, antialiased: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_CanvasItem_method_draw_multiline_colors>`{.interpreted-text
role="ref"}

Draws multiple disconnected lines with a uniform `width` and
segment-by-segment coloring. Each segment is defined by two consecutive
points from `points` array and a corresponding color from `colors`
array, i.e. i-th segment consists of `points[2 * i]`,
`points[2 * i + 1]` endpoints and has `colors[i]` color. When drawing
large amounts of lines, this is faster than using individual
`draw_line()<class_CanvasItem_method_draw_line>`{.interpreted-text
role="ref"} calls. To draw interconnected lines, use
`draw_polyline_colors()<class_CanvasItem_method_draw_polyline_colors>`{.interpreted-text
role="ref"} instead.

If `width` is negative, then two-point primitives will be drawn instead
of a four-point ones. This means that when the CanvasItem is scaled, the
lines will remain thin. If this behavior is not desired, then pass a
positive `width` like `1.0`.

\*\*Note:\*\* `antialiased` is only effective if `width` is greater than
`0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_multiline_string}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_multiline_string**(font: `Font<class_Font>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, text: `String<class_String>`{.interpreted-text role="ref"},
alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, max_lines: `int<class_int>`{.interpreted-text
role="ref"} = -1, modulate: `Color<class_Color>`{.interpreted-text
role="ref"} = Color(1, 1, 1, 1), brk_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] = 3, justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0, oversampling: `float<class_float>`{.interpreted-text role="ref"} =
0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_draw_multiline_string>`{.interpreted-text
role="ref"}

Breaks `text` into lines and draws it using the specified `font` at the
`pos` (top-left corner). The text will have its color multiplied by
`modulate`. If `width` is greater than or equal to 0, the text will be
clipped if it exceeds the specified width. If `oversampling` is greater
than zero, it is used as font oversampling factor, otherwise viewport
oversampling settings are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_multiline_string_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_multiline_string_outline**(font:
`Font<class_Font>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"}, alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, max_lines: `int<class_int>`{.interpreted-text
role="ref"} = -1, size: `int<class_int>`{.interpreted-text role="ref"} =
1, modulate: `Color<class_Color>`{.interpreted-text role="ref"} =
Color(1, 1, 1, 1), brk_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] = 3, justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0, oversampling: `float<class_float>`{.interpreted-text role="ref"} =
0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_draw_multiline_string_outline>`{.interpreted-text
role="ref"}

Breaks `text` to the lines and draws text outline using the specified
`font` at the `pos` (top-left corner). The text will have its color
multiplied by `modulate`. If `width` is greater than or equal to 0, the
text will be clipped if it exceeds the specified width. If
`oversampling` is greater than zero, it is used as font oversampling
factor, otherwise viewport oversampling settings are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_multimesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_multimesh**(multimesh:
`MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"}, texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_CanvasItem_method_draw_multimesh>`{.interpreted-text
role="ref"}

Draws a `MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"} in 2D
with the provided texture. See
`MultiMeshInstance2D<class_MultiMeshInstance2D>`{.interpreted-text
role="ref"} for related documentation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_polygon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_polygon**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, uvs:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} = PackedVector2Array(), texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} = null)
`🔗<class_CanvasItem_method_draw_polygon>`{.interpreted-text role="ref"}

Draws a solid polygon of any number of points, convex or concave. Unlike
`draw_colored_polygon()<class_CanvasItem_method_draw_colored_polygon>`{.interpreted-text
role="ref"}, each point\'s color can be changed individually. See also
`draw_polyline()<class_CanvasItem_method_draw_polyline>`{.interpreted-text
role="ref"} and
`draw_polyline_colors()<class_CanvasItem_method_draw_polyline_colors>`{.interpreted-text
role="ref"}. If you need more flexibility (such as being able to use
bones), use
`RenderingServer.canvas_item_add_triangle_array()<class_RenderingServer_method_canvas_item_add_triangle_array>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* If you frequently redraw the same polygon with a large
number of vertices, consider pre-calculating the triangulation with
`Geometry2D.triangulate_polygon()<class_Geometry2D_method_triangulate_polygon>`{.interpreted-text
role="ref"} and using
`draw_mesh()<class_CanvasItem_method_draw_mesh>`{.interpreted-text
role="ref"},
`draw_multimesh()<class_CanvasItem_method_draw_multimesh>`{.interpreted-text
role="ref"}, or
`RenderingServer.canvas_item_add_triangle_array()<class_RenderingServer_method_canvas_item_add_triangle_array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_polyline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_polyline**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"},
width: `float<class_float>`{.interpreted-text role="ref"} = -1.0,
antialiased: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CanvasItem_method_draw_polyline>`{.interpreted-text
role="ref"}

Draws interconnected line segments with a uniform `color` and `width`
and optional antialiasing (supported only for positive `width`). When
drawing large amounts of lines, this is faster than using individual
`draw_line()<class_CanvasItem_method_draw_line>`{.interpreted-text
role="ref"} calls. To draw disconnected lines, use
`draw_multiline()<class_CanvasItem_method_draw_multiline>`{.interpreted-text
role="ref"} instead. See also
`draw_polygon()<class_CanvasItem_method_draw_polygon>`{.interpreted-text
role="ref"}.

If `width` is negative, it will be ignored and the polyline will be
drawn using
`RenderingServer.PRIMITIVE_LINE_STRIP<class_RenderingServer_constant_PRIMITIVE_LINE_STRIP>`{.interpreted-text
role="ref"}. This means that when the CanvasItem is scaled, the polyline
will remain thin. If this behavior is not desired, then pass a positive
`width` like `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_polyline_colors}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_polyline_colors**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, width: `float<class_float>`{.interpreted-text role="ref"} =
-1.0, antialiased: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_CanvasItem_method_draw_polyline_colors>`{.interpreted-text
role="ref"}

Draws interconnected line segments with a uniform `width`,
point-by-point coloring, and optional antialiasing (supported only for
positive `width`). Colors assigned to line points match by index between
`points` and `colors`, i.e. each line segment is filled with a gradient
between the colors of the endpoints. When drawing large amounts of
lines, this is faster than using individual
`draw_line()<class_CanvasItem_method_draw_line>`{.interpreted-text
role="ref"} calls. To draw disconnected lines, use
`draw_multiline_colors()<class_CanvasItem_method_draw_multiline_colors>`{.interpreted-text
role="ref"} instead. See also
`draw_polygon()<class_CanvasItem_method_draw_polygon>`{.interpreted-text
role="ref"}.

If `width` is negative, it will be ignored and the polyline will be
drawn using
`RenderingServer.PRIMITIVE_LINE_STRIP<class_RenderingServer_constant_PRIMITIVE_LINE_STRIP>`{.interpreted-text
role="ref"}. This means that when the CanvasItem is scaled, the polyline
will remain thin. If this behavior is not desired, then pass a positive
`width` like `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_primitive}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_primitive**(points:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}, uvs:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"} = null)
`🔗<class_CanvasItem_method_draw_primitive>`{.interpreted-text
role="ref"}

Draws a custom primitive. 1 point for a point, 2 points for a line, 3
points for a triangle, and 4 points for a quad. If 0 points or more than
4 points are specified, nothing will be drawn and an error message will
be printed. See also
`draw_line()<class_CanvasItem_method_draw_line>`{.interpreted-text
role="ref"},
`draw_polyline()<class_CanvasItem_method_draw_polyline>`{.interpreted-text
role="ref"},
`draw_polygon()<class_CanvasItem_method_draw_polygon>`{.interpreted-text
role="ref"}, and
`draw_rect()<class_CanvasItem_method_draw_rect>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_rect**(rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"}, filled:
`bool<class_bool>`{.interpreted-text role="ref"} = true, width:
`float<class_float>`{.interpreted-text role="ref"} = -1.0, antialiased:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CanvasItem_method_draw_rect>`{.interpreted-text role="ref"}

Draws a rectangle. If `filled` is `true`, the rectangle will be filled
with the `color` specified. If `filled` is `false`, the rectangle will
be drawn as a stroke with the `color` and `width` specified. See also
`draw_texture_rect()<class_CanvasItem_method_draw_texture_rect>`{.interpreted-text
role="ref"}.

If `width` is negative, then two-point primitives will be drawn instead
of a four-point ones. This means that when the CanvasItem is scaled, the
lines will remain thin. If this behavior is not desired, then pass a
positive `width` like `1.0`.

If `antialiased` is `true`, half transparent \"feathers\" will be
attached to the boundary, making outlines smooth.

\*\*Note:\*\* `width` is only effective if `filled` is `false`.

\*\*Note:\*\* Unfilled rectangles drawn with a negative `width` may not
display perfectly. For example, corners may be missing or brighter due
to overlapping lines (for a translucent `color`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_set_transform**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, rotation:
`float<class_float>`{.interpreted-text role="ref"} = 0.0, scale:
`Vector2<class_Vector2>`{.interpreted-text role="ref"} = Vector2(1, 1))
`🔗<class_CanvasItem_method_draw_set_transform>`{.interpreted-text
role="ref"}

Sets a custom transform for drawing via components. Anything drawn
afterwards will be transformed by this.

\*\*Note:\*\*
`FontFile.oversampling<class_FontFile_property_oversampling>`{.interpreted-text
role="ref"} does *not* take `scale` into account. This means that
scaling up/down will cause bitmap fonts and rasterized (non-MSDF)
dynamic fonts to appear blurry or pixelated. To ensure text remains
crisp regardless of scale, you can enable MSDF font rendering by
enabling
`ProjectSettings.gui/theme/default_font_multichannel_signed_distance_field<class_ProjectSettings_property_gui/theme/default_font_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} (applies to the default project font only), or enabling
**Multichannel Signed Distance Field** in the import options of a
DynamicFont for custom fonts. On system fonts,
`SystemFont.multichannel_signed_distance_field<class_SystemFont_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} can be enabled in the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_set_transform_matrix}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_set_transform_matrix**(xform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_CanvasItem_method_draw_set_transform_matrix>`{.interpreted-text
role="ref"}

Sets a custom transform for drawing via matrix. Anything drawn
afterwards will be transformed by this.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_string}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_string**(font: `Font<class_Font>`{.interpreted-text role="ref"},
pos: `Vector2<class_Vector2>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"}, alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, modulate: `Color<class_Color>`{.interpreted-text
role="ref"} = Color(1, 1, 1, 1), justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0, oversampling: `float<class_float>`{.interpreted-text role="ref"} =
0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CanvasItem_method_draw_string>`{.interpreted-text
role="ref"}

Draws `text` using the specified `font` at the `pos` (bottom-left corner
using the baseline of the font). The text will have its color multiplied
by `modulate`. If `width` is greater than or equal to 0, the text will
be clipped if it exceeds the specified width. If `oversampling` is
greater than zero, it is used as font oversampling factor, otherwise
viewport oversampling settings are used.

\*\*Example:\*\* Draw \"Hello world\", using the project\'s default
font:

::::: tabs
::: code-tab
gdscript

\# If using this method in a script that redraws constantly, move the \#
[default_font]{.title-ref} declaration to a member variable assigned in
[\_ready()]{.title-ref} \# so the Control is only created once. var
default_font = ThemeDB.fallback_font var default_font_size =
ThemeDB.fallback_font_size draw_string(default_font, Vector2(64, 64),
\"Hello world\", HORIZONTAL_ALIGNMENT_LEFT, -1, default_font_size)
:::

::: code-tab
csharp

// If using this method in a script that redraws constantly, move the //
[default_font]{.title-ref} declaration to a member variable assigned in
[\_Ready()]{.title-ref} // so the Control is only created once. Font
defaultFont = ThemeDB.FallbackFont; int defaultFontSize =
ThemeDB.FallbackFontSize; DrawString(defaultFont, new Vector2(64, 64),
\"Hello world\", HORIZONTAL_ALIGNMENT_LEFT, -1, defaultFontSize);
:::
:::::

See also
`Font.draw_string()<class_Font_method_draw_string>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_string_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_string_outline**(font: `Font<class_Font>`{.interpreted-text
role="ref"}, pos: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, text: `String<class_String>`{.interpreted-text role="ref"},
alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 0, width: `float<class_float>`{.interpreted-text
role="ref"} = -1, font_size: `int<class_int>`{.interpreted-text
role="ref"} = 16, size: `int<class_int>`{.interpreted-text role="ref"} =
1, modulate: `Color<class_Color>`{.interpreted-text role="ref"} =
Color(1, 1, 1, 1), justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0, oversampling: `float<class_float>`{.interpreted-text role="ref"} =
0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_draw_string_outline>`{.interpreted-text
role="ref"}

Draws `text` outline using the specified `font` at the `pos`
(bottom-left corner using the baseline of the font). The text will have
its color multiplied by `modulate`. If `width` is greater than or equal
to 0, the text will be clipped if it exceeds the specified width. If
`oversampling` is greater than zero, it is used as font oversampling
factor, otherwise viewport oversampling settings are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_style_box}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_style_box**(style_box:
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})
`🔗<class_CanvasItem_method_draw_style_box>`{.interpreted-text
role="ref"}

Draws a styled rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_texture**(texture: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, modulate: `Color<class_Color>`{.interpreted-text
role="ref"} = Color(1, 1, 1, 1))
`🔗<class_CanvasItem_method_draw_texture>`{.interpreted-text role="ref"}

Draws a texture at a given position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_texture_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_texture_rect**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, tile:
`bool<class_bool>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
transpose: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CanvasItem_method_draw_texture_rect>`{.interpreted-text
role="ref"}

Draws a textured rectangle at a given position, optionally modulated by
a color. If `transpose` is `true`, the texture will have its X and Y
coordinates swapped. See also
`draw_rect()<class_CanvasItem_method_draw_rect>`{.interpreted-text
role="ref"} and
`draw_texture_rect_region()<class_CanvasItem_method_draw_texture_rect_region>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_draw_texture_rect_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_texture_rect_region**(texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, src_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"}, modulate:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
transpose: `bool<class_bool>`{.interpreted-text role="ref"} = false,
clip_uv: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_CanvasItem_method_draw_texture_rect_region>`{.interpreted-text
role="ref"}

Draws a textured rectangle from a texture\'s region (specified by
`src_rect`) at a given position, optionally modulated by a color. If
`transpose` is `true`, the texture will have its X and Y coordinates
swapped. See also
`draw_texture_rect()<class_CanvasItem_method_draw_texture_rect>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_force_update_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_update_transform**()
`🔗<class_CanvasItem_method_force_update_transform>`{.interpreted-text
role="ref"}

Forces the node\'s transform to update. Fails if the node is not inside
the tree. See also
`get_transform()<class_CanvasItem_method_get_transform>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For performance reasons, transform changes are usually
accumulated and applied *once* at the end of the frame. The update
propagates through **CanvasItem** children, as well. Therefore, use this
method only when you need an up-to-date transform (such as during
physics operations).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_canvas}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_canvas**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CanvasItem_method_get_canvas>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the
`World2D<class_World2D>`{.interpreted-text role="ref"} canvas where this
node is registered to, used by the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_canvas_item}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_canvas_item**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_canvas_item>`{.interpreted-text
role="ref"}

Returns the internal canvas item `RID<class_RID>`{.interpreted-text
role="ref"} used by the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
for this node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_canvas_layer_node}
::: rst-class
classref-method
:::
::::

`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"}
**get_canvas_layer_node**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_canvas_layer_node>`{.interpreted-text
role="ref"}

Returns the `CanvasLayer<class_CanvasLayer>`{.interpreted-text
role="ref"} that contains this node, or `null` if the node is not in any
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_canvas_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_canvas_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_canvas_transform>`{.interpreted-text
role="ref"}

Returns the transform of this node, converted from its registered
canvas\'s coordinate system to its viewport\'s coordinate system. See
also
`Node.get_viewport()<class_Node_method_get_viewport>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_global_mouse_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_global_mouse_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_global_mouse_position>`{.interpreted-text
role="ref"}

Returns mouse cursor\'s global position relative to the
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"} that
contains this node.

\*\*Note:\*\* For screen-space coordinates (e.g. when using a
non-embedded `Popup<class_Popup>`{.interpreted-text role="ref"}), you
can use
`DisplayServer.mouse_get_position()<class_DisplayServer_method_mouse_get_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_global_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_global_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_global_transform>`{.interpreted-text
role="ref"}

Returns the global transform matrix of this item, i.e. the combined
transform up to the topmost **CanvasItem** node. The topmost item is a
**CanvasItem** that either has no parent, has non-**CanvasItem** parent
or it has
`top_level<class_CanvasItem_property_top_level>`{.interpreted-text
role="ref"} enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_global_transform_with_canvas}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_global_transform_with_canvas**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_global_transform_with_canvas>`{.interpreted-text
role="ref"}

Returns the transform from the local coordinate system of this
**CanvasItem** to the `Viewport<class_Viewport>`{.interpreted-text
role="ref"}s coordinate system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_instance_shader_parameter}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_instance_shader_parameter**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_instance_shader_parameter>`{.interpreted-text
role="ref"}

Get the value of a shader parameter as set on this instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_local_mouse_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_local_mouse_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_local_mouse_position>`{.interpreted-text
role="ref"}

Returns the mouse\'s position in this **CanvasItem** using the local
coordinate system of this **CanvasItem**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_screen_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_screen_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_screen_transform>`{.interpreted-text
role="ref"}

Returns the transform of this **CanvasItem** in global screen
coordinates (i.e. taking window position into account). Mostly useful
for editor plugins.

Equals to
`get_global_transform()<class_CanvasItem_method_get_global_transform>`{.interpreted-text
role="ref"} if the window is embedded (see
`Viewport.gui_embed_subwindows<class_Viewport_property_gui_embed_subwindows>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_transform>`{.interpreted-text
role="ref"}

Returns the transform matrix of this **CanvasItem**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_viewport_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_viewport_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_viewport_rect>`{.interpreted-text
role="ref"}

Returns this node\'s viewport boundaries as a
`Rect2<class_Rect2>`{.interpreted-text role="ref"}. See also
`Node.get_viewport()<class_Node_method_get_viewport>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_viewport_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_viewport_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_viewport_transform>`{.interpreted-text
role="ref"}

Returns the transform of this node, converted from its registered
canvas\'s coordinate system to its viewport embedder\'s coordinate
system. See also
`Viewport.get_final_transform()<class_Viewport_method_get_final_transform>`{.interpreted-text
role="ref"} and
`Node.get_viewport()<class_Node_method_get_viewport>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_visibility_layer_bit}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_visibility_layer_bit**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_visibility_layer_bit>`{.interpreted-text
role="ref"}

Returns `true` if the layer at the given index is set in
`visibility_layer<class_CanvasItem_property_visibility_layer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_get_world_2d}
::: rst-class
classref-method
:::
::::

`World2D<class_World2D>`{.interpreted-text role="ref"}
**get_world_2d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_get_world_2d>`{.interpreted-text role="ref"}

Returns the `World2D<class_World2D>`{.interpreted-text role="ref"} this
node is registered to.

Usually, this is the same as this node\'s viewport (see
`Node.get_viewport()<class_Node_method_get_viewport>`{.interpreted-text
role="ref"} and
`Viewport.find_world_2d()<class_Viewport_method_find_world_2d>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_hide}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **hide**()
`🔗<class_CanvasItem_method_hide>`{.interpreted-text role="ref"}

Hide the **CanvasItem** if it\'s currently visible. This is equivalent
to setting
`visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_is_local_transform_notification_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_local_transform_notification_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_is_local_transform_notification_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the node receives
`NOTIFICATION_LOCAL_TRANSFORM_CHANGED<class_CanvasItem_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} whenever its local transform changes. This is enabled with
`set_notify_local_transform()<class_CanvasItem_method_set_notify_local_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_is_transform_notification_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_transform_notification_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_is_transform_notification_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the node receives
`NOTIFICATION_TRANSFORM_CHANGED<class_CanvasItem_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} whenever its global transform changes. This is enabled with
`set_notify_transform()<class_CanvasItem_method_set_notify_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_is_visible_in_tree}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_visible_in_tree**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_is_visible_in_tree>`{.interpreted-text
role="ref"}

Returns `true` if the node is present in the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}, its
`visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property is `true` and all its ancestors are also visible.
If any ancestor is hidden, this node will not be visible in the scene
tree, and is therefore not drawn (see
`_draw()<class_CanvasItem_private_method__draw>`{.interpreted-text
role="ref"}).

Visibility is checked only in parent nodes that inherit from
**CanvasItem**, `CanvasLayer<class_CanvasLayer>`{.interpreted-text
role="ref"}, and `Window<class_Window>`{.interpreted-text role="ref"}.
If the parent is of any other type (such as
`Node<class_Node>`{.interpreted-text role="ref"},
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"},
or `Node3D<class_Node3D>`{.interpreted-text role="ref"}), it is assumed
to be visible.

\*\*Note:\*\* This method does not take
`visibility_layer<class_CanvasItem_property_visibility_layer>`{.interpreted-text
role="ref"} into account, so even if this method returns `true`, the
node might end up not being rendered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_make_canvas_position_local}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**make_canvas_position_local**(viewport_point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_make_canvas_position_local>`{.interpreted-text
role="ref"}

Transforms `viewport_point` from the viewport\'s coordinates to this
node\'s local coordinates.

For the opposite operation, use
`get_global_transform_with_canvas()<class_CanvasItem_method_get_global_transform_with_canvas>`{.interpreted-text
role="ref"}.

    var viewport_point = get_global_transform_with_canvas() * local_point

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_make_input_local}
::: rst-class
classref-method
:::
::::

`InputEvent<class_InputEvent>`{.interpreted-text role="ref"}
**make_input_local**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CanvasItem_method_make_input_local>`{.interpreted-text
role="ref"}

Returns a copy of the given `event` with its coordinates converted from
global space to this **CanvasItem**\'s local space. If not possible,
returns the same `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} unchanged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_move_to_front}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_to_front**()
`🔗<class_CanvasItem_method_move_to_front>`{.interpreted-text
role="ref"}

Moves this node below its siblings, usually causing the node to draw on
top of its siblings. Does nothing if this node does not have a parent.
See also
`Node.move_child()<class_Node_method_move_child>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_queue_redraw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**queue_redraw**()
`🔗<class_CanvasItem_method_queue_redraw>`{.interpreted-text role="ref"}

Queues the **CanvasItem** to redraw. During idle time, if **CanvasItem**
is visible,
`NOTIFICATION_DRAW<class_CanvasItem_constant_NOTIFICATION_DRAW>`{.interpreted-text
role="ref"} is sent and
`_draw()<class_CanvasItem_private_method__draw>`{.interpreted-text
role="ref"} is called. This only occurs **once** per frame, even if this
method has been called multiple times.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_set_instance_shader_parameter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_instance_shader_parameter**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_CanvasItem_method_set_instance_shader_parameter>`{.interpreted-text
role="ref"}

Set the value of a shader uniform for this instance only ([per-instance
uniform](../tutorials/shaders/shader_reference/shading_language.html#per-instance-uniforms)).
See also
`ShaderMaterial.set_shader_parameter()<class_ShaderMaterial_method_set_shader_parameter>`{.interpreted-text
role="ref"} to assign a uniform on all instances using the same
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}.

\*\*Note:\*\* For a shader uniform to be assignable on a per-instance
basis, it *must* be defined with `instance uniform ...` rather than
`uniform ...` in the shader code.

\*\*Note:\*\* `name` is case-sensitive and must match the name of the
uniform in the code exactly (not the capitalized name in the inspector).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_set_notify_local_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_notify_local_transform**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CanvasItem_method_set_notify_local_transform>`{.interpreted-text
role="ref"}

If `true`, the node will receive
`NOTIFICATION_LOCAL_TRANSFORM_CHANGED<class_CanvasItem_constant_NOTIFICATION_LOCAL_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} whenever its local transform changes.

\*\*Note:\*\* Many canvas items such as
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} or
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text role="ref"}
automatically enable this in order to function correctly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_set_notify_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_notify_transform**(enable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_CanvasItem_method_set_notify_transform>`{.interpreted-text
role="ref"}

If `true`, the node will receive
`NOTIFICATION_TRANSFORM_CHANGED<class_CanvasItem_constant_NOTIFICATION_TRANSFORM_CHANGED>`{.interpreted-text
role="ref"} whenever global transform changes.

\*\*Note:\*\* Many canvas items such as
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"} or
`Light2D<class_Light2D>`{.interpreted-text role="ref"} automatically
enable this in order to function correctly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_set_visibility_layer_bit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_visibility_layer_bit**(layer: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CanvasItem_method_set_visibility_layer_bit>`{.interpreted-text
role="ref"}

Set/clear individual bits on the rendering visibility layer. This
simplifies editing this **CanvasItem**\'s visibility layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasItem_method_show}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **show**()
`🔗<class_CanvasItem_method_show>`{.interpreted-text role="ref"}

Show the **CanvasItem** if it\'s currently hidden. This is equivalent to
setting `visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} to `true`.

\*\*Note:\*\* For controls that inherit
`Popup<class_Popup>`{.interpreted-text role="ref"}, the correct way to
make them visible is to call one of the multiple `popup*()` functions
instead.
