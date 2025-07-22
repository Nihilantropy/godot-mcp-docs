github_url
:   hide

# OpenXRBindingModifierEditor {#class_OpenXRBindingModifierEditor}

**Inherits:** `PanelContainer<class_PanelContainer>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Binding modifier editor.

::: rst-class
classref-introduction-group
:::

## Description

This is the default binding modifier editor used in the OpenXR action
map.

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

:::: {#class_OpenXRBindingModifierEditor_signal_binding_modifier_removed}
::: rst-class
classref-signal
:::
::::

**binding_modifier_removed**(binding_modifier_editor:
`Object<class_Object>`{.interpreted-text role="ref"})
`🔗<class_OpenXRBindingModifierEditor_signal_binding_modifier_removed>`{.interpreted-text
role="ref"}

Signal emitted when the user presses the delete binding modifier button
for this modifier.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRBindingModifierEditor_method_get_binding_modifier}
::: rst-class
classref-method
:::
::::

`OpenXRBindingModifier<class_OpenXRBindingModifier>`{.interpreted-text
role="ref"} **get_binding_modifier**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRBindingModifierEditor_method_get_binding_modifier>`{.interpreted-text
role="ref"}

Returns the
`OpenXRBindingModifier<class_OpenXRBindingModifier>`{.interpreted-text
role="ref"} currently being edited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRBindingModifierEditor_method_setup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**setup**(action_map:
`OpenXRActionMap<class_OpenXRActionMap>`{.interpreted-text role="ref"},
binding_modifier:
`OpenXRBindingModifier<class_OpenXRBindingModifier>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRBindingModifierEditor_method_setup>`{.interpreted-text
role="ref"}

Setup this editor for the provided `action_map` and `binding_modifier`.
