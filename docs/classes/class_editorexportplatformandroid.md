github_url
:   hide

# EditorExportPlatformAndroid {#class_EditorExportPlatformAndroid}

**Inherits:**
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Exporter for Android.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Exporting for Android <../tutorials/export/exporting_for_android>`{.interpreted-text
  role="doc"}
- `Gradle builds for Android <../tutorials/export/android_gradle_build>`{.interpreted-text
  role="doc"}
- `Android plugins documentation index <../tutorials/platform/index>`{.interpreted-text
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

:::: {#class_EditorExportPlatformAndroid_property_apk_expansion/SALT}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**apk_expansion/SALT**
`🔗<class_EditorExportPlatformAndroid_property_apk_expansion/SALT>`{.interpreted-text
role="ref"}

Array of random bytes that the licensing Policy uses to create an
[Obfuscator](https://developer.android.com/google/play/licensing/adding-licensing#impl-Obfuscator).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_apk_expansion/enable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**apk_expansion/enable**
`🔗<class_EditorExportPlatformAndroid_property_apk_expansion/enable>`{.interpreted-text
role="ref"}

If `true`, project resources are stored in the separate APK expansion
file, instead of the APK.

\*\*Note:\*\* APK expansion should be enabled to use PCK encryption. See
[APK Expansion
Files](https://developer.android.com/google/play/expansion-files)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_apk_expansion/public_key}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**apk_expansion/public_key**
`🔗<class_EditorExportPlatformAndroid_property_apk_expansion/public_key>`{.interpreted-text
role="ref"}

Base64 encoded RSA public key for your publisher account, available from
the profile page on the \"Google Play Console\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_architectures/arm64-v8a}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**architectures/arm64-v8a**
`🔗<class_EditorExportPlatformAndroid_property_architectures/arm64-v8a>`{.interpreted-text
role="ref"}

If `true`, `arm64` binaries are included into exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_architectures/armeabi-v7a}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**architectures/armeabi-v7a**
`🔗<class_EditorExportPlatformAndroid_property_architectures/armeabi-v7a>`{.interpreted-text
role="ref"}

If `true`, `arm32` binaries are included into exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_architectures/x86}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **architectures/x86**
`🔗<class_EditorExportPlatformAndroid_property_architectures/x86>`{.interpreted-text
role="ref"}

If `true`, `x86_32` binaries are included into exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_architectures/x86_64}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**architectures/x86_64**
`🔗<class_EditorExportPlatformAndroid_property_architectures/x86_64>`{.interpreted-text
role="ref"}

If `true`, `x86_64` binaries are included into exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_command_line/extra_args}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**command_line/extra_args**
`🔗<class_EditorExportPlatformAndroid_property_command_line/extra_args>`{.interpreted-text
role="ref"}

A list of additional command line arguments, separated by space, which
the exported project will receive when started.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_custom_template/debug}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/debug**
`🔗<class_EditorExportPlatformAndroid_property_custom_template/debug>`{.interpreted-text
role="ref"}

Path to an APK file to use as a custom export template for debug
exports. If left empty, default template is used.

\*\*Note:\*\* This is only used if
`gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"} is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_custom_template/release}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/release**
`🔗<class_EditorExportPlatformAndroid_property_custom_template/release>`{.interpreted-text
role="ref"}

Path to an APK file to use as a custom export template for release
exports. If left empty, default template is used.

\*\*Note:\*\* This is only used if
`gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"} is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_gesture/swipe_to_dismiss}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gesture/swipe_to_dismiss**
`🔗<class_EditorExportPlatformAndroid_property_gesture/swipe_to_dismiss>`{.interpreted-text
role="ref"}

If `true`, [Swipe to
dismiss](https://developer.android.com/design/ui/wear/guides/components/swipe-to-dismiss)
will be enabled.

This functionality is intended for smartwatches and is generally ignored
on standard Android devices. However, some devices may not ignore it.
Therefore, it is recommended to keep this feature disabled for standard
Android apps to avoid unexpected behavior.

\*\*Note:\*\* This is `false` by default. To enable this behavior,
`gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"} is required.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_gradle_build/android_source_template}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**gradle_build/android_source_template**
`🔗<class_EditorExportPlatformAndroid_property_gradle_build/android_source_template>`{.interpreted-text
role="ref"}

Path to a ZIP file holding the source for the export template used in a
Gradle build. If left empty, the default template is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_gradle_build/custom_theme_attributes}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**gradle_build/custom_theme_attributes**
`🔗<class_EditorExportPlatformAndroid_property_gradle_build/custom_theme_attributes>`{.interpreted-text
role="ref"}

A dictionary of custom theme attributes to include in the exported
Android project. Each entry defines a theme attribute name and its
value, and will be added to the **GodotAppMainTheme**.

For example, the key `android:windowSwipeToDismiss` with the value
`false` is resolved to
`<item name="android:windowSwipeToDismiss">false</item>`.

\*\*Note:\*\* To add a custom attribute to the **GodotAppSplashTheme**,
prefix the attribute name with `[splash]`.

\*\*Note:\*\* Reserved attributes configured via other export options or
project settings cannot be overridden by `custom_theme_attributes` and
are skipped during export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_gradle_build/export_format}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**gradle_build/export_format**
`🔗<class_EditorExportPlatformAndroid_property_gradle_build/export_format>`{.interpreted-text
role="ref"}

Application export format (\*.apk or \*.aab).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_gradle_build/gradle_build_directory}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**gradle_build/gradle_build_directory**
`🔗<class_EditorExportPlatformAndroid_property_gradle_build/gradle_build_directory>`{.interpreted-text
role="ref"}

Path to the Gradle build directory. If left empty, then `res://android`
will be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_gradle_build/min_sdk}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**gradle_build/min_sdk**
`🔗<class_EditorExportPlatformAndroid_property_gradle_build/min_sdk>`{.interpreted-text
role="ref"}

Minimum Android API level required for the application to run (used
during Gradle build). See
[android:minSdkVersion](https://developer.android.com/guide/topics/manifest/uses-sdk-element#uses).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_gradle_build/target_sdk}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**gradle_build/target_sdk**
`🔗<class_EditorExportPlatformAndroid_property_gradle_build/target_sdk>`{.interpreted-text
role="ref"}

The Android API level on which the application is designed to run (used
during Gradle build). See
[android:targetSdkVersion](https://developer.android.com/guide/topics/manifest/uses-sdk-element#uses).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gradle_build/use_gradle_build**
`🔗<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"}

If `true`, Gradle build is used instead of pre-built APK.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_graphics/opengl_debug}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**graphics/opengl_debug**
`🔗<class_EditorExportPlatformAndroid_property_graphics/opengl_debug>`{.interpreted-text
role="ref"}

If `true`, OpenGL ES debug context will be created (additional runtime
checking, validation, and logging).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_keystore/debug}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **keystore/debug**
`🔗<class_EditorExportPlatformAndroid_property_keystore/debug>`{.interpreted-text
role="ref"}

Path of the debug keystore file.

Can be overridden with the environment variable
`GODOT_ANDROID_KEYSTORE_DEBUG_PATH`.

Fallbacks to `EditorSettings.export/android/debug_keystore` if empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_keystore/debug_password}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**keystore/debug_password**
`🔗<class_EditorExportPlatformAndroid_property_keystore/debug_password>`{.interpreted-text
role="ref"}

Password for the debug keystore file.

Can be overridden with the environment variable
`GODOT_ANDROID_KEYSTORE_DEBUG_PASSWORD`.

Fallbacks to `EditorSettings.export/android/debug_keystore_pass` if both
it and
`keystore/debug<class_EditorExportPlatformAndroid_property_keystore/debug>`{.interpreted-text
role="ref"} are empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_keystore/debug_user}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**keystore/debug_user**
`🔗<class_EditorExportPlatformAndroid_property_keystore/debug_user>`{.interpreted-text
role="ref"}

User name for the debug keystore file.

Can be overridden with the environment variable
`GODOT_ANDROID_KEYSTORE_DEBUG_USER`.

Fallbacks to `EditorSettings.export/android/debug_keystore_user` if both
it and
`keystore/debug<class_EditorExportPlatformAndroid_property_keystore/debug>`{.interpreted-text
role="ref"} are empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_keystore/release}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**keystore/release**
`🔗<class_EditorExportPlatformAndroid_property_keystore/release>`{.interpreted-text
role="ref"}

Path of the release keystore file.

Can be overridden with the environment variable
`GODOT_ANDROID_KEYSTORE_RELEASE_PATH`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_keystore/release_password}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**keystore/release_password**
`🔗<class_EditorExportPlatformAndroid_property_keystore/release_password>`{.interpreted-text
role="ref"}

Password for the release keystore file.

Can be overridden with the environment variable
`GODOT_ANDROID_KEYSTORE_RELEASE_PASSWORD`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_keystore/release_user}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**keystore/release_user**
`🔗<class_EditorExportPlatformAndroid_property_keystore/release_user>`{.interpreted-text
role="ref"}

User name for the release keystore file.

Can be overridden with the environment variable
`GODOT_ANDROID_KEYSTORE_RELEASE_USER`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_background_432x432}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**launcher_icons/adaptive_background_432x432**
`🔗<class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_background_432x432>`{.interpreted-text
role="ref"}

Background layer of the application adaptive icon file. See [Design
adaptive
icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_foreground_432x432}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**launcher_icons/adaptive_foreground_432x432**
`🔗<class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_foreground_432x432>`{.interpreted-text
role="ref"}

Foreground layer of the application adaptive icon file. See [Design
adaptive
icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_monochrome_432x432}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**launcher_icons/adaptive_monochrome_432x432**
`🔗<class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_monochrome_432x432>`{.interpreted-text
role="ref"}

Monochrome layer of the application adaptive icon file. See [Design
adaptive
icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_launcher_icons/main_192x192}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**launcher_icons/main_192x192**
`🔗<class_EditorExportPlatformAndroid_property_launcher_icons/main_192x192>`{.interpreted-text
role="ref"}

Application icon file. If left empty, it will fallback to
`ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_package/app_category}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **package/app_category**
`🔗<class_EditorExportPlatformAndroid_property_package/app_category>`{.interpreted-text
role="ref"}

Application category for the Google Play Store. Only define this if your
application fits one of the categories well. See
[android:appCategory](https://developer.android.com/guide/topics/manifest/application-element#appCategory).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_package/exclude_from_recents}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**package/exclude_from_recents**
`🔗<class_EditorExportPlatformAndroid_property_package/exclude_from_recents>`{.interpreted-text
role="ref"}

If `true`, task initiated by main activity will be excluded from the
list of recently used applications. See
[android:excludeFromRecents](https://developer.android.com/guide/topics/manifest/activity-element#exclude).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_package/name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **package/name**
`🔗<class_EditorExportPlatformAndroid_property_package/name>`{.interpreted-text
role="ref"}

Name of the application.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_package/retain_data_on_uninstall}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**package/retain_data_on_uninstall**
`🔗<class_EditorExportPlatformAndroid_property_package/retain_data_on_uninstall>`{.interpreted-text
role="ref"}

If `true`, when the user uninstalls an app, a prompt to keep the app\'s
data will be shown. See
[android:hasFragileUserData](https://developer.android.com/guide/topics/manifest/application-element#fragileuserdata).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_package/show_as_launcher_app}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**package/show_as_launcher_app**
`🔗<class_EditorExportPlatformAndroid_property_package/show_as_launcher_app>`{.interpreted-text
role="ref"}

If `true`, the user will be able to set this app as the system launcher
in Android preferences.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_package/show_in_android_tv}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**package/show_in_android_tv**
`🔗<class_EditorExportPlatformAndroid_property_package/show_in_android_tv>`{.interpreted-text
role="ref"}

If `true`, this app will show in Android TV launcher UI.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_package/show_in_app_library}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**package/show_in_app_library**
`🔗<class_EditorExportPlatformAndroid_property_package/show_in_app_library>`{.interpreted-text
role="ref"}

If `true`, this app will show in the device\'s app library.

\*\*Note:\*\* This is `true` by default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_package/signed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **package/signed**
`🔗<class_EditorExportPlatformAndroid_property_package/signed>`{.interpreted-text
role="ref"}

If `true`, package signing is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_package/unique_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**package/unique_name**
`🔗<class_EditorExportPlatformAndroid_property_package/unique_name>`{.interpreted-text
role="ref"}

Unique application identifier in a reverse-DNS format. The reverse DNS
format should preferably match a domain name you control, but this is
not strictly required. For instance, if you own `example.com`, your
package unique name should preferably be of the form
`com.example.mygame`. This identifier can only contain lowercase
alphanumeric characters (`a-z`, and `0-9`), underscores (`_`), and
periods (`.`). Each component of the reverse DNS format must start with
a letter: for instance, `com.example.8game` is not valid.

If `$genname` is present in the value, it will be replaced by the
project name converted to lowercase. If there are invalid characters in
the project name, they will be stripped. If all characters in the
project name are stripped, `$genname` is replaced by `noname`.

\*\*Note:\*\* Changing the package name will cause the package to be
considered as a new package, with its own installation and data paths.
The new package won\'t be usable to update existing installations.

\*\*Note:\*\* When publishing to Google Play, the package name must be
*globally* unique. This means no other apps published on Google Play
must be using the same package name as yours. Otherwise, you\'ll be
prevented from publishing your app on Google Play.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/access_checkin_properties}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/access_checkin_properties**
`🔗<class_EditorExportPlatformAndroid_property_permissions/access_checkin_properties>`{.interpreted-text
role="ref"}

Allows read/write access to the \"properties\" table in the checkin
database. See
[ACCESS_CHECKIN_PROPERTIES](https://developer.android.com/reference/android/Manifest.permission#ACCESS_CHECKIN_PROPERTIES).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/access_coarse_location}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/access_coarse_location**
`🔗<class_EditorExportPlatformAndroid_property_permissions/access_coarse_location>`{.interpreted-text
role="ref"}

Allows access to the approximate location information. See
[ACCESS_COARSE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/access_fine_location}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/access_fine_location**
`🔗<class_EditorExportPlatformAndroid_property_permissions/access_fine_location>`{.interpreted-text
role="ref"}

Allows access to the precise location information. See
[ACCESS_FINE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/access_location_extra_commands}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/access_location_extra_commands**
`🔗<class_EditorExportPlatformAndroid_property_permissions/access_location_extra_commands>`{.interpreted-text
role="ref"}

Allows access to the extra location provider commands. See
[ACCESS_LOCATION_EXTRA_COMMANDS](https://developer.android.com/reference/android/Manifest.permission#ACCESS_LOCATION_EXTRA_COMMANDS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/access_media_location}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/access_media_location**
`🔗<class_EditorExportPlatformAndroid_property_permissions/access_media_location>`{.interpreted-text
role="ref"}

Allows an application to access any geographic locations persisted in
the user\'s shared collection. See
[ACCESS_MEDIA_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_MEDIA_LOCATION).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/access_mock_location}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/access_mock_location**
`🔗<class_EditorExportPlatformAndroid_property_permissions/access_mock_location>`{.interpreted-text
role="ref"}

Allows an application to create mock location providers for testing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/access_network_state}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/access_network_state**
`🔗<class_EditorExportPlatformAndroid_property_permissions/access_network_state>`{.interpreted-text
role="ref"}

Allows access to the information about networks. See
[ACCESS_NETWORK_STATE](https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/access_surface_flinger}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/access_surface_flinger**
`🔗<class_EditorExportPlatformAndroid_property_permissions/access_surface_flinger>`{.interpreted-text
role="ref"}

Allows an application to use SurfaceFlinger\'s low level features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/access_wifi_state}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/access_wifi_state**
`🔗<class_EditorExportPlatformAndroid_property_permissions/access_wifi_state>`{.interpreted-text
role="ref"}

Allows access to the information about Wi-Fi networks. See
[ACCESS_WIFI_STATE](https://developer.android.com/reference/android/Manifest.permission#ACCESS_WIFI_STATE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/account_manager}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/account_manager**
`🔗<class_EditorExportPlatformAndroid_property_permissions/account_manager>`{.interpreted-text
role="ref"}

Allows applications to call into AccountAuthenticators. See
[ACCOUNT_MANAGER](https://developer.android.com/reference/android/Manifest.permission#ACCOUNT_MANAGER).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/add_voicemail}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/add_voicemail**
`🔗<class_EditorExportPlatformAndroid_property_permissions/add_voicemail>`{.interpreted-text
role="ref"}

Allows an application to add voicemails into the system. See
[ADD_VOICEMAIL](https://developer.android.com/reference/android/Manifest.permission#ADD_VOICEMAIL).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/authenticate_accounts}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/authenticate_accounts**
`🔗<class_EditorExportPlatformAndroid_property_permissions/authenticate_accounts>`{.interpreted-text
role="ref"}

Allows an application to act as an AccountAuthenticator for the
AccountManager.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/battery_stats}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/battery_stats**
`🔗<class_EditorExportPlatformAndroid_property_permissions/battery_stats>`{.interpreted-text
role="ref"}

Allows an application to collect battery statistics. See
[BATTERY_STATS](https://developer.android.com/reference/android/Manifest.permission#BATTERY_STATS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_accessibility_service}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_accessibility_service**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_accessibility_service>`{.interpreted-text
role="ref"}

Must be required by an AccessibilityService, to ensure that only the
system can bind to it. See
[BIND_ACCESSIBILITY_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_ACCESSIBILITY_SERVICE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_appwidget}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_appwidget**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_appwidget>`{.interpreted-text
role="ref"}

Allows an application to tell the AppWidget service which application
can access AppWidget\'s data. See
[BIND_APPWIDGET](https://developer.android.com/reference/android/Manifest.permission#BIND_APPWIDGET).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_device_admin}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_device_admin**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_device_admin>`{.interpreted-text
role="ref"}

Must be required by device administration receiver, to ensure that only
the system can interact with it. See
[BIND_DEVICE_ADMIN](https://developer.android.com/reference/android/Manifest.permission#BIND_DEVICE_ADMIN).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_input_method}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_input_method**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_input_method>`{.interpreted-text
role="ref"}

Must be required by an InputMethodService, to ensure that only the
system can bind to it. See
[BIND_INPUT_METHOD](https://developer.android.com/reference/android/Manifest.permission#BIND_INPUT_METHOD).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_nfc_service}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_nfc_service**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_nfc_service>`{.interpreted-text
role="ref"}

Must be required by a HostApduService or OffHostApduService to ensure
that only the system can bind to it. See
[BIND_NFC_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_NFC_SERVICE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_notification_listener_service}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_notification_listener_service**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_notification_listener_service>`{.interpreted-text
role="ref"}

Must be required by a NotificationListenerService, to ensure that only
the system can bind to it. See
[BIND_NOTIFICATION_LISTENER_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_NOTIFICATION_LISTENER_SERVICE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_print_service}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_print_service**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_print_service>`{.interpreted-text
role="ref"}

Must be required by a PrintService, to ensure that only the system can
bind to it. See
[BIND_PRINT_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_PRINT_SERVICE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_remoteviews}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_remoteviews**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_remoteviews>`{.interpreted-text
role="ref"}

Must be required by a RemoteViewsService, to ensure that only the system
can bind to it. See
[BIND_REMOTEVIEWS](https://developer.android.com/reference/android/Manifest.permission#BIND_REMOTEVIEWS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_text_service}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_text_service**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_text_service>`{.interpreted-text
role="ref"}

Must be required by a TextService (e.g. SpellCheckerService) to ensure
that only the system can bind to it. See
[BIND_TEXT_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_TEXT_SERVICE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_vpn_service}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_vpn_service**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_vpn_service>`{.interpreted-text
role="ref"}

Must be required by a VpnService, to ensure that only the system can
bind to it. See
[BIND_VPN_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_VPN_SERVICE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bind_wallpaper}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bind_wallpaper**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bind_wallpaper>`{.interpreted-text
role="ref"}

Must be required by a WallpaperService, to ensure that only the system
can bind to it. See
[BIND_WALLPAPER](https://developer.android.com/reference/android/Manifest.permission#BIND_WALLPAPER).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bluetooth}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bluetooth**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bluetooth>`{.interpreted-text
role="ref"}

Allows applications to connect to paired bluetooth devices. See
[BLUETOOTH](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bluetooth_admin}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bluetooth_admin**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bluetooth_admin>`{.interpreted-text
role="ref"}

Allows applications to discover and pair bluetooth devices. See
[BLUETOOTH_ADMIN](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADMIN).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/bluetooth_privileged}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/bluetooth_privileged**
`🔗<class_EditorExportPlatformAndroid_property_permissions/bluetooth_privileged>`{.interpreted-text
role="ref"}

Allows applications to pair bluetooth devices without user interaction,
and to allow or disallow phonebook access or message access. See
[BLUETOOTH_PRIVILEGED](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_PRIVILEGED).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/brick}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **permissions/brick**
`🔗<class_EditorExportPlatformAndroid_property_permissions/brick>`{.interpreted-text
role="ref"}

Required to be able to disable the device (very dangerous!).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/broadcast_package_removed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/broadcast_package_removed**
`🔗<class_EditorExportPlatformAndroid_property_permissions/broadcast_package_removed>`{.interpreted-text
role="ref"}

Allows an application to broadcast a notification that an application
package has been removed. See
[BROADCAST_PACKAGE_REMOVED](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_PACKAGE_REMOVED).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/broadcast_sms}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/broadcast_sms**
`🔗<class_EditorExportPlatformAndroid_property_permissions/broadcast_sms>`{.interpreted-text
role="ref"}

Allows an application to broadcast an SMS receipt notification. See
[BROADCAST_SMS](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_SMS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/broadcast_sticky}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/broadcast_sticky**
`🔗<class_EditorExportPlatformAndroid_property_permissions/broadcast_sticky>`{.interpreted-text
role="ref"}

Allows an application to broadcast sticky intents. See
[BROADCAST_STICKY](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_STICKY).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/broadcast_wap_push}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/broadcast_wap_push**
`🔗<class_EditorExportPlatformAndroid_property_permissions/broadcast_wap_push>`{.interpreted-text
role="ref"}

Allows an application to broadcast a WAP PUSH receipt notification. See
[BROADCAST_WAP_PUSH](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_WAP_PUSH).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/call_phone}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/call_phone**
`🔗<class_EditorExportPlatformAndroid_property_permissions/call_phone>`{.interpreted-text
role="ref"}

Allows an application to initiate a phone call without going through the
Dialer user interface. See
[CALL_PHONE](https://developer.android.com/reference/android/Manifest.permission#CALL_PHONE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/call_privileged}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/call_privileged**
`🔗<class_EditorExportPlatformAndroid_property_permissions/call_privileged>`{.interpreted-text
role="ref"}

Allows an application to call any phone number, including emergency
numbers, without going through the Dialer user interface. See
[CALL_PRIVILEGED](https://developer.android.com/reference/android/Manifest.permission#CALL_PRIVILEGED).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/camera}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **permissions/camera**
`🔗<class_EditorExportPlatformAndroid_property_permissions/camera>`{.interpreted-text
role="ref"}

Required to be able to access the camera device. See
[CAMERA](https://developer.android.com/reference/android/Manifest.permission#CAMERA).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/capture_audio_output}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/capture_audio_output**
`🔗<class_EditorExportPlatformAndroid_property_permissions/capture_audio_output>`{.interpreted-text
role="ref"}

Allows an application to capture audio output. See
[CAPTURE_AUDIO_OUTPUT](https://developer.android.com/reference/android/Manifest.permission#CAPTURE_AUDIO_OUTPUT).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/capture_secure_video_output}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/capture_secure_video_output**
`🔗<class_EditorExportPlatformAndroid_property_permissions/capture_secure_video_output>`{.interpreted-text
role="ref"}

Allows an application to capture secure video output.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/capture_video_output}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/capture_video_output**
`🔗<class_EditorExportPlatformAndroid_property_permissions/capture_video_output>`{.interpreted-text
role="ref"}

Allows an application to capture video output.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/change_component_enabled_state}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/change_component_enabled_state**
`🔗<class_EditorExportPlatformAndroid_property_permissions/change_component_enabled_state>`{.interpreted-text
role="ref"}

Allows an application to change whether an application component (other
than its own) is enabled or not. See
[CHANGE_COMPONENT_ENABLED_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_COMPONENT_ENABLED_STATE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/change_configuration}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/change_configuration**
`🔗<class_EditorExportPlatformAndroid_property_permissions/change_configuration>`{.interpreted-text
role="ref"}

Allows an application to modify the current configuration, such as
locale. See
[CHANGE_CONFIGURATION](https://developer.android.com/reference/android/Manifest.permission#CHANGE_CONFIGURATION).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/change_network_state}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/change_network_state**
`🔗<class_EditorExportPlatformAndroid_property_permissions/change_network_state>`{.interpreted-text
role="ref"}

Allows applications to change network connectivity state. See
[CHANGE_NETWORK_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_NETWORK_STATE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/change_wifi_multicast_state}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/change_wifi_multicast_state**
`🔗<class_EditorExportPlatformAndroid_property_permissions/change_wifi_multicast_state>`{.interpreted-text
role="ref"}

Allows applications to enter Wi-Fi Multicast mode. See
[CHANGE_WIFI_MULTICAST_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_MULTICAST_STATE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/change_wifi_state}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/change_wifi_state**
`🔗<class_EditorExportPlatformAndroid_property_permissions/change_wifi_state>`{.interpreted-text
role="ref"}

Allows applications to change Wi-Fi connectivity state. See
[CHANGE_WIFI_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/clear_app_cache}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/clear_app_cache**
`🔗<class_EditorExportPlatformAndroid_property_permissions/clear_app_cache>`{.interpreted-text
role="ref"}

Allows an application to clear the caches of all installed applications
on the device. See
[CLEAR_APP_CACHE](https://developer.android.com/reference/android/Manifest.permission#CLEAR_APP_CACHE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/clear_app_user_data}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/clear_app_user_data**
`🔗<class_EditorExportPlatformAndroid_property_permissions/clear_app_user_data>`{.interpreted-text
role="ref"}

Allows an application to clear user data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/control_location_updates}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/control_location_updates**
`🔗<class_EditorExportPlatformAndroid_property_permissions/control_location_updates>`{.interpreted-text
role="ref"}

Allows enabling/disabling location update notifications from the radio.
See
[CONTROL_LOCATION_UPDATES](https://developer.android.com/reference/android/Manifest.permission#CONTROL_LOCATION_UPDATES).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/custom_permissions}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **permissions/custom_permissions**
`🔗<class_EditorExportPlatformAndroid_property_permissions/custom_permissions>`{.interpreted-text
role="ref"}

Array of custom permission strings.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/delete_cache_files}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/delete_cache_files**
`🔗<class_EditorExportPlatformAndroid_property_permissions/delete_cache_files>`{.interpreted-text
role="ref"}

**Deprecated:** This property may be changed or removed in future
versions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/delete_packages}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/delete_packages**
`🔗<class_EditorExportPlatformAndroid_property_permissions/delete_packages>`{.interpreted-text
role="ref"}

Allows an application to delete packages. See
[DELETE_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#DELETE_PACKAGES).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/device_power}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/device_power**
`🔗<class_EditorExportPlatformAndroid_property_permissions/device_power>`{.interpreted-text
role="ref"}

Allows low-level access to power management.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/diagnostic}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/diagnostic**
`🔗<class_EditorExportPlatformAndroid_property_permissions/diagnostic>`{.interpreted-text
role="ref"}

Allows applications to RW to diagnostic resources. See
[DIAGNOSTIC](https://developer.android.com/reference/android/Manifest.permission#DIAGNOSTIC).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/disable_keyguard}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/disable_keyguard**
`🔗<class_EditorExportPlatformAndroid_property_permissions/disable_keyguard>`{.interpreted-text
role="ref"}

Allows applications to disable the keyguard if it is not secure. See
[DISABLE_KEYGUARD](https://developer.android.com/reference/android/Manifest.permission#DISABLE_KEYGUARD).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/dump}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **permissions/dump**
`🔗<class_EditorExportPlatformAndroid_property_permissions/dump>`{.interpreted-text
role="ref"}

Allows an application to retrieve state dump information from system
services. See
[DUMP](https://developer.android.com/reference/android/Manifest.permission#DUMP).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/expand_status_bar}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/expand_status_bar**
`🔗<class_EditorExportPlatformAndroid_property_permissions/expand_status_bar>`{.interpreted-text
role="ref"}

Allows an application to expand or collapse the status bar. See
[EXPAND_STATUS_BAR](https://developer.android.com/reference/android/Manifest.permission#EXPAND_STATUS_BAR).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/factory_test}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/factory_test**
`🔗<class_EditorExportPlatformAndroid_property_permissions/factory_test>`{.interpreted-text
role="ref"}

Run as a manufacturer test application, running as the root user. See
[FACTORY_TEST](https://developer.android.com/reference/android/Manifest.permission#FACTORY_TEST).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/flashlight}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/flashlight**
`🔗<class_EditorExportPlatformAndroid_property_permissions/flashlight>`{.interpreted-text
role="ref"}

Allows access to the flashlight.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/force_back}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/force_back**
`🔗<class_EditorExportPlatformAndroid_property_permissions/force_back>`{.interpreted-text
role="ref"}

Allows an application to force a BACK operation on whatever is the top
activity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/get_accounts}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/get_accounts**
`🔗<class_EditorExportPlatformAndroid_property_permissions/get_accounts>`{.interpreted-text
role="ref"}

Allows access to the list of accounts in the Accounts Service. See
[GET_ACCOUNTS](https://developer.android.com/reference/android/Manifest.permission#GET_ACCOUNTS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/get_package_size}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/get_package_size**
`🔗<class_EditorExportPlatformAndroid_property_permissions/get_package_size>`{.interpreted-text
role="ref"}

Allows an application to find out the space used by any package. See
[GET_PACKAGE_SIZE](https://developer.android.com/reference/android/Manifest.permission#GET_PACKAGE_SIZE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/get_tasks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/get_tasks**
`🔗<class_EditorExportPlatformAndroid_property_permissions/get_tasks>`{.interpreted-text
role="ref"}

**Deprecated:** Deprecated in API level 21.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/get_top_activity_info}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/get_top_activity_info**
`🔗<class_EditorExportPlatformAndroid_property_permissions/get_top_activity_info>`{.interpreted-text
role="ref"}

Allows an application to retrieve private information about the current
top activity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/global_search}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/global_search**
`🔗<class_EditorExportPlatformAndroid_property_permissions/global_search>`{.interpreted-text
role="ref"}

Used on content providers to allow the global search system to access
their data. See
[GLOBAL_SEARCH](https://developer.android.com/reference/android/Manifest.permission#GLOBAL_SEARCH).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/hardware_test}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/hardware_test**
`🔗<class_EditorExportPlatformAndroid_property_permissions/hardware_test>`{.interpreted-text
role="ref"}

Allows access to hardware peripherals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/inject_events}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/inject_events**
`🔗<class_EditorExportPlatformAndroid_property_permissions/inject_events>`{.interpreted-text
role="ref"}

Allows an application to inject user events (keys, touch, trackball)
into the event stream and deliver them to ANY window.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/install_location_provider}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/install_location_provider**
`🔗<class_EditorExportPlatformAndroid_property_permissions/install_location_provider>`{.interpreted-text
role="ref"}

Allows an application to install a location provider into the Location
Manager. See
[INSTALL_LOCATION_PROVIDER](https://developer.android.com/reference/android/Manifest.permission#INSTALL_LOCATION_PROVIDER).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/install_packages}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/install_packages**
`🔗<class_EditorExportPlatformAndroid_property_permissions/install_packages>`{.interpreted-text
role="ref"}

Allows an application to install packages. See
[INSTALL_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#INSTALL_PACKAGES).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/install_shortcut}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/install_shortcut**
`🔗<class_EditorExportPlatformAndroid_property_permissions/install_shortcut>`{.interpreted-text
role="ref"}

Allows an application to install a shortcut in Launcher. See
[INSTALL_SHORTCUT](https://developer.android.com/reference/android/Manifest.permission#INSTALL_SHORTCUT).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/internal_system_window}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/internal_system_window**
`🔗<class_EditorExportPlatformAndroid_property_permissions/internal_system_window>`{.interpreted-text
role="ref"}

Allows an application to open windows that are for use by parts of the
system user interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/internet}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/internet**
`🔗<class_EditorExportPlatformAndroid_property_permissions/internet>`{.interpreted-text
role="ref"}

Allows applications to open network sockets. See
[INTERNET](https://developer.android.com/reference/android/Manifest.permission#INTERNET).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/kill_background_processes}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/kill_background_processes**
`🔗<class_EditorExportPlatformAndroid_property_permissions/kill_background_processes>`{.interpreted-text
role="ref"}

Allows an application to call
ActivityManager.killBackgroundProcesses(String). See
[KILL_BACKGROUND_PROCESSES](https://developer.android.com/reference/android/Manifest.permission#KILL_BACKGROUND_PROCESSES).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/location_hardware}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/location_hardware**
`🔗<class_EditorExportPlatformAndroid_property_permissions/location_hardware>`{.interpreted-text
role="ref"}

Allows an application to use location features in hardware, such as the
geofencing api. See
[LOCATION_HARDWARE](https://developer.android.com/reference/android/Manifest.permission#LOCATION_HARDWARE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/manage_accounts}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/manage_accounts**
`🔗<class_EditorExportPlatformAndroid_property_permissions/manage_accounts>`{.interpreted-text
role="ref"}

Allows an application to manage the list of accounts in the
AccountManager.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/manage_app_tokens}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/manage_app_tokens**
`🔗<class_EditorExportPlatformAndroid_property_permissions/manage_app_tokens>`{.interpreted-text
role="ref"}

Allows an application to manage (create, destroy, Z-order) application
tokens in the window manager.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/manage_documents}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/manage_documents**
`🔗<class_EditorExportPlatformAndroid_property_permissions/manage_documents>`{.interpreted-text
role="ref"}

Allows an application to manage access to documents, usually as part of
a document picker. See
[MANAGE_DOCUMENTS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DOCUMENTS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/manage_external_storage}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/manage_external_storage**
`🔗<class_EditorExportPlatformAndroid_property_permissions/manage_external_storage>`{.interpreted-text
role="ref"}

Allows an application a broad access to external storage in scoped
storage. See
[MANAGE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_EXTERNAL_STORAGE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/master_clear}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/master_clear**
`🔗<class_EditorExportPlatformAndroid_property_permissions/master_clear>`{.interpreted-text
role="ref"}

See
[MASTER_CLEAR](https://developer.android.com/reference/android/Manifest.permission#MASTER_CLEAR).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/media_content_control}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/media_content_control**
`🔗<class_EditorExportPlatformAndroid_property_permissions/media_content_control>`{.interpreted-text
role="ref"}

Allows an application to know what content is playing and control its
playback. See
[MEDIA_CONTENT_CONTROL](https://developer.android.com/reference/android/Manifest.permission#MEDIA_CONTENT_CONTROL).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/modify_audio_settings}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/modify_audio_settings**
`🔗<class_EditorExportPlatformAndroid_property_permissions/modify_audio_settings>`{.interpreted-text
role="ref"}

Allows an application to modify global audio settings. See
[MODIFY_AUDIO_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#MODIFY_AUDIO_SETTINGS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/modify_phone_state}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/modify_phone_state**
`🔗<class_EditorExportPlatformAndroid_property_permissions/modify_phone_state>`{.interpreted-text
role="ref"}

Allows modification of the telephony state - power on, mmi, etc. Does
not include placing calls. See
[MODIFY_PHONE_STATE](https://developer.android.com/reference/android/Manifest.permission#MODIFY_PHONE_STATE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/mount_format_filesystems}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/mount_format_filesystems**
`🔗<class_EditorExportPlatformAndroid_property_permissions/mount_format_filesystems>`{.interpreted-text
role="ref"}

Allows formatting file systems for removable storage. See
[MOUNT_FORMAT_FILESYSTEMS](https://developer.android.com/reference/android/Manifest.permission#MOUNT_FORMAT_FILESYSTEMS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/mount_unmount_filesystems}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/mount_unmount_filesystems**
`🔗<class_EditorExportPlatformAndroid_property_permissions/mount_unmount_filesystems>`{.interpreted-text
role="ref"}

Allows mounting and unmounting file systems for removable storage. See
[MOUNT_UNMOUNT_FILESYSTEMS](https://developer.android.com/reference/android/Manifest.permission#MOUNT_UNMOUNT_FILESYSTEMS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/nfc}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **permissions/nfc**
`🔗<class_EditorExportPlatformAndroid_property_permissions/nfc>`{.interpreted-text
role="ref"}

Allows applications to perform I/O operations over NFC. See
[NFC](https://developer.android.com/reference/android/Manifest.permission#NFC).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/persistent_activity}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/persistent_activity**
`🔗<class_EditorExportPlatformAndroid_property_permissions/persistent_activity>`{.interpreted-text
role="ref"}

**Deprecated:** Deprecated in API level 15.

Allows an application to make its activities persistent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/post_notifications}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/post_notifications**
`🔗<class_EditorExportPlatformAndroid_property_permissions/post_notifications>`{.interpreted-text
role="ref"}

Allows an application to post notifications. Added in API level 33. See
[Notification runtime
permission](https://developer.android.com/develop/ui/views/notifications/notification-permission).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/process_outgoing_calls}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/process_outgoing_calls**
`🔗<class_EditorExportPlatformAndroid_property_permissions/process_outgoing_calls>`{.interpreted-text
role="ref"}

**Deprecated:** Deprecated in API level 29.

Allows an application to see the number being dialed during an outgoing
call with the option to redirect the call to a different number or abort
the call altogether. See
[PROCESS_OUTGOING_CALLS](https://developer.android.com/reference/android/Manifest.permission#PROCESS_OUTGOING_CALLS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_calendar}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_calendar**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_calendar>`{.interpreted-text
role="ref"}

Allows an application to read the user\'s calendar data. See
[READ_CALENDAR](https://developer.android.com/reference/android/Manifest.permission#READ_CALENDAR).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_call_log}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_call_log**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_call_log>`{.interpreted-text
role="ref"}

Allows an application to read the user\'s call log. See
[READ_CALL_LOG](https://developer.android.com/reference/android/Manifest.permission#READ_CALL_LOG).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_contacts}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_contacts**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_contacts>`{.interpreted-text
role="ref"}

Allows an application to read the user\'s contacts data. See
[READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_external_storage}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_external_storage**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_external_storage>`{.interpreted-text
role="ref"}

**Deprecated:** Deprecated in API level 33.

Allows an application to read from external storage. See
[READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_frame_buffer}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_frame_buffer**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_frame_buffer>`{.interpreted-text
role="ref"}

Allows an application to take screen shots and more generally get access
to the frame buffer data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_history_bookmarks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_history_bookmarks**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_history_bookmarks>`{.interpreted-text
role="ref"}

Allows an application to read (but not write) the user\'s browsing
history and bookmarks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_input_state}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_input_state**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_input_state>`{.interpreted-text
role="ref"}

**Deprecated:** Deprecated in API level 16.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_logs}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_logs**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_logs>`{.interpreted-text
role="ref"}

Allows an application to read the low-level system log files. See
[READ_LOGS](https://developer.android.com/reference/android/Manifest.permission#READ_LOGS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_media_audio}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_media_audio**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_media_audio>`{.interpreted-text
role="ref"}

Allows an application to read audio files from external storage. See
[READ_MEDIA_AUDIO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_AUDIO).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_media_images}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_media_images**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_media_images>`{.interpreted-text
role="ref"}

Allows an application to read image files from external storage. See
[READ_MEDIA_IMAGES](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_media_video}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_media_video**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_media_video>`{.interpreted-text
role="ref"}

Allows an application to read video files from external storage. See
[READ_MEDIA_VIDEO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_media_visual_user_selected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_media_visual_user_selected**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_media_visual_user_selected>`{.interpreted-text
role="ref"}

Allows an application to read image or video files from external storage
that a user has selected via the permission prompt photo picker. See
[READ_MEDIA_VISUAL_USER_SELECTED](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VISUAL_USER_SELECTED).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_phone_state}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_phone_state**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_phone_state>`{.interpreted-text
role="ref"}

Allows read only access to phone state. See
[READ_PHONE_STATE](https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_profile}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_profile**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_profile>`{.interpreted-text
role="ref"}

Allows an application to read the user\'s personal profile data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_sms}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_sms**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_sms>`{.interpreted-text
role="ref"}

Allows an application to read SMS messages. See
[READ_SMS](https://developer.android.com/reference/android/Manifest.permission#READ_SMS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_social_stream}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_social_stream**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_social_stream>`{.interpreted-text
role="ref"}

Allows an application to read from the user\'s social stream.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_sync_settings}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_sync_settings**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_sync_settings>`{.interpreted-text
role="ref"}

Allows applications to read the sync settings. See
[READ_SYNC_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#READ_SYNC_SETTINGS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_sync_stats}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_sync_stats**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_sync_stats>`{.interpreted-text
role="ref"}

Allows applications to read the sync stats. See
[READ_SYNC_STATS](https://developer.android.com/reference/android/Manifest.permission#READ_SYNC_STATS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/read_user_dictionary}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/read_user_dictionary**
`🔗<class_EditorExportPlatformAndroid_property_permissions/read_user_dictionary>`{.interpreted-text
role="ref"}

Allows an application to read the user dictionary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/reboot}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **permissions/reboot**
`🔗<class_EditorExportPlatformAndroid_property_permissions/reboot>`{.interpreted-text
role="ref"}

Required to be able to reboot the device. See
[REBOOT](https://developer.android.com/reference/android/Manifest.permission#REBOOT).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/receive_boot_completed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/receive_boot_completed**
`🔗<class_EditorExportPlatformAndroid_property_permissions/receive_boot_completed>`{.interpreted-text
role="ref"}

Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that
is broadcast after the system finishes booting. See
[RECEIVE_BOOT_COMPLETED](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_BOOT_COMPLETED).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/receive_mms}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/receive_mms**
`🔗<class_EditorExportPlatformAndroid_property_permissions/receive_mms>`{.interpreted-text
role="ref"}

Allows an application to monitor incoming MMS messages. See
[RECEIVE_MMS](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_MMS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/receive_sms}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/receive_sms**
`🔗<class_EditorExportPlatformAndroid_property_permissions/receive_sms>`{.interpreted-text
role="ref"}

Allows an application to receive SMS messages. See
[RECEIVE_SMS](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_SMS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/receive_wap_push}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/receive_wap_push**
`🔗<class_EditorExportPlatformAndroid_property_permissions/receive_wap_push>`{.interpreted-text
role="ref"}

Allows an application to receive WAP push messages. See
[RECEIVE_WAP_PUSH](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_WAP_PUSH).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/record_audio}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/record_audio**
`🔗<class_EditorExportPlatformAndroid_property_permissions/record_audio>`{.interpreted-text
role="ref"}

Allows an application to record audio. See
[RECORD_AUDIO](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/reorder_tasks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/reorder_tasks**
`🔗<class_EditorExportPlatformAndroid_property_permissions/reorder_tasks>`{.interpreted-text
role="ref"}

Allows an application to change the Z-order of tasks. See
[REORDER_TASKS](https://developer.android.com/reference/android/Manifest.permission#REORDER_TASKS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/restart_packages}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/restart_packages**
`🔗<class_EditorExportPlatformAndroid_property_permissions/restart_packages>`{.interpreted-text
role="ref"}

**Deprecated:** Deprecated in API level 15.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/send_respond_via_message}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/send_respond_via_message**
`🔗<class_EditorExportPlatformAndroid_property_permissions/send_respond_via_message>`{.interpreted-text
role="ref"}

Allows an application (Phone) to send a request to other applications to
handle the respond-via-message action during incoming calls. See
[SEND_RESPOND_VIA_MESSAGE](https://developer.android.com/reference/android/Manifest.permission#SEND_RESPOND_VIA_MESSAGE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/send_sms}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/send_sms**
`🔗<class_EditorExportPlatformAndroid_property_permissions/send_sms>`{.interpreted-text
role="ref"}

Allows an application to send SMS messages. See
[SEND_SMS](https://developer.android.com/reference/android/Manifest.permission#SEND_SMS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_activity_watcher}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_activity_watcher**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_activity_watcher>`{.interpreted-text
role="ref"}

Allows an application to watch and control how activities are started
globally in the system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_alarm}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_alarm**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_alarm>`{.interpreted-text
role="ref"}

Allows an application to broadcast an Intent to set an alarm for the
user. See
[SET_ALARM](https://developer.android.com/reference/android/Manifest.permission#SET_ALARM).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_always_finish}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_always_finish**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_always_finish>`{.interpreted-text
role="ref"}

Allows an application to control whether activities are immediately
finished when put in the background. See
[SET_ALWAYS_FINISH](https://developer.android.com/reference/android/Manifest.permission#SET_ALWAYS_FINISH).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_animation_scale}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_animation_scale**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_animation_scale>`{.interpreted-text
role="ref"}

Allows to modify the global animation scaling factor. See
[SET_ANIMATION_SCALE](https://developer.android.com/reference/android/Manifest.permission#SET_ANIMATION_SCALE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_debug_app}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_debug_app**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_debug_app>`{.interpreted-text
role="ref"}

Configure an application for debugging. See
[SET_DEBUG_APP](https://developer.android.com/reference/android/Manifest.permission#SET_DEBUG_APP).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_orientation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_orientation**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_orientation>`{.interpreted-text
role="ref"}

Allows low-level access to setting the orientation (actually rotation)
of the screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_pointer_speed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_pointer_speed**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_pointer_speed>`{.interpreted-text
role="ref"}

Allows low-level access to setting the pointer speed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_preferred_applications}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_preferred_applications**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_preferred_applications>`{.interpreted-text
role="ref"}

**Deprecated:** Deprecated in API level 15.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_process_limit}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_process_limit**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_process_limit>`{.interpreted-text
role="ref"}

Allows an application to set the maximum number of (not needed)
application processes that can be running. See
[SET_PROCESS_LIMIT](https://developer.android.com/reference/android/Manifest.permission#SET_PROCESS_LIMIT).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_time}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_time**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_time>`{.interpreted-text
role="ref"}

Allows applications to set the system time directly. See
[SET_TIME](https://developer.android.com/reference/android/Manifest.permission#SET_TIME).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_time_zone}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_time_zone**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_time_zone>`{.interpreted-text
role="ref"}

Allows applications to set the system time zone directly. See
[SET_TIME_ZONE](https://developer.android.com/reference/android/Manifest.permission#SET_TIME_ZONE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_wallpaper}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_wallpaper**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_wallpaper>`{.interpreted-text
role="ref"}

Allows applications to set the wallpaper. See
[SET_WALLPAPER](https://developer.android.com/reference/android/Manifest.permission#SET_WALLPAPER).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/set_wallpaper_hints}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/set_wallpaper_hints**
`🔗<class_EditorExportPlatformAndroid_property_permissions/set_wallpaper_hints>`{.interpreted-text
role="ref"}

Allows applications to set the wallpaper hints. See
[SET_WALLPAPER_HINTS](https://developer.android.com/reference/android/Manifest.permission#SET_WALLPAPER_HINTS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/signal_persistent_processes}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/signal_persistent_processes**
`🔗<class_EditorExportPlatformAndroid_property_permissions/signal_persistent_processes>`{.interpreted-text
role="ref"}

Allow an application to request that a signal be sent to all persistent
processes. See
[SIGNAL_PERSISTENT_PROCESSES](https://developer.android.com/reference/android/Manifest.permission#SIGNAL_PERSISTENT_PROCESSES).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/status_bar}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/status_bar**
`🔗<class_EditorExportPlatformAndroid_property_permissions/status_bar>`{.interpreted-text
role="ref"}

Allows an application to open, close, or disable the status bar and its
icons. See
[STATUS_BAR](https://developer.android.com/reference/android/Manifest.permission#STATUS_BAR).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/subscribed_feeds_read}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/subscribed_feeds_read**
`🔗<class_EditorExportPlatformAndroid_property_permissions/subscribed_feeds_read>`{.interpreted-text
role="ref"}

Allows an application to allow access the subscribed feeds
ContentProvider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/subscribed_feeds_write}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/subscribed_feeds_write**
`🔗<class_EditorExportPlatformAndroid_property_permissions/subscribed_feeds_write>`{.interpreted-text
role="ref"}

**Deprecated:** This property may be changed or removed in future
versions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/system_alert_window}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/system_alert_window**
`🔗<class_EditorExportPlatformAndroid_property_permissions/system_alert_window>`{.interpreted-text
role="ref"}

Allows an app to create windows using the type
WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY, shown on top of all
other apps. See
[SYSTEM_ALERT_WINDOW](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/transmit_ir}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/transmit_ir**
`🔗<class_EditorExportPlatformAndroid_property_permissions/transmit_ir>`{.interpreted-text
role="ref"}

Allows using the device\'s IR transmitter, if available. See
[TRANSMIT_IR](https://developer.android.com/reference/android/Manifest.permission#TRANSMIT_IR).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/uninstall_shortcut}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/uninstall_shortcut**
`🔗<class_EditorExportPlatformAndroid_property_permissions/uninstall_shortcut>`{.interpreted-text
role="ref"}

**Deprecated:** This property may be changed or removed in future
versions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/update_device_stats}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/update_device_stats**
`🔗<class_EditorExportPlatformAndroid_property_permissions/update_device_stats>`{.interpreted-text
role="ref"}

Allows an application to update device statistics. See
[UPDATE_DEVICE_STATS](https://developer.android.com/reference/android/Manifest.permission#UPDATE_DEVICE_STATS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/use_credentials}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/use_credentials**
`🔗<class_EditorExportPlatformAndroid_property_permissions/use_credentials>`{.interpreted-text
role="ref"}

Allows an application to request authtokens from the AccountManager.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/use_sip}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **permissions/use_sip**
`🔗<class_EditorExportPlatformAndroid_property_permissions/use_sip>`{.interpreted-text
role="ref"}

Allows an application to use SIP service. See
[USE_SIP](https://developer.android.com/reference/android/Manifest.permission#USE_SIP).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/vibrate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **permissions/vibrate**
`🔗<class_EditorExportPlatformAndroid_property_permissions/vibrate>`{.interpreted-text
role="ref"}

Allows access to the vibrator. See
[VIBRATE](https://developer.android.com/reference/android/Manifest.permission#VIBRATE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/wake_lock}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/wake_lock**
`🔗<class_EditorExportPlatformAndroid_property_permissions/wake_lock>`{.interpreted-text
role="ref"}

Allows using PowerManager WakeLocks to keep processor from sleeping or
screen from dimming. See
[WAKE_LOCK](https://developer.android.com/reference/android/Manifest.permission#WAKE_LOCK).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_apn_settings}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_apn_settings**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_apn_settings>`{.interpreted-text
role="ref"}

Allows applications to write the apn settings and read sensitive fields
of an existing apn settings like user and password. See
[WRITE_APN_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_APN_SETTINGS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_calendar}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_calendar**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_calendar>`{.interpreted-text
role="ref"}

Allows an application to write the user\'s calendar data. See
[WRITE_CALENDAR](https://developer.android.com/reference/android/Manifest.permission#WRITE_CALENDAR).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_call_log}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_call_log**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_call_log>`{.interpreted-text
role="ref"}

Allows an application to write (but not read) the user\'s call log data.
See
[WRITE_CALL_LOG](https://developer.android.com/reference/android/Manifest.permission#WRITE_CALL_LOG).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_contacts}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_contacts**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_contacts>`{.interpreted-text
role="ref"}

Allows an application to write the user\'s contacts data. See
[WRITE_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#WRITE_CONTACTS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_external_storage}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_external_storage**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_external_storage>`{.interpreted-text
role="ref"}

Allows an application to write to external storage. See
[WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_gservices}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_gservices**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_gservices>`{.interpreted-text
role="ref"}

Allows an application to modify the Google service map. See
[WRITE_GSERVICES](https://developer.android.com/reference/android/Manifest.permission#WRITE_GSERVICES).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_history_bookmarks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_history_bookmarks**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_history_bookmarks>`{.interpreted-text
role="ref"}

Allows an application to write (but not read) the user\'s browsing
history and bookmarks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_profile}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_profile**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_profile>`{.interpreted-text
role="ref"}

Allows an application to write (but not read) the user\'s personal
profile data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_secure_settings}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_secure_settings**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_secure_settings>`{.interpreted-text
role="ref"}

Allows an application to read or write the secure system settings. See
[WRITE_SECURE_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SECURE_SETTINGS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_settings}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_settings**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_settings>`{.interpreted-text
role="ref"}

Allows an application to read or write the system settings. See
[WRITE_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SETTINGS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_sms}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_sms**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_sms>`{.interpreted-text
role="ref"}

Allows an application to write SMS messages.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_social_stream}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_social_stream**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_social_stream>`{.interpreted-text
role="ref"}

Allows an application to write (but not read) the user\'s social stream
data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_sync_settings}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_sync_settings**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_sync_settings>`{.interpreted-text
role="ref"}

Allows applications to write the sync settings. See
[WRITE_SYNC_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SYNC_SETTINGS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_permissions/write_user_dictionary}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**permissions/write_user_dictionary**
`🔗<class_EditorExportPlatformAndroid_property_permissions/write_user_dictionary>`{.interpreted-text
role="ref"}

Allows an application to write to the user dictionary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_screen/edge_to_edge}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **screen/edge_to_edge**
`🔗<class_EditorExportPlatformAndroid_property_screen/edge_to_edge>`{.interpreted-text
role="ref"}

If `true`, this makes the navigation and status bars translucent and
allows the application content to extend edge to edge.

\*\*Note:\*\* You should ensure that none of the application content is
occluded by system elements by using the
`DisplayServer.get_display_safe_area()<class_DisplayServer_method_get_display_safe_area>`{.interpreted-text
role="ref"} and
`DisplayServer.get_display_cutouts()<class_DisplayServer_method_get_display_cutouts>`{.interpreted-text
role="ref"} methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_screen/immersive_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**screen/immersive_mode**
`🔗<class_EditorExportPlatformAndroid_property_screen/immersive_mode>`{.interpreted-text
role="ref"}

If `true`, hides the navigation and status bar. Set
`DisplayServer.window_set_mode()<class_DisplayServer_method_window_set_mode>`{.interpreted-text
role="ref"} to change this at runtime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_screen/support_large}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**screen/support_large**
`🔗<class_EditorExportPlatformAndroid_property_screen/support_large>`{.interpreted-text
role="ref"}

Indicates whether the application supports larger screen form-factors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_screen/support_normal}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**screen/support_normal**
`🔗<class_EditorExportPlatformAndroid_property_screen/support_normal>`{.interpreted-text
role="ref"}

Indicates whether an application supports the \"normal\" screen
form-factors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_screen/support_small}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**screen/support_small**
`🔗<class_EditorExportPlatformAndroid_property_screen/support_small>`{.interpreted-text
role="ref"}

Indicates whether the application supports smaller screen form-factors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_screen/support_xlarge}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**screen/support_xlarge**
`🔗<class_EditorExportPlatformAndroid_property_screen/support_xlarge>`{.interpreted-text
role="ref"}

Indicates whether the application supports extra large screen
form-factors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_shader_baker/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shader_baker/enabled**
`🔗<class_EditorExportPlatformAndroid_property_shader_baker/enabled>`{.interpreted-text
role="ref"}

If `true`, shaders will be compiled and embedded in the application.
This option is only supported when using the Forward+ or Mobile
renderers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_user_data_backup/allow}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**user_data_backup/allow**
`🔗<class_EditorExportPlatformAndroid_property_user_data_backup/allow>`{.interpreted-text
role="ref"}

If `true`, allows the application to participate in the backup and
restore infrastructure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_version/code}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **version/code**
`🔗<class_EditorExportPlatformAndroid_property_version/code>`{.interpreted-text
role="ref"}

Machine-readable application version. This must be incremented for every
new release pushed to the Play Store.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_version/name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **version/name**
`🔗<class_EditorExportPlatformAndroid_property_version/name>`{.interpreted-text
role="ref"}

Application version visible to the user. Falls back to
`ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>`{.interpreted-text
role="ref"} if left empty.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformAndroid_property_xr_features/xr_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **xr_features/xr_mode**
`🔗<class_EditorExportPlatformAndroid_property_xr_features/xr_mode>`{.interpreted-text
role="ref"}

The extended reality (XR) mode for this application.
