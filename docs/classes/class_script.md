github_url
:   hide

# Script {#class_Script}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `CSharpScript<class_CSharpScript>`{.interpreted-text
role="ref"}, `GDScript<class_GDScript>`{.interpreted-text role="ref"},
`ScriptExtension<class_ScriptExtension>`{.interpreted-text role="ref"}

A class stored as a resource.

::: rst-class
classref-introduction-group
:::

## Description

A class stored as a resource. A script extends the functionality of all
objects that instantiate it.

This is the base class for all scripts and should not be used directly.
Trying to create a new script with this class will result in an error.

The `new` method of a script subclass creates a new instance.
`Object.set_script()<class_Object_method_set_script>`{.interpreted-text
role="ref"} extends an existing object, if that object\'s class matches
one of the script\'s base classes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Scripting documentation index <../tutorials/scripting/index>`{.interpreted-text
  role="doc"}

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

## Property Descriptions

:::: {#class_Script_property_source_code}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **source_code**
`🔗<class_Script_property_source_code>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_source_code**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_source_code**()

The script source code or an empty string if source code is not
available. When set, does not reload the class implementation
automatically.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Script_method_can_instantiate}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_instantiate**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Script_method_can_instantiate>`{.interpreted-text
role="ref"}

Returns `true` if the script can be instantiated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_get_base_script}
::: rst-class
classref-method
:::
::::

`Script<class_Script>`{.interpreted-text role="ref"}
**get_base_script**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Script_method_get_base_script>`{.interpreted-text
role="ref"}

Returns the script directly inherited by this script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_get_global_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_global_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Script_method_get_global_name>`{.interpreted-text
role="ref"}

Returns the class name associated with the script, if there is one.
Returns an empty string otherwise.

To give the script a global name, you can use the `class_name` keyword
in GDScript and the `[GlobalClass]` attribute in C#.

::::: tabs
::: code-tab
gdscript

class_name MyNode extends Node
:::

::: code-tab
csharp

using Godot;

\[GlobalClass\] public partial class MyNode : Node { }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_get_instance_base_type}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_instance_base_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Script_method_get_instance_base_type>`{.interpreted-text
role="ref"}

Returns the script\'s base type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_get_property_default_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_property_default_value**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Script_method_get_property_default_value>`{.interpreted-text
role="ref"}

Returns the default value of the specified property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_get_rpc_config}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_rpc_config**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Script_method_get_rpc_config>`{.interpreted-text
role="ref"}

Returns a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
mapping method names to their RPC configuration defined by this script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_get_script_constant_map}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_script_constant_map**()
`🔗<class_Script_method_get_script_constant_map>`{.interpreted-text
role="ref"}

Returns a dictionary containing constant names and their values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_get_script_method_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_script_method_list**()
`🔗<class_Script_method_get_script_method_list>`{.interpreted-text
role="ref"}

Returns the list of methods in this **Script**.

\*\*Note:\*\* The dictionaries returned by this method are formatted
identically to those returned by
`Object.get_method_list()<class_Object_method_get_method_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_get_script_property_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_script_property_list**()
`🔗<class_Script_method_get_script_property_list>`{.interpreted-text
role="ref"}

Returns the list of properties in this **Script**.

\*\*Note:\*\* The dictionaries returned by this method are formatted
identically to those returned by
`Object.get_property_list()<class_Object_method_get_property_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_get_script_signal_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_script_signal_list**()
`🔗<class_Script_method_get_script_signal_list>`{.interpreted-text
role="ref"}

Returns the list of user signals defined in this **Script**.

\*\*Note:\*\* The dictionaries returned by this method are formatted
identically to those returned by
`Object.get_signal_list()<class_Object_method_get_signal_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_has_script_signal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_script_signal**(signal_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Script_method_has_script_signal>`{.interpreted-text
role="ref"}

Returns `true` if the script, or a base class, defines a signal with the
given name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_has_source_code}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_source_code**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Script_method_has_source_code>`{.interpreted-text
role="ref"}

Returns `true` if the script contains non-empty source code.

\*\*Note:\*\* If a script does not have source code, this does not mean
that it is invalid or unusable. For example, a
`GDScript<class_GDScript>`{.interpreted-text role="ref"} that was
exported with binary tokenization has no source code, but still behaves
as expected and could be instantiated. This can be checked with
`can_instantiate()<class_Script_method_can_instantiate>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_instance_has}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**instance_has**(base_object: `Object<class_Object>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Script_method_instance_has>`{.interpreted-text
role="ref"}

Returns `true` if `base_object` is an instance of this script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_is_abstract}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_abstract**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Script_method_is_abstract>`{.interpreted-text
role="ref"}

Returns `true` if the script is an abstract script. An abstract script
does not have a constructor and cannot be instantiated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_is_tool}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_tool**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Script_method_is_tool>`{.interpreted-text
role="ref"}

Returns `true` if the script is a tool script. A tool script can run in
the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Script_method_reload}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**reload**(keep_state: `bool<class_bool>`{.interpreted-text role="ref"}
= false) `🔗<class_Script_method_reload>`{.interpreted-text role="ref"}

Reloads the script\'s class implementation. Returns an error code.
