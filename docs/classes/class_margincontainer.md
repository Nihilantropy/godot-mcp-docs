github_url
:   hide

::: {.meta keywords="padding"}
:::

# MarginContainer {#class_MarginContainer}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A container that keeps a margin around its child controls.

::: rst-class
classref-introduction-group
:::

## Description

**MarginContainer** adds an adjustable margin on each side of its child
controls. The margins are added around all children, not around each
individual one. To control the **MarginContainer**\'s margins, use the
`margin_*` theme properties listed below.

\*\*Note:\*\* The margin sizes are theme overrides, not normal
properties. This is an example of how to change them in code:

::::: tabs
::: code-tab
gdscript

\# This code sample assumes the current script is extending
MarginContainer. var margin_value = 100
add_theme_constant_override(\"margin_top\", margin_value)
add_theme_constant_override(\"margin_left\", margin_value)
add_theme_constant_override(\"margin_bottom\", margin_value)
add_theme_constant_override(\"margin_right\", margin_value)
:::

::: code-tab
csharp

// This code sample assumes the current script is extending
MarginContainer. int marginValue = 100;
AddThemeConstantOverride(\"margin_top\", marginValue);
AddThemeConstantOverride(\"margin_left\", marginValue);
AddThemeConstantOverride(\"margin_bottom\", marginValue);
AddThemeConstantOverride(\"margin_right\", marginValue);
:::
:::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Containers <../tutorials/ui/gui_containers>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Theme Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_MarginContainer_theme_constant_margin_bottom}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **margin_bottom** = `0`
`🔗<class_MarginContainer_theme_constant_margin_bottom>`{.interpreted-text
role="ref"}

Offsets towards the inside direct children of the container by this
amount of pixels from the bottom.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MarginContainer_theme_constant_margin_left}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **margin_left** = `0`
`🔗<class_MarginContainer_theme_constant_margin_left>`{.interpreted-text
role="ref"}

Offsets towards the inside direct children of the container by this
amount of pixels from the left.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MarginContainer_theme_constant_margin_right}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **margin_right** = `0`
`🔗<class_MarginContainer_theme_constant_margin_right>`{.interpreted-text
role="ref"}

Offsets towards the inside direct children of the container by this
amount of pixels from the right.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MarginContainer_theme_constant_margin_top}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **margin_top** = `0`
`🔗<class_MarginContainer_theme_constant_margin_top>`{.interpreted-text
role="ref"}

Offsets towards the inside direct children of the container by this
amount of pixels from the top.
