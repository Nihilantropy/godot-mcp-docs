github_url
:   hide

# EditorImportPlugin {#class_EditorImportPlugin}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Registers a custom resource importer in the editor. Use the class to
parse any file and import it as a new resource type.

::: rst-class
classref-introduction-group
:::

## Description

**EditorImportPlugin**s provide a way to extend the editor\'s resource
import functionality. Use them to import resources from custom files or
to provide alternatives to the editor\'s existing importers.

EditorImportPlugins work by associating with specific file extensions
and a resource type. See
`_get_recognized_extensions()<class_EditorImportPlugin_private_method__get_recognized_extensions>`{.interpreted-text
role="ref"} and
`_get_resource_type()<class_EditorImportPlugin_private_method__get_resource_type>`{.interpreted-text
role="ref"}. They may optionally specify some import presets that affect
the import process. EditorImportPlugins are responsible for creating the
resources and saving them in the `.godot/imported` directory (see
`ProjectSettings.application/config/use_hidden_project_data_directory<class_ProjectSettings_property_application/config/use_hidden_project_data_directory>`{.interpreted-text
role="ref"}).

Below is an example EditorImportPlugin that imports a
`Mesh<class_Mesh>`{.interpreted-text role="ref"} from a file with the
extension \".special\" or \".spec\":

::::: tabs
::: code-tab
gdscript

\@tool extends EditorImportPlugin

func [get_importer_name]{#get_importer_name}():

:   return \"my.special.plugin\"

func [get_visible_name]{#get_visible_name}():

:   return \"Special Mesh\"

func [get_recognized_extensions]{#get_recognized_extensions}():

:   return \[\"special\", \"spec\"\]

func [get_save_extension]{#get_save_extension}():

:   return \"mesh\"

func [get_resource_type]{#get_resource_type}():

:   return \"Mesh\"

func [get_preset_count]{#get_preset_count}():

:   return 1

func [get_preset_name]{#get_preset_name}(preset_index):

:   return \"Default\"

func [get_import_options]{#get_import_options}(path, preset_index):

:   return \[{\"name\": \"my_option\", \"default_value\": false}\]

func [import]{#import}(source_file, save_path, options, platform_variants, gen_files):

:   var file = FileAccess.open(source_file, FileAccess.READ) if file ==
    null: return FAILED var mesh = ArrayMesh.new() \# Fill the Mesh with
    data read in \"file\", left as an exercise to the reader.

    var filename = save_path + \".\" +
    [get_save_extension]{#get_save_extension}() return
    ResourceSaver.save(mesh, filename)
:::

::: code-tab
csharp

using Godot;

public partial class MySpecialPlugin : EditorImportPlugin { public
override string [GetImporterName]{#getimportername}() { return
\"my.special.plugin\"; }

> public override string [GetVisibleName]{#getvisiblename}() { return
> \"Special Mesh\"; }
>
> public override string\[\]
> [GetRecognizedExtensions]{#getrecognizedextensions}() { return
> \[\"special\", \"spec\"\]; }
>
> public override string [GetSaveExtension]{#getsaveextension}() {
> return \"mesh\"; }
>
> public override string [GetResourceType]{#getresourcetype}() { return
> \"Mesh\"; }
>
> public override int [GetPresetCount]{#getpresetcount}() { return 1; }
>
> public override string [GetPresetName]{#getpresetname}(int
> presetIndex) { return \"Default\"; }
>
> public override
> Godot.Collections.Array\<Godot.Collections.Dictionary\>
> [GetImportOptions]{#getimportoptions}(string path, int presetIndex) {
> return \[ new Godot.Collections.Dictionary { { \"name\", \"myOption\"
> }, { \"default_value\", false }, }, \]; }
>
> public override Error [Import]{#import}(string sourceFile, string
> savePath, Godot.Collections.Dictionary options,
> Godot.Collections.Array\<string\> platformVariants,
> Godot.Collections.Array\<string\> genFiles) { using var file =
> FileAccess.Open(sourceFile, FileAccess.ModeFlags.Read); if
> (file.GetError() != Error.Ok) { return Error.Failed; }
>
> > var mesh = new ArrayMesh(); // Fill the Mesh with data read in
> > \"file\", left as an exercise to the reader. string filename =
> > \$\"{savePath}.{[GetSaveExtension]{#getsaveextension}()}\"; return
> > ResourceSaver.Save(mesh, filename);
>
> }

}
:::
:::::

To use **EditorImportPlugin**, register it using the
`EditorPlugin.add_import_plugin()<class_EditorPlugin_method_add_import_plugin>`{.interpreted-text
role="ref"} method first.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Import plugins <../tutorials/plugins/editor/import_plugins>`{.interpreted-text
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

:::: {#class_EditorImportPlugin_private_method__can_import_threaded}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_can_import_threaded**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__can_import_threaded>`{.interpreted-text
role="ref"}

Tells whether this importer can be run in parallel on threads, or, on
the contrary, it\'s only safe for the editor to call it from the main
thread, for one file at a time.

If this method is not overridden, it will return `false` by default.

If this importer\'s implementation is thread-safe and can be run in
parallel, override this with `true` to optimize for concurrency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_format_version}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_format_version**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_format_version>`{.interpreted-text
role="ref"}

Gets the format version of this importer. Increment this version when
making incompatible changes to the format of the imported resources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_import_options}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_get_import_options**(path:
`String<class_String>`{.interpreted-text role="ref"}, preset_index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_import_options>`{.interpreted-text
role="ref"}

Gets the options and default values for the preset at this index.
Returns an Array of Dictionaries with the following keys: `name`,
`default_value`, `property_hint` (optional), `hint_string` (optional),
`usage` (optional).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_import_order}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_import_order**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_import_order>`{.interpreted-text
role="ref"}

Gets the order of this importer to be run when importing resources.
Importers with *lower* import orders will be called first, and higher
values will be called later. Use this to ensure the importer runs after
the dependencies are already imported. The default import order is `0`
unless overridden by a specific importer. See
`ImportOrder<enum_ResourceImporter_ImportOrder>`{.interpreted-text
role="ref"} for some predefined values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_importer_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_importer_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_importer_name>`{.interpreted-text
role="ref"}

Gets the unique name of the importer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_option_visibility}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_get_option_visibility**(path:
`String<class_String>`{.interpreted-text role="ref"}, option_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, options:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_option_visibility>`{.interpreted-text
role="ref"}

Gets whether the import option specified by `option_name` should be
visible in the Import dock. The default implementation always returns
`true`, making all options visible. This is mainly useful for hiding
options that depend on others if one of them is disabled.

::::: tabs
::: code-tab
gdscript

func [get_option_visibility]{#get_option_visibility}(path, option_name, options):

:   \# Only show the lossy quality setting if the compression mode is
    set to \"Lossy\". if option_name == \"compress/lossy_quality\" and
    options.has(\"compress/mode\"): return
    int(options\[\"compress/mode\"\]) == COMPRESS_LOSSY \# This is a
    constant that you set

    return true
:::

::: code-tab
csharp

public override bool [GetOptionVisibility]{#getoptionvisibility}(string
path, StringName optionName, Godot.Collections.Dictionary options) { //
Only show the lossy quality setting if the compression mode is set to
\"Lossy\". if (optionName == \"compress/lossy_quality\" &&
options.ContainsKey(\"compress/mode\")) { return
(int)options\[\"compress/mode\"\] == CompressLossy; // This is a
constant you set }

> return true;

}
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_preset_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_preset_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_preset_count>`{.interpreted-text
role="ref"}

Gets the number of initial presets defined by the plugin. Use
`_get_import_options()<class_EditorImportPlugin_private_method__get_import_options>`{.interpreted-text
role="ref"} to get the default options for the preset and
`_get_preset_name()<class_EditorImportPlugin_private_method__get_preset_name>`{.interpreted-text
role="ref"} to get the name of the preset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_preset_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_preset_name**(preset_index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_preset_name>`{.interpreted-text
role="ref"}

Gets the name of the options preset at this index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_priority}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **\_get_priority**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_priority>`{.interpreted-text
role="ref"}

Gets the priority of this plugin for the recognized extension. Higher
priority plugins will be preferred. The default priority is `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_recognized_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_recognized_extensions**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_recognized_extensions>`{.interpreted-text
role="ref"}

Gets the list of file extensions to associate with this loader
(case-insensitive). e.g. `["obj"]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_resource_type}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_resource_type**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_resource_type>`{.interpreted-text
role="ref"}

Gets the Godot resource type associated with this loader. e.g. `"Mesh"`
or `"Animation"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_save_extension}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_save_extension**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_save_extension>`{.interpreted-text
role="ref"}

Gets the extension used to save this resource in the `.godot/imported`
directory (see
`ProjectSettings.application/config/use_hidden_project_data_directory<class_ProjectSettings_property_application/config/use_hidden_project_data_directory>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__get_visible_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_visible_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__get_visible_name>`{.interpreted-text
role="ref"}

Gets the name to display in the import window. You should choose this
name as a continuation to \"Import as\", e.g. \"Import as Special
Mesh\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_private_method__import}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**\_import**(source_file: `String<class_String>`{.interpreted-text
role="ref"}, save_path: `String<class_String>`{.interpreted-text
role="ref"}, options: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, platform_variants: `Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\],
gen_files: `Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorImportPlugin_private_method__import>`{.interpreted-text
role="ref"}

Imports `source_file` with the import `options` specified. Should return
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if the import is successful, other values indicate failure.

The imported resource is expected to be saved to
`save_path + "." + _get_save_extension()`. If a different variant is
preferred for a
`feature tag <../tutorials/export/feature_tags>`{.interpreted-text
role="doc"}, save the variant to
`save_path + "." + tag + "." + _get_save_extension()` and add the
feature tag to `platform_variants`.

If additional resource files are generated in the resource filesystem
(`res://`), add their full path to `gen_files` so that the editor knows
they depend on `source_file`.

This method must be overridden to do the actual importing work. See this
class\' description for an example of overriding this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorImportPlugin_method_append_import_external_resource}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**append_import_external_resource**(path:
`String<class_String>`{.interpreted-text role="ref"}, custom_options:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} = {},
custom_importer: `String<class_String>`{.interpreted-text role="ref"} =
\"\", generator_parameters: `Variant<class_Variant>`{.interpreted-text
role="ref"} = null)
`🔗<class_EditorImportPlugin_method_append_import_external_resource>`{.interpreted-text
role="ref"}

This function can only be called during the
`_import()<class_EditorImportPlugin_private_method__import>`{.interpreted-text
role="ref"} callback and it allows manually importing resources from it.
This is useful when the imported file generates external resources that
require importing (as example, images). Custom parameters for the
\".import\" file can be passed via the `custom_options`. Additionally,
in cases where multiple importers can handle a file, the
`custom_importer` can be specified to force a specific one. This
function performs a resource import and returns immediately with a
success or error code. `generator_parameters` defines optional extra
metadata which will be stored as `generator_parameters` in the `remap`
section of the `.import` file, for example to store a md5 hash of the
source data.
