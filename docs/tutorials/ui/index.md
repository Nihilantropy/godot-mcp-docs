allow_comments
:   False

# User interface (UI) {#doc_user_interface}

In this section of the tutorial we explain the basics of creating a
graphical user interface (GUI) in Godot.

## UI building blocks

Like everything else in Godot the user interface is built using nodes,
specifically `Control <class_Control>`{.interpreted-text role="ref"}
nodes. There are many different types of controls which are useful for
creating specific types of GUIs. For simplicity we can separate them
into two groups: content and layout.

Typical content controls include:

- `Buttons <class_Button>`{.interpreted-text role="ref"}
- `Labels <class_Label>`{.interpreted-text role="ref"}
- `LineEdits <class_LineEdit>`{.interpreted-text role="ref"} and
  `TextEdits <class_TextEdit>`{.interpreted-text role="ref"}

Typical layout controls include:

- `BoxContainers <class_BoxContainer>`{.interpreted-text role="ref"}
- `MarginContainers <class_MarginContainer>`{.interpreted-text
  role="ref"}
- `ScrollContainers <class_ScrollContainer>`{.interpreted-text
  role="ref"}
- `TabContainers <class_TabContainer>`{.interpreted-text role="ref"}
- `Popups <class_Popup>`{.interpreted-text role="ref"}

The following pages explain the basics of using such controls.

::: {#toc-gui-basics .toctree maxdepth="1"}
size_and_anchors gui_containers custom_gui_controls gui_navigation
control_node_gallery
:::

## GUI skinning and themes

Godot features an in-depth skinning/theming system for control nodes.
The pages in this section explain the benefits of that system and how to
set it up in your projects.

::: {#toc-gui-skinning .toctree maxdepth="1"}
gui_skinning gui_using_theme_editor gui_theme_type_variations
gui_using_fonts
:::

## Control node tutorials

The following articles cover specific details of using particular
control nodes.

::: {#toc-control-nodes-tutorials .toctree maxdepth="1"}
bbcode_in_richtextlabel
:::
