github_url
:   hide

# EditorExportPlatformMacOS {#class_EditorExportPlatformMacOS}

**Inherits:**
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Exporter for macOS.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Exporting for macOS <../tutorials/export/exporting_for_macos>`{.interpreted-text
  role="doc"}
- `Running Godot apps on macOS <../tutorials//export/running_on_macos>`{.interpreted-text
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

:::: {#class_EditorExportPlatformMacOS_property_application/additional_plist_content}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/additional_plist_content**
`🔗<class_EditorExportPlatformMacOS_property_application/additional_plist_content>`{.interpreted-text
role="ref"}

Additional data added to the root `<dict>` section of the
[Info.plist](https://developer.apple.com/documentation/bundleresources/information_property_list)
file. The value should be an XML section with pairs of key-value
elements, e.g.:

``` text
<key>key_name</key>
<string>value</string>
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/app_category}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/app_category**
`🔗<class_EditorExportPlatformMacOS_property_application/app_category>`{.interpreted-text
role="ref"}

Application category for the App Store.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/bundle_identifier}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/bundle_identifier**
`🔗<class_EditorExportPlatformMacOS_property_application/bundle_identifier>`{.interpreted-text
role="ref"}

Unique application identifier in a reverse-DNS format, can only contain
alphanumeric characters (`A-Z`, `a-z`, and `0-9`), hyphens (`-`), and
periods (`.`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/copyright}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/copyright**
`🔗<class_EditorExportPlatformMacOS_property_application/copyright>`{.interpreted-text
role="ref"}

Copyright notice for the bundle visible to the user (in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/copyright_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**application/copyright_localized**
`🔗<class_EditorExportPlatformMacOS_property_application/copyright_localized>`{.interpreted-text
role="ref"}

Copyright notice for the bundle visible to the user (localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/export_angle}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/export_angle**
`🔗<class_EditorExportPlatformMacOS_property_application/export_angle>`{.interpreted-text
role="ref"}

If set to `1`, ANGLE libraries are exported with the exported
application. If set to `0`, ANGLE libraries are exported only if
`ProjectSettings.rendering/gl_compatibility/driver<class_ProjectSettings_property_rendering/gl_compatibility/driver>`{.interpreted-text
role="ref"} is set to `"opengl3_angle"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/icon}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/icon**
`🔗<class_EditorExportPlatformMacOS_property_application/icon>`{.interpreted-text
role="ref"}

Application icon file. If left empty, it will fallback to
`ProjectSettings.application/config/macos_native_icon<class_ProjectSettings_property_application/config/macos_native_icon>`{.interpreted-text
role="ref"}, and then to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/icon_interpolation}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**application/icon_interpolation**
`🔗<class_EditorExportPlatformMacOS_property_application/icon_interpolation>`{.interpreted-text
role="ref"}

Interpolation method used to resize application icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/min_macos_version_arm64}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/min_macos_version_arm64**
`🔗<class_EditorExportPlatformMacOS_property_application/min_macos_version_arm64>`{.interpreted-text
role="ref"}

Minimum version of macOS required for this application to run on Apple
Silicon Macs, in the `major.minor.patch` or `major.minor` format, can
only contain numeric characters (`0-9`) and periods (`.`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/min_macos_version_x86_64}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/min_macos_version_x86_64**
`🔗<class_EditorExportPlatformMacOS_property_application/min_macos_version_x86_64>`{.interpreted-text
role="ref"}

Minimum version of macOS required for this application to run on Intel
Macs, in the `major.minor.patch` or `major.minor` format, can only
contain numeric characters (`0-9`) and periods (`.`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/short_version}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/short_version**
`🔗<class_EditorExportPlatformMacOS_property_application/short_version>`{.interpreted-text
role="ref"}

Application version visible to the user, can only contain numeric
characters (`0-9`) and periods (`.`). Falls back to
`ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>`{.interpreted-text
role="ref"} if left empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/signature}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/signature**
`🔗<class_EditorExportPlatformMacOS_property_application/signature>`{.interpreted-text
role="ref"}

A four-character creator code that is specific to the bundle. Optional.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_application/version}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**application/version**
`🔗<class_EditorExportPlatformMacOS_property_application/version>`{.interpreted-text
role="ref"}

Machine-readable application version, in the `major.minor.patch` format,
can only contain numeric characters (`0-9`) and periods (`.`). This must
be incremented on every new release pushed to the App Store.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_binary_format/architecture}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**binary_format/architecture**
`🔗<class_EditorExportPlatformMacOS_property_binary_format/architecture>`{.interpreted-text
role="ref"}

Application executable architecture.

Supported architectures: `x86_64`, `arm64`, and `universal`
(`x86_64 + arm64`).

Official export templates include `universal` binaries only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/apple_team_id}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/apple_team_id**
`🔗<class_EditorExportPlatformMacOS_property_codesign/apple_team_id>`{.interpreted-text
role="ref"}

Apple Team ID, unique 10-character string. To locate your Team ID check
\"Membership details\" section in your Apple developer account
dashboard, or \"Organizational Unit\" of your code signing certificate.
See [Locate your Team
ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/certificate_file}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/certificate_file**
`🔗<class_EditorExportPlatformMacOS_property_codesign/certificate_file>`{.interpreted-text
role="ref"}

PKCS #12 certificate file used to sign `.app` bundle.

Can be overridden with the environment variable
`GODOT_MACOS_CODESIGN_CERTIFICATE_FILE`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/certificate_password}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/certificate_password**
`🔗<class_EditorExportPlatformMacOS_property_codesign/certificate_password>`{.interpreted-text
role="ref"}

Password for the certificate file used to sign `.app` bundle.

Can be overridden with the environment variable
`GODOT_MACOS_CODESIGN_CERTIFICATE_PASSWORD`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/codesign}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **codesign/codesign**
`🔗<class_EditorExportPlatformMacOS_property_codesign/codesign>`{.interpreted-text
role="ref"}

Tool to use for code signing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/custom_options}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **codesign/custom_options**
`🔗<class_EditorExportPlatformMacOS_property_codesign/custom_options>`{.interpreted-text
role="ref"}

Array of the additional command line arguments passed to the code
signing tool.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/additional}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/entitlements/additional**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/additional>`{.interpreted-text
role="ref"}

Additional data added to the root `<dict>` section of the
[.entitlements](https://developer.apple.com/documentation/bundleresources/entitlements)
file. The value should be an XML section with pairs of key-value
elements, for example:

``` text
<key>key_name</key>
<string>value</string>
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/address_book}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/address_book**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/address_book>`{.interpreted-text
role="ref"}

Enable to allow access to contacts in the user\'s address book, if it\'s
enabled you should also provide usage message in the
`privacy/address_book_usage_description<class_EditorExportPlatformMacOS_property_privacy/address_book_usage_description>`{.interpreted-text
role="ref"} option. See
[com.apple.security.personal-information.addressbook](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_personal-information_addressbook).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/allow_dyld_environment_variables}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/allow_dyld_environment_variables**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/allow_dyld_environment_variables>`{.interpreted-text
role="ref"}

Allows app to use dynamic linker environment variables to inject code.
If you are using add-ons with dynamic or self-modifying native code,
enable them according to the add-on documentation. See
[com.apple.security.cs.allow-dyld-environment-variables](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_cs_allow-dyld-environment-variables).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/allow_jit_code_execution}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/allow_jit_code_execution**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/allow_jit_code_execution>`{.interpreted-text
role="ref"}

Allows creating writable and executable memory for JIT code. If you are
using add-ons with dynamic or self-modifying native code, enable them
according to the add-on documentation. See
[com.apple.security.cs.allow-jit](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_cs_allow-jit).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/allow_unsigned_executable_memory}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/allow_unsigned_executable_memory**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/allow_unsigned_executable_memory>`{.interpreted-text
role="ref"}

Allows creating writable and executable memory without JIT restrictions.
If you are using add-ons with dynamic or self-modifying native code,
enable them according to the add-on documentation. See
[com.apple.security.cs.allow-unsigned-executable-memory](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_cs_allow-unsigned-executable-memory).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/device_bluetooth}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/device_bluetooth**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/device_bluetooth>`{.interpreted-text
role="ref"}

Enable to allow app to interact with Bluetooth devices. This entitlement
is required to use wireless controllers. See
[com.apple.security.device.bluetooth](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_device_bluetooth).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/device_usb}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/device_usb**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/device_usb>`{.interpreted-text
role="ref"}

Enable to allow app to interact with USB devices. This entitlement is
required to use wired controllers. See
[com.apple.security.device.usb](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_device_usb).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/enabled**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/enabled>`{.interpreted-text
role="ref"}

Enables App Sandbox. The App Sandbox restricts access to user data,
networking, and devices. Sandboxed apps can\'t access most of the file
system, can\'t use custom file dialogs and execute binaries outside the
.app bundle. See [App
Sandbox](https://developer.apple.com/documentation/security/app_sandbox).

\*\*Note:\*\* To distribute an app through the App Store, you must
enable the App Sandbox.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_downloads}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/files_downloads**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_downloads>`{.interpreted-text
role="ref"}

Allows read or write access to the user\'s \"Downloads\" folder. See
[com.apple.security.files.downloads.read-write](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_files_downloads_read-write).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_movies}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/files_movies**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_movies>`{.interpreted-text
role="ref"}

Allows read or write access to the user\'s \"Movies\" folder. See
[com.apple.security.files.movies.read-write](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_assets_movies_read-write).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_music}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/files_music**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_music>`{.interpreted-text
role="ref"}

Allows read or write access to the user\'s \"Music\" folder. See
[com.apple.security.files.music.read-write](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_assets_music_read-write).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_pictures}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/files_pictures**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_pictures>`{.interpreted-text
role="ref"}

Allows read or write access to the user\'s \"Pictures\" folder. See
[com.apple.security.files.pictures.read-write](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_assets_pictures_read-write).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_user_selected}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/files_user_selected**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/files_user_selected>`{.interpreted-text
role="ref"}

Allows read or write access to the locations the user has selected using
a native file dialog. See
[com.apple.security.files.user-selected.read-write](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_files_user-selected_read-write).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/helper_executables}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/helper_executables**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/helper_executables>`{.interpreted-text
role="ref"}

List of helper executables to embedded to the app bundle. Sandboxed app
are limited to execute only these executable. See [Embedding a
command-line tool in a sandboxed
app](https://developer.apple.com/documentation/xcode/embedding-a-helper-tool-in-a-sandboxed-app).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/network_client}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/network_client**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/network_client>`{.interpreted-text
role="ref"}

Enable to allow app to establish outgoing network connections. See
[com.apple.security.network.client](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_network_client).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/network_server}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/app_sandbox/network_server**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/app_sandbox/network_server>`{.interpreted-text
role="ref"}

Enable to allow app to listen for incoming network connections. See
[com.apple.security.network.server](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_network_server).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/apple_events}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/apple_events**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/apple_events>`{.interpreted-text
role="ref"}

Enable to allow app to send Apple events to other apps. See
[com.apple.security.automation.apple-events](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_automation_apple-events).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/audio_input}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/audio_input**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/audio_input>`{.interpreted-text
role="ref"}

Enable if you need to use the microphone or other audio input sources,
if it\'s enabled you should also provide usage message in the
`privacy/microphone_usage_description<class_EditorExportPlatformMacOS_property_privacy/microphone_usage_description>`{.interpreted-text
role="ref"} option. See
[com.apple.security.device.audio-input](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_device_audio-input).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/calendars}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/calendars**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/calendars>`{.interpreted-text
role="ref"}

Enable to allow access to the user\'s calendar, if it\'s enabled you
should also provide usage message in the
`privacy/calendar_usage_description<class_EditorExportPlatformMacOS_property_privacy/calendar_usage_description>`{.interpreted-text
role="ref"} option. See
[com.apple.security.personal-information.calendars](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_personal-information_calendars).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/camera}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/camera**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/camera>`{.interpreted-text
role="ref"}

Enable if you need to use the camera, if it\'s enabled you should also
provide usage message in the
`privacy/camera_usage_description<class_EditorExportPlatformMacOS_property_privacy/camera_usage_description>`{.interpreted-text
role="ref"} option. See
[com.apple.security.device.camera](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_device_camera).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/custom_file}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/entitlements/custom_file**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/custom_file>`{.interpreted-text
role="ref"}

Custom entitlements `.plist` file, if specified the rest of entitlements
in the export config are ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/debugging}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/debugging**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/debugging>`{.interpreted-text
role="ref"}

You can temporarily enable this entitlement to use native debugger (GDB,
LLDB) with the exported app. This entitlement should be disabled for
production export. See [Embedding a command-line tool in a sandboxed
app](https://developer.apple.com/documentation/xcode/embedding-a-helper-tool-in-a-sandboxed-app).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/disable_library_validation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/disable_library_validation**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/disable_library_validation>`{.interpreted-text
role="ref"}

Allows app to load arbitrary libraries and frameworks (not signed with
the same Team ID as the main executable or by Apple). Enable it if you
are using GDExtension add-ons or ad-hoc signing, or want to support
user-provided external add-ons. See
[com.apple.security.cs.disable-library-validation](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_cs_disable-library-validation).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/location}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/location**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/location>`{.interpreted-text
role="ref"}

Enable if you need to use location information from Location Services,
if it\'s enabled you should also provide usage message in the
`privacy/location_usage_description<class_EditorExportPlatformMacOS_property_privacy/location_usage_description>`{.interpreted-text
role="ref"} option. See
[com.apple.security.personal-information.location](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_personal-information_location).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/entitlements/photos_library}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**codesign/entitlements/photos_library**
`🔗<class_EditorExportPlatformMacOS_property_codesign/entitlements/photos_library>`{.interpreted-text
role="ref"}

Enable to allow access to the user\'s Photos library, if it\'s enabled
you should also provide usage message in the
`privacy/photos_library_usage_description<class_EditorExportPlatformMacOS_property_privacy/photos_library_usage_description>`{.interpreted-text
role="ref"} option. See
[com.apple.security.personal-information.photos-library](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_personal-information_photos-library).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/identity}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/identity**
`🔗<class_EditorExportPlatformMacOS_property_codesign/identity>`{.interpreted-text
role="ref"}

The \"Full Name\", \"Common Name\" or SHA-1 hash of the signing identity
used to sign `.app` bundle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/installer_identity}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/installer_identity**
`🔗<class_EditorExportPlatformMacOS_property_codesign/installer_identity>`{.interpreted-text
role="ref"}

The \"Full Name\", \"Common Name\" or SHA-1 hash of the signing identity
used to sign `.pkg` installer package for App Store distribution, use
`3rd Party Mac Developer Installer: Name.` identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_codesign/provisioning_profile}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**codesign/provisioning_profile**
`🔗<class_EditorExportPlatformMacOS_property_codesign/provisioning_profile>`{.interpreted-text
role="ref"}

Provisioning profile file downloaded from Apple developer account
dashboard. See [Edit, download, or delete provisioning
profiles](https://developer.apple.com/help/account/manage-profiles/edit-download-or-delete-profiles).

Can be overridden with the environment variable
`GODOT_MACOS_CODESIGN_PROVISIONING_PROFILE`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_custom_template/debug}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/debug**
`🔗<class_EditorExportPlatformMacOS_property_custom_template/debug>`{.interpreted-text
role="ref"}

Path to the custom export template. If left empty, default template is
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_custom_template/release}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/release**
`🔗<class_EditorExportPlatformMacOS_property_custom_template/release>`{.interpreted-text
role="ref"}

Path to the custom export template. If left empty, default template is
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_debug/export_console_wrapper}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debug/export_console_wrapper**
`🔗<class_EditorExportPlatformMacOS_property_debug/export_console_wrapper>`{.interpreted-text
role="ref"}

If enabled, a wrapper that can be used to run the application with
console output is created alongside the exported application.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_display/high_res}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **display/high_res**
`🔗<class_EditorExportPlatformMacOS_property_display/high_res>`{.interpreted-text
role="ref"}

If `true`, the application is rendered at native display resolution,
otherwise it is always rendered at loDPI resolution and upscaled by OS
when required.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_export/distribution_type}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**export/distribution_type**
`🔗<class_EditorExportPlatformMacOS_property_export/distribution_type>`{.interpreted-text
role="ref"}

Application distribution target.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_notarization/api_key}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**notarization/api_key**
`🔗<class_EditorExportPlatformMacOS_property_notarization/api_key>`{.interpreted-text
role="ref"}

Apple App Store Connect API issuer key file.

Can be overridden with the environment variable
`GODOT_MACOS_NOTARIZATION_API_KEY`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_notarization/api_key_id}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**notarization/api_key_id**
`🔗<class_EditorExportPlatformMacOS_property_notarization/api_key_id>`{.interpreted-text
role="ref"}

Apple App Store Connect API issuer key ID.

Can be overridden with the environment variable
`GODOT_MACOS_NOTARIZATION_API_KEY_ID`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_notarization/api_uuid}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**notarization/api_uuid**
`🔗<class_EditorExportPlatformMacOS_property_notarization/api_uuid>`{.interpreted-text
role="ref"}

Apple App Store Connect API issuer UUID.

Can be overridden with the environment variable
`GODOT_MACOS_NOTARIZATION_API_UUID`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_notarization/apple_id_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**notarization/apple_id_name**
`🔗<class_EditorExportPlatformMacOS_property_notarization/apple_id_name>`{.interpreted-text
role="ref"}

Apple ID account name (email address).

Can be overridden with the environment variable
`GODOT_MACOS_NOTARIZATION_APPLE_ID_NAME`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_notarization/apple_id_password}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**notarization/apple_id_password**
`🔗<class_EditorExportPlatformMacOS_property_notarization/apple_id_password>`{.interpreted-text
role="ref"}

Apple ID app-specific password.

Can be overridden with the environment variable
`GODOT_MACOS_NOTARIZATION_APPLE_ID_PASSWORD`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_notarization/notarization}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**notarization/notarization**
`🔗<class_EditorExportPlatformMacOS_property_notarization/notarization>`{.interpreted-text
role="ref"}

Tool to use for notarization.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/address_book_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/address_book_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/address_book_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s contacts (in
English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/address_book_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/address_book_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/address_book_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s contacts
(localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/calendar_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/calendar_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/calendar_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s calendar data
(in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/calendar_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/calendar_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/calendar_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s calendar data
(localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/camera_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/camera_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/camera_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the device\'s camera (in
English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/camera_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/camera_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/camera_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the device\'s camera
(localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/advertising_data/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects advertising data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/advertising_data/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects advertising data. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/advertising_data/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links advertising data to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/advertising_data/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/advertising_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses advertising data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/audio_data/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects audio data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/audio_data/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects audio data. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/audio_data/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links audio data to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/audio_data/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/audio_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses audio data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/browsing_history/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects browsing history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/browsing_history/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects browsing history. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/browsing_history/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links browsing history to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/browsing_history/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/browsing_history/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses browsing history for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/coarse_location/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects coarse location data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/coarse_location/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects coarse location data. See [Describing data
use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/coarse_location/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links coarse location data to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/coarse_location/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/coarse_location/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses coarse location data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/contacts/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects contacts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/contacts/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects contacts. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/contacts/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links contacts to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/contacts/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/contacts/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses contacts for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/crash_data/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects crash data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/crash_data/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects crash data. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/crash_data/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links crash data to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/crash_data/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/crash_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses crash data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/credit_info/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects credit information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/credit_info/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects credit information. See [Describing data
use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/credit_info/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links credit information to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/credit_info/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/credit_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses credit information for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/customer_support/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects customer support data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/customer_support/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects customer support data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/customer_support/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links customer support data to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/customer_support/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/customer_support/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses customer support data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/device_id/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects device IDs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/device_id/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects device IDs. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/device_id/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links device IDs to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/device_id/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/device_id/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses device IDs for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/email_address/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects email address.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/email_address/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects email address. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/email_address/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links email address to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/email_address/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/email_address/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses email address for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/emails_or_text_messages/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects emails or text messages.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/emails_or_text_messages/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects emails or text messages. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/emails_or_text_messages/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links emails or text messages to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/emails_or_text_messages/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/emails_or_text_messages/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses emails or text messages for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/environment_scanning/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects environment scanning data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/environment_scanning/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects environment scanning data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/environment_scanning/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links environment scanning data to the
user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/environment_scanning/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/environment_scanning/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses environment scanning data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/fitness/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects fitness and exercise data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/fitness/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects fitness and exercise data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/fitness/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links fitness and exercise data to the
user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/fitness/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/fitness/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses fitness and exercise data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/gameplay_content/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects gameplay content.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/gameplay_content/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects gameplay content. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/gameplay_content/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links gameplay content to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/gameplay_content/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/gameplay_content/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses gameplay content for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/hands/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects user\'s hand structure and hand
movements.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/hands/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects user\'s hand structure and hand movements.
See [Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/hands/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links user\'s hand structure and hand
movements to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/hands/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/hands/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses user\'s hand structure and hand
movements for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/head/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/head/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/head/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects user\'s head movement.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/head/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/head/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/head/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects user\'s head movement. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/head/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/head/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/head/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links user\'s head movement to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/head/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/head/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/head/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses user\'s head movement for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/health/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/health/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/health/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects health and medical data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/health/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/health/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/health/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects health and medical data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/health/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/health/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/health/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links health and medical data to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/health/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/health/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/health/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses health and medical data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/name/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/name/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/name/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects user\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/name/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/name/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/name/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects user\'s name. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/name/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/name/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/name/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links user\'s name to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/name/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/name/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/name/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses user\'s name for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_contact_info/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other contact information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_contact_info/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other contact information. See
[Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_contact_info/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other contact information to the
user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_contact_info/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_contact_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other contact information for
tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_data_types/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_data_types/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other data. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_data_types/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other data to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_data_types/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_data_types/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_diagnostic_data/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other diagnostic data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_diagnostic_data/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other diagnostic data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_diagnostic_data/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other diagnostic data to the
user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_diagnostic_data/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_diagnostic_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other diagnostic data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_financial_info/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other financial information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_financial_info/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other financial information. See
[Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_financial_info/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other financial information to the
user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_financial_info/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_financial_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other financial information for
tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_usage_data/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other usage data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_usage_data/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other usage data. See [Describing data
use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_usage_data/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other usage data to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_usage_data/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_usage_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other usage data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_user_content/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects any other user generated content.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/other_user_content/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects any other user generated content. See
[Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_user_content/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links any other user generated content to the
user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/other_user_content/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/other_user_content/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses any other user generated content for
tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/payment_info/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects payment information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/payment_info/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects payment information. See [Describing data
use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/payment_info/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links payment information to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/payment_info/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/payment_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses payment information for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/performance_data/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects performance data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/performance_data/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects performance data. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/performance_data/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links performance data to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/performance_data/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/performance_data/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses performance data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/phone_number/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects phone number.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/phone_number/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects phone number. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/phone_number/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links phone number to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/phone_number/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/phone_number/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses phone number for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/photos_or_videos/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects photos or videos.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/photos_or_videos/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects photos or videos. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/photos_or_videos/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links photos or videos to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/photos_or_videos/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/photos_or_videos/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses photos or videos for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/physical_address/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects physical address.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/physical_address/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects physical address. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/physical_address/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links physical address to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/physical_address/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/physical_address/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses physical address for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/precise_location/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects precise location data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/precise_location/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects precise location data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/precise_location/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links precise location data to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/precise_location/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/precise_location/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses precise location data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/product_interaction/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects product interaction data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/product_interaction/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects product interaction data. See [Describing
data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/product_interaction/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links product interaction data to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/product_interaction/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/product_interaction/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses product interaction data for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/purchase_history/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects purchase history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/purchase_history/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects purchase history. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/purchase_history/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links purchase history to the user\'s
identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/purchase_history/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/purchase_history/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses purchase history for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/search_hhistory/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/search_hhistory/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/search_hhistory/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects search history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/search_hhistory/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/search_hhistory/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/search_hhistory/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects search history. See [Describing data use
in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/search_hhistory/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/search_hhistory/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/search_hhistory/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links search history to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/search_hhistory/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/search_hhistory/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/search_hhistory/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses search history for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/sensitive_info/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects sensitive user information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/sensitive_info/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects sensitive user information. See
[Describing data use in privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/sensitive_info/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links sensitive user information to the
user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/sensitive_info/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/sensitive_info/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses sensitive user information for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/collected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/user_id/collected**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/collected>`{.interpreted-text
role="ref"}

Indicates whether your app collects user IDs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/collection_purposes}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**privacy/collected_data/user_id/collection_purposes**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/collection_purposes>`{.interpreted-text
role="ref"}

The reasons your app collects user IDs. See [Describing data use in
privacy
manifests](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/linked_to_user}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/user_id/linked_to_user**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/linked_to_user>`{.interpreted-text
role="ref"}

Indicates whether your app links user IDs to the user\'s identity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/used_for_tracking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/collected_data/user_id/used_for_tracking**
`🔗<class_EditorExportPlatformMacOS_property_privacy/collected_data/user_id/used_for_tracking>`{.interpreted-text
role="ref"}

Indicates whether your app uses user IDs for tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/desktop_folder_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/desktop_folder_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/desktop_folder_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s \"Desktop\"
folder (in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/desktop_folder_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/desktop_folder_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/desktop_folder_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s \"Desktop\"
folder (localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/documents_folder_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/documents_folder_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/documents_folder_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s \"Documents\"
folder (in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/documents_folder_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/documents_folder_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/documents_folder_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s \"Documents\"
folder (localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/downloads_folder_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/downloads_folder_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/downloads_folder_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s \"Downloads\"
folder (in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/downloads_folder_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/downloads_folder_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/downloads_folder_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s \"Downloads\"
folder (localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/location_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/location_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/location_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s location
information (in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/location_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/location_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/location_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s location
information (localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/microphone_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/microphone_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/microphone_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the device\'s microphone
(in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/microphone_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/microphone_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/microphone_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the device\'s microphone
(localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/network_volumes_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/network_volumes_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/network_volumes_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s network drives
(in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/network_volumes_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/network_volumes_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/network_volumes_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s network drives
(localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/photos_library_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/photos_library_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/photos_library_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s photo library
(in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/photos_library_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/photos_library_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/photos_library_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s photo library
(localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/removable_volumes_usage_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**privacy/removable_volumes_usage_description**
`🔗<class_EditorExportPlatformMacOS_property_privacy/removable_volumes_usage_description>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s removable
drives (in English).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/removable_volumes_usage_description_localized}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**privacy/removable_volumes_usage_description_localized**
`🔗<class_EditorExportPlatformMacOS_property_privacy/removable_volumes_usage_description_localized>`{.interpreted-text
role="ref"}

A message displayed when requesting access to the user\'s removable
drives (localized).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/tracking_domains}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **privacy/tracking_domains**
`🔗<class_EditorExportPlatformMacOS_property_privacy/tracking_domains>`{.interpreted-text
role="ref"}

The list of internet domains your app connects to that engage in
tracking. See [Privacy manifest
files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_privacy/tracking_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**privacy/tracking_enabled**
`🔗<class_EditorExportPlatformMacOS_property_privacy/tracking_enabled>`{.interpreted-text
role="ref"}

Indicates whether your app uses data for tracking. See [Privacy manifest
files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_shader_baker/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shader_baker/enabled**
`🔗<class_EditorExportPlatformMacOS_property_shader_baker/enabled>`{.interpreted-text
role="ref"}

If `true`, shaders will be compiled and embedded in the application.
This option is only supported when using the Forward+ or Mobile
renderers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_ssh_remote_deploy/cleanup_script}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/cleanup_script**
`🔗<class_EditorExportPlatformMacOS_property_ssh_remote_deploy/cleanup_script>`{.interpreted-text
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

:::: {#class_EditorExportPlatformMacOS_property_ssh_remote_deploy/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**ssh_remote_deploy/enabled**
`🔗<class_EditorExportPlatformMacOS_property_ssh_remote_deploy/enabled>`{.interpreted-text
role="ref"}

Enables remote deploy using SSH/SCP.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_ssh_remote_deploy/extra_args_scp}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/extra_args_scp**
`🔗<class_EditorExportPlatformMacOS_property_ssh_remote_deploy/extra_args_scp>`{.interpreted-text
role="ref"}

Array of the additional command line arguments passed to the SCP.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_ssh_remote_deploy/extra_args_ssh}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/extra_args_ssh**
`🔗<class_EditorExportPlatformMacOS_property_ssh_remote_deploy/extra_args_ssh>`{.interpreted-text
role="ref"}

Array of the additional command line arguments passed to the SSH.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_ssh_remote_deploy/host}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/host**
`🔗<class_EditorExportPlatformMacOS_property_ssh_remote_deploy/host>`{.interpreted-text
role="ref"}

Remote host SSH user name and address, in `user@address` format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_ssh_remote_deploy/port}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/port**
`🔗<class_EditorExportPlatformMacOS_property_ssh_remote_deploy/port>`{.interpreted-text
role="ref"}

Remote host SSH port number.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_ssh_remote_deploy/run_script}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**ssh_remote_deploy/run_script**
`🔗<class_EditorExportPlatformMacOS_property_ssh_remote_deploy/run_script>`{.interpreted-text
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

:::: {#class_EditorExportPlatformMacOS_property_xcode/platform_build}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**xcode/platform_build**
`🔗<class_EditorExportPlatformMacOS_property_xcode/platform_build>`{.interpreted-text
role="ref"}

macOS build number used to build application executable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_xcode/sdk_build}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **xcode/sdk_build**
`🔗<class_EditorExportPlatformMacOS_property_xcode/sdk_build>`{.interpreted-text
role="ref"}

macOS SDK build number used to build application executable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_xcode/sdk_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **xcode/sdk_name**
`🔗<class_EditorExportPlatformMacOS_property_xcode/sdk_name>`{.interpreted-text
role="ref"}

macOS SDK name used to build application executable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_xcode/sdk_version}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**xcode/sdk_version**
`🔗<class_EditorExportPlatformMacOS_property_xcode/sdk_version>`{.interpreted-text
role="ref"}

macOS SDK version used to build application executable in the
`major.minor` format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_xcode/xcode_build}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**xcode/xcode_build**
`🔗<class_EditorExportPlatformMacOS_property_xcode/xcode_build>`{.interpreted-text
role="ref"}

Xcode build number used to build application executable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformMacOS_property_xcode/xcode_version}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**xcode/xcode_version**
`🔗<class_EditorExportPlatformMacOS_property_xcode/xcode_version>`{.interpreted-text
role="ref"}

Xcode version used to build application executable.
