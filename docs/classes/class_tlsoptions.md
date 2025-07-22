github_url
:   hide

# TLSOptions {#class_TLSOptions}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

TLS configuration for clients and servers.

::: rst-class
classref-introduction-group
:::

## Description

TLSOptions abstracts the configuration options for the
`StreamPeerTLS<class_StreamPeerTLS>`{.interpreted-text role="ref"} and
`PacketPeerDTLS<class_PacketPeerDTLS>`{.interpreted-text role="ref"}
classes.

Objects of this class cannot be instantiated directly, and one of the
static methods
`client()<class_TLSOptions_method_client>`{.interpreted-text
role="ref"},
`client_unsafe()<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}, or
`server()<class_TLSOptions_method_server>`{.interpreted-text role="ref"}
should be used instead.

:::: tabs
::: code-tab
gdscript

\# Create a TLS client configuration which uses our custom trusted CA
chain. var client_trusted_cas = load(\"res://my_trusted_cas.crt\") var
client_tls_options = TLSOptions.client(client_trusted_cas)

\# Create a TLS server configuration. var server_certs =
load(\"res://my_server_cas.crt\") var server_key =
load(\"res://my_server_key.key\") var server_tls_options =
TLSOptions.server(server_key, server_certs)
:::
::::

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

:::: {#class_TLSOptions_method_client}
::: rst-class
classref-method
:::
::::

`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"}
**client**(trusted_chain:
`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"} =
null, common_name_override: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_TLSOptions_method_client>`{.interpreted-text
role="ref"}

Creates a TLS client configuration which validates certificates and
their common names (fully qualified domain names).

You can specify a custom `trusted_chain` of certification authorities
(the default CA list will be used if `null`), and optionally provide a
`common_name_override` if you expect the certificate to have a common
name other than the server FQDN.

\*\*Note:\*\* On the Web platform, TLS verification is always enforced
against the CA list of the web browser. This is considered a security
feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TLSOptions_method_client_unsafe}
::: rst-class
classref-method
:::
::::

`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"}
**client_unsafe**(trusted_chain:
`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"} =
null)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}

Creates an **unsafe** TLS client configuration where certificate
validation is optional. You can optionally provide a valid
`trusted_chain`, but the common name of the certificates will never be
checked. Using this configuration for purposes other than testing **is
not recommended**.

\*\*Note:\*\* On the Web platform, TLS verification is always enforced
against the CA list of the web browser. This is considered a security
feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TLSOptions_method_get_common_name_override}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_common_name_override**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TLSOptions_method_get_common_name_override>`{.interpreted-text
role="ref"}

Returns the common name (domain name) override specified when creating
with `client()<class_TLSOptions_method_client>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TLSOptions_method_get_own_certificate}
::: rst-class
classref-method
:::
::::

`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"}
**get_own_certificate**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TLSOptions_method_get_own_certificate>`{.interpreted-text
role="ref"}

Returns the `X509Certificate<class_X509Certificate>`{.interpreted-text
role="ref"} specified when creating with
`server()<class_TLSOptions_method_server>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TLSOptions_method_get_private_key}
::: rst-class
classref-method
:::
::::

`CryptoKey<class_CryptoKey>`{.interpreted-text role="ref"}
**get_private_key**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TLSOptions_method_get_private_key>`{.interpreted-text
role="ref"}

Returns the `CryptoKey<class_CryptoKey>`{.interpreted-text role="ref"}
specified when creating with
`server()<class_TLSOptions_method_server>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TLSOptions_method_get_trusted_ca_chain}
::: rst-class
classref-method
:::
::::

`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"}
**get_trusted_ca_chain**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TLSOptions_method_get_trusted_ca_chain>`{.interpreted-text
role="ref"}

Returns the CA
`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"}
chain specified when creating with
`client()<class_TLSOptions_method_client>`{.interpreted-text role="ref"}
or
`client_unsafe()<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TLSOptions_method_is_server}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_server**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TLSOptions_method_is_server>`{.interpreted-text
role="ref"}

Returns `true` if created with
`server()<class_TLSOptions_method_server>`{.interpreted-text
role="ref"}, `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TLSOptions_method_is_unsafe_client}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_unsafe_client**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TLSOptions_method_is_unsafe_client>`{.interpreted-text
role="ref"}

Returns `true` if created with
`client_unsafe()<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}, `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TLSOptions_method_server}
::: rst-class
classref-method
:::
::::

`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"}
**server**(key: `CryptoKey<class_CryptoKey>`{.interpreted-text
role="ref"}, certificate:
`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_TLSOptions_method_server>`{.interpreted-text
role="ref"}

Creates a TLS server configuration using the provided `key` and
`certificate`.

\*\*Note:\*\* The `certificate` should include the full certificate
chain up to the signing CA (certificates file can be concatenated using
a general purpose text editor).
