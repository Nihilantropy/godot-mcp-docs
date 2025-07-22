github_url
:   hide

# Texture3D {#class_Texture3D}

**Inherits:** `Texture<class_Texture>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`CompressedTexture3D<class_CompressedTexture3D>`{.interpreted-text
role="ref"}, `ImageTexture3D<class_ImageTexture3D>`{.interpreted-text
role="ref"}, `NoiseTexture3D<class_NoiseTexture3D>`{.interpreted-text
role="ref"},
`PlaceholderTexture3D<class_PlaceholderTexture3D>`{.interpreted-text
role="ref"}, `Texture3DRD<class_Texture3DRD>`{.interpreted-text
role="ref"}

Base class for 3-dimensional textures.

::: rst-class
classref-introduction-group
:::

## Description

Base class for `ImageTexture3D<class_ImageTexture3D>`{.interpreted-text
role="ref"} and
`CompressedTexture3D<class_CompressedTexture3D>`{.interpreted-text
role="ref"}. Cannot be used directly, but contains all the functions
necessary for accessing the derived resource types. **Texture3D** is the
base class for all 3-dimensional texture types. See also
`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}.

All images need to have the same width, height and number of mipmap
levels.

To create such a texture file yourself, reimport your image files using
the Godot Editor import presets.

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

:::: {#class_Texture3D_private_method__get_data}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\]
**\_get_data**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture3D_private_method__get_data>`{.interpreted-text
role="ref"}

Called when the **Texture3D**\'s data is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_private_method__get_depth}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_depth**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture3D_private_method__get_depth>`{.interpreted-text
role="ref"}

Called when the **Texture3D**\'s depth is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_private_method__get_format}
::: rst-class
classref-method
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**\_get_format**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture3D_private_method__get_format>`{.interpreted-text
role="ref"}

Called when the **Texture3D**\'s format is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_private_method__get_height}
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
`🔗<class_Texture3D_private_method__get_height>`{.interpreted-text
role="ref"}

Called when the **Texture3D**\'s height is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_private_method__get_width}
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
`🔗<class_Texture3D_private_method__get_width>`{.interpreted-text
role="ref"}

Called when the **Texture3D**\'s width is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_private_method__has_mipmaps}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_has_mipmaps**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture3D_private_method__has_mipmaps>`{.interpreted-text
role="ref"}

Called when the presence of mipmaps in the **Texture3D** is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_method_create_placeholder}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**create_placeholder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Texture3D_method_create_placeholder>`{.interpreted-text
role="ref"}

Creates a placeholder version of this resource
(`PlaceholderTexture3D<class_PlaceholderTexture3D>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_method_get_data}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\]
**get_data**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture3D_method_get_data>`{.interpreted-text
role="ref"}

Returns the **Texture3D**\'s data as an array of
`Image<class_Image>`{.interpreted-text role="ref"}s. Each
`Image<class_Image>`{.interpreted-text role="ref"} represents a *slice*
of the **Texture3D**, with different slices mapping to different depth
(Z axis) levels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_method_get_depth}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_depth**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture3D_method_get_depth>`{.interpreted-text
role="ref"}

Returns the **Texture3D**\'s depth in pixels. Depth is typically
represented by the Z axis (a dimension not present in
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_method_get_format}
::: rst-class
classref-method
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**get_format**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture3D_method_get_format>`{.interpreted-text
role="ref"}

Returns the current format being used by this texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_method_get_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture3D_method_get_height>`{.interpreted-text
role="ref"}

Returns the **Texture3D**\'s height in pixels. Width is typically
represented by the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_method_get_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_width**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture3D_method_get_width>`{.interpreted-text
role="ref"}

Returns the **Texture3D**\'s width in pixels. Width is typically
represented by the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Texture3D_method_has_mipmaps}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_mipmaps**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Texture3D_method_has_mipmaps>`{.interpreted-text
role="ref"}

Returns `true` if the **Texture3D** has generated mipmaps.
