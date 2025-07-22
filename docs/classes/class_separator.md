github_url
:   hide

# Separator {#class_Separator}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `HSeparator<class_HSeparator>`{.interpreted-text
role="ref"}, `VSeparator<class_VSeparator>`{.interpreted-text
role="ref"}

Abstract base class for separators.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for separators, used for separating other controls.
**Separator**s are purely visual and normally drawn as a
`StyleBoxLine<class_StyleBoxLine>`{.interpreted-text role="ref"}.

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

:::: {#class_Separator_theme_constant_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **separation** = `0`
`🔗<class_Separator_theme_constant_separation>`{.interpreted-text
role="ref"}

The size of the area covered by the separator. Effectively works like a
minimum width/height.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Separator_theme_style_separator}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **separator**
`🔗<class_Separator_theme_style_separator>`{.interpreted-text
role="ref"}

The style for the separator line. Works best with
`StyleBoxLine<class_StyleBoxLine>`{.interpreted-text role="ref"}
(remember to enable
`StyleBoxLine.vertical<class_StyleBoxLine_property_vertical>`{.interpreted-text
role="ref"} for `VSeparator<class_VSeparator>`{.interpreted-text
role="ref"}).
