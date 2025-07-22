github_url
:   hide

# CameraServer {#class_CameraServer}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Server keeping track of different cameras accessible in Godot.

::: rst-class
classref-introduction-group
:::

## Description

The **CameraServer** keeps track of different cameras accessible in
Godot. These are external cameras such as webcams or the cameras on your
phone.

It is notably used to provide AR modules with a video feed from the
camera.

\*\*Note:\*\* This class is currently only implemented on Linux,
Android, macOS, and iOS. On other platforms no
`CameraFeed<class_CameraFeed>`{.interpreted-text role="ref"}s will be
available. To get a `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"} on iOS, the camera plugin from
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

:::: {#class_CameraServer_signal_camera_feed_added}
::: rst-class
classref-signal
:::
::::

**camera_feed_added**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_CameraServer_signal_camera_feed_added>`{.interpreted-text
role="ref"}

Emitted when a `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"} is added (e.g. a webcam is plugged in).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraServer_signal_camera_feed_removed}
::: rst-class
classref-signal
:::
::::

**camera_feed_removed**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_CameraServer_signal_camera_feed_removed>`{.interpreted-text
role="ref"}

Emitted when a `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"} is removed (e.g. a webcam is unplugged).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_CameraServer_FeedImage}
::: rst-class
classref-enumeration
:::
::::

enum **FeedImage**: `🔗<enum_CameraServer_FeedImage>`{.interpreted-text
role="ref"}

:::: {#class_CameraServer_constant_FEED_RGBA_IMAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedImage<enum_CameraServer_FeedImage>`{.interpreted-text role="ref"}
**FEED_RGBA_IMAGE** = `0`

The RGBA camera image.

:::: {#class_CameraServer_constant_FEED_YCBCR_IMAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedImage<enum_CameraServer_FeedImage>`{.interpreted-text role="ref"}
**FEED_YCBCR_IMAGE** = `0`

The [YCbCr](https://en.wikipedia.org/wiki/YCbCr) camera image.

:::: {#class_CameraServer_constant_FEED_Y_IMAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedImage<enum_CameraServer_FeedImage>`{.interpreted-text role="ref"}
**FEED_Y_IMAGE** = `0`

The Y component camera image.

:::: {#class_CameraServer_constant_FEED_CBCR_IMAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`FeedImage<enum_CameraServer_FeedImage>`{.interpreted-text role="ref"}
**FEED_CBCR_IMAGE** = `1`

The CbCr component camera image.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CameraServer_property_monitoring_feeds}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **monitoring_feeds** =
`false`
`🔗<class_CameraServer_property_monitoring_feeds>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_monitoring_feeds**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_monitoring_feeds**()

If `true`, the server is actively monitoring available camera feeds.

This has a performance cost, so only set it to `true` when you\'re
actively accessing the camera.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CameraServer_method_add_feed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_feed**(feed: `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"}) `🔗<class_CameraServer_method_add_feed>`{.interpreted-text
role="ref"}

Adds the camera `feed` to the camera server.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraServer_method_feeds}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"}\] **feeds**()
`🔗<class_CameraServer_method_feeds>`{.interpreted-text role="ref"}

Returns an array of `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraServer_method_get_feed}
::: rst-class
classref-method
:::
::::

`CameraFeed<class_CameraFeed>`{.interpreted-text role="ref"}
**get_feed**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CameraServer_method_get_feed>`{.interpreted-text role="ref"}

Returns the `CameraFeed<class_CameraFeed>`{.interpreted-text role="ref"}
corresponding to the camera with the given `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraServer_method_get_feed_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_feed_count**()
`🔗<class_CameraServer_method_get_feed_count>`{.interpreted-text
role="ref"}

Returns the number of `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"}s registered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraServer_method_remove_feed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_feed**(feed: `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"})
`🔗<class_CameraServer_method_remove_feed>`{.interpreted-text
role="ref"}

Removes the specified camera `feed`.
