github_url
:   hide

# ImageFormatLoaderExtension {#class_ImageFormatLoaderExtension}

**Inherits:**
`ImageFormatLoader<class_ImageFormatLoader>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Base class for creating
`ImageFormatLoader<class_ImageFormatLoader>`{.interpreted-text
role="ref"} extensions (adding support for extra image formats).

::: rst-class
classref-introduction-group
:::

## Description

The engine supports multiple image formats out of the box (PNG, SVG,
JPEG, WebP to name a few), but you can choose to implement support for
additional image formats by extending this class.

Be sure to respect the documented return types and values. You should
create an instance of it, and call
`add_format_loader()<class_ImageFormatLoaderExtension_method_add_format_loader>`{.interpreted-text
role="ref"} to register that loader during the initialization phase.

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

:::: {#class_ImageFormatLoaderExtension_private_method__get_recognized_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_recognized_extensions**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImageFormatLoaderExtension_private_method__get_recognized_extensions>`{.interpreted-text
role="ref"}

Returns the list of file extensions for this image format. Files with
the given extensions will be treated as image file and loaded using this
class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImageFormatLoaderExtension_private_method__load_image}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_load_image**(image: `Image<class_Image>`{.interpreted-text
role="ref"}, fileaccess:
`FileAccess<class_FileAccess>`{.interpreted-text role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LoaderFlags<enum_ImageFormatLoader_LoaderFlags>`{.interpreted-text
role="ref"}\], scale: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_ImageFormatLoaderExtension_private_method__load_image>`{.interpreted-text
role="ref"}

Loads the content of `fileaccess` into the provided `image`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImageFormatLoaderExtension_method_add_format_loader}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_format_loader**()
`🔗<class_ImageFormatLoaderExtension_method_add_format_loader>`{.interpreted-text
role="ref"}

Add this format loader to the engine, allowing it to recognize the file
extensions returned by
`_get_recognized_extensions()<class_ImageFormatLoaderExtension_private_method__get_recognized_extensions>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImageFormatLoaderExtension_method_remove_format_loader}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_format_loader**()
`🔗<class_ImageFormatLoaderExtension_method_remove_format_loader>`{.interpreted-text
role="ref"}

Remove this format loader from the engine.
