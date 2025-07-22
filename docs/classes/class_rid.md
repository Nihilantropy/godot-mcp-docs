github_url
:   hide

# RID {#class_RID}

A handle for a `Resource<class_Resource>`{.interpreted-text
role="ref"}\'s unique identifier.

::: rst-class
classref-introduction-group
:::

## Description

The RID `Variant<class_Variant>`{.interpreted-text role="ref"} type is
used to access a low-level resource by its unique ID. RIDs are opaque,
which means they do not grant access to the resource by themselves. They
are used by the low-level server classes, such as
`DisplayServer<class_DisplayServer>`{.interpreted-text role="ref"},
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"},
`TextServer<class_TextServer>`{.interpreted-text role="ref"}, etc.

A low-level resource may correspond to a high-level
`Resource<class_Resource>`{.interpreted-text role="ref"}, such as
`Texture<class_Texture>`{.interpreted-text role="ref"} or
`Mesh<class_Mesh>`{.interpreted-text role="ref"}.

\*\*Note:\*\* RIDs are only useful during the current session. It won\'t
correspond to a similar resource if sent over a network, or loaded from
a file at a later time.

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

:::: {#class_RID_constructor_RID}
::: rst-class
classref-constructor
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **RID**()
`🔗<class_RID_constructor_RID>`{.interpreted-text role="ref"}

Constructs an empty **RID** with the invalid ID `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`RID<class_RID>`{.interpreted-text role="ref"} **RID**(from:
`RID<class_RID>`{.interpreted-text role="ref"})

Constructs an **RID** as a copy of the given **RID**.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RID_method_get_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RID_method_get_id>`{.interpreted-text role="ref"}

Returns the ID of the referenced low-level resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RID_method_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_valid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RID_method_is_valid>`{.interpreted-text
role="ref"}

Returns `true` if the **RID** is not `0`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_RID_operator_neq_RID}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RID_operator_neq_RID>`{.interpreted-text role="ref"}

Returns `true` if the **RID**s are not equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RID_operator_lt_RID}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RID_operator_lt_RID>`{.interpreted-text role="ref"}

Returns `true` if the **RID**\'s ID is less than `right`\'s ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RID_operator_lte_RID}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<=**(right:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RID_operator_lte_RID>`{.interpreted-text role="ref"}

Returns `true` if the **RID**\'s ID is less than or equal to `right`\'s
ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RID_operator_eq_RID}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RID_operator_eq_RID>`{.interpreted-text role="ref"}

Returns `true` if both **RID**s are equal, which means they both refer
to the same low-level resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RID_operator_gt_RID}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RID_operator_gt_RID>`{.interpreted-text role="ref"}

Returns `true` if the **RID**\'s ID is greater than `right`\'s ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RID_operator_gte_RID}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>=**(right:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_RID_operator_gte_RID>`{.interpreted-text role="ref"}

Returns `true` if the **RID**\'s ID is greater than or equal to
`right`\'s ID.
