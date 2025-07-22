github_url
:   hide

# CanvasGroup {#class_CanvasGroup}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Merges several 2D nodes into a single draw operation.

::: rst-class
classref-introduction-group
:::

## Description

Child `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} nodes
of a **CanvasGroup** are drawn as a single object. It allows to e.g.
draw overlapping translucent 2D nodes without blending (set
`CanvasItem.self_modulate<class_CanvasItem_property_self_modulate>`{.interpreted-text
role="ref"} property of **CanvasGroup** to achieve this effect).

\*\*Note:\*\* The **CanvasGroup** uses a custom shader to read from the
backbuffer to draw its children. Assigning a
`Material<class_Material>`{.interpreted-text role="ref"} to the
**CanvasGroup** overrides the builtin shader. To duplicate the behavior
of the builtin shader in a custom
`Shader<class_Shader>`{.interpreted-text role="ref"} use the following:

    shader_type canvas_item;
    render_mode unshaded;

    uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_nearest;

    void fragment() {
        vec4 c = textureLod(screen_texture, SCREEN_UV, 0.0);

        if (c.a > 0.0001) {
            c.rgb /= c.a;
        }

        COLOR *= c;
    }

\*\*Note:\*\* Since **CanvasGroup** and
`CanvasItem.clip_children<class_CanvasItem_property_clip_children>`{.interpreted-text
role="ref"} both utilize the backbuffer, children of a **CanvasGroup**
who have their
`CanvasItem.clip_children<class_CanvasItem_property_clip_children>`{.interpreted-text
role="ref"} set to anything other than
`CanvasItem.CLIP_CHILDREN_DISABLED<class_CanvasItem_constant_CLIP_CHILDREN_DISABLED>`{.interpreted-text
role="ref"} will not function correctly.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CanvasGroup_property_clear_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **clear_margin** =
`10.0` `🔗<class_CanvasGroup_property_clear_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_clear_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_clear_margin**()

Sets the size of the margin used to expand the clearing rect of this
**CanvasGroup**. This expands the area of the backbuffer that will be
used by the **CanvasGroup**. A smaller margin will reduce the area of
the backbuffer used which can increase performance, however if
`use_mipmaps<class_CanvasGroup_property_use_mipmaps>`{.interpreted-text
role="ref"} is enabled, a small margin may result in mipmap errors at
the edge of the **CanvasGroup**. Accordingly, this should be left as
small as possible, but should be increased if artifacts appear along the
edges of the canvas group.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasGroup_property_fit_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fit_margin** =
`10.0` `🔗<class_CanvasGroup_property_fit_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fit_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fit_margin**()

Sets the size of a margin used to expand the drawable rect of this
**CanvasGroup**. The size of the **CanvasGroup** is determined by
fitting a rect around its children then expanding that rect by
`fit_margin<class_CanvasGroup_property_fit_margin>`{.interpreted-text
role="ref"}. This increases both the backbuffer area used and the area
covered by the **CanvasGroup** both of which can reduce performance.
This should be kept as small as possible and should only be expanded
when an increased size is needed (e.g. for custom shader effects).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasGroup_property_use_mipmaps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_mipmaps** =
`false` `🔗<class_CanvasGroup_property_use_mipmaps>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_mipmaps**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_mipmaps**()

If `true`, calculates mipmaps for the backbuffer before drawing the
**CanvasGroup** so that mipmaps can be used in a custom
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}
attached to the **CanvasGroup**. Generating mipmaps has a performance
cost so this should not be enabled unless required.
