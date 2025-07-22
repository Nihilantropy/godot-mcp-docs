github_url
:   hide

# JavaClass {#class_JavaClass}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a class from the Java Native Interface.

::: rst-class
classref-introduction-group
:::

## Description

Represents a class from the Java Native Interface. It is returned from
`JavaClassWrapper.wrap()<class_JavaClassWrapper_method_wrap>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This class only works on Android. On any other platform,
this class does nothing.

\*\*Note:\*\* This class is not to be confused with
`JavaScriptObject<class_JavaScriptObject>`{.interpreted-text
role="ref"}.

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

:::: {#class_JavaClass_method_get_java_class_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_java_class_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_JavaClass_method_get_java_class_name>`{.interpreted-text
role="ref"}

Returns the Java class name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaClass_method_get_java_method_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_java_method_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_JavaClass_method_get_java_method_list>`{.interpreted-text
role="ref"}

Returns the object\'s Java methods and their signatures as an
`Array<class_Array>`{.interpreted-text role="ref"} of dictionaries, in
the same format as
`Object.get_method_list()<class_Object_method_get_method_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaClass_method_get_java_parent_class}
::: rst-class
classref-method
:::
::::

`JavaClass<class_JavaClass>`{.interpreted-text role="ref"}
**get_java_parent_class**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_JavaClass_method_get_java_parent_class>`{.interpreted-text
role="ref"}

Returns a **JavaClass** representing the Java parent class of this
class.
