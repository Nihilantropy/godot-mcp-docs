github_url
:   hide

# EditorExportPlatformLinuxBSD {#class_EditorExportPlatformLinuxBSD}

**Inherits:**
`EditorExportPlatformPC<class_EditorExportPlatformPC>`{.interpreted-text
role="ref"} **\<**
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Exporter for Linux/BSD.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Exporting for Linux <../tutorials/export/exporting_for_linux>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_EditorExportPlatformLinuxBSD_property_binary_format/architecture}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**binary_format/architecture**
`🔗<class_EditorExportPlatformLinuxBSD_property_binary_format/architecture>`{.interpreted-text
role="ref"}

Application executable architecture.

Supported architectures: `x86_32`, `x86_64`, `arm64`, `arm32`, `rv64`,
`ppc64`, and `loongarch64`.

Official export templates include `x86_32`, `x86_64`, `arm32`, and
`arm64` binaries only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_binary_format/embed_pck}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**binary_format/embed_pck**
`🔗<class_EditorExportPlatformLinuxBSD_property_binary_format/embed_pck>`{.interpreted-text
role="ref"}

If `true`, project resources are embedded into the executable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_custom_template/debug}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/debug**
`🔗<class_EditorExportPlatformLinuxBSD_property_custom_template/debug>`{.interpreted-text
role="ref"}

Path to the custom export template. If left empty, default template is
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_custom_template/release}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/release**
`🔗<class_EditorExportPlatformLinuxBSD_property_custom_template/release>`{.interpreted-text
role="ref"}

Path to the custom export template. If left empty, default template is
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_debug/export_console_wrapper}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/export_console_wrapper**
`🔗<class_EditorExportPlatformLinuxBSD_property_debug/export_console_wrapper>`{.interpreted-text
role="ref"}

If `true`, a console wrapper is exported alongside the main executable,
which allows running the project with enabled console output.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_shader_baker/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shader_baker/enabled**
`🔗<class_EditorExportPlatformLinuxBSD_property_shader_baker/enabled>`{.interpreted-text
role="ref"}

If `true`, shaders will be compiled and embedded in the application.
This option is only supported when using the Forward+ or Mobile
renderers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/cleanup_script}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/cleanup_script**
`🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/cleanup_script>`{.interpreted-text
role="ref"}

Script code to execute on the remote host when app is finished.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload
  app and scripts to.
- `{archive_name}` - Name of the ZIP containing uploaded application.
- `{exe_name}` - Name of application executable.
- `{cmd_args}` - Array of the command line argument for the application.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**ssh_remote_deploy/enabled**
`🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/enabled>`{.interpreted-text
role="ref"}

Enables remote deploy using SSH/SCP.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/extra_args_scp}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/extra_args_scp**
`🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/extra_args_scp>`{.interpreted-text
role="ref"}

Array of the additional command line arguments passed to the SCP.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/extra_args_ssh}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/extra_args_ssh**
`🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/extra_args_ssh>`{.interpreted-text
role="ref"}

Array of the additional command line arguments passed to the SSH.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/host}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/host**
`🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/host>`{.interpreted-text
role="ref"}

Remote host SSH user name and address, in `user@address` format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/port}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/port**
`🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/port>`{.interpreted-text
role="ref"}

Remote host SSH port number.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/run_script}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/run_script**
`🔗<class_EditorExportPlatformLinuxBSD_property_ssh_remote_deploy/run_script>`{.interpreted-text
role="ref"}

Script code to execute on the remote host when running the app.

The following variables can be used in the script:

- `{temp_dir}` - Path of temporary folder on the remote, used to upload
  app and scripts to.
- `{archive_name}` - Name of the ZIP containing uploaded application.
- `{exe_name}` - Name of application executable.
- `{cmd_args}` - Array of the command line argument for the application.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_texture_format/etc2_astc}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**texture_format/etc2_astc**
`🔗<class_EditorExportPlatformLinuxBSD_property_texture_format/etc2_astc>`{.interpreted-text
role="ref"}

If `true`, project textures are exported in the ETC2/ASTC format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformLinuxBSD_property_texture_format/s3tc_bptc}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**texture_format/s3tc_bptc**
`🔗<class_EditorExportPlatformLinuxBSD_property_texture_format/s3tc_bptc>`{.interpreted-text
role="ref"}

If `true`, project textures are exported in the S3TC/BPTC format.
