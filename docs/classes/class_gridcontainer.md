github_url
:   hide

# GridContainer {#class_GridContainer}

**Inherits:** `Container<class_Container>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A container that arranges its child controls in a grid layout.

::: rst-class
classref-introduction-group
:::

## Description

**GridContainer** arranges its child controls in a grid layout. The
number of columns is specified by the
`columns<class_GridContainer_property_columns>`{.interpreted-text
role="ref"} property, whereas the number of rows depends on how many are
needed for the child controls. The number of rows and columns is
preserved for every size of the container.

\*\*Note:\*\* **GridContainer** only works with child nodes inheriting
from `Control<class_Control>`{.interpreted-text role="ref"}. It won\'t
rearrange child nodes inheriting from
`Node2D<class_Node2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Containers <../tutorials/ui/gui_containers>`{.interpreted-text
  role="doc"}
- [Operating System Testing
  Demo](https://godotengine.org/asset-library/asset/2789)

::: rst-class
classref-reftable-group
:::

## Properties

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

## Property Descriptions

:::: {#class_GridContainer_property_columns}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **columns** = `1`
`🔗<class_GridContainer_property_columns>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_columns**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_columns**()

The number of columns in the **GridContainer**. If modified,
**GridContainer** reorders its Control-derived children to accommodate
the new layout.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_GridContainer_theme_constant_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_separation** = `4`
`🔗<class_GridContainer_theme_constant_h_separation>`{.interpreted-text
role="ref"}

The horizontal separation of child nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GridContainer_theme_constant_v_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **v_separation** = `4`
`🔗<class_GridContainer_theme_constant_v_separation>`{.interpreted-text
role="ref"}

The vertical separation of child nodes.
