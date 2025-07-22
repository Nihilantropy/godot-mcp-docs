github_url
:   hide

# TextureLayered {#class_TextureLayered}

**Inherits:** `Texture<class_Texture>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`CompressedTextureLayered<class_CompressedTextureLayered>`{.interpreted-text
role="ref"},
`ImageTextureLayered<class_ImageTextureLayered>`{.interpreted-text
role="ref"},
`PlaceholderTextureLayered<class_PlaceholderTextureLayered>`{.interpreted-text
role="ref"},
`TextureLayeredRD<class_TextureLayeredRD>`{.interpreted-text role="ref"}

Base class for texture types which contain the data of multiple
`Image<class_Image>`{.interpreted-text role="ref"}s. Each image is of
the same size and format.

::: rst-class
classref-introduction-group
:::

## Description

Base class for
`ImageTextureLayered<class_ImageTextureLayered>`{.interpreted-text
role="ref"} and
`CompressedTextureLayered<class_CompressedTextureLayered>`{.interpreted-text
role="ref"}. Cannot be used directly, but contains all the functions
necessary for accessing the derived resource types. See also
`Texture3D<class_Texture3D>`{.interpreted-text role="ref"}.

Data is set on a per-layer basis. For
`Texture2DArray<class_Texture2DArray>`{.interpreted-text role="ref"}s,
the layer specifies the array layer.

All images need to have the same width, height and number of mipmap
levels.

A **TextureLayered** can be loaded with
`ResourceLoader.load()<class_ResourceLoader_method_load>`{.interpreted-text
role="ref"}.

Internally, Godot maps these files to their respective counterparts in
the target rendering driver (Vulkan, OpenGL3).

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

## Enumerations

:::: {#enum_TextureLayered_LayeredType}
::: rst-class
classref-enumeration
:::
::::

enum **LayeredType**:
`🔗<enum_TextureLayered_LayeredType>`{.interpreted-text role="ref"}

:::: {#class_TextureLayered_constant_LAYERED_TYPE_2D_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`LayeredType<enum_TextureLayered_LayeredType>`{.interpreted-text
role="ref"} **LAYERED_TYPE_2D_ARRAY** = `0`

Texture is a generic
`Texture2DArray<class_Texture2DArray>`{.interpreted-text role="ref"}.

:::: {#class_TextureLayered_constant_LAYERED_TYPE_CUBEMAP}
::: rst-class
classref-enumeration-constant
:::
::::

`LayeredType<enum_TextureLayered_LayeredType>`{.interpreted-text
role="ref"} **LAYERED_TYPE_CUBEMAP** = `1`

Texture is a `Cubemap<class_Cubemap>`{.interpreted-text role="ref"},
with each side in its own layer (6 in total).

:::: {#class_TextureLayered_constant_LAYERED_TYPE_CUBEMAP_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`LayeredType<enum_TextureLayered_LayeredType>`{.interpreted-text
role="ref"} **LAYERED_TYPE_CUBEMAP_ARRAY** = `2`

Texture is a `CubemapArray<class_CubemapArray>`{.interpreted-text
role="ref"}, with each cubemap being made of 6 layers.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TextureLayered_private_method__get_format}
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
`🔗<class_TextureLayered_private_method__get_format>`{.interpreted-text
role="ref"}

Called when the **TextureLayered**\'s format is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_private_method__get_height}
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
`🔗<class_TextureLayered_private_method__get_height>`{.interpreted-text
role="ref"}

Called when the **TextureLayered**\'s height is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_private_method__get_layer_data}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**\_get_layer_data**(layer_index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_private_method__get_layer_data>`{.interpreted-text
role="ref"}

Called when the data for a layer in the **TextureLayered** is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_private_method__get_layered_type}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_layered_type**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_private_method__get_layered_type>`{.interpreted-text
role="ref"}

Called when the layers\' type in the **TextureLayered** is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_private_method__get_layers}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_layers**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_private_method__get_layers>`{.interpreted-text
role="ref"}

Called when the number of layers in the **TextureLayered** is queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_private_method__get_width}
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
`🔗<class_TextureLayered_private_method__get_width>`{.interpreted-text
role="ref"}

Called when the **TextureLayered**\'s width queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_private_method__has_mipmaps}
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
`🔗<class_TextureLayered_private_method__has_mipmaps>`{.interpreted-text
role="ref"}

Called when the presence of mipmaps in the **TextureLayered** is
queried.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_method_get_format}
::: rst-class
classref-method
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**get_format**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_method_get_format>`{.interpreted-text
role="ref"}

Returns the current format being used by this texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_method_get_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_method_get_height>`{.interpreted-text
role="ref"}

Returns the height of the texture in pixels. Height is typically
represented by the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_method_get_layer_data}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**get_layer_data**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_method_get_layer_data>`{.interpreted-text
role="ref"}

Returns an `Image<class_Image>`{.interpreted-text role="ref"} resource
with the data from specified `layer`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_method_get_layered_type}
::: rst-class
classref-method
:::
::::

`LayeredType<enum_TextureLayered_LayeredType>`{.interpreted-text
role="ref"} **get_layered_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_method_get_layered_type>`{.interpreted-text
role="ref"}

Returns the **TextureLayered**\'s type. The type determines how the data
is accessed, with cubemaps having special types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_method_get_layers}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_layers**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_method_get_layers>`{.interpreted-text
role="ref"}

Returns the number of referenced `Image<class_Image>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_method_get_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_width**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_method_get_width>`{.interpreted-text
role="ref"}

Returns the width of the texture in pixels. Width is typically
represented by the X axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextureLayered_method_has_mipmaps}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_mipmaps**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextureLayered_method_has_mipmaps>`{.interpreted-text
role="ref"}

Returns `true` if the layers have generated mipmaps.
