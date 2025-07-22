github_url
:   hide

# WeakRef {#class_WeakRef}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Holds an `Object<class_Object>`{.interpreted-text role="ref"}. If the
object is `RefCounted<class_RefCounted>`{.interpreted-text role="ref"},
it doesn\'t update the reference count.

::: rst-class
classref-introduction-group
:::

## Description

A weakref can hold a `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} without contributing to the reference counter. A weakref can
be created from an `Object<class_Object>`{.interpreted-text role="ref"}
using
`@GlobalScope.weakref()<class_@GlobalScope_method_weakref>`{.interpreted-text
role="ref"}. If this object is not a reference, weakref still works,
however, it does not have any effect on the object. Weakrefs are useful
in cases where multiple classes have variables that refer to each other.
Without weakrefs, using these classes could lead to memory leaks, since
both references keep each other from being released. Making part of the
variables a weakref can prevent this cyclic dependency, and allows the
references to be released.

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

:::: {#class_WeakRef_method_get_ref}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **get_ref**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_WeakRef_method_get_ref>`{.interpreted-text
role="ref"}

Returns the `Object<class_Object>`{.interpreted-text role="ref"} this
weakref is referring to. Returns `null` if that object no longer exists.
