github_url
:   hide

# EditorExportPlugin {#class_EditorExportPlugin}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A script that is executed when exporting the project.

::: rst-class
classref-introduction-group
:::

## Description

**EditorExportPlugin**s are automatically invoked whenever the user
exports the project. Their most common use is to determine what files
are being included in the exported project. For each plugin,
`_export_begin()<class_EditorExportPlugin_private_method__export_begin>`{.interpreted-text
role="ref"} is called at the beginning of the export process and then
`_export_file()<class_EditorExportPlugin_private_method__export_file>`{.interpreted-text
role="ref"} is called for each exported file.

To use **EditorExportPlugin**, register it using the
`EditorPlugin.add_export_plugin()<class_EditorPlugin_method_add_export_plugin>`{.interpreted-text
role="ref"} method first.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Export Android plugins <../tutorials/platform/android/android_plugin>`{.interpreted-text
  role="doc"}

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

## Method Descriptions

:::: {#class_EditorExportPlugin_private_method__begin_customize_resources}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_begin_customize_resources**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, features:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__begin_customize_resources>`{.interpreted-text
role="ref"}

Return `true` if this plugin will customize resources based on the
platform and features used.

When enabled,
`_get_customization_configuration_hash()<class_EditorExportPlugin_private_method__get_customization_configuration_hash>`{.interpreted-text
role="ref"} and
`_customize_resource()<class_EditorExportPlugin_private_method__customize_resource>`{.interpreted-text
role="ref"} will be called and must be implemented.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__begin_customize_scenes}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_begin_customize_scenes**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, features:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__begin_customize_scenes>`{.interpreted-text
role="ref"}

Return `true` if this plugin will customize scenes based on the platform
and features used.

When enabled,
`_get_customization_configuration_hash()<class_EditorExportPlugin_private_method__get_customization_configuration_hash>`{.interpreted-text
role="ref"} and
`_customize_scene()<class_EditorExportPlugin_private_method__customize_scene>`{.interpreted-text
role="ref"} will be called and must be implemented.

\*\*Note:\*\*
`_customize_scene()<class_EditorExportPlugin_private_method__customize_scene>`{.interpreted-text
role="ref"} will only be called for scenes that have been modified since
the last export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__customize_resource}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**\_customize_resource**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"}, path:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__customize_resource>`{.interpreted-text
role="ref"}

Customize a resource. If changes are made to it, return the same or a
new resource. Otherwise, return `null`. When a new resource is returned,
`resource` will be replaced by a copy of the new resource.

The `path` argument is only used when customizing an actual file,
otherwise this means that this resource is part of another one and it
will be empty.

Implementing this method is required if
`_begin_customize_resources()<class_EditorExportPlugin_private_method__begin_customize_resources>`{.interpreted-text
role="ref"} returns `true`.

\*\*Note:\*\* When customizing any of the following types and returning
another resource, the other resource should not be skipped using
`skip()<class_EditorExportPlugin_method_skip>`{.interpreted-text
role="ref"} in
`_export_file()<class_EditorExportPlugin_private_method__export_file>`{.interpreted-text
role="ref"}:

- `AtlasTexture<class_AtlasTexture>`{.interpreted-text role="ref"}
- `CompressedCubemap<class_CompressedCubemap>`{.interpreted-text
  role="ref"}
- `CompressedCubemapArray<class_CompressedCubemapArray>`{.interpreted-text
  role="ref"}
- `CompressedTexture2D<class_CompressedTexture2D>`{.interpreted-text
  role="ref"}
- `CompressedTexture2DArray<class_CompressedTexture2DArray>`{.interpreted-text
  role="ref"}
- `CompressedTexture3D<class_CompressedTexture3D>`{.interpreted-text
  role="ref"}

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__customize_scene}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"}
**\_customize_scene**(scene: `Node<class_Node>`{.interpreted-text
role="ref"}, path: `String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__customize_scene>`{.interpreted-text
role="ref"}

Customize a scene. If changes are made to it, return the same or a new
scene. Otherwise, return `null`. If a new scene is returned, it is up to
you to dispose of the old one.

Implementing this method is required if
`_begin_customize_scenes()<class_EditorExportPlugin_private_method__begin_customize_scenes>`{.interpreted-text
role="ref"} returns `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__end_customize_resources}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_end_customize_resources**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__end_customize_resources>`{.interpreted-text
role="ref"}

This is called when the customization process for resources ends.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__end_customize_scenes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_end_customize_scenes**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__end_customize_scenes>`{.interpreted-text
role="ref"}

This is called when the customization process for scenes ends.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__export_begin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_export_begin**(features:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, is_debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, flags:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__export_begin>`{.interpreted-text
role="ref"}

Virtual method to be overridden by the user. It is called when the
export starts and provides all information about the export. `features`
is the list of features for the export, `is_debug` is `true` for debug
builds, `path` is the target path for the exported project. `flags` is
only used when running a runnable profile, e.g. when using native run on
Android.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__export_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_export_end**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__export_end>`{.interpreted-text
role="ref"}

Virtual method to be overridden by the user. Called when the export is
finished.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__export_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_export_file**(path: `String<class_String>`{.interpreted-text
role="ref"}, type: `String<class_String>`{.interpreted-text role="ref"},
features: `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__export_file>`{.interpreted-text
role="ref"}

Virtual method to be overridden by the user. Called for each exported
file before
`_customize_resource()<class_EditorExportPlugin_private_method__customize_resource>`{.interpreted-text
role="ref"} and
`_customize_scene()<class_EditorExportPlugin_private_method__customize_scene>`{.interpreted-text
role="ref"}. The arguments can be used to identify the file. `path` is
the path of the file, `type` is the
`Resource<class_Resource>`{.interpreted-text role="ref"} represented by
the file (e.g. `PackedScene<class_PackedScene>`{.interpreted-text
role="ref"}), and `features` is the list of features for the export.

Calling `skip()<class_EditorExportPlugin_method_skip>`{.interpreted-text
role="ref"} inside this callback will make the file not included in the
export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_android_dependencies}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_android_dependencies**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_android_dependencies>`{.interpreted-text
role="ref"}

Virtual method to be overridden by the user. This is called to retrieve
the set of Android dependencies provided by this plugin. Each returned
Android dependency should have the format of an Android remote binary
dependency: `org.godot.example:my-plugin:0.0.0`

For more information see [Android documentation on
dependencies](https://developer.android.com/build/dependencies?agpversion=4.1#dependency-types).

\*\*Note:\*\* Only supported on Android and requires
`EditorExportPlatformAndroid.gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"} to be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_android_dependencies_maven_repos}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_android_dependencies_maven_repos**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_android_dependencies_maven_repos>`{.interpreted-text
role="ref"}

Virtual method to be overridden by the user. This is called to retrieve
the URLs of Maven repositories for the set of Android dependencies
provided by this plugin.

For more information see [Gradle documentation on dependency
management](https://docs.gradle.org/current/userguide/dependency_management.html#sec:maven_repo).

\*\*Note:\*\* Google\'s Maven repo and the Maven Central repo are
already included by default.

\*\*Note:\*\* Only supported on Android and requires
`EditorExportPlatformAndroid.gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"} to be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_android_libraries}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_android_libraries**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_android_libraries>`{.interpreted-text
role="ref"}

Virtual method to be overridden by the user. This is called to retrieve
the local paths of the Android libraries archive (AAR) files provided by
this plugin.

\*\*Note:\*\* Relative paths **must** be relative to Godot\'s
`res://addons/` directory. For example, an AAR file located under
`res://addons/hello_world_plugin/HelloWorld.release.aar` can be returned
as an absolute path using
`res://addons/hello_world_plugin/HelloWorld.release.aar` or a relative
path using `hello_world_plugin/HelloWorld.release.aar`.

\*\*Note:\*\* Only supported on Android and requires
`EditorExportPlatformAndroid.gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"} to be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_android_manifest_activity_element_contents}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_android_manifest_activity_element_contents**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_android_manifest_activity_element_contents>`{.interpreted-text
role="ref"}

Virtual method to be overridden by the user. This is used at export time
to update the contents of the `activity` element in the generated
Android manifest.

\*\*Note:\*\* Only supported on Android and requires
`EditorExportPlatformAndroid.gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"} to be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_android_manifest_application_element_contents}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_android_manifest_application_element_contents**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_android_manifest_application_element_contents>`{.interpreted-text
role="ref"}

Virtual method to be overridden by the user. This is used at export time
to update the contents of the `application` element in the generated
Android manifest.

\*\*Note:\*\* Only supported on Android and requires
`EditorExportPlatformAndroid.gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"} to be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_android_manifest_element_contents}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_android_manifest_element_contents**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_android_manifest_element_contents>`{.interpreted-text
role="ref"}

Virtual method to be overridden by the user. This is used at export time
to update the contents of the `manifest` element in the generated
Android manifest.

\*\*Note:\*\* Only supported on Android and requires
`EditorExportPlatformAndroid.gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`{.interpreted-text
role="ref"} to be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_customization_configuration_hash}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_customization_configuration_hash**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_customization_configuration_hash>`{.interpreted-text
role="ref"}

Return a hash based on the configuration passed (for both scenes and
resources). This helps keep separate caches for separate export
configurations.

Implementing this method is required if
`_begin_customize_resources()<class_EditorExportPlugin_private_method__begin_customize_resources>`{.interpreted-text
role="ref"} returns `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_export_features}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_export_features**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_export_features>`{.interpreted-text
role="ref"}

Return a `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} of additional features this preset, for the given
`platform`, should have.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_export_option_visibility}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_get_export_option_visibility**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, option: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_export_option_visibility>`{.interpreted-text
role="ref"}

Validates `option` and returns the visibility for the specified
`platform`. The default implementation returns `true` for all options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_export_option_warning}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_export_option_warning**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, option: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_export_option_warning>`{.interpreted-text
role="ref"}

Check the requirements for the given `option` and return a non-empty
warning string if they are not met.

\*\*Note:\*\* Use
`get_option()<class_EditorExportPlugin_method_get_option>`{.interpreted-text
role="ref"} to check the value of the export options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_export_options}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_get_export_options**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_export_options>`{.interpreted-text
role="ref"}

Return a list of export options that can be configured for this export
plugin.

Each element in the return value is a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following keys:

- `option`: A dictionary with the structure documented by
  `Object.get_property_list()<class_Object_method_get_property_list>`{.interpreted-text
  role="ref"}, but all keys are optional.
- `default_value`: The default value for this option.
- `update_visibility`: An optional boolean value. If set to `true`, the
  preset will emit
  `Object.property_list_changed<class_Object_signal_property_list_changed>`{.interpreted-text
  role="ref"} when the option is changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_export_options_overrides}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_get_export_options_overrides**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_export_options_overrides>`{.interpreted-text
role="ref"}

Return a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"} of
override values for export options, that will be used instead of
user-provided values. Overridden options will be hidden from the user
interface.

    class MyExportPlugin extends EditorExportPlugin:
        func _get_name() -> String:
            return "MyExportPlugin"

        func _supports_platform(platform) -> bool:
            if platform is EditorExportPlatformPC:
                # Run on all desktop platforms including Windows, MacOS and Linux.
                return true
            return false

        func _get_export_options_overrides(platform) -> Dictionary:
            # Override "Embed PCK" to always be enabled.
            return {
                "binary_format/embed_pck": true,
            }

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **\_get_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__get_name>`{.interpreted-text
role="ref"}

Return the name identifier of this plugin (for future identification by
the exporter). The plugins are sorted by name before exporting.

Implementing this method is required.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__should_update_export_options}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_should_update_export_options**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__should_update_export_options>`{.interpreted-text
role="ref"}

Return `true` if the result of
`_get_export_options()<class_EditorExportPlugin_private_method__get_export_options>`{.interpreted-text
role="ref"} has changed and the export options of the preset
corresponding to `platform` should be updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__supports_platform}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_supports_platform**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__supports_platform>`{.interpreted-text
role="ref"}

Return `true` if the plugin supports the given `platform`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_private_method__update_android_prebuilt_manifest}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**\_update_android_prebuilt_manifest**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}, manifest_data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_private_method__update_android_prebuilt_manifest>`{.interpreted-text
role="ref"}

Provide access to the Android prebuilt manifest and allows the plugin to
modify it if needed.

Implementers of this virtual method should take the binary manifest data
from `manifest_data`, copy it, modify it, and then return it with the
modifications.

If no modifications are needed, then an empty
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
should be returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_apple_embedded_platform_bundle_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_apple_embedded_platform_bundle_file**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_apple_embedded_platform_bundle_file>`{.interpreted-text
role="ref"}

Adds an Apple embedded platform bundle file from the given `path` to the
exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_apple_embedded_platform_cpp_code}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_apple_embedded_platform_cpp_code**(code:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_apple_embedded_platform_cpp_code>`{.interpreted-text
role="ref"}

Adds C++ code to the Apple embedded platform export. The final code is
created from the code appended by each active export plugin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_apple_embedded_platform_embedded_framework}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_apple_embedded_platform_embedded_framework**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_apple_embedded_platform_embedded_framework>`{.interpreted-text
role="ref"}

Adds a dynamic library (\*.dylib, \*.framework) to the Linking Phase in
the Apple embedded platform\'s Xcode project and embeds it into the
resulting binary.

\*\*Note:\*\* For static libraries (\*.a), this works in the same way as
`add_apple_embedded_platform_framework()<class_EditorExportPlugin_method_add_apple_embedded_platform_framework>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method should not be used for System libraries as
they are already present on the device.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_apple_embedded_platform_framework}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_apple_embedded_platform_framework**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_apple_embedded_platform_framework>`{.interpreted-text
role="ref"}

Adds a static library (\*.a) or a dynamic library (\*.dylib,
\*.framework) to the Linking Phase to the Apple embedded platform\'s
Xcode project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_apple_embedded_platform_linker_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_apple_embedded_platform_linker_flags**(flags:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_apple_embedded_platform_linker_flags>`{.interpreted-text
role="ref"}

Adds linker flags for the Apple embedded platform export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_apple_embedded_platform_plist_content}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_apple_embedded_platform_plist_content**(plist_content:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_apple_embedded_platform_plist_content>`{.interpreted-text
role="ref"}

Adds additional fields to the Apple embedded platform\'s project
Info.plist file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_apple_embedded_platform_project_static_lib}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_apple_embedded_platform_project_static_lib**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_apple_embedded_platform_project_static_lib>`{.interpreted-text
role="ref"}

Adds a static library from the given `path` to the Apple embedded
platform project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_file**(path: `String<class_String>`{.interpreted-text role="ref"},
file: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}, remap: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_file>`{.interpreted-text
role="ref"}

Adds a custom file to be exported. `path` is the virtual path that can
be used to load the file, `file` is the binary data of the file.

When called inside
`_export_file()<class_EditorExportPlugin_private_method__export_file>`{.interpreted-text
role="ref"} and `remap` is `true`, the current file will not be
exported, but instead remapped to this custom file. `remap` is ignored
when called in other places.

`file` will not be imported, so consider using
`_customize_resource()<class_EditorExportPlugin_private_method__customize_resource>`{.interpreted-text
role="ref"} to remap imported resources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_ios_bundle_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_ios_bundle_file**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorExportPlugin_method_add_ios_bundle_file>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`add_apple_embedded_platform_bundle_file()<class_EditorExportPlugin_method_add_apple_embedded_platform_bundle_file>`{.interpreted-text
role="ref"} instead.

Adds an iOS bundle file from the given `path` to the exported project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_ios_cpp_code}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_ios_cpp_code**(code: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorExportPlugin_method_add_ios_cpp_code>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`add_apple_embedded_platform_cpp_code()<class_EditorExportPlugin_method_add_apple_embedded_platform_cpp_code>`{.interpreted-text
role="ref"} instead.

Adds C++ code to the iOS export. The final code is created from the code
appended by each active export plugin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_ios_embedded_framework}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_ios_embedded_framework**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_ios_embedded_framework>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`add_apple_embedded_platform_embedded_framework()<class_EditorExportPlugin_method_add_apple_embedded_platform_embedded_framework>`{.interpreted-text
role="ref"} instead.

Adds a dynamic library (\*.dylib, \*.framework) to Linking Phase in
iOS\'s Xcode project and embeds it into resulting binary.

\*\*Note:\*\* For static libraries (\*.a), this works the in same way as
`add_apple_embedded_platform_framework()<class_EditorExportPlugin_method_add_apple_embedded_platform_framework>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method should not be used for System libraries as
they are already present on the device.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_ios_framework}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_ios_framework**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorExportPlugin_method_add_ios_framework>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`add_apple_embedded_platform_framework()<class_EditorExportPlugin_method_add_apple_embedded_platform_framework>`{.interpreted-text
role="ref"} instead.

Adds a static library (\*.a) or a dynamic library (\*.dylib,
\*.framework) to the Linking Phase to the iOS Xcode project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_ios_linker_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_ios_linker_flags**(flags: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorExportPlugin_method_add_ios_linker_flags>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`add_apple_embedded_platform_linker_flags()<class_EditorExportPlugin_method_add_apple_embedded_platform_linker_flags>`{.interpreted-text
role="ref"} instead.

Adds linker flags for the iOS export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_ios_plist_content}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_ios_plist_content**(plist_content:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_ios_plist_content>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`add_apple_embedded_platform_plist_content()<class_EditorExportPlugin_method_add_apple_embedded_platform_plist_content>`{.interpreted-text
role="ref"} instead.

Adds additional fields to the iOS project Info.plist file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_ios_project_static_lib}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_ios_project_static_lib**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlugin_method_add_ios_project_static_lib>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`add_apple_embedded_platform_project_static_lib()<class_EditorExportPlugin_method_add_apple_embedded_platform_project_static_lib>`{.interpreted-text
role="ref"} instead.

Adds a static library from the given `path` to the iOS project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_macos_plugin_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_macos_plugin_file**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorExportPlugin_method_add_macos_plugin_file>`{.interpreted-text
role="ref"}

Adds file or directory matching `path` to `PlugIns` directory of macOS
app bundle.

\*\*Note:\*\* This is useful only for macOS exports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_add_shared_object}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_shared_object**(path: `String<class_String>`{.interpreted-text
role="ref"}, tags:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, target: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorExportPlugin_method_add_shared_object>`{.interpreted-text
role="ref"}

Adds a shared object or a directory containing only shared objects with
the given `tags` and destination `path`.

\*\*Note:\*\* In case of macOS exports, those shared objects will be
added to `Frameworks` directory of app bundle.

In case of a directory code-sign will error if you place non code object
in directory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_get_export_platform}
::: rst-class
classref-method
:::
::::

`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} **get_export_platform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_method_get_export_platform>`{.interpreted-text
role="ref"}

Returns currently used export platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_get_export_preset}
::: rst-class
classref-method
:::
::::

`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"} **get_export_preset**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_method_get_export_preset>`{.interpreted-text
role="ref"}

Returns currently used export preset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_get_option}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_option**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlugin_method_get_option>`{.interpreted-text
role="ref"}

Returns the current value of an export option supplied by
`_get_export_options()<class_EditorExportPlugin_private_method__get_export_options>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlugin_method_skip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **skip**()
`🔗<class_EditorExportPlugin_method_skip>`{.interpreted-text role="ref"}

To be called inside
`_export_file()<class_EditorExportPlugin_private_method__export_file>`{.interpreted-text
role="ref"}. Skips the current file, so it\'s not included in the
export.
