github_url
:   hide

# Object {#class_Object}

**Inherited By:** `AudioServer<class_AudioServer>`{.interpreted-text
role="ref"}, `CameraServer<class_CameraServer>`{.interpreted-text
role="ref"}, `ClassDB<class_ClassDB>`{.interpreted-text role="ref"},
`DisplayServer<class_DisplayServer>`{.interpreted-text role="ref"},
`EditorFileSystemDirectory<class_EditorFileSystemDirectory>`{.interpreted-text
role="ref"}, `EditorInterface<class_EditorInterface>`{.interpreted-text
role="ref"}, `EditorPaths<class_EditorPaths>`{.interpreted-text
role="ref"}, `EditorSelection<class_EditorSelection>`{.interpreted-text
role="ref"},
`EditorUndoRedoManager<class_EditorUndoRedoManager>`{.interpreted-text
role="ref"},
`EditorVCSInterface<class_EditorVCSInterface>`{.interpreted-text
role="ref"}, `Engine<class_Engine>`{.interpreted-text role="ref"},
`EngineDebugger<class_EngineDebugger>`{.interpreted-text role="ref"},
`FramebufferCacheRD<class_FramebufferCacheRD>`{.interpreted-text
role="ref"},
`GDExtensionManager<class_GDExtensionManager>`{.interpreted-text
role="ref"}, `Geometry2D<class_Geometry2D>`{.interpreted-text
role="ref"}, `Geometry3D<class_Geometry3D>`{.interpreted-text
role="ref"}, `Input<class_Input>`{.interpreted-text role="ref"},
`InputMap<class_InputMap>`{.interpreted-text role="ref"},
`IP<class_IP>`{.interpreted-text role="ref"},
`JavaClassWrapper<class_JavaClassWrapper>`{.interpreted-text
role="ref"},
`JavaScriptBridge<class_JavaScriptBridge>`{.interpreted-text
role="ref"}, `JNISingleton<class_JNISingleton>`{.interpreted-text
role="ref"}, `JSONRPC<class_JSONRPC>`{.interpreted-text role="ref"},
`MainLoop<class_MainLoop>`{.interpreted-text role="ref"},
`Marshalls<class_Marshalls>`{.interpreted-text role="ref"},
`MovieWriter<class_MovieWriter>`{.interpreted-text role="ref"},
`NativeMenu<class_NativeMenu>`{.interpreted-text role="ref"},
`NavigationMeshGenerator<class_NavigationMeshGenerator>`{.interpreted-text
role="ref"},
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"},
`NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"}, `Node<class_Node>`{.interpreted-text role="ref"},
`OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`{.interpreted-text
role="ref"},
`OpenXRInteractionProfileMetadata<class_OpenXRInteractionProfileMetadata>`{.interpreted-text
role="ref"}, `OS<class_OS>`{.interpreted-text role="ref"},
`Performance<class_Performance>`{.interpreted-text role="ref"},
`PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
role="ref"},
`PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>`{.interpreted-text
role="ref"},
`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"},
`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`{.interpreted-text
role="ref"}, `PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"},
`PhysicsServer2DManager<class_PhysicsServer2DManager>`{.interpreted-text
role="ref"}, `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"},
`PhysicsServer3DManager<class_PhysicsServer3DManager>`{.interpreted-text
role="ref"},
`PhysicsServer3DRenderingServerHandler<class_PhysicsServer3DRenderingServerHandler>`{.interpreted-text
role="ref"}, `ProjectSettings<class_ProjectSettings>`{.interpreted-text
role="ref"}, `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"}, `RenderData<class_RenderData>`{.interpreted-text
role="ref"}, `RenderingDevice<class_RenderingDevice>`{.interpreted-text
role="ref"}, `RenderingServer<class_RenderingServer>`{.interpreted-text
role="ref"}, `RenderSceneData<class_RenderSceneData>`{.interpreted-text
role="ref"}, `ResourceLoader<class_ResourceLoader>`{.interpreted-text
role="ref"}, `ResourceSaver<class_ResourceSaver>`{.interpreted-text
role="ref"}, `ResourceUID<class_ResourceUID>`{.interpreted-text
role="ref"}, `ScriptLanguage<class_ScriptLanguage>`{.interpreted-text
role="ref"}, `ShaderIncludeDB<class_ShaderIncludeDB>`{.interpreted-text
role="ref"},
`TextServerManager<class_TextServerManager>`{.interpreted-text
role="ref"}, `ThemeDB<class_ThemeDB>`{.interpreted-text role="ref"},
`TileData<class_TileData>`{.interpreted-text role="ref"},
`Time<class_Time>`{.interpreted-text role="ref"},
`TranslationServer<class_TranslationServer>`{.interpreted-text
role="ref"}, `TreeItem<class_TreeItem>`{.interpreted-text role="ref"},
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"},
`UniformSetCacheRD<class_UniformSetCacheRD>`{.interpreted-text
role="ref"},
`WorkerThreadPool<class_WorkerThreadPool>`{.interpreted-text
role="ref"}, `XRServer<class_XRServer>`{.interpreted-text role="ref"},
`XRVRS<class_XRVRS>`{.interpreted-text role="ref"}

Base class for all other classes in the engine.

::: rst-class
classref-introduction-group
:::

## Description

An advanced `Variant<class_Variant>`{.interpreted-text role="ref"} type.
All classes in the engine inherit from Object. Each class may define new
properties, methods or signals, which are available to all inheriting
classes. For example, a `Sprite2D<class_Sprite2D>`{.interpreted-text
role="ref"} instance is able to call
`Node.add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"} because it inherits from
`Node<class_Node>`{.interpreted-text role="ref"}.

You can create new instances, using `Object.new()` in GDScript, or
`new GodotObject` in C#.

To delete an Object instance, call
`free()<class_Object_method_free>`{.interpreted-text role="ref"}. This
is necessary for most classes inheriting Object, because they do not
manage memory on their own, and will otherwise cause memory leaks when
no longer in use. There are a few classes that perform memory
management. For example,
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} (and by
extension `Resource<class_Resource>`{.interpreted-text role="ref"})
deletes itself when no longer referenced, and
`Node<class_Node>`{.interpreted-text role="ref"} deletes its children
when freed.

Objects can have a `Script<class_Script>`{.interpreted-text role="ref"}
attached to them. Once the `Script<class_Script>`{.interpreted-text
role="ref"} is instantiated, it effectively acts as an extension to the
base class, allowing it to define and inherit new properties, methods
and signals.

Inside a `Script<class_Script>`{.interpreted-text role="ref"},
`_get_property_list()<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"} may be overridden to customize properties in several ways.
This allows them to be available to the editor, display as lists of
options, sub-divide into groups, save on disk, etc. Scripting languages
offer easier ways to customize properties, such as with the
`@GDScript.@export<class_@GDScript_annotation_@export>`{.interpreted-text
role="ref"} annotation.

Godot is very dynamic. An object\'s script, and therefore its
properties, methods and signals, can be changed at run-time. Because of
this, there can be occasions where, for example, a property required by
a method may not exist. To prevent run-time errors, see methods such as
`set()<class_Object_method_set>`{.interpreted-text role="ref"},
`get()<class_Object_method_get>`{.interpreted-text role="ref"},
`call()<class_Object_method_call>`{.interpreted-text role="ref"},
`has_method()<class_Object_method_has_method>`{.interpreted-text
role="ref"},
`has_signal()<class_Object_method_has_signal>`{.interpreted-text
role="ref"}, etc. Note that these methods are **much** slower than
direct references.

In GDScript, you can also check if a given property, method, or signal
name exists in an object with the `in` operator:

    var node = Node.new()
    print("name" in node)         # Prints true
    print("get_parent" in node)   # Prints true
    print("tree_entered" in node) # Prints true
    print("unknown" in node)      # Prints false

Notifications are `int<class_int>`{.interpreted-text role="ref"}
constants commonly sent and received by objects. For example, on every
rendered frame, the `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"} notifies nodes inside the tree with a
`Node.NOTIFICATION_PROCESS<class_Node_constant_NOTIFICATION_PROCESS>`{.interpreted-text
role="ref"}. The nodes receive it and may call
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} to update. To make use of notifications, see
`notification()<class_Object_method_notification>`{.interpreted-text
role="ref"} and
`_notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"}.

Lastly, every object can also contain metadata (data about data).
`set_meta()<class_Object_method_set_meta>`{.interpreted-text role="ref"}
can be useful to store information that the object itself does not
depend on. To keep your code clean, making excessive use of metadata is
discouraged.

\*\*Note:\*\* Unlike references to a
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"}, references
to an object stored in a variable can become invalid without being set
to `null`. To check if an object has been deleted, do *not* compare it
against `null`. Instead, use
`@GlobalScope.is_instance_valid()<class_@GlobalScope_method_is_instance_valid>`{.interpreted-text
role="ref"}. It\'s also recommended to inherit from
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} for classes
storing data instead of **Object**.

\*\*Note:\*\* The `script` is not exposed like most properties. To set
or get an object\'s `Script<class_Script>`{.interpreted-text role="ref"}
in code, use
`set_script()<class_Object_method_set_script>`{.interpreted-text
role="ref"} and
`get_script()<class_Object_method_get_script>`{.interpreted-text
role="ref"}, respectively.

\*\*Note:\*\* In a boolean context, an **Object** will evaluate to
`false` if it is equal to `null` or it has been freed. Otherwise, an
**Object** will always evaluate to `true`. See also
`@GlobalScope.is_instance_valid()<class_@GlobalScope_method_is_instance_valid>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Object class introduction <../contributing/development/core_and_modules/object_class>`{.interpreted-text
  role="doc"}
- `When and how to avoid using nodes for everything <../tutorials/best_practices/node_alternatives>`{.interpreted-text
  role="doc"}
- `Object notifications <../tutorials/best_practices/godot_notifications>`{.interpreted-text
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

## Signals

:::: {#class_Object_signal_property_list_changed}
::: rst-class
classref-signal
:::
::::

**property_list_changed**()
`🔗<class_Object_signal_property_list_changed>`{.interpreted-text
role="ref"}

Emitted when
`notify_property_list_changed()<class_Object_method_notify_property_list_changed>`{.interpreted-text
role="ref"} is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_signal_script_changed}
::: rst-class
classref-signal
:::
::::

**script_changed**()
`🔗<class_Object_signal_script_changed>`{.interpreted-text role="ref"}

Emitted when the object\'s script is changed.

\*\*Note:\*\* When this signal is emitted, the new script is not
initialized yet. If you need to access the new script, defer connections
to this signal with
`CONNECT_DEFERRED<class_Object_constant_CONNECT_DEFERRED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Object_ConnectFlags}
::: rst-class
classref-enumeration
:::
::::

enum **ConnectFlags**: `🔗<enum_Object_ConnectFlags>`{.interpreted-text
role="ref"}

:::: {#class_Object_constant_CONNECT_DEFERRED}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text role="ref"}
**CONNECT_DEFERRED** = `1`

Deferred connections trigger their
`Callable<class_Callable>`{.interpreted-text role="ref"}s on idle time
(at the end of the frame), rather than instantly.

:::: {#class_Object_constant_CONNECT_PERSIST}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text role="ref"}
**CONNECT_PERSIST** = `2`

Persisting connections are stored when the object is serialized (such as
when using
`PackedScene.pack()<class_PackedScene_method_pack>`{.interpreted-text
role="ref"}). In the editor, connections created through the Node dock
are always persisting.

:::: {#class_Object_constant_CONNECT_ONE_SHOT}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text role="ref"}
**CONNECT_ONE_SHOT** = `4`

One-shot connections disconnect themselves after emission.

:::: {#class_Object_constant_CONNECT_REFERENCE_COUNTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text role="ref"}
**CONNECT_REFERENCE_COUNTED** = `8`

Reference-counted connections can be assigned to the same
`Callable<class_Callable>`{.interpreted-text role="ref"} multiple times.
Each disconnection decreases the internal counter. The signal fully
disconnects only when the counter reaches 0.

:::: {#class_Object_constant_CONNECT_APPEND_SOURCE_OBJECT}
::: rst-class
classref-enumeration-constant
:::
::::

`ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text role="ref"}
**CONNECT_APPEND_SOURCE_OBJECT** = `16`

The source object is automatically bound when a
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"} is
instantiated. If this flag bit is enabled, the source object will be
appended right after the original arguments of the signal.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Object_constant_NOTIFICATION_POSTINITIALIZE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_POSTINITIALIZE** = `0`
`🔗<class_Object_constant_NOTIFICATION_POSTINITIALIZE>`{.interpreted-text
role="ref"}

Notification received when the object is initialized, before its script
is attached. Used internally.

:::: {#class_Object_constant_NOTIFICATION_PREDELETE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_PREDELETE** = `1`
`🔗<class_Object_constant_NOTIFICATION_PREDELETE>`{.interpreted-text
role="ref"}

Notification received when the object is about to be deleted. Can be
used like destructors in object-oriented programming languages.

:::: {#class_Object_constant_NOTIFICATION_EXTENSION_RELOADED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_EXTENSION_RELOADED** = `2`
`🔗<class_Object_constant_NOTIFICATION_EXTENSION_RELOADED>`{.interpreted-text
role="ref"}

Notification received when the object finishes hot reloading. This
notification is only sent for extensions classes and derived.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Object_private_method__get}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_get**(property: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"} `🔗<class_Object_private_method__get>`{.interpreted-text
role="ref"}

Override this method to customize the behavior of
`get()<class_Object_method_get>`{.interpreted-text role="ref"}. Should
return the given `property`\'s value, or `null` if the `property` should
be handled normally.

Combined with
`_set()<class_Object_private_method__set>`{.interpreted-text role="ref"}
and
`_get_property_list()<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"}, this method allows defining custom properties, which is
particularly useful for editor plugins.

\*\*Note:\*\* This method is not called when getting built-in properties
of an object, including properties defined with
`@GDScript.@export<class_@GDScript_annotation_@export>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

func [get]{#get}(property):

:   

    if property == \"fake_property\":

    :   print(\"Getting my property!\") return 4

func [get_property_list]{#get_property_list}():

:   

    return \[

    :   { \"name\": \"fake_property\", \"type\": TYPE_INT }

    \]
:::

::: code-tab
csharp

public override Variant [Get]{#get}(StringName property) { if (property
== \"FakeProperty\") { GD.Print(\"Getting my property!\"); return 4; }
return default; }

public override Godot.Collections.Array\<Godot.Collections.Dictionary\>
[GetPropertyList]{#getpropertylist}() { return \[ new
Godot.Collections.Dictionary() { { \"name\", \"FakeProperty\" }, {
\"type\", (int)Variant.Type.Int }, }, \]; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__get_property_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_get_property_list**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"}

Override this method to provide a custom list of additional properties
to handle by the engine.

Should return a property list, as an
`Array<class_Array>`{.interpreted-text role="ref"} of dictionaries. The
result is added to the array of
`get_property_list()<class_Object_method_get_property_list>`{.interpreted-text
role="ref"}, and should be formatted in the same way. Each
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} must at
least contain the `name` and `type` entries.

You can use
`_property_can_revert()<class_Object_private_method__property_can_revert>`{.interpreted-text
role="ref"} and
`_property_get_revert()<class_Object_private_method__property_get_revert>`{.interpreted-text
role="ref"} to customize the default values of the properties added by
this method.

The example below displays a list of numbers shown as words going from
`ZERO` to `FIVE`, with `number_count` controlling the size of the list:

::::: tabs
::: code-tab
gdscript

\@tool extends Node

\@export var number_count = 3:

:   

    set(nc):

    :   number_count = nc numbers.resize(number_count)
        notify_property_list_changed()

var numbers = PackedInt32Array(\[0, 0, 0\])

func [get_property_list]{#get_property_list}():

:   var properties = \[\]

    for i in range(number_count):

    :   

        properties.append({

        :   \"name\": \"number\_%d\" % i, \"type\": TYPE_INT, \"hint\":
            PROPERTY_HINT_ENUM, \"hint_string\":
            \"ZERO,ONE,TWO,THREE,FOUR,FIVE\",

        })

    return properties

func [get]{#get}(property):

:   

    if property.begins_with(\"number\_\"):

    :   var index = property.get_slice(\"\_\", 1).to_int() return
        numbers\[index\]

func [set]{#set}(property, value):

:   

    if property.begins_with(\"number\_\"):

    :   var index = property.get_slice(\"\_\", 1).to_int()
        numbers\[index\] = value return true

    return false
:::

::: code-tab
csharp

\[Tool\] public partial class MyNode : Node { private int
[numberCount]{#numbercount};

> \[Export\] public int NumberCount { get =\>
> [numberCount]{#numbercount}; set { [numberCount]{#numbercount} =
> value; [numbers.Resize]{#numbers.resize}([numberCount]{#numbercount});
> NotifyPropertyListChanged(); } }
>
> private Godot.Collections.Array\<int\> [numbers]{#numbers} = \[\];
>
> public override
> Godot.Collections.Array\<Godot.Collections.Dictionary\>
> [GetPropertyList]{#getpropertylist}() {
> Godot.Collections.Array\<Godot.Collections.Dictionary\> properties =
> \[\];
>
> > for (int i = 0; i \< [numberCount]{#numbercount}; i++) {
> > properties.Add(new Godot.Collections.Dictionary() { { \"name\",
> > \$\"number\_{i}\" }, { \"type\", (int)Variant.Type.Int }, {
> > \"hint\", (int)PropertyHint.Enum }, { \"hint_string\",
> > \"Zero,One,Two,Three,Four,Five\" }, }); }
> >
> > return properties;
>
> }
>
> public override Variant [Get]{#get}(StringName property) { string
> propertyName = property.ToString(); if
> (propertyName.StartsWith(\"number\_\")) { int index =
> int.Parse(propertyName.Substring(\"number\_\".Length)); return
> [numbers]{#numbers}\[index\]; } return default; }
>
> public override bool [Set]{#set}(StringName property, Variant value) {
> string propertyName = property.ToString(); if
> (propertyName.StartsWith(\"number\_\")) { int index =
> int.Parse(propertyName.Substring(\"number\_\".Length));
> [numbers]{#numbers}\[index\] = value.As\<int\>(); return true; }
> return false; }

}
:::
:::::

\*\*Note:\*\* This method is intended for advanced purposes. For most
common use cases, the scripting languages offer easier ways to handle
properties. See
`@GDScript.@export<class_@GDScript_annotation_@export>`{.interpreted-text
role="ref"},
`@GDScript.@export_enum<class_@GDScript_annotation_@export_enum>`{.interpreted-text
role="ref"},
`@GDScript.@export_group<class_@GDScript_annotation_@export_group>`{.interpreted-text
role="ref"}, etc. If you want to customize exported properties, use
`_validate_property()<class_Object_private_method__validate_property>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If the object\'s script is not
`@GDScript.@tool<class_@GDScript_annotation_@tool>`{.interpreted-text
role="ref"}, this method will not be called in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__init}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_init**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"} `🔗<class_Object_private_method__init>`{.interpreted-text
role="ref"}

Called when the object\'s script is instantiated, oftentimes after the
object is initialized in memory (through `Object.new()` in GDScript, or
`new GodotObject` in C#). It can be also defined to take in parameters.
This method is similar to a constructor in most programming languages.

\*\*Note:\*\* If
`_init()<class_Object_private_method__init>`{.interpreted-text
role="ref"} is defined with *required* parameters, the Object with
script may only be created directly. If any other means (such as
`PackedScene.instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"} or
`Node.duplicate()<class_Node_method_duplicate>`{.interpreted-text
role="ref"}) are used, the script\'s initialization will fail.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__iter_get}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_iter_get**(iter: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_private_method__iter_get>`{.interpreted-text
role="ref"}

Returns the current iterable value. `iter` stores the iteration state,
but unlike
`_iter_init()<class_Object_private_method__iter_init>`{.interpreted-text
role="ref"} and
`_iter_next()<class_Object_private_method__iter_next>`{.interpreted-text
role="ref"} the state is supposed to be read-only, so there is no
`Array<class_Array>`{.interpreted-text role="ref"} wrapper.

\*\*Tip:\*\* In GDScript, you can use a subtype of
`Variant<class_Variant>`{.interpreted-text role="ref"} as the return
type for
`_iter_get()<class_Object_private_method__iter_get>`{.interpreted-text
role="ref"}. The specified type will be used to set the type of the
iterator variable in `for` loops, enhancing type safety.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__iter_init}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_iter_init**(iter:
`Array<class_Array>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_private_method__iter_init>`{.interpreted-text
role="ref"}

Initializes the iterator. `iter` stores the iteration state. Since
GDScript does not support passing arguments by reference, a
single-element array is used as a wrapper. Returns `true` so long as the
iterator has not reached the end.

    class MyRange:
        var _from
        var _to

        func _init(from, to):
            assert(from <= to)
            _from = from
            _to = to

        func _iter_init(iter):
            iter[0] = _from
            return iter[0] < _to

        func _iter_next(iter):
            iter[0] += 1
            return iter[0] < _to

        func _iter_get(iter):
            return iter

    func _ready():
        var my_range = MyRange.new(2, 5)
        for x in my_range:
            print(x) # Prints 2, 3, 4.

\*\*Note:\*\* Alternatively, you can ignore `iter` and use the object\'s
state instead, see [online
docs](../tutorials/scripting/gdscript/gdscript_advanced.html#custom-iterators)
for an example. Note that in this case you will not be able to reuse the
same iterator instance in nested loops. Also, make sure you reset the
iterator state in this method if you want to reuse the same instance
multiple times.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__iter_next}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_iter_next**(iter:
`Array<class_Array>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_private_method__iter_next>`{.interpreted-text
role="ref"}

Moves the iterator to the next iteration. `iter` stores the iteration
state. Since GDScript does not support passing arguments by reference, a
single-element array is used as a wrapper. Returns `true` so long as the
iterator has not reached the end.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__notification}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_notification**(what: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_private_method__notification>`{.interpreted-text
role="ref"}

Called when the object receives a notification, which can be identified
in `what` by comparing it with a constant. See also
`notification()<class_Object_method_notification>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

func [notification]{#notification}(what):

:   

    if what == NOTIFICATION_PREDELETE:

    :   print(\"Goodbye!\")
:::

::: code-tab
csharp

public override void [Notification]{#notification}(int what) { if (what
== NotificationPredelete) { GD.Print(\"Goodbye!\"); } }
:::
:::::

\*\*Note:\*\* The base **Object** defines a few notifications
(`NOTIFICATION_POSTINITIALIZE<class_Object_constant_NOTIFICATION_POSTINITIALIZE>`{.interpreted-text
role="ref"} and
`NOTIFICATION_PREDELETE<class_Object_constant_NOTIFICATION_PREDELETE>`{.interpreted-text
role="ref"}). Inheriting classes such as
`Node<class_Node>`{.interpreted-text role="ref"} define a lot more
notifications, which are also received by this method.

\*\*Note:\*\* Unlike other virtual methods, this method is called
automatically for every script that overrides it. This means that the
base implementation should not be called via `super` in GDScript or its
equivalents in other languages.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__property_can_revert}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_property_can_revert**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_private_method__property_can_revert>`{.interpreted-text
role="ref"}

Override this method to customize the given `property`\'s revert
behavior. Should return `true` if the `property` has a custom default
value and is revertible in the Inspector dock. Use
`_property_get_revert()<class_Object_private_method__property_get_revert>`{.interpreted-text
role="ref"} to specify the `property`\'s default value.

\*\*Note:\*\* This method must return consistently, regardless of the
current value of the `property`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__property_get_revert}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_property_get_revert**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_private_method__property_get_revert>`{.interpreted-text
role="ref"}

Override this method to customize the given `property`\'s revert
behavior. Should return the default value for the `property`. If the
default value differs from the `property`\'s current value, a revert
icon is displayed in the Inspector dock.

\*\*Note:\*\*
`_property_can_revert()<class_Object_private_method__property_can_revert>`{.interpreted-text
role="ref"} must also be overridden for this method to be called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__set}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_set**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"} `🔗<class_Object_private_method__set>`{.interpreted-text
role="ref"}

Override this method to customize the behavior of
`set()<class_Object_method_set>`{.interpreted-text role="ref"}. Should
set the `property` to `value` and return `true`, or `false` if the
`property` should be handled normally. The *exact* way to set the
`property` is up to this method\'s implementation.

Combined with
`_get()<class_Object_private_method__get>`{.interpreted-text role="ref"}
and
`_get_property_list()<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"}, this method allows defining custom properties, which is
particularly useful for editor plugins.

\*\*Note:\*\* This method is not called when setting built-in properties
of an object, including properties defined with
`@GDScript.@export<class_@GDScript_annotation_@export>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var internal_data = {}

func [set]{#set}(property, value):

:   

    if property == \"fake_property\":

    :   \# Storing the value in the fake property.
        internal_data\[\"fake_property\"\] = value return true

    return false

func [get_property_list]{#get_property_list}():

:   

    return \[

    :   { \"name\": \"fake_property\", \"type\": TYPE_INT }

    \]
:::

::: code-tab
csharp

private Godot.Collections.Dictionary [internalData]{#internaldata} = new
Godot.Collections.Dictionary();

public override bool [Set]{#set}(StringName property, Variant value) {
if (property == \"FakeProperty\") { // Storing the value in the fake
property. [internalData]{#internaldata}\[\"FakeProperty\"\] = value;
return true; }

> return false;

}

public override Godot.Collections.Array\<Godot.Collections.Dictionary\>
[GetPropertyList]{#getpropertylist}() { return \[ new
Godot.Collections.Dictionary() { { \"name\", \"FakeProperty\" }, {
\"type\", (int)Variant.Type.Int }, }, \]; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__to_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **\_to_string**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_private_method__to_string>`{.interpreted-text
role="ref"}

Override this method to customize the return value of
`to_string()<class_Object_method_to_string>`{.interpreted-text
role="ref"}, and therefore the object\'s representation as a
`String<class_String>`{.interpreted-text role="ref"}.

    func _to_string():
        return "Welcome to Godot 4!"

    func _init():
        print(self)       # Prints "Welcome to Godot 4!"
        var a = str(self) # a is "Welcome to Godot 4!"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_private_method__validate_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_validate_property**(property:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_private_method__validate_property>`{.interpreted-text
role="ref"}

Override this method to customize existing properties. Every property
info goes through this method, except properties added with
`_get_property_list()<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"}. The dictionary contents is the same as in
`_get_property_list()<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

\@tool extends Node

\@export var is_number_editable: bool:

:   

    set(value):

    :   is_number_editable = value notify_property_list_changed()

\@export var number: int

func [validate_property]{#validate_property}(property: Dictionary):

:   

    if property.name == \"number\" and not is_number_editable:

    :   property.usage \|= PROPERTY_USAGE_READ_ONLY
:::

::: code-tab
csharp

\[Tool\] public partial class MyNode : Node { private bool
[isNumberEditable]{#isnumbereditable};

> \[Export\] public bool IsNumberEditable { get =\>
> [isNumberEditable]{#isnumbereditable}; set {
> [isNumberEditable]{#isnumbereditable} = value;
> NotifyPropertyListChanged(); } }
>
> \[Export\] public int Number { get; set; }
>
> public override void
> [ValidateProperty]{#validateproperty}(Godot.Collections.Dictionary
> property) { if (property\[\"name\"\].AsStringName() ==
> PropertyName.Number && !IsNumberEditable) { var usage =
> property\[\"usage\"\].As\<PropertyUsageFlags\>() \|
> PropertyUsageFlags.ReadOnly; property\[\"usage\"\] = (int)usage; } }

}
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_add_user_signal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_user_signal**(signal: `String<class_String>`{.interpreted-text
role="ref"}, arguments: `Array<class_Array>`{.interpreted-text
role="ref"} = \[\])
`🔗<class_Object_method_add_user_signal>`{.interpreted-text role="ref"}

Adds a user-defined signal named `signal`. Optional arguments for the
signal can be added as an `Array<class_Array>`{.interpreted-text
role="ref"} of dictionaries, each defining a `name`
`String<class_String>`{.interpreted-text role="ref"} and a `type`
`int<class_int>`{.interpreted-text role="ref"} (see
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"}). See also
`has_user_signal()<class_Object_method_has_user_signal>`{.interpreted-text
role="ref"} and
`remove_user_signal()<class_Object_method_remove_user_signal>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

add_user_signal(\"hurt\", \[

:   { \"name\": \"damage\", \"type\": TYPE_INT }, { \"name\":
    \"source\", \"type\": TYPE_OBJECT }

\])
:::

::: code-tab
csharp

AddUserSignal(\"Hurt\", \[ new Godot.Collections.Dictionary() { {
\"name\", \"damage\" }, { \"type\", (int)Variant.Type.Int }, }, new
Godot.Collections.Dictionary() { { \"name\", \"source\" }, { \"type\",
(int)Variant.Type.Object }, }, \]);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_call}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **call**(method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_call>`{.interpreted-text
role="ref"}

Calls the `method` on the object and returns the result. This method
supports a variable number of arguments, so parameters can be passed as
a comma separated list.

::::: tabs
::: code-tab
gdscript

var node = Node3D.new() node.call(\"rotate\", Vector3(1.0, 0.0, 0.0),
1.571)
:::

::: code-tab
csharp

var node = new Node3D(); node.Call(Node3D.MethodName.Rotate, new
Vector3(1f, 0f, 0f), 1.571f);
:::
:::::

\*\*Note:\*\* In C#, `method` must be in snake_case when referring to
built-in Godot methods. Prefer using the names exposed in the
`MethodName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_call_deferred}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**call_deferred**(method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_call_deferred>`{.interpreted-text
role="ref"}

Calls the `method` on the object during idle time. Always returns
`null`, **not** the method\'s result.

Idle time happens mainly at the end of process and physics frames. In
it, deferred calls will be run until there are none left, which means
you can defer calls from other deferred calls and they\'ll still be run
in the current idle time cycle. This means you should not call a method
deferred from itself (or from a method called by it), as this causes
infinite recursion the same way as if you had called the method
directly.

This method supports a variable number of arguments, so parameters can
be passed as a comma separated list.

::::: tabs
::: code-tab
gdscript

var node = Node3D.new() node.call_deferred(\"rotate\", Vector3(1.0, 0.0,
0.0), 1.571)
:::

::: code-tab
csharp

var node = new Node3D(); node.CallDeferred(Node3D.MethodName.Rotate, new
Vector3(1f, 0f, 0f), 1.571f);
:::
:::::

See also
`Callable.call_deferred()<class_Callable_method_call_deferred>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In C#, `method` must be in snake_case when referring to
built-in Godot methods. Prefer using the names exposed in the
`MethodName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

\*\*Note:\*\* If you\'re looking to delay the function call by a frame,
refer to the
`SceneTree.process_frame<class_SceneTree_signal_process_frame>`{.interpreted-text
role="ref"} and
`SceneTree.physics_frame<class_SceneTree_signal_physics_frame>`{.interpreted-text
role="ref"} signals.

    var node = Node3D.new()
    # Make a Callable and bind the arguments to the node's rotate() call.
    var callable = node.rotate.bind(Vector3(1.0, 0.0, 0.0), 1.571)
    # Connect the callable to the process_frame signal, so it gets called in the next process frame.
    # CONNECT_ONE_SHOT makes sure it only gets called once instead of every frame.
    get_tree().process_frame.connect(callable, CONNECT_ONE_SHOT)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_callv}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **callv**(method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, arg_array:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Object_method_callv>`{.interpreted-text role="ref"}

Calls the `method` on the object and returns the result. Unlike
`call()<class_Object_method_call>`{.interpreted-text role="ref"}, this
method expects all parameters to be contained inside `arg_array`.

::::: tabs
::: code-tab
gdscript

var node = Node3D.new() node.callv(\"rotate\", \[Vector3(1.0, 0.0, 0.0),
1.571\])
:::

::: code-tab
csharp

var node = new Node3D(); node.Callv(Node3D.MethodName.Rotate, \[new
Vector3(1f, 0f, 0f), 1.571f\]);
:::
:::::

\*\*Note:\*\* In C#, `method` must be in snake_case when referring to
built-in Godot methods. Prefer using the names exposed in the
`MethodName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_can_translate_messages}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**can_translate_messages**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_can_translate_messages>`{.interpreted-text
role="ref"}

Returns `true` if the object is allowed to translate messages with
`tr()<class_Object_method_tr>`{.interpreted-text role="ref"} and
`tr_n()<class_Object_method_tr_n>`{.interpreted-text role="ref"}. See
also
`set_message_translation()<class_Object_method_set_message_translation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_cancel_free}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cancel_free**()
`🔗<class_Object_method_cancel_free>`{.interpreted-text role="ref"}

If this method is called during
`NOTIFICATION_PREDELETE<class_Object_constant_NOTIFICATION_PREDELETE>`{.interpreted-text
role="ref"}, this object will reject being freed and will remain
allocated. This is mostly an internal function used for error handling
to avoid the user from freeing objects when they are not intended to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_connect}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**connect**(signal: `StringName<class_StringName>`{.interpreted-text
role="ref"}, callable: `Callable<class_Callable>`{.interpreted-text
role="ref"}, flags: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_Object_method_connect>`{.interpreted-text role="ref"}

Connects a `signal` by name to a `callable`. Optional `flags` can be
also added to configure the connection\'s behavior (see
`ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text role="ref"}
constants).

A signal can only be connected once to the same
`Callable<class_Callable>`{.interpreted-text role="ref"}. If the signal
is already connected, this method returns
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} and generates an error, unless the signal is connected with
`CONNECT_REFERENCE_COUNTED<class_Object_constant_CONNECT_REFERENCE_COUNTED>`{.interpreted-text
role="ref"}. To prevent this, use
`is_connected()<class_Object_method_is_connected>`{.interpreted-text
role="ref"} first to check for existing connections.

\*\*Note:\*\* If the `callable`\'s object is freed, the connection will
be lost.

\*\*Note:\*\* In GDScript, it is generally recommended to connect
signals with
`Signal.connect()<class_Signal_method_connect>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* This operation (and all other signal related operations)
is thread-safe.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_disconnect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect**(signal: `StringName<class_StringName>`{.interpreted-text
role="ref"}, callable: `Callable<class_Callable>`{.interpreted-text
role="ref"}) `🔗<class_Object_method_disconnect>`{.interpreted-text
role="ref"}

Disconnects a `signal` by name from a given `callable`. If the
connection does not exist, generates an error. Use
`is_connected()<class_Object_method_is_connected>`{.interpreted-text
role="ref"} to make sure that the connection exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_emit_signal}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**emit_signal**(signal: `StringName<class_StringName>`{.interpreted-text
role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_emit_signal>`{.interpreted-text
role="ref"}

Emits the given `signal` by name. The signal must exist, so it should be
a built-in signal of this class or one of its inherited classes, or a
user-defined signal (see
`add_user_signal()<class_Object_method_add_user_signal>`{.interpreted-text
role="ref"}). This method supports a variable number of arguments, so
parameters can be passed as a comma separated list.

Returns
`@GlobalScope.ERR_UNAVAILABLE<class_@GlobalScope_constant_ERR_UNAVAILABLE>`{.interpreted-text
role="ref"} if `signal` does not exist or the parameters are invalid.

::::: tabs
::: code-tab
gdscript

emit_signal(\"hit\", \"sword\", 100) emit_signal(\"game_over\")
:::

::: code-tab
csharp

EmitSignal(SignalName.Hit, \"sword\", 100);
EmitSignal(SignalName.GameOver);
:::
:::::

\*\*Note:\*\* In C#, `signal` must be in snake_case when referring to
built-in Godot signals. Prefer using the names exposed in the
`SignalName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_free}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **free**()
`🔗<class_Object_method_free>`{.interpreted-text role="ref"}

Deletes the object from memory. Pre-existing references to the object
become invalid, and any attempt to access them will result in a runtime
error. Checking the references with
`@GlobalScope.is_instance_valid()<class_@GlobalScope_method_is_instance_valid>`{.interpreted-text
role="ref"} will return `false`. This is equivalent to the `memdelete`
function in GDExtension C++.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **get**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_get>`{.interpreted-text role="ref"}

Returns the `Variant<class_Variant>`{.interpreted-text role="ref"} value
of the given `property`. If the `property` does not exist, this method
returns `null`.

::::: tabs
::: code-tab
gdscript

var node = Node2D.new() node.rotation = 1.5 var a =
node.get(\"rotation\") \# a is 1.5
:::

::: code-tab
csharp

var node = new Node2D(); node.Rotation = 1.5f; var a =
node.Get(Node2D.PropertyName.Rotation); // a is 1.5
:::
:::::

\*\*Note:\*\* In C#, `property` must be in snake_case when referring to
built-in Godot properties. Prefer using the names exposed in the
`PropertyName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_class}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_class**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_get_class>`{.interpreted-text
role="ref"}

Returns the object\'s built-in class name, as a
`String<class_String>`{.interpreted-text role="ref"}. See also
`is_class()<class_Object_method_is_class>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method ignores `class_name` declarations. If this
object\'s script has defined a `class_name`, the base, built-in class
name is returned instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_incoming_connections}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_incoming_connections**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_get_incoming_connections>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of signal
connections received by this object. Each connection is represented as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} that
contains three entries:

- `signal` is a reference to the
  `Signal<class_Signal>`{.interpreted-text role="ref"};
- `callable` is a reference to the
  `Callable<class_Callable>`{.interpreted-text role="ref"};
- `flags` is a combination of
  `ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text
  role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_indexed}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_indexed**(property_path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_get_indexed>`{.interpreted-text
role="ref"}

Gets the object\'s property indexed by the given `property_path`. The
path should be a `NodePath<class_NodePath>`{.interpreted-text
role="ref"} relative to the current object and can use the colon
character (`:`) to access nested properties.

\*\*Examples:\*\* `"position:x"` or `"material:next_pass:blend_mode"`.

::::: tabs
::: code-tab
gdscript

var node = Node2D.new() node.position = Vector2(5, -10) var a =
node.get_indexed(\"position\") \# a is Vector2(5, -10) var b =
node.get_indexed(\"position:y\") \# b is -10
:::

::: code-tab
csharp

var node = new Node2D(); node.Position = new Vector2(5, -10); var a =
node.GetIndexed(\"position\"); // a is Vector2(5, -10) var b =
node.GetIndexed(\"position:y\"); // b is -10
:::
:::::

\*\*Note:\*\* In C#, `property_path` must be in snake_case when
referring to built-in Godot properties. Prefer using the names exposed
in the `PropertyName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

\*\*Note:\*\* This method does not support actual paths to nodes in the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}, only
sub-property paths. In the context of nodes, use
`Node.get_node_and_resource()<class_Node_method_get_node_and_resource>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_instance_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_instance_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}

Returns the object\'s unique instance ID. This ID can be saved in
`EncodedObjectAsID<class_EncodedObjectAsID>`{.interpreted-text
role="ref"}, and can be used to retrieve this object instance with
`@GlobalScope.instance_from_id()<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This ID is only useful during the current session. It
won\'t correspond to a similar object if the ID is sent over a network,
or loaded from a file at a later time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_meta}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_meta**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, default: `Variant<class_Variant>`{.interpreted-text
role="ref"} = null)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_get_meta>`{.interpreted-text
role="ref"}

Returns the object\'s metadata value for the given entry `name`. If the
entry does not exist, returns `default`. If `default` is `null`, an
error is also generated.

\*\*Note:\*\* A metadata\'s name must be a valid identifier as per
`StringName.is_valid_identifier()<class_StringName_method_is_valid_identifier>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* Metadata that has a name starting with an underscore (`_`)
is considered editor-only. Editor-only metadata is not displayed in the
Inspector and should not be edited, although it can still be found by
this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_meta_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_meta_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_get_meta_list>`{.interpreted-text
role="ref"}

Returns the object\'s metadata entry names as an
`Array<class_Array>`{.interpreted-text role="ref"} of
`StringName<class_StringName>`{.interpreted-text role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_method_argument_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_method_argument_count**(method:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_get_method_argument_count>`{.interpreted-text
role="ref"}

Returns the number of arguments of the given `method` by name.

\*\*Note:\*\* In C#, `method` must be in snake_case when referring to
built-in Godot methods. Prefer using the names exposed in the
`MethodName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_method_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_method_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_get_method_list>`{.interpreted-text
role="ref"}

Returns this object\'s methods and their signatures as an
`Array<class_Array>`{.interpreted-text role="ref"} of dictionaries. Each
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} contains
the following entries:

- `name` is the name of the method, as a
  `String<class_String>`{.interpreted-text role="ref"};
- `args` is an `Array<class_Array>`{.interpreted-text role="ref"} of
  dictionaries representing the arguments;
- `default_args` is the default arguments as an
  `Array<class_Array>`{.interpreted-text role="ref"} of variants;
- `flags` is a combination of
  `MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
  role="ref"};
- `id` is the method\'s internal identifier
  `int<class_int>`{.interpreted-text role="ref"};
- `return` is the returned value, as a
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"};

\*\*Note:\*\* The dictionaries of `args` and `return` are formatted
identically to the results of
`get_property_list()<class_Object_method_get_property_list>`{.interpreted-text
role="ref"}, although not all entries are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_property_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_property_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_get_property_list>`{.interpreted-text
role="ref"}

Returns the object\'s property list as an
`Array<class_Array>`{.interpreted-text role="ref"} of dictionaries. Each
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} contains
the following entries:

- `name` is the property\'s name, as a
  `String<class_String>`{.interpreted-text role="ref"};
- `class_name` is an empty
  `StringName<class_StringName>`{.interpreted-text role="ref"}, unless
  the property is
  `@GlobalScope.TYPE_OBJECT<class_@GlobalScope_constant_TYPE_OBJECT>`{.interpreted-text
  role="ref"} and it inherits from a class;
- `type` is the property\'s type, as an
  `int<class_int>`{.interpreted-text role="ref"} (see
  `Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
  role="ref"});
- `hint` is *how* the property is meant to be edited (see
  `PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
  role="ref"});
- `hint_string` depends on the hint (see
  `PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
  role="ref"});
- `usage` is a combination of
  `PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
  role="ref"}.

\*\*Note:\*\* In GDScript, all class members are treated as properties.
In C# and GDExtension, it may be necessary to explicitly mark class
members as Godot properties using decorators or attributes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_script}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **get_script**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_get_script>`{.interpreted-text
role="ref"}

Returns the object\'s `Script<class_Script>`{.interpreted-text
role="ref"} instance, or `null` if no script is attached.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_signal_connection_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_signal_connection_list**(signal:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_get_signal_connection_list>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
connections for the given `signal` name. Each connection is represented
as a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"} that
contains three entries:

- `signal` is a reference to the
  `Signal<class_Signal>`{.interpreted-text role="ref"};
- `callable` is a reference to the connected
  `Callable<class_Callable>`{.interpreted-text role="ref"};
- `flags` is a combination of
  `ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text
  role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_signal_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_signal_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_get_signal_list>`{.interpreted-text
role="ref"}

Returns the list of existing signals as an
`Array<class_Array>`{.interpreted-text role="ref"} of dictionaries.

\*\*Note:\*\* Due of the implementation, each
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} is
formatted very similarly to the returned values of
`get_method_list()<class_Object_method_get_method_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_get_translation_domain}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_translation_domain**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_get_translation_domain>`{.interpreted-text
role="ref"}

Returns the name of the translation domain used by
`tr()<class_Object_method_tr>`{.interpreted-text role="ref"} and
`tr_n()<class_Object_method_tr_n>`{.interpreted-text role="ref"}. See
also `TranslationServer<class_TranslationServer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_has_connections}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_connections**(signal:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_has_connections>`{.interpreted-text
role="ref"}

Returns `true` if any connection exists on the given `signal` name.

\*\*Note:\*\* In C#, `signal` must be in snake_case when referring to
built-in Godot methods. Prefer using the names exposed in the
`SignalName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_has_meta}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_meta**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_has_meta>`{.interpreted-text
role="ref"}

Returns `true` if a metadata entry is found with the given `name`. See
also `get_meta()<class_Object_method_get_meta>`{.interpreted-text
role="ref"},
`set_meta()<class_Object_method_set_meta>`{.interpreted-text role="ref"}
and `remove_meta()<class_Object_method_remove_meta>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* A metadata\'s name must be a valid identifier as per
`StringName.is_valid_identifier()<class_StringName_method_is_valid_identifier>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* Metadata that has a name starting with an underscore (`_`)
is considered editor-only. Editor-only metadata is not displayed in the
Inspector and should not be edited, although it can still be found by
this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_has_method}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_method**(method:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_has_method>`{.interpreted-text
role="ref"}

Returns `true` if the given `method` name exists in the object.

\*\*Note:\*\* In C#, `method` must be in snake_case when referring to
built-in Godot methods. Prefer using the names exposed in the
`MethodName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_has_signal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_signal**(signal:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_has_signal>`{.interpreted-text
role="ref"}

Returns `true` if the given `signal` name exists in the object.

\*\*Note:\*\* In C#, `signal` must be in snake_case when referring to
built-in Godot signals. Prefer using the names exposed in the
`SignalName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_has_user_signal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_user_signal**(signal:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_has_user_signal>`{.interpreted-text
role="ref"}

Returns `true` if the given user-defined `signal` name exists. Only
signals added with
`add_user_signal()<class_Object_method_add_user_signal>`{.interpreted-text
role="ref"} are included. See also
`remove_user_signal()<class_Object_method_remove_user_signal>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_is_blocking_signals}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_blocking_signals**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_is_blocking_signals>`{.interpreted-text
role="ref"}

Returns `true` if the object is blocking its signals from being emitted.
See
`set_block_signals()<class_Object_method_set_block_signals>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_is_class}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_class**(class:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_is_class>`{.interpreted-text
role="ref"}

Returns `true` if the object inherits from the given `class`. See also
`get_class()<class_Object_method_get_class>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var sprite2d = Sprite2D.new() sprite2d.is_class(\"Sprite2D\") \# Returns
true sprite2d.is_class(\"Node\") \# Returns true
sprite2d.is_class(\"Node3D\") \# Returns false
:::

::: code-tab
csharp

var sprite2D = new Sprite2D(); sprite2D.IsClass(\"Sprite2D\"); //
Returns true sprite2D.IsClass(\"Node\"); // Returns true
sprite2D.IsClass(\"Node3D\"); // Returns false
:::
:::::

\*\*Note:\*\* This method ignores `class_name` declarations in the
object\'s script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_is_connected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_connected**(signal:
`StringName<class_StringName>`{.interpreted-text role="ref"}, callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_is_connected>`{.interpreted-text
role="ref"}

Returns `true` if a connection exists between the given `signal` name
and `callable`.

\*\*Note:\*\* In C#, `signal` must be in snake_case when referring to
built-in Godot signals. Prefer using the names exposed in the
`SignalName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_is_queued_for_deletion}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_queued_for_deletion**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_is_queued_for_deletion>`{.interpreted-text
role="ref"}

Returns `true` if the
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"} method was called for the object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_notification}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notification**(what: `int<class_int>`{.interpreted-text role="ref"},
reversed: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Object_method_notification>`{.interpreted-text role="ref"}

Sends the given `what` notification to all classes inherited by the
object, triggering calls to
`_notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"}, starting from the highest ancestor (the **Object** class)
and going down to the object\'s script.

If `reversed` is `true`, the call order is reversed.

::::: tabs
::: code-tab
gdscript

var player = Node2D.new() player.set_script(load(\"res://player.gd\"))

player.notification(NOTIFICATION_ENTER_TREE) \# The call order is Object
-\> Node -\> Node2D -\> player.gd.

player.notification(NOTIFICATION_ENTER_TREE, true) \# The call order is
player.gd -\> Node2D -\> Node -\> Object.
:::

::: code-tab
csharp

var player = new Node2D();
player.SetScript(GD.Load(\"res://player.gd\"));

player.Notification(NotificationEnterTree); // The call order is
GodotObject -\> Node -\> Node2D -\> player.gd.

player.Notification(NotificationEnterTree, true); // The call order is
player.gd -\> Node2D -\> Node -\> GodotObject.
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_notify_property_list_changed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notify_property_list_changed**()
`🔗<class_Object_method_notify_property_list_changed>`{.interpreted-text
role="ref"}

Emits the
`property_list_changed<class_Object_signal_property_list_changed>`{.interpreted-text
role="ref"} signal. This is mainly used to refresh the editor, so that
the Inspector and editor plugins are properly updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_property_can_revert}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**property_can_revert**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_property_can_revert>`{.interpreted-text
role="ref"}

Returns `true` if the given `property` has a custom default value. Use
`property_get_revert()<class_Object_method_property_get_revert>`{.interpreted-text
role="ref"} to get the `property`\'s default value.

\*\*Note:\*\* This method is used by the Inspector dock to display a
revert icon. The object must implement
`_property_can_revert()<class_Object_private_method__property_can_revert>`{.interpreted-text
role="ref"} to customize the default value. If
`_property_can_revert()<class_Object_private_method__property_can_revert>`{.interpreted-text
role="ref"} is not implemented, this method returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_property_get_revert}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**property_get_revert**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Object_method_property_get_revert>`{.interpreted-text
role="ref"}

Returns the custom default value of the given `property`. Use
`property_can_revert()<class_Object_method_property_can_revert>`{.interpreted-text
role="ref"} to check if the `property` has a custom default value.

\*\*Note:\*\* This method is used by the Inspector dock to display a
revert icon. The object must implement
`_property_get_revert()<class_Object_private_method__property_get_revert>`{.interpreted-text
role="ref"} to customize the default value. If
`_property_get_revert()<class_Object_private_method__property_get_revert>`{.interpreted-text
role="ref"} is not implemented, this method returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_remove_meta}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_meta**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Object_method_remove_meta>`{.interpreted-text
role="ref"}

Removes the given entry `name` from the object\'s metadata. See also
`has_meta()<class_Object_method_has_meta>`{.interpreted-text
role="ref"},
`get_meta()<class_Object_method_get_meta>`{.interpreted-text role="ref"}
and `set_meta()<class_Object_method_set_meta>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* A metadata\'s name must be a valid identifier as per
`StringName.is_valid_identifier()<class_StringName_method_is_valid_identifier>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* Metadata that has a name starting with an underscore (`_`)
is considered editor-only. Editor-only metadata is not displayed in the
Inspector and should not be edited, although it can still be found by
this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_remove_user_signal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_user_signal**(signal:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Object_method_remove_user_signal>`{.interpreted-text
role="ref"}

Removes the given user signal `signal` from the object. See also
`add_user_signal()<class_Object_method_add_user_signal>`{.interpreted-text
role="ref"} and
`has_user_signal()<class_Object_method_has_user_signal>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set**(property: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"}) `🔗<class_Object_method_set>`{.interpreted-text role="ref"}

Assigns `value` to the given `property`. If the property does not exist
or the given `value`\'s type doesn\'t match, nothing happens.

::::: tabs
::: code-tab
gdscript

var node = Node2D.new() node.set(\"global_scale\", Vector2(8, 2.5))
print(node.global_scale) \# Prints (8.0, 2.5)
:::

::: code-tab
csharp

var node = new Node2D(); node.Set(Node2D.PropertyName.GlobalScale, new
Vector2(8, 2.5f)); GD.Print(node.GlobalScale); // Prints (8, 2.5)
:::
:::::

\*\*Note:\*\* In C#, `property` must be in snake_case when referring to
built-in Godot properties. Prefer using the names exposed in the
`PropertyName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_set_block_signals}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_block_signals**(enable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Object_method_set_block_signals>`{.interpreted-text
role="ref"}

If set to `true`, the object becomes unable to emit signals. As such,
`emit_signal()<class_Object_method_emit_signal>`{.interpreted-text
role="ref"} and signal connections will not work, until it is set to
`false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_set_deferred}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_deferred**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Object_method_set_deferred>`{.interpreted-text role="ref"}

Assigns `value` to the given `property`, at the end of the current
frame. This is equivalent to calling
`set()<class_Object_method_set>`{.interpreted-text role="ref"} through
`call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var node = Node2D.new() add_child(node)

node.rotation = 1.5 node.set_deferred(\"rotation\", 3.0)
print(node.rotation) \# Prints 1.5

await get_tree().process_frame print(node.rotation) \# Prints 3.0
:::

::: code-tab
csharp

var node = new Node2D(); node.Rotation = 1.5f;
node.SetDeferred(Node2D.PropertyName.Rotation, 3f);
GD.Print(node.Rotation); // Prints 1.5

await ToSignal(GetTree(), SceneTree.SignalName.ProcessFrame);
GD.Print(node.Rotation); // Prints 3.0
:::
:::::

\*\*Note:\*\* In C#, `property` must be in snake_case when referring to
built-in Godot properties. Prefer using the names exposed in the
`PropertyName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_set_indexed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_indexed**(property_path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Object_method_set_indexed>`{.interpreted-text role="ref"}

Assigns a new `value` to the property identified by the `property_path`.
The path should be a `NodePath<class_NodePath>`{.interpreted-text
role="ref"} relative to this object, and can use the colon character
(`:`) to access nested properties.

::::: tabs
::: code-tab
gdscript

var node = Node2D.new() node.set_indexed(\"position\", Vector2(42, 0))
node.set_indexed(\"position:y\", -10) print(node.position) \# Prints
(42.0, -10.0)
:::

::: code-tab
csharp

var node = new Node2D(); node.SetIndexed(\"position\", new Vector2(42,
0)); node.SetIndexed(\"position:y\", -10); GD.Print(node.Position); //
Prints (42, -10)
:::
:::::

\*\*Note:\*\* In C#, `property_path` must be in snake_case when
referring to built-in Godot properties. Prefer using the names exposed
in the `PropertyName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_set_message_translation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_message_translation**(enable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Object_method_set_message_translation>`{.interpreted-text
role="ref"}

If set to `true`, allows the object to translate messages with
`tr()<class_Object_method_tr>`{.interpreted-text role="ref"} and
`tr_n()<class_Object_method_tr_n>`{.interpreted-text role="ref"}.
Enabled by default. See also
`can_translate_messages()<class_Object_method_can_translate_messages>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_set_meta}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_meta**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"}) `🔗<class_Object_method_set_meta>`{.interpreted-text
role="ref"}

Adds or changes the entry `name` inside the object\'s metadata. The
metadata `value` can be any `Variant<class_Variant>`{.interpreted-text
role="ref"}, although some types cannot be serialized correctly.

If `value` is `null`, the entry is removed. This is the equivalent of
using `remove_meta()<class_Object_method_remove_meta>`{.interpreted-text
role="ref"}. See also
`has_meta()<class_Object_method_has_meta>`{.interpreted-text role="ref"}
and `get_meta()<class_Object_method_get_meta>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* A metadata\'s name must be a valid identifier as per
`StringName.is_valid_identifier()<class_StringName_method_is_valid_identifier>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* Metadata that has a name starting with an underscore (`_`)
is considered editor-only. Editor-only metadata is not displayed in the
Inspector and should not be edited, although it can still be found by
this method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_set_script}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_script**(script: `Variant<class_Variant>`{.interpreted-text
role="ref"}) `🔗<class_Object_method_set_script>`{.interpreted-text
role="ref"}

Attaches `script` to the object, and instantiates it. As a result, the
script\'s `_init()<class_Object_private_method__init>`{.interpreted-text
role="ref"} is called. A `Script<class_Script>`{.interpreted-text
role="ref"} is used to extend the object\'s functionality.

If a script already exists, its instance is detached, and its property
values and state are lost. Built-in property values are still kept.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_set_translation_domain}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_translation_domain**(domain:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Object_method_set_translation_domain>`{.interpreted-text
role="ref"}

Sets the name of the translation domain used by
`tr()<class_Object_method_tr>`{.interpreted-text role="ref"} and
`tr_n()<class_Object_method_tr_n>`{.interpreted-text role="ref"}. See
also `TranslationServer<class_TranslationServer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_to_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **to_string**()
`🔗<class_Object_method_to_string>`{.interpreted-text role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"}
representing the object. Defaults to `"<ClassName#RID>"`. Override
`_to_string()<class_Object_private_method__to_string>`{.interpreted-text
role="ref"} to customize the string representation of the object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_tr}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **tr**(message:
`StringName<class_StringName>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_tr>`{.interpreted-text role="ref"}

Translates a `message`, using the translation catalogs configured in the
Project Settings. Further `context` can be specified to help with the
translation. Note that most `Control<class_Control>`{.interpreted-text
role="ref"} nodes automatically translate their strings, so this method
is mostly useful for formatted strings or custom drawn text.

If
`can_translate_messages()<class_Object_method_can_translate_messages>`{.interpreted-text
role="ref"} is `false`, or no translation is available, this method
returns the `message` without changes. See
`set_message_translation()<class_Object_method_set_message_translation>`{.interpreted-text
role="ref"}.

For detailed examples, see
`Internationalizing games <../tutorials/i18n/internationalizing_games>`{.interpreted-text
role="doc"}.

\*\*Note:\*\* This method can\'t be used without an **Object** instance,
as it requires the
`can_translate_messages()<class_Object_method_can_translate_messages>`{.interpreted-text
role="ref"} method. To translate strings in a static context, use
`TranslationServer.translate()<class_TranslationServer_method_translate>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Object_method_tr_n}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **tr_n**(message:
`StringName<class_StringName>`{.interpreted-text role="ref"},
plural_message: `StringName<class_StringName>`{.interpreted-text
role="ref"}, n: `int<class_int>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Object_method_tr_n>`{.interpreted-text
role="ref"}

Translates a `message` or `plural_message`, using the translation
catalogs configured in the Project Settings. Further `context` can be
specified to help with the translation.

If
`can_translate_messages()<class_Object_method_can_translate_messages>`{.interpreted-text
role="ref"} is `false`, or no translation is available, this method
returns `message` or `plural_message`, without changes. See
`set_message_translation()<class_Object_method_set_message_translation>`{.interpreted-text
role="ref"}.

The `n` is the number, or amount, of the message\'s subject. It is used
by the translation system to fetch the correct plural form for the
current language.

For detailed examples, see
`Localization using gettext <../tutorials/i18n/localization_using_gettext>`{.interpreted-text
role="doc"}.

\*\*Note:\*\* Negative and `float<class_float>`{.interpreted-text
role="ref"} numbers may not properly apply to some countable subjects.
It\'s recommended to handle these cases with
`tr()<class_Object_method_tr>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This method can\'t be used without an **Object** instance,
as it requires the
`can_translate_messages()<class_Object_method_can_translate_messages>`{.interpreted-text
role="ref"} method. To translate strings in a static context, use
`TranslationServer.translate_plural()<class_TranslationServer_method_translate_plural>`{.interpreted-text
role="ref"}.
