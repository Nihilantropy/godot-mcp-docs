# What is GDExtension? {#doc_what_is_gdextension}

**GDExtension** is a Godot-specific technology that lets the engine
interact with native [shared
libraries](https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries)
at runtime. You can use it to run native code without compiling it with
the engine.

There are three primary methods with which this is achieved:

- `gdextension_interface.h`: A set of C functions that Godot and a
  GDExtension can use to communicate.
- `extension_api.json`: A list of C functions that are exposed from
  Godot APIs
  (`Core Features <doc_scripting_core_features>`{.interpreted-text
  role="ref"}).
- `*.gdextension <doc_gdextension_file>`{.interpreted-text role="ref"}:
  A file format read by Godot to load a GDExtension.

Most people create GDExtensions with some existing language binding,
such as `godot-cpp (for C++) <doc_godot_cpp>`{.interpreted-text
role="ref"}, or one of the
`community-made ones <doc_what_is_gdnative_third_party_bindings>`{.interpreted-text
role="ref"}.

## Version compatibility

See
`godot-cpp Version Compatibility <doc_what_is_gdextension_version_compatibility>`{.interpreted-text
role="ref"}, which applies to all GDExtensions.
