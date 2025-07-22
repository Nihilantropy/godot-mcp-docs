# Object class {#doc_object_class}

::: seealso
This page describes the C++ implementation of objects in Godot. Looking
for the Object class reference?
`Have a look here. <class_Object>`{.interpreted-text role="ref"}
:::

## General definition

`Object <class_object>`{.interpreted-text role="ref"} is the base class
for almost everything. Most classes in Godot inherit directly or
indirectly from it. Objects provide reflection and editable properties,
and declaring them is a matter of using a single macro like this:

``` cpp
class CustomObject : public Object {

    GDCLASS(CustomObject, Object); // this is required to inherit
};
```

This adds a lot of functionality to Objects. For example:

``` cpp
obj = memnew(CustomObject);
print_line("Object class: ", obj->get_class()); // print object class

obj2 = Object::cast_to<OtherClass>(obj); // converting between classes, this also works without RTTI enabled.
```

### References:

- [core/object/object.h](https://github.com/godotengine/godot/blob/master/core/object/object.h)

## Registering an Object

ClassDB is a static class that holds the entire list of registered
classes that inherit from Object, as well as dynamic bindings to all
their methods properties and integer constants.

Classes are registered by calling:

``` cpp
ClassDB::register_class<MyCustomClass>()
```

Registering it will allow the class to be instanced by scripts, code, or
creating them again when deserializing.

Registering as virtual is the same but it can\'t be instanced.

``` cpp
ClassDB::register_virtual_class<MyCustomClass>()
```

Object-derived classes can override the static function
`static void _bind_methods()`. When one class is registered, this static
function is called to register all the object methods, properties,
constants, etc. It\'s only called once. If an Object derived class is
instanced but has not been registered, it will be registered as virtual
automatically.

Inside `_bind_methods`, there are a couple of things that can be done.
Registering functions is one:

``` cpp
ClassDB::bind_method(D_METHOD("methodname", "arg1name", "arg2name", "arg3name"), &MyCustomType::method);
```

Default values for arguments can be passed as parameters at the end:

``` cpp
ClassDB::bind_method(D_METHOD("methodname", "arg1name", "arg2name", "arg3name"), &MyCustomType::method, DEFVAL(-1), DEFVAL(-2)); // Default values for arg2name (-1) and arg3name (-2).
```

Default values must be provided in the same order as they are declared,
skipping required arguments and then providing default values for the
optional ones. This matches the syntax for declaring methods in C++.

`D_METHOD` is a macro that converts \"methodname\" to a StringName for
more efficiency. Argument names are used for introspection, but when
compiling on release, the macro ignores them, so the strings are unused
and optimized away.

Check `_bind_methods` of Control or Object for more examples.

If just adding modules and functionality that is not expected to be
documented as thoroughly, the `D_METHOD()` macro can safely be ignored
and a string passing the name can be passed for brevity.

### References:

- [core/object/class_db.h](https://github.com/godotengine/godot/blob/master/core/object/class_db.h)

## Constants

Classes often have enums such as:

``` cpp
enum SomeMode {
   MODE_FIRST,
   MODE_SECOND
};
```

For these to work when binding to methods, the enum must be declared
convertible to int. A macro is provided to help with this:

``` cpp
VARIANT_ENUM_CAST(MyClass::SomeMode); // now functions that take SomeMode can be bound.
```

The constants can also be bound inside `_bind_methods`, by using:

``` cpp
BIND_CONSTANT(MODE_FIRST);
BIND_CONSTANT(MODE_SECOND);
```

## Properties (set/get)

Objects export properties, properties are useful for the following:

- Serializing and deserializing the object.
- Creating a list of editable values for the Object derived class.

Properties are usually defined by the PropertyInfo() class and
constructed as:

``` cpp
PropertyInfo(type, name, hint, hint_string, usage_flags)
```

For example:

``` cpp
PropertyInfo(Variant::INT, "amount", PROPERTY_HINT_RANGE, "0,49,1", PROPERTY_USAGE_EDITOR)
```

This is an integer property named \"amount\". The hint is a range, and
the range goes from 0 to 49 in steps of 1 (integers). It is only usable
for the editor (editing the value visually) but won\'t be serialized.

Another example:

``` cpp
PropertyInfo(Variant::STRING, "modes", PROPERTY_HINT_ENUM, "Enabled,Disabled,Turbo")
```

This is a string property, can take any string but the editor will only
allow the defined hint ones. Since no usage flags were specified, the
default ones are PROPERTY_USAGE_STORAGE and PROPERTY_USAGE_EDITOR.

There are plenty of hints and usage flags available in object.h, give
them a check.

Properties can also work like C# properties and be accessed from script
using indexing, but this usage is generally discouraged, as using
functions is preferred for legibility. Many properties are also bound
with categories, such as \"animation/frame\" which also make indexing
impossible unless using operator \[\].

From `_bind_methods()`, properties can be created and bound as long as
set/get functions exist. Example:

``` cpp
ADD_PROPERTY(PropertyInfo(Variant::INT, "amount"), "set_amount", "get_amount")
```

This creates the property using the setter and the getter.

## Binding properties using `_set`/`_get`/`_get_property_list` {#doc_binding_properties_using_set_get_property_list}

An additional method of creating properties exists when more flexibility
is desired (i.e. adding or removing properties on context).

The following functions can be overridden in an Object derived class,
they are NOT virtual, DO NOT make them virtual, they are called for
every override and the previous ones are not invalidated (multilevel
call).

``` cpp
protected:
     void _get_property_list(List<PropertyInfo> *r_props) const;      // return list of properties
     bool _get(const StringName &p_property, Variant &r_value) const; // return true if property was found
     bool _set(const StringName &p_property, const Variant &p_value); // return true if property was found
```

This is also a little less efficient since `p_property` must be compared
against the desired names in serial order.

## Dynamic casting

Godot provides dynamic casting between Object-derived classes, for
example:

``` cpp
void somefunc(Object *some_obj) {

     Button *button = Object::cast_to<Button>(some_obj);
}
```

If cast fails, NULL is returned. This system uses RTTI, but it also
works fine (although a bit slower) when RTTI is disabled. This is useful
on platforms where a small binary size is ideal, such as HTML5 or
consoles (with low memory footprint).

## Signals

Objects can have a set of signals defined (similar to Delegates in other
languages). This example shows how to connect to them:

``` cpp
obj->connect(<signal>, target_instance, target_method)
// for example:
obj->connect("enter_tree", this, "_node_entered_tree")
```

The method `_node_entered_tree` must be registered to the class using
`ClassDB::bind_method` (explained before).

Adding signals to a class is done in `_bind_methods`, using the
`ADD_SIGNAL` macro, for example:

``` cpp
ADD_SIGNAL(MethodInfo("been_killed"))
```

## Notifications

All objects in Godot have a
`_notification <class_Object_private_method__notification>`{.interpreted-text
role="ref"} method that allows it to respond to engine level callbacks
that may relate to it. More information can be found on the
`doc_godot_notifications`{.interpreted-text role="ref"} page.

## References

`RefCounted <class_RefCounted>`{.interpreted-text role="ref"} inherits
from Object and holds a reference count. It is the base for reference
counted object types. Declaring them must be done using Ref\<\>
template. For example:

``` cpp
class MyReference: public RefCounted {
    GDCLASS(MyReference, RefCounted);
};

Ref<MyReference> myref(memnew(MyReference));
```

`myref` is reference counted. It will be freed when no more Ref\<\>
templates point to it.

### References:

- [core/object/reference.h](https://github.com/godotengine/godot/blob/master/core/object/ref_counted.h)

## Resources

`Resource <class_resource>`{.interpreted-text role="ref"} inherits from
RefCounted, so all resources are reference counted. Resources can
optionally contain a path, which reference a file on disk. This can be
set with `resource.set_path(path)`, though this is normally done by the
resource loader. No two different resources can have the same path;
attempting to do so will result in an error.

Resources without a path are fine too.

### References:

- [core/io/resource.h](https://github.com/godotengine/godot/blob/master/core/io/resource.h)

## Resource loading

Resources can be loaded with the ResourceLoader API, like this:

``` cpp
Ref<Resource> res = ResourceLoader::load("res://someresource.res")
```

If a reference to that resource has been loaded previously and is in
memory, the resource loader will return that reference. This means that
there can be only one resource loaded from a file referenced on disk at
the same time.

- resourceinteractiveloader (TODO)

### References:

- [core/io/resource_loader.h](https://github.com/godotengine/godot/blob/master/core/io/resource_loader.h)

## Resource saving

Saving a resource can be done with the resource saver API:

``` cpp
ResourceSaver::save("res://someresource.res", instance)
```

The instance will be saved, and sub resources that have a path to a file
will be saved as a reference to that resource. Sub resources without a
path will be bundled with the saved resource and assigned sub-IDs, like
`res://someresource.res::1`. This also helps to cache them when loaded.

### References:

- [core/io/resource_saver.h](https://github.com/godotengine/godot/blob/master/core/io/resource_saver.h)
