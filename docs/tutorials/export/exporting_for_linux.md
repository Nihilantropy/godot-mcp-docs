# Exporting for Linux {#doc_exporting_for_linux}

::: seealso
This page describes how to export a Godot project to Linux. If you\'re
looking to compile editor or export template binaries from source
instead, read `doc_compiling_for_linuxbsd`{.interpreted-text
role="ref"}.
:::

The simplest way to distribute a game for PC is to copy the executable
(`godot`), compress the folder and send it to someone else. However,
this is often not desired.

Godot offers a more elegant approach for PC distribution when using the
export system. When exporting for Linux, the exporter takes all the
project files and creates a `data.pck` file. This file is bundled with a
specially optimized binary that is smaller, faster and does not contain
the editor and debugger.

## Environment variables

You can use the following environment variables to set export options
outside of the editor. During the export process, these override the
values that you set in the export menu.

  Export option                 Environment variable
  ----------------------------- -------------------------------
  Encryption / Encryption Key   `GODOT_SCRIPT_ENCRYPTION_KEY`

  : Linux export environment variables

## Export options

You can find a full list of export options available in the
`class_EditorExportPlatformLinuxBSD`{.interpreted-text role="ref"} class
reference.
