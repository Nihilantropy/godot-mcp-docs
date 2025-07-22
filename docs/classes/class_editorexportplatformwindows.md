github_url
:   hide

# EditorExportPlatformWindows {#class_EditorExportPlatformWindows}

**Inherits:**
`EditorExportPlatformPC<class_EditorExportPlatformPC>`{.interpreted-text
role="ref"} **\<**
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Exporter for Windows.

::: rst-class
classref-introduction-group
:::

## Description

The Windows exporter customizes how a Windows build is handled. In the
editor\'s \"Export\" window, it is created when adding a new \"Windows\"
preset.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Exporting for Windows <../tutorials/export/exporting_for_windows>`{.interpreted-text
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

:::: {#class_EditorExportPlatformWindows_property_application/company_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/company_name**
`🔗<class_EditorExportPlatformWindows_property_application/company_name>`{.interpreted-text
role="ref"}

Company that produced the application. Required. See
[StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/console_wrapper_icon}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/console_wrapper_icon**
`🔗<class_EditorExportPlatformWindows_property_application/console_wrapper_icon>`{.interpreted-text
role="ref"}

Console wrapper icon file. If left empty, it will fallback to
`application/icon<class_EditorExportPlatformWindows_property_application/icon>`{.interpreted-text
role="ref"}, then to
`ProjectSettings.application/config/windows_native_icon<class_ProjectSettings_property_application/config/windows_native_icon>`{.interpreted-text
role="ref"}, and lastly,
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/copyright}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/copyright**
`🔗<class_EditorExportPlatformWindows_property_application/copyright>`{.interpreted-text
role="ref"}

Copyright notice for the bundle visible to the user. Optional. See
[StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/d3d12_agility_sdk_multiarch}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/d3d12_agility_sdk_multiarch**
`🔗<class_EditorExportPlatformWindows_property_application/d3d12_agility_sdk_multiarch>`{.interpreted-text
role="ref"}

If `true`, and
`application/export_d3d12<class_EditorExportPlatformWindows_property_application/export_d3d12>`{.interpreted-text
role="ref"} is set, the Agility SDK DLLs will be stored in arch-specific
subdirectories.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/export_angle}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/export_angle**
`🔗<class_EditorExportPlatformWindows_property_application/export_angle>`{.interpreted-text
role="ref"}

If set to `1`, ANGLE libraries are exported with the exported
application. If set to `0`, ANGLE libraries are exported only if
`ProjectSettings.rendering/gl_compatibility/driver<class_ProjectSettings_property_rendering/gl_compatibility/driver>`{.interpreted-text
role="ref"} is set to `"opengl3_angle"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/export_d3d12}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/export_d3d12**
`🔗<class_EditorExportPlatformWindows_property_application/export_d3d12>`{.interpreted-text
role="ref"}

If set to `1`, the Direct3D 12 runtime libraries (Agility SDK, PIX) are
exported with the exported application. If set to `0`, Direct3D 12
libraries are exported only if
`ProjectSettings.rendering/rendering_device/driver<class_ProjectSettings_property_rendering/rendering_device/driver>`{.interpreted-text
role="ref"} is set to `"d3d12"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/file_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/file_description**
`🔗<class_EditorExportPlatformWindows_property_application/file_description>`{.interpreted-text
role="ref"}

File description to be presented to users. Required. See
[StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/file_version}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/file_version**
`🔗<class_EditorExportPlatformWindows_property_application/file_version>`{.interpreted-text
role="ref"}

Version number of the file. Falls back to
`ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>`{.interpreted-text
role="ref"} if left empty. See
[StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/icon}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/icon**
`🔗<class_EditorExportPlatformWindows_property_application/icon>`{.interpreted-text
role="ref"}

Application icon file. If left empty, it will fallback to
`ProjectSettings.application/config/windows_native_icon<class_ProjectSettings_property_application/config/windows_native_icon>`{.interpreted-text
role="ref"}, and then to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/icon_interpolation}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/icon_interpolation**
`🔗<class_EditorExportPlatformWindows_property_application/icon_interpolation>`{.interpreted-text
role="ref"}

Interpolation method used to resize application icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/modify_resources}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**application/modify_resources**
`🔗<class_EditorExportPlatformWindows_property_application/modify_resources>`{.interpreted-text
role="ref"}

If enabled, icon and metadata of the exported executable is set
according to the other `application/*` values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/product_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/product_name**
`🔗<class_EditorExportPlatformWindows_property_application/product_name>`{.interpreted-text
role="ref"}

Name of the application. Required. See
[StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/product_version}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/product_version**
`🔗<class_EditorExportPlatformWindows_property_application/product_version>`{.interpreted-text
role="ref"}

Application version visible to the user. Falls back to
`ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>`{.interpreted-text
role="ref"} if left empty. See
[StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_application/trademarks}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/trademarks**
`🔗<class_EditorExportPlatformWindows_property_application/trademarks>`{.interpreted-text
role="ref"}

Trademarks and registered trademarks that apply to the file. Optional.
See
[StringFileInfo](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_binary_format/architecture}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**binary_format/architecture**
`🔗<class_EditorExportPlatformWindows_property_binary_format/architecture>`{.interpreted-text
role="ref"}

Application executable architecture.

Supported architectures: `x86_32`, `x86_64`, and `arm64`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_binary_format/embed_pck}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**binary_format/embed_pck**
`🔗<class_EditorExportPlatformWindows_property_binary_format/embed_pck>`{.interpreted-text
role="ref"}

If `true`, project resources are embedded into the executable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_codesign/custom_options}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **codesign/custom_options**
`🔗<class_EditorExportPlatformWindows_property_codesign/custom_options>`{.interpreted-text
role="ref"}

Array of the additional command line arguments passed to the code
signing tool. See [Sign
Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_codesign/description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/description**
`🔗<class_EditorExportPlatformWindows_property_codesign/description>`{.interpreted-text
role="ref"}

Description of the signed content. See [Sign
Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_codesign/digest_algorithm}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**codesign/digest_algorithm**
`🔗<class_EditorExportPlatformWindows_property_codesign/digest_algorithm>`{.interpreted-text
role="ref"}

Digest algorithm to use for creating signature. See [Sign
Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_codesign/enable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **codesign/enable**
`🔗<class_EditorExportPlatformWindows_property_codesign/enable>`{.interpreted-text
role="ref"}

If `true`, executable signing is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_codesign/identity}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/identity**
`🔗<class_EditorExportPlatformWindows_property_codesign/identity>`{.interpreted-text
role="ref"}

PKCS #12 certificate file used to sign executable or certificate SHA-1
hash (if
`codesign/identity_type<class_EditorExportPlatformWindows_property_codesign/identity_type>`{.interpreted-text
role="ref"} is set to \"Use certificate store\"). See [Sign
Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

Can be overridden with the environment variable
`GODOT_WINDOWS_CODESIGN_IDENTITY`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_codesign/identity_type}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**codesign/identity_type**
`🔗<class_EditorExportPlatformWindows_property_codesign/identity_type>`{.interpreted-text
role="ref"}

Type of identity to use. See [Sign
Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

Can be overridden with the environment variable
`GODOT_WINDOWS_CODESIGN_IDENTITY_TYPE`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_codesign/password}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/password**
`🔗<class_EditorExportPlatformWindows_property_codesign/password>`{.interpreted-text
role="ref"}

Password for the certificate file used to sign executable. See [Sign
Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

Can be overridden with the environment variable
`GODOT_WINDOWS_CODESIGN_PASSWORD`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_codesign/timestamp}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **codesign/timestamp**
`🔗<class_EditorExportPlatformWindows_property_codesign/timestamp>`{.interpreted-text
role="ref"}

If `true`, time-stamp is added to the signature. See [Sign
Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_codesign/timestamp_server_url}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/timestamp_server_url**
`🔗<class_EditorExportPlatformWindows_property_codesign/timestamp_server_url>`{.interpreted-text
role="ref"}

URL of the time stamp server. If left empty, the default server is used.
See [Sign
Tool](https://learn.microsoft.com/en-us/dotnet/framework/tools/signtool-exe).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_custom_template/debug}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/debug**
`🔗<class_EditorExportPlatformWindows_property_custom_template/debug>`{.interpreted-text
role="ref"}

Path to the custom export template. If left empty, default template is
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_custom_template/release}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/release**
`🔗<class_EditorExportPlatformWindows_property_custom_template/release>`{.interpreted-text
role="ref"}

Path to the custom export template. If left empty, default template is
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_debug/export_console_wrapper}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/export_console_wrapper**
`🔗<class_EditorExportPlatformWindows_property_debug/export_console_wrapper>`{.interpreted-text
role="ref"}

If `true`, a console wrapper executable is exported alongside the main
executable, which allows running the project with enabled console
output.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_shader_baker/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shader_baker/enabled**
`🔗<class_EditorExportPlatformWindows_property_shader_baker/enabled>`{.interpreted-text
role="ref"}

If `true`, shaders will be compiled and embedded in the application.
This option is only supported when using the Forward+ and Mobile
renderers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_ssh_remote_deploy/cleanup_script}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/cleanup_script**
`🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/cleanup_script>`{.interpreted-text
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

:::: {#class_EditorExportPlatformWindows_property_ssh_remote_deploy/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**ssh_remote_deploy/enabled**
`🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/enabled>`{.interpreted-text
role="ref"}

Enables remote deploy using SSH/SCP.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_scp}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/extra_args_scp**
`🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_scp>`{.interpreted-text
role="ref"}

Array of the additional command line arguments passed to the SCP.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_ssh}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/extra_args_ssh**
`🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/extra_args_ssh>`{.interpreted-text
role="ref"}

Array of the additional command line arguments passed to the SSH.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_ssh_remote_deploy/host}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/host**
`🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/host>`{.interpreted-text
role="ref"}

Remote host SSH user name and address, in `user@address` format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_ssh_remote_deploy/port}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/port**
`🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/port>`{.interpreted-text
role="ref"}

Remote host SSH port number.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_ssh_remote_deploy/run_script}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/run_script**
`🔗<class_EditorExportPlatformWindows_property_ssh_remote_deploy/run_script>`{.interpreted-text
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

:::: {#class_EditorExportPlatformWindows_property_texture_format/etc2_astc}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**texture_format/etc2_astc**
`🔗<class_EditorExportPlatformWindows_property_texture_format/etc2_astc>`{.interpreted-text
role="ref"}

If `true`, project textures are exported in the ETC2/ASTC format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWindows_property_texture_format/s3tc_bptc}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**texture_format/s3tc_bptc**
`🔗<class_EditorExportPlatformWindows_property_texture_format/s3tc_bptc>`{.interpreted-text
role="ref"}

If `true`, project textures are exported in the S3TC/BPTC format.
