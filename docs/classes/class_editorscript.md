github_url
:   hide

# EditorScript {#class_EditorScript}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Base script that can be used to add extension functions to the editor.

::: rst-class
classref-introduction-group
:::

## Description

Scripts extending this class and implementing its
`_run()<class_EditorScript_private_method__run>`{.interpreted-text
role="ref"} method can be executed from the Script Editor\'s **File \>
Run** menu option (or by pressing `Ctrl + Shift + X`{.interpreted-text
role="kbd"}) while the editor is running. This is useful for adding
custom in-editor functionality to Godot. For more complex additions,
consider using `EditorPlugin<class_EditorPlugin>`{.interpreted-text
role="ref"}s instead.

If a script extending this class also has a global class name, it will
be included in the editor\'s command palette.

\*\*Note:\*\* Extending scripts need to have `tool` mode enabled.

\*\*Example:\*\* Running the following script prints \"Hello from the
Godot Editor!\":

::::: tabs
::: code-tab
gdscript

\@tool extends EditorScript

func [run]{#run}():

:   print(\"Hello from the Godot Editor!\")
:::

::: code-tab
csharp

using Godot;

\[Tool\] public partial class HelloEditor : EditorScript { public
override void [Run]{#run}() { GD.Print(\"Hello from the Godot
Editor!\"); } }
:::
:::::

\*\*Note:\*\* The script is run in the Editor context, which means the
output is visible in the console window started with the Editor (stdout)
instead of the usual Godot **Output** dock.

\*\*Note:\*\* EditorScript is
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"}, meaning it
is destroyed when nothing references it. This can cause errors during
asynchronous operations if there are no references to the script.

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

:::: {#class_EditorScript_private_method__run}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_run**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScript_private_method__run>`{.interpreted-text
role="ref"}

This method is executed by the Editor when **File \> Run** is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScript_method_add_root_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_root_node**(node: `Node<class_Node>`{.interpreted-text
role="ref"})
`🔗<class_EditorScript_method_add_root_node>`{.interpreted-text
role="ref"}

Makes `node` root of the currently opened scene. Only works if the scene
is empty. If the `node` is a scene instance, an inheriting scene will be
created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScript_method_get_editor_interface}
::: rst-class
classref-method
:::
::::

`EditorInterface<class_EditorInterface>`{.interpreted-text role="ref"}
**get_editor_interface**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorScript_method_get_editor_interface>`{.interpreted-text
role="ref"}

**Deprecated:**
`EditorInterface<class_EditorInterface>`{.interpreted-text role="ref"}
is a global singleton and can be accessed directly by its name.

Returns the `EditorInterface<class_EditorInterface>`{.interpreted-text
role="ref"} singleton instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorScript_method_get_scene}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **get_scene**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_EditorScript_method_get_scene>`{.interpreted-text
role="ref"}

Returns the edited (current) scene\'s root
`Node<class_Node>`{.interpreted-text role="ref"}. Equivalent of
`EditorInterface.get_edited_scene_root()<class_EditorInterface_method_get_edited_scene_root>`{.interpreted-text
role="ref"}.
