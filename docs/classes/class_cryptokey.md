github_url
:   hide

# CryptoKey {#class_CryptoKey}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A cryptographic key (RSA or elliptic-curve).

::: rst-class
classref-introduction-group
:::

## Description

The CryptoKey class represents a cryptographic key. Keys can be loaded
and saved like any other `Resource<class_Resource>`{.interpreted-text
role="ref"}.

They can be used to generate a self-signed
`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"}
via
`Crypto.generate_self_signed_certificate()<class_Crypto_method_generate_self_signed_certificate>`{.interpreted-text
role="ref"} and as private key in
`StreamPeerTLS.accept_stream()<class_StreamPeerTLS_method_accept_stream>`{.interpreted-text
role="ref"} along with the appropriate certificate.

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

:::: {#class_CryptoKey_method_is_public_only}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_public_only**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CryptoKey_method_is_public_only>`{.interpreted-text
role="ref"}

Returns `true` if this CryptoKey only has the public part, and not the
private one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CryptoKey_method_load}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load**(path: `String<class_String>`{.interpreted-text role="ref"},
public_only: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CryptoKey_method_load>`{.interpreted-text role="ref"}

Loads a key from `path`. If `public_only` is `true`, only the public key
will be loaded.

\*\*Note:\*\* `path` should be a \"\*.pub\" file if `public_only` is
`true`, a \"\*.key\" file otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CryptoKey_method_load_from_string}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_from_string**(string_key:
`String<class_String>`{.interpreted-text role="ref"}, public_only:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CryptoKey_method_load_from_string>`{.interpreted-text
role="ref"}

Loads a key from the given `string_key`. If `public_only` is `true`,
only the public key will be loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CryptoKey_method_save}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save**(path: `String<class_String>`{.interpreted-text role="ref"},
public_only: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CryptoKey_method_save>`{.interpreted-text role="ref"}

Saves a key to the given `path`. If `public_only` is `true`, only the
public key will be saved.

\*\*Note:\*\* `path` should be a \"\*.pub\" file if `public_only` is
`true`, a \"\*.key\" file otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CryptoKey_method_save_to_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**save_to_string**(public_only: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_CryptoKey_method_save_to_string>`{.interpreted-text
role="ref"}

Returns a string containing the key in PEM format. If `public_only` is
`true`, only the public key will be included.
