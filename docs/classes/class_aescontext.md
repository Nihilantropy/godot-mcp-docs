github_url
:   hide

# AESContext {#class_AESContext}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides access to AES encryption/decryption of raw data.

::: rst-class
classref-introduction-group
:::

## Description

This class holds the context information required for encryption and
decryption operations with AES (Advanced Encryption Standard). Both
AES-ECB and AES-CBC modes are supported.

::::: tabs
::: code-tab
gdscript

extends Node

var aes = AESContext.new()

func [ready]{#ready}():

:   var key = \"My secret key!!!\" \# Key must be either 16 or 32 bytes.
    var data = \"My secret text!!\" \# Data size must be multiple of 16
    bytes, apply padding if needed. \# Encrypt ECB
    aes.start(AESContext.MODE_ECB_ENCRYPT, key.to_utf8_buffer()) var
    encrypted = aes.update(data.to_utf8_buffer()) aes.finish() \#
    Decrypt ECB aes.start(AESContext.MODE_ECB_DECRYPT,
    key.to_utf8_buffer()) var decrypted = aes.update(encrypted)
    aes.finish() \# Check ECB assert(decrypted == data.to_utf8_buffer())

    var iv = \"My secret iv!!!!\" \# IV must be of exactly 16 bytes. \#
    Encrypt CBC aes.start(AESContext.MODE_CBC_ENCRYPT,
    key.to_utf8_buffer(), iv.to_utf8_buffer()) encrypted =
    aes.update(data.to_utf8_buffer()) aes.finish() \# Decrypt CBC
    aes.start(AESContext.MODE_CBC_DECRYPT, key.to_utf8_buffer(),
    iv.to_utf8_buffer()) decrypted = aes.update(encrypted) aes.finish()
    \# Check CBC assert(decrypted == data.to_utf8_buffer())
:::

::: code-tab
csharp

using Godot; using System.Diagnostics;

public partial class MyNode : Node { private AesContext [aes]{#aes} =
new AesContext();

> public override void [Ready]{#ready}() { string key = \"My secret
> key!!!\"; // Key must be either 16 or 32 bytes. string data = \"My
> secret text!!\"; // Data size must be multiple of 16 bytes, apply
> padding if needed. // Encrypt ECB
> [aes.Start]{#aes.start}(AesContext.Mode.EcbEncrypt,
> key.ToUtf8Buffer()); byte\[\] encrypted =
> [aes.Update]{#aes.update}(data.ToUtf8Buffer());
> [aes.Finish]{#aes.finish}(); // Decrypt ECB
> [aes.Start]{#aes.start}(AesContext.Mode.EcbDecrypt,
> key.ToUtf8Buffer()); byte\[\] decrypted =
> [aes.Update]{#aes.update}(encrypted); [aes.Finish]{#aes.finish}(); //
> Check ECB Debug.Assert(decrypted == data.ToUtf8Buffer());
>
> > string iv = \"My secret iv!!!!\"; // IV must be of exactly 16 bytes.
> > // Encrypt CBC [aes.Start]{#aes.start}(AesContext.Mode.EcbEncrypt,
> > key.ToUtf8Buffer(), iv.ToUtf8Buffer()); encrypted =
> > [aes.Update]{#aes.update}(data.ToUtf8Buffer());
> > [aes.Finish]{#aes.finish}(); // Decrypt CBC
> > [aes.Start]{#aes.start}(AesContext.Mode.EcbDecrypt,
> > key.ToUtf8Buffer(), iv.ToUtf8Buffer()); decrypted =
> > [aes.Update]{#aes.update}(encrypted); [aes.Finish]{#aes.finish}();
> > // Check CBC Debug.Assert(decrypted == data.ToUtf8Buffer());
>
> }

}
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

## Enumerations

:::: {#enum_AESContext_Mode}
::: rst-class
classref-enumeration
:::
::::

enum **Mode**: `🔗<enum_AESContext_Mode>`{.interpreted-text role="ref"}

:::: {#class_AESContext_constant_MODE_ECB_ENCRYPT}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AESContext_Mode>`{.interpreted-text role="ref"}
**MODE_ECB_ENCRYPT** = `0`

AES electronic codebook encryption mode.

:::: {#class_AESContext_constant_MODE_ECB_DECRYPT}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AESContext_Mode>`{.interpreted-text role="ref"}
**MODE_ECB_DECRYPT** = `1`

AES electronic codebook decryption mode.

:::: {#class_AESContext_constant_MODE_CBC_ENCRYPT}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AESContext_Mode>`{.interpreted-text role="ref"}
**MODE_CBC_ENCRYPT** = `2`

AES cipher blocker chaining encryption mode.

:::: {#class_AESContext_constant_MODE_CBC_DECRYPT}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AESContext_Mode>`{.interpreted-text role="ref"}
**MODE_CBC_DECRYPT** = `3`

AES cipher blocker chaining decryption mode.

:::: {#class_AESContext_constant_MODE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_AESContext_Mode>`{.interpreted-text role="ref"} **MODE_MAX**
= `4`

Maximum value for the mode enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AESContext_method_finish}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **finish**()
`🔗<class_AESContext_method_finish>`{.interpreted-text role="ref"}

Close this AES context so it can be started again. See
`start()<class_AESContext_method_start>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AESContext_method_get_iv_state}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_iv_state**()
`🔗<class_AESContext_method_get_iv_state>`{.interpreted-text role="ref"}

Get the current IV state for this context (IV gets updated when calling
`update()<class_AESContext_method_update>`{.interpreted-text
role="ref"}). You normally don\'t need this function.

\*\*Note:\*\* This function only makes sense when the context is started
with
`MODE_CBC_ENCRYPT<class_AESContext_constant_MODE_CBC_ENCRYPT>`{.interpreted-text
role="ref"} or
`MODE_CBC_DECRYPT<class_AESContext_constant_MODE_CBC_DECRYPT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AESContext_method_start}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**start**(mode: `Mode<enum_AESContext_Mode>`{.interpreted-text
role="ref"}, key:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
iv: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"} = PackedByteArray())
`🔗<class_AESContext_method_start>`{.interpreted-text role="ref"}

Start the AES context in the given `mode`. A `key` of either 16 or 32
bytes must always be provided, while an `iv` (initialization vector) of
exactly 16 bytes, is only needed when `mode` is either
`MODE_CBC_ENCRYPT<class_AESContext_constant_MODE_CBC_ENCRYPT>`{.interpreted-text
role="ref"} or
`MODE_CBC_DECRYPT<class_AESContext_constant_MODE_CBC_DECRYPT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AESContext_method_update}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**update**(src:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_AESContext_method_update>`{.interpreted-text role="ref"}

Run the desired operation for this AES context. Will return a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
containing the result of encrypting (or decrypting) the given `src`. See
`start()<class_AESContext_method_start>`{.interpreted-text role="ref"}
for mode of operation.

\*\*Note:\*\* The size of `src` must be a multiple of 16. Apply some
padding if needed.
