github_url
:   hide

# JavaObject {#class_JavaObject}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents an object from the Java Native Interface.

::: rst-class
classref-introduction-group
:::

## Description

Represents an object from the Java Native Interface. It can be returned
from Java methods called on
`JavaClass<class_JavaClass>`{.interpreted-text role="ref"} or other
**JavaObject**s. See
`JavaClassWrapper<class_JavaClassWrapper>`{.interpreted-text role="ref"}
for an example.

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

:::: {#class_JavaObject_method_get_java_class}
::: rst-class
classref-method
:::
::::

`JavaClass<class_JavaClass>`{.interpreted-text role="ref"}
**get_java_class**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_JavaObject_method_get_java_class>`{.interpreted-text
role="ref"}

Returns the `JavaClass<class_JavaClass>`{.interpreted-text role="ref"}
that this object is an instance of.
