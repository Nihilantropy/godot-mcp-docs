github_url
:   hide

# TextServerFallback {#class_TextServerFallback}

**Inherits:**
`TextServerExtension<class_TextServerExtension>`{.interpreted-text
role="ref"} **\<** `TextServer<class_TextServer>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A fallback implementation of Godot\'s text server, without support for
BiDi and complex text layout.

::: rst-class
classref-introduction-group
:::

## Description

A fallback implementation of Godot\'s text server. This fallback is
faster than
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"} for processing a lot of text, but it does not support BiDi
and complex text layout.

\*\*Note:\*\* This text server is not part of official Godot binaries.
If you want to use it, compile the engine with the option
`module_text_server_fb_enabled=yes`. When building with
**TextServerFallback**, consider also disabling
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"} with `module_text_server_adv_enabled=no` to reduce binary
size.
