github_url
:   hide

# Window {#class_Window}

**Inherits:** `Viewport<class_Viewport>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `AcceptDialog<class_AcceptDialog>`{.interpreted-text
role="ref"}, `Popup<class_Popup>`{.interpreted-text role="ref"}

Base class for all windows, dialogs, and popups.

::: rst-class
classref-introduction-group
:::

## Description

A node that creates a window. The window can either be a native system
window or embedded inside another **Window** (see
`Viewport.gui_embed_subwindows<class_Viewport_property_gui_embed_subwindows>`{.interpreted-text
role="ref"}).

At runtime, **Window**s will not close automatically when requested. You
need to handle it manually using the
`close_requested<class_Window_signal_close_requested>`{.interpreted-text
role="ref"} signal (this applies both to pressing the close button and
clicking outside of a popup).

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

:::: {#class_Window_signal_about_to_popup}
::: rst-class
classref-signal
:::
::::

**about_to_popup**()
`🔗<class_Window_signal_about_to_popup>`{.interpreted-text role="ref"}

Emitted right after
`popup()<class_Window_method_popup>`{.interpreted-text role="ref"} call,
before the **Window** appears or does anything.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_close_requested}
::: rst-class
classref-signal
:::
::::

**close_requested**()
`🔗<class_Window_signal_close_requested>`{.interpreted-text role="ref"}

Emitted when the **Window**\'s close button is pressed or when
`popup_window<class_Window_property_popup_window>`{.interpreted-text
role="ref"} is enabled and user clicks outside the window.

This signal can be used to handle window closing, e.g. by connecting it
to `hide()<class_Window_method_hide>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_dpi_changed}
::: rst-class
classref-signal
:::
::::

**dpi_changed**()
`🔗<class_Window_signal_dpi_changed>`{.interpreted-text role="ref"}

Emitted when the **Window**\'s DPI changes as a result of OS-level
changes (e.g. moving the window from a Retina display to a lower
resolution one).

\*\*Note:\*\* Only implemented on macOS and Linux (Wayland).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_files_dropped}
::: rst-class
classref-signal
:::
::::

**files_dropped**(files:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}) `🔗<class_Window_signal_files_dropped>`{.interpreted-text
role="ref"}

Emitted when files are dragged from the OS file manager and dropped in
the game window. The argument is a list of file paths.

    func _ready():
        get_window().files_dropped.connect(on_files_dropped)

    func on_files_dropped(files):
        print(files)

\*\*Note:\*\* This signal only works with native windows, i.e. the main
window and **Window**-derived nodes when
`Viewport.gui_embed_subwindows<class_Viewport_property_gui_embed_subwindows>`{.interpreted-text
role="ref"} is disabled in the main viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_focus_entered}
::: rst-class
classref-signal
:::
::::

**focus_entered**()
`🔗<class_Window_signal_focus_entered>`{.interpreted-text role="ref"}

Emitted when the **Window** gains focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_focus_exited}
::: rst-class
classref-signal
:::
::::

**focus_exited**()
`🔗<class_Window_signal_focus_exited>`{.interpreted-text role="ref"}

Emitted when the **Window** loses its focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_go_back_requested}
::: rst-class
classref-signal
:::
::::

**go_back_requested**()
`🔗<class_Window_signal_go_back_requested>`{.interpreted-text
role="ref"}

Emitted when a go back request is sent (e.g. pressing the \"Back\"
button on Android), right after
`Node.NOTIFICATION_WM_GO_BACK_REQUEST<class_Node_constant_NOTIFICATION_WM_GO_BACK_REQUEST>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_mouse_entered}
::: rst-class
classref-signal
:::
::::

**mouse_entered**()
`🔗<class_Window_signal_mouse_entered>`{.interpreted-text role="ref"}

Emitted when the mouse cursor enters the **Window**\'s visible area,
that is not occluded behind other
`Control<class_Control>`{.interpreted-text role="ref"}s or windows,
provided its
`Viewport.gui_disable_input<class_Viewport_property_gui_disable_input>`{.interpreted-text
role="ref"} is `false` and regardless if it\'s currently focused or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_mouse_exited}
::: rst-class
classref-signal
:::
::::

**mouse_exited**()
`🔗<class_Window_signal_mouse_exited>`{.interpreted-text role="ref"}

Emitted when the mouse cursor leaves the **Window**\'s visible area,
that is not occluded behind other
`Control<class_Control>`{.interpreted-text role="ref"}s or windows,
provided its
`Viewport.gui_disable_input<class_Viewport_property_gui_disable_input>`{.interpreted-text
role="ref"} is `false` and regardless if it\'s currently focused or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_theme_changed}
::: rst-class
classref-signal
:::
::::

**theme_changed**()
`🔗<class_Window_signal_theme_changed>`{.interpreted-text role="ref"}

Emitted when the
`NOTIFICATION_THEME_CHANGED<class_Window_constant_NOTIFICATION_THEME_CHANGED>`{.interpreted-text
role="ref"} notification is sent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_title_changed}
::: rst-class
classref-signal
:::
::::

**title_changed**()
`🔗<class_Window_signal_title_changed>`{.interpreted-text role="ref"}

Emitted when window title bar text is changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_titlebar_changed}
::: rst-class
classref-signal
:::
::::

**titlebar_changed**()
`🔗<class_Window_signal_titlebar_changed>`{.interpreted-text role="ref"}

Emitted when window title bar decorations are changed, e.g. macOS window
enter/exit full screen mode, or extend-to-title flag is changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_visibility_changed}
::: rst-class
classref-signal
:::
::::

**visibility_changed**()
`🔗<class_Window_signal_visibility_changed>`{.interpreted-text
role="ref"}

Emitted when **Window** is made visible or disappears.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_signal_window_input}
::: rst-class
classref-signal
:::
::::

**window_input**(event: `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}) `🔗<class_Window_signal_window_input>`{.interpreted-text
role="ref"}

Emitted when the **Window** is currently focused and receives any input,
passing the received event as an argument. The event\'s position, if
present, is in the embedder\'s coordinate system.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Window_Mode}
::: rst-class
classref-enumeration
:::
::::

enum **Mode**: `🔗<enum_Window_Mode>`{.interpreted-text role="ref"}

:::: {#class_Window_constant_MODE_WINDOWED}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Window_Mode>`{.interpreted-text role="ref"} **MODE_WINDOWED**
= `0`

Windowed mode, i.e. **Window** doesn\'t occupy the whole screen (unless
set to the size of the screen).

:::: {#class_Window_constant_MODE_MINIMIZED}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Window_Mode>`{.interpreted-text role="ref"}
**MODE_MINIMIZED** = `1`

Minimized window mode, i.e. **Window** is not visible and available on
window manager\'s window list. Normally happens when the minimize button
is pressed.

:::: {#class_Window_constant_MODE_MAXIMIZED}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Window_Mode>`{.interpreted-text role="ref"}
**MODE_MAXIMIZED** = `2`

Maximized window mode, i.e. **Window** will occupy whole screen area
except task bar and still display its borders. Normally happens when the
maximize button is pressed.

:::: {#class_Window_constant_MODE_FULLSCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Window_Mode>`{.interpreted-text role="ref"}
**MODE_FULLSCREEN** = `3`

Full screen mode with full multi-window support.

Full screen window covers the entire display area of a screen and has no
decorations. The display\'s video mode is not changed.

\*\*On Android:\*\* This enables immersive mode.

\*\*On macOS:\*\* A new desktop is used to display the running project.

\*\*Note:\*\* Regardless of the platform, enabling full screen will
change the window size to match the monitor\'s size. Therefore, make
sure your project supports
`multiple resolutions <../tutorials/rendering/multiple_resolutions>`{.interpreted-text
role="doc"} when enabling full screen mode.

:::: {#class_Window_constant_MODE_EXCLUSIVE_FULLSCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Mode<enum_Window_Mode>`{.interpreted-text role="ref"}
**MODE_EXCLUSIVE_FULLSCREEN** = `4`

A single window full screen mode. This mode has less overhead, but only
one window can be open on a given screen at a time (opening a child
window or application switching will trigger a full screen transition).

Full screen window covers the entire display area of a screen and has no
border or decorations. The display\'s video mode is not changed.

\*\*Note:\*\* This mode might not work with screen recording software.

\*\*On Android:\*\* This enables immersive mode.

\*\*On Windows:\*\* Depending on video driver, full screen transition
might cause screens to go black for a moment.

\*\*On macOS:\*\* A new desktop is used to display the running project.
Exclusive full screen mode prevents Dock and Menu from showing up when
the mouse pointer is hovering the edge of the screen.

\*\*On Linux (X11):\*\* Exclusive full screen mode bypasses compositor.

\*\*On Linux (Wayland):\*\* Equivalent to
`MODE_FULLSCREEN<class_Window_constant_MODE_FULLSCREEN>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Regardless of the platform, enabling full screen will
change the window size to match the monitor\'s size. Therefore, make
sure your project supports
`multiple resolutions <../tutorials/rendering/multiple_resolutions>`{.interpreted-text
role="doc"} when enabling full screen mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Window_Flags}
::: rst-class
classref-enumeration
:::
::::

enum **Flags**: `🔗<enum_Window_Flags>`{.interpreted-text role="ref"}

:::: {#class_Window_constant_FLAG_RESIZE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_RESIZE_DISABLED** = `0`

The window can\'t be resized by dragging its resize grip. It\'s still
possible to resize the window using
`size<class_Window_property_size>`{.interpreted-text role="ref"}. This
flag is ignored for full screen windows. Set with
`unresizable<class_Window_property_unresizable>`{.interpreted-text
role="ref"}.

:::: {#class_Window_constant_FLAG_BORDERLESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_BORDERLESS** = `1`

The window do not have native title bar and other decorations. This flag
is ignored for full-screen windows. Set with
`borderless<class_Window_property_borderless>`{.interpreted-text
role="ref"}.

:::: {#class_Window_constant_FLAG_ALWAYS_ON_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_ALWAYS_ON_TOP** = `2`

The window is floating on top of all other windows. This flag is ignored
for full-screen windows. Set with
`always_on_top<class_Window_property_always_on_top>`{.interpreted-text
role="ref"}.

:::: {#class_Window_constant_FLAG_TRANSPARENT}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_TRANSPARENT** = `3`

The window background can be transparent. Set with
`transparent<class_Window_property_transparent>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This flag has no effect if either
`ProjectSettings.display/window/per_pixel_transparency/allowed<class_ProjectSettings_property_display/window/per_pixel_transparency/allowed>`{.interpreted-text
role="ref"}, or the window\'s
`Viewport.transparent_bg<class_Viewport_property_transparent_bg>`{.interpreted-text
role="ref"} is set to `false`.

:::: {#class_Window_constant_FLAG_NO_FOCUS}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_NO_FOCUS** = `4`

The window can\'t be focused. No-focus window will ignore all input,
except mouse clicks. Set with
`unfocusable<class_Window_property_unfocusable>`{.interpreted-text
role="ref"}.

:::: {#class_Window_constant_FLAG_POPUP}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"} **FLAG_POPUP**
= `5`

Window is part of menu or
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"}
dropdown. This flag can\'t be changed when the window is visible. An
active popup window will exclusively receive all input, without stealing
focus from its parent. Popup windows are automatically closed when uses
click outside it, or when an application is switched. Popup window must
have transient parent set (see
`transient<class_Window_property_transient>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* This flag has no effect in embedded windows (unless said
window is a `Popup<class_Popup>`{.interpreted-text role="ref"}).

:::: {#class_Window_constant_FLAG_EXTEND_TO_TITLE}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_EXTEND_TO_TITLE** = `6`

Window content is expanded to the full size of the window. Unlike
borderless window, the frame is left intact and can be used to resize
the window, title bar is transparent, but have minimize/maximize/close
buttons. Set with
`extend_to_title<class_Window_property_extend_to_title>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This flag is implemented only on macOS.

\*\*Note:\*\* This flag has no effect in embedded windows.

:::: {#class_Window_constant_FLAG_MOUSE_PASSTHROUGH}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_MOUSE_PASSTHROUGH** = `7`

All mouse events are passed to the underlying window of the same
application.

\*\*Note:\*\* This flag has no effect in embedded windows.

:::: {#class_Window_constant_FLAG_SHARP_CORNERS}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_SHARP_CORNERS** = `8`

Window style is overridden, forcing sharp corners.

\*\*Note:\*\* This flag has no effect in embedded windows.

\*\*Note:\*\* This flag is implemented only on Windows (11).

:::: {#class_Window_constant_FLAG_EXCLUDE_FROM_CAPTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_EXCLUDE_FROM_CAPTURE** = `9`

Windows is excluded from screenshots taken by
`DisplayServer.screen_get_image()<class_DisplayServer_method_screen_get_image>`{.interpreted-text
role="ref"},
`DisplayServer.screen_get_image_rect()<class_DisplayServer_method_screen_get_image_rect>`{.interpreted-text
role="ref"}, and
`DisplayServer.screen_get_pixel()<class_DisplayServer_method_screen_get_pixel>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This flag is implemented on macOS and Windows.

\*\*Note:\*\* Setting this flag will prevent standard screenshot methods
from capturing a window image, but does **NOT** guarantee that other
apps won\'t be able to capture an image. It should not be used as a DRM
or security measure.

:::: {#class_Window_constant_FLAG_POPUP_WM_HINT}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_POPUP_WM_HINT** = `10`

Signals the window manager that this window is supposed to be an
implementation-defined \"popup\" (usually a floating, borderless,
untileable and immovable child window).

:::: {#class_Window_constant_FLAG_MINIMIZE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_MINIMIZE_DISABLED** = `11`

Window minimize button is disabled.

\*\*Note:\*\* This flag is implemented on macOS and Windows.

:::: {#class_Window_constant_FLAG_MAXIMIZE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"}
**FLAG_MAXIMIZE_DISABLED** = `12`

Window maximize button is disabled.

\*\*Note:\*\* This flag is implemented on macOS and Windows.

:::: {#class_Window_constant_FLAG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Flags<enum_Window_Flags>`{.interpreted-text role="ref"} **FLAG_MAX** =
`13`

Max value of the `Flags<enum_Window_Flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Window_ContentScaleMode}
::: rst-class
classref-enumeration
:::
::::

enum **ContentScaleMode**:
`🔗<enum_Window_ContentScaleMode>`{.interpreted-text role="ref"}

:::: {#class_Window_constant_CONTENT_SCALE_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleMode<enum_Window_ContentScaleMode>`{.interpreted-text
role="ref"} **CONTENT_SCALE_MODE_DISABLED** = `0`

The content will not be scaled to match the **Window**\'s size.

:::: {#class_Window_constant_CONTENT_SCALE_MODE_CANVAS_ITEMS}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleMode<enum_Window_ContentScaleMode>`{.interpreted-text
role="ref"} **CONTENT_SCALE_MODE_CANVAS_ITEMS** = `1`

The content will be rendered at the target size. This is more
performance-expensive than
`CONTENT_SCALE_MODE_VIEWPORT<class_Window_constant_CONTENT_SCALE_MODE_VIEWPORT>`{.interpreted-text
role="ref"}, but provides better results.

:::: {#class_Window_constant_CONTENT_SCALE_MODE_VIEWPORT}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleMode<enum_Window_ContentScaleMode>`{.interpreted-text
role="ref"} **CONTENT_SCALE_MODE_VIEWPORT** = `2`

The content will be rendered at the base size and then scaled to the
target size. More performant than
`CONTENT_SCALE_MODE_CANVAS_ITEMS<class_Window_constant_CONTENT_SCALE_MODE_CANVAS_ITEMS>`{.interpreted-text
role="ref"}, but results in pixelated image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Window_ContentScaleAspect}
::: rst-class
classref-enumeration
:::
::::

enum **ContentScaleAspect**:
`🔗<enum_Window_ContentScaleAspect>`{.interpreted-text role="ref"}

:::: {#class_Window_constant_CONTENT_SCALE_ASPECT_IGNORE}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleAspect<enum_Window_ContentScaleAspect>`{.interpreted-text
role="ref"} **CONTENT_SCALE_ASPECT_IGNORE** = `0`

The aspect will be ignored. Scaling will simply stretch the content to
fit the target size.

:::: {#class_Window_constant_CONTENT_SCALE_ASPECT_KEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleAspect<enum_Window_ContentScaleAspect>`{.interpreted-text
role="ref"} **CONTENT_SCALE_ASPECT_KEEP** = `1`

The content\'s aspect will be preserved. If the target size has
different aspect from the base one, the image will be centered and black
bars will appear on left and right sides.

:::: {#class_Window_constant_CONTENT_SCALE_ASPECT_KEEP_WIDTH}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleAspect<enum_Window_ContentScaleAspect>`{.interpreted-text
role="ref"} **CONTENT_SCALE_ASPECT_KEEP_WIDTH** = `2`

The content can be expanded vertically. Scaling horizontally will result
in keeping the width ratio and then black bars on left and right sides.

:::: {#class_Window_constant_CONTENT_SCALE_ASPECT_KEEP_HEIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleAspect<enum_Window_ContentScaleAspect>`{.interpreted-text
role="ref"} **CONTENT_SCALE_ASPECT_KEEP_HEIGHT** = `3`

The content can be expanded horizontally. Scaling vertically will result
in keeping the height ratio and then black bars on top and bottom sides.

:::: {#class_Window_constant_CONTENT_SCALE_ASPECT_EXPAND}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleAspect<enum_Window_ContentScaleAspect>`{.interpreted-text
role="ref"} **CONTENT_SCALE_ASPECT_EXPAND** = `4`

The content\'s aspect will be preserved. If the target size has
different aspect from the base one, the content will stay in the
top-left corner and add an extra visible area in the stretched space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Window_ContentScaleStretch}
::: rst-class
classref-enumeration
:::
::::

enum **ContentScaleStretch**:
`🔗<enum_Window_ContentScaleStretch>`{.interpreted-text role="ref"}

:::: {#class_Window_constant_CONTENT_SCALE_STRETCH_FRACTIONAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleStretch<enum_Window_ContentScaleStretch>`{.interpreted-text
role="ref"} **CONTENT_SCALE_STRETCH_FRACTIONAL** = `0`

The content will be stretched according to a fractional factor. This
fills all the space available in the window, but allows \"pixel wobble\"
to occur due to uneven pixel scaling.

:::: {#class_Window_constant_CONTENT_SCALE_STRETCH_INTEGER}
::: rst-class
classref-enumeration-constant
:::
::::

`ContentScaleStretch<enum_Window_ContentScaleStretch>`{.interpreted-text
role="ref"} **CONTENT_SCALE_STRETCH_INTEGER** = `1`

The content will be stretched only according to an integer factor,
preserving sharp pixels. This may leave a black background visible on
the window\'s edges depending on the window size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Window_LayoutDirection}
::: rst-class
classref-enumeration
:::
::::

enum **LayoutDirection**:
`🔗<enum_Window_LayoutDirection>`{.interpreted-text role="ref"}

:::: {#class_Window_constant_LAYOUT_DIRECTION_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_INHERITED** = `0`

Automatic layout direction, determined from the parent window layout
direction.

:::: {#class_Window_constant_LAYOUT_DIRECTION_APPLICATION_LOCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_APPLICATION_LOCALE** = `1`

Automatic layout direction, determined from the current locale.

:::: {#class_Window_constant_LAYOUT_DIRECTION_LTR}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_LTR** = `2`

Left-to-right layout direction.

:::: {#class_Window_constant_LAYOUT_DIRECTION_RTL}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_RTL** = `3`

Right-to-left layout direction.

:::: {#class_Window_constant_LAYOUT_DIRECTION_SYSTEM_LOCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_SYSTEM_LOCALE** = `4`

Automatic layout direction, determined from the system locale.

:::: {#class_Window_constant_LAYOUT_DIRECTION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_MAX** = `5`

Represents the size of the
`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"} enum.

:::: {#class_Window_constant_LAYOUT_DIRECTION_LOCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_LOCALE** = `1`

**Deprecated:** Use
`LAYOUT_DIRECTION_APPLICATION_LOCALE<class_Window_constant_LAYOUT_DIRECTION_APPLICATION_LOCALE>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Window_WindowInitialPosition}
::: rst-class
classref-enumeration
:::
::::

enum **WindowInitialPosition**:
`🔗<enum_Window_WindowInitialPosition>`{.interpreted-text role="ref"}

:::: {#class_Window_constant_WINDOW_INITIAL_POSITION_ABSOLUTE}
::: rst-class
classref-enumeration-constant
:::
::::

`WindowInitialPosition<enum_Window_WindowInitialPosition>`{.interpreted-text
role="ref"} **WINDOW_INITIAL_POSITION_ABSOLUTE** = `0`

Initial window position is determined by
`position<class_Window_property_position>`{.interpreted-text
role="ref"}.

:::: {#class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_PRIMARY_SCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`WindowInitialPosition<enum_Window_WindowInitialPosition>`{.interpreted-text
role="ref"} **WINDOW_INITIAL_POSITION_CENTER_PRIMARY_SCREEN** = `1`

Initial window position is the center of the primary screen.

:::: {#class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_MAIN_WINDOW_SCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`WindowInitialPosition<enum_Window_WindowInitialPosition>`{.interpreted-text
role="ref"} **WINDOW_INITIAL_POSITION_CENTER_MAIN_WINDOW_SCREEN** = `2`

Initial window position is the center of the main window screen.

:::: {#class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_OTHER_SCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`WindowInitialPosition<enum_Window_WindowInitialPosition>`{.interpreted-text
role="ref"} **WINDOW_INITIAL_POSITION_CENTER_OTHER_SCREEN** = `3`

Initial window position is the center of
`current_screen<class_Window_property_current_screen>`{.interpreted-text
role="ref"} screen.

:::: {#class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_MOUSE_FOCUS}
::: rst-class
classref-enumeration-constant
:::
::::

`WindowInitialPosition<enum_Window_WindowInitialPosition>`{.interpreted-text
role="ref"} **WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_MOUSE_FOCUS** =
`4`

Initial window position is the center of the screen containing the mouse
pointer.

:::: {#class_Window_constant_WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_KEYBOARD_FOCUS}
::: rst-class
classref-enumeration-constant
:::
::::

`WindowInitialPosition<enum_Window_WindowInitialPosition>`{.interpreted-text
role="ref"}
**WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_KEYBOARD_FOCUS** = `5`

Initial window position is the center of the screen containing the
window with the keyboard focus.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Window_constant_NOTIFICATION_VISIBILITY_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_VISIBILITY_CHANGED** = `30`
`🔗<class_Window_constant_NOTIFICATION_VISIBILITY_CHANGED>`{.interpreted-text
role="ref"}

Emitted when **Window**\'s visibility changes, right before
`visibility_changed<class_Window_signal_visibility_changed>`{.interpreted-text
role="ref"}.

:::: {#class_Window_constant_NOTIFICATION_THEME_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_THEME_CHANGED** = `32`
`🔗<class_Window_constant_NOTIFICATION_THEME_CHANGED>`{.interpreted-text
role="ref"}

Sent when the node needs to refresh its theme items. This happens in one
of the following cases:

- The `theme<class_Window_property_theme>`{.interpreted-text role="ref"}
  property is changed on this node or any of its ancestors.
- The
  `theme_type_variation<class_Window_property_theme_type_variation>`{.interpreted-text
  role="ref"} property is changed on this node.
- The node enters the scene tree.

\*\*Note:\*\* As an optimization, this notification won\'t be sent from
changes that occur while this node is outside of the scene tree.
Instead, all of the theme item updates can be applied at once when the
node enters the scene tree.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Window_property_accessibility_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**accessibility_description** = `""`
`🔗<class_Window_property_accessibility_description>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessibility_description**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_accessibility_description**()

The human-readable node description that is reported to assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_accessibility_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**accessibility_name** = `""`
`🔗<class_Window_property_accessibility_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessibility_name**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_accessibility_name**()

The human-readable node name that is reported to assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_always_on_top}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **always_on_top** =
`false` `🔗<class_Window_property_always_on_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the window will be on top of all other windows. Does not work
if `transient<class_Window_property_transient>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_auto_translate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **auto_translate**
`🔗<class_Window_property_auto_translate>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_translate**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_auto_translating**()

**Deprecated:** Use
`Node.auto_translate_mode<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"} and
`Node.can_auto_translate()<class_Node_method_can_auto_translate>`{.interpreted-text
role="ref"} instead.

Toggles if any text should automatically change to its translated
version depending on the current locale.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_borderless}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **borderless** =
`false` `🔗<class_Window_property_borderless>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the window will have no borders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_content_scale_aspect}
::: rst-class
classref-property
:::
::::

`ContentScaleAspect<enum_Window_ContentScaleAspect>`{.interpreted-text
role="ref"} **content_scale_aspect** = `0`
`🔗<class_Window_property_content_scale_aspect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_content_scale_aspect**(value:
  `ContentScaleAspect<enum_Window_ContentScaleAspect>`{.interpreted-text
  role="ref"})
- `ContentScaleAspect<enum_Window_ContentScaleAspect>`{.interpreted-text
  role="ref"} **get_content_scale_aspect**()

Specifies how the content\'s aspect behaves when the **Window** is
resized. The base aspect is determined by
`content_scale_size<class_Window_property_content_scale_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_content_scale_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**content_scale_factor** = `1.0`
`🔗<class_Window_property_content_scale_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_content_scale_factor**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_content_scale_factor**()

Specifies the base scale of **Window**\'s content when its
`size<class_Window_property_size>`{.interpreted-text role="ref"} is
equal to
`content_scale_size<class_Window_property_content_scale_size>`{.interpreted-text
role="ref"}. See also
`Viewport.get_stretch_transform()<class_Viewport_method_get_stretch_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_content_scale_mode}
::: rst-class
classref-property
:::
::::

`ContentScaleMode<enum_Window_ContentScaleMode>`{.interpreted-text
role="ref"} **content_scale_mode** = `0`
`🔗<class_Window_property_content_scale_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_content_scale_mode**(value:
  `ContentScaleMode<enum_Window_ContentScaleMode>`{.interpreted-text
  role="ref"})
- `ContentScaleMode<enum_Window_ContentScaleMode>`{.interpreted-text
  role="ref"} **get_content_scale_mode**()

Specifies how the content is scaled when the **Window** is resized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_content_scale_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**content_scale_size** = `Vector2i(0, 0)`
`🔗<class_Window_property_content_scale_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_content_scale_size**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_content_scale_size**()

Base size of the content (i.e. nodes that are drawn inside the window).
If non-zero, **Window**\'s content will be scaled when the window is
resized to a different size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_content_scale_stretch}
::: rst-class
classref-property
:::
::::

`ContentScaleStretch<enum_Window_ContentScaleStretch>`{.interpreted-text
role="ref"} **content_scale_stretch** = `0`
`🔗<class_Window_property_content_scale_stretch>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_content_scale_stretch**(value:
  `ContentScaleStretch<enum_Window_ContentScaleStretch>`{.interpreted-text
  role="ref"})
- `ContentScaleStretch<enum_Window_ContentScaleStretch>`{.interpreted-text
  role="ref"} **get_content_scale_stretch**()

The policy to use to determine the final scale factor for 2D elements.
This affects how
`content_scale_factor<class_Window_property_content_scale_factor>`{.interpreted-text
role="ref"} is applied, in addition to the automatic scale factor
determined by
`content_scale_size<class_Window_property_content_scale_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_current_screen}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **current_screen**
`🔗<class_Window_property_current_screen>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_screen**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_current_screen**()

The screen the window is currently on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_exclude_from_capture}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**exclude_from_capture** = `false`
`🔗<class_Window_property_exclude_from_capture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the **Window** is excluded from screenshots taken by
`DisplayServer.screen_get_image()<class_DisplayServer_method_screen_get_image>`{.interpreted-text
role="ref"},
`DisplayServer.screen_get_image_rect()<class_DisplayServer_method_screen_get_image_rect>`{.interpreted-text
role="ref"}, and
`DisplayServer.screen_get_pixel()<class_DisplayServer_method_screen_get_pixel>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is implemented on macOS and Windows.

\*\*Note:\*\* Enabling this setting will prevent standard screenshot
methods from capturing a window image, but does **NOT** guarantee that
other apps won\'t be able to capture an image. It should not be used as
a DRM or security measure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_exclusive}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **exclusive** = `false`
`🔗<class_Window_property_exclusive>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exclusive**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_exclusive**()

If `true`, the **Window** will be in exclusive mode. Exclusive windows
are always on top of their parent and will block all input going to the
parent **Window**.

Needs `transient<class_Window_property_transient>`{.interpreted-text
role="ref"} enabled to work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_extend_to_title}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **extend_to_title** =
`false` `🔗<class_Window_property_extend_to_title>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the **Window** contents is expanded to the full size of the
window, window title bar is transparent.

\*\*Note:\*\* This property is implemented only on macOS.

\*\*Note:\*\* This property only works with native windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_force_native}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **force_native** =
`false` `🔗<class_Window_property_force_native>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_force_native**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_force_native**()

If `true`, native window will be used regardless of parent viewport and
project settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_initial_position}
::: rst-class
classref-property
:::
::::

`WindowInitialPosition<enum_Window_WindowInitialPosition>`{.interpreted-text
role="ref"} **initial_position** = `0`
`🔗<class_Window_property_initial_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_initial_position**(value:
  `WindowInitialPosition<enum_Window_WindowInitialPosition>`{.interpreted-text
  role="ref"})
- `WindowInitialPosition<enum_Window_WindowInitialPosition>`{.interpreted-text
  role="ref"} **get_initial_position**()

Specifies the initial type of position for the **Window**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_keep_title_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **keep_title_visible**
= `false`
`🔗<class_Window_property_keep_title_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keep_title_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_keep_title_visible**()

If `true`, the **Window** width is expanded to keep the title bar text
fully visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_max_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **max_size** =
`Vector2i(0, 0)` `🔗<class_Window_property_max_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_size**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_max_size**()

If non-zero, the **Window** can\'t be resized to be bigger than this
size.

\*\*Note:\*\* This property will be ignored if the value is lower than
`min_size<class_Window_property_min_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_maximize_disabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **maximize_disabled** =
`false` `🔗<class_Window_property_maximize_disabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the **Window**\'s maximize button is disabled.

\*\*Note:\*\* If both minimize and maximize buttons are disabled,
buttons are fully hidden, and only close button is visible.

\*\*Note:\*\* This property is implemented only on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_min_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **min_size** =
`Vector2i(0, 0)` `🔗<class_Window_property_min_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_size**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_min_size**()

If non-zero, the **Window** can\'t be resized to be smaller than this
size.

\*\*Note:\*\* This property will be ignored in favor of
`get_contents_minimum_size()<class_Window_method_get_contents_minimum_size>`{.interpreted-text
role="ref"} if
`wrap_controls<class_Window_property_wrap_controls>`{.interpreted-text
role="ref"} is enabled and if its size is bigger.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_minimize_disabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **minimize_disabled** =
`false` `🔗<class_Window_property_minimize_disabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the **Window**\'s minimize button is disabled.

\*\*Note:\*\* If both minimize and maximize buttons are disabled,
buttons are fully hidden, and only close button is visible.

\*\*Note:\*\* This property is implemented only on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_mode}
::: rst-class
classref-property
:::
::::

`Mode<enum_Window_Mode>`{.interpreted-text role="ref"} **mode** = `0`
`🔗<class_Window_property_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mode**(value: `Mode<enum_Window_Mode>`{.interpreted-text
  role="ref"})
- `Mode<enum_Window_Mode>`{.interpreted-text role="ref"} **get_mode**()

Set\'s the window\'s current mode.

\*\*Note:\*\* Fullscreen mode is not exclusive full screen on Windows
and Linux.

\*\*Note:\*\* This method only works with native windows, i.e. the main
window and **Window**-derived nodes when
`Viewport.gui_embed_subwindows<class_Viewport_property_gui_embed_subwindows>`{.interpreted-text
role="ref"} is disabled in the main viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_mouse_passthrough}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **mouse_passthrough** =
`false` `🔗<class_Window_property_mouse_passthrough>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, all mouse events will be passed to the underlying window of
the same application. See also
`mouse_passthrough_polygon<class_Window_property_mouse_passthrough_polygon>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is implemented on Linux (X11), macOS and
Windows.

\*\*Note:\*\* This property only works with native windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_mouse_passthrough_polygon}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **mouse_passthrough_polygon** = `PackedVector2Array()`
`🔗<class_Window_property_mouse_passthrough_polygon>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mouse_passthrough_polygon**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_mouse_passthrough_polygon**()

Sets a polygonal region of the window which accepts mouse events. Mouse
events outside the region will be passed through.

Passing an empty array will disable passthrough support (all mouse
events will be intercepted by the window, which is the default
behavior).

::::: tabs
::: code-tab
gdscript

\# Set region, using Path2D node. \$Window.mouse_passthrough_polygon =
\$Path2D.curve.get_baked_points()

\# Set region, using Polygon2D node. \$Window.mouse_passthrough_polygon
= \$Polygon2D.polygon

\# Reset region to default. \$Window.mouse_passthrough_polygon = \[\]
:::

::: code-tab
csharp

// Set region, using Path2D node.
GetNode\<Window\>(\"Window\").MousePassthroughPolygon =
GetNode\<Path2D\>(\"Path2D\").Curve.GetBakedPoints();

// Set region, using Polygon2D node.
GetNode\<Window\>(\"Window\").MousePassthroughPolygon =
GetNode\<Polygon2D\>(\"Polygon2D\").Polygon;

// Reset region to default.
GetNode\<Window\>(\"Window\").MousePassthroughPolygon = \[\];
:::
:::::

\*\*Note:\*\* This property is ignored if
`mouse_passthrough<class_Window_property_mouse_passthrough>`{.interpreted-text
role="ref"} is set to `true`.

\*\*Note:\*\* On Windows, the portion of a window that lies outside the
region is not drawn, while on Linux (X11) and macOS it is.

\*\*Note:\*\* This property is implemented on Linux (X11), macOS and
Windows.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_popup_window}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **popup_window** =
`false` `🔗<class_Window_property_popup_window>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the **Window** will be considered a popup. Popups are
sub-windows that don\'t show as separate windows in system\'s window
manager\'s window list and will send close request when anything is
clicked outside of them (unless
`exclusive<class_Window_property_exclusive>`{.interpreted-text
role="ref"} is enabled).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_popup_wm_hint}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **popup_wm_hint** =
`false` `🔗<class_Window_property_popup_wm_hint>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the **Window** will signal to the window manager that it is
supposed to be an implementation-defined \"popup\" (usually a floating,
borderless, untileable and immovable child window).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_position}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **position** =
`Vector2i(0, 0)` `🔗<class_Window_property_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_position**()

The window\'s position in pixels.

If
`ProjectSettings.display/window/subwindows/embed_subwindows<class_ProjectSettings_property_display/window/subwindows/embed_subwindows>`{.interpreted-text
role="ref"} is `false`, the position is in absolute screen coordinates.
This typically applies to editor plugins. If the setting is `true`, the
window\'s position is in the coordinates of its parent
`Viewport<class_Viewport>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This property only works if
`initial_position<class_Window_property_initial_position>`{.interpreted-text
role="ref"} is set to
`WINDOW_INITIAL_POSITION_ABSOLUTE<class_Window_constant_WINDOW_INITIAL_POSITION_ABSOLUTE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_sharp_corners}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sharp_corners** =
`false` `🔗<class_Window_property_sharp_corners>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the **Window** will override the OS window style to display
sharp corners.

\*\*Note:\*\* This property is implemented only on Windows (11).

\*\*Note:\*\* This property only works with native windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **size** =
`Vector2i(100, 100)` `🔗<class_Window_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_size**()

The window\'s size in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_theme}
::: rst-class
classref-property
:::
::::

`Theme<class_Theme>`{.interpreted-text role="ref"} **theme**
`🔗<class_Window_property_theme>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_theme**(value: `Theme<class_Theme>`{.interpreted-text
  role="ref"})
- `Theme<class_Theme>`{.interpreted-text role="ref"} **get_theme**()

The `Theme<class_Theme>`{.interpreted-text role="ref"} resource this
node and all its `Control<class_Control>`{.interpreted-text role="ref"}
and **Window** children use. If a child node has its own
`Theme<class_Theme>`{.interpreted-text role="ref"} resource set, theme
items are merged with child\'s definitions having higher priority.

\*\*Note:\*\* **Window** styles will have no effect unless the window is
embedded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_theme_type_variation}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**theme_type_variation** = `&""`
`🔗<class_Window_property_theme_type_variation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_theme_type_variation**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_theme_type_variation**()

The name of a theme type variation used by this **Window** to look up
its own theme items. See
`Control.theme_type_variation<class_Control_property_theme_type_variation>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_title}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **title** = `""`
`🔗<class_Window_property_title>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_title**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_title**()

The window\'s title. If the **Window** is native, title styles set in
`Theme<class_Theme>`{.interpreted-text role="ref"} will have no effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_transient}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **transient** = `false`
`🔗<class_Window_property_transient>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transient**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_transient**()

If `true`, the **Window** is transient, i.e. it\'s considered a child of
another **Window**. The transient window will be destroyed with its
transient parent and will return focus to their parent when closed. The
transient window is displayed on top of a non-exclusive full-screen
parent window. Transient windows can\'t enter full-screen mode.

Note that behavior might be different depending on the platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_transient_to_focused}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**transient_to_focused** = `false`
`🔗<class_Window_property_transient_to_focused>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transient_to_focused**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_transient_to_focused**()

If `true`, and the **Window** is
`transient<class_Window_property_transient>`{.interpreted-text
role="ref"}, this window will (at the time of becoming visible) become
transient to the currently focused window instead of the immediate
parent window in the hierarchy. Note that the transient parent is
assigned at the time this window becomes visible, so changing it
afterwards has no effect until re-shown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_transparent}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **transparent** =
`false` `🔗<class_Window_property_transparent>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the **Window**\'s background can be transparent. This is best
used with embedded windows.

\*\*Note:\*\* Transparency support is implemented on Linux, macOS and
Windows, but availability might vary depending on GPU driver, display
manager, and compositor capabilities.

\*\*Note:\*\* This property has no effect if
`ProjectSettings.display/window/per_pixel_transparency/allowed<class_ProjectSettings_property_display/window/per_pixel_transparency/allowed>`{.interpreted-text
role="ref"} is set to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_unfocusable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **unfocusable** =
`false` `🔗<class_Window_property_unfocusable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the **Window** can\'t be focused nor interacted with. It can
still be visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_unresizable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **unresizable** =
`false` `🔗<class_Window_property_unresizable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
  `Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, the window can\'t be resized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **visible** = `true`
`🔗<class_Window_property_visible>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_visible**()

If `true`, the window is visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_property_wrap_controls}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **wrap_controls** =
`false` `🔗<class_Window_property_wrap_controls>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wrap_controls**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_wrapping_controls**()

If `true`, the window\'s size will automatically update when a child
node is added or removed, ignoring
`min_size<class_Window_property_min_size>`{.interpreted-text role="ref"}
if the new size is bigger.

If `false`, you need to call
`child_controls_changed()<class_Window_method_child_controls_changed>`{.interpreted-text
role="ref"} manually.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Window_private_method__get_contents_minimum_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_contents_minimum_size**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_private_method__get_contents_minimum_size>`{.interpreted-text
role="ref"}

Virtual method to be implemented by the user. Overrides the value
returned by
`get_contents_minimum_size()<class_Window_method_get_contents_minimum_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_add_theme_color_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_color_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Window_method_add_theme_color_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme
`Color<class_Color>`{.interpreted-text role="ref"} with the specified
`name`. Local overrides always take precedence when fetching theme items
for the control. An override can be removed with
`remove_theme_color_override()<class_Window_method_remove_theme_color_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_color()<class_Window_method_get_theme_color>`{.interpreted-text
role="ref"} and
`Control.add_theme_color_override()<class_Control_method_add_theme_color_override>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_add_theme_constant_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_constant_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, constant:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Window_method_add_theme_constant_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme constant with the specified `name`.
Local overrides always take precedence when fetching theme items for the
control. An override can be removed with
`remove_theme_constant_override()<class_Window_method_remove_theme_constant_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_constant()<class_Window_method_get_theme_constant>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_add_theme_font_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_font_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, font:
`Font<class_Font>`{.interpreted-text role="ref"})
`🔗<class_Window_method_add_theme_font_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme
`Font<class_Font>`{.interpreted-text role="ref"} with the specified
`name`. Local overrides always take precedence when fetching theme items
for the control. An override can be removed with
`remove_theme_font_override()<class_Window_method_remove_theme_font_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_font()<class_Window_method_get_theme_font>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_add_theme_font_size_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_font_size_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, font_size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Window_method_add_theme_font_size_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme font size with the specified
`name`. Local overrides always take precedence when fetching theme items
for the control. An override can be removed with
`remove_theme_font_size_override()<class_Window_method_remove_theme_font_size_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_font_size()<class_Window_method_get_theme_font_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_add_theme_icon_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_icon_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_Window_method_add_theme_icon_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme icon with the specified `name`.
Local overrides always take precedence when fetching theme items for the
control. An override can be removed with
`remove_theme_icon_override()<class_Window_method_remove_theme_icon_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_icon()<class_Window_method_get_theme_icon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_add_theme_stylebox_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_stylebox_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, stylebox:
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"})
`🔗<class_Window_method_add_theme_stylebox_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} with the
specified `name`. Local overrides always take precedence when fetching
theme items for the control. An override can be removed with
`remove_theme_stylebox_override()<class_Window_method_remove_theme_stylebox_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_stylebox()<class_Window_method_get_theme_stylebox>`{.interpreted-text
role="ref"} and
`Control.add_theme_stylebox_override()<class_Control_method_add_theme_stylebox_override>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_begin_bulk_theme_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**begin_bulk_theme_override**()
`🔗<class_Window_method_begin_bulk_theme_override>`{.interpreted-text
role="ref"}

Prevents `*_theme_*_override` methods from emitting
`NOTIFICATION_THEME_CHANGED<class_Window_constant_NOTIFICATION_THEME_CHANGED>`{.interpreted-text
role="ref"} until
`end_bulk_theme_override()<class_Window_method_end_bulk_theme_override>`{.interpreted-text
role="ref"} is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_can_draw}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_draw**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_can_draw>`{.interpreted-text
role="ref"}

Returns whether the window is being drawn to the screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_child_controls_changed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**child_controls_changed**()
`🔗<class_Window_method_child_controls_changed>`{.interpreted-text
role="ref"}

Requests an update of the **Window** size to fit underlying
`Control<class_Control>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_end_bulk_theme_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**end_bulk_theme_override**()
`🔗<class_Window_method_end_bulk_theme_override>`{.interpreted-text
role="ref"}

Ends a bulk theme override update. See
`begin_bulk_theme_override()<class_Window_method_begin_bulk_theme_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_contents_minimum_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_contents_minimum_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_contents_minimum_size>`{.interpreted-text
role="ref"}

Returns the combined minimum size from the child
`Control<class_Control>`{.interpreted-text role="ref"} nodes of the
window. Use
`child_controls_changed()<class_Window_method_child_controls_changed>`{.interpreted-text
role="ref"} to update it when child nodes have changed.

The value returned by this method can be overridden with
`_get_contents_minimum_size()<class_Window_private_method__get_contents_minimum_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_flag**(flag:
`Flags<enum_Window_Flags>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_get_flag>`{.interpreted-text
role="ref"}

Returns `true` if the `flag` is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_focused_window}
::: rst-class
classref-method
:::
::::

`Window<class_Window>`{.interpreted-text role="ref"}
**get_focused_window**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_focused_window>`{.interpreted-text
role="ref"}

Returns the focused window.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_layout_direction}
::: rst-class
classref-method
:::
::::

`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"} **get_layout_direction**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_layout_direction>`{.interpreted-text
role="ref"}

Returns layout direction and text writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_position_with_decorations}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_position_with_decorations**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_position_with_decorations>`{.interpreted-text
role="ref"}

Returns the window\'s position including its border.

\*\*Note:\*\* If
`visible<class_Window_property_visible>`{.interpreted-text role="ref"}
is `false`, this method returns the same value as
`position<class_Window_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_size_with_decorations}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_size_with_decorations**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_size_with_decorations>`{.interpreted-text
role="ref"}

Returns the window\'s size including its border.

\*\*Note:\*\* If
`visible<class_Window_property_visible>`{.interpreted-text role="ref"}
is `false`, this method returns the same value as
`size<class_Window_property_size>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_theme_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_theme_color**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_get_theme_color>`{.interpreted-text
role="ref"}

Returns a `Color<class_Color>`{.interpreted-text role="ref"} from the
first matching `Theme<class_Theme>`{.interpreted-text role="ref"} in the
tree if that `Theme<class_Theme>`{.interpreted-text role="ref"} has a
color item with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_theme_constant}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_theme_constant**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_theme_constant>`{.interpreted-text
role="ref"}

Returns a constant from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a constant item
with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_theme_default_base_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_theme_default_base_scale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_theme_default_base_scale>`{.interpreted-text
role="ref"}

Returns the default base scale value from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a valid
`Theme.default_base_scale<class_Theme_property_default_base_scale>`{.interpreted-text
role="ref"} value.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_theme_default_font}
::: rst-class
classref-method
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"}
**get_theme_default_font**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_theme_default_font>`{.interpreted-text
role="ref"}

Returns the default font from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a valid
`Theme.default_font<class_Theme_property_default_font>`{.interpreted-text
role="ref"} value.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_theme_default_font_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_theme_default_font_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_theme_default_font_size>`{.interpreted-text
role="ref"}

Returns the default font size value from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a valid
`Theme.default_font_size<class_Theme_property_default_font_size>`{.interpreted-text
role="ref"} value.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_theme_font}
::: rst-class
classref-method
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"}
**get_theme_font**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_get_theme_font>`{.interpreted-text
role="ref"}

Returns a `Font<class_Font>`{.interpreted-text role="ref"} from the
first matching `Theme<class_Theme>`{.interpreted-text role="ref"} in the
tree if that `Theme<class_Theme>`{.interpreted-text role="ref"} has a
font item with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_theme_font_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_theme_font_size**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_theme_font_size>`{.interpreted-text
role="ref"}

Returns a font size from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a font size item
with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_theme_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_theme_icon**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_get_theme_icon>`{.interpreted-text
role="ref"}

Returns an icon from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has an icon item with
the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_theme_stylebox}
::: rst-class
classref-method
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**get_theme_stylebox**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_get_theme_stylebox>`{.interpreted-text
role="ref"}

Returns a `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} from
the first matching `Theme<class_Theme>`{.interpreted-text role="ref"} in
the tree if that `Theme<class_Theme>`{.interpreted-text role="ref"} has
a stylebox item with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_get_window_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_window_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_get_window_id>`{.interpreted-text
role="ref"}

Returns the ID of the window.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_grab_focus}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**grab_focus**() `🔗<class_Window_method_grab_focus>`{.interpreted-text
role="ref"}

Causes the window to grab focus, allowing it to receive user input.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_focus}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_focus**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_has_focus>`{.interpreted-text
role="ref"}

Returns `true` if the window is focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_color}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_color**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_has_theme_color>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a color item with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_color_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_color_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_has_theme_color_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme
`Color<class_Color>`{.interpreted-text role="ref"} with the specified
`name` in this `Control<class_Control>`{.interpreted-text role="ref"}
node.

See
`add_theme_color_override()<class_Window_method_add_theme_color_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_constant}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_constant**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_has_theme_constant>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a constant item with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_constant_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_constant_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_has_theme_constant_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme constant with
the specified `name` in this `Control<class_Control>`{.interpreted-text
role="ref"} node.

See
`add_theme_constant_override()<class_Window_method_add_theme_constant_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_font}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_font**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_has_theme_font>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a font item with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_font_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_font_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_has_theme_font_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme
`Font<class_Font>`{.interpreted-text role="ref"} with the specified
`name` in this `Control<class_Control>`{.interpreted-text role="ref"}
node.

See
`add_theme_font_override()<class_Window_method_add_theme_font_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_font_size}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_font_size**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_has_theme_font_size>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a font size item with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_font_size_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_font_size_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_has_theme_font_size_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme font size with
the specified `name` in this `Control<class_Control>`{.interpreted-text
role="ref"} node.

See
`add_theme_font_size_override()<class_Window_method_add_theme_font_size_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_icon}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_icon**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_has_theme_icon>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
an icon item with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_icon_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_icon_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_has_theme_icon_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme icon with the
specified `name` in this `Control<class_Control>`{.interpreted-text
role="ref"} node.

See
`add_theme_icon_override()<class_Window_method_add_theme_icon_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_stylebox}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_stylebox**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_has_theme_stylebox>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a stylebox item with the specified `name` and `theme_type`.

See
`Control.get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_has_theme_stylebox_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_stylebox_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_has_theme_stylebox_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} with the
specified `name` in this `Control<class_Control>`{.interpreted-text
role="ref"} node.

See
`add_theme_stylebox_override()<class_Window_method_add_theme_stylebox_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_hide}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **hide**()
`🔗<class_Window_method_hide>`{.interpreted-text role="ref"}

Hides the window. This is not the same as minimized state. Hidden window
can\'t be interacted with and needs to be made visible with
`show()<class_Window_method_show>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_is_embedded}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_embedded**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_is_embedded>`{.interpreted-text
role="ref"}

Returns `true` if the window is currently embedded in another window.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_is_layout_rtl}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_layout_rtl**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Window_method_is_layout_rtl>`{.interpreted-text
role="ref"}

Returns `true` if the layout is right-to-left.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_is_maximize_allowed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_maximize_allowed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_is_maximize_allowed>`{.interpreted-text
role="ref"}

Returns `true` if the window can be maximized (the maximize button is
enabled).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_is_using_font_oversampling}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_using_font_oversampling**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Window_method_is_using_font_oversampling>`{.interpreted-text
role="ref"}

Returns `true` if font oversampling is enabled. See
`set_use_font_oversampling()<class_Window_method_set_use_font_oversampling>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_move_to_center}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_to_center**()
`🔗<class_Window_method_move_to_center>`{.interpreted-text role="ref"}

Centers a native window on the current screen and an embedded window on
its embedder `Viewport<class_Viewport>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_move_to_foreground}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_to_foreground**()
`🔗<class_Window_method_move_to_foreground>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`grab_focus()<class_Window_method_grab_focus>`{.interpreted-text
role="ref"} instead.

Causes the window to grab focus, allowing it to receive user input.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **popup**(rect:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} = Rect2i(0, 0, 0,
0)) `🔗<class_Window_method_popup>`{.interpreted-text role="ref"}

Shows the **Window** and makes it transient (see
`transient<class_Window_property_transient>`{.interpreted-text
role="ref"}). If `rect` is provided, it will be set as the **Window**\'s
size. Fails if called on the main window.

If
`ProjectSettings.display/window/subwindows/embed_subwindows<class_ProjectSettings_property_display/window/subwindows/embed_subwindows>`{.interpreted-text
role="ref"} is `true` (single-window mode), `rect`\'s coordinates are
global and relative to the main window\'s top-left corner (excluding
window decorations). If `rect`\'s position coordinates are negative, the
window will be located outside the main window and may not be visible as
a result.

If
`ProjectSettings.display/window/subwindows/embed_subwindows<class_ProjectSettings_property_display/window/subwindows/embed_subwindows>`{.interpreted-text
role="ref"} is `false` (multi-window mode), `rect`\'s coordinates are
global and relative to the top-left corner of the leftmost screen. If
`rect`\'s position coordinates are negative, the window will be placed
at the top-left corner of the screen.

\*\*Note:\*\* `rect` must be in global coordinates if specified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup_centered}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_centered**(minsize: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"} = Vector2i(0, 0))
`🔗<class_Window_method_popup_centered>`{.interpreted-text role="ref"}

Popups the **Window** at the center of the current screen, with
optionally given minimum size. If the **Window** is embedded, it will be
centered in the parent `Viewport<class_Viewport>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* Calling it with the default value of `minsize` is
equivalent to calling it with
`size<class_Window_property_size>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup_centered_clamped}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_centered_clamped**(minsize:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} = Vector2i(0,
0), fallback_ratio: `float<class_float>`{.interpreted-text role="ref"} =
0.75) `🔗<class_Window_method_popup_centered_clamped>`{.interpreted-text
role="ref"}

Popups the **Window** centered inside its parent **Window**.
`fallback_ratio` determines the maximum size of the **Window**, in
relation to its parent.

\*\*Note:\*\* Calling it with the default value of `minsize` is
equivalent to calling it with
`size<class_Window_property_size>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup_centered_ratio}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_centered_ratio**(ratio: `float<class_float>`{.interpreted-text
role="ref"} = 0.8)
`🔗<class_Window_method_popup_centered_ratio>`{.interpreted-text
role="ref"}

If **Window** is embedded, popups the **Window** centered inside its
embedder and sets its size as a `ratio` of embedder\'s size.

If **Window** is a native window, popups the **Window** centered inside
the screen of its parent **Window** and sets its size as a `ratio` of
the screen size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup_exclusive}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_exclusive**(from_node: `Node<class_Node>`{.interpreted-text
role="ref"}, rect: `Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
= Rect2i(0, 0, 0, 0))
`🔗<class_Window_method_popup_exclusive>`{.interpreted-text role="ref"}

Attempts to parent this dialog to the last exclusive window relative to
`from_node`, and then calls
`popup()<class_Window_method_popup>`{.interpreted-text role="ref"} on
it. The dialog must have no current parent, otherwise the method fails.

See also
`set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"} and
`Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup_exclusive_centered}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_exclusive_centered**(from_node:
`Node<class_Node>`{.interpreted-text role="ref"}, minsize:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} = Vector2i(0,
0)) `🔗<class_Window_method_popup_exclusive_centered>`{.interpreted-text
role="ref"}

Attempts to parent this dialog to the last exclusive window relative to
`from_node`, and then calls
`popup_centered()<class_Window_method_popup_centered>`{.interpreted-text
role="ref"} on it. The dialog must have no current parent, otherwise the
method fails.

See also
`set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"} and
`Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup_exclusive_centered_clamped}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_exclusive_centered_clamped**(from_node:
`Node<class_Node>`{.interpreted-text role="ref"}, minsize:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} = Vector2i(0,
0), fallback_ratio: `float<class_float>`{.interpreted-text role="ref"} =
0.75)
`🔗<class_Window_method_popup_exclusive_centered_clamped>`{.interpreted-text
role="ref"}

Attempts to parent this dialog to the last exclusive window relative to
`from_node`, and then calls
`popup_centered_clamped()<class_Window_method_popup_centered_clamped>`{.interpreted-text
role="ref"} on it. The dialog must have no current parent, otherwise the
method fails.

See also
`set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"} and
`Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup_exclusive_centered_ratio}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_exclusive_centered_ratio**(from_node:
`Node<class_Node>`{.interpreted-text role="ref"}, ratio:
`float<class_float>`{.interpreted-text role="ref"} = 0.8)
`🔗<class_Window_method_popup_exclusive_centered_ratio>`{.interpreted-text
role="ref"}

Attempts to parent this dialog to the last exclusive window relative to
`from_node`, and then calls
`popup_centered_ratio()<class_Window_method_popup_centered_ratio>`{.interpreted-text
role="ref"} on it. The dialog must have no current parent, otherwise the
method fails.

See also
`set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"} and
`Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup_exclusive_on_parent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_exclusive_on_parent**(from_node:
`Node<class_Node>`{.interpreted-text role="ref"}, parent_rect:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`🔗<class_Window_method_popup_exclusive_on_parent>`{.interpreted-text
role="ref"}

Attempts to parent this dialog to the last exclusive window relative to
`from_node`, and then calls
`popup_on_parent()<class_Window_method_popup_on_parent>`{.interpreted-text
role="ref"} on it. The dialog must have no current parent, otherwise the
method fails.

See also
`set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"} and
`Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_popup_on_parent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_on_parent**(parent_rect:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`🔗<class_Window_method_popup_on_parent>`{.interpreted-text role="ref"}

Popups the **Window** with a position shifted by parent **Window**\'s
position. If the **Window** is embedded, has the same effect as
`popup()<class_Window_method_popup>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_remove_theme_color_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_color_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Window_method_remove_theme_color_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme
`Color<class_Color>`{.interpreted-text role="ref"} with the specified
`name` previously added by
`add_theme_color_override()<class_Window_method_add_theme_color_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_remove_theme_constant_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_constant_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Window_method_remove_theme_constant_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme constant with the specified `name`
previously added by
`add_theme_constant_override()<class_Window_method_add_theme_constant_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_remove_theme_font_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_font_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Window_method_remove_theme_font_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme
`Font<class_Font>`{.interpreted-text role="ref"} with the specified
`name` previously added by
`add_theme_font_override()<class_Window_method_add_theme_font_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_remove_theme_font_size_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_font_size_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Window_method_remove_theme_font_size_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme font size with the specified `name`
previously added by
`add_theme_font_size_override()<class_Window_method_add_theme_font_size_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_remove_theme_icon_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_icon_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Window_method_remove_theme_icon_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme icon with the specified `name`
previously added by
`add_theme_icon_override()<class_Window_method_add_theme_icon_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_remove_theme_stylebox_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_stylebox_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Window_method_remove_theme_stylebox_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} with the
specified `name` previously added by
`add_theme_stylebox_override()<class_Window_method_add_theme_stylebox_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_request_attention}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**request_attention**()
`🔗<class_Window_method_request_attention>`{.interpreted-text
role="ref"}

Tells the OS that the **Window** needs an attention. This makes the
window stand out in some way depending on the system, e.g. it might
blink on the task bar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_reset_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reset_size**() `🔗<class_Window_method_reset_size>`{.interpreted-text
role="ref"}

Resets the size to the minimum size, which is the max of
`min_size<class_Window_property_min_size>`{.interpreted-text role="ref"}
and (if
`wrap_controls<class_Window_property_wrap_controls>`{.interpreted-text
role="ref"} is enabled)
`get_contents_minimum_size()<class_Window_method_get_contents_minimum_size>`{.interpreted-text
role="ref"}. This is equivalent to calling `set_size(Vector2i())` (or
any size below the minimum).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_set_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_flag**(flag: `Flags<enum_Window_Flags>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Window_method_set_flag>`{.interpreted-text role="ref"}

Sets a specified window flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_set_ime_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ime_active**(active: `bool<class_bool>`{.interpreted-text
role="ref"}) `🔗<class_Window_method_set_ime_active>`{.interpreted-text
role="ref"}

If `active` is `true`, enables system\'s native IME (Input Method
Editor).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_set_ime_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ime_position**(position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_Window_method_set_ime_position>`{.interpreted-text role="ref"}

Moves IME to the given position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_set_layout_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layout_direction**(direction:
`LayoutDirection<enum_Window_LayoutDirection>`{.interpreted-text
role="ref"})
`🔗<class_Window_method_set_layout_direction>`{.interpreted-text
role="ref"}

Sets layout direction and text writing direction. Right-to-left layouts
are necessary for certain languages (e.g. Arabic and Hebrew).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_set_unparent_when_invisible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_unparent_when_invisible**(unparent:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"}

If `unparent` is `true`, the window is automatically unparented when
going invisible.

\*\*Note:\*\* Make sure to keep a reference to the node, otherwise it
will be orphaned. You also need to manually call
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"} to free the window if it\'s not parented.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_set_use_font_oversampling}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_use_font_oversampling**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Window_method_set_use_font_oversampling>`{.interpreted-text
role="ref"}

Enables font oversampling. This makes fonts look better when they are
scaled up.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_show}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **show**()
`🔗<class_Window_method_show>`{.interpreted-text role="ref"}

Makes the **Window** appear. This enables interactions with the
**Window** and doesn\'t change any of its property other than visibility
(unlike e.g. `popup()<class_Window_method_popup>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_start_drag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**start_drag**() `🔗<class_Window_method_start_drag>`{.interpreted-text
role="ref"}

Starts an interactive drag operation on the window, using the current
mouse position. Call this method when handling a mouse button being
pressed to simulate a pressed event on the window\'s title bar. Using
this method allows the window to participate in space switching, tiling,
and other system features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_method_start_resize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**start_resize**(edge:
`WindowResizeEdge<enum_DisplayServer_WindowResizeEdge>`{.interpreted-text
role="ref"}) `🔗<class_Window_method_start_resize>`{.interpreted-text
role="ref"}

Starts an interactive resize operation on the window, using the current
mouse position. Call this method when handling a mouse button being
pressed to simulate a pressed event on the window\'s edge.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_Window_theme_color_title_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **title_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_Window_theme_color_title_color>`{.interpreted-text role="ref"}

The color of the title\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_color_title_outline_modulate}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**title_outline_modulate** = `Color(0, 0, 0, 1)`
`🔗<class_Window_theme_color_title_outline_modulate>`{.interpreted-text
role="ref"}

The color of the title\'s text outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_constant_close_h_offset}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **close_h_offset** = `18`
`🔗<class_Window_theme_constant_close_h_offset>`{.interpreted-text
role="ref"}

Horizontal position offset of the close button, relative to the end of
the title bar, towards the beginning of the title bar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_constant_close_v_offset}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **close_v_offset** = `24`
`🔗<class_Window_theme_constant_close_v_offset>`{.interpreted-text
role="ref"}

Vertical position offset of the close button, relative to the bottom of
the title bar, towards the top of the title bar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_constant_resize_margin}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **resize_margin** = `4`
`🔗<class_Window_theme_constant_resize_margin>`{.interpreted-text
role="ref"}

Defines the outside margin at which the window border can be grabbed
with mouse and resized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_constant_title_height}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **title_height** = `36`
`🔗<class_Window_theme_constant_title_height>`{.interpreted-text
role="ref"}

Height of the title bar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_constant_title_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **title_outline_size** =
`0`
`🔗<class_Window_theme_constant_title_outline_size>`{.interpreted-text
role="ref"}

The size of the title outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_font_title_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **title_font**
`🔗<class_Window_theme_font_title_font>`{.interpreted-text role="ref"}

The font used to draw the title.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_font_size_title_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **title_font_size**
`🔗<class_Window_theme_font_size_title_font_size>`{.interpreted-text
role="ref"}

The size of the title font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_icon_close}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **close**
`🔗<class_Window_theme_icon_close>`{.interpreted-text role="ref"}

The icon for the close button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_icon_close_pressed}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**close_pressed**
`🔗<class_Window_theme_icon_close_pressed>`{.interpreted-text
role="ref"}

The icon for the close button when it\'s being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_style_embedded_border}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**embedded_border**
`🔗<class_Window_theme_style_embedded_border>`{.interpreted-text
role="ref"}

The background style used when the **Window** is embedded. Note that
this is drawn only under the window\'s content, excluding the title. For
proper borders and title bar style, you can use `expand_margin_*`
properties of `StyleBoxFlat<class_StyleBoxFlat>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The content background will not be visible unless
`transparent<class_Window_property_transparent>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Window_theme_style_embedded_unfocused_border}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**embedded_unfocused_border**
`🔗<class_Window_theme_style_embedded_unfocused_border>`{.interpreted-text
role="ref"}

The background style used when the **Window** is embedded and unfocused.
