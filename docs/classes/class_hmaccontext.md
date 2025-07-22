github_url
:   hide

# HMACContext {#class_HMACContext}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Used to create an HMAC for a message using a key.

::: rst-class
classref-introduction-group
:::

## Description

The HMACContext class is useful for advanced HMAC use cases, such as
streaming the message as it supports creating the message over time
rather than providing it all at once.

::::: tabs
::: code-tab
gdscript

extends Node var ctx = HMACContext.new()

func [ready]{#ready}():

:   var key = \"supersecret\".to_utf8_buffer() var err =
    ctx.start(HashingContext.HASH_SHA256, key) assert(err == OK) var
    msg1 = \"this is \".to_utf8_buffer() var msg2 = \"super duper
    secret\".to_utf8_buffer() err = ctx.update(msg1) assert(err == OK)
    err = ctx.update(msg2) assert(err == OK) var hmac = ctx.finish()
    print(hmac.hex_encode())
:::

::: code-tab
csharp

using Godot; using System.Diagnostics;

public partial class MyNode : Node { private HmacContext [ctx]{#ctx} =
new HmacContext();

> public override void [Ready]{#ready}() { byte\[\] key =
> \"supersecret\".ToUtf8Buffer(); Error err =
> [ctx.Start]{#ctx.start}(HashingContext.HashType.Sha256, key);
> Debug.Assert(err == Error.Ok); byte\[\] msg1 = \"this is
> \".ToUtf8Buffer(); byte\[\] msg2 = \"super duper
> secret\".ToUtf8Buffer(); err = [ctx.Update]{#ctx.update}(msg1);
> Debug.Assert(err == Error.Ok); err = [ctx.Update]{#ctx.update}(msg2);
> Debug.Assert(err == Error.Ok); byte\[\] hmac =
> [ctx.Finish]{#ctx.finish}(); GD.Print(hmac.HexEncode()); }

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

## Method Descriptions

:::: {#class_HMACContext_method_finish}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**finish**() `🔗<class_HMACContext_method_finish>`{.interpreted-text
role="ref"}

Returns the resulting HMAC. If the HMAC failed, an empty
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HMACContext_method_start}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**start**(hash_type:
`HashType<enum_HashingContext_HashType>`{.interpreted-text role="ref"},
key: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}) `🔗<class_HMACContext_method_start>`{.interpreted-text
role="ref"}

Initializes the HMACContext. This method cannot be called again on the
same HMACContext until
`finish()<class_HMACContext_method_finish>`{.interpreted-text
role="ref"} has been called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HMACContext_method_update}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**update**(data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_HMACContext_method_update>`{.interpreted-text role="ref"}

Updates the message to be HMACed. This can be called multiple times
before `finish()<class_HMACContext_method_finish>`{.interpreted-text
role="ref"} is called to append `data` to the message, but cannot be
called until `start()<class_HMACContext_method_start>`{.interpreted-text
role="ref"} has been called.
