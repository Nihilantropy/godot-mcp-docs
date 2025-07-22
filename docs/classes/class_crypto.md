github_url
:   hide

# Crypto {#class_Crypto}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides access to advanced cryptographic functionalities.

::: rst-class
classref-introduction-group
:::

## Description

The Crypto class provides access to advanced cryptographic
functionalities.

Currently, this includes asymmetric key encryption/decryption,
signing/verification, and generating cryptographically secure random
bytes, RSA keys, HMAC digests, and self-signed
`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"}s.

::::: tabs
::: code-tab
gdscript

var crypto = Crypto.new()

\# Generate new RSA key. var key = crypto.generate_rsa(4096)

\# Generate new self-signed certificate with the given key. var cert =
crypto.generate_self_signed_certificate(key, \"CN=mydomain.com,O=My Game
Company,C=IT\")

\# Save key and certificate in the user folder.
key.save(\"user://generated.key\") cert.save(\"user://generated.crt\")

\# Encryption var data = \"Some data\" var encrypted =
crypto.encrypt(key, data.to_utf8_buffer())

\# Decryption var decrypted = crypto.decrypt(key, encrypted)

\# Signing var signature = crypto.sign(HashingContext.HASH_SHA256,
data.sha256_buffer(), key)

\# Verifying var verified = crypto.verify(HashingContext.HASH_SHA256,
data.sha256_buffer(), signature, key)

\# Checks assert(verified) assert(data.to_utf8_buffer() == decrypted)
:::

::: code-tab
csharp

using Godot; using System.Diagnostics;

Crypto crypto = new Crypto();

// Generate new RSA key. CryptoKey key = crypto.GenerateRsa(4096);

// Generate new self-signed certificate with the given key.
X509Certificate cert = crypto.GenerateSelfSignedCertificate(key,
\"CN=mydomain.com,O=My Game Company,C=IT\");

// Save key and certificate in the user folder.
key.Save(\"user://generated.key\"); cert.Save(\"user://generated.crt\");

// Encryption string data = \"Some data\"; byte\[\] encrypted =
crypto.Encrypt(key, data.ToUtf8Buffer());

// Decryption byte\[\] decrypted = crypto.Decrypt(key, encrypted);

// Signing byte\[\] signature =
crypto.Sign(HashingContext.HashType.Sha256, Data.Sha256Buffer(), key);

// Verifying bool verified =
crypto.Verify(HashingContext.HashType.Sha256, Data.Sha256Buffer(),
signature, key);

// Checks Debug.Assert(verified); Debug.Assert(data.ToUtf8Buffer() ==
decrypted);
:::
:::::

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

:::: {#class_Crypto_method_constant_time_compare}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**constant_time_compare**(trusted:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
received: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"})
`🔗<class_Crypto_method_constant_time_compare>`{.interpreted-text
role="ref"}

Compares two `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}s for equality without leaking timing information in order to
prevent timing attacks.

See [this blog
post](https://paragonie.com/blog/2015/11/preventing-timing-attacks-on-string-comparison-with-double-hmac-strategy)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Crypto_method_decrypt}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**decrypt**(key: `CryptoKey<class_CryptoKey>`{.interpreted-text
role="ref"}, ciphertext:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Crypto_method_decrypt>`{.interpreted-text role="ref"}

Decrypt the given `ciphertext` with the provided private `key`.

\*\*Note:\*\* The maximum size of accepted ciphertext is limited by the
key size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Crypto_method_encrypt}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**encrypt**(key: `CryptoKey<class_CryptoKey>`{.interpreted-text
role="ref"}, plaintext:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Crypto_method_encrypt>`{.interpreted-text role="ref"}

Encrypt the given `plaintext` with the provided public `key`.

\*\*Note:\*\* The maximum size of accepted plaintext is limited by the
key size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Crypto_method_generate_random_bytes}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**generate_random_bytes**(size: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Crypto_method_generate_random_bytes>`{.interpreted-text
role="ref"}

Generates a `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"} of cryptographically secure random bytes with given `size`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Crypto_method_generate_rsa}
::: rst-class
classref-method
:::
::::

`CryptoKey<class_CryptoKey>`{.interpreted-text role="ref"}
**generate_rsa**(size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Crypto_method_generate_rsa>`{.interpreted-text role="ref"}

Generates an RSA `CryptoKey<class_CryptoKey>`{.interpreted-text
role="ref"} that can be used for creating self-signed certificates and
passed to
`StreamPeerTLS.accept_stream()<class_StreamPeerTLS_method_accept_stream>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Crypto_method_generate_self_signed_certificate}
::: rst-class
classref-method
:::
::::

`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"}
**generate_self_signed_certificate**(key:
`CryptoKey<class_CryptoKey>`{.interpreted-text role="ref"}, issuer_name:
`String<class_String>`{.interpreted-text role="ref"} =
\"CN=myserver,O=myorganisation,C=IT\", not_before:
`String<class_String>`{.interpreted-text role="ref"} =
\"20140101000000\", not_after: `String<class_String>`{.interpreted-text
role="ref"} = \"20340101000000\")
`🔗<class_Crypto_method_generate_self_signed_certificate>`{.interpreted-text
role="ref"}

Generates a self-signed
`X509Certificate<class_X509Certificate>`{.interpreted-text role="ref"}
from the given `CryptoKey<class_CryptoKey>`{.interpreted-text
role="ref"} and `issuer_name`. The certificate validity will be defined
by `not_before` and `not_after` (first valid date and last valid date).
The `issuer_name` must contain at least \"CN=\" (common name, i.e. the
domain name), \"O=\" (organization, i.e. your company name), \"C=\"
(country, i.e. 2 lettered ISO-3166 code of the country the organization
is based in).

A small example to generate an RSA key and an X509 self-signed
certificate.

::::: tabs
::: code-tab
gdscript

var crypto = Crypto.new() \# Generate 4096 bits RSA key. var key =
crypto.generate_rsa(4096) \# Generate self-signed certificate using the
given key. var cert = crypto.generate_self_signed_certificate(key,
\"CN=example.com,O=A Game Company,C=IT\")
:::

::: code-tab
csharp

var crypto = new Crypto(); // Generate 4096 bits RSA key. CryptoKey key
= crypto.GenerateRsa(4096); // Generate self-signed certificate using
the given key. X509Certificate cert =
crypto.GenerateSelfSignedCertificate(key, \"CN=mydomain.com,O=My Game
Company,C=IT\");
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Crypto_method_hmac_digest}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**hmac_digest**(hash_type:
`HashType<enum_HashingContext_HashType>`{.interpreted-text role="ref"},
key: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}, msg:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_Crypto_method_hmac_digest>`{.interpreted-text role="ref"}

Generates an [HMAC](https://en.wikipedia.org/wiki/HMAC) digest of `msg`
using `key`. The `hash_type` parameter is the hashing algorithm that is
used for the inner and outer hashes.

Currently, only
`HashingContext.HASH_SHA256<class_HashingContext_constant_HASH_SHA256>`{.interpreted-text
role="ref"} and
`HashingContext.HASH_SHA1<class_HashingContext_constant_HASH_SHA1>`{.interpreted-text
role="ref"} are supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Crypto_method_sign}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**sign**(hash_type:
`HashType<enum_HashingContext_HashType>`{.interpreted-text role="ref"},
hash: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}, key: `CryptoKey<class_CryptoKey>`{.interpreted-text
role="ref"}) `🔗<class_Crypto_method_sign>`{.interpreted-text
role="ref"}

Sign a given `hash` of type `hash_type` with the provided private `key`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Crypto_method_verify}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **verify**(hash_type:
`HashType<enum_HashingContext_HashType>`{.interpreted-text role="ref"},
hash: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}, signature:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
key: `CryptoKey<class_CryptoKey>`{.interpreted-text role="ref"})
`🔗<class_Crypto_method_verify>`{.interpreted-text role="ref"}

Verify that a given `signature` for `hash` of type `hash_type` against
the provided public `key`.
