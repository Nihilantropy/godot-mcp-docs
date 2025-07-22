github_url
:   hide

# EditorResourceConversionPlugin {#class_EditorResourceConversionPlugin}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Plugin for adding custom converters from one resource format to another
in the editor resource picker context menu; for example, converting a
`StandardMaterial3D<class_StandardMaterial3D>`{.interpreted-text
role="ref"} to a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**EditorResourceConversionPlugin** is invoked when the context menu is
brought up for a resource in the editor inspector. Relevant conversion
plugins will appear as menu options to convert the given resource to a
target type.

Below shows an example of a basic plugin that will convert an
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"} to a
`PortableCompressedTexture2D<class_PortableCompressedTexture2D>`{.interpreted-text
role="ref"}.

:::: tabs
::: code-tab
gdscript

extends EditorResourceConversionPlugin

func [handles]{#handles}(resource: Resource):

:   return resource is ImageTexture

func [converts_to]{#converts_to}():

:   return \"PortableCompressedTexture2D\"

func [convert]{#convert}(itex: Resource):

:   var ptex = PortableCompressedTexture2D.new()
    ptex.create_from_image(itex.get_image(),
    PortableCompressedTexture2D.COMPRESSION_MODE_LOSSLESS) return ptex
:::
::::

To use an **EditorResourceConversionPlugin**, register it using the
`EditorPlugin.add_resource_conversion_plugin()<class_EditorPlugin_method_add_resource_conversion_plugin>`{.interpreted-text
role="ref"} method first.

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

:::: {#class_EditorResourceConversionPlugin_private_method__convert}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**\_convert**(resource: `Resource<class_Resource>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourceConversionPlugin_private_method__convert>`{.interpreted-text
role="ref"}

Takes an input `Resource<class_Resource>`{.interpreted-text role="ref"}
and converts it to the type given in
`_converts_to()<class_EditorResourceConversionPlugin_private_method__converts_to>`{.interpreted-text
role="ref"}. The returned `Resource<class_Resource>`{.interpreted-text
role="ref"} is the result of the conversion, and the input
`Resource<class_Resource>`{.interpreted-text role="ref"} remains
unchanged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourceConversionPlugin_private_method__converts_to}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **\_converts_to**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourceConversionPlugin_private_method__converts_to>`{.interpreted-text
role="ref"}

Returns the class name of the target type of
`Resource<class_Resource>`{.interpreted-text role="ref"} that this
plugin converts source resources to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourceConversionPlugin_private_method__handles}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_handles**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourceConversionPlugin_private_method__handles>`{.interpreted-text
role="ref"}

Called to determine whether a particular
`Resource<class_Resource>`{.interpreted-text role="ref"} can be
converted to the target resource type by this plugin.
