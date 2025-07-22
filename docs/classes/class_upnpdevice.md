github_url
:   hide

# UPNPDevice {#class_UPNPDevice}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Universal Plug and Play (UPnP) device.

::: rst-class
classref-introduction-group
:::

## Description

Universal Plug and Play (UPnP) device. See
`UPNP<class_UPNP>`{.interpreted-text role="ref"} for UPnP discovery and
utility functions. Provides low-level access to UPNP control commands.
Allows to manage port mappings (port forwarding) and to query network
information of the device (like local and external IP address and
status). Note that methods on this class are synchronous and block the
calling thread.

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

## Enumerations

:::: {#enum_UPNPDevice_IGDStatus}
::: rst-class
classref-enumeration
:::
::::

enum **IGDStatus**: `🔗<enum_UPNPDevice_IGDStatus>`{.interpreted-text
role="ref"}

:::: {#class_UPNPDevice_constant_IGD_STATUS_OK}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_OK** = `0`

OK.

:::: {#class_UPNPDevice_constant_IGD_STATUS_HTTP_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_HTTP_ERROR** = `1`

HTTP error.

:::: {#class_UPNPDevice_constant_IGD_STATUS_HTTP_EMPTY}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_HTTP_EMPTY** = `2`

Empty HTTP response.

:::: {#class_UPNPDevice_constant_IGD_STATUS_NO_URLS}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_NO_URLS** = `3`

**Deprecated:** This value is no longer used.

Returned response contained no URLs.

:::: {#class_UPNPDevice_constant_IGD_STATUS_NO_IGD}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_NO_IGD** = `4`

Not a valid IGD.

:::: {#class_UPNPDevice_constant_IGD_STATUS_DISCONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_DISCONNECTED** = `5`

Disconnected.

:::: {#class_UPNPDevice_constant_IGD_STATUS_UNKNOWN_DEVICE}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_UNKNOWN_DEVICE** = `6`

Unknown device.

:::: {#class_UPNPDevice_constant_IGD_STATUS_INVALID_CONTROL}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_INVALID_CONTROL** = `7`

Invalid control.

:::: {#class_UPNPDevice_constant_IGD_STATUS_MALLOC_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_MALLOC_ERROR** = `8`

**Deprecated:** This value is no longer used.

Memory allocation error.

:::: {#class_UPNPDevice_constant_IGD_STATUS_UNKNOWN_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**IGD_STATUS_UNKNOWN_ERROR** = `9`

Unknown error.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_UPNPDevice_property_description_url}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **description_url**
= `""` `🔗<class_UPNPDevice_property_description_url>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_description_url**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_description_url**()

URL to the device description.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UPNPDevice_property_igd_control_url}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **igd_control_url**
= `""` `🔗<class_UPNPDevice_property_igd_control_url>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_igd_control_url**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_igd_control_url**()

IDG control URL.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UPNPDevice_property_igd_our_addr}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **igd_our_addr** =
`""` `🔗<class_UPNPDevice_property_igd_our_addr>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_igd_our_addr**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_igd_our_addr**()

Address of the local machine in the network connecting it to this
**UPNPDevice**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UPNPDevice_property_igd_service_type}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**igd_service_type** = `""`
`🔗<class_UPNPDevice_property_igd_service_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_igd_service_type**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_igd_service_type**()

IGD service type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UPNPDevice_property_igd_status}
::: rst-class
classref-property
:::
::::

`IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
**igd_status** = `9`
`🔗<class_UPNPDevice_property_igd_status>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_igd_status**(value:
  `IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"})
- `IGDStatus<enum_UPNPDevice_IGDStatus>`{.interpreted-text role="ref"}
  **get_igd_status**()

IGD status.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UPNPDevice_property_service_type}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **service_type** =
`""` `🔗<class_UPNPDevice_property_service_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_service_type**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_service_type**()

Service type.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_UPNPDevice_method_add_port_mapping}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**add_port_mapping**(port: `int<class_int>`{.interpreted-text
role="ref"}, port_internal: `int<class_int>`{.interpreted-text
role="ref"} = 0, desc: `String<class_String>`{.interpreted-text
role="ref"} = \"\", proto: `String<class_String>`{.interpreted-text
role="ref"} = \"UDP\", duration: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_UPNPDevice_method_add_port_mapping>`{.interpreted-text
role="ref"}

Adds a port mapping to forward the given external port on this
**UPNPDevice** for the given protocol to the local machine. See
`UPNP.add_port_mapping()<class_UPNP_method_add_port_mapping>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UPNPDevice_method_delete_port_mapping}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**delete_port_mapping**(port: `int<class_int>`{.interpreted-text
role="ref"}, proto: `String<class_String>`{.interpreted-text role="ref"}
= \"UDP\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_UPNPDevice_method_delete_port_mapping>`{.interpreted-text
role="ref"}

Deletes the port mapping identified by the given port and protocol
combination on this device. See
`UPNP.delete_port_mapping()<class_UPNP_method_delete_port_mapping>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UPNPDevice_method_is_valid_gateway}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_valid_gateway**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_UPNPDevice_method_is_valid_gateway>`{.interpreted-text
role="ref"}

Returns `true` if this is a valid IGD (InternetGatewayDevice) which
potentially supports port forwarding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UPNPDevice_method_query_external_address}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**query_external_address**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_UPNPDevice_method_query_external_address>`{.interpreted-text
role="ref"}

Returns the external IP address of this **UPNPDevice** or an empty
string.
