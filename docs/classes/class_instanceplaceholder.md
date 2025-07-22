github_url
:   hide

# InstancePlaceholder {#class_InstancePlaceholder}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Placeholder for the root `Node<class_Node>`{.interpreted-text
role="ref"} of a `PackedScene<class_PackedScene>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Turning on the option **Load As Placeholder** for an instantiated scene
in the editor causes it to be replaced by an **InstancePlaceholder**
when running the game, this will not replace the node in the editor.
This makes it possible to delay actually loading the scene until calling
`create_instance()<class_InstancePlaceholder_method_create_instance>`{.interpreted-text
role="ref"}. This is useful to avoid loading large scenes all at once by
loading parts of it selectively.

\*\*Note:\*\* Like `Node<class_Node>`{.interpreted-text role="ref"},
**InstancePlaceholder** does not have a transform. This causes any child
nodes to be positioned relatively to the
`Viewport<class_Viewport>`{.interpreted-text role="ref"} origin, rather
than their parent as displayed in the editor. Replacing the placeholder
with a scene with a transform will transform children relatively to
their parent again.

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

:::: {#class_InstancePlaceholder_method_create_instance}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"}
**create_instance**(replace: `bool<class_bool>`{.interpreted-text
role="ref"} = false, custom_scene:
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"} = null)
`🔗<class_InstancePlaceholder_method_create_instance>`{.interpreted-text
role="ref"}

Call this method to actually load in the node. The created node will be
placed as a sibling *above* the **InstancePlaceholder** in the scene
tree. The `Node<class_Node>`{.interpreted-text role="ref"}\'s reference
is also returned for convenience.

\*\*Note:\*\*
`create_instance()<class_InstancePlaceholder_method_create_instance>`{.interpreted-text
role="ref"} is not thread-safe. Use
`Object.call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"} if calling from a thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InstancePlaceholder_method_get_instance_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_instance_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InstancePlaceholder_method_get_instance_path>`{.interpreted-text
role="ref"}

Gets the path to the `PackedScene<class_PackedScene>`{.interpreted-text
role="ref"} resource file that is loaded by default when calling
`create_instance()<class_InstancePlaceholder_method_create_instance>`{.interpreted-text
role="ref"}. Not thread-safe. Use
`Object.call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"} if calling from a thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InstancePlaceholder_method_get_stored_values}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_stored_values**(with_order: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_InstancePlaceholder_method_get_stored_values>`{.interpreted-text
role="ref"}

Returns the list of properties that will be applied to the node when
`create_instance()<class_InstancePlaceholder_method_create_instance>`{.interpreted-text
role="ref"} is called.

If `with_order` is `true`, a key named `.order` (note the leading
period) is added to the dictionary. This `.order` key is an
`Array<class_Array>`{.interpreted-text role="ref"} of
`String<class_String>`{.interpreted-text role="ref"} property names
specifying the order in which properties will be applied (with index 0
being the first).
