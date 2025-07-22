github_url
:   hide

# SubViewport {#class_SubViewport}

**Inherits:** `Viewport<class_Viewport>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An interface to a game world that doesn\'t create a window or draw to
the screen directly.

::: rst-class
classref-introduction-group
:::

## Description

**SubViewport** Isolates a rectangular region of a scene to be displayed
independently. This can be used, for example, to display UI in 3D space.

\*\*Note:\*\* **SubViewport** is a
`Viewport<class_Viewport>`{.interpreted-text role="ref"} that isn\'t a
`Window<class_Window>`{.interpreted-text role="ref"}, i.e. it doesn\'t
draw anything by itself. To display anything, **SubViewport** must have
a non-zero size and be either put inside a
`SubViewportContainer<class_SubViewportContainer>`{.interpreted-text
role="ref"} or assigned to a
`ViewportTexture<class_ViewportTexture>`{.interpreted-text role="ref"}.

\*\*Note:\*\* `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}s are not passed to a standalone **SubViewport** by default.
To ensure `InputEvent<class_InputEvent>`{.interpreted-text role="ref"}
propagation, a **SubViewport** can be placed inside of a
`SubViewportContainer<class_SubViewportContainer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Viewports <../tutorials/rendering/viewports>`{.interpreted-text
  role="doc"}
- `Viewport and canvas transforms <../tutorials/2d/2d_transforms>`{.interpreted-text
  role="doc"}
- [GUI in 3D Viewport
  Demo](https://godotengine.org/asset-library/asset/2807)
- [3D in 2D Viewport
  Demo](https://godotengine.org/asset-library/asset/2804)
- [2D in 3D Viewport
  Demo](https://godotengine.org/asset-library/asset/2803)
- [Screen Capture
  Demo](https://godotengine.org/asset-library/asset/2808)
- [Dynamic Split Screen
  Demo](https://godotengine.org/asset-library/asset/2806)
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

## Enumerations

:::: {#enum_SubViewport_ClearMode}
::: rst-class
classref-enumeration
:::
::::

enum **ClearMode**: `🔗<enum_SubViewport_ClearMode>`{.interpreted-text
role="ref"}

:::: {#class_SubViewport_constant_CLEAR_MODE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`ClearMode<enum_SubViewport_ClearMode>`{.interpreted-text role="ref"}
**CLEAR_MODE_ALWAYS** = `0`

Always clear the render target before drawing.

:::: {#class_SubViewport_constant_CLEAR_MODE_NEVER}
::: rst-class
classref-enumeration-constant
:::
::::

`ClearMode<enum_SubViewport_ClearMode>`{.interpreted-text role="ref"}
**CLEAR_MODE_NEVER** = `1`

Never clear the render target.

:::: {#class_SubViewport_constant_CLEAR_MODE_ONCE}
::: rst-class
classref-enumeration-constant
:::
::::

`ClearMode<enum_SubViewport_ClearMode>`{.interpreted-text role="ref"}
**CLEAR_MODE_ONCE** = `2`

Clear the render target on the next frame, then switch to
`CLEAR_MODE_NEVER<class_SubViewport_constant_CLEAR_MODE_NEVER>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_SubViewport_UpdateMode}
::: rst-class
classref-enumeration
:::
::::

enum **UpdateMode**: `🔗<enum_SubViewport_UpdateMode>`{.interpreted-text
role="ref"}

:::: {#class_SubViewport_constant_UPDATE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_SubViewport_UpdateMode>`{.interpreted-text role="ref"}
**UPDATE_DISABLED** = `0`

Do not update the render target.

:::: {#class_SubViewport_constant_UPDATE_ONCE}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_SubViewport_UpdateMode>`{.interpreted-text role="ref"}
**UPDATE_ONCE** = `1`

Update the render target once, then switch to
`UPDATE_DISABLED<class_SubViewport_constant_UPDATE_DISABLED>`{.interpreted-text
role="ref"}.

:::: {#class_SubViewport_constant_UPDATE_WHEN_VISIBLE}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_SubViewport_UpdateMode>`{.interpreted-text role="ref"}
**UPDATE_WHEN_VISIBLE** = `2`

Update the render target only when it is visible. This is the default
value.

:::: {#class_SubViewport_constant_UPDATE_WHEN_PARENT_VISIBLE}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_SubViewport_UpdateMode>`{.interpreted-text role="ref"}
**UPDATE_WHEN_PARENT_VISIBLE** = `3`

Update the render target only when its parent is visible.

:::: {#class_SubViewport_constant_UPDATE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_SubViewport_UpdateMode>`{.interpreted-text role="ref"}
**UPDATE_ALWAYS** = `4`

Always update the render target.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SubViewport_property_render_target_clear_mode}
::: rst-class
classref-property
:::
::::

`ClearMode<enum_SubViewport_ClearMode>`{.interpreted-text role="ref"}
**render_target_clear_mode** = `0`
`🔗<class_SubViewport_property_render_target_clear_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_clear_mode**(value:
  `ClearMode<enum_SubViewport_ClearMode>`{.interpreted-text role="ref"})
- `ClearMode<enum_SubViewport_ClearMode>`{.interpreted-text role="ref"}
  **get_clear_mode**()

The clear mode when the sub-viewport is used as a render target.

\*\*Note:\*\* This property is intended for 2D usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SubViewport_property_render_target_update_mode}
::: rst-class
classref-property
:::
::::

`UpdateMode<enum_SubViewport_UpdateMode>`{.interpreted-text role="ref"}
**render_target_update_mode** = `2`
`🔗<class_SubViewport_property_render_target_update_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_update_mode**(value:
  `UpdateMode<enum_SubViewport_UpdateMode>`{.interpreted-text
  role="ref"})
- `UpdateMode<enum_SubViewport_UpdateMode>`{.interpreted-text
  role="ref"} **get_update_mode**()

The update mode when the sub-viewport is used as a render target.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SubViewport_property_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **size** =
`Vector2i(512, 512)`
`🔗<class_SubViewport_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_size**()

The width and height of the sub-viewport. Must be set to a value greater
than or equal to 2 pixels on both dimensions. Otherwise, nothing will be
displayed.

\*\*Note:\*\* If the parent node is a
`SubViewportContainer<class_SubViewportContainer>`{.interpreted-text
role="ref"} and its
`SubViewportContainer.stretch<class_SubViewportContainer_property_stretch>`{.interpreted-text
role="ref"} is `true`, the viewport size cannot be changed manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SubViewport_property_size_2d_override}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**size_2d_override** = `Vector2i(0, 0)`
`🔗<class_SubViewport_property_size_2d_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size_2d_override**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_size_2d_override**()

The 2D size override of the sub-viewport. If either the width or height
is `0`, the override is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SubViewport_property_size_2d_override_stretch}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**size_2d_override_stretch** = `false`
`🔗<class_SubViewport_property_size_2d_override_stretch>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size_2d_override_stretch**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_size_2d_override_stretch_enabled**()

If `true`, the 2D size override affects stretch as well.
