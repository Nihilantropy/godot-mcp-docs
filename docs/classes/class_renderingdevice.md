github_url
:   hide

# RenderingDevice {#class_RenderingDevice}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Abstraction for working with modern low-level graphics APIs.

::: rst-class
classref-introduction-group
:::

## Description

**RenderingDevice** is an abstraction for working with modern low-level
graphics APIs such as Vulkan. Compared to
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
(which works with Godot\'s own rendering subsystems),
**RenderingDevice** is much lower-level and allows working more directly
with the underlying graphics APIs. **RenderingDevice** is used in Godot
to provide support for several modern low-level graphics APIs while
reducing the amount of code duplication required. **RenderingDevice**
can also be used in your own projects to perform things that are not
exposed by `RenderingServer<class_RenderingServer>`{.interpreted-text
role="ref"} or high-level nodes, such as using compute shaders.

On startup, Godot creates a global **RenderingDevice** which can be
retrieved using
`RenderingServer.get_rendering_device()<class_RenderingServer_method_get_rendering_device>`{.interpreted-text
role="ref"}. This global **RenderingDevice** performs drawing to the
screen.

\*\*Local RenderingDevices:\*\* Using
`RenderingServer.create_local_rendering_device()<class_RenderingServer_method_create_local_rendering_device>`{.interpreted-text
role="ref"}, you can create \"secondary\" rendering devices to perform
drawing and GPU compute operations on separate threads.

\*\*Note:\*\* **RenderingDevice** assumes intermediate knowledge of
modern graphics APIs such as Vulkan, Direct3D 12, Metal or WebGPU. These
graphics APIs are lower-level than OpenGL or Direct3D 11, requiring you
to perform what was previously done by the graphics driver itself. If
you have difficulty understanding the concepts used in this class,
follow the [Vulkan Tutorial](https://vulkan-tutorial.com/) or [Vulkan
Guide](https://vkguide.dev/). It\'s recommended to have existing modern
OpenGL or Direct3D 11 knowledge before attempting to learn a low-level
graphics API.

\*\*Note:\*\* **RenderingDevice** is not available when running in
headless mode or when using the Compatibility rendering method.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using compute shaders <../tutorials/shaders/compute_shaders>`{.interpreted-text
  role="doc"}

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

:::: {#enum_RenderingDevice_DeviceType}
::: rst-class
classref-enumeration
:::
::::

enum **DeviceType**:
`🔗<enum_RenderingDevice_DeviceType>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_DEVICE_TYPE_OTHER}
::: rst-class
classref-enumeration-constant
:::
::::

`DeviceType<enum_RenderingDevice_DeviceType>`{.interpreted-text
role="ref"} **DEVICE_TYPE_OTHER** = `0`

Rendering device type does not match any of the other enum values or is
unknown.

:::: {#class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU}
::: rst-class
classref-enumeration-constant
:::
::::

`DeviceType<enum_RenderingDevice_DeviceType>`{.interpreted-text
role="ref"} **DEVICE_TYPE_INTEGRATED_GPU** = `1`

Rendering device is an integrated GPU, which is typically *(but not
always)* slower than dedicated GPUs
(`DEVICE_TYPE_DISCRETE_GPU<class_RenderingDevice_constant_DEVICE_TYPE_DISCRETE_GPU>`{.interpreted-text
role="ref"}). On Android and iOS, the rendering device type is always
considered to be
`DEVICE_TYPE_INTEGRATED_GPU<class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_DEVICE_TYPE_DISCRETE_GPU}
::: rst-class
classref-enumeration-constant
:::
::::

`DeviceType<enum_RenderingDevice_DeviceType>`{.interpreted-text
role="ref"} **DEVICE_TYPE_DISCRETE_GPU** = `2`

Rendering device is a dedicated GPU, which is typically *(but not
always)* faster than integrated GPUs
(`DEVICE_TYPE_INTEGRATED_GPU<class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_DEVICE_TYPE_VIRTUAL_GPU}
::: rst-class
classref-enumeration-constant
:::
::::

`DeviceType<enum_RenderingDevice_DeviceType>`{.interpreted-text
role="ref"} **DEVICE_TYPE_VIRTUAL_GPU** = `3`

Rendering device is an emulated GPU in a virtual environment. This is
typically much slower than the host GPU, which means the expected
performance level on a dedicated GPU will be roughly equivalent to
`DEVICE_TYPE_INTEGRATED_GPU<class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU>`{.interpreted-text
role="ref"}. Virtual machine GPU passthrough (such as VFIO) will not
report the device type as
`DEVICE_TYPE_VIRTUAL_GPU<class_RenderingDevice_constant_DEVICE_TYPE_VIRTUAL_GPU>`{.interpreted-text
role="ref"}. Instead, the host GPU\'s device type will be reported as if
the GPU was not emulated.

:::: {#class_RenderingDevice_constant_DEVICE_TYPE_CPU}
::: rst-class
classref-enumeration-constant
:::
::::

`DeviceType<enum_RenderingDevice_DeviceType>`{.interpreted-text
role="ref"} **DEVICE_TYPE_CPU** = `4`

Rendering device is provided by software emulation (such as Lavapipe or
[SwiftShader](https://github.com/google/swiftshader)). This is the
slowest kind of rendering device available; it\'s typically much slower
than
`DEVICE_TYPE_INTEGRATED_GPU<class_RenderingDevice_constant_DEVICE_TYPE_INTEGRATED_GPU>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_DEVICE_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DeviceType<enum_RenderingDevice_DeviceType>`{.interpreted-text
role="ref"} **DEVICE_TYPE_MAX** = `5`

Represents the size of the
`DeviceType<enum_RenderingDevice_DeviceType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_DriverResource}
::: rst-class
classref-enumeration
:::
::::

enum **DriverResource**:
`🔗<enum_RenderingDevice_DriverResource>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_LOGICAL_DEVICE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_LOGICAL_DEVICE** = `0`

Specific device object based on a physical device.

- Vulkan: Vulkan device driver resource (`VkDevice`) (`rid` parameter is
  ignored).

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_PHYSICAL_DEVICE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_PHYSICAL_DEVICE** = `1`

Physical device the specific logical device is based on.

- Vulkan: `VkDevice` (`rid` parameter is ignored).

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_TOPMOST_OBJECT}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_TOPMOST_OBJECT** = `2`

Top-most graphics API entry object.

- Vulkan: `VkInstance` (`rid` parameter is ignored).

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_COMMAND_QUEUE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_COMMAND_QUEUE** = `3`

The main graphics-compute command queue.

- Vulkan: `VkQueue` (`rid` parameter is ignored).

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_QUEUE_FAMILY}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_QUEUE_FAMILY** = `4`

The specific family the main queue belongs to.

- Vulkan: The queue family index, a `uint32_t` (`rid` parameter is
  ignored).

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_TEXTURE** = `5`

- Vulkan: `VkImage`.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE_VIEW}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_TEXTURE_VIEW** = `6`

The view of an owned or shared texture.

- Vulkan: `VkImageView`.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE_DATA_FORMAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_TEXTURE_DATA_FORMAT** = `7`

The native id of the data format of the texture.

- Vulkan: `VkFormat`.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_SAMPLER}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_SAMPLER** = `8`

- Vulkan: `VkSampler`.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_UNIFORM_SET}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_UNIFORM_SET** = `9`

- Vulkan: `VkDescriptorSet`.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_BUFFER** = `10`

Buffer of any kind of (storage, vertex, etc.).

- Vulkan: `VkBuffer`.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_COMPUTE_PIPELINE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_COMPUTE_PIPELINE** = `11`

- Vulkan: `VkPipeline`.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_RENDER_PIPELINE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_RENDER_PIPELINE** = `12`

- Vulkan: `VkPipeline`.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_DEVICE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_DEVICE** = `0`

**Deprecated:** Use
`DRIVER_RESOURCE_LOGICAL_DEVICE<class_RenderingDevice_constant_DRIVER_RESOURCE_LOGICAL_DEVICE>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_PHYSICAL_DEVICE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_PHYSICAL_DEVICE** = `1`

**Deprecated:** Use
`DRIVER_RESOURCE_PHYSICAL_DEVICE<class_RenderingDevice_constant_DRIVER_RESOURCE_PHYSICAL_DEVICE>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_INSTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_INSTANCE** = `2`

**Deprecated:** Use
`DRIVER_RESOURCE_TOPMOST_OBJECT<class_RenderingDevice_constant_DRIVER_RESOURCE_TOPMOST_OBJECT>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_QUEUE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_QUEUE** = `3`

**Deprecated:** Use
`DRIVER_RESOURCE_COMMAND_QUEUE<class_RenderingDevice_constant_DRIVER_RESOURCE_COMMAND_QUEUE>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_QUEUE_FAMILY_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_QUEUE_FAMILY_INDEX** = `4`

**Deprecated:** Use
`DRIVER_RESOURCE_QUEUE_FAMILY<class_RenderingDevice_constant_DRIVER_RESOURCE_QUEUE_FAMILY>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_IMAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_IMAGE** = `5`

**Deprecated:** Use
`DRIVER_RESOURCE_TEXTURE<class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_IMAGE_VIEW}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_IMAGE_VIEW** = `6`

**Deprecated:** Use
`DRIVER_RESOURCE_TEXTURE_VIEW<class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE_VIEW>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_IMAGE_NATIVE_TEXTURE_FORMAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_IMAGE_NATIVE_TEXTURE_FORMAT** = `7`

**Deprecated:** Use
`DRIVER_RESOURCE_TEXTURE_DATA_FORMAT<class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE_DATA_FORMAT>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_SAMPLER}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_SAMPLER** = `8`

**Deprecated:** Use
`DRIVER_RESOURCE_SAMPLER<class_RenderingDevice_constant_DRIVER_RESOURCE_SAMPLER>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_DESCRIPTOR_SET}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_DESCRIPTOR_SET** = `9`

**Deprecated:** Use
`DRIVER_RESOURCE_UNIFORM_SET<class_RenderingDevice_constant_DRIVER_RESOURCE_UNIFORM_SET>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_BUFFER** = `10`

**Deprecated:** Use
`DRIVER_RESOURCE_BUFFER<class_RenderingDevice_constant_DRIVER_RESOURCE_BUFFER>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_COMPUTE_PIPELINE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_COMPUTE_PIPELINE** = `11`

**Deprecated:** Use
`DRIVER_RESOURCE_COMPUTE_PIPELINE<class_RenderingDevice_constant_DRIVER_RESOURCE_COMPUTE_PIPELINE>`{.interpreted-text
role="ref"} instead.

:::: {#class_RenderingDevice_constant_DRIVER_RESOURCE_VULKAN_RENDER_PIPELINE}
::: rst-class
classref-enumeration-constant
:::
::::

`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"} **DRIVER_RESOURCE_VULKAN_RENDER_PIPELINE** = `12`

**Deprecated:** Use
`DRIVER_RESOURCE_RENDER_PIPELINE<class_RenderingDevice_constant_DRIVER_RESOURCE_RENDER_PIPELINE>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_DataFormat}
::: rst-class
classref-enumeration
:::
::::

enum **DataFormat**:
`🔗<enum_RenderingDevice_DataFormat>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R4G4_UNORM_PACK8}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R4G4_UNORM_PACK8** = `0`

4-bit-per-channel red/green channel data format, packed into 8 bits.
Values are in the `[0.0, 1.0]` range.

\*\*Note:\*\* More information on all data formats can be found on the
[Identification of
formats](https://registry.khronos.org/vulkan/specs/1.1/html/vkspec.html#_identification_of_formats)
section of the Vulkan specification, as well as the
[VkFormat](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkFormat.html)
enum.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R4G4B4A4_UNORM_PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R4G4B4A4_UNORM_PACK16** = `1`

4-bit-per-channel red/green/blue/alpha channel data format, packed into
16 bits. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B4G4R4A4_UNORM_PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B4G4R4A4_UNORM_PACK16** = `2`

4-bit-per-channel blue/green/red/alpha channel data format, packed into
16 bits. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R5G6B5_UNORM_PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R5G6B5_UNORM_PACK16** = `3`

Red/green/blue channel data format with 5 bits of red, 6 bits of green
and 5 bits of blue, packed into 16 bits. Values are in the `[0.0, 1.0]`
range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B5G6R5_UNORM_PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B5G6R5_UNORM_PACK16** = `4`

Blue/green/red channel data format with 5 bits of blue, 6 bits of green
and 5 bits of red, packed into 16 bits. Values are in the `[0.0, 1.0]`
range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R5G5B5A1_UNORM_PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R5G5B5A1_UNORM_PACK16** = `5`

Red/green/blue/alpha channel data format with 5 bits of red, 6 bits of
green, 5 bits of blue and 1 bit of alpha, packed into 16 bits. Values
are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B5G5R5A1_UNORM_PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B5G5R5A1_UNORM_PACK16** = `6`

Blue/green/red/alpha channel data format with 5 bits of blue, 6 bits of
green, 5 bits of red and 1 bit of alpha, packed into 16 bits. Values are
in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A1R5G5B5_UNORM_PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A1R5G5B5_UNORM_PACK16** = `7`

Alpha/red/green/blue channel data format with 1 bit of alpha, 5 bits of
red, 6 bits of green and 5 bits of blue, packed into 16 bits. Values are
in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8_UNORM** = `8`

8-bit-per-channel unsigned floating-point red channel data format with
normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8_SNORM** = `9`

8-bit-per-channel signed floating-point red channel data format with
normalized value. Values are in the `[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8_USCALED** = `10`

8-bit-per-channel unsigned floating-point red channel data format with
scaled value (value is converted from integer to float). Values are in
the `[0.0, 255.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8_SSCALED** = `11`

8-bit-per-channel signed floating-point red channel data format with
scaled value (value is converted from integer to float). Values are in
the `[-127.0, 127.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8_UINT** = `12`

8-bit-per-channel unsigned integer red channel data format. Values are
in the `[0, 255]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8_SINT** = `13`

8-bit-per-channel signed integer red channel data format. Values are in
the `[-127, 127]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8_SRGB** = `14`

8-bit-per-channel unsigned floating-point red channel data format with
normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8_UNORM** = `15`

8-bit-per-channel unsigned floating-point red/green channel data format
with normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8_SNORM** = `16`

8-bit-per-channel signed floating-point red/green channel data format
with normalized value. Values are in the `[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8_USCALED** = `17`

8-bit-per-channel unsigned floating-point red/green channel data format
with scaled value (value is converted from integer to float). Values are
in the `[0.0, 255.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8_SSCALED** = `18`

8-bit-per-channel signed floating-point red/green channel data format
with scaled value (value is converted from integer to float). Values are
in the `[-127.0, 127.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8_UINT** = `19`

8-bit-per-channel unsigned integer red/green channel data format. Values
are in the `[0, 255]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8_SINT** = `20`

8-bit-per-channel signed integer red/green channel data format. Values
are in the `[-127, 127]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8_SRGB** = `21`

8-bit-per-channel unsigned floating-point red/green channel data format
with normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8_UNORM** = `22`

8-bit-per-channel unsigned floating-point red/green/blue channel data
format with normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8_SNORM** = `23`

8-bit-per-channel signed floating-point red/green/blue channel data
format with normalized value. Values are in the `[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8_USCALED** = `24`

8-bit-per-channel unsigned floating-point red/green/blue channel data
format with scaled value (value is converted from integer to float).
Values are in the `[0.0, 255.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8_SSCALED** = `25`

8-bit-per-channel signed floating-point red/green/blue channel data
format with scaled value (value is converted from integer to float).
Values are in the `[-127.0, 127.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8_UINT** = `26`

8-bit-per-channel unsigned integer red/green/blue channel data format.
Values are in the `[0, 255]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8_SINT** = `27`

8-bit-per-channel signed integer red/green/blue channel data format.
Values are in the `[-127, 127]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8_SRGB** = `28`

8-bit-per-channel unsigned floating-point red/green/blue channel data
format with normalized value and non-linear sRGB encoding. Values are in
the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8_UNORM** = `29`

8-bit-per-channel unsigned floating-point blue/green/red channel data
format with normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8_SNORM** = `30`

8-bit-per-channel signed floating-point blue/green/red channel data
format with normalized value. Values are in the `[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8_USCALED** = `31`

8-bit-per-channel unsigned floating-point blue/green/red channel data
format with scaled value (value is converted from integer to float).
Values are in the `[0.0, 255.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8_SSCALED** = `32`

8-bit-per-channel signed floating-point blue/green/red channel data
format with scaled value (value is converted from integer to float).
Values are in the `[-127.0, 127.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8_UINT** = `33`

8-bit-per-channel unsigned integer blue/green/red channel data format.
Values are in the `[0, 255]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8_SINT** = `34`

8-bit-per-channel signed integer blue/green/red channel data format.
Values are in the `[-127, 127]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8_SRGB** = `35`

8-bit-per-channel unsigned floating-point blue/green/red data format
with normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8A8_UNORM** = `36`

8-bit-per-channel unsigned floating-point red/green/blue/alpha channel
data format with normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8A8_SNORM** = `37`

8-bit-per-channel signed floating-point red/green/blue/alpha channel
data format with normalized value. Values are in the `[-1.0, 1.0]`
range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8A8_USCALED** = `38`

8-bit-per-channel unsigned floating-point red/green/blue/alpha channel
data format with scaled value (value is converted from integer to
float). Values are in the `[0.0, 255.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8A8_SSCALED** = `39`

8-bit-per-channel signed floating-point red/green/blue/alpha channel
data format with scaled value (value is converted from integer to
float). Values are in the `[-127.0, 127.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8A8_UINT** = `40`

8-bit-per-channel unsigned integer red/green/blue/alpha channel data
format. Values are in the `[0, 255]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8A8_SINT** = `41`

8-bit-per-channel signed integer red/green/blue/alpha channel data
format. Values are in the `[-127, 127]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R8G8B8A8_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R8G8B8A8_SRGB** = `42`

8-bit-per-channel unsigned floating-point red/green/blue/alpha channel
data format with normalized value and non-linear sRGB encoding. Values
are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8A8_UNORM** = `43`

8-bit-per-channel unsigned floating-point blue/green/red/alpha channel
data format with normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8A8_SNORM** = `44`

8-bit-per-channel signed floating-point blue/green/red/alpha channel
data format with normalized value. Values are in the `[-1.0, 1.0]`
range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8A8_USCALED** = `45`

8-bit-per-channel unsigned floating-point blue/green/red/alpha channel
data format with scaled value (value is converted from integer to
float). Values are in the `[0.0, 255.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8A8_SSCALED** = `46`

8-bit-per-channel signed floating-point blue/green/red/alpha channel
data format with scaled value (value is converted from integer to
float). Values are in the `[-127.0, 127.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8A8_UINT** = `47`

8-bit-per-channel unsigned integer blue/green/red/alpha channel data
format. Values are in the `[0, 255]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8A8_SINT** = `48`

8-bit-per-channel signed integer blue/green/red/alpha channel data
format. Values are in the `[-127, 127]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8A8_SRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8A8_SRGB** = `49`

8-bit-per-channel unsigned floating-point blue/green/red/alpha channel
data format with normalized value and non-linear sRGB encoding. Values
are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_UNORM_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A8B8G8R8_UNORM_PACK32** = `50`

8-bit-per-channel unsigned floating-point alpha/red/green/blue channel
data format with normalized value, packed in 32 bits. Values are in the
`[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_SNORM_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A8B8G8R8_SNORM_PACK32** = `51`

8-bit-per-channel signed floating-point alpha/red/green/blue channel
data format with normalized value, packed in 32 bits. Values are in the
`[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_USCALED_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A8B8G8R8_USCALED_PACK32** = `52`

8-bit-per-channel unsigned floating-point alpha/red/green/blue channel
data format with scaled value (value is converted from integer to
float), packed in 32 bits. Values are in the `[0.0, 255.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_SSCALED_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A8B8G8R8_SSCALED_PACK32** = `53`

8-bit-per-channel signed floating-point alpha/red/green/blue channel
data format with scaled value (value is converted from integer to
float), packed in 32 bits. Values are in the `[-127.0, 127.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_UINT_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A8B8G8R8_UINT_PACK32** = `54`

8-bit-per-channel unsigned integer alpha/red/green/blue channel data
format, packed in 32 bits. Values are in the `[0, 255]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_SINT_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A8B8G8R8_SINT_PACK32** = `55`

8-bit-per-channel signed integer alpha/red/green/blue channel data
format, packed in 32 bits. Values are in the `[-127, 127]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A8B8G8R8_SRGB_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A8B8G8R8_SRGB_PACK32** = `56`

8-bit-per-channel unsigned floating-point alpha/red/green/blue channel
data format with normalized value and non-linear sRGB encoding, packed
in 32 bits. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_UNORM_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2R10G10B10_UNORM_PACK32** = `57`

Unsigned floating-point alpha/red/green/blue channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of red, 10 bits of green and 10 bits of blue. Values are in the
`[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_SNORM_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2R10G10B10_SNORM_PACK32** = `58`

Signed floating-point alpha/red/green/blue channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of red, 10 bits of green and 10 bits of blue. Values are in the
`[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_USCALED_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2R10G10B10_USCALED_PACK32** = `59`

Unsigned floating-point alpha/red/green/blue channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of red, 10 bits of green and 10 bits of blue. Values are in the
`[0.0, 1023.0]` range for red/green/blue and `[0.0, 3.0]` for alpha.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_SSCALED_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2R10G10B10_SSCALED_PACK32** = `60`

Signed floating-point alpha/red/green/blue channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of red, 10 bits of green and 10 bits of blue. Values are in the
`[-511.0, 511.0]` range for red/green/blue and `[-1.0, 1.0]` for alpha.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_UINT_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2R10G10B10_UINT_PACK32** = `61`

Unsigned integer alpha/red/green/blue channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of red, 10 bits of green and 10 bits of blue. Values are in the
`[0, 1023]` range for red/green/blue and `[0, 3]` for alpha.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2R10G10B10_SINT_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2R10G10B10_SINT_PACK32** = `62`

Signed integer alpha/red/green/blue channel data format with normalized
value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of
red, 10 bits of green and 10 bits of blue. Values are in the
`[-511, 511]` range for red/green/blue and `[-1, 1]` for alpha.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_UNORM_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2B10G10R10_UNORM_PACK32** = `63`

Unsigned floating-point alpha/blue/green/red channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of blue, 10 bits of green and 10 bits of red. Values are in the
`[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_SNORM_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2B10G10R10_SNORM_PACK32** = `64`

Signed floating-point alpha/blue/green/red channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of blue, 10 bits of green and 10 bits of red. Values are in the
`[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_USCALED_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2B10G10R10_USCALED_PACK32** = `65`

Unsigned floating-point alpha/blue/green/red channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of blue, 10 bits of green and 10 bits of red. Values are in the
`[0.0, 1023.0]` range for blue/green/red and `[0.0, 3.0]` for alpha.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_SSCALED_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2B10G10R10_SSCALED_PACK32** = `66`

Signed floating-point alpha/blue/green/red channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of blue, 10 bits of green and 10 bits of red. Values are in the
`[-511.0, 511.0]` range for blue/green/red and `[-1.0, 1.0]` for alpha.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_UINT_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2B10G10R10_UINT_PACK32** = `67`

Unsigned integer alpha/blue/green/red channel data format with
normalized value, packed in 32 bits. Format contains 2 bits of alpha, 10
bits of blue, 10 bits of green and 10 bits of red. Values are in the
`[0, 1023]` range for blue/green/red and `[0, 3]` for alpha.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_A2B10G10R10_SINT_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_A2B10G10R10_SINT_PACK32** = `68`

Signed integer alpha/blue/green/red channel data format with normalized
value, packed in 32 bits. Format contains 2 bits of alpha, 10 bits of
blue, 10 bits of green and 10 bits of red. Values are in the
`[-511, 511]` range for blue/green/red and `[-1, 1]` for alpha.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16_UNORM** = `69`

16-bit-per-channel unsigned floating-point red channel data format with
normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16_SNORM** = `70`

16-bit-per-channel signed floating-point red channel data format with
normalized value. Values are in the `[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16_USCALED** = `71`

16-bit-per-channel unsigned floating-point red channel data format with
scaled value (value is converted from integer to float). Values are in
the `[0.0, 65535.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16_SSCALED** = `72`

16-bit-per-channel signed floating-point red channel data format with
scaled value (value is converted from integer to float). Values are in
the `[-32767.0, 32767.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16_UINT** = `73`

16-bit-per-channel unsigned integer red channel data format. Values are
in the `[0.0, 65535]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16_SINT** = `74`

16-bit-per-channel signed integer red channel data format. Values are in
the `[-32767, 32767]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16_SFLOAT** = `75`

16-bit-per-channel signed floating-point red channel data format with
the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16_UNORM** = `76`

16-bit-per-channel unsigned floating-point red/green channel data format
with normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16_SNORM** = `77`

16-bit-per-channel signed floating-point red/green channel data format
with normalized value. Values are in the `[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16_USCALED** = `78`

16-bit-per-channel unsigned floating-point red/green channel data format
with scaled value (value is converted from integer to float). Values are
in the `[0.0, 65535.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16_SSCALED** = `79`

16-bit-per-channel signed floating-point red/green channel data format
with scaled value (value is converted from integer to float). Values are
in the `[-32767.0, 32767.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16_UINT** = `80`

16-bit-per-channel unsigned integer red/green channel data format.
Values are in the `[0.0, 65535]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16_SINT** = `81`

16-bit-per-channel signed integer red/green channel data format. Values
are in the `[-32767, 32767]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16_SFLOAT** = `82`

16-bit-per-channel signed floating-point red/green channel data format
with the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16_UNORM** = `83`

16-bit-per-channel unsigned floating-point red/green/blue channel data
format with normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16_SNORM** = `84`

16-bit-per-channel signed floating-point red/green/blue channel data
format with normalized value. Values are in the `[-1.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16_USCALED** = `85`

16-bit-per-channel unsigned floating-point red/green/blue channel data
format with scaled value (value is converted from integer to float).
Values are in the `[0.0, 65535.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16_SSCALED** = `86`

16-bit-per-channel signed floating-point red/green/blue channel data
format with scaled value (value is converted from integer to float).
Values are in the `[-32767.0, 32767.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16_UINT** = `87`

16-bit-per-channel unsigned integer red/green/blue channel data format.
Values are in the `[0.0, 65535]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16_SINT** = `88`

16-bit-per-channel signed integer red/green/blue channel data format.
Values are in the `[-32767, 32767]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16_SFLOAT** = `89`

16-bit-per-channel signed floating-point red/green/blue channel data
format with the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16A16_UNORM** = `90`

16-bit-per-channel unsigned floating-point red/green/blue/alpha channel
data format with normalized value. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16A16_SNORM** = `91`

16-bit-per-channel signed floating-point red/green/blue/alpha channel
data format with normalized value. Values are in the `[-1.0, 1.0]`
range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_USCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16A16_USCALED** = `92`

16-bit-per-channel unsigned floating-point red/green/blue/alpha channel
data format with scaled value (value is converted from integer to
float). Values are in the `[0.0, 65535.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_SSCALED}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16A16_SSCALED** = `93`

16-bit-per-channel signed floating-point red/green/blue/alpha channel
data format with scaled value (value is converted from integer to
float). Values are in the `[-32767.0, 32767.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16A16_UINT** = `94`

16-bit-per-channel unsigned integer red/green/blue/alpha channel data
format. Values are in the `[0.0, 65535]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16A16_SINT** = `95`

16-bit-per-channel signed integer red/green/blue/alpha channel data
format. Values are in the `[-32767, 32767]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R16G16B16A16_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R16G16B16A16_SFLOAT** = `96`

16-bit-per-channel signed floating-point red/green/blue/alpha channel
data format with the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32_UINT** = `97`

32-bit-per-channel unsigned integer red channel data format. Values are
in the `[0, 2^32 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32_SINT** = `98`

32-bit-per-channel signed integer red channel data format. Values are in
the `[2^31 + 1, 2^31 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32_SFLOAT** = `99`

32-bit-per-channel signed floating-point red channel data format with
the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32G32_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32G32_UINT** = `100`

32-bit-per-channel unsigned integer red/green channel data format.
Values are in the `[0, 2^32 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32G32_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32G32_SINT** = `101`

32-bit-per-channel signed integer red/green channel data format. Values
are in the `[2^31 + 1, 2^31 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32G32_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32G32_SFLOAT** = `102`

32-bit-per-channel signed floating-point red/green channel data format
with the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32G32B32_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32G32B32_UINT** = `103`

32-bit-per-channel unsigned integer red/green/blue channel data format.
Values are in the `[0, 2^32 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32G32B32_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32G32B32_SINT** = `104`

32-bit-per-channel signed integer red/green/blue channel data format.
Values are in the `[2^31 + 1, 2^31 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32G32B32_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32G32B32_SFLOAT** = `105`

32-bit-per-channel signed floating-point red/green/blue channel data
format with the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32G32B32A32_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32G32B32A32_UINT** = `106`

32-bit-per-channel unsigned integer red/green/blue/alpha channel data
format. Values are in the `[0, 2^32 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32G32B32A32_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32G32B32A32_SINT** = `107`

32-bit-per-channel signed integer red/green/blue/alpha channel data
format. Values are in the `[2^31 + 1, 2^31 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R32G32B32A32_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R32G32B32A32_SFLOAT** = `108`

32-bit-per-channel signed floating-point red/green/blue/alpha channel
data format with the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64_UINT** = `109`

64-bit-per-channel unsigned integer red channel data format. Values are
in the `[0, 2^64 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64_SINT** = `110`

64-bit-per-channel signed integer red channel data format. Values are in
the `[2^63 + 1, 2^63 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64_SFLOAT** = `111`

64-bit-per-channel signed floating-point red channel data format with
the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64G64_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64G64_UINT** = `112`

64-bit-per-channel unsigned integer red/green channel data format.
Values are in the `[0, 2^64 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64G64_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64G64_SINT** = `113`

64-bit-per-channel signed integer red/green channel data format. Values
are in the `[2^63 + 1, 2^63 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64G64_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64G64_SFLOAT** = `114`

64-bit-per-channel signed floating-point red/green channel data format
with the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64G64B64_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64G64B64_UINT** = `115`

64-bit-per-channel unsigned integer red/green/blue channel data format.
Values are in the `[0, 2^64 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64G64B64_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64G64B64_SINT** = `116`

64-bit-per-channel signed integer red/green/blue channel data format.
Values are in the `[2^63 + 1, 2^63 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64G64B64_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64G64B64_SFLOAT** = `117`

64-bit-per-channel signed floating-point red/green/blue channel data
format with the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64G64B64A64_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64G64B64A64_UINT** = `118`

64-bit-per-channel unsigned integer red/green/blue/alpha channel data
format. Values are in the `[0, 2^64 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64G64B64A64_SINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64G64B64A64_SINT** = `119`

64-bit-per-channel signed integer red/green/blue/alpha channel data
format. Values are in the `[2^63 + 1, 2^63 - 1]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R64G64B64A64_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R64G64B64A64_SFLOAT** = `120`

64-bit-per-channel signed floating-point red/green/blue/alpha channel
data format with the value stored as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B10G11R11_UFLOAT_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B10G11R11_UFLOAT_PACK32** = `121`

Unsigned floating-point blue/green/red data format with the value stored
as-is, packed in 32 bits. The format\'s precision is 10 bits of blue
channel, 11 bits of green channel and 11 bits of red channel.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_E5B9G9R9_UFLOAT_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_E5B9G9R9_UFLOAT_PACK32** = `122`

Unsigned floating-point exposure/blue/green/red data format with the
value stored as-is, packed in 32 bits. The format\'s precision is 5 bits
of exposure, 9 bits of blue channel, 9 bits of green channel and 9 bits
of red channel.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_D16_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_D16_UNORM** = `123`

16-bit unsigned floating-point depth data format with normalized value.
Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_X8_D24_UNORM_PACK32}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_X8_D24_UNORM_PACK32** = `124`

24-bit unsigned floating-point depth data format with normalized value,
plus 8 unused bits, packed in 32 bits. Values for depth are in the
`[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_D32_SFLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_D32_SFLOAT** = `125`

32-bit signed floating-point depth data format with the value stored
as-is.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_S8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_S8_UINT** = `126`

8-bit unsigned integer stencil data format.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_D16_UNORM_S8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_D16_UNORM_S8_UINT** = `127`

16-bit unsigned floating-point depth data format with normalized value,
plus 8 bits of stencil in unsigned integer format. Values for depth are
in the `[0.0, 1.0]` range. Values for stencil are in the `[0, 255]`
range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_D24_UNORM_S8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_D24_UNORM_S8_UINT** = `128`

24-bit unsigned floating-point depth data format with normalized value,
plus 8 bits of stencil in unsigned integer format. Values for depth are
in the `[0.0, 1.0]` range. Values for stencil are in the `[0, 255]`
range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_D32_SFLOAT_S8_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_D32_SFLOAT_S8_UINT** = `129`

32-bit signed floating-point depth data format with the value stored
as-is, plus 8 bits of stencil in unsigned integer format. Values for
stencil are in the `[0, 255]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC1_RGB_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC1_RGB_UNORM_BLOCK** = `130`

VRAM-compressed unsigned red/green/blue channel data format with
normalized value. Values are in the `[0.0, 1.0]` range. The format\'s
precision is 5 bits of red channel, 6 bits of green channel and 5 bits
of blue channel. Using BC1 texture compression (also known as S3TC
DXT1).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC1_RGB_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC1_RGB_SRGB_BLOCK** = `131`

VRAM-compressed unsigned red/green/blue channel data format with
normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range. The format\'s precision is 5 bits of red channel, 6
bits of green channel and 5 bits of blue channel. Using BC1 texture
compression (also known as S3TC DXT1).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC1_RGBA_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC1_RGBA_UNORM_BLOCK** = `132`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value. Values are in the `[0.0, 1.0]` range. The format\'s
precision is 5 bits of red channel, 6 bits of green channel, 5 bits of
blue channel and 1 bit of alpha channel. Using BC1 texture compression
(also known as S3TC DXT1).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC1_RGBA_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC1_RGBA_SRGB_BLOCK** = `133`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range. The format\'s precision is 5 bits of red channel, 6
bits of green channel, 5 bits of blue channel and 1 bit of alpha
channel. Using BC1 texture compression (also known as S3TC DXT1).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC2_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC2_UNORM_BLOCK** = `134`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value. Values are in the `[0.0, 1.0]` range. The format\'s
precision is 5 bits of red channel, 6 bits of green channel, 5 bits of
blue channel and 4 bits of alpha channel. Using BC2 texture compression
(also known as S3TC DXT3).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC2_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC2_SRGB_BLOCK** = `135`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range. The format\'s precision is 5 bits of red channel, 6
bits of green channel, 5 bits of blue channel and 4 bits of alpha
channel. Using BC2 texture compression (also known as S3TC DXT3).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC3_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC3_UNORM_BLOCK** = `136`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value. Values are in the `[0.0, 1.0]` range. The format\'s
precision is 5 bits of red channel, 6 bits of green channel, 5 bits of
blue channel and 8 bits of alpha channel. Using BC3 texture compression
(also known as S3TC DXT5).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC3_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC3_SRGB_BLOCK** = `137`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range. The format\'s precision is 5 bits of red channel, 6
bits of green channel, 5 bits of blue channel and 8 bits of alpha
channel. Using BC3 texture compression (also known as S3TC DXT5).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC4_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC4_UNORM_BLOCK** = `138`

VRAM-compressed unsigned red channel data format with normalized value.
Values are in the `[0.0, 1.0]` range. The format\'s precision is 8 bits
of red channel. Using BC4 texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC4_SNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC4_SNORM_BLOCK** = `139`

VRAM-compressed signed red channel data format with normalized value.
Values are in the `[-1.0, 1.0]` range. The format\'s precision is 8 bits
of red channel. Using BC4 texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC5_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC5_UNORM_BLOCK** = `140`

VRAM-compressed unsigned red/green channel data format with normalized
value. Values are in the `[0.0, 1.0]` range. The format\'s precision is
8 bits of red channel and 8 bits of green channel. Using BC5 texture
compression (also known as S3TC RGTC).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC5_SNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC5_SNORM_BLOCK** = `141`

VRAM-compressed signed red/green channel data format with normalized
value. Values are in the `[-1.0, 1.0]` range. The format\'s precision is
8 bits of red channel and 8 bits of green channel. Using BC5 texture
compression (also known as S3TC RGTC).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC6H_UFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC6H_UFLOAT_BLOCK** = `142`

VRAM-compressed unsigned red/green/blue channel data format with the
floating-point value stored as-is. The format\'s precision is between 10
and 13 bits for the red/green/blue channels. Using BC6H texture
compression (also known as BPTC HDR).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC6H_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC6H_SFLOAT_BLOCK** = `143`

VRAM-compressed signed red/green/blue channel data format with the
floating-point value stored as-is. The format\'s precision is between 10
and 13 bits for the red/green/blue channels. Using BC6H texture
compression (also known as BPTC HDR).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC7_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC7_UNORM_BLOCK** = `144`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value. Values are in the `[0.0, 1.0]` range. The format\'s
precision is between 4 and 7 bits for the red/green/blue channels and
between 0 and 8 bits for the alpha channel. Also known as BPTC LDR.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_BC7_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_BC7_SRGB_BLOCK** = `145`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range. The format\'s precision is between 4 and 7 bits for
the red/green/blue channels and between 0 and 8 bits for the alpha
channel. Also known as BPTC LDR.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ETC2_R8G8B8_UNORM_BLOCK** = `146`

VRAM-compressed unsigned red/green/blue channel data format with
normalized value. Values are in the `[0.0, 1.0]` range. Using ETC2
texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ETC2_R8G8B8_SRGB_BLOCK** = `147`

VRAM-compressed unsigned red/green/blue channel data format with
normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range. Using ETC2 texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8A1_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ETC2_R8G8B8A1_UNORM_BLOCK** = `148`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value. Values are in the `[0.0, 1.0]` range. Red/green/blue
use 8 bit of precision each, with alpha using 1 bit of precision. Using
ETC2 texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8A1_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ETC2_R8G8B8A1_SRGB_BLOCK** = `149`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range. Red/green/blue use 8 bit of precision each, with
alpha using 1 bit of precision. Using ETC2 texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8A8_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ETC2_R8G8B8A8_UNORM_BLOCK** = `150`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value. Values are in the `[0.0, 1.0]` range. Red/green/blue
use 8 bits of precision each, with alpha using 8 bits of precision.
Using ETC2 texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ETC2_R8G8B8A8_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ETC2_R8G8B8A8_SRGB_BLOCK** = `151`

VRAM-compressed unsigned red/green/blue/alpha channel data format with
normalized value and non-linear sRGB encoding. Values are in the
`[0.0, 1.0]` range. Red/green/blue use 8 bits of precision each, with
alpha using 8 bits of precision. Using ETC2 texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_EAC_R11_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_EAC_R11_UNORM_BLOCK** = `152`

11-bit VRAM-compressed unsigned red channel data format with normalized
value. Values are in the `[0.0, 1.0]` range. Using ETC2 texture
compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_EAC_R11_SNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_EAC_R11_SNORM_BLOCK** = `153`

11-bit VRAM-compressed signed red channel data format with normalized
value. Values are in the `[-1.0, 1.0]` range. Using ETC2 texture
compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_EAC_R11G11_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_EAC_R11G11_UNORM_BLOCK** = `154`

11-bit VRAM-compressed unsigned red/green channel data format with
normalized value. Values are in the `[0.0, 1.0]` range. Using ETC2
texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_EAC_R11G11_SNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_EAC_R11G11_SNORM_BLOCK** = `155`

11-bit VRAM-compressed signed red/green channel data format with
normalized value. Values are in the `[-1.0, 1.0]` range. Using ETC2
texture compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_4x4_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_4x4_UNORM_BLOCK** = `156`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 4×4 blocks (highest quality). Values are in the
`[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_4x4_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_4x4_SRGB_BLOCK** = `157`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 4×4 blocks (highest
quality). Values are in the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x4_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_5x4_UNORM_BLOCK** = `158`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 5×4 blocks. Values are in the `[0.0, 1.0]` range. Using
ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x4_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_5x4_SRGB_BLOCK** = `159`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 5×4 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x5_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_5x5_UNORM_BLOCK** = `160`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 5×5 blocks. Values are in the `[0.0, 1.0]` range. Using
ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x5_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_5x5_SRGB_BLOCK** = `161`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 5×5 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x5_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_6x5_UNORM_BLOCK** = `162`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 6×5 blocks. Values are in the `[0.0, 1.0]` range. Using
ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x5_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_6x5_SRGB_BLOCK** = `163`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 6×5 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x6_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_6x6_UNORM_BLOCK** = `164`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 6×6 blocks. Values are in the `[0.0, 1.0]` range. Using
ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x6_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_6x6_SRGB_BLOCK** = `165`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 6×6 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x5_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_8x5_UNORM_BLOCK** = `166`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 8×5 blocks. Values are in the `[0.0, 1.0]` range. Using
ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x5_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_8x5_SRGB_BLOCK** = `167`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 8×5 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x6_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_8x6_UNORM_BLOCK** = `168`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 8×6 blocks. Values are in the `[0.0, 1.0]` range. Using
ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x6_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_8x6_SRGB_BLOCK** = `169`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 8×6 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x8_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_8x8_UNORM_BLOCK** = `170`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 8×8 blocks. Values are in the `[0.0, 1.0]` range. Using
ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x8_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_8x8_SRGB_BLOCK** = `171`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 8×8 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x5_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x5_UNORM_BLOCK** = `172`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 10×5 blocks. Values are in the `[0.0, 1.0]` range.
Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x5_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x5_SRGB_BLOCK** = `173`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 10×5 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x6_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x6_UNORM_BLOCK** = `174`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 10×6 blocks. Values are in the `[0.0, 1.0]` range.
Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x6_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x6_SRGB_BLOCK** = `175`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 10×6 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x8_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x8_UNORM_BLOCK** = `176`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 10×8 blocks. Values are in the `[0.0, 1.0]` range.
Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x8_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x8_SRGB_BLOCK** = `177`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 10×8 blocks. Values are in
the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x10_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x10_UNORM_BLOCK** = `178`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 10×10 blocks. Values are in the `[0.0, 1.0]` range.
Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x10_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x10_SRGB_BLOCK** = `179`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 10×10 blocks. Values are
in the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x10_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_12x10_UNORM_BLOCK** = `180`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 12×10 blocks. Values are in the `[0.0, 1.0]` range.
Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x10_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_12x10_SRGB_BLOCK** = `181`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 12×10 blocks. Values are
in the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x12_UNORM_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_12x12_UNORM_BLOCK** = `182`

VRAM-compressed unsigned floating-point data format with normalized
value, packed in 12 blocks (lowest quality). Values are in the
`[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x12_SRGB_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_12x12_SRGB_BLOCK** = `183`

VRAM-compressed unsigned floating-point data format with normalized
value and non-linear sRGB encoding, packed in 12 blocks (lowest
quality). Values are in the `[0.0, 1.0]` range. Using ASTC compression.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G8B8G8R8_422_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G8B8G8R8_422_UNORM** = `184`

8-bit-per-channel unsigned floating-point green/blue/red channel data
format with normalized value. Values are in the `[0.0, 1.0]` range. Blue
and red channel data is stored at halved horizontal resolution (i.e. 2
horizontally adjacent pixels will share the same value for the blue/red
channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B8G8R8G8_422_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B8G8R8G8_422_UNORM** = `185`

8-bit-per-channel unsigned floating-point blue/green/red channel data
format with normalized value. Values are in the `[0.0, 1.0]` range. Blue
and red channel data is stored at halved horizontal resolution (i.e. 2
horizontally adjacent pixels will share the same value for the blue/red
channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G8_B8_R8_3PLANE_420_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G8_B8_R8_3PLANE_420_UNORM** = `186`

8-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, stored across 3 separate planes (green + blue +
red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is
stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent
pixels will share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G8_B8R8_2PLANE_420_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G8_B8R8_2PLANE_420_UNORM** = `187`

8-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, stored across 2 separate planes (green +
blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel
data is stored at halved horizontal and vertical resolution (i.e. 2×2
adjacent pixels will share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G8_B8_R8_3PLANE_422_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G8_B8_R8_3PLANE_422_UNORM** = `188`

8-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, stored across 2 separate planes (green + blue +
red). Values are in the `[0.0, 1.0]` range. Blue and red channel data is
stored at halved horizontal resolution (i.e. 2 horizontally adjacent
pixels will share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G8_B8R8_2PLANE_422_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G8_B8R8_2PLANE_422_UNORM** = `189`

8-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, stored across 2 separate planes (green +
blue/red). Values are in the `[0.0, 1.0]` range. Blue and red channel
data is stored at halved horizontal resolution (i.e. 2 horizontally
adjacent pixels will share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G8_B8_R8_3PLANE_444_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G8_B8_R8_3PLANE_444_UNORM** = `190`

8-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, stored across 3 separate planes. Values are in
the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R10X6_UNORM_PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R10X6_UNORM_PACK16** = `191`

10-bit-per-channel unsigned floating-point red channel data with
normalized value, plus 6 unused bits, packed in 16 bits. Values are in
the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R10X6G10X6_UNORM_2PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R10X6G10X6_UNORM_2PACK16** = `192`

10-bit-per-channel unsigned floating-point red/green channel data with
normalized value, plus 6 unused bits after each channel, packed in 2×16
bits. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R10X6G10X6B10X6A10X6_UNORM_4PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R10X6G10X6B10X6A10X6_UNORM_4PACK16** = `193`

10-bit-per-channel unsigned floating-point red/green/blue/alpha channel
data with normalized value, plus 6 unused bits after each channel,
packed in 4×16 bits. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G10X6B10X6G10X6R10X6_422_UNORM_4PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G10X6B10X6G10X6R10X6_422_UNORM_4PACK16** =
`194`

10-bit-per-channel unsigned floating-point green/blue/green/red channel
data with normalized value, plus 6 unused bits after each channel,
packed in 4×16 bits. Values are in the `[0.0, 1.0]` range. Blue and red
channel data is stored at halved horizontal resolution (i.e. 2
horizontally adjacent pixels will share the same value for the blue/red
channel). The green channel is listed twice, but contains different
values to allow it to be represented at full resolution.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B10X6G10X6R10X6G10X6_422_UNORM_4PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B10X6G10X6R10X6G10X6_422_UNORM_4PACK16** =
`195`

10-bit-per-channel unsigned floating-point blue/green/red/green channel
data with normalized value, plus 6 unused bits after each channel,
packed in 4×16 bits. Values are in the `[0.0, 1.0]` range. Blue and red
channel data is stored at halved horizontal resolution (i.e. 2
horizontally adjacent pixels will share the same value for the blue/red
channel). The green channel is listed twice, but contains different
values to allow it to be represented at full resolution.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_420_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_420_UNORM_3PACK16** =
`196`

10-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 2 separate planes (green + blue + red).
Values are in the `[0.0, 1.0]` range. Blue and red channel data is
stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent
pixels will share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_420_UNORM_3PACK16** =
`197`

10-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 2 separate planes (green + blue/red). Values
are in the `[0.0, 1.0]` range. Blue and red channel data is stored at
halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will
share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_422_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_422_UNORM_3PACK16** =
`198`

10-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 3 separate planes (green + blue + red).
Values are in the `[0.0, 1.0]` range. Blue and red channel data is
stored at halved horizontal resolution (i.e. 2 horizontally adjacent
pixels will share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_422_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G10X6_B10X6R10X6_2PLANE_422_UNORM_3PACK16** =
`199`

10-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 3 separate planes (green + blue/red). Values
are in the `[0.0, 1.0]` range. Blue and red channel data is stored at
halved horizontal resolution (i.e. 2 horizontally adjacent pixels will
share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_444_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G10X6_B10X6_R10X6_3PLANE_444_UNORM_3PACK16** =
`200`

10-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 3 separate planes (green + blue + red).
Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R12X4_UNORM_PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R12X4_UNORM_PACK16** = `201`

12-bit-per-channel unsigned floating-point red channel data with
normalized value, plus 6 unused bits, packed in 16 bits. Values are in
the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R12X4G12X4_UNORM_2PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R12X4G12X4_UNORM_2PACK16** = `202`

12-bit-per-channel unsigned floating-point red/green channel data with
normalized value, plus 6 unused bits after each channel, packed in 2×16
bits. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_R12X4G12X4B12X4A12X4_UNORM_4PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_R12X4G12X4B12X4A12X4_UNORM_4PACK16** = `203`

12-bit-per-channel unsigned floating-point red/green/blue/alpha channel
data with normalized value, plus 6 unused bits after each channel,
packed in 4×16 bits. Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G12X4B12X4G12X4R12X4_422_UNORM_4PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G12X4B12X4G12X4R12X4_422_UNORM_4PACK16** =
`204`

12-bit-per-channel unsigned floating-point green/blue/green/red channel
data with normalized value, plus 6 unused bits after each channel,
packed in 4×16 bits. Values are in the `[0.0, 1.0]` range. Blue and red
channel data is stored at halved horizontal resolution (i.e. 2
horizontally adjacent pixels will share the same value for the blue/red
channel). The green channel is listed twice, but contains different
values to allow it to be represented at full resolution.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B12X4G12X4R12X4G12X4_422_UNORM_4PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B12X4G12X4R12X4G12X4_422_UNORM_4PACK16** =
`205`

12-bit-per-channel unsigned floating-point blue/green/red/green channel
data with normalized value, plus 6 unused bits after each channel,
packed in 4×16 bits. Values are in the `[0.0, 1.0]` range. Blue and red
channel data is stored at halved horizontal resolution (i.e. 2
horizontally adjacent pixels will share the same value for the blue/red
channel). The green channel is listed twice, but contains different
values to allow it to be represented at full resolution.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_420_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_420_UNORM_3PACK16** =
`206`

12-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 2 separate planes (green + blue + red).
Values are in the `[0.0, 1.0]` range. Blue and red channel data is
stored at halved horizontal and vertical resolution (i.e. 2×2 adjacent
pixels will share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_420_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_420_UNORM_3PACK16** =
`207`

12-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 2 separate planes (green + blue/red). Values
are in the `[0.0, 1.0]` range. Blue and red channel data is stored at
halved horizontal and vertical resolution (i.e. 2×2 adjacent pixels will
share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_422_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_422_UNORM_3PACK16** =
`208`

12-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 3 separate planes (green + blue + red).
Values are in the `[0.0, 1.0]` range. Blue and red channel data is
stored at halved horizontal resolution (i.e. 2 horizontally adjacent
pixels will share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_422_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G12X4_B12X4R12X4_2PLANE_422_UNORM_3PACK16** =
`209`

12-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 3 separate planes (green + blue/red). Values
are in the `[0.0, 1.0]` range. Blue and red channel data is stored at
halved horizontal resolution (i.e. 2 horizontally adjacent pixels will
share the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_444_UNORM_3PACK16}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G12X4_B12X4_R12X4_3PLANE_444_UNORM_3PACK16** =
`210`

12-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Packed in
3×16 bits and stored across 3 separate planes (green + blue + red).
Values are in the `[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G16B16G16R16_422_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G16B16G16R16_422_UNORM** = `211`

16-bit-per-channel unsigned floating-point green/blue/red channel data
format with normalized value. Values are in the `[0.0, 1.0]` range. Blue
and red channel data is stored at halved horizontal resolution (i.e. 2
horizontally adjacent pixels will share the same value for the blue/red
channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_B16G16R16G16_422_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_B16G16R16G16_422_UNORM** = `212`

16-bit-per-channel unsigned floating-point blue/green/red channel data
format with normalized value. Values are in the `[0.0, 1.0]` range. Blue
and red channel data is stored at halved horizontal resolution (i.e. 2
horizontally adjacent pixels will share the same value for the blue/red
channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G16_B16_R16_3PLANE_420_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G16_B16_R16_3PLANE_420_UNORM** = `213`

16-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Stored
across 2 separate planes (green + blue + red). Values are in the
`[0.0, 1.0]` range. Blue and red channel data is stored at halved
horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share
the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G16_B16R16_2PLANE_420_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G16_B16R16_2PLANE_420_UNORM** = `214`

16-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Stored
across 2 separate planes (green + blue/red). Values are in the
`[0.0, 1.0]` range. Blue and red channel data is stored at halved
horizontal and vertical resolution (i.e. 2×2 adjacent pixels will share
the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G16_B16_R16_3PLANE_422_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G16_B16_R16_3PLANE_422_UNORM** = `215`

16-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Stored
across 3 separate planes (green + blue + red). Values are in the
`[0.0, 1.0]` range. Blue and red channel data is stored at halved
horizontal resolution (i.e. 2 horizontally adjacent pixels will share
the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G16_B16R16_2PLANE_422_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G16_B16R16_2PLANE_422_UNORM** = `216`

16-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Stored
across 3 separate planes (green + blue/red). Values are in the
`[0.0, 1.0]` range. Blue and red channel data is stored at halved
horizontal resolution (i.e. 2 horizontally adjacent pixels will share
the same value for the blue/red channel).

:::: {#class_RenderingDevice_constant_DATA_FORMAT_G16_B16_R16_3PLANE_444_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_G16_B16_R16_3PLANE_444_UNORM** = `217`

16-bit-per-channel unsigned floating-point green/blue/red channel data
with normalized value, plus 6 unused bits after each channel. Stored
across 3 separate planes (green + blue + red). Values are in the
`[0.0, 1.0]` range.

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_4x4_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_4x4_SFLOAT_BLOCK** = `218`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x4_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_5x4_SFLOAT_BLOCK** = `219`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_5x5_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_5x5_SFLOAT_BLOCK** = `220`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x5_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_6x5_SFLOAT_BLOCK** = `221`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_6x6_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_6x6_SFLOAT_BLOCK** = `222`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x5_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_8x5_SFLOAT_BLOCK** = `223`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x6_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_8x6_SFLOAT_BLOCK** = `224`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_8x8_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_8x8_SFLOAT_BLOCK** = `225`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x5_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x5_SFLOAT_BLOCK** = `226`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x6_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x6_SFLOAT_BLOCK** = `227`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x8_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x8_SFLOAT_BLOCK** = `228`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_10x10_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_10x10_SFLOAT_BLOCK** = `229`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x10_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_12x10_SFLOAT_BLOCK** = `230`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_ASTC_12x12_SFLOAT_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_ASTC_12x12_SFLOAT_BLOCK** = `231`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DATA_FORMAT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} **DATA_FORMAT_MAX** = `232`

Represents the size of the
`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_BarrierMask}
::: rst-class
classref-enumeration
:::
::::

flags **BarrierMask**:
`🔗<enum_RenderingDevice_BarrierMask>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_BARRIER_MASK_VERTEX}
::: rst-class
classref-enumeration-constant
:::
::::

`BarrierMask<enum_RenderingDevice_BarrierMask>`{.interpreted-text
role="ref"} **BARRIER_MASK_VERTEX** = `1`

Vertex shader barrier mask.

:::: {#class_RenderingDevice_constant_BARRIER_MASK_FRAGMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`BarrierMask<enum_RenderingDevice_BarrierMask>`{.interpreted-text
role="ref"} **BARRIER_MASK_FRAGMENT** = `8`

Fragment shader barrier mask.

:::: {#class_RenderingDevice_constant_BARRIER_MASK_COMPUTE}
::: rst-class
classref-enumeration-constant
:::
::::

`BarrierMask<enum_RenderingDevice_BarrierMask>`{.interpreted-text
role="ref"} **BARRIER_MASK_COMPUTE** = `2`

Compute barrier mask.

:::: {#class_RenderingDevice_constant_BARRIER_MASK_TRANSFER}
::: rst-class
classref-enumeration-constant
:::
::::

`BarrierMask<enum_RenderingDevice_BarrierMask>`{.interpreted-text
role="ref"} **BARRIER_MASK_TRANSFER** = `4`

Transfer barrier mask.

:::: {#class_RenderingDevice_constant_BARRIER_MASK_RASTER}
::: rst-class
classref-enumeration-constant
:::
::::

`BarrierMask<enum_RenderingDevice_BarrierMask>`{.interpreted-text
role="ref"} **BARRIER_MASK_RASTER** = `9`

Raster barrier mask (vertex and fragment). Equivalent to
`BARRIER_MASK_VERTEX | BARRIER_MASK_FRAGMENT`.

:::: {#class_RenderingDevice_constant_BARRIER_MASK_ALL_BARRIERS}
::: rst-class
classref-enumeration-constant
:::
::::

`BarrierMask<enum_RenderingDevice_BarrierMask>`{.interpreted-text
role="ref"} **BARRIER_MASK_ALL_BARRIERS** = `32767`

Barrier mask for all types (vertex, fragment, compute, transfer).

:::: {#class_RenderingDevice_constant_BARRIER_MASK_NO_BARRIER}
::: rst-class
classref-enumeration-constant
:::
::::

`BarrierMask<enum_RenderingDevice_BarrierMask>`{.interpreted-text
role="ref"} **BARRIER_MASK_NO_BARRIER** = `32768`

No barrier for any type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_TextureType}
::: rst-class
classref-enumeration
:::
::::

enum **TextureType**:
`🔗<enum_RenderingDevice_TextureType>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_TEXTURE_TYPE_1D}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_1D** = `0`

1-dimensional texture.

:::: {#class_RenderingDevice_constant_TEXTURE_TYPE_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_2D** = `1`

2-dimensional texture.

:::: {#class_RenderingDevice_constant_TEXTURE_TYPE_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_3D** = `2`

3-dimensional texture.

:::: {#class_RenderingDevice_constant_TEXTURE_TYPE_CUBE}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_CUBE** = `3`

`Cubemap<class_Cubemap>`{.interpreted-text role="ref"} texture.

:::: {#class_RenderingDevice_constant_TEXTURE_TYPE_1D_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_1D_ARRAY** = `4`

Array of 1-dimensional textures.

:::: {#class_RenderingDevice_constant_TEXTURE_TYPE_2D_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_2D_ARRAY** = `5`

Array of 2-dimensional textures.

:::: {#class_RenderingDevice_constant_TEXTURE_TYPE_CUBE_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_CUBE_ARRAY** = `6`

Array of `Cubemap<class_Cubemap>`{.interpreted-text role="ref"}
textures.

:::: {#class_RenderingDevice_constant_TEXTURE_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} **TEXTURE_TYPE_MAX** = `7`

Represents the size of the
`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_TextureSamples}
::: rst-class
classref-enumeration
:::
::::

enum **TextureSamples**:
`🔗<enum_RenderingDevice_TextureSamples>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_TEXTURE_SAMPLES_1}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **TEXTURE_SAMPLES_1** = `0`

Perform 1 texture sample (this is the fastest but lowest-quality for
antialiasing).

:::: {#class_RenderingDevice_constant_TEXTURE_SAMPLES_2}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **TEXTURE_SAMPLES_2** = `1`

Perform 2 texture samples.

:::: {#class_RenderingDevice_constant_TEXTURE_SAMPLES_4}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **TEXTURE_SAMPLES_4** = `2`

Perform 4 texture samples.

:::: {#class_RenderingDevice_constant_TEXTURE_SAMPLES_8}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **TEXTURE_SAMPLES_8** = `3`

Perform 8 texture samples. Not supported on mobile GPUs (including Apple
Silicon).

:::: {#class_RenderingDevice_constant_TEXTURE_SAMPLES_16}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **TEXTURE_SAMPLES_16** = `4`

Perform 16 texture samples. Not supported on mobile GPUs and many
desktop GPUs.

:::: {#class_RenderingDevice_constant_TEXTURE_SAMPLES_32}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **TEXTURE_SAMPLES_32** = `5`

Perform 32 texture samples. Not supported on most GPUs.

:::: {#class_RenderingDevice_constant_TEXTURE_SAMPLES_64}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **TEXTURE_SAMPLES_64** = `6`

Perform 64 texture samples (this is the slowest but highest-quality for
antialiasing). Not supported on most GPUs.

:::: {#class_RenderingDevice_constant_TEXTURE_SAMPLES_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **TEXTURE_SAMPLES_MAX** = `7`

Represents the size of the
`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_TextureUsageBits}
::: rst-class
classref-enumeration
:::
::::

flags **TextureUsageBits**:
`🔗<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_SAMPLING_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_SAMPLING_BIT** = `1`

Texture can be sampled.

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_COLOR_ATTACHMENT_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_COLOR_ATTACHMENT_BIT** = `2`

Texture can be used as a color attachment in a framebuffer.

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_DEPTH_STENCIL_ATTACHMENT_BIT** = `4`

Texture can be used as a depth/stencil attachment in a framebuffer.

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_STORAGE_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_STORAGE_BIT** = `8`

Texture can be used as a [storage
image](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#descriptorsets-storageimage).

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_STORAGE_ATOMIC_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_STORAGE_ATOMIC_BIT** = `16`

Texture can be used as a [storage
image](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#descriptorsets-storageimage)
with support for atomic operations.

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_CPU_READ_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_CPU_READ_BIT** = `32`

Texture can be read back on the CPU using
`texture_get_data()<class_RenderingDevice_method_texture_get_data>`{.interpreted-text
role="ref"} faster than without this bit, since it is always kept in the
system memory.

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_CAN_UPDATE_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_CAN_UPDATE_BIT** = `64`

Texture can be updated using
`texture_update()<class_RenderingDevice_method_texture_update>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_FROM_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_CAN_COPY_FROM_BIT** = `128`

Texture can be a source for
`texture_copy()<class_RenderingDevice_method_texture_copy>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_TO_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_CAN_COPY_TO_BIT** = `256`

Texture can be a destination for
`texture_copy()<class_RenderingDevice_method_texture_copy>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_TEXTURE_USAGE_INPUT_ATTACHMENT_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"} **TEXTURE_USAGE_INPUT_ATTACHMENT_BIT** = `512`

Texture can be used as a [input
attachment](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#descriptorsets-inputattachment)
in a framebuffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_TextureSwizzle}
::: rst-class
classref-enumeration
:::
::::

enum **TextureSwizzle**:
`🔗<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_TEXTURE_SWIZZLE_IDENTITY}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **TEXTURE_SWIZZLE_IDENTITY** = `0`

Return the sampled value as-is.

:::: {#class_RenderingDevice_constant_TEXTURE_SWIZZLE_ZERO}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **TEXTURE_SWIZZLE_ZERO** = `1`

Always return `0.0` when sampling.

:::: {#class_RenderingDevice_constant_TEXTURE_SWIZZLE_ONE}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **TEXTURE_SWIZZLE_ONE** = `2`

Always return `1.0` when sampling.

:::: {#class_RenderingDevice_constant_TEXTURE_SWIZZLE_R}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **TEXTURE_SWIZZLE_R** = `3`

Sample the red color channel.

:::: {#class_RenderingDevice_constant_TEXTURE_SWIZZLE_G}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **TEXTURE_SWIZZLE_G** = `4`

Sample the green color channel.

:::: {#class_RenderingDevice_constant_TEXTURE_SWIZZLE_B}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **TEXTURE_SWIZZLE_B** = `5`

Sample the blue color channel.

:::: {#class_RenderingDevice_constant_TEXTURE_SWIZZLE_A}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **TEXTURE_SWIZZLE_A** = `6`

Sample the alpha channel.

:::: {#class_RenderingDevice_constant_TEXTURE_SWIZZLE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} **TEXTURE_SWIZZLE_MAX** = `7`

Represents the size of the
`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_TextureSliceType}
::: rst-class
classref-enumeration
:::
::::

enum **TextureSliceType**:
`🔗<enum_RenderingDevice_TextureSliceType>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_TEXTURE_SLICE_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSliceType<enum_RenderingDevice_TextureSliceType>`{.interpreted-text
role="ref"} **TEXTURE_SLICE_2D** = `0`

2-dimensional texture slice.

:::: {#class_RenderingDevice_constant_TEXTURE_SLICE_CUBEMAP}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSliceType<enum_RenderingDevice_TextureSliceType>`{.interpreted-text
role="ref"} **TEXTURE_SLICE_CUBEMAP** = `1`

Cubemap texture slice.

:::: {#class_RenderingDevice_constant_TEXTURE_SLICE_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSliceType<enum_RenderingDevice_TextureSliceType>`{.interpreted-text
role="ref"} **TEXTURE_SLICE_3D** = `2`

3-dimensional texture slice.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_SamplerFilter}
::: rst-class
classref-enumeration
:::
::::

enum **SamplerFilter**:
`🔗<enum_RenderingDevice_SamplerFilter>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_SAMPLER_FILTER_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
role="ref"} **SAMPLER_FILTER_NEAREST** = `0`

Nearest-neighbor sampler filtering. Sampling at higher resolutions than
the source will result in a pixelated look.

:::: {#class_RenderingDevice_constant_SAMPLER_FILTER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
role="ref"} **SAMPLER_FILTER_LINEAR** = `1`

Bilinear sampler filtering. Sampling at higher resolutions than the
source will result in a blurry look.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_SamplerRepeatMode}
::: rst-class
classref-enumeration
:::
::::

enum **SamplerRepeatMode**:
`🔗<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_REPEAT}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} **SAMPLER_REPEAT_MODE_REPEAT** = `0`

Sample with repeating enabled.

:::: {#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_MIRRORED_REPEAT}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} **SAMPLER_REPEAT_MODE_MIRRORED_REPEAT** = `1`

Sample with mirrored repeating enabled. When sampling outside the
`[0.0, 1.0]` range, return a mirrored version of the sampler. This
mirrored version is mirrored again if sampling further away, with the
pattern repeating indefinitely.

:::: {#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_EDGE}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} **SAMPLER_REPEAT_MODE_CLAMP_TO_EDGE** = `2`

Sample with repeating disabled. When sampling outside the `[0.0, 1.0]`
range, return the color of the last pixel on the edge.

:::: {#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} **SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER** = `3`

Sample with repeating disabled. When sampling outside the `[0.0, 1.0]`
range, return the specified
`RDSamplerState.border_color<class_RDSamplerState_property_border_color>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_MIRROR_CLAMP_TO_EDGE}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} **SAMPLER_REPEAT_MODE_MIRROR_CLAMP_TO_EDGE** = `4`

Sample with mirrored repeating enabled, but only once. When sampling in
the `[-1.0, 0.0]` range, return a mirrored version of the sampler. When
sampling outside the `[-1.0, 1.0]` range, return the color of the last
pixel on the edge.

:::: {#class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} **SAMPLER_REPEAT_MODE_MAX** = `5`

Represents the size of the
`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_SamplerBorderColor}
::: rst-class
classref-enumeration
:::
::::

enum **SamplerBorderColor**:
`🔗<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_FLOAT_TRANSPARENT_BLACK}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"} **SAMPLER_BORDER_COLOR_FLOAT_TRANSPARENT_BLACK** = `0`

Return a floating-point transparent black color when sampling outside
the `[0.0, 1.0]` range. Only effective if the sampler repeat mode is
`SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER<class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_INT_TRANSPARENT_BLACK}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"} **SAMPLER_BORDER_COLOR_INT_TRANSPARENT_BLACK** = `1`

Return an integer transparent black color when sampling outside the
`[0.0, 1.0]` range. Only effective if the sampler repeat mode is
`SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER<class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_BLACK}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"} **SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_BLACK** = `2`

Return a floating-point opaque black color when sampling outside the
`[0.0, 1.0]` range. Only effective if the sampler repeat mode is
`SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER<class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_INT_OPAQUE_BLACK}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"} **SAMPLER_BORDER_COLOR_INT_OPAQUE_BLACK** = `3`

Return an integer opaque black color when sampling outside the
`[0.0, 1.0]` range. Only effective if the sampler repeat mode is
`SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER<class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_WHITE}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"} **SAMPLER_BORDER_COLOR_FLOAT_OPAQUE_WHITE** = `4`

Return a floating-point opaque white color when sampling outside the
`[0.0, 1.0]` range. Only effective if the sampler repeat mode is
`SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER<class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_INT_OPAQUE_WHITE}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"} **SAMPLER_BORDER_COLOR_INT_OPAQUE_WHITE** = `5`

Return an integer opaque white color when sampling outside the
`[0.0, 1.0]` range. Only effective if the sampler repeat mode is
`SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER<class_RenderingDevice_constant_SAMPLER_REPEAT_MODE_CLAMP_TO_BORDER>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_SAMPLER_BORDER_COLOR_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"} **SAMPLER_BORDER_COLOR_MAX** = `6`

Represents the size of the
`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_VertexFrequency}
::: rst-class
classref-enumeration
:::
::::

enum **VertexFrequency**:
`🔗<enum_RenderingDevice_VertexFrequency>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_VERTEX_FREQUENCY_VERTEX}
::: rst-class
classref-enumeration-constant
:::
::::

`VertexFrequency<enum_RenderingDevice_VertexFrequency>`{.interpreted-text
role="ref"} **VERTEX_FREQUENCY_VERTEX** = `0`

Vertex attribute addressing is a function of the vertex. This is used to
specify the rate at which vertex attributes are pulled from buffers.

:::: {#class_RenderingDevice_constant_VERTEX_FREQUENCY_INSTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`VertexFrequency<enum_RenderingDevice_VertexFrequency>`{.interpreted-text
role="ref"} **VERTEX_FREQUENCY_INSTANCE** = `1`

Vertex attribute addressing is a function of the instance index. This is
used to specify the rate at which vertex attributes are pulled from
buffers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_IndexBufferFormat}
::: rst-class
classref-enumeration
:::
::::

enum **IndexBufferFormat**:
`🔗<enum_RenderingDevice_IndexBufferFormat>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_INDEX_BUFFER_FORMAT_UINT16}
::: rst-class
classref-enumeration-constant
:::
::::

`IndexBufferFormat<enum_RenderingDevice_IndexBufferFormat>`{.interpreted-text
role="ref"} **INDEX_BUFFER_FORMAT_UINT16** = `0`

Index buffer in 16-bit unsigned integer format. This limits the maximum
index that can be specified to `65535`.

:::: {#class_RenderingDevice_constant_INDEX_BUFFER_FORMAT_UINT32}
::: rst-class
classref-enumeration-constant
:::
::::

`IndexBufferFormat<enum_RenderingDevice_IndexBufferFormat>`{.interpreted-text
role="ref"} **INDEX_BUFFER_FORMAT_UINT32** = `1`

Index buffer in 32-bit unsigned integer format. This limits the maximum
index that can be specified to `4294967295`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_StorageBufferUsage}
::: rst-class
classref-enumeration
:::
::::

flags **StorageBufferUsage**:
`🔗<enum_RenderingDevice_StorageBufferUsage>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT}
::: rst-class
classref-enumeration-constant
:::
::::

`StorageBufferUsage<enum_RenderingDevice_StorageBufferUsage>`{.interpreted-text
role="ref"} **STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_BufferCreationBits}
::: rst-class
classref-enumeration
:::
::::

flags **BufferCreationBits**:
`🔗<enum_RenderingDevice_BufferCreationBits>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_BUFFER_CREATION_DEVICE_ADDRESS_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`BufferCreationBits<enum_RenderingDevice_BufferCreationBits>`{.interpreted-text
role="ref"} **BUFFER_CREATION_DEVICE_ADDRESS_BIT** = `1`

Optionally, set this flag if you wish to use
`buffer_get_device_address()<class_RenderingDevice_method_buffer_get_device_address>`{.interpreted-text
role="ref"} functionality. You must first check the GPU supports it:

:::: tabs
::: code-tab
gdscript

rd = RenderingServer.get_rendering_device()

if rd.has_feature(RenderingDevice.SUPPORTS_BUFFER_DEVICE_ADDRESS):

:   storage_buffer = rd.storage_buffer_create(bytes.size(), bytes,
    RenderingDevice.STORAGE_BUFFER_USAGE_SHADER_DEVICE_ADDRESS)
    storage_buffer_address =
    rd.buffer_get_device_address(storage_buffer)
:::
::::

:::: {#class_RenderingDevice_constant_BUFFER_CREATION_AS_STORAGE_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`BufferCreationBits<enum_RenderingDevice_BufferCreationBits>`{.interpreted-text
role="ref"} **BUFFER_CREATION_AS_STORAGE_BIT** = `2`

Set this flag so that it is created as storage. This is useful if
Compute Shaders need access (for reading or writing) to the buffer, e.g.
skeletal animations are processed in Compute Shaders which need access
to vertex buffers, to be later consumed by vertex shaders as part of the
regular rasterization pipeline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_UniformType}
::: rst-class
classref-enumeration
:::
::::

enum **UniformType**:
`🔗<enum_RenderingDevice_UniformType>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_SAMPLER}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_SAMPLER** = `0`

Sampler uniform.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_SAMPLER_WITH_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_SAMPLER_WITH_TEXTURE** = `1`

Sampler uniform with a texture.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_TEXTURE** = `2`

Texture uniform.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_IMAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_IMAGE** = `3`

Image uniform.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_TEXTURE_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_TEXTURE_BUFFER** = `4`

Texture buffer uniform.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_SAMPLER_WITH_TEXTURE_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_SAMPLER_WITH_TEXTURE_BUFFER** = `5`

Sampler uniform with a texture buffer.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_IMAGE_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_IMAGE_BUFFER** = `6`

Image buffer uniform.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_UNIFORM_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_UNIFORM_BUFFER** = `7`

Uniform buffer uniform.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_STORAGE_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_STORAGE_BUFFER** = `8`

[Storage buffer](https://vkguide.dev/docs/chapter-4/storage_buffers/)
uniform.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_INPUT_ATTACHMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_INPUT_ATTACHMENT** = `9`

Input attachment uniform.

:::: {#class_RenderingDevice_constant_UNIFORM_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} **UNIFORM_TYPE_MAX** = `10`

Represents the size of the
`UniformType<enum_RenderingDevice_UniformType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_RenderPrimitive}
::: rst-class
classref-enumeration
:::
::::

enum **RenderPrimitive**:
`🔗<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_POINTS}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_POINTS** = `0`

Point rendering primitive (with constant size, regardless of distance
from camera).

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_LINES}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_LINES** = `1`

Line list rendering primitive. Lines are drawn separated from each
other.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_LINES_WITH_ADJACENCY}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_LINES_WITH_ADJACENCY** = `2`

[Line list rendering primitive with
adjacency.](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#drawing-line-lists-with-adjacency)

\*\*Note:\*\* Adjacency is only useful with geometry shaders, which
Godot does not expose.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_LINESTRIPS}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_LINESTRIPS** = `3`

Line strip rendering primitive. Lines drawn are connected to the
previous vertex.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_LINESTRIPS_WITH_ADJACENCY}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_LINESTRIPS_WITH_ADJACENCY** = `4`

[Line strip rendering primitive with
adjacency.](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#drawing-line-strips-with-adjacency)

\*\*Note:\*\* Adjacency is only useful with geometry shaders, which
Godot does not expose.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLES}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_TRIANGLES** = `5`

Triangle list rendering primitive. Triangles are drawn separated from
each other.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLES_WITH_ADJACENCY}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_TRIANGLES_WITH_ADJACENCY** = `6`

[Triangle list rendering primitive with
adjacency.](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#drawing-triangle-lists-with-adjacency)

\*\*Note:\*\* Adjacency is only useful with geometry shaders, which
Godot does not expose.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLE_STRIPS}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_TRIANGLE_STRIPS** = `7`

Triangle strip rendering primitive. Triangles drawn are connected to the
previous triangle.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_AJACENCY}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_AJACENCY** = `8`

[Triangle strip rendering primitive with
adjacency.](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#drawing-triangle-strips-with-adjacency)

\*\*Note:\*\* Adjacency is only useful with geometry shaders, which
Godot does not expose.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_RESTART_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_TRIANGLE_STRIPS_WITH_RESTART_INDEX** =
`9`

Triangle strip rendering primitive with *primitive restart* enabled.
Triangles drawn are connected to the previous triangle, but a primitive
restart index can be specified before drawing to create a second
triangle strip after the specified index.

\*\*Note:\*\* Only compatible with indexed draws.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_TESSELATION_PATCH}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_TESSELATION_PATCH** = `10`

Tessellation patch rendering primitive. Only useful with tessellation
shaders, which can be used to deform these patches.

:::: {#class_RenderingDevice_constant_RENDER_PRIMITIVE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} **RENDER_PRIMITIVE_MAX** = `11`

Represents the size of the
`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_PolygonCullMode}
::: rst-class
classref-enumeration
:::
::::

enum **PolygonCullMode**:
`🔗<enum_RenderingDevice_PolygonCullMode>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_POLYGON_CULL_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`PolygonCullMode<enum_RenderingDevice_PolygonCullMode>`{.interpreted-text
role="ref"} **POLYGON_CULL_DISABLED** = `0`

Do not use polygon front face or backface culling.

:::: {#class_RenderingDevice_constant_POLYGON_CULL_FRONT}
::: rst-class
classref-enumeration-constant
:::
::::

`PolygonCullMode<enum_RenderingDevice_PolygonCullMode>`{.interpreted-text
role="ref"} **POLYGON_CULL_FRONT** = `1`

Use polygon frontface culling (faces pointing towards the camera are
hidden).

:::: {#class_RenderingDevice_constant_POLYGON_CULL_BACK}
::: rst-class
classref-enumeration-constant
:::
::::

`PolygonCullMode<enum_RenderingDevice_PolygonCullMode>`{.interpreted-text
role="ref"} **POLYGON_CULL_BACK** = `2`

Use polygon backface culling (faces pointing away from the camera are
hidden).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_PolygonFrontFace}
::: rst-class
classref-enumeration
:::
::::

enum **PolygonFrontFace**:
`🔗<enum_RenderingDevice_PolygonFrontFace>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_POLYGON_FRONT_FACE_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`PolygonFrontFace<enum_RenderingDevice_PolygonFrontFace>`{.interpreted-text
role="ref"} **POLYGON_FRONT_FACE_CLOCKWISE** = `0`

Clockwise winding order to determine which face of a polygon is its
front face.

:::: {#class_RenderingDevice_constant_POLYGON_FRONT_FACE_COUNTER_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`PolygonFrontFace<enum_RenderingDevice_PolygonFrontFace>`{.interpreted-text
role="ref"} **POLYGON_FRONT_FACE_COUNTER_CLOCKWISE** = `1`

Counter-clockwise winding order to determine which face of a polygon is
its front face.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_StencilOperation}
::: rst-class
classref-enumeration
:::
::::

enum **StencilOperation**:
`🔗<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_STENCIL_OP_KEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **STENCIL_OP_KEEP** = `0`

Keep the current stencil value.

:::: {#class_RenderingDevice_constant_STENCIL_OP_ZERO}
::: rst-class
classref-enumeration-constant
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **STENCIL_OP_ZERO** = `1`

Set the stencil value to `0`.

:::: {#class_RenderingDevice_constant_STENCIL_OP_REPLACE}
::: rst-class
classref-enumeration-constant
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **STENCIL_OP_REPLACE** = `2`

Replace the existing stencil value with the new one.

:::: {#class_RenderingDevice_constant_STENCIL_OP_INCREMENT_AND_CLAMP}
::: rst-class
classref-enumeration-constant
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **STENCIL_OP_INCREMENT_AND_CLAMP** = `3`

Increment the existing stencil value and clamp to the maximum
representable unsigned value if reached. Stencil bits are considered as
an unsigned integer.

:::: {#class_RenderingDevice_constant_STENCIL_OP_DECREMENT_AND_CLAMP}
::: rst-class
classref-enumeration-constant
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **STENCIL_OP_DECREMENT_AND_CLAMP** = `4`

Decrement the existing stencil value and clamp to the minimum value if
reached. Stencil bits are considered as an unsigned integer.

:::: {#class_RenderingDevice_constant_STENCIL_OP_INVERT}
::: rst-class
classref-enumeration-constant
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **STENCIL_OP_INVERT** = `5`

Bitwise-invert the existing stencil value.

:::: {#class_RenderingDevice_constant_STENCIL_OP_INCREMENT_AND_WRAP}
::: rst-class
classref-enumeration-constant
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **STENCIL_OP_INCREMENT_AND_WRAP** = `6`

Increment the stencil value and wrap around to `0` if reaching the
maximum representable unsigned. Stencil bits are considered as an
unsigned integer.

:::: {#class_RenderingDevice_constant_STENCIL_OP_DECREMENT_AND_WRAP}
::: rst-class
classref-enumeration-constant
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **STENCIL_OP_DECREMENT_AND_WRAP** = `7`

Decrement the stencil value and wrap around to the maximum representable
unsigned if reaching the minimum. Stencil bits are considered as an
unsigned integer.

:::: {#class_RenderingDevice_constant_STENCIL_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **STENCIL_OP_MAX** = `8`

Represents the size of the
`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_CompareOperator}
::: rst-class
classref-enumeration
:::
::::

enum **CompareOperator**:
`🔗<enum_RenderingDevice_CompareOperator>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_COMPARE_OP_NEVER}
::: rst-class
classref-enumeration-constant
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **COMPARE_OP_NEVER** = `0`

\"Never\" comparison (opposite of
`COMPARE_OP_ALWAYS<class_RenderingDevice_constant_COMPARE_OP_ALWAYS>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_COMPARE_OP_LESS}
::: rst-class
classref-enumeration-constant
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **COMPARE_OP_LESS** = `1`

\"Less than\" comparison.

:::: {#class_RenderingDevice_constant_COMPARE_OP_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **COMPARE_OP_EQUAL** = `2`

\"Equal\" comparison.

:::: {#class_RenderingDevice_constant_COMPARE_OP_LESS_OR_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **COMPARE_OP_LESS_OR_EQUAL** = `3`

\"Less than or equal\" comparison.

:::: {#class_RenderingDevice_constant_COMPARE_OP_GREATER}
::: rst-class
classref-enumeration-constant
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **COMPARE_OP_GREATER** = `4`

\"Greater than\" comparison.

:::: {#class_RenderingDevice_constant_COMPARE_OP_NOT_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **COMPARE_OP_NOT_EQUAL** = `5`

\"Not equal\" comparison.

:::: {#class_RenderingDevice_constant_COMPARE_OP_GREATER_OR_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **COMPARE_OP_GREATER_OR_EQUAL** = `6`

\"Greater than or equal\" comparison.

:::: {#class_RenderingDevice_constant_COMPARE_OP_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **COMPARE_OP_ALWAYS** = `7`

\"Always\" comparison (opposite of
`COMPARE_OP_NEVER<class_RenderingDevice_constant_COMPARE_OP_NEVER>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_COMPARE_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **COMPARE_OP_MAX** = `8`

Represents the size of the
`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_LogicOperation}
::: rst-class
classref-enumeration
:::
::::

enum **LogicOperation**:
`🔗<enum_RenderingDevice_LogicOperation>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_LOGIC_OP_CLEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_CLEAR** = `0`

Clear logic operation (result is always `0`). See also
`LOGIC_OP_SET<class_RenderingDevice_constant_LOGIC_OP_SET>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_LOGIC_OP_AND}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_AND** = `1`

AND logic operation.

:::: {#class_RenderingDevice_constant_LOGIC_OP_AND_REVERSE}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_AND_REVERSE** = `2`

AND logic operation with the *destination* operand being inverted. See
also
`LOGIC_OP_AND_INVERTED<class_RenderingDevice_constant_LOGIC_OP_AND_INVERTED>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_LOGIC_OP_COPY}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_COPY** = `3`

Copy logic operation (keeps the *source* value as-is). See also
`LOGIC_OP_COPY_INVERTED<class_RenderingDevice_constant_LOGIC_OP_COPY_INVERTED>`{.interpreted-text
role="ref"} and
`LOGIC_OP_NO_OP<class_RenderingDevice_constant_LOGIC_OP_NO_OP>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_LOGIC_OP_AND_INVERTED}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_AND_INVERTED** = `4`

AND logic operation with the *source* operand being inverted. See also
`LOGIC_OP_AND_REVERSE<class_RenderingDevice_constant_LOGIC_OP_AND_REVERSE>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_LOGIC_OP_NO_OP}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_NO_OP** = `5`

No-op logic operation (keeps the *destination* value as-is). See also
`LOGIC_OP_COPY<class_RenderingDevice_constant_LOGIC_OP_COPY>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_LOGIC_OP_XOR}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_XOR** = `6`

Exclusive or (XOR) logic operation.

:::: {#class_RenderingDevice_constant_LOGIC_OP_OR}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_OR** = `7`

OR logic operation.

:::: {#class_RenderingDevice_constant_LOGIC_OP_NOR}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_NOR** = `8`

Not-OR (NOR) logic operation.

:::: {#class_RenderingDevice_constant_LOGIC_OP_EQUIVALENT}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_EQUIVALENT** = `9`

Not-XOR (XNOR) logic operation.

:::: {#class_RenderingDevice_constant_LOGIC_OP_INVERT}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_INVERT** = `10`

Invert logic operation.

:::: {#class_RenderingDevice_constant_LOGIC_OP_OR_REVERSE}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_OR_REVERSE** = `11`

OR logic operation with the *destination* operand being inverted. See
also
`LOGIC_OP_OR_REVERSE<class_RenderingDevice_constant_LOGIC_OP_OR_REVERSE>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_LOGIC_OP_COPY_INVERTED}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_COPY_INVERTED** = `12`

NOT logic operation (inverts the value). See also
`LOGIC_OP_COPY<class_RenderingDevice_constant_LOGIC_OP_COPY>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_LOGIC_OP_OR_INVERTED}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_OR_INVERTED** = `13`

OR logic operation with the *source* operand being inverted. See also
`LOGIC_OP_OR_REVERSE<class_RenderingDevice_constant_LOGIC_OP_OR_REVERSE>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_LOGIC_OP_NAND}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_NAND** = `14`

Not-AND (NAND) logic operation.

:::: {#class_RenderingDevice_constant_LOGIC_OP_SET}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_SET** = `15`

SET logic operation (result is always `1`). See also
`LOGIC_OP_CLEAR<class_RenderingDevice_constant_LOGIC_OP_CLEAR>`{.interpreted-text
role="ref"}.

:::: {#class_RenderingDevice_constant_LOGIC_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **LOGIC_OP_MAX** = `16`

Represents the size of the
`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_BlendFactor}
::: rst-class
classref-enumeration
:::
::::

enum **BlendFactor**:
`🔗<enum_RenderingDevice_BlendFactor>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ZERO}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ZERO** = `0`

Constant `0.0` blend factor.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ONE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ONE** = `1`

Constant `1.0` blend factor.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_SRC_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_SRC_COLOR** = `2`

Color blend factor is `source color`. Alpha blend factor is
`source alpha`.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ONE_MINUS_SRC_COLOR** = `3`

Color blend factor is `1.0 - source color`. Alpha blend factor is
`1.0 - source alpha`.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_DST_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_DST_COLOR** = `4`

Color blend factor is `destination color`. Alpha blend factor is
`destination alpha`.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_DST_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ONE_MINUS_DST_COLOR** = `5`

Color blend factor is `1.0 - destination color`. Alpha blend factor is
`1.0 - destination alpha`.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_SRC_ALPHA** = `6`

Color and alpha blend factor is `source alpha`.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ONE_MINUS_SRC_ALPHA** = `7`

Color and alpha blend factor is `1.0 - source alpha`.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_DST_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_DST_ALPHA** = `8`

Color and alpha blend factor is `destination alpha`.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_DST_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ONE_MINUS_DST_ALPHA** = `9`

Color and alpha blend factor is `1.0 - destination alpha`.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_CONSTANT_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_CONSTANT_COLOR** = `10`

Color blend factor is `blend constant color`. Alpha blend factor is
`blend constant alpha` (see
`draw_list_set_blend_constants()<class_RenderingDevice_method_draw_list_set_blend_constants>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR** = `11`

Color blend factor is `1.0 - blend constant color`. Alpha blend factor
is `1.0 - blend constant alpha` (see
`draw_list_set_blend_constants()<class_RenderingDevice_method_draw_list_set_blend_constants>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_CONSTANT_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_CONSTANT_ALPHA** = `12`

Color and alpha blend factor is `blend constant alpha` (see
`draw_list_set_blend_constants()<class_RenderingDevice_method_draw_list_set_blend_constants>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA** = `13`

Color and alpha blend factor is `1.0 - blend constant alpha` (see
`draw_list_set_blend_constants()<class_RenderingDevice_method_draw_list_set_blend_constants>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA_SATURATE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_SRC_ALPHA_SATURATE** = `14`

Color blend factor is `min(source alpha, 1.0 - destination alpha)`.
Alpha blend factor is `1.0`.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_SRC1_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_SRC1_COLOR** = `15`

Color blend factor is `second source color`. Alpha blend factor is
`second source alpha`. Only relevant for dual-source blending.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC1_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ONE_MINUS_SRC1_COLOR** = `16`

Color blend factor is `1.0 - second source color`. Alpha blend factor is
`1.0 - second source alpha`. Only relevant for dual-source blending.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_SRC1_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_SRC1_ALPHA** = `17`

Color and alpha blend factor is `second source alpha`. Only relevant for
dual-source blending.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC1_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_ONE_MINUS_SRC1_ALPHA** = `18`

Color and alpha blend factor is `1.0 - second source alpha`. Only
relevant for dual-source blending.

:::: {#class_RenderingDevice_constant_BLEND_FACTOR_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **BLEND_FACTOR_MAX** = `19`

Represents the size of the
`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_BlendOperation}
::: rst-class
classref-enumeration
:::
::::

enum **BlendOperation**:
`🔗<enum_RenderingDevice_BlendOperation>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_BLEND_OP_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
role="ref"} **BLEND_OP_ADD** = `0`

Additive blending operation (`source + destination`).

:::: {#class_RenderingDevice_constant_BLEND_OP_SUBTRACT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
role="ref"} **BLEND_OP_SUBTRACT** = `1`

Subtractive blending operation (`source - destination`).

:::: {#class_RenderingDevice_constant_BLEND_OP_REVERSE_SUBTRACT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
role="ref"} **BLEND_OP_REVERSE_SUBTRACT** = `2`

Reverse subtractive blending operation (`destination - source`).

:::: {#class_RenderingDevice_constant_BLEND_OP_MINIMUM}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
role="ref"} **BLEND_OP_MINIMUM** = `3`

Minimum blending operation (keep the lowest value of the two).

:::: {#class_RenderingDevice_constant_BLEND_OP_MAXIMUM}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
role="ref"} **BLEND_OP_MAXIMUM** = `4`

Maximum blending operation (keep the highest value of the two).

:::: {#class_RenderingDevice_constant_BLEND_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
role="ref"} **BLEND_OP_MAX** = `5`

Represents the size of the
`BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_PipelineDynamicStateFlags}
::: rst-class
classref-enumeration
:::
::::

flags **PipelineDynamicStateFlags**:
`🔗<enum_RenderingDevice_PipelineDynamicStateFlags>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_DYNAMIC_STATE_LINE_WIDTH}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineDynamicStateFlags<enum_RenderingDevice_PipelineDynamicStateFlags>`{.interpreted-text
role="ref"} **DYNAMIC_STATE_LINE_WIDTH** = `1`

Allows dynamically changing the width of rendering lines.

:::: {#class_RenderingDevice_constant_DYNAMIC_STATE_DEPTH_BIAS}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineDynamicStateFlags<enum_RenderingDevice_PipelineDynamicStateFlags>`{.interpreted-text
role="ref"} **DYNAMIC_STATE_DEPTH_BIAS** = `2`

Allows dynamically changing the depth bias.

:::: {#class_RenderingDevice_constant_DYNAMIC_STATE_BLEND_CONSTANTS}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineDynamicStateFlags<enum_RenderingDevice_PipelineDynamicStateFlags>`{.interpreted-text
role="ref"} **DYNAMIC_STATE_BLEND_CONSTANTS** = `4`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DYNAMIC_STATE_DEPTH_BOUNDS}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineDynamicStateFlags<enum_RenderingDevice_PipelineDynamicStateFlags>`{.interpreted-text
role="ref"} **DYNAMIC_STATE_DEPTH_BOUNDS** = `8`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DYNAMIC_STATE_STENCIL_COMPARE_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineDynamicStateFlags<enum_RenderingDevice_PipelineDynamicStateFlags>`{.interpreted-text
role="ref"} **DYNAMIC_STATE_STENCIL_COMPARE_MASK** = `16`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DYNAMIC_STATE_STENCIL_WRITE_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineDynamicStateFlags<enum_RenderingDevice_PipelineDynamicStateFlags>`{.interpreted-text
role="ref"} **DYNAMIC_STATE_STENCIL_WRITE_MASK** = `32`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_RenderingDevice_constant_DYNAMIC_STATE_STENCIL_REFERENCE}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineDynamicStateFlags<enum_RenderingDevice_PipelineDynamicStateFlags>`{.interpreted-text
role="ref"} **DYNAMIC_STATE_STENCIL_REFERENCE** = `64`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_InitialAction}
::: rst-class
classref-enumeration
:::
::::

enum **InitialAction**:
`🔗<enum_RenderingDevice_InitialAction>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_INITIAL_ACTION_LOAD}
::: rst-class
classref-enumeration-constant
:::
::::

`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} **INITIAL_ACTION_LOAD** = `0`

**Deprecated:** Initial actions are solved automatically by
RenderingDevice.

Load the previous contents of the framebuffer.

:::: {#class_RenderingDevice_constant_INITIAL_ACTION_CLEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} **INITIAL_ACTION_CLEAR** = `1`

**Deprecated:** Initial actions are solved automatically by
RenderingDevice.

Clear the whole framebuffer or its specified region.

:::: {#class_RenderingDevice_constant_INITIAL_ACTION_DISCARD}
::: rst-class
classref-enumeration-constant
:::
::::

`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} **INITIAL_ACTION_DISCARD** = `2`

**Deprecated:** Initial actions are solved automatically by
RenderingDevice.

Ignore the previous contents of the framebuffer. This is the fastest
option if you\'ll overwrite all of the pixels and don\'t need to read
any of them.

:::: {#class_RenderingDevice_constant_INITIAL_ACTION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} **INITIAL_ACTION_MAX** = `3`

**Deprecated:** Initial actions are solved automatically by
RenderingDevice.

Represents the size of the
`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} enum.

:::: {#class_RenderingDevice_constant_INITIAL_ACTION_CLEAR_REGION}
::: rst-class
classref-enumeration-constant
:::
::::

`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} **INITIAL_ACTION_CLEAR_REGION** = `1`

**Deprecated:** Initial actions are solved automatically by
RenderingDevice.

:::: {#class_RenderingDevice_constant_INITIAL_ACTION_CLEAR_REGION_CONTINUE}
::: rst-class
classref-enumeration-constant
:::
::::

`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} **INITIAL_ACTION_CLEAR_REGION_CONTINUE** = `1`

**Deprecated:** Initial actions are solved automatically by
RenderingDevice.

:::: {#class_RenderingDevice_constant_INITIAL_ACTION_KEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} **INITIAL_ACTION_KEEP** = `0`

**Deprecated:** Initial actions are solved automatically by
RenderingDevice.

:::: {#class_RenderingDevice_constant_INITIAL_ACTION_DROP}
::: rst-class
classref-enumeration-constant
:::
::::

`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} **INITIAL_ACTION_DROP** = `2`

**Deprecated:** Initial actions are solved automatically by
RenderingDevice.

:::: {#class_RenderingDevice_constant_INITIAL_ACTION_CONTINUE}
::: rst-class
classref-enumeration-constant
:::
::::

`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"} **INITIAL_ACTION_CONTINUE** = `0`

**Deprecated:** Initial actions are solved automatically by
RenderingDevice.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_FinalAction}
::: rst-class
classref-enumeration
:::
::::

enum **FinalAction**:
`🔗<enum_RenderingDevice_FinalAction>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_FINAL_ACTION_STORE}
::: rst-class
classref-enumeration-constant
:::
::::

`FinalAction<enum_RenderingDevice_FinalAction>`{.interpreted-text
role="ref"} **FINAL_ACTION_STORE** = `0`

**Deprecated:** Final actions are solved automatically by
RenderingDevice.

Store the result of the draw list in the framebuffer. This is generally
what you want to do.

:::: {#class_RenderingDevice_constant_FINAL_ACTION_DISCARD}
::: rst-class
classref-enumeration-constant
:::
::::

`FinalAction<enum_RenderingDevice_FinalAction>`{.interpreted-text
role="ref"} **FINAL_ACTION_DISCARD** = `1`

**Deprecated:** Final actions are solved automatically by
RenderingDevice.

Discard the contents of the framebuffer. This is the fastest option if
you don\'t need to use the results of the draw list.

:::: {#class_RenderingDevice_constant_FINAL_ACTION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`FinalAction<enum_RenderingDevice_FinalAction>`{.interpreted-text
role="ref"} **FINAL_ACTION_MAX** = `2`

**Deprecated:** Final actions are solved automatically by
RenderingDevice.

Represents the size of the
`FinalAction<enum_RenderingDevice_FinalAction>`{.interpreted-text
role="ref"} enum.

:::: {#class_RenderingDevice_constant_FINAL_ACTION_READ}
::: rst-class
classref-enumeration-constant
:::
::::

`FinalAction<enum_RenderingDevice_FinalAction>`{.interpreted-text
role="ref"} **FINAL_ACTION_READ** = `0`

**Deprecated:** Final actions are solved automatically by
RenderingDevice.

:::: {#class_RenderingDevice_constant_FINAL_ACTION_CONTINUE}
::: rst-class
classref-enumeration-constant
:::
::::

`FinalAction<enum_RenderingDevice_FinalAction>`{.interpreted-text
role="ref"} **FINAL_ACTION_CONTINUE** = `0`

**Deprecated:** Final actions are solved automatically by
RenderingDevice.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_ShaderStage}
::: rst-class
classref-enumeration
:::
::::

enum **ShaderStage**:
`🔗<enum_RenderingDevice_ShaderStage>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_SHADER_STAGE_VERTEX}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_VERTEX** = `0`

Vertex shader stage. This can be used to manipulate vertices from a
shader (but not create new vertices).

:::: {#class_RenderingDevice_constant_SHADER_STAGE_FRAGMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_FRAGMENT** = `1`

Fragment shader stage (called \"pixel shader\" in Direct3D). This can be
used to manipulate pixels from a shader.

:::: {#class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_CONTROL}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_TESSELATION_CONTROL** = `2`

Tessellation control shader stage. This can be used to create additional
geometry from a shader.

:::: {#class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_EVALUATION}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_TESSELATION_EVALUATION** = `3`

Tessellation evaluation shader stage. This can be used to create
additional geometry from a shader.

:::: {#class_RenderingDevice_constant_SHADER_STAGE_COMPUTE}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_COMPUTE** = `4`

Compute shader stage. This can be used to run arbitrary computing tasks
in a shader, performing them on the GPU instead of the CPU.

:::: {#class_RenderingDevice_constant_SHADER_STAGE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_MAX** = `5`

Represents the size of the
`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} enum.

:::: {#class_RenderingDevice_constant_SHADER_STAGE_VERTEX_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_VERTEX_BIT** = `1`

Vertex shader stage bit (see also
`SHADER_STAGE_VERTEX<class_RenderingDevice_constant_SHADER_STAGE_VERTEX>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_SHADER_STAGE_FRAGMENT_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_FRAGMENT_BIT** = `2`

Fragment shader stage bit (see also
`SHADER_STAGE_FRAGMENT<class_RenderingDevice_constant_SHADER_STAGE_FRAGMENT>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_CONTROL_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_TESSELATION_CONTROL_BIT** = `4`

Tessellation control shader stage bit (see also
`SHADER_STAGE_TESSELATION_CONTROL<class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_CONTROL>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_EVALUATION_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_TESSELATION_EVALUATION_BIT** = `8`

Tessellation evaluation shader stage bit (see also
`SHADER_STAGE_TESSELATION_EVALUATION<class_RenderingDevice_constant_SHADER_STAGE_TESSELATION_EVALUATION>`{.interpreted-text
role="ref"}).

:::: {#class_RenderingDevice_constant_SHADER_STAGE_COMPUTE_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderStage<enum_RenderingDevice_ShaderStage>`{.interpreted-text
role="ref"} **SHADER_STAGE_COMPUTE_BIT** = `16`

Compute shader stage bit (see also
`SHADER_STAGE_COMPUTE<class_RenderingDevice_constant_SHADER_STAGE_COMPUTE>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_ShaderLanguage}
::: rst-class
classref-enumeration
:::
::::

enum **ShaderLanguage**:
`🔗<enum_RenderingDevice_ShaderLanguage>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_SHADER_LANGUAGE_GLSL}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderLanguage<enum_RenderingDevice_ShaderLanguage>`{.interpreted-text
role="ref"} **SHADER_LANGUAGE_GLSL** = `0`

Khronos\' GLSL shading language (used natively by OpenGL and Vulkan).
This is the language used for core Godot shaders.

:::: {#class_RenderingDevice_constant_SHADER_LANGUAGE_HLSL}
::: rst-class
classref-enumeration-constant
:::
::::

`ShaderLanguage<enum_RenderingDevice_ShaderLanguage>`{.interpreted-text
role="ref"} **SHADER_LANGUAGE_HLSL** = `1`

Microsoft\'s High-Level Shading Language (used natively by Direct3D, but
can also be used in Vulkan).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_PipelineSpecializationConstantType}
::: rst-class
classref-enumeration
:::
::::

enum **PipelineSpecializationConstantType**:
`🔗<enum_RenderingDevice_PipelineSpecializationConstantType>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_PIPELINE_SPECIALIZATION_CONSTANT_TYPE_BOOL}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineSpecializationConstantType<enum_RenderingDevice_PipelineSpecializationConstantType>`{.interpreted-text
role="ref"} **PIPELINE_SPECIALIZATION_CONSTANT_TYPE_BOOL** = `0`

Boolean specialization constant.

:::: {#class_RenderingDevice_constant_PIPELINE_SPECIALIZATION_CONSTANT_TYPE_INT}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineSpecializationConstantType<enum_RenderingDevice_PipelineSpecializationConstantType>`{.interpreted-text
role="ref"} **PIPELINE_SPECIALIZATION_CONSTANT_TYPE_INT** = `1`

Integer specialization constant.

:::: {#class_RenderingDevice_constant_PIPELINE_SPECIALIZATION_CONSTANT_TYPE_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`PipelineSpecializationConstantType<enum_RenderingDevice_PipelineSpecializationConstantType>`{.interpreted-text
role="ref"} **PIPELINE_SPECIALIZATION_CONSTANT_TYPE_FLOAT** = `2`

Floating-point specialization constant.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_Features}
::: rst-class
classref-enumeration
:::
::::

enum **Features**: `🔗<enum_RenderingDevice_Features>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_SUPPORTS_METALFX_SPATIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Features<enum_RenderingDevice_Features>`{.interpreted-text role="ref"}
**SUPPORTS_METALFX_SPATIAL** = `3`

Support for MetalFX spatial upscaling.

:::: {#class_RenderingDevice_constant_SUPPORTS_METALFX_TEMPORAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Features<enum_RenderingDevice_Features>`{.interpreted-text role="ref"}
**SUPPORTS_METALFX_TEMPORAL** = `4`

Support for MetalFX temporal upscaling.

:::: {#class_RenderingDevice_constant_SUPPORTS_BUFFER_DEVICE_ADDRESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Features<enum_RenderingDevice_Features>`{.interpreted-text role="ref"}
**SUPPORTS_BUFFER_DEVICE_ADDRESS** = `6`

Features support for buffer device address extension.

:::: {#class_RenderingDevice_constant_SUPPORTS_IMAGE_ATOMIC_32_BIT}
::: rst-class
classref-enumeration-constant
:::
::::

`Features<enum_RenderingDevice_Features>`{.interpreted-text role="ref"}
**SUPPORTS_IMAGE_ATOMIC_32_BIT** = `7`

Support for 32-bit image atomic operations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_Limit}
::: rst-class
classref-enumeration
:::
::::

enum **Limit**: `🔗<enum_RenderingDevice_Limit>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_LIMIT_MAX_BOUND_UNIFORM_SETS}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_BOUND_UNIFORM_SETS** = `0`

Maximum number of uniform sets that can be bound at a given time.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_FRAMEBUFFER_COLOR_ATTACHMENTS}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_FRAMEBUFFER_COLOR_ATTACHMENTS** = `1`

Maximum number of color framebuffer attachments that can be used at a
given time.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_TEXTURES_PER_UNIFORM_SET}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_TEXTURES_PER_UNIFORM_SET** = `2`

Maximum number of textures that can be used per uniform set.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_SAMPLERS_PER_UNIFORM_SET}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_SAMPLERS_PER_UNIFORM_SET** = `3`

Maximum number of samplers that can be used per uniform set.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_STORAGE_BUFFERS_PER_UNIFORM_SET}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_STORAGE_BUFFERS_PER_UNIFORM_SET** = `4`

Maximum number of [storage
buffers](https://vkguide.dev/docs/chapter-4/storage_buffers/) per
uniform set.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_STORAGE_IMAGES_PER_UNIFORM_SET}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_STORAGE_IMAGES_PER_UNIFORM_SET** = `5`

Maximum number of storage images per uniform set.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_UNIFORM_BUFFERS_PER_UNIFORM_SET}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_UNIFORM_BUFFERS_PER_UNIFORM_SET** = `6`

Maximum number of uniform buffers per uniform set.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_DRAW_INDEXED_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_DRAW_INDEXED_INDEX** = `7`

Maximum index for an indexed draw command.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_FRAMEBUFFER_HEIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_FRAMEBUFFER_HEIGHT** = `8`

Maximum height of a framebuffer (in pixels).

:::: {#class_RenderingDevice_constant_LIMIT_MAX_FRAMEBUFFER_WIDTH}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_FRAMEBUFFER_WIDTH** = `9`

Maximum width of a framebuffer (in pixels).

:::: {#class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_ARRAY_LAYERS}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_TEXTURE_ARRAY_LAYERS** = `10`

Maximum number of texture array layers.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_SIZE_1D}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_TEXTURE_SIZE_1D** = `11`

Maximum supported 1-dimensional texture size (in pixels on a single
axis).

:::: {#class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_SIZE_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_TEXTURE_SIZE_2D** = `12`

Maximum supported 2-dimensional texture size (in pixels on a single
axis).

:::: {#class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_SIZE_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_TEXTURE_SIZE_3D** = `13`

Maximum supported 3-dimensional texture size (in pixels on a single
axis).

:::: {#class_RenderingDevice_constant_LIMIT_MAX_TEXTURE_SIZE_CUBE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_TEXTURE_SIZE_CUBE** = `14`

Maximum supported cubemap texture size (in pixels on a single axis of a
single face).

:::: {#class_RenderingDevice_constant_LIMIT_MAX_TEXTURES_PER_SHADER_STAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_TEXTURES_PER_SHADER_STAGE** = `15`

Maximum number of textures per shader stage.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_SAMPLERS_PER_SHADER_STAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_SAMPLERS_PER_SHADER_STAGE** = `16`

Maximum number of samplers per shader stage.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_STORAGE_BUFFERS_PER_SHADER_STAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_STORAGE_BUFFERS_PER_SHADER_STAGE** = `17`

Maximum number of [storage
buffers](https://vkguide.dev/docs/chapter-4/storage_buffers/) per shader
stage.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_STORAGE_IMAGES_PER_SHADER_STAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_STORAGE_IMAGES_PER_SHADER_STAGE** = `18`

Maximum number of storage images per shader stage.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_UNIFORM_BUFFERS_PER_SHADER_STAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_UNIFORM_BUFFERS_PER_SHADER_STAGE** = `19`

Maximum number of uniform buffers per uniform set.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_PUSH_CONSTANT_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_PUSH_CONSTANT_SIZE** = `20`

Maximum size of a push constant. A lot of devices are limited to 128
bytes, so try to avoid exceeding 128 bytes in push constants to ensure
compatibility even if your GPU is reporting a higher value.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_UNIFORM_BUFFER_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_UNIFORM_BUFFER_SIZE** = `21`

Maximum size of a uniform buffer.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_VERTEX_INPUT_ATTRIBUTE_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_VERTEX_INPUT_ATTRIBUTE_OFFSET** = `22`

Maximum vertex input attribute offset.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_VERTEX_INPUT_ATTRIBUTES}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_VERTEX_INPUT_ATTRIBUTES** = `23`

Maximum number of vertex input attributes.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_VERTEX_INPUT_BINDINGS}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_VERTEX_INPUT_BINDINGS** = `24`

Maximum number of vertex input bindings.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_VERTEX_INPUT_BINDING_STRIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_VERTEX_INPUT_BINDING_STRIDE** = `25`

Maximum vertex input binding stride.

:::: {#class_RenderingDevice_constant_LIMIT_MIN_UNIFORM_BUFFER_OFFSET_ALIGNMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MIN_UNIFORM_BUFFER_OFFSET_ALIGNMENT** = `26`

Minimum uniform buffer offset alignment.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_SHARED_MEMORY_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_COMPUTE_SHARED_MEMORY_SIZE** = `27`

Maximum shared memory size for compute shaders.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_X** = `28`

Maximum number of workgroups for compute shaders on the X axis.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Y** = `29`

Maximum number of workgroups for compute shaders on the Y axis.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_COMPUTE_WORKGROUP_COUNT_Z** = `30`

Maximum number of workgroups for compute shaders on the Z axis.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_INVOCATIONS}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_COMPUTE_WORKGROUP_INVOCATIONS** = `31`

Maximum number of workgroup invocations for compute shaders.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_X** = `32`

Maximum workgroup size for compute shaders on the X axis.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Y** = `33`

Maximum workgroup size for compute shaders on the Y axis.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_COMPUTE_WORKGROUP_SIZE_Z** = `34`

Maximum workgroup size for compute shaders on the Z axis.

:::: {#class_RenderingDevice_constant_LIMIT_MAX_VIEWPORT_DIMENSIONS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_VIEWPORT_DIMENSIONS_X** = `35`

Maximum viewport width (in pixels).

:::: {#class_RenderingDevice_constant_LIMIT_MAX_VIEWPORT_DIMENSIONS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_MAX_VIEWPORT_DIMENSIONS_Y** = `36`

Maximum viewport height (in pixels).

:::: {#class_RenderingDevice_constant_LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE** = `46`

Returns the smallest value for
`ProjectSettings.rendering/scaling_3d/scale<class_ProjectSettings_property_rendering/scaling_3d/scale>`{.interpreted-text
role="ref"} when using the MetalFX temporal upscaler.

\*\*Note:\*\* The returned value is multiplied by a factor of `1000000`
to preserve 6 digits of precision. It must be divided by `1000000.0` to
convert the value to a floating point number.

:::: {#class_RenderingDevice_constant_LIMIT_METALFX_TEMPORAL_SCALER_MAX_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"}
**LIMIT_METALFX_TEMPORAL_SCALER_MAX_SCALE** = `47`

Returns the largest value for
`ProjectSettings.rendering/scaling_3d/scale<class_ProjectSettings_property_rendering/scaling_3d/scale>`{.interpreted-text
role="ref"} when using the MetalFX temporal upscaler.

\*\*Note:\*\* The returned value is multiplied by a factor of `1000000`
to preserve 6 digits of precision. It must be divided by `1000000.0` to
convert the value to a floating point number.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_MemoryType}
::: rst-class
classref-enumeration
:::
::::

enum **MemoryType**:
`🔗<enum_RenderingDevice_MemoryType>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_MEMORY_TEXTURES}
::: rst-class
classref-enumeration-constant
:::
::::

`MemoryType<enum_RenderingDevice_MemoryType>`{.interpreted-text
role="ref"} **MEMORY_TEXTURES** = `0`

Memory taken by textures.

:::: {#class_RenderingDevice_constant_MEMORY_BUFFERS}
::: rst-class
classref-enumeration-constant
:::
::::

`MemoryType<enum_RenderingDevice_MemoryType>`{.interpreted-text
role="ref"} **MEMORY_BUFFERS** = `1`

Memory taken by buffers.

:::: {#class_RenderingDevice_constant_MEMORY_TOTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`MemoryType<enum_RenderingDevice_MemoryType>`{.interpreted-text
role="ref"} **MEMORY_TOTAL** = `2`

Total memory taken. This is greater than the sum of
`MEMORY_TEXTURES<class_RenderingDevice_constant_MEMORY_TEXTURES>`{.interpreted-text
role="ref"} and
`MEMORY_BUFFERS<class_RenderingDevice_constant_MEMORY_BUFFERS>`{.interpreted-text
role="ref"}, as it also includes miscellaneous memory usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_BreadcrumbMarker}
::: rst-class
classref-enumeration
:::
::::

enum **BreadcrumbMarker**:
`🔗<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"}

:::: {#class_RenderingDevice_constant_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **NONE** = `0`

No breadcrumb marker will be added.

:::: {#class_RenderingDevice_constant_REFLECTION_PROBES}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **REFLECTION_PROBES** = `65536`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"REFLECTION_PROBES"` for added context as to when the crash
occurred.

:::: {#class_RenderingDevice_constant_SKY_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **SKY_PASS** = `131072`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"SKY_PASS"` for added context as to when the crash occurred.

:::: {#class_RenderingDevice_constant_LIGHTMAPPER_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **LIGHTMAPPER_PASS** = `196608`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"LIGHTMAPPER_PASS"` for added context as to when the crash
occurred.

:::: {#class_RenderingDevice_constant_SHADOW_PASS_DIRECTIONAL}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **SHADOW_PASS_DIRECTIONAL** = `262144`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"SHADOW_PASS_DIRECTIONAL"` for added context as to when the
crash occurred.

:::: {#class_RenderingDevice_constant_SHADOW_PASS_CUBE}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **SHADOW_PASS_CUBE** = `327680`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"SHADOW_PASS_CUBE"` for added context as to when the crash
occurred.

:::: {#class_RenderingDevice_constant_OPAQUE_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **OPAQUE_PASS** = `393216`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"OPAQUE_PASS"` for added context as to when the crash occurred.

:::: {#class_RenderingDevice_constant_ALPHA_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **ALPHA_PASS** = `458752`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"ALPHA_PASS"` for added context as to when the crash occurred.

:::: {#class_RenderingDevice_constant_TRANSPARENT_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **TRANSPARENT_PASS** = `524288`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"TRANSPARENT_PASS"` for added context as to when the crash
occurred.

:::: {#class_RenderingDevice_constant_POST_PROCESSING_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **POST_PROCESSING_PASS** = `589824`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"POST_PROCESSING_PASS"` for added context as to when the crash
occurred.

:::: {#class_RenderingDevice_constant_BLIT_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **BLIT_PASS** = `655360`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"BLIT_PASS"` for added context as to when the crash occurred.

:::: {#class_RenderingDevice_constant_UI_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **UI_PASS** = `720896`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"UI_PASS"` for added context as to when the crash occurred.

:::: {#class_RenderingDevice_constant_DEBUG_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} **DEBUG_PASS** = `786432`

During a GPU crash in dev or debug mode, Godot\'s error message will
include `"DEBUG_PASS"` for added context as to when the crash occurred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RenderingDevice_DrawFlags}
::: rst-class
classref-enumeration
:::
::::

flags **DrawFlags**:
`🔗<enum_RenderingDevice_DrawFlags>`{.interpreted-text role="ref"}

:::: {#class_RenderingDevice_constant_DRAW_DEFAULT_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_DEFAULT_ALL** = `0`

Do not clear or ignore any attachments.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_0}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_0** = `1`

Clear the first color attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_1}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_1** = `2`

Clear the second color attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_2}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_2** = `4`

Clear the third color attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_3}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_3** = `8`

Clear the fourth color attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_4}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_4** = `16`

Clear the fifth color attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_5}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_5** = `32`

Clear the sixth color attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_6}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_6** = `64`

Clear the seventh color attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_7}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_7** = `128`

Clear the eighth color attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_MASK** = `255`

Mask for clearing all color attachments.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_COLOR_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_COLOR_ALL** = `255`

Clear all color attachments.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_0}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_0** = `256`

Ignore the previous contents of the first color attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_1}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_1** = `512`

Ignore the previous contents of the second color attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_2}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_2** = `1024`

Ignore the previous contents of the third color attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_3}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_3** = `2048`

Ignore the previous contents of the fourth color attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_4}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_4** = `4096`

Ignore the previous contents of the fifth color attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_5}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_5** = `8192`

Ignore the previous contents of the sixth color attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_6}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_6** = `16384`

Ignore the previous contents of the seventh color attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_7}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_7** = `32768`

Ignore the previous contents of the eighth color attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_MASK** = `65280`

Mask for ignoring all the previous contents of the color attachments.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_COLOR_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_COLOR_ALL** = `65280`

Ignore the previous contents of all color attachments.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_DEPTH}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_DEPTH** = `65536`

Clear the depth attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_DEPTH}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_DEPTH** = `131072`

Ignore the previous contents of the depth attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_STENCIL}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_STENCIL** = `262144`

Clear the stencil attachment.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_STENCIL}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_STENCIL** = `524288`

Ignore the previous contents of the stencil attachment.

:::: {#class_RenderingDevice_constant_DRAW_CLEAR_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_CLEAR_ALL** = `327935`

Clear all attachments.

:::: {#class_RenderingDevice_constant_DRAW_IGNORE_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"} **DRAW_IGNORE_ALL** = `720640`

Ignore the previous contents of all attachments.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_RenderingDevice_constant_INVALID_ID}
::: rst-class
classref-constant
:::
::::

**INVALID_ID** = `-1`
`🔗<class_RenderingDevice_constant_INVALID_ID>`{.interpreted-text
role="ref"}

Returned by functions that return an ID if a value is invalid.

:::: {#class_RenderingDevice_constant_INVALID_FORMAT_ID}
::: rst-class
classref-constant
:::
::::

**INVALID_FORMAT_ID** = `-1`
`🔗<class_RenderingDevice_constant_INVALID_FORMAT_ID>`{.interpreted-text
role="ref"}

Returned by functions that return a format ID if a value is invalid.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RenderingDevice_method_barrier}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**barrier**(from:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`BarrierMask<enum_RenderingDevice_BarrierMask>`{.interpreted-text
role="ref"}\] = 32767, to:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`BarrierMask<enum_RenderingDevice_BarrierMask>`{.interpreted-text
role="ref"}\] = 32767)
`🔗<class_RenderingDevice_method_barrier>`{.interpreted-text role="ref"}

**Deprecated:** Barriers are automatically inserted by RenderingDevice.

This method does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_buffer_clear}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**buffer_clear**(buffer: `RID<class_RID>`{.interpreted-text role="ref"},
offset: `int<class_int>`{.interpreted-text role="ref"}, size_bytes:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_buffer_clear>`{.interpreted-text
role="ref"}

Clears the contents of the `buffer`, clearing `size_bytes` bytes,
starting at `offset`.

Prints an error if:

- the size isn\'t a multiple of four
- the region specified by `offset` + `size_bytes` exceeds the buffer
- a draw list is currently active (created by
  `draw_list_begin()<class_RenderingDevice_method_draw_list_begin>`{.interpreted-text
  role="ref"})
- a compute list is currently active (created by
  `compute_list_begin()<class_RenderingDevice_method_compute_list_begin>`{.interpreted-text
  role="ref"})

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_buffer_copy}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**buffer_copy**(src_buffer: `RID<class_RID>`{.interpreted-text
role="ref"}, dst_buffer: `RID<class_RID>`{.interpreted-text role="ref"},
src_offset: `int<class_int>`{.interpreted-text role="ref"}, dst_offset:
`int<class_int>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_buffer_copy>`{.interpreted-text
role="ref"}

Copies `size` bytes from the `src_buffer` at `src_offset` into
`dst_buffer` at `dst_offset`.

Prints an error if:

- `size` exceeds the size of either `src_buffer` or `dst_buffer` at
  their corresponding offsets
- a draw list is currently active (created by
  `draw_list_begin()<class_RenderingDevice_method_draw_list_begin>`{.interpreted-text
  role="ref"})
- a compute list is currently active (created by
  `compute_list_begin()<class_RenderingDevice_method_compute_list_begin>`{.interpreted-text
  role="ref"})

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_buffer_get_data}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**buffer_get_data**(buffer: `RID<class_RID>`{.interpreted-text
role="ref"}, offset_bytes: `int<class_int>`{.interpreted-text
role="ref"} = 0, size_bytes: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_RenderingDevice_method_buffer_get_data>`{.interpreted-text
role="ref"}

Returns a copy of the data of the specified `buffer`, optionally
`offset_bytes` and `size_bytes` can be set to copy only a portion of the
buffer.

\*\*Note:\*\* This method will block the GPU from working until the data
is retrieved. Refer to
`buffer_get_data_async()<class_RenderingDevice_method_buffer_get_data_async>`{.interpreted-text
role="ref"} for an alternative that returns the data in more performant
way.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_buffer_get_data_async}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**buffer_get_data_async**(buffer: `RID<class_RID>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"}, offset_bytes: `int<class_int>`{.interpreted-text
role="ref"} = 0, size_bytes: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_RenderingDevice_method_buffer_get_data_async>`{.interpreted-text
role="ref"}

Asynchronous version of
`buffer_get_data()<class_RenderingDevice_method_buffer_get_data>`{.interpreted-text
role="ref"}. RenderingDevice will call `callback` in a certain amount of
frames with the data the buffer had at the time of the request.

\*\*Note:\*\* At the moment, the delay corresponds to the amount of
frames specified by
`ProjectSettings.rendering/rendering_device/vsync/frame_queue_size<class_ProjectSettings_property_rendering/rendering_device/vsync/frame_queue_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Downloading large buffers can have a prohibitive cost for
real-time even when using the asynchronous method due to hardware
bandwidth limitations. When dealing with large resources, you can adjust
settings such as
`ProjectSettings.rendering/rendering_device/staging_buffer/block_size_kb<class_ProjectSettings_property_rendering/rendering_device/staging_buffer/block_size_kb>`{.interpreted-text
role="ref"} to improve the transfer speed at the cost of extra memory.

    func _buffer_get_data_callback(array):
        value = array.decode_u32(0)

    ...

    rd.buffer_get_data_async(buffer, _buffer_get_data_callback)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_buffer_get_device_address}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**buffer_get_device_address**(buffer: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_buffer_get_device_address>`{.interpreted-text
role="ref"}

Returns the address of the given `buffer` which can be passed to shaders
in any way to access underlying data. Buffer must have been created with
this feature enabled.

\*\*Note:\*\* You must check that the GPU supports this functionality by
calling
`has_feature()<class_RenderingDevice_method_has_feature>`{.interpreted-text
role="ref"} with
`SUPPORTS_BUFFER_DEVICE_ADDRESS<class_RenderingDevice_constant_SUPPORTS_BUFFER_DEVICE_ADDRESS>`{.interpreted-text
role="ref"} as a parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_buffer_update}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**buffer_update**(buffer: `RID<class_RID>`{.interpreted-text
role="ref"}, offset: `int<class_int>`{.interpreted-text role="ref"},
size_bytes: `int<class_int>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_buffer_update>`{.interpreted-text
role="ref"}

Updates a region of `size_bytes` bytes, starting at `offset`, in the
buffer, with the specified `data`.

Prints an error if:

- the region specified by `offset` + `size_bytes` exceeds the buffer
- a draw list is currently active (created by
  `draw_list_begin()<class_RenderingDevice_method_draw_list_begin>`{.interpreted-text
  role="ref"})
- a compute list is currently active (created by
  `compute_list_begin()<class_RenderingDevice_method_compute_list_begin>`{.interpreted-text
  role="ref"})

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_capture_timestamp}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**capture_timestamp**(name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_capture_timestamp>`{.interpreted-text
role="ref"}

Creates a timestamp marker with the specified `name`. This is used for
performance reporting with the
`get_captured_timestamp_cpu_time()<class_RenderingDevice_method_get_captured_timestamp_cpu_time>`{.interpreted-text
role="ref"},
`get_captured_timestamp_gpu_time()<class_RenderingDevice_method_get_captured_timestamp_gpu_time>`{.interpreted-text
role="ref"} and
`get_captured_timestamp_name()<class_RenderingDevice_method_get_captured_timestamp_name>`{.interpreted-text
role="ref"} methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_list_add_barrier}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compute_list_add_barrier**(compute_list:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_compute_list_add_barrier>`{.interpreted-text
role="ref"}

Raises a Vulkan compute barrier in the specified `compute_list`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_list_begin}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **compute_list_begin**()
`🔗<class_RenderingDevice_method_compute_list_begin>`{.interpreted-text
role="ref"}

Starts a list of compute commands created with the `compute_*` methods.
The returned value should be passed to other `compute_list_*` functions.

Multiple compute lists cannot be created at the same time; you must
finish the previous compute list first using
`compute_list_end()<class_RenderingDevice_method_compute_list_end>`{.interpreted-text
role="ref"}.

A simple compute operation might look like this (code is not a complete
example):

    var rd = RenderingDevice.new()
    var compute_list = rd.compute_list_begin()

    rd.compute_list_bind_compute_pipeline(compute_list, compute_shader_dilate_pipeline)
    rd.compute_list_bind_uniform_set(compute_list, compute_base_uniform_set, 0)
    rd.compute_list_bind_uniform_set(compute_list, dilate_uniform_set, 1)

    for i in atlas_slices:
        rd.compute_list_set_push_constant(compute_list, push_constant, push_constant.size())
        rd.compute_list_dispatch(compute_list, group_size.x, group_size.y, group_size.z)
        # No barrier, let them run all together.

    rd.compute_list_end()

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_list_bind_compute_pipeline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compute_list_bind_compute_pipeline**(compute_list:
`int<class_int>`{.interpreted-text role="ref"}, compute_pipeline:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_compute_list_bind_compute_pipeline>`{.interpreted-text
role="ref"}

Tells the GPU what compute pipeline to use when processing the compute
list. If the shader has changed since the last time this function was
called, Godot will unbind all descriptor sets and will re-bind them
inside
`compute_list_dispatch()<class_RenderingDevice_method_compute_list_dispatch>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_list_bind_uniform_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compute_list_bind_uniform_set**(compute_list:
`int<class_int>`{.interpreted-text role="ref"}, uniform_set:
`RID<class_RID>`{.interpreted-text role="ref"}, set_index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_compute_list_bind_uniform_set>`{.interpreted-text
role="ref"}

Binds the `uniform_set` to this `compute_list`. Godot ensures that all
textures in the uniform set have the correct Vulkan access masks. If
Godot had to change access masks of textures, it will raise a Vulkan
image memory barrier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_list_dispatch}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compute_list_dispatch**(compute_list:
`int<class_int>`{.interpreted-text role="ref"}, x_groups:
`int<class_int>`{.interpreted-text role="ref"}, y_groups:
`int<class_int>`{.interpreted-text role="ref"}, z_groups:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_compute_list_dispatch>`{.interpreted-text
role="ref"}

Submits the compute list for processing on the GPU. This is the compute
equivalent to
`draw_list_draw()<class_RenderingDevice_method_draw_list_draw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_list_dispatch_indirect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compute_list_dispatch_indirect**(compute_list:
`int<class_int>`{.interpreted-text role="ref"}, buffer:
`RID<class_RID>`{.interpreted-text role="ref"}, offset:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_compute_list_dispatch_indirect>`{.interpreted-text
role="ref"}

Submits the compute list for processing on the GPU with the given group
counts stored in the `buffer` at `offset`. Buffer must have been created
with
`STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT<class_RenderingDevice_constant_STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT>`{.interpreted-text
role="ref"} flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_list_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compute_list_end**()
`🔗<class_RenderingDevice_method_compute_list_end>`{.interpreted-text
role="ref"}

Finishes a list of compute commands created with the `compute_*`
methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_list_set_push_constant}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**compute_list_set_push_constant**(compute_list:
`int<class_int>`{.interpreted-text role="ref"}, buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
size_bytes: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_compute_list_set_push_constant>`{.interpreted-text
role="ref"}

Sets the push constant data to `buffer` for the specified
`compute_list`. The shader determines how this binary data is used. The
buffer\'s size in bytes must also be specified in `size_bytes` (this can
be obtained by calling the
`PackedByteArray.size()<class_PackedByteArray_method_size>`{.interpreted-text
role="ref"} method on the passed `buffer`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_pipeline_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**compute_pipeline_create**(shader: `RID<class_RID>`{.interpreted-text
role="ref"}, specialization_constants:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RDPipelineSpecializationConstant<class_RDPipelineSpecializationConstant>`{.interpreted-text
role="ref"}\] = \[\])
`🔗<class_RenderingDevice_method_compute_pipeline_create>`{.interpreted-text
role="ref"}

Creates a new compute pipeline. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_compute_pipeline_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**compute_pipeline_is_valid**(compute_pipeline:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_compute_pipeline_is_valid>`{.interpreted-text
role="ref"}

Returns `true` if the compute pipeline specified by the
`compute_pipeline` RID is valid, `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_create_local_device}
::: rst-class
classref-method
:::
::::

`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}
**create_local_device**()
`🔗<class_RenderingDevice_method_create_local_device>`{.interpreted-text
role="ref"}

Create a new local **RenderingDevice**. This is most useful for
performing compute operations on the GPU independently from the rest of
the engine.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_command_begin_label}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_command_begin_label**(name:
`String<class_String>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_command_begin_label>`{.interpreted-text
role="ref"}

Create a command buffer debug label region that can be displayed in
third-party tools such as [RenderDoc](https://renderdoc.org/). All
regions must be ended with a
`draw_command_end_label()<class_RenderingDevice_method_draw_command_end_label>`{.interpreted-text
role="ref"} call. When viewed from the linear series of submissions to a
single queue, calls to
`draw_command_begin_label()<class_RenderingDevice_method_draw_command_begin_label>`{.interpreted-text
role="ref"} and
`draw_command_end_label()<class_RenderingDevice_method_draw_command_end_label>`{.interpreted-text
role="ref"} must be matched and balanced.

The `VK_EXT_DEBUG_UTILS_EXTENSION_NAME` Vulkan extension must be
available and enabled for command buffer debug label region to work. See
also
`draw_command_end_label()<class_RenderingDevice_method_draw_command_end_label>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_command_end_label}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_command_end_label**()
`🔗<class_RenderingDevice_method_draw_command_end_label>`{.interpreted-text
role="ref"}

Ends the command buffer debug label region started by a
`draw_command_begin_label()<class_RenderingDevice_method_draw_command_begin_label>`{.interpreted-text
role="ref"} call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_command_insert_label}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_command_insert_label**(name:
`String<class_String>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_command_insert_label>`{.interpreted-text
role="ref"}

**Deprecated:** Inserting labels no longer applies due to command
reordering.

This method does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_begin}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**draw_list_begin**(framebuffer: `RID<class_RID>`{.interpreted-text
role="ref"}, draw_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DrawFlags<enum_RenderingDevice_DrawFlags>`{.interpreted-text
role="ref"}\] = 0, clear_color_values:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
= PackedColorArray(), clear_depth_value:
`float<class_float>`{.interpreted-text role="ref"} = 1.0,
clear_stencil_value: `int<class_int>`{.interpreted-text role="ref"} = 0,
region: `Rect2<class_Rect2>`{.interpreted-text role="ref"} = Rect2(0, 0,
0, 0), breadcrumb: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_RenderingDevice_method_draw_list_begin>`{.interpreted-text
role="ref"}

Starts a list of raster drawing commands created with the `draw_*`
methods. The returned value should be passed to other `draw_list_*`
functions.

Multiple draw lists cannot be created at the same time; you must finish
the previous draw list first using
`draw_list_end()<class_RenderingDevice_method_draw_list_end>`{.interpreted-text
role="ref"}.

A simple drawing operation might look like this (code is not a complete
example):

    var rd = RenderingDevice.new()
    var clear_colors = PackedColorArray([Color(0, 0, 0, 0), Color(0, 0, 0, 0), Color(0, 0, 0, 0)])
    var draw_list = rd.draw_list_begin(framebuffers[i], RenderingDevice.CLEAR_COLOR_ALL, clear_colors, true, 1.0f, true, 0, Rect2(), RenderingDevice.OPAQUE_PASS)

    # Draw opaque.
    rd.draw_list_bind_render_pipeline(draw_list, raster_pipeline)
    rd.draw_list_bind_uniform_set(draw_list, raster_base_uniform, 0)
    rd.draw_list_set_push_constant(draw_list, raster_push_constant, raster_push_constant.size())
    rd.draw_list_draw(draw_list, false, 1, slice_triangle_count[i] * 3)
    # Draw wire.
    rd.draw_list_bind_render_pipeline(draw_list, raster_pipeline_wire)
    rd.draw_list_bind_uniform_set(draw_list, raster_base_uniform, 0)
    rd.draw_list_set_push_constant(draw_list, raster_push_constant, raster_push_constant.size())
    rd.draw_list_draw(draw_list, false, 1, slice_triangle_count[i] * 3)

    rd.draw_list_end()

The `draw_flags` indicates if the texture attachments of the framebuffer
should be cleared or ignored. Only one of the two flags can be used for
each individual attachment. Ignoring an attachment means that any
contents that existed before the draw list will be completely discarded,
reducing the memory bandwidth used by the render pass but producing
garbage results if the pixels aren\'t replaced. The default behavior
allows the engine to figure out the right operation to use if the
texture is discardable, which can result in increased performance. See
`RDTextureFormat<class_RDTextureFormat>`{.interpreted-text role="ref"}
or
`texture_set_discardable()<class_RenderingDevice_method_texture_set_discardable>`{.interpreted-text
role="ref"}.

The `breadcrumb` parameter can be an arbitrary 32-bit integer that is
useful to diagnose GPU crashes. If Godot is built in dev or debug mode;
when the GPU crashes Godot will dump all shaders that were being
executed at the time of the crash and the breadcrumb is useful to
diagnose what passes did those shaders belong to.

It does not affect rendering behavior and can be set to 0. It is
recommended to use
`BreadcrumbMarker<enum_RenderingDevice_BreadcrumbMarker>`{.interpreted-text
role="ref"} enumerations for consistency but it\'s not required. It is
also possible to use bitwise operations to add extra data. e.g.

    rd.draw_list_begin(fb[i], RenderingDevice.CLEAR_COLOR_ALL, clear_colors, true, 1.0f, true, 0, Rect2(), RenderingDevice.OPAQUE_PASS | 5)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_begin_for_screen}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**draw_list_begin_for_screen**(screen:
`int<class_int>`{.interpreted-text role="ref"} = 0, clear_color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(0, 0, 0, 1))
`🔗<class_RenderingDevice_method_draw_list_begin_for_screen>`{.interpreted-text
role="ref"}

High-level variant of
`draw_list_begin()<class_RenderingDevice_method_draw_list_begin>`{.interpreted-text
role="ref"}, with the parameters automatically being adjusted for
drawing onto the window specified by the `screen` ID.

\*\*Note:\*\* Cannot be used with local RenderingDevices, as these
don\'t have a screen. If called on a local RenderingDevice,
`draw_list_begin_for_screen()<class_RenderingDevice_method_draw_list_begin_for_screen>`{.interpreted-text
role="ref"} returns
`INVALID_ID<class_RenderingDevice_constant_INVALID_ID>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_begin_split}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**draw_list_begin_split**(framebuffer:
`RID<class_RID>`{.interpreted-text role="ref"}, splits:
`int<class_int>`{.interpreted-text role="ref"}, initial_color_action:
`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"}, final_color_action:
`FinalAction<enum_RenderingDevice_FinalAction>`{.interpreted-text
role="ref"}, initial_depth_action:
`InitialAction<enum_RenderingDevice_InitialAction>`{.interpreted-text
role="ref"}, final_depth_action:
`FinalAction<enum_RenderingDevice_FinalAction>`{.interpreted-text
role="ref"}, clear_color_values:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
= PackedColorArray(), clear_depth:
`float<class_float>`{.interpreted-text role="ref"} = 1.0, clear_stencil:
`int<class_int>`{.interpreted-text role="ref"} = 0, region:
`Rect2<class_Rect2>`{.interpreted-text role="ref"} = Rect2(0, 0, 0, 0),
storage_textures: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\] = \[\])
`🔗<class_RenderingDevice_method_draw_list_begin_split>`{.interpreted-text
role="ref"}

**Deprecated:** Split draw lists are used automatically by
RenderingDevice.

This method does nothing and always returns an empty
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_bind_index_array}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_bind_index_array**(draw_list:
`int<class_int>`{.interpreted-text role="ref"}, index_array:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_list_bind_index_array>`{.interpreted-text
role="ref"}

Binds `index_array` to the specified `draw_list`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_bind_render_pipeline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_bind_render_pipeline**(draw_list:
`int<class_int>`{.interpreted-text role="ref"}, render_pipeline:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_list_bind_render_pipeline>`{.interpreted-text
role="ref"}

Binds `render_pipeline` to the specified `draw_list`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_bind_uniform_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_bind_uniform_set**(draw_list:
`int<class_int>`{.interpreted-text role="ref"}, uniform_set:
`RID<class_RID>`{.interpreted-text role="ref"}, set_index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_list_bind_uniform_set>`{.interpreted-text
role="ref"}

Binds `uniform_set` to the specified `draw_list`. A `set_index` must
also be specified, which is an identifier starting from `0` that must
match the one expected by the draw list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_bind_vertex_array}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_bind_vertex_array**(draw_list:
`int<class_int>`{.interpreted-text role="ref"}, vertex_array:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_list_bind_vertex_array>`{.interpreted-text
role="ref"}

Binds `vertex_array` to the specified `draw_list`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_disable_scissor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_disable_scissor**(draw_list:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_list_disable_scissor>`{.interpreted-text
role="ref"}

Removes and disables the scissor rectangle for the specified
`draw_list`. See also
`draw_list_enable_scissor()<class_RenderingDevice_method_draw_list_enable_scissor>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_draw**(draw_list: `int<class_int>`{.interpreted-text
role="ref"}, use_indices: `bool<class_bool>`{.interpreted-text
role="ref"}, instances: `int<class_int>`{.interpreted-text role="ref"},
procedural_vertex_count: `int<class_int>`{.interpreted-text role="ref"}
= 0) `🔗<class_RenderingDevice_method_draw_list_draw>`{.interpreted-text
role="ref"}

Submits `draw_list` for rendering on the GPU. This is the raster
equivalent to
`compute_list_dispatch()<class_RenderingDevice_method_compute_list_dispatch>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_draw_indirect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_draw_indirect**(draw_list:
`int<class_int>`{.interpreted-text role="ref"}, use_indices:
`bool<class_bool>`{.interpreted-text role="ref"}, buffer:
`RID<class_RID>`{.interpreted-text role="ref"}, offset:
`int<class_int>`{.interpreted-text role="ref"} = 0, draw_count:
`int<class_int>`{.interpreted-text role="ref"} = 1, stride:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_RenderingDevice_method_draw_list_draw_indirect>`{.interpreted-text
role="ref"}

Submits `draw_list` for rendering on the GPU with the given parameters
stored in the `buffer` at `offset`. Parameters being integers: vertex
count, instance count, first vertex, first instance. And when using
indices: index count, instance count, first index, vertex offset, first
instance. Buffer must have been created with
`STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT<class_RenderingDevice_constant_STORAGE_BUFFER_USAGE_DISPATCH_INDIRECT>`{.interpreted-text
role="ref"} flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_enable_scissor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_enable_scissor**(draw_list:
`int<class_int>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"} = Rect2(0, 0, 0, 0))
`🔗<class_RenderingDevice_method_draw_list_enable_scissor>`{.interpreted-text
role="ref"}

Creates a scissor rectangle and enables it for the specified
`draw_list`. Scissor rectangles are used for clipping by discarding
fragments that fall outside a specified rectangular portion of the
screen. See also
`draw_list_disable_scissor()<class_RenderingDevice_method_draw_list_disable_scissor>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The specified `rect` is automatically intersected with the
screen\'s dimensions, which means it cannot exceed the screen\'s
dimensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_end**()
`🔗<class_RenderingDevice_method_draw_list_end>`{.interpreted-text
role="ref"}

Finishes a list of raster drawing commands created with the `draw_*`
methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_set_blend_constants}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_set_blend_constants**(draw_list:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_list_set_blend_constants>`{.interpreted-text
role="ref"}

Sets blend constants for the specified `draw_list` to `color`. Blend
constants are used only if the graphics pipeline is created with
`DYNAMIC_STATE_BLEND_CONSTANTS<class_RenderingDevice_constant_DYNAMIC_STATE_BLEND_CONSTANTS>`{.interpreted-text
role="ref"} flag set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_set_push_constant}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_list_set_push_constant**(draw_list:
`int<class_int>`{.interpreted-text role="ref"}, buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
size_bytes: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_list_set_push_constant>`{.interpreted-text
role="ref"}

Sets the push constant data to `buffer` for the specified `draw_list`.
The shader determines how this binary data is used. The buffer\'s size
in bytes must also be specified in `size_bytes` (this can be obtained by
calling the
`PackedByteArray.size()<class_PackedByteArray_method_size>`{.interpreted-text
role="ref"} method on the passed `buffer`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_switch_to_next_pass}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**draw_list_switch_to_next_pass**()
`🔗<class_RenderingDevice_method_draw_list_switch_to_next_pass>`{.interpreted-text
role="ref"}

Switches to the next draw pass.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_draw_list_switch_to_next_pass_split}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**draw_list_switch_to_next_pass_split**(splits:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_draw_list_switch_to_next_pass_split>`{.interpreted-text
role="ref"}

**Deprecated:** Split draw lists are used automatically by
RenderingDevice.

This method does nothing and always returns an empty
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_framebuffer_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**framebuffer_create**(textures: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\],
validate_with_format: `int<class_int>`{.interpreted-text role="ref"} =
-1, view_count: `int<class_int>`{.interpreted-text role="ref"} = 1)
`🔗<class_RenderingDevice_method_framebuffer_create>`{.interpreted-text
role="ref"}

Creates a new framebuffer. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_framebuffer_create_empty}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**framebuffer_create_empty**(size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, samples:
`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} = 0, validate_with_format:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_RenderingDevice_method_framebuffer_create_empty>`{.interpreted-text
role="ref"}

Creates a new empty framebuffer. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_framebuffer_create_multipass}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**framebuffer_create_multipass**(textures:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\], passes:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RDFramebufferPass<class_RDFramebufferPass>`{.interpreted-text
role="ref"}\], validate_with_format: `int<class_int>`{.interpreted-text
role="ref"} = -1, view_count: `int<class_int>`{.interpreted-text
role="ref"} = 1)
`🔗<class_RenderingDevice_method_framebuffer_create_multipass>`{.interpreted-text
role="ref"}

Creates a new multipass framebuffer. It can be accessed with the RID
that is returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_framebuffer_format_create}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**framebuffer_format_create**(attachments:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RDAttachmentFormat<class_RDAttachmentFormat>`{.interpreted-text
role="ref"}\], view_count: `int<class_int>`{.interpreted-text
role="ref"} = 1)
`🔗<class_RenderingDevice_method_framebuffer_format_create>`{.interpreted-text
role="ref"}

Creates a new framebuffer format with the specified `attachments` and
`view_count`. Returns the new framebuffer\'s unique framebuffer format
ID.

If `view_count` is greater than or equal to `2`, enables multiview which
is used for VR rendering. This requires support for the Vulkan multiview
extension.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_framebuffer_format_create_empty}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**framebuffer_format_create_empty**(samples:
`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} = 0)
`🔗<class_RenderingDevice_method_framebuffer_format_create_empty>`{.interpreted-text
role="ref"}

Creates a new empty framebuffer format with the specified number of
`samples` and returns its ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_framebuffer_format_create_multipass}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**framebuffer_format_create_multipass**(attachments:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RDAttachmentFormat<class_RDAttachmentFormat>`{.interpreted-text
role="ref"}\], passes: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RDFramebufferPass<class_RDFramebufferPass>`{.interpreted-text
role="ref"}\], view_count: `int<class_int>`{.interpreted-text
role="ref"} = 1)
`🔗<class_RenderingDevice_method_framebuffer_format_create_multipass>`{.interpreted-text
role="ref"}

Creates a multipass framebuffer format with the specified `attachments`,
`passes` and `view_count` and returns its ID. If `view_count` is greater
than or equal to `2`, enables multiview which is used for VR rendering.
This requires support for the Vulkan multiview extension.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_framebuffer_format_get_texture_samples}
::: rst-class
classref-method
:::
::::

`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"} **framebuffer_format_get_texture_samples**(format:
`int<class_int>`{.interpreted-text role="ref"}, render_pass:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_RenderingDevice_method_framebuffer_format_get_texture_samples>`{.interpreted-text
role="ref"}

Returns the number of texture samples used for the given framebuffer
`format` ID (returned by
`framebuffer_get_format()<class_RenderingDevice_method_framebuffer_get_format>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_framebuffer_get_format}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**framebuffer_get_format**(framebuffer:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_framebuffer_get_format>`{.interpreted-text
role="ref"}

Returns the format ID of the framebuffer specified by the `framebuffer`
RID. This ID is guaranteed to be unique for the same formats and does
not need to be freed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_framebuffer_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**framebuffer_is_valid**(framebuffer: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_framebuffer_is_valid>`{.interpreted-text
role="ref"}

Returns `true` if the framebuffer specified by the `framebuffer` RID is
valid, `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_free_rid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**free_rid**(rid: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"}

Tries to free an object in the RenderingDevice. To avoid memory leaks,
this should be called after using an object as memory management does
not occur automatically when using RenderingDevice directly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_full_barrier}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**full_barrier**()
`🔗<class_RenderingDevice_method_full_barrier>`{.interpreted-text
role="ref"}

**Deprecated:** Barriers are automatically inserted by RenderingDevice.

This method does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_captured_timestamp_cpu_time}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_captured_timestamp_cpu_time**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_captured_timestamp_cpu_time>`{.interpreted-text
role="ref"}

Returns the timestamp in CPU time for the rendering step specified by
`index` (in microseconds since the engine started). See also
`get_captured_timestamp_gpu_time()<class_RenderingDevice_method_get_captured_timestamp_gpu_time>`{.interpreted-text
role="ref"} and
`capture_timestamp()<class_RenderingDevice_method_capture_timestamp>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_captured_timestamp_gpu_time}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_captured_timestamp_gpu_time**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_captured_timestamp_gpu_time>`{.interpreted-text
role="ref"}

Returns the timestamp in GPU time for the rendering step specified by
`index` (in microseconds since the engine started). See also
`get_captured_timestamp_cpu_time()<class_RenderingDevice_method_get_captured_timestamp_cpu_time>`{.interpreted-text
role="ref"} and
`capture_timestamp()<class_RenderingDevice_method_capture_timestamp>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_captured_timestamp_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_captured_timestamp_name**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_captured_timestamp_name>`{.interpreted-text
role="ref"}

Returns the timestamp\'s name for the rendering step specified by
`index`. See also
`capture_timestamp()<class_RenderingDevice_method_capture_timestamp>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_captured_timestamps_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_captured_timestamps_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_captured_timestamps_count>`{.interpreted-text
role="ref"}

Returns the total number of timestamps (rendering steps) available for
profiling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_captured_timestamps_frame}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_captured_timestamps_frame**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_captured_timestamps_frame>`{.interpreted-text
role="ref"}

Returns the index of the last frame rendered that has rendering
timestamps available for querying.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_device_allocation_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_device_allocation_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_device_allocation_count>`{.interpreted-text
role="ref"}

Returns how many allocations the GPU has performed for internal driver
structures.

This is only used by Vulkan in debug builds and can return 0 when this
information is not tracked or unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_device_allocs_by_object_type}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_device_allocs_by_object_type**(type:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_device_allocs_by_object_type>`{.interpreted-text
role="ref"}

Same as
`get_device_allocation_count()<class_RenderingDevice_method_get_device_allocation_count>`{.interpreted-text
role="ref"} but filtered for a given object type.

The type argument must be in range
`[0; get_tracked_object_type_count - 1]`. If
`get_tracked_object_type_count()<class_RenderingDevice_method_get_tracked_object_type_count>`{.interpreted-text
role="ref"} is 0, then type argument is ignored and always returns 0.

This is only used by Vulkan in debug builds and can return 0 when this
information is not tracked or unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_device_memory_by_object_type}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_device_memory_by_object_type**(type:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_device_memory_by_object_type>`{.interpreted-text
role="ref"}

Same as
`get_device_total_memory()<class_RenderingDevice_method_get_device_total_memory>`{.interpreted-text
role="ref"} but filtered for a given object type.

The type argument must be in range
`[0; get_tracked_object_type_count - 1]`. If
`get_tracked_object_type_count()<class_RenderingDevice_method_get_tracked_object_type_count>`{.interpreted-text
role="ref"} is 0, then type argument is ignored and always returns 0.

This is only used by Vulkan in debug builds and can return 0 when this
information is not tracked or unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_device_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_device_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_device_name>`{.interpreted-text
role="ref"}

Returns the name of the video adapter (e.g. \"GeForce GTX
1080/PCIe/SSE2\"). Equivalent to
`RenderingServer.get_video_adapter_name()<class_RenderingServer_method_get_video_adapter_name>`{.interpreted-text
role="ref"}. See also
`get_device_vendor_name()<class_RenderingDevice_method_get_device_vendor_name>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_device_pipeline_cache_uuid}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_device_pipeline_cache_uuid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_device_pipeline_cache_uuid>`{.interpreted-text
role="ref"}

Returns the universally unique identifier for the pipeline cache. This
is used to cache shader files on disk, which avoids shader
recompilations on subsequent engine runs. This UUID varies depending on
the graphics card model, but also the driver version. Therefore,
updating graphics drivers will invalidate the shader cache.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_device_total_memory}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_device_total_memory**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_device_total_memory>`{.interpreted-text
role="ref"}

Returns how much bytes the GPU is using.

This is only used by Vulkan in debug builds and can return 0 when this
information is not tracked or unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_device_vendor_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_device_vendor_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_device_vendor_name>`{.interpreted-text
role="ref"}

Returns the vendor of the video adapter (e.g. \"NVIDIA Corporation\").
Equivalent to
`RenderingServer.get_video_adapter_vendor()<class_RenderingServer_method_get_video_adapter_vendor>`{.interpreted-text
role="ref"}. See also
`get_device_name()<class_RenderingDevice_method_get_device_name>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_driver_allocation_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_driver_allocation_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_driver_allocation_count>`{.interpreted-text
role="ref"}

Returns how many allocations the GPU driver has performed for internal
driver structures.

This is only used by Vulkan in debug builds and can return 0 when this
information is not tracked or unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_driver_allocs_by_object_type}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_driver_allocs_by_object_type**(type:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_driver_allocs_by_object_type>`{.interpreted-text
role="ref"}

Same as
`get_driver_allocation_count()<class_RenderingDevice_method_get_driver_allocation_count>`{.interpreted-text
role="ref"} but filtered for a given object type.

The type argument must be in range
`[0; get_tracked_object_type_count - 1]`. If
`get_tracked_object_type_count()<class_RenderingDevice_method_get_tracked_object_type_count>`{.interpreted-text
role="ref"} is 0, then type argument is ignored and always returns 0.

This is only used by Vulkan in debug builds and can return 0 when this
information is not tracked or unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_driver_and_device_memory_report}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_driver_and_device_memory_report**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_driver_and_device_memory_report>`{.interpreted-text
role="ref"}

Returns string report in CSV format using the following methods:

- `get_tracked_object_name()<class_RenderingDevice_method_get_tracked_object_name>`{.interpreted-text
  role="ref"}
- `get_tracked_object_type_count()<class_RenderingDevice_method_get_tracked_object_type_count>`{.interpreted-text
  role="ref"}
- `get_driver_total_memory()<class_RenderingDevice_method_get_driver_total_memory>`{.interpreted-text
  role="ref"}
- `get_driver_allocation_count()<class_RenderingDevice_method_get_driver_allocation_count>`{.interpreted-text
  role="ref"}
- `get_driver_memory_by_object_type()<class_RenderingDevice_method_get_driver_memory_by_object_type>`{.interpreted-text
  role="ref"}
- `get_driver_allocs_by_object_type()<class_RenderingDevice_method_get_driver_allocs_by_object_type>`{.interpreted-text
  role="ref"}
- `get_device_total_memory()<class_RenderingDevice_method_get_device_total_memory>`{.interpreted-text
  role="ref"}
- `get_device_allocation_count()<class_RenderingDevice_method_get_device_allocation_count>`{.interpreted-text
  role="ref"}
- `get_device_memory_by_object_type()<class_RenderingDevice_method_get_device_memory_by_object_type>`{.interpreted-text
  role="ref"}
- `get_device_allocs_by_object_type()<class_RenderingDevice_method_get_device_allocs_by_object_type>`{.interpreted-text
  role="ref"}

This is only used by Vulkan in debug builds. Godot must also be started
with the `--extra-gpu-memory-tracking`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_driver_memory_by_object_type}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_driver_memory_by_object_type**(type:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_driver_memory_by_object_type>`{.interpreted-text
role="ref"}

Same as
`get_driver_total_memory()<class_RenderingDevice_method_get_driver_total_memory>`{.interpreted-text
role="ref"} but filtered for a given object type.

The type argument must be in range
`[0; get_tracked_object_type_count - 1]`. If
`get_tracked_object_type_count()<class_RenderingDevice_method_get_tracked_object_type_count>`{.interpreted-text
role="ref"} is 0, then type argument is ignored and always returns 0.

This is only used by Vulkan in debug builds and can return 0 when this
information is not tracked or unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_driver_resource}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_driver_resource**(resource:
`DriverResource<enum_RenderingDevice_DriverResource>`{.interpreted-text
role="ref"}, rid: `RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_get_driver_resource>`{.interpreted-text
role="ref"}

Returns the unique identifier of the driver `resource` for the specified
`rid`. Some driver resource types ignore the specified `rid`. `index` is
always ignored but must be specified anyway.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_driver_total_memory}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_driver_total_memory**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_driver_total_memory>`{.interpreted-text
role="ref"}

Returns how much bytes the GPU driver is using for internal driver
structures.

This is only used by Vulkan in debug builds and can return 0 when this
information is not tracked or unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_frame_delay}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_frame_delay**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_frame_delay>`{.interpreted-text
role="ref"}

Returns the frame count kept by the graphics API. Higher values result
in higher input lag, but with more consistent throughput. For the main
**RenderingDevice**, frames are cycled (usually 3 with triple-buffered
V-Sync enabled). However, local **RenderingDevice**s only have 1 frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_memory_usage}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_memory_usage**(type:
`MemoryType<enum_RenderingDevice_MemoryType>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_memory_usage>`{.interpreted-text
role="ref"}

Returns the memory usage in bytes corresponding to the given `type`.
When using Vulkan, these statistics are calculated by [Vulkan Memory
Allocator](https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_perf_report}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_perf_report**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_perf_report>`{.interpreted-text
role="ref"}

Returns a string with a performance report from the past frame. Updates
every frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_tracked_object_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tracked_object_name**(type_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_tracked_object_name>`{.interpreted-text
role="ref"}

Returns the name of the type of object for the given `type_index`. This
value must be in range `[0; get_tracked_object_type_count - 1]`. If
`get_tracked_object_type_count()<class_RenderingDevice_method_get_tracked_object_type_count>`{.interpreted-text
role="ref"} is 0, then type argument is ignored and always returns the
same string.

The return value is important because it gives meaning to the types
passed to
`get_driver_memory_by_object_type()<class_RenderingDevice_method_get_driver_memory_by_object_type>`{.interpreted-text
role="ref"},
`get_driver_allocs_by_object_type()<class_RenderingDevice_method_get_driver_allocs_by_object_type>`{.interpreted-text
role="ref"},
`get_device_memory_by_object_type()<class_RenderingDevice_method_get_device_memory_by_object_type>`{.interpreted-text
role="ref"}, and
`get_device_allocs_by_object_type()<class_RenderingDevice_method_get_device_allocs_by_object_type>`{.interpreted-text
role="ref"}. Examples of strings it can return (not exhaustive):

- DEVICE_MEMORY
- PIPELINE_CACHE
- SWAPCHAIN_KHR
- COMMAND_POOL

Thus if e.g. `get_tracked_object_name(5)` returns \"COMMAND_POOL\", then
`get_device_memory_by_object_type(5)` returns the bytes used by the GPU
for command pools.

This is only used by Vulkan in debug builds. Godot must also be started
with the `--extra-gpu-memory-tracking`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_get_tracked_object_type_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_tracked_object_type_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_get_tracked_object_type_count>`{.interpreted-text
role="ref"}

Returns how many types of trackable objects there are.

This is only used by Vulkan in debug builds. Godot must also be started
with the `--extra-gpu-memory-tracking`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_has_feature}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_feature**(feature:
`Features<enum_RenderingDevice_Features>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_has_feature>`{.interpreted-text
role="ref"}

Returns `true` if the `feature` is supported by the GPU.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_index_array_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**index_array_create**(index_buffer: `RID<class_RID>`{.interpreted-text
role="ref"}, index_offset: `int<class_int>`{.interpreted-text
role="ref"}, index_count: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_index_array_create>`{.interpreted-text
role="ref"}

Creates a new index array. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_index_buffer_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**index_buffer_create**(size_indices: `int<class_int>`{.interpreted-text
role="ref"}, format:
`IndexBufferFormat<enum_RenderingDevice_IndexBufferFormat>`{.interpreted-text
role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"} =
PackedByteArray(), use_restart_indices:
`bool<class_bool>`{.interpreted-text role="ref"} = false, creation_bits:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`BufferCreationBits<enum_RenderingDevice_BufferCreationBits>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_RenderingDevice_method_index_buffer_create>`{.interpreted-text
role="ref"}

Creates a new index buffer. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_limit_get}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **limit_get**(limit:
`Limit<enum_RenderingDevice_Limit>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_limit_get>`{.interpreted-text
role="ref"}

Returns the value of the specified `limit`. This limit varies depending
on the current graphics hardware (and sometimes the driver version). If
the given limit is exceeded, rendering errors will occur.

Limits for various graphics hardware can be found in the [Vulkan
Hardware Database](https://vulkan.gpuinfo.org/).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_render_pipeline_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**render_pipeline_create**(shader: `RID<class_RID>`{.interpreted-text
role="ref"}, framebuffer_format: `int<class_int>`{.interpreted-text
role="ref"}, vertex_format: `int<class_int>`{.interpreted-text
role="ref"}, primitive:
`RenderPrimitive<enum_RenderingDevice_RenderPrimitive>`{.interpreted-text
role="ref"}, rasterization_state:
`RDPipelineRasterizationState<class_RDPipelineRasterizationState>`{.interpreted-text
role="ref"}, multisample_state:
`RDPipelineMultisampleState<class_RDPipelineMultisampleState>`{.interpreted-text
role="ref"}, stencil_state:
`RDPipelineDepthStencilState<class_RDPipelineDepthStencilState>`{.interpreted-text
role="ref"}, color_blend_state:
`RDPipelineColorBlendState<class_RDPipelineColorBlendState>`{.interpreted-text
role="ref"}, dynamic_state_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`PipelineDynamicStateFlags<enum_RenderingDevice_PipelineDynamicStateFlags>`{.interpreted-text
role="ref"}\] = 0, for_render_pass: `int<class_int>`{.interpreted-text
role="ref"} = 0, specialization_constants:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RDPipelineSpecializationConstant<class_RDPipelineSpecializationConstant>`{.interpreted-text
role="ref"}\] = \[\])
`🔗<class_RenderingDevice_method_render_pipeline_create>`{.interpreted-text
role="ref"}

Creates a new render pipeline. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_render_pipeline_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**render_pipeline_is_valid**(render_pipeline:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_render_pipeline_is_valid>`{.interpreted-text
role="ref"}

Returns `true` if the render pipeline specified by the `render_pipeline`
RID is valid, `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_sampler_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **sampler_create**(state:
`RDSamplerState<class_RDSamplerState>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_sampler_create>`{.interpreted-text
role="ref"}

Creates a new sampler. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_sampler_is_format_supported_for_filter}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**sampler_is_format_supported_for_filter**(format:
`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"}, sampler_filter:
`SamplerFilter<enum_RenderingDevice_SamplerFilter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_sampler_is_format_supported_for_filter>`{.interpreted-text
role="ref"}

Returns `true` if implementation supports using a texture of `format`
with the given `sampler_filter`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_screen_get_framebuffer_format}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**screen_get_framebuffer_format**(screen:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_screen_get_framebuffer_format>`{.interpreted-text
role="ref"}

Returns the framebuffer format of the given screen.

\*\*Note:\*\* Only the main **RenderingDevice** returned by
`RenderingServer.get_rendering_device()<class_RenderingServer_method_get_rendering_device>`{.interpreted-text
role="ref"} has a format. If called on a local **RenderingDevice**, this
method prints an error and returns
`INVALID_ID<class_RenderingDevice_constant_INVALID_ID>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_screen_get_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**screen_get_height**(screen: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_screen_get_height>`{.interpreted-text
role="ref"}

Returns the window height matching the graphics API context for the
given window ID (in pixels). Despite the parameter being named `screen`,
this returns the *window* size. See also
`screen_get_width()<class_RenderingDevice_method_screen_get_width>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only the main **RenderingDevice** returned by
`RenderingServer.get_rendering_device()<class_RenderingServer_method_get_rendering_device>`{.interpreted-text
role="ref"} has a height. If called on a local **RenderingDevice**, this
method prints an error and returns
`INVALID_ID<class_RenderingDevice_constant_INVALID_ID>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_screen_get_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**screen_get_width**(screen: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_screen_get_width>`{.interpreted-text
role="ref"}

Returns the window width matching the graphics API context for the given
window ID (in pixels). Despite the parameter being named `screen`, this
returns the *window* size. See also
`screen_get_height()<class_RenderingDevice_method_screen_get_height>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only the main **RenderingDevice** returned by
`RenderingServer.get_rendering_device()<class_RenderingServer_method_get_rendering_device>`{.interpreted-text
role="ref"} has a width. If called on a local **RenderingDevice**, this
method prints an error and returns
`INVALID_ID<class_RenderingDevice_constant_INVALID_ID>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_set_resource_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_resource_name**(id: `RID<class_RID>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_set_resource_name>`{.interpreted-text
role="ref"}

Sets the resource name for `id` to `name`. This is used for debugging
with third-party tools such as [RenderDoc](https://renderdoc.org/).

The following types of resources can be named: texture, sampler, vertex
buffer, index buffer, uniform buffer, texture buffer, storage buffer,
uniform set buffer, shader, render pipeline and compute pipeline.
Framebuffers cannot be named. Attempting to name an incompatible
resource type will print an error.

\*\*Note:\*\* Resource names are only set when the engine runs in
verbose mode
(`OS.is_stdout_verbose()<class_OS_method_is_stdout_verbose>`{.interpreted-text
role="ref"} = `true`), or when using an engine build compiled with the
`dev_mode=yes` SCons option. The graphics driver must also support the
`VK_EXT_DEBUG_UTILS_EXTENSION_NAME` Vulkan extension for named resources
to work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_shader_compile_binary_from_spirv}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**shader_compile_binary_from_spirv**(spirv_data:
`RDShaderSPIRV<class_RDShaderSPIRV>`{.interpreted-text role="ref"},
name: `String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_RenderingDevice_method_shader_compile_binary_from_spirv>`{.interpreted-text
role="ref"}

Compiles a binary shader from `spirv_data` and returns the compiled
binary data as a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.
This compiled shader is specific to the GPU model and driver version
used; it will not work on different GPU models or even different driver
versions. See also
`shader_compile_spirv_from_source()<class_RenderingDevice_method_shader_compile_spirv_from_source>`{.interpreted-text
role="ref"}.

`name` is an optional human-readable name that can be given to the
compiled shader for organizational purposes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_shader_compile_spirv_from_source}
::: rst-class
classref-method
:::
::::

`RDShaderSPIRV<class_RDShaderSPIRV>`{.interpreted-text role="ref"}
**shader_compile_spirv_from_source**(shader_source:
`RDShaderSource<class_RDShaderSource>`{.interpreted-text role="ref"},
allow_cache: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_RenderingDevice_method_shader_compile_spirv_from_source>`{.interpreted-text
role="ref"}

Compiles a SPIR-V from the shader source code in `shader_source` and
returns the SPIR-V as an
`RDShaderSPIRV<class_RDShaderSPIRV>`{.interpreted-text role="ref"}. This
intermediate language shader is portable across different GPU models and
driver versions, but cannot be run directly by GPUs until compiled into
a binary shader using
`shader_compile_binary_from_spirv()<class_RenderingDevice_method_shader_compile_binary_from_spirv>`{.interpreted-text
role="ref"}.

If `allow_cache` is `true`, make use of the shader cache generated by
Godot. This avoids a potentially lengthy shader compilation step if the
shader is already in cache. If `allow_cache` is `false`, Godot\'s shader
cache is ignored and the shader will always be recompiled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_shader_create_from_bytecode}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**shader_create_from_bytecode**(binary_data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
placeholder_rid: `RID<class_RID>`{.interpreted-text role="ref"} = RID())
`🔗<class_RenderingDevice_method_shader_create_from_bytecode>`{.interpreted-text
role="ref"}

Creates a new shader instance from a binary compiled shader. It can be
accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method. See also
`shader_compile_binary_from_spirv()<class_RenderingDevice_method_shader_compile_binary_from_spirv>`{.interpreted-text
role="ref"} and
`shader_create_from_spirv()<class_RenderingDevice_method_shader_create_from_spirv>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_shader_create_from_spirv}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**shader_create_from_spirv**(spirv_data:
`RDShaderSPIRV<class_RDShaderSPIRV>`{.interpreted-text role="ref"},
name: `String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_RenderingDevice_method_shader_create_from_spirv>`{.interpreted-text
role="ref"}

Creates a new shader instance from SPIR-V intermediate code. It can be
accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method. See also
`shader_compile_spirv_from_source()<class_RenderingDevice_method_shader_compile_spirv_from_source>`{.interpreted-text
role="ref"} and
`shader_create_from_bytecode()<class_RenderingDevice_method_shader_create_from_bytecode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_shader_create_placeholder}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**shader_create_placeholder**()
`🔗<class_RenderingDevice_method_shader_create_placeholder>`{.interpreted-text
role="ref"}

Create a placeholder RID by allocating an RID without initializing it
for use in
`shader_create_from_bytecode()<class_RenderingDevice_method_shader_create_from_bytecode>`{.interpreted-text
role="ref"}. This allows you to create an RID for a shader and pass it
around, but defer compiling the shader to a later time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_shader_get_vertex_input_attribute_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shader_get_vertex_input_attribute_mask**(shader:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_shader_get_vertex_input_attribute_mask>`{.interpreted-text
role="ref"}

Returns the internal vertex input mask. Internally, the vertex input
mask is an unsigned integer consisting of the locations (specified in
GLSL via. `layout(location = ...)`) of the input variables (specified in
GLSL by the `in` keyword).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_storage_buffer_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**storage_buffer_create**(size_bytes: `int<class_int>`{.interpreted-text
role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"} =
PackedByteArray(), usage:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`StorageBufferUsage<enum_RenderingDevice_StorageBufferUsage>`{.interpreted-text
role="ref"}\] = 0, creation_bits:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`BufferCreationBits<enum_RenderingDevice_BufferCreationBits>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_RenderingDevice_method_storage_buffer_create>`{.interpreted-text
role="ref"}

Creates a [storage
buffer](https://vkguide.dev/docs/chapter-4/storage_buffers/) with the
specified `data` and `usage`. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_submit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **submit**()
`🔗<class_RenderingDevice_method_submit>`{.interpreted-text role="ref"}

Pushes the frame setup and draw command buffers then marks the local
device as currently processing (which allows calling
`sync()<class_RenderingDevice_method_sync>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* Only available in local RenderingDevices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_sync}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **sync**()
`🔗<class_RenderingDevice_method_sync>`{.interpreted-text role="ref"}

Forces a synchronization between the CPU and GPU, which may be required
in certain cases. Only call this when needed, as CPU-GPU synchronization
has a performance cost.

\*\*Note:\*\* Only available in local RenderingDevices.

\*\*Note:\*\*
`sync()<class_RenderingDevice_method_sync>`{.interpreted-text
role="ref"} can only be called after a
`submit()<class_RenderingDevice_method_submit>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_buffer_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_buffer_create**(size_bytes: `int<class_int>`{.interpreted-text
role="ref"}, format:
`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"} =
PackedByteArray())
`🔗<class_RenderingDevice_method_texture_buffer_create>`{.interpreted-text
role="ref"}

Creates a new texture buffer. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_clear}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**texture_clear**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"},
base_mipmap: `int<class_int>`{.interpreted-text role="ref"},
mipmap_count: `int<class_int>`{.interpreted-text role="ref"},
base_layer: `int<class_int>`{.interpreted-text role="ref"}, layer_count:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_texture_clear>`{.interpreted-text
role="ref"}

Clears the specified `texture` by replacing all of its pixels with the
specified `color`. `base_mipmap` and `mipmap_count` determine which
mipmaps of the texture are affected by this clear operation, while
`base_layer` and `layer_count` determine which layers of a 3D texture
(or texture array) are affected by this clear operation. For 2D textures
(which only have one layer by design), `base_layer` must be `0` and
`layer_count` must be `1`.

\*\*Note:\*\* `texture` can\'t be cleared while a draw list that uses it
as part of a framebuffer is being created. Ensure the draw list is
finalized (and that the color/depth texture using it is not set to
`FINAL_ACTION_CONTINUE<class_RenderingDevice_constant_FINAL_ACTION_CONTINUE>`{.interpreted-text
role="ref"}) to clear this texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_copy}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**texture_copy**(from_texture: `RID<class_RID>`{.interpreted-text
role="ref"}, to_texture: `RID<class_RID>`{.interpreted-text role="ref"},
from_pos: `Vector3<class_Vector3>`{.interpreted-text role="ref"},
to_pos: `Vector3<class_Vector3>`{.interpreted-text role="ref"}, size:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, src_mipmap:
`int<class_int>`{.interpreted-text role="ref"}, dst_mipmap:
`int<class_int>`{.interpreted-text role="ref"}, src_layer:
`int<class_int>`{.interpreted-text role="ref"}, dst_layer:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_texture_copy>`{.interpreted-text
role="ref"}

Copies the `from_texture` to `to_texture` with the specified `from_pos`,
`to_pos` and `size` coordinates. The Z axis of the `from_pos`, `to_pos`
and `size` must be `0` for 2-dimensional textures. Source and
destination mipmaps/layers must also be specified, with these parameters
being `0` for textures without mipmaps or single-layer textures. Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if the texture copy was successful or
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} otherwise.

\*\*Note:\*\* `from_texture` texture can\'t be copied while a draw list
that uses it as part of a framebuffer is being created. Ensure the draw
list is finalized (and that the color/depth texture using it is not set
to
`FINAL_ACTION_CONTINUE<class_RenderingDevice_constant_FINAL_ACTION_CONTINUE>`{.interpreted-text
role="ref"}) to copy this texture.

\*\*Note:\*\* `from_texture` texture requires the
`TEXTURE_USAGE_CAN_COPY_FROM_BIT<class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_FROM_BIT>`{.interpreted-text
role="ref"} to be retrieved.

\*\*Note:\*\* `to_texture` can\'t be copied while a draw list that uses
it as part of a framebuffer is being created. Ensure the draw list is
finalized (and that the color/depth texture using it is not set to
`FINAL_ACTION_CONTINUE<class_RenderingDevice_constant_FINAL_ACTION_CONTINUE>`{.interpreted-text
role="ref"}) to copy this texture.

\*\*Note:\*\* `to_texture` requires the
`TEXTURE_USAGE_CAN_COPY_TO_BIT<class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_TO_BIT>`{.interpreted-text
role="ref"} to be retrieved.

\*\*Note:\*\* `from_texture` and `to_texture` must be of the same type
(color or depth).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_create**(format:
`RDTextureFormat<class_RDTextureFormat>`{.interpreted-text role="ref"},
view: `RDTextureView<class_RDTextureView>`{.interpreted-text
role="ref"}, data: `Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}\] = \[\])
`🔗<class_RenderingDevice_method_texture_create>`{.interpreted-text
role="ref"}

Creates a new texture. It can be accessed with the RID that is returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* `data` takes an `Array<class_Array>`{.interpreted-text
role="ref"} of
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}s.
For
`TEXTURE_TYPE_1D<class_RenderingDevice_constant_TEXTURE_TYPE_1D>`{.interpreted-text
role="ref"},
`TEXTURE_TYPE_2D<class_RenderingDevice_constant_TEXTURE_TYPE_2D>`{.interpreted-text
role="ref"}, and
`TEXTURE_TYPE_3D<class_RenderingDevice_constant_TEXTURE_TYPE_3D>`{.interpreted-text
role="ref"} types, this array should only have one element, a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
containing all the data for the texture. For `_ARRAY` and `_CUBE` types,
the length should be the same as the number of
`RDTextureFormat.array_layers<class_RDTextureFormat_property_array_layers>`{.interpreted-text
role="ref"} in `format`.

\*\*Note:\*\* Not to be confused with
`RenderingServer.texture_2d_create()<class_RenderingServer_method_texture_2d_create>`{.interpreted-text
role="ref"}, which creates the Godot-specific
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} resource as
opposed to the graphics API\'s own texture type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_create_from_extension}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_create_from_extension**(type:
`TextureType<enum_RenderingDevice_TextureType>`{.interpreted-text
role="ref"}, format:
`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"}, samples:
`TextureSamples<enum_RenderingDevice_TextureSamples>`{.interpreted-text
role="ref"}, usage_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"}\], image: `int<class_int>`{.interpreted-text role="ref"},
width: `int<class_int>`{.interpreted-text role="ref"}, height:
`int<class_int>`{.interpreted-text role="ref"}, depth:
`int<class_int>`{.interpreted-text role="ref"}, layers:
`int<class_int>`{.interpreted-text role="ref"}, mipmaps:
`int<class_int>`{.interpreted-text role="ref"} = 1)
`🔗<class_RenderingDevice_method_texture_create_from_extension>`{.interpreted-text
role="ref"}

Returns an RID for an existing `image` (`VkImage`) with the given
`type`, `format`, `samples`, `usage_flags`, `width`, `height`, `depth`,
`layers`, and `mipmaps`. This can be used to allow Godot to render onto
foreign images.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_create_shared}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_create_shared**(view:
`RDTextureView<class_RDTextureView>`{.interpreted-text role="ref"},
with_texture: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_texture_create_shared>`{.interpreted-text
role="ref"}

Creates a shared texture using the specified `view` and the texture
information from `with_texture`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_create_shared_from_slice}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**texture_create_shared_from_slice**(view:
`RDTextureView<class_RDTextureView>`{.interpreted-text role="ref"},
with_texture: `RID<class_RID>`{.interpreted-text role="ref"}, layer:
`int<class_int>`{.interpreted-text role="ref"}, mipmap:
`int<class_int>`{.interpreted-text role="ref"}, mipmaps:
`int<class_int>`{.interpreted-text role="ref"} = 1, slice_type:
`TextureSliceType<enum_RenderingDevice_TextureSliceType>`{.interpreted-text
role="ref"} = 0)
`🔗<class_RenderingDevice_method_texture_create_shared_from_slice>`{.interpreted-text
role="ref"}

Creates a shared texture using the specified `view` and the texture
information from `with_texture`\'s `layer` and `mipmap`. The number of
included mipmaps from the original texture can be controlled using the
`mipmaps` parameter. Only relevant for textures with multiple layers,
such as 3D textures, texture arrays and cubemaps. For single-layer
textures, use
`texture_create_shared()<class_RenderingDevice_method_texture_create_shared>`{.interpreted-text
role="ref"}.

For 2D textures (which only have one layer), `layer` must be `0`.

\*\*Note:\*\* Layer slicing is only supported for 2D texture arrays, not
3D textures or cubemaps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_get_data}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**texture_get_data**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_texture_get_data>`{.interpreted-text
role="ref"}

Returns the `texture` data for the specified `layer` as raw binary data.
For 2D textures (which only have one layer), `layer` must be `0`.

\*\*Note:\*\* `texture` can\'t be retrieved while a draw list that uses
it as part of a framebuffer is being created. Ensure the draw list is
finalized (and that the color/depth texture using it is not set to
`FINAL_ACTION_CONTINUE<class_RenderingDevice_constant_FINAL_ACTION_CONTINUE>`{.interpreted-text
role="ref"}) to retrieve this texture. Otherwise, an error is printed
and an empty `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"} is returned.

\*\*Note:\*\* `texture` requires the
`TEXTURE_USAGE_CAN_COPY_FROM_BIT<class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_FROM_BIT>`{.interpreted-text
role="ref"} to be retrieved. Otherwise, an error is printed and an empty
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
is returned.

\*\*Note:\*\* This method will block the GPU from working until the data
is retrieved. Refer to
`texture_get_data_async()<class_RenderingDevice_method_texture_get_data_async>`{.interpreted-text
role="ref"} for an alternative that returns the data in more performant
way.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_get_data_async}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**texture_get_data_async**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"},
callback: `Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_texture_get_data_async>`{.interpreted-text
role="ref"}

Asynchronous version of
`texture_get_data()<class_RenderingDevice_method_texture_get_data>`{.interpreted-text
role="ref"}. RenderingDevice will call `callback` in a certain amount of
frames with the data the texture had at the time of the request.

\*\*Note:\*\* At the moment, the delay corresponds to the amount of
frames specified by
`ProjectSettings.rendering/rendering_device/vsync/frame_queue_size<class_ProjectSettings_property_rendering/rendering_device/vsync/frame_queue_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Downloading large textures can have a prohibitive cost for
real-time even when using the asynchronous method due to hardware
bandwidth limitations. When dealing with large resources, you can adjust
settings such as
`ProjectSettings.rendering/rendering_device/staging_buffer/texture_download_region_size_px<class_ProjectSettings_property_rendering/rendering_device/staging_buffer/texture_download_region_size_px>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/rendering_device/staging_buffer/block_size_kb<class_ProjectSettings_property_rendering/rendering_device/staging_buffer/block_size_kb>`{.interpreted-text
role="ref"} to improve the transfer speed at the cost of extra memory.

    func _texture_get_data_callback(array):
        value = array.decode_u32(0)

    ...

    rd.texture_get_data_async(texture, 0, _texture_get_data_callback)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_get_format}
::: rst-class
classref-method
:::
::::

`RDTextureFormat<class_RDTextureFormat>`{.interpreted-text role="ref"}
**texture_get_format**(texture: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_texture_get_format>`{.interpreted-text
role="ref"}

Returns the data format used to create this texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_get_native_handle}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**texture_get_native_handle**(texture:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_texture_get_native_handle>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`get_driver_resource()<class_RenderingDevice_method_get_driver_resource>`{.interpreted-text
role="ref"} with
`DRIVER_RESOURCE_TEXTURE<class_RenderingDevice_constant_DRIVER_RESOURCE_TEXTURE>`{.interpreted-text
role="ref"} instead.

Returns the internal graphics handle for this texture object. For use
when communicating with third-party APIs mostly with GDExtension.

\*\*Note:\*\* This function returns a `uint64_t` which internally maps
to a `GLuint` (OpenGL) or `VkImage` (Vulkan).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_is_discardable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**texture_is_discardable**(texture: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_texture_is_discardable>`{.interpreted-text
role="ref"}

Returns `true` if the `texture` is discardable, `false` otherwise. See
`RDTextureFormat<class_RDTextureFormat>`{.interpreted-text role="ref"}
or
`texture_set_discardable()<class_RenderingDevice_method_texture_set_discardable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_is_format_supported_for_usage}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**texture_is_format_supported_for_usage**(format:
`DataFormat<enum_RenderingDevice_DataFormat>`{.interpreted-text
role="ref"}, usage_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`{.interpreted-text
role="ref"}\])
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RenderingDevice_method_texture_is_format_supported_for_usage>`{.interpreted-text
role="ref"}

Returns `true` if the specified `format` is supported for the given
`usage_flags`, `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_is_shared}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**texture_is_shared**(texture: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_texture_is_shared>`{.interpreted-text
role="ref"}

Returns `true` if the `texture` is shared, `false` otherwise. See
`RDTextureView<class_RDTextureView>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**texture_is_valid**(texture: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_texture_is_valid>`{.interpreted-text
role="ref"}

Returns `true` if the `texture` is valid, `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_resolve_multisample}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**texture_resolve_multisample**(from_texture:
`RID<class_RID>`{.interpreted-text role="ref"}, to_texture:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_texture_resolve_multisample>`{.interpreted-text
role="ref"}

Resolves the `from_texture` texture onto `to_texture` with multisample
antialiasing enabled. This must be used when rendering a framebuffer for
MSAA to work. Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if successful,
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} otherwise.

\*\*Note:\*\* `from_texture` and `to_texture` textures must have the
same dimension, format and type (color or depth).

\*\*Note:\*\* `from_texture` can\'t be copied while a draw list that
uses it as part of a framebuffer is being created. Ensure the draw list
is finalized (and that the color/depth texture using it is not set to
`FINAL_ACTION_CONTINUE<class_RenderingDevice_constant_FINAL_ACTION_CONTINUE>`{.interpreted-text
role="ref"}) to resolve this texture.

\*\*Note:\*\* `from_texture` requires the
`TEXTURE_USAGE_CAN_COPY_FROM_BIT<class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_FROM_BIT>`{.interpreted-text
role="ref"} to be retrieved.

\*\*Note:\*\* `from_texture` must be multisampled and must also be 2D
(or a slice of a 3D/cubemap texture).

\*\*Note:\*\* `to_texture` can\'t be copied while a draw list that uses
it as part of a framebuffer is being created. Ensure the draw list is
finalized (and that the color/depth texture using it is not set to
`FINAL_ACTION_CONTINUE<class_RenderingDevice_constant_FINAL_ACTION_CONTINUE>`{.interpreted-text
role="ref"}) to resolve this texture.

\*\*Note:\*\* `to_texture` texture requires the
`TEXTURE_USAGE_CAN_COPY_TO_BIT<class_RenderingDevice_constant_TEXTURE_USAGE_CAN_COPY_TO_BIT>`{.interpreted-text
role="ref"} to be retrieved.

\*\*Note:\*\* `to_texture` texture must **not** be multisampled and must
also be 2D (or a slice of a 3D/cubemap texture).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_set_discardable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**texture_set_discardable**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, discardable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_texture_set_discardable>`{.interpreted-text
role="ref"}

Updates the discardable property of `texture`.

If a texture is discardable, its contents do not need to be preserved
between frames. This flag is only relevant when the texture is used as
target in a draw list.

This information is used by **RenderingDevice** to figure out if a
texture\'s contents can be discarded, eliminating unnecessary writes to
memory and boosting performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_texture_update}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**texture_update**(texture: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"},
data: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_texture_update>`{.interpreted-text
role="ref"}

Updates texture data with new data, replacing the previous data in
place. The updated texture data must have the same dimensions and
format. For 2D textures (which only have one layer), `layer` must be
`0`. Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if the update was successful,
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} otherwise.

\*\*Note:\*\* Updating textures is forbidden during creation of a draw
or compute list.

\*\*Note:\*\* The existing `texture` can\'t be updated while a draw list
that uses it as part of a framebuffer is being created. Ensure the draw
list is finalized (and that the color/depth texture using it is not set
to
`FINAL_ACTION_CONTINUE<class_RenderingDevice_constant_FINAL_ACTION_CONTINUE>`{.interpreted-text
role="ref"}) to update this texture.

\*\*Note:\*\* The existing `texture` requires the
`TEXTURE_USAGE_CAN_UPDATE_BIT<class_RenderingDevice_constant_TEXTURE_USAGE_CAN_UPDATE_BIT>`{.interpreted-text
role="ref"} to be updatable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_uniform_buffer_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**uniform_buffer_create**(size_bytes: `int<class_int>`{.interpreted-text
role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"} =
PackedByteArray(), creation_bits:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`BufferCreationBits<enum_RenderingDevice_BufferCreationBits>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_RenderingDevice_method_uniform_buffer_create>`{.interpreted-text
role="ref"}

Creates a new uniform buffer. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_uniform_set_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**uniform_set_create**(uniforms: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RDUniform<class_RDUniform>`{.interpreted-text
role="ref"}\], shader: `RID<class_RID>`{.interpreted-text role="ref"},
shader_set: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RenderingDevice_method_uniform_set_create>`{.interpreted-text
role="ref"}

Creates a new uniform set. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_uniform_set_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**uniform_set_is_valid**(uniform_set: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_RenderingDevice_method_uniform_set_is_valid>`{.interpreted-text
role="ref"}

Checks if the `uniform_set` is valid, i.e. is owned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_vertex_array_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**vertex_array_create**(vertex_count: `int<class_int>`{.interpreted-text
role="ref"}, vertex_format: `int<class_int>`{.interpreted-text
role="ref"}, src_buffers: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\], offsets:
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
= PackedInt64Array())
`🔗<class_RenderingDevice_method_vertex_array_create>`{.interpreted-text
role="ref"}

Creates a vertex array based on the specified buffers. Optionally,
`offsets` (in bytes) may be defined for each buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_vertex_buffer_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**vertex_buffer_create**(size_bytes: `int<class_int>`{.interpreted-text
role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"} =
PackedByteArray(), creation_bits:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`BufferCreationBits<enum_RenderingDevice_BufferCreationBits>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_RenderingDevice_method_vertex_buffer_create>`{.interpreted-text
role="ref"}

Creates a new vertex buffer. It can be accessed with the RID that is
returned.

Once finished with your RID, you will want to free the RID using the
RenderingDevice\'s
`free_rid()<class_RenderingDevice_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderingDevice_method_vertex_format_create}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**vertex_format_create**(vertex_descriptions:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RDVertexAttribute<class_RDVertexAttribute>`{.interpreted-text
role="ref"}\])
`🔗<class_RenderingDevice_method_vertex_format_create>`{.interpreted-text
role="ref"}

Creates a new vertex format with the specified `vertex_descriptions`.
Returns a unique vertex format ID corresponding to the newly created
vertex format.
