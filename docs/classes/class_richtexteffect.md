github_url
:   hide

# RichTextEffect {#class_RichTextEffect}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A custom effect for a
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A custom effect for a
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"},
which can be loaded in the
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"}
inspector or using
`RichTextLabel.install_effect()<class_RichTextLabel_method_install_effect>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For a **RichTextEffect** to be usable, a BBCode tag must
be defined as a member variable called `bbcode` in the script.

::::: tabs
::: code-tab
gdscript

\# The RichTextEffect will be usable like this: [\[example\]Some
text\[/example\]]{.title-ref} var bbcode = \"example\"
:::

::: code-tab
csharp

// The RichTextEffect will be usable like this: [\[example\]Some
text\[/example\]]{.title-ref} string bbcode = \"example\";
:::
:::::

\*\*Note:\*\* As soon as a
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"}
contains at least one **RichTextEffect**, it will continuously process
the effect unless the project is paused. This may impact battery life
negatively.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `BBCode in RichTextLabel <../tutorials/ui/bbcode_in_richtextlabel>`{.interpreted-text
  role="doc"}
- [RichTextEffect test project
  (third-party)](https://github.com/Eoin-ONeill-Yokai/Godot-Rich-Text-Effect-Test-Project)

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

:::: {#class_RichTextEffect_private_method__process_custom_fx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_process_custom_fx**(char_fx:
`CharFXTransform<class_CharFXTransform>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextEffect_private_method__process_custom_fx>`{.interpreted-text
role="ref"}

Override this method to modify properties in `char_fx`. The method must
return `true` if the character could be transformed successfully. If the
method returns `false`, it will skip transformation to avoid displaying
broken text.
