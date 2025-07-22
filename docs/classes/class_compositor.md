github_url
:   hide

# Compositor {#class_Compositor}

**Experimental:** More customization of the rendering pipeline will be
added in the future.

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Stores attributes used to customize how a Viewport is rendered.

::: rst-class
classref-introduction-group
:::

## Description

The compositor resource stores attributes used to customize how a
`Viewport<class_Viewport>`{.interpreted-text role="ref"} is rendered.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `The Compositor <../tutorials/rendering/compositor>`{.interpreted-text
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

:::: {#class_Compositor_property_compositor_effects}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`CompositorEffect<class_CompositorEffect>`{.interpreted-text
role="ref"}\] **compositor_effects** = `[]`
`🔗<class_Compositor_property_compositor_effects>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_compositor_effects**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`CompositorEffect<class_CompositorEffect>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`CompositorEffect<class_CompositorEffect>`{.interpreted-text
  role="ref"}\] **get_compositor_effects**()

The custom `CompositorEffect<class_CompositorEffect>`{.interpreted-text
role="ref"}s that are applied during rendering of viewports using this
compositor.
