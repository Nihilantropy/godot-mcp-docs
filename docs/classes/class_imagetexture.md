github_url
:   hide

# ImageTexture {#class_ImageTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `Texture2D<class_Texture2D>`{.interpreted-text role="ref"} based on an
`Image<class_Image>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A `Texture2D<class_Texture2D>`{.interpreted-text role="ref"} based on an
`Image<class_Image>`{.interpreted-text role="ref"}. For an image to be
displayed, an **ImageTexture** has to be created from it using the
`create_from_image()<class_ImageTexture_method_create_from_image>`{.interpreted-text
role="ref"} method:

    var image = Image.load_from_file("res://icon.svg")
    var texture = ImageTexture.create_from_image(image)
    $Sprite2D.texture = texture

This way, textures can be created at run-time by loading images both
from within the editor and externally.

\*\*Warning:\*\* Prefer to load imported textures with
`@GDScript.load()<class_@GDScript_method_load>`{.interpreted-text
role="ref"} over loading them from within the filesystem dynamically
with `Image.load()<class_Image_method_load>`{.interpreted-text
role="ref"}, as it may not work in exported projects:

    var texture = load("res://icon.svg")
    $Sprite2D.texture = texture

This is because images have to be imported as a
`CompressedTexture2D<class_CompressedTexture2D>`{.interpreted-text
role="ref"} first to be loaded with
`@GDScript.load()<class_@GDScript_method_load>`{.interpreted-text
role="ref"}. If you\'d still like to load an image file just like any
other `Resource<class_Resource>`{.interpreted-text role="ref"}, import
it as an `Image<class_Image>`{.interpreted-text role="ref"} resource
instead, and then load it normally using the
`@GDScript.load()<class_@GDScript_method_load>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* The image can be retrieved from an imported texture using
the
`Texture2D.get_image()<class_Texture2D_method_get_image>`{.interpreted-text
role="ref"} method, which returns a copy of the image:

    var texture = load("res://icon.svg")
    var image = texture.get_image()

An **ImageTexture** is not meant to be operated from within the editor
interface directly, and is mostly useful for rendering images on screen
dynamically via code. If you need to generate images procedurally from
within the editor, consider saving and importing images as custom
texture resources implementing a new
`EditorImportPlugin<class_EditorImportPlugin>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The maximum texture size is 16384×16384 pixels due to
graphics hardware limitations.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Importing images <../tutorials/assets_pipeline/importing_images>`{.interpreted-text
  role="doc"}

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

## Method Descriptions

:::: {#class_ImageTexture_method_create_from_image}
::: rst-class
classref-method
:::
::::

`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"}
**create_from_image**(image: `Image<class_Image>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_ImageTexture_method_create_from_image>`{.interpreted-text
role="ref"}

Creates a new **ImageTexture** and initializes it by allocating and
setting the data from an `Image<class_Image>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImageTexture_method_get_format}
::: rst-class
classref-method
:::
::::

`Format<enum_Image_Format>`{.interpreted-text role="ref"}
**get_format**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImageTexture_method_get_format>`{.interpreted-text role="ref"}

Returns the format of the texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImageTexture_method_set_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_image**(image: `Image<class_Image>`{.interpreted-text role="ref"})
`🔗<class_ImageTexture_method_set_image>`{.interpreted-text role="ref"}

Replaces the texture\'s data with a new
`Image<class_Image>`{.interpreted-text role="ref"}. This will
re-allocate new memory for the texture.

If you want to update the image, but don\'t need to change its
parameters (format, size), use
`update()<class_ImageTexture_method_update>`{.interpreted-text
role="ref"} instead for better performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImageTexture_method_set_size_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_size_override**(size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_ImageTexture_method_set_size_override>`{.interpreted-text
role="ref"}

Resizes the texture to the specified dimensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImageTexture_method_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update**(image: `Image<class_Image>`{.interpreted-text role="ref"})
`🔗<class_ImageTexture_method_update>`{.interpreted-text role="ref"}

Replaces the texture\'s data with a new
`Image<class_Image>`{.interpreted-text role="ref"}.

\*\*Note:\*\* The texture has to be created using
`create_from_image()<class_ImageTexture_method_create_from_image>`{.interpreted-text
role="ref"} or initialized first with the
`set_image()<class_ImageTexture_method_set_image>`{.interpreted-text
role="ref"} method before it can be updated. The new image dimensions,
format, and mipmaps configuration should match the existing texture\'s
image configuration.

Use this method over
`set_image()<class_ImageTexture_method_set_image>`{.interpreted-text
role="ref"} if you need to update the texture frequently, which is
faster than allocating additional memory for a new texture each time.
