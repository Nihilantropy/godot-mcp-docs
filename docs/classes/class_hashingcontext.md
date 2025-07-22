github_url
:   hide

# HashingContext {#class_HashingContext}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides functionality for computing cryptographic hashes chunk by
chunk.

::: rst-class
classref-introduction-group
:::

## Description

The HashingContext class provides an interface for computing
cryptographic hashes over multiple iterations. Useful for computing
hashes of big files (so you don\'t have to load them all in memory),
network streams, and data streams in general (so you don\'t have to hold
buffers).

The `HashType<enum_HashingContext_HashType>`{.interpreted-text
role="ref"} enum shows the supported hashing algorithms.

::::: tabs
::: code-tab
gdscript

const CHUNK_SIZE = 1024

func hash_file(path):

:   \# Check that file exists. if not FileAccess.file_exists(path):
    return \# Start an SHA-256 context. var ctx = HashingContext.new()
    ctx.start(HashingContext.HASH_SHA256) \# Open the file to hash. var
    file = FileAccess.open(path, FileAccess.READ) \# Update the context
    after reading each chunk. while file.get_position() \<
    file.get_length(): var remaining = file.get_length() -
    file.get_position() ctx.update(file.get_buffer(min(remaining,
    CHUNK_SIZE))) \# Get the computed hash. var res = ctx.finish() \#
    Print the result as hex string and array. printt(res.hex_encode(),
    Array(res))
:::

::: code-tab
csharp

public const int ChunkSize = 1024;

public void HashFile(string path) { // Check that file exists. if
(!FileAccess.FileExists(path)) { return; } // Start an SHA-256 context.
var ctx = new HashingContext();
ctx.Start(HashingContext.HashType.Sha256); // Open the file to hash.
using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read); //
Update the context after reading each chunk. while (file.GetPosition()
\< file.GetLength()) { int remaining = (int)(file.GetLength() -
file.GetPosition()); ctx.Update(file.GetBuffer(Mathf.Min(remaining,
ChunkSize))); } // Get the computed hash. byte\[\] res = ctx.Finish();
// Print the result as hex string and array. GD.PrintT(res.HexEncode(),
(Variant)res); }
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

:::: {#enum_HashingContext_HashType}
::: rst-class
classref-enumeration
:::
::::

enum **HashType**: `🔗<enum_HashingContext_HashType>`{.interpreted-text
role="ref"}

:::: {#class_HashingContext_constant_HASH_MD5}
::: rst-class
classref-enumeration-constant
:::
::::

`HashType<enum_HashingContext_HashType>`{.interpreted-text role="ref"}
**HASH_MD5** = `0`

Hashing algorithm: MD5.

:::: {#class_HashingContext_constant_HASH_SHA1}
::: rst-class
classref-enumeration-constant
:::
::::

`HashType<enum_HashingContext_HashType>`{.interpreted-text role="ref"}
**HASH_SHA1** = `1`

Hashing algorithm: SHA-1.

:::: {#class_HashingContext_constant_HASH_SHA256}
::: rst-class
classref-enumeration-constant
:::
::::

`HashType<enum_HashingContext_HashType>`{.interpreted-text role="ref"}
**HASH_SHA256** = `2`

Hashing algorithm: SHA-256.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_HashingContext_method_finish}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**finish**() `🔗<class_HashingContext_method_finish>`{.interpreted-text
role="ref"}

Closes the current context, and return the computed hash.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HashingContext_method_start}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**start**(type:
`HashType<enum_HashingContext_HashType>`{.interpreted-text role="ref"})
`🔗<class_HashingContext_method_start>`{.interpreted-text role="ref"}

Starts a new hash computation of the given `type` (e.g.
`HASH_SHA256<class_HashingContext_constant_HASH_SHA256>`{.interpreted-text
role="ref"} to start computation of an SHA-256).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HashingContext_method_update}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**update**(chunk:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_HashingContext_method_update>`{.interpreted-text role="ref"}

Updates the computation with the given `chunk` of data.
