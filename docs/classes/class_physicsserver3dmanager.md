github_url
:   hide

# PhysicsServer3DManager {#class_PhysicsServer3DManager}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton for managing
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}
implementations.

::: rst-class
classref-introduction-group
:::

## Description

**PhysicsServer3DManager** is the API for registering
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}
implementations and for setting the default implementation.

\*\*Note:\*\* It is not possible to switch physics servers at runtime.
This class is only used on startup at the server initialization level,
by Godot itself and possibly by GDExtensions.

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

:::: {#class_PhysicsServer3DManager_method_register_server}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_server**(name: `String<class_String>`{.interpreted-text
role="ref"}, create_callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3DManager_method_register_server>`{.interpreted-text
role="ref"}

Register a `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"} implementation by passing a `name` and a
`Callable<class_Callable>`{.interpreted-text role="ref"} that returns a
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}
object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3DManager_method_set_default_server}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_default_server**(name: `String<class_String>`{.interpreted-text
role="ref"}, priority: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3DManager_method_set_default_server>`{.interpreted-text
role="ref"}

Set the default
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}
implementation to the one identified by `name`, if `priority` is greater
than the priority of the current default implementation.
