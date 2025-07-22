github_url
:   hide

# RenderSceneBuffersExtension {#class_RenderSceneBuffersExtension}

**Inherits:**
`RenderSceneBuffers<class_RenderSceneBuffers>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

This class allows for a RenderSceneBuffer implementation to be made in
GDExtension.

::: rst-class
classref-introduction-group
:::

## Description

This class allows for a RenderSceneBuffer implementation to be made in
GDExtension.

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

:::: {#class_RenderSceneBuffersExtension_private_method__configure}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_configure**(config:
`RenderSceneBuffersConfiguration<class_RenderSceneBuffersConfiguration>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersExtension_private_method__configure>`{.interpreted-text
role="ref"}

Implement this in GDExtension to handle the (re)sizing of a viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersExtension_private_method__set_anisotropic_filtering_level}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_anisotropic_filtering_level**(anisotropic_filtering_level:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersExtension_private_method__set_anisotropic_filtering_level>`{.interpreted-text
role="ref"}

Implement this in GDExtension to change the anisotropic filtering level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersExtension_private_method__set_fsr_sharpness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_fsr_sharpness**(fsr_sharpness:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersExtension_private_method__set_fsr_sharpness>`{.interpreted-text
role="ref"}

Implement this in GDExtension to record a new FSR sharpness value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersExtension_private_method__set_texture_mipmap_bias}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_texture_mipmap_bias**(texture_mipmap_bias:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersExtension_private_method__set_texture_mipmap_bias>`{.interpreted-text
role="ref"}

Implement this in GDExtension to change the texture mipmap bias.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersExtension_private_method__set_use_debanding}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_use_debanding**(use_debanding:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderSceneBuffersExtension_private_method__set_use_debanding>`{.interpreted-text
role="ref"}

Implement this in GDExtension to react to the debanding flag changing.
