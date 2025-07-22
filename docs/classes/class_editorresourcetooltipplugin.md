github_url
:   hide

# EditorResourceTooltipPlugin {#class_EditorResourceTooltipPlugin}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A plugin that advanced tooltip for its handled resource type.

::: rst-class
classref-introduction-group
:::

## Description

Resource tooltip plugins are used by
`FileSystemDock<class_FileSystemDock>`{.interpreted-text role="ref"} to
generate customized tooltips for specific resources. E.g. tooltip for a
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} displays a
bigger preview and the texture\'s dimensions.

A plugin must be first registered with
`FileSystemDock.add_resource_tooltip_plugin()<class_FileSystemDock_method_add_resource_tooltip_plugin>`{.interpreted-text
role="ref"}. When the user hovers a resource in filesystem dock which is
handled by the plugin,
`_make_tooltip_for_path()<class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path>`{.interpreted-text
role="ref"} is called to create the tooltip. It works similarly to
`Control._make_custom_tooltip()<class_Control_private_method__make_custom_tooltip>`{.interpreted-text
role="ref"}.

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

:::: {#class_EditorResourceTooltipPlugin_private_method__handles}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_handles**(type:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourceTooltipPlugin_private_method__handles>`{.interpreted-text
role="ref"}

Return `true` if the plugin is going to handle the given
`Resource<class_Resource>`{.interpreted-text role="ref"} `type`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**\_make_tooltip_for_path**(path:
`String<class_String>`{.interpreted-text role="ref"}, metadata:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}, base:
`Control<class_Control>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path>`{.interpreted-text
role="ref"}

Create and return a tooltip that will be displayed when the user hovers
a resource under the given `path` in filesystem dock.

The `metadata` dictionary is provided by preview generator (see
`EditorResourcePreviewGenerator._generate()<class_EditorResourcePreviewGenerator_private_method__generate>`{.interpreted-text
role="ref"}).

`base` is the base default tooltip, which is a
`VBoxContainer<class_VBoxContainer>`{.interpreted-text role="ref"} with
a file name, type and size labels. If another plugin handled the same
file type, `base` will be output from the previous plugin. For best
result, make sure the base tooltip is part of the returned
`Control<class_Control>`{.interpreted-text role="ref"}.

\*\*Note:\*\* It\'s unadvised to use
`ResourceLoader.load()<class_ResourceLoader_method_load>`{.interpreted-text
role="ref"}, especially with heavy resources like models or textures,
because it will make the editor unresponsive when creating the tooltip.
You can use
`request_thumbnail()<class_EditorResourceTooltipPlugin_method_request_thumbnail>`{.interpreted-text
role="ref"} if you want to display a preview in your tooltip.

\*\*Note:\*\* If you decide to discard the `base`, make sure to call
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"}, because it\'s not freed automatically.

    func _make_tooltip_for_path(path, metadata, base):
        var t_rect = TextureRect.new()
        request_thumbnail(path, t_rect)
        base.add_child(t_rect) # The TextureRect will appear at the bottom of the tooltip.
        return base

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourceTooltipPlugin_method_request_thumbnail}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**request_thumbnail**(path: `String<class_String>`{.interpreted-text
role="ref"}, control: `TextureRect<class_TextureRect>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourceTooltipPlugin_method_request_thumbnail>`{.interpreted-text
role="ref"}

Requests a thumbnail for the given
`TextureRect<class_TextureRect>`{.interpreted-text role="ref"}. The
thumbnail is created asynchronously by
`EditorResourcePreview<class_EditorResourcePreview>`{.interpreted-text
role="ref"} and automatically set when available.
