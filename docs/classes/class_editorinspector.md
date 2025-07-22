github_url
:   hide

# EditorInspector {#class_EditorInspector}

**Inherits:** `ScrollContainer<class_ScrollContainer>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A control used to edit properties of an object.

::: rst-class
classref-introduction-group
:::

## Description

This is the control that implements property editing in the editor\'s
Settings dialogs, the Inspector dock, etc. To get the
**EditorInspector** used in the editor\'s Inspector dock, use
`EditorInterface.get_inspector()<class_EditorInterface_method_get_inspector>`{.interpreted-text
role="ref"}.

\*\*EditorInspector\*\* will show properties in the same order as the
array returned by
`Object.get_property_list()<class_Object_method_get_property_list>`{.interpreted-text
role="ref"}.

If a property\'s name is path-like (i.e. if it contains forward
slashes), **EditorInspector** will create nested sections for
\"directories\" along the path. For example, if a property is named
`highlighting/gdscript/node_path_color`, it will be shown as \"Node Path
Color\" inside the \"GDScript\" section nested inside the
\"Highlighting\" section.

If a property has
`@GlobalScope.PROPERTY_USAGE_GROUP<class_@GlobalScope_constant_PROPERTY_USAGE_GROUP>`{.interpreted-text
role="ref"} usage, it will group subsequent properties whose name starts
with the property\'s hint string. The group ends when a property does
not start with that hint string or when a new group starts. An empty
group name effectively ends the current group. **EditorInspector** will
create a top-level section for each group. For example, if a property
with group usage is named `Collide With` and its hint string is
`collide_with_`, a subsequent `collide_with_area` property will be shown
as \"Area\" inside the \"Collide With\" section. There is also a special
case: when the hint string contains the name of a property, that
property is grouped too. This is mainly to help grouping properties like
`font`, `font_color` and `font_size` (using the hint string `font_`).

If a property has
`@GlobalScope.PROPERTY_USAGE_SUBGROUP<class_@GlobalScope_constant_PROPERTY_USAGE_SUBGROUP>`{.interpreted-text
role="ref"} usage, a subgroup will be created in the same way as a
group, and a second-level section will be created for each subgroup.

\*\*Note:\*\* Unlike sections created from path-like property names,
**EditorInspector** won\'t capitalize the name for sections created from
groups. So properties with group usage usually use capitalized names
instead of snake_cased names.

::: rst-class
classref-reftable-group
:::

## Properties

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

## Signals

:::: {#class_EditorInspector_signal_edited_object_changed}
::: rst-class
classref-signal
:::
::::

**edited_object_changed**()
`🔗<class_EditorInspector_signal_edited_object_changed>`{.interpreted-text
role="ref"}

Emitted when the object being edited by the inspector has changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_signal_object_id_selected}
::: rst-class
classref-signal
:::
::::

**object_id_selected**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_EditorInspector_signal_object_id_selected>`{.interpreted-text
role="ref"}

Emitted when the Edit button of an
`Object<class_Object>`{.interpreted-text role="ref"} has been pressed in
the inspector. This is mainly used in the remote scene tree Inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_signal_property_deleted}
::: rst-class
classref-signal
:::
::::

**property_deleted**(property: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorInspector_signal_property_deleted>`{.interpreted-text
role="ref"}

Emitted when a property is removed from the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_signal_property_edited}
::: rst-class
classref-signal
:::
::::

**property_edited**(property: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorInspector_signal_property_edited>`{.interpreted-text
role="ref"}

Emitted when a property is edited in the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_signal_property_keyed}
::: rst-class
classref-signal
:::
::::

**property_keyed**(property: `String<class_String>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"}, advance: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorInspector_signal_property_keyed>`{.interpreted-text
role="ref"}

Emitted when a property is keyed in the inspector. Properties can be
keyed by clicking the \"key\" icon next to a property when the Animation
panel is toggled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_signal_property_selected}
::: rst-class
classref-signal
:::
::::

**property_selected**(property: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorInspector_signal_property_selected>`{.interpreted-text
role="ref"}

Emitted when a property is selected in the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_signal_property_toggled}
::: rst-class
classref-signal
:::
::::

**property_toggled**(property: `String<class_String>`{.interpreted-text
role="ref"}, checked: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorInspector_signal_property_toggled>`{.interpreted-text
role="ref"}

Emitted when a boolean property is toggled in the inspector.

\*\*Note:\*\* This signal is never emitted if the internal `autoclear`
property enabled. Since this property is always enabled in the editor
inspector, this signal is never emitted by the editor itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_signal_resource_selected}
::: rst-class
classref-signal
:::
::::

**resource_selected**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"}, path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorInspector_signal_resource_selected>`{.interpreted-text
role="ref"}

Emitted when a resource is selected in the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_signal_restart_requested}
::: rst-class
classref-signal
:::
::::

**restart_requested**()
`🔗<class_EditorInspector_signal_restart_requested>`{.interpreted-text
role="ref"}

Emitted when a property that requires a restart to be applied is edited
in the inspector. This is only used in the Project Settings and Editor
Settings.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorInspector_method_edit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**edit**(object: `Object<class_Object>`{.interpreted-text role="ref"})
`🔗<class_EditorInspector_method_edit>`{.interpreted-text role="ref"}

Shows the properties of the given `object` in this inspector for
editing. To clear the inspector, call this method with `null`.

\*\*Note:\*\* If you want to edit an object in the editor\'s main
inspector, use the `edit_*` methods in
`EditorInterface<class_EditorInterface>`{.interpreted-text role="ref"}
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_method_get_edited_object}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**get_edited_object**()
`🔗<class_EditorInspector_method_get_edited_object>`{.interpreted-text
role="ref"}

Returns the object currently selected in this inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_method_get_selected_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_selected_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInspector_method_get_selected_path>`{.interpreted-text
role="ref"}

Gets the path of the currently selected property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspector_method_instantiate_property_editor}
::: rst-class
classref-method
:::
::::

`EditorProperty<class_EditorProperty>`{.interpreted-text role="ref"}
**instantiate_property_editor**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, type:
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"}, path: `String<class_String>`{.interpreted-text role="ref"},
hint: `PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"}, hint_text: `String<class_String>`{.interpreted-text
role="ref"}, usage: `int<class_int>`{.interpreted-text role="ref"},
wide: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInspector_method_instantiate_property_editor>`{.interpreted-text
role="ref"}

Creates a property editor that can be used by plugin UI to edit the
specified property of an `object`.
