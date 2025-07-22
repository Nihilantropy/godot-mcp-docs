github_url
:   hide

# MainLoop {#class_MainLoop}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"}

Abstract base class for the game\'s main loop.

::: rst-class
classref-introduction-group
:::

## Description

**MainLoop** is the abstract base class for a Godot project\'s game
loop. It is inherited by `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"}, which is the default game loop implementation used in Godot
projects, though it is also possible to write and use one\'s own
**MainLoop** subclass instead of the scene tree.

Upon the application start, a **MainLoop** implementation must be
provided to the OS; otherwise, the application will exit. This happens
automatically (and a `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"} is created) unless a **MainLoop**
`Script<class_Script>`{.interpreted-text role="ref"} is provided from
the command line (with e.g. `godot -s my_loop.gd`) or the
`ProjectSettings.application/run/main_loop_type<class_ProjectSettings_property_application/run/main_loop_type>`{.interpreted-text
role="ref"} project setting is overwritten.

Here is an example script implementing a simple **MainLoop**:

::::: tabs
::: code-tab
gdscript

class_name CustomMainLoop extends MainLoop

var time_elapsed = 0

func [initialize]{#initialize}():

:   print(\"Initialized:\") print(\" Starting time: %s\" %
    str(time_elapsed))

func [process]{#process}(delta):

:   time_elapsed += delta \# Return true to end the main loop. return
    Input.get_mouse_button_mask() != 0 \|\|
    Input.is_key_pressed(KEY_ESCAPE)

func [finalize]{#finalize}():

:   print(\"Finalized:\") print(\" End time: %s\" % str(time_elapsed))
:::

::: code-tab
csharp

using Godot;

\[GlobalClass\] public partial class CustomMainLoop : MainLoop { private
double [timeElapsed]{#timeelapsed} = 0;

> public override void [Initialize]{#initialize}() {
> GD.Print(\"Initialized:\"); GD.Print(\$\" Starting Time:
> {[timeElapsed]{#timeelapsed}}\"); }
>
> public override bool [Process]{#process}(double delta) {
> [timeElapsed]{#timeelapsed} += delta; // Return true to end the main
> loop. return Input.GetMouseButtonMask() != 0 \|\|
> Input.IsKeyPressed(Key.Escape); }
>
> private void [Finalize]{#finalize}() { GD.Print(\"Finalized:\");
> GD.Print(\$\" End Time: {[timeElapsed]{#timeelapsed}}\"); }

}
:::
:::::

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

:::: {#class_MainLoop_signal_on_request_permissions_result}
::: rst-class
classref-signal
:::
::::

**on_request_permissions_result**(permission:
`String<class_String>`{.interpreted-text role="ref"}, granted:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_MainLoop_signal_on_request_permissions_result>`{.interpreted-text
role="ref"}

Emitted when a user responds to a permission request.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_MainLoop_constant_NOTIFICATION_OS_MEMORY_WARNING}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_OS_MEMORY_WARNING** = `2009`
`🔗<class_MainLoop_constant_NOTIFICATION_OS_MEMORY_WARNING>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is exceeding its
allocated memory.

Specific to the iOS platform.

:::: {#class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_TRANSLATION_CHANGED** = `2010`
`🔗<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"}

Notification received when translations may have changed. Can be
triggered by the user changing the locale. Can be used to respond to
language changes, for example to change the UI strings on the fly.
Useful when working with the built-in translation support, like
`Object.tr()<class_Object_method_tr>`{.interpreted-text role="ref"}.

:::: {#class_MainLoop_constant_NOTIFICATION_WM_ABOUT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_ABOUT** = `2011`
`🔗<class_MainLoop_constant_NOTIFICATION_WM_ABOUT>`{.interpreted-text
role="ref"}

Notification received from the OS when a request for \"About\"
information is sent.

Specific to the macOS platform.

:::: {#class_MainLoop_constant_NOTIFICATION_CRASH}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_CRASH** = `2012`
`🔗<class_MainLoop_constant_NOTIFICATION_CRASH>`{.interpreted-text
role="ref"}

Notification received from Godot\'s crash handler when the engine is
about to crash.

Implemented on desktop platforms if the crash handler is enabled.

:::: {#class_MainLoop_constant_NOTIFICATION_OS_IME_UPDATE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_OS_IME_UPDATE** = `2013`
`🔗<class_MainLoop_constant_NOTIFICATION_OS_IME_UPDATE>`{.interpreted-text
role="ref"}

Notification received from the OS when an update of the Input Method
Engine occurs (e.g. change of IME cursor position or composition
string).

Specific to the macOS platform.

:::: {#class_MainLoop_constant_NOTIFICATION_APPLICATION_RESUMED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_APPLICATION_RESUMED** = `2014`
`🔗<class_MainLoop_constant_NOTIFICATION_APPLICATION_RESUMED>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is resumed.

Specific to the Android and iOS platforms.

:::: {#class_MainLoop_constant_NOTIFICATION_APPLICATION_PAUSED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_APPLICATION_PAUSED** = `2015`
`🔗<class_MainLoop_constant_NOTIFICATION_APPLICATION_PAUSED>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is paused.

Specific to the Android and iOS platforms.

\*\*Note:\*\* On iOS, you only have approximately 5 seconds to finish a
task started by this signal. If you go over this allotment, iOS will
kill the app instead of pausing it.

:::: {#class_MainLoop_constant_NOTIFICATION_APPLICATION_FOCUS_IN}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_APPLICATION_FOCUS_IN** = `2016`
`🔗<class_MainLoop_constant_NOTIFICATION_APPLICATION_FOCUS_IN>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is focused, i.e.
when changing the focus from the OS desktop or a thirdparty application
to any open window of the Godot instance.

Implemented on desktop and mobile platforms.

:::: {#class_MainLoop_constant_NOTIFICATION_APPLICATION_FOCUS_OUT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_APPLICATION_FOCUS_OUT** = `2017`
`🔗<class_MainLoop_constant_NOTIFICATION_APPLICATION_FOCUS_OUT>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is defocused,
i.e. when changing the focus from any open window of the Godot instance
to the OS desktop or a thirdparty application.

Implemented on desktop and mobile platforms.

:::: {#class_MainLoop_constant_NOTIFICATION_TEXT_SERVER_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_TEXT_SERVER_CHANGED** = `2018`
`🔗<class_MainLoop_constant_NOTIFICATION_TEXT_SERVER_CHANGED>`{.interpreted-text
role="ref"}

Notification received when text server is changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MainLoop_private_method__finalize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_finalize**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MainLoop_private_method__finalize>`{.interpreted-text
role="ref"}

Called before the program exits.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MainLoop_private_method__initialize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_initialize**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MainLoop_private_method__initialize>`{.interpreted-text
role="ref"}

Called once during initialization.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MainLoop_private_method__physics_process}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_physics_process**(delta: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MainLoop_private_method__physics_process>`{.interpreted-text
role="ref"}

Called each physics frame with the time since the last physics frame as
argument (`delta`, in seconds). Equivalent to
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}.

If implemented, the method must return a boolean value. `true` ends the
main loop, while `false` lets it proceed to the next frame.

\*\*Note:\*\* `delta` will be larger than expected if running at a
framerate lower than
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"} /
`Engine.max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>`{.interpreted-text
role="ref"} FPS. This is done to avoid \"spiral of death\" scenarios
where performance would plummet due to an ever-increasing number of
physics steps per frame. This behavior affects both
`_process()<class_MainLoop_private_method__process>`{.interpreted-text
role="ref"} and
`_physics_process()<class_MainLoop_private_method__physics_process>`{.interpreted-text
role="ref"}. As a result, avoid using `delta` for time measurements in
real-world seconds. Use the `Time<class_Time>`{.interpreted-text
role="ref"} singleton\'s methods for this purpose instead, such as
`Time.get_ticks_usec()<class_Time_method_get_ticks_usec>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MainLoop_private_method__process}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_process**(delta:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_MainLoop_private_method__process>`{.interpreted-text
role="ref"}

Called each process (idle) frame with the time since the last process
frame as argument (in seconds). Equivalent to
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}.

If implemented, the method must return a boolean value. `true` ends the
main loop, while `false` lets it proceed to the next frame.

\*\*Note:\*\* `delta` will be larger than expected if running at a
framerate lower than
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"} /
`Engine.max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>`{.interpreted-text
role="ref"} FPS. This is done to avoid \"spiral of death\" scenarios
where performance would plummet due to an ever-increasing number of
physics steps per frame. This behavior affects both
`_process()<class_MainLoop_private_method__process>`{.interpreted-text
role="ref"} and
`_physics_process()<class_MainLoop_private_method__physics_process>`{.interpreted-text
role="ref"}. As a result, avoid using `delta` for time measurements in
real-world seconds. Use the `Time<class_Time>`{.interpreted-text
role="ref"} singleton\'s methods for this purpose instead, such as
`Time.get_ticks_usec()<class_Time_method_get_ticks_usec>`{.interpreted-text
role="ref"}.
