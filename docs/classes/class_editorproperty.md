github_url
:   hide

# EditorProperty {#class_EditorProperty}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Custom control for editing properties that can be added to the
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A custom control for editing properties that can be added to the
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}.
It is added via
`EditorInspectorPlugin<class_EditorInspectorPlugin>`{.interpreted-text
role="ref"}.

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

:::: {#class_EditorProperty_signal_multiple_properties_changed}
::: rst-class
classref-signal
:::
::::

**multiple_properties_changed**(properties:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, value: `Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_multiple_properties_changed>`{.interpreted-text
role="ref"}

Emit it if you want multiple properties modified at the same time. Do
not use if added via
`EditorInspectorPlugin._parse_property()<class_EditorInspectorPlugin_private_method__parse_property>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_object_id_selected}
::: rst-class
classref-signal
:::
::::

**object_id_selected**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_object_id_selected>`{.interpreted-text
role="ref"}

Used by sub-inspectors. Emit it if what was selected was an Object ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_property_can_revert_changed}
::: rst-class
classref-signal
:::
::::

**property_can_revert_changed**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"},
can_revert: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_property_can_revert_changed>`{.interpreted-text
role="ref"}

Emitted when the revertability (i.e., whether it has a non-default value
and thus is displayed with a revert icon) of a property has changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_property_changed}
::: rst-class
classref-signal
:::
::::

**property_changed**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, field:
`StringName<class_StringName>`{.interpreted-text role="ref"}, changing:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_property_changed>`{.interpreted-text
role="ref"}

Do not emit this manually, use the
`emit_changed()<class_EditorProperty_method_emit_changed>`{.interpreted-text
role="ref"} method instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_property_checked}
::: rst-class
classref-signal
:::
::::

**property_checked**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, checked:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_property_checked>`{.interpreted-text
role="ref"}

Emitted when a property was checked. Used internally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_property_deleted}
::: rst-class
classref-signal
:::
::::

**property_deleted**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_property_deleted>`{.interpreted-text
role="ref"}

Emitted when a property was deleted. Used internally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_property_favorited}
::: rst-class
classref-signal
:::
::::

**property_favorited**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, favorited:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_property_favorited>`{.interpreted-text
role="ref"}

Emit it if you want to mark a property as favorited, making it appear at
the top of the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_property_keyed}
::: rst-class
classref-signal
:::
::::

**property_keyed**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_property_keyed>`{.interpreted-text
role="ref"}

Emit it if you want to add this value as an animation key (check for
keying being enabled first).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_property_keyed_with_value}
::: rst-class
classref-signal
:::
::::

**property_keyed_with_value**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_property_keyed_with_value>`{.interpreted-text
role="ref"}

Emit it if you want to key a property with a single value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_property_overridden}
::: rst-class
classref-signal
:::
::::

**property_overridden**()
`🔗<class_EditorProperty_signal_property_overridden>`{.interpreted-text
role="ref"}

Emitted when a setting override for the current project is requested.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_property_pinned}
::: rst-class
classref-signal
:::
::::

**property_pinned**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, pinned:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_property_pinned>`{.interpreted-text
role="ref"}

Emit it if you want to mark (or unmark) the value of a property for
being saved regardless of being equal to the default value.

The default value is the one the property will get when the node is just
instantiated and can come from an ancestor scene in the
inheritance/instantiation chain, a script or a builtin class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_resource_selected}
::: rst-class
classref-signal
:::
::::

**resource_selected**(path: `String<class_String>`{.interpreted-text
role="ref"}, resource: `Resource<class_Resource>`{.interpreted-text
role="ref"})
`🔗<class_EditorProperty_signal_resource_selected>`{.interpreted-text
role="ref"}

If you want a sub-resource to be edited, emit this signal with the
resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_signal_selected}
::: rst-class
classref-signal
:::
::::

**selected**(path: `String<class_String>`{.interpreted-text role="ref"},
focusable_idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_signal_selected>`{.interpreted-text role="ref"}

Emitted when selected. Used internally.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_EditorProperty_property_checkable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **checkable** = `false`
`🔗<class_EditorProperty_property_checkable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_checkable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_checkable**()

Used by the inspector, set to `true` when the property is checkable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_checked}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **checked** = `false`
`🔗<class_EditorProperty_property_checked>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_checked**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_checked**()

Used by the inspector, set to `true` when the property is checked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_deletable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **deletable** = `false`
`🔗<class_EditorProperty_property_deletable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_deletable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_deletable**()

Used by the inspector, set to `true` when the property can be deleted by
the user.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_draw_background}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_background** =
`true`
`🔗<class_EditorProperty_property_draw_background>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_background**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_draw_background**()

Used by the inspector, set to `true` when the property background is
drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_draw_label}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_label** = `true`
`🔗<class_EditorProperty_property_draw_label>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_label**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_draw_label**()

Used by the inspector, set to `true` when the property label is drawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_draw_warning}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_warning** =
`false`
`🔗<class_EditorProperty_property_draw_warning>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_warning**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_draw_warning**()

Used by the inspector, set to `true` when the property is drawn with the
editor theme\'s warning color. This is used for editable children\'s
properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_keying}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **keying** = `false`
`🔗<class_EditorProperty_property_keying>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keying**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_keying**()

Used by the inspector, set to `true` when the property can add keys for
animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_label}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **label** = `""`
`🔗<class_EditorProperty_property_label>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_label**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_label**()

Set this property to change the label (if you want to show one).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_name_split_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **name_split_ratio**
= `0.5`
`🔗<class_EditorProperty_property_name_split_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_name_split_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_name_split_ratio**()

Space distribution ratio between the label and the editing field.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_read_only}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **read_only** = `false`
`🔗<class_EditorProperty_property_read_only>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_read_only**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_read_only**()

Used by the inspector, set to `true` when the property is read-only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_selectable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **selectable** = `true`
`🔗<class_EditorProperty_property_selectable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_selectable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_selectable**()

Used by the inspector, set to `true` when the property is selectable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_property_use_folding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_folding** =
`false`
`🔗<class_EditorProperty_property_use_folding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_folding**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_folding**()

Used by the inspector, set to `true` when the property is using folding.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorProperty_private_method__set_read_only}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_read_only**(read_only: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorProperty_private_method__set_read_only>`{.interpreted-text
role="ref"}

Called when the read-only status of the property is changed. It may be
used to change custom controls into a read-only or modifiable state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_private_method__update_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_update_property**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorProperty_private_method__update_property>`{.interpreted-text
role="ref"}

When this virtual function is called, you must update your editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_add_focusable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_focusable**(control: `Control<class_Control>`{.interpreted-text
role="ref"})
`🔗<class_EditorProperty_method_add_focusable>`{.interpreted-text
role="ref"}

If any of the controls added can gain keyboard focus, add it here. This
ensures that focus will be restored if the inspector is refreshed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_deselect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **deselect**()
`🔗<class_EditorProperty_method_deselect>`{.interpreted-text role="ref"}

Draw property as not selected. Used by the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_emit_changed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**emit_changed**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, field:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
changing: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_EditorProperty_method_emit_changed>`{.interpreted-text
role="ref"}

If one or several properties have changed, this must be called. `field`
is used in case your editor can modify fields separately (as an example,
Vector3.x). The `changing` argument avoids the editor requesting this
property to be refreshed (leave as `false` if unsure).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_get_edited_object}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**get_edited_object**()
`🔗<class_EditorProperty_method_get_edited_object>`{.interpreted-text
role="ref"}

Returns the edited object.

\*\*Note:\*\* This method could return `null` if the editor has not yet
been associated with a property. However, in
`_update_property()<class_EditorProperty_private_method__update_property>`{.interpreted-text
role="ref"} and
`_set_read_only()<class_EditorProperty_private_method__set_read_only>`{.interpreted-text
role="ref"}, this value is *guaranteed* to be non-`null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_get_edited_property}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_edited_property**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorProperty_method_get_edited_property>`{.interpreted-text
role="ref"}

Returns the edited property. If your editor is for a single property
(added via
`EditorInspectorPlugin._parse_property()<class_EditorInspectorPlugin_private_method__parse_property>`{.interpreted-text
role="ref"}), then this will return the property.

\*\*Note:\*\* This method could return `null` if the editor has not yet
been associated with a property. However, in
`_update_property()<class_EditorProperty_private_method__update_property>`{.interpreted-text
role="ref"} and
`_set_read_only()<class_EditorProperty_private_method__set_read_only>`{.interpreted-text
role="ref"}, this value is *guaranteed* to be non-`null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_is_selected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_selected**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorProperty_method_is_selected>`{.interpreted-text
role="ref"}

Returns `true` if property is drawn as selected. Used by the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_select}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**select**(focusable: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_EditorProperty_method_select>`{.interpreted-text
role="ref"}

Draw property as selected. Used by the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_set_bottom_editor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bottom_editor**(editor: `Control<class_Control>`{.interpreted-text
role="ref"})
`🔗<class_EditorProperty_method_set_bottom_editor>`{.interpreted-text
role="ref"}

Puts the `editor` control below the property label. The control must be
previously added using
`Node.add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_set_label_reference}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_label_reference**(control:
`Control<class_Control>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_method_set_label_reference>`{.interpreted-text
role="ref"}

Used by the inspector, set to a control that will be used as a reference
to calculate the size of the label.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_set_object_and_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_object_and_property**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_EditorProperty_method_set_object_and_property>`{.interpreted-text
role="ref"}

Assigns object and property to edit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorProperty_method_update_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_property**()
`🔗<class_EditorProperty_method_update_property>`{.interpreted-text
role="ref"}

Forces a refresh of the property display.
