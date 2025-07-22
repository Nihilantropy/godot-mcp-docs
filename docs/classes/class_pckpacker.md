github_url
:   hide

# PCKPacker {#class_PCKPacker}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Creates packages that can be loaded into a running project.

::: rst-class
classref-introduction-group
:::

## Description

The **PCKPacker** is used to create packages that can be loaded into a
running project using
`ProjectSettings.load_resource_pack()<class_ProjectSettings_method_load_resource_pack>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var packer = PCKPacker.new() packer.pck_start(\"test.pck\")
packer.add_file(\"res://text.txt\", \"text.txt\") packer.flush()
:::

::: code-tab
csharp

var packer = new PckPacker(); packer.PckStart(\"test.pck\");
packer.AddFile(\"res://text.txt\", \"text.txt\"); packer.Flush();
:::
:::::

The above **PCKPacker** creates package `test.pck`, then adds a file
named `text.txt` at the root of the package.

\*\*Note:\*\* PCK is Godot\'s own pack file format. To create ZIP
archives that can be read by any program, use
`ZIPPacker<class_ZIPPacker>`{.interpreted-text role="ref"} instead.

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

:::: {#class_PCKPacker_method_add_file}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**add_file**(target_path: `String<class_String>`{.interpreted-text
role="ref"}, source_path: `String<class_String>`{.interpreted-text
role="ref"}, encrypt: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_PCKPacker_method_add_file>`{.interpreted-text
role="ref"}

Adds the `source_path` file to the current PCK package at the
`target_path` internal path. The `res://` prefix for `target_path` is
optional and stripped internally. File content is immediately written to
the PCK.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PCKPacker_method_add_file_removal}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**add_file_removal**(target_path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_PCKPacker_method_add_file_removal>`{.interpreted-text
role="ref"}

Registers a file removal of the `target_path` internal path to the PCK.
This is mainly used for patches. If the file at this path has been
loaded from a previous PCK, it will be removed. The `res://` prefix for
`target_path` is optional and stripped internally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PCKPacker_method_flush}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**flush**(verbose: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_PCKPacker_method_flush>`{.interpreted-text role="ref"}

Writes the file directory and closes the PCK. If `verbose` is `true`, a
list of files added will be printed to the console for easier debugging.

\*\*Note:\*\* **PCKPacker** will automatically flush when it\'s freed,
which happens when it goes out of scope or when it gets assigned with
`null`. In C# the reference must be disposed after use, either with the
`using` statement or by calling the `Dispose` method directly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PCKPacker_method_pck_start}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**pck_start**(pck_path: `String<class_String>`{.interpreted-text
role="ref"}, alignment: `int<class_int>`{.interpreted-text role="ref"} =
32, key: `String<class_String>`{.interpreted-text role="ref"} =
\"0000000000000000000000000000000000000000000000000000000000000000\",
encrypt_directory: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_PCKPacker_method_pck_start>`{.interpreted-text
role="ref"}

Creates a new PCK file at the file path `pck_path`. The `.pck` file
extension isn\'t added automatically, so it should be part of `pck_path`
(even though it\'s not required).
