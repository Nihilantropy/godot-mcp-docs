github_url
:   hide

# Expression {#class_Expression}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A class that stores an expression you can execute.

::: rst-class
classref-introduction-group
:::

## Description

An expression can be made of any arithmetic operation, built-in math
function call, method call of a passed instance, or built-in type
construction call.

An example expression text using the built-in math functions could be
`sqrt(pow(3, 2) + pow(4, 2))`.

In the following example we use a
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} node to write
our expression and show the result.

::::: tabs
::: code-tab
gdscript

var expression = Expression.new()

func [ready]{#ready}():

:   \$LineEdit.text_submitted.connect(self.\_on_text_submitted)

func [on_text_submitted]{#on_text_submitted}(command):

:   var error = expression.parse(command) if error != OK:
    print(expression.get_error_text()) return var result =
    expression.execute() if not expression.has_execute_failed():
    \$LineEdit.text = str(result)
:::

::: code-tab
csharp

private Expression [expression]{#expression} = new Expression();

public override void [Ready]{#ready}() {
GetNode\<LineEdit\>(\"LineEdit\").TextSubmitted += OnTextEntered; }

private void OnTextEntered(string command) { Error error =
[expression.Parse]{#expression.parse}(command); if (error != Error.Ok) {
GD.Print([expression.GetErrorText]{#expression.geterrortext}()); return;
} Variant result = [expression.Execute]{#expression.execute}(); if
(!\_expression.HasExecuteFailed()) {
GetNode\<LineEdit\>(\"LineEdit\").Text = result.ToString(); } }
:::
:::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Evaluating Expressions <../tutorials/scripting/evaluating_expressions>`{.interpreted-text
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

:::: {#class_Expression_method_execute}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**execute**(inputs: `Array<class_Array>`{.interpreted-text role="ref"} =
\[\], base_instance: `Object<class_Object>`{.interpreted-text
role="ref"} = null, show_error: `bool<class_bool>`{.interpreted-text
role="ref"} = true, const_calls_only:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Expression_method_execute>`{.interpreted-text role="ref"}

Executes the expression that was previously parsed by
`parse()<class_Expression_method_parse>`{.interpreted-text role="ref"}
and returns the result. Before you use the returned object, you should
check if the method failed by calling
`has_execute_failed()<class_Expression_method_has_execute_failed>`{.interpreted-text
role="ref"}.

If you defined input variables in
`parse()<class_Expression_method_parse>`{.interpreted-text role="ref"},
you can specify their values in the inputs array, in the same order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Expression_method_get_error_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_error_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Expression_method_get_error_text>`{.interpreted-text
role="ref"}

Returns the error text if
`parse()<class_Expression_method_parse>`{.interpreted-text role="ref"}
or `execute()<class_Expression_method_execute>`{.interpreted-text
role="ref"} has failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Expression_method_has_execute_failed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_execute_failed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Expression_method_has_execute_failed>`{.interpreted-text
role="ref"}

Returns `true` if
`execute()<class_Expression_method_execute>`{.interpreted-text
role="ref"} has failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Expression_method_parse}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**parse**(expression: `String<class_String>`{.interpreted-text
role="ref"}, input_names:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} = PackedStringArray())
`🔗<class_Expression_method_parse>`{.interpreted-text role="ref"}

Parses the expression and returns an
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} code.

You can optionally specify names of variables that may appear in the
expression with `input_names`, so that you can bind them when it gets
executed.
