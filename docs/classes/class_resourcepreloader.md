github_url
:   hide

# ResourcePreloader {#class_ResourcePreloader}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node used to preload sub-resources inside a scene.

::: rst-class
classref-introduction-group
:::

## Description

This node is used to preload sub-resources inside a scene, so when the
scene is loaded, all the resources are ready to use and can be retrieved
from the preloader. You can add the resources using the
ResourcePreloader tab when the node is selected.

GDScript has a simplified
`@GDScript.preload()<class_@GDScript_method_preload>`{.interpreted-text
role="ref"} built-in method which can be used in most situations,
leaving the use of **ResourcePreloader** for more advanced scenarios.

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

:::: {#class_ResourcePreloader_method_add_resource}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_resource**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, resource: `Resource<class_Resource>`{.interpreted-text
role="ref"})
`🔗<class_ResourcePreloader_method_add_resource>`{.interpreted-text
role="ref"}

Adds a resource to the preloader with the given `name`. If a resource
with the given `name` already exists, the new resource will be renamed
to \"`name` N\" where N is an incrementing number starting from 2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourcePreloader_method_get_resource}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**get_resource**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourcePreloader_method_get_resource>`{.interpreted-text
role="ref"}

Returns the resource associated to `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourcePreloader_method_get_resource_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_resource_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourcePreloader_method_get_resource_list>`{.interpreted-text
role="ref"}

Returns the list of resources inside the preloader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourcePreloader_method_has_resource}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_resource**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourcePreloader_method_has_resource>`{.interpreted-text
role="ref"}

Returns `true` if the preloader contains a resource associated to
`name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourcePreloader_method_remove_resource}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_resource**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_ResourcePreloader_method_remove_resource>`{.interpreted-text
role="ref"}

Removes the resource associated to `name` from the preloader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourcePreloader_method_rename_resource}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_resource**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, newname:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_ResourcePreloader_method_rename_resource>`{.interpreted-text
role="ref"}

Renames a resource inside the preloader from `name` to `newname`.
