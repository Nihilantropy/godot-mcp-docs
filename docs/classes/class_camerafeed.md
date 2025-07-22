github_url
:   hide

# CameraFeed {#class_CameraFeed}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A camera feed gives you access to a single physical camera attached to
your device.

::: rst-class
classref-introduction-group
:::

## Description

A camera feed gives you access to a single physical camera attached to
your device. When enabled, Godot will start capturing frames from the
camera which can then be used. See also
`CameraServer<class_CameraServer>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Many cameras will return YCbCr images which are split into
two textures and need to be combined in a shader. Godot does this
automatically for you if you set the environment to show the camera
image in the background.

\*\*Note:\*\* This class is currently only implemented on Linux,
Android, macOS, and iOS. On other platforms no **CameraFeed**s will be
available. To get a **CameraFeed** on iOS, the camera plugin from
[godot-ios-plugins](https://github.com/godotengine/godot-ios-plugins) is
required.

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

## Signals

:::: {#class_CameraFeed_signal_format_changed}
::: rst-class
classref-signal
:::
::::

**format_changed**()
`🔗<class_CameraFeed_signal_format_changed>`{.interpreted-text
role="ref"}

Emitted when the format has changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_signal_frame_changed}
::: rst-class
classref-signal
:::
::::

**frame_changed**()
`🔗<class_CameraFeed_signal_frame_changed>`{.interpreted-text
role="ref"}

Emitted when a new frame is available.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_CameraFeed_FeedDataType}
::: rst-class
classref-enumeration
:::
::::

enum **FeedDataType**:
`🔗<enum_CameraFeed_FeedDataType>`{.interpreted-text role="ref"}

:::: {#class_CameraFeed_constant_FEED_NOIMAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedDataType<enum_CameraFeed_FeedDataType>`{.interpreted-text
role="ref"} **FEED_NOIMAGE** = `0`

No image set for the feed.

:::: {#class_CameraFeed_constant_FEED_RGB}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedDataType<enum_CameraFeed_FeedDataType>`{.interpreted-text
role="ref"} **FEED_RGB** = `1`

Feed supplies RGB images.

:::: {#class_CameraFeed_constant_FEED_YCBCR}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedDataType<enum_CameraFeed_FeedDataType>`{.interpreted-text
role="ref"} **FEED_YCBCR** = `2`

Feed supplies YCbCr images that need to be converted to RGB.

:::: {#class_CameraFeed_constant_FEED_YCBCR_SEP}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedDataType<enum_CameraFeed_FeedDataType>`{.interpreted-text
role="ref"} **FEED_YCBCR_SEP** = `3`

Feed supplies separate Y and CbCr images that need to be combined and
converted to RGB.

:::: {#class_CameraFeed_constant_FEED_EXTERNAL}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedDataType<enum_CameraFeed_FeedDataType>`{.interpreted-text
role="ref"} **FEED_EXTERNAL** = `4`

Feed supplies external image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CameraFeed_FeedPosition}
::: rst-class
classref-enumeration
:::
::::

enum **FeedPosition**:
`🔗<enum_CameraFeed_FeedPosition>`{.interpreted-text role="ref"}

:::: {#class_CameraFeed_constant_FEED_UNSPECIFIED}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedPosition<enum_CameraFeed_FeedPosition>`{.interpreted-text
role="ref"} **FEED_UNSPECIFIED** = `0`

Unspecified position.

:::: {#class_CameraFeed_constant_FEED_FRONT}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedPosition<enum_CameraFeed_FeedPosition>`{.interpreted-text
role="ref"} **FEED_FRONT** = `1`

Camera is mounted at the front of the device.

:::: {#class_CameraFeed_constant_FEED_BACK}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedPosition<enum_CameraFeed_FeedPosition>`{.interpreted-text
role="ref"} **FEED_BACK** = `2`

Camera is mounted at the back of the device.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CameraFeed_property_feed_is_active}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **feed_is_active** =
`false` `🔗<class_CameraFeed_property_feed_is_active>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_active**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_active**()

If `true`, the feed is active.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_property_feed_transform}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**feed_transform** = `Transform2D(1, 0, 0, -1, 0, 1)`
`🔗<class_CameraFeed_property_feed_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform**(value:
  `Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_transform**()

The transform applied to the camera\'s image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_property_formats}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **formats** = `[]`
`🔗<class_CameraFeed_property_formats>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `Array<class_Array>`{.interpreted-text role="ref"} **get_formats**()

Formats supported by the feed. Each entry is a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} describing
format parameters.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CameraFeed_private_method__activate_feed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_activate_feed**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_CameraFeed_private_method__activate_feed>`{.interpreted-text
role="ref"}

Called when the camera feed is activated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_private_method__deactivate_feed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_deactivate_feed**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_CameraFeed_private_method__deactivate_feed>`{.interpreted-text
role="ref"}

Called when the camera feed is deactivated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_get_datatype}
::: rst-class
classref-method
:::
::::

`FeedDataType<enum_CameraFeed_FeedDataType>`{.interpreted-text
role="ref"} **get_datatype**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CameraFeed_method_get_datatype>`{.interpreted-text role="ref"}

Returns feed image data type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_get_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CameraFeed_method_get_id>`{.interpreted-text
role="ref"}

Returns the unique ID for this feed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CameraFeed_method_get_name>`{.interpreted-text
role="ref"}

Returns the camera\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_get_position}
::: rst-class
classref-method
:::
::::

`FeedPosition<enum_CameraFeed_FeedPosition>`{.interpreted-text
role="ref"} **get_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CameraFeed_method_get_position>`{.interpreted-text role="ref"}

Returns the position of camera on the device.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_get_texture_tex_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_texture_tex_id**(feed_image_type:
`FeedImage<enum_CameraServer_FeedImage>`{.interpreted-text role="ref"})
`🔗<class_CameraFeed_method_get_texture_tex_id>`{.interpreted-text
role="ref"}

Returns the texture backend ID (usable by some external libraries that
need a handle to a texture to write data).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_set_external}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_external**(width: `int<class_int>`{.interpreted-text role="ref"},
height: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CameraFeed_method_set_external>`{.interpreted-text role="ref"}

Sets the feed as external feed provided by another library.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_set_format}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **set_format**(index:
`int<class_int>`{.interpreted-text role="ref"}, parameters:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_CameraFeed_method_set_format>`{.interpreted-text role="ref"}

Sets the feed format parameters for the given `index` in the
`formats<class_CameraFeed_property_formats>`{.interpreted-text
role="ref"} array. Returns `true` on success. By default, the YUYV
encoded stream is transformed to
`FEED_RGB<class_CameraFeed_constant_FEED_RGB>`{.interpreted-text
role="ref"}. The YUYV encoded stream output format can be changed by
setting `parameters`\'s `output` entry to one of the following:

- `"separate"` will result in
  `FEED_YCBCR_SEP<class_CameraFeed_constant_FEED_YCBCR_SEP>`{.interpreted-text
  role="ref"};
- `"grayscale"` will result in desaturated
  `FEED_RGB<class_CameraFeed_constant_FEED_RGB>`{.interpreted-text
  role="ref"};
- `"copy"` will result in
  `FEED_YCBCR<class_CameraFeed_constant_FEED_YCBCR>`{.interpreted-text
  role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_set_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_name**(name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CameraFeed_method_set_name>`{.interpreted-text role="ref"}

Sets the camera\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_set_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_position**(position:
`FeedPosition<enum_CameraFeed_FeedPosition>`{.interpreted-text
role="ref"})
`🔗<class_CameraFeed_method_set_position>`{.interpreted-text role="ref"}

Sets the position of this camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_set_rgb_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_rgb_image**(rgb_image: `Image<class_Image>`{.interpreted-text
role="ref"})
`🔗<class_CameraFeed_method_set_rgb_image>`{.interpreted-text
role="ref"}

Sets RGB image for this feed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraFeed_method_set_ycbcr_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ycbcr_image**(ycbcr_image: `Image<class_Image>`{.interpreted-text
role="ref"})
`🔗<class_CameraFeed_method_set_ycbcr_image>`{.interpreted-text
role="ref"}

Sets YCbCr image for this feed.
