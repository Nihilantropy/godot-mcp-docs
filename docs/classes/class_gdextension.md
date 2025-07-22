github_url
:   hide

# GDExtension {#class_GDExtension}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A native library for GDExtension.

::: rst-class
classref-introduction-group
:::

## Description

The **GDExtension** resource type represents a [shared
library](https://en.wikipedia.org/wiki/Shared_library) which can expand
the functionality of the engine. The
`GDExtensionManager<class_GDExtensionManager>`{.interpreted-text
role="ref"} singleton is responsible for loading, reloading, and
unloading **GDExtension** resources.

\*\*Note:\*\* GDExtension itself is not a scripting language and has no
relation to `GDScript<class_GDScript>`{.interpreted-text role="ref"}
resources.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `GDExtension overview <../tutorials/scripting/gdextension/what_is_gdextension>`{.interpreted-text
  role="doc"}
- `GDExtension example in C++ <../tutorials/scripting/cpp/gdextension_cpp_example>`{.interpreted-text
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

## Enumerations

:::: {#enum_GDExtension_InitializationLevel}
::: rst-class
classref-enumeration
:::
::::

enum **InitializationLevel**:
`🔗<enum_GDExtension_InitializationLevel>`{.interpreted-text role="ref"}

:::: {#class_GDExtension_constant_INITIALIZATION_LEVEL_CORE}
::: rst-class
classref-enumeration-constant
:::
::::

`InitializationLevel<enum_GDExtension_InitializationLevel>`{.interpreted-text
role="ref"} **INITIALIZATION_LEVEL_CORE** = `0`

The library is initialized at the same time as the core features of the
engine.

:::: {#class_GDExtension_constant_INITIALIZATION_LEVEL_SERVERS}
::: rst-class
classref-enumeration-constant
:::
::::

`InitializationLevel<enum_GDExtension_InitializationLevel>`{.interpreted-text
role="ref"} **INITIALIZATION_LEVEL_SERVERS** = `1`

The library is initialized at the same time as the engine\'s servers
(such as `RenderingServer<class_RenderingServer>`{.interpreted-text
role="ref"} or
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}).

:::: {#class_GDExtension_constant_INITIALIZATION_LEVEL_SCENE}
::: rst-class
classref-enumeration-constant
:::
::::

`InitializationLevel<enum_GDExtension_InitializationLevel>`{.interpreted-text
role="ref"} **INITIALIZATION_LEVEL_SCENE** = `2`

The library is initialized at the same time as the engine\'s
scene-related classes.

:::: {#class_GDExtension_constant_INITIALIZATION_LEVEL_EDITOR}
::: rst-class
classref-enumeration-constant
:::
::::

`InitializationLevel<enum_GDExtension_InitializationLevel>`{.interpreted-text
role="ref"} **INITIALIZATION_LEVEL_EDITOR** = `3`

The library is initialized at the same time as the engine\'s editor
classes. Only happens when loading the GDExtension in the editor.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GDExtension_method_get_minimum_library_initialization_level}
::: rst-class
classref-method
:::
::::

`InitializationLevel<enum_GDExtension_InitializationLevel>`{.interpreted-text
role="ref"} **get_minimum_library_initialization_level**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GDExtension_method_get_minimum_library_initialization_level>`{.interpreted-text
role="ref"}

Returns the lowest level required for this extension to be properly
initialized (see the
`InitializationLevel<enum_GDExtension_InitializationLevel>`{.interpreted-text
role="ref"} enum).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GDExtension_method_is_library_open}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_library_open**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GDExtension_method_is_library_open>`{.interpreted-text
role="ref"}

Returns `true` if this extension\'s library has been opened.
