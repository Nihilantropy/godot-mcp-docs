github_url
:   hide

# ImageTexture3D {#class_ImageTexture3D}

**Inherits:** `Texture3D<class_Texture3D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Texture with 3 dimensions.

::: rst-class
classref-introduction-group
:::

## Description

**ImageTexture3D** is a 3-dimensional
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"} that
has a width, height, and depth. See also
`ImageTextureLayered<class_ImageTextureLayered>`{.interpreted-text
role="ref"}.

3D textures are typically used to store density maps for
`FogMaterial<class_FogMaterial>`{.interpreted-text role="ref"}, color
correction LUTs for `Environment<class_Environment>`{.interpreted-text
role="ref"}, vector fields for
`GPUParticlesAttractorVectorField3D<class_GPUParticlesAttractorVectorField3D>`{.interpreted-text
role="ref"} and collision maps for
`GPUParticlesCollisionSDF3D<class_GPUParticlesCollisionSDF3D>`{.interpreted-text
role="ref"}. 3D textures can also be used in custom shaders.

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

:::: {#class_ImageTexture3D_method_create}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create**(format: `Format<enum_Image_Format>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"},
height: `int<class_int>`{.interpreted-text role="ref"}, depth:
`int<class_int>`{.interpreted-text role="ref"}, use_mipmaps:
`bool<class_bool>`{.interpreted-text role="ref"}, data:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\])
`🔗<class_ImageTexture3D_method_create>`{.interpreted-text role="ref"}

Creates the **ImageTexture3D** with specified `format`, `width`,
`height`, and `depth`. If `use_mipmaps` is `true`, generates mipmaps for
the **ImageTexture3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImageTexture3D_method_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update**(data: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\])
`🔗<class_ImageTexture3D_method_update>`{.interpreted-text role="ref"}

Replaces the texture\'s existing data with the layers specified in
`data`. The size of `data` must match the parameters that were used for
`create()<class_ImageTexture3D_method_create>`{.interpreted-text
role="ref"}. In other words, the texture cannot be resized or have its
format changed by calling
`update()<class_ImageTexture3D_method_update>`{.interpreted-text
role="ref"}.
