allow_comments
:   False

# The GDExtension system {#doc_gdextension}

**GDExtension** is a Godot-specific technology that lets the engine
interact with native [shared
libraries](https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries)
at runtime. You can use it to run native code without compiling it with
the engine.

:::: note
::: title
Note
:::

GDExtension is *not* a scripting language and has no relation to
`GDScript <doc_gdscript>`{.interpreted-text role="ref"}.
::::

This section describes how GDExtension works, and is generally aimed at
people wanting to make a GDExtension from scratch, for example to create
language bindings. If you want to use existing language bindings, please
refer to other articles instead, such as the articles about
`C++ (godot-cpp) <doc_godot_cpp>`{.interpreted-text role="ref"} or one
of the
`community-made ones <doc_what_is_gdnative_third_party_bindings>`{.interpreted-text
role="ref"}.

::: {#toc-tutorials-gdextension .toctree maxdepth="1"}
what_is_gdextension gdextension_file gdextension_c_example
:::
