# Using Viewports {#doc_viewports}

## Introduction

Think of a `Viewport <class_Viewport>`{.interpreted-text role="ref"} as
a screen onto which the game is projected. In order to see the game, we
need to have a surface on which to draw it. That surface is the Root
Viewport.

![image](img/subviewportnode.webp)

`SubViewports <class_SubViewport>`{.interpreted-text role="ref"} are a
kind of Viewport that can be added to the scene so that there are
multiple surfaces to draw on. When we are drawing to a SubViewport, we
call it a render target. We can access the contents of a render target
by accessing its corresponding
`texture <class_Viewport_method_get_texture>`{.interpreted-text
role="ref"}. By using a SubViewport as render target, we can either
render multiple scenes simultaneously or we can render to a
`ViewportTexture <class_ViewportTexture>`{.interpreted-text role="ref"}
which is applied to an object in the scene, for example a dynamic
skybox.

`SubViewports <class_SubViewport>`{.interpreted-text role="ref"} have a
variety of use cases, including:

- Rendering 3D objects within a 2D game
- Rendering 2D elements in a 3D game
- Rendering dynamic textures
- Generating procedural textures at runtime
- Rendering multiple cameras in the same scene

What all these use cases have in common is that you are given the
ability to draw objects to a texture as if it were another screen and
can then choose what to do with the resulting texture.

Another kind of Viewports in Godot are
`Windows <class_Window>`{.interpreted-text role="ref"}. They allow their
content to be projected onto a window. While the Root Viewport is a
Window, they are less flexible. If you want to use the texture of a
Viewport, you\'ll be working with
`SubViewports <class_SubViewport>`{.interpreted-text role="ref"} most of
the time.

## Input

`Viewports <class_Viewport>`{.interpreted-text role="ref"} are also
responsible for delivering properly adjusted and scaled input events to
their children nodes. By default
`SubViewports <class_SubViewport>`{.interpreted-text role="ref"} don\'t
automatically receive input, unless they receive it from their direct
`SubViewportContainer <class_SubViewportContainer>`{.interpreted-text
role="ref"} parent node. In this case, input can be disabled with the
`Disable Input <class_Viewport_property_gui_disable_input>`{.interpreted-text
role="ref"} property.

![image](img/input.webp)

For more information on how Godot handles input, please read the
`Input Event Tutorial <doc_inputevent>`{.interpreted-text role="ref"}.

## Listener

Godot supports 3D sound (in both 2D and 3D nodes). More on this can be
found in the
`Audio Streams Tutorial <doc_audio_streams>`{.interpreted-text
role="ref"}. For this type of sound to be audible, the
`Viewport <class_Viewport>`{.interpreted-text role="ref"} needs to be
enabled as a listener (for 2D or 3D). If you are using a
`SubViewport <class_SubViewport>`{.interpreted-text role="ref"} to
display your `World3D <class_World3D>`{.interpreted-text role="ref"} or
`World2D <class_World2D>`{.interpreted-text role="ref"}, don\'t forget
to enable this!

## Cameras (2D & 3D)

When using a `Camera3D <class_Camera3D>`{.interpreted-text role="ref"}
or `Camera2D <class_Camera2D>`{.interpreted-text role="ref"}, it will
always display on the closest parent
`Viewport <class_Viewport>`{.interpreted-text role="ref"} (going towards
the root). For example, in the following hierarchy:

![image](img/cameras.webp)

`CameraA` will display on the Root
`Viewport <class_Viewport>`{.interpreted-text role="ref"} and it will
draw `MeshA`. `CameraB` will be captured by the
`SubViewport <class_SubViewport>`{.interpreted-text role="ref"} along
with `MeshB`. Even though `MeshB` is in the scene hierarchy, it will
still not be drawn to the Root Viewport. Similarly, `MeshA` will not be
visible from the SubViewport because SubViewports only capture nodes
below them in the hierarchy.

There can only be one active camera per
`Viewport <class_Viewport>`{.interpreted-text role="ref"}, so if there
is more than one, make sure that the desired one has the
`current <class_Camera3D_property_current>`{.interpreted-text
role="ref"} property set, or make it the current camera by calling:

:::: tabs
.. code-tab:: gdscript GDScript

camera.make_current()

::: code-tab
csharp
:::

camera.MakeCurrent();
::::

By default, cameras will render all objects in their world. In 3D,
cameras can use their
`cull_mask <class_Camera3D_property_cull_mask>`{.interpreted-text
role="ref"} property combined with the
`VisualInstance3D's <class_VisualInstance3D>`{.interpreted-text
role="ref"}
`layer <class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"} property to restrict which objects are rendered.

## Scale & stretching

`SubViewports <class_SubViewport>`{.interpreted-text role="ref"} have a
`size<class_SubViewport_property_size>`{.interpreted-text role="ref"}
property, which represents the size of the SubViewport in pixels. For
SubViewports which are children of
`SubViewportContainers <class_SubViewportContainer>`{.interpreted-text
role="ref"}, these values are overridden, but for all others, this sets
their resolution.

It is also possible to scale the 2D content and make the
`SubViewport <class_SubViewport>`{.interpreted-text role="ref"}
resolution different from the one specified in size, by calling:

:::: tabs
.. code-tab:: gdscript GDScript

sub_viewport.set_size_2d_override(Vector2i(width, height)) \# Custom
size for 2D. sub_viewport.set_size_2d_override_stretch(true) \# Enable
stretch for custom size.

::: code-tab
csharp
:::

subViewport.Size2DOverride = new Vector2I(width, height); // Custom size
for 2D. subViewport.Size2DOverrideStretch = true; // Enable stretch for
custom size.
::::

For information on scaling and stretching with the Root Viewport visit
the
`Multiple Resolutions Tutorial <doc_multiple_resolutions>`{.interpreted-text
role="ref"}

## Worlds

For 3D, a `Viewport <class_Viewport>`{.interpreted-text role="ref"} will
contain a `World3D <class_World3D>`{.interpreted-text role="ref"}. This
is basically the universe that links physics and rendering together.
Node3D-based nodes will register using the World3D of the closest
Viewport. By default, newly created Viewports do not contain a World3D
but use the same as their parent Viewport. The Root Viewport always
contains a World3D, which is the one objects are rendered to by default.

A `World3D <class_World3D>`{.interpreted-text role="ref"} can be set in
a `Viewport <class_Viewport>`{.interpreted-text role="ref"} using the
`World 3D<class_Viewport_property_world_3d>`{.interpreted-text
role="ref"} property, that will separate all children nodes of this
`Viewport <class_Viewport>`{.interpreted-text role="ref"} and will
prevent them from interacting with the parent Viewport\'s World3D. This
is especially useful in scenarios where, for example, you might want to
show a separate character in 3D imposed over the game (like in
StarCraft).

As a helper for situations where you want to create
`Viewports <class_Viewport>`{.interpreted-text role="ref"} that display
single objects and don\'t want to create a
`World3D <class_World3D>`{.interpreted-text role="ref"}, Viewport has
the option to use its
`Own World3D <class_Viewport_property_own_world_3d>`{.interpreted-text
role="ref"}. This is useful when you want to instance 3D characters or
objects in `World2D <class_World2D>`{.interpreted-text role="ref"}.

For 2D, each `Viewport <class_Viewport>`{.interpreted-text role="ref"}
always contains its own `World2D <class_World2D>`{.interpreted-text
role="ref"}. This suffices in most cases, but in case sharing them may
be desired, it is possible to do so by setting
`world_2d<class_Viewport_property_world_2d>`{.interpreted-text
role="ref"} on the Viewport through code.

For an example of how this works, see the demo projects [3D in
2D](https://github.com/godotengine/godot-demo-projects/tree/master/viewport/3d_in_2d)
and [2D in
3D](https://github.com/godotengine/godot-demo-projects/tree/master/viewport/2d_in_3d)
respectively.

## Capture

It is possible to query a capture of the
`Viewport <class_Viewport>`{.interpreted-text role="ref"} contents. For
the Root Viewport, this is effectively a screen capture. This is done
with the following code:

:::: tabs
.. code-tab:: gdscript GDScript

\# Retrieve the captured Image using get_image(). var img =
get_viewport().get_texture().get_image() \# Convert Image to
ImageTexture. var tex = ImageTexture.create_from_image(img) \# Set
sprite texture. sprite.texture = tex

::: code-tab
csharp

// Retrieve the captured Image using get_image(). var img =
GetViewport().GetTexture().GetImage(); // Convert Image to ImageTexture.
var tex = ImageTexture.CreateFromImage(img); // Set sprite texture.
sprite.Texture = tex;
:::
::::

But if you use this in `_ready()` or from the first frame of the
`Viewport's <class_Viewport>`{.interpreted-text role="ref"}
initialization, you will get an empty texture because there is nothing
to get as texture. You can deal with it using (for example):

:::: tabs
.. code-tab:: gdscript GDScript

\# Wait until the frame has finished before getting the texture. await
RenderingServer.frame_post_draw \# You can get the image after this.

::: code-tab
csharp

// Wait until the frame has finished before getting the texture. await
RenderingServer.Singleton.ToSignal(RenderingServer.SignalName.FramePostDraw);
// You can get the image after this.
:::
::::

## Viewport Container

If the `SubViewport <class_SubViewport>`{.interpreted-text role="ref"}
is a child of a
`SubViewportContainer <class_SubViewportContainer>`{.interpreted-text
role="ref"}, it will become active and display anything it has inside.
The layout looks like this:

![image](img/container.webp)

The `SubViewport <class_SubViewport>`{.interpreted-text role="ref"} will
cover the area of its parent
`SubViewportContainer <class_SubViewportContainer>`{.interpreted-text
role="ref"} completely if
`Stretch<class_SubViewportContainer_property_stretch>`{.interpreted-text
role="ref"} is set to `true` in the SubViewportContainer.

:::: note
::: title
Note
:::

The size of the
`SubViewportContainer <class_SubViewportContainer>`{.interpreted-text
role="ref"} cannot be smaller than the size of the
`SubViewport <class_SubViewport>`{.interpreted-text role="ref"}.
::::

## Rendering

Due to the fact that the `Viewport <class_Viewport>`{.interpreted-text
role="ref"} is an entryway into another rendering surface, it exposes a
few rendering properties that can be different from the project
settings. You can choose to use a different level of
`MSAA <class_Viewport_property_msaa_2d>`{.interpreted-text role="ref"}
for each Viewport. The default behavior is `Disabled`.

If you know that the `Viewport <class_Viewport>`{.interpreted-text
role="ref"} is only going to be used for 2D, you can
`Disable 3D<class_Viewport_property_disable_3d>`{.interpreted-text
role="ref"}. Godot will then restrict how the Viewport is drawn.
Disabling 3D is slightly faster and uses less memory compared to enabled
3D. It\'s a good idea to disable 3D if your viewport doesn\'t render
anything in 3D.

:::: note
::: title
Note
:::

If you need to render 3D shadows in the viewport, make sure to set the
viewport\'s
`positional_shadow_atlas_size<class_Viewport_property_positional_shadow_atlas_size>`{.interpreted-text
role="ref"} property to a value higher than `0`. Otherwise, shadows
won\'t be rendered. By default, the equivalent project setting is set to
`4096` on desktop platforms and `2048` on mobile platforms.
::::

Godot also provides a way of customizing how everything is drawn inside
`Viewports <class_Viewport>`{.interpreted-text role="ref"} using
`Debug Draw<class_Viewport_property_debug_draw>`{.interpreted-text
role="ref"}. Debug Draw allows you to specify a mode which determines
how the Viewport will display things drawn inside it. Debug Draw is
`Disabled` by default. Some other options are `Unshaded`, `Overdraw`,
and `Wireframe`. For a full list, refer to the
`Viewport Documentation<class_Viewport_property_debug_draw>`{.interpreted-text
role="ref"}.

- **Debug Draw = Disabled** (default): The scene is drawn normally.

> ![image](img/default_scene.webp)

- **Debug Draw = Unshaded**: Unshaded draws the scene without using
  lighting information so all the objects appear flatly colored in their
  albedo color.

> ![image](img/unshaded.webp)

- **Debug Draw = Overdraw**: Overdraw draws the meshes semi-transparent
  with an additive blend so you can see how the meshes overlap.

> ![image](img/overdraw.webp)

- **Debug Draw = Wireframe**: Wireframe draws the scene using only the
  edges of triangles in the meshes.

> ![image](img/wireframe.webp)

:::: note
::: title
Note
:::

Debug Draw modes are currently **not** supported when using the
Compatibility rendering method. They will appear as regular draw modes.
::::

## Render target

When rendering to a `SubViewport <class_SubViewport>`{.interpreted-text
role="ref"}, whatever is inside will not be visible in the scene editor.
To display the contents, you have to draw the SubViewport\'s
`ViewportTexture <class_ViewportTexture>`{.interpreted-text role="ref"}
somewhere. This can be requested via code using (for example):

:::: tabs
.. code-tab:: gdscript GDScript

\# This gives us the ViewportTexture. var tex = viewport.get_texture()
sprite.texture = tex

::: code-tab
csharp
:::

// This gives us the ViewportTexture. var tex = viewport.GetTexture();
sprite.Texture = tex;
::::

Or it can be assigned in the editor by selecting \"New ViewportTexture\"

![image](img/texturemenu.webp)

and then selecting the `Viewport <class_Viewport>`{.interpreted-text
role="ref"} you want to use.

![image](img/texturepath.webp)

Every frame, the `Viewport's <class_Viewport>`{.interpreted-text
role="ref"} texture is cleared away with the default clear color (or a
transparent color if
`Transparent BG<class_Viewport_property_transparent_bg>`{.interpreted-text
role="ref"} is set to `true`). This can be changed by setting
`Clear Mode<class_SubViewport_property_render_target_clear_mode>`{.interpreted-text
role="ref"} to `Never` or `Next Frame`. As the name implies, Never means
the texture will never be cleared, while next frame will clear the
texture on the next frame and then set itself to Never.

By default, re-rendering of the
`SubViewport <class_SubViewport>`{.interpreted-text role="ref"} happens
when its `ViewportTexture <class_ViewportTexture>`{.interpreted-text
role="ref"} has been drawn in a frame. If visible, it will be rendered,
otherwise, it will not. This behavior can be changed by setting
`Update Mode<class_SubViewport_property_render_target_update_mode>`{.interpreted-text
role="ref"} to `Never`, `Once`, `Always`, or `When Parent Visible`.
Never and Always will never or always re-render respectively. Once will
re-render the next frame and change to Never afterwards. This can be
used to manually update the Viewport. This flexibility allows users to
render an image once and then use the texture without incurring the cost
of rendering every frame.

:::: note
::: title
Note
:::

Make sure to check the Viewport demos. They are available in the
viewport folder of the demos archive, or at
<https://github.com/godotengine/godot-demo-projects/tree/master/viewport>.
::::
