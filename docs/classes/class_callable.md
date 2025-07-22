github_url
:   hide

# Callable {#class_Callable}

A built-in type representing a method or a standalone function.

::: rst-class
classref-introduction-group
:::

## Description

**Callable** is a built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type that represents a function. It can either be a method
within an `Object<class_Object>`{.interpreted-text role="ref"} instance,
or a custom callable used for different purposes (see
`is_custom()<class_Callable_method_is_custom>`{.interpreted-text
role="ref"}). Like all `Variant<class_Variant>`{.interpreted-text
role="ref"} types, it can be stored in variables and passed to other
functions. It is most commonly used for signal callbacks.

::::: tabs
::: code-tab
gdscript

func print_args(arg1, arg2, arg3 = \"\"):

:   prints(arg1, arg2, arg3)

func test():

:   var callable = Callable(self, \"print_args\")
    callable.call(\"hello\", \"world\") \# Prints \"hello world \".
    callable.call(Vector2.UP, 42, callable) \# Prints \"(0.0, -1.0) 42
    Node(node.gd)::print_args\" callable.call(\"invalid\") \# Invalid
    call, should have at least 2 arguments.
:::

::: code-tab
csharp

// Default parameter values are not supported. public void
PrintArgs(Variant arg1, Variant arg2, Variant arg3 = default) {
GD.PrintS(arg1, arg2, arg3); }

public void Test() { // Invalid calls fail silently. Callable callable =
new Callable(this, MethodName.PrintArgs); callable.Call(\"hello\",
\"world\"); // Default parameter values are not supported, should have 3
arguments. callable.Call(Vector2.Up, 42, callable); // Prints \"(0, -1)
42 Node(Node.cs)::PrintArgs\" callable.Call(\"invalid\"); // Invalid
call, should have 3 arguments. }
:::
:::::

In GDScript, it\'s possible to create lambda functions within a method.
Lambda functions are custom callables that are not associated with an
`Object<class_Object>`{.interpreted-text role="ref"} instance.
Optionally, lambda functions can also be named. The name will be
displayed in the debugger, or when calling
`get_method()<class_Callable_method_get_method>`{.interpreted-text
role="ref"}.

    func _init():
        var my_lambda = func (message):
            print(message)

        # Prints "Hello everyone!"
        my_lambda.call("Hello everyone!")

        # Prints "Attack!", when the button_pressed signal is emitted.
        button_pressed.connect(func(): print("Attack!"))

In GDScript, you can access methods and global functions as
**Callable**s:

    tween.tween_callback(node.queue_free)  # Object methods.
    tween.tween_callback(array.clear)  # Methods of built-in types.
    tween.tween_callback(print.bind("Test"))  # Global functions.

\*\*Note:\*\* `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} does not support the above due to ambiguity with keys.

    var dictionary = { "hello": "world" }

    # This will not work, `clear` is treated as a key.
    tween.tween_callback(dictionary.clear)

    # This will work.
    tween.tween_callback(Callable.create(dictionary, "clear"))

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

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

:::: {#class_Callable_constructor_Callable}
::: rst-class
classref-constructor
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"} **Callable**()
`🔗<class_Callable_constructor_Callable>`{.interpreted-text role="ref"}

Constructs an empty **Callable**, with no object nor method bound.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**Callable**(from: `Callable<class_Callable>`{.interpreted-text
role="ref"})

Constructs a **Callable** as a copy of the given **Callable**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**Callable**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, method: `StringName<class_StringName>`{.interpreted-text
role="ref"})

Creates a new **Callable** for the method named `method` in the
specified `object`.

\*\*Note:\*\* For methods of built-in
`Variant<class_Variant>`{.interpreted-text role="ref"} types, use
`create()<class_Callable_method_create>`{.interpreted-text role="ref"}
instead.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Callable_method_bind}
::: rst-class
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"} **bind**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_bind>`{.interpreted-text
role="ref"}

Returns a copy of this **Callable** with one or more arguments bound.
When called, the bound arguments are passed *after* the arguments
supplied by `call()<class_Callable_method_call>`{.interpreted-text
role="ref"}. See also
`unbind()<class_Callable_method_unbind>`{.interpreted-text role="ref"}.

\*\*Note:\*\* When this method is chained with other similar methods,
the order in which the argument list is modified is read from right to
left.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_bindv}
::: rst-class
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**bindv**(arguments: `Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_Callable_method_bindv>`{.interpreted-text role="ref"}

Returns a copy of this **Callable** with one or more arguments bound,
reading them from an array. When called, the bound arguments are passed
*after* the arguments supplied by
`call()<class_Callable_method_call>`{.interpreted-text role="ref"}. See
also `unbind()<class_Callable_method_unbind>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When this method is chained with other similar methods,
the order in which the argument list is modified is read from right to
left.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_call}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **call**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_call>`{.interpreted-text
role="ref"}

Calls the method represented by this **Callable**. Arguments can be
passed and should match the method\'s signature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_call_deferred}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**call_deferred**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_call_deferred>`{.interpreted-text
role="ref"}

Calls the method represented by this **Callable** in deferred mode, i.e.
at the end of the current frame. Arguments can be passed and should
match the method\'s signature.

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   grab_focus.call_deferred()
:::

::: code-tab
csharp

public override void [Ready]{#ready}() {
Callable.From(GrabFocus).CallDeferred(); }
:::
:::::

\*\*Note:\*\* Deferred calls are processed at idle time. Idle time
happens mainly at the end of process and physics frames. In it, deferred
calls will be run until there are none left, which means you can defer
calls from other deferred calls and they\'ll still be run in the current
idle time cycle. This means you should not call a method deferred from
itself (or from a method called by it), as this causes infinite
recursion the same way as if you had called the method directly.

See also
`Object.call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_callv}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**callv**(arguments: `Array<class_Array>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_callv>`{.interpreted-text
role="ref"}

Calls the method represented by this **Callable**. Unlike
`call()<class_Callable_method_call>`{.interpreted-text role="ref"}, this
method expects all arguments to be contained inside the `arguments`
`Array<class_Array>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_create}
::: rst-class
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**create**(variant: `Variant<class_Variant>`{.interpreted-text
role="ref"}, method: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_create>`{.interpreted-text
role="ref"}

Creates a new **Callable** for the method named `method` in the
specified `variant`. To represent a method of a built-in
`Variant<class_Variant>`{.interpreted-text role="ref"} type, a custom
callable is used (see
`is_custom()<class_Callable_method_is_custom>`{.interpreted-text
role="ref"}). If `variant` is `Object<class_Object>`{.interpreted-text
role="ref"}, then a standard callable will be created instead.

\*\*Note:\*\* This method is always necessary for the
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} type, as
property syntax is used to access its entries. You may also use this
method when `variant`\'s type is not known in advance (for
polymorphism).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_get_argument_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_argument_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Callable_method_get_argument_count>`{.interpreted-text
role="ref"}

Returns the total number of arguments this **Callable** should take,
including optional arguments. This means that any arguments bound with
`bind()<class_Callable_method_bind>`{.interpreted-text role="ref"} are
*subtracted* from the result, and any arguments unbound with
`unbind()<class_Callable_method_unbind>`{.interpreted-text role="ref"}
are *added* to the result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_get_bound_arguments}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_bound_arguments**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Callable_method_get_bound_arguments>`{.interpreted-text
role="ref"}

Returns the array of arguments bound via successive
`bind()<class_Callable_method_bind>`{.interpreted-text role="ref"} or
`unbind()<class_Callable_method_unbind>`{.interpreted-text role="ref"}
calls. These arguments will be added *after* the arguments passed to the
call, from which
`get_unbound_arguments_count()<class_Callable_method_get_unbound_arguments_count>`{.interpreted-text
role="ref"} arguments on the right have been previously excluded.

    func get_effective_arguments(callable, call_args):
        assert(call_args.size() - callable.get_unbound_arguments_count() >= 0)
        var result = call_args.slice(0, call_args.size() - callable.get_unbound_arguments_count())
        result.append_array(callable.get_bound_arguments())
        return result

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_get_bound_arguments_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_bound_arguments_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Callable_method_get_bound_arguments_count>`{.interpreted-text
role="ref"}

Returns the total amount of arguments bound via successive
`bind()<class_Callable_method_bind>`{.interpreted-text role="ref"} or
`unbind()<class_Callable_method_unbind>`{.interpreted-text role="ref"}
calls. This is the same as the size of the array returned by
`get_bound_arguments()<class_Callable_method_get_bound_arguments>`{.interpreted-text
role="ref"}. See
`get_bound_arguments()<class_Callable_method_get_bound_arguments>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* The
`get_bound_arguments_count()<class_Callable_method_get_bound_arguments_count>`{.interpreted-text
role="ref"} and
`get_unbound_arguments_count()<class_Callable_method_get_unbound_arguments_count>`{.interpreted-text
role="ref"} methods can both return positive values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_get_method}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_method**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_get_method>`{.interpreted-text
role="ref"}

Returns the name of the method represented by this **Callable**. If the
callable is a GDScript lambda function, returns the function\'s name or
`"<anonymous lambda>"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_get_object}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"} **get_object**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_get_object>`{.interpreted-text
role="ref"}

Returns the object on which this **Callable** is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_get_object_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_object_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_get_object_id>`{.interpreted-text
role="ref"}

Returns the ID of this **Callable**\'s object (see
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_get_unbound_arguments_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_unbound_arguments_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Callable_method_get_unbound_arguments_count>`{.interpreted-text
role="ref"}

Returns the total amount of arguments unbound via successive
`bind()<class_Callable_method_bind>`{.interpreted-text role="ref"} or
`unbind()<class_Callable_method_unbind>`{.interpreted-text role="ref"}
calls. See
`get_bound_arguments()<class_Callable_method_get_bound_arguments>`{.interpreted-text
role="ref"} for details.

\*\*Note:\*\* The
`get_bound_arguments_count()<class_Callable_method_get_bound_arguments_count>`{.interpreted-text
role="ref"} and
`get_unbound_arguments_count()<class_Callable_method_get_unbound_arguments_count>`{.interpreted-text
role="ref"} methods can both return positive values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_hash}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hash**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_hash>`{.interpreted-text
role="ref"}

Returns the 32-bit hash value of this **Callable**\'s object.

\*\*Note:\*\* **Callable**s with equal content will always produce
identical hash values. However, the reverse is not true. Returning
identical hash values does *not* imply the callables are equal, because
different callables can have identical hash values due to hash
collisions. The engine uses a 32-bit hash algorithm for
`hash()<class_Callable_method_hash>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_is_custom}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_custom**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_is_custom>`{.interpreted-text
role="ref"}

Returns `true` if this **Callable** is a custom callable. Custom
callables are used:

- for binding/unbinding arguments (see
  `bind()<class_Callable_method_bind>`{.interpreted-text role="ref"} and
  `unbind()<class_Callable_method_unbind>`{.interpreted-text
  role="ref"});
- for representing methods of built-in
  `Variant<class_Variant>`{.interpreted-text role="ref"} types (see
  `create()<class_Callable_method_create>`{.interpreted-text
  role="ref"});
- for representing global, lambda, and RPC functions in GDScript;
- for other purposes in the core, GDExtension, and C#.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_is_null}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_null**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_is_null>`{.interpreted-text
role="ref"}

Returns `true` if this **Callable** has no target to call the method on.
Equivalent to `callable == Callable()`.

\*\*Note:\*\* This is *not* the same as `not is_valid()` and using
`not is_null()` will *not* guarantee that this callable can be called.
Use `is_valid()<class_Callable_method_is_valid>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_is_standard}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_standard**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_is_standard>`{.interpreted-text
role="ref"}

Returns `true` if this **Callable** is a standard callable. This method
is the opposite of
`is_custom()<class_Callable_method_is_custom>`{.interpreted-text
role="ref"}. Returns `false` if this callable is a lambda function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_valid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_is_valid>`{.interpreted-text
role="ref"}

Returns `true` if the callable\'s object exists and has a valid method
name assigned, or is a custom callable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_rpc}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **rpc**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_rpc>`{.interpreted-text
role="ref"}

Perform an RPC (Remote Procedure Call) on all connected peers. This is
used for multiplayer and is normally not available, unless the function
being called has been marked as *RPC* (using
`@GDScript.@rpc<class_@GDScript_annotation_@rpc>`{.interpreted-text
role="ref"} or
`Node.rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"}). Calling this method on unsupported functions will result
in an error. See `Node.rpc()<class_Node_method_rpc>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_rpc_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rpc_id**(peer_id: `int<class_int>`{.interpreted-text role="ref"},
\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_rpc_id>`{.interpreted-text
role="ref"}

Perform an RPC (Remote Procedure Call) on a specific peer ID (see
multiplayer documentation for reference). This is used for multiplayer
and is normally not available unless the function being called has been
marked as *RPC* (using
`@GDScript.@rpc<class_@GDScript_annotation_@rpc>`{.interpreted-text
role="ref"} or
`Node.rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"}). Calling this method on unsupported functions will result
in an error. See
`Node.rpc_id()<class_Node_method_rpc_id>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_method_unbind}
::: rst-class
classref-method
:::
::::

`Callable<class_Callable>`{.interpreted-text role="ref"}
**unbind**(argcount: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Callable_method_unbind>`{.interpreted-text
role="ref"}

Returns a copy of this **Callable** with a number of arguments unbound.
In other words, when the new callable is called the last few arguments
supplied by the user are ignored, according to `argcount`. The remaining
arguments are passed to the callable. This allows to use the original
callable in a context that attempts to pass more arguments than this
callable can handle, e.g. a signal with a fixed number of arguments. See
also `bind()<class_Callable_method_bind>`{.interpreted-text role="ref"}.

\*\*Note:\*\* When this method is chained with other similar methods,
the order in which the argument list is modified is read from right to
left.

    func _ready():
        foo.unbind(1).call(1, 2) # Calls foo(1).
        foo.bind(3, 4).unbind(1).call(1, 2) # Calls foo(1, 3, 4), note that it does not change the arguments from bind.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Callable_operator_neq_Callable}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_Callable_operator_neq_Callable>`{.interpreted-text role="ref"}

Returns `true` if both **Callable**s invoke different targets.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Callable_operator_eq_Callable}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_Callable_operator_eq_Callable>`{.interpreted-text role="ref"}

Returns `true` if both **Callable**s invoke the same custom target.
