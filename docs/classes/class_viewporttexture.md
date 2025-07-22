github_url
:   hide

# ViewportTexture {#class_ViewportTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Provides the content of a `Viewport<class_Viewport>`{.interpreted-text
role="ref"} as a dynamic texture.

::: rst-class
classref-introduction-group
:::

## Description

A **ViewportTexture** provides the content of a
`Viewport<class_Viewport>`{.interpreted-text role="ref"} as a dynamic
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}. This can be
used to combine the rendering of
`Control<class_Control>`{.interpreted-text role="ref"},
`Node2D<class_Node2D>`{.interpreted-text role="ref"} and
`Node3D<class_Node3D>`{.interpreted-text role="ref"} nodes. For example,
you can use this texture to display a 3D scene inside a
`TextureRect<class_TextureRect>`{.interpreted-text role="ref"}, or a 2D
overlay in a `Sprite3D<class_Sprite3D>`{.interpreted-text role="ref"}.

To get a **ViewportTexture** in code, use the
`Viewport.get_texture()<class_Viewport_method_get_texture>`{.interpreted-text
role="ref"} method on the target viewport.

\*\*Note:\*\* A **ViewportTexture** is always local to its scene (see
`Resource.resource_local_to_scene<class_Resource_property_resource_local_to_scene>`{.interpreted-text
role="ref"}). If the scene root is not ready, it may return incorrect
data (see `Node.ready<class_Node_signal_ready>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* Instantiating scenes containing a high-resolution
**ViewportTexture** may cause noticeable stutter.

\*\*Note:\*\* When using a `Viewport<class_Viewport>`{.interpreted-text
role="ref"} with
`Viewport.use_hdr_2d<class_Viewport_property_use_hdr_2d>`{.interpreted-text
role="ref"} set to `true`, the returned texture will be an HDR image
encoded in linear space. This may look darker than normal when displayed
directly on screen. To convert to gamma space, you can do the following:

    img.convert(Image.FORMAT_RGBA8)
    imb.linear_to_srgb()

\*\*Note:\*\* Some nodes such as `Decal<class_Decal>`{.interpreted-text
role="ref"}, `Light3D<class_Light3D>`{.interpreted-text role="ref"}, and
`PointLight2D<class_PointLight2D>`{.interpreted-text role="ref"} do not
support using **ViewportTexture** directly. To use texture data from a
**ViewportTexture** in these nodes, you need to create an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"} by
calling
`Texture2D.get_image()<class_Texture2D_method_get_image>`{.interpreted-text
role="ref"} on the **ViewportTexture** and passing the result to
`ImageTexture.create_from_image()<class_ImageTexture_method_create_from_image>`{.interpreted-text
role="ref"}. This conversion is a slow operation, so it should not be
performed every frame.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [GUI in 3D Viewport
  Demo](https://godotengine.org/asset-library/asset/2807)
- [3D in 2D Viewport
  Demo](https://godotengine.org/asset-library/asset/2804)
- [2D in 3D Viewport
  Demo](https://godotengine.org/asset-library/asset/2803)
- [3D Resolution Scaling
  Demo](https://godotengine.org/asset-library/asset/2805)

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

:::: {#class_ViewportTexture_property_viewport_path}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**viewport_path** = `NodePath("")`
`🔗<class_ViewportTexture_property_viewport_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_viewport_path_in_scene**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_viewport_path_in_scene**()

The path to the `Viewport<class_Viewport>`{.interpreted-text role="ref"}
node to display. This is relative to the local scene root (see
`Resource.get_local_scene()<class_Resource_method_get_local_scene>`{.interpreted-text
role="ref"}), **not** to the nodes that use this texture.

\*\*Note:\*\* In the editor, this path is automatically updated when the
target viewport or one of its ancestors is renamed or moved. At runtime,
this path may not automatically update if the scene root cannot be
found.
