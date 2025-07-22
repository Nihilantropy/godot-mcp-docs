github_url
:   hide

# OS {#class_OS}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Provides access to common operating system functionalities.

::: rst-class
classref-introduction-group
:::

## Description

The **OS** class wraps the most common functionalities for communicating
with the host operating system, such as the video driver, delays,
environment variables, execution of binaries, command line, etc.

\*\*Note:\*\* In Godot 4, **OS** functions related to window management,
clipboard, and TTS were moved to the
`DisplayServer<class_DisplayServer>`{.interpreted-text role="ref"}
singleton (and the `Window<class_Window>`{.interpreted-text role="ref"}
class). Functions related to time were removed and are only available in
the `Time<class_Time>`{.interpreted-text role="ref"} class.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Operating System Testing
  Demo](https://godotengine.org/asset-library/asset/2789)

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

## Enumerations

:::: {#enum_OS_RenderingDriver}
::: rst-class
classref-enumeration
:::
::::

enum **RenderingDriver**:
`🔗<enum_OS_RenderingDriver>`{.interpreted-text role="ref"}

:::: {#class_OS_constant_RENDERING_DRIVER_VULKAN}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingDriver<enum_OS_RenderingDriver>`{.interpreted-text role="ref"}
**RENDERING_DRIVER_VULKAN** = `0`

The Vulkan rendering driver. It requires Vulkan 1.0 support and
automatically uses features from Vulkan 1.1 and 1.2 if available.

:::: {#class_OS_constant_RENDERING_DRIVER_OPENGL3}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingDriver<enum_OS_RenderingDriver>`{.interpreted-text role="ref"}
**RENDERING_DRIVER_OPENGL3** = `1`

The OpenGL 3 rendering driver. It uses OpenGL 3.3 Core Profile on
desktop platforms, OpenGL ES 3.0 on mobile devices, and WebGL 2.0 on
Web.

:::: {#class_OS_constant_RENDERING_DRIVER_D3D12}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingDriver<enum_OS_RenderingDriver>`{.interpreted-text role="ref"}
**RENDERING_DRIVER_D3D12** = `2`

The Direct3D 12 rendering driver.

:::: {#class_OS_constant_RENDERING_DRIVER_METAL}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderingDriver<enum_OS_RenderingDriver>`{.interpreted-text role="ref"}
**RENDERING_DRIVER_METAL** = `3`

The Metal rendering driver.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OS_SystemDir}
::: rst-class
classref-enumeration
:::
::::

enum **SystemDir**: `🔗<enum_OS_SystemDir>`{.interpreted-text
role="ref"}

:::: {#class_OS_constant_SYSTEM_DIR_DESKTOP}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemDir<enum_OS_SystemDir>`{.interpreted-text role="ref"}
**SYSTEM_DIR_DESKTOP** = `0`

Refers to the Desktop directory path.

:::: {#class_OS_constant_SYSTEM_DIR_DCIM}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemDir<enum_OS_SystemDir>`{.interpreted-text role="ref"}
**SYSTEM_DIR_DCIM** = `1`

Refers to the DCIM (Digital Camera Images) directory path.

:::: {#class_OS_constant_SYSTEM_DIR_DOCUMENTS}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemDir<enum_OS_SystemDir>`{.interpreted-text role="ref"}
**SYSTEM_DIR_DOCUMENTS** = `2`

Refers to the Documents directory path.

:::: {#class_OS_constant_SYSTEM_DIR_DOWNLOADS}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemDir<enum_OS_SystemDir>`{.interpreted-text role="ref"}
**SYSTEM_DIR_DOWNLOADS** = `3`

Refers to the Downloads directory path.

:::: {#class_OS_constant_SYSTEM_DIR_MOVIES}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemDir<enum_OS_SystemDir>`{.interpreted-text role="ref"}
**SYSTEM_DIR_MOVIES** = `4`

Refers to the Movies (or Videos) directory path.

:::: {#class_OS_constant_SYSTEM_DIR_MUSIC}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemDir<enum_OS_SystemDir>`{.interpreted-text role="ref"}
**SYSTEM_DIR_MUSIC** = `5`

Refers to the Music directory path.

:::: {#class_OS_constant_SYSTEM_DIR_PICTURES}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemDir<enum_OS_SystemDir>`{.interpreted-text role="ref"}
**SYSTEM_DIR_PICTURES** = `6`

Refers to the Pictures directory path.

:::: {#class_OS_constant_SYSTEM_DIR_RINGTONES}
::: rst-class
classref-enumeration-constant
:::
::::

`SystemDir<enum_OS_SystemDir>`{.interpreted-text role="ref"}
**SYSTEM_DIR_RINGTONES** = `7`

Refers to the Ringtones directory path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OS_StdHandleType}
::: rst-class
classref-enumeration
:::
::::

enum **StdHandleType**: `🔗<enum_OS_StdHandleType>`{.interpreted-text
role="ref"}

:::: {#class_OS_constant_STD_HANDLE_INVALID}
::: rst-class
classref-enumeration-constant
:::
::::

`StdHandleType<enum_OS_StdHandleType>`{.interpreted-text role="ref"}
**STD_HANDLE_INVALID** = `0`

Standard I/O device is invalid. No data can be received from or sent to
these standard I/O devices.

:::: {#class_OS_constant_STD_HANDLE_CONSOLE}
::: rst-class
classref-enumeration-constant
:::
::::

`StdHandleType<enum_OS_StdHandleType>`{.interpreted-text role="ref"}
**STD_HANDLE_CONSOLE** = `1`

Standard I/O device is a console. This typically occurs when Godot is
run from a terminal with no redirection. This is also used for all
standard I/O devices when running Godot from the editor, at least on
desktop platforms.

:::: {#class_OS_constant_STD_HANDLE_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`StdHandleType<enum_OS_StdHandleType>`{.interpreted-text role="ref"}
**STD_HANDLE_FILE** = `2`

Standard I/O device is a regular file. This typically occurs with
redirection from a terminal, e.g. `godot > stdout.txt`,
`godot < stdin.txt` or `godot > stdout_stderr.txt 2>&1`.

:::: {#class_OS_constant_STD_HANDLE_PIPE}
::: rst-class
classref-enumeration-constant
:::
::::

`StdHandleType<enum_OS_StdHandleType>`{.interpreted-text role="ref"}
**STD_HANDLE_PIPE** = `3`

Standard I/O device is a FIFO/pipe. This typically occurs with pipe
usage from a terminal, e.g. `echo "Hello" | godot`.

:::: {#class_OS_constant_STD_HANDLE_UNKNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`StdHandleType<enum_OS_StdHandleType>`{.interpreted-text role="ref"}
**STD_HANDLE_UNKNOWN** = `4`

Standard I/O device type is unknown.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OS_property_delta_smoothing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **delta_smoothing** =
`true` `🔗<class_OS_property_delta_smoothing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_delta_smoothing**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_delta_smoothing_enabled**()

If `true`, the engine filters the time delta measured between each
frame, and attempts to compensate for random variation. This only works
on systems where V-Sync is active.

\*\*Note:\*\* On start-up, this is the same as
`ProjectSettings.application/run/delta_smoothing<class_ProjectSettings_property_application/run/delta_smoothing>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_property_low_processor_usage_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**low_processor_usage_mode** = `false`
`🔗<class_OS_property_low_processor_usage_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_low_processor_usage_mode**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_in_low_processor_usage_mode**()

If `true`, the engine optimizes for low processor usage by only
refreshing the screen if needed. Can improve battery consumption on
mobile.

\*\*Note:\*\* On start-up, this is the same as
`ProjectSettings.application/run/low_processor_mode<class_ProjectSettings_property_application/run/low_processor_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_property_low_processor_usage_mode_sleep_usec}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**low_processor_usage_mode_sleep_usec** = `6900`
`🔗<class_OS_property_low_processor_usage_mode_sleep_usec>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_low_processor_usage_mode_sleep_usec**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_low_processor_usage_mode_sleep_usec**()

The amount of sleeping between frames when the low-processor usage mode
is enabled, in microseconds. Higher values will result in lower CPU
usage. See also
`low_processor_usage_mode<class_OS_property_low_processor_usage_mode>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* On start-up, this is the same as
`ProjectSettings.application/run/low_processor_mode_sleep_usec<class_ProjectSettings_property_application/run/low_processor_mode_sleep_usec>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OS_method_add_logger}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_logger**(logger: `Logger<class_Logger>`{.interpreted-text
role="ref"}) `🔗<class_OS_method_add_logger>`{.interpreted-text
role="ref"}

Add a custom logger to intercept the internal message stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_alert}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **alert**(text:
`String<class_String>`{.interpreted-text role="ref"}, title:
`String<class_String>`{.interpreted-text role="ref"} = \"Alert!\")
`🔗<class_OS_method_alert>`{.interpreted-text role="ref"}

Displays a modal dialog box using the host platform\'s implementation.
The engine execution is blocked until the dialog is closed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_close_midi_inputs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**close_midi_inputs**()
`🔗<class_OS_method_close_midi_inputs>`{.interpreted-text role="ref"}

Shuts down the system MIDI driver. Godot will no longer receive
`InputEventMIDI<class_InputEventMIDI>`{.interpreted-text role="ref"}.
See also
`open_midi_inputs()<class_OS_method_open_midi_inputs>`{.interpreted-text
role="ref"} and
`get_connected_midi_inputs()<class_OS_method_get_connected_midi_inputs>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is implemented on Linux, macOS, Windows, and
Web.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_crash}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**crash**(message: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_OS_method_crash>`{.interpreted-text role="ref"}

Crashes the engine (or the editor if called within a `@tool` script).
See also `kill()<class_OS_method_kill>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This method should *only* be used for testing the
system\'s crash handler, not for any other purpose. For general error
reporting, use (in order of preference)
`@GDScript.assert()<class_@GDScript_method_assert>`{.interpreted-text
role="ref"},
`@GlobalScope.push_error()<class_@GlobalScope_method_push_error>`{.interpreted-text
role="ref"}, or `alert()<class_OS_method_alert>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_create_instance}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**create_instance**(arguments:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}) `🔗<class_OS_method_create_instance>`{.interpreted-text
role="ref"}

Creates a new instance of Godot that runs independently. The `arguments`
are used in the given order and separated by a space.

If the process is successfully created, this method returns the new
process\' ID, which you can use to monitor the process (and potentially
terminate it with `kill()<class_OS_method_kill>`{.interpreted-text
role="ref"}). If the process cannot be created, this method returns
`-1`.

See `create_process()<class_OS_method_create_process>`{.interpreted-text
role="ref"} if you wish to run a different process.

\*\*Note:\*\* This method is implemented on Android, Linux, macOS and
Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_create_process}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **create_process**(path:
`String<class_String>`{.interpreted-text role="ref"}, arguments:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, open_console: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_OS_method_create_process>`{.interpreted-text role="ref"}

Creates a new process that runs independently of Godot. It will not
terminate when Godot terminates. The path specified in `path` must exist
and be an executable file or macOS `.app` bundle. The path is resolved
based on the current platform. The `arguments` are used in the given
order and separated by a space.

On Windows, if `open_console` is `true` and the process is a console
app, a new terminal window will be opened.

If the process is successfully created, this method returns its process
ID, which you can use to monitor the process (and potentially terminate
it with `kill()<class_OS_method_kill>`{.interpreted-text role="ref"}).
Otherwise, this method returns `-1`.

\*\*Example:\*\* Run another instance of the project:

::::: tabs
::: code-tab
gdscript

var pid = OS.create_process(OS.get_executable_path(), \[\])
:::

::: code-tab
csharp

var pid = OS.CreateProcess(OS.GetExecutablePath(), \[\]);
:::
:::::

See `execute()<class_OS_method_execute>`{.interpreted-text role="ref"}
if you wish to run an external command and retrieve the results.

\*\*Note:\*\* This method is implemented on Android, Linux, macOS, and
Windows.

\*\*Note:\*\* On macOS, sandboxed applications are limited to run only
embedded helper executables, specified during export or system .app
bundle, system .app bundles will ignore arguments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_delay_msec}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**delay_msec**(msec: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_delay_msec>`{.interpreted-text
role="ref"}

Delays execution of the current thread by `msec` milliseconds. `msec`
must be greater than or equal to `0`. Otherwise,
`delay_msec()<class_OS_method_delay_msec>`{.interpreted-text role="ref"}
does nothing and prints an error message.

\*\*Note:\*\*
`delay_msec()<class_OS_method_delay_msec>`{.interpreted-text role="ref"}
is a *blocking* way to delay code execution. To delay code execution in
a non-blocking way, you may use
`SceneTree.create_timer()<class_SceneTree_method_create_timer>`{.interpreted-text
role="ref"}. Awaiting with
`SceneTreeTimer<class_SceneTreeTimer>`{.interpreted-text role="ref"}
delays the execution of code placed below the `await` without affecting
the rest of the project (or editor, for
`EditorPlugin<class_EditorPlugin>`{.interpreted-text role="ref"}s and
`EditorScript<class_EditorScript>`{.interpreted-text role="ref"}s).

\*\*Note:\*\* When
`delay_msec()<class_OS_method_delay_msec>`{.interpreted-text role="ref"}
is called on the main thread, it will freeze the project and will
prevent it from redrawing and registering input until the delay has
passed. When using
`delay_msec()<class_OS_method_delay_msec>`{.interpreted-text role="ref"}
as part of an `EditorPlugin<class_EditorPlugin>`{.interpreted-text
role="ref"} or `EditorScript<class_EditorScript>`{.interpreted-text
role="ref"}, it will freeze the editor but won\'t freeze the project if
it is currently running (since the project is an independent child
process).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_delay_usec}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**delay_usec**(usec: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_delay_usec>`{.interpreted-text
role="ref"}

Delays execution of the current thread by `usec` microseconds. `usec`
must be greater than or equal to `0`. Otherwise,
`delay_usec()<class_OS_method_delay_usec>`{.interpreted-text role="ref"}
does nothing and prints an error message.

\*\*Note:\*\*
`delay_usec()<class_OS_method_delay_usec>`{.interpreted-text role="ref"}
is a *blocking* way to delay code execution. To delay code execution in
a non-blocking way, you may use
`SceneTree.create_timer()<class_SceneTree_method_create_timer>`{.interpreted-text
role="ref"}. Awaiting with a
`SceneTreeTimer<class_SceneTreeTimer>`{.interpreted-text role="ref"}
delays the execution of code placed below the `await` without affecting
the rest of the project (or editor, for
`EditorPlugin<class_EditorPlugin>`{.interpreted-text role="ref"}s and
`EditorScript<class_EditorScript>`{.interpreted-text role="ref"}s).

\*\*Note:\*\* When
`delay_usec()<class_OS_method_delay_usec>`{.interpreted-text role="ref"}
is called on the main thread, it will freeze the project and will
prevent it from redrawing and registering input until the delay has
passed. When using
`delay_usec()<class_OS_method_delay_usec>`{.interpreted-text role="ref"}
as part of an `EditorPlugin<class_EditorPlugin>`{.interpreted-text
role="ref"} or `EditorScript<class_EditorScript>`{.interpreted-text
role="ref"}, it will freeze the editor but won\'t freeze the project if
it is currently running (since the project is an independent child
process).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_execute}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **execute**(path:
`String<class_String>`{.interpreted-text role="ref"}, arguments:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, output: `Array<class_Array>`{.interpreted-text role="ref"}
= \[\], read_stderr: `bool<class_bool>`{.interpreted-text role="ref"} =
false, open_console: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_OS_method_execute>`{.interpreted-text role="ref"}

Executes the given process in a *blocking* way. The file specified in
`path` must exist and be executable. The system path resolution will be
used. The `arguments` are used in the given order, separated by spaces,
and wrapped in quotes.

If an `output` array is provided, the complete shell output of the
process is appended to `output` as a single
`String<class_String>`{.interpreted-text role="ref"} element. If
`read_stderr` is `true`, the output to the standard error stream is also
appended to the array.

On Windows, if `open_console` is `true` and the process is a console
app, a new terminal window is opened.

This method returns the exit code of the command, or `-1` if the process
fails to execute.

\*\*Note:\*\* The main thread will be blocked until the executed command
terminates. Use `Thread<class_Thread>`{.interpreted-text role="ref"} to
create a separate thread that will not block the main thread, or use
`create_process()<class_OS_method_create_process>`{.interpreted-text
role="ref"} to create a completely independent process.

For example, to retrieve a list of the working directory\'s contents:

::::: tabs
::: code-tab
gdscript

var output = \[\] var exit_code = OS.execute(\"ls\", \[\"-l\",
\"/tmp\"\], output)
:::

::: code-tab
csharp

Godot.Collections.Array output = \[\]; int exitCode = OS.Execute(\"ls\",
\[\"-l\", \"/tmp\"\], output);
:::
:::::

If you wish to access a shell built-in or execute a composite command, a
platform-specific shell can be invoked. For example:

::::: tabs
::: code-tab
gdscript

var output = \[\] OS.execute(\"CMD.exe\", \[\"/C\", \"cd %TEMP% &&
dir\"\], output)
:::

::: code-tab
csharp

Godot.Collections.Array output = \[\]; OS.Execute(\"CMD.exe\", \[\"/C\",
\"cd %TEMP% && dir\"\], output);
:::
:::::

\*\*Note:\*\* This method is implemented on Android, Linux, macOS, and
Windows.

\*\*Note:\*\* To execute a Windows command interpreter built-in command,
specify `cmd.exe` in `path`, `/c` as the first argument, and the desired
command as the second argument.

\*\*Note:\*\* To execute a PowerShell built-in command, specify
`powershell.exe` in `path`, `-Command` as the first argument, and the
desired command as the second argument.

\*\*Note:\*\* To execute a Unix shell built-in command, specify shell
executable name in `path`, `-c` as the first argument, and the desired
command as the second argument.

\*\*Note:\*\* On macOS, sandboxed applications are limited to run only
embedded helper executables, specified during export.

\*\*Note:\*\* On Android, system commands such as `dumpsys` can only be
run on a rooted device.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_execute_with_pipe}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**execute_with_pipe**(path: `String<class_String>`{.interpreted-text
role="ref"}, arguments:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, blocking: `bool<class_bool>`{.interpreted-text role="ref"}
= true) `🔗<class_OS_method_execute_with_pipe>`{.interpreted-text
role="ref"}

Creates a new process that runs independently of Godot with redirected
IO. It will not terminate when Godot terminates. The path specified in
`path` must exist and be an executable file or macOS `.app` bundle. The
path is resolved based on the current platform. The `arguments` are used
in the given order and separated by a space.

If `blocking` is `false`, created pipes work in non-blocking mode, i.e.
read and write operations will return immediately. Use
`FileAccess.get_error()<class_FileAccess_method_get_error>`{.interpreted-text
role="ref"} to check if the last read/write operation was successful.

If the process cannot be created, this method returns an empty
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}. Otherwise,
this method returns a `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} with the following keys:

- `"stdio"` - `FileAccess<class_FileAccess>`{.interpreted-text
  role="ref"} to access the process stdin and stdout pipes (read/write).
- `"stderr"` - `FileAccess<class_FileAccess>`{.interpreted-text
  role="ref"} to access the process stderr pipe (read only).
- `"pid"` - Process ID as an `int<class_int>`{.interpreted-text
  role="ref"}, which you can use to monitor the process (and potentially
  terminate it with `kill()<class_OS_method_kill>`{.interpreted-text
  role="ref"}).

\*\*Note:\*\* This method is implemented on Android, Linux, macOS, and
Windows.

\*\*Note:\*\* To execute a Windows command interpreter built-in command,
specify `cmd.exe` in `path`, `/c` as the first argument, and the desired
command as the second argument.

\*\*Note:\*\* To execute a PowerShell built-in command, specify
`powershell.exe` in `path`, `-Command` as the first argument, and the
desired command as the second argument.

\*\*Note:\*\* To execute a Unix shell built-in command, specify shell
executable name in `path`, `-c` as the first argument, and the desired
command as the second argument.

\*\*Note:\*\* On macOS, sandboxed applications are limited to run only
embedded helper executables, specified during export or system .app
bundle, system .app bundles will ignore arguments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_find_keycode_from_string}
::: rst-class
classref-method
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**find_keycode_from_string**(string:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_find_keycode_from_string>`{.interpreted-text
role="ref"}

Finds the keycode for the given string. The returned values are
equivalent to the `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} constants.

::::: tabs
::: code-tab
gdscript

print(OS.find_keycode_from_string(\"C\")) \# Prints 67 (KEY_C)
print(OS.find_keycode_from_string(\"Escape\")) \# Prints 4194305
(KEY_ESCAPE) print(OS.find_keycode_from_string(\"Shift+Tab\")) \# Prints
37748738 (KEY_MASK_SHIFT \| KEY_TAB)
print(OS.find_keycode_from_string(\"Unknown\")) \# Prints 0 (KEY_NONE)
:::

::: code-tab
csharp

GD.Print(OS.FindKeycodeFromString(\"C\")); // Prints C (Key.C)
GD.Print(OS.FindKeycodeFromString(\"Escape\")); // Prints Escape
(Key.Escape) GD.Print(OS.FindKeycodeFromString(\"Shift+Tab\")); //
Prints 37748738 (KeyModifierMask.MaskShift \| Key.Tab)
GD.Print(OS.FindKeycodeFromString(\"Unknown\")); // Prints None
(Key.None)
:::
:::::

See also
`get_keycode_string()<class_OS_method_get_keycode_string>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_cache_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_cache_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_cache_dir>`{.interpreted-text
role="ref"}

Returns the *global* cache data directory according to the operating
system\'s standards.

On the Linux/BSD platform, this path can be overridden by setting the
`XDG_CACHE_HOME` environment variable before starting the project. See
`File paths in Godot projects <../tutorials/io/data_paths>`{.interpreted-text
role="doc"} in the documentation for more information. See also
`get_config_dir()<class_OS_method_get_config_dir>`{.interpreted-text
role="ref"} and
`get_data_dir()<class_OS_method_get_data_dir>`{.interpreted-text
role="ref"}.

Not to be confused with
`get_user_data_dir()<class_OS_method_get_user_data_dir>`{.interpreted-text
role="ref"}, which returns the *project-specific* user data path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_cmdline_args}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_cmdline_args**()
`🔗<class_OS_method_get_cmdline_args>`{.interpreted-text role="ref"}

Returns the command-line arguments passed to the engine.

Command-line arguments can be written in any form, including both
`--key value` and `--key=value` forms so they can be properly parsed, as
long as custom command-line arguments do not conflict with engine
arguments.

You can also incorporate environment variables using the
`get_environment()<class_OS_method_get_environment>`{.interpreted-text
role="ref"} method.

You can set
`ProjectSettings.editor/run/main_run_args<class_ProjectSettings_property_editor/run/main_run_args>`{.interpreted-text
role="ref"} to define command-line arguments to be passed by the editor
when running the project.

\*\*Example:\*\* Parse command-line arguments into a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} using the
`--key=value` form for arguments:

::::: tabs
::: code-tab
gdscript

var arguments = {} for argument in OS.get_cmdline_args(): if
argument.contains(\"=\"): var key_value = argument.split(\"=\")
arguments\[key_value\[0\].trim_prefix(\"\--\")\] = key_value\[1\] else:
\# Options without an argument will be present in the dictionary, \#
with the value set to an empty string.
arguments\[argument.trim_prefix(\"\--\")\] = \"\"
:::

::: code-tab
csharp

var arguments = new Dictionary\<string, string\>(); foreach (var
argument in OS.GetCmdlineArgs()) { if (argument.Contains(\'=\')) {
string\[\] keyValue = argument.Split(\"=\");
arguments\[keyValue\[0\].TrimPrefix(\"\--\")\] = keyValue\[1\]; } else {
// Options without an argument will be present in the dictionary, //
with the value set to an empty string.
arguments\[argument.TrimPrefix(\"\--\")\] = \"\"; } }
:::
:::::

\*\*Note:\*\* Passing custom user arguments directly is not recommended,
as the engine may discard or modify them. Instead, pass the standard
UNIX double dash (`--`) and then the custom arguments, which the engine
will ignore by design. These can be read via
`get_cmdline_user_args()<class_OS_method_get_cmdline_user_args>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_cmdline_user_args}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_cmdline_user_args**()
`🔗<class_OS_method_get_cmdline_user_args>`{.interpreted-text
role="ref"}

Returns the command-line user arguments passed to the engine. User
arguments are ignored by the engine and reserved for the user. They are
passed after the double dash `--` argument. `++` may be used when `--`
is intercepted by another program (such as `startx`).

    # Godot has been executed with the following command:
    # godot --fullscreen -- --level=2 --hardcore

    OS.get_cmdline_args()      # Returns ["--fullscreen", "--level=2", "--hardcore"]
    OS.get_cmdline_user_args() # Returns ["--level=2", "--hardcore"]

To get all passed arguments, use
`get_cmdline_args()<class_OS_method_get_cmdline_args>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_config_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_config_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_config_dir>`{.interpreted-text
role="ref"}

Returns the *global* user configuration directory according to the
operating system\'s standards.

On the Linux/BSD platform, this path can be overridden by setting the
`XDG_CONFIG_HOME` environment variable before starting the project. See
`File paths in Godot projects <../tutorials/io/data_paths>`{.interpreted-text
role="doc"} in the documentation for more information. See also
`get_cache_dir()<class_OS_method_get_cache_dir>`{.interpreted-text
role="ref"} and
`get_data_dir()<class_OS_method_get_data_dir>`{.interpreted-text
role="ref"}.

Not to be confused with
`get_user_data_dir()<class_OS_method_get_user_data_dir>`{.interpreted-text
role="ref"}, which returns the *project-specific* user data path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_connected_midi_inputs}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_connected_midi_inputs**()
`🔗<class_OS_method_get_connected_midi_inputs>`{.interpreted-text
role="ref"}

Returns an array of connected MIDI device names, if they exist. Returns
an empty array if the system MIDI driver has not previously been
initialized with
`open_midi_inputs()<class_OS_method_open_midi_inputs>`{.interpreted-text
role="ref"}. See also
`close_midi_inputs()<class_OS_method_close_midi_inputs>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is implemented on Linux, macOS, Windows, and
Web.

\*\*Note:\*\* On the Web platform, Web MIDI needs to be supported by the
browser. [For the time being](https://caniuse.com/midi), it is currently
supported by all major browsers, except Safari.

\*\*Note:\*\* On the Web platform, using MIDI input requires a browser
permission to be granted first. This permission request is performed
when calling
`open_midi_inputs()<class_OS_method_open_midi_inputs>`{.interpreted-text
role="ref"}. The browser will refrain from processing MIDI input until
the user accepts the permission request.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_data_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_data_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_data_dir>`{.interpreted-text
role="ref"}

Returns the *global* user data directory according to the operating
system\'s standards.

On the Linux/BSD platform, this path can be overridden by setting the
`XDG_DATA_HOME` environment variable before starting the project. See
`File paths in Godot projects <../tutorials/io/data_paths>`{.interpreted-text
role="doc"} in the documentation for more information. See also
`get_cache_dir()<class_OS_method_get_cache_dir>`{.interpreted-text
role="ref"} and
`get_config_dir()<class_OS_method_get_config_dir>`{.interpreted-text
role="ref"}.

Not to be confused with
`get_user_data_dir()<class_OS_method_get_user_data_dir>`{.interpreted-text
role="ref"}, which returns the *project-specific* user data path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_distribution_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_distribution_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_distribution_name>`{.interpreted-text
role="ref"}

Returns the name of the distribution for Linux and BSD platforms (e.g.
\"Ubuntu\", \"Manjaro\", \"OpenBSD\", etc.).

Returns the same value as
`get_name()<class_OS_method_get_name>`{.interpreted-text role="ref"} for
stock Android ROMs, but attempts to return the custom ROM name for
popular Android derivatives such as \"LineageOS\".

Returns the same value as
`get_name()<class_OS_method_get_name>`{.interpreted-text role="ref"} for
other platforms.

\*\*Note:\*\* This method is not supported on the Web platform. It
returns an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_entropy}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_entropy**(size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_OS_method_get_entropy>`{.interpreted-text role="ref"}

Generates a `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"} of cryptographically secure random bytes with given `size`.

\*\*Note:\*\* Generating large quantities of bytes using this method can
result in locking and entropy of lower quality on most platforms. Using
`Crypto.generate_random_bytes()<class_Crypto_method_generate_random_bytes>`{.interpreted-text
role="ref"} is preferred in most cases.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_environment}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_environment**(variable: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_environment>`{.interpreted-text
role="ref"}

Returns the value of the given environment variable, or an empty string
if `variable` doesn\'t exist.

\*\*Note:\*\* Double-check the casing of `variable`. Environment
variable names are case-sensitive on all platforms except Windows.

\*\*Note:\*\* On macOS, applications do not have access to shell
environment variables.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_executable_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_executable_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_executable_path>`{.interpreted-text
role="ref"}

Returns the file path to the current engine executable.

\*\*Note:\*\* On macOS, if you want to launch another instance of Godot,
always use
`create_instance()<class_OS_method_create_instance>`{.interpreted-text
role="ref"} instead of relying on the executable path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_granted_permissions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_granted_permissions**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_granted_permissions>`{.interpreted-text
role="ref"}

On Android devices: Returns the list of dangerous permissions that have
been granted.

On macOS: Returns the list of granted permissions and user selected
folders accessible to the application (sandboxed applications only). Use
the native file dialog to request folder access permission.

On iOS, visionOS: Returns the list of granted permissions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_keycode_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_keycode_string**(code:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_keycode_string>`{.interpreted-text
role="ref"}

Returns the given keycode as a `String<class_String>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

print(OS.get_keycode_string(KEY_C)) \# Prints \"C\"
print(OS.get_keycode_string(KEY_ESCAPE)) \# Prints \"Escape\"
print(OS.get_keycode_string(KEY_MASK_SHIFT \| KEY_TAB)) \# Prints
\"Shift+Tab\"
:::

::: code-tab
csharp

GD.Print(OS.GetKeycodeString(Key.C)); // Prints \"C\"
GD.Print(OS.GetKeycodeString(Key.Escape)); // Prints \"Escape\"
GD.Print(OS.GetKeycodeString((Key)KeyModifierMask.MaskShift \|
Key.Tab)); // Prints \"Shift+Tab\"
:::
:::::

See also
`find_keycode_from_string()<class_OS_method_find_keycode_from_string>`{.interpreted-text
role="ref"},
`InputEventKey.keycode<class_InputEventKey_property_keycode>`{.interpreted-text
role="ref"}, and
`InputEventKey.get_keycode_with_modifiers()<class_InputEventKey_method_get_keycode_with_modifiers>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_locale}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_locale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_locale>`{.interpreted-text
role="ref"}

Returns the host OS locale as a `String<class_String>`{.interpreted-text
role="ref"} of the form `language_Script_COUNTRY_VARIANT@extra`. Every
substring after `language` is optional and may not exist.

- `language` - 2 or 3-letter [language
  code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), in lower
  case.
- `Script` - 4-letter [script
  code](https://en.wikipedia.org/wiki/ISO_15924), in title case.
- `COUNTRY` - 2 or 3-letter [country
  code](https://en.wikipedia.org/wiki/ISO_3166-1), in upper case.
- `VARIANT` - language variant, region and sort order. The variant can
  have any number of underscored keywords.
- `extra` - semicolon separated list of additional key words. This may
  include currency, calendar, sort order and numbering system
  information.

If you want only the language code and not the fully specified locale
from the OS, you can use
`get_locale_language()<class_OS_method_get_locale_language>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_locale_language}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_locale_language**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_locale_language>`{.interpreted-text
role="ref"}

Returns the host OS locale\'s 2 or 3-letter [language
code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) as a string
which should be consistent on all platforms. This is equivalent to
extracting the `language` part of the
`get_locale()<class_OS_method_get_locale>`{.interpreted-text role="ref"}
string.

This can be used to narrow down fully specified locale strings to only
the \"common\" language code, when you don\'t need the additional
information about country code or variants. For example, for a French
Canadian user with `fr_CA` locale, this would return `fr`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_main_thread_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_main_thread_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_main_thread_id>`{.interpreted-text
role="ref"}

Returns the ID of the main thread. See
`get_thread_caller_id()<class_OS_method_get_thread_caller_id>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Thread IDs are not deterministic and may be reused across
application restarts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_memory_info}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_memory_info**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_memory_info>`{.interpreted-text
role="ref"}

Returns a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
containing information about the current memory with the following
entries:

- `"physical"` - total amount of usable physical memory in bytes. This
  value can be slightly less than the actual physical memory amount,
  since it does not include memory reserved by the kernel and devices.
- `"free"` - amount of physical memory, that can be immediately
  allocated without disk access or other costly operations, in bytes.
  The process might be able to allocate more physical memory, but this
  action will require moving inactive pages to disk, which can be
  expensive.
- `"available"` - amount of memory that can be allocated without
  extending the swap file(s), in bytes. This value includes both
  physical memory and swap.
- `"stack"` - size of the current thread stack in bytes.

\*\*Note:\*\* Each entry\'s value may be `-1` if it is unknown.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_model_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_model_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_model_name>`{.interpreted-text
role="ref"}

Returns the model name of the current device.

\*\*Note:\*\* This method is implemented on Android, iOS, macOS, and
Windows. Returns `"GenericDevice"` on unsupported platforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_name>`{.interpreted-text
role="ref"}

Returns the name of the host platform.

- On Windows, this is `"Windows"`.
- On macOS, this is `"macOS"`.
- On Linux-based operating systems, this is `"Linux"`.
- On BSD-based operating systems, this is `"FreeBSD"`, `"NetBSD"`,
  `"OpenBSD"`, or `"BSD"` as a fallback.
- On Android, this is `"Android"`.
- On iOS, this is `"iOS"`.
- On Web, this is `"Web"`.

\*\*Note:\*\* Custom builds of the engine may support additional
platforms, such as consoles, possibly returning other names.

::::: tabs
::: code-tab
gdscript

match OS.get_name():

:   

    \"Windows\":

    :   print(\"Welcome to Windows!\")

    \"macOS\":

    :   print(\"Welcome to macOS!\")

    \"Linux\", \"FreeBSD\", \"NetBSD\", \"OpenBSD\", \"BSD\":

    :   print(\"Welcome to Linux/BSD!\")

    \"Android\":

    :   print(\"Welcome to Android!\")

    \"iOS\":

    :   print(\"Welcome to iOS!\")

    \"Web\":

    :   print(\"Welcome to the Web!\")
:::

::: code-tab
csharp

switch (OS.GetName()) { case \"Windows\": GD.Print(\"Welcome to
Windows\"); break; case \"macOS\": GD.Print(\"Welcome to macOS!\");
break; case \"Linux\": case \"FreeBSD\": case \"NetBSD\": case
\"OpenBSD\": case \"BSD\": GD.Print(\"Welcome to Linux/BSD!\"); break;
case \"Android\": GD.Print(\"Welcome to Android!\"); break; case
\"iOS\": GD.Print(\"Welcome to iOS!\"); break; case \"Web\":
GD.Print(\"Welcome to the Web!\"); break; }
:::
:::::

\*\*Note:\*\* On Web platforms, it is still possible to determine the
host platform\'s OS with feature tags. See
`has_feature()<class_OS_method_has_feature>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_process_exit_code}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_process_exit_code**(pid: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_process_exit_code>`{.interpreted-text
role="ref"}

Returns the exit code of a spawned process once it has finished running
(see
`is_process_running()<class_OS_method_is_process_running>`{.interpreted-text
role="ref"}).

Returns `-1` if the `pid` is not a PID of a spawned child process, the
process is still running, or the method is not implemented for the
current platform.

\*\*Note:\*\* Returns `-1` if the `pid` is a macOS bundled app process.

\*\*Note:\*\* This method is implemented on Android, Linux, macOS and
Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_process_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_process_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_process_id>`{.interpreted-text
role="ref"}

Returns the number used by the host machine to uniquely identify this
application.

\*\*Note:\*\* On Web, this method always returns `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_processor_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_processor_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_processor_count>`{.interpreted-text
role="ref"}

Returns the number of *logical* CPU cores available on the host machine.
On CPUs with HyperThreading enabled, this number will be greater than
the number of *physical* CPU cores.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_processor_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_processor_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_processor_name>`{.interpreted-text
role="ref"}

Returns the full name of the CPU model on the host machine (e.g.
`"Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz"`).

\*\*Note:\*\* This method is only implemented on Windows, macOS, Linux
and iOS. On Android and Web,
`get_processor_name()<class_OS_method_get_processor_name>`{.interpreted-text
role="ref"} returns an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_restart_on_exit_arguments}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_restart_on_exit_arguments**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_restart_on_exit_arguments>`{.interpreted-text
role="ref"}

Returns the list of command line arguments that will be used when the
project automatically restarts using
`set_restart_on_exit()<class_OS_method_set_restart_on_exit>`{.interpreted-text
role="ref"}. See also
`is_restart_on_exit_set()<class_OS_method_is_restart_on_exit_set>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_static_memory_peak_usage}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_static_memory_peak_usage**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_static_memory_peak_usage>`{.interpreted-text
role="ref"}

Returns the maximum amount of static memory used. Only works in debug
builds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_static_memory_usage}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_static_memory_usage**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_static_memory_usage>`{.interpreted-text
role="ref"}

Returns the amount of static memory being used by the program in bytes.
Only works in debug builds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_stderr_type}
::: rst-class
classref-method
:::
::::

`StdHandleType<enum_OS_StdHandleType>`{.interpreted-text role="ref"}
**get_stderr_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_stderr_type>`{.interpreted-text
role="ref"}

Returns the type of the standard error device.

\*\*Note:\*\* This method is implemented on Linux, macOS, and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_stdin_type}
::: rst-class
classref-method
:::
::::

`StdHandleType<enum_OS_StdHandleType>`{.interpreted-text role="ref"}
**get_stdin_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_stdin_type>`{.interpreted-text
role="ref"}

Returns the type of the standard input device.

\*\*Note:\*\* This method is implemented on Linux, macOS, and Windows.

\*\*Note:\*\* On exported Windows builds, run the console wrapper
executable to access the standard input. If you need a single executable
with full console support, use a custom build compiled with the
`windows_subsystem=console` flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_stdout_type}
::: rst-class
classref-method
:::
::::

`StdHandleType<enum_OS_StdHandleType>`{.interpreted-text role="ref"}
**get_stdout_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_stdout_type>`{.interpreted-text
role="ref"}

Returns the type of the standard output device.

\*\*Note:\*\* This method is implemented on Linux, macOS, and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_system_ca_certificates}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_system_ca_certificates**()
`🔗<class_OS_method_get_system_ca_certificates>`{.interpreted-text
role="ref"}

Returns the list of certification authorities trusted by the operating
system as a string of concatenated certificates in PEM format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_system_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_system_dir**(dir: `SystemDir<enum_OS_SystemDir>`{.interpreted-text
role="ref"}, shared_storage: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_system_dir>`{.interpreted-text
role="ref"}

Returns the path to commonly used folders across different platforms, as
defined by `dir`. See the
`SystemDir<enum_OS_SystemDir>`{.interpreted-text role="ref"} constants
for available locations.

\*\*Note:\*\* This method is implemented on Android, Linux, macOS and
Windows.

\*\*Note:\*\* Shared storage is implemented on Android and allows to
differentiate between app specific and shared directories, if
`shared_storage` is `true`. Shared directories have additional
restrictions on Android.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_system_font_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_system_font_path**(font_name:
`String<class_String>`{.interpreted-text role="ref"}, weight:
`int<class_int>`{.interpreted-text role="ref"} = 400, stretch:
`int<class_int>`{.interpreted-text role="ref"} = 100, italic:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_system_font_path>`{.interpreted-text role="ref"}

Returns the path to the system font file with `font_name` and style.
Returns an empty string if no matching fonts found.

The following aliases can be used to request default fonts:
\"sans-serif\", \"serif\", \"monospace\", \"cursive\", and \"fantasy\".

\*\*Note:\*\* Returned font might have different style if the requested
style is not available.

\*\*Note:\*\* This method is implemented on Android, iOS, Linux, macOS
and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_system_font_path_for_text}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_system_font_path_for_text**(font_name:
`String<class_String>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"}, locale:
`String<class_String>`{.interpreted-text role="ref"} = \"\", script:
`String<class_String>`{.interpreted-text role="ref"} = \"\", weight:
`int<class_int>`{.interpreted-text role="ref"} = 400, stretch:
`int<class_int>`{.interpreted-text role="ref"} = 100, italic:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_system_font_path_for_text>`{.interpreted-text
role="ref"}

Returns an array of the system substitute font file paths, which are
similar to the font with `font_name` and style for the specified text,
locale, and script. Returns an empty array if no matching fonts found.

The following aliases can be used to request default fonts:
\"sans-serif\", \"serif\", \"monospace\", \"cursive\", and \"fantasy\".

\*\*Note:\*\* Depending on OS, it\'s not guaranteed that any of the
returned fonts will be suitable for rendering specified text. Fonts
should be loaded and checked in the order they are returned, and the
first suitable one used.

\*\*Note:\*\* Returned fonts might have different style if the requested
style is not available or belong to a different font family.

\*\*Note:\*\* This method is implemented on Android, iOS, Linux, macOS
and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_system_fonts}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_system_fonts**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_system_fonts>`{.interpreted-text
role="ref"}

Returns the list of font family names available.

\*\*Note:\*\* This method is implemented on Android, iOS, Linux, macOS
and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_temp_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_temp_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_temp_dir>`{.interpreted-text
role="ref"}

Returns the *global* temporary data directory according to the operating
system\'s standards.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_thread_caller_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_thread_caller_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_thread_caller_id>`{.interpreted-text role="ref"}

Returns the ID of the current thread. This can be used in logs to ease
debugging of multi-threaded applications.

\*\*Note:\*\* Thread IDs are not deterministic and may be reused across
application restarts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_unique_id}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_unique_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_unique_id>`{.interpreted-text
role="ref"}

Returns a string that is unique to the device.

\*\*Note:\*\* This string may change without notice if the user
reinstalls their operating system, upgrades it, or modifies their
hardware. This means it should generally not be used to encrypt
persistent data, as the data saved before an unexpected ID change would
become inaccessible. The returned string may also be falsified using
external programs, so do not rely on the string returned by this method
for security purposes.

\*\*Note:\*\* On Web, returns an empty string and generates an error, as
this method cannot be implemented for security reasons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_user_data_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_user_data_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_user_data_dir>`{.interpreted-text
role="ref"}

Returns the absolute directory path where user data is written (the
`user://` directory in Godot). The path depends on the project name and
`ProjectSettings.application/config/use_custom_user_dir<class_ProjectSettings_property_application/config/use_custom_user_dir>`{.interpreted-text
role="ref"}.

- On Windows, this is `%AppData%\Godot\app_userdata\[project_name]`, or
  `%AppData%\[custom_name]` if `use_custom_user_dir` is set. `%AppData%`
  expands to `%UserProfile%\AppData\Roaming`.
- On macOS, this is
  `~/Library/Application Support/Godot/app_userdata/[project_name]`, or
  `~/Library/Application Support/[custom_name]` if `use_custom_user_dir`
  is set.
- On Linux and BSD, this is
  `~/.local/share/godot/app_userdata/[project_name]`, or
  `~/.local/share/[custom_name]` if `use_custom_user_dir` is set.
- On Android and iOS, this is a sandboxed directory in either internal
  or external storage, depending on the user\'s configuration.
- On Web, this is a virtual directory managed by the browser.

If the project name is empty, `[project_name]` falls back to
`[unnamed project]`.

Not to be confused with
`get_data_dir()<class_OS_method_get_data_dir>`{.interpreted-text
role="ref"}, which returns the *global* (non-project-specific) user home
directory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_version}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_version**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_version>`{.interpreted-text
role="ref"}

Returns the exact production and build version of the operating system.
This is different from the branded version used in marketing. This helps
to distinguish between different releases of operating systems,
including minor versions, and insider and custom builds.

- For Windows, the major and minor version are returned, as well as the
  build number. For example, the returned string may look like
  `10.0.9926` for a build of Windows 10.
- For rolling distributions, such as Arch Linux, an empty string is
  returned.
- For macOS and iOS, the major and minor version are returned, as well
  as the patch number.
- For Android, the SDK version and the incremental build number are
  returned. If it\'s a custom ROM, it attempts to return its version
  instead.

\*\*Note:\*\* This method is not supported on the Web platform. It
returns an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_version_alias}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_version_alias**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_get_version_alias>`{.interpreted-text
role="ref"}

Returns the branded version used in marketing, followed by the build
number (on Windows), the version number (on macOS), or the SDK version
and incremental build number (on Android). Examples include
`11 (build 22000)`, `Sequoia (15.0.0)`, and
`15 (SDK 35 build abc528-11988f)`.

This value can then be appended to
`get_name()<class_OS_method_get_name>`{.interpreted-text role="ref"} to
get a full, human-readable operating system name and version combination
for the operating system. Windows feature updates such as 24H2 are not
contained in the resulting string, but Windows Server is recognized as
such (e.g. `2025 (build 26100)` for Windows Server 2025).

\*\*Note:\*\* This method is only supported on Windows, macOS, and
Android. On other operating systems, it returns the same value as
`get_version()<class_OS_method_get_version>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_get_video_adapter_driver_info}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_video_adapter_driver_info**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_get_video_adapter_driver_info>`{.interpreted-text
role="ref"}

Returns the video adapter driver name and version for the user\'s
currently active graphics card, as a
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}. See also
`RenderingServer.get_video_adapter_api_version()<class_RenderingServer_method_get_video_adapter_api_version>`{.interpreted-text
role="ref"}.

The first element holds the driver name, such as `nvidia`, `amdgpu`,
etc.

The second element holds the driver version. For example, on the
`nvidia` driver on a Linux/BSD platform, the version is in the format
`510.85.02`. For Windows, the driver\'s format is `31.0.15.1659`.

\*\*Note:\*\* This method is only supported on Linux/BSD and Windows
when not running in headless mode. On other platforms, it returns an
empty array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_has_environment}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_environment**(variable: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_has_environment>`{.interpreted-text
role="ref"}

Returns `true` if the environment variable with the name `variable`
exists.

\*\*Note:\*\* Double-check the casing of `variable`. Environment
variable names are case-sensitive on all platforms except Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_has_feature}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_feature**(tag_name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_has_feature>`{.interpreted-text
role="ref"}

Returns `true` if the feature for the given feature tag is supported in
the currently running instance, depending on the platform, build, etc.
Can be used to check whether you\'re currently running a debug build, on
a certain platform or arch, etc. Refer to the
`Feature Tags <../tutorials/export/feature_tags>`{.interpreted-text
role="doc"} documentation for more details.

\*\*Note:\*\* Tag names are case-sensitive.

\*\*Note:\*\* On the Web platform, one of the following additional tags
is defined to indicate the host platform: `web_android`, `web_ios`,
`web_linuxbsd`, `web_macos`, or `web_windows`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_is_debug_build}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_debug_build**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_is_debug_build>`{.interpreted-text
role="ref"}

Returns `true` if the Godot binary used to run the project is a *debug*
export template, or when running in the editor.

Returns `false` if the Godot binary used to run the project is a
*release* export template.

\*\*Note:\*\* To check whether the Godot binary used to run the project
is an export template (debug or release), use
`OS.has_feature("template")` instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_is_keycode_unicode}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_keycode_unicode**(code: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_is_keycode_unicode>`{.interpreted-text
role="ref"}

Returns `true` if the input keycode corresponds to a Unicode character.
For a list of codes, see the
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} constants.

::::: tabs
::: code-tab
gdscript

print(OS.is_keycode_unicode(KEY_G)) \# Prints true
print(OS.is_keycode_unicode(KEY_KP_4)) \# Prints true
print(OS.is_keycode_unicode(KEY_TAB)) \# Prints false
print(OS.is_keycode_unicode(KEY_ESCAPE)) \# Prints false
:::

::: code-tab
csharp

GD.Print(OS.IsKeycodeUnicode((long)Key.G)); // Prints True
GD.Print(OS.IsKeycodeUnicode((long)Key.Kp4)); // Prints True
GD.Print(OS.IsKeycodeUnicode((long)Key.Tab)); // Prints False
GD.Print(OS.IsKeycodeUnicode((long)Key.Escape)); // Prints False
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_is_process_running}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_process_running**(pid: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_is_process_running>`{.interpreted-text
role="ref"}

Returns `true` if the child process ID (`pid`) is still running or
`false` if it has terminated. `pid` must be a valid ID generated from
`create_process()<class_OS_method_create_process>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is implemented on Android, iOS, Linux, macOS,
and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_is_restart_on_exit_set}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_restart_on_exit_set**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_is_restart_on_exit_set>`{.interpreted-text
role="ref"}

Returns `true` if the project will automatically restart when it exits
for any reason, `false` otherwise. See also
`set_restart_on_exit()<class_OS_method_set_restart_on_exit>`{.interpreted-text
role="ref"} and
`get_restart_on_exit_arguments()<class_OS_method_get_restart_on_exit_arguments>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_is_sandboxed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_sandboxed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_is_sandboxed>`{.interpreted-text
role="ref"}

Returns `true` if the application is running in the sandbox.

\*\*Note:\*\* This method is only implemented on macOS and Linux.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_is_stdout_verbose}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_stdout_verbose**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_is_stdout_verbose>`{.interpreted-text
role="ref"}

Returns `true` if the engine was executed with the `--verbose` or `-v`
command line argument, or if
`ProjectSettings.debug/settings/stdout/verbose_stdout<class_ProjectSettings_property_debug/settings/stdout/verbose_stdout>`{.interpreted-text
role="ref"} is `true`. See also
`@GlobalScope.print_verbose()<class_@GlobalScope_method_print_verbose>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_is_userfs_persistent}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_userfs_persistent**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OS_method_is_userfs_persistent>`{.interpreted-text role="ref"}

Returns `true` if the `user://` file system is persistent, that is, its
state is the same after a player quits and starts the game again.
Relevant to the Web platform, where this persistence may be unavailable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_kill}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**kill**(pid: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_OS_method_kill>`{.interpreted-text role="ref"}

Kill (terminate) the process identified by the given process ID (`pid`),
such as the ID returned by
`execute()<class_OS_method_execute>`{.interpreted-text role="ref"} in
non-blocking mode. See also
`crash()<class_OS_method_crash>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This method can also be used to kill processes that were
not spawned by the engine.

\*\*Note:\*\* This method is implemented on Android, iOS, Linux, macOS
and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_move_to_trash}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**move_to_trash**(path: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_move_to_trash>`{.interpreted-text
role="ref"}

Moves the file or directory at the given `path` to the system\'s recycle
bin. See also
`DirAccess.remove()<class_DirAccess_method_remove>`{.interpreted-text
role="ref"}.

The method takes only global paths, so you may need to use
`ProjectSettings.globalize_path()<class_ProjectSettings_method_globalize_path>`{.interpreted-text
role="ref"}. Do not use it for files in `res://` as it will not work in
exported projects.

Returns
`@GlobalScope.FAILED<class_@GlobalScope_constant_FAILED>`{.interpreted-text
role="ref"} if the file or directory cannot be found, or the system does
not support this method.

::::: tabs
::: code-tab
gdscript

var file_to_remove = \"user://slot1.save\"
OS.move_to_trash(ProjectSettings.globalize_path(file_to_remove))
:::

::: code-tab
csharp

var fileToRemove = \"user://slot1.save\";
OS.MoveToTrash(ProjectSettings.GlobalizePath(fileToRemove));
:::
:::::

\*\*Note:\*\* This method is implemented on Android, Linux, macOS and
Windows.

\*\*Note:\*\* If the user has disabled the recycle bin on their system,
the file will be permanently deleted instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_open_midi_inputs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**open_midi_inputs**()
`🔗<class_OS_method_open_midi_inputs>`{.interpreted-text role="ref"}

Initializes the singleton for the system MIDI driver, allowing Godot to
receive `InputEventMIDI<class_InputEventMIDI>`{.interpreted-text
role="ref"}. See also
`get_connected_midi_inputs()<class_OS_method_get_connected_midi_inputs>`{.interpreted-text
role="ref"} and
`close_midi_inputs()<class_OS_method_close_midi_inputs>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is implemented on Linux, macOS, Windows, and
Web.

\*\*Note:\*\* On the Web platform, Web MIDI needs to be supported by the
browser. [For the time being](https://caniuse.com/midi), it is currently
supported by all major browsers, except Safari.

\*\*Note:\*\* On the Web platform, using MIDI input requires a browser
permission to be granted first. This permission request is performed
when calling
`open_midi_inputs()<class_OS_method_open_midi_inputs>`{.interpreted-text
role="ref"}. The browser will refrain from processing MIDI input until
the user accepts the permission request.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_open_with_program}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**open_with_program**(program_path:
`String<class_String>`{.interpreted-text role="ref"}, paths:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}) `🔗<class_OS_method_open_with_program>`{.interpreted-text
role="ref"}

Opens one or more files/directories with the specified application. The
`program_path` specifies the path to the application to use for opening
the files, and `paths` contains an array of file/directory paths to
open.

\*\*Note:\*\* This method is mostly only relevant for macOS, where
opening files using
`create_process()<class_OS_method_create_process>`{.interpreted-text
role="ref"} might fail. On other platforms, this falls back to using
`create_process()<class_OS_method_create_process>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* On macOS, `program_path` should ideally be the path to a
`.app` bundle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_read_buffer_from_stdin}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**read_buffer_from_stdin**(buffer_size:
`int<class_int>`{.interpreted-text role="ref"} = 1024)
`🔗<class_OS_method_read_buffer_from_stdin>`{.interpreted-text
role="ref"}

Reads a user input as raw data from the standard input. This operation
can be *blocking*, which causes the window to freeze if
`read_buffer_from_stdin()<class_OS_method_read_buffer_from_stdin>`{.interpreted-text
role="ref"} is called on the main thread.

- If standard input is console, this method will block until the program
  receives a line break in standard input (usually by the user pressing
  `Enter`{.interpreted-text role="kbd"}).
- If standard input is pipe, this method will block until a specific
  amount of data is read or pipe is closed.
- If standard input is a file, this method will read a specific amount
  of data (or less if end-of-file is reached) and return immediately.

\*\*Note:\*\* This method is implemented on Linux, macOS, and Windows.

\*\*Note:\*\* On exported Windows builds, run the console wrapper
executable to access the terminal. If standard input is console, calling
this method without console wrapped will freeze permanently. If standard
input is pipe or file, it can be used without console wrapper. If you
need a single executable with full console support, use a custom build
compiled with the `windows_subsystem=console` flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_read_string_from_stdin}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**read_string_from_stdin**(buffer_size:
`int<class_int>`{.interpreted-text role="ref"} = 1024)
`🔗<class_OS_method_read_string_from_stdin>`{.interpreted-text
role="ref"}

Reads a user input as a UTF-8 encoded string from the standard input.
This operation can be *blocking*, which causes the window to freeze if
`read_string_from_stdin()<class_OS_method_read_string_from_stdin>`{.interpreted-text
role="ref"} is called on the main thread.

- If standard input is console, this method will block until the program
  receives a line break in standard input (usually by the user pressing
  `Enter`{.interpreted-text role="kbd"}).
- If standard input is pipe, this method will block until a specific
  amount of data is read or pipe is closed.
- If standard input is a file, this method will read a specific amount
  of data (or less if end-of-file is reached) and return immediately.

\*\*Note:\*\* This method automatically replaces `\r\n` line breaks with
`\n` and removes them from the end of the string. Use
`read_buffer_from_stdin()<class_OS_method_read_buffer_from_stdin>`{.interpreted-text
role="ref"} to read the unprocessed data.

\*\*Note:\*\* This method is implemented on Linux, macOS, and Windows.

\*\*Note:\*\* On exported Windows builds, run the console wrapper
executable to access the terminal. If standard input is console, calling
this method without console wrapped will freeze permanently. If standard
input is pipe or file, it can be used without console wrapper. If you
need a single executable with full console support, use a custom build
compiled with the `windows_subsystem=console` flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_remove_logger}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_logger**(logger: `Logger<class_Logger>`{.interpreted-text
role="ref"}) `🔗<class_OS_method_remove_logger>`{.interpreted-text
role="ref"}

Remove a custom logger added by
`add_logger()<class_OS_method_add_logger>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_request_permission}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**request_permission**(name: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_OS_method_request_permission>`{.interpreted-text
role="ref"}

Requests permission from the OS for the given `name`. Returns `true` if
the permission has already been granted. See also
`MainLoop.on_request_permissions_result<class_MainLoop_signal_on_request_permissions_result>`{.interpreted-text
role="ref"}.

The `name` must be the full permission name. For example:

- `OS.request_permission("android.permission.READ_EXTERNAL_STORAGE")`
- `OS.request_permission("android.permission.POST_NOTIFICATIONS")`
- `OS.request_permission("macos.permission.RECORD_SCREEN")`
- `OS.request_permission("appleembedded.permission.AUDIO_RECORD")`

\*\*Note:\*\* On Android, permission must be checked during export.

\*\*Note:\*\* This method is implemented on Android, macOS, and visionOS
platforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_request_permissions}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**request_permissions**()
`🔗<class_OS_method_request_permissions>`{.interpreted-text role="ref"}

Requests *dangerous* permissions from the OS. Returns `true` if
permissions have already been granted. See also
`MainLoop.on_request_permissions_result<class_MainLoop_signal_on_request_permissions_result>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Permissions must be checked during export.

\*\*Note:\*\* This method is only implemented on Android. Normal
permissions are automatically granted at install time in Android
applications.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_revoke_granted_permissions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**revoke_granted_permissions**()
`🔗<class_OS_method_revoke_granted_permissions>`{.interpreted-text
role="ref"}

On macOS (sandboxed applications only), this function clears list of
user selected folders accessible to the application.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_set_environment}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_environment**(variable: `String<class_String>`{.interpreted-text
role="ref"}, value: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_set_environment>`{.interpreted-text
role="ref"}

Sets the value of the environment variable `variable` to `value`. The
environment variable will be set for the Godot process and any process
executed with `execute()<class_OS_method_execute>`{.interpreted-text
role="ref"} after running
`set_environment()<class_OS_method_set_environment>`{.interpreted-text
role="ref"}. The environment variable will *not* persist to processes
run after the Godot process was terminated.

\*\*Note:\*\* Environment variable names are case-sensitive on all
platforms except Windows. The `variable` name cannot be empty or include
the `=` character. On Windows, there is a 32767 characters limit for the
combined length of `variable`, `value`, and the `=` and null terminator
characters that will be registered in the environment block.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_set_restart_on_exit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_restart_on_exit**(restart: `bool<class_bool>`{.interpreted-text
role="ref"}, arguments:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} = PackedStringArray())
`🔗<class_OS_method_set_restart_on_exit>`{.interpreted-text role="ref"}

If `restart` is `true`, restarts the project automatically when it is
exited with
`SceneTree.quit()<class_SceneTree_method_quit>`{.interpreted-text
role="ref"} or
`Node.NOTIFICATION_WM_CLOSE_REQUEST<class_Node_constant_NOTIFICATION_WM_CLOSE_REQUEST>`{.interpreted-text
role="ref"}. Command-line `arguments` can be supplied. To restart the
project with the same command line arguments as originally used to run
the project, pass
`get_cmdline_args()<class_OS_method_get_cmdline_args>`{.interpreted-text
role="ref"} as the value for `arguments`.

This method can be used to apply setting changes that require a restart.
See also
`is_restart_on_exit_set()<class_OS_method_is_restart_on_exit_set>`{.interpreted-text
role="ref"} and
`get_restart_on_exit_arguments()<class_OS_method_get_restart_on_exit_arguments>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is only effective on desktop platforms, and
only when the project isn\'t started from the editor. It will have no
effect on mobile and Web platforms, or when the project is started from
the editor.

\*\*Note:\*\* If the project process crashes or is *killed* by the user
(by sending `SIGKILL` instead of the usual `SIGTERM`), the project
won\'t restart automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_set_thread_name}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**set_thread_name**(name: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_OS_method_set_thread_name>`{.interpreted-text
role="ref"}

Assigns the given name to the current thread. Returns
`@GlobalScope.ERR_UNAVAILABLE<class_@GlobalScope_constant_ERR_UNAVAILABLE>`{.interpreted-text
role="ref"} if unavailable on the current platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_set_use_file_access_save_and_swap}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_use_file_access_save_and_swap**(enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_OS_method_set_use_file_access_save_and_swap>`{.interpreted-text
role="ref"}

If `enabled` is `true`, when opening a file for writing, a temporary
file is used in its place. When closed, it is automatically applied to
the target file.

This can useful when files may be opened by other applications, such as
antiviruses, text editors, or even the Godot editor itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_shell_open}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**shell_open**(uri: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_OS_method_shell_open>`{.interpreted-text
role="ref"}

Requests the OS to open a resource identified by `uri` with the most
appropriate program. For example:

- `OS.shell_open("C:\\Users\\name\\Downloads")` on Windows opens the
  file explorer at the user\'s Downloads folder.
- `OS.shell_open("C:/Users/name/Downloads")` also works on Windows and
  opens the file explorer at the user\'s Downloads folder.
- `OS.shell_open("https://godotengine.org")` opens the default web
  browser on the official Godot website.
- `OS.shell_open("mailto:example@example.com")` opens the default email
  client with the \"To\" field set to `example@example.com`. See [RFC
  2368 - The \[code\]mailto\[/code\] URL
  scheme](https://datatracker.ietf.org/doc/html/rfc2368) for a list of
  fields that can be added.

Use
`ProjectSettings.globalize_path()<class_ProjectSettings_method_globalize_path>`{.interpreted-text
role="ref"} to convert a `res://` or `user://` project path into a
system path for use with this method.

\*\*Note:\*\* Use
`String.uri_encode()<class_String_method_uri_encode>`{.interpreted-text
role="ref"} to encode characters within URLs in a URL-safe, portable
way. This is especially required for line breaks. Otherwise,
`shell_open()<class_OS_method_shell_open>`{.interpreted-text role="ref"}
may not work correctly in a project exported to the Web platform.

\*\*Note:\*\* This method is implemented on Android, iOS, Web, Linux,
macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_shell_show_in_file_manager}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**shell_show_in_file_manager**(file_or_dir_path:
`String<class_String>`{.interpreted-text role="ref"}, open_folder:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_OS_method_shell_show_in_file_manager>`{.interpreted-text
role="ref"}

Requests the OS to open the file manager, navigate to the given
`file_or_dir_path` and select the target file or folder.

If `open_folder` is `true` and `file_or_dir_path` is a valid directory
path, the OS will open the file manager and navigate to the target
folder without selecting anything.

Use
`ProjectSettings.globalize_path()<class_ProjectSettings_method_globalize_path>`{.interpreted-text
role="ref"} to convert a `res://` or `user://` project path into a
system path to use with this method.

\*\*Note:\*\* This method is currently only implemented on Windows and
macOS. On other platforms, it will fallback to
`shell_open()<class_OS_method_shell_open>`{.interpreted-text role="ref"}
with a directory path of `file_or_dir_path` prefixed with `file://`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OS_method_unset_environment}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unset_environment**(variable: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_OS_method_unset_environment>`{.interpreted-text
role="ref"}

Removes the given environment variable from the current environment, if
it exists. The `variable` name cannot be empty or include the `=`
character. The environment variable will be removed for the Godot
process and any process executed with
`execute()<class_OS_method_execute>`{.interpreted-text role="ref"} after
running
`unset_environment()<class_OS_method_unset_environment>`{.interpreted-text
role="ref"}. The removal of the environment variable will *not* persist
to processes run after the Godot process was terminated.

\*\*Note:\*\* Environment variable names are case-sensitive on all
platforms except Windows.
