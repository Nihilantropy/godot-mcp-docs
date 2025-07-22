github_url
:   hide

# CameraTexture {#class_CameraTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Texture provided by a `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This texture gives access to the camera texture provided by a
`CameraFeed<class_CameraFeed>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Many cameras supply YCbCr images which need to be
converted in a shader.

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

:::: {#class_CameraTexture_property_camera_feed_id}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **camera_feed_id** = `0`
`🔗<class_CameraTexture_property_camera_feed_id>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_camera_feed_id**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_camera_feed_id**()

The ID of the `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"} for which we want to display the image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraTexture_property_camera_is_active}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **camera_is_active** =
`false`
`🔗<class_CameraTexture_property_camera_is_active>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_camera_active**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_camera_active**()

Convenience property that gives access to the active property of the
`CameraFeed<class_CameraFeed>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraTexture_property_which_feed}
::: rst-class
classref-property
:::
::::

`FeedImage<enum_CameraServer_FeedImage>`{.interpreted-text role="ref"}
**which_feed** = `0`
`🔗<class_CameraTexture_property_which_feed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_which_feed**(value:
  `FeedImage<enum_CameraServer_FeedImage>`{.interpreted-text
  role="ref"})
- `FeedImage<enum_CameraServer_FeedImage>`{.interpreted-text role="ref"}
  **get_which_feed**()

Which image within the `CameraFeed<class_CameraFeed>`{.interpreted-text
role="ref"} we want access to, important if the camera image is split in
a Y and CbCr component.
