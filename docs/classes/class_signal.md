github_url
:   hide

# Signal {#class_Signal}

A built-in type representing a signal of an
`Object<class_Object>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**Signal** is a built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type that represents a signal of an
`Object<class_Object>`{.interpreted-text role="ref"} instance. Like all
`Variant<class_Variant>`{.interpreted-text role="ref"} types, it can be
stored in variables and passed to functions. Signals allow all connected
`Callable<class_Callable>`{.interpreted-text role="ref"}s (and by
extension their respective objects) to listen and react to events,
without directly referencing one another. This keeps the code flexible
and easier to manage. You can check whether an
`Object<class_Object>`{.interpreted-text role="ref"} has a given signal
name using
`Object.has_signal()<class_Object_method_has_signal>`{.interpreted-text
role="ref"}.

In GDScript, signals can be declared with the `signal` keyword. In C#,
you may use the `[Signal]` attribute on a delegate.

::::: tabs
::: code-tab
gdscript

signal attacked

\# Additional arguments may be declared. \# These arguments must be
passed when the signal is emitted. signal item_dropped(item_name,
amount)
:::

::: code-tab
csharp

\[Signal\] delegate void AttackedEventHandler();

// Additional arguments may be declared. // These arguments must be
passed when the signal is emitted. \[Signal\] delegate void
ItemDroppedEventHandler(string itemName, int amount);
:::
:::::

Connecting signals is one of the most common operations in Godot and the
API gives many options to do so, which are described further down. The
code block below shows the recommended approach.

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   var button = Button.new() \# [button_down]{.title-ref} here is a
    Signal Variant type. We therefore call the Signal.connect() method,
    not Object.connect(). \# See discussion below for a more in-depth
    overview of the API.
    button.button_down.connect([on_button_down]{#on_button_down})

    \# This assumes that a [Player]{.title-ref} class exists, which
    defines a [hit]{.title-ref} signal. var player = Player.new() \# We
    use Signal.connect() again, and we also use the Callable.bind()
    method, \# which returns a new Callable with the parameter binds.
    player.hit.connect([on_player_hit.bind]{#on_player_hit.bind}(\"sword\",
    100))

func [on_button_down]{#on_button_down}():

:   print(\"Button down!\")

func [on_player_hit]{#on_player_hit}(weapon_type, damage):

:   print(\"Hit with weapon %s for %d damage.\" % \[weapon_type,
    damage\])
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { var button = new Button(); //
C# supports passing signals as events, so we can use this idiomatic
construct: button.ButtonDown += OnButtonDown;

> // This assumes that a [Player]{.title-ref} class exists, which
> defines a [Hit]{.title-ref} signal. var player = new Player(); // We
> can use lambdas when we need to bind additional parameters. player.Hit
> += () =\> OnPlayerHit(\"sword\", 100);

}

private void OnButtonDown() { GD.Print(\"Button down!\"); }

private void OnPlayerHit(string weaponType, int damage) {
GD.Print(\$\"Hit with weapon {weaponType} for {damage} damage.\"); }
:::
:::::

\*\*`Object.connect()` or `Signal.connect()`?\*\*

As seen above, the recommended method to connect signals is not
`Object.connect()<class_Object_method_connect>`{.interpreted-text
role="ref"}. The code block below shows the four options for connecting
signals, using either this legacy method or the recommended
`connect()<class_Signal_method_connect>`{.interpreted-text role="ref"},
and using either an implicit
`Callable<class_Callable>`{.interpreted-text role="ref"} or a manually
defined one.

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   var button = Button.new() \# Option 1: Object.connect() with an
    implicit Callable for the defined function.
    button.connect(\"button_down\", [on_button_down]{#on_button_down})
    \# Option 2: Object.connect() with a constructed Callable using a
    target object and method name. button.connect(\"button_down\",
    Callable(self, \"\_on_button_down\")) \# Option 3: Signal.connect()
    with an implicit Callable for the defined function.
    button.button_down.connect([on_button_down]{#on_button_down}) \#
    Option 4: Signal.connect() with a constructed Callable using a
    target object and method name.
    button.button_down.connect(Callable(self, \"\_on_button_down\"))

func [on_button_down]{#on_button_down}():

:   print(\"Button down!\")
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { var button = new Button(); //
Option 1: In C#, we can use signals as events and connect with this
idiomatic syntax: button.ButtonDown += OnButtonDown; // Option 2:
GodotObject.Connect() with a constructed Callable from a method group.
button.Connect(Button.SignalName.ButtonDown,
Callable.From(OnButtonDown)); // Option 3: GodotObject.Connect() with a
constructed Callable using a target object and method name.
button.Connect(Button.SignalName.ButtonDown, new Callable(this,
MethodName.OnButtonDown)); }

private void OnButtonDown() { GD.Print(\"Button down!\"); }
:::
:::::

While all options have the same outcome (`button`\'s
`BaseButton.button_down<class_BaseButton_signal_button_down>`{.interpreted-text
role="ref"} signal will be connected to `_on_button_down`), **option 3**
offers the best validation: it will print a compile-time error if either
the `button_down` **Signal** or the `_on_button_down`
`Callable<class_Callable>`{.interpreted-text role="ref"} are not
defined. On the other hand, **option 2** only relies on string names and
will only be able to validate either names at runtime: it will generate
an error at runtime if `"button_down"` is not a signal, or if
`"_on_button_down"` is not a method in the object `self`. The main
reason for using options 1, 2, or 4 would be if you actually need to use
strings (e.g. to connect signals programmatically based on strings read
from a configuration file). Otherwise, option 3 is the recommended (and
fastest) method.

\*\*Binding and passing parameters:\*\*

The syntax to bind parameters is through
`Callable.bind()<class_Callable_method_bind>`{.interpreted-text
role="ref"}, which returns a copy of the
`Callable<class_Callable>`{.interpreted-text role="ref"} with its
parameters bound.

When calling `emit()<class_Signal_method_emit>`{.interpreted-text
role="ref"} or
`Object.emit_signal()<class_Object_method_emit_signal>`{.interpreted-text
role="ref"}, the signal parameters can be also passed. The examples
below show the relationship between these signal parameters and bound
parameters.

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   \# This assumes that a [Player]{.title-ref} class exists, which
    defines a [hit]{.title-ref} signal. var player = Player.new() \#
    Using Callable.bind().
    player.hit.connect([on_player_hit.bind]{#on_player_hit.bind}(\"sword\",
    100))

    \# Parameters added when emitting the signal are passed first.
    player.hit.emit(\"Dark lord\", 5)

\# We pass two arguments when emitting ([hit_by]{.title-ref},
[level]{.title-ref}), \# and bind two more arguments when connecting
([weapon_type]{.title-ref}, [damage]{.title-ref}). func
[on_player_hit]{#on_player_hit}(hit_by, level, weapon_type, damage):
print(\"Hit by %s (level %d) with weapon %s for %d damage.\" % \[hit_by,
level, weapon_type, damage\])
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { // This assumes that a
[Player]{.title-ref} class exists, which defines a [Hit]{.title-ref}
signal. var player = new Player(); // Using lambda expressions that
create a closure that captures the additional parameters. // The lambda
only receives the parameters defined by the signal\'s delegate.
player.Hit += (hitBy, level) =\> OnPlayerHit(hitBy, level, \"sword\",
100);

> // Parameters added when emitting the signal are passed first.
> player.EmitSignal(SignalName.Hit, \"Dark lord\", 5);

}

// We pass two arguments when emitting ([hit_by]{.title-ref},
[level]{.title-ref}), // and bind two more arguments when connecting
([weapon_type]{.title-ref}, [damage]{.title-ref}). private void
OnPlayerHit(string hitBy, int level, string weaponType, int damage) {
GD.Print(\$\"Hit by {hitBy} (level {level}) with weapon {weaponType} for
{damage} damage.\"); }
:::
:::::

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Signals <../getting_started/step_by_step/signals>`{.interpreted-text
  role="doc"}
- [GDScript
  Basics](../tutorials/scripting/gdscript/gdscript_basics.html#signals)

::: rst-class
classref-reftable-group
:::

## Constructors

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Operators

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Signal_constructor_Signal}
::: rst-class
classref-constructor
:::
::::

`Signal<class_Signal>`{.interpreted-text role="ref"} **Signal**()
`🔗<class_Signal_constructor_Signal>`{.interpreted-text role="ref"}

Constructs an empty **Signal** with no object nor signal name bound.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Signal<class_Signal>`{.interpreted-text role="ref"} **Signal**(from:
`Signal<class_Signal>`{.interpreted-text role="ref"})

Constructs a **Signal** as a copy of the given **Signal**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Signal<class_Signal>`{.interpreted-text role="ref"} **Signal**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, signal:
`StringName<class_StringName>`{.interpreted-text role="ref"})

Creates a **Signal** object referencing a signal named `signal` in the
specified `object`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Signal_method_connect}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **connect**(callable:
`Callable<class_Callable>`{.interpreted-text role="ref"}, flags:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_Signal_method_connect>`{.interpreted-text role="ref"}

Connects this signal to the specified `callable`. Optional `flags` can
be also added to configure the connection\'s behavior (see
`ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text role="ref"}
constants). You can provide additional arguments to the connected
`callable` by using
`Callable.bind()<class_Callable_method_bind>`{.interpreted-text
role="ref"}.

A signal can only be connected once to the same
`Callable<class_Callable>`{.interpreted-text role="ref"}. If the signal
is already connected, this method returns
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} and generates an error, unless the signal is connected with
`Object.CONNECT_REFERENCE_COUNTED<class_Object_constant_CONNECT_REFERENCE_COUNTED>`{.interpreted-text
role="ref"}. To prevent this, use
`is_connected()<class_Signal_method_is_connected>`{.interpreted-text
role="ref"} first to check for existing connections.

    for button in $Buttons.get_children():
        button.pressed.connect(_on_pressed.bind(button))

    func _on_pressed(button):
        print(button.name, " was pressed")

\*\*Note:\*\* If the `callable`\'s object is freed, the connection will
be lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_disconnect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**disconnect**(callable: `Callable<class_Callable>`{.interpreted-text
role="ref"}) `🔗<class_Signal_method_disconnect>`{.interpreted-text
role="ref"}

Disconnects this signal from the specified
`Callable<class_Callable>`{.interpreted-text role="ref"}. If the
connection does not exist, generates an error. Use
`is_connected()<class_Signal_method_is_connected>`{.interpreted-text
role="ref"} to make sure that the connection exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_emit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **emit**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_emit>`{.interpreted-text
role="ref"}

Emits this signal. All `Callable<class_Callable>`{.interpreted-text
role="ref"}s connected to this signal will be triggered. This method
supports a variable number of arguments, so parameters can be passed as
a comma separated list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_get_connections}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_connections**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_get_connections>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
connections for this signal. Each connection is represented as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} that
contains three entries:

- `signal` is a reference to this signal;
- `callable` is a reference to the connected
  `Callable<class_Callable>`{.interpreted-text role="ref"};
- `flags` is a combination of
  `ConnectFlags<enum_Object_ConnectFlags>`{.interpreted-text
  role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_get_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_get_name>`{.interpreted-text
role="ref"}

Returns the name of this signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_get_object}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"} **get_object**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_get_object>`{.interpreted-text
role="ref"}

Returns the object emitting this signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_get_object_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_object_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_get_object_id>`{.interpreted-text
role="ref"}

Returns the ID of the object emitting this signal (see
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_has_connections}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_connections**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_has_connections>`{.interpreted-text
role="ref"}

Returns `true` if any `Callable<class_Callable>`{.interpreted-text
role="ref"} is connected to this signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_is_connected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_connected**(callable: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_is_connected>`{.interpreted-text
role="ref"}

Returns `true` if the specified
`Callable<class_Callable>`{.interpreted-text role="ref"} is connected to
this signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_method_is_null}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_null**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Signal_method_is_null>`{.interpreted-text
role="ref"}

Returns `true` if this **Signal** has no object and the signal name is
empty. Equivalent to `signal == Signal()`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Signal_operator_neq_Signal}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Signal<class_Signal>`{.interpreted-text role="ref"})
`🔗<class_Signal_operator_neq_Signal>`{.interpreted-text role="ref"}

Returns `true` if the signals do not share the same object and name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Signal_operator_eq_Signal}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Signal<class_Signal>`{.interpreted-text role="ref"})
`🔗<class_Signal_operator_eq_Signal>`{.interpreted-text role="ref"}

Returns `true` if both signals share the same object and name.
