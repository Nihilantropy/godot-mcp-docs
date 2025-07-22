github_url
:   hide

# bool {#class_bool}

A built-in boolean type.

::: rst-class
classref-introduction-group
:::

## Description

The **bool** is a built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type that may only store one of two values: `true` or
`false`. You can imagine it as a switch that can be either turned on or
off, or as a binary digit that can either be 1 or 0.

Booleans can be directly used in `if`, and other conditional statements:

::::: tabs
::: code-tab
gdscript

var can_shoot = true if can_shoot: launch_bullet()
:::

::: code-tab
csharp

bool canShoot = true; if (canShoot) { LaunchBullet(); }
:::
:::::

All comparison operators return booleans (`==`, `>`, `<=`, etc.). As
such, it is not necessary to compare booleans themselves. You do not
need to add `== true` or `== false`.

Booleans can be combined with the logical operators `and`, `or`, `not`
to create complex conditions:

::::: tabs
::: code-tab
gdscript

if bullets \> 0 and not is_reloading():

:   launch_bullet()

if bullets == 0 or is_reloading():

:   play_clack_sound()
:::

::: code-tab
csharp

if (bullets \> 0 && !IsReloading()) { LaunchBullet(); }

if (bullets == 0 \|\| IsReloading()) { PlayClackSound(); }
:::
:::::

\*\*Note:\*\* In modern programming languages, logical operators are
evaluated in order. All remaining conditions are skipped if their result
would have no effect on the final value. This concept is known as
[short-circuit
evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation) and
can be useful to avoid evaluating expensive conditions in some
performance-critical cases.

\*\*Note:\*\* By convention, built-in methods and properties that return
booleans are usually defined as yes-no questions, single adjectives, or
similar
(`String.is_empty()<class_String_method_is_empty>`{.interpreted-text
role="ref"},
`Node.can_process()<class_Node_method_can_process>`{.interpreted-text
role="ref"},
`Camera2D.enabled<class_Camera2D_property_enabled>`{.interpreted-text
role="ref"}, etc.).

::: rst-class
classref-reftable-group
:::

## Constructors

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

:::: {#class_bool_constructor_bool}
::: rst-class
classref-constructor
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **bool**()
`🔗<class_bool_constructor_bool>`{.interpreted-text role="ref"}

Constructs a **bool** set to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`bool<class_bool>`{.interpreted-text role="ref"} **bool**(from:
`bool<class_bool>`{.interpreted-text role="ref"})

Constructs a **bool** as a copy of the given **bool**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`bool<class_bool>`{.interpreted-text role="ref"} **bool**(from:
`float<class_float>`{.interpreted-text role="ref"})

Cast a `float<class_float>`{.interpreted-text role="ref"} value to a
boolean value. Returns `false` if `from` is equal to `0.0` (including
`-0.0`), and `true` for all other values (including
`@GDScript.INF<class_@GDScript_constant_INF>`{.interpreted-text
role="ref"} and
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`bool<class_bool>`{.interpreted-text role="ref"} **bool**(from:
`int<class_int>`{.interpreted-text role="ref"})

Cast an `int<class_int>`{.interpreted-text role="ref"} value to a
boolean value. Returns `false` if `from` is equal to `0`, and `true` for
all other values.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_bool_operator_neq_bool}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_bool_operator_neq_bool>`{.interpreted-text role="ref"}

Returns `true` if the two booleans are not equal. That is, one is `true`
and the other is `false`. This operation can be seen as a logical XOR.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_bool_operator_lt_bool}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \<**(right:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_bool_operator_lt_bool>`{.interpreted-text role="ref"}

Returns `true` if the left operand is `false` and the right operand is
`true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_bool_operator_eq_bool}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_bool_operator_eq_bool>`{.interpreted-text role="ref"}

Returns `true` if the two booleans are equal. That is, both are `true`
or both are `false`. This operation can be seen as a logical EQ or XNOR.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_bool_operator_gt_bool}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator \>**(right:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_bool_operator_gt_bool>`{.interpreted-text role="ref"}

Returns `true` if the left operand is `true` and the right operand is
`false`.
