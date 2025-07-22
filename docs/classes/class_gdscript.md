github_url
:   hide

# GDScript {#class_GDScript}

**Inherits:** `Script<class_Script>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A script implemented in the GDScript programming language.

::: rst-class
classref-introduction-group
:::

## Description

A script implemented in the GDScript programming language, saved with
the `.gd` extension. The script extends the functionality of all objects
that instantiate it.

Calling `new()<class_GDScript_method_new>`{.interpreted-text role="ref"}
creates a new instance of the script.
`Object.set_script()<class_Object_method_set_script>`{.interpreted-text
role="ref"} extends an existing object, if that object\'s class matches
one of the script\'s base classes.

If you are looking for GDScript\'s built-in functions, see
`@GDScript<class_@GDScript>`{.interpreted-text role="ref"} instead.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `GDScript documentation index <../tutorials/scripting/gdscript/index>`{.interpreted-text
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

## Method Descriptions

:::: {#class_GDScript_method_new}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **new**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_GDScript_method_new>`{.interpreted-text
role="ref"}

Returns a new instance of the script.

    var MyClass = load("myclass.gd")
    var instance = MyClass.new()
    print(instance.get_script() == MyClass) # Prints true
