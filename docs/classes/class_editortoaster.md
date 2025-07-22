github_url
:   hide

# EditorToaster {#class_EditorToaster}

**Inherits:** `HBoxContainer<class_HBoxContainer>`{.interpreted-text
role="ref"} **\<** `BoxContainer<class_BoxContainer>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Manages toast notifications within the editor.

::: rst-class
classref-introduction-group
:::

## Description

This object manages the functionality and display of toast notifications
within the editor, ensuring timely and informative alerts are presented
to users.

\*\*Note:\*\* This class shouldn\'t be instantiated directly. Instead,
access the singleton using
`EditorInterface.get_editor_toaster()<class_EditorInterface_method_get_editor_toaster>`{.interpreted-text
role="ref"}.

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

:::: {#enum_EditorToaster_Severity}
::: rst-class
classref-enumeration
:::
::::

enum **Severity**: `🔗<enum_EditorToaster_Severity>`{.interpreted-text
role="ref"}

:::: {#class_EditorToaster_constant_SEVERITY_INFO}
::: rst-class
classref-enumeration-constant
:::
::::

`Severity<enum_EditorToaster_Severity>`{.interpreted-text role="ref"}
**SEVERITY_INFO** = `0`

Toast will display with an INFO severity.

:::: {#class_EditorToaster_constant_SEVERITY_WARNING}
::: rst-class
classref-enumeration-constant
:::
::::

`Severity<enum_EditorToaster_Severity>`{.interpreted-text role="ref"}
**SEVERITY_WARNING** = `1`

Toast will display with a WARNING severity and have a corresponding
color.

:::: {#class_EditorToaster_constant_SEVERITY_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Severity<enum_EditorToaster_Severity>`{.interpreted-text role="ref"}
**SEVERITY_ERROR** = `2`

Toast will display with an ERROR severity and have a corresponding
color.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorToaster_method_push_toast}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_toast**(message: `String<class_String>`{.interpreted-text
role="ref"}, severity:
`Severity<enum_EditorToaster_Severity>`{.interpreted-text role="ref"} =
0, tooltip: `String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_EditorToaster_method_push_toast>`{.interpreted-text
role="ref"}

Pushes a toast notification to the editor for display.
