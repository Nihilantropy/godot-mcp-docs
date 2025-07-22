github_url
:   hide

# EditorInspectorPlugin {#class_EditorInspectorPlugin}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Plugin for adding custom property editors on the inspector.

::: rst-class
classref-introduction-group
:::

## Description

**EditorInspectorPlugin** allows adding custom property editors to
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}.

When an object is edited, the
`_can_handle()<class_EditorInspectorPlugin_private_method__can_handle>`{.interpreted-text
role="ref"} function is called and must return `true` if the object type
is supported.

If supported, the function
`_parse_begin()<class_EditorInspectorPlugin_private_method__parse_begin>`{.interpreted-text
role="ref"} will be called, allowing to place custom controls at the
beginning of the class.

Subsequently, the
`_parse_category()<class_EditorInspectorPlugin_private_method__parse_category>`{.interpreted-text
role="ref"} and
`_parse_property()<class_EditorInspectorPlugin_private_method__parse_property>`{.interpreted-text
role="ref"} are called for every category and property. They offer the
ability to add custom controls to the inspector too.

Finally,
`_parse_end()<class_EditorInspectorPlugin_private_method__parse_end>`{.interpreted-text
role="ref"} will be called.

On each of these calls, the \"add\" functions can be called.

To use **EditorInspectorPlugin**, register it using the
`EditorPlugin.add_inspector_plugin()<class_EditorPlugin_method_add_inspector_plugin>`{.interpreted-text
role="ref"} method first.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Inspector plugins <../tutorials/plugins/editor/inspector_plugins>`{.interpreted-text
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

## Method Descriptions

:::: {#class_EditorInspectorPlugin_private_method__can_handle}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_can_handle**(object: `Object<class_Object>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInspectorPlugin_private_method__can_handle>`{.interpreted-text
role="ref"}

Returns `true` if this object can be handled by this plugin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspectorPlugin_private_method__parse_begin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_parse_begin**(object: `Object<class_Object>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInspectorPlugin_private_method__parse_begin>`{.interpreted-text
role="ref"}

Called to allow adding controls at the beginning of the property list
for `object`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspectorPlugin_private_method__parse_category}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_parse_category**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, category: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInspectorPlugin_private_method__parse_category>`{.interpreted-text
role="ref"}

Called to allow adding controls at the beginning of a category in the
property list for `object`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspectorPlugin_private_method__parse_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_parse_end**(object: `Object<class_Object>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInspectorPlugin_private_method__parse_end>`{.interpreted-text
role="ref"}

Called to allow adding controls at the end of the property list for
`object`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspectorPlugin_private_method__parse_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_parse_group**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, group: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInspectorPlugin_private_method__parse_group>`{.interpreted-text
role="ref"}

Called to allow adding controls at the beginning of a group or a
sub-group in the property list for `object`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspectorPlugin_private_method__parse_property}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_parse_property**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, type:
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"},
hint_type:
`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"}, hint_string: `String<class_String>`{.interpreted-text
role="ref"}, usage_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"}\], wide: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInspectorPlugin_private_method__parse_property>`{.interpreted-text
role="ref"}

Called to allow adding property-specific editors to the property list
for `object`. The added editor control must extend
`EditorProperty<class_EditorProperty>`{.interpreted-text role="ref"}.
Returning `true` removes the built-in editor for this property,
otherwise allows to insert a custom editor before the built-in one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspectorPlugin_method_add_custom_control}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_custom_control**(control:
`Control<class_Control>`{.interpreted-text role="ref"})
`🔗<class_EditorInspectorPlugin_method_add_custom_control>`{.interpreted-text
role="ref"}

Adds a custom control, which is not necessarily a property editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspectorPlugin_method_add_property_editor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_property_editor**(property:
`String<class_String>`{.interpreted-text role="ref"}, editor:
`Control<class_Control>`{.interpreted-text role="ref"}, add_to_end:
`bool<class_bool>`{.interpreted-text role="ref"} = false, label:
`String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_EditorInspectorPlugin_method_add_property_editor>`{.interpreted-text
role="ref"}

Adds a property editor for an individual property. The `editor` control
must extend `EditorProperty<class_EditorProperty>`{.interpreted-text
role="ref"}.

There can be multiple property editors for a property. If `add_to_end`
is `true`, this newly added editor will be displayed after all the other
editors of the property whose `add_to_end` is `false`. For example, the
editor uses this parameter to add an \"Edit Region\" button for
`Sprite2D.region_rect<class_Sprite2D_property_region_rect>`{.interpreted-text
role="ref"} below the regular `Rect2<class_Rect2>`{.interpreted-text
role="ref"} editor.

`label` can be used to choose a custom label for the property editor in
the inspector. If left empty, the label is computed from the name of the
property instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInspectorPlugin_method_add_property_editor_for_multiple_properties}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_property_editor_for_multiple_properties**(label:
`String<class_String>`{.interpreted-text role="ref"}, properties:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, editor: `Control<class_Control>`{.interpreted-text
role="ref"})
`🔗<class_EditorInspectorPlugin_method_add_property_editor_for_multiple_properties>`{.interpreted-text
role="ref"}

Adds an editor that allows modifying multiple properties. The `editor`
control must extend
`EditorProperty<class_EditorProperty>`{.interpreted-text role="ref"}.
