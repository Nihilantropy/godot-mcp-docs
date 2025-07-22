github_url
:   hide

# ExternalTexture {#class_ExternalTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Texture which displays the content of an external buffer.

::: rst-class
classref-introduction-group
:::

## Description

Displays the content of an external buffer provided by the platform.

Requires the
[OES_EGL_image_external](https://registry.khronos.org/OpenGL/extensions/OES/OES_EGL_image_external.txt)
extension (OpenGL) or
[VK_ANDROID_external_memory_android_hardware_buffer](https://registry.khronos.org/vulkan/specs/1.1-extensions/html/vkspec.html#VK_ANDROID_external_memory_android_hardware_buffer)
extension (Vulkan).

\*\*Note:\*\* This is currently only supported in Android builds.

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

## Property Descriptions

:::: {#class_ExternalTexture_property_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **size** =
`Vector2(256, 256)`
`🔗<class_ExternalTexture_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_size**()

External texture size.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ExternalTexture_method_get_external_texture_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_external_texture_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ExternalTexture_method_get_external_texture_id>`{.interpreted-text
role="ref"}

Returns the external texture ID.

Depending on your use case, you may need to pass this to platform APIs,
for example, when creating an `android.graphics.SurfaceTexture` on
Android.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ExternalTexture_method_set_external_buffer_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_external_buffer_id**(external_buffer_id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ExternalTexture_method_set_external_buffer_id>`{.interpreted-text
role="ref"}

Sets the external buffer ID.

Depending on your use case, you may need to call this with data received
from a platform API, for example, `SurfaceTexture.getHardwareBuffer()`
on Android.
