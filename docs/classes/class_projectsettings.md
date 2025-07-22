github_url
:   hide

# ProjectSettings {#class_ProjectSettings}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Stores globally-accessible variables.

::: rst-class
classref-introduction-group
:::

## Description

Stores variables that can be accessed from everywhere. Use
`get_setting()<class_ProjectSettings_method_get_setting>`{.interpreted-text
role="ref"},
`set_setting()<class_ProjectSettings_method_set_setting>`{.interpreted-text
role="ref"} or
`has_setting()<class_ProjectSettings_method_has_setting>`{.interpreted-text
role="ref"} to access them. Variables stored in `project.godot` are also
loaded into **ProjectSettings**, making this object very useful for
reading custom game configuration options.

When naming a Project Settings property, use the full path to the
setting including the category. For example, `"application/config/name"`
for the project name. Category and property names can be viewed in the
Project Settings dialog.

\*\*Feature tags:\*\* Project settings can be overridden for specific
platforms and configurations (debug, release, \...) using
`feature tags <../tutorials/export/feature_tags>`{.interpreted-text
role="doc"}.

\*\*Overriding:\*\* Any project setting can be overridden by creating a
file named `override.cfg` in the project\'s root directory. This can
also be used in exported projects by placing this file in the same
directory as the project binary. Overriding will still take the base
project settings\'
`feature tags <../tutorials/export/feature_tags>`{.interpreted-text
role="doc"} in account. Therefore, make sure to *also* override the
setting with the desired feature tags if you want them to override base
project settings on all platforms and configurations.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Project Settings <../tutorials/editor/project_settings>`{.interpreted-text
  role="doc"}
- [3D Physics Tests
  Demo](https://godotengine.org/asset-library/asset/2747)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
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

## Signals

:::: {#class_ProjectSettings_signal_settings_changed}
::: rst-class
classref-signal
:::
::::

**settings_changed**()
`🔗<class_ProjectSettings_signal_settings_changed>`{.interpreted-text
role="ref"}

Emitted when any setting is changed, up to once per process frame.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ProjectSettings_property_accessibility/general/accessibility_support}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**accessibility/general/accessibility_support** = `0`
`🔗<class_ProjectSettings_property_accessibility/general/accessibility_support>`{.interpreted-text
role="ref"}

Accessibility support mode:

- **Auto** (`0`): Accessibility support is enabled, but updates to the
  accessibility information are processed only if an assistive app (such
  as a screen reader or a Braille display) is active (default).
- **Always Active** (`1`): Accessibility support is enabled, and updates
  to the accessibility information are always processed, regardless of
  the status of assistive apps.
- **Disabled** (`2`): Accessibility support is fully disabled.

\*\*Note:\*\* Accessibility debugging tools, such as Accessibility
Insights for Windows, Accessibility Inspector (macOS), or AT-SPI Browser
(Linux/BSD) do not count as assistive apps. To test your project with
these tools, use **Always Active**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_accessibility/general/updates_per_second}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**accessibility/general/updates_per_second** = `60`
`🔗<class_ProjectSettings_property_accessibility/general/updates_per_second>`{.interpreted-text
role="ref"}

The number of accessibility information updates per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_animation/warnings/check_angle_interpolation_type_conflicting}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**animation/warnings/check_angle_interpolation_type_conflicting** =
`true`
`🔗<class_ProjectSettings_property_animation/warnings/check_angle_interpolation_type_conflicting>`{.interpreted-text
role="ref"}

If `true`, `AnimationMixer<class_AnimationMixer>`{.interpreted-text
role="ref"} prints the warning of interpolation being forced to choose
the shortest rotation path due to multiple angle interpolation types
being mixed in the
`AnimationMixer<class_AnimationMixer>`{.interpreted-text role="ref"}
cache.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_animation/warnings/check_invalid_track_paths}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**animation/warnings/check_invalid_track_paths** = `true`
`🔗<class_ProjectSettings_property_animation/warnings/check_invalid_track_paths>`{.interpreted-text
role="ref"}

If `true`, `AnimationMixer<class_AnimationMixer>`{.interpreted-text
role="ref"} prints the warning of no matching object of the track path
in the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/boot_splash/bg_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**application/boot_splash/bg_color** = `Color(0.14, 0.14, 0.14, 1)`
`🔗<class_ProjectSettings_property_application/boot_splash/bg_color>`{.interpreted-text
role="ref"}

Background color for the boot splash.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/boot_splash/fullsize}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/boot_splash/fullsize** = `true`
`🔗<class_ProjectSettings_property_application/boot_splash/fullsize>`{.interpreted-text
role="ref"}

If `true`, scale the boot splash image to the full window size
(preserving the aspect ratio) when the engine starts. If `false`, the
engine will leave it at the default pixel size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/boot_splash/image}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/boot_splash/image** = `""`
`🔗<class_ProjectSettings_property_application/boot_splash/image>`{.interpreted-text
role="ref"}

Path to an image used as the boot splash. If left empty, the default
Godot Engine splash will be displayed instead.

\*\*Note:\*\* Only effective if
`application/boot_splash/show_image<class_ProjectSettings_property_application/boot_splash/show_image>`{.interpreted-text
role="ref"} is `true`.

\*\*Note:\*\* The only supported format is PNG. Using another image
format will result in an error.

\*\*Note:\*\* The image will also show when opening the project in the
editor. If you want to display the default splash image in the editor,
add an empty override for `editor_hint` feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/boot_splash/minimum_display_time}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/boot_splash/minimum_display_time** = `0`
`🔗<class_ProjectSettings_property_application/boot_splash/minimum_display_time>`{.interpreted-text
role="ref"}

Minimum boot splash display time (in milliseconds). It is not
recommended to set too high values for this setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/boot_splash/show_image}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/boot_splash/show_image** = `true`
`🔗<class_ProjectSettings_property_application/boot_splash/show_image>`{.interpreted-text
role="ref"}

If `true`, displays the image specified in
`application/boot_splash/image<class_ProjectSettings_property_application/boot_splash/image>`{.interpreted-text
role="ref"} when the engine starts. If `false`, only displays the plain
color specified in
`application/boot_splash/bg_color<class_ProjectSettings_property_application/boot_splash/bg_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/boot_splash/use_filter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/boot_splash/use_filter** = `true`
`🔗<class_ProjectSettings_property_application/boot_splash/use_filter>`{.interpreted-text
role="ref"}

If `true`, applies linear filtering when scaling the image (recommended
for high-resolution artwork). If `false`, uses nearest-neighbor
interpolation (recommended for pixel art).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/auto_accept_quit}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/config/auto_accept_quit** = `true`
`🔗<class_ProjectSettings_property_application/config/auto_accept_quit>`{.interpreted-text
role="ref"}

If `true`, the application automatically accepts quitting requests.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/custom_user_dir_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/config/custom_user_dir_name** = `""`
`🔗<class_ProjectSettings_property_application/config/custom_user_dir_name>`{.interpreted-text
role="ref"}

This user directory is used for storing persistent data (`user://`
filesystem). If a custom directory name is defined, this name will be
appended to the system-specific user data directory (same parent folder
as the Godot configuration folder documented in
`OS.get_user_data_dir()<class_OS_method_get_user_data_dir>`{.interpreted-text
role="ref"}).

The
`application/config/use_custom_user_dir<class_ProjectSettings_property_application/config/use_custom_user_dir>`{.interpreted-text
role="ref"} setting must be enabled for this to take effect.

\*\*Note:\*\* If
`application/config/custom_user_dir_name<class_ProjectSettings_property_application/config/custom_user_dir_name>`{.interpreted-text
role="ref"} contains trailing periods, they will be stripped as folder
names ending with a period are not allowed on Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/config/description** = `""`
`🔗<class_ProjectSettings_property_application/config/description>`{.interpreted-text
role="ref"}

The project\'s description, displayed as a tooltip in the Project
Manager when hovering the project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/icon}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/config/icon** = `""`
`🔗<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}

Icon used for the project, set when project loads. Exporters will also
use this icon as a fallback if necessary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/macos_native_icon}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/config/macos_native_icon** = `""`
`🔗<class_ProjectSettings_property_application/config/macos_native_icon>`{.interpreted-text
role="ref"}

Icon set in `.icns` format used on macOS to set the game\'s icon. This
is done automatically on start by calling
`DisplayServer.set_native_icon()<class_DisplayServer_method_set_native_icon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/config/name** = `""`
`🔗<class_ProjectSettings_property_application/config/name>`{.interpreted-text
role="ref"}

The project\'s name. It is used both by the Project Manager and by
exporters. The project name can be translated by translating its value
in localization files. The window title will be set to match the project
name automatically on startup.

\*\*Note:\*\* Changing this value will also change the user data
folder\'s path if
`application/config/use_custom_user_dir<class_ProjectSettings_property_application/config/use_custom_user_dir>`{.interpreted-text
role="ref"} is `false`. After renaming the project, you will no longer
be able to access existing data in `user://` unless you rename the old
folder to match the new project name. See
`Data paths <../tutorials/io/data_paths>`{.interpreted-text role="doc"}
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/name_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**application/config/name_localized** = `{}`
`🔗<class_ProjectSettings_property_application/config/name_localized>`{.interpreted-text
role="ref"}

Translations of the project\'s name. This setting is used by OS tools to
translate application name on Android, iOS and macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/project_settings_override}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/config/project_settings_override** = `""`
`🔗<class_ProjectSettings_property_application/config/project_settings_override>`{.interpreted-text
role="ref"}

Specifies a file to override project settings. For example:
`user://custom_settings.cfg`. See \"Overriding\" in the
**ProjectSettings** class description at the top for more information.

\*\*Note:\*\* Regardless of this setting\'s value, `res://override.cfg`
will still be read to override the project settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/quit_on_go_back}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/config/quit_on_go_back** = `true`
`🔗<class_ProjectSettings_property_application/config/quit_on_go_back>`{.interpreted-text
role="ref"}

If `true`, the application quits automatically when navigating back
(e.g. using the system \"Back\" button on Android).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/use_custom_user_dir}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/config/use_custom_user_dir** = `false`
`🔗<class_ProjectSettings_property_application/config/use_custom_user_dir>`{.interpreted-text
role="ref"}

If `true`, the project will save user data to its own user directory. If
`application/config/custom_user_dir_name<class_ProjectSettings_property_application/config/custom_user_dir_name>`{.interpreted-text
role="ref"} is empty, `<OS user data directory>/<project name>`
directory will be used. If `false`, the project will save user data to
`<OS user data directory>/Godot/app_userdata/<project name>`.

See also [File paths in Godot
projects](../tutorials/io/data_paths.html#accessing-persistent-user-data-user).
This setting is only effective on desktop platforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/use_hidden_project_data_directory}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/config/use_hidden_project_data_directory** = `true`
`🔗<class_ProjectSettings_property_application/config/use_hidden_project_data_directory>`{.interpreted-text
role="ref"}

If `true`, the project will use a hidden directory (`.godot`) for
storing project-specific data (metadata, shader cache, etc.).

If `false`, a non-hidden directory (`godot`) will be used instead.

\*\*Note:\*\* Restart the application after changing this setting.

\*\*Note:\*\* Changing this value can help on platforms or with
third-party tools where hidden directory patterns are disallowed. Only
modify this setting if you know that your environment requires it, as
changing the default can impact compatibility with some external tools
or plugins which expect the default `.godot` folder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/version}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/config/version** = `""`
`🔗<class_ProjectSettings_property_application/config/version>`{.interpreted-text
role="ref"}

The project\'s human-readable version identifier. This is used by
exporters if the version identifier isn\'t overridden there. If
`application/config/version<class_ProjectSettings_property_application/config/version>`{.interpreted-text
role="ref"} is an empty string and the version identifier isn\'t
overridden in an exporter, the exporter will use `1.0.0` as a version
identifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/config/windows_native_icon}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/config/windows_native_icon** = `""`
`🔗<class_ProjectSettings_property_application/config/windows_native_icon>`{.interpreted-text
role="ref"}

Icon set in `.ico` format used on Windows to set the game\'s icon. This
is done automatically on start by calling
`DisplayServer.set_native_icon()<class_DisplayServer_method_set_native_icon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/delta_smoothing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/run/delta_smoothing** = `true`
`🔗<class_ProjectSettings_property_application/run/delta_smoothing>`{.interpreted-text
role="ref"}

Time samples for frame deltas are subject to random variation introduced
by the platform, even when frames are displayed at regular intervals
thanks to V-Sync. This can lead to jitter. Delta smoothing can often
give a better result by filtering the input deltas to correct for minor
fluctuations from the refresh rate.

\*\*Note:\*\* Delta smoothing is only attempted when
`display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>`{.interpreted-text
role="ref"} is set to `enabled`, as it does not work well without
V-Sync.

It may take several seconds at a stable frame rate before the smoothing
is initially activated. It will only be active on machines where
performance is adequate to render frames at the refresh rate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/disable_stderr}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/run/disable_stderr** = `false`
`🔗<class_ProjectSettings_property_application/run/disable_stderr>`{.interpreted-text
role="ref"}

If `true`, disables printing to standard error. If `true`, this also
hides error and warning messages printed by
`@GlobalScope.push_error()<class_@GlobalScope_method_push_error>`{.interpreted-text
role="ref"} and
`@GlobalScope.push_warning()<class_@GlobalScope_method_push_warning>`{.interpreted-text
role="ref"}. See also
`application/run/disable_stdout<class_ProjectSettings_property_application/run/disable_stdout>`{.interpreted-text
role="ref"}.

Changes to this setting will only be applied upon restarting the
application. To control this at runtime, use
`Engine.print_error_messages<class_Engine_property_print_error_messages>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/disable_stdout}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/run/disable_stdout** = `false`
`🔗<class_ProjectSettings_property_application/run/disable_stdout>`{.interpreted-text
role="ref"}

If `true`, disables printing to standard output. This is equivalent to
starting the editor or project with the `--quiet`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}. See also
`application/run/disable_stderr<class_ProjectSettings_property_application/run/disable_stderr>`{.interpreted-text
role="ref"}.

Changes to this setting will only be applied upon restarting the
application. To control this at runtime, use
`Engine.print_to_stdout<class_Engine_property_print_to_stdout>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/enable_alt_space_menu}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/run/enable_alt_space_menu** = `false`
`🔗<class_ProjectSettings_property_application/run/enable_alt_space_menu>`{.interpreted-text
role="ref"}

If `true`, allows the `Alt + Space`{.interpreted-text role="kbd"} keys
to display the window menu. This menu allows the user to perform various
window management operations such as moving, resizing, or minimizing the
window.

\*\*Note:\*\* When the menu is displayed, project execution will pause
until the menu is *fully* closed due to Windows behavior. Consider this
when enabling this setting in a networked multiplayer game. The menu is
only considered fully closed when an option is selected, when the user
clicks outside, or when `Escape`{.interpreted-text role="kbd"} is
pressed after bringing up the window menu *and* another key is pressed
afterwards.

\*\*Note:\*\* This setting is implemented only on Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/flush_stdout_on_print}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/run/flush_stdout_on_print** = `false`
`🔗<class_ProjectSettings_property_application/run/flush_stdout_on_print>`{.interpreted-text
role="ref"}

If `true`, flushes the standard output stream every time a line is
printed. This affects both terminal logging and file logging.

When running a project, this setting must be enabled if you want logs to
be collected by service managers such as systemd/journalctl. This
setting is disabled by default on release builds, since flushing on
every printed line will negatively affect performance if lots of lines
are printed in a rapid succession. Also, if this setting is enabled,
logged files will still be written successfully if the application
crashes or is otherwise killed by the user (without being closed
\"normally\").

\*\*Note:\*\* Regardless of this setting, the standard error stream
(`stderr`) is always flushed when a line is printed to it.

Changes to this setting will only be applied upon restarting the
application.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/flush_stdout_on_print.debug}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/run/flush_stdout_on_print.debug** = `true`
`🔗<class_ProjectSettings_property_application/run/flush_stdout_on_print.debug>`{.interpreted-text
role="ref"}

Debug build override for
`application/run/flush_stdout_on_print<class_ProjectSettings_property_application/run/flush_stdout_on_print>`{.interpreted-text
role="ref"}, as performance is less important during debugging.

Changes to this setting will only be applied upon restarting the
application.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/frame_delay_msec}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/run/frame_delay_msec** = `0`
`🔗<class_ProjectSettings_property_application/run/frame_delay_msec>`{.interpreted-text
role="ref"}

Forces a *constant* delay between frames in the main loop (in
milliseconds). In most situations,
`application/run/max_fps<class_ProjectSettings_property_application/run/max_fps>`{.interpreted-text
role="ref"} should be preferred as an FPS limiter as it\'s more precise.

This setting can be overridden using the `--frame-delay <ms;>` command
line argument.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/load_shell_environment}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/run/load_shell_environment** = `false`
`🔗<class_ProjectSettings_property_application/run/load_shell_environment>`{.interpreted-text
role="ref"}

If `true`, loads the default shell and copies environment variables set
by the shell startup scripts to the app environment.

\*\*Note:\*\* This setting is implemented on macOS for non-sandboxed
applications only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/low_processor_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/run/low_processor_mode** = `false`
`🔗<class_ProjectSettings_property_application/run/low_processor_mode>`{.interpreted-text
role="ref"}

If `true`, enables low-processor usage mode. When enabled, the engine
takes longer to redraw, but only redraws the screen if necessary. This
may lower power consumption, and is intended for editors or mobile
applications. For most games, because the screen needs to be redrawn
every frame, it is recommended to keep this setting disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/low_processor_mode_sleep_usec}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/run/low_processor_mode_sleep_usec** = `6900`
`🔗<class_ProjectSettings_property_application/run/low_processor_mode_sleep_usec>`{.interpreted-text
role="ref"}

Amount of sleeping between frames when the low-processor usage mode is
enabled (in microseconds). Higher values will result in lower CPU usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/main_loop_type}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/run/main_loop_type** = `"SceneTree"`
`🔗<class_ProjectSettings_property_application/run/main_loop_type>`{.interpreted-text
role="ref"}

The name of the type implementing the engine\'s main loop.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/main_scene}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/run/main_scene** = `""`
`🔗<class_ProjectSettings_property_application/run/main_scene>`{.interpreted-text
role="ref"}

Path to the main scene file that will be loaded when the project runs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/max_fps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/run/max_fps** = `0`
`🔗<class_ProjectSettings_property_application/run/max_fps>`{.interpreted-text
role="ref"}

Maximum number of frames per second allowed. A value of `0` means \"no
limit\". The actual number of frames per second may still be below this
value if the CPU or GPU cannot keep up with the project logic and
rendering.

Limiting the FPS can be useful to reduce system power consumption, which
reduces heat and noise emissions (and improves battery life on mobile
devices).

If
`display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>`{.interpreted-text
role="ref"} is set to `Enabled` or `Adaptive`, it takes precedence and
the forced FPS number cannot exceed the monitor\'s refresh rate.

If
`display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>`{.interpreted-text
role="ref"} is `Enabled`, on monitors with variable refresh rate enabled
(G-Sync/FreeSync), using an FPS limit a few frames lower than the
monitor\'s refresh rate will [reduce input lag while avoiding
tearing](https://blurbusters.com/howto-low-lag-vsync-on/).

If
`display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>`{.interpreted-text
role="ref"} is `Disabled`, limiting the FPS to a high value that can be
consistently reached on the system can reduce input lag compared to an
uncapped framerate. Since this works by ensuring the GPU load is lower
than 100%, this latency reduction is only effective in GPU-bottlenecked
scenarios, not CPU-bottlenecked scenarios.

See also
`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"}.

This setting can be overridden using the `--max-fps <fps>` command line
argument (including with a value of `0` for unlimited framerate).

\*\*Note:\*\* This property is only read when the project starts. To
change the rendering FPS cap at runtime, set
`Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_application/run/print_header}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/run/print_header** = `true`
`🔗<class_ProjectSettings_property_application/run/print_header>`{.interpreted-text
role="ref"}

If `true`, the engine header is printed in the console on startup. This
header describes the current version of the engine, as well as the
renderer being used. This behavior can also be disabled on the command
line with the `--no-header` option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/buses/channel_disable_threshold_db}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**audio/buses/channel_disable_threshold_db** = `-60.0`
`🔗<class_ProjectSettings_property_audio/buses/channel_disable_threshold_db>`{.interpreted-text
role="ref"}

Audio buses will disable automatically when sound goes below a given dB
threshold for a given time. This saves CPU as effects assigned to that
bus will no longer do any processing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/buses/channel_disable_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**audio/buses/channel_disable_time** = `2.0`
`🔗<class_ProjectSettings_property_audio/buses/channel_disable_time>`{.interpreted-text
role="ref"}

Audio buses will disable automatically when sound goes below a given dB
threshold for a given time. This saves CPU as effects assigned to that
bus will no longer do any processing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/buses/default_bus_layout}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**audio/buses/default_bus_layout** = `"res://default_bus_layout.tres"`
`🔗<class_ProjectSettings_property_audio/buses/default_bus_layout>`{.interpreted-text
role="ref"}

Default `AudioBusLayout<class_AudioBusLayout>`{.interpreted-text
role="ref"} resource file to use in the project, unless overridden by
the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/driver/driver}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**audio/driver/driver**
`🔗<class_ProjectSettings_property_audio/driver/driver>`{.interpreted-text
role="ref"}

Specifies the audio driver to use. This setting is platform-dependent as
each platform supports different audio drivers. If left empty, the
default audio driver will be used.

The `Dummy` audio driver disables all audio playback and recording,
which is useful for non-game applications as it reduces CPU usage. It
also prevents the engine from appearing as an application playing audio
in the OS\' audio mixer.

To query the value that is being used at run-time (which may be
overridden by command-line arguments or headless mode), use
`AudioServer.get_driver_name()<class_AudioServer_method_get_driver_name>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The driver in use can be overridden at runtime via the
`--audio-driver`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/driver/enable_input}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**audio/driver/enable_input** = `false`
`🔗<class_ProjectSettings_property_audio/driver/enable_input>`{.interpreted-text
role="ref"}

If `true`, microphone input will be allowed. This requires appropriate
permissions to be set when exporting to Android or iOS.

\*\*Note:\*\* If the operating system blocks access to audio input
devices (due to the user\'s privacy settings), audio capture will only
return silence. On Windows, make sure that apps are allowed to access
the microphone in the OS\' privacy settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/driver/mix_rate}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **audio/driver/mix_rate**
= `44100`
`🔗<class_ProjectSettings_property_audio/driver/mix_rate>`{.interpreted-text
role="ref"}

Target mixing rate used for audio (in Hz). In general, it\'s better to
not touch this and leave it to the host operating system.

\*\*Note:\*\* On iOS and macOS, mixing rate is determined by audio
driver, this value is ignored.

\*\*Note:\*\* Input and output mixing rates might be different. Use
`AudioServer.get_mix_rate()<class_AudioServer_method_get_mix_rate>`{.interpreted-text
role="ref"} and
`AudioServer.get_input_mix_rate()<class_AudioServer_method_get_input_mix_rate>`{.interpreted-text
role="ref"} to get actual values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/driver/mix_rate.web}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**audio/driver/mix_rate.web** = `0`
`🔗<class_ProjectSettings_property_audio/driver/mix_rate.web>`{.interpreted-text
role="ref"}

Safer override for
`audio/driver/mix_rate<class_ProjectSettings_property_audio/driver/mix_rate>`{.interpreted-text
role="ref"} in the Web platform. Here `0` means \"let the browser
choose\" (since some browsers do not like forcing the mix rate).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/driver/output_latency}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**audio/driver/output_latency** = `15`
`🔗<class_ProjectSettings_property_audio/driver/output_latency>`{.interpreted-text
role="ref"}

Specifies the preferred output latency in milliseconds for audio. Lower
values will result in lower audio latency at the cost of increased CPU
usage. Low values may result in audible crackling on slower hardware.

Audio output latency may be constrained by the host operating system and
audio hardware drivers. If the host can not provide the specified audio
output latency then Godot will attempt to use the nearest latency
allowed by the host. As such you should always use
`AudioServer.get_output_latency()<class_AudioServer_method_get_output_latency>`{.interpreted-text
role="ref"} to determine the actual audio output latency.

Audio output latency can be overridden using the
`--audio-output-latency <ms>` command line argument.

\*\*Note:\*\* This setting is ignored on Android.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/driver/output_latency.web}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**audio/driver/output_latency.web** = `50`
`🔗<class_ProjectSettings_property_audio/driver/output_latency.web>`{.interpreted-text
role="ref"}

Safer override for
`audio/driver/output_latency<class_ProjectSettings_property_audio/driver/output_latency>`{.interpreted-text
role="ref"} in the Web platform, to avoid audio issues especially on
mobile devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/general/2d_panning_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**audio/general/2d_panning_strength** = `0.5`
`🔗<class_ProjectSettings_property_audio/general/2d_panning_strength>`{.interpreted-text
role="ref"}

The base strength of the panning effect for all
`AudioStreamPlayer2D<class_AudioStreamPlayer2D>`{.interpreted-text
role="ref"} nodes. The panning strength can be further scaled on each
Node using
`AudioStreamPlayer2D.panning_strength<class_AudioStreamPlayer2D_property_panning_strength>`{.interpreted-text
role="ref"}. A value of `0.0` disables stereo panning entirely, leaving
only volume attenuation in place. A value of `1.0` completely mutes one
of the channels if the sound is located exactly to the left (or right)
of the listener.

The default value of `0.5` is tuned for headphones. When using speakers,
you may find lower values to sound better as speakers have a lower
stereo separation compared to headphones.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/general/3d_panning_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**audio/general/3d_panning_strength** = `0.5`
`🔗<class_ProjectSettings_property_audio/general/3d_panning_strength>`{.interpreted-text
role="ref"}

The base strength of the panning effect for all
`AudioStreamPlayer3D<class_AudioStreamPlayer3D>`{.interpreted-text
role="ref"} nodes. The panning strength can be further scaled on each
Node using
`AudioStreamPlayer3D.panning_strength<class_AudioStreamPlayer3D_property_panning_strength>`{.interpreted-text
role="ref"}. A value of `0.0` disables stereo panning entirely, leaving
only volume attenuation in place. A value of `1.0` completely mutes one
of the channels if the sound is located exactly to the left (or right)
of the listener.

The default value of `0.5` is tuned for headphones which means that the
opposite side channel goes no lower than 50% of the volume of the
nearside channel. You may find that you can set this value higher for
speakers to have the same effect since both ears can hear from each
speaker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/general/default_playback_type}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**audio/general/default_playback_type** = `0`
`🔗<class_ProjectSettings_property_audio/general/default_playback_type>`{.interpreted-text
role="ref"}

**Experimental:** This property may be changed or removed in future
versions.

Specifies the default playback type of the platform.

The default value is set to **Stream**, as most platforms have no issues
mixing streams.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/general/default_playback_type.web}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**audio/general/default_playback_type.web** = `1`
`🔗<class_ProjectSettings_property_audio/general/default_playback_type.web>`{.interpreted-text
role="ref"}

**Experimental:** This property may be changed or removed in future
versions.

Specifies the default playback type of the Web platform.

The default value is set to **Sample** as the Web platform is not suited
to mix audio streams outside of the Web Audio API, especially when
exporting a single-threaded game. **Sample** allows for lower latency on
the web platform at the cost of flexibility
(`AudioEffect<class_AudioEffect>`{.interpreted-text role="ref"}s are not
supported).

\*\*Warning:\*\* Forcing **Stream** on the Web platform may cause high
audio latency and crackling, especially when exporting a multi-threaded
game.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/general/ios/mix_with_others}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**audio/general/ios/mix_with_others** = `false`
`🔗<class_ProjectSettings_property_audio/general/ios/mix_with_others>`{.interpreted-text
role="ref"}

Sets the
[mixWithOthers](https://developer.apple.com/documentation/avfaudio/avaudiosession/categoryoptions/1616611-mixwithothers)
option for the AVAudioSession on iOS. This will override the mix
behavior, if the category is set to `Play and Record`, `Playback`, or
`Multi Route`.

`Ambient` always has this set per default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/general/ios/session_category}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**audio/general/ios/session_category** = `0`
`🔗<class_ProjectSettings_property_audio/general/ios/session_category>`{.interpreted-text
role="ref"}

Sets the
[AVAudioSessionCategory](https://developer.apple.com/documentation/avfaudio/avaudiosessioncategory)
on iOS. Use the `Playback` category to get sound output, even if the
phone is in silent mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/general/text_to_speech}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**audio/general/text_to_speech** = `false`
`🔗<class_ProjectSettings_property_audio/general/text_to_speech>`{.interpreted-text
role="ref"}

If `true`, text-to-speech support is enabled on startup, otherwise it is
enabled first time TTS method is used, see
`DisplayServer.tts_get_voices()<class_DisplayServer_method_tts_get_voices>`{.interpreted-text
role="ref"} and
`DisplayServer.tts_speak()<class_DisplayServer_method_tts_speak>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Enabling TTS can cause addition idle CPU usage and
interfere with the sleep mode, so consider disabling it if TTS is not
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_audio/video/video_delay_compensation_ms}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**audio/video/video_delay_compensation_ms** = `0`
`🔗<class_ProjectSettings_property_audio/video/video_delay_compensation_ms>`{.interpreted-text
role="ref"}

Setting to hardcode audio delay when playing video. Best to leave this
unchanged unless you know what you are doing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_collada/use_ambient}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collada/use_ambient**
= `false`
`🔗<class_ProjectSettings_property_collada/use_ambient>`{.interpreted-text
role="ref"}

If `true`, ambient lights will be imported from COLLADA models as
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}. If `false`, ambient lights will be ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_compression/formats/gzip/compression_level}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**compression/formats/gzip/compression_level** = `-1`
`🔗<class_ProjectSettings_property_compression/formats/gzip/compression_level>`{.interpreted-text
role="ref"}

The default compression level for gzip. Affects compressed scenes and
resources. Higher levels result in smaller files at the cost of
compression speed. Decompression speed is mostly unaffected by the
compression level. `-1` uses the default gzip compression level, which
is identical to `6` but could change in the future due to underlying
zlib updates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_compression/formats/zlib/compression_level}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**compression/formats/zlib/compression_level** = `-1`
`🔗<class_ProjectSettings_property_compression/formats/zlib/compression_level>`{.interpreted-text
role="ref"}

The default compression level for Zlib. Affects compressed scenes and
resources. Higher levels result in smaller files at the cost of
compression speed. Decompression speed is mostly unaffected by the
compression level. `-1` uses the default gzip compression level, which
is identical to `6` but could change in the future due to underlying
zlib updates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_compression/formats/zstd/compression_level}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**compression/formats/zstd/compression_level** = `3`
`🔗<class_ProjectSettings_property_compression/formats/zstd/compression_level>`{.interpreted-text
role="ref"}

The default compression level for Zstandard. Affects compressed scenes
and resources. Higher levels result in smaller files at the cost of
compression speed. Decompression speed is mostly unaffected by the
compression level.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_compression/formats/zstd/long_distance_matching}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**compression/formats/zstd/long_distance_matching** = `false`
`🔗<class_ProjectSettings_property_compression/formats/zstd/long_distance_matching>`{.interpreted-text
role="ref"}

Enables [long-distance
matching](https://github.com/facebook/zstd/releases/tag/v1.3.2) in
Zstandard.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_compression/formats/zstd/window_log_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**compression/formats/zstd/window_log_size** = `27`
`🔗<class_ProjectSettings_property_compression/formats/zstd/window_log_size>`{.interpreted-text
role="ref"}

Largest size limit (in power of 2) allowed when compressing using
long-distance matching with Zstandard. Higher values can result in
better compression, but will require more memory when compressing and
decompressing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/canvas_items/debug_redraw_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/canvas_items/debug_redraw_color** = `Color(1, 0.2, 0.2, 0.5)`
`🔗<class_ProjectSettings_property_debug/canvas_items/debug_redraw_color>`{.interpreted-text
role="ref"}

If canvas item redraw debugging is active, this color will be flashed on
canvas items when they redraw.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/canvas_items/debug_redraw_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**debug/canvas_items/debug_redraw_time** = `1.0`
`🔗<class_ProjectSettings_property_debug/canvas_items/debug_redraw_time>`{.interpreted-text
role="ref"}

If canvas item redraw debugging is active, this will be the time the
flash will last each time they redraw.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/file_logging/enable_file_logging}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/file_logging/enable_file_logging** = `false`
`🔗<class_ProjectSettings_property_debug/file_logging/enable_file_logging>`{.interpreted-text
role="ref"}

If `true`, logs all output and error messages to files. See also
`debug/file_logging/log_path<class_ProjectSettings_property_debug/file_logging/log_path>`{.interpreted-text
role="ref"},
`debug/file_logging/max_log_files<class_ProjectSettings_property_debug/file_logging/max_log_files>`{.interpreted-text
role="ref"}, and
`application/run/flush_stdout_on_print<class_ProjectSettings_property_application/run/flush_stdout_on_print>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/file_logging/enable_file_logging.pc}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/file_logging/enable_file_logging.pc** = `true`
`🔗<class_ProjectSettings_property_debug/file_logging/enable_file_logging.pc>`{.interpreted-text
role="ref"}

Desktop override for
`debug/file_logging/enable_file_logging<class_ProjectSettings_property_debug/file_logging/enable_file_logging>`{.interpreted-text
role="ref"}, as log files are not readily accessible on mobile/Web
platforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/file_logging/log_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**debug/file_logging/log_path** = `"user://logs/godot.log"`
`🔗<class_ProjectSettings_property_debug/file_logging/log_path>`{.interpreted-text
role="ref"}

Path at which to store log files for the project. Using a path under
`user://` is recommended.

This can be specified manually on the command line using the
`--log-file <file>`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}. If this command line argument is specified, log rotation is
automatically disabled (see
`debug/file_logging/max_log_files<class_ProjectSettings_property_debug/file_logging/max_log_files>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/file_logging/max_log_files}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/file_logging/max_log_files** = `5`
`🔗<class_ProjectSettings_property_debug/file_logging/max_log_files>`{.interpreted-text
role="ref"}

Specifies the maximum number of log files allowed (used for rotation).
Set to `1` to disable log file rotation.

If the `--log-file <file>`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"} is used, log rotation is always disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/assert_always_false}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/assert_always_false** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/assert_always_false>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when an `assert` call always evaluates to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/assert_always_true}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/assert_always_true** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/assert_always_true>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when an `assert` call always evaluates to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/confusable_capture_reassignment}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/confusable_capture_reassignment** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/confusable_capture_reassignment>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a local variable captured by a lambda is reassigned,
since this does not modify the outer local variable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/confusable_identifier}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/confusable_identifier** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/confusable_identifier>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when an identifier contains characters that can be confused
with something else, like when mixing different alphabets.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/confusable_local_declaration}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/confusable_local_declaration** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/confusable_local_declaration>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when an identifier declared in the nested block has the
same name as an identifier declared below in the parent block.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/confusable_local_usage}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/confusable_local_usage** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/confusable_local_usage>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when an identifier that will be shadowed below in the block
is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/deprecated_keyword}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/deprecated_keyword** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/deprecated_keyword>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when deprecated keywords are used.

\*\*Note:\*\* There are currently no deprecated keywords, so this
warning is never produced.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/empty_file}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/empty_file** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/empty_file>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when an empty file is parsed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/enable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/enable** = `true`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/enable>`{.interpreted-text
role="ref"}

If `true`, enables specific GDScript warnings (see
`debug/gdscript/warnings/*` settings). If `false`, disables all GDScript
warnings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/enum_variable_without_default}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/enum_variable_without_default** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/enum_variable_without_default>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a variable has an enum type but no explicit default
value, but only if the enum does not contain `0` as a valid value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/exclude_addons}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/exclude_addons** = `true`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/exclude_addons>`{.interpreted-text
role="ref"}

If `true`, scripts in the `res://addons` folder will not generate
warnings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/get_node_default_without_onready}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/get_node_default_without_onready** = `2`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/get_node_default_without_onready>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when
`Node.get_node()<class_Node_method_get_node>`{.interpreted-text
role="ref"} (or the shorthand `$`) is used as default value of a class
variable without the `@onready` annotation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/incompatible_ternary}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/incompatible_ternary** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/incompatible_ternary>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a ternary operator may emit values with incompatible
types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/inference_on_variant}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/inference_on_variant** = `2`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/inference_on_variant>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a static inferred type uses a
`Variant<class_Variant>`{.interpreted-text role="ref"} as initial value,
which makes the static type to also be Variant.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/inferred_declaration}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/inferred_declaration** = `0`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/inferred_declaration>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a variable, constant, or parameter has an implicitly
inferred static type.

\*\*Note:\*\* This warning is recommended *in addition* to
`debug/gdscript/warnings/untyped_declaration<class_ProjectSettings_property_debug/gdscript/warnings/untyped_declaration>`{.interpreted-text
role="ref"} if you want to always specify the type explicitly. Having
`INFERRED_DECLARATION` warning level higher than `UNTYPED_DECLARATION`
warning level makes little sense and is not recommended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/int_as_enum_without_cast}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/int_as_enum_without_cast** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/int_as_enum_without_cast>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when trying to use an integer as an enum without an
explicit cast.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/int_as_enum_without_match}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/int_as_enum_without_match** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/int_as_enum_without_match>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when trying to use an integer as an enum when there is no
matching enum member for that numeric value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/integer_division}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/integer_division** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/integer_division>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when dividing an integer by another integer (the decimal
part will be discarded).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/missing_tool}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/missing_tool** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/missing_tool>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when the base class script has the `@tool` annotation, but
the current class script does not have it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/narrowing_conversion}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/narrowing_conversion** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/narrowing_conversion>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when passing a floating-point value to a function that
expects an integer (it will be converted and lose precision).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/native_method_override}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/native_method_override** = `2`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/native_method_override>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a method in the script overrides a native method,
because it may not behave as expected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/onready_with_export}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/onready_with_export** = `2`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/onready_with_export>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when the `@onready` annotation is used together with the
`@export` annotation, since it may not behave as expected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/redundant_await}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/redundant_await** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/redundant_await>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a function that is not a coroutine is called with
await.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/redundant_static_unload}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/redundant_static_unload** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/redundant_static_unload>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when the `@static_unload` annotation is used in a script
without any static variables.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/renamed_in_godot_4_hint}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/renamed_in_godot_4_hint** = `true`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/renamed_in_godot_4_hint>`{.interpreted-text
role="ref"}

When enabled, using a property, enum, or function that was renamed since
Godot 3 will produce a hint if an error occurs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/return_value_discarded}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/return_value_discarded** = `0`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/return_value_discarded>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when calling a function without using its return value (by
assigning it to a variable or using it as a function argument). These
return values are sometimes used to indicate possible errors using the
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/shadowed_global_identifier}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/shadowed_global_identifier** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/shadowed_global_identifier>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when defining a local or member variable, signal, or enum
that would have the same name as a built-in function or global class
name, thus shadowing it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/shadowed_variable}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/shadowed_variable** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/shadowed_variable>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a local variable or local constant shadows a member
declared in the current class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/shadowed_variable_base_class}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/shadowed_variable_base_class** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/shadowed_variable_base_class>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a local variable or local constant shadows a member
declared in a base class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/standalone_expression}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/standalone_expression** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/standalone_expression>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when calling an expression that may have no effect on the
surrounding code, such as writing `2 + 2` as a statement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/standalone_ternary}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/standalone_ternary** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/standalone_ternary>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when calling a ternary expression that may have no effect
on the surrounding code, such as writing `42 if active else 0` as a
statement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/static_called_on_instance}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/static_called_on_instance** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/static_called_on_instance>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when calling a static method from an instance of a class
instead of from the class directly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unassigned_variable}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unassigned_variable** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unassigned_variable>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when using a variable that wasn\'t previously assigned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unassigned_variable_op_assign}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unassigned_variable_op_assign** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unassigned_variable_op_assign>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when assigning a variable using an assignment operator like
`+=` if the variable wasn\'t previously assigned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unreachable_code}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unreachable_code** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unreachable_code>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when unreachable code is detected (such as after a `return`
statement that will always be executed).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unreachable_pattern}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unreachable_pattern** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unreachable_pattern>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when an unreachable `match` pattern is detected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unsafe_call_argument}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unsafe_call_argument** = `0`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unsafe_call_argument>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when using an expression whose type may not be compatible
with the function parameter expected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unsafe_cast}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unsafe_cast** = `0`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unsafe_cast>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a `Variant<class_Variant>`{.interpreted-text
role="ref"} value is cast to a non-Variant.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unsafe_method_access}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unsafe_method_access** = `0`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unsafe_method_access>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when calling a method whose presence is not guaranteed at
compile-time in the class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unsafe_property_access}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unsafe_property_access** = `0`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unsafe_property_access>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when accessing a property whose presence is not guaranteed
at compile-time in the class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unsafe_void_return}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unsafe_void_return** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unsafe_void_return>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when returning a call from a `void` function when such call
cannot be guaranteed to be also `void`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/untyped_declaration}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/untyped_declaration** = `0`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/untyped_declaration>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a variable or parameter has no static type, or if a
function has no static return type.

\*\*Note:\*\* This warning is recommended together with
`EditorSettings.text_editor/completion/add_type_hints<class_EditorSettings_property_text_editor/completion/add_type_hints>`{.interpreted-text
role="ref"} to help achieve type safety.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unused_local_constant}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unused_local_constant** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unused_local_constant>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a local constant is never used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unused_parameter}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unused_parameter** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unused_parameter>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a function parameter is never used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unused_private_class_variable}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unused_private_class_variable** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unused_private_class_variable>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a private member variable is never used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unused_signal}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unused_signal** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unused_signal>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a signal is declared but never explicitly used in the
class.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/gdscript/warnings/unused_variable}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/gdscript/warnings/unused_variable** = `1`
`🔗<class_ProjectSettings_property_debug/gdscript/warnings/unused_variable>`{.interpreted-text
role="ref"}

When set to `warn` or `error`, produces a warning or an error
respectively when a local variable is unused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/crash_handler/message}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**debug/settings/crash_handler/message** =
`"Please include this when reporting the bug to the project developer."`
`🔗<class_ProjectSettings_property_debug/settings/crash_handler/message>`{.interpreted-text
role="ref"}

Message to be displayed before the backtrace when the engine crashes. By
default, this message is only used in exported projects due to the
editor-only override applied to this setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/crash_handler/message.editor}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**debug/settings/crash_handler/message.editor** =
`"Please include this when reporting the bug on: https://github.com/godotengine/godot/issues"`
`🔗<class_ProjectSettings_property_debug/settings/crash_handler/message.editor>`{.interpreted-text
role="ref"}

Editor-only override for
`debug/settings/crash_handler/message<class_ProjectSettings_property_debug/settings/crash_handler/message>`{.interpreted-text
role="ref"}. Does not affect exported projects in debug or release mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/gdscript/always_track_call_stacks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/settings/gdscript/always_track_call_stacks** = `false`
`🔗<class_ProjectSettings_property_debug/settings/gdscript/always_track_call_stacks>`{.interpreted-text
role="ref"}

Whether GDScript call stacks will be tracked in release builds, thus
allowing
`Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`{.interpreted-text
role="ref"} to function.

\*\*Note:\*\* This setting has no effect on editor builds or debug
builds, where GDScript call stacks are tracked regardless.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/gdscript/always_track_local_variables}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/settings/gdscript/always_track_local_variables** = `false`
`🔗<class_ProjectSettings_property_debug/settings/gdscript/always_track_local_variables>`{.interpreted-text
role="ref"}

Whether GDScript local variables will be tracked in all builds,
including export builds, thus allowing
`Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`{.interpreted-text
role="ref"} to capture them when enabling its `include_variables`
parameter.

Enabling this comes at the cost of roughly 50 bytes of memory per local
variable, for every compiled class in the entire project, so can be
several MiB in larger projects.

\*\*Note:\*\* This setting has no effect when running the game from the
editor, where GDScript local variables are tracked regardless.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/gdscript/max_call_stack}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/settings/gdscript/max_call_stack** = `1024`
`🔗<class_ProjectSettings_property_debug/settings/gdscript/max_call_stack>`{.interpreted-text
role="ref"}

Maximum call stack allowed for debugging GDScript.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/physics_interpolation/enable_warnings}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/settings/physics_interpolation/enable_warnings** = `true`
`🔗<class_ProjectSettings_property_debug/settings/physics_interpolation/enable_warnings>`{.interpreted-text
role="ref"}

If `true`, enables warnings which can help pinpoint where nodes are
being incorrectly updated, which will result in incorrect interpolation
and visual glitches.

When a node is being interpolated, it is essential that the transform is
set during
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} (during a physics tick) rather than
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} (during a frame).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/profiler/max_functions}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/settings/profiler/max_functions** = `16384`
`🔗<class_ProjectSettings_property_debug/settings/profiler/max_functions>`{.interpreted-text
role="ref"}

Maximum number of functions per frame allowed when profiling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/profiler/max_timestamp_query_elements}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/settings/profiler/max_timestamp_query_elements** = `256`
`🔗<class_ProjectSettings_property_debug/settings/profiler/max_timestamp_query_elements>`{.interpreted-text
role="ref"}

Maximum number of timestamp query elements allowed per frame for visual
profiling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/stdout/print_fps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/settings/stdout/print_fps** = `false`
`🔗<class_ProjectSettings_property_debug/settings/stdout/print_fps>`{.interpreted-text
role="ref"}

Print frames per second to standard output every second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/stdout/print_gpu_profile}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/settings/stdout/print_gpu_profile** = `false`
`🔗<class_ProjectSettings_property_debug/settings/stdout/print_gpu_profile>`{.interpreted-text
role="ref"}

Print GPU profile information to standard output every second. This
includes how long each frame takes the GPU to render on average, broken
down into different steps of the render pipeline, such as CanvasItems,
shadows, glow, etc.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/settings/stdout/verbose_stdout}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/settings/stdout/verbose_stdout** = `false`
`🔗<class_ProjectSettings_property_debug/settings/stdout/verbose_stdout>`{.interpreted-text
role="ref"}

Print more information to standard output when running. It displays
information such as memory leaks, which scenes and resources are being
loaded, etc. This can also be enabled using the `--verbose` or `-v`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}, even on an exported project. See also
`OS.is_stdout_verbose()<class_OS_method_is_stdout_verbose>`{.interpreted-text
role="ref"} and
`@GlobalScope.print_verbose()<class_@GlobalScope_method_print_verbose>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/device_limit_exceeded}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/device_limit_exceeded** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/device_limit_exceeded>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning when the shader exceeds certain
device limits. Currently, the only device limit checked is the limit on
uniform buffer size. More device limits will be added in the future.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/enable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/enable** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/enable>`{.interpreted-text
role="ref"}

If `true`, enables specific shader warnings (see
`debug/shader_language/warnings/*` settings). If `false`, disables all
shader warnings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/float_comparison}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/float_comparison** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/float_comparison>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning when two floating-point numbers
are compared directly with the `==` operator or the `!=` operator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/formatting_error}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/formatting_error** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/formatting_error>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning upon encountering certain
formatting errors. Currently this only checks for empty statements. More
formatting errors may be added over time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/magic_position_write}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/magic_position_write** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/magic_position_write>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning when the shader contains
`POSITION = vec4(vertex,` as this was very common code written in Godot
4.2 and earlier that was paired with a QuadMesh to produce a full screen
post processes pass. With the switch to reversed z in 4.3, this trick no
longer works, as it implicitly relied on the `VERTEX.z` being 0.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/treat_warnings_as_errors}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/treat_warnings_as_errors** = `false`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/treat_warnings_as_errors>`{.interpreted-text
role="ref"}

When set to `true`, warnings are treated as errors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/unused_constant}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/unused_constant** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/unused_constant>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning when a constant is never used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/unused_function}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/unused_function** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/unused_function>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning when a function is never used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/unused_local_variable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/unused_local_variable** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/unused_local_variable>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning when a local variable is never
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/unused_struct}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/unused_struct** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/unused_struct>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning when a struct is never used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/unused_uniform}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/unused_uniform** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/unused_uniform>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning when a uniform is never used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shader_language/warnings/unused_varying}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shader_language/warnings/unused_varying** = `true`
`🔗<class_ProjectSettings_property_debug/shader_language/warnings/unused_varying>`{.interpreted-text
role="ref"}

When set to `true`, produces a warning when a varying is never used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/2d/agents_radius_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/2d/agents_radius_color** =
`Color(1, 1, 0, 0.25)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/2d/agents_radius_color>`{.interpreted-text
role="ref"}

Color of the avoidance agents radius, visible when \"Visible Avoidance\"
is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/2d/enable_agents_radius}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/2d/enable_agents_radius** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/2d/enable_agents_radius>`{.interpreted-text
role="ref"}

If enabled, displays avoidance agents radius when \"Visible Avoidance\"
is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/2d/enable_obstacles_radius}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/2d/enable_obstacles_radius** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/2d/enable_obstacles_radius>`{.interpreted-text
role="ref"}

If enabled, displays avoidance obstacles radius when \"Visible
Avoidance\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/2d/enable_obstacles_static}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/2d/enable_obstacles_static** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/2d/enable_obstacles_static>`{.interpreted-text
role="ref"}

If enabled, displays static avoidance obstacles when \"Visible
Avoidance\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_radius_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/2d/obstacles_radius_color** =
`Color(1, 0.5, 0, 0.25)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_radius_color>`{.interpreted-text
role="ref"}

Color of the avoidance obstacles radius, visible when \"Visible
Avoidance\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_static_edge_pushin_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/2d/obstacles_static_edge_pushin_color** =
`Color(1, 0, 0, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_static_edge_pushin_color>`{.interpreted-text
role="ref"}

Color of the static avoidance obstacles edges when their vertices are
winded in order to push agents in, visible when \"Visible Avoidance\" is
enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_static_edge_pushout_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/2d/obstacles_static_edge_pushout_color** =
`Color(1, 1, 0, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_static_edge_pushout_color>`{.interpreted-text
role="ref"}

Color of the static avoidance obstacles edges when their vertices are
winded in order to push agents out, visible when \"Visible Avoidance\"
is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_static_face_pushin_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/2d/obstacles_static_face_pushin_color** =
`Color(1, 0, 0, 0)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_static_face_pushin_color>`{.interpreted-text
role="ref"}

Color of the static avoidance obstacles faces when their vertices are
winded in order to push agents in, visible when \"Visible Avoidance\" is
enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_static_face_pushout_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/2d/obstacles_static_face_pushout_color** =
`Color(1, 1, 0, 0.5)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/2d/obstacles_static_face_pushout_color>`{.interpreted-text
role="ref"}

Color of the static avoidance obstacles faces when their vertices are
winded in order to push agents out, visible when \"Visible Avoidance\"
is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/3d/agents_radius_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/3d/agents_radius_color** =
`Color(1, 1, 0, 0.25)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/3d/agents_radius_color>`{.interpreted-text
role="ref"}

Color of the avoidance agents radius, visible when \"Visible Avoidance\"
is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/3d/enable_agents_radius}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/3d/enable_agents_radius** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/3d/enable_agents_radius>`{.interpreted-text
role="ref"}

If enabled, displays avoidance agents radius when \"Visible Avoidance\"
is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/3d/enable_obstacles_radius}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/3d/enable_obstacles_radius** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/3d/enable_obstacles_radius>`{.interpreted-text
role="ref"}

If enabled, displays avoidance obstacles radius when \"Visible
Avoidance\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/3d/enable_obstacles_static}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/3d/enable_obstacles_static** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/3d/enable_obstacles_static>`{.interpreted-text
role="ref"}

If enabled, displays static avoidance obstacles when \"Visible
Avoidance\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_radius_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/3d/obstacles_radius_color** =
`Color(1, 0.5, 0, 0.25)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_radius_color>`{.interpreted-text
role="ref"}

Color of the avoidance obstacles radius, visible when \"Visible
Avoidance\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_static_edge_pushin_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/3d/obstacles_static_edge_pushin_color** =
`Color(1, 0, 0, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_static_edge_pushin_color>`{.interpreted-text
role="ref"}

Color of the static avoidance obstacles edges when their vertices are
winded in order to push agents in, visible when \"Visible Avoidance\" is
enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_static_edge_pushout_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/3d/obstacles_static_edge_pushout_color** =
`Color(1, 1, 0, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_static_edge_pushout_color>`{.interpreted-text
role="ref"}

Color of the static avoidance obstacles edges when their vertices are
winded in order to push agents out, visible when \"Visible Avoidance\"
is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_static_face_pushin_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/3d/obstacles_static_face_pushin_color** =
`Color(1, 0, 0, 0)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_static_face_pushin_color>`{.interpreted-text
role="ref"}

Color of the static avoidance obstacles faces when their vertices are
winded in order to push agents in, visible when \"Visible Avoidance\" is
enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_static_face_pushout_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/avoidance/3d/obstacles_static_face_pushout_color** =
`Color(1, 1, 0, 0.5)`
`🔗<class_ProjectSettings_property_debug/shapes/avoidance/3d/obstacles_static_face_pushout_color>`{.interpreted-text
role="ref"}

Color of the static avoidance obstacles faces when their vertices are
winded in order to push agents out, visible when \"Visible Avoidance\"
is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/collision/contact_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/collision/contact_color** = `Color(1, 0.2, 0.1, 0.8)`
`🔗<class_ProjectSettings_property_debug/shapes/collision/contact_color>`{.interpreted-text
role="ref"}

Color of the contact points between collision shapes, visible when
\"Visible Collision Shapes\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/collision/draw_2d_outlines}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/collision/draw_2d_outlines** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/collision/draw_2d_outlines>`{.interpreted-text
role="ref"}

Sets whether 2D physics will display collision outlines in game when
\"Visible Collision Shapes\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/collision/max_contacts_displayed}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/shapes/collision/max_contacts_displayed** = `10000`
`🔗<class_ProjectSettings_property_debug/shapes/collision/max_contacts_displayed>`{.interpreted-text
role="ref"}

Maximum number of contact points between collision shapes to display
when \"Visible Collision Shapes\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/collision/shape_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/collision/shape_color** = `Color(0, 0.6, 0.7, 0.42)`
`🔗<class_ProjectSettings_property_debug/shapes/collision/shape_color>`{.interpreted-text
role="ref"}

Color of the collision shapes, visible when \"Visible Collision Shapes\"
is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/agent_path_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/agent_path_color** = `Color(1, 0, 0, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/agent_path_color>`{.interpreted-text
role="ref"}

Color to display enabled navigation agent paths when an agent has debug
enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/agent_path_point_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/agent_path_point_size** = `4.0`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/agent_path_point_size>`{.interpreted-text
role="ref"}

Rasterized size (pixel) used to render navigation agent path points when
an agent has debug enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/edge_connection_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/edge_connection_color** =
`Color(1, 0, 1, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/edge_connection_color>`{.interpreted-text
role="ref"}

Color to display edge connections between navigation regions, visible
when \"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/enable_agent_paths}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/enable_agent_paths** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/enable_agent_paths>`{.interpreted-text
role="ref"}

If enabled, displays navigation agent paths when an agent has debug
enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/enable_edge_connections}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/enable_edge_connections** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/enable_edge_connections>`{.interpreted-text
role="ref"}

If enabled, displays edge connections between navigation regions when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/enable_edge_lines}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/enable_edge_lines** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/enable_edge_lines>`{.interpreted-text
role="ref"}

If enabled, displays navigation mesh polygon edges when \"Visible
Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/enable_geometry_face_random_color}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/enable_geometry_face_random_color** =
`true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/enable_geometry_face_random_color>`{.interpreted-text
role="ref"}

If enabled, colorizes each navigation mesh polygon face with a random
color when \"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/enable_link_connections}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/enable_link_connections** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/enable_link_connections>`{.interpreted-text
role="ref"}

If enabled, displays navigation link connections when \"Visible
Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/geometry_edge_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/geometry_edge_color** =
`Color(0.5, 1, 1, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/geometry_edge_color>`{.interpreted-text
role="ref"}

Color to display enabled navigation mesh polygon edges, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/geometry_edge_disabled_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/geometry_edge_disabled_color** =
`Color(0.5, 0.5, 0.5, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/geometry_edge_disabled_color>`{.interpreted-text
role="ref"}

Color to display disabled navigation mesh polygon edges, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/geometry_face_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/geometry_face_color** =
`Color(0.5, 1, 1, 0.4)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/geometry_face_color>`{.interpreted-text
role="ref"}

Color to display enabled navigation mesh polygon faces, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/geometry_face_disabled_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/geometry_face_disabled_color** =
`Color(0.5, 0.5, 0.5, 0.4)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/geometry_face_disabled_color>`{.interpreted-text
role="ref"}

Color to display disabled navigation mesh polygon faces, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/link_connection_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/link_connection_color** =
`Color(1, 0.5, 1, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/link_connection_color>`{.interpreted-text
role="ref"}

Color to use to display navigation link connections, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/2d/link_connection_disabled_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/2d/link_connection_disabled_color** =
`Color(0.5, 0.5, 0.5, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/2d/link_connection_disabled_color>`{.interpreted-text
role="ref"}

Color to use to display disabled navigation link connections, visible
when \"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/agent_path_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/agent_path_color** = `Color(1, 0, 0, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/agent_path_color>`{.interpreted-text
role="ref"}

Color to display enabled navigation agent paths when an agent has debug
enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/agent_path_point_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/agent_path_point_size** = `4.0`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/agent_path_point_size>`{.interpreted-text
role="ref"}

Rasterized size (pixel) used to render navigation agent path points when
an agent has debug enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/edge_connection_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/edge_connection_color** =
`Color(1, 0, 1, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/edge_connection_color>`{.interpreted-text
role="ref"}

Color to display edge connections between navigation regions, visible
when \"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/enable_agent_paths}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/enable_agent_paths** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/enable_agent_paths>`{.interpreted-text
role="ref"}

If enabled, displays navigation agent paths when an agent has debug
enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/enable_agent_paths_xray}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/enable_agent_paths_xray** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/enable_agent_paths_xray>`{.interpreted-text
role="ref"}

If enabled, displays navigation agent paths through geometry when an
agent has debug enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/enable_edge_connections}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/enable_edge_connections** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/enable_edge_connections>`{.interpreted-text
role="ref"}

If enabled, displays edge connections between navigation regions when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/enable_edge_connections_xray}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/enable_edge_connections_xray** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/enable_edge_connections_xray>`{.interpreted-text
role="ref"}

If enabled, displays edge connections between navigation regions through
geometry when \"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/enable_edge_lines}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/enable_edge_lines** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/enable_edge_lines>`{.interpreted-text
role="ref"}

If enabled, displays navigation mesh polygon edges when \"Visible
Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/enable_edge_lines_xray}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/enable_edge_lines_xray** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/enable_edge_lines_xray>`{.interpreted-text
role="ref"}

If enabled, displays navigation mesh polygon edges through geometry when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/enable_geometry_face_random_color}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/enable_geometry_face_random_color** =
`true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/enable_geometry_face_random_color>`{.interpreted-text
role="ref"}

If enabled, colorizes each navigation mesh polygon face with a random
color when \"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/enable_link_connections}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/enable_link_connections** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/enable_link_connections>`{.interpreted-text
role="ref"}

If enabled, displays navigation link connections when \"Visible
Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/enable_link_connections_xray}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/enable_link_connections_xray** = `true`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/enable_link_connections_xray>`{.interpreted-text
role="ref"}

If enabled, displays navigation link connections through geometry when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/geometry_edge_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/geometry_edge_color** =
`Color(0.5, 1, 1, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/geometry_edge_color>`{.interpreted-text
role="ref"}

Color to display enabled navigation mesh polygon edges, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/geometry_edge_disabled_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/geometry_edge_disabled_color** =
`Color(0.5, 0.5, 0.5, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/geometry_edge_disabled_color>`{.interpreted-text
role="ref"}

Color to display disabled navigation mesh polygon edges, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/geometry_face_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/geometry_face_color** =
`Color(0.5, 1, 1, 0.4)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/geometry_face_color>`{.interpreted-text
role="ref"}

Color to display enabled navigation mesh polygon faces, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/geometry_face_disabled_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/geometry_face_disabled_color** =
`Color(0.5, 0.5, 0.5, 0.4)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/geometry_face_disabled_color>`{.interpreted-text
role="ref"}

Color to display disabled navigation mesh polygon faces, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/link_connection_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/link_connection_color** =
`Color(1, 0.5, 1, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/link_connection_color>`{.interpreted-text
role="ref"}

Color to use to display navigation link connections, visible when
\"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/navigation/3d/link_connection_disabled_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/navigation/3d/link_connection_disabled_color** =
`Color(0.5, 0.5, 0.5, 1)`
`🔗<class_ProjectSettings_property_debug/shapes/navigation/3d/link_connection_disabled_color>`{.interpreted-text
role="ref"}

Color to use to display disabled navigation link connections, visible
when \"Visible Navigation\" is enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/paths/geometry_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug/shapes/paths/geometry_color** = `Color(0.1, 1, 0.7, 0.4)`
`🔗<class_ProjectSettings_property_debug/shapes/paths/geometry_color>`{.interpreted-text
role="ref"}

Color of the curve path geometry, visible when \"Visible Paths\" is
enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_debug/shapes/paths/geometry_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**debug/shapes/paths/geometry_width** = `2.0`
`🔗<class_ProjectSettings_property_debug/shapes/paths/geometry_width>`{.interpreted-text
role="ref"}

Line width of the curve path geometry, visible when \"Visible Paths\" is
enabled in the Debug menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/display_server/driver}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/display_server/driver**
`🔗<class_ProjectSettings_property_display/display_server/driver>`{.interpreted-text
role="ref"}

Sets the driver to be used by the display server. This property can not
be edited directly, instead, set the driver using the platform-specific
overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/display_server/driver.android}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/display_server/driver.android**
`🔗<class_ProjectSettings_property_display/display_server/driver.android>`{.interpreted-text
role="ref"}

Android override for
`display/display_server/driver<class_ProjectSettings_property_display/display_server/driver>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/display_server/driver.ios}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/display_server/driver.ios**
`🔗<class_ProjectSettings_property_display/display_server/driver.ios>`{.interpreted-text
role="ref"}

iOS override for
`display/display_server/driver<class_ProjectSettings_property_display/display_server/driver>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/display_server/driver.linuxbsd}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/display_server/driver.linuxbsd**
`🔗<class_ProjectSettings_property_display/display_server/driver.linuxbsd>`{.interpreted-text
role="ref"}

LinuxBSD override for
`display/display_server/driver<class_ProjectSettings_property_display/display_server/driver>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/display_server/driver.macos}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/display_server/driver.macos**
`🔗<class_ProjectSettings_property_display/display_server/driver.macos>`{.interpreted-text
role="ref"}

MacOS override for
`display/display_server/driver<class_ProjectSettings_property_display/display_server/driver>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/display_server/driver.visionos}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/display_server/driver.visionos**
`🔗<class_ProjectSettings_property_display/display_server/driver.visionos>`{.interpreted-text
role="ref"}

visionOS override for
`display/display_server/driver<class_ProjectSettings_property_display/display_server/driver>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/display_server/driver.windows}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/display_server/driver.windows**
`🔗<class_ProjectSettings_property_display/display_server/driver.windows>`{.interpreted-text
role="ref"}

Windows override for
`display/display_server/driver<class_ProjectSettings_property_display/display_server/driver>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/mouse_cursor/custom_image}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/mouse_cursor/custom_image** = `""`
`🔗<class_ProjectSettings_property_display/mouse_cursor/custom_image>`{.interpreted-text
role="ref"}

Custom image for the mouse cursor (limited to 256×256).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/mouse_cursor/custom_image_hotspot}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**display/mouse_cursor/custom_image_hotspot** = `Vector2(0, 0)`
`🔗<class_ProjectSettings_property_display/mouse_cursor/custom_image_hotspot>`{.interpreted-text
role="ref"}

Hotspot for the custom mouse cursor image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/mouse_cursor/tooltip_position_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**display/mouse_cursor/tooltip_position_offset** = `Vector2(10, 10)`
`🔗<class_ProjectSettings_property_display/mouse_cursor/tooltip_position_offset>`{.interpreted-text
role="ref"}

Position offset for tooltips, relative to the mouse cursor\'s hotspot.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/dpi/allow_hidpi}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/dpi/allow_hidpi** = `true`
`🔗<class_ProjectSettings_property_display/window/dpi/allow_hidpi>`{.interpreted-text
role="ref"}

If `true`, allows HiDPI display on Windows, macOS, Android, iOS and Web.
If `false`, the platform\'s low-DPI fallback will be used on HiDPI
displays, which causes the window to be displayed in a blurry or
pixelated manner (and can cause various window management bugs).
Therefore, it is recommended to make your project scale to
`multiple resolutions <../tutorials/rendering/multiple_resolutions>`{.interpreted-text
role="doc"} instead of disabling this setting.

\*\*Note:\*\* This setting has no effect on Linux as DPI-awareness
fallbacks are not supported there.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/energy_saving/keep_screen_on}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/energy_saving/keep_screen_on** = `true`
`🔗<class_ProjectSettings_property_display/window/energy_saving/keep_screen_on>`{.interpreted-text
role="ref"}

If `true`, keeps the screen on (even in case of inactivity), so the
screensaver does not take over. Works on desktop and mobile platforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/frame_pacing/android/enable_frame_pacing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/frame_pacing/android/enable_frame_pacing** = `true`
`🔗<class_ProjectSettings_property_display/window/frame_pacing/android/enable_frame_pacing>`{.interpreted-text
role="ref"}

Enable Swappy for stable frame pacing on Android. Highly recommended.

\*\*Note:\*\* This option will be forced off when using OpenXR.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/frame_pacing/android/swappy_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/frame_pacing/android/swappy_mode** = `2`
`🔗<class_ProjectSettings_property_display/window/frame_pacing/android/swappy_mode>`{.interpreted-text
role="ref"}

Swappy mode to use. The options are:

- `pipeline_forced_on`: Try to honor
  `Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
  role="ref"}. Pipelining is always on. This is the same behavior as a
  desktop PC.
- `auto_fps_pipeline_forced_on`: Calculate the max FPS automatically.
  The actual max FPS will be between `0` and
  `Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
  role="ref"}. While this sounds convenient, beware that Swappy will
  often downgrade the max FPS until it finds a value that can be
  maintained. That means, if your game runs between 40fps and 60fps on a
  60hz screen, after some time Swappy will downgrade the max FPS so that
  the game renders at a perfect 30fps.
- `auto_fps_auto_pipeline`: Same as `auto_fps_pipeline_forced_on`, but
  if Swappy detects that rendering is very fast (for example it takes
  less than 8ms to render on a 60hz screen), Swappy will disable
  pipelining to minimize input latency. This is the default.

\*\*Note:\*\* If
`Engine.max_fps<class_Engine_property_max_fps>`{.interpreted-text
role="ref"} is `0`, the actual max FPS will be considered to be the
screen\'s refresh rate (often 60hz, 90hz, or 120hz, depending on device
model and OS settings).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/handheld/orientation}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/handheld/orientation** = `0`
`🔗<class_ProjectSettings_property_display/window/handheld/orientation>`{.interpreted-text
role="ref"}

The default screen orientation to use on mobile devices. See
`ScreenOrientation<enum_DisplayServer_ScreenOrientation>`{.interpreted-text
role="ref"} for possible values.

\*\*Note:\*\* When set to a portrait orientation, this project setting
does not flip the project resolution\'s width and height automatically.
Instead, you have to set
`display/window/size/viewport_width<class_ProjectSettings_property_display/window/size/viewport_width>`{.interpreted-text
role="ref"} and
`display/window/size/viewport_height<class_ProjectSettings_property_display/window/size/viewport_height>`{.interpreted-text
role="ref"} accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/ios/allow_high_refresh_rate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/ios/allow_high_refresh_rate** = `true`
`🔗<class_ProjectSettings_property_display/window/ios/allow_high_refresh_rate>`{.interpreted-text
role="ref"}

If `true`, iOS devices that support high refresh rate/\"ProMotion\" will
be allowed to render at up to 120 frames per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/ios/hide_home_indicator}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/ios/hide_home_indicator** = `true`
`🔗<class_ProjectSettings_property_display/window/ios/hide_home_indicator>`{.interpreted-text
role="ref"}

If `true`, the home indicator is hidden automatically. This only affects
iOS devices without a physical home button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/ios/hide_status_bar}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/ios/hide_status_bar** = `true`
`🔗<class_ProjectSettings_property_display/window/ios/hide_status_bar>`{.interpreted-text
role="ref"}

If `true`, the status bar is hidden while the app is running.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/ios/suppress_ui_gesture}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/ios/suppress_ui_gesture** = `true`
`🔗<class_ProjectSettings_property_display/window/ios/suppress_ui_gesture>`{.interpreted-text
role="ref"}

If `true`, it will require two swipes to access iOS UI that uses
gestures.

\*\*Note:\*\* This setting has no effect on the home indicator if
`hide_home_indicator` is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/per_pixel_transparency/allowed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/per_pixel_transparency/allowed** = `false`
`🔗<class_ProjectSettings_property_display/window/per_pixel_transparency/allowed>`{.interpreted-text
role="ref"}

If `true`, allows per-pixel transparency for the window background. This
affects performance, so leave it on `false` unless you need it. See also
`display/window/size/transparent<class_ProjectSettings_property_display/window/size/transparent>`{.interpreted-text
role="ref"} and
`rendering/viewport/transparent_background<class_ProjectSettings_property_rendering/viewport/transparent_background>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/always_on_top}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/size/always_on_top** = `false`
`🔗<class_ProjectSettings_property_display/window/size/always_on_top>`{.interpreted-text
role="ref"}

Forces the main window to be always on top.

\*\*Note:\*\* This setting is ignored on iOS, Android, and Web.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/borderless}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/size/borderless** = `false`
`🔗<class_ProjectSettings_property_display/window/size/borderless>`{.interpreted-text
role="ref"}

Forces the main window to be borderless.

\*\*Note:\*\* This setting is ignored on iOS, Android, and Web.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/extend_to_title}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/size/extend_to_title** = `false`
`🔗<class_ProjectSettings_property_display/window/size/extend_to_title>`{.interpreted-text
role="ref"}

Main window content is expanded to the full size of the window. Unlike a
borderless window, the frame is left intact and can be used to resize
the window, and the title bar is transparent, but has
minimize/maximize/close buttons.

\*\*Note:\*\* This setting is implemented only on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/initial_position}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**display/window/size/initial_position** = `Vector2i(0, 0)`
`🔗<class_ProjectSettings_property_display/window/size/initial_position>`{.interpreted-text
role="ref"}

Main window initial position (in virtual desktop coordinates), this
setting is used only if
`display/window/size/initial_position_type<class_ProjectSettings_property_display/window/size/initial_position_type>`{.interpreted-text
role="ref"} is set to \"Absolute\" (`0`).

\*\*Note:\*\* This setting only affects the exported project, or when
the project is run from the command line. In the editor, the value of
`EditorSettings.run/window_placement/rect_custom_position<class_EditorSettings_property_run/window_placement/rect_custom_position>`{.interpreted-text
role="ref"} is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/initial_position_type}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/size/initial_position_type** = `1`
`🔗<class_ProjectSettings_property_display/window/size/initial_position_type>`{.interpreted-text
role="ref"}

Main window initial position.

`0` - \"Absolute\",
`display/window/size/initial_position<class_ProjectSettings_property_display/window/size/initial_position>`{.interpreted-text
role="ref"} is used to set window position.

`1` - \"Primary Screen Center\".

`2` - \"Other Screen Center\",
`display/window/size/initial_screen<class_ProjectSettings_property_display/window/size/initial_screen>`{.interpreted-text
role="ref"} is used to set the screen.

\*\*Note:\*\* This setting only affects the exported project, or when
the project is run from the command line. In the editor, the value of
`EditorSettings.run/window_placement/rect<class_EditorSettings_property_run/window_placement/rect>`{.interpreted-text
role="ref"} is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/initial_screen}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/size/initial_screen** = `0`
`🔗<class_ProjectSettings_property_display/window/size/initial_screen>`{.interpreted-text
role="ref"}

Main window initial screen, this setting is used only if
`display/window/size/initial_position_type<class_ProjectSettings_property_display/window/size/initial_position_type>`{.interpreted-text
role="ref"} is set to \"Other Screen Center\" (`2`).

\*\*Note:\*\* This setting only affects the exported project, or when
the project is run from the command line. In the editor, the value of
`EditorSettings.run/window_placement/screen<class_EditorSettings_property_run/window_placement/screen>`{.interpreted-text
role="ref"} is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/maximize_disabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/size/maximize_disabled** = `false`
`🔗<class_ProjectSettings_property_display/window/size/maximize_disabled>`{.interpreted-text
role="ref"}

If `true`, the main window\'s maximize button is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/minimize_disabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/size/minimize_disabled** = `false`
`🔗<class_ProjectSettings_property_display/window/size/minimize_disabled>`{.interpreted-text
role="ref"}

If `true`, the main window\'s minimize button is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/size/mode** = `0`
`🔗<class_ProjectSettings_property_display/window/size/mode>`{.interpreted-text
role="ref"}

Main window mode. See
`WindowMode<enum_DisplayServer_WindowMode>`{.interpreted-text
role="ref"} for possible values and how each mode behaves.

\*\*Note:\*\* Game embedding is available only in the \"Windowed\" mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/no_focus}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/size/no_focus** = `false`
`🔗<class_ProjectSettings_property_display/window/size/no_focus>`{.interpreted-text
role="ref"}

Main window can\'t be focused. No-focus window will ignore all input,
except mouse clicks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/resizable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/size/resizable** = `true`
`🔗<class_ProjectSettings_property_display/window/size/resizable>`{.interpreted-text
role="ref"}

If `true`, allows the window to be resizable by default.

\*\*Note:\*\* This property is only read when the project starts. To
change whether the window is resizable at runtime, set
`Window.unresizable<class_Window_property_unresizable>`{.interpreted-text
role="ref"} instead on the root Window, which can be retrieved using
`get_viewport().get_window()`.
`Window.unresizable<class_Window_property_unresizable>`{.interpreted-text
role="ref"} takes the opposite value of this setting.

\*\*Note:\*\* Certain window managers can be configured to ignore the
non-resizable status of a window. Do not rely on this setting as a
guarantee that the window will *never* be resizable.

\*\*Note:\*\* This setting is ignored on iOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/sharp_corners}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/size/sharp_corners** = `false`
`🔗<class_ProjectSettings_property_display/window/size/sharp_corners>`{.interpreted-text
role="ref"}

If `true`, the main window uses sharp corners by default.

\*\*Note:\*\* This property is implemented only on Windows (11).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/transparent}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/size/transparent** = `false`
`🔗<class_ProjectSettings_property_display/window/size/transparent>`{.interpreted-text
role="ref"}

If `true`, enables a window manager hint that the main window background
*can* be transparent. This does not make the background actually
transparent. For the background to be transparent, the root viewport
must also be made transparent by enabling
`rendering/viewport/transparent_background<class_ProjectSettings_property_rendering/viewport/transparent_background>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* To use a transparent splash screen, set
`application/boot_splash/bg_color<class_ProjectSettings_property_application/boot_splash/bg_color>`{.interpreted-text
role="ref"} to `Color(0, 0, 0, 0)`.

\*\*Note:\*\* This setting has no effect if
`display/window/per_pixel_transparency/allowed<class_ProjectSettings_property_display/window/per_pixel_transparency/allowed>`{.interpreted-text
role="ref"} is set to `false`.

\*\*Note:\*\* This setting has no effect on Android as transparency is
controlled only via
`display/window/per_pixel_transparency/allowed<class_ProjectSettings_property_display/window/per_pixel_transparency/allowed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/viewport_height}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/size/viewport_height** = `648`
`🔗<class_ProjectSettings_property_display/window/size/viewport_height>`{.interpreted-text
role="ref"}

Sets the game\'s main viewport height. On desktop platforms, this is
also the initial window height, represented by an indigo-colored
rectangle in the 2D editor. Stretch mode settings also use this as a
reference when using the `canvas_items` or `viewport` stretch modes. See
also
`display/window/size/viewport_width<class_ProjectSettings_property_display/window/size/viewport_width>`{.interpreted-text
role="ref"},
`display/window/size/window_width_override<class_ProjectSettings_property_display/window/size/window_width_override>`{.interpreted-text
role="ref"} and
`display/window/size/window_height_override<class_ProjectSettings_property_display/window/size/window_height_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/viewport_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/size/viewport_width** = `1152`
`🔗<class_ProjectSettings_property_display/window/size/viewport_width>`{.interpreted-text
role="ref"}

Sets the game\'s main viewport width. On desktop platforms, this is also
the initial window width, represented by an indigo-colored rectangle in
the 2D editor. Stretch mode settings also use this as a reference when
using the `canvas_items` or `viewport` stretch modes. See also
`display/window/size/viewport_height<class_ProjectSettings_property_display/window/size/viewport_height>`{.interpreted-text
role="ref"},
`display/window/size/window_width_override<class_ProjectSettings_property_display/window/size/window_width_override>`{.interpreted-text
role="ref"} and
`display/window/size/window_height_override<class_ProjectSettings_property_display/window/size/window_height_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/window_height_override}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/size/window_height_override** = `0`
`🔗<class_ProjectSettings_property_display/window/size/window_height_override>`{.interpreted-text
role="ref"}

On desktop platforms, overrides the game\'s initial window height. See
also
`display/window/size/window_width_override<class_ProjectSettings_property_display/window/size/window_width_override>`{.interpreted-text
role="ref"},
`display/window/size/viewport_width<class_ProjectSettings_property_display/window/size/viewport_width>`{.interpreted-text
role="ref"} and
`display/window/size/viewport_height<class_ProjectSettings_property_display/window/size/viewport_height>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* By default, or when set to `0`, the initial window height
is the
`display/window/size/viewport_height<class_ProjectSettings_property_display/window/size/viewport_height>`{.interpreted-text
role="ref"}. This setting is ignored on iOS, Android, and Web.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/size/window_width_override}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/size/window_width_override** = `0`
`🔗<class_ProjectSettings_property_display/window/size/window_width_override>`{.interpreted-text
role="ref"}

On desktop platforms, overrides the game\'s initial window width. See
also
`display/window/size/window_height_override<class_ProjectSettings_property_display/window/size/window_height_override>`{.interpreted-text
role="ref"},
`display/window/size/viewport_width<class_ProjectSettings_property_display/window/size/viewport_width>`{.interpreted-text
role="ref"} and
`display/window/size/viewport_height<class_ProjectSettings_property_display/window/size/viewport_height>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* By default, or when set to `0`, the initial window width
is the
`display/window/size/viewport_width<class_ProjectSettings_property_display/window/size/viewport_width>`{.interpreted-text
role="ref"}. This setting is ignored on iOS, Android, and Web.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/stretch/aspect}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/window/stretch/aspect** = `"keep"`
`🔗<class_ProjectSettings_property_display/window/stretch/aspect>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/stretch/mode}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/window/stretch/mode** = `"disabled"`
`🔗<class_ProjectSettings_property_display/window/stretch/mode>`{.interpreted-text
role="ref"}

Defines how the base size is stretched to fit the resolution of the
window or screen.

\*\*\"disabled\"\*\*: No stretching happens. One unit in the scene
corresponds to one pixel on the screen. In this mode,
`display/window/stretch/aspect<class_ProjectSettings_property_display/window/stretch/aspect>`{.interpreted-text
role="ref"} has no effect. Recommended for non-game applications.

\*\*\"canvas_items\"\*\*: The base size specified in width and height in
the project settings is stretched to cover the whole screen (taking
`display/window/stretch/aspect<class_ProjectSettings_property_display/window/stretch/aspect>`{.interpreted-text
role="ref"} into account). This means that everything is rendered
directly at the target resolution. 3D is unaffected, while in 2D, there
is no longer a 1:1 correspondence between sprite pixels and screen
pixels, which may result in scaling artifacts. Recommended for most
games that don\'t use a pixel art aesthetic, although it is possible to
use this stretch mode for pixel art games too (especially in 3D).

\*\*\"viewport\"\*\*: The size of the root
`Viewport<class_Viewport>`{.interpreted-text role="ref"} is set
precisely to the base size specified in the Project Settings\' Display
section. The scene is rendered to this viewport first. Finally, this
viewport is scaled to fit the screen (taking
`display/window/stretch/aspect<class_ProjectSettings_property_display/window/stretch/aspect>`{.interpreted-text
role="ref"} into account). Recommended for games that use a pixel art
aesthetic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/stretch/scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**display/window/stretch/scale** = `1.0`
`🔗<class_ProjectSettings_property_display/window/stretch/scale>`{.interpreted-text
role="ref"}

The scale factor multiplier to use for 2D elements. This multiplies the
final scale factor determined by
`display/window/stretch/mode<class_ProjectSettings_property_display/window/stretch/mode>`{.interpreted-text
role="ref"}. If using the **Disabled** stretch mode, this scale factor
is applied as-is. This can be adjusted to make the UI easier to read on
certain displays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/stretch/scale_mode}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**display/window/stretch/scale_mode** = `"fractional"`
`🔗<class_ProjectSettings_property_display/window/stretch/scale_mode>`{.interpreted-text
role="ref"}

The policy to use to determine the final scale factor for 2D elements.
This affects how
`display/window/stretch/scale<class_ProjectSettings_property_display/window/stretch/scale>`{.interpreted-text
role="ref"} is applied, in addition to the automatic scale factor
determined by
`display/window/stretch/mode<class_ProjectSettings_property_display/window/stretch/mode>`{.interpreted-text
role="ref"}.

\*\*\"fractional\"\*\*: The scale factor will not be modified.

\*\*\"integer\"\*\*: The scale factor will be floored to an integer
value, which means that the screen size will always be an integer
multiple of the base viewport size. This provides a crisp pixel art
appearance.

\*\*Note:\*\* When using integer scaling with a stretch mode, resizing
the window to be smaller than the base viewport size will clip the
contents. Consider preventing that by setting
`Window.min_size<class_Window_property_min_size>`{.interpreted-text
role="ref"} to the same value as the base viewport size defined in
`display/window/size/viewport_width<class_ProjectSettings_property_display/window/size/viewport_width>`{.interpreted-text
role="ref"} and
`display/window/size/viewport_height<class_ProjectSettings_property_display/window/size/viewport_height>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/subwindows/embed_subwindows}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**display/window/subwindows/embed_subwindows** = `true`
`🔗<class_ProjectSettings_property_display/window/subwindows/embed_subwindows>`{.interpreted-text
role="ref"}

If `true`, subwindows are embedded in the main window (this is also
called single-window mode). Single-window mode can be faster as it does
not need to create a separate window for every popup and tooltip, which
can be a slow operation depending on the operating system and rendering
method in use.

If `false`, subwindows are created as separate windows (this is also
called multi-window mode). This allows them to be moved outside the main
window and use native operating system window decorations.

This is equivalent to
`EditorSettings.interface/editor/single_window_mode<class_EditorSettings_property_interface/editor/single_window_mode>`{.interpreted-text
role="ref"} in the editor, except the setting\'s value is inverted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_display/window/vsync/vsync_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**display/window/vsync/vsync_mode** = `1`
`🔗<class_ProjectSettings_property_display/window/vsync/vsync_mode>`{.interpreted-text
role="ref"}

Sets the V-Sync mode for the main game window. The editor\'s own V-Sync
mode can be set using
`EditorSettings.interface/editor/vsync_mode<class_EditorSettings_property_interface/editor/vsync_mode>`{.interpreted-text
role="ref"}.

See `VSyncMode<enum_DisplayServer_VSyncMode>`{.interpreted-text
role="ref"} for possible values and how they affect the behavior of your
application.

Depending on the platform and rendering method, the engine will fall
back to **Enabled** if the desired mode is not supported.

V-Sync can be disabled on the command line using the `--disable-vsync`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

\*\*Note:\*\* The **Adaptive** and **Mailbox** V-Sync modes are only
supported in the Forward+ and Mobile rendering methods, not
Compatibility.

\*\*Note:\*\* This property is only read when the project starts. To
change the V-Sync mode at runtime, call
`DisplayServer.window_set_vsync_mode()<class_DisplayServer_method_window_set_vsync_mode>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_dotnet/project/assembly_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**dotnet/project/assembly_name** = `""`
`🔗<class_ProjectSettings_property_dotnet/project/assembly_name>`{.interpreted-text
role="ref"}

Name of the .NET assembly. This name is used as the name of the
`.csproj` and `.sln` files. By default, it\'s set to the name of the
project
(`application/config/name<class_ProjectSettings_property_application/config/name>`{.interpreted-text
role="ref"}) allowing to change it in the future without affecting the
.NET assembly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_dotnet/project/assembly_reload_attempts}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**dotnet/project/assembly_reload_attempts** = `3`
`🔗<class_ProjectSettings_property_dotnet/project/assembly_reload_attempts>`{.interpreted-text
role="ref"}

Number of times to attempt assembly reloading after rebuilding .NET
assemblies. Effectively also the timeout in seconds to wait for
unloading of script assemblies to finish.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_dotnet/project/solution_directory}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**dotnet/project/solution_directory** = `""`
`🔗<class_ProjectSettings_property_dotnet/project/solution_directory>`{.interpreted-text
role="ref"}

Directory that contains the `.sln` file. By default, the `.sln` files is
in the root of the project directory, next to the `project.godot` and
`.csproj` files.

Changing this value allows setting up a multi-project scenario where
there are multiple `.csproj`. Keep in mind that the Godot project is
considered one of the C# projects in the workspace and it\'s root
directory should contain the `project.godot` and `.csproj` next to each
other.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/export/convert_text_resources_to_binary}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editor/export/convert_text_resources_to_binary** = `true`
`🔗<class_ProjectSettings_property_editor/export/convert_text_resources_to_binary>`{.interpreted-text
role="ref"}

If `true`, text resource (`tres`) and text scene (`tscn`) files are
converted to their corresponding binary format on export. This decreases
file sizes and speeds up loading slightly.

\*\*Note:\*\* Because a resource\'s file extension may change in an
exported project, it is heavily recommended to use
`@GDScript.load()<class_@GDScript_method_load>`{.interpreted-text
role="ref"} or `ResourceLoader<class_ResourceLoader>`{.interpreted-text
role="ref"} instead of `FileAccess<class_FileAccess>`{.interpreted-text
role="ref"} to load resources dynamically.

\*\*Note:\*\* The project settings file (`project.godot`) will always be
converted to binary on export, regardless of this setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/import/atlas_max_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/import/atlas_max_width** = `2048`
`🔗<class_ProjectSettings_property_editor/import/atlas_max_width>`{.interpreted-text
role="ref"}

The maximum width to use when importing textures as an atlas. The value
will be rounded to the nearest power of two when used. Use this to
prevent imported textures from growing too large in the other direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/import/reimport_missing_imported_files}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editor/import/reimport_missing_imported_files** = `true`
`🔗<class_ProjectSettings_property_editor/import/reimport_missing_imported_files>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/import/use_multiple_threads}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editor/import/use_multiple_threads** = `true`
`🔗<class_ProjectSettings_property_editor/import/use_multiple_threads>`{.interpreted-text
role="ref"}

If `true` importing of resources is run on multiple threads.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/movie_writer/disable_vsync}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editor/movie_writer/disable_vsync** = `false`
`🔗<class_ProjectSettings_property_editor/movie_writer/disable_vsync>`{.interpreted-text
role="ref"}

If `true`, requests V-Sync to be disabled when writing a movie (similar
to setting
`display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>`{.interpreted-text
role="ref"} to **Disabled**). This can speed up video writing if the
hardware is fast enough to render, encode and save the video at a
framerate higher than the monitor\'s refresh rate.

\*\*Note:\*\*
`editor/movie_writer/disable_vsync<class_ProjectSettings_property_editor/movie_writer/disable_vsync>`{.interpreted-text
role="ref"} has no effect if the operating system or graphics driver
forces V-Sync with no way for applications to disable it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/movie_writer/fps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/movie_writer/fps** = `60`
`🔗<class_ProjectSettings_property_editor/movie_writer/fps>`{.interpreted-text
role="ref"}

The number of frames per second to record in the video when writing a
movie. Simulation speed will adjust to always match the specified
framerate, which means the engine will appear to run slower at higher
`editor/movie_writer/fps<class_ProjectSettings_property_editor/movie_writer/fps>`{.interpreted-text
role="ref"} values. Certain FPS values will require you to adjust
`editor/movie_writer/mix_rate<class_ProjectSettings_property_editor/movie_writer/mix_rate>`{.interpreted-text
role="ref"} to prevent audio from desynchronizing over time.

This can be specified manually on the command line using the
`--fixed-fps <fps>`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/movie_writer/mix_rate}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/movie_writer/mix_rate** = `48000`
`🔗<class_ProjectSettings_property_editor/movie_writer/mix_rate>`{.interpreted-text
role="ref"}

The audio mix rate to use in the recorded audio when writing a movie (in
Hz). This can be different from
`audio/driver/mix_rate<class_ProjectSettings_property_audio/driver/mix_rate>`{.interpreted-text
role="ref"}, but this value must be divisible by
`editor/movie_writer/fps<class_ProjectSettings_property_editor/movie_writer/fps>`{.interpreted-text
role="ref"} to prevent audio from desynchronizing over time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/movie_writer/movie_file}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**editor/movie_writer/movie_file** = `""`
`🔗<class_ProjectSettings_property_editor/movie_writer/movie_file>`{.interpreted-text
role="ref"}

The output path for the movie. The file extension determines the
`MovieWriter<class_MovieWriter>`{.interpreted-text role="ref"} that will
be used.

Godot has 3 built-in `MovieWriter<class_MovieWriter>`{.interpreted-text
role="ref"}s:

- OGV container with Theora for video and Vorbis for audio (`.ogv` file
  extension). Lossy compression, medium file sizes, fast encoding. The
  lossy compression quality can be adjusted by changing
  `editor/movie_writer/video_quality<class_ProjectSettings_property_editor/movie_writer/video_quality>`{.interpreted-text
  role="ref"} and
  `editor/movie_writer/ogv/audio_quality<class_ProjectSettings_property_editor/movie_writer/ogv/audio_quality>`{.interpreted-text
  role="ref"}. The resulting file can be viewed in Godot with
  `VideoStreamPlayer<class_VideoStreamPlayer>`{.interpreted-text
  role="ref"} and most video players, but not web browsers as they
  don\'t support Theora.
- AVI container with MJPEG for video and uncompressed audio (`.avi` file
  extension). Lossy compression, medium file sizes, fast encoding. The
  lossy compression quality can be adjusted by changing
  `editor/movie_writer/video_quality<class_ProjectSettings_property_editor/movie_writer/video_quality>`{.interpreted-text
  role="ref"}. The resulting file can be viewed in most video players,
  but it must be converted to another format for viewing on the web or
  by Godot with
  `VideoStreamPlayer<class_VideoStreamPlayer>`{.interpreted-text
  role="ref"}. MJPEG does not support transparency. AVI output is
  currently limited to a file of 4 GB in size at most.
- PNG image sequence for video and WAV for audio (`.png` file
  extension). Lossless compression, large file sizes, slow encoding.
  Designed to be encoded to a video file with another tool such as
  [FFmpeg](https://ffmpeg.org/) after recording. Transparency is
  currently not supported, even if the root viewport is set to be
  transparent.

If you need to encode to a different format or pipe a stream through
third-party software, you can extend this
`MovieWriter<class_MovieWriter>`{.interpreted-text role="ref"} class to
create your own movie writers.

When using PNG output, the frame number will be appended at the end of
the file name. It starts from 0 and is padded with 8 digits to ensure
correct sorting and easier processing. For example, if the output path
is `/tmp/hello.png`, the first two frames will be
`/tmp/hello00000000.png` and `/tmp/hello00000001.png`. The audio will be
saved at `/tmp/hello.wav`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/movie_writer/ogv/audio_quality}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editor/movie_writer/ogv/audio_quality** = `0.5`
`🔗<class_ProjectSettings_property_editor/movie_writer/ogv/audio_quality>`{.interpreted-text
role="ref"}

The audio encoding quality to use when writing Vorbis audio to a file,
between `-0.1` and `1.0` (inclusive). Higher `quality` values result in
better-sounding output at the cost of larger file sizes. Even at quality
`1.0`, compression remains lossy.

\*\*Note:\*\* This does not affect video quality, which is controlled by
`editor/movie_writer/video_quality<class_ProjectSettings_property_editor/movie_writer/video_quality>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/movie_writer/ogv/encoding_speed}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/movie_writer/ogv/encoding_speed** = `4`
`🔗<class_ProjectSettings_property_editor/movie_writer/ogv/encoding_speed>`{.interpreted-text
role="ref"}

The tradeoff between encoding speed and compression efficiency. Speed
`1` is the slowest but provides the best compression. Speed `4` is the
fastest but provides the worst compression. Video quality is generally
not affected significantly by this setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/movie_writer/ogv/keyframe_interval}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/movie_writer/ogv/keyframe_interval** = `64`
`🔗<class_ProjectSettings_property_editor/movie_writer/ogv/keyframe_interval>`{.interpreted-text
role="ref"}

Forces keyframes at the specified interval (in frame count). Higher
values can improve compression up to a certain level at the expense of
higher latency when seeking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/movie_writer/speaker_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/movie_writer/speaker_mode** = `0`
`🔗<class_ProjectSettings_property_editor/movie_writer/speaker_mode>`{.interpreted-text
role="ref"}

The speaker mode to use in the recorded audio when writing a movie. See
`SpeakerMode<enum_AudioServer_SpeakerMode>`{.interpreted-text
role="ref"} for possible values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/movie_writer/video_quality}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editor/movie_writer/video_quality** = `0.75`
`🔗<class_ProjectSettings_property_editor/movie_writer/video_quality>`{.interpreted-text
role="ref"}

The video encoding quality to use when writing a Theora or AVI (MJPEG)
video to a file, between `0.0` and `1.0` (inclusive). Higher `quality`
values result in better-looking output at the cost of larger file sizes.
Recommended `quality` values are between `0.75` and `0.9`. Even at
quality `1.0`, compression remains lossy.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/naming/default_signal_callback_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**editor/naming/default_signal_callback_name** =
`"_on_{node_name}_{signal_name}"`
`🔗<class_ProjectSettings_property_editor/naming/default_signal_callback_name>`{.interpreted-text
role="ref"}

The format of the default signal callback name (in the Signal Connection
Dialog). The following substitutions are available: `{NodeName}`,
`{nodeName}`, `{node_name}`, `{SignalName}`, `{signalName}`, and
`{signal_name}`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/naming/default_signal_callback_to_self_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**editor/naming/default_signal_callback_to_self_name** =
`"_on_{signal_name}"`
`🔗<class_ProjectSettings_property_editor/naming/default_signal_callback_to_self_name>`{.interpreted-text
role="ref"}

The format of the default signal callback name when a signal connects to
the same node that emits it (in the Signal Connection Dialog). The
following substitutions are available: `{NodeName}`, `{nodeName}`,
`{node_name}`, `{SignalName}`, `{signalName}`, and `{signal_name}`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/naming/node_name_casing}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/naming/node_name_casing** = `0`
`🔗<class_ProjectSettings_property_editor/naming/node_name_casing>`{.interpreted-text
role="ref"}

When creating node names automatically, set the type of casing to use in
this project. This is mostly an editor setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/naming/node_name_num_separator}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/naming/node_name_num_separator** = `0`
`🔗<class_ProjectSettings_property_editor/naming/node_name_num_separator>`{.interpreted-text
role="ref"}

What to use to separate node name from number. This is mostly an editor
setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/naming/scene_name_casing}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/naming/scene_name_casing** = `2`
`🔗<class_ProjectSettings_property_editor/naming/scene_name_casing>`{.interpreted-text
role="ref"}

When generating scene file names from scene root node, set the type of
casing to use in this project. This is mostly an editor setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/naming/script_name_casing}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editor/naming/script_name_casing** = `0`
`🔗<class_ProjectSettings_property_editor/naming/script_name_casing>`{.interpreted-text
role="ref"}

When generating script file names from the selected node, set the type
of casing to use in this project. This is mostly an editor setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/run/main_run_args}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**editor/run/main_run_args** = `""`
`🔗<class_ProjectSettings_property_editor/run/main_run_args>`{.interpreted-text
role="ref"}

The command-line arguments to append to Godot\'s own command line when
running the project. This doesn\'t affect the editor itself.

It is possible to make another executable run Godot by using the
`%command%` placeholder. The placeholder will be replaced with Godot\'s
own command line. Program-specific arguments should be placed *before*
the placeholder, whereas Godot-specific arguments should be placed
*after* the placeholder.

For example, this can be used to force the project to run on the
dedicated GPU in an NVIDIA Optimus system on Linux:

``` text
prime-run %command%
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/script/search_in_file_extensions}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **editor/script/search_in_file_extensions**
`🔗<class_ProjectSettings_property_editor/script/search_in_file_extensions>`{.interpreted-text
role="ref"}

Text-based file extensions to include in the script editor\'s \"Find in
Files\" feature. You can add e.g. `tscn` if you wish to also parse your
scene files, especially if you use built-in scripts which are serialized
in the scene files.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/script/templates_search_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**editor/script/templates_search_path** = `"res://script_templates"`
`🔗<class_ProjectSettings_property_editor/script/templates_search_path>`{.interpreted-text
role="ref"}

Search path for project-specific script templates. Godot will search for
script templates both in the editor-specific path and in this
project-specific path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/version_control/autoload_on_startup}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editor/version_control/autoload_on_startup** = `false`
`🔗<class_ProjectSettings_property_editor/version_control/autoload_on_startup>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_editor/version_control/plugin_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**editor/version_control/plugin_name** = `""`
`🔗<class_ProjectSettings_property_editor/version_control/plugin_name>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_filesystem/import/blender/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/import/blender/enabled** = `true`
`🔗<class_ProjectSettings_property_filesystem/import/blender/enabled>`{.interpreted-text
role="ref"}

If `true`, Blender 3D scene files with the `.blend` extension will be
imported by converting them to glTF 2.0.

This requires configuring a path to a Blender executable in the
`EditorSettings.filesystem/import/blender/blender_path<class_EditorSettings_property_filesystem/import/blender/blender_path>`{.interpreted-text
role="ref"} setting. Blender 3.0 or later is required.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_filesystem/import/blender/enabled.android}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/import/blender/enabled.android** = `false`
`🔗<class_ProjectSettings_property_filesystem/import/blender/enabled.android>`{.interpreted-text
role="ref"}

Override for
`filesystem/import/blender/enabled<class_ProjectSettings_property_filesystem/import/blender/enabled>`{.interpreted-text
role="ref"} on Android where Blender can\'t easily be accessed from
Godot.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_filesystem/import/blender/enabled.web}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/import/blender/enabled.web** = `false`
`🔗<class_ProjectSettings_property_filesystem/import/blender/enabled.web>`{.interpreted-text
role="ref"}

Override for
`filesystem/import/blender/enabled<class_ProjectSettings_property_filesystem/import/blender/enabled>`{.interpreted-text
role="ref"} on the Web where Blender can\'t easily be accessed from
Godot.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/import/fbx2gltf/enabled** = `true`
`🔗<class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled>`{.interpreted-text
role="ref"}

If `true`, Autodesk FBX 3D scene files with the `.fbx` extension will be
imported by converting them to glTF 2.0.

This requires configuring a path to an FBX2glTF executable in the editor
settings at
`EditorSettings.filesystem/import/fbx/fbx2gltf_path<class_EditorSettings_property_filesystem/import/fbx/fbx2gltf_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled.android}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/import/fbx2gltf/enabled.android** = `false`
`🔗<class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled.android>`{.interpreted-text
role="ref"}

Override for
`filesystem/import/fbx2gltf/enabled<class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled>`{.interpreted-text
role="ref"} on Android where FBX2glTF can\'t easily be accessed from
Godot.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled.web}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/import/fbx2gltf/enabled.web** = `false`
`🔗<class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled.web>`{.interpreted-text
role="ref"}

Override for
`filesystem/import/fbx2gltf/enabled<class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled>`{.interpreted-text
role="ref"} on the Web where FBX2glTF can\'t easily be accessed from
Godot.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/common/default_scroll_deadzone}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**gui/common/default_scroll_deadzone** = `0`
`🔗<class_ProjectSettings_property_gui/common/default_scroll_deadzone>`{.interpreted-text
role="ref"}

Default value for
`ScrollContainer.scroll_deadzone<class_ScrollContainer_property_scroll_deadzone>`{.interpreted-text
role="ref"}, which will be used for all
`ScrollContainer<class_ScrollContainer>`{.interpreted-text role="ref"}s
unless overridden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/common/snap_controls_to_pixels}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gui/common/snap_controls_to_pixels** = `true`
`🔗<class_ProjectSettings_property_gui/common/snap_controls_to_pixels>`{.interpreted-text
role="ref"}

If `true`, snaps `Control<class_Control>`{.interpreted-text role="ref"}
node vertices to the nearest pixel to ensure they remain crisp even when
the camera moves or zooms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/common/swap_cancel_ok}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**gui/common/swap_cancel_ok** = `0`
`🔗<class_ProjectSettings_property_gui/common/swap_cancel_ok>`{.interpreted-text
role="ref"}

How to position the Cancel and OK buttons in the project\'s
`AcceptDialog<class_AcceptDialog>`{.interpreted-text role="ref"}s.
Different platforms have different standard behaviors for this, which
can be overridden using this setting.

- **Auto** (`0`) follows the platform convention: OK first on Windows,
  KDE, and LXQt, Cancel first on macOS and other Linux desktop
  environments.
  `DisplayServer.get_swap_cancel_ok()<class_DisplayServer_method_get_swap_cancel_ok>`{.interpreted-text
  role="ref"} can be used to query whether buttons are swapped at
  run-time.
- **Cancel First** (`1`) forces the ordering Cancel/OK.
- **OK First** (`2`) forces the ordering OK/Cancel.

\*\*Note:\*\* This doesn\'t affect native dialogs such as the ones
spawned by
`DisplayServer.dialog_show()<class_DisplayServer_method_dialog_show>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/common/text_edit_undo_stack_max_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**gui/common/text_edit_undo_stack_max_size** = `1024`
`🔗<class_ProjectSettings_property_gui/common/text_edit_undo_stack_max_size>`{.interpreted-text
role="ref"}

Maximum undo/redo history size for
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"} fields.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/fonts/dynamic_fonts/use_oversampling}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gui/fonts/dynamic_fonts/use_oversampling** = `true`
`🔗<class_ProjectSettings_property_gui/fonts/dynamic_fonts/use_oversampling>`{.interpreted-text
role="ref"}

If set to `true` and
`display/window/stretch/mode<class_ProjectSettings_property_display/window/stretch/mode>`{.interpreted-text
role="ref"} is set to **\"canvas_items\"**, font and
`SVGTexture<class_SVGTexture>`{.interpreted-text role="ref"}
oversampling is enabled in the main window. Use
`Viewport.oversampling<class_Viewport_property_oversampling>`{.interpreted-text
role="ref"} to control oversampling in other viewports and windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/theme/custom}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**gui/theme/custom** = `""`
`🔗<class_ProjectSettings_property_gui/theme/custom>`{.interpreted-text
role="ref"}

Path to a custom `Theme<class_Theme>`{.interpreted-text role="ref"}
resource file to use for the project (`.theme` or generic `.tres`/`.res`
extension).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/theme/custom_font}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**gui/theme/custom_font** = `""`
`🔗<class_ProjectSettings_property_gui/theme/custom_font>`{.interpreted-text
role="ref"}

Path to a custom `Font<class_Font>`{.interpreted-text role="ref"}
resource to use as default for all GUI elements of the project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/theme/default_font_antialiasing}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**gui/theme/default_font_antialiasing** = `1`
`🔗<class_ProjectSettings_property_gui/theme/default_font_antialiasing>`{.interpreted-text
role="ref"}

Font anti-aliasing mode for the default project font. See
`FontFile.antialiasing<class_FontFile_property_antialiasing>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This setting does not affect custom
`Font<class_Font>`{.interpreted-text role="ref"}s used within the
project. Use the **Import** dock for that instead (see
`ResourceImporterDynamicFont.antialiasing<class_ResourceImporterDynamicFont_property_antialiasing>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/theme/default_font_generate_mipmaps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gui/theme/default_font_generate_mipmaps** = `false`
`🔗<class_ProjectSettings_property_gui/theme/default_font_generate_mipmaps>`{.interpreted-text
role="ref"}

If set to `true`, the default font will have mipmaps generated. This
prevents text from looking grainy when a
`Control<class_Control>`{.interpreted-text role="ref"} is scaled down,
or when a `Label3D<class_Label3D>`{.interpreted-text role="ref"} is
viewed from a long distance (if
`Label3D.texture_filter<class_Label3D_property_texture_filter>`{.interpreted-text
role="ref"} is set to a mode that displays mipmaps).

Enabling
`gui/theme/default_font_generate_mipmaps<class_ProjectSettings_property_gui/theme/default_font_generate_mipmaps>`{.interpreted-text
role="ref"} increases font generation time and memory usage. Only enable
this setting if you actually need it.

\*\*Note:\*\* This setting does not affect custom
`Font<class_Font>`{.interpreted-text role="ref"}s used within the
project. Use the **Import** dock for that instead (see
`ResourceImporterDynamicFont.generate_mipmaps<class_ResourceImporterDynamicFont_property_generate_mipmaps>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/theme/default_font_hinting}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**gui/theme/default_font_hinting** = `1`
`🔗<class_ProjectSettings_property_gui/theme/default_font_hinting>`{.interpreted-text
role="ref"}

Font hinting mode for the default project font. See
`FontFile.hinting<class_FontFile_property_hinting>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This setting does not affect custom
`Font<class_Font>`{.interpreted-text role="ref"}s used within the
project. Use the **Import** dock for that instead (see
`ResourceImporterDynamicFont.hinting<class_ResourceImporterDynamicFont_property_hinting>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/theme/default_font_multichannel_signed_distance_field}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gui/theme/default_font_multichannel_signed_distance_field** = `false`
`🔗<class_ProjectSettings_property_gui/theme/default_font_multichannel_signed_distance_field>`{.interpreted-text
role="ref"}

If set to `true`, the default font will use multichannel signed distance
field (MSDF) for crisp rendering at any size. Since this approach does
not rely on rasterizing the font every time its size changes, this
allows for resizing the font in real-time without any performance
penalty. Text will also not look grainy for
`Control<class_Control>`{.interpreted-text role="ref"}s that are scaled
down (or for `Label3D<class_Label3D>`{.interpreted-text role="ref"}s
viewed from a long distance).

MSDF font rendering can be combined with
`gui/theme/default_font_generate_mipmaps<class_ProjectSettings_property_gui/theme/default_font_generate_mipmaps>`{.interpreted-text
role="ref"} to further improve font rendering quality when scaled down.

\*\*Note:\*\* This setting does not affect custom
`Font<class_Font>`{.interpreted-text role="ref"}s used within the
project. Use the **Import** dock for that instead (see
`ResourceImporterDynamicFont.multichannel_signed_distance_field<class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/theme/default_font_subpixel_positioning}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**gui/theme/default_font_subpixel_positioning** = `1`
`🔗<class_ProjectSettings_property_gui/theme/default_font_subpixel_positioning>`{.interpreted-text
role="ref"}

Font glyph subpixel positioning mode for the default project font. See
`FontFile.subpixel_positioning<class_FontFile_property_subpixel_positioning>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This setting does not affect custom
`Font<class_Font>`{.interpreted-text role="ref"}s used within the
project. Use the **Import** dock for that instead (see
`ResourceImporterDynamicFont.subpixel_positioning<class_ResourceImporterDynamicFont_property_subpixel_positioning>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/theme/default_theme_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**gui/theme/default_theme_scale** = `1.0`
`🔗<class_ProjectSettings_property_gui/theme/default_theme_scale>`{.interpreted-text
role="ref"}

The default scale factor for `Control<class_Control>`{.interpreted-text
role="ref"}s, when not overridden by a
`Theme<class_Theme>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This property is only read when the project starts. To
change the default scale at runtime, set
`ThemeDB.fallback_base_scale<class_ThemeDB_property_fallback_base_scale>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/theme/lcd_subpixel_layout}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**gui/theme/lcd_subpixel_layout** = `1`
`🔗<class_ProjectSettings_property_gui/theme/lcd_subpixel_layout>`{.interpreted-text
role="ref"}

LCD subpixel layout used for font anti-aliasing. See
`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/timers/button_shortcut_feedback_highlight_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**gui/timers/button_shortcut_feedback_highlight_time** = `0.2`
`🔗<class_ProjectSettings_property_gui/timers/button_shortcut_feedback_highlight_time>`{.interpreted-text
role="ref"}

When
`BaseButton.shortcut_feedback<class_BaseButton_property_shortcut_feedback>`{.interpreted-text
role="ref"} is enabled, this is the time the
`BaseButton<class_BaseButton>`{.interpreted-text role="ref"} will remain
highlighted after a shortcut.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/timers/incremental_search_max_interval_msec}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**gui/timers/incremental_search_max_interval_msec** = `2000`
`🔗<class_ProjectSettings_property_gui/timers/incremental_search_max_interval_msec>`{.interpreted-text
role="ref"}

Timer setting for incremental search in
`Tree<class_Tree>`{.interpreted-text role="ref"},
`ItemList<class_ItemList>`{.interpreted-text role="ref"}, etc. controls
(in milliseconds).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/timers/text_edit_idle_detect_sec}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**gui/timers/text_edit_idle_detect_sec** = `3`
`🔗<class_ProjectSettings_property_gui/timers/text_edit_idle_detect_sec>`{.interpreted-text
role="ref"}

Timer for detecting idle in `TextEdit<class_TextEdit>`{.interpreted-text
role="ref"} (in seconds).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/timers/tooltip_delay_sec}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**gui/timers/tooltip_delay_sec** = `0.5`
`🔗<class_ProjectSettings_property_gui/timers/tooltip_delay_sec>`{.interpreted-text
role="ref"}

Default delay for tooltips (in seconds).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_gui/timers/tooltip_delay_sec.editor_hint}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**gui/timers/tooltip_delay_sec.editor_hint** = `0.5`
`🔗<class_ProjectSettings_property_gui/timers/tooltip_delay_sec.editor_hint>`{.interpreted-text
role="ref"}

Delay for tooltips in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_accept}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_accept**
`🔗<class_ProjectSettings_property_input/ui_accept>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to confirm a focused button, menu or list item, or validate
input.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_accessibility_drag_and_drop}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_accessibility_drag_and_drop**
`🔗<class_ProjectSettings_property_input/ui_accessibility_drag_and_drop>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to start or end a drag-and-drop operation without using
mouse.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_cancel}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_cancel**
`🔗<class_ProjectSettings_property_input/ui_cancel>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to discard a modal or pending input.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_colorpicker_delete_preset}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_colorpicker_delete_preset**
`🔗<class_ProjectSettings_property_input/ui_colorpicker_delete_preset>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to delete a color preset in a
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_copy}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_copy**
`🔗<class_ProjectSettings_property_input/ui_copy>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to copy a selection to the clipboard.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_cut}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_cut**
`🔗<class_ProjectSettings_property_input/ui_cut>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to cut a selection to the clipboard.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_down}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_down**
`🔗<class_ProjectSettings_property_input/ui_down>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move down in the UI.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_end}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_end**
`🔗<class_ProjectSettings_property_input/ui_end>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to go to the end position of a
`Control<class_Control>`{.interpreted-text role="ref"} (e.g. last item
in an `ItemList<class_ItemList>`{.interpreted-text role="ref"} or a
`Tree<class_Tree>`{.interpreted-text role="ref"}), matching the behavior
of
`@GlobalScope.KEY_END<class_@GlobalScope_constant_KEY_END>`{.interpreted-text
role="ref"} on typical desktop UI systems.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_filedialog_refresh}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_filedialog_refresh**
`🔗<class_ProjectSettings_property_input/ui_filedialog_refresh>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to refresh the contents of the current directory of a
`FileDialog<class_FileDialog>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_filedialog_show_hidden}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_filedialog_show_hidden**
`🔗<class_ProjectSettings_property_input/ui_filedialog_show_hidden>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to toggle showing hidden files and directories in a
`FileDialog<class_FileDialog>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_filedialog_up_one_level}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_filedialog_up_one_level**
`🔗<class_ProjectSettings_property_input/ui_filedialog_up_one_level>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to go up one directory in a
`FileDialog<class_FileDialog>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_focus_mode}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_focus_mode**
`🔗<class_ProjectSettings_property_input/ui_focus_mode>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to switch `TextEdit<class_TextEdit>`{.interpreted-text
role="ref"}
`input/ui_text_indent<class_ProjectSettings_property_input/ui_text_indent>`{.interpreted-text
role="ref"} between moving keyboard focus to the next
`Control<class_Control>`{.interpreted-text role="ref"} in the scene and
inputting a `Tab` character.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_focus_next}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_focus_next**
`🔗<class_ProjectSettings_property_input/ui_focus_next>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to focus the next `Control<class_Control>`{.interpreted-text
role="ref"} in the scene. The focus behavior can be configured via
`Control.focus_next<class_Control_property_focus_next>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_focus_prev}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_focus_prev**
`🔗<class_ProjectSettings_property_input/ui_focus_prev>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to focus the previous
`Control<class_Control>`{.interpreted-text role="ref"} in the scene. The
focus behavior can be configured via
`Control.focus_previous<class_Control_property_focus_previous>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_graph_delete}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_graph_delete**
`🔗<class_ProjectSettings_property_input/ui_graph_delete>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to delete a `GraphNode<class_GraphNode>`{.interpreted-text
role="ref"} in a `GraphEdit<class_GraphEdit>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_graph_duplicate}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_graph_duplicate**
`🔗<class_ProjectSettings_property_input/ui_graph_duplicate>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to duplicate a
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"} in a
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_graph_follow_left}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_graph_follow_left**
`🔗<class_ProjectSettings_property_input/ui_graph_follow_left>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to follow a `GraphNode<class_GraphNode>`{.interpreted-text
role="ref"} input port connection.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_graph_follow_left.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_graph_follow_left.macos**
`🔗<class_ProjectSettings_property_input/ui_graph_follow_left.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to follow a
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"} input port
connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_graph_follow_right}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_graph_follow_right**
`🔗<class_ProjectSettings_property_input/ui_graph_follow_right>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to follow a `GraphNode<class_GraphNode>`{.interpreted-text
role="ref"} output port connection.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_graph_follow_right.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_graph_follow_right.macos**
`🔗<class_ProjectSettings_property_input/ui_graph_follow_right.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to follow a
`GraphNode<class_GraphNode>`{.interpreted-text role="ref"} output port
connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_home}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_home**
`🔗<class_ProjectSettings_property_input/ui_home>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to go to the start position of a
`Control<class_Control>`{.interpreted-text role="ref"} (e.g. first item
in an `ItemList<class_ItemList>`{.interpreted-text role="ref"} or a
`Tree<class_Tree>`{.interpreted-text role="ref"}), matching the behavior
of
`@GlobalScope.KEY_HOME<class_@GlobalScope_constant_KEY_HOME>`{.interpreted-text
role="ref"} on typical desktop UI systems.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_left}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_left**
`🔗<class_ProjectSettings_property_input/ui_left>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move left in the UI.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_menu}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_menu**
`🔗<class_ProjectSettings_property_input/ui_menu>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to open a context menu in a text field.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_page_down}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_page_down**
`🔗<class_ProjectSettings_property_input/ui_page_down>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to go down a page in a
`Control<class_Control>`{.interpreted-text role="ref"} (e.g. in an
`ItemList<class_ItemList>`{.interpreted-text role="ref"} or a
`Tree<class_Tree>`{.interpreted-text role="ref"}), matching the behavior
of
`@GlobalScope.KEY_PAGEDOWN<class_@GlobalScope_constant_KEY_PAGEDOWN>`{.interpreted-text
role="ref"} on typical desktop UI systems.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_page_up}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_page_up**
`🔗<class_ProjectSettings_property_input/ui_page_up>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to go up a page in a
`Control<class_Control>`{.interpreted-text role="ref"} (e.g. in an
`ItemList<class_ItemList>`{.interpreted-text role="ref"} or a
`Tree<class_Tree>`{.interpreted-text role="ref"}), matching the behavior
of
`@GlobalScope.KEY_PAGEUP<class_@GlobalScope_constant_KEY_PAGEUP>`{.interpreted-text
role="ref"} on typical desktop UI systems.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_paste}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_paste**
`🔗<class_ProjectSettings_property_input/ui_paste>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to paste from the clipboard.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_redo}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_redo**
`🔗<class_ProjectSettings_property_input/ui_redo>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to redo an undone action.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_right}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_right**
`🔗<class_ProjectSettings_property_input/ui_right>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move right in the UI.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_select}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_select**
`🔗<class_ProjectSettings_property_input/ui_select>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to select an item in a
`Control<class_Control>`{.interpreted-text role="ref"} (e.g. in an
`ItemList<class_ItemList>`{.interpreted-text role="ref"} or a
`Tree<class_Tree>`{.interpreted-text role="ref"}).

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_swap_input_direction}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_swap_input_direction**
`🔗<class_ProjectSettings_property_input/ui_swap_input_direction>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to swap input direction, i.e. change between left-to-right
to right-to-left modes. Affects text-editing controls
(`LineEdit<class_LineEdit>`{.interpreted-text role="ref"},
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_add_selection_for_next_occurrence}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_add_selection_for_next_occurrence**
`🔗<class_ProjectSettings_property_input/ui_text_add_selection_for_next_occurrence>`{.interpreted-text
role="ref"}

If a selection is currently active with the last caret in text fields,
searches for the next occurrence of the selection, adds a caret and
selects the next occurrence.

If no selection is currently active with the last caret in text fields,
selects the word currently under the caret.

The action can be performed sequentially for all occurrences of the
selection of the last caret and for all existing carets.

The viewport is adjusted to the latest newly added caret.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_backspace}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_backspace**
`🔗<class_ProjectSettings_property_input/ui_text_backspace>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to delete the character before the text cursor.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_backspace_all_to_left}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_backspace_all_to_left**
`🔗<class_ProjectSettings_property_input/ui_text_backspace_all_to_left>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to delete **all** text before the text cursor.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_backspace_all_to_left.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_backspace_all_to_left.macos**
`🔗<class_ProjectSettings_property_input/ui_text_backspace_all_to_left.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to delete all text before the
text cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_backspace_word}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_backspace_word**
`🔗<class_ProjectSettings_property_input/ui_text_backspace_word>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to delete all characters before the cursor up until a
whitespace or punctuation character.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_backspace_word.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_backspace_word.macos**
`🔗<class_ProjectSettings_property_input/ui_text_backspace_word.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to delete a word.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_add_above}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_add_above**
`🔗<class_ProjectSettings_property_input/ui_text_caret_add_above>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to add an additional caret above every caret of a text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_add_above.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_add_above.macos**
`🔗<class_ProjectSettings_property_input/ui_text_caret_add_above.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to add a caret above every
caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_add_below}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_add_below**
`🔗<class_ProjectSettings_property_input/ui_text_caret_add_below>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to add an additional caret below every caret of a text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_add_below.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_add_below.macos**
`🔗<class_ProjectSettings_property_input/ui_text_caret_add_below.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to add a caret below every
caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_document_end}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_document_end**
`🔗<class_ProjectSettings_property_input/ui_text_caret_document_end>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor to the end of the text.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_document_end.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_document_end.macos**
`🔗<class_ProjectSettings_property_input/ui_text_caret_document_end.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to move the text cursor to the
end of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_document_start}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_document_start**
`🔗<class_ProjectSettings_property_input/ui_text_caret_document_start>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor to the start of the text.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_document_start.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_document_start.macos**
`🔗<class_ProjectSettings_property_input/ui_text_caret_document_start.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to move the text cursor to the
start of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_down}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_down**
`🔗<class_ProjectSettings_property_input/ui_text_caret_down>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor down.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_left}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_left**
`🔗<class_ProjectSettings_property_input/ui_text_caret_left>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor left.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_line_end}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_line_end**
`🔗<class_ProjectSettings_property_input/ui_text_caret_line_end>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor to the end of the line.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_line_end.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_line_end.macos**
`🔗<class_ProjectSettings_property_input/ui_text_caret_line_end.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to move the text cursor to the
end of the line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_line_start}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_line_start**
`🔗<class_ProjectSettings_property_input/ui_text_caret_line_start>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor to the start of the line.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_line_start.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_line_start.macos**
`🔗<class_ProjectSettings_property_input/ui_text_caret_line_start.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to move the text cursor to the
start of the line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_page_down}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_page_down**
`🔗<class_ProjectSettings_property_input/ui_text_caret_page_down>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor down one page.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_page_up}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_page_up**
`🔗<class_ProjectSettings_property_input/ui_text_caret_page_up>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor up one page.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_right}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_right**
`🔗<class_ProjectSettings_property_input/ui_text_caret_right>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor right.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_up}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_up**
`🔗<class_ProjectSettings_property_input/ui_text_caret_up>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor up.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_word_left}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_word_left**
`🔗<class_ProjectSettings_property_input/ui_text_caret_word_left>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor left to the next whitespace or
punctuation.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_word_left.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_word_left.macos**
`🔗<class_ProjectSettings_property_input/ui_text_caret_word_left.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to move the text cursor back
one word.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_word_right}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_word_right**
`🔗<class_ProjectSettings_property_input/ui_text_caret_word_right>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move the text cursor right to the next whitespace or
punctuation.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_caret_word_right.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_caret_word_right.macos**
`🔗<class_ProjectSettings_property_input/ui_text_caret_word_right.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to move the text cursor forward
one word.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_clear_carets_and_selection}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_clear_carets_and_selection**
`🔗<class_ProjectSettings_property_input/ui_text_clear_carets_and_selection>`{.interpreted-text
role="ref"}

If there\'s only one caret active and with a selection, clears the
selection.

In case there\'s more than one caret active, removes the secondary
carets and clears their selections.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_completion_accept}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_completion_accept**
`🔗<class_ProjectSettings_property_input/ui_text_completion_accept>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to accept an autocompletion hint.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_completion_query}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_completion_query**
`🔗<class_ProjectSettings_property_input/ui_text_completion_query>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to request autocompletion.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_completion_replace}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_completion_replace**
`🔗<class_ProjectSettings_property_input/ui_text_completion_replace>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to accept an autocompletion hint, replacing existing text.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_dedent}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_dedent**
`🔗<class_ProjectSettings_property_input/ui_text_dedent>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to unindent text.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_delete}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_delete**
`🔗<class_ProjectSettings_property_input/ui_text_delete>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to delete the character after the text cursor.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_delete_all_to_right}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_delete_all_to_right**
`🔗<class_ProjectSettings_property_input/ui_text_delete_all_to_right>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to delete **all** text after the text cursor.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_delete_all_to_right.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_delete_all_to_right.macos**
`🔗<class_ProjectSettings_property_input/ui_text_delete_all_to_right.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to delete all text after the
text cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_delete_word}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_delete_word**
`🔗<class_ProjectSettings_property_input/ui_text_delete_word>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to delete all characters after the cursor up until a
whitespace or punctuation character.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_delete_word.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_delete_word.macos**
`🔗<class_ProjectSettings_property_input/ui_text_delete_word.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to delete a word after the text
cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_indent}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_indent**
`🔗<class_ProjectSettings_property_input/ui_text_indent>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to indent the current line.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_newline}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_newline**
`🔗<class_ProjectSettings_property_input/ui_text_newline>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to insert a new line at the position of the text cursor.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_newline_above}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_newline_above**
`🔗<class_ProjectSettings_property_input/ui_text_newline_above>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to insert a new line before the current one.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_newline_blank}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_newline_blank**
`🔗<class_ProjectSettings_property_input/ui_text_newline_blank>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to insert a new line after the current one.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_scroll_down}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_scroll_down**
`🔗<class_ProjectSettings_property_input/ui_text_scroll_down>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to scroll down one line of text.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_scroll_down.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_scroll_down.macos**
`🔗<class_ProjectSettings_property_input/ui_text_scroll_down.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to scroll down one line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_scroll_up}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_scroll_up**
`🔗<class_ProjectSettings_property_input/ui_text_scroll_up>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to scroll up one line of text.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_scroll_up.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_scroll_up.macos**
`🔗<class_ProjectSettings_property_input/ui_text_scroll_up.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to scroll up one line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_select_all}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_select_all**
`🔗<class_ProjectSettings_property_input/ui_text_select_all>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to select all text.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_select_word_under_caret}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_select_word_under_caret**
`🔗<class_ProjectSettings_property_input/ui_text_select_word_under_caret>`{.interpreted-text
role="ref"}

If no selection is currently active, selects the word currently under
the caret in text fields. If a selection is currently active, deselects
the current selection.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_select_word_under_caret.macos}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_select_word_under_caret.macos**
`🔗<class_ProjectSettings_property_input/ui_text_select_word_under_caret.macos>`{.interpreted-text
role="ref"}

macOS specific override for the shortcut to select the word currently
under the caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_skip_selection_for_next_occurrence}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_skip_selection_for_next_occurrence**
`🔗<class_ProjectSettings_property_input/ui_text_skip_selection_for_next_occurrence>`{.interpreted-text
role="ref"}

If no selection is currently active with the last caret in text fields,
searches for the next occurrence of the word currently under the caret
and moves the caret to the next occurrence. The action can be performed
sequentially for other occurrences of the word under the last caret.

If a selection is currently active with the last caret in text fields,
searches for the next occurrence of the selection, adds a caret, selects
the next occurrence then deselects the previous selection and its
associated caret. The action can be performed sequentially for other
occurrences of the selection of the last caret.

The viewport is adjusted to the latest newly added caret.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_submit}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_submit**
`🔗<class_ProjectSettings_property_input/ui_text_submit>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to submit a text field.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_text_toggle_insert_mode}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_text_toggle_insert_mode**
`🔗<class_ProjectSettings_property_input/ui_text_toggle_insert_mode>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to toggle *insert mode* in a text field. While in insert
mode, inserting new text overrides the character after the cursor,
unless the next character is a new line.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_undo}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_undo**
`🔗<class_ProjectSettings_property_input/ui_undo>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to undo the most recent action.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_unicode_start}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_unicode_start**
`🔗<class_ProjectSettings_property_input/ui_unicode_start>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to start Unicode character hexadecimal code input in a text
field.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input/ui_up}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**input/ui_up**
`🔗<class_ProjectSettings_property_input/ui_up>`{.interpreted-text
role="ref"}

Default `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} to move up in the UI.

\*\*Note:\*\* Default `ui_*` actions cannot be removed as they are
necessary for the internal logic of several
`Control<class_Control>`{.interpreted-text role="ref"}s. The events
assigned to the action can however be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/buffering/agile_event_flushing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/buffering/agile_event_flushing** = `false`
`🔗<class_ProjectSettings_property_input_devices/buffering/agile_event_flushing>`{.interpreted-text
role="ref"}

If `true`, key/touch/joystick events will be flushed just before every
idle and physics frame.

If `false`, such events will be flushed only once per process frame,
between iterations of the engine.

Enabling this can greatly improve the responsiveness to input, specially
in devices that need to run multiple physics frames per visible
(process) frame, because they can\'t run at the target frame rate.

\*\*Note:\*\* Currently implemented only on Android.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/compatibility/legacy_just_pressed_behavior}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/compatibility/legacy_just_pressed_behavior** = `false`
`🔗<class_ProjectSettings_property_input_devices/compatibility/legacy_just_pressed_behavior>`{.interpreted-text
role="ref"}

If `true`,
`Input.is_action_just_pressed()<class_Input_method_is_action_just_pressed>`{.interpreted-text
role="ref"} and
`Input.is_action_just_released()<class_Input_method_is_action_just_released>`{.interpreted-text
role="ref"} will only return `true` if the action is still in the
respective state, i.e. an action that is pressed *and* released on the
same frame will be missed.

If `false`, no input will be lost.

\*\*Note:\*\* You should in nearly all cases prefer the `false` setting.
The legacy behavior is to enable supporting old projects that rely on
the old logic, without changes to script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/pen_tablet/driver}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**input_devices/pen_tablet/driver**
`🔗<class_ProjectSettings_property_input_devices/pen_tablet/driver>`{.interpreted-text
role="ref"}

Specifies the tablet driver to use. If left empty, the default driver
will be used.

\*\*Note:\*\* The driver in use can be overridden at runtime via the
`--tablet-driver`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

\*\*Note:\*\* Use
`DisplayServer.tablet_set_current_driver()<class_DisplayServer_method_tablet_set_current_driver>`{.interpreted-text
role="ref"} to switch tablet driver in runtime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/pen_tablet/driver.windows}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**input_devices/pen_tablet/driver.windows**
`🔗<class_ProjectSettings_property_input_devices/pen_tablet/driver.windows>`{.interpreted-text
role="ref"}

Override for
`input_devices/pen_tablet/driver<class_ProjectSettings_property_input_devices/pen_tablet/driver>`{.interpreted-text
role="ref"} on Windows. Supported values are:

- `auto` (default), uses `wintab` if Windows Ink is disabled in the
  Wacom Tablet Properties or system settings, `winink` otherwise.
- `winink`, uses Windows native \"Windows Ink\" driver.
- `wintab`, uses Wacom \"WinTab\" driver.
- `dummy`, tablet input is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/pointing/android/disable_scroll_deadzone}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/pointing/android/disable_scroll_deadzone** = `false`
`🔗<class_ProjectSettings_property_input_devices/pointing/android/disable_scroll_deadzone>`{.interpreted-text
role="ref"}

If `true`, disables the scroll deadzone on Android, allowing even very
small scroll movements to be registered. This may increase scroll
sensitivity but can also lead to unintended scrolling from slight finger
movements.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/pointing/android/enable_long_press_as_right_click}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/pointing/android/enable_long_press_as_right_click** =
`false`
`🔗<class_ProjectSettings_property_input_devices/pointing/android/enable_long_press_as_right_click>`{.interpreted-text
role="ref"}

If `true`, long press events on an Android touchscreen are transformed
into right click events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/pointing/android/enable_pan_and_scale_gestures}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/pointing/android/enable_pan_and_scale_gestures** =
`false`
`🔗<class_ProjectSettings_property_input_devices/pointing/android/enable_pan_and_scale_gestures>`{.interpreted-text
role="ref"}

If `true`, multi-touch pan and scale gestures are enabled on Android
devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/pointing/android/override_volume_buttons}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/pointing/android/override_volume_buttons** = `false`
`🔗<class_ProjectSettings_property_input_devices/pointing/android/override_volume_buttons>`{.interpreted-text
role="ref"}

If `true`, system volume changes are disabled when the buttons are used
within the app.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/pointing/android/rotary_input_scroll_axis}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**input_devices/pointing/android/rotary_input_scroll_axis** = `1`
`🔗<class_ProjectSettings_property_input_devices/pointing/android/rotary_input_scroll_axis>`{.interpreted-text
role="ref"}

On Wear OS devices, defines which axis of the mouse wheel rotary input
is mapped to. This rotary input is usually performed by rotating the
physical or virtual (touch-based) bezel on a smartwatch.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/pointing/emulate_mouse_from_touch}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/pointing/emulate_mouse_from_touch** = `true`
`🔗<class_ProjectSettings_property_input_devices/pointing/emulate_mouse_from_touch>`{.interpreted-text
role="ref"}

If `true`, sends mouse input events when tapping or swiping on the
touchscreen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/pointing/emulate_touch_from_mouse** = `false`
`🔗<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>`{.interpreted-text
role="ref"}

If `true`, sends touch input events when clicking or dragging the mouse.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/sensors/enable_accelerometer}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/sensors/enable_accelerometer** = `false`
`🔗<class_ProjectSettings_property_input_devices/sensors/enable_accelerometer>`{.interpreted-text
role="ref"}

If `true`, the accelerometer sensor is enabled and
`Input.get_accelerometer()<class_Input_method_get_accelerometer>`{.interpreted-text
role="ref"} returns valid data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/sensors/enable_gravity}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/sensors/enable_gravity** = `false`
`🔗<class_ProjectSettings_property_input_devices/sensors/enable_gravity>`{.interpreted-text
role="ref"}

If `true`, the gravity sensor is enabled and
`Input.get_gravity()<class_Input_method_get_gravity>`{.interpreted-text
role="ref"} returns valid data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/sensors/enable_gyroscope}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/sensors/enable_gyroscope** = `false`
`🔗<class_ProjectSettings_property_input_devices/sensors/enable_gyroscope>`{.interpreted-text
role="ref"}

If `true`, the gyroscope sensor is enabled and
`Input.get_gyroscope()<class_Input_method_get_gyroscope>`{.interpreted-text
role="ref"} returns valid data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_input_devices/sensors/enable_magnetometer}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input_devices/sensors/enable_magnetometer** = `false`
`🔗<class_ProjectSettings_property_input_devices/sensors/enable_magnetometer>`{.interpreted-text
role="ref"}

If `true`, the magnetometer sensor is enabled and
`Input.get_magnetometer()<class_Input_method_get_magnetometer>`{.interpreted-text
role="ref"} returns valid data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/locale/fallback}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**internationalization/locale/fallback** = `"en"`
`🔗<class_ProjectSettings_property_internationalization/locale/fallback>`{.interpreted-text
role="ref"}

The locale to fall back to if a translation isn\'t available in a given
language. If left empty, `en` (English) will be used.

\*\*Note:\*\* Not to be confused with
`TextServerFallback<class_TextServerFallback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/locale/include_text_server_data}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**internationalization/locale/include_text_server_data** = `false`
`🔗<class_ProjectSettings_property_internationalization/locale/include_text_server_data>`{.interpreted-text
role="ref"}

If `true`, text server break iteration rule sets, dictionaries and other
optional data are included in the exported project.

\*\*Note:\*\* \"ICU / HarfBuzz / Graphite\" text server data includes
dictionaries for Burmese, Chinese, Japanese, Khmer, Lao and Thai as well
as Unicode Standard Annex #29 and Unicode Standard Annex #14 word and
line breaking rules. Data is about 4 MB large.

\*\*Note:\*\*
`TextServerFallback<class_TextServerFallback>`{.interpreted-text
role="ref"} does not use additional data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/locale/line_breaking_strictness}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**internationalization/locale/line_breaking_strictness** = `0`
`🔗<class_ProjectSettings_property_internationalization/locale/line_breaking_strictness>`{.interpreted-text
role="ref"}

Default strictness of line-breaking rules. Can be overridden by adding
`@lb={auto,loose,normal,strict}` to the language code.

- **Auto** (`0`) - strictness is based on the length of the line.
- **Loose** (`1`) - the least restrictive set of line-breaking rules.
  Typically used for short lines.
- **Normal** (`2`) - the most common set of line-breaking rules.
- **Strict** (`3`) - the most stringent set of line-breaking rules.

See [Line Breaking Strictness: the line-break
property](https://www.w3.org/TR/css-text-3/#line-break-property) for
more info.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/locale/test}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**internationalization/locale/test** = `""`
`🔗<class_ProjectSettings_property_internationalization/locale/test>`{.interpreted-text
role="ref"}

If non-empty, this locale will be used instead of the automatically
detected system locale.

\*\*Note:\*\* This setting also applies to the exported project. To only
affect testing within the editor, override this setting with an `editor`
`feature tag <../tutorials/export/feature_tags>`{.interpreted-text
role="doc"} for localization testing purposes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/pseudolocalization/double_vowels}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**internationalization/pseudolocalization/double_vowels** = `false`
`🔗<class_ProjectSettings_property_internationalization/pseudolocalization/double_vowels>`{.interpreted-text
role="ref"}

Double vowels in strings during pseudolocalization to simulate the
lengthening of text due to localization.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/pseudolocalization/expansion_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**internationalization/pseudolocalization/expansion_ratio** = `0.0`
`🔗<class_ProjectSettings_property_internationalization/pseudolocalization/expansion_ratio>`{.interpreted-text
role="ref"}

The expansion ratio to use during pseudolocalization. A value of `0.3`
is sufficient for most practical purposes, and will increase the length
of each string by 30%.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/pseudolocalization/fake_bidi}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**internationalization/pseudolocalization/fake_bidi** = `false`
`🔗<class_ProjectSettings_property_internationalization/pseudolocalization/fake_bidi>`{.interpreted-text
role="ref"}

If `true`, emulate bidirectional (right-to-left) text when
pseudolocalization is enabled. This can be used to spot issues with RTL
layout and UI mirroring that will crop up if the project is localized to
RTL languages such as Arabic or Hebrew. See also
`internationalization/rendering/force_right_to_left_layout_direction<class_ProjectSettings_property_internationalization/rendering/force_right_to_left_layout_direction>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/pseudolocalization/override}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**internationalization/pseudolocalization/override** = `false`
`🔗<class_ProjectSettings_property_internationalization/pseudolocalization/override>`{.interpreted-text
role="ref"}

Replace all characters in the string with `*`. Useful for finding
non-localizable strings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/pseudolocalization/prefix}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**internationalization/pseudolocalization/prefix** = `"["`
`🔗<class_ProjectSettings_property_internationalization/pseudolocalization/prefix>`{.interpreted-text
role="ref"}

Prefix that will be prepended to the pseudolocalized string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/pseudolocalization/replace_with_accents}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**internationalization/pseudolocalization/replace_with_accents** =
`true`
`🔗<class_ProjectSettings_property_internationalization/pseudolocalization/replace_with_accents>`{.interpreted-text
role="ref"}

Replace all characters with their accented variants during
pseudolocalization.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/pseudolocalization/skip_placeholders}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**internationalization/pseudolocalization/skip_placeholders** = `true`
`🔗<class_ProjectSettings_property_internationalization/pseudolocalization/skip_placeholders>`{.interpreted-text
role="ref"}

Skip placeholders for string formatting like `%s` or `%f` during
pseudolocalization. Useful to identify strings which need additional
control characters to display correctly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/pseudolocalization/suffix}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**internationalization/pseudolocalization/suffix** = `"]"`
`🔗<class_ProjectSettings_property_internationalization/pseudolocalization/suffix>`{.interpreted-text
role="ref"}

Suffix that will be appended to the pseudolocalized string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/pseudolocalization/use_pseudolocalization}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**internationalization/pseudolocalization/use_pseudolocalization** =
`false`
`🔗<class_ProjectSettings_property_internationalization/pseudolocalization/use_pseudolocalization>`{.interpreted-text
role="ref"}

If `true`, enables pseudolocalization for the project. This can be used
to spot untranslatable strings or layout issues that may occur once the
project is localized to languages that have longer strings than the
source language.

\*\*Note:\*\* This property is only read when the project starts. To
toggle pseudolocalization at run-time, use
`TranslationServer.pseudolocalization_enabled<class_TranslationServer_property_pseudolocalization_enabled>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/rendering/force_right_to_left_layout_direction}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**internationalization/rendering/force_right_to_left_layout_direction**
= `false`
`🔗<class_ProjectSettings_property_internationalization/rendering/force_right_to_left_layout_direction>`{.interpreted-text
role="ref"}

Force layout direction and text writing direction to RTL for all
controls, even if the current locale is intended to use a left-to-right
layout and text writing direction. This should be enabled for testing
purposes only. See also
`internationalization/pseudolocalization/fake_bidi<class_ProjectSettings_property_internationalization/pseudolocalization/fake_bidi>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/rendering/root_node_auto_translate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**internationalization/rendering/root_node_auto_translate** = `true`
`🔗<class_ProjectSettings_property_internationalization/rendering/root_node_auto_translate>`{.interpreted-text
role="ref"}

If `true`, root node will use
`Node.AUTO_TRANSLATE_MODE_ALWAYS<class_Node_constant_AUTO_TRANSLATE_MODE_ALWAYS>`{.interpreted-text
role="ref"}, otherwise
`Node.AUTO_TRANSLATE_MODE_DISABLED<class_Node_constant_AUTO_TRANSLATE_MODE_DISABLED>`{.interpreted-text
role="ref"} will be used.

\*\*Note:\*\* This property is only read when the project starts. To
change the auto translate mode at runtime, set
`Node.auto_translate_mode<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"} of
`SceneTree.root<class_SceneTree_property_root>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/rendering/root_node_layout_direction}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**internationalization/rendering/root_node_layout_direction** = `0`
`🔗<class_ProjectSettings_property_internationalization/rendering/root_node_layout_direction>`{.interpreted-text
role="ref"}

Root node default layout direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_internationalization/rendering/text_driver}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**internationalization/rendering/text_driver** = `""`
`🔗<class_ProjectSettings_property_internationalization/rendering/text_driver>`{.interpreted-text
role="ref"}

Specifies the `TextServer<class_TextServer>`{.interpreted-text
role="ref"} to use. If left empty, the default will be used.

\"ICU / HarfBuzz / Graphite\"
(`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"}) is the most advanced text driver, supporting right-to-left
typesetting and complex scripts (for languages like Arabic, Hebrew,
etc.). The \"Fallback\" text driver
(`TextServerFallback<class_TextServerFallback>`{.interpreted-text
role="ref"}) does not support right-to-left typesetting and complex
scripts.

\*\*Note:\*\* The driver in use can be overridden at runtime via the
`--text-driver`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

\*\*Note:\*\* There is an additional `Dummy` text driver available,
which disables all text rendering and font-related functionality. This
driver is not listed in the project settings, but it can be enabled when
running the editor or project using the `--text-driver Dummy`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_1}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_1** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_1>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 1. If left empty, the layer
will display as \"Layer 1\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_2}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_2** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_2>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 2. If left empty, the layer
will display as \"Layer 2\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_3}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_3** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_3>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 3. If left empty, the layer
will display as \"Layer 3\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_4}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_4** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_4>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 4. If left empty, the layer
will display as \"Layer 4\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_5}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_5** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_5>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 5. If left empty, the layer
will display as \"Layer 5\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_6}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_6** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_6>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 6. If left empty, the layer
will display as \"Layer 6\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_7}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_7** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_7>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 7. If left empty, the layer
will display as \"Layer 7\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_8}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_8** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_8>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 8. If left empty, the layer
will display as \"Layer 8\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_9}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_9** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_9>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 9. If left empty, the layer
will display as \"Layer 9\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_10}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_10** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_10>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 10. If left empty, the layer
will display as \"Layer 10\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_11}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_11** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_11>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 11. If left empty, the layer
will display as \"Layer 11\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_12}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_12** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_12>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 12. If left empty, the layer
will display as \"Layer 12\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_13}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_13** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_13>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 13. If left empty, the layer
will display as \"Layer 13\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_14}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_14** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_14>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 14. If left empty, the layer
will display as \"Layer 14\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_15}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_15** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_15>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 15. If left empty, the layer
will display as \"Layer 15\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_16}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_16** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_16>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 16. If left empty, the layer
will display as \"Layer 16\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_17}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_17** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_17>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 17. If left empty, the layer
will display as \"Layer 17\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_18}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_18** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_18>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 18. If left empty, the layer
will display as \"Layer 18\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_19}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_19** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_19>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 19. If left empty, the layer
will display as \"Layer 19\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_20}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_20** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_20>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 20. If left empty, the layer
will display as \"Layer 20\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_21}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_21** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_21>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 21. If left empty, the layer
will display as \"Layer 21\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_22}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_22** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_22>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 22. If left empty, the layer
will display as \"Layer 22\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_23}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_23** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_23>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 23. If left empty, the layer
will display as \"Layer 23\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_24}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_24** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_24>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 24. If left empty, the layer
will display as \"Layer 24\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_25}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_25** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_25>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 25. If left empty, the layer
will display as \"Layer 25\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_26}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_26** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_26>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 26. If left empty, the layer
will display as \"Layer 26\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_27}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_27** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_27>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 27. If left empty, the layer
will display as \"Layer 27\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_28}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_28** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_28>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 28. If left empty, the layer
will display as \"Layer 28\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_29}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_29** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_29>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 29. If left empty, the layer
will display as \"Layer 29\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_30}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_30** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_30>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 30. If left empty, the layer
will display as \"Layer 30\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_31}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_31** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_31>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 31. If left empty, the layer
will display as \"Layer 31\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_navigation/layer_32}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_navigation/layer_32** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_navigation/layer_32>`{.interpreted-text
role="ref"}

Optional name for the 2D navigation layer 32. If left empty, the layer
will display as \"Layer 32\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_1}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_1** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_1>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 1. If left empty, the layer will
display as \"Layer 1\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_2}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_2** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_2>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 2. If left empty, the layer will
display as \"Layer 2\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_3}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_3** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_3>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 3. If left empty, the layer will
display as \"Layer 3\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_4}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_4** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_4>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 4. If left empty, the layer will
display as \"Layer 4\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_5}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_5** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_5>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 5. If left empty, the layer will
display as \"Layer 5\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_6}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_6** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_6>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 6. If left empty, the layer will
display as \"Layer 6\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_7}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_7** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_7>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 7. If left empty, the layer will
display as \"Layer 7\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_8}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_8** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_8>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 8. If left empty, the layer will
display as \"Layer 8\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_9}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_9** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_9>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 9. If left empty, the layer will
display as \"Layer 9\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_10}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_10** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_10>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 10. If left empty, the layer will
display as \"Layer 10\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_11}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_11** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_11>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 11. If left empty, the layer will
display as \"Layer 11\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_12}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_12** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_12>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 12. If left empty, the layer will
display as \"Layer 12\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_13}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_13** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_13>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 13. If left empty, the layer will
display as \"Layer 13\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_14}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_14** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_14>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 14. If left empty, the layer will
display as \"Layer 14\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_15}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_15** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_15>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 15. If left empty, the layer will
display as \"Layer 15\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_16}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_16** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_16>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 16. If left empty, the layer will
display as \"Layer 16\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_17}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_17** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_17>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 17. If left empty, the layer will
display as \"Layer 17\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_18}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_18** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_18>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 18. If left empty, the layer will
display as \"Layer 18\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_19}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_19** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_19>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 19. If left empty, the layer will
display as \"Layer 19\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_20}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_20** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_20>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 20. If left empty, the layer will
display as \"Layer 20\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_21}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_21** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_21>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 21. If left empty, the layer will
display as \"Layer 21\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_22}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_22** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_22>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 22. If left empty, the layer will
display as \"Layer 22\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_23}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_23** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_23>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 23. If left empty, the layer will
display as \"Layer 23\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_24}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_24** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_24>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 24. If left empty, the layer will
display as \"Layer 24\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_25}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_25** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_25>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 25. If left empty, the layer will
display as \"Layer 25\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_26}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_26** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_26>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 26. If left empty, the layer will
display as \"Layer 26\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_27}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_27** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_27>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 27. If left empty, the layer will
display as \"Layer 27\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_28}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_28** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_28>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 28. If left empty, the layer will
display as \"Layer 28\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_29}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_29** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_29>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 29. If left empty, the layer will
display as \"Layer 29\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_30}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_30** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_30>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 30. If left empty, the layer will
display as \"Layer 30\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_31}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_31** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_31>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 31. If left empty, the layer will
display as \"Layer 31\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_physics/layer_32}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_physics/layer_32** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_physics/layer_32>`{.interpreted-text
role="ref"}

Optional name for the 2D physics layer 32. If left empty, the layer will
display as \"Layer 32\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_1}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_1** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_1>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 1. If left empty, the layer will
display as \"Layer 1\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_2}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_2** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_2>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 2. If left empty, the layer will
display as \"Layer 2\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_3}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_3** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_3>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 3. If left empty, the layer will
display as \"Layer 3\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_4}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_4** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_4>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 4. If left empty, the layer will
display as \"Layer 4\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_5}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_5** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_5>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 5. If left empty, the layer will
display as \"Layer 5\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_6}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_6** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_6>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 6. If left empty, the layer will
display as \"Layer 6\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_7}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_7** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_7>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 7. If left empty, the layer will
display as \"Layer 7\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_8}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_8** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_8>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 8. If left empty, the layer will
display as \"Layer 8\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_9}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_9** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_9>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 9. If left empty, the layer will
display as \"Layer 9\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_10}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_10** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_10>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 10. If left empty, the layer will
display as \"Layer 10\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_11}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_11** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_11>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 11. If left empty, the layer will
display as \"Layer 11\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_12}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_12** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_12>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 12. If left empty, the layer will
display as \"Layer 12\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_13}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_13** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_13>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 13. If left empty, the layer will
display as \"Layer 13\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_14}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_14** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_14>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 14. If left empty, the layer will
display as \"Layer 14\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_15}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_15** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_15>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 15. If left empty, the layer will
display as \"Layer 15\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_16}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_16** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_16>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 16. If left empty, the layer will
display as \"Layer 16\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_17}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_17** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_17>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 17. If left empty, the layer will
display as \"Layer 17\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_18}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_18** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_18>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 18. If left empty, the layer will
display as \"Layer 18\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_19}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_19** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_19>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 19. If left empty, the layer will
display as \"Layer 19\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/2d_render/layer_20}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/2d_render/layer_20** = `""`
`🔗<class_ProjectSettings_property_layer_names/2d_render/layer_20>`{.interpreted-text
role="ref"}

Optional name for the 2D render layer 20. If left empty, the layer will
display as \"Layer 20\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_1}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_1** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_1>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 1. If left empty, the layer
will display as \"Layer 1\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_2}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_2** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_2>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 2. If left empty, the layer
will display as \"Layer 2\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_3}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_3** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_3>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 3. If left empty, the layer
will display as \"Layer 3\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_4}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_4** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_4>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 4. If left empty, the layer
will display as \"Layer 4\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_5}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_5** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_5>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 5. If left empty, the layer
will display as \"Layer 5\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_6}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_6** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_6>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 6. If left empty, the layer
will display as \"Layer 6\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_7}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_7** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_7>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 7. If left empty, the layer
will display as \"Layer 7\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_8}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_8** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_8>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 8. If left empty, the layer
will display as \"Layer 8\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_9}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_9** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_9>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 9. If left empty, the layer
will display as \"Layer 9\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_10}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_10** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_10>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 10. If left empty, the layer
will display as \"Layer 10\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_11}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_11** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_11>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 11. If left empty, the layer
will display as \"Layer 11\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_12}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_12** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_12>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 12. If left empty, the layer
will display as \"Layer 12\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_13}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_13** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_13>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 13. If left empty, the layer
will display as \"Layer 13\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_14}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_14** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_14>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 14. If left empty, the layer
will display as \"Layer 14\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_15}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_15** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_15>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 15. If left empty, the layer
will display as \"Layer 15\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_16}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_16** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_16>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 16. If left empty, the layer
will display as \"Layer 16\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_17}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_17** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_17>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 17. If left empty, the layer
will display as \"Layer 17\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_18}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_18** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_18>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 18. If left empty, the layer
will display as \"Layer 18\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_19}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_19** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_19>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 19. If left empty, the layer
will display as \"Layer 19\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_20}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_20** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_20>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 20. If left empty, the layer
will display as \"Layer 20\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_21}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_21** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_21>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 21. If left empty, the layer
will display as \"Layer 21\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_22}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_22** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_22>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 22. If left empty, the layer
will display as \"Layer 22\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_23}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_23** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_23>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 23. If left empty, the layer
will display as \"Layer 23\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_24}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_24** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_24>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 24. If left empty, the layer
will display as \"Layer 24\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_25}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_25** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_25>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 25. If left empty, the layer
will display as \"Layer 25\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_26}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_26** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_26>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 26. If left empty, the layer
will display as \"Layer 26\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_27}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_27** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_27>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 27. If left empty, the layer
will display as \"Layer 27\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_28}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_28** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_28>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 28. If left empty, the layer
will display as \"Layer 28\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_29}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_29** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_29>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 29. If left empty, the layer
will display as \"Layer 29\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_30}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_30** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_30>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 30. If left empty, the layer
will display as \"Layer 30\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_31}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_31** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_31>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 31. If left empty, the layer
will display as \"Layer 31\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_navigation/layer_32}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_navigation/layer_32** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_navigation/layer_32>`{.interpreted-text
role="ref"}

Optional name for the 3D navigation layer 32. If left empty, the layer
will display as \"Layer 32\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_1}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_1** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_1>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 1. If left empty, the layer will
display as \"Layer 1\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_2}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_2** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_2>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 2. If left empty, the layer will
display as \"Layer 2\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_3}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_3** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_3>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 3. If left empty, the layer will
display as \"Layer 3\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_4}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_4** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_4>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 4. If left empty, the layer will
display as \"Layer 4\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_5}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_5** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_5>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 5. If left empty, the layer will
display as \"Layer 5\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_6}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_6** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_6>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 6. If left empty, the layer will
display as \"Layer 6\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_7}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_7** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_7>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 7. If left empty, the layer will
display as \"Layer 7\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_8}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_8** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_8>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 8. If left empty, the layer will
display as \"Layer 8\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_9}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_9** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_9>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 9. If left empty, the layer will
display as \"Layer 9\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_10}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_10** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_10>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 10. If left empty, the layer will
display as \"Layer 10\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_11}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_11** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_11>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 11. If left empty, the layer will
display as \"Layer 11\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_12}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_12** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_12>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 12. If left empty, the layer will
display as \"Layer 12\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_13}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_13** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_13>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 13. If left empty, the layer will
display as \"Layer 13\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_14}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_14** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_14>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 14. If left empty, the layer will
display as \"Layer 14\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_15}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_15** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_15>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 15. If left empty, the layer will
display as \"Layer 15\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_16}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_16** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_16>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 16. If left empty, the layer will
display as \"Layer 16\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_17}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_17** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_17>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 17. If left empty, the layer will
display as \"Layer 17\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_18}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_18** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_18>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 18. If left empty, the layer will
display as \"Layer 18\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_19}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_19** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_19>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 19. If left empty, the layer will
display as \"Layer 19\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_20}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_20** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_20>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 20. If left empty, the layer will
display as \"Layer 20\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_21}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_21** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_21>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 21. If left empty, the layer will
display as \"Layer 21\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_22}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_22** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_22>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 22. If left empty, the layer will
display as \"Layer 22\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_23}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_23** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_23>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 23. If left empty, the layer will
display as \"Layer 23\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_24}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_24** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_24>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 24. If left empty, the layer will
display as \"Layer 24\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_25}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_25** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_25>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 25. If left empty, the layer will
display as \"Layer 25\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_26}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_26** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_26>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 26. If left empty, the layer will
display as \"Layer 26\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_27}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_27** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_27>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 27. If left empty, the layer will
display as \"Layer 27\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_28}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_28** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_28>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 28. If left empty, the layer will
display as \"Layer 28\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_29}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_29** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_29>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 29. If left empty, the layer will
display as \"Layer 29\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_30}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_30** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_30>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 30. If left empty, the layer will
display as \"Layer 30\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_31}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_31** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_31>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 31. If left empty, the layer will
display as \"Layer 31\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_physics/layer_32}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_physics/layer_32** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_physics/layer_32>`{.interpreted-text
role="ref"}

Optional name for the 3D physics layer 32. If left empty, the layer will
display as \"Layer 32\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_1}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_1** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_1>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 1. If left empty, the layer will
display as \"Layer 1\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_2}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_2** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_2>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 2. If left empty, the layer will
display as \"Layer 2\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_3}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_3** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_3>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 3. If left empty, the layer will
display as \"Layer 3\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_4}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_4** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_4>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 4. If left empty, the layer will
display as \"Layer 4\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_5}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_5** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_5>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 5. If left empty, the layer will
display as \"Layer 5\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_6}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_6** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_6>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 6. If left empty, the layer will
display as \"Layer 6\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_7}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_7** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_7>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 7. If left empty, the layer will
display as \"Layer 7\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_8}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_8** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_8>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 8. If left empty, the layer will
display as \"Layer 8\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_9}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_9** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_9>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 9. If left empty, the layer will
display as \"Layer 9\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_10}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_10** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_10>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 10. If left empty, the layer will
display as \"Layer 10\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_11}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_11** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_11>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 11. If left empty, the layer will
display as \"Layer 11\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_12}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_12** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_12>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 12. If left empty, the layer will
display as \"Layer 12\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_13}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_13** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_13>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 13. If left empty, the layer will
display as \"Layer 13\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_14}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_14** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_14>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 14. If left empty, the layer will
display as \"Layer 14\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_15}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_15** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_15>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 15. If left empty, the layer will
display as \"Layer 15\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_16}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_16** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_16>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 16. If left empty, the layer will
display as \"Layer 16\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_17}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_17** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_17>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 17. If left empty, the layer will
display as \"Layer 17\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_18}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_18** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_18>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 18. If left empty, the layer will
display as \"Layer 18\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_19}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_19** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_19>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 19. If left empty, the layer will
display as \"Layer 19\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/3d_render/layer_20}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/3d_render/layer_20** = `""`
`🔗<class_ProjectSettings_property_layer_names/3d_render/layer_20>`{.interpreted-text
role="ref"}

Optional name for the 3D render layer 20. If left empty, the layer will
display as \"Layer 20\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_1}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_1** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_1>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 1. If left empty, the
layer will display as \"Layer 1\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_2}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_2** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_2>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 2. If left empty, the
layer will display as \"Layer 2\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_3}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_3** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_3>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 3. If left empty, the
layer will display as \"Layer 3\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_4}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_4** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_4>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 4. If left empty, the
layer will display as \"Layer 4\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_5}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_5** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_5>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 5. If left empty, the
layer will display as \"Layer 5\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_6}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_6** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_6>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 6. If left empty, the
layer will display as \"Layer 6\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_7}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_7** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_7>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 7. If left empty, the
layer will display as \"Layer 7\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_8}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_8** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_8>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 8. If left empty, the
layer will display as \"Layer 8\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_9}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_9** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_9>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 9. If left empty, the
layer will display as \"Layer 9\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_10}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_10** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_10>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 10. If left empty, the
layer will display as \"Layer 10\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_11}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_11** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_11>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 11. If left empty, the
layer will display as \"Layer 11\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_12}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_12** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_12>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 12. If left empty, the
layer will display as \"Layer 12\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_13}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_13** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_13>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 13. If left empty, the
layer will display as \"Layer 13\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_14}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_14** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_14>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 14. If left empty, the
layer will display as \"Layer 14\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_15}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_15** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_15>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 15. If left empty, the
layer will display as \"Layer 15\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_16}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_16** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_16>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 16. If left empty, the
layer will display as \"Layer 16\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_17}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_17** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_17>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 17. If left empty, the
layer will display as \"Layer 17\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_18}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_18** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_18>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 18. If left empty, the
layer will display as \"Layer 18\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_19}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_19** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_19>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 19. If left empty, the
layer will display as \"Layer 19\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_20}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_20** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_20>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 20. If left empty, the
layer will display as \"Layer 20\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_21}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_21** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_21>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 21. If left empty, the
layer will display as \"Layer 21\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_22}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_22** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_22>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 22. If left empty, the
layer will display as \"Layer 22\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_23}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_23** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_23>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 23. If left empty, the
layer will display as \"Layer 23\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_24}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_24** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_24>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 24. If left empty, the
layer will display as \"Layer 24\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_25}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_25** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_25>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 25. If left empty, the
layer will display as \"Layer 25\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_26}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_26** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_26>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 26. If left empty, the
layer will display as \"Layer 26\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_27}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_27** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_27>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 27. If left empty, the
layer will display as \"Layer 27\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_28}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_28** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_28>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 28. If left empty, the
layer will display as \"Layer 28\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_29}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_29** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_29>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 29. If left empty, the
layer will display as \"Layer 29\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_30}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_30** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_30>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 30. If left empty, the
layer will display as \"Layer 30\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_31}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_31** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_31>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 31. If left empty, the
layer will display as \"Layer 31\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_layer_names/avoidance/layer_32}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**layer_names/avoidance/layer_32** = `""`
`🔗<class_ProjectSettings_property_layer_names/avoidance/layer_32>`{.interpreted-text
role="ref"}

Optional name for the navigation avoidance layer 32. If left empty, the
layer will display as \"Layer 32\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_memory/limits/message_queue/max_size_mb}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**memory/limits/message_queue/max_size_mb** = `32`
`🔗<class_ProjectSettings_property_memory/limits/message_queue/max_size_mb>`{.interpreted-text
role="ref"}

Godot uses a message queue to defer some function calls. If you run out
of space on it (you will see an error), you can increase the size here.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/2d/default_cell_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**navigation/2d/default_cell_size** = `1.0`
`🔗<class_ProjectSettings_property_navigation/2d/default_cell_size>`{.interpreted-text
role="ref"}

Default cell size for 2D navigation maps. See
`NavigationServer2D.map_set_cell_size()<class_NavigationServer2D_method_map_set_cell_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/2d/default_edge_connection_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**navigation/2d/default_edge_connection_margin** = `1.0`
`🔗<class_ProjectSettings_property_navigation/2d/default_edge_connection_margin>`{.interpreted-text
role="ref"}

Default edge connection margin for 2D navigation maps. See
`NavigationServer2D.map_set_edge_connection_margin()<class_NavigationServer2D_method_map_set_edge_connection_margin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/2d/default_link_connection_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**navigation/2d/default_link_connection_radius** = `4.0`
`🔗<class_ProjectSettings_property_navigation/2d/default_link_connection_radius>`{.interpreted-text
role="ref"}

Default link connection radius for 2D navigation maps. See
`NavigationServer2D.map_set_link_connection_radius()<class_NavigationServer2D_method_map_set_link_connection_radius>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/2d/merge_rasterizer_cell_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**navigation/2d/merge_rasterizer_cell_scale** = `1.0`
`🔗<class_ProjectSettings_property_navigation/2d/merge_rasterizer_cell_scale>`{.interpreted-text
role="ref"}

Default merge rasterizer cell scale for 2D navigation maps. See
`NavigationServer2D.map_set_merge_rasterizer_cell_scale()<class_NavigationServer2D_method_map_set_merge_rasterizer_cell_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/2d/use_edge_connections}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**navigation/2d/use_edge_connections** = `true`
`🔗<class_ProjectSettings_property_navigation/2d/use_edge_connections>`{.interpreted-text
role="ref"}

If enabled 2D navigation regions will use edge connections to connect
with other navigation regions within proximity of the navigation map
edge connection margin. This setting only affects World2D default
navigation maps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/3d/default_cell_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**navigation/3d/default_cell_height** = `0.25`
`🔗<class_ProjectSettings_property_navigation/3d/default_cell_height>`{.interpreted-text
role="ref"}

Default cell height for 3D navigation maps. See
`NavigationServer3D.map_set_cell_height()<class_NavigationServer3D_method_map_set_cell_height>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/3d/default_cell_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**navigation/3d/default_cell_size** = `0.25`
`🔗<class_ProjectSettings_property_navigation/3d/default_cell_size>`{.interpreted-text
role="ref"}

Default cell size for 3D navigation maps. See
`NavigationServer3D.map_set_cell_size()<class_NavigationServer3D_method_map_set_cell_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/3d/default_edge_connection_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**navigation/3d/default_edge_connection_margin** = `0.25`
`🔗<class_ProjectSettings_property_navigation/3d/default_edge_connection_margin>`{.interpreted-text
role="ref"}

Default edge connection margin for 3D navigation maps. See
`NavigationServer3D.map_set_edge_connection_margin()<class_NavigationServer3D_method_map_set_edge_connection_margin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/3d/default_link_connection_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**navigation/3d/default_link_connection_radius** = `1.0`
`🔗<class_ProjectSettings_property_navigation/3d/default_link_connection_radius>`{.interpreted-text
role="ref"}

Default link connection radius for 3D navigation maps. See
`NavigationServer3D.map_set_link_connection_radius()<class_NavigationServer3D_method_map_set_link_connection_radius>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/3d/default_up}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**navigation/3d/default_up** = `Vector3(0, 1, 0)`
`🔗<class_ProjectSettings_property_navigation/3d/default_up>`{.interpreted-text
role="ref"}

Default up orientation for 3D navigation maps. See
`NavigationServer3D.map_set_up()<class_NavigationServer3D_method_map_set_up>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/3d/merge_rasterizer_cell_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**navigation/3d/merge_rasterizer_cell_scale** = `1.0`
`🔗<class_ProjectSettings_property_navigation/3d/merge_rasterizer_cell_scale>`{.interpreted-text
role="ref"}

Default merge rasterizer cell scale for 3D navigation maps. See
`NavigationServer3D.map_set_merge_rasterizer_cell_scale()<class_NavigationServer3D_method_map_set_merge_rasterizer_cell_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/3d/use_edge_connections}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**navigation/3d/use_edge_connections** = `true`
`🔗<class_ProjectSettings_property_navigation/3d/use_edge_connections>`{.interpreted-text
role="ref"}

If enabled 3D navigation regions will use edge connections to connect
with other navigation regions within proximity of the navigation map
edge connection margin. This setting only affects World3D default
navigation maps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/avoidance/thread_model/avoidance_use_high_priority_threads}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**navigation/avoidance/thread_model/avoidance_use_high_priority_threads**
= `true`
`🔗<class_ProjectSettings_property_navigation/avoidance/thread_model/avoidance_use_high_priority_threads>`{.interpreted-text
role="ref"}

If enabled and avoidance calculations use multiple threads the threads
run with high priority.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/avoidance/thread_model/avoidance_use_multiple_threads}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**navigation/avoidance/thread_model/avoidance_use_multiple_threads** =
`true`
`🔗<class_ProjectSettings_property_navigation/avoidance/thread_model/avoidance_use_multiple_threads>`{.interpreted-text
role="ref"}

If enabled the avoidance calculations use multiple threads.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/baking/thread_model/baking_use_high_priority_threads}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**navigation/baking/thread_model/baking_use_high_priority_threads** =
`true`
`🔗<class_ProjectSettings_property_navigation/baking/thread_model/baking_use_high_priority_threads>`{.interpreted-text
role="ref"}

If enabled and async navmesh baking uses multiple threads the threads
run with high priority.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/baking/thread_model/baking_use_multiple_threads}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**navigation/baking/thread_model/baking_use_multiple_threads** = `true`
`🔗<class_ProjectSettings_property_navigation/baking/thread_model/baking_use_multiple_threads>`{.interpreted-text
role="ref"}

If enabled the async navmesh baking uses multiple threads.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/baking/use_crash_prevention_checks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**navigation/baking/use_crash_prevention_checks** = `true`
`🔗<class_ProjectSettings_property_navigation/baking/use_crash_prevention_checks>`{.interpreted-text
role="ref"}

If enabled, and baking would potentially lead to an engine crash, the
baking will be interrupted and an error message with explanation will be
raised.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/pathfinding/max_threads}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**navigation/pathfinding/max_threads** = `4`
`🔗<class_ProjectSettings_property_navigation/pathfinding/max_threads>`{.interpreted-text
role="ref"}

Maximum number of threads that can run pathfinding queries
simultaneously on the same pathfinding graph, for example the same
navigation map. Additional threads increase memory consumption and
synchronization time due to the need for extra data copies prepared for
each thread. A value of `-1` means unlimited and the maximum available
OS processor count is used. Defaults to `1` when the OS does not support
threads.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/world/map_use_async_iterations}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**navigation/world/map_use_async_iterations** = `true`
`🔗<class_ProjectSettings_property_navigation/world/map_use_async_iterations>`{.interpreted-text
role="ref"}

If enabled, navigation map synchronization uses an async process that
runs on a background thread. This avoids stalling the main thread but
adds an additional delay to any navigation map change.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_navigation/world/region_use_async_iterations}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**navigation/world/region_use_async_iterations** = `true`
`🔗<class_ProjectSettings_property_navigation/world/region_use_async_iterations>`{.interpreted-text
role="ref"}

If enabled, navigation region synchronization uses an async process that
runs on a background thread. This avoids stalling the main thread but
adds an additional delay to any navigation region change.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_network/limits/debugger/max_chars_per_second}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/limits/debugger/max_chars_per_second** = `32768`
`🔗<class_ProjectSettings_property_network/limits/debugger/max_chars_per_second>`{.interpreted-text
role="ref"}

Maximum number of characters allowed to send as output from the
debugger. Over this value, content is dropped. This helps not to stall
the debugger connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_network/limits/debugger/max_errors_per_second}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/limits/debugger/max_errors_per_second** = `400`
`🔗<class_ProjectSettings_property_network/limits/debugger/max_errors_per_second>`{.interpreted-text
role="ref"}

Maximum number of errors allowed to be sent from the debugger. Over this
value, content is dropped. This helps not to stall the debugger
connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_network/limits/debugger/max_queued_messages}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/limits/debugger/max_queued_messages** = `2048`
`🔗<class_ProjectSettings_property_network/limits/debugger/max_queued_messages>`{.interpreted-text
role="ref"}

Maximum number of messages in the debugger queue. Over this value,
content is dropped. This helps to limit the debugger memory usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_network/limits/debugger/max_warnings_per_second}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/limits/debugger/max_warnings_per_second** = `400`
`🔗<class_ProjectSettings_property_network/limits/debugger/max_warnings_per_second>`{.interpreted-text
role="ref"}

Maximum number of warnings allowed to be sent from the debugger. Over
this value, content is dropped. This helps not to stall the debugger
connection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_network/limits/packet_peer_stream/max_buffer_po2}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/limits/packet_peer_stream/max_buffer_po2** = `16`
`🔗<class_ProjectSettings_property_network/limits/packet_peer_stream/max_buffer_po2>`{.interpreted-text
role="ref"}

Default size of packet peer stream for deserializing Godot data (in
bytes, specified as a power of two). The default value `16` is equal to
65,536 bytes. Over this size, data is dropped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_network/limits/tcp/connect_timeout_seconds}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/limits/tcp/connect_timeout_seconds** = `30`
`🔗<class_ProjectSettings_property_network/limits/tcp/connect_timeout_seconds>`{.interpreted-text
role="ref"}

Timeout (in seconds) for connection attempts using TCP.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_network/limits/webrtc/max_channel_in_buffer_kb}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/limits/webrtc/max_channel_in_buffer_kb** = `64`
`🔗<class_ProjectSettings_property_network/limits/webrtc/max_channel_in_buffer_kb>`{.interpreted-text
role="ref"}

Maximum size (in kiB) for the
`WebRTCDataChannel<class_WebRTCDataChannel>`{.interpreted-text
role="ref"} input buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_network/tls/certificate_bundle_override}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**network/tls/certificate_bundle_override** = `""`
`🔗<class_ProjectSettings_property_network/tls/certificate_bundle_override>`{.interpreted-text
role="ref"}

The CA certificates bundle to use for TLS connections. If this is set to
a non-empty value, this will *override* Godot\'s default [Mozilla
certificate
bundle](https://github.com/godotengine/godot/blob/master/thirdparty/certs/ca-certificates.crt).
If left empty, the default certificate bundle will be used.

If in doubt, leave this setting empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_network/tls/enable_tls_v1.3}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**network/tls/enable_tls_v1.3** = `true`
`🔗<class_ProjectSettings_property_network/tls/enable_tls_v1.3>`{.interpreted-text
role="ref"}

If `true`, enable TLSv1.3 negotiation.

\*\*Note:\*\* Only supported when using Mbed TLS 3.0 or later (Linux
distribution packages may be compiled against older system Mbed TLS
packages), otherwise the maximum supported TLS version is always
TLSv1.2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/default_angular_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/default_angular_damp** = `1.0`
`🔗<class_ProjectSettings_property_physics/2d/default_angular_damp>`{.interpreted-text
role="ref"}

The default rotational motion damping in 2D. Damping is used to
gradually slow down physical objects over time. RigidBodies will fall
back to this value when combining their own damping values and no area
damping value is present.

Suggested values are in the range `0` to `30`. At value `0` objects will
keep moving with the same velocity. Greater values will stop the object
faster. A value equal to or greater than the physics tick rate
(`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"}) will bring the object to a stop in one iteration.

\*\*Note:\*\* Godot damping calculations are velocity-dependent, meaning
bodies moving faster will take a longer time to come to rest. They do
not simulate inertia, friction, or air resistance. Therefore heavier or
larger bodies will lose speed at the same proportional rate as lighter
or smaller bodies.

During each physics tick, Godot will multiply the linear velocity of
RigidBodies by `1.0 - combined_damp / physics_ticks_per_second`. By
default, bodies combine damp factors: `combined_damp` is the sum of the
damp value of the body and this value or the area\'s value the body is
in. See `DampMode<enum_RigidBody2D_DampMode>`{.interpreted-text
role="ref"}.

\*\*Warning:\*\* Godot\'s damping calculations are simulation tick rate
dependent. Changing
`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"} may significantly change the outcomes and feel of your
simulation. This is true for the entire range of damping values greater
than 0. To get back to a similar feel, you also need to change your damp
values. This needed change is not proportional and differs from case to
case.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/default_gravity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/default_gravity** = `980.0`
`🔗<class_ProjectSettings_property_physics/2d/default_gravity>`{.interpreted-text
role="ref"}

The default gravity strength in 2D (in pixels per second squared).

\*\*Note:\*\* This property is only read when the project starts. To
change the default gravity at runtime, use the following code sample:

::::: tabs
::: code-tab
gdscript

\# Set the default gravity strength to 980.
PhysicsServer2D.area_set_param(get_viewport().find_world_2d().space,
PhysicsServer2D.AREA_PARAM_GRAVITY, 980)
:::

::: code-tab
csharp

// Set the default gravity strength to 980.
PhysicsServer2D.AreaSetParam(GetViewport().FindWorld2D().Space,
PhysicsServer2D.AreaParameter.Gravity, 980);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/default_gravity_vector}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**physics/2d/default_gravity_vector** = `Vector2(0, 1)`
`🔗<class_ProjectSettings_property_physics/2d/default_gravity_vector>`{.interpreted-text
role="ref"}

The default gravity direction in 2D.

\*\*Note:\*\* This property is only read when the project starts. To
change the default gravity vector at runtime, use the following code
sample:

::::: tabs
::: code-tab
gdscript

\# Set the default gravity direction to [Vector2(0, 1)]{.title-ref}.
PhysicsServer2D.area_set_param(get_viewport().find_world_2d().space,
PhysicsServer2D.AREA_PARAM_GRAVITY_VECTOR, Vector2.DOWN)
:::

::: code-tab
csharp

// Set the default gravity direction to [Vector2(0, 1)]{.title-ref}.
PhysicsServer2D.AreaSetParam(GetViewport().FindWorld2D().Space,
PhysicsServer2D.AreaParameter.GravityVector, Vector2.Down)
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/default_linear_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/default_linear_damp** = `0.1`
`🔗<class_ProjectSettings_property_physics/2d/default_linear_damp>`{.interpreted-text
role="ref"}

The default linear motion damping in 2D. Damping is used to gradually
slow down physical objects over time. RigidBodies will fall back to this
value when combining their own damping values and no area damping value
is present.

Suggested values are in the range `0` to `30`. At value `0` objects will
keep moving with the same velocity. Greater values will stop the object
faster. A value equal to or greater than the physics tick rate
(`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"}) will bring the object to a stop in one iteration.

\*\*Note:\*\* Godot damping calculations are velocity-dependent, meaning
bodies moving faster will take a longer time to come to rest. They do
not simulate inertia, friction, or air resistance. Therefore heavier or
larger bodies will lose speed at the same proportional rate as lighter
or smaller bodies.

During each physics tick, Godot will multiply the linear velocity of
RigidBodies by `1.0 - combined_damp / physics_ticks_per_second`, where
`combined_damp` is the sum of the linear damp of the body and this
value, or the area\'s value the body is in, assuming the body defaults
to combine damp values. See
`DampMode<enum_RigidBody2D_DampMode>`{.interpreted-text role="ref"}.

\*\*Warning:\*\* Godot\'s damping calculations are simulation tick rate
dependent. Changing
`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"} may significantly change the outcomes and feel of your
simulation. This is true for the entire range of damping values greater
than 0. To get back to a similar feel, you also need to change your damp
values. This needed change is not proportional and differs from case to
case.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/physics_engine}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**physics/2d/physics_engine** = `"DEFAULT"`
`🔗<class_ProjectSettings_property_physics/2d/physics_engine>`{.interpreted-text
role="ref"}

Sets which physics engine to use for 2D physics.

\*\*DEFAULT\*\* is currently equivalent to **GodotPhysics2D**, but may
change in future releases. Select an explicit implementation if you want
to ensure that your project stays on the same engine.

\*\*GodotPhysics2D\*\* is Godot\'s internal 2D physics engine.

\*\*Dummy\*\* is a 2D physics server that does nothing and returns only
dummy values, effectively disabling all 2D physics functionality.

Third-party extensions and modules can add other physics engines to
select with this setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/run_on_separate_thread}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/2d/run_on_separate_thread** = `false`
`🔗<class_ProjectSettings_property_physics/2d/run_on_separate_thread>`{.interpreted-text
role="ref"}

If `true`, the 2D physics server runs on a separate thread, making
better use of multi-core CPUs. If `false`, the 2D physics server runs on
the main thread. Running the physics server on a separate thread can
increase performance, but restricts API access to only physics process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/sleep_threshold_angular}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/sleep_threshold_angular** = `0.13962634`
`🔗<class_ProjectSettings_property_physics/2d/sleep_threshold_angular>`{.interpreted-text
role="ref"}

Threshold angular velocity under which a 2D physics body will be
considered inactive. See
`PhysicsServer2D.SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD<class_PhysicsServer2D_constant_SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/sleep_threshold_linear}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/sleep_threshold_linear** = `2.0`
`🔗<class_ProjectSettings_property_physics/2d/sleep_threshold_linear>`{.interpreted-text
role="ref"}

Threshold linear velocity under which a 2D physics body will be
considered inactive. See
`PhysicsServer2D.SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD<class_PhysicsServer2D_constant_SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/solver/contact_max_allowed_penetration}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/solver/contact_max_allowed_penetration** = `0.3`
`🔗<class_ProjectSettings_property_physics/2d/solver/contact_max_allowed_penetration>`{.interpreted-text
role="ref"}

Maximum distance a shape can penetrate another shape before it is
considered a collision. See
`PhysicsServer2D.SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION<class_PhysicsServer2D_constant_SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/solver/contact_max_separation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/solver/contact_max_separation** = `1.5`
`🔗<class_ProjectSettings_property_physics/2d/solver/contact_max_separation>`{.interpreted-text
role="ref"}

Maximum distance a shape can be from another before they are considered
separated and the contact is discarded. See
`PhysicsServer2D.SPACE_PARAM_CONTACT_MAX_SEPARATION<class_PhysicsServer2D_constant_SPACE_PARAM_CONTACT_MAX_SEPARATION>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/solver/contact_recycle_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/solver/contact_recycle_radius** = `1.0`
`🔗<class_ProjectSettings_property_physics/2d/solver/contact_recycle_radius>`{.interpreted-text
role="ref"}

Maximum distance a pair of bodies has to move before their collision
status has to be recalculated. See
`PhysicsServer2D.SPACE_PARAM_CONTACT_RECYCLE_RADIUS<class_PhysicsServer2D_constant_SPACE_PARAM_CONTACT_RECYCLE_RADIUS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/solver/default_constraint_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/solver/default_constraint_bias** = `0.2`
`🔗<class_ProjectSettings_property_physics/2d/solver/default_constraint_bias>`{.interpreted-text
role="ref"}

Default solver bias for all physics constraints. Defines how much bodies
react to enforce constraints. See
`PhysicsServer2D.SPACE_PARAM_CONSTRAINT_DEFAULT_BIAS<class_PhysicsServer2D_constant_SPACE_PARAM_CONSTRAINT_DEFAULT_BIAS>`{.interpreted-text
role="ref"}.

Individual constraints can have a specific bias value (see
`Joint2D.bias<class_Joint2D_property_bias>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/solver/default_contact_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/solver/default_contact_bias** = `0.8`
`🔗<class_ProjectSettings_property_physics/2d/solver/default_contact_bias>`{.interpreted-text
role="ref"}

Default solver bias for all physics contacts. Defines how much bodies
react to enforce contact separation. See
`PhysicsServer2D.SPACE_PARAM_CONTACT_DEFAULT_BIAS<class_PhysicsServer2D_constant_SPACE_PARAM_CONTACT_DEFAULT_BIAS>`{.interpreted-text
role="ref"}.

Individual shapes can have a specific bias value (see
`Shape2D.custom_solver_bias<class_Shape2D_property_custom_solver_bias>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/solver/solver_iterations}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/2d/solver/solver_iterations** = `16`
`🔗<class_ProjectSettings_property_physics/2d/solver/solver_iterations>`{.interpreted-text
role="ref"}

Number of solver iterations for all contacts and constraints. The
greater the number of iterations, the more accurate the collisions will
be. However, a greater number of iterations requires more CPU power,
which can decrease performance. See
`PhysicsServer2D.SPACE_PARAM_SOLVER_ITERATIONS<class_PhysicsServer2D_constant_SPACE_PARAM_SOLVER_ITERATIONS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/2d/time_before_sleep}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/2d/time_before_sleep** = `0.5`
`🔗<class_ProjectSettings_property_physics/2d/time_before_sleep>`{.interpreted-text
role="ref"}

Time (in seconds) of inactivity before which a 2D physics body will put
to sleep. See
`PhysicsServer2D.SPACE_PARAM_BODY_TIME_TO_SLEEP<class_PhysicsServer2D_constant_SPACE_PARAM_BODY_TIME_TO_SLEEP>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/default_angular_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/default_angular_damp** = `0.1`
`🔗<class_ProjectSettings_property_physics/3d/default_angular_damp>`{.interpreted-text
role="ref"}

The default rotational motion damping in 3D. Damping is used to
gradually slow down physical objects over time. RigidBodies will fall
back to this value when combining their own damping values and no area
damping value is present.

Suggested values are in the range `0` to `30`. At value `0` objects will
keep moving with the same velocity. Greater values will stop the object
faster. A value equal to or greater than the physics tick rate
(`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"}) will bring the object to a stop in one iteration.

\*\*Note:\*\* Godot damping calculations are velocity-dependent, meaning
bodies moving faster will take a longer time to come to rest. They do
not simulate inertia, friction, or air resistance. Therefore heavier or
larger bodies will lose speed at the same proportional rate as lighter
or smaller bodies.

During each physics tick, Godot will multiply the angular velocity of
RigidBodies by `1.0 - combined_damp / physics_ticks_per_second`. By
default, bodies combine damp factors: `combined_damp` is the sum of the
damp value of the body and this value or the area\'s value the body is
in. See `DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text
role="ref"}.

\*\*Warning:\*\* Godot\'s damping calculations are simulation tick rate
dependent. Changing
`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"} may significantly change the outcomes and feel of your
simulation. This is true for the entire range of damping values greater
than 0. To get back to a similar feel, you also need to change your damp
values. This needed change is not proportional and differs from case to
case.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/default_gravity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/default_gravity** = `9.8`
`🔗<class_ProjectSettings_property_physics/3d/default_gravity>`{.interpreted-text
role="ref"}

The default gravity strength in 3D (in meters per second squared).

\*\*Note:\*\* This property is only read when the project starts. To
change the default gravity at runtime, use the following code sample:

::::: tabs
::: code-tab
gdscript

\# Set the default gravity strength to 9.8.
PhysicsServer3D.area_set_param(get_viewport().find_world_3d().space,
PhysicsServer3D.AREA_PARAM_GRAVITY, 9.8)
:::

::: code-tab
csharp

// Set the default gravity strength to 9.8.
PhysicsServer3D.AreaSetParam(GetViewport().FindWorld3D().Space,
PhysicsServer3D.AreaParameter.Gravity, 9.8);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/default_gravity_vector}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**physics/3d/default_gravity_vector** = `Vector3(0, -1, 0)`
`🔗<class_ProjectSettings_property_physics/3d/default_gravity_vector>`{.interpreted-text
role="ref"}

The default gravity direction in 3D.

\*\*Note:\*\* This property is only read when the project starts. To
change the default gravity vector at runtime, use the following code
sample:

::::: tabs
::: code-tab
gdscript

\# Set the default gravity direction to [Vector3(0, -1, 0)]{.title-ref}.
PhysicsServer3D.area_set_param(get_viewport().find_world_3d().space,
PhysicsServer3D.AREA_PARAM_GRAVITY_VECTOR, Vector3.DOWN)
:::

::: code-tab
csharp

// Set the default gravity direction to [Vector3(0, -1, 0)]{.title-ref}.
PhysicsServer3D.AreaSetParam(GetViewport().FindWorld3D().Space,
PhysicsServer3D.AreaParameter.GravityVector, Vector3.Down)
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/default_linear_damp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/default_linear_damp** = `0.1`
`🔗<class_ProjectSettings_property_physics/3d/default_linear_damp>`{.interpreted-text
role="ref"}

The default linear motion damping in 3D. Damping is used to gradually
slow down physical objects over time. RigidBodies will fall back to this
value when combining their own damping values and no area damping value
is present.

Suggested values are in the range `0` to `30`. At value `0` objects will
keep moving with the same velocity. Greater values will stop the object
faster. A value equal to or greater than the physics tick rate
(`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"}) will bring the object to a stop in one iteration.

\*\*Note:\*\* Godot damping calculations are velocity-dependent, meaning
bodies moving faster will take a longer time to come to rest. They do
not simulate inertia, friction, or air resistance. Therefore heavier or
larger bodies will lose speed at the same proportional rate as lighter
or smaller bodies.

During each physics tick, Godot will multiply the linear velocity of
RigidBodies by `1.0 - combined_damp / physics_ticks_per_second`. By
default, bodies combine damp factors: `combined_damp` is the sum of the
damp value of the body and this value or the area\'s value the body is
in. See `DampMode<enum_RigidBody3D_DampMode>`{.interpreted-text
role="ref"}.

\*\*Warning:\*\* Godot\'s damping calculations are simulation tick rate
dependent. Changing
`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"} may significantly change the outcomes and feel of your
simulation. This is true for the entire range of damping values greater
than 0. To get back to a similar feel, you also need to change your damp
values. This needed change is not proportional and differs from case to
case.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/physics_engine}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**physics/3d/physics_engine** = `"DEFAULT"`
`🔗<class_ProjectSettings_property_physics/3d/physics_engine>`{.interpreted-text
role="ref"}

Sets which physics engine to use for 3D physics.

\*\*DEFAULT\*\* is currently equivalent to **GodotPhysics3D**, but may
change in future releases. Select an explicit implementation if you want
to ensure that your project stays on the same engine.

\*\*GodotPhysics3D\*\* is Godot\'s internal 3D physics engine.

\*\*Jolt Physics\*\* is an alternative physics engine that is generally
faster and more reliable than **GodotPhysics3D**. As it was recently
implemented, it is currently considered experimental and its behavior
may change in future releases.

\*\*Dummy\*\* is a 3D physics server that does nothing and returns only
dummy values, effectively disabling all 3D physics functionality.

Third-party extensions and modules can add other physics engines to
select with this setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/physics_interpolation/scene_traversal}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**physics/3d/physics_interpolation/scene_traversal** = `"DEFAULT"`
`🔗<class_ProjectSettings_property_physics/3d/physics_interpolation/scene_traversal>`{.interpreted-text
role="ref"}

The approach used for 3D scene traversal when physics interpolation is
enabled.

- `DEFAULT`: The default optimized method.
- `Legacy`: The previous reference method used for scene tree traversal,
  which is slower.
- `Debug`: Swaps between `DEFAULT` and `Legacy` methods on alternating
  frames, and provides logging information (which in turn makes it
  slower). Intended for debugging only; you should use the `DEFAULT`
  method in most cases.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/run_on_separate_thread}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/3d/run_on_separate_thread** = `false`
`🔗<class_ProjectSettings_property_physics/3d/run_on_separate_thread>`{.interpreted-text
role="ref"}

If `true`, the 3D physics server runs on a separate thread, making
better use of multi-core CPUs. If `false`, the 3D physics server runs on
the main thread. Running the physics server on a separate thread can
increase performance, but restricts API access to only physics process.

\*\*Note:\*\* When
`physics/3d/physics_engine<class_ProjectSettings_property_physics/3d/physics_engine>`{.interpreted-text
role="ref"} is set to `Jolt Physics`, enabling this setting will prevent
the 3D physics server from being able to provide any context when
reporting errors and warnings, and will instead always refer to nodes as
`<unknown>`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/sleep_threshold_angular}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/sleep_threshold_angular** = `0.13962634`
`🔗<class_ProjectSettings_property_physics/3d/sleep_threshold_angular>`{.interpreted-text
role="ref"}

Threshold angular velocity under which a 3D physics body will be
considered inactive. See
`PhysicsServer3D.SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD<class_PhysicsServer3D_constant_SPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/sleep_threshold_linear}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/sleep_threshold_linear** = `0.1`
`🔗<class_ProjectSettings_property_physics/3d/sleep_threshold_linear>`{.interpreted-text
role="ref"}

Threshold linear velocity under which a 3D physics body will be
considered inactive. See
`PhysicsServer3D.SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD<class_PhysicsServer3D_constant_SPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/solver/contact_max_allowed_penetration}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/solver/contact_max_allowed_penetration** = `0.01`
`🔗<class_ProjectSettings_property_physics/3d/solver/contact_max_allowed_penetration>`{.interpreted-text
role="ref"}

Maximum distance a shape can penetrate another shape before it is
considered a collision. See
`PhysicsServer3D.SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION<class_PhysicsServer3D_constant_SPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/solver/contact_max_separation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/solver/contact_max_separation** = `0.05`
`🔗<class_ProjectSettings_property_physics/3d/solver/contact_max_separation>`{.interpreted-text
role="ref"}

Maximum distance a shape can be from another before they are considered
separated and the contact is discarded. See
`PhysicsServer3D.SPACE_PARAM_CONTACT_MAX_SEPARATION<class_PhysicsServer3D_constant_SPACE_PARAM_CONTACT_MAX_SEPARATION>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/solver/contact_recycle_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/solver/contact_recycle_radius** = `0.01`
`🔗<class_ProjectSettings_property_physics/3d/solver/contact_recycle_radius>`{.interpreted-text
role="ref"}

Maximum distance a pair of bodies has to move before their collision
status has to be recalculated. See
`PhysicsServer3D.SPACE_PARAM_CONTACT_RECYCLE_RADIUS<class_PhysicsServer3D_constant_SPACE_PARAM_CONTACT_RECYCLE_RADIUS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/solver/default_contact_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/solver/default_contact_bias** = `0.8`
`🔗<class_ProjectSettings_property_physics/3d/solver/default_contact_bias>`{.interpreted-text
role="ref"}

Default solver bias for all physics contacts. Defines how much bodies
react to enforce contact separation. See
`PhysicsServer3D.SPACE_PARAM_CONTACT_DEFAULT_BIAS<class_PhysicsServer3D_constant_SPACE_PARAM_CONTACT_DEFAULT_BIAS>`{.interpreted-text
role="ref"}.

Individual shapes can have a specific bias value (see
`Shape3D.custom_solver_bias<class_Shape3D_property_custom_solver_bias>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/solver/solver_iterations}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/3d/solver/solver_iterations** = `16`
`🔗<class_ProjectSettings_property_physics/3d/solver/solver_iterations>`{.interpreted-text
role="ref"}

Number of solver iterations for all contacts and constraints. The
greater the number of iterations, the more accurate the collisions will
be. However, a greater number of iterations requires more CPU power,
which can decrease performance. See
`PhysicsServer3D.SPACE_PARAM_SOLVER_ITERATIONS<class_PhysicsServer3D_constant_SPACE_PARAM_SOLVER_ITERATIONS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/3d/time_before_sleep}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/3d/time_before_sleep** = `0.5`
`🔗<class_ProjectSettings_property_physics/3d/time_before_sleep>`{.interpreted-text
role="ref"}

Time (in seconds) of inactivity before which a 3D physics body will put
to sleep. See
`PhysicsServer3D.SPACE_PARAM_BODY_TIME_TO_SLEEP<class_PhysicsServer3D_constant_SPACE_PARAM_BODY_TIME_TO_SLEEP>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/common/enable_object_picking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/common/enable_object_picking** = `true`
`🔗<class_ProjectSettings_property_physics/common/enable_object_picking>`{.interpreted-text
role="ref"}

Enables
`Viewport.physics_object_picking<class_Viewport_property_physics_object_picking>`{.interpreted-text
role="ref"} on the root viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/common/max_physics_steps_per_frame}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/common/max_physics_steps_per_frame** = `8`
`🔗<class_ProjectSettings_property_physics/common/max_physics_steps_per_frame>`{.interpreted-text
role="ref"}

Controls the maximum number of physics steps that can be simulated each
rendered frame. The default value is tuned to avoid \"spiral of death\"
situations where expensive physics simulations trigger more expensive
simulations indefinitely. However, the game will appear to slow down if
the rendering FPS is less than `1 / max_physics_steps_per_frame` of
`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"}. This occurs even if `delta` is consistently used in physics
calculations. To avoid this, increase
`physics/common/max_physics_steps_per_frame<class_ProjectSettings_property_physics/common/max_physics_steps_per_frame>`{.interpreted-text
role="ref"} if you have increased
`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"} significantly above its default value.

\*\*Note:\*\* This property is only read when the project starts. To
change the maximum number of simulated physics steps per frame at
runtime, set
`Engine.max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/common/physics_interpolation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/common/physics_interpolation** = `false`
`🔗<class_ProjectSettings_property_physics/common/physics_interpolation>`{.interpreted-text
role="ref"}

If `true`, the renderer will interpolate the transforms of objects (both
physics and non-physics) between the last two transforms, so that smooth
motion is seen even when physics ticks do not coincide with rendered
frames. See also
`Node.reset_physics_interpolation()<class_Node_method_reset_physics_interpolation>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Although this is a global setting, finer control of
individual branches of the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} is possible
using
`Node.physics_interpolation_mode<class_Node_property_physics_interpolation_mode>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is only read when the project starts. To
toggle physics interpolation at runtime, set
`SceneTree.physics_interpolation<class_SceneTree_property_physics_interpolation>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* Property
`physics/common/physics_jitter_fix<class_ProjectSettings_property_physics/common/physics_jitter_fix>`{.interpreted-text
role="ref"} is automatically disabled if
`physics/common/physics_interpolation<class_ProjectSettings_property_physics/common/physics_interpolation>`{.interpreted-text
role="ref"} is set to `true`, as the two methods are incompatible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/common/physics_jitter_fix}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/common/physics_jitter_fix** = `0.5`
`🔗<class_ProjectSettings_property_physics/common/physics_jitter_fix>`{.interpreted-text
role="ref"}

Controls how much physics ticks are synchronized with real time. For 0
or less, the ticks are synchronized. Such values are recommended for
network games, where clock synchronization matters. Higher values cause
higher deviation of in-game clock and real clock, but allows smoothing
out framerate jitters. The default value of 0.5 should be good enough
for most; values above 2 could cause the game to react to dropped frames
with a noticeable delay and are not recommended.

\*\*Note:\*\* Jitter fix is automatically disabled at runtime when
`physics/common/physics_interpolation<class_ProjectSettings_property_physics/common/physics_interpolation>`{.interpreted-text
role="ref"} is enabled.

\*\*Note:\*\* When using a custom physics interpolation solution, the
physics jitter fix should be disabled by setting
`physics/common/physics_jitter_fix<class_ProjectSettings_property_physics/common/physics_jitter_fix>`{.interpreted-text
role="ref"} to `0.0`.

\*\*Note:\*\* This property is only read when the project starts. To
change the physics jitter fix at runtime, set
`Engine.physics_jitter_fix<class_Engine_property_physics_jitter_fix>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/common/physics_ticks_per_second}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/common/physics_ticks_per_second** = `60`
`🔗<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"}

The number of fixed iterations per second. This controls how often
physics simulation and
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} methods are run. See also
`application/run/max_fps<class_ProjectSettings_property_application/run/max_fps>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is only read when the project starts. To
change the physics FPS at runtime, set
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* Only
`physics/common/max_physics_steps_per_frame<class_ProjectSettings_property_physics/common/max_physics_steps_per_frame>`{.interpreted-text
role="ref"} physics ticks may be simulated per rendered frame at most.
If more physics ticks have to be simulated per rendered frame to keep up
with rendering, the project will appear to slow down (even if `delta` is
used consistently in physics calculations). Therefore, it is recommended
to also increase
`physics/common/max_physics_steps_per_frame<class_ProjectSettings_property_physics/common/max_physics_steps_per_frame>`{.interpreted-text
role="ref"} if increasing
`physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"} significantly above its default value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/collisions/active_edge_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/collisions/active_edge_threshold** =
`0.87266463`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/collisions/active_edge_threshold>`{.interpreted-text
role="ref"}

The maximum angle, in radians, between two adjacent triangles in a
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} or
`HeightMapShape3D<class_HeightMapShape3D>`{.interpreted-text role="ref"}
for which the edge between those triangles is considered inactive.

Collisions against an inactive edge will have its normal overridden to
instead be the surface normal of the triangle. This can help alleviate
ghost collisions.

\*\*Note:\*\* Setting this too high can result in objects not
depenetrating properly.

\*\*Note:\*\* This applies to all shape queries, as well as physics
bodies within the simulation.

\*\*Note:\*\* This does not apply when enabling Jolt\'s enhanced
internal edge removal, which supersedes this.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/collisions/collision_margin_fraction}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/collisions/collision_margin_fraction** =
`0.08`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/collisions/collision_margin_fraction>`{.interpreted-text
role="ref"}

The amount of collision margin to use for certain convex collision
shapes, such as `BoxShape3D<class_BoxShape3D>`{.interpreted-text
role="ref"}, `CylinderShape3D<class_CylinderShape3D>`{.interpreted-text
role="ref"} and
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"}, as a fraction of the shape\'s shortest axis, with
`Shape3D.margin<class_Shape3D_property_margin>`{.interpreted-text
role="ref"} as the upper bound. This is mainly used to speed up
collision detection with convex shapes.

\*\*Note:\*\* Collision margins in Jolt do not add any extra size to the
shape. Instead the shape is first shrunk by the margin and then expanded
by the same amount, resulting in a shape with rounded corners.

\*\*Note:\*\* Setting this value too close to `0.0` may also negatively
affect the accuracy of the collision detection with convex shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/joints/world_node}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/joints/world_node** = `0`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/joints/world_node>`{.interpreted-text
role="ref"}

Which of the two nodes bound by a joint should represent the world when
one of the two is omitted, as either
`Joint3D.node_a<class_Joint3D_property_node_a>`{.interpreted-text
role="ref"} or
`Joint3D.node_b<class_Joint3D_property_node_b>`{.interpreted-text
role="ref"}. This can be thought of as having the omitted node be a
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"} at the
joint\'s position. Joint limits are more easily expressed when
`Joint3D.node_a<class_Joint3D_property_node_a>`{.interpreted-text
role="ref"} represents the world.

\*\*Note:\*\* In Godot Physics, only
`Joint3D.node_b<class_Joint3D_property_node_b>`{.interpreted-text
role="ref"} can represent the world.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_angular_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/limits/max_angular_velocity** = `47.12389`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_angular_velocity>`{.interpreted-text
role="ref"}

The maximum angular velocity that a
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} can
reach, in radians per second.

This is mainly used as a fail-safe, to prevent the simulation from
exploding, as fast-moving objects colliding with complex physics
structures can otherwise cause them to go out of control. Fast-moving
objects can also cause a lot of stress on the collision detection
system, which can slow down the simulation considerably.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_bodies}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/limits/max_bodies** = `10240`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_bodies>`{.interpreted-text
role="ref"}

The maximum number of
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} to
support at the same time, awake or sleeping. When this limit is
exceeded, an error is reported and anything past that point is undefined
behavior.

\*\*Note:\*\* This limit also applies within the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_body_pairs}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/limits/max_body_pairs** = `65536`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_body_pairs>`{.interpreted-text
role="ref"}

The maximum number of body pairs to allow processing of. When this limit
is exceeded, a warning is reported and collisions will randomly be
ignored while bodies pass through each other.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_contact_constraints}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/limits/max_contact_constraints** = `20480`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_contact_constraints>`{.interpreted-text
role="ref"}

The maximum number of contact constraints to allow processing of. When
this limit is exceeded, a warning is reported and collisions will
randomly be ignored while bodies pass through each other.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_linear_velocity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/limits/max_linear_velocity** = `500.0`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/limits/max_linear_velocity>`{.interpreted-text
role="ref"}

The maximum linear velocity that a
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} can
reach, in meters per second.

This is mainly used as a fail-safe, to prevent the simulation from
exploding, as fast-moving objects colliding with complex physics
structures can otherwise cause them to go out of control. Fast-moving
objects can also cause a lot of stress on the collision detection
system, which can slow down the simulation considerably.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/limits/temporary_memory_buffer_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/limits/temporary_memory_buffer_size** = `32`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/limits/temporary_memory_buffer_size>`{.interpreted-text
role="ref"}

The amount of memory to pre-allocate for the stack allocator used within
Jolt, in MiB. This allocator is used within the physics step to store
things that are only needed during it, like which bodies are in contact,
how they form islands and the data needed to solve the contacts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/limits/world_boundary_shape_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/limits/world_boundary_shape_size** = `2000.0`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/limits/world_boundary_shape_size>`{.interpreted-text
role="ref"}

The size of
`WorldBoundaryShape3D<class_WorldBoundaryShape3D>`{.interpreted-text
role="ref"} boundaries, for all three dimensions. The plane is
effectively centered within a box of this size, and anything outside of
the box will not collide with it. This is necessary as
`WorldBoundaryShape3D<class_WorldBoundaryShape3D>`{.interpreted-text
role="ref"} is not unbounded when using Jolt, in order to prevent
precision issues.

\*\*Note:\*\* Setting this value too high can make collision detection
less accurate.

\*\*Note:\*\* Collisions against the effective edges of a
`WorldBoundaryShape3D<class_WorldBoundaryShape3D>`{.interpreted-text
role="ref"} will be inconsistent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/motion_queries/recovery_amount}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/motion_queries/recovery_amount** = `0.4`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/motion_queries/recovery_amount>`{.interpreted-text
role="ref"}

Fraction of the total penetration to depenetrate per iteration during
motion queries.

\*\*Note:\*\* This affects methods
`CharacterBody3D.move_and_slide()<class_CharacterBody3D_method_move_and_slide>`{.interpreted-text
role="ref"},
`PhysicsBody3D.move_and_collide()<class_PhysicsBody3D_method_move_and_collide>`{.interpreted-text
role="ref"},
`PhysicsBody3D.test_move()<class_PhysicsBody3D_method_test_move>`{.interpreted-text
role="ref"} and
`PhysicsServer3D.body_test_motion()<class_PhysicsServer3D_method_body_test_motion>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/motion_queries/recovery_iterations}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/motion_queries/recovery_iterations** = `4`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/motion_queries/recovery_iterations>`{.interpreted-text
role="ref"}

The number of iterations to run when depenetrating during motion
queries.

\*\*Note:\*\* This affects methods
`CharacterBody3D.move_and_slide()<class_CharacterBody3D_method_move_and_slide>`{.interpreted-text
role="ref"},
`PhysicsBody3D.move_and_collide()<class_PhysicsBody3D_method_move_and_collide>`{.interpreted-text
role="ref"},
`PhysicsBody3D.test_move()<class_PhysicsBody3D_method_test_move>`{.interpreted-text
role="ref"} and
`PhysicsServer3D.body_test_motion()<class_PhysicsServer3D_method_body_test_motion>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/motion_queries/use_enhanced_internal_edge_removal}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/motion_queries/use_enhanced_internal_edge_removal**
= `true`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/motion_queries/use_enhanced_internal_edge_removal>`{.interpreted-text
role="ref"}

If `true`, enables Jolt\'s enhanced internal edge removal during motion
queries. This can help alleviate ghost collisions, but only with edges
within a single body, meaning edges between separate bodies can still
cause ghost collisions.

\*\*Note:\*\* This affects methods
`CharacterBody3D.move_and_slide()<class_CharacterBody3D_method_move_and_slide>`{.interpreted-text
role="ref"},
`PhysicsBody3D.move_and_collide()<class_PhysicsBody3D_method_move_and_collide>`{.interpreted-text
role="ref"},
`PhysicsBody3D.test_move()<class_PhysicsBody3D_method_test_move>`{.interpreted-text
role="ref"} and
`PhysicsServer3D.body_test_motion()<class_PhysicsServer3D_method_body_test_motion>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/queries/enable_ray_cast_face_index}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/queries/enable_ray_cast_face_index** = `false`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/queries/enable_ray_cast_face_index>`{.interpreted-text
role="ref"}

If `true`, populates the `face_index` field in the results of
`PhysicsDirectSpaceState3D.intersect_ray()<class_PhysicsDirectSpaceState3D_method_intersect_ray>`{.interpreted-text
role="ref"}, also accessed through
`RayCast3D.get_collision_face_index()<class_RayCast3D_method_get_collision_face_index>`{.interpreted-text
role="ref"}. If `false`, the `face_index` field will be left at its
default value of `-1`.

\*\*Note:\*\* Enabling this setting will increase Jolt\'s memory usage
for
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} by around 25%.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/queries/use_enhanced_internal_edge_removal}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/queries/use_enhanced_internal_edge_removal** =
`false`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/queries/use_enhanced_internal_edge_removal>`{.interpreted-text
role="ref"}

If `true`, enables Jolt\'s enhanced internal edge removal during shape
queries. This can help alleviate ghost collisions when using shape
queries for things like character movement, but only with edges within a
single body, meaning edges between separate bodies can still cause ghost
collisions.

\*\*Note:\*\* This affects methods
`PhysicsDirectSpaceState3D.cast_motion()<class_PhysicsDirectSpaceState3D_method_cast_motion>`{.interpreted-text
role="ref"},
`PhysicsDirectSpaceState3D.collide_shape()<class_PhysicsDirectSpaceState3D_method_collide_shape>`{.interpreted-text
role="ref"},
`PhysicsDirectSpaceState3D.get_rest_info()<class_PhysicsDirectSpaceState3D_method_get_rest_info>`{.interpreted-text
role="ref"} and
`PhysicsDirectSpaceState3D.intersect_shape()<class_PhysicsDirectSpaceState3D_method_intersect_shape>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Enabling this setting can cause certain shapes to be
culled from the results entirely, but you will get at least one
intersection per body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/allow_sleep}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/allow_sleep** = `true`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/allow_sleep>`{.interpreted-text
role="ref"}

If `true`, `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} nodes are allowed to go to sleep if their velocity is below
the threshold defined in
`physics/jolt_physics_3d/simulation/sleep_velocity_threshold<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/sleep_velocity_threshold>`{.interpreted-text
role="ref"} for the duration set in
`physics/jolt_physics_3d/simulation/sleep_time_threshold<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/sleep_time_threshold>`{.interpreted-text
role="ref"}. This can improve physics simulation performance when there
are non-moving `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} nodes, at the cost of some nodes possibly failing to wake up
in certain scenarios. Consider disabling this temporarily to
troubleshoot `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} nodes not moving when they should.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/baumgarte_stabilization_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/baumgarte_stabilization_factor** =
`0.2`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/baumgarte_stabilization_factor>`{.interpreted-text
role="ref"}

How much of the position error of a
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} to fix
during a physics step, where `0.0` is none and `1.0` is the full amount.
This affects things like how quickly bodies depenetrate.

\*\*Note:\*\* Setting this value too high can make
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} nodes
unstable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/body_pair_contact_cache_angle_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/body_pair_contact_cache_angle_threshold**
= `0.034906585`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/body_pair_contact_cache_angle_threshold>`{.interpreted-text
role="ref"}

The maximum relative angle by which a body pair can move and still reuse
the collision results from the previous physics step, in radians.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/body_pair_contact_cache_distance_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/body_pair_contact_cache_distance_threshold**
= `0.001`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/body_pair_contact_cache_distance_threshold>`{.interpreted-text
role="ref"}

The maximum relative distance by which a body pair can move and still
reuse the collision results from the previous physics step, in meters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/body_pair_contact_cache_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/body_pair_contact_cache_enabled** =
`true`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/body_pair_contact_cache_enabled>`{.interpreted-text
role="ref"}

If `true`, enables the body pair contact cache, which removes the need
for potentially expensive collision detection when the relative
orientation between two bodies hasn\'t changed much.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/bounce_velocity_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/bounce_velocity_threshold** = `1.0`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/bounce_velocity_threshold>`{.interpreted-text
role="ref"}

The minimum velocity needed before a collision can be bouncy, in meters
per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/continuous_cd_max_penetration}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/continuous_cd_max_penetration** =
`0.25`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/continuous_cd_max_penetration>`{.interpreted-text
role="ref"}

Fraction of a body\'s inner radius that may penetrate another body while
using continuous collision detection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/continuous_cd_movement_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/continuous_cd_movement_threshold**
= `0.75`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/continuous_cd_movement_threshold>`{.interpreted-text
role="ref"}

Fraction of a body\'s inner radius that the body must move per step to
make use of continuous collision detection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/generate_all_kinematic_contacts}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/generate_all_kinematic_contacts** =
`false`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/generate_all_kinematic_contacts>`{.interpreted-text
role="ref"}

If `true`, a `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} frozen with
`RigidBody3D.FREEZE_MODE_KINEMATIC<class_RigidBody3D_constant_FREEZE_MODE_KINEMATIC>`{.interpreted-text
role="ref"} is able to collide with other kinematic and static bodies,
and therefore generate contacts for them.

\*\*Note:\*\* This setting can come at a heavy CPU and memory cost if
you allow many/large frozen kinematic bodies with a non-zero
`RigidBody3D.max_contacts_reported<class_RigidBody3D_property_max_contacts_reported>`{.interpreted-text
role="ref"} to overlap with complex static geometry, such as
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} or
`HeightMapShape3D<class_HeightMapShape3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/penetration_slop}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/penetration_slop** = `0.02`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/penetration_slop>`{.interpreted-text
role="ref"}

How much bodies are allowed to penetrate each other, in meters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/position_steps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/position_steps** = `2`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/position_steps>`{.interpreted-text
role="ref"}

Number of solver position iterations. The greater the number of
iterations, the more accurate the simulation will be, at the cost of CPU
performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/sleep_time_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/sleep_time_threshold** = `0.5`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/sleep_time_threshold>`{.interpreted-text
role="ref"}

Time in seconds a `RigidBody3D<class_RigidBody3D>`{.interpreted-text
role="ref"} will spend below the sleep velocity threshold before going
to sleep.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/sleep_velocity_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/sleep_velocity_threshold** = `0.03`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/sleep_velocity_threshold>`{.interpreted-text
role="ref"}

The linear velocity of specific points on the bounding box of a
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"}, below
which it can be put to sleep, in meters per second. These points help
capture both the linear and angular motion of a
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/soft_body_point_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/soft_body_point_radius** = `0.01`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/soft_body_point_radius>`{.interpreted-text
role="ref"}

How big the points of a `SoftBody3D<class_SoftBody3D>`{.interpreted-text
role="ref"} are, in meters. A higher value can prevent behavior such as
cloth laying perfectly flush against other surfaces and causing
Z-fighting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/speculative_contact_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/speculative_contact_distance** =
`0.02`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/speculative_contact_distance>`{.interpreted-text
role="ref"}

Radius around physics bodies, inside which speculative contact points
will be detected, in meters. This is mainly used to prevent
tunneling/penetration for
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} nodes
during simulation.

\*\*Note:\*\* Setting this too high may result in ghost collisions, as
speculative contacts are based on the closest points during the
collision detection step which may not be the actual closest points by
the time the two bodies hit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/use_enhanced_internal_edge_removal}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/use_enhanced_internal_edge_removal**
= `true`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/use_enhanced_internal_edge_removal>`{.interpreted-text
role="ref"}

If `true`, enables Jolt\'s enhanced internal edge removal for
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"}. This can
help alleviate ghost collisions when, for example, a
`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"} collides
with the edges of two perfectly joined
`BoxShape3D<class_BoxShape3D>`{.interpreted-text role="ref"}. The
removal only applies to edges internal to a single body, meaning edges
between separate bodies can still cause ghost collisions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_physics/jolt_physics_3d/simulation/velocity_steps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physics/jolt_physics_3d/simulation/velocity_steps** = `10`
`🔗<class_ProjectSettings_property_physics/jolt_physics_3d/simulation/velocity_steps>`{.interpreted-text
role="ref"}

Number of solver velocity iterations. The greater the number of
iterations, the more accurate the simulation will be, at the cost of CPU
performance.

\*\*Note:\*\* This needs to be at least `2` in order for friction to
work, as friction is applied using the non-penetration impulse from the
previous iteration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/2d/batching/item_buffer_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/2d/batching/item_buffer_size** = `16384`
`🔗<class_ProjectSettings_property_rendering/2d/batching/item_buffer_size>`{.interpreted-text
role="ref"}

Maximum number of canvas item commands that can be batched into a single
draw call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/2d/batching/uniform_set_cache_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/2d/batching/uniform_set_cache_size** = `4096`
`🔗<class_ProjectSettings_property_rendering/2d/batching/uniform_set_cache_size>`{.interpreted-text
role="ref"}

Maximum number of uniform sets that will be cached by the 2D renderer
when batching draw calls.

\*\*Note:\*\* Increasing this value can improve performance if the
project renders many unique sprite textures every frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/2d/sdf/oversize}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/2d/sdf/oversize** = `1`
`🔗<class_ProjectSettings_property_rendering/2d/sdf/oversize>`{.interpreted-text
role="ref"}

Controls how much of the original viewport size should be covered by the
2D signed distance field. This SDF can be sampled in
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} shaders and
is used for `GPUParticles2D<class_GPUParticles2D>`{.interpreted-text
role="ref"} collision. Higher values allow portions of occluders located
outside the viewport to still be taken into account in the generated
signed distance field, at the cost of performance. If you notice
particles falling through
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"}s
as the occluders leave the viewport, increase this setting.

The percentage specified is added on each axis and on both sides. For
example, with the default setting of 120%, the signed distance field
will cover 20% of the viewport\'s size outside the viewport on each side
(top, right, bottom, left).

\*\*Note:\*\* This property is only read when the project starts. To
change the 2D SDF oversizing percentage at runtime, use
`RenderingServer.viewport_set_sdf_oversize_and_scale()<class_RenderingServer_method_viewport_set_sdf_oversize_and_scale>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/2d/sdf/scale}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/2d/sdf/scale** = `1`
`🔗<class_ProjectSettings_property_rendering/2d/sdf/scale>`{.interpreted-text
role="ref"}

The resolution scale to use for the 2D signed distance field. Higher
values lead to a more precise and more stable signed distance field as
the camera moves, at the cost of performance. The default value (50%)
renders at half the resolution of the viewport size on each axis, which
means the SDF is generated with 25% of the viewport\'s pixel count.

\*\*Note:\*\* This property is only read when the project starts. To
change the 2D SDF resolution scale at runtime, use
`RenderingServer.viewport_set_sdf_oversize_and_scale()<class_RenderingServer_method_viewport_set_sdf_oversize_and_scale>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/2d/shadow_atlas/size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/2d/shadow_atlas/size** = `2048`
`🔗<class_ProjectSettings_property_rendering/2d/shadow_atlas/size>`{.interpreted-text
role="ref"}

The size of the 2D shadow atlas in pixels. Higher values result in more
precise `Light2D<class_Light2D>`{.interpreted-text role="ref"} shadows,
at the cost of performance and video memory usage. The specified value
is rounded up to the nearest power of 2.

\*\*Note:\*\* This property is only read when the project starts. To
change the 2D shadow atlas size at runtime, use
`RenderingServer.canvas_set_shadow_texture_size()<class_RenderingServer_method_canvas_set_shadow_texture_size>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/2d/snap/snap_2d_transforms_to_pixel}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/2d/snap/snap_2d_transforms_to_pixel** = `false`
`🔗<class_ProjectSettings_property_rendering/2d/snap/snap_2d_transforms_to_pixel>`{.interpreted-text
role="ref"}

If `true`, `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
nodes will internally snap to full pixels. Useful for low-resolution
pixel art games. Their position can still be sub-pixel, but the decimals
will not have effect as the position is rounded. This can lead to a
crisper appearance at the cost of less smooth movement, especially when
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"} smoothing is
enabled.

\*\*Note:\*\* This property is only read when the project starts. To
toggle 2D transform snapping at runtime, use
`RenderingServer.viewport_set_snap_2d_transforms_to_pixel()<class_RenderingServer_method_viewport_set_snap_2d_transforms_to_pixel>`{.interpreted-text
role="ref"} on the root `Viewport<class_Viewport>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* `Control<class_Control>`{.interpreted-text role="ref"}
nodes are snapped to the nearest pixel by default. This is controlled by
`gui/common/snap_controls_to_pixels<class_ProjectSettings_property_gui/common/snap_controls_to_pixels>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* It is not recommended to use this setting together with
`rendering/2d/snap/snap_2d_vertices_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_vertices_to_pixel>`{.interpreted-text
role="ref"}, as movement may appear even less smooth. Prefer only
enabling this setting instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/2d/snap/snap_2d_vertices_to_pixel}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/2d/snap/snap_2d_vertices_to_pixel** = `false`
`🔗<class_ProjectSettings_property_rendering/2d/snap/snap_2d_vertices_to_pixel>`{.interpreted-text
role="ref"}

If `true`, vertices of `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} nodes will snap to full pixels. Useful for low-resolution
pixel art games. Only affects the final vertex positions, not the
transforms. This can lead to a crisper appearance at the cost of less
smooth movement, especially when
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"} smoothing is
enabled.

\*\*Note:\*\* This property is only read when the project starts. To
toggle 2D vertex snapping at runtime, use
`RenderingServer.viewport_set_snap_2d_vertices_to_pixel()<class_RenderingServer_method_viewport_set_snap_2d_vertices_to_pixel>`{.interpreted-text
role="ref"} on the root `Viewport<class_Viewport>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* `Control<class_Control>`{.interpreted-text role="ref"}
nodes are snapped to the nearest pixel by default. This is controlled by
`gui/common/snap_controls_to_pixels<class_ProjectSettings_property_gui/common/snap_controls_to_pixels>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* It is not recommended to use this setting together with
`rendering/2d/snap/snap_2d_transforms_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_transforms_to_pixel>`{.interpreted-text
role="ref"}, as movement may appear even less smooth. Prefer only
enabling that setting instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_2d}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/anti_aliasing/quality/msaa_2d** = `0`
`🔗<class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_2d>`{.interpreted-text
role="ref"}

Sets the number of multisample antialiasing (MSAA) samples to use for
2D/Canvas rendering (as a power of two). MSAA is used to reduce aliasing
around the edges of polygons. A higher MSAA value results in smoother
edges but can be significantly slower on some hardware, especially
integrated graphics due to their limited memory bandwidth. This has no
effect on shader-induced aliasing or texture aliasing.

\*\*Note:\*\* MSAA is only supported in the Forward+ and Mobile
rendering methods, not Compatibility.

\*\*Note:\*\* This property is only read when the project starts. To set
the number of 2D MSAA samples at runtime, set
`Viewport.msaa_2d<class_Viewport_property_msaa_2d>`{.interpreted-text
role="ref"} or use
`RenderingServer.viewport_set_msaa_2d()<class_RenderingServer_method_viewport_set_msaa_2d>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_3d}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/anti_aliasing/quality/msaa_3d** = `0`
`🔗<class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_3d>`{.interpreted-text
role="ref"}

Sets the number of multisample antialiasing (MSAA) samples to use for 3D
rendering (as a power of two). MSAA is used to reduce aliasing around
the edges of polygons. A higher MSAA value results in smoother edges but
can be significantly slower on some hardware, especially integrated
graphics due to their limited memory bandwidth. See also
`rendering/scaling_3d/mode<class_ProjectSettings_property_rendering/scaling_3d/mode>`{.interpreted-text
role="ref"} for supersampling, which provides higher quality but is much
more expensive. This has no effect on shader-induced aliasing or texture
aliasing.

\*\*Note:\*\* This property is only read when the project starts. To set
the number of 3D MSAA samples at runtime, set
`Viewport.msaa_3d<class_Viewport_property_msaa_3d>`{.interpreted-text
role="ref"} or use
`RenderingServer.viewport_set_msaa_3d()<class_RenderingServer_method_viewport_set_msaa_3d>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/anti_aliasing/quality/screen_space_aa}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/anti_aliasing/quality/screen_space_aa** = `0`
`🔗<class_ProjectSettings_property_rendering/anti_aliasing/quality/screen_space_aa>`{.interpreted-text
role="ref"}

Sets the screen-space antialiasing mode for the default screen
`Viewport<class_Viewport>`{.interpreted-text role="ref"}. Screen-space
antialiasing works by selectively blurring edges in a post-process
shader. It differs from MSAA which takes multiple coverage samples while
rendering objects. Screen-space AA methods are typically faster than
MSAA and will smooth out specular aliasing, but tend to make scenes
appear blurry. The blurriness is partially counteracted by automatically
using a negative mipmap LOD bias (see
`rendering/textures/default_filters/texture_mipmap_bias<class_ProjectSettings_property_rendering/textures/default_filters/texture_mipmap_bias>`{.interpreted-text
role="ref"}).

Another way to combat specular aliasing is to enable
`rendering/anti_aliasing/screen_space_roughness_limiter/enabled<class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/enabled>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Screen-space antialiasing is only supported in the
Forward+ and Mobile rendering methods, not Compatibility.

\*\*Note:\*\* This property is only read when the project starts. To set
the screen-space antialiasing mode at runtime, set
`Viewport.screen_space_aa<class_Viewport_property_screen_space_aa>`{.interpreted-text
role="ref"} on the root `Viewport<class_Viewport>`{.interpreted-text
role="ref"} instead, or use
`RenderingServer.viewport_set_screen_space_aa()<class_RenderingServer_method_viewport_set_screen_space_aa>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/anti_aliasing/quality/smaa_edge_detection_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/anti_aliasing/quality/smaa_edge_detection_threshold** =
`0.05`
`🔗<class_ProjectSettings_property_rendering/anti_aliasing/quality/smaa_edge_detection_threshold>`{.interpreted-text
role="ref"}

Sets the sensitivity to edges when using SMAA for antialiasing. Lower
values will catch more edges, at a potentially higher performance cost.

\*\*Note:\*\* This property is only read when the project starts. There
is currently no way to change this setting at run-time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/anti_aliasing/quality/use_debanding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/anti_aliasing/quality/use_debanding** = `false`
`🔗<class_ProjectSettings_property_rendering/anti_aliasing/quality/use_debanding>`{.interpreted-text
role="ref"}

If `true`, uses a fast post-processing filter to make banding
significantly less visible. If
`rendering/viewport/hdr_2d<class_ProjectSettings_property_rendering/viewport/hdr_2d>`{.interpreted-text
role="ref"} is `false`, 2D rendering is *not* affected by debanding
unless the
`Environment.background_mode<class_Environment_property_background_mode>`{.interpreted-text
role="ref"} is
`Environment.BG_CANVAS<class_Environment_constant_BG_CANVAS>`{.interpreted-text
role="ref"}. If
`rendering/viewport/hdr_2d<class_ProjectSettings_property_rendering/viewport/hdr_2d>`{.interpreted-text
role="ref"} is `true`, debanding will affect all 2D and 3D rendering,
including canvas items.

In some cases, debanding may introduce a slightly noticeable dithering
pattern. It\'s recommended to enable debanding only when actually needed
since the dithering pattern will make lossless-compressed screenshots
larger.

\*\*Note:\*\* This property is only read when the project starts. To set
debanding at runtime, set
`Viewport.use_debanding<class_Viewport_property_use_debanding>`{.interpreted-text
role="ref"} on the root `Viewport<class_Viewport>`{.interpreted-text
role="ref"} instead, or use
`RenderingServer.viewport_set_use_debanding()<class_RenderingServer_method_viewport_set_use_debanding>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/anti_aliasing/quality/use_taa}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/anti_aliasing/quality/use_taa** = `false`
`🔗<class_ProjectSettings_property_rendering/anti_aliasing/quality/use_taa>`{.interpreted-text
role="ref"}

Enables temporal antialiasing for the default screen
`Viewport<class_Viewport>`{.interpreted-text role="ref"}. TAA works by
jittering the camera and accumulating the images of the last rendered
frames, motion vector rendering is used to account for camera and object
motion. Enabling TAA can make the image blurrier, which is partially
counteracted by automatically using a negative mipmap LOD bias (see
`rendering/textures/default_filters/texture_mipmap_bias<class_ProjectSettings_property_rendering/textures/default_filters/texture_mipmap_bias>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* The implementation is not complete yet. Some visual
instances such as particles and skinned meshes may show ghosting
artifacts in motion.

\*\*Note:\*\* TAA is only supported in the Forward+ rendering method,
not Mobile or Compatibility.

\*\*Note:\*\* This property is only read when the project starts. To set
TAA at runtime, set
`Viewport.use_taa<class_Viewport_property_use_taa>`{.interpreted-text
role="ref"} on the root `Viewport<class_Viewport>`{.interpreted-text
role="ref"} instead, or use
`RenderingServer.viewport_set_use_taa()<class_RenderingServer_method_viewport_set_use_taa>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/amount}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/anti_aliasing/screen_space_roughness_limiter/amount** =
`0.25`
`🔗<class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/amount>`{.interpreted-text
role="ref"}

**Note:** This property is only read when the project starts. To control
the screen-space roughness limiter at runtime, call
`RenderingServer.screen_space_roughness_limiter_set_active()<class_RenderingServer_method_screen_space_roughness_limiter_set_active>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/anti_aliasing/screen_space_roughness_limiter/enabled** =
`true`
`🔗<class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/enabled>`{.interpreted-text
role="ref"}

If `true`, enables a spatial filter to limit roughness in areas with
high-frequency detail. This can help reduce specular aliasing to an
extent, though not as much as enabling
`rendering/anti_aliasing/quality/use_taa<class_ProjectSettings_property_rendering/anti_aliasing/quality/use_taa>`{.interpreted-text
role="ref"}. This filter has a small performance cost, so consider
disabling it if it doesn\'t benefit your scene noticeably.

\*\*Note:\*\* The screen-space roughness limiter is only supported in
the Forward+ and Mobile rendering methods, not Compatibility.

\*\*Note:\*\* This property is only read when the project starts. To
control the screen-space roughness limiter at runtime, call
`RenderingServer.screen_space_roughness_limiter_set_active()<class_RenderingServer_method_screen_space_roughness_limiter_set_active>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/limit}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/anti_aliasing/screen_space_roughness_limiter/limit** =
`0.18`
`🔗<class_ProjectSettings_property_rendering/anti_aliasing/screen_space_roughness_limiter/limit>`{.interpreted-text
role="ref"}

**Note:** This property is only read when the project starts. To control
the screen-space roughness limiter at runtime, call
`RenderingServer.screen_space_roughness_limiter_set_active()<class_RenderingServer_method_screen_space_roughness_limiter_set_active>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/camera/depth_of_field/depth_of_field_bokeh_quality}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/camera/depth_of_field/depth_of_field_bokeh_quality** = `1`
`🔗<class_ProjectSettings_property_rendering/camera/depth_of_field/depth_of_field_bokeh_quality>`{.interpreted-text
role="ref"}

Sets the quality of the depth of field effect. Higher quality takes more
samples, which is slower but looks smoother.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/camera/depth_of_field/depth_of_field_bokeh_shape}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/camera/depth_of_field/depth_of_field_bokeh_shape** = `1`
`🔗<class_ProjectSettings_property_rendering/camera/depth_of_field/depth_of_field_bokeh_shape>`{.interpreted-text
role="ref"}

Sets the depth of field shape. Can be Box, Hexagon, or Circle. Box is
the fastest. Circle is the most realistic, but also the most expensive
to compute.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/camera/depth_of_field/depth_of_field_use_jitter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/camera/depth_of_field/depth_of_field_use_jitter** = `false`
`🔗<class_ProjectSettings_property_rendering/camera/depth_of_field/depth_of_field_use_jitter>`{.interpreted-text
role="ref"}

If `true`, jitters DOF samples to make effect slightly blurrier and hide
lines created from low sample rates. This can result in a slightly
grainy appearance when used with a low number of samples.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/driver/depth_prepass/disable_for_vendors}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/driver/depth_prepass/disable_for_vendors** =
`"PowerVR,Mali,Adreno,Apple"`
`🔗<class_ProjectSettings_property_rendering/driver/depth_prepass/disable_for_vendors>`{.interpreted-text
role="ref"}

Disables
`rendering/driver/depth_prepass/enable<class_ProjectSettings_property_rendering/driver/depth_prepass/enable>`{.interpreted-text
role="ref"} conditionally for certain vendors. By default, disables the
depth prepass for mobile devices as mobile devices do not benefit from
the depth prepass due to their unique architecture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/driver/depth_prepass/enable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/driver/depth_prepass/enable** = `true`
`🔗<class_ProjectSettings_property_rendering/driver/depth_prepass/enable>`{.interpreted-text
role="ref"}

If `true`, performs a previous depth pass before rendering 3D materials.
This increases performance significantly in scenes with high overdraw,
when complex materials and lighting are used. However, in scenes with
few occluded surfaces, the depth prepass may reduce performance. If your
game is viewed from a fixed angle that makes it easy to avoid overdraw
(such as top-down or side-scrolling perspective), consider disabling the
depth prepass to improve performance. This setting can be changed at
run-time to optimize performance depending on the scene currently being
viewed.

\*\*Note:\*\* Depth prepass is only supported when using the Forward+ or
Compatibility rendering method. When using the Mobile rendering method,
there is no depth prepass performed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/driver/threads/thread_model}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/driver/threads/thread_model** = `1`
`🔗<class_ProjectSettings_property_rendering/driver/threads/thread_model>`{.interpreted-text
role="ref"}

**Experimental:** This setting has several known bugs which can lead to
crashing, especially when using particles or resizing the window. Not
recommended for use in production at this stage.

The thread model to use for rendering. Rendering on a thread may improve
performance, but synchronizing to the main thread can cause a bit more
jitter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/defaults/default_clear_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**rendering/environment/defaults/default_clear_color** =
`Color(0.3, 0.3, 0.3, 1)`
`🔗<class_ProjectSettings_property_rendering/environment/defaults/default_clear_color>`{.interpreted-text
role="ref"}

Default background clear color. Overridable per
`Viewport<class_Viewport>`{.interpreted-text role="ref"} using its
`Environment<class_Environment>`{.interpreted-text role="ref"}. See
`Environment.background_mode<class_Environment_property_background_mode>`{.interpreted-text
role="ref"} and
`Environment.background_color<class_Environment_property_background_color>`{.interpreted-text
role="ref"} in particular. To change this default color
programmatically, use
`RenderingServer.set_default_clear_color()<class_RenderingServer_method_set_default_clear_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/defaults/default_environment}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/environment/defaults/default_environment** = `""`
`🔗<class_ProjectSettings_property_rendering/environment/defaults/default_environment>`{.interpreted-text
role="ref"}

`Environment<class_Environment>`{.interpreted-text role="ref"} that will
be used as a fallback environment in case a scene does not specify its
own environment. The default environment is loaded in at scene load time
regardless of whether you have set an environment or not. If you do not
rely on the fallback environment, you do not need to set this property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/glow/upscale_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/glow/upscale_mode** = `1`
`🔗<class_ProjectSettings_property_rendering/environment/glow/upscale_mode>`{.interpreted-text
role="ref"}

Sets how the glow effect is upscaled before being copied onto the
screen. Linear is faster, but looks blocky. Bicubic is slower but looks
smooth.

\*\*Note:\*\*
`rendering/environment/glow/upscale_mode<class_ProjectSettings_property_rendering/environment/glow/upscale_mode>`{.interpreted-text
role="ref"} is only effective when using the Forward+ or Mobile
rendering methods, as Compatibility uses a different glow
implementation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/glow/upscale_mode.mobile}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/glow/upscale_mode.mobile** = `0`
`🔗<class_ProjectSettings_property_rendering/environment/glow/upscale_mode.mobile>`{.interpreted-text
role="ref"}

Lower-end override for
`rendering/environment/glow/upscale_mode<class_ProjectSettings_property_rendering/environment/glow/upscale_mode>`{.interpreted-text
role="ref"} on mobile devices, due to performance concerns or driver
support.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/screen_space_reflection/roughness_quality}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/screen_space_reflection/roughness_quality** =
`1`
`🔗<class_ProjectSettings_property_rendering/environment/screen_space_reflection/roughness_quality>`{.interpreted-text
role="ref"}

Sets the quality for rough screen-space reflections. Turning off will
make all screen space reflections sharp, while higher values make rough
reflections look better.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssao/adaptive_target}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/environment/ssao/adaptive_target** = `0.5`
`🔗<class_ProjectSettings_property_rendering/environment/ssao/adaptive_target>`{.interpreted-text
role="ref"}

Quality target to use when
`rendering/environment/ssao/quality<class_ProjectSettings_property_rendering/environment/ssao/quality>`{.interpreted-text
role="ref"} is set to `Ultra`. A value of `0.0` provides a quality and
speed similar to `Medium` while a value of `1.0` provides much higher
quality than any of the other settings at the cost of performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssao/blur_passes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/ssao/blur_passes** = `2`
`🔗<class_ProjectSettings_property_rendering/environment/ssao/blur_passes>`{.interpreted-text
role="ref"}

Number of blur passes to use when computing screen-space ambient
occlusion. A higher number will result in a smoother look, but will be
slower to compute and will have less high-frequency detail.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssao/fadeout_from}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/environment/ssao/fadeout_from** = `50.0`
`🔗<class_ProjectSettings_property_rendering/environment/ssao/fadeout_from>`{.interpreted-text
role="ref"}

Distance at which the screen-space ambient occlusion effect starts to
fade out. Use this hide ambient occlusion from far away.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssao/fadeout_to}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/environment/ssao/fadeout_to** = `300.0`
`🔗<class_ProjectSettings_property_rendering/environment/ssao/fadeout_to>`{.interpreted-text
role="ref"}

Distance at which the screen-space ambient occlusion is fully faded out.
Use this hide ambient occlusion from far away.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssao/half_size}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/environment/ssao/half_size** = `true`
`🔗<class_ProjectSettings_property_rendering/environment/ssao/half_size>`{.interpreted-text
role="ref"}

If `true`, screen-space ambient occlusion will be rendered at half size
and then upscaled before being added to the scene. This is significantly
faster but may miss small details. If `false`, screen-space ambient
occlusion will be rendered at full size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssao/quality}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/ssao/quality** = `2`
`🔗<class_ProjectSettings_property_rendering/environment/ssao/quality>`{.interpreted-text
role="ref"}

Sets the quality of the screen-space ambient occlusion effect. Higher
values take more samples and so will result in better quality, at the
cost of performance. Setting to `Ultra` will use the
`rendering/environment/ssao/adaptive_target<class_ProjectSettings_property_rendering/environment/ssao/adaptive_target>`{.interpreted-text
role="ref"} setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssil/adaptive_target}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/environment/ssil/adaptive_target** = `0.5`
`🔗<class_ProjectSettings_property_rendering/environment/ssil/adaptive_target>`{.interpreted-text
role="ref"}

Quality target to use when
`rendering/environment/ssil/quality<class_ProjectSettings_property_rendering/environment/ssil/quality>`{.interpreted-text
role="ref"} is set to `Ultra`. A value of `0.0` provides a quality and
speed similar to `Medium` while a value of `1.0` provides much higher
quality than any of the other settings at the cost of performance. When
using the adaptive target, the performance cost scales with the
complexity of the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssil/blur_passes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/ssil/blur_passes** = `4`
`🔗<class_ProjectSettings_property_rendering/environment/ssil/blur_passes>`{.interpreted-text
role="ref"}

Number of blur passes to use when computing screen-space indirect
lighting. A higher number will result in a smoother look, but will be
slower to compute and will have less high-frequency detail.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssil/fadeout_from}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/environment/ssil/fadeout_from** = `50.0`
`🔗<class_ProjectSettings_property_rendering/environment/ssil/fadeout_from>`{.interpreted-text
role="ref"}

Distance at which the screen-space indirect lighting effect starts to
fade out. Use this to hide screen-space indirect lighting from far away.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssil/fadeout_to}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/environment/ssil/fadeout_to** = `300.0`
`🔗<class_ProjectSettings_property_rendering/environment/ssil/fadeout_to>`{.interpreted-text
role="ref"}

Distance at which the screen-space indirect lighting is fully faded out.
Use this to hide screen-space indirect lighting from far away.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssil/half_size}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/environment/ssil/half_size** = `true`
`🔗<class_ProjectSettings_property_rendering/environment/ssil/half_size>`{.interpreted-text
role="ref"}

If `true`, screen-space indirect lighting will be rendered at half size
and then upscaled before being added to the scene. This is significantly
faster but may miss small details and may result in some objects
appearing to glow at their edges.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/ssil/quality}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/ssil/quality** = `2`
`🔗<class_ProjectSettings_property_rendering/environment/ssil/quality>`{.interpreted-text
role="ref"}

Sets the quality of the screen-space indirect lighting effect. Higher
values take more samples and so will result in better quality, at the
cost of performance. Setting to `Ultra` will use the
`rendering/environment/ssil/adaptive_target<class_ProjectSettings_property_rendering/environment/ssil/adaptive_target>`{.interpreted-text
role="ref"} setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale**
= `0.01`
`🔗<class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale>`{.interpreted-text
role="ref"}

Scales the depth over which the subsurface scattering effect is applied.
A high value may allow light to scatter into a part of the mesh or
another mesh that is close in screen space but far in depth. See also
`rendering/environment/subsurface_scattering/subsurface_scattering_scale<class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_scale>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is only read when the project starts. To set
the subsurface scattering depth scale at runtime, call
`RenderingServer.sub_surface_scattering_set_scale()<class_RenderingServer_method_sub_surface_scattering_set_scale>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_quality}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/subsurface_scattering/subsurface_scattering_quality**
= `1`
`🔗<class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_quality>`{.interpreted-text
role="ref"}

Sets the quality of the subsurface scattering effect. Higher values are
slower but look nicer. This affects the rendering of materials that have
`BaseMaterial3D.subsurf_scatter_enabled<class_BaseMaterial3D_property_subsurf_scatter_enabled>`{.interpreted-text
role="ref"} set to `true`, along with
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}s
that set `SSS_STRENGTH`.

\*\*Note:\*\* This property is only read when the project starts. To set
the subsurface scattering quality at runtime, call
`RenderingServer.sub_surface_scattering_set_quality()<class_RenderingServer_method_sub_surface_scattering_set_quality>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/environment/subsurface_scattering/subsurface_scattering_scale**
= `0.05`
`🔗<class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_scale>`{.interpreted-text
role="ref"}

Scales the distance over which samples are taken for subsurface
scattering effect. Changing this does not impact performance, but higher
values will result in significant artifacts as the samples will become
obviously spread out. A lower value results in a smaller spread of
scattered light. See also
`rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale<class_ProjectSettings_property_rendering/environment/subsurface_scattering/subsurface_scattering_depth_scale>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is only read when the project starts. To set
the subsurface scattering scale at runtime, call
`RenderingServer.sub_surface_scattering_set_scale()<class_RenderingServer_method_sub_surface_scattering_set_scale>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/volumetric_fog/use_filter}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/volumetric_fog/use_filter** = `1`
`🔗<class_ProjectSettings_property_rendering/environment/volumetric_fog/use_filter>`{.interpreted-text
role="ref"}

Enables filtering of the volumetric fog effect prior to integration.
This substantially blurs the fog which reduces fine details but also
smooths out harsh edges and aliasing artifacts. Disable when more detail
is required.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/volumetric_fog/volume_depth}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/volumetric_fog/volume_depth** = `64`
`🔗<class_ProjectSettings_property_rendering/environment/volumetric_fog/volume_depth>`{.interpreted-text
role="ref"}

Number of slices to use along the depth of the froxel buffer for
volumetric fog. A lower number will be more efficient but may result in
artifacts appearing during camera movement. See also
`Environment.volumetric_fog_length<class_Environment_property_volumetric_fog_length>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/environment/volumetric_fog/volume_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/environment/volumetric_fog/volume_size** = `64`
`🔗<class_ProjectSettings_property_rendering/environment/volumetric_fog/volume_size>`{.interpreted-text
role="ref"}

Base size used to determine size of froxel buffer in the camera X-axis
and Y-axis. The final size is scaled by the aspect ratio of the screen,
so actual values may differ from what is set. Set a larger size for more
detailed fog, set a smaller size for better performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/driver}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/driver** = `"opengl3"`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/driver>`{.interpreted-text
role="ref"}

Sets the driver to be used by the renderer when using the Compatibility
renderer. Editing this property has no effect in the default
configuration, as first-party platforms each have platform-specific
overrides. Use those overrides to configure the driver for each
platform.

This can be overridden using the `--rendering-driver <driver>` command
line argument.

Supported values are:

- `opengl3`, OpenGL 3.3 on desktop platforms, OpenGL ES 3.0 on mobile
  platforms, WebGL 2.0 on web.
- `opengl3_angle`, OpenGL ES 3.0 using the ANGLE compatibility layer,
  supported on macOS (over native OpenGL) and Windows (over Direct3D
  11).
- `opengl3_es`, OpenGL ES 3.0 on Linux/BSD.

\*\*Note:\*\* The availability of these options depends on whether the
engine was compiled with support for them (determined by SCons options
`opengl3` and `angle_libs`).

\*\*Note:\*\* The actual rendering driver may be automatically changed
by the engine as a result of a fallback, or a user-specified command
line argument. To get the actual rendering driver that is used at
runtime, use
`RenderingServer.get_current_rendering_driver_name()<class_RenderingServer_method_get_current_rendering_driver_name>`{.interpreted-text
role="ref"} instead of reading this project setting\'s value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/driver.android}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/driver.android** = `"opengl3"`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/driver.android>`{.interpreted-text
role="ref"}

Android override for
`rendering/gl_compatibility/driver<class_ProjectSettings_property_rendering/gl_compatibility/driver>`{.interpreted-text
role="ref"}.

Only one option is supported:

- `opengl3`, OpenGL ES 3.0 from native drivers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/driver.ios}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/driver.ios** = `"opengl3"`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/driver.ios>`{.interpreted-text
role="ref"}

iOS override for
`rendering/gl_compatibility/driver<class_ProjectSettings_property_rendering/gl_compatibility/driver>`{.interpreted-text
role="ref"}.

Only one option is supported:

- `opengl3`, OpenGL ES 3.0 from native drivers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/driver.linuxbsd}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/driver.linuxbsd** = `"opengl3"`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/driver.linuxbsd>`{.interpreted-text
role="ref"}

LinuxBSD override for
`rendering/gl_compatibility/driver<class_ProjectSettings_property_rendering/gl_compatibility/driver>`{.interpreted-text
role="ref"}.

Two options are supported:

- `opengl3` (default), OpenGL 3.3 from native drivers.
- `opengl3_es`, OpenGL ES 3.0 from native drivers. If
  `rendering/gl_compatibility/fallback_to_gles<class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_gles>`{.interpreted-text
  role="ref"} is enabled, this is used as a fallback if OpenGL 3.3 is
  not supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/driver.macos}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/driver.macos** = `"opengl3"`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/driver.macos>`{.interpreted-text
role="ref"}

macOS override for
`rendering/gl_compatibility/driver<class_ProjectSettings_property_rendering/gl_compatibility/driver>`{.interpreted-text
role="ref"}.

Two options are supported:

- `opengl3` (default), OpenGL 3.3 from native drivers. If
  `rendering/gl_compatibility/fallback_to_native<class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_native>`{.interpreted-text
  role="ref"} is enabled, this is used as a fallback if ANGLE is
  configured as the preferred driver but not supported.
- `opengl3_angle`, OpenGL ES 3.0 using the ANGLE compatibility layer
  over native OpenGL drivers. If
  `rendering/gl_compatibility/fallback_to_angle<class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_angle>`{.interpreted-text
  role="ref"} is enabled, this is used as a fallback if OpenGL 3.3 is
  not supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/driver.web}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/driver.web** = `"opengl3"`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/driver.web>`{.interpreted-text
role="ref"}

Web override for
`rendering/gl_compatibility/driver<class_ProjectSettings_property_rendering/gl_compatibility/driver>`{.interpreted-text
role="ref"}.

Only one option is supported:

- `opengl3`, WebGL 2.0. The underlying native API depends on the target
  OS, browser, and browser configuration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/driver.windows}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/driver.windows** = `"opengl3"`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/driver.windows>`{.interpreted-text
role="ref"}

Windows override for
`rendering/gl_compatibility/driver<class_ProjectSettings_property_rendering/gl_compatibility/driver>`{.interpreted-text
role="ref"}.

Two options are supported:

- `opengl3` (default), OpenGL 3.3 from native drivers. If
  `rendering/gl_compatibility/fallback_to_native<class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_native>`{.interpreted-text
  role="ref"} is enabled, this is used as a fallback if ANGLE is
  configured as the preferred driver but not supported.
- `opengl3_angle`, OpenGL ES 3.0 using the ANGLE compatibility layer
  over native Direct3D 11 drivers. If
  `rendering/gl_compatibility/fallback_to_angle<class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_angle>`{.interpreted-text
  role="ref"} is enabled, this is used as a fallback if OpenGL 3.3 is
  not supported. By default, ANGLE is used as the default driver for
  some devices listed in
  `rendering/gl_compatibility/force_angle_on_devices<class_ProjectSettings_property_rendering/gl_compatibility/force_angle_on_devices>`{.interpreted-text
  role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_angle}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/fallback_to_angle** = `true`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_angle>`{.interpreted-text
role="ref"}

If `true`, the Compatibility renderer will fall back to ANGLE if native
OpenGL is not supported or the device is listed in
`rendering/gl_compatibility/force_angle_on_devices<class_ProjectSettings_property_rendering/gl_compatibility/force_angle_on_devices>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This setting is implemented only on Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_gles}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/fallback_to_gles** = `true`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_gles>`{.interpreted-text
role="ref"}

If `true`, the Compatibility renderer will fall back to OpenGLES if
desktop OpenGL is not supported.

\*\*Note:\*\* This setting is implemented only on Linux/X11.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_native}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/fallback_to_native** = `true`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/fallback_to_native>`{.interpreted-text
role="ref"}

If `true`, the Compatibility renderer will fall back to native OpenGL if
ANGLE is not supported, or ANGLE dynamic libraries aren\'t found.

\*\*Note:\*\* This setting is implemented on macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/force_angle_on_devices}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/force_angle_on_devices**
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/force_angle_on_devices>`{.interpreted-text
role="ref"}

An `Array<class_Array>`{.interpreted-text role="ref"} of devices which
should always use the ANGLE renderer.

Each entry is a `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} with the following keys: `vendor` and `name`. `name` can be
set to `*` to add all devices with the specified `vendor`.

\*\*Note:\*\* This setting is implemented only on Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/item_buffer_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/item_buffer_size** = `16384`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/item_buffer_size>`{.interpreted-text
role="ref"}

Maximum number of canvas items commands that can be drawn in a single
viewport update. If more render commands are issued they will be
ignored. Decreasing this limit may improve performance on bandwidth
limited devices. Increase this limit if you find that not all objects
are being drawn in a frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/gl_compatibility/nvidia_disable_threaded_optimization}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/gl_compatibility/nvidia_disable_threaded_optimization** =
`true`
`🔗<class_ProjectSettings_property_rendering/gl_compatibility/nvidia_disable_threaded_optimization>`{.interpreted-text
role="ref"}

If `true`, disables the threaded optimization feature from the NVIDIA
drivers, which are known to cause stuttering in most OpenGL
applications.

\*\*Note:\*\* This setting only works on Windows, as threaded
optimization is disabled by default on other platforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/global_illumination/gi/use_half_resolution}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/global_illumination/gi/use_half_resolution** = `false`
`🔗<class_ProjectSettings_property_rendering/global_illumination/gi/use_half_resolution>`{.interpreted-text
role="ref"}

If `true`, renders `VoxelGI<class_VoxelGI>`{.interpreted-text
role="ref"} and SDFGI
(`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}) buffers at halved resolution (e.g. 960×540 when the
viewport size is 1920×1080). This improves performance significantly
when VoxelGI or SDFGI is enabled, at the cost of artifacts that may be
visible on polygon edges. The loss in quality becomes less noticeable as
the viewport resolution increases.
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} rendering
is not affected by this setting.

\*\*Note:\*\* This property is only read when the project starts. To set
half-resolution GI at run-time, call
`RenderingServer.gi_set_use_half_resolution()<class_RenderingServer_method_gi_set_use_half_resolution>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_converge}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/global_illumination/sdfgi/frames_to_converge** = `5`
`🔗<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_converge>`{.interpreted-text
role="ref"}

The number of frames to use for converging signed distance field global
illumination. Higher values lead to a less noisy result, at the cost of
taking a longer time to fully converge. This means the scene\'s global
illumination will be too dark for a longer period of time, especially
when the camera moves fast. The actual convergence speed depends on
rendered framerate. For example, with the default setting of 30 frames,
rendering at 60 FPS will make SDFGI fully converge after 0.5 seconds.
See also
`rendering/global_illumination/sdfgi/frames_to_update_lights<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_update_lights>`{.interpreted-text
role="ref"} and
`rendering/global_illumination/sdfgi/probe_ray_count<class_ProjectSettings_property_rendering/global_illumination/sdfgi/probe_ray_count>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is only read when the project starts. To
control SDFGI convergence speed at runtime, call
`RenderingServer.environment_set_sdfgi_frames_to_converge()<class_RenderingServer_method_environment_set_sdfgi_frames_to_converge>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_update_lights}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/global_illumination/sdfgi/frames_to_update_lights** = `2`
`🔗<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_update_lights>`{.interpreted-text
role="ref"}

The number of frames over which dynamic lights should be updated in
signed distance field global illumination. Higher values take more time
to update indirect lighting coming from dynamic lights, but result in
better performance when many dynamic lights are present. See also
`rendering/global_illumination/sdfgi/frames_to_converge<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_converge>`{.interpreted-text
role="ref"} and
`rendering/global_illumination/sdfgi/probe_ray_count<class_ProjectSettings_property_rendering/global_illumination/sdfgi/probe_ray_count>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This only affects
`Light3D<class_Light3D>`{.interpreted-text role="ref"} nodes whose
`Light3D.light_bake_mode<class_Light3D_property_light_bake_mode>`{.interpreted-text
role="ref"} is
`Light3D.BAKE_DYNAMIC<class_Light3D_constant_BAKE_DYNAMIC>`{.interpreted-text
role="ref"} (which is the default). Consider making non-moving lights
use the
`Light3D.BAKE_STATIC<class_Light3D_constant_BAKE_STATIC>`{.interpreted-text
role="ref"} bake mode to improve performance.

\*\*Note:\*\* This property is only read when the project starts. To
control SDFGI light update speed at runtime, call
`RenderingServer.environment_set_sdfgi_frames_to_update_light()<class_RenderingServer_method_environment_set_sdfgi_frames_to_update_light>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/global_illumination/sdfgi/probe_ray_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/global_illumination/sdfgi/probe_ray_count** = `1`
`🔗<class_ProjectSettings_property_rendering/global_illumination/sdfgi/probe_ray_count>`{.interpreted-text
role="ref"}

The number of rays to throw per frame when computing signed distance
field global illumination. Higher values lead to a less noisy result, at
the cost of performance. See also
`rendering/global_illumination/sdfgi/frames_to_converge<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_converge>`{.interpreted-text
role="ref"} and
`rendering/global_illumination/sdfgi/frames_to_update_lights<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_update_lights>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is only read when the project starts. To
control SDFGI quality at runtime, call
`RenderingServer.environment_set_sdfgi_ray_count()<class_RenderingServer_method_environment_set_sdfgi_ray_count>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/global_illumination/voxel_gi/quality}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/global_illumination/voxel_gi/quality** = `0`
`🔗<class_ProjectSettings_property_rendering/global_illumination/voxel_gi/quality>`{.interpreted-text
role="ref"}

The VoxelGI quality to use. High quality leads to more precise lighting
and better reflections, but is slower to render. This setting does not
affect the baked data and doesn\'t require baking the
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} again to apply.

\*\*Note:\*\* This property is only read when the project starts. To
control VoxelGI quality at runtime, call
`RenderingServer.voxel_gi_set_quality()<class_RenderingServer_method_voxel_gi_set_quality>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_performance/max_rays_per_pass}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_performance/max_rays_per_pass** = `4`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_performance/max_rays_per_pass>`{.interpreted-text
role="ref"}

The maximum number of rays that can be thrown per pass when baking
lightmaps with `LightmapGI<class_LightmapGI>`{.interpreted-text
role="ref"}. Depending on the scene, adjusting this value may result in
higher GPU utilization when baking lightmaps, leading to faster bake
times.

\*\*Note:\*\* Using a value that is too high for your system can cause
crashes due to the GPU being unresponsive for long periods of time, and
the graphics driver being reset by the OS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_performance/max_rays_per_probe_pass}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_performance/max_rays_per_probe_pass** =
`64`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_performance/max_rays_per_probe_pass>`{.interpreted-text
role="ref"}

The maximum number of rays that can be thrown per pass when baking
dynamic object lighting in
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}s with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}. Depending
on the scene, adjusting this value may result in higher GPU utilization
when baking lightmaps, leading to faster bake times.

\*\*Note:\*\* Using a value that is too high for your system can cause
crashes due to the GPU being unresponsive for long periods of time, and
the graphics driver being reset by the OS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_performance/max_transparency_rays}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_performance/max_transparency_rays** = `8`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_performance/max_transparency_rays>`{.interpreted-text
role="ref"}

The maximum number of retry rays that can be thrown per pass when
hitting a transparent surface when baking lightmaps with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}. Depending
on the scene, reducing this value may lead to faster bake times.

\*\*Note:\*\* Using a value that is too high for your system can cause
crashes due to the GPU being unresponsive for long periods of time, and
the graphics driver being reset by the OS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_performance/region_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_performance/region_size** = `512`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_performance/region_size>`{.interpreted-text
role="ref"}

The region size to use when baking lightmaps with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}. The
specified value is rounded up to the nearest power of 2.

\*\*Note:\*\* Using a value that is too high for your system can cause
crashes due to the GPU being unresponsive for long periods of time, and
the graphics driver being reset by the OS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_quality/high_quality_probe_ray_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_quality/high_quality_probe_ray_count** =
`512`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_quality/high_quality_probe_ray_count>`{.interpreted-text
role="ref"}

The number of rays to use for baking dynamic object lighting in
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}s when
`LightmapGI.quality<class_LightmapGI_property_quality>`{.interpreted-text
role="ref"} is
`LightmapGI.BAKE_QUALITY_HIGH<class_LightmapGI_constant_BAKE_QUALITY_HIGH>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_quality/high_quality_ray_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_quality/high_quality_ray_count** = `512`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_quality/high_quality_ray_count>`{.interpreted-text
role="ref"}

The number of rays to use for baking lightmaps with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} when
`LightmapGI.quality<class_LightmapGI_property_quality>`{.interpreted-text
role="ref"} is
`LightmapGI.BAKE_QUALITY_HIGH<class_LightmapGI_constant_BAKE_QUALITY_HIGH>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_quality/low_quality_probe_ray_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_quality/low_quality_probe_ray_count** =
`64`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_quality/low_quality_probe_ray_count>`{.interpreted-text
role="ref"}

The number of rays to use for baking dynamic object lighting in
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}s when
`LightmapGI.quality<class_LightmapGI_property_quality>`{.interpreted-text
role="ref"} is
`LightmapGI.BAKE_QUALITY_LOW<class_LightmapGI_constant_BAKE_QUALITY_LOW>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_quality/low_quality_ray_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_quality/low_quality_ray_count** = `32`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_quality/low_quality_ray_count>`{.interpreted-text
role="ref"}

The number of rays to use for baking lightmaps with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} when
`LightmapGI.quality<class_LightmapGI_property_quality>`{.interpreted-text
role="ref"} is
`LightmapGI.BAKE_QUALITY_LOW<class_LightmapGI_constant_BAKE_QUALITY_LOW>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_quality/medium_quality_probe_ray_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_quality/medium_quality_probe_ray_count** =
`256`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_quality/medium_quality_probe_ray_count>`{.interpreted-text
role="ref"}

The number of rays to use for baking dynamic object lighting in
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}s when
`LightmapGI.quality<class_LightmapGI_property_quality>`{.interpreted-text
role="ref"} is
`LightmapGI.BAKE_QUALITY_MEDIUM<class_LightmapGI_constant_BAKE_QUALITY_MEDIUM>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_quality/medium_quality_ray_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_quality/medium_quality_ray_count** = `128`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_quality/medium_quality_ray_count>`{.interpreted-text
role="ref"}

The number of rays to use for baking lightmaps with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} when
`LightmapGI.quality<class_LightmapGI_property_quality>`{.interpreted-text
role="ref"} is
`LightmapGI.BAKE_QUALITY_MEDIUM<class_LightmapGI_constant_BAKE_QUALITY_MEDIUM>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count** =
`2048`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count>`{.interpreted-text
role="ref"}

The number of rays to use for baking dynamic object lighting in
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}s when
`LightmapGI.quality<class_LightmapGI_property_quality>`{.interpreted-text
role="ref"} is
`LightmapGI.BAKE_QUALITY_ULTRA<class_LightmapGI_constant_BAKE_QUALITY_ULTRA>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/bake_quality/ultra_quality_ray_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/bake_quality/ultra_quality_ray_count** = `2048`
`🔗<class_ProjectSettings_property_rendering/lightmapping/bake_quality/ultra_quality_ray_count>`{.interpreted-text
role="ref"}

The number of rays to use for baking lightmaps with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} when
`LightmapGI.quality<class_LightmapGI_property_quality>`{.interpreted-text
role="ref"} is
`LightmapGI.BAKE_QUALITY_ULTRA<class_LightmapGI_constant_BAKE_QUALITY_ULTRA>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/denoising/denoiser}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lightmapping/denoising/denoiser** = `0`
`🔗<class_ProjectSettings_property_rendering/lightmapping/denoising/denoiser>`{.interpreted-text
role="ref"}

Denoiser tool used for denoising lightmaps.

Using [OpenImageDenoise](https://www.openimagedenoise.org/) (OIDN)
requires configuring a path to an OIDN executable in the editor settings
at
`EditorSettings.filesystem/tools/oidn/oidn_denoise_path<class_EditorSettings_property_filesystem/tools/oidn/oidn_denoise_path>`{.interpreted-text
role="ref"}. OIDN can be downloaded from [OpenImageDenoise\'s downloads
page](https://www.openimagedenoise.org/downloads.html).

OIDN will use GPU acceleration when available. Unlike JNLM which uses
compute shaders for acceleration, OIDN uses vendor-specific acceleration
methods. For GPU acceleration to be available, the following libraries
must be installed on the system depending on your GPU:

- NVIDIA GPUs: CUDA libraries
- AMD GPUs: HIP libraries
- Intel GPUs: SYCL libraries

If no GPU acceleration is configured on the system, multi-threaded
CPU-based denoising will be performed instead. This CPU-based denoising
is significantly slower than the JNLM denoiser in most cases.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/lightmap_gi/use_bicubic_filter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/lightmapping/lightmap_gi/use_bicubic_filter** = `true`
`🔗<class_ProjectSettings_property_rendering/lightmapping/lightmap_gi/use_bicubic_filter>`{.interpreted-text
role="ref"}

If `true`, applies a bicubic filter during lightmap sampling. This makes
lightmaps look much smoother, at a moderate performance cost.

\*\*Note:\*\* The bicubic filter exaggerates the \'bleeding\' effect
that occurs when a lightmap\'s resolution is low enough.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/primitive_meshes/texel_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/lightmapping/primitive_meshes/texel_size** = `0.2`
`🔗<class_ProjectSettings_property_rendering/lightmapping/primitive_meshes/texel_size>`{.interpreted-text
role="ref"}

The texel_size that is used to calculate the
`Mesh.lightmap_size_hint<class_Mesh_property_lightmap_size_hint>`{.interpreted-text
role="ref"} on `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} resources if
`PrimitiveMesh.add_uv2<class_PrimitiveMesh_property_add_uv2>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lightmapping/probe_capture/update_speed}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/lightmapping/probe_capture/update_speed** = `15`
`🔗<class_ProjectSettings_property_rendering/lightmapping/probe_capture/update_speed>`{.interpreted-text
role="ref"}

The framerate-independent update speed when representing dynamic object
lighting from `LightmapProbe<class_LightmapProbe>`{.interpreted-text
role="ref"}s. Higher values make dynamic object lighting update faster.
Higher values can prevent fast-moving objects from having \"outdated\"
indirect lighting displayed on them, at the cost of possible flickering
when an object moves from a bright area to a shaded area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/16_bits}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/directional_shadow/16_bits** = `true`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/16_bits>`{.interpreted-text
role="ref"}

Use 16 bits for the directional shadow depth map. Enabling this results
in shadows having less precision and may result in shadow acne, but can
lead to performance improvements on some devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/directional_shadow/size** = `4096`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/size>`{.interpreted-text
role="ref"}

The directional shadow\'s size in pixels. Higher values will result in
sharper shadows, at the cost of performance. The value is rounded up to
the nearest power of 2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/size.mobile}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/directional_shadow/size.mobile** = `2048`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/size.mobile>`{.interpreted-text
role="ref"}

Lower-end override for
`rendering/lights_and_shadows/directional_shadow/size<class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/size>`{.interpreted-text
role="ref"} on mobile devices, due to performance concerns or driver
support.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality**
= `2`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality>`{.interpreted-text
role="ref"}

Quality setting for shadows cast by
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s. Higher quality settings use more samples when reading from
shadow maps and are thus slower. Low quality settings may result in
shadows looking grainy.

\*\*Note:\*\* The Soft Very Low setting will automatically multiply
*constant* shadow blur by 0.75x to reduce the amount of noise visible.
This automatic blur change only affects the constant blur factor defined
in
`Light3D.shadow_blur<class_Light3D_property_shadow_blur>`{.interpreted-text
role="ref"}, not the variable blur performed by
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s\'
`Light3D.light_angular_distance<class_Light3D_property_light_angular_distance>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The Soft High and Soft Ultra settings will automatically
multiply *constant* shadow blur by 1.5× and 2× respectively to make
better use of the increased sample count. This increased blur also
improves stability of dynamic object shadows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality.mobile}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality.mobile**
= `0`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality.mobile>`{.interpreted-text
role="ref"}

Lower-end override for
`rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality<class_ProjectSettings_property_rendering/lights_and_shadows/directional_shadow/soft_shadow_filter_quality>`{.interpreted-text
role="ref"} on mobile devices, due to performance concerns or driver
support.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_16_bits}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/positional_shadow/atlas_16_bits** =
`true`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_16_bits>`{.interpreted-text
role="ref"}

Use 16 bits for the omni/spot shadow depth map. Enabling this results in
shadows having less precision and may result in shadow acne, but can
lead to performance improvements on some devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_quadrant_0_subdiv}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/positional_shadow/atlas_quadrant_0_subdiv**
= `2`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_quadrant_0_subdiv>`{.interpreted-text
role="ref"}

The subdivision amount of the first quadrant on the shadow atlas. See
the
[documentation](../tutorials/tutorials/3d/lights_and_shadows.html#shadow-atlas)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_quadrant_1_subdiv}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/positional_shadow/atlas_quadrant_1_subdiv**
= `2`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_quadrant_1_subdiv>`{.interpreted-text
role="ref"}

The subdivision amount of the second quadrant on the shadow atlas. See
the
[documentation](../tutorials/tutorials/3d/lights_and_shadows.html#shadow-atlas)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_quadrant_2_subdiv}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/positional_shadow/atlas_quadrant_2_subdiv**
= `3`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_quadrant_2_subdiv>`{.interpreted-text
role="ref"}

The subdivision amount of the third quadrant on the shadow atlas. See
the
[documentation](../tutorials/tutorials/3d/lights_and_shadows.html#shadow-atlas)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_quadrant_3_subdiv}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/positional_shadow/atlas_quadrant_3_subdiv**
= `4`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_quadrant_3_subdiv>`{.interpreted-text
role="ref"}

The subdivision amount of the fourth quadrant on the shadow atlas. See
the
[documentation](../tutorials/tutorials/3d/lights_and_shadows.html#shadow-atlas)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/positional_shadow/atlas_size** = `4096`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_size>`{.interpreted-text
role="ref"}

The size of the shadow atlas used for
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"} nodes.
See the
[documentation](../tutorials/tutorials/3d/lights_and_shadows.html#shadow-atlas)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_size.mobile}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/positional_shadow/atlas_size.mobile** =
`2048`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_size.mobile>`{.interpreted-text
role="ref"}

Lower-end override for
`rendering/lights_and_shadows/positional_shadow/atlas_size<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/atlas_size>`{.interpreted-text
role="ref"} on mobile devices, due to performance concerns or driver
support.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality**
= `2`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality>`{.interpreted-text
role="ref"}

Quality setting for shadows cast by
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"}s and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}s. Higher
quality settings use more samples when reading from shadow maps and are
thus slower. Low quality settings may result in shadows looking grainy.

\*\*Note:\*\* The Soft Very Low setting will automatically multiply
*constant* shadow blur by 0.75x to reduce the amount of noise visible.
This automatic blur change only affects the constant blur factor defined
in
`Light3D.shadow_blur<class_Light3D_property_shadow_blur>`{.interpreted-text
role="ref"}, not the variable blur performed by
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s\'
`Light3D.light_angular_distance<class_Light3D_property_light_angular_distance>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The Soft High and Soft Ultra settings will automatically
multiply shadow blur by 1.5× and 2× respectively to make better use of
the increased sample count. This increased blur also improves stability
of dynamic object shadows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality.mobile}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality.mobile**
= `0`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality.mobile>`{.interpreted-text
role="ref"}

Lower-end override for
`rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality<class_ProjectSettings_property_rendering/lights_and_shadows/positional_shadow/soft_shadow_filter_quality>`{.interpreted-text
role="ref"} on mobile devices, due to performance concerns or driver
support.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/tighter_shadow_caster_culling}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/tighter_shadow_caster_culling** = `true`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/tighter_shadow_caster_culling>`{.interpreted-text
role="ref"}

If `true`, items that cannot cast shadows into the view frustum will not
be rendered into shadow maps.

This can increase performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/lights_and_shadows/use_physical_light_units** = `false`
`🔗<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>`{.interpreted-text
role="ref"}

Enables the use of physically based units for light sources. Physically
based units tend to be much larger than the arbitrary units used by
Godot, but they can be used to match lighting within Godot to real-world
lighting. Due to the large dynamic range of lighting conditions present
in nature, Godot bakes exposure into the various lighting quantities
before rendering. Most light sources bake exposure automatically at run
time based on the active
`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
resource, but `LightmapGI<class_LightmapGI>`{.interpreted-text
role="ref"} and `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}
require a `CameraAttributes<class_CameraAttributes>`{.interpreted-text
role="ref"} resource to be set at bake time to reduce the dynamic range.
At run time, Godot will automatically reconcile the baked exposure with
the active exposure to ensure lighting remains consistent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/limits/cluster_builder/max_clustered_elements}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/limits/cluster_builder/max_clustered_elements** = `512`
`🔗<class_ProjectSettings_property_rendering/limits/cluster_builder/max_clustered_elements>`{.interpreted-text
role="ref"}

The maximum number of clustered elements
(`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} +
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"} +
`Decal<class_Decal>`{.interpreted-text role="ref"} +
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"})
that can be rendered at once in the camera view. If there are more
clustered elements present in the camera view, some of them will not be
rendered (leading to pop-in during camera movement). Enabling distance
fade on lights and decals
(`Light3D.distance_fade_enabled<class_Light3D_property_distance_fade_enabled>`{.interpreted-text
role="ref"},
`Decal.distance_fade_enabled<class_Decal_property_distance_fade_enabled>`{.interpreted-text
role="ref"}) can help avoid reaching this limit.

Decreasing this value may improve GPU performance on certain setups,
even if the maximum number of clustered elements is never reached in the
project.

\*\*Note:\*\* This setting is only effective when using the Forward+
rendering method, not Mobile and Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/limits/global_shader_variables/buffer_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/limits/global_shader_variables/buffer_size** = `65536`
`🔗<class_ProjectSettings_property_rendering/limits/global_shader_variables/buffer_size>`{.interpreted-text
role="ref"}

The maximum number of uniforms that can be used by the global shader
uniform buffer. Each item takes up one slot. In other words, a single
uniform float and a uniform vec4 will take the same amount of space in
the buffer.

\*\*Note:\*\* When using the Compatibility renderer, most mobile devices
(and all web exports) will be limited to a maximum size of 1024 due to
hardware constraints.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/limits/opengl/max_lights_per_object}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/limits/opengl/max_lights_per_object** = `8`
`🔗<class_ProjectSettings_property_rendering/limits/opengl/max_lights_per_object>`{.interpreted-text
role="ref"}

Max number of omnilights and spotlights renderable per object. At the
default value of 8, this means that each surface can be affected by up
to 8 omnilights and 8 spotlights. This is further limited by hardware
support and
`rendering/limits/opengl/max_renderable_lights<class_ProjectSettings_property_rendering/limits/opengl/max_renderable_lights>`{.interpreted-text
role="ref"}. Setting this low will slightly reduce memory usage, may
decrease shader compile times, and may result in faster rendering on
low-end, mobile, or web devices.

\*\*Note:\*\* This setting is only effective when using the
Compatibility rendering method, not Forward+ and Mobile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/limits/opengl/max_renderable_elements}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/limits/opengl/max_renderable_elements** = `65536`
`🔗<class_ProjectSettings_property_rendering/limits/opengl/max_renderable_elements>`{.interpreted-text
role="ref"}

Max number of elements renderable in a frame. If more elements than this
are visible per frame, they will not be drawn. Keep in mind elements
refer to mesh surfaces and not meshes themselves. Setting this low will
slightly reduce memory usage and may decrease shader compile times,
particularly on web. For most uses, the default value is suitable, but
consider lowering as much as possible on web export.

\*\*Note:\*\* This setting is only effective when using the
Compatibility rendering method, not Forward+ and Mobile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/limits/opengl/max_renderable_lights}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/limits/opengl/max_renderable_lights** = `32`
`🔗<class_ProjectSettings_property_rendering/limits/opengl/max_renderable_lights>`{.interpreted-text
role="ref"}

Max number of positional lights renderable in a frame. If more lights
than this number are used, they will be ignored. Setting this low will
slightly reduce memory usage and may decrease shader compile times,
particularly on web. For most uses, the default value is suitable, but
consider lowering as much as possible on web export.

\*\*Note:\*\* This setting is only effective when using the
Compatibility rendering method, not Forward+ and Mobile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/limits/spatial_indexer/threaded_cull_minimum_instances}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/limits/spatial_indexer/threaded_cull_minimum_instances** =
`1000`
`🔗<class_ProjectSettings_property_rendering/limits/spatial_indexer/threaded_cull_minimum_instances>`{.interpreted-text
role="ref"}

The minimum number of instances that must be present in a scene to
enable culling computations on multiple threads. If a scene has fewer
instances than this number, culling is done on a single thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/limits/spatial_indexer/update_iterations_per_frame}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/limits/spatial_indexer/update_iterations_per_frame** = `10`
`🔗<class_ProjectSettings_property_rendering/limits/spatial_indexer/update_iterations_per_frame>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/limits/time/time_rollover_secs}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/limits/time/time_rollover_secs** = `3600`
`🔗<class_ProjectSettings_property_rendering/limits/time/time_rollover_secs>`{.interpreted-text
role="ref"}

Maximum time (in seconds) before the `TIME` shader built-in variable
rolls over. The `TIME` variable increments by `delta` each frame, and
when it exceeds this value, it rolls over to `0.0`. Since large
floating-point values are less precise than small floating-point values,
this should be set as low as possible to maximize the precision of the
`TIME` built-in variable in shaders. This is especially important on
mobile platforms where precision in shaders is significantly reduced.
However, if this is set too low, shader animations may appear to restart
from the beginning while the project is running.

On desktop platforms, values below `4096` are recommended, ideally below
`2048`. On mobile platforms, values below `64` are recommended, ideally
below `32`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/mesh_lod/lod_change/threshold_pixels}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/mesh_lod/lod_change/threshold_pixels** = `1.0`
`🔗<class_ProjectSettings_property_rendering/mesh_lod/lod_change/threshold_pixels>`{.interpreted-text
role="ref"}

The automatic LOD bias to use for meshes rendered within the
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}.
Higher values will use less detailed versions of meshes that have LOD
variations generated. If set to `0.0`, automatic LOD is disabled.
Increase
`rendering/mesh_lod/lod_change/threshold_pixels<class_ProjectSettings_property_rendering/mesh_lod/lod_change/threshold_pixels>`{.interpreted-text
role="ref"} to improve performance at the cost of geometry detail.

\*\*Note:\*\*
`rendering/mesh_lod/lod_change/threshold_pixels<class_ProjectSettings_property_rendering/mesh_lod/lod_change/threshold_pixels>`{.interpreted-text
role="ref"} does not affect
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} visibility ranges (also known as \"manual\" LOD or
hierarchical LOD).

\*\*Note:\*\* This property is only read when the project starts. To
adjust the automatic LOD threshold at runtime, set
`Viewport.mesh_lod_threshold<class_Viewport_property_mesh_lod_threshold>`{.interpreted-text
role="ref"} on the root `Viewport<class_Viewport>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/occlusion_culling/bvh_build_quality}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/occlusion_culling/bvh_build_quality** = `2`
`🔗<class_ProjectSettings_property_rendering/occlusion_culling/bvh_build_quality>`{.interpreted-text
role="ref"}

The [Bounding Volume
Hierarchy](https://en.wikipedia.org/wiki/Bounding_volume_hierarchy)
quality to use when rendering the occlusion culling buffer. Higher
values will result in more accurate occlusion culling, at the cost of
higher CPU usage. See also
`rendering/occlusion_culling/occlusion_rays_per_thread<class_ProjectSettings_property_rendering/occlusion_culling/occlusion_rays_per_thread>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is only read when the project starts. To
adjust the BVH build quality at runtime, use
`RenderingServer.viewport_set_occlusion_culling_build_quality()<class_RenderingServer_method_viewport_set_occlusion_culling_build_quality>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/occlusion_culling/jitter_projection}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/occlusion_culling/jitter_projection** = `true`
`🔗<class_ProjectSettings_property_rendering/occlusion_culling/jitter_projection>`{.interpreted-text
role="ref"}

If `true`, the projection used for rendering the occlusion buffer will
be jittered. This can help prevent objects being incorrectly culled when
visible through small gaps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/occlusion_culling/occlusion_rays_per_thread}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/occlusion_culling/occlusion_rays_per_thread** = `512`
`🔗<class_ProjectSettings_property_rendering/occlusion_culling/occlusion_rays_per_thread>`{.interpreted-text
role="ref"}

The number of occlusion rays traced per CPU thread. Higher values will
result in more accurate occlusion culling, at the cost of higher CPU
usage. The occlusion culling buffer\'s pixel count is roughly equal to
`occlusion_rays_per_thread * number_of_logical_cpu_cores`, so it will
depend on the system\'s CPU. Therefore, CPUs with fewer cores will use a
lower resolution to attempt keeping performance costs even across
devices. See also
`rendering/occlusion_culling/bvh_build_quality<class_ProjectSettings_property_rendering/occlusion_culling/bvh_build_quality>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property is only read when the project starts. To
adjust the number of occlusion rays traced per thread at runtime, use
`RenderingServer.viewport_set_occlusion_rays_per_thread()<class_RenderingServer_method_viewport_set_occlusion_rays_per_thread>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/occlusion_culling/use_occlusion_culling}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/occlusion_culling/use_occlusion_culling** = `false`
`🔗<class_ProjectSettings_property_rendering/occlusion_culling/use_occlusion_culling>`{.interpreted-text
role="ref"}

If `true`,
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"} nodes will be usable for occlusion culling in 3D in the root
viewport. In custom viewports,
`Viewport.use_occlusion_culling<class_Viewport_property_use_occlusion_culling>`{.interpreted-text
role="ref"} must be set to `true` instead.

\*\*Note:\*\* Enabling occlusion culling has a cost on the CPU. Only
enable occlusion culling if you actually plan to use it. Large open
scenes with few or no objects blocking the view will generally not
benefit much from occlusion culling. Large open scenes generally benefit
more from mesh LOD and visibility ranges
(`GeometryInstance3D.visibility_range_begin<class_GeometryInstance3D_property_visibility_range_begin>`{.interpreted-text
role="ref"} and
`GeometryInstance3D.visibility_range_end<class_GeometryInstance3D_property_visibility_range_end>`{.interpreted-text
role="ref"}) compared to occlusion culling.

\*\*Note:\*\* Due to memory constraints, occlusion culling is not
supported by default in Web export templates. It can be enabled by
compiling custom Web export templates with `module_raycast_enabled=yes`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/reflection_atlas/reflection_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/reflections/reflection_atlas/reflection_count** = `64`
`🔗<class_ProjectSettings_property_rendering/reflections/reflection_atlas/reflection_count>`{.interpreted-text
role="ref"}

Number of cubemaps to store in the reflection atlas. The number of
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}s
in a scene will be limited by this amount. A higher number requires more
VRAM.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/reflection_atlas/reflection_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/reflections/reflection_atlas/reflection_size** = `256`
`🔗<class_ProjectSettings_property_rendering/reflections/reflection_atlas/reflection_size>`{.interpreted-text
role="ref"}

Size of cubemap faces for
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}s.
A higher number requires more VRAM and may make reflection probe
updating slower.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/reflection_atlas/reflection_size.mobile}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/reflections/reflection_atlas/reflection_size.mobile** =
`128`
`🔗<class_ProjectSettings_property_rendering/reflections/reflection_atlas/reflection_size.mobile>`{.interpreted-text
role="ref"}

Lower-end override for
`rendering/reflections/reflection_atlas/reflection_size<class_ProjectSettings_property_rendering/reflections/reflection_atlas/reflection_size>`{.interpreted-text
role="ref"} on mobile devices, due to performance concerns or driver
support.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/sky_reflections/fast_filter_high_quality}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/reflections/sky_reflections/fast_filter_high_quality** =
`false`
`🔗<class_ProjectSettings_property_rendering/reflections/sky_reflections/fast_filter_high_quality>`{.interpreted-text
role="ref"}

Use a higher quality variant of the fast filtering algorithm.
Significantly slower than using default quality, but results in smoother
reflections. Should only be used when the scene is especially detailed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/sky_reflections/ggx_samples}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/reflections/sky_reflections/ggx_samples** = `32`
`🔗<class_ProjectSettings_property_rendering/reflections/sky_reflections/ggx_samples>`{.interpreted-text
role="ref"}

Sets the number of samples to take when using importance sampling for
`Sky<class_Sky>`{.interpreted-text role="ref"}s and
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}s.
A higher value will result in smoother, higher quality reflections, but
increases time to calculate radiance maps. In general, fewer samples are
needed for simpler, low dynamic range environments while more samples
are needed for HDR environments and environments with a high level of
detail.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/sky_reflections/ggx_samples.mobile}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/reflections/sky_reflections/ggx_samples.mobile** = `16`
`🔗<class_ProjectSettings_property_rendering/reflections/sky_reflections/ggx_samples.mobile>`{.interpreted-text
role="ref"}

Lower-end override for
`rendering/reflections/sky_reflections/ggx_samples<class_ProjectSettings_property_rendering/reflections/sky_reflections/ggx_samples>`{.interpreted-text
role="ref"} on mobile devices, due to performance concerns or driver
support.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/sky_reflections/roughness_layers}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/reflections/sky_reflections/roughness_layers** = `8`
`🔗<class_ProjectSettings_property_rendering/reflections/sky_reflections/roughness_layers>`{.interpreted-text
role="ref"}

Limits the number of layers to use in radiance maps when using
importance sampling. A lower number will be slightly faster and take up
less VRAM.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/sky_reflections/texture_array_reflections}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/reflections/sky_reflections/texture_array_reflections** =
`true`
`🔗<class_ProjectSettings_property_rendering/reflections/sky_reflections/texture_array_reflections>`{.interpreted-text
role="ref"}

If `true`, uses texture arrays instead of mipmaps for reflection probes
and panorama backgrounds (sky). This reduces jitter noise and upscaling
artifacts on reflections, but is significantly slower to compute and
uses
`rendering/reflections/sky_reflections/roughness_layers<class_ProjectSettings_property_rendering/reflections/sky_reflections/roughness_layers>`{.interpreted-text
role="ref"} times more memory.

\*\*Note:\*\* Texture array reflections are always disabled on macOS on
Intel GPUs due to driver bugs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/sky_reflections/texture_array_reflections.mobile}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/reflections/sky_reflections/texture_array_reflections.mobile**
= `false`
`🔗<class_ProjectSettings_property_rendering/reflections/sky_reflections/texture_array_reflections.mobile>`{.interpreted-text
role="ref"}

Lower-end override for
`rendering/reflections/sky_reflections/texture_array_reflections<class_ProjectSettings_property_rendering/reflections/sky_reflections/texture_array_reflections>`{.interpreted-text
role="ref"} on mobile devices, due to performance concerns or driver
support.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/reflections/specular_occlusion/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/reflections/specular_occlusion/enabled** = `true`
`🔗<class_ProjectSettings_property_rendering/reflections/specular_occlusion/enabled>`{.interpreted-text
role="ref"}

If `true`, reduces reflections based on ambient light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/renderer/rendering_method}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/renderer/rendering_method** = `"forward_plus"`
`🔗<class_ProjectSettings_property_rendering/renderer/rendering_method>`{.interpreted-text
role="ref"}

Sets the renderer that will be used by the project. Options are:

\*\*forward_plus\*\* (Forward+): High-end renderer designed for desktop
devices. Has a higher base overhead, but scales well with complex
scenes. Not suitable for older devices or mobile.

\*\*mobile\*\* (Mobile): Modern renderer designed for mobile devices.
Has a lower base overhead than Forward+, but does not scale as well to
large scenes with many elements.

\*\*gl_compatibility\*\* (Compatibility): Low-end renderer designed for
older devices. Based on the limitations of the OpenGL 3.3 / OpenGL ES
3.0 / WebGL 2 APIs.

This can be overridden using the `--rendering-method <method>` command
line argument.

\*\*Note:\*\* The actual rendering method may be automatically changed
by the engine as a result of a fallback, or a user-specified command
line argument. To get the actual rendering method that is used at
runtime, use
`RenderingServer.get_current_rendering_method()<class_RenderingServer_method_get_current_rendering_method>`{.interpreted-text
role="ref"} instead of reading this project setting\'s value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/renderer/rendering_method.mobile}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/renderer/rendering_method.mobile** = `"mobile"`
`🔗<class_ProjectSettings_property_rendering/renderer/rendering_method.mobile>`{.interpreted-text
role="ref"}

Override for
`rendering/renderer/rendering_method<class_ProjectSettings_property_rendering/renderer/rendering_method>`{.interpreted-text
role="ref"} on mobile devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/renderer/rendering_method.web}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/renderer/rendering_method.web** = `"gl_compatibility"`
`🔗<class_ProjectSettings_property_rendering/renderer/rendering_method.web>`{.interpreted-text
role="ref"}

Override for
`rendering/renderer/rendering_method<class_ProjectSettings_property_rendering/renderer/rendering_method>`{.interpreted-text
role="ref"} on web.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/d3d12/agility_sdk_version}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/d3d12/agility_sdk_version** = `613`
`🔗<class_ProjectSettings_property_rendering/rendering_device/d3d12/agility_sdk_version>`{.interpreted-text
role="ref"}

Version code of the [Direct3D 12 Agility
SDK](https://devblogs.microsoft.com/directx/directx12agility/) to use
(`D3D12SDKVersion`). This must match the *minor* version that is
installed next to the editor binary and in the export templates
directory for the current editor version. For example, if you have
`1.613.3` installed, you need to input `613` here.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/d3d12/max_misc_descriptors_per_frame}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/d3d12/max_misc_descriptors_per_frame** =
`512`
`🔗<class_ProjectSettings_property_rendering/rendering_device/d3d12/max_misc_descriptors_per_frame>`{.interpreted-text
role="ref"}

The number of entries in the miscellaneous descriptors heap the Direct3D
12 rendering driver uses each frame, used for various operations like
clearing a texture.

Depending on the complexity of scenes, this value may be lowered or may
need to be raised.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/d3d12/max_resource_descriptors_per_frame}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/d3d12/max_resource_descriptors_per_frame**
= `16384`
`🔗<class_ProjectSettings_property_rendering/rendering_device/d3d12/max_resource_descriptors_per_frame>`{.interpreted-text
role="ref"}

The number of entries in the resource descriptors heap the Direct3D 12
rendering driver uses each frame, used for most rendering operations.

Depending on the complexity of scenes, this value may be lowered or may
need to be raised.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/d3d12/max_sampler_descriptors_per_frame}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/d3d12/max_sampler_descriptors_per_frame** =
`1024`
`🔗<class_ProjectSettings_property_rendering/rendering_device/d3d12/max_sampler_descriptors_per_frame>`{.interpreted-text
role="ref"}

The number of entries in the sampler descriptors heap the Direct3D 12
rendering driver uses each frame, used for most rendering operations.

Depending on the complexity of scenes, this value may be lowered or may
need to be raised.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/driver}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/rendering_device/driver** = `"vulkan"`
`🔗<class_ProjectSettings_property_rendering/rendering_device/driver>`{.interpreted-text
role="ref"}

Sets the driver to be used by the renderer when using a
RenderingDevice-based renderer like the Forward+ or Mobile renderers.
Editing this property has no effect in the default configuration, as
first-party platforms each have platform-specific overrides. Use those
overrides to configure the driver for each platform.

This can be overridden using the `--rendering-driver <driver>` command
line argument.

Supported values are:

- `metal`, Metal (supported on Apple Silicon Macs and iOS).
- `vulkan`, Vulkan (supported on all desktop and mobile platforms).
- `d3d12`, Direct3D 12 (supported on Windows).

\*\*Note:\*\* The availability of these options depends on whether the
engine was compiled with support for them (determined by SCons options
`vulkan`, `metal`, and `d3d12`).

\*\*Note:\*\* If a given platform has no registered drivers, it can fall
back to the Compatibility renderer (OpenGL 3) if
`rendering/rendering_device/fallback_to_opengl3<class_ProjectSettings_property_rendering/rendering_device/fallback_to_opengl3>`{.interpreted-text
role="ref"} is enabled. This fallback happens automatically for the Web
platform regardless of that property.

\*\*Note:\*\* The actual rendering driver may be automatically changed
by the engine as a result of a fallback, or a user-specified command
line argument. To get the actual rendering driver that is used at
runtime, use
`RenderingServer.get_current_rendering_driver_name()<class_RenderingServer_method_get_current_rendering_driver_name>`{.interpreted-text
role="ref"} instead of reading this project setting\'s value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/driver.android}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/rendering_device/driver.android** = `"vulkan"`
`🔗<class_ProjectSettings_property_rendering/rendering_device/driver.android>`{.interpreted-text
role="ref"}

Android override for
`rendering/rendering_device/driver<class_ProjectSettings_property_rendering/rendering_device/driver>`{.interpreted-text
role="ref"}.

Only one option is supported:

- `vulkan`, Vulkan from native drivers.

\*\*Note:\*\* If Vulkan was disabled at compile time, there is no
alternative RenderingDevice driver.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/driver.ios}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/rendering_device/driver.ios** = `"metal"`
`🔗<class_ProjectSettings_property_rendering/rendering_device/driver.ios>`{.interpreted-text
role="ref"}

iOS override for
`rendering/rendering_device/driver<class_ProjectSettings_property_rendering/rendering_device/driver>`{.interpreted-text
role="ref"}.

Two options are supported:

- `metal` (default), Metal from native drivers.
- `vulkan`, Vulkan over Metal via MoltenVK.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/driver.linuxbsd}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/rendering_device/driver.linuxbsd** = `"vulkan"`
`🔗<class_ProjectSettings_property_rendering/rendering_device/driver.linuxbsd>`{.interpreted-text
role="ref"}

LinuxBSD override for
`rendering/rendering_device/driver<class_ProjectSettings_property_rendering/rendering_device/driver>`{.interpreted-text
role="ref"}.

Only one option is supported:

- `vulkan`, Vulkan from native drivers.

\*\*Note:\*\* If Vulkan was disabled at compile time, there is no
alternative RenderingDevice driver.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/driver.macos}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/rendering_device/driver.macos** = `"metal"`
`🔗<class_ProjectSettings_property_rendering/rendering_device/driver.macos>`{.interpreted-text
role="ref"}

macOS override for
`rendering/rendering_device/driver<class_ProjectSettings_property_rendering/rendering_device/driver>`{.interpreted-text
role="ref"}.

Two options are supported:

- `metal` (default), Metal from native drivers, only supported on Apple
  Silicon Macs. On Intel Macs, it will automatically fall back to
  `vulkan` as Metal support is not implemented.
- `vulkan`, Vulkan over Metal via MoltenVK, supported on both Apple
  Silicon and Intel Macs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/driver.visionos}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/rendering_device/driver.visionos** = `"metal"`
`🔗<class_ProjectSettings_property_rendering/rendering_device/driver.visionos>`{.interpreted-text
role="ref"}

visionOS override for
`rendering/rendering_device/driver<class_ProjectSettings_property_rendering/rendering_device/driver>`{.interpreted-text
role="ref"}.

Only one option is supported:

- `metal` (default), Metal from native drivers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/driver.windows}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/rendering_device/driver.windows** = `"vulkan"`
`🔗<class_ProjectSettings_property_rendering/rendering_device/driver.windows>`{.interpreted-text
role="ref"}

Windows override for
`rendering/rendering_device/driver<class_ProjectSettings_property_rendering/rendering_device/driver>`{.interpreted-text
role="ref"}.

Two options are supported:

- `vulkan` (default), Vulkan from native drivers. If
  `rendering/rendering_device/fallback_to_vulkan<class_ProjectSettings_property_rendering/rendering_device/fallback_to_vulkan>`{.interpreted-text
  role="ref"} is enabled, this is used as a fallback if Direct3D 12 is
  not supported.
- `d3d12`, Direct3D 12 from native drivers. If
  `rendering/rendering_device/fallback_to_d3d12<class_ProjectSettings_property_rendering/rendering_device/fallback_to_d3d12>`{.interpreted-text
  role="ref"} is enabled, this is used as a fallback if Vulkan is not
  supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/fallback_to_d3d12}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/rendering_device/fallback_to_d3d12** = `true`
`🔗<class_ProjectSettings_property_rendering/rendering_device/fallback_to_d3d12>`{.interpreted-text
role="ref"}

If `true`, the forward renderer will fall back to Direct3D 12 if Vulkan
is not supported. The fallback is always attempted regardless of this
setting if Vulkan driver support was disabled at compile time.

\*\*Note:\*\* This setting is implemented only on Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/fallback_to_opengl3}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/rendering_device/fallback_to_opengl3** = `true`
`🔗<class_ProjectSettings_property_rendering/rendering_device/fallback_to_opengl3>`{.interpreted-text
role="ref"}

If `true`, the forward renderer will fall back to OpenGL 3 if Direct3D
12, Metal, and Vulkan are not supported.

\*\*Note:\*\* This setting is implemented on Windows, Android, macOS,
iOS, and Linux/X11.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/fallback_to_vulkan}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/rendering_device/fallback_to_vulkan** = `true`
`🔗<class_ProjectSettings_property_rendering/rendering_device/fallback_to_vulkan>`{.interpreted-text
role="ref"}

If `true`, the forward renderer will fall back to Vulkan if Direct3D 12
(on Windows) or Metal (on macOS x86_64) are not supported. The fallback
is always attempted regardless of this setting if Direct3D 12 (Windows)
or Metal (macOS) driver support was disabled at compile time.

\*\*Note:\*\* This setting is implemented on Windows and macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/pipeline_cache/enable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/rendering_device/pipeline_cache/enable** = `true`
`🔗<class_ProjectSettings_property_rendering/rendering_device/pipeline_cache/enable>`{.interpreted-text
role="ref"}

Enable the pipeline cache that is saved to disk if the graphics API
supports it.

\*\*Note:\*\* This property is unable to control the pipeline caching
the GPU driver itself does. Only turn this off along with deleting the
contents of the driver\'s cache if you wish to simulate the experience a
user will get when starting the game for the first time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/pipeline_cache/save_chunk_size_mb}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/rendering_device/pipeline_cache/save_chunk_size_mb** = `3.0`
`🔗<class_ProjectSettings_property_rendering/rendering_device/pipeline_cache/save_chunk_size_mb>`{.interpreted-text
role="ref"}

Determines at which interval pipeline cache is saved to disk. The lower
the value, the more often it is saved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/staging_buffer/block_size_kb}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/staging_buffer/block_size_kb** = `256`
`🔗<class_ProjectSettings_property_rendering/rendering_device/staging_buffer/block_size_kb>`{.interpreted-text
role="ref"}

The size of a block allocated in the staging buffers. Staging buffers
are the intermediate resources the engine uses to upload or download
data to the GPU. This setting determines the max amount of data that can
be transferred in a copy operation. Increasing this will result in
faster data transfers at the cost of extra memory.

\*\*Note:\*\* This property is only read when the project starts. There
is currently no way to change this value at run-time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/staging_buffer/max_size_mb}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/staging_buffer/max_size_mb** = `128`
`🔗<class_ProjectSettings_property_rendering/rendering_device/staging_buffer/max_size_mb>`{.interpreted-text
role="ref"}

The maximum amount of memory allowed to be used by staging buffers. If
the amount of data being uploaded or downloaded exceeds this amount, the
GPU will stall and wait for previous frames to finish.

\*\*Note:\*\* This property is only read when the project starts. There
is currently no way to change this value at run-time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/staging_buffer/texture_download_region_size_px}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/staging_buffer/texture_download_region_size_px**
= `64`
`🔗<class_ProjectSettings_property_rendering/rendering_device/staging_buffer/texture_download_region_size_px>`{.interpreted-text
role="ref"}

The region size in pixels used to download texture data from the GPU
when using methods like
`RenderingDevice.texture_get_data_async()<class_RenderingDevice_method_texture_get_data_async>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property\'s upper limit is controlled by
`rendering/rendering_device/staging_buffer/block_size_kb<class_ProjectSettings_property_rendering/rendering_device/staging_buffer/block_size_kb>`{.interpreted-text
role="ref"} and whether it\'s possible to allocate a single block of
texture data with this region size in the format that is requested.

\*\*Note:\*\* This property is only read when the project starts. There
is currently no way to change this value at run-time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/staging_buffer/texture_upload_region_size_px}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/staging_buffer/texture_upload_region_size_px**
= `64`
`🔗<class_ProjectSettings_property_rendering/rendering_device/staging_buffer/texture_upload_region_size_px>`{.interpreted-text
role="ref"}

The region size in pixels used to upload texture data from the GPU when
using methods like
`RenderingDevice.texture_update()<class_RenderingDevice_method_texture_update>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This property\'s upper limit is controlled by
`rendering/rendering_device/staging_buffer/block_size_kb<class_ProjectSettings_property_rendering/rendering_device/staging_buffer/block_size_kb>`{.interpreted-text
role="ref"} and whether it\'s possible to allocate a single block of
texture data with this region size in the format that is requested.

\*\*Note:\*\* This property is only read when the project starts. There
is currently no way to change this value at run-time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/vsync/frame_queue_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/vsync/frame_queue_size** = `2`
`🔗<class_ProjectSettings_property_rendering/rendering_device/vsync/frame_queue_size>`{.interpreted-text
role="ref"}

The number of frames to track on the CPU side before stalling to wait
for the GPU.

Try the [V-Sync
Simulator](https://darksylinc.github.io/vsync_simulator/), an
interactive interface that simulates presentation to better understand
how it is affected by different variables under various conditions.

\*\*Note:\*\* This property is only read when the project starts. There
is currently no way to change this value at run-time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/vsync/swapchain_image_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/vsync/swapchain_image_count** = `3`
`🔗<class_ProjectSettings_property_rendering/rendering_device/vsync/swapchain_image_count>`{.interpreted-text
role="ref"}

The number of images the swapchain will consist of (back buffers + front
buffer).

`2` corresponds to double-buffering and `3` to triple-buffering.

Double-buffering may give you the lowest lag/latency but if V-Sync is on
and the system can\'t render at 60 fps, the framerate will go down in
multiples of it (e.g. 30 fps, 15, 7.5, etc.). Triple buffering gives you
higher framerate (specially if the system can\'t reach a constant 60
fps) at the cost of up to 1 frame of latency, with
`DisplayServer.VSYNC_ENABLED<class_DisplayServer_constant_VSYNC_ENABLED>`{.interpreted-text
role="ref"} (FIFO).

Use double-buffering with
`DisplayServer.VSYNC_ENABLED<class_DisplayServer_constant_VSYNC_ENABLED>`{.interpreted-text
role="ref"}. Triple-buffering is a must if you plan on using
`DisplayServer.VSYNC_MAILBOX<class_DisplayServer_constant_VSYNC_MAILBOX>`{.interpreted-text
role="ref"} mode.

Try the [V-Sync
Simulator](https://darksylinc.github.io/vsync_simulator/), an
interactive interface that simulates presentation to better understand
how it is affected by different variables under various conditions.

\*\*Note:\*\* This property is only read when the project starts. There
is currently no way to change this value at run-time.

\*\*Note:\*\* Some platforms may restrict the actual value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/rendering_device/vulkan/max_descriptors_per_pool}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/rendering_device/vulkan/max_descriptors_per_pool** = `64`
`🔗<class_ProjectSettings_property_rendering/rendering_device/vulkan/max_descriptors_per_pool>`{.interpreted-text
role="ref"}

The number of descriptors per pool. Godot\'s Vulkan backend uses linear
pools for descriptors that will be created and destroyed within a single
frame. Instead of destroying every single descriptor every frame, they
all can be destroyed at once by resetting the pool they belong to.

A larger number is more efficient up to a limit, after that it will only
waste RAM (maximum efficiency is achieved when there is no more than 1
pool per frame). A small number could end up with one pool per
descriptor, which negatively impacts performance.

\*\*Note:\*\* Changing this property requires a restart to take effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/scaling_3d/fsr_sharpness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/scaling_3d/fsr_sharpness** = `0.2`
`🔗<class_ProjectSettings_property_rendering/scaling_3d/fsr_sharpness>`{.interpreted-text
role="ref"}

Determines how sharp the upscaled image will be when using the FSR
upscaling mode. Sharpness halves with every whole number. Values go from
0.0 (sharpest) to 2.0. Values above 2.0 won\'t make a visible
difference.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/scaling_3d/mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/scaling_3d/mode** = `0`
`🔗<class_ProjectSettings_property_rendering/scaling_3d/mode>`{.interpreted-text
role="ref"}

Sets the scaling 3D mode. Bilinear scaling renders at different
resolution to either undersample or supersample the viewport. FidelityFX
Super Resolution 1.0, abbreviated to FSR, is an upscaling technology
that produces high quality images at fast framerates by using a
spatially-aware upscaling algorithm. FSR is slightly more expensive than
bilinear, but it produces significantly higher image quality. On
particularly low-end GPUs, the added cost of FSR may not be worth it
(compared to using bilinear scaling with a slightly higher resolution
scale to match performance).

\*\*Note:\*\* FSR is only effective when using the Forward+ rendering
method, not Mobile or Compatibility. If using an incompatible rendering
method, FSR will fall back to bilinear scaling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/scaling_3d/mode.ios}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/scaling_3d/mode.ios**
`🔗<class_ProjectSettings_property_rendering/scaling_3d/mode.ios>`{.interpreted-text
role="ref"}

iOS override for
`rendering/scaling_3d/mode<class_ProjectSettings_property_rendering/scaling_3d/mode>`{.interpreted-text
role="ref"}. This allows selecting the MetalFX spatial and MetalFX
temporal scaling modes, which are exclusive to platforms where the Metal
rendering driver is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/scaling_3d/mode.macos}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/scaling_3d/mode.macos**
`🔗<class_ProjectSettings_property_rendering/scaling_3d/mode.macos>`{.interpreted-text
role="ref"}

macOS override for
`rendering/scaling_3d/mode<class_ProjectSettings_property_rendering/scaling_3d/mode>`{.interpreted-text
role="ref"}. This allows selecting the MetalFX spatial and MetalFX
temporal scaling modes, which are exclusive to platforms where the Metal
rendering driver is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/scaling_3d/scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/scaling_3d/scale** = `1.0`
`🔗<class_ProjectSettings_property_rendering/scaling_3d/scale>`{.interpreted-text
role="ref"}

Scales the 3D render buffer based on the viewport size uses an image
filter specified in
`rendering/scaling_3d/mode<class_ProjectSettings_property_rendering/scaling_3d/mode>`{.interpreted-text
role="ref"} to scale the output image to the full viewport size. Values
lower than `1.0` can be used to speed up 3D rendering at the cost of
quality (undersampling). Values greater than `1.0` are only valid for
bilinear mode and can be used to improve 3D rendering quality at a high
performance cost (supersampling). See also
`rendering/anti_aliasing/quality/msaa_3d<class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_3d>`{.interpreted-text
role="ref"} for multi-sample antialiasing, which is significantly
cheaper but only smooths the edges of polygons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/shader_compiler/shader_cache/compress}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/shader_compiler/shader_cache/compress** = `true`
`🔗<class_ProjectSettings_property_rendering/shader_compiler/shader_cache/compress>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/shader_compiler/shader_cache/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/shader_compiler/shader_cache/enabled** = `true`
`🔗<class_ProjectSettings_property_rendering/shader_compiler/shader_cache/enabled>`{.interpreted-text
role="ref"}

Enable the shader cache, which stores compiled shaders to disk to
prevent stuttering from shader compilation the next time the shader is
needed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/shader_compiler/shader_cache/strip_debug}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/shader_compiler/shader_cache/strip_debug** = `false`
`🔗<class_ProjectSettings_property_rendering/shader_compiler/shader_cache/strip_debug>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/shader_compiler/shader_cache/strip_debug.release}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/shader_compiler/shader_cache/strip_debug.release** = `true`
`🔗<class_ProjectSettings_property_rendering/shader_compiler/shader_cache/strip_debug.release>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/shader_compiler/shader_cache/use_zstd_compression}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/shader_compiler/shader_cache/use_zstd_compression** = `true`
`🔗<class_ProjectSettings_property_rendering/shader_compiler/shader_cache/use_zstd_compression>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/shading/overrides/force_lambert_over_burley}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/shading/overrides/force_lambert_over_burley** = `false`
`🔗<class_ProjectSettings_property_rendering/shading/overrides/force_lambert_over_burley>`{.interpreted-text
role="ref"}

If `true`, uses faster but lower-quality Lambert material lighting model
instead of Burley.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/shading/overrides/force_lambert_over_burley.mobile}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/shading/overrides/force_lambert_over_burley.mobile** =
`true`
`🔗<class_ProjectSettings_property_rendering/shading/overrides/force_lambert_over_burley.mobile>`{.interpreted-text
role="ref"}

Lower-end override for
`rendering/shading/overrides/force_lambert_over_burley<class_ProjectSettings_property_rendering/shading/overrides/force_lambert_over_burley>`{.interpreted-text
role="ref"} on mobile devices, due to performance concerns or driver
support.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/shading/overrides/force_vertex_shading}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/shading/overrides/force_vertex_shading** = `false`
`🔗<class_ProjectSettings_property_rendering/shading/overrides/force_vertex_shading>`{.interpreted-text
role="ref"}

If `true`, forces vertex shading for all rendering. This can increase
performance a lot, but also reduces quality immensely. Can be used to
optimize performance on low-end mobile devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/basis_universal/rdo_dict_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/textures/basis_universal/rdo_dict_size** = `1024`
`🔗<class_ProjectSettings_property_rendering/textures/basis_universal/rdo_dict_size>`{.interpreted-text
role="ref"}

The dictionary size for Rate-Distortion Optimization (RDO) when
importing textures as Basis Universal and when RDO is enabled, ranging
from `64` to `65536`. Higher values reduce the file sizes further, but
make encoding times significantly longer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/basis_universal/zstd_supercompression}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/textures/basis_universal/zstd_supercompression** = `true`
`🔗<class_ProjectSettings_property_rendering/textures/basis_universal/zstd_supercompression>`{.interpreted-text
role="ref"}

If `true`, enables Zstandard supercompression to reduce file size when
importing textures as Basis Universal.

\*\*Note:\*\* Basis Universal textures need to be compressed to gain the
benefit of smaller file sizes, otherwise they are as large as
VRAM-compressed textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/basis_universal/zstd_supercompression_level}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/textures/basis_universal/zstd_supercompression_level** = `6`
`🔗<class_ProjectSettings_property_rendering/textures/basis_universal/zstd_supercompression_level>`{.interpreted-text
role="ref"}

Specify the compression level for Basis Universal Zstandard
supercompression, ranging from `1` to `22`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/canvas_textures/default_texture_filter}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/textures/canvas_textures/default_texture_filter** = `1`
`🔗<class_ProjectSettings_property_rendering/textures/canvas_textures/default_texture_filter>`{.interpreted-text
role="ref"}

The default texture filtering mode to use for
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}s built-in
texture. In shaders, this texture is accessed as `TEXTURE`.

\*\*Note:\*\* For pixel art aesthetics, see also
`rendering/2d/snap/snap_2d_vertices_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_vertices_to_pixel>`{.interpreted-text
role="ref"} and
`rendering/2d/snap/snap_2d_transforms_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_transforms_to_pixel>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/canvas_textures/default_texture_repeat}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/textures/canvas_textures/default_texture_repeat** = `0`
`🔗<class_ProjectSettings_property_rendering/textures/canvas_textures/default_texture_repeat>`{.interpreted-text
role="ref"}

The default texture repeating mode to use for
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}s built-in
texture. In shaders, this texture is accessed as `TEXTURE`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/decals/filter}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/textures/decals/filter** = `3`
`🔗<class_ProjectSettings_property_rendering/textures/decals/filter>`{.interpreted-text
role="ref"}

The filtering quality to use for `Decal<class_Decal>`{.interpreted-text
role="ref"} nodes. When using one of the anisotropic filtering modes,
the anisotropic filtering level is controlled by
`rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/textures/default_filters/anisotropic_filtering_level** = `2`
`🔗<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}

Sets the maximum number of samples to take when using anisotropic
filtering on textures (as a power of two). A higher sample count will
result in sharper textures at oblique angles, but is more expensive to
compute. A value of `0` forcibly disables anisotropic filtering, even on
materials where it is enabled.

The anisotropic filtering level also affects decals and light projectors
if they are configured to use anisotropic filtering. See
`rendering/textures/decals/filter<class_ProjectSettings_property_rendering/textures/decals/filter>`{.interpreted-text
role="ref"} and
`rendering/textures/light_projectors/filter<class_ProjectSettings_property_rendering/textures/light_projectors/filter>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In 3D, for this setting to have an effect, set
`BaseMaterial3D.texture_filter<class_BaseMaterial3D_property_texture_filter>`{.interpreted-text
role="ref"} to
`BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC<class_BaseMaterial3D_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} or
`BaseMaterial3D.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC<class_BaseMaterial3D_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} on materials.

\*\*Note:\*\* In 2D, for this setting to have an effect, set
`CanvasItem.texture_filter<class_CanvasItem_property_texture_filter>`{.interpreted-text
role="ref"} to
`CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC<class_CanvasItem_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} or
`CanvasItem.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC<class_CanvasItem_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} on the `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} node displaying the texture (or in
`CanvasTexture<class_CanvasTexture>`{.interpreted-text role="ref"}).
However, anisotropic filtering is rarely useful in 2D, so only enable it
for textures in 2D if it makes a meaningful visual difference.

\*\*Note:\*\* This property is only read when the project starts. To
change the anisotropic filtering level at runtime, set
`Viewport.anisotropic_filtering_level<class_Viewport_property_anisotropic_filtering_level>`{.interpreted-text
role="ref"} on the root `Viewport<class_Viewport>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/default_filters/texture_mipmap_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/textures/default_filters/texture_mipmap_bias** = `0.0`
`🔗<class_ProjectSettings_property_rendering/textures/default_filters/texture_mipmap_bias>`{.interpreted-text
role="ref"}

Affects the final texture sharpness by reading from a lower or higher
mipmap (also called \"texture LOD bias\"). Negative values make
mipmapped textures sharper but grainier when viewed at a distance, while
positive values make mipmapped textures blurrier (even when up close).

Enabling temporal antialiasing
(`rendering/anti_aliasing/quality/use_taa<class_ProjectSettings_property_rendering/anti_aliasing/quality/use_taa>`{.interpreted-text
role="ref"}) will automatically apply a `-0.5` offset to this value,
while enabling FXAA
(`rendering/anti_aliasing/quality/screen_space_aa<class_ProjectSettings_property_rendering/anti_aliasing/quality/screen_space_aa>`{.interpreted-text
role="ref"}) will automatically apply a `-0.25` offset to this value. If
both TAA and FXAA are enabled at the same time, an offset of `-0.75` is
applied to this value.

\*\*Note:\*\* If
`rendering/scaling_3d/scale<class_ProjectSettings_property_rendering/scaling_3d/scale>`{.interpreted-text
role="ref"} is lower than `1.0` (exclusive),
`rendering/textures/default_filters/texture_mipmap_bias<class_ProjectSettings_property_rendering/textures/default_filters/texture_mipmap_bias>`{.interpreted-text
role="ref"} is used to adjust the automatic mipmap bias which is
calculated internally based on the scale factor. The formula for this is
`log2(scaling_3d_scale) + mipmap_bias`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/textures/default_filters/use_nearest_mipmap_filter** =
`false`
`🔗<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"}

If `true`, uses nearest-neighbor mipmap filtering when using mipmaps
(also called \"bilinear filtering\"), which will result in visible seams
appearing between mipmap stages. This may increase performance in mobile
as less memory bandwidth is used. If `false`, linear mipmap filtering
(also called \"trilinear filtering\") is used.

\*\*Note:\*\* This property is only read when the project starts. There
is currently no way to change this setting at run-time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/light_projectors/filter}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/textures/light_projectors/filter** = `3`
`🔗<class_ProjectSettings_property_rendering/textures/light_projectors/filter>`{.interpreted-text
role="ref"}

The filtering quality to use for
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}
projectors. When using one of the anisotropic filtering modes, the
anisotropic filtering level is controlled by
`rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/lossless_compression/force_png}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/textures/lossless_compression/force_png** = `false`
`🔗<class_ProjectSettings_property_rendering/textures/lossless_compression/force_png>`{.interpreted-text
role="ref"}

If `true`, the texture importer will import lossless textures using the
PNG format. Otherwise, it will default to using WebP.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/vram_compression/cache_gpu_compressor}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/textures/vram_compression/cache_gpu_compressor** = `true`
`🔗<class_ProjectSettings_property_rendering/textures/vram_compression/cache_gpu_compressor>`{.interpreted-text
role="ref"}

If `true`, the GPU texture compressor will cache the local
RenderingDevice and its resources (shaders and pipelines), allowing for
faster subsequent imports at a memory cost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/vram_compression/compress_with_gpu}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/textures/vram_compression/compress_with_gpu** = `true`
`🔗<class_ProjectSettings_property_rendering/textures/vram_compression/compress_with_gpu>`{.interpreted-text
role="ref"}

If `true`, the texture importer will utilize the GPU for compressing
textures, improving the import time of large images.

\*\*Note:\*\* This only functions on a device which supports either
Vulkan, Direct3D 12, or Metal as a rendering driver.

\*\*Note:\*\* Currently this only affects certain compressed formats
(BC1, BC3, BC4, BC5, and BC6), all of which are exclusive to desktop
platforms and consoles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/vram_compression/import_etc2_astc}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/textures/vram_compression/import_etc2_astc** = `false`
`🔗<class_ProjectSettings_property_rendering/textures/vram_compression/import_etc2_astc>`{.interpreted-text
role="ref"}

If `true`, the texture importer will import VRAM-compressed textures
using the Ericsson Texture Compression 2 algorithm for lower quality
textures and normal maps and Adaptable Scalable Texture Compression
algorithm for high quality textures (in 4×4 block size).

\*\*Note:\*\* This setting is an override. The texture importer will
always import the format the host platform needs, even if this is set to
`false`.

\*\*Note:\*\* Changing this setting does *not* impact textures that were
already imported before. To make this setting apply to textures that
were already imported, exit the editor, remove the `.godot/imported/`
folder located inside the project folder then restart the editor (see
`application/config/use_hidden_project_data_directory<class_ProjectSettings_property_application/config/use_hidden_project_data_directory>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/vram_compression/import_s3tc_bptc}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/textures/vram_compression/import_s3tc_bptc** = `false`
`🔗<class_ProjectSettings_property_rendering/textures/vram_compression/import_s3tc_bptc>`{.interpreted-text
role="ref"}

If `true`, the texture importer will import VRAM-compressed textures
using the S3 Texture Compression algorithm (DXT1-5) for lower quality
textures and the BPTC algorithm (BC6H and BC7) for high quality
textures. This algorithm is only supported on PC desktop platforms and
consoles.

\*\*Note:\*\* This setting is an override. The texture importer will
always import the format the host platform needs, even if this is set to
`false`.

\*\*Note:\*\* Changing this setting does *not* impact textures that were
already imported before. To make this setting apply to textures that
were already imported, exit the editor, remove the `.godot/imported/`
folder located inside the project folder then restart the editor (see
`application/config/use_hidden_project_data_directory<class_ProjectSettings_property_application/config/use_hidden_project_data_directory>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/webp_compression/compression_method}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rendering/textures/webp_compression/compression_method** = `2`
`🔗<class_ProjectSettings_property_rendering/textures/webp_compression/compression_method>`{.interpreted-text
role="ref"}

The default compression method for WebP. Affects both lossy and lossless
WebP. A higher value results in smaller files at the cost of compression
speed. Decompression speed is mostly unaffected by the compression
method. Supported values are 0 to 6. Note that compression methods above
4 are very slow and offer very little savings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/textures/webp_compression/lossless_compression_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rendering/textures/webp_compression/lossless_compression_factor** =
`25`
`🔗<class_ProjectSettings_property_rendering/textures/webp_compression/lossless_compression_factor>`{.interpreted-text
role="ref"}

The default compression factor for lossless WebP. Decompression speed is
mostly unaffected by the compression factor. Supported values are 0 to
100.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/viewport/hdr_2d}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/viewport/hdr_2d** = `false`
`🔗<class_ProjectSettings_property_rendering/viewport/hdr_2d>`{.interpreted-text
role="ref"}

If `true`, enables
`Viewport.use_hdr_2d<class_Viewport_property_use_hdr_2d>`{.interpreted-text
role="ref"} on the root viewport. 2D rendering will use a high dynamic
range (HDR) format framebuffer matching the bit depth of the 3D
framebuffer. When using the Forward+ renderer this will be an `RGBA16`
framebuffer, while when using the Mobile renderer it will be an
`RGB10_A2` framebuffer. Additionally, 2D rendering will take place in
linear color space and will be converted to sRGB space immediately
before blitting to the screen. Practically speaking, this means that the
end result of the Viewport will not be clamped into the `0-1` range and
can be used in 3D rendering without color space adjustments. This allows
2D rendering to take advantage of effects requiring high dynamic range
(e.g. 2D glow) as well as substantially improves the appearance of
effects requiring highly detailed gradients.

\*\*Note:\*\* This setting will have no effect when using the
Compatibility renderer, which always renders in low dynamic range for
performance reasons.

\*\*Note:\*\* This property is only read when the project starts. To
toggle HDR 2D at runtime, set
`Viewport.use_hdr_2d<class_Viewport_property_use_hdr_2d>`{.interpreted-text
role="ref"} on the root `Viewport<class_Viewport>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/viewport/transparent_background}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**rendering/viewport/transparent_background** = `false`
`🔗<class_ProjectSettings_property_rendering/viewport/transparent_background>`{.interpreted-text
role="ref"}

If `true`, enables
`Viewport.transparent_bg<class_Viewport_property_transparent_bg>`{.interpreted-text
role="ref"} on the root viewport. This allows per-pixel transparency to
be effective after also enabling
`display/window/size/transparent<class_ProjectSettings_property_display/window/size/transparent>`{.interpreted-text
role="ref"} and
`display/window/per_pixel_transparency/allowed<class_ProjectSettings_property_display/window/per_pixel_transparency/allowed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/vrs/mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rendering/vrs/mode** =
`0`
`🔗<class_ProjectSettings_property_rendering/vrs/mode>`{.interpreted-text
role="ref"}

Set the default Variable Rate Shading (VRS) mode for the main viewport.
See
`Viewport.vrs_mode<class_Viewport_property_vrs_mode>`{.interpreted-text
role="ref"} to change this at runtime, and
`VRSMode<enum_Viewport_VRSMode>`{.interpreted-text role="ref"} for
possible values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_rendering/vrs/texture}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**rendering/vrs/texture** = `""`
`🔗<class_ProjectSettings_property_rendering/vrs/texture>`{.interpreted-text
role="ref"}

If
`rendering/vrs/mode<class_ProjectSettings_property_rendering/vrs/mode>`{.interpreted-text
role="ref"} is set to **Texture**, this is the path to default texture
loaded as the VRS image.

The texture *must* use a lossless compression format so that colors can
be matched precisely. The following VRS densities are mapped to various
colors, with brighter colors representing a lower level of shading
precision:

``` text
- 1×1 = rgb(0, 0, 0)     - #000000
- 1×2 = rgb(0, 85, 0)    - #005500
- 2×1 = rgb(85, 0, 0)    - #550000
- 2×2 = rgb(85, 85, 0)   - #555500
- 2×4 = rgb(85, 170, 0)  - #55aa00
- 4×2 = rgb(170, 85, 0)  - #aa5500
- 4×4 = rgb(170, 170, 0) - #aaaa00
- 4×8 = rgb(170, 255, 0) - #aaff00 - Not supported on most hardware
- 8×4 = rgb(255, 170, 0) - #ffaa00 - Not supported on most hardware
- 8×8 = rgb(255, 255, 0) - #ffff00 - Not supported on most hardware
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_threading/worker_pool/low_priority_thread_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**threading/worker_pool/low_priority_thread_ratio** = `0.3`
`🔗<class_ProjectSettings_property_threading/worker_pool/low_priority_thread_ratio>`{.interpreted-text
role="ref"}

The ratio of
`WorkerThreadPool<class_WorkerThreadPool>`{.interpreted-text
role="ref"}\'s threads that will be reserved for low-priority tasks. For
example, if 10 threads are available and this value is set to `0.3`, 3
of the worker threads will be reserved for low-priority tasks. The
actual value won\'t exceed the number of CPU cores minus one, and if
possible, at least one worker thread will be dedicated to low-priority
tasks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_threading/worker_pool/max_threads}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**threading/worker_pool/max_threads** = `-1`
`🔗<class_ProjectSettings_property_threading/worker_pool/max_threads>`{.interpreted-text
role="ref"}

Maximum number of threads to be used by
`WorkerThreadPool<class_WorkerThreadPool>`{.interpreted-text
role="ref"}. Value of `-1` means `1` on Web, or a number of *logical*
CPU cores available on other platforms (see
`OS.get_processor_count()<class_OS_method_get_processor_count>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/binding_modifiers/analog_threshold}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/binding_modifiers/analog_threshold** = `false`
`🔗<class_ProjectSettings_property_xr/openxr/binding_modifiers/analog_threshold>`{.interpreted-text
role="ref"}

If `true`, enables the analog threshold binding modifier if supported by
the XR runtime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/binding_modifiers/dpad_binding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/binding_modifiers/dpad_binding** = `false`
`🔗<class_ProjectSettings_property_xr/openxr/binding_modifiers/dpad_binding>`{.interpreted-text
role="ref"}

If `true`, enables the D-pad binding modifier if supported by the XR
runtime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/default_action_map}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**xr/openxr/default_action_map** = `"res://openxr_action_map.tres"`
`🔗<class_ProjectSettings_property_xr/openxr/default_action_map>`{.interpreted-text
role="ref"}

Action map configuration to load by default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **xr/openxr/enabled** =
`false`
`🔗<class_ProjectSettings_property_xr/openxr/enabled>`{.interpreted-text
role="ref"}

If `true`, Godot will setup and initialize OpenXR on startup.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/environment_blend_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**xr/openxr/environment_blend_mode** = `"0"`
`🔗<class_ProjectSettings_property_xr/openxr/environment_blend_mode>`{.interpreted-text
role="ref"}

Specify how OpenXR should blend in the environment. This is specific to
certain AR and passthrough devices where camera images are blended in by
the XR compositor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/extensions/debug_message_types}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**xr/openxr/extensions/debug_message_types** = `"15"`
`🔗<class_ProjectSettings_property_xr/openxr/extensions/debug_message_types>`{.interpreted-text
role="ref"}

Specifies the message types for which we request debug messages.
Requires
`xr/openxr/extensions/debug_utils<class_ProjectSettings_property_xr/openxr/extensions/debug_utils>`{.interpreted-text
role="ref"} to be set and the extension to be supported by the XR
runtime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/extensions/debug_utils}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**xr/openxr/extensions/debug_utils** = `"0"`
`🔗<class_ProjectSettings_property_xr/openxr/extensions/debug_utils>`{.interpreted-text
role="ref"}

Enables debug utilities on XR runtimes that supports the debug utils
extension. Sets the maximum severity being reported (0 = disabled, 1 =
error, 2 = warning, 3 = info, 4 = verbose).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/extensions/eye_gaze_interaction}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/extensions/eye_gaze_interaction** = `false`
`🔗<class_ProjectSettings_property_xr/openxr/extensions/eye_gaze_interaction>`{.interpreted-text
role="ref"}

Specify whether to enable eye tracking for this project. Depending on
the platform, additional export configuration may be needed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/extensions/hand_interaction_profile}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/extensions/hand_interaction_profile** = `false`
`🔗<class_ProjectSettings_property_xr/openxr/extensions/hand_interaction_profile>`{.interpreted-text
role="ref"}

If `true` the hand interaction profile extension will be activated if
supported by the platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/extensions/hand_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/extensions/hand_tracking** = `false`
`🔗<class_ProjectSettings_property_xr/openxr/extensions/hand_tracking>`{.interpreted-text
role="ref"}

If `true`, the hand tracking extension is enabled if available.

\*\*Note:\*\* By default hand tracking will only work for data sources
chosen by the XR runtime. For SteamVR this is the controller inferred
data source, for most other runtimes this is the unobstructed data
source. There is no way to query this. If a runtime supports the OpenXR
data source extension you can use the
`xr/openxr/extensions/hand_tracking_controller_data_source<class_ProjectSettings_property_xr/openxr/extensions/hand_tracking_controller_data_source>`{.interpreted-text
role="ref"} and/or
`xr/openxr/extensions/hand_tracking_unobstructed_data_source<class_ProjectSettings_property_xr/openxr/extensions/hand_tracking_unobstructed_data_source>`{.interpreted-text
role="ref"} to indicate you wish to enable these data sources. If
neither is selected the data source extension is not enabled and the XR
runtimes default behavior persists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/extensions/hand_tracking_controller_data_source}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/extensions/hand_tracking_controller_data_source** = `false`
`🔗<class_ProjectSettings_property_xr/openxr/extensions/hand_tracking_controller_data_source>`{.interpreted-text
role="ref"}

If `true`, support for the controller inferred data source is requested.
If supported, you will receive hand tracking data even if the user has a
controller in hand, with finger positions automatically inferred from
controller input and/or sensors.

\*\*Note:\*\* This requires the OpenXR data source extension and
controller inferred handtracking to be supported by the XR runtime. If
not supported this setting will be ignored.
`xr/openxr/extensions/hand_tracking<class_ProjectSettings_property_xr/openxr/extensions/hand_tracking>`{.interpreted-text
role="ref"} must be enabled for this setting to be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/extensions/hand_tracking_unobstructed_data_source}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/extensions/hand_tracking_unobstructed_data_source** =
`false`
`🔗<class_ProjectSettings_property_xr/openxr/extensions/hand_tracking_unobstructed_data_source>`{.interpreted-text
role="ref"}

If `true`, support for the unobstructed data source is requested. If
supported, you will receive hand tracking data based on the actual
finger positions of the user often determined by optical tracking.

\*\*Note:\*\* This requires the OpenXR data source extension and
unobstructed handtracking to be supported by the XR runtime. If not
supported this setting will be ignored.
`xr/openxr/extensions/hand_tracking<class_ProjectSettings_property_xr/openxr/extensions/hand_tracking>`{.interpreted-text
role="ref"} must be enabled for this setting to be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/extensions/render_model}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/extensions/render_model** = `false`
`🔗<class_ProjectSettings_property_xr/openxr/extensions/render_model>`{.interpreted-text
role="ref"}

If `true` we enable the render model extension if available.

\*\*Note:\*\* This relates to the core OpenXR render model extension and
has no relation to any vendor render model extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/form_factor}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **xr/openxr/form_factor**
= `"0"`
`🔗<class_ProjectSettings_property_xr/openxr/form_factor>`{.interpreted-text
role="ref"}

Specify whether OpenXR should be configured for an HMD or a hand held
device.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/foveation_dynamic}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/foveation_dynamic** = `false`
`🔗<class_ProjectSettings_property_xr/openxr/foveation_dynamic>`{.interpreted-text
role="ref"}

If `true` and foveation is supported, will automatically adjust
foveation level based on framerate up to the level set on
`xr/openxr/foveation_level<class_ProjectSettings_property_xr/openxr/foveation_level>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/foveation_level}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**xr/openxr/foveation_level** = `"0"`
`🔗<class_ProjectSettings_property_xr/openxr/foveation_level>`{.interpreted-text
role="ref"}

Applied foveation level if supported: 0 = off, 1 = low, 2 = medium, 3 =
high.

\*\*Note:\*\* On platforms other than Android, if
`rendering/anti_aliasing/quality/msaa_3d<class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_3d>`{.interpreted-text
role="ref"} is enabled, this feature will be disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/reference_space}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**xr/openxr/reference_space** = `"1"`
`🔗<class_ProjectSettings_property_xr/openxr/reference_space>`{.interpreted-text
role="ref"}

Specify the default reference space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/startup_alert}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/startup_alert** = `true`
`🔗<class_ProjectSettings_property_xr/openxr/startup_alert>`{.interpreted-text
role="ref"}

If `true`, Godot will display an alert modal when OpenXR initialization
fails on startup.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/submit_depth_buffer}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**xr/openxr/submit_depth_buffer** = `false`
`🔗<class_ProjectSettings_property_xr/openxr/submit_depth_buffer>`{.interpreted-text
role="ref"}

If `true`, OpenXR will manage the depth buffer and use the depth buffer
for advanced reprojection provided this is supported by the XR runtime.
Note that some rendering features in Godot can\'t be used with this
feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/openxr/view_configuration}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**xr/openxr/view_configuration** = `"1"`
`🔗<class_ProjectSettings_property_xr/openxr/view_configuration>`{.interpreted-text
role="ref"}

Specify the view configuration with which to configure OpenXR setting up
either Mono or Stereo rendering.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_property_xr/shaders/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **xr/shaders/enabled**
= `false`
`🔗<class_ProjectSettings_property_xr/shaders/enabled>`{.interpreted-text
role="ref"}

If `true`, Godot will compile shaders required for XR.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ProjectSettings_method_add_property_info}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_property_info**(hint:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_ProjectSettings_method_add_property_info>`{.interpreted-text
role="ref"}

Adds a custom property info to a property. The dictionary must contain:

- `"name"`: `String<class_String>`{.interpreted-text role="ref"} (the
  property\'s name)
- `"type"`: `int<class_int>`{.interpreted-text role="ref"} (see
  `Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
  role="ref"})
- optionally `"hint"`: `int<class_int>`{.interpreted-text role="ref"}
  (see `PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
  role="ref"}) and `"hint_string"`:
  `String<class_String>`{.interpreted-text role="ref"}

::::: tabs
::: code-tab
gdscript

ProjectSettings.set(\"category/property_name\", 0)

var property_info = {

:   \"name\": \"category/property_name\", \"type\": TYPE_INT, \"hint\":
    PROPERTY_HINT_ENUM, \"hint_string\": \"one,two,three\"

}

ProjectSettings.add_property_info(property_info)
:::

::: code-tab
csharp

ProjectSettings.Singleton.Set(\"category/property_name\", 0);

var propertyInfo = new Godot.Collections.Dictionary { { \"name\",
\"category/propertyName\" }, { \"type\", (int)Variant.Type.Int }, {
\"hint\", (int)PropertyHint.Enum }, { \"hint_string\", \"one,two,three\"
}, };

ProjectSettings.AddPropertyInfo(propertyInfo);
:::
:::::

\*\*Note:\*\* Setting `"usage"` for the property is not supported. Use
`set_as_basic()<class_ProjectSettings_method_set_as_basic>`{.interpreted-text
role="ref"},
`set_restart_if_changed()<class_ProjectSettings_method_set_restart_if_changed>`{.interpreted-text
role="ref"}, and
`set_as_internal()<class_ProjectSettings_method_set_as_internal>`{.interpreted-text
role="ref"} to modify usage flags.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**(name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ProjectSettings_method_clear>`{.interpreted-text role="ref"}

Clears the whole configuration (not recommended, may break things).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_get_global_class_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_global_class_list**()
`🔗<class_ProjectSettings_method_get_global_class_list>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
registered global classes. Each global class is represented as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} that
contains the following entries:

- `base` is a name of the base class;
- `class` is a name of the registered global class;
- `icon` is a path to a custom icon of the global class, if it has any;
- `language` is a name of a programming language in which the global
  class is written;
- `path` is a path to a file containing the global class.

\*\*Note:\*\* Both the script and the icon paths are local to the
project filesystem, i.e. they start with `res://`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_get_order}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_order**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ProjectSettings_method_get_order>`{.interpreted-text
role="ref"}

Returns the order of a configuration value (influences when saved to the
config file).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_get_setting}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_setting**(name: `String<class_String>`{.interpreted-text
role="ref"}, default_value: `Variant<class_Variant>`{.interpreted-text
role="ref"} = null)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ProjectSettings_method_get_setting>`{.interpreted-text
role="ref"}

Returns the value of the setting identified by `name`. If the setting
doesn\'t exist and `default_value` is specified, the value of
`default_value` is returned. Otherwise, `null` is returned.

::::: tabs
::: code-tab
gdscript

print(ProjectSettings.get_setting(\"application/config/name\"))
print(ProjectSettings.get_setting(\"application/config/custom_description\",
\"No description specified.\"))
:::

::: code-tab
csharp

GD.Print(ProjectSettings.GetSetting(\"application/config/name\"));
GD.Print(ProjectSettings.GetSetting(\"application/config/custom_description\",
\"No description specified.\"));
:::
:::::

\*\*Note:\*\* This method doesn\'t take potential feature overrides into
account automatically. Use
`get_setting_with_override()<class_ProjectSettings_method_get_setting_with_override>`{.interpreted-text
role="ref"} to handle seamlessly.

See also
`has_setting()<class_ProjectSettings_method_has_setting>`{.interpreted-text
role="ref"} to check whether a setting exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_get_setting_with_override}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_setting_with_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ProjectSettings_method_get_setting_with_override>`{.interpreted-text
role="ref"}

Similar to
`get_setting()<class_ProjectSettings_method_get_setting>`{.interpreted-text
role="ref"}, but applies feature tag overrides if any exists and is
valid.

\*\*Example:\*\* If the setting override
`"application/config/name.windows"` exists, and the following code is
executed on a *Windows* operating system, the overridden setting is
printed instead:

::::: tabs
::: code-tab
gdscript

print(ProjectSettings.get_setting_with_override(\"application/config/name\"))
:::

::: code-tab
csharp

GD.Print(ProjectSettings.GetSettingWithOverride(\"application/config/name\"));
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_get_setting_with_override_and_custom_features}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_setting_with_override_and_custom_features**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, features:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ProjectSettings_method_get_setting_with_override_and_custom_features>`{.interpreted-text
role="ref"}

Similar to
`get_setting_with_override()<class_ProjectSettings_method_get_setting_with_override>`{.interpreted-text
role="ref"}, but applies feature tag overrides instead of current OS
features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_globalize_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**globalize_path**(path: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ProjectSettings_method_globalize_path>`{.interpreted-text
role="ref"}

Returns the absolute, native OS path corresponding to the localized
`path` (starting with `res://` or `user://`). The returned path will
vary depending on the operating system and user preferences. See
`File paths in Godot projects <../tutorials/io/data_paths>`{.interpreted-text
role="doc"} to see what those paths convert to. See also
`localize_path()<class_ProjectSettings_method_localize_path>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`globalize_path()<class_ProjectSettings_method_globalize_path>`{.interpreted-text
role="ref"} with `res://` will not work in an exported project. Instead,
prepend the executable\'s base directory to the path when running from
an exported project:

    var path = ""
    if OS.has_feature("editor"):
        # Running from an editor binary.
        # `path` will contain the absolute path to `hello.txt` located in the project root.
        path = ProjectSettings.globalize_path("res://hello.txt")
    else:
        # Running from an exported project.
        # `path` will contain the absolute path to `hello.txt` next to the executable.
        # This is *not* identical to using `ProjectSettings.globalize_path()` with a `res://` path,
        # but is close enough in spirit.
        path = OS.get_executable_path().get_base_dir().path_join("hello.txt")

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_has_setting}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_setting**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ProjectSettings_method_has_setting>`{.interpreted-text
role="ref"}

Returns `true` if a configuration value is present.

\*\*Note:\*\* In order to be be detected, custom settings have to be
either defined with
`set_setting()<class_ProjectSettings_method_set_setting>`{.interpreted-text
role="ref"}, or exist in the `project.godot` file. This is especially
relevant when using
`set_initial_value()<class_ProjectSettings_method_set_initial_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_load_resource_pack}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**load_resource_pack**(pack: `String<class_String>`{.interpreted-text
role="ref"}, replace_files: `bool<class_bool>`{.interpreted-text
role="ref"} = true, offset: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_ProjectSettings_method_load_resource_pack>`{.interpreted-text
role="ref"}

Loads the contents of the .pck or .zip file specified by `pack` into the
resource filesystem (`res://`). Returns `true` on success.

\*\*Note:\*\* If a file from `pack` shares the same path as a file
already in the resource filesystem, any attempts to load that file will
use the file from `pack` unless `replace_files` is set to `false`.

\*\*Note:\*\* The optional `offset` parameter can be used to specify the
offset in bytes to the start of the resource pack. This is only
supported for .pck files.

\*\*Note:\*\* `DirAccess<class_DirAccess>`{.interpreted-text role="ref"}
will not show changes made to the contents of `res://` after calling
this function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_localize_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**localize_path**(path: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ProjectSettings_method_localize_path>`{.interpreted-text
role="ref"}

Returns the localized path (starting with `res://`) corresponding to the
absolute, native OS `path`. See also
`globalize_path()<class_ProjectSettings_method_globalize_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_save}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save**() `🔗<class_ProjectSettings_method_save>`{.interpreted-text
role="ref"}

Saves the configuration to the `project.godot` file.

\*\*Note:\*\* This method is intended to be used by editor plugins, as
modified **ProjectSettings** can\'t be loaded back in the running app.
If you want to change project settings in exported projects, use
`save_custom()<class_ProjectSettings_method_save_custom>`{.interpreted-text
role="ref"} to save `override.cfg` file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_save_custom}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_custom**(file: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ProjectSettings_method_save_custom>`{.interpreted-text
role="ref"}

Saves the configuration to a custom file. The file extension must be
`.godot` (to save in text-based
`ConfigFile<class_ConfigFile>`{.interpreted-text role="ref"} format) or
`.binary` (to save in binary format). You can also save `override.cfg`
file, which is also text, but can be used in exported projects unlike
other formats.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_set_as_basic}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_as_basic**(name: `String<class_String>`{.interpreted-text
role="ref"}, basic: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ProjectSettings_method_set_as_basic>`{.interpreted-text
role="ref"}

Defines if the specified setting is considered basic or advanced. Basic
settings will always be shown in the project settings. Advanced settings
will only be shown if the user enables the \"Advanced Settings\" option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_set_as_internal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_as_internal**(name: `String<class_String>`{.interpreted-text
role="ref"}, internal: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ProjectSettings_method_set_as_internal>`{.interpreted-text
role="ref"}

Defines if the specified setting is considered internal. An internal
setting won\'t show up in the Project Settings dialog. This is mostly
useful for addons that need to store their own internal settings without
exposing them directly to the user.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_set_initial_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_initial_value**(name: `String<class_String>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_ProjectSettings_method_set_initial_value>`{.interpreted-text
role="ref"}

Sets the specified setting\'s initial value. This is the value the
setting reverts to. The setting should already exist before calling this
method. Note that project settings equal to their default value are not
saved, so your code needs to account for that.

    extends EditorPlugin

    const SETTING_NAME = "addons/my_setting"
    const SETTING_DEFAULT = 10.0

    func _enter_tree():
        if not ProjectSettings.has_setting(SETTING_NAME):
            ProjectSettings.set_setting(SETTING_NAME, SETTING_DEFAULT)

        ProjectSettings.set_initial_value(SETTING_NAME, SETTING_DEFAULT)

If you have a project setting defined by an
`EditorPlugin<class_EditorPlugin>`{.interpreted-text role="ref"}, but
want to use it in a running project, you will need a similar code at
runtime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_set_order}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_order**(name: `String<class_String>`{.interpreted-text
role="ref"}, position: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ProjectSettings_method_set_order>`{.interpreted-text
role="ref"}

Sets the order of a configuration value (influences when saved to the
config file).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_set_restart_if_changed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_restart_if_changed**(name:
`String<class_String>`{.interpreted-text role="ref"}, restart:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ProjectSettings_method_set_restart_if_changed>`{.interpreted-text
role="ref"}

Sets whether a setting requires restarting the editor to properly take
effect.

\*\*Note:\*\* This is just a hint to display to the user that the editor
must be restarted for changes to take effect. Enabling
`set_restart_if_changed()<class_ProjectSettings_method_set_restart_if_changed>`{.interpreted-text
role="ref"} does *not* delay the setting being set when changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ProjectSettings_method_set_setting}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_setting**(name: `String<class_String>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_ProjectSettings_method_set_setting>`{.interpreted-text
role="ref"}

Sets the value of a setting.

::::: tabs
::: code-tab
gdscript

ProjectSettings.set_setting(\"application/config/name\", \"Example\")
:::

::: code-tab
csharp

ProjectSettings.SetSetting(\"application/config/name\", \"Example\");
:::
:::::

This can also be used to erase custom project settings. To do this
change the setting value to `null`.
