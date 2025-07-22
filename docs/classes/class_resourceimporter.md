github_url
:   hide

# ResourceImporter {#class_ResourceImporter}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`EditorImportPlugin<class_EditorImportPlugin>`{.interpreted-text
role="ref"},
`ResourceImporterBitMap<class_ResourceImporterBitMap>`{.interpreted-text
role="ref"},
`ResourceImporterBMFont<class_ResourceImporterBMFont>`{.interpreted-text
role="ref"},
`ResourceImporterCSVTranslation<class_ResourceImporterCSVTranslation>`{.interpreted-text
role="ref"},
`ResourceImporterDynamicFont<class_ResourceImporterDynamicFont>`{.interpreted-text
role="ref"},
`ResourceImporterImage<class_ResourceImporterImage>`{.interpreted-text
role="ref"},
`ResourceImporterImageFont<class_ResourceImporterImageFont>`{.interpreted-text
role="ref"},
`ResourceImporterLayeredTexture<class_ResourceImporterLayeredTexture>`{.interpreted-text
role="ref"},
`ResourceImporterMP3<class_ResourceImporterMP3>`{.interpreted-text
role="ref"},
`ResourceImporterOBJ<class_ResourceImporterOBJ>`{.interpreted-text
role="ref"},
`ResourceImporterOggVorbis<class_ResourceImporterOggVorbis>`{.interpreted-text
role="ref"},
`ResourceImporterScene<class_ResourceImporterScene>`{.interpreted-text
role="ref"},
`ResourceImporterShaderFile<class_ResourceImporterShaderFile>`{.interpreted-text
role="ref"},
`ResourceImporterSVG<class_ResourceImporterSVG>`{.interpreted-text
role="ref"},
`ResourceImporterTexture<class_ResourceImporterTexture>`{.interpreted-text
role="ref"},
`ResourceImporterTextureAtlas<class_ResourceImporterTextureAtlas>`{.interpreted-text
role="ref"},
`ResourceImporterWAV<class_ResourceImporterWAV>`{.interpreted-text
role="ref"}

Base class for resource importers.

::: rst-class
classref-introduction-group
:::

## Description

This is the base class for Godot\'s resource importers. To implement
your own resource importers using editor plugins, see
`EditorImportPlugin<class_EditorImportPlugin>`{.interpreted-text
role="ref"}.

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

## Enumerations

:::: {#enum_ResourceImporter_ImportOrder}
::: rst-class
classref-enumeration
:::
::::

enum **ImportOrder**:
`🔗<enum_ResourceImporter_ImportOrder>`{.interpreted-text role="ref"}

:::: {#class_ResourceImporter_constant_IMPORT_ORDER_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`ImportOrder<enum_ResourceImporter_ImportOrder>`{.interpreted-text
role="ref"} **IMPORT_ORDER_DEFAULT** = `0`

The default import order.

:::: {#class_ResourceImporter_constant_IMPORT_ORDER_SCENE}
::: rst-class
classref-enumeration-constant
:::
::::

`ImportOrder<enum_ResourceImporter_ImportOrder>`{.interpreted-text
role="ref"} **IMPORT_ORDER_SCENE** = `100`

The import order for scenes, which ensures scenes are imported *after*
all other core resources such as textures. Custom importers should
generally have an import order lower than `100` to avoid issues when
importing scenes that rely on custom resources.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ResourceImporter_private_method__get_build_dependencies}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_build_dependencies**(path:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ResourceImporter_private_method__get_build_dependencies>`{.interpreted-text
role="ref"}

Called when the engine compilation profile editor wants to check what
build options an imported resource needs. For example,
`ResourceImporterDynamicFont<class_ResourceImporterDynamicFont>`{.interpreted-text
role="ref"} has a property called
`ResourceImporterDynamicFont.multichannel_signed_distance_field<class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"}, that depends on the engine to be build with the \"msdfgen\"
module. If that resource happened to be a custom one, it would be
handled like this:

    func _get_build_dependencies(path):
        var resource = load(path)
        var dependencies = PackedStringArray()

        if resource.multichannel_signed_distance_field:
            dependencies.push_back("module_msdfgen_enabled")

        return dependencies
