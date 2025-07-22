article_outdated
:   True

# Custom GUI controls {#doc_custom_gui_controls}

## So many controls\...

Yet there are never enough. Creating your own custom controls that act
just the way you want them to is an obsession of almost every GUI
programmer. Godot provides plenty of them, but they may not work exactly
the way you want. Before contacting the developers with a pull-request
to support diagonal scrollbars, at least it will be good to know how to
create these controls easily from script.

## Drawing

For drawing, it is recommended to check the
`doc_custom_drawing_in_2d`{.interpreted-text role="ref"} tutorial. The
same applies. Some functions are worth mentioning due to their
usefulness when drawing, so they will be detailed next:

### Checking control size

Unlike 2D nodes, \"size\" is important with controls, as it helps to
organize them in proper layouts. For this, the
`Control.size <class_Control_property_size>`{.interpreted-text
role="ref"} property is provided. Checking it during `_draw()` is vital
to ensure everything is kept in-bounds.

### Checking focus

Some controls (such as buttons or text editors) might provide input
focus for keyboard or joypad input. Examples of this are entering text
or pressing a button. This is controlled with the
`Control.focus_mode <class_Control_property_focus_mode>`{.interpreted-text
role="ref"} property. When drawing, and if the control supports input
focus, it is always desired to show some sort of indicator (highlight,
box, etc.) to indicate that this is the currently focused control. To
check for this status, the
`Control.has_focus() <class_Control_method_has_focus>`{.interpreted-text
role="ref"} method exists. Example

:::: tabs
.. code-tab:: gdscript GDScript

func [draw]{#draw}():

:   

    if has_focus():

    :   draw_selected()

    else:

    :   draw_normal()

::: code-tab
csharp
:::

public override void [Draw]{#draw}() { if (HasFocus()) { DrawSelected()
} else { DrawNormal(); } }
::::

## Sizing

As mentioned before, size is important to controls. This allows them to
lay out properly, when set into grids, containers, or anchored.
Controls, most of the time, provide a *minimum size* to help properly
lay them out. For example, if controls are placed vertically on top of
each other using a
`VBoxContainer <class_VBoxContainer>`{.interpreted-text role="ref"}, the
minimum size will make sure your custom control is not squished by the
other controls in the container.

To provide this callback, just override
`Control._get_minimum_size() <class_Control_private_method__get_minimum_size>`{.interpreted-text
role="ref"}, for example:

:::: tabs
.. code-tab:: gdscript GDScript

func [get_minimum_size]{#get_minimum_size}():

:   return Vector2(30, 30)

::: code-tab
csharp
:::

public override Vector2 [GetMinimumSize]{#getminimumsize}() { return new
Vector2(20, 20); }
::::

Alternatively, set it using a function:

:::: tabs
.. code-tab:: gdscript GDScript

func [ready]{#ready}():

:   set_custom_minimum_size(Vector2(30, 30))

::: code-tab
csharp
:::

public override void [Ready]{#ready}() { CustomMinimumSize = new
Vector2(20, 20); }
::::

## Input

Controls provide a few helpers to make managing input events much easier
than regular nodes.

### Input events

There are a few tutorials about input before this one, but it\'s worth
mentioning that controls have a special input method that only works
when:

- The mouse pointer is over the control.
- The button was pressed over this control (control always captures
  input until button is released)
- Control provides keyboard/joypad focus via
  `Control.focus_mode <class_Control_property_focus_mode>`{.interpreted-text
  role="ref"}.

This function is
`Control._gui_input() <class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}. To use it, override it in your control. No processing needs
to be set.

:::: tabs
.. code-tab:: gdscript GDScript

extends Control

func [gui_input]{#gui_input}(event):

:   

    if event is InputEventMouseButton and event.button_index == MOUSE_BUTTON_LEFT and event.pressed:

    :   print(\"Left mouse button was pressed!\")

::: code-tab
csharp
:::

public override void [GuiInput]{#guiinput}(InputEvent \@event) { if
(@event is InputEventMouseButton mbe && mbe.ButtonIndex ==
MouseButton.Left && mbe.Pressed) { GD.Print(\"Left mouse button was
pressed!\"); } }
::::

For more information about events themselves, check the
`doc_inputevent`{.interpreted-text role="ref"} tutorial.

### Notifications

Controls also have many useful notifications for which no dedicated
callback exists, but which can be checked with the
[notification]{#notification} callback:

:::: tabs
.. code-tab:: gdscript GDScript

func [notification]{#notification}(what):

:   

    match what:

    :   

        NOTIFICATION_MOUSE_ENTER:

        :   pass \# Mouse entered the area of this control.

        NOTIFICATION_MOUSE_EXIT:

        :   pass \# Mouse exited the area of this control.

        NOTIFICATION_FOCUS_ENTER:

        :   pass \# Control gained focus.

        NOTIFICATION_FOCUS_EXIT:

        :   pass \# Control lost focus.

        NOTIFICATION_THEME_CHANGED:

        :   pass \# Theme used to draw the control changed; \# update
            and redraw is recommended if using a theme.

        NOTIFICATION_VISIBILITY_CHANGED:

        :   pass \# Control became visible/invisible; \# check new
            status with is_visible().

        NOTIFICATION_RESIZED:

        :   pass \# Control changed size; check new size \# with
            get_size().

        NOTIFICATION_MODAL_CLOSE:

        :   pass \# For modal pop-ups, notification \# that the pop-up
            was closed.

::: code-tab
csharp
:::

public override void [Notification]{#notification}(int what) { switch
(what) { case NotificationMouseEnter: // Mouse entered the area of this
control. break;

> 
>
> case NotificationMouseExit:
>
> :   // Mouse exited the area of this control. break;
>
> case NotificationFocusEnter:
>
> :   // Control gained focus. break;
>
> case NotificationFocusExit:
>
> :   // Control lost focus. break;
>
> case NotificationThemeChanged:
>
> :   // Theme used to draw the control changed; // update and redraw is
>     recommended if using a theme. break;
>
> case NotificationVisibilityChanged:
>
> :   // Control became visible/invisible; // check new status with
>     is_visible(). break;
>
> case NotificationResized:
>
> :   // Control changed size; check new size with get_size(). break;
>
> case NotificationModalClose:
>
> :   // For modal pop-ups, notification that the pop-up was closed.
>     break;
>
> }

}
::::
