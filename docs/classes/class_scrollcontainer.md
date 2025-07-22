github_url
:   hide

# ScrollContainer {#class_ScrollContainer}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}

A container used to provide scrollbars to a child control when needed.

::: rst-class
classref-introduction-group
:::

## Description

A container used to provide a child control with scrollbars when needed.
Scrollbars will automatically be drawn at the right (for vertical) or
bottom (for horizontal) and will enable dragging to move the viewable
Control (and its children) within the ScrollContainer. Scrollbars will
also automatically resize the grabber based on the
`Control.custom_minimum_size<class_Control_property_custom_minimum_size>`{.interpreted-text
role="ref"} of the Control relative to the ScrollContainer.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Containers <../tutorials/ui/gui_containers>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Theme Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Signals

:::: {#class_ScrollContainer_signal_scroll_ended}
::: rst-class
classref-signal
:::
::::

**scroll_ended**()
`🔗<class_ScrollContainer_signal_scroll_ended>`{.interpreted-text
role="ref"}

Emitted when scrolling stops when dragging the scrollable area *with a
touch event*. This signal is *not* emitted when scrolling by dragging
the scrollbar, scrolling with the mouse wheel or scrolling with
keyboard/gamepad events.

\*\*Note:\*\* This signal is only emitted on Android or iOS, or on
desktop/web platforms when
`ProjectSettings.input_devices/pointing/emulate_touch_from_mouse<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_signal_scroll_started}
::: rst-class
classref-signal
:::
::::

**scroll_started**()
`🔗<class_ScrollContainer_signal_scroll_started>`{.interpreted-text
role="ref"}

Emitted when scrolling starts when dragging the scrollable area w\*ith a
touch event\*. This signal is *not* emitted when scrolling by dragging
the scrollbar, scrolling with the mouse wheel or scrolling with
keyboard/gamepad events.

\*\*Note:\*\* This signal is only emitted on Android or iOS, or on
desktop/web platforms when
`ProjectSettings.input_devices/pointing/emulate_touch_from_mouse<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_ScrollContainer_ScrollMode}
::: rst-class
classref-enumeration
:::
::::

enum **ScrollMode**:
`🔗<enum_ScrollContainer_ScrollMode>`{.interpreted-text role="ref"}

:::: {#class_ScrollContainer_constant_SCROLL_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
role="ref"} **SCROLL_MODE_DISABLED** = `0`

Scrolling disabled, scrollbar will be invisible.

:::: {#class_ScrollContainer_constant_SCROLL_MODE_AUTO}
::: rst-class
classref-enumeration-constant
:::
::::

`ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
role="ref"} **SCROLL_MODE_AUTO** = `1`

Scrolling enabled, scrollbar will be visible only if necessary, i.e.
container\'s content is bigger than the container.

:::: {#class_ScrollContainer_constant_SCROLL_MODE_SHOW_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
role="ref"} **SCROLL_MODE_SHOW_ALWAYS** = `2`

Scrolling enabled, scrollbar will be always visible.

:::: {#class_ScrollContainer_constant_SCROLL_MODE_SHOW_NEVER}
::: rst-class
classref-enumeration-constant
:::
::::

`ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
role="ref"} **SCROLL_MODE_SHOW_NEVER** = `3`

Scrolling enabled, scrollbar will be hidden.

:::: {#class_ScrollContainer_constant_SCROLL_MODE_RESERVE}
::: rst-class
classref-enumeration-constant
:::
::::

`ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
role="ref"} **SCROLL_MODE_RESERVE** = `4`

Combines
`SCROLL_MODE_AUTO<class_ScrollContainer_constant_SCROLL_MODE_AUTO>`{.interpreted-text
role="ref"} and
`SCROLL_MODE_SHOW_ALWAYS<class_ScrollContainer_constant_SCROLL_MODE_SHOW_ALWAYS>`{.interpreted-text
role="ref"}. The scrollbar is only visible if necessary, but the content
size is adjusted as if it was always visible. It\'s useful for ensuring
that content size stays the same regardless if the scrollbar is visible.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ScrollContainer_property_draw_focus_border}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_focus_border** =
`false`
`🔗<class_ScrollContainer_property_draw_focus_border>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_focus_border**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_focus_border**()

If `true`,
`focus<class_ScrollContainer_theme_style_focus>`{.interpreted-text
role="ref"} is drawn when the ScrollContainer or one of its descendant
nodes is focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_property_follow_focus}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **follow_focus** =
`false`
`🔗<class_ScrollContainer_property_follow_focus>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_follow_focus**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_following_focus**()

If `true`, the ScrollContainer will automatically scroll to focused
children (including indirect children) to make sure they are fully
visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_property_horizontal_scroll_mode}
::: rst-class
classref-property
:::
::::

`ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
role="ref"} **horizontal_scroll_mode** = `1`
`🔗<class_ScrollContainer_property_horizontal_scroll_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_horizontal_scroll_mode**(value:
  `ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
  role="ref"})
- `ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
  role="ref"} **get_horizontal_scroll_mode**()

Controls whether horizontal scrollbar can be used and when it should be
visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_property_scroll_deadzone}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scroll_deadzone** = `0`
`🔗<class_ScrollContainer_property_scroll_deadzone>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_deadzone**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_deadzone**()

Deadzone for touch scrolling. Lower deadzone makes the scrolling more
sensitive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_property_scroll_horizontal}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scroll_horizontal** =
`0`
`🔗<class_ScrollContainer_property_scroll_horizontal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_h_scroll**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_h_scroll**()

The current horizontal scroll value.

\*\*Note:\*\* If you are setting this value in the
`Node._ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} function or earlier, it needs to be wrapped with
`Object.set_deferred()<class_Object_method_set_deferred>`{.interpreted-text
role="ref"}, since scroll bar\'s
`Range.max_value<class_Range_property_max_value>`{.interpreted-text
role="ref"} is not initialized yet.

    func _ready():
        set_deferred("scroll_horizontal", 600)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_property_scroll_horizontal_custom_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**scroll_horizontal_custom_step** = `-1.0`
`🔗<class_ScrollContainer_property_scroll_horizontal_custom_step>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_horizontal_custom_step**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_horizontal_custom_step**()

Overrides the
`ScrollBar.custom_step<class_ScrollBar_property_custom_step>`{.interpreted-text
role="ref"} used when clicking the internal scroll bar\'s horizontal
increment and decrement buttons or when using arrow keys when the
`ScrollBar<class_ScrollBar>`{.interpreted-text role="ref"} is focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_property_scroll_vertical}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scroll_vertical** = `0`
`🔗<class_ScrollContainer_property_scroll_vertical>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_scroll**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_v_scroll**()

The current vertical scroll value.

\*\*Note:\*\* Setting it early needs to be deferred, just like in
`scroll_horizontal<class_ScrollContainer_property_scroll_horizontal>`{.interpreted-text
role="ref"}.

    func _ready():
        set_deferred("scroll_vertical", 600)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_property_scroll_vertical_custom_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**scroll_vertical_custom_step** = `-1.0`
`🔗<class_ScrollContainer_property_scroll_vertical_custom_step>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertical_custom_step**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_vertical_custom_step**()

Overrides the
`ScrollBar.custom_step<class_ScrollBar_property_custom_step>`{.interpreted-text
role="ref"} used when clicking the internal scroll bar\'s vertical
increment and decrement buttons or when using arrow keys when the
`ScrollBar<class_ScrollBar>`{.interpreted-text role="ref"} is focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_property_vertical_scroll_mode}
::: rst-class
classref-property
:::
::::

`ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
role="ref"} **vertical_scroll_mode** = `1`
`🔗<class_ScrollContainer_property_vertical_scroll_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertical_scroll_mode**(value:
  `ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
  role="ref"})
- `ScrollMode<enum_ScrollContainer_ScrollMode>`{.interpreted-text
  role="ref"} **get_vertical_scroll_mode**()

Controls whether vertical scrollbar can be used and when it should be
visible.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ScrollContainer_method_ensure_control_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**ensure_control_visible**(control:
`Control<class_Control>`{.interpreted-text role="ref"})
`🔗<class_ScrollContainer_method_ensure_control_visible>`{.interpreted-text
role="ref"}

Ensures the given `control` is visible (must be a direct or indirect
child of the ScrollContainer). Used by
`follow_focus<class_ScrollContainer_property_follow_focus>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This will not work on a node that was just added during
the same frame. If you want to scroll to a newly added child, you must
wait until the next frame using
`SceneTree.process_frame<class_SceneTree_signal_process_frame>`{.interpreted-text
role="ref"}:

    add_child(child_node)
    await get_tree().process_frame
    ensure_control_visible(child_node)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_method_get_h_scroll_bar}
::: rst-class
classref-method
:::
::::

`HScrollBar<class_HScrollBar>`{.interpreted-text role="ref"}
**get_h_scroll_bar**()
`🔗<class_ScrollContainer_method_get_h_scroll_bar>`{.interpreted-text
role="ref"}

Returns the horizontal scrollbar
`HScrollBar<class_HScrollBar>`{.interpreted-text role="ref"} of this
**ScrollContainer**.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to disable or hide a scrollbar, you
can use
`horizontal_scroll_mode<class_ScrollContainer_property_horizontal_scroll_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_method_get_v_scroll_bar}
::: rst-class
classref-method
:::
::::

`VScrollBar<class_VScrollBar>`{.interpreted-text role="ref"}
**get_v_scroll_bar**()
`🔗<class_ScrollContainer_method_get_v_scroll_bar>`{.interpreted-text
role="ref"}

Returns the vertical scrollbar
`VScrollBar<class_VScrollBar>`{.interpreted-text role="ref"} of this
**ScrollContainer**.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to disable or hide a scrollbar, you
can use
`vertical_scroll_mode<class_ScrollContainer_property_vertical_scroll_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_ScrollContainer_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_ScrollContainer_theme_style_focus>`{.interpreted-text
role="ref"}

The focus border `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"} of the **ScrollContainer**. Only used if
`draw_focus_border<class_ScrollContainer_property_draw_focus_border>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScrollContainer_theme_style_panel}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **panel**
`🔗<class_ScrollContainer_theme_style_panel>`{.interpreted-text
role="ref"}

The background `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
of the **ScrollContainer**.
