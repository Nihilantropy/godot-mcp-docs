# Exporting for macOS {#doc_exporting_for_macos}

::: seealso
This page describes how to export a Godot project to macOS. If you\'re
looking to compile editor or export template binaries from source
instead, read `doc_compiling_for_macos`{.interpreted-text role="ref"}.
:::

macOS apps exported with the official export templates are exported as a
single \"Universal 2\" binary `.app` bundle, a folder with a specific
structure which stores the executable, libraries and all the project
files. This bundle can be exported as is, packed in a ZIP archive, or
packed in a DMG disk image (only supported when exporting from macOS).
[Universal binaries for macOS support both Intel x86_64 and ARM64 (Apple
Silicon)
architectures](https://developer.apple.com/documentation/apple-silicon/building-a-universal-macos-binary).

:::: warning
::: title
Warning
:::

Due to file system limitations, `.app` bundles exported from Windows
lack the `executable` flag and won\'t run on macOS. Projects exported as
`.zip` are not affected by this issue. To run `.app` bundles exported
from Windows on macOS, transfer the `.app` to a device running macOS or
Linux and use the `chmod +x {executable_name}` terminal command to add
the `executable` permission. The main executable located in the
`Contents/MacOS/` subfolder, as well as optional helper executables in
the `Contents/Helpers/` subfolder, should have the `executable`
permission for the `.app` bundle to be valid.
::::

## Requirements

- Download the Godot export templates. Use the Godot menu:
  `Editor > Manage Export Templates`.
- A valid and unique `Bundle identifier` should be set in the
  `Application` section of the export options.

:::: warning
::: title
Warning
:::

Projects exported without code signing and notarization will be blocked
by Gatekeeper if they are downloaded from unknown sources, see the
`Running Godot apps on macOS <doc_running_on_macos>`{.interpreted-text
role="ref"} page for more information.
::::

## Code signing and notarization

By default, macOS will run only applications that are signed and
notarized. If you use any other signing configuration, see
`Running Godot apps on macOS <doc_running_on_macos>`{.interpreted-text
role="ref"} for workarounds.

To notarize an app, you **must** have a valid [Apple Developer ID
Certificate](https://developer.apple.com/).

### If you have an Apple Developer ID Certificate and exporting from macOS

Install [Xcode](https://developer.apple.com/xcode/) command line tools
and open Xcode at least once or run the
`sudo xcodebuild -license accept` command to accept license agreement.

#### To sign exported app

- Select `Xcode codesign` in the `Code Signing > Codesign` option.
- Set valid Apple ID certificate identity (certificate \"Common Name\")
  in the `Code Signing > Identity` section.

#### To notarize exported app

- Select `Xcode altool` in the `Notarization > Notarization` option.
- Disable the `Debugging` entitlement.
- Set valid Apple ID login / app. specific password or [App Store
  Connect](https://developer.apple.com/documentation/appstoreconnectapi)
  API UUID / Key in the `Notarization` section.

You can use the `xcrun notarytool history` command to check notarization
status and use the `xcrun notarytool log {ID}` command to download the
notarization log.

If you encounter notarization issues, see [Resolving common notarization
issues](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/resolving_common_notarization_issues)
for more info.

After notarization is completed, [staple the
ticket](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution/customizing_the_notarization_workflow)
to the exported project.

### If you have an Apple Developer ID Certificate and exporting from Linux or Windows

Install [PyOxidizer
rcodesign](https://github.com/indygreg/apple-platform-rs/tree/main/apple-codesign),
and configure the path to `rcodesign` in the
`Editor Settings > Export > macOS > rcodesign`.

#### To sign exported app

- Select `PyOxidizer rcodesign` in the `Code Signing > Codesign` option.
- Set valid Apple ID PKCS #12 certificate file and password in the
  `Code Signing` section.

#### To notarize exported app

- Select `PyOxidizer rcodesign` in the `Notarization > Notarization`
  option.
- Disable the `Debugging` entitlement.
- Set valid [App Store
  Connect](https://developer.apple.com/documentation/appstoreconnectapi)
  API UUID / Key in the `Notarization` section.

You can use the `rcodesign notary-log` command to check notarization
status.

After notarization is completed, use the `rcodesign staple` command to
staple the ticket to the exported project.

### If you do not have an Apple Developer ID Certificate

- Select `Built-in (ad-hoc only)` in the `Code Signing > Codesign`
  option.
- Select `Disabled` in the `Notarization > Notarization` option.

In this case Godot will use an ad-hoc signature, which will make running
an exported app easier for the end users, see the
`Running Godot apps on macOS <doc_running_on_macos>`{.interpreted-text
role="ref"} page for more information.

### Signing Options

  -----------------------------------------------------------------------
  Option           Description
  ---------------- ------------------------------------------------------
  Codesign         Tool to use for code signing.

  Identity         The \"Full Name\" or \"Common Name\" of the signing
                   identity, store in the macOS keychain.[^1]

  Certificate File The PKCS #12 certificate file.[^2]

  Certificate      Password for the certificate file.[^3]
  Password         

  Custom Options   Array of command line arguments passed to the code
                   signing tool.
  -----------------------------------------------------------------------

### Notarization Options

  ---------------------------------------------------------------------------------------
  Option         Description
  -------------- ------------------------------------------------------------------------
  Notarization   Tool to use for notarization.

  Apple ID Name  Apple ID account name (email address).[^4]

  Apple ID       Apple ID app-specific password. See [Using app-specific
  Password       passwords](https://support.apple.com/en-us/HT204397) to enable
                 two-factor authentication and create app password.[^5]

  Apple Team ID  Team ID (\"Organization Unit\"), if your Apple ID belongs to multiple
                 teams (optional).[^6]

  API UUID       Apple [App Store
                 Connect](https://developer.apple.com/documentation/appstoreconnectapi)
                 API issuer UUID.

  API Key        Apple [App Store
                 Connect](https://developer.apple.com/documentation/appstoreconnectapi)
                 API key.
  ---------------------------------------------------------------------------------------

:::: note
::: title
Note
:::

You should set either Apple ID Name/Password or App Store Connect API
UUID/Key.
::::

See [Notarizing macOS Software Before
Distribution](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution?language=objc)
for more info.

## Entitlements

### Hardened Runtime Entitlements

Hardened Runtime entitlements manage security options and resource
access policy. See [Hardened
Runtime](https://developer.apple.com/documentation/security/hardened_runtime?language=objc)
for more info.

  --------------------------------------------------------------------------
  Entitlement     Description
  --------------- ----------------------------------------------------------
  Allow JIT Code  Allows creating writable and executable memory for JIT
  Execution[^7]   code. If you are using add-ons with dynamic or
                  self-modifying native code, enable them according to the
                  add-on documentation.

  Allow Unsigned  Allows creating writable and executable memory without JIT
  Executable      restrictions. If you are using add-ons with dynamic or
  Memory[^8]      self-modifying native code, enable them according to the
                  add-on documentation.

  Allow DYLD      Allows app to uss dynamic linker environment variables to
  Environment     inject code. If you are using add-ons with dynamic or
  Variables[^9]   self-modifying native code, enable them according to the
                  add-on documentation.

  Disable Library Allows app to load arbitrary libraries and frameworks.
  Validation      Enable it if you are using GDExtension add-ons or ad-hoc
                  signing, or want to support user-provided external
                  add-ons.

  Audio Input     Enable if you need to use the microphone or other audio
                  input sources, if it\'s enabled you should also provide
                  usage message in the
                  [privacy/microphone_usage_description]{.title-ref} option.

  Camera          Enable if you need to use the camera, if it\'s enabled you
                  should also provide usage message in the
                  [privacy/camera_usage_description]{.title-ref} option.

  Location        Enable if you need to use location information from
                  Location Services, if it\'s enabled you should also
                  provide usage message in the
                  [privacy/location_usage_description]{.title-ref} option.

  Address Book    [^10] Enable to allow access contacts in the user\'s
                  address book, if it\'s enabled you should also provide
                  usage message in the
                  [privacy/address_book_usage_description]{.title-ref}
                  option.

  Calendars       [^11] Enable to allow access to the user\'s calendar, if
                  it\'s enabled you should also provide usage message in the
                  [privacy/calendar_usage_description]{.title-ref} option.

  Photo Library   [^12] Enable to allow access to the user\'s Photos
                  library, if it\'s enabled you should also provide usage
                  message in the
                  [privacy/photos_library_usage_description]{.title-ref}
                  option.

  Apple Events    [^13] Enable to allow app to send Apple events to other
                  apps.

  Debugging       [^14] You can temporarily enable this entitlement to use
                  native debugger (GDB, LLDB) with the exported app. This
                  entitlement should be disabled for production export.
  --------------------------------------------------------------------------

### App Sandbox Entitlement

The App Sandbox restricts access to user data, networking and devices.
Sandboxed apps can\'t access most of the file system, can\'t use custom
file dialogs and execute binaries (using `OS.execute` and
`OS.create_process`) outside the `.app` bundle. See [App
Sandbox](https://developer.apple.com/documentation/security/app_sandbox?language=objc)
for more info.

:::: note
::: title
Note
:::

To distribute an app through the App Store, you must enable the App
Sandbox.
::::

  -------------------------------------------------------------------------
  Entitlement      Description
  ---------------- --------------------------------------------------------
  Enabled          Enables App Sandbox.

  Network Server   Enable to allow app to listen for incoming network
                   connections.

  Network Client   Enable to allow app to establish outgoing network
                   connections.

  Device USB       Enable to allow app to interact with USB devices. This
                   entitlement is required to use wired controllers.

  Device Bluetooth Enable to allow app to interact with Bluetooth devices.
                   This entitlement is required to use wireless
                   controllers.

  Files            Allows read or write access to the user\'s \"Downloads\"
  Downloads[^15]   folder.

  Files            Allows read or write access to the user\'s \"Pictures\"
  Pictures[^16]    folder.

  Files Music[^17] Allows read or write access to the user\'s \"Music\"
                   folder.

  Files            Allows read or write access to the user\'s \"Movies\"
  Movies[^18]      folder.

  Files User       Allows read or write access to arbitrary folder. To gain
  Selected[^19]    access, a folder must be selected from the native file
                   dialog by the user.

  Helper           List of helper executables to embedded to the app
  Executable       bundle. Sandboxed app are limited to execute only these
                   executable.
  -------------------------------------------------------------------------

:::: note
::: title
Note
:::

You can override default entitlements by selecting custom entitlements
file, in this case all other entitlement are ignored.
::::

## Environment variables

You can use the following environment variables to set export options
outside of the editor. During the export process, these override the
values that you set in the export menu.

  Export option                                Environment variable
  -------------------------------------------- ----------------------------------------------
  Encryption / Encryption Key                  `GODOT_SCRIPT_ENCRYPTION_KEY`
  Options / Codesign / Certificate File        `GODOT_MACOS_CODESIGN_CERTIFICATE_FILE`
  Options / Codesign / Certificate Password    `GODOT_MACOS_CODESIGN_CERTIFICATE_PASSWORD`
  Options / Codesign / Provisioning Profile    `GODOT_MACOS_CODESIGN_PROVISIONING_PROFILE`
  Options / Notarization / API UUID            `GODOT_MACOS_NOTARIZATION_API_UUID`
  Options / Notarization / API Key             `GODOT_MACOS_NOTARIZATION_API_KEY`
  Options / Notarization / API Key ID          `GODOT_MACOS_NOTARIZATION_API_KEY_ID`
  Options / Notarization / Apple ID Name       `GODOT_MACOS_NOTARIZATION_APPLE_ID_NAME`
  Options / Notarization / Apple ID Password   `GODOT_MACOS_NOTARIZATION_APPLE_ID_PASSWORD`

  : macOS export environment variables

## Export options

You can find a full list of export options available in the
`class_EditorExportPlatformMacOS`{.interpreted-text role="ref"} class
reference.

[^1]: This option is visible only when signing with Xcode codesign.

[^2]: These options are visible only when signing with PyOxidizer
    rcodesign.

[^3]: These options are visible only when signing with PyOxidizer
    rcodesign.

[^4]: These options are visible only when notarizing with Xcode altool.

[^5]: These options are visible only when notarizing with Xcode altool.

[^6]: These options are visible only when notarizing with Xcode altool.

[^7]: The `Allow JIT Code Execution`, `Allow Unsigned Executable Memory`
    and `Allow DYLD Environment Variables` entitlements are always
    enabled for the Godot Mono exports, and are not visible in the
    export options.

[^8]: The `Allow JIT Code Execution`, `Allow Unsigned Executable Memory`
    and `Allow DYLD Environment Variables` entitlements are always
    enabled for the Godot Mono exports, and are not visible in the
    export options.

[^9]: The `Allow JIT Code Execution`, `Allow Unsigned Executable Memory`
    and `Allow DYLD Environment Variables` entitlements are always
    enabled for the Godot Mono exports, and are not visible in the
    export options.

[^10]: These features aren\'t supported by Godot out of the box, enable
    them only if you are using add-ons which require them.

[^11]: These features aren\'t supported by Godot out of the box, enable
    them only if you are using add-ons which require them.

[^12]: These features aren\'t supported by Godot out of the box, enable
    them only if you are using add-ons which require them.

[^13]: These features aren\'t supported by Godot out of the box, enable
    them only if you are using add-ons which require them.

[^14]: To notarize an app, you must disable the `Debugging` entitlement.

[^15]: You can optionally provide usage messages for various folders in
    the [privacy/\*\_folder_usage_description]{.title-ref} options.

[^16]: You can optionally provide usage messages for various folders in
    the [privacy/\*\_folder_usage_description]{.title-ref} options.

[^17]: You can optionally provide usage messages for various folders in
    the [privacy/\*\_folder_usage_description]{.title-ref} options.

[^18]: You can optionally provide usage messages for various folders in
    the [privacy/\*\_folder_usage_description]{.title-ref} options.

[^19]: You can optionally provide usage messages for various folders in
    the [privacy/\*\_folder_usage_description]{.title-ref} options.
