github_url
:   hide

# X509Certificate {#class_X509Certificate}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

An X509 certificate (e.g. for TLS).

::: rst-class
classref-introduction-group
:::

## Description

The X509Certificate class represents an X509 certificate. Certificates
can be loaded and saved like any other
`Resource<class_Resource>`{.interpreted-text role="ref"}.

They can be used as the server certificate in
`StreamPeerTLS.accept_stream()<class_StreamPeerTLS_method_accept_stream>`{.interpreted-text
role="ref"} (along with the proper
`CryptoKey<class_CryptoKey>`{.interpreted-text role="ref"}), and to
specify the only certificate that should be accepted when connecting to
a TLS server via
`StreamPeerTLS.connect_to_stream()<class_StreamPeerTLS_method_connect_to_stream>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `SSL certificates <../tutorials/networking/ssl_certificates>`{.interpreted-text
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

## Method Descriptions

:::: {#class_X509Certificate_method_load}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_X509Certificate_method_load>`{.interpreted-text role="ref"}

Loads a certificate from `path` (\"\*.crt\" file).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_X509Certificate_method_load_from_string}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_from_string**(string: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_X509Certificate_method_load_from_string>`{.interpreted-text
role="ref"}

Loads a certificate from the given `string`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_X509Certificate_method_save}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_X509Certificate_method_save>`{.interpreted-text role="ref"}

Saves a certificate to the given `path` (should be a \"\*.crt\" file).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_X509Certificate_method_save_to_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**save_to_string**()
`🔗<class_X509Certificate_method_save_to_string>`{.interpreted-text
role="ref"}

Returns a string representation of the certificate, or an empty string
if the certificate is invalid.
