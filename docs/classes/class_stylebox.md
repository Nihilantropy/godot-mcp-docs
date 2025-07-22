github_url
:   hide

# StyleBox {#class_StyleBox}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `StyleBoxEmpty<class_StyleBoxEmpty>`{.interpreted-text
role="ref"}, `StyleBoxFlat<class_StyleBoxFlat>`{.interpreted-text
role="ref"}, `StyleBoxLine<class_StyleBoxLine>`{.interpreted-text
role="ref"}, `StyleBoxTexture<class_StyleBoxTexture>`{.interpreted-text
role="ref"}

Abstract base class for defining stylized boxes for UI elements.

::: rst-class
classref-introduction-group
:::

## Description

**StyleBox** is an abstract base class for drawing stylized boxes for UI
elements. It is used for panels, buttons,
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} backgrounds,
`Tree<class_Tree>`{.interpreted-text role="ref"} backgrounds, etc. and
also for testing a transparency mask for pointer signals. If mask test
fails on a **StyleBox** assigned as mask to a control, clicks and motion
signals will go through it to the one below.

\*\*Note:\*\* For control nodes that have *Theme Properties*, the
`focus` **StyleBox** is displayed over the `normal`, `hover` or
`pressed` **StyleBox**. This makes the `focus` **StyleBox** more
reusable across different nodes.

::: rst-class
classref-reftable-group
:::

## Properties

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

## Property Descriptions

:::: {#class_StyleBox_property_content_margin_bottom}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**content_margin_bottom** = `-1.0`
`🔗<class_StyleBox_property_content_margin_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_content_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, offset:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_content_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The bottom margin for the contents of this style box. Increasing this
value reduces the space available to the contents from the bottom.

If this value is negative, it is ignored and a child-specific margin is
used instead. For example, for
`StyleBoxFlat<class_StyleBoxFlat>`{.interpreted-text role="ref"}, the
border thickness (if any) is used instead.

It is up to the code using this style box to decide what these contents
are: for example, a `Button<class_Button>`{.interpreted-text role="ref"}
respects this content margin for the textual contents of the button.

`get_margin()<class_StyleBox_method_get_margin>`{.interpreted-text
role="ref"} should be used to fetch this value as consumer instead of
reading these properties directly. This is because it correctly respects
negative values and the fallback mentioned above.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_property_content_margin_left}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**content_margin_left** = `-1.0`
`🔗<class_StyleBox_property_content_margin_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_content_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, offset:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_content_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The left margin for the contents of this style box. Increasing this
value reduces the space available to the contents from the left.

Refer to
`content_margin_bottom<class_StyleBox_property_content_margin_bottom>`{.interpreted-text
role="ref"} for extra considerations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_property_content_margin_right}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**content_margin_right** = `-1.0`
`🔗<class_StyleBox_property_content_margin_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_content_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, offset:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_content_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The right margin for the contents of this style box. Increasing this
value reduces the space available to the contents from the right.

Refer to
`content_margin_bottom<class_StyleBox_property_content_margin_bottom>`{.interpreted-text
role="ref"} for extra considerations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_property_content_margin_top}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**content_margin_top** = `-1.0`
`🔗<class_StyleBox_property_content_margin_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_content_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, offset:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_content_margin**(margin:
  `Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The top margin for the contents of this style box. Increasing this value
reduces the space available to the contents from the top.

Refer to
`content_margin_bottom<class_StyleBox_property_content_margin_bottom>`{.interpreted-text
role="ref"} for extra considerations.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_StyleBox_private_method__draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_draw**(to_canvas_item: `RID<class_RID>`{.interpreted-text
role="ref"}, rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_StyleBox_private_method__draw>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_private_method__get_draw_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**\_get_draw_rect**(rect: `Rect2<class_Rect2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBox_private_method__get_draw_rect>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_private_method__get_minimum_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_minimum_size**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBox_private_method__get_minimum_size>`{.interpreted-text
role="ref"}

Virtual method to be implemented by the user. Returns a custom minimum
size that the stylebox must respect when drawing. By default
`get_minimum_size()<class_StyleBox_method_get_minimum_size>`{.interpreted-text
role="ref"} only takes content margins into account. This method can be
overridden to add another size restriction. A combination of the default
behavior and the output of this method will be used, to account for both
sizes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_private_method__test_mask}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_test_mask**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBox_private_method__test_mask>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_method_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw**(canvas_item: `RID<class_RID>`{.interpreted-text role="ref"},
rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_StyleBox_method_draw>`{.interpreted-text
role="ref"}

Draws this stylebox using a canvas item identified by the given
`RID<class_RID>`{.interpreted-text role="ref"}.

The `RID<class_RID>`{.interpreted-text role="ref"} value can either be
the result of
`CanvasItem.get_canvas_item()<class_CanvasItem_method_get_canvas_item>`{.interpreted-text
role="ref"} called on an existing
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}-derived
node, or directly from creating a canvas item in the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
with
`RenderingServer.canvas_item_create()<class_RenderingServer_method_canvas_item_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_method_get_content_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_content_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBox_method_get_content_margin>`{.interpreted-text
role="ref"}

Returns the default margin of the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_method_get_current_item_drawn}
::: rst-class
classref-method
:::
::::

`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**get_current_item_drawn**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBox_method_get_current_item_drawn>`{.interpreted-text
role="ref"}

Returns the `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
that handles its
`CanvasItem.NOTIFICATION_DRAW<class_CanvasItem_constant_NOTIFICATION_DRAW>`{.interpreted-text
role="ref"} or
`CanvasItem._draw()<class_CanvasItem_private_method__draw>`{.interpreted-text
role="ref"} callback at this moment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_method_get_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_margin**(margin: `Side<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_StyleBox_method_get_margin>`{.interpreted-text
role="ref"}

Returns the content margin offset for the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}.

Positive values reduce size inwards, unlike
`Control<class_Control>`{.interpreted-text role="ref"}\'s margin values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_method_get_minimum_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_minimum_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_StyleBox_method_get_minimum_size>`{.interpreted-text
role="ref"}

Returns the minimum size that this stylebox can be shrunk to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_method_get_offset}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_offset**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_StyleBox_method_get_offset>`{.interpreted-text
role="ref"}

Returns the \"offset\" of a stylebox. This helper function returns a
value equivalent to
`Vector2(style.get_margin(MARGIN_LEFT), style.get_margin(MARGIN_TOP))`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_method_set_content_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_content_margin**(margin:
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}, offset:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_StyleBox_method_set_content_margin>`{.interpreted-text
role="ref"}

Sets the default value of the specified
`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"} to `offset`
pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_method_set_content_margin_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_content_margin_all**(offset:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_StyleBox_method_set_content_margin_all>`{.interpreted-text
role="ref"}

Sets the default margin to `offset` pixels for all sides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_StyleBox_method_test_mask}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **test_mask**(point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_StyleBox_method_test_mask>`{.interpreted-text
role="ref"}

Test a position in a rectangle, return whether it passes the mask test.
