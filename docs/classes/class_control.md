github_url
:   hide

# Control {#class_Control}

**Inherits:** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `BaseButton<class_BaseButton>`{.interpreted-text
role="ref"}, `ColorRect<class_ColorRect>`{.interpreted-text role="ref"},
`Container<class_Container>`{.interpreted-text role="ref"},
`GraphEdit<class_GraphEdit>`{.interpreted-text role="ref"},
`ItemList<class_ItemList>`{.interpreted-text role="ref"},
`Label<class_Label>`{.interpreted-text role="ref"},
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"},
`MenuBar<class_MenuBar>`{.interpreted-text role="ref"},
`NinePatchRect<class_NinePatchRect>`{.interpreted-text role="ref"},
`Panel<class_Panel>`{.interpreted-text role="ref"},
`Range<class_Range>`{.interpreted-text role="ref"},
`ReferenceRect<class_ReferenceRect>`{.interpreted-text role="ref"},
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"},
`Separator<class_Separator>`{.interpreted-text role="ref"},
`TabBar<class_TabBar>`{.interpreted-text role="ref"},
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"},
`TextureRect<class_TextureRect>`{.interpreted-text role="ref"},
`Tree<class_Tree>`{.interpreted-text role="ref"},
`VideoStreamPlayer<class_VideoStreamPlayer>`{.interpreted-text
role="ref"}

Base class for all GUI controls. Adapts its position and size based on
its parent control.

::: rst-class
classref-introduction-group
:::

## Description

Base class for all UI-related nodes. **Control** features a bounding
rectangle that defines its extents, an anchor position relative to its
parent control or the current viewport, and offsets relative to the
anchor. The offsets update automatically when the node, any of its
parents, or the screen size change.

For more information on Godot\'s UI system, anchors, offsets, and
containers, see the related tutorials in the manual. To build flexible
UIs, you\'ll need a mix of UI elements that inherit from **Control** and
`Container<class_Container>`{.interpreted-text role="ref"} nodes.

\*\*Note:\*\* Since both `Node2D<class_Node2D>`{.interpreted-text
role="ref"} and **Control** inherit from
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}, they share
several concepts from the class such as the
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} and
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} properties.

\*\*User Interface nodes and input\*\*

Godot propagates input events via viewports. Each
`Viewport<class_Viewport>`{.interpreted-text role="ref"} is responsible
for propagating `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}s to their child nodes. As the
`SceneTree.root<class_SceneTree_property_root>`{.interpreted-text
role="ref"} is a `Window<class_Window>`{.interpreted-text role="ref"},
this already happens automatically for all UI elements in your game.

Input events are propagated through the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} from the root
node to all child nodes by calling
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}. For UI elements specifically, it makes more sense to
override the virtual method
`_gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}, which filters out unrelated input events, such as by
checking z-order,
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"}, focus, or if the event was inside of the control\'s
bounding box.

Call
`accept_event()<class_Control_method_accept_event>`{.interpreted-text
role="ref"} so no other node receives the event. Once you accept an
input, it becomes handled so
`Node._unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"} will not process it.

Only one **Control** node can be in focus. Only the node in focus will
receive events. To get the focus, call
`grab_focus()<class_Control_method_grab_focus>`{.interpreted-text
role="ref"}. **Control** nodes lose focus when another node grabs it, or
if you hide the node in focus.

Sets
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} to
`MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>`{.interpreted-text
role="ref"} to tell a **Control** node to ignore mouse or touch events.
You\'ll need it if you place an icon on top of a button.

`Theme<class_Theme>`{.interpreted-text role="ref"} resources change the
control\'s appearance. The
`theme<class_Control_property_theme>`{.interpreted-text role="ref"} of a
**Control** node affects all of its direct and indirect children (as
long as a chain of controls is uninterrupted). To override some of the
theme items, call one of the `add_theme_*_override` methods, like
`add_theme_font_override()<class_Control_method_add_theme_font_override>`{.interpreted-text
role="ref"}. You can also override theme items in the Inspector.

\*\*Note:\*\* Theme items are *not*
`Object<class_Object>`{.interpreted-text role="ref"} properties. This
means you can\'t access their values using
`Object.get()<class_Object_method_get>`{.interpreted-text role="ref"}
and `Object.set()<class_Object_method_set>`{.interpreted-text
role="ref"}. Instead, use the `get_theme_*` and `add_theme_*_override`
methods provided by this class.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `GUI documentation index <../tutorials/ui/index>`{.interpreted-text
  role="doc"}
- `Custom drawing in 2D <../tutorials/2d/custom_drawing_in_2d>`{.interpreted-text
  role="doc"}
- `Control node gallery <../tutorials/ui/control_node_gallery>`{.interpreted-text
  role="doc"}
- `Multiple resolutions <../tutorials/rendering/multiple_resolutions>`{.interpreted-text
  role="doc"}
- [All GUI
  Demos](https://github.com/godotengine/godot-demo-projects/tree/master/gui)

::: rst-class
classref-reftable-group
:::

## Properties

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

## Signals

:::: {#class_Control_signal_focus_entered}
::: rst-class
classref-signal
:::
::::

**focus_entered**()
`🔗<class_Control_signal_focus_entered>`{.interpreted-text role="ref"}

Emitted when the node gains focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_signal_focus_exited}
::: rst-class
classref-signal
:::
::::

**focus_exited**()
`🔗<class_Control_signal_focus_exited>`{.interpreted-text role="ref"}

Emitted when the node loses focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_signal_gui_input}
::: rst-class
classref-signal
:::
::::

**gui_input**(event: `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}) `🔗<class_Control_signal_gui_input>`{.interpreted-text
role="ref"}

Emitted when the node receives an
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_signal_minimum_size_changed}
::: rst-class
classref-signal
:::
::::

**minimum_size_changed**()
`🔗<class_Control_signal_minimum_size_changed>`{.interpreted-text
role="ref"}

Emitted when the node\'s minimum size changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_signal_mouse_entered}
::: rst-class
classref-signal
:::
::::

**mouse_entered**()
`🔗<class_Control_signal_mouse_entered>`{.interpreted-text role="ref"}

Emitted when the mouse cursor enters the control\'s (or any child
control\'s) visible area, that is not occluded behind other Controls or
Windows, provided its
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} lets the event reach it and regardless if it\'s currently
focused or not.

\*\*Note:\*\*
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} doesn\'t affect, which Control receives the signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_signal_mouse_exited}
::: rst-class
classref-signal
:::
::::

**mouse_exited**()
`🔗<class_Control_signal_mouse_exited>`{.interpreted-text role="ref"}

Emitted when the mouse cursor leaves the control\'s (and all child
control\'s) visible area, that is not occluded behind other Controls or
Windows, provided its
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} lets the event reach it and regardless if it\'s currently
focused or not.

\*\*Note:\*\*
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} doesn\'t affect, which Control receives the signal.

\*\*Note:\*\* If you want to check whether the mouse truly left the
area, ignoring any top nodes, you can use code like this:

    func _on_mouse_exited():
        if not Rect2(Vector2(), size).has_point(get_local_mouse_position()):
            # Not hovering over area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_signal_resized}
::: rst-class
classref-signal
:::
::::

**resized**() `🔗<class_Control_signal_resized>`{.interpreted-text
role="ref"}

Emitted when the control changes size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_signal_size_flags_changed}
::: rst-class
classref-signal
:::
::::

**size_flags_changed**()
`🔗<class_Control_signal_size_flags_changed>`{.interpreted-text
role="ref"}

Emitted when one of the size flags changes. See
`size_flags_horizontal<class_Control_property_size_flags_horizontal>`{.interpreted-text
role="ref"} and
`size_flags_vertical<class_Control_property_size_flags_vertical>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_signal_theme_changed}
::: rst-class
classref-signal
:::
::::

**theme_changed**()
`🔗<class_Control_signal_theme_changed>`{.interpreted-text role="ref"}

Emitted when the
`NOTIFICATION_THEME_CHANGED<class_Control_constant_NOTIFICATION_THEME_CHANGED>`{.interpreted-text
role="ref"} notification is sent.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Control_FocusMode}
::: rst-class
classref-enumeration
:::
::::

enum **FocusMode**: `🔗<enum_Control_FocusMode>`{.interpreted-text
role="ref"}

:::: {#class_Control_constant_FOCUS_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
**FOCUS_NONE** = `0`

The node cannot grab focus. Use with
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_FOCUS_CLICK}
::: rst-class
classref-enumeration-constant
:::
::::

`FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
**FOCUS_CLICK** = `1`

The node can only grab focus on mouse clicks. Use with
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_FOCUS_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
**FOCUS_ALL** = `2`

The node can grab focus on mouse click, using the arrows and the Tab
keys on the keyboard, or using the D-pad buttons on a gamepad. Use with
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_FOCUS_ACCESSIBILITY}
::: rst-class
classref-enumeration-constant
:::
::::

`FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
**FOCUS_ACCESSIBILITY** = `3`

The node can grab focus only when screen reader is active. Use with
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_FocusBehaviorRecursive}
::: rst-class
classref-enumeration
:::
::::

enum **FocusBehaviorRecursive**:
`🔗<enum_Control_FocusBehaviorRecursive>`{.interpreted-text role="ref"}

:::: {#class_Control_constant_FOCUS_BEHAVIOR_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`FocusBehaviorRecursive<enum_Control_FocusBehaviorRecursive>`{.interpreted-text
role="ref"} **FOCUS_BEHAVIOR_INHERITED** = `0`

Inherits the
`focus_behavior_recursive<class_Control_property_focus_behavior_recursive>`{.interpreted-text
role="ref"} from the parent control. If there is no parent control, this
is the same as
`FOCUS_BEHAVIOR_ENABLED<class_Control_constant_FOCUS_BEHAVIOR_ENABLED>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_FOCUS_BEHAVIOR_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`FocusBehaviorRecursive<enum_Control_FocusBehaviorRecursive>`{.interpreted-text
role="ref"} **FOCUS_BEHAVIOR_DISABLED** = `1`

Prevents the control from getting focused.
`get_focus_mode_with_override()<class_Control_method_get_focus_mode_with_override>`{.interpreted-text
role="ref"} will return
`FOCUS_NONE<class_Control_constant_FOCUS_NONE>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_FOCUS_BEHAVIOR_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`FocusBehaviorRecursive<enum_Control_FocusBehaviorRecursive>`{.interpreted-text
role="ref"} **FOCUS_BEHAVIOR_ENABLED** = `2`

Allows the control to be focused, depending on the
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}. This can be used to ignore the parent\'s
`focus_behavior_recursive<class_Control_property_focus_behavior_recursive>`{.interpreted-text
role="ref"}.
`get_focus_mode_with_override()<class_Control_method_get_focus_mode_with_override>`{.interpreted-text
role="ref"} will return the
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_MouseBehaviorRecursive}
::: rst-class
classref-enumeration
:::
::::

enum **MouseBehaviorRecursive**:
`🔗<enum_Control_MouseBehaviorRecursive>`{.interpreted-text role="ref"}

:::: {#class_Control_constant_MOUSE_BEHAVIOR_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseBehaviorRecursive<enum_Control_MouseBehaviorRecursive>`{.interpreted-text
role="ref"} **MOUSE_BEHAVIOR_INHERITED** = `0`

Inherits the
`mouse_behavior_recursive<class_Control_property_mouse_behavior_recursive>`{.interpreted-text
role="ref"} from the parent control. If there is no parent control, this
is the same as
`MOUSE_BEHAVIOR_ENABLED<class_Control_constant_MOUSE_BEHAVIOR_ENABLED>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_MOUSE_BEHAVIOR_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseBehaviorRecursive<enum_Control_MouseBehaviorRecursive>`{.interpreted-text
role="ref"} **MOUSE_BEHAVIOR_DISABLED** = `1`

Prevents the control from receiving mouse input.
`get_mouse_filter_with_override()<class_Control_method_get_mouse_filter_with_override>`{.interpreted-text
role="ref"} will return
`MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_MOUSE_BEHAVIOR_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseBehaviorRecursive<enum_Control_MouseBehaviorRecursive>`{.interpreted-text
role="ref"} **MOUSE_BEHAVIOR_ENABLED** = `2`

Allows the control to be receive mouse input, depending on the
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"}. This can be used to ignore the parent\'s
`mouse_behavior_recursive<class_Control_property_mouse_behavior_recursive>`{.interpreted-text
role="ref"}.
`get_mouse_filter_with_override()<class_Control_method_get_mouse_filter_with_override>`{.interpreted-text
role="ref"} will return the
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_CursorShape}
::: rst-class
classref-enumeration
:::
::::

enum **CursorShape**: `🔗<enum_Control_CursorShape>`{.interpreted-text
role="ref"}

:::: {#class_Control_constant_CURSOR_ARROW}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_ARROW** = `0`

Show the system\'s arrow mouse cursor when the user hovers the node. Use
with
`mouse_default_cursor_shape<class_Control_property_mouse_default_cursor_shape>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_CURSOR_IBEAM}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_IBEAM** = `1`

Show the system\'s I-beam mouse cursor when the user hovers the node.
The I-beam pointer has a shape similar to \"I\". It tells the user they
can highlight or insert text.

:::: {#class_Control_constant_CURSOR_POINTING_HAND}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_POINTING_HAND** = `2`

Show the system\'s pointing hand mouse cursor when the user hovers the
node.

:::: {#class_Control_constant_CURSOR_CROSS}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_CROSS** = `3`

Show the system\'s cross mouse cursor when the user hovers the node.

:::: {#class_Control_constant_CURSOR_WAIT}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_WAIT** = `4`

Show the system\'s wait mouse cursor when the user hovers the node.
Often an hourglass.

:::: {#class_Control_constant_CURSOR_BUSY}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_BUSY** = `5`

Show the system\'s busy mouse cursor when the user hovers the node.
Often an arrow with a small hourglass.

:::: {#class_Control_constant_CURSOR_DRAG}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_DRAG** = `6`

Show the system\'s drag mouse cursor, often a closed fist or a cross
symbol, when the user hovers the node. It tells the user they\'re
currently dragging an item, like a node in the Scene dock.

:::: {#class_Control_constant_CURSOR_CAN_DROP}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_CAN_DROP** = `7`

Show the system\'s drop mouse cursor when the user hovers the node. It
can be an open hand. It tells the user they can drop an item they\'re
currently grabbing, like a node in the Scene dock.

:::: {#class_Control_constant_CURSOR_FORBIDDEN}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_FORBIDDEN** = `8`

Show the system\'s forbidden mouse cursor when the user hovers the node.
Often a crossed circle.

:::: {#class_Control_constant_CURSOR_VSIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_VSIZE** = `9`

Show the system\'s vertical resize mouse cursor when the user hovers the
node. A double-headed vertical arrow. It tells the user they can resize
the window or the panel vertically.

:::: {#class_Control_constant_CURSOR_HSIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_HSIZE** = `10`

Show the system\'s horizontal resize mouse cursor when the user hovers
the node. A double-headed horizontal arrow. It tells the user they can
resize the window or the panel horizontally.

:::: {#class_Control_constant_CURSOR_BDIAGSIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_BDIAGSIZE** = `11`

Show the system\'s window resize mouse cursor when the user hovers the
node. The cursor is a double-headed arrow that goes from the bottom left
to the top right. It tells the user they can resize the window or the
panel both horizontally and vertically.

:::: {#class_Control_constant_CURSOR_FDIAGSIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_FDIAGSIZE** = `12`

Show the system\'s window resize mouse cursor when the user hovers the
node. The cursor is a double-headed arrow that goes from the top left to
the bottom right, the opposite of
`CURSOR_BDIAGSIZE<class_Control_constant_CURSOR_BDIAGSIZE>`{.interpreted-text
role="ref"}. It tells the user they can resize the window or the panel
both horizontally and vertically.

:::: {#class_Control_constant_CURSOR_MOVE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_MOVE** = `13`

Show the system\'s move mouse cursor when the user hovers the node. It
shows 2 double-headed arrows at a 90 degree angle. It tells the user
they can move a UI element freely.

:::: {#class_Control_constant_CURSOR_VSPLIT}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_VSPLIT** = `14`

Show the system\'s vertical split mouse cursor when the user hovers the
node. On Windows, it\'s the same as
`CURSOR_VSIZE<class_Control_constant_CURSOR_VSIZE>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_CURSOR_HSPLIT}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_HSPLIT** = `15`

Show the system\'s horizontal split mouse cursor when the user hovers
the node. On Windows, it\'s the same as
`CURSOR_HSIZE<class_Control_constant_CURSOR_HSIZE>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_CURSOR_HELP}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_HELP** = `16`

Show the system\'s help mouse cursor when the user hovers the node, a
question mark.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_LayoutPreset}
::: rst-class
classref-enumeration
:::
::::

enum **LayoutPreset**: `🔗<enum_Control_LayoutPreset>`{.interpreted-text
role="ref"}

:::: {#class_Control_constant_PRESET_TOP_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_TOP_LEFT** = `0`

Snap all 4 anchors to the top-left of the parent control\'s bounds. Use
with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_TOP_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_TOP_RIGHT** = `1`

Snap all 4 anchors to the top-right of the parent control\'s bounds. Use
with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_BOTTOM_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_BOTTOM_LEFT** = `2`

Snap all 4 anchors to the bottom-left of the parent control\'s bounds.
Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_BOTTOM_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_BOTTOM_RIGHT** = `3`

Snap all 4 anchors to the bottom-right of the parent control\'s bounds.
Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_CENTER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_CENTER_LEFT** = `4`

Snap all 4 anchors to the center of the left edge of the parent
control\'s bounds. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_CENTER_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_CENTER_TOP** = `5`

Snap all 4 anchors to the center of the top edge of the parent
control\'s bounds. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_CENTER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_CENTER_RIGHT** = `6`

Snap all 4 anchors to the center of the right edge of the parent
control\'s bounds. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_CENTER_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_CENTER_BOTTOM** = `7`

Snap all 4 anchors to the center of the bottom edge of the parent
control\'s bounds. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_CENTER** = `8`

Snap all 4 anchors to the center of the parent control\'s bounds. Use
with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_LEFT_WIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_LEFT_WIDE** = `9`

Snap all 4 anchors to the left edge of the parent control. The left
offset becomes relative to the left edge and the top offset relative to
the top left corner of the node\'s parent. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_TOP_WIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_TOP_WIDE** = `10`

Snap all 4 anchors to the top edge of the parent control. The left
offset becomes relative to the top left corner, the top offset relative
to the top edge, and the right offset relative to the top right corner
of the node\'s parent. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_RIGHT_WIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_RIGHT_WIDE** = `11`

Snap all 4 anchors to the right edge of the parent control. The right
offset becomes relative to the right edge and the top offset relative to
the top right corner of the node\'s parent. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_BOTTOM_WIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_BOTTOM_WIDE** = `12`

Snap all 4 anchors to the bottom edge of the parent control. The left
offset becomes relative to the bottom left corner, the bottom offset
relative to the bottom edge, and the right offset relative to the bottom
right corner of the node\'s parent. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_VCENTER_WIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_VCENTER_WIDE** = `13`

Snap all 4 anchors to a vertical line that cuts the parent control in
half. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_HCENTER_WIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_HCENTER_WIDE** = `14`

Snap all 4 anchors to a horizontal line that cuts the parent control in
half. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_PRESET_FULL_RECT}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
**PRESET_FULL_RECT** = `15`

Snap all 4 anchors to the respective corners of the parent control. Set
all 4 offsets to 0 after you applied this preset and the **Control**
will fit its parent control. Use with
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_LayoutPresetMode}
::: rst-class
classref-enumeration
:::
::::

enum **LayoutPresetMode**:
`🔗<enum_Control_LayoutPresetMode>`{.interpreted-text role="ref"}

:::: {#class_Control_constant_PRESET_MODE_MINSIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPresetMode<enum_Control_LayoutPresetMode>`{.interpreted-text
role="ref"} **PRESET_MODE_MINSIZE** = `0`

The control will be resized to its minimum size.

:::: {#class_Control_constant_PRESET_MODE_KEEP_WIDTH}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPresetMode<enum_Control_LayoutPresetMode>`{.interpreted-text
role="ref"} **PRESET_MODE_KEEP_WIDTH** = `1`

The control\'s width will not change.

:::: {#class_Control_constant_PRESET_MODE_KEEP_HEIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPresetMode<enum_Control_LayoutPresetMode>`{.interpreted-text
role="ref"} **PRESET_MODE_KEEP_HEIGHT** = `2`

The control\'s height will not change.

:::: {#class_Control_constant_PRESET_MODE_KEEP_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutPresetMode<enum_Control_LayoutPresetMode>`{.interpreted-text
role="ref"} **PRESET_MODE_KEEP_SIZE** = `3`

The control\'s size will not change.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_SizeFlags}
::: rst-class
classref-enumeration
:::
::::

flags **SizeFlags**: `🔗<enum_Control_SizeFlags>`{.interpreted-text
role="ref"}

:::: {#class_Control_constant_SIZE_SHRINK_BEGIN}
::: rst-class
classref-enumeration-constant
:::
::::

`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"}
**SIZE_SHRINK_BEGIN** = `0`

Tells the parent `Container<class_Container>`{.interpreted-text
role="ref"} to align the node with its start, either the top or the left
edge. It is mutually exclusive with
`SIZE_FILL<class_Control_constant_SIZE_FILL>`{.interpreted-text
role="ref"} and other shrink size flags, but can be used with
`SIZE_EXPAND<class_Control_constant_SIZE_EXPAND>`{.interpreted-text
role="ref"} in some containers. Use with
`size_flags_horizontal<class_Control_property_size_flags_horizontal>`{.interpreted-text
role="ref"} and
`size_flags_vertical<class_Control_property_size_flags_vertical>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Setting this flag is equal to not having any size flags.

:::: {#class_Control_constant_SIZE_FILL}
::: rst-class
classref-enumeration-constant
:::
::::

`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"}
**SIZE_FILL** = `1`

Tells the parent `Container<class_Container>`{.interpreted-text
role="ref"} to expand the bounds of this node to fill all the available
space without pushing any other node. It is mutually exclusive with
shrink size flags. Use with
`size_flags_horizontal<class_Control_property_size_flags_horizontal>`{.interpreted-text
role="ref"} and
`size_flags_vertical<class_Control_property_size_flags_vertical>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_SIZE_EXPAND}
::: rst-class
classref-enumeration-constant
:::
::::

`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"}
**SIZE_EXPAND** = `2`

Tells the parent `Container<class_Container>`{.interpreted-text
role="ref"} to let this node take all the available space on the axis
you flag. If multiple neighboring nodes are set to expand, they\'ll
share the space based on their stretch ratio. See
`size_flags_stretch_ratio<class_Control_property_size_flags_stretch_ratio>`{.interpreted-text
role="ref"}. Use with
`size_flags_horizontal<class_Control_property_size_flags_horizontal>`{.interpreted-text
role="ref"} and
`size_flags_vertical<class_Control_property_size_flags_vertical>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_SIZE_EXPAND_FILL}
::: rst-class
classref-enumeration-constant
:::
::::

`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"}
**SIZE_EXPAND_FILL** = `3`

Sets the node\'s size flags to both fill and expand. See
`SIZE_FILL<class_Control_constant_SIZE_FILL>`{.interpreted-text
role="ref"} and
`SIZE_EXPAND<class_Control_constant_SIZE_EXPAND>`{.interpreted-text
role="ref"} for more information.

:::: {#class_Control_constant_SIZE_SHRINK_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"}
**SIZE_SHRINK_CENTER** = `4`

Tells the parent `Container<class_Container>`{.interpreted-text
role="ref"} to center the node in the available space. It is mutually
exclusive with
`SIZE_FILL<class_Control_constant_SIZE_FILL>`{.interpreted-text
role="ref"} and other shrink size flags, but can be used with
`SIZE_EXPAND<class_Control_constant_SIZE_EXPAND>`{.interpreted-text
role="ref"} in some containers. Use with
`size_flags_horizontal<class_Control_property_size_flags_horizontal>`{.interpreted-text
role="ref"} and
`size_flags_vertical<class_Control_property_size_flags_vertical>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_SIZE_SHRINK_END}
::: rst-class
classref-enumeration-constant
:::
::::

`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"}
**SIZE_SHRINK_END** = `8`

Tells the parent `Container<class_Container>`{.interpreted-text
role="ref"} to align the node with its end, either the bottom or the
right edge. It is mutually exclusive with
`SIZE_FILL<class_Control_constant_SIZE_FILL>`{.interpreted-text
role="ref"} and other shrink size flags, but can be used with
`SIZE_EXPAND<class_Control_constant_SIZE_EXPAND>`{.interpreted-text
role="ref"} in some containers. Use with
`size_flags_horizontal<class_Control_property_size_flags_horizontal>`{.interpreted-text
role="ref"} and
`size_flags_vertical<class_Control_property_size_flags_vertical>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_MouseFilter}
::: rst-class
classref-enumeration
:::
::::

enum **MouseFilter**: `🔗<enum_Control_MouseFilter>`{.interpreted-text
role="ref"}

:::: {#class_Control_constant_MOUSE_FILTER_STOP}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseFilter<enum_Control_MouseFilter>`{.interpreted-text role="ref"}
**MOUSE_FILTER_STOP** = `0`

The control will receive mouse movement input events and mouse button
input events if clicked on through
`_gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}. The control will also receive the
`mouse_entered<class_Control_signal_mouse_entered>`{.interpreted-text
role="ref"} and
`mouse_exited<class_Control_signal_mouse_exited>`{.interpreted-text
role="ref"} signals. These events are automatically marked as handled,
and they will not propagate further to other controls. This also results
in blocking signals in other controls.

:::: {#class_Control_constant_MOUSE_FILTER_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseFilter<enum_Control_MouseFilter>`{.interpreted-text role="ref"}
**MOUSE_FILTER_PASS** = `1`

The control will receive mouse movement input events and mouse button
input events if clicked on through
`_gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}. The control will also receive the
`mouse_entered<class_Control_signal_mouse_entered>`{.interpreted-text
role="ref"} and
`mouse_exited<class_Control_signal_mouse_exited>`{.interpreted-text
role="ref"} signals.

If this control does not handle the event, the event will propagate up
to its parent control if it has one. The event is bubbled up the node
hierarchy until it reaches a
non-`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}, a
control with
`MOUSE_FILTER_STOP<class_Control_constant_MOUSE_FILTER_STOP>`{.interpreted-text
role="ref"}, or a `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} with
`CanvasItem.top_level<class_CanvasItem_property_top_level>`{.interpreted-text
role="ref"} enabled. This will allow signals to fire in all controls it
reaches. If no control handled it, the event will be passed to
`Node._shortcut_input()<class_Node_private_method__shortcut_input>`{.interpreted-text
role="ref"} for further processing.

:::: {#class_Control_constant_MOUSE_FILTER_IGNORE}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseFilter<enum_Control_MouseFilter>`{.interpreted-text role="ref"}
**MOUSE_FILTER_IGNORE** = `2`

The control will not receive any mouse movement input events nor mouse
button input events through
`_gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}. The control will also not receive the
`mouse_entered<class_Control_signal_mouse_entered>`{.interpreted-text
role="ref"} nor
`mouse_exited<class_Control_signal_mouse_exited>`{.interpreted-text
role="ref"} signals. This will not block other controls from receiving
these events or firing the signals. Ignored events will not be handled
automatically. If a child has
`MOUSE_FILTER_PASS<class_Control_constant_MOUSE_FILTER_PASS>`{.interpreted-text
role="ref"} and an event was passed to this control, the event will
further propagate up to the control\'s parent.

\*\*Note:\*\* If the control has received
`mouse_entered<class_Control_signal_mouse_entered>`{.interpreted-text
role="ref"} but not
`mouse_exited<class_Control_signal_mouse_exited>`{.interpreted-text
role="ref"}, changing the
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} to
`MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>`{.interpreted-text
role="ref"} will cause
`mouse_exited<class_Control_signal_mouse_exited>`{.interpreted-text
role="ref"} to be emitted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_GrowDirection}
::: rst-class
classref-enumeration
:::
::::

enum **GrowDirection**:
`🔗<enum_Control_GrowDirection>`{.interpreted-text role="ref"}

:::: {#class_Control_constant_GROW_DIRECTION_BEGIN}
::: rst-class
classref-enumeration-constant
:::
::::

`GrowDirection<enum_Control_GrowDirection>`{.interpreted-text
role="ref"} **GROW_DIRECTION_BEGIN** = `0`

The control will grow to the left or top to make up if its minimum size
is changed to be greater than its current size on the respective axis.

:::: {#class_Control_constant_GROW_DIRECTION_END}
::: rst-class
classref-enumeration-constant
:::
::::

`GrowDirection<enum_Control_GrowDirection>`{.interpreted-text
role="ref"} **GROW_DIRECTION_END** = `1`

The control will grow to the right or bottom to make up if its minimum
size is changed to be greater than its current size on the respective
axis.

:::: {#class_Control_constant_GROW_DIRECTION_BOTH}
::: rst-class
classref-enumeration-constant
:::
::::

`GrowDirection<enum_Control_GrowDirection>`{.interpreted-text
role="ref"} **GROW_DIRECTION_BOTH** = `2`

The control will grow in both directions equally to make up if its
minimum size is changed to be greater than its current size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_Anchor}
::: rst-class
classref-enumeration
:::
::::

enum **Anchor**: `🔗<enum_Control_Anchor>`{.interpreted-text role="ref"}

:::: {#class_Control_constant_ANCHOR_BEGIN}
::: rst-class
classref-enumeration-constant
:::
::::

`Anchor<enum_Control_Anchor>`{.interpreted-text role="ref"}
**ANCHOR_BEGIN** = `0`

Snaps one of the 4 anchor\'s sides to the origin of the node\'s `Rect`,
in the top left. Use it with one of the `anchor_*` member variables,
like `anchor_left<class_Control_property_anchor_left>`{.interpreted-text
role="ref"}. To change all 4 anchors at once, use
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_ANCHOR_END}
::: rst-class
classref-enumeration-constant
:::
::::

`Anchor<enum_Control_Anchor>`{.interpreted-text role="ref"}
**ANCHOR_END** = `1`

Snaps one of the 4 anchor\'s sides to the end of the node\'s `Rect`, in
the bottom right. Use it with one of the `anchor_*` member variables,
like `anchor_left<class_Control_property_anchor_left>`{.interpreted-text
role="ref"}. To change all 4 anchors at once, use
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_LayoutDirection}
::: rst-class
classref-enumeration
:::
::::

enum **LayoutDirection**:
`🔗<enum_Control_LayoutDirection>`{.interpreted-text role="ref"}

:::: {#class_Control_constant_LAYOUT_DIRECTION_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_INHERITED** = `0`

Automatic layout direction, determined from the parent control layout
direction.

:::: {#class_Control_constant_LAYOUT_DIRECTION_APPLICATION_LOCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_APPLICATION_LOCALE** = `1`

Automatic layout direction, determined from the current locale.
Right-to-left layout direction is automatically used for languages that
require it such as Arabic and Hebrew, but only if a valid translation
file is loaded for the given language (unless said language is
configured as a fallback in
`ProjectSettings.internationalization/locale/fallback<class_ProjectSettings_property_internationalization/locale/fallback>`{.interpreted-text
role="ref"}). For all other languages (or if no valid translation file
is found by Godot), left-to-right layout direction is used. If using
`TextServerFallback<class_TextServerFallback>`{.interpreted-text
role="ref"}
(`ProjectSettings.internationalization/rendering/text_driver<class_ProjectSettings_property_internationalization/rendering/text_driver>`{.interpreted-text
role="ref"}), left-to-right layout direction is always used regardless
of the language. Right-to-left layout direction can also be forced using
`ProjectSettings.internationalization/rendering/force_right_to_left_layout_direction<class_ProjectSettings_property_internationalization/rendering/force_right_to_left_layout_direction>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_LAYOUT_DIRECTION_LTR}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_LTR** = `2`

Left-to-right layout direction.

:::: {#class_Control_constant_LAYOUT_DIRECTION_RTL}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_RTL** = `3`

Right-to-left layout direction.

:::: {#class_Control_constant_LAYOUT_DIRECTION_SYSTEM_LOCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_SYSTEM_LOCALE** = `4`

Automatic layout direction, determined from the system locale.
Right-to-left layout direction is automatically used for languages that
require it such as Arabic and Hebrew, but only if a valid translation
file is loaded for the given language.. For all other languages (or if
no valid translation file is found by Godot), left-to-right layout
direction is used. If using
`TextServerFallback<class_TextServerFallback>`{.interpreted-text
role="ref"}
(`ProjectSettings.internationalization/rendering/text_driver<class_ProjectSettings_property_internationalization/rendering/text_driver>`{.interpreted-text
role="ref"}), left-to-right layout direction is always used regardless
of the language.

:::: {#class_Control_constant_LAYOUT_DIRECTION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_MAX** = `5`

Represents the size of the
`LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
role="ref"} enum.

:::: {#class_Control_constant_LAYOUT_DIRECTION_LOCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
role="ref"} **LAYOUT_DIRECTION_LOCALE** = `1`

**Deprecated:** Use
`LAYOUT_DIRECTION_APPLICATION_LOCALE<class_Control_constant_LAYOUT_DIRECTION_APPLICATION_LOCALE>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Control_TextDirection}
::: rst-class
classref-enumeration
:::
::::

enum **TextDirection**:
`🔗<enum_Control_TextDirection>`{.interpreted-text role="ref"}

:::: {#class_Control_constant_TEXT_DIRECTION_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **TEXT_DIRECTION_INHERITED** = `3`

Text writing direction is the same as layout direction.

:::: {#class_Control_constant_TEXT_DIRECTION_AUTO}
::: rst-class
classref-enumeration-constant
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **TEXT_DIRECTION_AUTO** = `0`

Automatic text writing direction, determined from the current locale and
text content.

:::: {#class_Control_constant_TEXT_DIRECTION_LTR}
::: rst-class
classref-enumeration-constant
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **TEXT_DIRECTION_LTR** = `1`

Left-to-right text writing direction.

:::: {#class_Control_constant_TEXT_DIRECTION_RTL}
::: rst-class
classref-enumeration-constant
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **TEXT_DIRECTION_RTL** = `2`

Right-to-left text writing direction.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Control_constant_NOTIFICATION_RESIZED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_RESIZED** = `40`
`🔗<class_Control_constant_NOTIFICATION_RESIZED>`{.interpreted-text
role="ref"}

Sent when the node changes size. Use
`size<class_Control_property_size>`{.interpreted-text role="ref"} to get
the new size.

:::: {#class_Control_constant_NOTIFICATION_MOUSE_ENTER}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_MOUSE_ENTER** = `41`
`🔗<class_Control_constant_NOTIFICATION_MOUSE_ENTER>`{.interpreted-text
role="ref"}

Sent when the mouse cursor enters the control\'s (or any child
control\'s) visible area, that is not occluded behind other Controls or
Windows, provided its
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} lets the event reach it and regardless if it\'s currently
focused or not.

\*\*Note:\*\*
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} doesn\'t affect which Control receives the notification.

See also
`NOTIFICATION_MOUSE_ENTER_SELF<class_Control_constant_NOTIFICATION_MOUSE_ENTER_SELF>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_NOTIFICATION_MOUSE_EXIT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_MOUSE_EXIT** = `42`
`🔗<class_Control_constant_NOTIFICATION_MOUSE_EXIT>`{.interpreted-text
role="ref"}

Sent when the mouse cursor leaves the control\'s (and all child
control\'s) visible area, that is not occluded behind other Controls or
Windows, provided its
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} lets the event reach it and regardless if it\'s currently
focused or not.

\*\*Note:\*\*
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} doesn\'t affect which Control receives the notification.

See also
`NOTIFICATION_MOUSE_EXIT_SELF<class_Control_constant_NOTIFICATION_MOUSE_EXIT_SELF>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_NOTIFICATION_MOUSE_ENTER_SELF}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_MOUSE_ENTER_SELF** = `60`
`🔗<class_Control_constant_NOTIFICATION_MOUSE_ENTER_SELF>`{.interpreted-text
role="ref"}

**Experimental:** The reason this notification is sent may change in the
future.

Sent when the mouse cursor enters the control\'s visible area, that is
not occluded behind other Controls or Windows, provided its
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} lets the event reach it and regardless if it\'s currently
focused or not.

\*\*Note:\*\*
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} doesn\'t affect which Control receives the notification.

See also
`NOTIFICATION_MOUSE_ENTER<class_Control_constant_NOTIFICATION_MOUSE_ENTER>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_NOTIFICATION_MOUSE_EXIT_SELF}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_MOUSE_EXIT_SELF** = `61`
`🔗<class_Control_constant_NOTIFICATION_MOUSE_EXIT_SELF>`{.interpreted-text
role="ref"}

**Experimental:** The reason this notification is sent may change in the
future.

Sent when the mouse cursor leaves the control\'s visible area, that is
not occluded behind other Controls or Windows, provided its
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} lets the event reach it and regardless if it\'s currently
focused or not.

\*\*Note:\*\*
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} doesn\'t affect which Control receives the notification.

See also
`NOTIFICATION_MOUSE_EXIT<class_Control_constant_NOTIFICATION_MOUSE_EXIT>`{.interpreted-text
role="ref"}.

:::: {#class_Control_constant_NOTIFICATION_FOCUS_ENTER}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_FOCUS_ENTER** = `43`
`🔗<class_Control_constant_NOTIFICATION_FOCUS_ENTER>`{.interpreted-text
role="ref"}

Sent when the node grabs focus.

:::: {#class_Control_constant_NOTIFICATION_FOCUS_EXIT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_FOCUS_EXIT** = `44`
`🔗<class_Control_constant_NOTIFICATION_FOCUS_EXIT>`{.interpreted-text
role="ref"}

Sent when the node loses focus.

:::: {#class_Control_constant_NOTIFICATION_THEME_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_THEME_CHANGED** = `45`
`🔗<class_Control_constant_NOTIFICATION_THEME_CHANGED>`{.interpreted-text
role="ref"}

Sent when the node needs to refresh its theme items. This happens in one
of the following cases:

- The `theme<class_Control_property_theme>`{.interpreted-text
  role="ref"} property is changed on this node or any of its ancestors.
- The
  `theme_type_variation<class_Control_property_theme_type_variation>`{.interpreted-text
  role="ref"} property is changed on this node.
- One of the node\'s theme property overrides is changed.
- The node enters the scene tree.

\*\*Note:\*\* As an optimization, this notification won\'t be sent from
changes that occur while this node is outside of the scene tree.
Instead, all of the theme item updates can be applied at once when the
node enters the scene tree.

\*\*Note:\*\* This notification is received alongside
`Node.NOTIFICATION_ENTER_TREE<class_Node_constant_NOTIFICATION_ENTER_TREE>`{.interpreted-text
role="ref"}, so if you are instantiating a scene, the child nodes will
not be initialized yet. You can use it to setup theming for this node,
child nodes created from script, or if you want to access child nodes
added in the editor, make sure the node is ready using
`Node.is_node_ready()<class_Node_method_is_node_ready>`{.interpreted-text
role="ref"}.

    func _notification(what):
        if what == NOTIFICATION_THEME_CHANGED:
            if not is_node_ready():
                await ready # Wait until ready signal.
            $Label.add_theme_color_override("font_color", Color.YELLOW)

:::: {#class_Control_constant_NOTIFICATION_SCROLL_BEGIN}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_SCROLL_BEGIN** = `47`
`🔗<class_Control_constant_NOTIFICATION_SCROLL_BEGIN>`{.interpreted-text
role="ref"}

Sent when this node is inside a
`ScrollContainer<class_ScrollContainer>`{.interpreted-text role="ref"}
which has begun being scrolled when dragging the scrollable area *with a
touch event*. This notification is *not* sent when scrolling by dragging
the scrollbar, scrolling with the mouse wheel or scrolling with
keyboard/gamepad events.

\*\*Note:\*\* This signal is only emitted on Android or iOS, or on
desktop/web platforms when
`ProjectSettings.input_devices/pointing/emulate_touch_from_mouse<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>`{.interpreted-text
role="ref"} is enabled.

:::: {#class_Control_constant_NOTIFICATION_SCROLL_END}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_SCROLL_END** = `48`
`🔗<class_Control_constant_NOTIFICATION_SCROLL_END>`{.interpreted-text
role="ref"}

Sent when this node is inside a
`ScrollContainer<class_ScrollContainer>`{.interpreted-text role="ref"}
which has stopped being scrolled when dragging the scrollable area *with
a touch event*. This notification is *not* sent when scrolling by
dragging the scrollbar, scrolling with the mouse wheel or scrolling with
keyboard/gamepad events.

\*\*Note:\*\* This signal is only emitted on Android or iOS, or on
desktop/web platforms when
`ProjectSettings.input_devices/pointing/emulate_touch_from_mouse<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>`{.interpreted-text
role="ref"} is enabled.

:::: {#class_Control_constant_NOTIFICATION_LAYOUT_DIRECTION_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_LAYOUT_DIRECTION_CHANGED** = `49`
`🔗<class_Control_constant_NOTIFICATION_LAYOUT_DIRECTION_CHANGED>`{.interpreted-text
role="ref"}

Sent when the control layout direction is changed from LTR or RTL or
vice versa. This notification is propagated to child Control nodes as
result of a change to
`layout_direction<class_Control_property_layout_direction>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Control_property_accessibility_controls_nodes}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text role="ref"}\]
**accessibility_controls_nodes** = `[]`
`🔗<class_Control_property_accessibility_controls_nodes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessibility_controls_nodes**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\] **get_accessibility_controls_nodes**()

The paths to the nodes which are controlled by this node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_accessibility_described_by_nodes}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text role="ref"}\]
**accessibility_described_by_nodes** = `[]`
`🔗<class_Control_property_accessibility_described_by_nodes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessibility_described_by_nodes**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\] **get_accessibility_described_by_nodes**()

The paths to the nodes which are describing this node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_accessibility_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**accessibility_description** = `""`
`🔗<class_Control_property_accessibility_description>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessibility_description**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_accessibility_description**()

The human-readable node description that is reported to assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_accessibility_flow_to_nodes}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text role="ref"}\]
**accessibility_flow_to_nodes** = `[]`
`🔗<class_Control_property_accessibility_flow_to_nodes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessibility_flow_to_nodes**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\] **get_accessibility_flow_to_nodes**()

The paths to the nodes which this node flows into.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_accessibility_labeled_by_nodes}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text role="ref"}\]
**accessibility_labeled_by_nodes** = `[]`
`🔗<class_Control_property_accessibility_labeled_by_nodes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessibility_labeled_by_nodes**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`NodePath<class_NodePath>`{.interpreted-text
  role="ref"}\] **get_accessibility_labeled_by_nodes**()

The paths to the nodes which label this node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_accessibility_live}
::: rst-class
classref-property
:::
::::

`AccessibilityLiveMode<enum_DisplayServer_AccessibilityLiveMode>`{.interpreted-text
role="ref"} **accessibility_live** = `0`
`🔗<class_Control_property_accessibility_live>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessibility_live**(value:
  `AccessibilityLiveMode<enum_DisplayServer_AccessibilityLiveMode>`{.interpreted-text
  role="ref"})
- `AccessibilityLiveMode<enum_DisplayServer_AccessibilityLiveMode>`{.interpreted-text
  role="ref"} **get_accessibility_live**()

The mode with which a live region updates. A live region is a
`Node<class_Node>`{.interpreted-text role="ref"} that is updated as a
result of an external event when the user\'s focus may be elsewhere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_accessibility_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**accessibility_name** = `""`
`🔗<class_Control_property_accessibility_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accessibility_name**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_accessibility_name**()

The human-readable node name that is reported to assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_anchor_bottom}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anchor_bottom** =
`0.0` `🔗<class_Control_property_anchor_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"}
  **get_anchor**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Anchors the bottom edge of the node to the origin, the center, or the
end of its parent control. It changes how the bottom offset updates when
the node moves or changes size. You can use one of the
`Anchor<enum_Control_Anchor>`{.interpreted-text role="ref"} constants
for convenience.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_anchor_left}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anchor_left** =
`0.0` `🔗<class_Control_property_anchor_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"}
  **get_anchor**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Anchors the left edge of the node to the origin, the center or the end
of its parent control. It changes how the left offset updates when the
node moves or changes size. You can use one of the
`Anchor<enum_Control_Anchor>`{.interpreted-text role="ref"} constants
for convenience.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_anchor_right}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anchor_right** =
`0.0` `🔗<class_Control_property_anchor_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"}
  **get_anchor**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Anchors the right edge of the node to the origin, the center or the end
of its parent control. It changes how the right offset updates when the
node moves or changes size. You can use one of the
`Anchor<enum_Control_Anchor>`{.interpreted-text role="ref"} constants
for convenience.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_anchor_top}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anchor_top** =
`0.0` `🔗<class_Control_property_anchor_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"}
  **get_anchor**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Anchors the top edge of the node to the origin, the center or the end of
its parent control. It changes how the top offset updates when the node
moves or changes size. You can use one of the
`Anchor<enum_Control_Anchor>`{.interpreted-text role="ref"} constants
for convenience.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_auto_translate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **auto_translate**
`🔗<class_Control_property_auto_translate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_translate**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_auto_translating**()

**Deprecated:** Use
`Node.auto_translate_mode<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"} and
`Node.can_auto_translate()<class_Node_method_can_auto_translate>`{.interpreted-text
role="ref"} instead.

Toggles if any text should automatically change to its translated
version depending on the current locale.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_clip_contents}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **clip_contents** =
`false` `🔗<class_Control_property_clip_contents>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_clip_contents**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_clipping_contents**()

Enables whether rendering of
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} based
children should be clipped to this control\'s rectangle. If `true`,
parts of a child which would be visibly outside of this control\'s
rectangle will not be rendered and won\'t receive input.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_custom_minimum_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**custom_minimum_size** = `Vector2(0, 0)`
`🔗<class_Control_property_custom_minimum_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_minimum_size**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_custom_minimum_size**()

The minimum size of the node\'s bounding rectangle. If you set it to a
value greater than `(0, 0)`, the node\'s bounding rectangle will always
have at least this size. Note that **Control** nodes have their internal
minimum size returned by
`get_minimum_size()<class_Control_method_get_minimum_size>`{.interpreted-text
role="ref"}. It depends on the control\'s contents, like text, textures,
or style boxes. The actual minimum size is the maximum value of this
property and the internal minimum size (see
`get_combined_minimum_size()<class_Control_method_get_combined_minimum_size>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_focus_behavior_recursive}
::: rst-class
classref-property
:::
::::

`FocusBehaviorRecursive<enum_Control_FocusBehaviorRecursive>`{.interpreted-text
role="ref"} **focus_behavior_recursive** = `0`
`🔗<class_Control_property_focus_behavior_recursive>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focus_behavior_recursive**(value:
  `FocusBehaviorRecursive<enum_Control_FocusBehaviorRecursive>`{.interpreted-text
  role="ref"})
- `FocusBehaviorRecursive<enum_Control_FocusBehaviorRecursive>`{.interpreted-text
  role="ref"} **get_focus_behavior_recursive**()

Determines which controls can be focused together with
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}. See
`get_focus_mode_with_override()<class_Control_method_get_focus_mode_with_override>`{.interpreted-text
role="ref"}. Since the default behavior is
`FOCUS_BEHAVIOR_INHERITED<class_Control_constant_FOCUS_BEHAVIOR_INHERITED>`{.interpreted-text
role="ref"}, this can be used to prevent all children controls from
getting focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_focus_mode}
::: rst-class
classref-property
:::
::::

`FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
**focus_mode** = `0`
`🔗<class_Control_property_focus_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focus_mode**(value:
  `FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"})
- `FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
  **get_focus_mode**()

Determines which controls can be focused. Only one control can be
focused at a time, and the focused control will receive keyboard,
gamepad, and mouse events in
`_gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}. Use
`get_focus_mode_with_override()<class_Control_method_get_focus_mode_with_override>`{.interpreted-text
role="ref"} to determine if a control can grab focus, since
`focus_behavior_recursive<class_Control_property_focus_behavior_recursive>`{.interpreted-text
role="ref"} also affects it. See also
`grab_focus()<class_Control_method_grab_focus>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_focus_neighbor_bottom}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**focus_neighbor_bottom** = `NodePath("")`
`🔗<class_Control_property_focus_neighbor_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focus_neighbor**(side:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"},
  neighbor: `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_focus_neighbor**(side:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Tells Godot which node it should give focus to if the user presses the
down arrow on the keyboard or down on a gamepad by default. You can
change the key by editing the
`ProjectSettings.input/ui_down<class_ProjectSettings_property_input/ui_down>`{.interpreted-text
role="ref"} input action. The node must be a **Control**. If this
property is not set, Godot will give focus to the closest **Control** to
the bottom of this one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_focus_neighbor_left}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**focus_neighbor_left** = `NodePath("")`
`🔗<class_Control_property_focus_neighbor_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focus_neighbor**(side:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"},
  neighbor: `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_focus_neighbor**(side:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Tells Godot which node it should give focus to if the user presses the
left arrow on the keyboard or left on a gamepad by default. You can
change the key by editing the
`ProjectSettings.input/ui_left<class_ProjectSettings_property_input/ui_left>`{.interpreted-text
role="ref"} input action. The node must be a **Control**. If this
property is not set, Godot will give focus to the closest **Control** to
the left of this one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_focus_neighbor_right}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**focus_neighbor_right** = `NodePath("")`
`🔗<class_Control_property_focus_neighbor_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focus_neighbor**(side:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"},
  neighbor: `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_focus_neighbor**(side:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Tells Godot which node it should give focus to if the user presses the
right arrow on the keyboard or right on a gamepad by default. You can
change the key by editing the
`ProjectSettings.input/ui_right<class_ProjectSettings_property_input/ui_right>`{.interpreted-text
role="ref"} input action. The node must be a **Control**. If this
property is not set, Godot will give focus to the closest **Control** to
the right of this one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_focus_neighbor_top}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**focus_neighbor_top** = `NodePath("")`
`🔗<class_Control_property_focus_neighbor_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focus_neighbor**(side:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"},
  neighbor: `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_focus_neighbor**(side:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Tells Godot which node it should give focus to if the user presses the
top arrow on the keyboard or top on a gamepad by default. You can change
the key by editing the
`ProjectSettings.input/ui_up<class_ProjectSettings_property_input/ui_up>`{.interpreted-text
role="ref"} input action. The node must be a **Control**. If this
property is not set, Godot will give focus to the closest **Control** to
the top of this one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_focus_next}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **focus_next**
= `NodePath("")`
`🔗<class_Control_property_focus_next>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focus_next**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_focus_next**()

Tells Godot which node it should give focus to if the user presses
`Tab`{.interpreted-text role="kbd"} on a keyboard by default. You can
change the key by editing the
`ProjectSettings.input/ui_focus_next<class_ProjectSettings_property_input/ui_focus_next>`{.interpreted-text
role="ref"} input action.

If this property is not set, Godot will select a \"best guess\" based on
surrounding nodes in the scene tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_focus_previous}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**focus_previous** = `NodePath("")`
`🔗<class_Control_property_focus_previous>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focus_previous**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_focus_previous**()

Tells Godot which node it should give focus to if the user presses
`Shift + Tab`{.interpreted-text role="kbd"} on a keyboard by default.
You can change the key by editing the
`ProjectSettings.input/ui_focus_prev<class_ProjectSettings_property_input/ui_focus_prev>`{.interpreted-text
role="ref"} input action.

If this property is not set, Godot will select a \"best guess\" based on
surrounding nodes in the scene tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_global_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**global_position**
`🔗<class_Control_property_global_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_global_position**()

The node\'s global position, relative to the world (usually to the
`CanvasLayer<class_CanvasLayer>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_grow_horizontal}
::: rst-class
classref-property
:::
::::

`GrowDirection<enum_Control_GrowDirection>`{.interpreted-text
role="ref"} **grow_horizontal** = `1`
`🔗<class_Control_property_grow_horizontal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_h_grow_direction**(value:
  `GrowDirection<enum_Control_GrowDirection>`{.interpreted-text
  role="ref"})
- `GrowDirection<enum_Control_GrowDirection>`{.interpreted-text
  role="ref"} **get_h_grow_direction**()

Controls the direction on the horizontal axis in which the control
should grow if its horizontal minimum size is changed to be greater than
its current size, as the control always has to be at least the minimum
size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_grow_vertical}
::: rst-class
classref-property
:::
::::

`GrowDirection<enum_Control_GrowDirection>`{.interpreted-text
role="ref"} **grow_vertical** = `1`
`🔗<class_Control_property_grow_vertical>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_grow_direction**(value:
  `GrowDirection<enum_Control_GrowDirection>`{.interpreted-text
  role="ref"})
- `GrowDirection<enum_Control_GrowDirection>`{.interpreted-text
  role="ref"} **get_v_grow_direction**()

Controls the direction on the vertical axis in which the control should
grow if its vertical minimum size is changed to be greater than its
current size, as the control always has to be at least the minimum size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_layout_direction}
::: rst-class
classref-property
:::
::::

`LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
role="ref"} **layout_direction** = `0`
`🔗<class_Control_property_layout_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_layout_direction**(value:
  `LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
  role="ref"})
- `LayoutDirection<enum_Control_LayoutDirection>`{.interpreted-text
  role="ref"} **get_layout_direction**()

Controls layout direction and text writing direction. Right-to-left
layouts are necessary for certain languages (e.g. Arabic and Hebrew).
See also
`is_layout_rtl()<class_Control_method_is_layout_rtl>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_localize_numeral_system}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**localize_numeral_system** = `true`
`🔗<class_Control_property_localize_numeral_system>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_localize_numeral_system**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_localizing_numeral_system**()

If `true`, automatically converts code line numbers, list indices,
`SpinBox<class_SpinBox>`{.interpreted-text role="ref"} and
`ProgressBar<class_ProgressBar>`{.interpreted-text role="ref"} values
from the Western Arabic (0..9) to the numeral systems used in current
locale.

\*\*Note:\*\* Numbers within the text are not automatically converted,
it can be done manually, using
`TextServer.format_number()<class_TextServer_method_format_number>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_mouse_behavior_recursive}
::: rst-class
classref-property
:::
::::

`MouseBehaviorRecursive<enum_Control_MouseBehaviorRecursive>`{.interpreted-text
role="ref"} **mouse_behavior_recursive** = `0`
`🔗<class_Control_property_mouse_behavior_recursive>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mouse_behavior_recursive**(value:
  `MouseBehaviorRecursive<enum_Control_MouseBehaviorRecursive>`{.interpreted-text
  role="ref"})
- `MouseBehaviorRecursive<enum_Control_MouseBehaviorRecursive>`{.interpreted-text
  role="ref"} **get_mouse_behavior_recursive**()

Determines which controls can receive mouse input together with
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"}. See
`get_mouse_filter_with_override()<class_Control_method_get_mouse_filter_with_override>`{.interpreted-text
role="ref"}. Since the default behavior is
`MOUSE_BEHAVIOR_INHERITED<class_Control_constant_MOUSE_BEHAVIOR_INHERITED>`{.interpreted-text
role="ref"}, this can be used to prevent all children controls from
receiving mouse input.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_mouse_default_cursor_shape}
::: rst-class
classref-property
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**mouse_default_cursor_shape** = `0`
`🔗<class_Control_property_mouse_default_cursor_shape>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_cursor_shape**(value:
  `CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"})
- `CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
  **get_default_cursor_shape**()

The default cursor shape for this control. Useful for Godot plugins and
applications or games that use the system\'s mouse cursors.

\*\*Note:\*\* On Linux, shapes may vary depending on the cursor theme of
the system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_mouse_filter}
::: rst-class
classref-property
:::
::::

`MouseFilter<enum_Control_MouseFilter>`{.interpreted-text role="ref"}
**mouse_filter** = `0`
`🔗<class_Control_property_mouse_filter>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mouse_filter**(value:
  `MouseFilter<enum_Control_MouseFilter>`{.interpreted-text role="ref"})
- `MouseFilter<enum_Control_MouseFilter>`{.interpreted-text role="ref"}
  **get_mouse_filter**()

Determines which controls will be able to receive mouse button input
events through
`_gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"} and the
`mouse_entered<class_Control_signal_mouse_entered>`{.interpreted-text
role="ref"}, and
`mouse_exited<class_Control_signal_mouse_exited>`{.interpreted-text
role="ref"} signals. Also determines how these events should be
propagated. See the constants to learn what each does. Use
`get_mouse_filter_with_override()<class_Control_method_get_mouse_filter_with_override>`{.interpreted-text
role="ref"} to determine if a control can receive mouse input, since
`mouse_behavior_recursive<class_Control_property_mouse_behavior_recursive>`{.interpreted-text
role="ref"} also affects it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_mouse_force_pass_scroll_events}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**mouse_force_pass_scroll_events** = `true`
`🔗<class_Control_property_mouse_force_pass_scroll_events>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_force_pass_scroll_events**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_force_pass_scroll_events**()

When enabled, scroll wheel events processed by
`_gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"} will be passed to the parent control even if
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} is set to
`MOUSE_FILTER_STOP<class_Control_constant_MOUSE_FILTER_STOP>`{.interpreted-text
role="ref"}.

You should disable it on the root of your UI if you do not want scroll
events to go to the
`Node._unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"} processing.

\*\*Note:\*\* Because this property defaults to `true`, this allows
nested scrollable containers to work out of the box.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_offset_bottom}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **offset_bottom** =
`0.0` `🔗<class_Control_property_offset_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"}, offset: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_offset**(offset:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Distance between the node\'s bottom edge and its parent control, based
on
`anchor_bottom<class_Control_property_anchor_bottom>`{.interpreted-text
role="ref"}.

Offsets are often controlled by one or multiple parent
`Container<class_Container>`{.interpreted-text role="ref"} nodes, so you
should not modify them manually if your node is a direct child of a
`Container<class_Container>`{.interpreted-text role="ref"}. Offsets
update automatically when you move or resize the node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_offset_left}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **offset_left** =
`0.0` `🔗<class_Control_property_offset_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"}, offset: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_offset**(offset:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Distance between the node\'s left edge and its parent control, based on
`anchor_left<class_Control_property_anchor_left>`{.interpreted-text
role="ref"}.

Offsets are often controlled by one or multiple parent
`Container<class_Container>`{.interpreted-text role="ref"} nodes, so you
should not modify them manually if your node is a direct child of a
`Container<class_Container>`{.interpreted-text role="ref"}. Offsets
update automatically when you move or resize the node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_offset_right}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **offset_right** =
`0.0` `🔗<class_Control_property_offset_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"}, offset: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_offset**(offset:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Distance between the node\'s right edge and its parent control, based on
`anchor_right<class_Control_property_anchor_right>`{.interpreted-text
role="ref"}.

Offsets are often controlled by one or multiple parent
`Container<class_Container>`{.interpreted-text role="ref"} nodes, so you
should not modify them manually if your node is a direct child of a
`Container<class_Container>`{.interpreted-text role="ref"}. Offsets
update automatically when you move or resize the node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_offset_top}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **offset_top** =
`0.0` `🔗<class_Control_property_offset_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
  role="ref"}, offset: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_offset**(offset:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Distance between the node\'s top edge and its parent control, based on
`anchor_top<class_Control_property_anchor_top>`{.interpreted-text
role="ref"}.

Offsets are often controlled by one or multiple parent
`Container<class_Container>`{.interpreted-text role="ref"} nodes, so you
should not modify them manually if your node is a direct child of a
`Container<class_Container>`{.interpreted-text role="ref"}. Offsets
update automatically when you move or resize the node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_pivot_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **pivot_offset**
= `Vector2(0, 0)`
`🔗<class_Control_property_pivot_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pivot_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_pivot_offset**()

By default, the node\'s pivot is its top-left corner. When you change
its `rotation<class_Control_property_rotation>`{.interpreted-text
role="ref"} or `scale<class_Control_property_scale>`{.interpreted-text
role="ref"}, it will rotate or scale around this pivot. Set this
property to `size<class_Control_property_size>`{.interpreted-text
role="ref"} / 2 to pivot around the Control\'s center.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **position** =
`Vector2(0, 0)` `🔗<class_Control_property_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_position**()

The node\'s position, relative to its containing node. It corresponds to
the rectangle\'s top-left corner. The property is not affected by
`pivot_offset<class_Control_property_pivot_offset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_rotation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **rotation** = `0.0`
`🔗<class_Control_property_rotation>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_rotation**()

The node\'s rotation around its pivot, in radians. See
`pivot_offset<class_Control_property_pivot_offset>`{.interpreted-text
role="ref"} to change the pivot\'s position.

\*\*Note:\*\* This property is edited in the inspector in degrees. If
you want to use degrees in a script, use
`rotation_degrees<class_Control_property_rotation_degrees>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_rotation_degrees}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **rotation_degrees**
`🔗<class_Control_property_rotation_degrees>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rotation_degrees**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_rotation_degrees**()

Helper property to access
`rotation<class_Control_property_rotation>`{.interpreted-text
role="ref"} in degrees instead of radians.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_scale}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **scale** =
`Vector2(1, 1)` `🔗<class_Control_property_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scale**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_scale**()

The node\'s scale, relative to its
`size<class_Control_property_size>`{.interpreted-text role="ref"}.
Change this property to scale the node around its
`pivot_offset<class_Control_property_pivot_offset>`{.interpreted-text
role="ref"}. The Control\'s tooltip will also scale according to this
value.

\*\*Note:\*\* This property is mainly intended to be used for animation
purposes. To support multiple resolutions in your project, use an
appropriate viewport stretch mode as described in the
`documentation <../tutorials/rendering/multiple_resolutions>`{.interpreted-text
role="doc"} instead of scaling Controls individually.

\*\*Note:\*\*
`FontFile.oversampling<class_FontFile_property_oversampling>`{.interpreted-text
role="ref"} does *not* take **Control**
`scale<class_Control_property_scale>`{.interpreted-text role="ref"} into
account. This means that scaling up/down will cause bitmap fonts and
rasterized (non-MSDF) dynamic fonts to appear blurry or pixelated. To
ensure text remains crisp regardless of scale, you can enable MSDF font
rendering by enabling
`ProjectSettings.gui/theme/default_font_multichannel_signed_distance_field<class_ProjectSettings_property_gui/theme/default_font_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} (applies to the default project font only), or enabling
**Multichannel Signed Distance Field** in the import options of a
DynamicFont for custom fonts. On system fonts,
`SystemFont.multichannel_signed_distance_field<class_SystemFont_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} can be enabled in the inspector.

\*\*Note:\*\* If the Control node is a child of a
`Container<class_Container>`{.interpreted-text role="ref"} node, the
scale will be reset to `Vector2(1, 1)` when the scene is instantiated.
To set the Control\'s scale when it\'s instantiated, wait for one frame
using `await get_tree().process_frame` then set its
`scale<class_Control_property_scale>`{.interpreted-text role="ref"}
property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_shortcut_context}
::: rst-class
classref-property
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **shortcut_context**
`🔗<class_Control_property_shortcut_context>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shortcut_context**(value: `Node<class_Node>`{.interpreted-text
  role="ref"})
- `Node<class_Node>`{.interpreted-text role="ref"}
  **get_shortcut_context**()

The `Node<class_Node>`{.interpreted-text role="ref"} which must be a
parent of the focused **Control** for the shortcut to be activated. If
`null`, the shortcut can be activated when any control is focused (a
global shortcut). This allows shortcuts to be accepted only when the
user has a certain area of the GUI focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **size** =
`Vector2(0, 0)` `🔗<class_Control_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_size**()

The size of the node\'s bounding rectangle, in the node\'s coordinate
system. `Container<class_Container>`{.interpreted-text role="ref"} nodes
update this property automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_size_flags_horizontal}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text
role="ref"}\] **size_flags_horizontal** = `1`
`🔗<class_Control_property_size_flags_horizontal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_h_size_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text
  role="ref"}\] **get_h_size_flags**()

Tells the parent `Container<class_Container>`{.interpreted-text
role="ref"} nodes how they should resize and place the node on the X
axis. Use a combination of the
`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"}
constants to change the flags. See the constants to learn what each
does.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_size_flags_stretch_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**size_flags_stretch_ratio** = `1.0`
`🔗<class_Control_property_size_flags_stretch_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_stretch_ratio**()

If the node and at least one of its neighbors uses the
`SIZE_EXPAND<class_Control_constant_SIZE_EXPAND>`{.interpreted-text
role="ref"} size flag, the parent
`Container<class_Container>`{.interpreted-text role="ref"} will let it
take more or less space depending on this property. If this node has a
stretch ratio of 2 and its neighbor a ratio of 1, this node will take
two thirds of the available space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_size_flags_vertical}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text
role="ref"}\] **size_flags_vertical** = `1`
`🔗<class_Control_property_size_flags_vertical>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_size_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text
  role="ref"}\] **get_v_size_flags**()

Tells the parent `Container<class_Container>`{.interpreted-text
role="ref"} nodes how they should resize and place the node on the Y
axis. Use a combination of the
`SizeFlags<enum_Control_SizeFlags>`{.interpreted-text role="ref"}
constants to change the flags. See the constants to learn what each
does.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_theme}
::: rst-class
classref-property
:::
::::

`Theme<class_Theme>`{.interpreted-text role="ref"} **theme**
`🔗<class_Control_property_theme>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_theme**(value: `Theme<class_Theme>`{.interpreted-text
  role="ref"})
- `Theme<class_Theme>`{.interpreted-text role="ref"} **get_theme**()

The `Theme<class_Theme>`{.interpreted-text role="ref"} resource this
node and all its **Control** and
`Window<class_Window>`{.interpreted-text role="ref"} children use. If a
child node has its own `Theme<class_Theme>`{.interpreted-text
role="ref"} resource set, theme items are merged with child\'s
definitions having higher priority.

\*\*Note:\*\* `Window<class_Window>`{.interpreted-text role="ref"}
styles will have no effect unless the window is embedded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_theme_type_variation}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**theme_type_variation** = `&""`
`🔗<class_Control_property_theme_type_variation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_theme_type_variation**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_theme_type_variation**()

The name of a theme type variation used by this **Control** to look up
its own theme items. When empty, the class name of the node is used
(e.g. `Button` for the `Button<class_Button>`{.interpreted-text
role="ref"} control), as well as the class names of all parent classes
(in order of inheritance).

When set, this property gives the highest priority to the type of the
specified name. This type can in turn extend another type, forming a
dependency chain. See
`Theme.set_type_variation()<class_Theme_method_set_type_variation>`{.interpreted-text
role="ref"}. If the theme item cannot be found using this type or its
base types, lookup falls back on the class names.

\*\*Note:\*\* To look up **Control**\'s own items use various
`get_theme_*` methods without specifying `theme_type`.

\*\*Note:\*\* Theme items are looked for in the tree order, from branch
to root, where each **Control** node is checked for its
`theme<class_Control_property_theme>`{.interpreted-text role="ref"}
property. The earliest match against any type/class name is returned.
The project-level Theme and the default Theme are checked last.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_tooltip_auto_translate_mode}
::: rst-class
classref-property
:::
::::

`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"} **tooltip_auto_translate_mode** = `0`
`🔗<class_Control_property_tooltip_auto_translate_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tooltip_auto_translate_mode**(value:
  `AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
  role="ref"})
- `AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
  role="ref"} **get_tooltip_auto_translate_mode**()

Defines if tooltip text should automatically change to its translated
version depending on the current locale. Uses the same auto translate
mode as this control when set to
`Node.AUTO_TRANSLATE_MODE_INHERIT<class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Tooltips customized using
`_make_custom_tooltip()<class_Control_private_method__make_custom_tooltip>`{.interpreted-text
role="ref"} do not use this auto translate mode automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_property_tooltip_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **tooltip_text** =
`""` `🔗<class_Control_property_tooltip_text>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tooltip_text**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_tooltip_text**()

The default tooltip text. The tooltip appears when the user\'s mouse
cursor stays idle over this control for a few moments, provided that the
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"} property is not
`MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>`{.interpreted-text
role="ref"}. The time required for the tooltip to appear can be changed
with the
`ProjectSettings.gui/timers/tooltip_delay_sec<class_ProjectSettings_property_gui/timers/tooltip_delay_sec>`{.interpreted-text
role="ref"} setting.

This string is the default return value of
`get_tooltip()<class_Control_method_get_tooltip>`{.interpreted-text
role="ref"}. Override
`_get_tooltip()<class_Control_private_method__get_tooltip>`{.interpreted-text
role="ref"} to generate tooltip text dynamically. Override
`_make_custom_tooltip()<class_Control_private_method__make_custom_tooltip>`{.interpreted-text
role="ref"} to customize the tooltip interface and behavior.

The tooltip popup will use either a default implementation, or a custom
one that you can provide by overriding
`_make_custom_tooltip()<class_Control_private_method__make_custom_tooltip>`{.interpreted-text
role="ref"}. The default tooltip includes a
`PopupPanel<class_PopupPanel>`{.interpreted-text role="ref"} and
`Label<class_Label>`{.interpreted-text role="ref"} whose theme
properties can be customized using
`Theme<class_Theme>`{.interpreted-text role="ref"} methods with the
`"TooltipPanel"` and `"TooltipLabel"` respectively. For example:

::::: tabs
::: code-tab
gdscript

var style_box = StyleBoxFlat.new() style_box.set_bg_color(Color(1, 1,
0)) style_box.set_border_width_all(2) \# We assume here that the
[theme]{.title-ref} property has been assigned a custom Theme
beforehand. theme.set_stylebox(\"panel\", \"TooltipPanel\", style_box)
theme.set_color(\"font_color\", \"TooltipLabel\", Color(0, 1, 1))
:::

::: code-tab
csharp

var styleBox = new StyleBoxFlat(); styleBox.SetBgColor(new Color(1, 1,
0)); styleBox.SetBorderWidthAll(2); // We assume here that the
[Theme]{.title-ref} property has been assigned a custom Theme
beforehand. Theme.SetStyleBox(\"panel\", \"TooltipPanel\", styleBox);
Theme.SetColor(\"font_color\", \"TooltipLabel\", new Color(0, 1, 1));
:::
:::::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Control_private_method__accessibility_get_contextual_info}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_accessibility_get_contextual_info**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__accessibility_get_contextual_info>`{.interpreted-text
role="ref"}

Return the description of the keyboard shortcuts and other contextual
help for this control.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__can_drop_data}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_can_drop_data**(at_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, data:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__can_drop_data>`{.interpreted-text
role="ref"}

Godot calls this method to test if `data` from a control\'s
`_get_drag_data()<class_Control_private_method__get_drag_data>`{.interpreted-text
role="ref"} can be dropped at `at_position`. `at_position` is local to
this control.

This method should only be used to test the data. Process the data in
`_drop_data()<class_Control_private_method__drop_data>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If the drag was initiated by a keyboard shortcut or
`accessibility_drag()<class_Control_method_accessibility_drag>`{.interpreted-text
role="ref"}, `at_position` is set to
`Vector2.INF<class_Vector2_constant_INF>`{.interpreted-text role="ref"},
and the currently selected item/text position should be used as the drop
position.

::::: tabs
::: code-tab
gdscript

func [can_drop_data]{#can_drop_data}(position, data):

:   \# Check position if it is relevant to you \# Otherwise, just check
    data return typeof(data) == TYPE_DICTIONARY and
    data.has(\"expected\")
:::

::: code-tab
csharp

public override bool [CanDropData]{#candropdata}(Vector2 atPosition,
Variant data) { // Check position if it is relevant to you // Otherwise,
just check data return data.VariantType == Variant.Type.Dictionary &&
data.AsGodotDictionary().ContainsKey(\"expected\"); }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__drop_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_drop_data**(at_position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, data: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__drop_data>`{.interpreted-text
role="ref"}

Godot calls this method to pass you the `data` from a control\'s
`_get_drag_data()<class_Control_private_method__get_drag_data>`{.interpreted-text
role="ref"} result. Godot first calls
`_can_drop_data()<class_Control_private_method__can_drop_data>`{.interpreted-text
role="ref"} to test if `data` is allowed to drop at `at_position` where
`at_position` is local to this control.

\*\*Note:\*\* If the drag was initiated by a keyboard shortcut or
`accessibility_drag()<class_Control_method_accessibility_drag>`{.interpreted-text
role="ref"}, `at_position` is set to
`Vector2.INF<class_Vector2_constant_INF>`{.interpreted-text role="ref"},
and the currently selected item/text position should be used as the drop
position.

::::: tabs
::: code-tab
gdscript

func [can_drop_data]{#can_drop_data}(position, data):

:   return typeof(data) == TYPE_DICTIONARY and data.has(\"color\")

func [drop_data]{#drop_data}(position, data):

:   var color = data\[\"color\"\]
:::

::: code-tab
csharp

public override bool [CanDropData]{#candropdata}(Vector2 atPosition,
Variant data) { return data.VariantType == Variant.Type.Dictionary &&
data.AsGodotDictionary().ContainsKey(\"color\"); }

public override void [DropData]{#dropdata}(Vector2 atPosition, Variant
data) { Color color = data.AsGodotDictionary()\[\"color\"\].AsColor(); }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__get_accessibility_container_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_accessibility_container_name**(node:
`Node<class_Node>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__get_accessibility_container_name>`{.interpreted-text
role="ref"}

Override this method to return a human-readable description of the
position of the child `node` in the custom container, added to the
`accessibility_name<class_Control_property_accessibility_name>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__get_drag_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_get_drag_data**(at_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__get_drag_data>`{.interpreted-text
role="ref"}

Godot calls this method to get data that can be dragged and dropped onto
controls that expect drop data. Returns `null` if there is no data to
drag. Controls that want to receive drop data should implement
`_can_drop_data()<class_Control_private_method__can_drop_data>`{.interpreted-text
role="ref"} and
`_drop_data()<class_Control_private_method__drop_data>`{.interpreted-text
role="ref"}. `at_position` is local to this control. Drag may be forced
with `force_drag()<class_Control_method_force_drag>`{.interpreted-text
role="ref"}.

A preview that will follow the mouse that should represent the data can
be set with
`set_drag_preview()<class_Control_method_set_drag_preview>`{.interpreted-text
role="ref"}. A good time to set the preview is in this method.

\*\*Note:\*\* If the drag was initiated by a keyboard shortcut or
`accessibility_drag()<class_Control_method_accessibility_drag>`{.interpreted-text
role="ref"}, `at_position` is set to
`Vector2.INF<class_Vector2_constant_INF>`{.interpreted-text role="ref"},
and the currently selected item/text position should be used as the drag
position.

::::: tabs
::: code-tab
gdscript

func [get_drag_data]{#get_drag_data}(position):

:   var mydata = make_data() \# This is your custom method generating
    the drag data. set_drag_preview(make_preview(mydata)) \# This is
    your custom method generating the preview of the drag data. return
    mydata
:::

::: code-tab
csharp

public override Variant [GetDragData]{#getdragdata}(Vector2 atPosition)
{ var myData = MakeData(); // This is your custom method generating the
drag data. SetDragPreview(MakePreview(myData)); // This is your custom
method generating the preview of the drag data. return myData; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__get_minimum_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_minimum_size**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__get_minimum_size>`{.interpreted-text
role="ref"}

Virtual method to be implemented by the user. Returns the minimum size
for this control. Alternative to
`custom_minimum_size<class_Control_property_custom_minimum_size>`{.interpreted-text
role="ref"} for controlling minimum size via code. The actual minimum
size will be the max value of these two (in each axis separately).

If not overridden, defaults to
`Vector2.ZERO<class_Vector2_constant_ZERO>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method will not be called when the script is attached
to a **Control** node that already overrides its minimum size (e.g.
`Label<class_Label>`{.interpreted-text role="ref"},
`Button<class_Button>`{.interpreted-text role="ref"},
`PanelContainer<class_PanelContainer>`{.interpreted-text role="ref"}
etc.). It can only be used with most basic GUI nodes, like **Control**,
`Container<class_Container>`{.interpreted-text role="ref"},
`Panel<class_Panel>`{.interpreted-text role="ref"} etc.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__get_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_tooltip**(at_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__get_tooltip>`{.interpreted-text
role="ref"}

Virtual method to be implemented by the user. Returns the tooltip text
for the position `at_position` in control\'s local coordinates, which
will typically appear when the cursor is resting over this control. See
`get_tooltip()<class_Control_method_get_tooltip>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If this method returns an empty
`String<class_String>`{.interpreted-text role="ref"} and
`_make_custom_tooltip()<class_Control_private_method__make_custom_tooltip>`{.interpreted-text
role="ref"} is not overridden, no tooltip is displayed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__gui_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_gui_input**(event: `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"}

Virtual method to be implemented by the user. Override this method to
handle and accept inputs on UI elements. See also
`accept_event()<class_Control_method_accept_event>`{.interpreted-text
role="ref"}.

\*\*Example:\*\* Click on the control to print a message:

::::: tabs
::: code-tab
gdscript

func [gui_input]{#gui_input}(event):

:   

    if event is InputEventMouseButton:

    :   

        if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:

        :   print(\"I\'ve been clicked D:\")
:::

::: code-tab
csharp

public override void [GuiInput]{#guiinput}(InputEvent \@event) { if
(@event is InputEventMouseButton mb) { if (mb.ButtonIndex ==
MouseButton.Left && mb.Pressed) { GD.Print(\"I\'ve been clicked D:\"); }
} }
:::
:::::

If the `event` inherits
`InputEventMouse<class_InputEventMouse>`{.interpreted-text role="ref"},
this method will **not** be called when:

- the control\'s
  `mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
  role="ref"} is set to
  `MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>`{.interpreted-text
  role="ref"};
- the control is obstructed by another control on top, that doesn\'t
  have
  `mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
  role="ref"} set to
  `MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>`{.interpreted-text
  role="ref"};
- the control\'s parent has
  `mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
  role="ref"} set to
  `MOUSE_FILTER_STOP<class_Control_constant_MOUSE_FILTER_STOP>`{.interpreted-text
  role="ref"} or has accepted the event;
- the control\'s parent has
  `clip_contents<class_Control_property_clip_contents>`{.interpreted-text
  role="ref"} enabled and the `event`\'s position is outside the
  parent\'s rectangle;
- the `event`\'s position is outside the control (see
  `_has_point()<class_Control_private_method__has_point>`{.interpreted-text
  role="ref"}).

\*\*Note:\*\* The `event`\'s position is relative to this control\'s
origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__has_point}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_has_point**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__has_point>`{.interpreted-text
role="ref"}

Virtual method to be implemented by the user. Returns whether the given
`point` is inside this control.

If not overridden, default behavior is checking if the point is within
control\'s Rect.

\*\*Note:\*\* If you want to check if a point is inside the control, you
can use `Rect2(Vector2.ZERO, size).has_point(point)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__make_custom_tooltip}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**\_make_custom_tooltip**(for_text:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__make_custom_tooltip>`{.interpreted-text
role="ref"}

Virtual method to be implemented by the user. Returns a **Control** node
that should be used as a tooltip instead of the default one. `for_text`
is the return value of
`get_tooltip()<class_Control_method_get_tooltip>`{.interpreted-text
role="ref"}.

The returned node must be of type **Control** or Control-derived. It can
have child nodes of any type. It is freed when the tooltip disappears,
so make sure you always provide a new instance (if you want to use a
pre-existing node from your scene tree, you can duplicate it and pass
the duplicated instance). When `null` or a non-Control node is returned,
the default tooltip will be used instead.

The returned node will be added as child to a
`PopupPanel<class_PopupPanel>`{.interpreted-text role="ref"}, so you
should only provide the contents of that panel. That
`PopupPanel<class_PopupPanel>`{.interpreted-text role="ref"} can be
themed using
`Theme.set_stylebox()<class_Theme_method_set_stylebox>`{.interpreted-text
role="ref"} for the type `"TooltipPanel"` (see
`tooltip_text<class_Control_property_tooltip_text>`{.interpreted-text
role="ref"} for an example).

\*\*Note:\*\* The tooltip is shrunk to minimal size. If you want to
ensure it\'s fully visible, you might want to set its
`custom_minimum_size<class_Control_property_custom_minimum_size>`{.interpreted-text
role="ref"} to some non-zero value.

\*\*Note:\*\* The node (and any relevant children) should have their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} set to `true` when returned, otherwise, the viewport that
instantiates it will not be able to calculate its minimum size reliably.

\*\*Note:\*\* If overridden, this method is called even if
`get_tooltip()<class_Control_method_get_tooltip>`{.interpreted-text
role="ref"} returns an empty string. When this happens with the default
tooltip, it is not displayed. To copy this behavior, return `null` in
this method when `for_text` is empty.

\*\*Example:\*\* Use a constructed node as a tooltip:

::::: tabs
::: code-tab
gdscript

func [make_custom_tooltip]{#make_custom_tooltip}(for_text):

:   var label = Label.new() label.text = for_text return label
:::

::: code-tab
csharp

public override Control [MakeCustomTooltip]{#makecustomtooltip}(string
forText) { var label = new Label(); label.Text = forText; return label;
}
:::
:::::

\*\*Example:\*\* Usa a scene instance as a tooltip:

::::: tabs
::: code-tab
gdscript

func [make_custom_tooltip]{#make_custom_tooltip}(for_text):

:   var tooltip =
    preload(\"res://some_tooltip_scene.tscn\").instantiate()
    tooltip.get_node(\"Label\").text = for_text return tooltip
:::

::: code-tab
csharp

public override Control [MakeCustomTooltip]{#makecustomtooltip}(string
forText) { Node tooltip =
ResourceLoader.Load\<PackedScene\>(\"res://some_tooltip_scene.tscn\").Instantiate();
tooltip.GetNode\<Label\>(\"Label\").Text = forText; return tooltip; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_private_method__structured_text_parser}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}\]
**\_structured_text_parser**(args:
`Array<class_Array>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_private_method__structured_text_parser>`{.interpreted-text
role="ref"}

User defined BiDi algorithm override function.

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"} text ranges and
text base directions, in the left-to-right order. Ranges should cover
full source `text` without overlaps. BiDi algorithm will be used on each
range separately.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_accept_event}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**accept_event**()
`🔗<class_Control_method_accept_event>`{.interpreted-text role="ref"}

Marks an input event as handled. Once you accept an input event, it
stops propagating, even to nodes listening to
`Node._unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"} or
`Node._unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This does not affect the methods in
`Input<class_Input>`{.interpreted-text role="ref"}, only the way events
are propagated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_accessibility_drag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**accessibility_drag**()
`🔗<class_Control_method_accessibility_drag>`{.interpreted-text
role="ref"}

Starts drag-and-drop operation without using a mouse.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_accessibility_drop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**accessibility_drop**()
`🔗<class_Control_method_accessibility_drop>`{.interpreted-text
role="ref"}

Ends drag-and-drop operation without using a mouse.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_add_theme_color_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_color_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Control_method_add_theme_color_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme
`Color<class_Color>`{.interpreted-text role="ref"} with the specified
`name`. Local overrides always take precedence when fetching theme items
for the control. An override can be removed with
`remove_theme_color_override()<class_Control_method_remove_theme_color_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"}.

\*\*Example:\*\* Override a `Label<class_Label>`{.interpreted-text
role="ref"}\'s color and reset it later:

::::: tabs
::: code-tab
gdscript

\# Given the child Label node \"MyLabel\", override its font color with
a custom value. \$MyLabel.add_theme_color_override(\"font_color\",
Color(1, 0.5, 0)) \# Reset the font color of the child label.
\$MyLabel.remove_theme_color_override(\"font_color\") \# Alternatively
it can be overridden with the default value from the Label type.
\$MyLabel.add_theme_color_override(\"font_color\",
get_theme_color(\"font_color\", \"Label\"))
:::

::: code-tab
csharp

// Given the child Label node \"MyLabel\", override its font color with
a custom value.
GetNode\<Label\>(\"MyLabel\").AddThemeColorOverride(\"font_color\", new
Color(1, 0.5f, 0)); // Reset the font color of the child label.
GetNode\<Label\>(\"MyLabel\").RemoveThemeColorOverride(\"font_color\");
// Alternatively it can be overridden with the default value from the
Label type.
GetNode\<Label\>(\"MyLabel\").AddThemeColorOverride(\"font_color\",
GetThemeColor(\"font_color\", \"Label\"));
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_add_theme_constant_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_constant_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, constant:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Control_method_add_theme_constant_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme constant with the specified `name`.
Local overrides always take precedence when fetching theme items for the
control. An override can be removed with
`remove_theme_constant_override()<class_Control_method_remove_theme_constant_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_constant()<class_Control_method_get_theme_constant>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_add_theme_font_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_font_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, font:
`Font<class_Font>`{.interpreted-text role="ref"})
`🔗<class_Control_method_add_theme_font_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme
`Font<class_Font>`{.interpreted-text role="ref"} with the specified
`name`. Local overrides always take precedence when fetching theme items
for the control. An override can be removed with
`remove_theme_font_override()<class_Control_method_remove_theme_font_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_font()<class_Control_method_get_theme_font>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_add_theme_font_size_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_font_size_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, font_size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Control_method_add_theme_font_size_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme font size with the specified
`name`. Local overrides always take precedence when fetching theme items
for the control. An override can be removed with
`remove_theme_font_size_override()<class_Control_method_remove_theme_font_size_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_font_size()<class_Control_method_get_theme_font_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_add_theme_icon_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_icon_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_Control_method_add_theme_icon_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme icon with the specified `name`.
Local overrides always take precedence when fetching theme items for the
control. An override can be removed with
`remove_theme_icon_override()<class_Control_method_remove_theme_icon_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_icon()<class_Control_method_get_theme_icon>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_add_theme_stylebox_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_theme_stylebox_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, stylebox:
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"})
`🔗<class_Control_method_add_theme_stylebox_override>`{.interpreted-text
role="ref"}

Creates a local override for a theme
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} with the
specified `name`. Local overrides always take precedence when fetching
theme items for the control. An override can be removed with
`remove_theme_stylebox_override()<class_Control_method_remove_theme_stylebox_override>`{.interpreted-text
role="ref"}.

See also
`get_theme_stylebox()<class_Control_method_get_theme_stylebox>`{.interpreted-text
role="ref"}.

\*\*Example:\*\* Modify a property in a
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} by duplicating
it:

::::: tabs
::: code-tab
gdscript

\# The snippet below assumes the child node \"MyButton\" has a
StyleBoxFlat assigned. \# Resources are shared across instances, so we
need to duplicate it \# to avoid modifying the appearance of all other
buttons. var new_stylebox_normal =
\$MyButton.get_theme_stylebox(\"normal\").duplicate()
new_stylebox_normal.border_width_top = 3
new_stylebox_normal.border_color = Color(0, 1, 0.5)
\$MyButton.add_theme_stylebox_override(\"normal\", new_stylebox_normal)
\# Remove the stylebox override.
\$MyButton.remove_theme_stylebox_override(\"normal\")
:::

::: code-tab
csharp

// The snippet below assumes the child node \"MyButton\" has a
StyleBoxFlat assigned. // Resources are shared across instances, so we
need to duplicate it // to avoid modifying the appearance of all other
buttons. StyleBoxFlat newStyleboxNormal =
GetNode\<Button\>(\"MyButton\").GetThemeStylebox(\"normal\").Duplicate()
as StyleBoxFlat; newStyleboxNormal.BorderWidthTop = 3;
newStyleboxNormal.BorderColor = new Color(0, 1, 0.5f);
GetNode\<Button\>(\"MyButton\").AddThemeStyleboxOverride(\"normal\",
newStyleboxNormal); // Remove the stylebox override.
GetNode\<Button\>(\"MyButton\").RemoveThemeStyleboxOverride(\"normal\");
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_begin_bulk_theme_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**begin_bulk_theme_override**()
`🔗<class_Control_method_begin_bulk_theme_override>`{.interpreted-text
role="ref"}

Prevents `*_theme_*_override` methods from emitting
`NOTIFICATION_THEME_CHANGED<class_Control_constant_NOTIFICATION_THEME_CHANGED>`{.interpreted-text
role="ref"} until
`end_bulk_theme_override()<class_Control_method_end_bulk_theme_override>`{.interpreted-text
role="ref"} is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_end_bulk_theme_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**end_bulk_theme_override**()
`🔗<class_Control_method_end_bulk_theme_override>`{.interpreted-text
role="ref"}

Ends a bulk theme override update. See
`begin_bulk_theme_override()<class_Control_method_begin_bulk_theme_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_find_next_valid_focus}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**find_next_valid_focus**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_find_next_valid_focus>`{.interpreted-text
role="ref"}

Finds the next (below in the tree) **Control** that can receive the
focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_find_prev_valid_focus}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**find_prev_valid_focus**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_find_prev_valid_focus>`{.interpreted-text
role="ref"}

Finds the previous (above in the tree) **Control** that can receive the
focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_find_valid_focus_neighbor}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**find_valid_focus_neighbor**(side:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_find_valid_focus_neighbor>`{.interpreted-text
role="ref"}

Finds the next **Control** that can receive the focus on the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This is different from
`get_focus_neighbor()<class_Control_method_get_focus_neighbor>`{.interpreted-text
role="ref"}, which returns the path of a specified focus neighbor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_force_drag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_drag**(data: `Variant<class_Variant>`{.interpreted-text
role="ref"}, preview: `Control<class_Control>`{.interpreted-text
role="ref"}) `🔗<class_Control_method_force_drag>`{.interpreted-text
role="ref"}

Forces drag and bypasses
`_get_drag_data()<class_Control_private_method__get_drag_data>`{.interpreted-text
role="ref"} and
`set_drag_preview()<class_Control_method_set_drag_preview>`{.interpreted-text
role="ref"} by passing `data` and `preview`. Drag will start even if the
mouse is neither over nor pressed on this control.

The methods
`_can_drop_data()<class_Control_private_method__can_drop_data>`{.interpreted-text
role="ref"} and
`_drop_data()<class_Control_private_method__drop_data>`{.interpreted-text
role="ref"} must be implemented on controls that want to receive drop
data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_anchor}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_anchor**(side:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_get_anchor>`{.interpreted-text
role="ref"}

Returns the anchor for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}. A getter
method for
`anchor_bottom<class_Control_property_anchor_bottom>`{.interpreted-text
role="ref"},
`anchor_left<class_Control_property_anchor_left>`{.interpreted-text
role="ref"},
`anchor_right<class_Control_property_anchor_right>`{.interpreted-text
role="ref"} and
`anchor_top<class_Control_property_anchor_top>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_begin}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_begin**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_get_begin>`{.interpreted-text
role="ref"}

Returns
`offset_left<class_Control_property_offset_left>`{.interpreted-text
role="ref"} and
`offset_top<class_Control_property_offset_top>`{.interpreted-text
role="ref"}. See also
`position<class_Control_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_combined_minimum_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_combined_minimum_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_combined_minimum_size>`{.interpreted-text
role="ref"}

Returns combined minimum size from
`custom_minimum_size<class_Control_property_custom_minimum_size>`{.interpreted-text
role="ref"} and
`get_minimum_size()<class_Control_method_get_minimum_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_cursor_shape}
::: rst-class
classref-method
:::
::::

`CursorShape<enum_Control_CursorShape>`{.interpreted-text role="ref"}
**get_cursor_shape**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"} = Vector2(0, 0))
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_cursor_shape>`{.interpreted-text
role="ref"}

Returns the mouse cursor shape for this control when hovered over
`position` in local coordinates. For most controls, this is the same as
`mouse_default_cursor_shape<class_Control_property_mouse_default_cursor_shape>`{.interpreted-text
role="ref"}, but some built-in controls implement more complex logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_end}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_end**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_get_end>`{.interpreted-text
role="ref"}

Returns
`offset_right<class_Control_property_offset_right>`{.interpreted-text
role="ref"} and
`offset_bottom<class_Control_property_offset_bottom>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_focus_mode_with_override}
::: rst-class
classref-method
:::
::::

`FocusMode<enum_Control_FocusMode>`{.interpreted-text role="ref"}
**get_focus_mode_with_override**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_focus_mode_with_override>`{.interpreted-text
role="ref"}

Returns the
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}, but takes the
`focus_behavior_recursive<class_Control_property_focus_behavior_recursive>`{.interpreted-text
role="ref"} into account. If
`focus_behavior_recursive<class_Control_property_focus_behavior_recursive>`{.interpreted-text
role="ref"} is set to
`FOCUS_BEHAVIOR_DISABLED<class_Control_constant_FOCUS_BEHAVIOR_DISABLED>`{.interpreted-text
role="ref"}, or it is set to
`FOCUS_BEHAVIOR_INHERITED<class_Control_constant_FOCUS_BEHAVIOR_INHERITED>`{.interpreted-text
role="ref"} and its ancestor is set to
`FOCUS_BEHAVIOR_DISABLED<class_Control_constant_FOCUS_BEHAVIOR_DISABLED>`{.interpreted-text
role="ref"}, then this returns
`FOCUS_NONE<class_Control_constant_FOCUS_NONE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_focus_neighbor}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_focus_neighbor**(side:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_focus_neighbor>`{.interpreted-text
role="ref"}

Returns the focus neighbor for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}. A getter
method for
`focus_neighbor_bottom<class_Control_property_focus_neighbor_bottom>`{.interpreted-text
role="ref"},
`focus_neighbor_left<class_Control_property_focus_neighbor_left>`{.interpreted-text
role="ref"},
`focus_neighbor_right<class_Control_property_focus_neighbor_right>`{.interpreted-text
role="ref"} and
`focus_neighbor_top<class_Control_property_focus_neighbor_top>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* To find the next **Control** on the specific
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, even if a
neighbor is not assigned, use
`find_valid_focus_neighbor()<class_Control_method_find_valid_focus_neighbor>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_global_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_global_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_global_rect>`{.interpreted-text role="ref"}

Returns the position and size of the control relative to the containing
canvas. See
`global_position<class_Control_property_global_position>`{.interpreted-text
role="ref"} and `size<class_Control_property_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If the node itself or any parent
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} between the
node and the canvas have a non default rotation or skew, the resulting
size is likely not meaningful.

\*\*Note:\*\* Setting
`Viewport.gui_snap_controls_to_pixels<class_Viewport_property_gui_snap_controls_to_pixels>`{.interpreted-text
role="ref"} to `true` can lead to rounding inaccuracies between the
displayed control and the returned
`Rect2<class_Rect2>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_minimum_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_minimum_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_minimum_size>`{.interpreted-text
role="ref"}

Returns the minimum size for this control. See
`custom_minimum_size<class_Control_property_custom_minimum_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_mouse_filter_with_override}
::: rst-class
classref-method
:::
::::

`MouseFilter<enum_Control_MouseFilter>`{.interpreted-text role="ref"}
**get_mouse_filter_with_override**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_mouse_filter_with_override>`{.interpreted-text
role="ref"}

Returns the
`mouse_filter<class_Control_property_mouse_filter>`{.interpreted-text
role="ref"}, but takes the
`mouse_behavior_recursive<class_Control_property_mouse_behavior_recursive>`{.interpreted-text
role="ref"} into account. If
`mouse_behavior_recursive<class_Control_property_mouse_behavior_recursive>`{.interpreted-text
role="ref"} is set to
`MOUSE_BEHAVIOR_DISABLED<class_Control_constant_MOUSE_BEHAVIOR_DISABLED>`{.interpreted-text
role="ref"}, or it is set to
`MOUSE_BEHAVIOR_INHERITED<class_Control_constant_MOUSE_BEHAVIOR_INHERITED>`{.interpreted-text
role="ref"} and its ancestor is set to
`MOUSE_BEHAVIOR_DISABLED<class_Control_constant_MOUSE_BEHAVIOR_DISABLED>`{.interpreted-text
role="ref"}, then this returns
`MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_offset**(offset: `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_get_offset>`{.interpreted-text
role="ref"}

Returns the offset for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}. A getter
method for
`offset_bottom<class_Control_property_offset_bottom>`{.interpreted-text
role="ref"},
`offset_left<class_Control_property_offset_left>`{.interpreted-text
role="ref"},
`offset_right<class_Control_property_offset_right>`{.interpreted-text
role="ref"} and
`offset_top<class_Control_property_offset_top>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_parent_area_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_parent_area_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_parent_area_size>`{.interpreted-text
role="ref"}

Returns the width/height occupied in the parent control.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_parent_control}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**get_parent_control**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_parent_control>`{.interpreted-text
role="ref"}

Returns the parent control node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **get_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_get_rect>`{.interpreted-text
role="ref"}

Returns the position and size of the control in the coordinate system of
the containing node. See
`position<class_Control_property_position>`{.interpreted-text
role="ref"}, `scale<class_Control_property_scale>`{.interpreted-text
role="ref"} and `size<class_Control_property_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If
`rotation<class_Control_property_rotation>`{.interpreted-text
role="ref"} is not the default rotation, the resulting size is not
meaningful.

\*\*Note:\*\* Setting
`Viewport.gui_snap_controls_to_pixels<class_Viewport_property_gui_snap_controls_to_pixels>`{.interpreted-text
role="ref"} to `true` can lead to rounding inaccuracies between the
displayed control and the returned
`Rect2<class_Rect2>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_screen_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_screen_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_screen_position>`{.interpreted-text
role="ref"}

Returns the position of this **Control** in global screen coordinates
(i.e. taking window position into account). Mostly useful for editor
plugins.

Equals to
`global_position<class_Control_property_global_position>`{.interpreted-text
role="ref"} if the window is embedded (see
`Viewport.gui_embed_subwindows<class_Viewport_property_gui_embed_subwindows>`{.interpreted-text
role="ref"}).

\*\*Example:\*\* Show a popup at the mouse position:

    popup_menu.position = get_screen_position() + get_local_mouse_position()
    popup_menu.reset_size()
    popup_menu.popup()

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_theme_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_theme_color**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_theme_color>`{.interpreted-text role="ref"}

Returns a `Color<class_Color>`{.interpreted-text role="ref"} from the
first matching `Theme<class_Theme>`{.interpreted-text role="ref"} in the
tree if that `Theme<class_Theme>`{.interpreted-text role="ref"} has a
color item with the specified `name` and `theme_type`. If `theme_type`
is omitted the class name of the current control is used as the type, or
`theme_type_variation<class_Control_property_theme_type_variation>`{.interpreted-text
role="ref"} if it is defined. If the type is a class name its parent
classes are also checked, in order of inheritance. If the type is a
variation its base types are checked, in order of dependency, then the
control\'s class name and its parent classes are checked.

For the current control its local overrides are considered first (see
`add_theme_color_override()<class_Control_method_add_theme_color_override>`{.interpreted-text
role="ref"}), then its assigned
`theme<class_Control_property_theme>`{.interpreted-text role="ref"}.
After the current control, each parent control and its assigned
`theme<class_Control_property_theme>`{.interpreted-text role="ref"} are
considered; controls without a
`theme<class_Control_property_theme>`{.interpreted-text role="ref"}
assigned are skipped. If no matching
`Theme<class_Theme>`{.interpreted-text role="ref"} is found in the tree,
the custom project `Theme<class_Theme>`{.interpreted-text role="ref"}
(see
`ProjectSettings.gui/theme/custom<class_ProjectSettings_property_gui/theme/custom>`{.interpreted-text
role="ref"}) and the default `Theme<class_Theme>`{.interpreted-text
role="ref"} are used (see `ThemeDB<class_ThemeDB>`{.interpreted-text
role="ref"}).

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   \# Get the font color defined for the current Control\'s class, if
    it exists. modulate = get_theme_color(\"font_color\") \# Get the
    font color defined for the Button class. modulate =
    get_theme_color(\"font_color\", \"Button\")
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { // Get the font color defined
for the current Control\'s class, if it exists. Modulate =
GetThemeColor(\"font_color\"); // Get the font color defined for the
Button class. Modulate = GetThemeColor(\"font_color\", \"Button\"); }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_theme_constant}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_theme_constant**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_theme_constant>`{.interpreted-text
role="ref"}

Returns a constant from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a constant item
with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_theme_default_base_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_theme_default_base_scale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_theme_default_base_scale>`{.interpreted-text
role="ref"}

Returns the default base scale value from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a valid
`Theme.default_base_scale<class_Theme_property_default_base_scale>`{.interpreted-text
role="ref"} value.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_theme_default_font}
::: rst-class
classref-method
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"}
**get_theme_default_font**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_theme_default_font>`{.interpreted-text
role="ref"}

Returns the default font from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a valid
`Theme.default_font<class_Theme_property_default_font>`{.interpreted-text
role="ref"} value.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_theme_default_font_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_theme_default_font_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_theme_default_font_size>`{.interpreted-text
role="ref"}

Returns the default font size value from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a valid
`Theme.default_font_size<class_Theme_property_default_font_size>`{.interpreted-text
role="ref"} value.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_theme_font}
::: rst-class
classref-method
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"}
**get_theme_font**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_get_theme_font>`{.interpreted-text
role="ref"}

Returns a `Font<class_Font>`{.interpreted-text role="ref"} from the
first matching `Theme<class_Theme>`{.interpreted-text role="ref"} in the
tree if that `Theme<class_Theme>`{.interpreted-text role="ref"} has a
font item with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_theme_font_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_theme_font_size**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_theme_font_size>`{.interpreted-text
role="ref"}

Returns a font size from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has a font size item
with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_theme_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_theme_icon**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_get_theme_icon>`{.interpreted-text
role="ref"}

Returns an icon from the first matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree if that
`Theme<class_Theme>`{.interpreted-text role="ref"} has an icon item with
the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_theme_stylebox}
::: rst-class
classref-method
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**get_theme_stylebox**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_get_theme_stylebox>`{.interpreted-text
role="ref"}

Returns a `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} from
the first matching `Theme<class_Theme>`{.interpreted-text role="ref"} in
the tree if that `Theme<class_Theme>`{.interpreted-text role="ref"} has
a stylebox item with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_get_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tooltip**(at_position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"} = Vector2(0, 0))
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_get_tooltip>`{.interpreted-text
role="ref"}

Returns the tooltip text for the position `at_position` in control\'s
local coordinates, which will typically appear when the cursor is
resting over this control. By default, it returns
`tooltip_text<class_Control_property_tooltip_text>`{.interpreted-text
role="ref"}.

This method can be overridden to customize its behavior. See
`_get_tooltip()<class_Control_private_method__get_tooltip>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If this method returns an empty
`String<class_String>`{.interpreted-text role="ref"} and
`_make_custom_tooltip()<class_Control_private_method__make_custom_tooltip>`{.interpreted-text
role="ref"} is not overridden, no tooltip is displayed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_grab_click_focus}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**grab_click_focus**()
`🔗<class_Control_method_grab_click_focus>`{.interpreted-text
role="ref"}

Creates an
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} that attempts to click the control. If the event is
received, the control gains focus.

::::: tabs
::: code-tab
gdscript

func [process]{#process}(delta):

:   grab_click_focus() \# When clicking another Control node, this node
    will be clicked instead.
:::

::: code-tab
csharp

public override void [Process]{#process}(double delta) {
GrabClickFocus(); // When clicking another Control node, this node will
be clicked instead. }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_grab_focus}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**grab_focus**() `🔗<class_Control_method_grab_focus>`{.interpreted-text
role="ref"}

Steal the focus from another control and become the focused control (see
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* Using this method together with
`Callable.call_deferred()<class_Callable_method_call_deferred>`{.interpreted-text
role="ref"} makes it more reliable, especially when called inside
`Node._ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_focus}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_focus**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_has_focus>`{.interpreted-text
role="ref"}

Returns `true` if this is the current focused control. See
`focus_mode<class_Control_property_focus_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_color}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_color**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_color>`{.interpreted-text role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a color item with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_color_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_color_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_color_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme
`Color<class_Color>`{.interpreted-text role="ref"} with the specified
`name` in this **Control** node.

See
`add_theme_color_override()<class_Control_method_add_theme_color_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_constant}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_constant**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_constant>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a constant item with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_constant_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_constant_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_constant_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme constant with
the specified `name` in this **Control** node.

See
`add_theme_constant_override()<class_Control_method_add_theme_constant_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_font}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_font**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_has_theme_font>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a font item with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_font_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_font_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_font_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme
`Font<class_Font>`{.interpreted-text role="ref"} with the specified
`name` in this **Control** node.

See
`add_theme_font_override()<class_Control_method_add_theme_font_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_font_size}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_font_size**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_font_size>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a font size item with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_font_size_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_font_size_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_font_size_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme font size with
the specified `name` in this **Control** node.

See
`add_theme_font_size_override()<class_Control_method_add_theme_font_size_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_icon}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_icon**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_has_theme_icon>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
an icon item with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_icon_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_icon_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_icon_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme icon with the
specified `name` in this **Control** node.

See
`add_theme_icon_override()<class_Control_method_add_theme_icon_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_stylebox}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_stylebox**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text role="ref"}
= &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_stylebox>`{.interpreted-text
role="ref"}

Returns `true` if there is a matching
`Theme<class_Theme>`{.interpreted-text role="ref"} in the tree that has
a stylebox item with the specified `name` and `theme_type`.

See
`get_theme_color()<class_Control_method_get_theme_color>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_has_theme_stylebox_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_stylebox_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_has_theme_stylebox_override>`{.interpreted-text
role="ref"}

Returns `true` if there is a local override for a theme
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} with the
specified `name` in this **Control** node.

See
`add_theme_stylebox_override()<class_Control_method_add_theme_stylebox_override>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_is_drag_successful}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_drag_successful**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Control_method_is_drag_successful>`{.interpreted-text
role="ref"}

Returns `true` if a drag operation is successful. Alternative to
`Viewport.gui_is_drag_successful()<class_Viewport_method_gui_is_drag_successful>`{.interpreted-text
role="ref"}.

Best used with
`Node.NOTIFICATION_DRAG_END<class_Node_constant_NOTIFICATION_DRAG_END>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_is_layout_rtl}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_layout_rtl**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Control_method_is_layout_rtl>`{.interpreted-text
role="ref"}

Returns `true` if the layout is right-to-left. See also
`layout_direction<class_Control_property_layout_direction>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_release_focus}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**release_focus**()
`🔗<class_Control_method_release_focus>`{.interpreted-text role="ref"}

Give up the focus. No other control will be able to receive input.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_remove_theme_color_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_color_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Control_method_remove_theme_color_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme
`Color<class_Color>`{.interpreted-text role="ref"} with the specified
`name` previously added by
`add_theme_color_override()<class_Control_method_add_theme_color_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_remove_theme_constant_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_constant_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Control_method_remove_theme_constant_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme constant with the specified `name`
previously added by
`add_theme_constant_override()<class_Control_method_add_theme_constant_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_remove_theme_font_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_font_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Control_method_remove_theme_font_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme
`Font<class_Font>`{.interpreted-text role="ref"} with the specified
`name` previously added by
`add_theme_font_override()<class_Control_method_add_theme_font_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_remove_theme_font_size_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_font_size_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Control_method_remove_theme_font_size_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme font size with the specified `name`
previously added by
`add_theme_font_size_override()<class_Control_method_add_theme_font_size_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_remove_theme_icon_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_icon_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Control_method_remove_theme_icon_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme icon with the specified `name`
previously added by
`add_theme_icon_override()<class_Control_method_add_theme_icon_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_remove_theme_stylebox_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_theme_stylebox_override**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Control_method_remove_theme_stylebox_override>`{.interpreted-text
role="ref"}

Removes a local override for a theme
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} with the
specified `name` previously added by
`add_theme_stylebox_override()<class_Control_method_add_theme_stylebox_override>`{.interpreted-text
role="ref"} or via the Inspector dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_reset_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reset_size**() `🔗<class_Control_method_reset_size>`{.interpreted-text
role="ref"}

Resets the size to
`get_combined_minimum_size()<class_Control_method_get_combined_minimum_size>`{.interpreted-text
role="ref"}. This is equivalent to calling `set_size(Vector2())` (or any
size below the minimum).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_anchor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_anchor**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"}, anchor: `float<class_float>`{.interpreted-text role="ref"},
keep_offset: `bool<class_bool>`{.interpreted-text role="ref"} = false,
push_opposite_anchor: `bool<class_bool>`{.interpreted-text role="ref"} =
true) `🔗<class_Control_method_set_anchor>`{.interpreted-text
role="ref"}

Sets the anchor for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"} to
`anchor`. A setter method for
`anchor_bottom<class_Control_property_anchor_bottom>`{.interpreted-text
role="ref"},
`anchor_left<class_Control_property_anchor_left>`{.interpreted-text
role="ref"},
`anchor_right<class_Control_property_anchor_right>`{.interpreted-text
role="ref"} and
`anchor_top<class_Control_property_anchor_top>`{.interpreted-text
role="ref"}.

If `keep_offset` is `true`, offsets aren\'t updated after this
operation.

If `push_opposite_anchor` is `true` and the opposite anchor overlaps
this anchor, the opposite one will have its value overridden. For
example, when setting left anchor to 1 and the right anchor has value of
0.5, the right anchor will also get value of 1. If
`push_opposite_anchor` was `false`, the left anchor would get value 0.5.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_anchor_and_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_anchor_and_offset**(side:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, anchor:
`float<class_float>`{.interpreted-text role="ref"}, offset:
`float<class_float>`{.interpreted-text role="ref"},
push_opposite_anchor: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_Control_method_set_anchor_and_offset>`{.interpreted-text
role="ref"}

Works the same as
`set_anchor()<class_Control_method_set_anchor>`{.interpreted-text
role="ref"}, but instead of `keep_offset` argument and automatic update
of offset, it allows to set the offset yourself (see
`set_offset()<class_Control_method_set_offset>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_anchors_and_offsets_preset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_anchors_and_offsets_preset**(preset:
`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"},
resize_mode:
`LayoutPresetMode<enum_Control_LayoutPresetMode>`{.interpreted-text
role="ref"} = 0, margin: `int<class_int>`{.interpreted-text role="ref"}
= 0)
`🔗<class_Control_method_set_anchors_and_offsets_preset>`{.interpreted-text
role="ref"}

Sets both anchor preset and offset preset. See
`set_anchors_preset()<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"} and
`set_offsets_preset()<class_Control_method_set_offsets_preset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_anchors_preset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_anchors_preset**(preset:
`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"},
keep_offsets: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Control_method_set_anchors_preset>`{.interpreted-text
role="ref"}

Sets the anchors to a `preset` from
`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
enum. This is the code equivalent to using the Layout menu in the 2D
editor.

If `keep_offsets` is `true`, control\'s position will also be updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_begin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_begin**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_Control_method_set_begin>`{.interpreted-text
role="ref"}

Sets `offset_left<class_Control_property_offset_left>`{.interpreted-text
role="ref"} and
`offset_top<class_Control_property_offset_top>`{.interpreted-text
role="ref"} at the same time. Equivalent of changing
`position<class_Control_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_drag_forwarding}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_drag_forwarding**(drag_func:
`Callable<class_Callable>`{.interpreted-text role="ref"}, can_drop_func:
`Callable<class_Callable>`{.interpreted-text role="ref"}, drop_func:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_Control_method_set_drag_forwarding>`{.interpreted-text
role="ref"}

Sets the given callables to be used instead of the control\'s own
drag-and-drop virtual methods. If a callable is empty, its respective
virtual method is used as normal.

The arguments for each callable should be exactly the same as their
respective virtual methods, which would be:

- `drag_func` corresponds to
  `_get_drag_data()<class_Control_private_method__get_drag_data>`{.interpreted-text
  role="ref"} and requires a `Vector2<class_Vector2>`{.interpreted-text
  role="ref"};
- `can_drop_func` corresponds to
  `_can_drop_data()<class_Control_private_method__can_drop_data>`{.interpreted-text
  role="ref"} and requires both a
  `Vector2<class_Vector2>`{.interpreted-text role="ref"} and a
  `Variant<class_Variant>`{.interpreted-text role="ref"};
- `drop_func` corresponds to
  `_drop_data()<class_Control_private_method__drop_data>`{.interpreted-text
  role="ref"} and requires both a
  `Vector2<class_Vector2>`{.interpreted-text role="ref"} and a
  `Variant<class_Variant>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_drag_preview}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_drag_preview**(control: `Control<class_Control>`{.interpreted-text
role="ref"})
`🔗<class_Control_method_set_drag_preview>`{.interpreted-text
role="ref"}

Shows the given control at the mouse pointer. A good time to call this
method is in
`_get_drag_data()<class_Control_private_method__get_drag_data>`{.interpreted-text
role="ref"}. The control must not be in the scene tree. You should not
free the control, and you should not keep a reference to the control
beyond the duration of the drag. It will be deleted automatically after
the drag has ended.

::::: tabs
::: code-tab
gdscript

\@export var color = Color(1, 0, 0, 1)

func [get_drag_data]{#get_drag_data}(position):

:   \# Use a control that is not in the tree var cpb =
    ColorPickerButton.new() cpb.color = color cpb.size = Vector2(50, 50)
    set_drag_preview(cpb) return color
:::

::: code-tab
csharp

\[Export\] private Color [color]{#color} = new Color(1, 0, 0, 1);

public override Variant [GetDragData]{#getdragdata}(Vector2 atPosition)
{ // Use a control that is not in the tree var cpb = new
ColorPickerButton(); cpb.Color = [color]{#color}; cpb.Size = new
Vector2(50, 50); SetDragPreview(cpb); return [color]{#color}; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_end**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_Control_method_set_end>`{.interpreted-text
role="ref"}

Sets
`offset_right<class_Control_property_offset_right>`{.interpreted-text
role="ref"} and
`offset_bottom<class_Control_property_offset_bottom>`{.interpreted-text
role="ref"} at the same time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_focus_neighbor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_focus_neighbor**(side:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, neighbor:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_Control_method_set_focus_neighbor>`{.interpreted-text
role="ref"}

Sets the focus neighbor for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"} to the
**Control** at `neighbor` node path. A setter method for
`focus_neighbor_bottom<class_Control_property_focus_neighbor_bottom>`{.interpreted-text
role="ref"},
`focus_neighbor_left<class_Control_property_focus_neighbor_left>`{.interpreted-text
role="ref"},
`focus_neighbor_right<class_Control_property_focus_neighbor_right>`{.interpreted-text
role="ref"} and
`focus_neighbor_top<class_Control_property_focus_neighbor_top>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_global_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_global_position**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, keep_offsets:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Control_method_set_global_position>`{.interpreted-text
role="ref"}

Sets the
`global_position<class_Control_property_global_position>`{.interpreted-text
role="ref"} to given `position`.

If `keep_offsets` is `true`, control\'s anchors will be updated instead
of offsets.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_offset**(side: `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"}, offset: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Control_method_set_offset>`{.interpreted-text role="ref"}

Sets the offset for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"} to
`offset`. A setter method for
`offset_bottom<class_Control_property_offset_bottom>`{.interpreted-text
role="ref"},
`offset_left<class_Control_property_offset_left>`{.interpreted-text
role="ref"},
`offset_right<class_Control_property_offset_right>`{.interpreted-text
role="ref"} and
`offset_top<class_Control_property_offset_top>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_offsets_preset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_offsets_preset**(preset:
`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"},
resize_mode:
`LayoutPresetMode<enum_Control_LayoutPresetMode>`{.interpreted-text
role="ref"} = 0, margin: `int<class_int>`{.interpreted-text role="ref"}
= 0) `🔗<class_Control_method_set_offsets_preset>`{.interpreted-text
role="ref"}

Sets the offsets to a `preset` from
`LayoutPreset<enum_Control_LayoutPreset>`{.interpreted-text role="ref"}
enum. This is the code equivalent to using the Layout menu in the 2D
editor.

Use parameter `resize_mode` with constants from
`LayoutPresetMode<enum_Control_LayoutPresetMode>`{.interpreted-text
role="ref"} to better determine the resulting size of the **Control**.
Constant size will be ignored if used with presets that change size,
e.g.
`PRESET_LEFT_WIDE<class_Control_constant_PRESET_LEFT_WIDE>`{.interpreted-text
role="ref"}.

Use parameter `margin` to determine the gap between the **Control** and
the edges.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_position**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, keep_offsets: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_Control_method_set_position>`{.interpreted-text role="ref"}

Sets the `position<class_Control_property_position>`{.interpreted-text
role="ref"} to given `position`.

If `keep_offsets` is `true`, control\'s anchors will be updated instead
of offsets.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_set_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_size**(size: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, keep_offsets: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_Control_method_set_size>`{.interpreted-text role="ref"}

Sets the size (see `size<class_Control_property_size>`{.interpreted-text
role="ref"}).

If `keep_offsets` is `true`, control\'s anchors will be updated instead
of offsets.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_update_minimum_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_minimum_size**()
`🔗<class_Control_method_update_minimum_size>`{.interpreted-text
role="ref"}

Invalidates the size cache in this node and in parent nodes up to top
level. Intended to be used with
`get_minimum_size()<class_Control_method_get_minimum_size>`{.interpreted-text
role="ref"} when the return value is changed. Setting
`custom_minimum_size<class_Control_property_custom_minimum_size>`{.interpreted-text
role="ref"} directly calls this method automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Control_method_warp_mouse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**warp_mouse**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_Control_method_warp_mouse>`{.interpreted-text
role="ref"}

Moves the mouse cursor to `position`, relative to
`position<class_Control_property_position>`{.interpreted-text
role="ref"} of this **Control**.

\*\*Note:\*\*
`warp_mouse()<class_Control_method_warp_mouse>`{.interpreted-text
role="ref"} is only supported on Windows, macOS and Linux. It has no
effect on Android, iOS and Web.
