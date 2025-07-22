# JetBrains Rider {#doc_configuring_an_ide_rider}

[JetBrains Rider](https://www.jetbrains.com/rider/) is a commercial
[JetBrains](https://www.jetbrains.com/) IDE for C++, C# and GDScript
that uses the same solution system as Visual Studio.

:::: note
::: title
Note
:::

This documentation is for contributing to the game engine, not for using
JetBrains Rider as a C# or GDScript editor. To code C# or GDScript in an
external editor, see
`the C# guide to configure an external editor <doc_c_sharp_setup_external_editor>`{.interpreted-text
role="ref"}.
::::

## Importing the project

:::: tip
::: title
Tip
:::

If you already use Visual Studio as your main IDE, you can use the same
solution file in Rider. Rider and Visual Studio use the same solution
format, so you can switch between the two IDEs without rebuilding the
solution file. Debug configurations need to be changed when going from
one IDE to another.
::::

If you are starting from the scratch, please follow
`instructions<doc_compiling_index>`{.interpreted-text role="ref"},
specifically:

- Install all the dependencies.
- Figure out the scons command for compiling to target a specific
  platform.

Provide scons with additional arguments to request a solution file
generation:

- Add [vsproj=yes dev_build=yes]{.title-ref} to the scons command

The `vsproj` parameter signals that you want Visual Studio solution
generated. The `dev_build` parameter ensures the debug symbols are
included, allowing to e.g. step through code using breakpoints.

- Open the generated `godot.sln` in Rider.

:::: note
::: title
Note
:::

Ensure that the appropriate Solution configuration is selected on the
Rider toolbar. It affects resolve of the SDKs, code analysis, build,
run, etc.
::::

## Compiling and debugging the project

Rider comes with a built-in debugger that can be used to debug the Godot
project. You can launch the debugger by pressing the **Debug** icon at
the top of the screen, this only works for the Project Manager, if you
want to debug the editor, you need to configure the debugger first.

<figure class="align-center">
<img src="img/rider_run_debug.webp" alt="img/rider_run_debug.webp" />
</figure>

- Click on the **Godot \> Edit Configurations** option at the top of the
  screen.

<figure class="align-center">
<img src="img/rider_configurations.webp"
alt="img/rider_configurations.webp" />
</figure>

- Ensure the following values for the C++ Project Run Configuration:

  > - Exe Path : `$(LocalDebuggerCommand)`
  > - Program Arguments: `-e --path <path to the Godot project>`
  > - Working Directory: `$(LocalDebuggerWorkingDirectory)`
  > - Before Launch has a value of \"Build Project\"

This will tell the executable to debug the specified project without
opening the Project Manager. Use the root path to the project folder,
not `project.godot` file path.

<figure class="align-center">
<img src="img/rider_configurations_changed.webp"
alt="img/rider_configurations_changed.webp" />
</figure>

- Finally click on \"Apply\" and \"OK\" to save the changes.
- When you press the **Debug** icon at the top of the screen, JetBrains
  Rider will launch the Godot editor with the debugger attached.

Alternatively you can use **Run \> Attach to Process** to attach the
debugger to a running Godot instance.

<figure class="align-center">
<img src="img/rider_attach_to_process.webp"
alt="img/rider_attach_to_process.webp" />
</figure>

- You can find the Godot instance by searching for `godot.editor` and
  then clicking `Attach with LLDB`

<figure class="align-center">
<img src="img/rider_attach_to_process_dialog.webp"
alt="img/rider_attach_to_process_dialog.webp" />
</figure>

| 

## Debug visualizers

Debug visualizers customize how complex data structures are displayed
during debugging. For Windows \"natvis\" (short for \"Native
Visualization\") built-in with Godot are automatically used. For other
operating systems, similar functionality can be setup manually.

Please follow
[RIDER-123535](https://youtrack.jetbrains.com/issue/RIDER-123535/nix-Debug-Godot-Cpp-from-Rider-pretty-printers-usability).

## Unit testing

Leverage Rider `doctest<doc_unit_testing>`{.interpreted-text role="ref"}
support. Please refer to [the
instructions](https://github.com/JetBrains/godot-support/wiki/Godot-doctest-Unit-Tests).

## Profiling

Please refer to [the profiling
instructions](https://github.com/JetBrains/godot-support/wiki/Profiling-Godot-engine-(native-code)-with-dotTrace-or-JetBrains-Rider).

Please consult the [JetBrains Rider
documentation](https://www.jetbrains.com/rider/documentation/) for any
specific information about the JetBrains IDE.

## Known issues

Debugging Windows MinGV build - symbols are not loaded. Reported
[RIDER-106816](https://youtrack.jetbrains.com/issue/RIDER-106816/Upgrade-LLDB-to-actual-version).
