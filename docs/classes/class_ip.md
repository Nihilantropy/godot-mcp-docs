github_url
:   hide

::: {.meta keywords="dns"}
:::

# IP {#class_IP}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Internet protocol (IP) support functions such as DNS resolution.

::: rst-class
classref-introduction-group
:::

## Description

IP contains support functions for the Internet Protocol (IP). TCP/IP
support is in different classes (see
`StreamPeerTCP<class_StreamPeerTCP>`{.interpreted-text role="ref"} and
`TCPServer<class_TCPServer>`{.interpreted-text role="ref"}). IP provides
DNS hostname resolution support, both blocking and threaded.

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

:::: {#enum_IP_ResolverStatus}
::: rst-class
classref-enumeration
:::
::::

enum **ResolverStatus**: `🔗<enum_IP_ResolverStatus>`{.interpreted-text
role="ref"}

:::: {#class_IP_constant_RESOLVER_STATUS_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResolverStatus<enum_IP_ResolverStatus>`{.interpreted-text role="ref"}
**RESOLVER_STATUS_NONE** = `0`

DNS hostname resolver status: No status.

:::: {#class_IP_constant_RESOLVER_STATUS_WAITING}
::: rst-class
classref-enumeration-constant
:::
::::

`ResolverStatus<enum_IP_ResolverStatus>`{.interpreted-text role="ref"}
**RESOLVER_STATUS_WAITING** = `1`

DNS hostname resolver status: Waiting.

:::: {#class_IP_constant_RESOLVER_STATUS_DONE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResolverStatus<enum_IP_ResolverStatus>`{.interpreted-text role="ref"}
**RESOLVER_STATUS_DONE** = `2`

DNS hostname resolver status: Done.

:::: {#class_IP_constant_RESOLVER_STATUS_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`ResolverStatus<enum_IP_ResolverStatus>`{.interpreted-text role="ref"}
**RESOLVER_STATUS_ERROR** = `3`

DNS hostname resolver status: Error.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_IP_Type}
::: rst-class
classref-enumeration
:::
::::

enum **Type**: `🔗<enum_IP_Type>`{.interpreted-text role="ref"}

:::: {#class_IP_constant_TYPE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_IP_Type>`{.interpreted-text role="ref"} **TYPE_NONE** = `0`

Address type: None.

:::: {#class_IP_constant_TYPE_IPV4}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_IP_Type>`{.interpreted-text role="ref"} **TYPE_IPV4** = `1`

Address type: Internet protocol version 4 (IPv4).

:::: {#class_IP_constant_TYPE_IPV6}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_IP_Type>`{.interpreted-text role="ref"} **TYPE_IPV6** = `2`

Address type: Internet protocol version 6 (IPv6).

:::: {#class_IP_constant_TYPE_ANY}
::: rst-class
classref-enumeration-constant
:::
::::

`Type<enum_IP_Type>`{.interpreted-text role="ref"} **TYPE_ANY** = `3`

Address type: Any.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_IP_constant_RESOLVER_MAX_QUERIES}
::: rst-class
classref-constant
:::
::::

**RESOLVER_MAX_QUERIES** = `256`
`🔗<class_IP_constant_RESOLVER_MAX_QUERIES>`{.interpreted-text
role="ref"}

Maximum number of concurrent DNS resolver queries allowed,
`RESOLVER_INVALID_ID<class_IP_constant_RESOLVER_INVALID_ID>`{.interpreted-text
role="ref"} is returned if exceeded.

:::: {#class_IP_constant_RESOLVER_INVALID_ID}
::: rst-class
classref-constant
:::
::::

**RESOLVER_INVALID_ID** = `-1`
`🔗<class_IP_constant_RESOLVER_INVALID_ID>`{.interpreted-text
role="ref"}

Invalid ID constant. Returned if
`RESOLVER_MAX_QUERIES<class_IP_constant_RESOLVER_MAX_QUERIES>`{.interpreted-text
role="ref"} is exceeded.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_IP_method_clear_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_cache**(hostname: `String<class_String>`{.interpreted-text
role="ref"} = \"\") `🔗<class_IP_method_clear_cache>`{.interpreted-text
role="ref"}

Removes all of a `hostname`\'s cached references. If no `hostname` is
given, all cached IP addresses are removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_IP_method_erase_resolve_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_resolve_item**(id: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_IP_method_erase_resolve_item>`{.interpreted-text
role="ref"}

Removes a given item `id` from the queue. This should be used to free a
queue after it has completed to enable more queries to happen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_IP_method_get_local_addresses}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_local_addresses**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_IP_method_get_local_addresses>`{.interpreted-text
role="ref"}

Returns all the user\'s current IPv4 and IPv6 addresses as an array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_IP_method_get_local_interfaces}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_local_interfaces**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_IP_method_get_local_interfaces>`{.interpreted-text role="ref"}

Returns all network adapters as an array.

Each adapter is a dictionary of the form:

    {
        "index": "1", # Interface index.
        "name": "eth0", # Interface name.
        "friendly": "Ethernet One", # A friendly name (might be empty).
        "addresses": ["192.168.1.101"], # An array of IP addresses associated to this interface.
    }

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_IP_method_get_resolve_item_address}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_resolve_item_address**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_IP_method_get_resolve_item_address>`{.interpreted-text
role="ref"}

Returns a queued hostname\'s IP address, given its queue `id`. Returns
an empty string on error or if resolution hasn\'t happened yet (see
`get_resolve_item_status()<class_IP_method_get_resolve_item_status>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_IP_method_get_resolve_item_addresses}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_resolve_item_addresses**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_IP_method_get_resolve_item_addresses>`{.interpreted-text
role="ref"}

Returns resolved addresses, or an empty array if an error happened or
resolution didn\'t happen yet (see
`get_resolve_item_status()<class_IP_method_get_resolve_item_status>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_IP_method_get_resolve_item_status}
::: rst-class
classref-method
:::
::::

`ResolverStatus<enum_IP_ResolverStatus>`{.interpreted-text role="ref"}
**get_resolve_item_status**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_IP_method_get_resolve_item_status>`{.interpreted-text
role="ref"}

Returns a queued hostname\'s status as a
`ResolverStatus<enum_IP_ResolverStatus>`{.interpreted-text role="ref"}
constant, given its queue `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_IP_method_resolve_hostname}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**resolve_hostname**(host: `String<class_String>`{.interpreted-text
role="ref"}, ip_type: `Type<enum_IP_Type>`{.interpreted-text role="ref"}
= 3) `🔗<class_IP_method_resolve_hostname>`{.interpreted-text
role="ref"}

Returns a given hostname\'s IPv4 or IPv6 address when resolved
(blocking-type method). The address type returned depends on the
`Type<enum_IP_Type>`{.interpreted-text role="ref"} constant given as
`ip_type`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_IP_method_resolve_hostname_addresses}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **resolve_hostname_addresses**(host:
`String<class_String>`{.interpreted-text role="ref"}, ip_type:
`Type<enum_IP_Type>`{.interpreted-text role="ref"} = 3)
`🔗<class_IP_method_resolve_hostname_addresses>`{.interpreted-text
role="ref"}

Resolves a given hostname in a blocking way. Addresses are returned as
an `Array<class_Array>`{.interpreted-text role="ref"} of IPv4 or IPv6
addresses depending on `ip_type`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_IP_method_resolve_hostname_queue_item}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**resolve_hostname_queue_item**(host:
`String<class_String>`{.interpreted-text role="ref"}, ip_type:
`Type<enum_IP_Type>`{.interpreted-text role="ref"} = 3)
`🔗<class_IP_method_resolve_hostname_queue_item>`{.interpreted-text
role="ref"}

Creates a queue item to resolve a hostname to an IPv4 or IPv6 address
depending on the `Type<enum_IP_Type>`{.interpreted-text role="ref"}
constant given as `ip_type`. Returns the queue ID if successful, or
`RESOLVER_INVALID_ID<class_IP_constant_RESOLVER_INVALID_ID>`{.interpreted-text
role="ref"} on error.
