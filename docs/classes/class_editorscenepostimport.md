github_url
:   hide

# EditorScenePostImport {#class_EditorScenePostImport}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Post-processes scenes after import.

::: rst-class
classref-introduction-group
:::

## Description

Imported scenes can be automatically modified right after import by
setting their **Custom Script** Import property to a `tool` script that
inherits from this class.

The
`_post_import()<class_EditorScenePostImport_private_method__post_import>`{.interpreted-text
role="ref"} callback receives the imported scene\'s root node and
returns the modified version of the scene:

::::: tabs
::: code-tab
gdscript

\@tool \# Needed so it runs in editor. extends EditorScenePostImport

\# This sample changes all node names. \# Called right after the scene
is imported and gets the root node. func
[post_import]{#post_import}(scene): \# Change all node names to
\"modified\_\[oldnodename\]\" iterate(scene) return scene \# Remember to
return the imported scene

func iterate(node):

:   

    if node != null:

    :   node.name = \"modified\_\" + node.name for child in
        node.get_children(): iterate(child)
:::

::: code-tab
csharp

using Godot;

// This sample changes all node names. // Called right after the scene
is imported and gets the root node. \[Tool\] public partial class
NodeRenamer : EditorScenePostImport { public override GodotObject
[PostImport]{#postimport}(Node scene) { // Change all node names to
\"modified\_\[oldnodename\]\" Iterate(scene); return scene; // Remember
to return the imported scene }

> public void Iterate(Node node) { if (node != null) { node.Name =
> \$\"modified\_{node.Name}\"; foreach (Node child in
> node.GetChildren()) { Iterate(child); } } }

}
:::
:::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Importing 3D scenes: Configuration: Using import scripts for
  automation](../tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html#using-import-scripts-for-automation)

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

:::: {#class_EditorScenePostImport_private_method__post_import}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**\_post_import**(scene: `Node<class_Node>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImport_private_method__post_import>`{.interpreted-text
role="ref"}

Called after the scene was imported. This method must return the
modified version of the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScenePostImport_method_get_source_file}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_source_file**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScenePostImport_method_get_source_file>`{.interpreted-text
role="ref"}

Returns the source file path which got imported (e.g.
`res://scene.dae`).
