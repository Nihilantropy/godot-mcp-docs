github_url
:   hide

# \@GlobalScope {#class_@GlobalScope}

Global scope constants and functions.

::: rst-class
classref-introduction-group
:::

## Description

A list of global scope enumerated constants and built-in functions. This
is all that resides in the globals, constants regarding error codes,
keycodes, property hints, etc.

Singletons are also documented here, since they can be accessed from
anywhere.

For the entries that can only be accessed from scripts written in
GDScript, see `@GDScript<class_@GDScript>`{.interpreted-text
role="ref"}.

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Random number generation <../tutorials/math/random_number_generation>`{.interpreted-text
  role="doc"}

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

## Enumerations

:::: {#enum_@GlobalScope_Side}
::: rst-class
classref-enumeration
:::
::::

enum **Side**: `🔗<enum_@GlobalScope_Side>`{.interpreted-text
role="ref"}

:::: {#class_@GlobalScope_constant_SIDE_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}
**SIDE_LEFT** = `0`

Left side, usually used for `Control<class_Control>`{.interpreted-text
role="ref"} or `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}-derived classes.

:::: {#class_@GlobalScope_constant_SIDE_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}
**SIDE_TOP** = `1`

Top side, usually used for `Control<class_Control>`{.interpreted-text
role="ref"} or `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}-derived classes.

:::: {#class_@GlobalScope_constant_SIDE_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}
**SIDE_RIGHT** = `2`

Right side, usually used for `Control<class_Control>`{.interpreted-text
role="ref"} or `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}-derived classes.

:::: {#class_@GlobalScope_constant_SIDE_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`Side<enum_@GlobalScope_Side>`{.interpreted-text role="ref"}
**SIDE_BOTTOM** = `3`

Bottom side, usually used for `Control<class_Control>`{.interpreted-text
role="ref"} or `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}-derived classes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_Corner}
::: rst-class
classref-enumeration
:::
::::

enum **Corner**: `🔗<enum_@GlobalScope_Corner>`{.interpreted-text
role="ref"}

:::: {#class_@GlobalScope_constant_CORNER_TOP_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"}
**CORNER_TOP_LEFT** = `0`

Top-left corner.

:::: {#class_@GlobalScope_constant_CORNER_TOP_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"}
**CORNER_TOP_RIGHT** = `1`

Top-right corner.

:::: {#class_@GlobalScope_constant_CORNER_BOTTOM_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"}
**CORNER_BOTTOM_RIGHT** = `2`

Bottom-right corner.

:::: {#class_@GlobalScope_constant_CORNER_BOTTOM_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Corner<enum_@GlobalScope_Corner>`{.interpreted-text role="ref"}
**CORNER_BOTTOM_LEFT** = `3`

Bottom-left corner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_Orientation}
::: rst-class
classref-enumeration
:::
::::

enum **Orientation**:
`🔗<enum_@GlobalScope_Orientation>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_VERTICAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Orientation<enum_@GlobalScope_Orientation>`{.interpreted-text
role="ref"} **VERTICAL** = `1`

General vertical alignment, usually used for
`Separator<class_Separator>`{.interpreted-text role="ref"},
`ScrollBar<class_ScrollBar>`{.interpreted-text role="ref"},
`Slider<class_Slider>`{.interpreted-text role="ref"}, etc.

:::: {#class_@GlobalScope_constant_HORIZONTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Orientation<enum_@GlobalScope_Orientation>`{.interpreted-text
role="ref"} **HORIZONTAL** = `0`

General horizontal alignment, usually used for
`Separator<class_Separator>`{.interpreted-text role="ref"},
`ScrollBar<class_ScrollBar>`{.interpreted-text role="ref"},
`Slider<class_Slider>`{.interpreted-text role="ref"}, etc.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_ClockDirection}
::: rst-class
classref-enumeration
:::
::::

enum **ClockDirection**:
`🔗<enum_@GlobalScope_ClockDirection>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_CLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`ClockDirection<enum_@GlobalScope_ClockDirection>`{.interpreted-text
role="ref"} **CLOCKWISE** = `0`

Clockwise rotation. Used by some methods (e.g.
`Image.rotate_90()<class_Image_method_rotate_90>`{.interpreted-text
role="ref"}).

:::: {#class_@GlobalScope_constant_COUNTERCLOCKWISE}
::: rst-class
classref-enumeration-constant
:::
::::

`ClockDirection<enum_@GlobalScope_ClockDirection>`{.interpreted-text
role="ref"} **COUNTERCLOCKWISE** = `1`

Counter-clockwise rotation. Used by some methods (e.g.
`Image.rotate_90()<class_Image_method_rotate_90>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_HorizontalAlignment}
::: rst-class
classref-enumeration
:::
::::

enum **HorizontalAlignment**:
`🔗<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"}

:::: {#class_@GlobalScope_constant_HORIZONTAL_ALIGNMENT_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **HORIZONTAL_ALIGNMENT_LEFT** = `0`

Horizontal left alignment, usually for text-derived classes.

:::: {#class_@GlobalScope_constant_HORIZONTAL_ALIGNMENT_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **HORIZONTAL_ALIGNMENT_CENTER** = `1`

Horizontal center alignment, usually for text-derived classes.

:::: {#class_@GlobalScope_constant_HORIZONTAL_ALIGNMENT_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **HORIZONTAL_ALIGNMENT_RIGHT** = `2`

Horizontal right alignment, usually for text-derived classes.

:::: {#class_@GlobalScope_constant_HORIZONTAL_ALIGNMENT_FILL}
::: rst-class
classref-enumeration-constant
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **HORIZONTAL_ALIGNMENT_FILL** = `3`

Expand row to fit width, usually for text-derived classes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_VerticalAlignment}
::: rst-class
classref-enumeration
:::
::::

enum **VerticalAlignment**:
`🔗<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_VERTICAL_ALIGNMENT_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} **VERTICAL_ALIGNMENT_TOP** = `0`

Vertical top alignment, usually for text-derived classes.

:::: {#class_@GlobalScope_constant_VERTICAL_ALIGNMENT_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} **VERTICAL_ALIGNMENT_CENTER** = `1`

Vertical center alignment, usually for text-derived classes.

:::: {#class_@GlobalScope_constant_VERTICAL_ALIGNMENT_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} **VERTICAL_ALIGNMENT_BOTTOM** = `2`

Vertical bottom alignment, usually for text-derived classes.

:::: {#class_@GlobalScope_constant_VERTICAL_ALIGNMENT_FILL}
::: rst-class
classref-enumeration-constant
:::
::::

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} **VERTICAL_ALIGNMENT_FILL** = `3`

Expand rows to fit height, usually for text-derived classes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_InlineAlignment}
::: rst-class
classref-enumeration
:::
::::

enum **InlineAlignment**:
`🔗<enum_@GlobalScope_InlineAlignment>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_TOP_TO}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_TOP_TO** = `0`

Aligns the top of the inline object (e.g. image, table) to the position
of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_CENTER_TO}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_CENTER_TO** = `1`

Aligns the center of the inline object (e.g. image, table) to the
position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_BASELINE_TO}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_BASELINE_TO** = `3`

Aligns the baseline (user defined) of the inline object (e.g. image,
table) to the position of the text specified by `INLINE_ALIGNMENT_TO_*`
constant.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_BOTTOM_TO}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_BOTTOM_TO** = `2`

Aligns the bottom of the inline object (e.g. image, table) to the
position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_TO_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_TO_TOP** = `0`

Aligns the position of the inline object (e.g. image, table) specified
by `INLINE_ALIGNMENT_*_TO` constant to the top of the text.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_TO_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_TO_CENTER** = `4`

Aligns the position of the inline object (e.g. image, table) specified
by `INLINE_ALIGNMENT_*_TO` constant to the center of the text.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_TO_BASELINE}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_TO_BASELINE** = `8`

Aligns the position of the inline object (e.g. image, table) specified
by `INLINE_ALIGNMENT_*_TO` constant to the baseline of the text.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_TO_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_TO_BOTTOM** = `12`

Aligns inline object (e.g. image, table) to the bottom of the text.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_TOP** = `0`

Aligns top of the inline object (e.g. image, table) to the top of the
text. Equivalent to `INLINE_ALIGNMENT_TOP_TO | INLINE_ALIGNMENT_TO_TOP`.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_CENTER** = `5`

Aligns center of the inline object (e.g. image, table) to the center of
the text. Equivalent to
`INLINE_ALIGNMENT_CENTER_TO | INLINE_ALIGNMENT_TO_CENTER`.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_BOTTOM** = `14`

Aligns bottom of the inline object (e.g. image, table) to the bottom of
the text. Equivalent to
`INLINE_ALIGNMENT_BOTTOM_TO | INLINE_ALIGNMENT_TO_BOTTOM`.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_IMAGE_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_IMAGE_MASK** = `3`

A bit mask for `INLINE_ALIGNMENT_*_TO` alignment constants.

:::: {#class_@GlobalScope_constant_INLINE_ALIGNMENT_TEXT_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} **INLINE_ALIGNMENT_TEXT_MASK** = `12`

A bit mask for `INLINE_ALIGNMENT_TO_*` alignment constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_EulerOrder}
::: rst-class
classref-enumeration
:::
::::

enum **EulerOrder**:
`🔗<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_EULER_ORDER_XYZ}
::: rst-class
classref-enumeration-constant
:::
::::

`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
**EULER_ORDER_XYZ** = `0`

Specifies that Euler angles should be in XYZ order. When composing, the
order is X, Y, Z. When decomposing, the order is reversed, first Z, then
Y, and X last.

:::: {#class_@GlobalScope_constant_EULER_ORDER_XZY}
::: rst-class
classref-enumeration-constant
:::
::::

`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
**EULER_ORDER_XZY** = `1`

Specifies that Euler angles should be in XZY order. When composing, the
order is X, Z, Y. When decomposing, the order is reversed, first Y, then
Z, and X last.

:::: {#class_@GlobalScope_constant_EULER_ORDER_YXZ}
::: rst-class
classref-enumeration-constant
:::
::::

`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
**EULER_ORDER_YXZ** = `2`

Specifies that Euler angles should be in YXZ order. When composing, the
order is Y, X, Z. When decomposing, the order is reversed, first Z, then
X, and Y last.

:::: {#class_@GlobalScope_constant_EULER_ORDER_YZX}
::: rst-class
classref-enumeration-constant
:::
::::

`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
**EULER_ORDER_YZX** = `3`

Specifies that Euler angles should be in YZX order. When composing, the
order is Y, Z, X. When decomposing, the order is reversed, first X, then
Z, and Y last.

:::: {#class_@GlobalScope_constant_EULER_ORDER_ZXY}
::: rst-class
classref-enumeration-constant
:::
::::

`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
**EULER_ORDER_ZXY** = `4`

Specifies that Euler angles should be in ZXY order. When composing, the
order is Z, X, Y. When decomposing, the order is reversed, first Y, then
X, and Z last.

:::: {#class_@GlobalScope_constant_EULER_ORDER_ZYX}
::: rst-class
classref-enumeration-constant
:::
::::

`EulerOrder<enum_@GlobalScope_EulerOrder>`{.interpreted-text role="ref"}
**EULER_ORDER_ZYX** = `5`

Specifies that Euler angles should be in ZYX order. When composing, the
order is Z, Y, X. When decomposing, the order is reversed, first X, then
Y, and Z last.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_Key}
::: rst-class
classref-enumeration
:::
::::

enum **Key**: `🔗<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_KEY_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_NONE**
= `0`

Enum value which doesn\'t correspond to any key. This is used to
initialize `Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
properties with a generic state.

:::: {#class_@GlobalScope_constant_KEY_SPECIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_SPECIAL** = `4194304`

Keycodes with this bit applied are non-printable.

:::: {#class_@GlobalScope_constant_KEY_ESCAPE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_ESCAPE** = `4194305`

Escape key.

:::: {#class_@GlobalScope_constant_KEY_TAB}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_TAB** =
`4194306`

Tab key.

:::: {#class_@GlobalScope_constant_KEY_BACKTAB}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_BACKTAB** = `4194307`

Shift + Tab key.

:::: {#class_@GlobalScope_constant_KEY_BACKSPACE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_BACKSPACE** = `4194308`

Backspace key.

:::: {#class_@GlobalScope_constant_KEY_ENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_ENTER**
= `4194309`

Return key (on the main keyboard).

:::: {#class_@GlobalScope_constant_KEY_KP_ENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_KP_ENTER** = `4194310`

Enter key on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_INSERT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_INSERT** = `4194311`

Insert key.

:::: {#class_@GlobalScope_constant_KEY_DELETE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_DELETE** = `4194312`

Delete key.

:::: {#class_@GlobalScope_constant_KEY_PAUSE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_PAUSE**
= `4194313`

Pause key.

:::: {#class_@GlobalScope_constant_KEY_PRINT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_PRINT**
= `4194314`

Print Screen key.

:::: {#class_@GlobalScope_constant_KEY_SYSREQ}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_SYSREQ** = `4194315`

System Request key.

:::: {#class_@GlobalScope_constant_KEY_CLEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_CLEAR**
= `4194316`

Clear key.

:::: {#class_@GlobalScope_constant_KEY_HOME}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_HOME**
= `4194317`

Home key.

:::: {#class_@GlobalScope_constant_KEY_END}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_END** =
`4194318`

End key.

:::: {#class_@GlobalScope_constant_KEY_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_LEFT**
= `4194319`

Left arrow key.

:::: {#class_@GlobalScope_constant_KEY_UP}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_UP** =
`4194320`

Up arrow key.

:::: {#class_@GlobalScope_constant_KEY_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_RIGHT**
= `4194321`

Right arrow key.

:::: {#class_@GlobalScope_constant_KEY_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_DOWN**
= `4194322`

Down arrow key.

:::: {#class_@GlobalScope_constant_KEY_PAGEUP}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_PAGEUP** = `4194323`

Page Up key.

:::: {#class_@GlobalScope_constant_KEY_PAGEDOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_PAGEDOWN** = `4194324`

Page Down key.

:::: {#class_@GlobalScope_constant_KEY_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_SHIFT**
= `4194325`

Shift key.

:::: {#class_@GlobalScope_constant_KEY_CTRL}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_CTRL**
= `4194326`

Control key.

:::: {#class_@GlobalScope_constant_KEY_META}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_META**
= `4194327`

Meta key.

:::: {#class_@GlobalScope_constant_KEY_ALT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_ALT** =
`4194328`

Alt key.

:::: {#class_@GlobalScope_constant_KEY_CAPSLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_CAPSLOCK** = `4194329`

Caps Lock key.

:::: {#class_@GlobalScope_constant_KEY_NUMLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_NUMLOCK** = `4194330`

Num Lock key.

:::: {#class_@GlobalScope_constant_KEY_SCROLLLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_SCROLLLOCK** = `4194331`

Scroll Lock key.

:::: {#class_@GlobalScope_constant_KEY_F1}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F1** =
`4194332`

F1 key.

:::: {#class_@GlobalScope_constant_KEY_F2}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F2** =
`4194333`

F2 key.

:::: {#class_@GlobalScope_constant_KEY_F3}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F3** =
`4194334`

F3 key.

:::: {#class_@GlobalScope_constant_KEY_F4}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F4** =
`4194335`

F4 key.

:::: {#class_@GlobalScope_constant_KEY_F5}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F5** =
`4194336`

F5 key.

:::: {#class_@GlobalScope_constant_KEY_F6}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F6** =
`4194337`

F6 key.

:::: {#class_@GlobalScope_constant_KEY_F7}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F7** =
`4194338`

F7 key.

:::: {#class_@GlobalScope_constant_KEY_F8}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F8** =
`4194339`

F8 key.

:::: {#class_@GlobalScope_constant_KEY_F9}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F9** =
`4194340`

F9 key.

:::: {#class_@GlobalScope_constant_KEY_F10}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F10** =
`4194341`

F10 key.

:::: {#class_@GlobalScope_constant_KEY_F11}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F11** =
`4194342`

F11 key.

:::: {#class_@GlobalScope_constant_KEY_F12}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F12** =
`4194343`

F12 key.

:::: {#class_@GlobalScope_constant_KEY_F13}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F13** =
`4194344`

F13 key.

:::: {#class_@GlobalScope_constant_KEY_F14}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F14** =
`4194345`

F14 key.

:::: {#class_@GlobalScope_constant_KEY_F15}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F15** =
`4194346`

F15 key.

:::: {#class_@GlobalScope_constant_KEY_F16}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F16** =
`4194347`

F16 key.

:::: {#class_@GlobalScope_constant_KEY_F17}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F17** =
`4194348`

F17 key.

:::: {#class_@GlobalScope_constant_KEY_F18}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F18** =
`4194349`

F18 key.

:::: {#class_@GlobalScope_constant_KEY_F19}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F19** =
`4194350`

F19 key.

:::: {#class_@GlobalScope_constant_KEY_F20}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F20** =
`4194351`

F20 key.

:::: {#class_@GlobalScope_constant_KEY_F21}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F21** =
`4194352`

F21 key.

:::: {#class_@GlobalScope_constant_KEY_F22}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F22** =
`4194353`

F22 key.

:::: {#class_@GlobalScope_constant_KEY_F23}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F23** =
`4194354`

F23 key.

:::: {#class_@GlobalScope_constant_KEY_F24}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F24** =
`4194355`

F24 key.

:::: {#class_@GlobalScope_constant_KEY_F25}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F25** =
`4194356`

F25 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F26}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F26** =
`4194357`

F26 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F27}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F27** =
`4194358`

F27 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F28}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F28** =
`4194359`

F28 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F29}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F29** =
`4194360`

F29 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F30}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F30** =
`4194361`

F30 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F31}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F31** =
`4194362`

F31 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F32}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F32** =
`4194363`

F32 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F33}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F33** =
`4194364`

F33 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F34}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F34** =
`4194365`

F34 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_F35}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F35** =
`4194366`

F35 key. Only supported on macOS and Linux due to a Windows limitation.

:::: {#class_@GlobalScope_constant_KEY_KP_MULTIPLY}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_KP_MULTIPLY** = `4194433`

Multiply (\*) key on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_DIVIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_KP_DIVIDE** = `4194434`

Divide (/) key on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_SUBTRACT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_KP_SUBTRACT** = `4194435`

Subtract (-) key on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_PERIOD}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_KP_PERIOD** = `4194436`

Period (.) key on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_KP_ADD** = `4194437`

Add (+) key on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_0}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_0**
= `4194438`

Number 0 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_1}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_1**
= `4194439`

Number 1 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_2}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_2**
= `4194440`

Number 2 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_3}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_3**
= `4194441`

Number 3 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_4}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_4**
= `4194442`

Number 4 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_5}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_5**
= `4194443`

Number 5 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_6}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_6**
= `4194444`

Number 6 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_7}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_7**
= `4194445`

Number 7 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_8}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_8**
= `4194446`

Number 8 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_KP_9}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_KP_9**
= `4194447`

Number 9 on the numeric keypad.

:::: {#class_@GlobalScope_constant_KEY_MENU}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_MENU**
= `4194370`

Context menu key.

:::: {#class_@GlobalScope_constant_KEY_HYPER}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_HYPER**
= `4194371`

Hyper key. (On Linux/X11 only).

:::: {#class_@GlobalScope_constant_KEY_HELP}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_HELP**
= `4194373`

Help key.

:::: {#class_@GlobalScope_constant_KEY_BACK}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_BACK**
= `4194376`

Back key.

:::: {#class_@GlobalScope_constant_KEY_FORWARD}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_FORWARD** = `4194377`

Forward key.

:::: {#class_@GlobalScope_constant_KEY_STOP}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_STOP**
= `4194378`

Media stop key.

:::: {#class_@GlobalScope_constant_KEY_REFRESH}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_REFRESH** = `4194379`

Refresh key.

:::: {#class_@GlobalScope_constant_KEY_VOLUMEDOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_VOLUMEDOWN** = `4194380`

Volume down key.

:::: {#class_@GlobalScope_constant_KEY_VOLUMEMUTE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_VOLUMEMUTE** = `4194381`

Mute volume key.

:::: {#class_@GlobalScope_constant_KEY_VOLUMEUP}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_VOLUMEUP** = `4194382`

Volume up key.

:::: {#class_@GlobalScope_constant_KEY_MEDIAPLAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_MEDIAPLAY** = `4194388`

Media play key.

:::: {#class_@GlobalScope_constant_KEY_MEDIASTOP}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_MEDIASTOP** = `4194389`

Media stop key.

:::: {#class_@GlobalScope_constant_KEY_MEDIAPREVIOUS}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_MEDIAPREVIOUS** = `4194390`

Previous song key.

:::: {#class_@GlobalScope_constant_KEY_MEDIANEXT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_MEDIANEXT** = `4194391`

Next song key.

:::: {#class_@GlobalScope_constant_KEY_MEDIARECORD}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_MEDIARECORD** = `4194392`

Media record key.

:::: {#class_@GlobalScope_constant_KEY_HOMEPAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_HOMEPAGE** = `4194393`

Home page key.

:::: {#class_@GlobalScope_constant_KEY_FAVORITES}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_FAVORITES** = `4194394`

Favorites key.

:::: {#class_@GlobalScope_constant_KEY_SEARCH}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_SEARCH** = `4194395`

Search key.

:::: {#class_@GlobalScope_constant_KEY_STANDBY}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_STANDBY** = `4194396`

Standby key.

:::: {#class_@GlobalScope_constant_KEY_OPENURL}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_OPENURL** = `4194397`

Open URL / Launch Browser key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCHMAIL}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCHMAIL** = `4194398`

Launch Mail key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCHMEDIA}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCHMEDIA** = `4194399`

Launch Media key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH0}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH0** = `4194400`

Launch Shortcut 0 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH1}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH1** = `4194401`

Launch Shortcut 1 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH2}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH2** = `4194402`

Launch Shortcut 2 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH3}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH3** = `4194403`

Launch Shortcut 3 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH4}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH4** = `4194404`

Launch Shortcut 4 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH5}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH5** = `4194405`

Launch Shortcut 5 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH6}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH6** = `4194406`

Launch Shortcut 6 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH7}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH7** = `4194407`

Launch Shortcut 7 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH8}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH8** = `4194408`

Launch Shortcut 8 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCH9}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCH9** = `4194409`

Launch Shortcut 9 key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCHA}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCHA** = `4194410`

Launch Shortcut A key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCHB}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCHB** = `4194411`

Launch Shortcut B key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCHC}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCHC** = `4194412`

Launch Shortcut C key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCHD}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCHD** = `4194413`

Launch Shortcut D key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCHE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCHE** = `4194414`

Launch Shortcut E key.

:::: {#class_@GlobalScope_constant_KEY_LAUNCHF}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_LAUNCHF** = `4194415`

Launch Shortcut F key.

:::: {#class_@GlobalScope_constant_KEY_GLOBE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_GLOBE**
= `4194416`

\"Globe\" key on Mac / iPad keyboard.

:::: {#class_@GlobalScope_constant_KEY_KEYBOARD}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_KEYBOARD** = `4194417`

\"On-screen keyboard\" key on iPad keyboard.

:::: {#class_@GlobalScope_constant_KEY_JIS_EISU}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_JIS_EISU** = `4194418`

英数 key on Mac keyboard.

:::: {#class_@GlobalScope_constant_KEY_JIS_KANA}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_JIS_KANA** = `4194419`

かな key on Mac keyboard.

:::: {#class_@GlobalScope_constant_KEY_UNKNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_UNKNOWN** = `8388607`

Unknown key.

:::: {#class_@GlobalScope_constant_KEY_SPACE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_SPACE**
= `32`

Space key.

:::: {#class_@GlobalScope_constant_KEY_EXCLAM}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_EXCLAM** = `33`

Exclamation mark (`!`) key.

:::: {#class_@GlobalScope_constant_KEY_QUOTEDBL}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_QUOTEDBL** = `34`

Double quotation mark (`"`) key.

:::: {#class_@GlobalScope_constant_KEY_NUMBERSIGN}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_NUMBERSIGN** = `35`

Number sign or *hash* (`#`) key.

:::: {#class_@GlobalScope_constant_KEY_DOLLAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_DOLLAR** = `36`

Dollar sign (`$`) key.

:::: {#class_@GlobalScope_constant_KEY_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_PERCENT** = `37`

Percent sign (`%`) key.

:::: {#class_@GlobalScope_constant_KEY_AMPERSAND}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_AMPERSAND** = `38`

Ampersand (`&`) key.

:::: {#class_@GlobalScope_constant_KEY_APOSTROPHE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_APOSTROPHE** = `39`

Apostrophe (`'`) key.

:::: {#class_@GlobalScope_constant_KEY_PARENLEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_PARENLEFT** = `40`

Left parenthesis (`(`) key.

:::: {#class_@GlobalScope_constant_KEY_PARENRIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_PARENRIGHT** = `41`

Right parenthesis (`)`) key.

:::: {#class_@GlobalScope_constant_KEY_ASTERISK}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_ASTERISK** = `42`

Asterisk (`*`) key.

:::: {#class_@GlobalScope_constant_KEY_PLUS}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_PLUS**
= `43`

Plus (`+`) key.

:::: {#class_@GlobalScope_constant_KEY_COMMA}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_COMMA**
= `44`

Comma (`,`) key.

:::: {#class_@GlobalScope_constant_KEY_MINUS}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_MINUS**
= `45`

Minus (`-`) key.

:::: {#class_@GlobalScope_constant_KEY_PERIOD}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_PERIOD** = `46`

Period (`.`) key.

:::: {#class_@GlobalScope_constant_KEY_SLASH}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_SLASH**
= `47`

Slash (`/`) key.

:::: {#class_@GlobalScope_constant_KEY_0}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_0** =
`48`

Number 0 key.

:::: {#class_@GlobalScope_constant_KEY_1}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_1** =
`49`

Number 1 key.

:::: {#class_@GlobalScope_constant_KEY_2}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_2** =
`50`

Number 2 key.

:::: {#class_@GlobalScope_constant_KEY_3}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_3** =
`51`

Number 3 key.

:::: {#class_@GlobalScope_constant_KEY_4}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_4** =
`52`

Number 4 key.

:::: {#class_@GlobalScope_constant_KEY_5}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_5** =
`53`

Number 5 key.

:::: {#class_@GlobalScope_constant_KEY_6}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_6** =
`54`

Number 6 key.

:::: {#class_@GlobalScope_constant_KEY_7}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_7** =
`55`

Number 7 key.

:::: {#class_@GlobalScope_constant_KEY_8}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_8** =
`56`

Number 8 key.

:::: {#class_@GlobalScope_constant_KEY_9}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_9** =
`57`

Number 9 key.

:::: {#class_@GlobalScope_constant_KEY_COLON}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_COLON**
= `58`

Colon (`:`) key.

:::: {#class_@GlobalScope_constant_KEY_SEMICOLON}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_SEMICOLON** = `59`

Semicolon (`;`) key.

:::: {#class_@GlobalScope_constant_KEY_LESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_LESS**
= `60`

Less-than sign (`<`) key.

:::: {#class_@GlobalScope_constant_KEY_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_EQUAL**
= `61`

Equal sign (`=`) key.

:::: {#class_@GlobalScope_constant_KEY_GREATER}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_GREATER** = `62`

Greater-than sign (`>`) key.

:::: {#class_@GlobalScope_constant_KEY_QUESTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_QUESTION** = `63`

Question mark (`?`) key.

:::: {#class_@GlobalScope_constant_KEY_AT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_AT** =
`64`

At sign (`@`) key.

:::: {#class_@GlobalScope_constant_KEY_A}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_A** =
`65`

A key.

:::: {#class_@GlobalScope_constant_KEY_B}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_B** =
`66`

B key.

:::: {#class_@GlobalScope_constant_KEY_C}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_C** =
`67`

C key.

:::: {#class_@GlobalScope_constant_KEY_D}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_D** =
`68`

D key.

:::: {#class_@GlobalScope_constant_KEY_E}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_E** =
`69`

E key.

:::: {#class_@GlobalScope_constant_KEY_F}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_F** =
`70`

F key.

:::: {#class_@GlobalScope_constant_KEY_G}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_G** =
`71`

G key.

:::: {#class_@GlobalScope_constant_KEY_H}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_H** =
`72`

H key.

:::: {#class_@GlobalScope_constant_KEY_I}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_I** =
`73`

I key.

:::: {#class_@GlobalScope_constant_KEY_J}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_J** =
`74`

J key.

:::: {#class_@GlobalScope_constant_KEY_K}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_K** =
`75`

K key.

:::: {#class_@GlobalScope_constant_KEY_L}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_L** =
`76`

L key.

:::: {#class_@GlobalScope_constant_KEY_M}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_M** =
`77`

M key.

:::: {#class_@GlobalScope_constant_KEY_N}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_N** =
`78`

N key.

:::: {#class_@GlobalScope_constant_KEY_O}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_O** =
`79`

O key.

:::: {#class_@GlobalScope_constant_KEY_P}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_P** =
`80`

P key.

:::: {#class_@GlobalScope_constant_KEY_Q}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_Q** =
`81`

Q key.

:::: {#class_@GlobalScope_constant_KEY_R}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_R** =
`82`

R key.

:::: {#class_@GlobalScope_constant_KEY_S}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_S** =
`83`

S key.

:::: {#class_@GlobalScope_constant_KEY_T}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_T** =
`84`

T key.

:::: {#class_@GlobalScope_constant_KEY_U}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_U** =
`85`

U key.

:::: {#class_@GlobalScope_constant_KEY_V}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_V** =
`86`

V key.

:::: {#class_@GlobalScope_constant_KEY_W}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_W** =
`87`

W key.

:::: {#class_@GlobalScope_constant_KEY_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_X** =
`88`

X key.

:::: {#class_@GlobalScope_constant_KEY_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_Y** =
`89`

Y key.

:::: {#class_@GlobalScope_constant_KEY_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_Z** =
`90`

Z key.

:::: {#class_@GlobalScope_constant_KEY_BRACKETLEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_BRACKETLEFT** = `91`

Left bracket (`[lb]`) key.

:::: {#class_@GlobalScope_constant_KEY_BACKSLASH}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_BACKSLASH** = `92`

Backslash (`\`) key.

:::: {#class_@GlobalScope_constant_KEY_BRACKETRIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_BRACKETRIGHT** = `93`

Right bracket (`[rb]`) key.

:::: {#class_@GlobalScope_constant_KEY_ASCIICIRCUM}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_ASCIICIRCUM** = `94`

Caret (`^`) key.

:::: {#class_@GlobalScope_constant_KEY_UNDERSCORE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_UNDERSCORE** = `95`

Underscore (`_`) key.

:::: {#class_@GlobalScope_constant_KEY_QUOTELEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_QUOTELEFT** = `96`

Backtick (``\`) key.

:::: {#class_@GlobalScope_constant_KEY_BRACELEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_BRACELEFT** = `123`

Left brace (`{`) key.

:::: {#class_@GlobalScope_constant_KEY_BAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_BAR** =
`124`

Vertical bar or *pipe* (`|`) key.

:::: {#class_@GlobalScope_constant_KEY_BRACERIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_BRACERIGHT** = `125`

Right brace (`}`) key.

:::: {#class_@GlobalScope_constant_KEY_ASCIITILDE}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_ASCIITILDE** = `126`

Tilde (`~`) key.

:::: {#class_@GlobalScope_constant_KEY_YEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} **KEY_YEN** =
`165`

Yen symbol (`¥`) key.

:::: {#class_@GlobalScope_constant_KEY_SECTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"}
**KEY_SECTION** = `167`

Section sign (`§`) key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_KeyModifierMask}
::: rst-class
classref-enumeration
:::
::::

flags **KeyModifierMask**:
`🔗<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_KEY_CODE_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"} **KEY_CODE_MASK** = `8388607`

Key Code mask.

:::: {#class_@GlobalScope_constant_KEY_MODIFIER_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"} **KEY_MODIFIER_MASK** = `2130706432`

Modifier key mask.

:::: {#class_@GlobalScope_constant_KEY_MASK_CMD_OR_CTRL}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"} **KEY_MASK_CMD_OR_CTRL** = `16777216`

Automatically remapped to
`KEY_META<class_@GlobalScope_constant_KEY_META>`{.interpreted-text
role="ref"} on macOS and
`KEY_CTRL<class_@GlobalScope_constant_KEY_CTRL>`{.interpreted-text
role="ref"} on other platforms, this mask is never set in the actual
events, and should be used for key mapping only.

:::: {#class_@GlobalScope_constant_KEY_MASK_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"} **KEY_MASK_SHIFT** = `33554432`

Shift key mask.

:::: {#class_@GlobalScope_constant_KEY_MASK_ALT}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"} **KEY_MASK_ALT** = `67108864`

Alt or Option (on macOS) key mask.

:::: {#class_@GlobalScope_constant_KEY_MASK_META}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"} **KEY_MASK_META** = `134217728`

Command (on macOS) or Meta/Windows key mask.

:::: {#class_@GlobalScope_constant_KEY_MASK_CTRL}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"} **KEY_MASK_CTRL** = `268435456`

Control key mask.

:::: {#class_@GlobalScope_constant_KEY_MASK_KPAD}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"} **KEY_MASK_KPAD** = `536870912`

Keypad key mask.

:::: {#class_@GlobalScope_constant_KEY_MASK_GROUP_SWITCH}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`{.interpreted-text
role="ref"} **KEY_MASK_GROUP_SWITCH** = `1073741824`

Group Switch key mask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_KeyLocation}
::: rst-class
classref-enumeration
:::
::::

enum **KeyLocation**:
`🔗<enum_@GlobalScope_KeyLocation>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_KEY_LOCATION_UNSPECIFIED}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyLocation<enum_@GlobalScope_KeyLocation>`{.interpreted-text
role="ref"} **KEY_LOCATION_UNSPECIFIED** = `0`

Used for keys which only appear once, or when a comparison doesn\'t need
to differentiate the `LEFT` and `RIGHT` versions.

For example, when using
`InputEvent.is_match()<class_InputEvent_method_is_match>`{.interpreted-text
role="ref"}, an event which has
`KEY_LOCATION_UNSPECIFIED<class_@GlobalScope_constant_KEY_LOCATION_UNSPECIFIED>`{.interpreted-text
role="ref"} will match any
`KeyLocation<enum_@GlobalScope_KeyLocation>`{.interpreted-text
role="ref"} on the passed event.

:::: {#class_@GlobalScope_constant_KEY_LOCATION_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyLocation<enum_@GlobalScope_KeyLocation>`{.interpreted-text
role="ref"} **KEY_LOCATION_LEFT** = `1`

A key which is to the left of its twin.

:::: {#class_@GlobalScope_constant_KEY_LOCATION_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`KeyLocation<enum_@GlobalScope_KeyLocation>`{.interpreted-text
role="ref"} **KEY_LOCATION_RIGHT** = `2`

A key which is to the right of its twin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_MouseButton}
::: rst-class
classref-enumeration
:::
::::

enum **MouseButton**:
`🔗<enum_@GlobalScope_MouseButton>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_NONE** = `0`

Enum value which doesn\'t correspond to any mouse button. This is used
to initialize
`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} properties with a generic state.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_LEFT** = `1`

Primary mouse button, usually assigned to the left button.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_RIGHT** = `2`

Secondary mouse button, usually assigned to the right button.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_MIDDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_MIDDLE** = `3`

Middle mouse button.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_UP}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_WHEEL_UP** = `4`

Mouse wheel scrolling up.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_WHEEL_DOWN** = `5`

Mouse wheel scrolling down.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_WHEEL_LEFT** = `6`

Mouse wheel left button (only present on some mice).

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_WHEEL_RIGHT** = `7`

Mouse wheel right button (only present on some mice).

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_XBUTTON1}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_XBUTTON1** = `8`

Extra mouse button 1. This is sometimes present, usually to the sides of
the mouse.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_XBUTTON2}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_XBUTTON2** = `9`

Extra mouse button 2. This is sometimes present, usually to the sides of
the mouse.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_MouseButtonMask}
::: rst-class
classref-enumeration
:::
::::

flags **MouseButtonMask**:
`🔗<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_MASK_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_MASK_LEFT** = `1`

Primary mouse button mask, usually for the left button.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_MASK_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_MASK_RIGHT** = `2`

Secondary mouse button mask, usually for the right button.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_MASK_MIDDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_MASK_MIDDLE** = `4`

Middle mouse button mask.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_MASK_MB_XBUTTON1}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_MASK_MB_XBUTTON1** = `128`

Extra mouse button 1 mask.

:::: {#class_@GlobalScope_constant_MOUSE_BUTTON_MASK_MB_XBUTTON2}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
role="ref"} **MOUSE_BUTTON_MASK_MB_XBUTTON2** = `256`

Extra mouse button 2 mask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_JoyButton}
::: rst-class
classref-enumeration
:::
::::

enum **JoyButton**: `🔗<enum_@GlobalScope_JoyButton>`{.interpreted-text
role="ref"}

:::: {#class_@GlobalScope_constant_JOY_BUTTON_INVALID}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_INVALID** = `-1`

An invalid game controller button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_A}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_A** = `0`

Game controller SDL button A. Corresponds to the bottom action button:
Sony Cross, Xbox A, Nintendo B.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_B}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_B** = `1`

Game controller SDL button B. Corresponds to the right action button:
Sony Circle, Xbox B, Nintendo A.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_X}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_X** = `2`

Game controller SDL button X. Corresponds to the left action button:
Sony Square, Xbox X, Nintendo Y.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_Y** = `3`

Game controller SDL button Y. Corresponds to the top action button: Sony
Triangle, Xbox Y, Nintendo X.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_BACK}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_BACK** = `4`

Game controller SDL back button. Corresponds to the Sony Select, Xbox
Back, Nintendo - button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_GUIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_GUIDE** = `5`

Game controller SDL guide button. Corresponds to the Sony PS, Xbox Home
button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_START}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_START** = `6`

Game controller SDL start button. Corresponds to the Sony Options, Xbox
Menu, Nintendo + button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_LEFT_STICK}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_LEFT_STICK** = `7`

Game controller SDL left stick button. Corresponds to the Sony L3, Xbox
L/LS button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_RIGHT_STICK}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_RIGHT_STICK** = `8`

Game controller SDL right stick button. Corresponds to the Sony R3, Xbox
R/RS button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_LEFT_SHOULDER}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_LEFT_SHOULDER** = `9`

Game controller SDL left shoulder button. Corresponds to the Sony L1,
Xbox LB button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_RIGHT_SHOULDER}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_RIGHT_SHOULDER** = `10`

Game controller SDL right shoulder button. Corresponds to the Sony R1,
Xbox RB button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_DPAD_UP}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_DPAD_UP** = `11`

Game controller D-pad up button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_DPAD_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_DPAD_DOWN** = `12`

Game controller D-pad down button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_DPAD_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_DPAD_LEFT** = `13`

Game controller D-pad left button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_DPAD_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_DPAD_RIGHT** = `14`

Game controller D-pad right button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_MISC1}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_MISC1** = `15`

Game controller SDL miscellaneous button. Corresponds to Xbox share
button, PS5 microphone button, Nintendo Switch capture button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_PADDLE1}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_PADDLE1** = `16`

Game controller SDL paddle 1 button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_PADDLE2}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_PADDLE2** = `17`

Game controller SDL paddle 2 button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_PADDLE3}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_PADDLE3** = `18`

Game controller SDL paddle 3 button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_PADDLE4}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_PADDLE4** = `19`

Game controller SDL paddle 4 button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_TOUCHPAD}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_TOUCHPAD** = `20`

Game controller SDL touchpad button.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_SDL_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_SDL_MAX** = `21`

The number of SDL game controller buttons.

:::: {#class_@GlobalScope_constant_JOY_BUTTON_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"}
**JOY_BUTTON_MAX** = `128`

The maximum number of game controller buttons supported by the engine.
The actual limit may be lower on specific platforms:

- **Android:** Up to 36 buttons.
- **Linux:** Up to 80 buttons.
- **Windows** and **macOS:** Up to 128 buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_JoyAxis}
::: rst-class
classref-enumeration
:::
::::

enum **JoyAxis**: `🔗<enum_@GlobalScope_JoyAxis>`{.interpreted-text
role="ref"}

:::: {#class_@GlobalScope_constant_JOY_AXIS_INVALID}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**JOY_AXIS_INVALID** = `-1`

An invalid game controller axis.

:::: {#class_@GlobalScope_constant_JOY_AXIS_LEFT_X}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**JOY_AXIS_LEFT_X** = `0`

Game controller left joystick x-axis.

:::: {#class_@GlobalScope_constant_JOY_AXIS_LEFT_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**JOY_AXIS_LEFT_Y** = `1`

Game controller left joystick y-axis.

:::: {#class_@GlobalScope_constant_JOY_AXIS_RIGHT_X}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**JOY_AXIS_RIGHT_X** = `2`

Game controller right joystick x-axis.

:::: {#class_@GlobalScope_constant_JOY_AXIS_RIGHT_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**JOY_AXIS_RIGHT_Y** = `3`

Game controller right joystick y-axis.

:::: {#class_@GlobalScope_constant_JOY_AXIS_TRIGGER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**JOY_AXIS_TRIGGER_LEFT** = `4`

Game controller left trigger axis.

:::: {#class_@GlobalScope_constant_JOY_AXIS_TRIGGER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**JOY_AXIS_TRIGGER_RIGHT** = `5`

Game controller right trigger axis.

:::: {#class_@GlobalScope_constant_JOY_AXIS_SDL_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**JOY_AXIS_SDL_MAX** = `6`

The number of SDL game controller axes.

:::: {#class_@GlobalScope_constant_JOY_AXIS_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text role="ref"}
**JOY_AXIS_MAX** = `10`

The maximum number of game controller axes: OpenVR supports up to 5
Joysticks making a total of 10 axes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_MIDIMessage}
::: rst-class
classref-enumeration
:::
::::

enum **MIDIMessage**:
`🔗<enum_@GlobalScope_MIDIMessage>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_NONE** = `0`

Does not correspond to any MIDI message. This is the default value of
`InputEventMIDI.message<class_InputEventMIDI_property_message>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_NOTE_OFF}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_NOTE_OFF** = `8`

MIDI message sent when a note is released.

\*\*Note:\*\* Not all MIDI devices send this message; some may send
`MIDI_MESSAGE_NOTE_ON<class_@GlobalScope_constant_MIDI_MESSAGE_NOTE_ON>`{.interpreted-text
role="ref"} with
`InputEventMIDI.velocity<class_InputEventMIDI_property_velocity>`{.interpreted-text
role="ref"} set to `0`.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_NOTE_ON}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_NOTE_ON** = `9`

MIDI message sent when a note is pressed.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_AFTERTOUCH}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_AFTERTOUCH** = `10`

MIDI message sent to indicate a change in pressure while a note is being
pressed down, also called aftertouch.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_CONTROL_CHANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_CONTROL_CHANGE** = `11`

MIDI message sent when a controller value changes. In a MIDI device, a
controller is any input that doesn\'t play notes. These may include
sliders for volume, balance, and panning, as well as switches and
pedals. See the [General MIDI
specification](https://en.wikipedia.org/wiki/General_MIDI#Controller_events)
for a small list.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_PROGRAM_CHANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_PROGRAM_CHANGE** = `12`

MIDI message sent when the MIDI device changes its current instrument
(also called *program* or *preset*).

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_CHANNEL_PRESSURE}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_CHANNEL_PRESSURE** = `13`

MIDI message sent to indicate a change in pressure for the whole
channel. Some MIDI devices may send this instead of
`MIDI_MESSAGE_AFTERTOUCH<class_@GlobalScope_constant_MIDI_MESSAGE_AFTERTOUCH>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_PITCH_BEND}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_PITCH_BEND** = `14`

MIDI message sent when the value of the pitch bender changes, usually a
wheel on the MIDI device.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_SYSTEM_EXCLUSIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_SYSTEM_EXCLUSIVE** = `240`

MIDI system exclusive (SysEx) message. This type of message is not
standardized and it\'s highly dependent on the MIDI device sending it.

\*\*Note:\*\* Getting this message\'s data from
`InputEventMIDI<class_InputEventMIDI>`{.interpreted-text role="ref"} is
not implemented.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_QUARTER_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_QUARTER_FRAME** = `241`

MIDI message sent every quarter frame to keep connected MIDI devices
synchronized. Related to
`MIDI_MESSAGE_TIMING_CLOCK<class_@GlobalScope_constant_MIDI_MESSAGE_TIMING_CLOCK>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Getting this message\'s data from
`InputEventMIDI<class_InputEventMIDI>`{.interpreted-text role="ref"} is
not implemented.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_SONG_POSITION_POINTER}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_SONG_POSITION_POINTER** = `242`

MIDI message sent to jump onto a new position in the current sequence or
song.

\*\*Note:\*\* Getting this message\'s data from
`InputEventMIDI<class_InputEventMIDI>`{.interpreted-text role="ref"} is
not implemented.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_SONG_SELECT}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_SONG_SELECT** = `243`

MIDI message sent to select a sequence or song to play.

\*\*Note:\*\* Getting this message\'s data from
`InputEventMIDI<class_InputEventMIDI>`{.interpreted-text role="ref"} is
not implemented.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_TUNE_REQUEST}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_TUNE_REQUEST** = `246`

MIDI message sent to request a tuning calibration. Used on analog
synthesizers. Most modern MIDI devices do not need this message.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_TIMING_CLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_TIMING_CLOCK** = `248`

MIDI message sent 24 times after
`MIDI_MESSAGE_QUARTER_FRAME<class_@GlobalScope_constant_MIDI_MESSAGE_QUARTER_FRAME>`{.interpreted-text
role="ref"}, to keep connected MIDI devices synchronized.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_START}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_START** = `250`

MIDI message sent to start the current sequence or song from the
beginning.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_CONTINUE}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_CONTINUE** = `251`

MIDI message sent to resume from the point the current sequence or song
was paused.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_STOP}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_STOP** = `252`

MIDI message sent to pause the current sequence or song.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_ACTIVE_SENSING}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_ACTIVE_SENSING** = `254`

MIDI message sent repeatedly while the MIDI device is idle, to tell the
receiver that the connection is alive. Most MIDI devices do not send
this message.

:::: {#class_@GlobalScope_constant_MIDI_MESSAGE_SYSTEM_RESET}
::: rst-class
classref-enumeration-constant
:::
::::

`MIDIMessage<enum_@GlobalScope_MIDIMessage>`{.interpreted-text
role="ref"} **MIDI_MESSAGE_SYSTEM_RESET** = `255`

MIDI message sent to reset a MIDI device to its default state, as if it
was just turned on. It should not be sent when the MIDI device is being
turned on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_Error}
::: rst-class
classref-enumeration
:::
::::

enum **Error**: `🔗<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"}

:::: {#class_@GlobalScope_constant_OK}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} **OK** =
`0`

Methods that return `Error<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"} return
`OK<class_@GlobalScope_constant_OK>`{.interpreted-text role="ref"} when
no error occurred.

Since `OK<class_@GlobalScope_constant_OK>`{.interpreted-text role="ref"}
has value `0`, and all other error constants are positive integers, it
can also be used in boolean checks.

    var error = method_that_returns_error()
    if error != OK:
        printerr("Failure!")

    # Or, alternatively:
    if error:
        printerr("Still failing!")

\*\*Note:\*\* Many functions do not return an error code, but will print
error messages to standard output.

:::: {#class_@GlobalScope_constant_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**FAILED** = `1`

Generic error.

:::: {#class_@GlobalScope_constant_ERR_UNAVAILABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_UNAVAILABLE** = `2`

Unavailable error.

:::: {#class_@GlobalScope_constant_ERR_UNCONFIGURED}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_UNCONFIGURED** = `3`

Unconfigured error.

:::: {#class_@GlobalScope_constant_ERR_UNAUTHORIZED}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_UNAUTHORIZED** = `4`

Unauthorized error.

:::: {#class_@GlobalScope_constant_ERR_PARAMETER_RANGE_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_PARAMETER_RANGE_ERROR** = `5`

Parameter range error.

:::: {#class_@GlobalScope_constant_ERR_OUT_OF_MEMORY}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_OUT_OF_MEMORY** = `6`

Out of memory (OOM) error.

:::: {#class_@GlobalScope_constant_ERR_FILE_NOT_FOUND}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_NOT_FOUND** = `7`

File: Not found error.

:::: {#class_@GlobalScope_constant_ERR_FILE_BAD_DRIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_BAD_DRIVE** = `8`

File: Bad drive error.

:::: {#class_@GlobalScope_constant_ERR_FILE_BAD_PATH}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_BAD_PATH** = `9`

File: Bad path error.

:::: {#class_@GlobalScope_constant_ERR_FILE_NO_PERMISSION}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_NO_PERMISSION** = `10`

File: No permission error.

:::: {#class_@GlobalScope_constant_ERR_FILE_ALREADY_IN_USE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_ALREADY_IN_USE** = `11`

File: Already in use error.

:::: {#class_@GlobalScope_constant_ERR_FILE_CANT_OPEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_CANT_OPEN** = `12`

File: Can\'t open error.

:::: {#class_@GlobalScope_constant_ERR_FILE_CANT_WRITE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_CANT_WRITE** = `13`

File: Can\'t write error.

:::: {#class_@GlobalScope_constant_ERR_FILE_CANT_READ}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_CANT_READ** = `14`

File: Can\'t read error.

:::: {#class_@GlobalScope_constant_ERR_FILE_UNRECOGNIZED}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_UNRECOGNIZED** = `15`

File: Unrecognized error.

:::: {#class_@GlobalScope_constant_ERR_FILE_CORRUPT}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_CORRUPT** = `16`

File: Corrupt error.

:::: {#class_@GlobalScope_constant_ERR_FILE_MISSING_DEPENDENCIES}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_MISSING_DEPENDENCIES** = `17`

File: Missing dependencies error.

:::: {#class_@GlobalScope_constant_ERR_FILE_EOF}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_FILE_EOF** = `18`

File: End of file (EOF) error.

:::: {#class_@GlobalScope_constant_ERR_CANT_OPEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_CANT_OPEN** = `19`

Can\'t open error.

:::: {#class_@GlobalScope_constant_ERR_CANT_CREATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_CANT_CREATE** = `20`

Can\'t create error.

:::: {#class_@GlobalScope_constant_ERR_QUERY_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_QUERY_FAILED** = `21`

Query failed error.

:::: {#class_@GlobalScope_constant_ERR_ALREADY_IN_USE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_ALREADY_IN_USE** = `22`

Already in use error.

:::: {#class_@GlobalScope_constant_ERR_LOCKED}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_LOCKED** = `23`

Locked error.

:::: {#class_@GlobalScope_constant_ERR_TIMEOUT}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_TIMEOUT** = `24`

Timeout error.

:::: {#class_@GlobalScope_constant_ERR_CANT_CONNECT}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_CANT_CONNECT** = `25`

Can\'t connect error.

:::: {#class_@GlobalScope_constant_ERR_CANT_RESOLVE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_CANT_RESOLVE** = `26`

Can\'t resolve error.

:::: {#class_@GlobalScope_constant_ERR_CONNECTION_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_CONNECTION_ERROR** = `27`

Connection error.

:::: {#class_@GlobalScope_constant_ERR_CANT_ACQUIRE_RESOURCE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_CANT_ACQUIRE_RESOURCE** = `28`

Can\'t acquire resource error.

:::: {#class_@GlobalScope_constant_ERR_CANT_FORK}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_CANT_FORK** = `29`

Can\'t fork process error.

:::: {#class_@GlobalScope_constant_ERR_INVALID_DATA}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_INVALID_DATA** = `30`

Invalid data error.

:::: {#class_@GlobalScope_constant_ERR_INVALID_PARAMETER}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_INVALID_PARAMETER** = `31`

Invalid parameter error.

:::: {#class_@GlobalScope_constant_ERR_ALREADY_EXISTS}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_ALREADY_EXISTS** = `32`

Already exists error.

:::: {#class_@GlobalScope_constant_ERR_DOES_NOT_EXIST}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_DOES_NOT_EXIST** = `33`

Does not exist error.

:::: {#class_@GlobalScope_constant_ERR_DATABASE_CANT_READ}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_DATABASE_CANT_READ** = `34`

Database: Read error.

:::: {#class_@GlobalScope_constant_ERR_DATABASE_CANT_WRITE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_DATABASE_CANT_WRITE** = `35`

Database: Write error.

:::: {#class_@GlobalScope_constant_ERR_COMPILATION_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_COMPILATION_FAILED** = `36`

Compilation failed error.

:::: {#class_@GlobalScope_constant_ERR_METHOD_NOT_FOUND}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_METHOD_NOT_FOUND** = `37`

Method not found error.

:::: {#class_@GlobalScope_constant_ERR_LINK_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_LINK_FAILED** = `38`

Linking failed error.

:::: {#class_@GlobalScope_constant_ERR_SCRIPT_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_SCRIPT_FAILED** = `39`

Script failed error.

:::: {#class_@GlobalScope_constant_ERR_CYCLIC_LINK}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_CYCLIC_LINK** = `40`

Cycling link (import cycle) error.

:::: {#class_@GlobalScope_constant_ERR_INVALID_DECLARATION}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_INVALID_DECLARATION** = `41`

Invalid declaration error.

:::: {#class_@GlobalScope_constant_ERR_DUPLICATE_SYMBOL}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_DUPLICATE_SYMBOL** = `42`

Duplicate symbol error.

:::: {#class_@GlobalScope_constant_ERR_PARSE_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_PARSE_ERROR** = `43`

Parse error.

:::: {#class_@GlobalScope_constant_ERR_BUSY}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_BUSY** = `44`

Busy error.

:::: {#class_@GlobalScope_constant_ERR_SKIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_SKIP** = `45`

Skip error.

:::: {#class_@GlobalScope_constant_ERR_HELP}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_HELP** = `46`

Help error. Used internally when passing `--version` or `--help` as
executable options.

:::: {#class_@GlobalScope_constant_ERR_BUG}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_BUG** = `47`

Bug error, caused by an implementation issue in the method.

\*\*Note:\*\* If a built-in method returns this code, please open an
issue on [the GitHub Issue
Tracker](https://github.com/godotengine/godot/issues).

:::: {#class_@GlobalScope_constant_ERR_PRINTER_ON_FIRE}
::: rst-class
classref-enumeration-constant
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ERR_PRINTER_ON_FIRE** = `48`

Printer on fire error (This is an easter egg, no built-in methods return
this error code).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_PropertyHint}
::: rst-class
classref-enumeration
:::
::::

enum **PropertyHint**:
`🔗<enum_@GlobalScope_PropertyHint>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_NONE** = `0`

The property has no hint for the editor.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_RANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_RANGE** = `1`

Hints that an `int<class_int>`{.interpreted-text role="ref"} or
`float<class_float>`{.interpreted-text role="ref"} property should be
within a range specified via the hint string `"min,max"` or
`"min,max,step"`. The hint string can optionally include `"or_greater"`
and/or `"or_less"` to allow manual input going respectively above the
max or below the min values.

\*\*Example:\*\* `"-360,360,1,or_greater,or_less"`.

Additionally, other keywords can be included: `"exp"` for exponential
range editing, `"radians_as_degrees"` for editing radian angles in
degrees (the range values are also in degrees), `"degrees"` to hint at
an angle and `"hide_slider"` to hide the slider.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_ENUM}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_ENUM** = `2`

Hints that an `int<class_int>`{.interpreted-text role="ref"} or
`String<class_String>`{.interpreted-text role="ref"} property is an
enumerated value to pick in a list specified via a hint string.

The hint string is a comma separated list of names such as
`"Hello,Something,Else"`. Whitespaces are **not** removed from either
end of a name. For integer properties, the first name in the list has
value 0, the next 1, and so on. Explicit values can also be specified by
appending `:integer` to the name, e.g. `"Zero,One,Three:3,Four,Six:6"`.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_ENUM_SUGGESTION}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_ENUM_SUGGESTION** = `3`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property can be an enumerated value to pick in a list specified via a
hint string such as `"Hello,Something,Else"`.

Unlike
`PROPERTY_HINT_ENUM<class_@GlobalScope_constant_PROPERTY_HINT_ENUM>`{.interpreted-text
role="ref"}, a property with this hint still accepts arbitrary values
and can be empty. The list of values serves to suggest possible values.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_EXP_EASING}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_EXP_EASING** = `4`

Hints that a `float<class_float>`{.interpreted-text role="ref"} property
should be edited via an exponential easing function. The hint string can
include `"attenuation"` to flip the curve horizontally and/or
`"positive_only"` to exclude in/out easing and limit values to be
greater than or equal to zero.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LINK}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LINK** = `5`

Hints that a vector property should allow its components to be linked.
For example, this allows
`Vector2.x<class_Vector2_property_x>`{.interpreted-text role="ref"} and
`Vector2.y<class_Vector2_property_y>`{.interpreted-text role="ref"} to
be edited together.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_FLAGS}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_FLAGS** = `6`

Hints that an `int<class_int>`{.interpreted-text role="ref"} property is
a bitmask with named bit flags.

The hint string is a comma separated list of names such as
`"Bit0,Bit1,Bit2,Bit3"`. Whitespaces are **not** removed from either end
of a name. The first name in the list has value 1, the next 2, then 4,
8, 16 and so on. Explicit values can also be specified by appending
`:integer` to the name, e.g. `"A:4,B:8,C:16"`. You can also combine
several flags (`"A:4,B:8,AB:12,C:16"`).

\*\*Note:\*\* A flag value must be at least `1` and at most
`2 ** 32 - 1`.

\*\*Note:\*\* Unlike
`PROPERTY_HINT_ENUM<class_@GlobalScope_constant_PROPERTY_HINT_ENUM>`{.interpreted-text
role="ref"}, the previous explicit value is not taken into account. For
the hint `"A:16,B,C"`, A is 16, B is 2, C is 4.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_2D_RENDER}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LAYERS_2D_RENDER** = `7`

Hints that an `int<class_int>`{.interpreted-text role="ref"} property is
a bitmask using the optionally named 2D render layers.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_2D_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LAYERS_2D_PHYSICS** = `8`

Hints that an `int<class_int>`{.interpreted-text role="ref"} property is
a bitmask using the optionally named 2D physics layers.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_2D_NAVIGATION}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LAYERS_2D_NAVIGATION** = `9`

Hints that an `int<class_int>`{.interpreted-text role="ref"} property is
a bitmask using the optionally named 2D navigation layers.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_3D_RENDER}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LAYERS_3D_RENDER** = `10`

Hints that an `int<class_int>`{.interpreted-text role="ref"} property is
a bitmask using the optionally named 3D render layers.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_3D_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LAYERS_3D_PHYSICS** = `11`

Hints that an `int<class_int>`{.interpreted-text role="ref"} property is
a bitmask using the optionally named 3D physics layers.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_3D_NAVIGATION}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LAYERS_3D_NAVIGATION** = `12`

Hints that an `int<class_int>`{.interpreted-text role="ref"} property is
a bitmask using the optionally named 3D navigation layers.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LAYERS_AVOIDANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LAYERS_AVOIDANCE** = `37`

Hints that an integer property is a bitmask using the optionally named
avoidance layers.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_FILE** = `13`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property is a path to a file. Editing it will show a file dialog for
picking the path. The hint string can be a set of filters with wildcards
like `"*.png,*.jpg"`. By default the file will be stored as UID whenever
available. You can use
`ResourceUID<class_ResourceUID>`{.interpreted-text role="ref"} methods
to convert it back to path. For storing a raw path, use
`PROPERTY_HINT_FILE_PATH<class_@GlobalScope_constant_PROPERTY_HINT_FILE_PATH>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_DIR}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_DIR** = `14`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property is a path to a directory. Editing it will show a file dialog
for picking the path.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_GLOBAL_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_GLOBAL_FILE** = `15`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property is an absolute path to a file outside the project folder.
Editing it will show a file dialog for picking the path. The hint string
can be a set of filters with wildcards, like `"*.png,*.jpg"`.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_GLOBAL_DIR}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_GLOBAL_DIR** = `16`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property is an absolute path to a directory outside the project folder.
Editing it will show a file dialog for picking the path.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_RESOURCE_TYPE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_RESOURCE_TYPE** = `17`

Hints that a property is an instance of a
`Resource<class_Resource>`{.interpreted-text role="ref"}-derived type,
optionally specified via the hint string (e.g. `"Texture2D"`). Editing
it will show a popup menu of valid resource types to instantiate.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_MULTILINE_TEXT}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_MULTILINE_TEXT** = `18`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property is text with line breaks. Editing it will show a text input
field where line breaks can be typed.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_EXPRESSION}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_EXPRESSION** = `19`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property is an `Expression<class_Expression>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_PLACEHOLDER_TEXT}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_PLACEHOLDER_TEXT** = `20`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property should show a placeholder text on its input field, if empty.
The hint string is the placeholder text to use.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_COLOR_NO_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_COLOR_NO_ALPHA** = `21`

Hints that a `Color<class_Color>`{.interpreted-text role="ref"} property
should be edited without affecting its transparency
(`Color.a<class_Color_property_a>`{.interpreted-text role="ref"} is not
editable).

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_OBJECT_ID}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_OBJECT_ID** = `22`

Hints that the property\'s value is an object encoded as object ID, with
its type specified in the hint string. Used by the debugger.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_TYPE_STRING}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_TYPE_STRING** = `23`

If a property is `String<class_String>`{.interpreted-text role="ref"},
hints that the property represents a particular type (class). This
allows to select a type from the create dialog. The property will store
the selected type as a string.

If a property is `Array<class_Array>`{.interpreted-text role="ref"},
hints the editor how to show elements. The `hint_string` must encode
nested types using `":"` and `"/"`.

If a property is `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}, hints the editor how to show elements. The `hint_string` is
the same as `Array<class_Array>`{.interpreted-text role="ref"}, with a
`";"` separating the key and value.

::::: tabs
::: code-tab
gdscript

\# Array of elem_type. hint_string = \"%d:\" % \[elem_type\] hint_string
= \"%d/%d:%s\" % \[elem_type, elem_hint, elem_hint_string\] \#
Two-dimensional array of elem_type (array of arrays of elem_type).
hint_string = \"%d:%d:\" % \[TYPE_ARRAY, elem_type\] hint_string =
\"%d:%d/%d:%s\" % \[TYPE_ARRAY, elem_type, elem_hint, elem_hint_string\]
\# Three-dimensional array of elem_type (array of arrays of arrays of
elem_type). hint_string = \"%d:%d:%d:\" % \[TYPE_ARRAY, TYPE_ARRAY,
elem_type\] hint_string = \"%d:%d:%d/%d:%s\" % \[TYPE_ARRAY, TYPE_ARRAY,
elem_type, elem_hint, elem_hint_string\]
:::

::: code-tab
csharp

// Array of elemType. hintString = \$\"{elemType:D}:\"; hintString =
\$\"{elemType:}/{elemHint:D}:{elemHintString}\"; // Two-dimensional
array of elemType (array of arrays of elemType). hintString =
\$\"{Variant.Type.Array:D}:{elemType:D}:\"; hintString =
\$\"{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}\";
// Three-dimensional array of elemType (array of arrays of arrays of
elemType). hintString =
\$\"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}:\";
hintString =
\$\"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}\";
:::
:::::

\*\*Examples:\*\*

::::: tabs
::: code-tab
gdscript

hint_string = \"%d:\" % \[TYPE_INT\] \# Array of integers. hint_string =
\"%d/%d:1,10,1\" % \[TYPE_INT, PROPERTY_HINT_RANGE\] \# Array of
integers (in range from 1 to 10). hint_string = \"%d/%d:Zero,One,Two\" %
\[TYPE_INT, PROPERTY_HINT_ENUM\] \# Array of integers (an enum).
hint_string = \"%d/%d:Zero,One,Three:3,Six:6\" % \[TYPE_INT,
PROPERTY_HINT_ENUM\] \# Array of integers (an enum). hint_string =
\"%d/%d:\*.png\" % \[TYPE_STRING, PROPERTY_HINT_FILE\] \# Array of
strings (file paths). hint_string = \"%d/%d:Texture2D\" % \[TYPE_OBJECT,
PROPERTY_HINT_RESOURCE_TYPE\] \# Array of textures.

hint_string = \"%d:%d:\" % \[TYPE_ARRAY, TYPE_FLOAT\] \# Two-dimensional
array of floats. hint_string = \"%d:%d/%d:\" % \[TYPE_ARRAY,
TYPE_STRING, PROPERTY_HINT_MULTILINE_TEXT\] \# Two-dimensional array of
multiline strings. hint_string = \"%d:%d/%d:-1,1,0.1\" % \[TYPE_ARRAY,
TYPE_FLOAT, PROPERTY_HINT_RANGE\] \# Two-dimensional array of floats (in
range from -1 to 1). hint_string = \"%d:%d/%d:Texture2D\" %
\[TYPE_ARRAY, TYPE_OBJECT, PROPERTY_HINT_RESOURCE_TYPE\] \#
Two-dimensional array of textures.
:::

::: code-tab
csharp

hintString = \$\"{Variant.Type.Int:D}/{PropertyHint.Range:D}:1,10,1\";
// Array of integers (in range from 1 to 10). hintString =
\$\"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Two\"; // Array
of integers (an enum). hintString =
\$\"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Three:3,Six:6\";
// Array of integers (an enum). hintString =
\$\"{Variant.Type.String:D}/{PropertyHint.File:D}:\*.png\"; // Array of
strings (file paths). hintString =
\$\"{Variant.Type.Object:D}/{PropertyHint.ResourceType:D}:Texture2D\";
// Array of textures.

hintString = \$\"{Variant.Type.Array:D}:{Variant.Type.Float:D}:\"; //
Two-dimensional array of floats. hintString =
\$\"{Variant.Type.Array:D}:{Variant.Type.String:D}/{PropertyHint.MultilineText:D}:\";
// Two-dimensional array of multiline strings. hintString =
\$\"{Variant.Type.Array:D}:{Variant.Type.Float:D}/{PropertyHint.Range:D}:-1,1,0.1\";
// Two-dimensional array of floats (in range from -1 to 1). hintString =
\$\"{Variant.Type.Array:D}:{Variant.Type.Object:D}/{PropertyHint.ResourceType:D}:Texture2D\";
// Two-dimensional array of textures.
:::
:::::

\*\*Note:\*\* The trailing colon is required for properly detecting
built-in types.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_NODE_PATH_TO_EDITED_NODE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_NODE_PATH_TO_EDITED_NODE** = `24`

**Deprecated:** This hint is not used by the engine.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_OBJECT_TOO_BIG}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_OBJECT_TOO_BIG** = `25`

Hints that an object is too big to be sent via the debugger.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_NODE_PATH_VALID_TYPES}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_NODE_PATH_VALID_TYPES** = `26`

Hints that the hint string specifies valid node types for property of
type `NodePath<class_NodePath>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_SAVE_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_SAVE_FILE** = `27`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property is a path to a file. Editing it will show a file dialog for
picking the path for the file to be saved at. The dialog has access to
the project\'s directory. The hint string can be a set of filters with
wildcards like `"*.png,*.jpg"`. See also
`FileDialog.filters<class_FileDialog_property_filters>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_GLOBAL_SAVE_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_GLOBAL_SAVE_FILE** = `28`

Hints that a `String<class_String>`{.interpreted-text role="ref"}
property is a path to a file. Editing it will show a file dialog for
picking the path for the file to be saved at. The dialog has access to
the entire filesystem. The hint string can be a set of filters with
wildcards like `"*.png,*.jpg"`. See also
`FileDialog.filters<class_FileDialog_property_filters>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_INT_IS_OBJECTID}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_INT_IS_OBJECTID** = `29`

**Deprecated:** This hint is not used by the engine.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_INT_IS_POINTER}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_INT_IS_POINTER** = `30`

Hints that an `int<class_int>`{.interpreted-text role="ref"} property is
a pointer. Used by GDExtension.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_ARRAY_TYPE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_ARRAY_TYPE** = `31`

Hints that a property is an `Array<class_Array>`{.interpreted-text
role="ref"} with the stored type specified in the hint string. The hint
string contains the type of the array (e.g. `"String"`).

Use the hint string format from
`PROPERTY_HINT_TYPE_STRING<class_@GlobalScope_constant_PROPERTY_HINT_TYPE_STRING>`{.interpreted-text
role="ref"} for more control over the stored type.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_DICTIONARY_TYPE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_DICTIONARY_TYPE** = `38`

Hints that a property is a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
stored types specified in the hint string. The hint string contains the
key and value types separated by a semicolon (e.g. `"int;String"`).

Use the hint string format from
`PROPERTY_HINT_TYPE_STRING<class_@GlobalScope_constant_PROPERTY_HINT_TYPE_STRING>`{.interpreted-text
role="ref"} for more control over the stored types.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LOCALE_ID}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LOCALE_ID** = `32`

Hints that a string property is a locale code. Editing it will show a
locale dialog for picking language and country.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_LOCALIZABLE_STRING}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_LOCALIZABLE_STRING** = `33`

Hints that a dictionary property is string translation map. Dictionary
keys are locale codes and, values are translated strings.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_NODE_TYPE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_NODE_TYPE** = `34`

Hints that a property is an instance of a
`Node<class_Node>`{.interpreted-text role="ref"}-derived type,
optionally specified via the hint string (e.g. `"Node2D"`). Editing it
will show a dialog for picking a node from the scene.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_HIDE_QUATERNION_EDIT}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_HIDE_QUATERNION_EDIT** = `35`

Hints that a quaternion property should disable the temporary euler
editor.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_PASSWORD}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_PASSWORD** = `36`

Hints that a string property is a password, and every character is
replaced with the secret character.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_TOOL_BUTTON}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_TOOL_BUTTON** = `39`

Hints that a `Callable<class_Callable>`{.interpreted-text role="ref"}
property should be displayed as a clickable button. When the button is
pressed, the callable is called. The hint string specifies the button
text and optionally an icon from the `"EditorIcons"` theme type.

``` text
"Click me!" - A button with the text "Click me!" and the default "Callable" icon.
"Click me!,ColorRect" - A button with the text "Click me!" and the "ColorRect" icon.
```

\*\*Note:\*\* A `Callable<class_Callable>`{.interpreted-text role="ref"}
cannot be properly serialized and stored in a file, so it is recommended
to use
`PROPERTY_USAGE_EDITOR<class_@GlobalScope_constant_PROPERTY_USAGE_EDITOR>`{.interpreted-text
role="ref"} instead of
`PROPERTY_USAGE_DEFAULT<class_@GlobalScope_constant_PROPERTY_USAGE_DEFAULT>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_ONESHOT}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_ONESHOT** = `40`

Hints that a property will be changed on its own after setting, such as
`AudioStreamPlayer.playing<class_AudioStreamPlayer_property_playing>`{.interpreted-text
role="ref"} or
`GPUParticles3D.emitting<class_GPUParticles3D_property_emitting>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_GROUP_ENABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_GROUP_ENABLE** = `42`

Hints that a boolean property will enable the feature associated with
the group that it occurs in. The property will be displayed as a
checkbox on the group header. Only works within a group or subgroup.

By default, disabling the property hides all properties in the group.
Use the optional hint string `"checkbox_only"` to disable this behavior.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_INPUT_NAME}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_INPUT_NAME** = `43`

Hints that a `String<class_String>`{.interpreted-text role="ref"} or
`StringName<class_StringName>`{.interpreted-text role="ref"} property is
the name of an input action. This allows the selection of any action
name from the Input Map in the Project Settings. The hint string may
contain two options separated by commas:

- If it contains `"show_builtin"`, built-in input actions are included
  in the selection.
- If it contains `"loose_mode"`, loose mode is enabled. This allows
  inserting any action name even if it\'s not present in the input map.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_FILE_PATH}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_FILE_PATH** = `44`

Like
`PROPERTY_HINT_FILE<class_@GlobalScope_constant_PROPERTY_HINT_FILE>`{.interpreted-text
role="ref"}, but the property is stored as a raw path, not UID. That
means the reference will be broken if you move the file. Consider using
`PROPERTY_HINT_FILE<class_@GlobalScope_constant_PROPERTY_HINT_FILE>`{.interpreted-text
role="ref"} when possible.

:::: {#class_@GlobalScope_constant_PROPERTY_HINT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} **PROPERTY_HINT_MAX** = `45`

Represents the size of the
`PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_PropertyUsageFlags}
::: rst-class
classref-enumeration
:::
::::

flags **PropertyUsageFlags**:
`🔗<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_NONE** = `0`

The property is not stored, and does not display in the editor. This is
the default for non-exported properties.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_STORAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_STORAGE** = `2`

The property is serialized and saved in the scene file (default for
exported properties).

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_EDITOR}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_EDITOR** = `4`

The property is shown in the
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}
(default for exported properties).

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_INTERNAL}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_INTERNAL** = `8`

The property is excluded from the class reference.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_CHECKABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_CHECKABLE** = `16`

The property can be checked in the
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_CHECKED}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_CHECKED** = `32`

The property is checked in the
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_GROUP}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_GROUP** = `64`

Used to group properties together in the editor. See
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_CATEGORY}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_CATEGORY** = `128`

Used to categorize properties together in the editor.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_SUBGROUP}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_SUBGROUP** = `256`

Used to group properties together in the editor in a subgroup (under a
group). See `EditorInspector<class_EditorInspector>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_CLASS_IS_BITFIELD}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_CLASS_IS_BITFIELD** = `512`

The property is a bitfield, i.e. it contains multiple flags represented
as bits.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_NO_INSTANCE_STATE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_NO_INSTANCE_STATE** = `1024`

The property does not save its state in
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_RESTART_IF_CHANGED}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_RESTART_IF_CHANGED** = `2048`

Editing the property prompts the user for restarting the editor.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_SCRIPT_VARIABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_SCRIPT_VARIABLE** = `4096`

The property is a script variable.
`PROPERTY_USAGE_SCRIPT_VARIABLE<class_@GlobalScope_constant_PROPERTY_USAGE_SCRIPT_VARIABLE>`{.interpreted-text
role="ref"} can be used to distinguish between exported script variables
from built-in variables (which don\'t have this usage flag). By default,
`PROPERTY_USAGE_SCRIPT_VARIABLE<class_@GlobalScope_constant_PROPERTY_USAGE_SCRIPT_VARIABLE>`{.interpreted-text
role="ref"} is **not** applied to variables that are created by
overriding
`Object._get_property_list()<class_Object_private_method__get_property_list>`{.interpreted-text
role="ref"} in a script.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_STORE_IF_NULL}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_STORE_IF_NULL** = `8192`

The property value of type `Object<class_Object>`{.interpreted-text
role="ref"} will be stored even if its value is `null`.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_UPDATE_ALL_IF_MODIFIED}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_UPDATE_ALL_IF_MODIFIED** = `16384`

If this property is modified, all inspector fields will be refreshed.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_SCRIPT_DEFAULT_VALUE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_SCRIPT_DEFAULT_VALUE** = `32768`

**Deprecated:** This flag is not used by the engine.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_CLASS_IS_ENUM}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_CLASS_IS_ENUM** = `65536`

The property is a variable of enum type, i.e. it only takes named
integer constants from its associated enumeration.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_NIL_IS_VARIANT}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_NIL_IS_VARIANT** = `131072`

If property has `nil` as default value, its type will be
`Variant<class_Variant>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_ARRAY** = `262144`

The property is an array.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_ALWAYS_DUPLICATE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_ALWAYS_DUPLICATE** = `524288`

When duplicating a resource with
`Resource.duplicate()<class_Resource_method_duplicate>`{.interpreted-text
role="ref"}, and this flag is set on a property of that resource, the
property should always be duplicated, regardless of the `subresources`
bool parameter.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_NEVER_DUPLICATE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_NEVER_DUPLICATE** = `1048576`

When duplicating a resource with
`Resource.duplicate()<class_Resource_method_duplicate>`{.interpreted-text
role="ref"}, and this flag is set on a property of that resource, the
property should never be duplicated, regardless of the `subresources`
bool parameter.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_HIGH_END_GFX}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_HIGH_END_GFX** = `2097152`

The property is only shown in the editor if modern renderers are
supported (the Compatibility rendering method is excluded).

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_NODE_PATH_FROM_SCENE_ROOT}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_NODE_PATH_FROM_SCENE_ROOT** = `4194304`

The `NodePath<class_NodePath>`{.interpreted-text role="ref"} property
will always be relative to the scene\'s root. Mostly useful for local
resources.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_RESOURCE_NOT_PERSISTENT}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_RESOURCE_NOT_PERSISTENT** = `8388608`

Use when a resource is created on the fly, i.e. the getter will always
return a different instance.
`ResourceSaver<class_ResourceSaver>`{.interpreted-text role="ref"} needs
this information to properly save such resources.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_KEYING_INCREMENTS}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_KEYING_INCREMENTS** = `16777216`

Inserting an animation key frame of this property will automatically
increment the value, allowing to easily keyframe multiple values in a
row.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_DEFERRED_SET_RESOURCE}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_DEFERRED_SET_RESOURCE** = `33554432`

**Deprecated:** This flag is not used by the engine.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_EDITOR_INSTANTIATE_OBJECT}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_EDITOR_INSTANTIATE_OBJECT** = `67108864`

When this property is a `Resource<class_Resource>`{.interpreted-text
role="ref"} and base object is a `Node<class_Node>`{.interpreted-text
role="ref"}, a resource instance will be automatically created whenever
the node is created in the editor.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_EDITOR_BASIC_SETTING}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_EDITOR_BASIC_SETTING** = `134217728`

The property is considered a basic setting and will appear even when
advanced mode is disabled. Used for project settings.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_READ_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_READ_ONLY** = `268435456`

The property is read-only in the
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_SECRET}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_SECRET** = `536870912`

An export preset property with this flag contains confidential
information and is stored separately from the rest of the export preset
configuration.

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_DEFAULT** = `6`

Default usage (storage and editor).

:::: {#class_@GlobalScope_constant_PROPERTY_USAGE_NO_EDITOR}
::: rst-class
classref-enumeration-constant
:::
::::

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
role="ref"} **PROPERTY_USAGE_NO_EDITOR** = `2`

Default usage but without showing the property in the editor (storage).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_MethodFlags}
::: rst-class
classref-enumeration
:::
::::

flags **MethodFlags**:
`🔗<enum_@GlobalScope_MethodFlags>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_METHOD_FLAG_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
role="ref"} **METHOD_FLAG_NORMAL** = `1`

Flag for a normal method.

:::: {#class_@GlobalScope_constant_METHOD_FLAG_EDITOR}
::: rst-class
classref-enumeration-constant
:::
::::

`MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
role="ref"} **METHOD_FLAG_EDITOR** = `2`

Flag for an editor method.

:::: {#class_@GlobalScope_constant_METHOD_FLAG_CONST}
::: rst-class
classref-enumeration-constant
:::
::::

`MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
role="ref"} **METHOD_FLAG_CONST** = `4`

Flag for a constant method.

:::: {#class_@GlobalScope_constant_METHOD_FLAG_VIRTUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
role="ref"} **METHOD_FLAG_VIRTUAL** = `8`

Flag for a virtual method.

:::: {#class_@GlobalScope_constant_METHOD_FLAG_VARARG}
::: rst-class
classref-enumeration-constant
:::
::::

`MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
role="ref"} **METHOD_FLAG_VARARG** = `16`

Flag for a method with a variable number of arguments.

:::: {#class_@GlobalScope_constant_METHOD_FLAG_STATIC}
::: rst-class
classref-enumeration-constant
:::
::::

`MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
role="ref"} **METHOD_FLAG_STATIC** = `32`

Flag for a static method.

:::: {#class_@GlobalScope_constant_METHOD_FLAG_OBJECT_CORE}
::: rst-class
classref-enumeration-constant
:::
::::

`MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
role="ref"} **METHOD_FLAG_OBJECT_CORE** = `64`

Used internally. Allows to not dump core virtual methods (such as
`Object._notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"}) to the JSON API.

:::: {#class_@GlobalScope_constant_METHOD_FLAG_VIRTUAL_REQUIRED}
::: rst-class
classref-enumeration-constant
:::
::::

`MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
role="ref"} **METHOD_FLAG_VIRTUAL_REQUIRED** = `128`

Flag for a virtual method that is required. In GDScript, this flag is
set for abstract functions.

:::: {#class_@GlobalScope_constant_METHOD_FLAGS_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`MethodFlags<enum_@GlobalScope_MethodFlags>`{.interpreted-text
role="ref"} **METHOD_FLAGS_DEFAULT** = `1`

Default method flags (normal).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_Variant.Type}
::: rst-class
classref-enumeration
:::
::::

enum **Variant.Type**:
`🔗<enum_@GlobalScope_Variant.Type>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_TYPE_NIL}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_NIL** = `0`

Variable is `null`.

:::: {#class_@GlobalScope_constant_TYPE_BOOL}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_BOOL** = `1`

Variable is of type `bool<class_bool>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_INT}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_INT** = `2`

Variable is of type `int<class_int>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_FLOAT** = `3`

Variable is of type `float<class_float>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_STRING}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_STRING** = `4`

Variable is of type `String<class_String>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_VECTOR2}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_VECTOR2** = `5`

Variable is of type `Vector2<class_Vector2>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_VECTOR2I}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_VECTOR2I** = `6`

Variable is of type `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_RECT2}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_RECT2** = `7`

Variable is of type `Rect2<class_Rect2>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_RECT2I}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_RECT2I** = `8`

Variable is of type `Rect2i<class_Rect2i>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_VECTOR3}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_VECTOR3** = `9`

Variable is of type `Vector3<class_Vector3>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_VECTOR3I}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_VECTOR3I** = `10`

Variable is of type `Vector3i<class_Vector3i>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_TRANSFORM2D}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_TRANSFORM2D** = `11`

Variable is of type `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_VECTOR4}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_VECTOR4** = `12`

Variable is of type `Vector4<class_Vector4>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_VECTOR4I}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_VECTOR4I** = `13`

Variable is of type `Vector4i<class_Vector4i>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PLANE}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PLANE** = `14`

Variable is of type `Plane<class_Plane>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_QUATERNION}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_QUATERNION** = `15`

Variable is of type `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_AABB}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_AABB** = `16`

Variable is of type `AABB<class_AABB>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_BASIS}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_BASIS** = `17`

Variable is of type `Basis<class_Basis>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_TRANSFORM3D}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_TRANSFORM3D** = `18`

Variable is of type `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PROJECTION}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PROJECTION** = `19`

Variable is of type `Projection<class_Projection>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_COLOR** = `20`

Variable is of type `Color<class_Color>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_STRING_NAME}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_STRING_NAME** = `21`

Variable is of type `StringName<class_StringName>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_NODE_PATH}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_NODE_PATH** = `22`

Variable is of type `NodePath<class_NodePath>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_RID}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_RID** = `23`

Variable is of type `RID<class_RID>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_OBJECT}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_OBJECT** = `24`

Variable is of type `Object<class_Object>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_CALLABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_CALLABLE** = `25`

Variable is of type `Callable<class_Callable>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_SIGNAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_SIGNAL** = `26`

Variable is of type `Signal<class_Signal>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_DICTIONARY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_DICTIONARY** = `27`

Variable is of type `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_ARRAY** = `28`

Variable is of type `Array<class_Array>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_BYTE_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_BYTE_ARRAY** = `29`

Variable is of type
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_INT32_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_INT32_ARRAY** = `30`

Variable is of type
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_INT64_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_INT64_ARRAY** = `31`

Variable is of type
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_FLOAT32_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_FLOAT32_ARRAY** = `32`

Variable is of type
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_FLOAT64_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_FLOAT64_ARRAY** = `33`

Variable is of type
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_STRING_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_STRING_ARRAY** = `34`

Variable is of type
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_VECTOR2_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_VECTOR2_ARRAY** = `35`

Variable is of type
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_VECTOR3_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_VECTOR3_ARRAY** = `36`

Variable is of type
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_COLOR_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_COLOR_ARRAY** = `37`

Variable is of type
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_PACKED_VECTOR4_ARRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_PACKED_VECTOR4_ARRAY** = `38`

Variable is of type
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"}.

:::: {#class_@GlobalScope_constant_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} **TYPE_MAX** = `39`

Represents the size of the
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_@GlobalScope_Variant.Operator}
::: rst-class
classref-enumeration
:::
::::

enum **Variant.Operator**:
`🔗<enum_@GlobalScope_Variant.Operator>`{.interpreted-text role="ref"}

:::: {#class_@GlobalScope_constant_OP_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_EQUAL** = `0`

Equality operator (`==`).

:::: {#class_@GlobalScope_constant_OP_NOT_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_NOT_EQUAL** = `1`

Inequality operator (`!=`).

:::: {#class_@GlobalScope_constant_OP_LESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_LESS** = `2`

Less than operator (`<`).

:::: {#class_@GlobalScope_constant_OP_LESS_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_LESS_EQUAL** = `3`

Less than or equal operator (`<=`).

:::: {#class_@GlobalScope_constant_OP_GREATER}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_GREATER** = `4`

Greater than operator (`>`).

:::: {#class_@GlobalScope_constant_OP_GREATER_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_GREATER_EQUAL** = `5`

Greater than or equal operator (`>=`).

:::: {#class_@GlobalScope_constant_OP_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_ADD** = `6`

Addition operator (`+`).

:::: {#class_@GlobalScope_constant_OP_SUBTRACT}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_SUBTRACT** = `7`

Subtraction operator (`-`).

:::: {#class_@GlobalScope_constant_OP_MULTIPLY}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_MULTIPLY** = `8`

Multiplication operator (`*`).

:::: {#class_@GlobalScope_constant_OP_DIVIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_DIVIDE** = `9`

Division operator (`/`).

:::: {#class_@GlobalScope_constant_OP_NEGATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_NEGATE** = `10`

Unary negation operator (`-`).

:::: {#class_@GlobalScope_constant_OP_POSITIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_POSITIVE** = `11`

Unary plus operator (`+`).

:::: {#class_@GlobalScope_constant_OP_MODULE}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_MODULE** = `12`

Remainder/modulo operator (`%`).

:::: {#class_@GlobalScope_constant_OP_POWER}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_POWER** = `13`

Power operator (`**`).

:::: {#class_@GlobalScope_constant_OP_SHIFT_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_SHIFT_LEFT** = `14`

Left shift operator (`<<`).

:::: {#class_@GlobalScope_constant_OP_SHIFT_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_SHIFT_RIGHT** = `15`

Right shift operator (`>>`).

:::: {#class_@GlobalScope_constant_OP_BIT_AND}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_BIT_AND** = `16`

Bitwise AND operator (`&`).

:::: {#class_@GlobalScope_constant_OP_BIT_OR}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_BIT_OR** = `17`

Bitwise OR operator (`|`).

:::: {#class_@GlobalScope_constant_OP_BIT_XOR}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_BIT_XOR** = `18`

Bitwise XOR operator (`^`).

:::: {#class_@GlobalScope_constant_OP_BIT_NEGATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_BIT_NEGATE** = `19`

Bitwise NOT operator (`~`).

:::: {#class_@GlobalScope_constant_OP_AND}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_AND** = `20`

Logical AND operator (`and` or `&&`).

:::: {#class_@GlobalScope_constant_OP_OR}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_OR** = `21`

Logical OR operator (`or` or `||`).

:::: {#class_@GlobalScope_constant_OP_XOR}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_XOR** = `22`

Logical XOR operator (not implemented in GDScript).

:::: {#class_@GlobalScope_constant_OP_NOT}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_NOT** = `23`

Logical NOT operator (`not` or `!`).

:::: {#class_@GlobalScope_constant_OP_IN}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_IN** = `24`

Logical IN operator (`in`).

:::: {#class_@GlobalScope_constant_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} **OP_MAX** = `25`

Represents the size of the
`Variant.Operator<enum_@GlobalScope_Variant.Operator>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_@GlobalScope_property_AudioServer}
::: rst-class
classref-property
:::
::::

`AudioServer<class_AudioServer>`{.interpreted-text role="ref"}
**AudioServer**
`🔗<class_@GlobalScope_property_AudioServer>`{.interpreted-text
role="ref"}

The `AudioServer<class_AudioServer>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_CameraServer}
::: rst-class
classref-property
:::
::::

`CameraServer<class_CameraServer>`{.interpreted-text role="ref"}
**CameraServer**
`🔗<class_@GlobalScope_property_CameraServer>`{.interpreted-text
role="ref"}

The `CameraServer<class_CameraServer>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_ClassDB}
::: rst-class
classref-property
:::
::::

`ClassDB<class_ClassDB>`{.interpreted-text role="ref"} **ClassDB**
`🔗<class_@GlobalScope_property_ClassDB>`{.interpreted-text role="ref"}

The `ClassDB<class_ClassDB>`{.interpreted-text role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_DisplayServer}
::: rst-class
classref-property
:::
::::

`DisplayServer<class_DisplayServer>`{.interpreted-text role="ref"}
**DisplayServer**
`🔗<class_@GlobalScope_property_DisplayServer>`{.interpreted-text
role="ref"}

The `DisplayServer<class_DisplayServer>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_EditorInterface}
::: rst-class
classref-property
:::
::::

`EditorInterface<class_EditorInterface>`{.interpreted-text role="ref"}
**EditorInterface**
`🔗<class_@GlobalScope_property_EditorInterface>`{.interpreted-text
role="ref"}

The `EditorInterface<class_EditorInterface>`{.interpreted-text
role="ref"} singleton.

\*\*Note:\*\* Only available in editor builds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_Engine}
::: rst-class
classref-property
:::
::::

`Engine<class_Engine>`{.interpreted-text role="ref"} **Engine**
`🔗<class_@GlobalScope_property_Engine>`{.interpreted-text role="ref"}

The `Engine<class_Engine>`{.interpreted-text role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_EngineDebugger}
::: rst-class
classref-property
:::
::::

`EngineDebugger<class_EngineDebugger>`{.interpreted-text role="ref"}
**EngineDebugger**
`🔗<class_@GlobalScope_property_EngineDebugger>`{.interpreted-text
role="ref"}

The `EngineDebugger<class_EngineDebugger>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_GDExtensionManager}
::: rst-class
classref-property
:::
::::

`GDExtensionManager<class_GDExtensionManager>`{.interpreted-text
role="ref"} **GDExtensionManager**
`🔗<class_@GlobalScope_property_GDExtensionManager>`{.interpreted-text
role="ref"}

The `GDExtensionManager<class_GDExtensionManager>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_Geometry2D}
::: rst-class
classref-property
:::
::::

`Geometry2D<class_Geometry2D>`{.interpreted-text role="ref"}
**Geometry2D**
`🔗<class_@GlobalScope_property_Geometry2D>`{.interpreted-text
role="ref"}

The `Geometry2D<class_Geometry2D>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_Geometry3D}
::: rst-class
classref-property
:::
::::

`Geometry3D<class_Geometry3D>`{.interpreted-text role="ref"}
**Geometry3D**
`🔗<class_@GlobalScope_property_Geometry3D>`{.interpreted-text
role="ref"}

The `Geometry3D<class_Geometry3D>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_IP}
::: rst-class
classref-property
:::
::::

`IP<class_IP>`{.interpreted-text role="ref"} **IP**
`🔗<class_@GlobalScope_property_IP>`{.interpreted-text role="ref"}

The `IP<class_IP>`{.interpreted-text role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_Input}
::: rst-class
classref-property
:::
::::

`Input<class_Input>`{.interpreted-text role="ref"} **Input**
`🔗<class_@GlobalScope_property_Input>`{.interpreted-text role="ref"}

The `Input<class_Input>`{.interpreted-text role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_InputMap}
::: rst-class
classref-property
:::
::::

`InputMap<class_InputMap>`{.interpreted-text role="ref"} **InputMap**
`🔗<class_@GlobalScope_property_InputMap>`{.interpreted-text role="ref"}

The `InputMap<class_InputMap>`{.interpreted-text role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_JavaClassWrapper}
::: rst-class
classref-property
:::
::::

`JavaClassWrapper<class_JavaClassWrapper>`{.interpreted-text role="ref"}
**JavaClassWrapper**
`🔗<class_@GlobalScope_property_JavaClassWrapper>`{.interpreted-text
role="ref"}

The `JavaClassWrapper<class_JavaClassWrapper>`{.interpreted-text
role="ref"} singleton.

\*\*Note:\*\* Only implemented on Android.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_JavaScriptBridge}
::: rst-class
classref-property
:::
::::

`JavaScriptBridge<class_JavaScriptBridge>`{.interpreted-text role="ref"}
**JavaScriptBridge**
`🔗<class_@GlobalScope_property_JavaScriptBridge>`{.interpreted-text
role="ref"}

The `JavaScriptBridge<class_JavaScriptBridge>`{.interpreted-text
role="ref"} singleton.

\*\*Note:\*\* Only implemented on the Web platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_Marshalls}
::: rst-class
classref-property
:::
::::

`Marshalls<class_Marshalls>`{.interpreted-text role="ref"} **Marshalls**
`🔗<class_@GlobalScope_property_Marshalls>`{.interpreted-text
role="ref"}

The `Marshalls<class_Marshalls>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_NativeMenu}
::: rst-class
classref-property
:::
::::

`NativeMenu<class_NativeMenu>`{.interpreted-text role="ref"}
**NativeMenu**
`🔗<class_@GlobalScope_property_NativeMenu>`{.interpreted-text
role="ref"}

The `NativeMenu<class_NativeMenu>`{.interpreted-text role="ref"}
singleton.

\*\*Note:\*\* Only implemented on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_NavigationMeshGenerator}
::: rst-class
classref-property
:::
::::

`NavigationMeshGenerator<class_NavigationMeshGenerator>`{.interpreted-text
role="ref"} **NavigationMeshGenerator**
`🔗<class_@GlobalScope_property_NavigationMeshGenerator>`{.interpreted-text
role="ref"}

The
`NavigationMeshGenerator<class_NavigationMeshGenerator>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_NavigationServer2D}
::: rst-class
classref-property
:::
::::

`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"} **NavigationServer2D**
`🔗<class_@GlobalScope_property_NavigationServer2D>`{.interpreted-text
role="ref"}

The `NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_NavigationServer3D}
::: rst-class
classref-property
:::
::::

`NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"} **NavigationServer3D**
`🔗<class_@GlobalScope_property_NavigationServer3D>`{.interpreted-text
role="ref"}

The `NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_OS}
::: rst-class
classref-property
:::
::::

`OS<class_OS>`{.interpreted-text role="ref"} **OS**
`🔗<class_@GlobalScope_property_OS>`{.interpreted-text role="ref"}

The `OS<class_OS>`{.interpreted-text role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_Performance}
::: rst-class
classref-property
:::
::::

`Performance<class_Performance>`{.interpreted-text role="ref"}
**Performance**
`🔗<class_@GlobalScope_property_Performance>`{.interpreted-text
role="ref"}

The `Performance<class_Performance>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_PhysicsServer2D}
::: rst-class
classref-property
:::
::::

`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}
**PhysicsServer2D**
`🔗<class_@GlobalScope_property_PhysicsServer2D>`{.interpreted-text
role="ref"}

The `PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_PhysicsServer2DManager}
::: rst-class
classref-property
:::
::::

`PhysicsServer2DManager<class_PhysicsServer2DManager>`{.interpreted-text
role="ref"} **PhysicsServer2DManager**
`🔗<class_@GlobalScope_property_PhysicsServer2DManager>`{.interpreted-text
role="ref"}

The
`PhysicsServer2DManager<class_PhysicsServer2DManager>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_PhysicsServer3D}
::: rst-class
classref-property
:::
::::

`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}
**PhysicsServer3D**
`🔗<class_@GlobalScope_property_PhysicsServer3D>`{.interpreted-text
role="ref"}

The `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_PhysicsServer3DManager}
::: rst-class
classref-property
:::
::::

`PhysicsServer3DManager<class_PhysicsServer3DManager>`{.interpreted-text
role="ref"} **PhysicsServer3DManager**
`🔗<class_@GlobalScope_property_PhysicsServer3DManager>`{.interpreted-text
role="ref"}

The
`PhysicsServer3DManager<class_PhysicsServer3DManager>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_ProjectSettings}
::: rst-class
classref-property
:::
::::

`ProjectSettings<class_ProjectSettings>`{.interpreted-text role="ref"}
**ProjectSettings**
`🔗<class_@GlobalScope_property_ProjectSettings>`{.interpreted-text
role="ref"}

The `ProjectSettings<class_ProjectSettings>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_RenderingServer}
::: rst-class
classref-property
:::
::::

`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
**RenderingServer**
`🔗<class_@GlobalScope_property_RenderingServer>`{.interpreted-text
role="ref"}

The `RenderingServer<class_RenderingServer>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_ResourceLoader}
::: rst-class
classref-property
:::
::::

`ResourceLoader<class_ResourceLoader>`{.interpreted-text role="ref"}
**ResourceLoader**
`🔗<class_@GlobalScope_property_ResourceLoader>`{.interpreted-text
role="ref"}

The `ResourceLoader<class_ResourceLoader>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_ResourceSaver}
::: rst-class
classref-property
:::
::::

`ResourceSaver<class_ResourceSaver>`{.interpreted-text role="ref"}
**ResourceSaver**
`🔗<class_@GlobalScope_property_ResourceSaver>`{.interpreted-text
role="ref"}

The `ResourceSaver<class_ResourceSaver>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_ResourceUID}
::: rst-class
classref-property
:::
::::

`ResourceUID<class_ResourceUID>`{.interpreted-text role="ref"}
**ResourceUID**
`🔗<class_@GlobalScope_property_ResourceUID>`{.interpreted-text
role="ref"}

The `ResourceUID<class_ResourceUID>`{.interpreted-text role="ref"}
singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_TextServerManager}
::: rst-class
classref-property
:::
::::

`TextServerManager<class_TextServerManager>`{.interpreted-text
role="ref"} **TextServerManager**
`🔗<class_@GlobalScope_property_TextServerManager>`{.interpreted-text
role="ref"}

The `TextServerManager<class_TextServerManager>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_ThemeDB}
::: rst-class
classref-property
:::
::::

`ThemeDB<class_ThemeDB>`{.interpreted-text role="ref"} **ThemeDB**
`🔗<class_@GlobalScope_property_ThemeDB>`{.interpreted-text role="ref"}

The `ThemeDB<class_ThemeDB>`{.interpreted-text role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_Time}
::: rst-class
classref-property
:::
::::

`Time<class_Time>`{.interpreted-text role="ref"} **Time**
`🔗<class_@GlobalScope_property_Time>`{.interpreted-text role="ref"}

The `Time<class_Time>`{.interpreted-text role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_TranslationServer}
::: rst-class
classref-property
:::
::::

`TranslationServer<class_TranslationServer>`{.interpreted-text
role="ref"} **TranslationServer**
`🔗<class_@GlobalScope_property_TranslationServer>`{.interpreted-text
role="ref"}

The `TranslationServer<class_TranslationServer>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_WorkerThreadPool}
::: rst-class
classref-property
:::
::::

`WorkerThreadPool<class_WorkerThreadPool>`{.interpreted-text role="ref"}
**WorkerThreadPool**
`🔗<class_@GlobalScope_property_WorkerThreadPool>`{.interpreted-text
role="ref"}

The `WorkerThreadPool<class_WorkerThreadPool>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_property_XRServer}
::: rst-class
classref-property
:::
::::

`XRServer<class_XRServer>`{.interpreted-text role="ref"} **XRServer**
`🔗<class_@GlobalScope_property_XRServer>`{.interpreted-text role="ref"}

The `XRServer<class_XRServer>`{.interpreted-text role="ref"} singleton.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_@GlobalScope_method_abs}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **abs**(x:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_abs>`{.interpreted-text role="ref"}

Returns the absolute value of a
`Variant<class_Variant>`{.interpreted-text role="ref"} parameter `x`
(i.e. non-negative value). Supported types:
`int<class_int>`{.interpreted-text role="ref"},
`float<class_float>`{.interpreted-text role="ref"},
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"},
`Vector4<class_Vector4>`{.interpreted-text role="ref"},
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}.

    var a = abs(-1)
    # a is 1

    var b = abs(-1.2)
    # b is 1.2

    var c = abs(Vector2(-3.5, -4))
    # c is (3.5, 4)

    var d = abs(Vector2i(-5, -6))
    # d is (5, 6)

    var e = abs(Vector3(-7, 8.5, -3.8))
    # e is (7, 8.5, 3.8)

    var f = abs(Vector3i(-7, -8, -9))
    # f is (7, 8, 9)

\*\*Note:\*\* For better type safety, use
`absf()<class_@GlobalScope_method_absf>`{.interpreted-text role="ref"},
`absi()<class_@GlobalScope_method_absi>`{.interpreted-text role="ref"},
`Vector2.abs()<class_Vector2_method_abs>`{.interpreted-text role="ref"},
`Vector2i.abs()<class_Vector2i_method_abs>`{.interpreted-text
role="ref"}, `Vector3.abs()<class_Vector3_method_abs>`{.interpreted-text
role="ref"},
`Vector3i.abs()<class_Vector3i_method_abs>`{.interpreted-text
role="ref"}, `Vector4.abs()<class_Vector4_method_abs>`{.interpreted-text
role="ref"}, or
`Vector4i.abs()<class_Vector4i_method_abs>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_absf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **absf**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_absf>`{.interpreted-text role="ref"}

Returns the absolute value of float parameter `x` (i.e. positive value).

    # a is 1.2
    var a = absf(-1.2)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_absi}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **absi**(x:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_absi>`{.interpreted-text role="ref"}

Returns the absolute value of int parameter `x` (i.e. positive value).

    # a is 1
    var a = absi(-1)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_acos}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **acos**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_acos>`{.interpreted-text role="ref"}

Returns the arc cosine of `x` in radians. Use to get the angle of cosine
`x`. `x` will be clamped between `-1.0` and `1.0` (inclusive), in order
to prevent `acos()<class_@GlobalScope_method_acos>`{.interpreted-text
role="ref"} from returning
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"}.

    # c is 0.523599 or 30 degrees if converted with rad_to_deg(c)
    var c = acos(0.866025)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_acosh}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **acosh**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_acosh>`{.interpreted-text role="ref"}

Returns the hyperbolic arc (also called inverse) cosine of `x`,
returning a value in radians. Use it to get the angle from an angle\'s
cosine in hyperbolic space if `x` is larger or equal to 1. For values of
`x` lower than 1, it will return 0, in order to prevent
`acosh()<class_@GlobalScope_method_acosh>`{.interpreted-text role="ref"}
from returning
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"}.

    var a = acosh(2) # Returns 1.31695789692482
    cosh(a) # Returns 2

    var b = acosh(-1) # Returns 0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_angle_difference}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angle_difference**(from: `float<class_float>`{.interpreted-text
role="ref"}, to: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_angle_difference>`{.interpreted-text
role="ref"}

Returns the difference between the two angles (in radians), in the range
of `[-PI, +PI]`. When `from` and `to` are opposite, returns `-PI` if
`from` is smaller than `to`, or `PI` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_asin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **asin**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_asin>`{.interpreted-text role="ref"}

Returns the arc sine of `x` in radians. Use to get the angle of sine
`x`. `x` will be clamped between `-1.0` and `1.0` (inclusive), in order
to prevent `asin()<class_@GlobalScope_method_asin>`{.interpreted-text
role="ref"} from returning
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"}.

    # s is 0.523599 or 30 degrees if converted with rad_to_deg(s)
    var s = asin(0.5)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_asinh}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **asinh**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_asinh>`{.interpreted-text role="ref"}

Returns the hyperbolic arc (also called inverse) sine of `x`, returning
a value in radians. Use it to get the angle from an angle\'s sine in
hyperbolic space.

    var a = asinh(0.9) # Returns 0.8088669356527824
    sinh(a) # Returns 0.9

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_atan}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **atan**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_atan>`{.interpreted-text role="ref"}

Returns the arc tangent of `x` in radians. Use it to get the angle from
an angle\'s tangent in trigonometry.

The method cannot know in which quadrant the angle should fall. See
`atan2()<class_@GlobalScope_method_atan2>`{.interpreted-text role="ref"}
if you have both `y` and `x`.

    var a = atan(0.5) # a is 0.463648

If `x` is between `-PI / 2` and `PI / 2` (inclusive), `atan(tan(x))` is
equal to `x`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_atan2}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **atan2**(y:
`float<class_float>`{.interpreted-text role="ref"}, x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_atan2>`{.interpreted-text role="ref"}

Returns the arc tangent of `y/x` in radians. Use to get the angle of
tangent `y/x`. To compute the value, the method takes into account the
sign of both arguments in order to determine the quadrant.

Important note: The Y coordinate comes first, by convention.

    var a = atan2(0, -1) # a is 3.141593

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_atanh}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **atanh**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_atanh>`{.interpreted-text role="ref"}

Returns the hyperbolic arc (also called inverse) tangent of `x`,
returning a value in radians. Use it to get the angle from an angle\'s
tangent in hyperbolic space if `x` is between -1 and 1 (non-inclusive).

In mathematics, the inverse hyperbolic tangent is only defined for -1 \<
`x` \< 1 in the real set, so values equal or lower to -1 for `x` return
negative `@GDScript.INF<class_@GDScript_constant_INF>`{.interpreted-text
role="ref"} and values equal or higher than 1 return positive
`@GDScript.INF<class_@GDScript_constant_INF>`{.interpreted-text
role="ref"} in order to prevent
`atanh()<class_@GlobalScope_method_atanh>`{.interpreted-text role="ref"}
from returning
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"}.

    var a = atanh(0.9) # Returns 1.47221948958322
    tanh(a) # Returns 0.9

    var b = atanh(-2) # Returns -inf
    tanh(b) # Returns -1

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_bezier_derivative}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**bezier_derivative**(start: `float<class_float>`{.interpreted-text
role="ref"}, control_1: `float<class_float>`{.interpreted-text
role="ref"}, control_2: `float<class_float>`{.interpreted-text
role="ref"}, end: `float<class_float>`{.interpreted-text role="ref"}, t:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_bezier_derivative>`{.interpreted-text
role="ref"}

Returns the derivative at the given `t` on a one-dimensional [Bézier
curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) defined by the
given `control_1`, `control_2`, and `end` points.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_bezier_interpolate}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**bezier_interpolate**(start: `float<class_float>`{.interpreted-text
role="ref"}, control_1: `float<class_float>`{.interpreted-text
role="ref"}, control_2: `float<class_float>`{.interpreted-text
role="ref"}, end: `float<class_float>`{.interpreted-text role="ref"}, t:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_bezier_interpolate>`{.interpreted-text
role="ref"}

Returns the point at the given `t` on a one-dimensional [Bézier
curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) defined by the
given `control_1`, `control_2`, and `end` points.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_bytes_to_var}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**bytes_to_var**(bytes:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_bytes_to_var>`{.interpreted-text
role="ref"}

Decodes a byte array back to a
`Variant<class_Variant>`{.interpreted-text role="ref"} value, without
decoding objects.

\*\*Note:\*\* If you need object deserialization, see
`bytes_to_var_with_objects()<class_@GlobalScope_method_bytes_to_var_with_objects>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_bytes_to_var_with_objects}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**bytes_to_var_with_objects**(bytes:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_bytes_to_var_with_objects>`{.interpreted-text
role="ref"}

Decodes a byte array back to a
`Variant<class_Variant>`{.interpreted-text role="ref"} value. Decoding
objects is allowed.

\*\*Warning:\*\* Deserialized object can contain code which gets
executed. Do not use this option if the serialized object comes from
untrusted sources to avoid potential security threats (remote code
execution).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_ceil}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **ceil**(x:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_ceil>`{.interpreted-text role="ref"}

Rounds `x` upward (towards positive infinity), returning the smallest
whole number that is not less than `x`. Supported types:
`int<class_int>`{.interpreted-text role="ref"},
`float<class_float>`{.interpreted-text role="ref"},
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"},
`Vector4<class_Vector4>`{.interpreted-text role="ref"},
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}.

    var i = ceil(1.45) # i is 2.0
    i = ceil(1.001)    # i is 2.0

See also `floor()<class_@GlobalScope_method_floor>`{.interpreted-text
role="ref"},
`round()<class_@GlobalScope_method_round>`{.interpreted-text
role="ref"}, and
`snapped()<class_@GlobalScope_method_snapped>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For better type safety, use
`ceilf()<class_@GlobalScope_method_ceilf>`{.interpreted-text
role="ref"},
`ceili()<class_@GlobalScope_method_ceili>`{.interpreted-text
role="ref"},
`Vector2.ceil()<class_Vector2_method_ceil>`{.interpreted-text
role="ref"},
`Vector3.ceil()<class_Vector3_method_ceil>`{.interpreted-text
role="ref"}, or
`Vector4.ceil()<class_Vector4_method_ceil>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_ceilf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ceilf**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_ceilf>`{.interpreted-text role="ref"}

Rounds `x` upward (towards positive infinity), returning the smallest
whole number that is not less than `x`.

A type-safe version of
`ceil()<class_@GlobalScope_method_ceil>`{.interpreted-text role="ref"},
returning a `float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_ceili}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **ceili**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_ceili>`{.interpreted-text role="ref"}

Rounds `x` upward (towards positive infinity), returning the smallest
whole number that is not less than `x`.

A type-safe version of
`ceil()<class_@GlobalScope_method_ceil>`{.interpreted-text role="ref"},
returning an `int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_clamp}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **clamp**(value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, min:
`Variant<class_Variant>`{.interpreted-text role="ref"}, max:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_clamp>`{.interpreted-text role="ref"}

Clamps the `value`, returning a
`Variant<class_Variant>`{.interpreted-text role="ref"} not less than
`min` and not more than `max`. Any values that can be compared with the
less than and greater than operators will work.

    var a = clamp(-10, -1, 5)
    # a is -1

    var b = clamp(8.1, 0.9, 5.5)
    # b is 5.5

\*\*Note:\*\* For better type safety, use
`clampf()<class_@GlobalScope_method_clampf>`{.interpreted-text
role="ref"},
`clampi()<class_@GlobalScope_method_clampi>`{.interpreted-text
role="ref"},
`Vector2.clamp()<class_Vector2_method_clamp>`{.interpreted-text
role="ref"},
`Vector2i.clamp()<class_Vector2i_method_clamp>`{.interpreted-text
role="ref"},
`Vector3.clamp()<class_Vector3_method_clamp>`{.interpreted-text
role="ref"},
`Vector3i.clamp()<class_Vector3i_method_clamp>`{.interpreted-text
role="ref"},
`Vector4.clamp()<class_Vector4_method_clamp>`{.interpreted-text
role="ref"},
`Vector4i.clamp()<class_Vector4i_method_clamp>`{.interpreted-text
role="ref"}, or
`Color.clamp()<class_Color_method_clamp>`{.interpreted-text role="ref"}
(not currently supported by this method).

\*\*Note:\*\* When using this on vectors it will *not* perform
component-wise clamping, and will pick `min` if `value < min` or `max`
if `value > max`. To perform component-wise clamping use the methods
listed above.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_clampf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **clampf**(value:
`float<class_float>`{.interpreted-text role="ref"}, min:
`float<class_float>`{.interpreted-text role="ref"}, max:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_clampf>`{.interpreted-text role="ref"}

Clamps the `value`, returning a `float<class_float>`{.interpreted-text
role="ref"} not less than `min` and not more than `max`.

    var speed = 42.1
    var a = clampf(speed, 1.0, 20.5) # a is 20.5

    speed = -10.0
    var b = clampf(speed, -1.0, 1.0) # b is -1.0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_clampi}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **clampi**(value:
`int<class_int>`{.interpreted-text role="ref"}, min:
`int<class_int>`{.interpreted-text role="ref"}, max:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_clampi>`{.interpreted-text role="ref"}

Clamps the `value`, returning an `int<class_int>`{.interpreted-text
role="ref"} not less than `min` and not more than `max`.

    var speed = 42
    var a = clampi(speed, 1, 20) # a is 20

    speed = -10
    var b = clampi(speed, -1, 1) # b is -1

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_cos}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cos**(angle_rad:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_cos>`{.interpreted-text role="ref"}

Returns the cosine of angle `angle_rad` in radians.

    cos(PI * 2)         # Returns 1.0
    cos(PI)             # Returns -1.0
    cos(deg_to_rad(90)) # Returns 0.0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_cosh}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **cosh**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_cosh>`{.interpreted-text role="ref"}

Returns the hyperbolic cosine of `x` in radians.

    print(cosh(1)) # Prints 1.543081

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_cubic_interpolate}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**cubic_interpolate**(from: `float<class_float>`{.interpreted-text
role="ref"}, to: `float<class_float>`{.interpreted-text role="ref"},
pre: `float<class_float>`{.interpreted-text role="ref"}, post:
`float<class_float>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_cubic_interpolate>`{.interpreted-text
role="ref"}

Cubic interpolates between two values by the factor defined in `weight`
with `pre` and `post` values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_cubic_interpolate_angle}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**cubic_interpolate_angle**(from: `float<class_float>`{.interpreted-text
role="ref"}, to: `float<class_float>`{.interpreted-text role="ref"},
pre: `float<class_float>`{.interpreted-text role="ref"}, post:
`float<class_float>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_cubic_interpolate_angle>`{.interpreted-text
role="ref"}

Cubic interpolates between two rotation values with shortest path by the
factor defined in `weight` with `pre` and `post` values. See also
`lerp_angle()<class_@GlobalScope_method_lerp_angle>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_cubic_interpolate_angle_in_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**cubic_interpolate_angle_in_time**(from:
`float<class_float>`{.interpreted-text role="ref"}, to:
`float<class_float>`{.interpreted-text role="ref"}, pre:
`float<class_float>`{.interpreted-text role="ref"}, post:
`float<class_float>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"}, to_t:
`float<class_float>`{.interpreted-text role="ref"}, pre_t:
`float<class_float>`{.interpreted-text role="ref"}, post_t:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_cubic_interpolate_angle_in_time>`{.interpreted-text
role="ref"}

Cubic interpolates between two rotation values with shortest path by the
factor defined in `weight` with `pre` and `post` values. See also
`lerp_angle()<class_@GlobalScope_method_lerp_angle>`{.interpreted-text
role="ref"}.

It can perform smoother interpolation than
`cubic_interpolate()<class_@GlobalScope_method_cubic_interpolate>`{.interpreted-text
role="ref"} by the time values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_cubic_interpolate_in_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**cubic_interpolate_in_time**(from:
`float<class_float>`{.interpreted-text role="ref"}, to:
`float<class_float>`{.interpreted-text role="ref"}, pre:
`float<class_float>`{.interpreted-text role="ref"}, post:
`float<class_float>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"}, to_t:
`float<class_float>`{.interpreted-text role="ref"}, pre_t:
`float<class_float>`{.interpreted-text role="ref"}, post_t:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_cubic_interpolate_in_time>`{.interpreted-text
role="ref"}

Cubic interpolates between two values by the factor defined in `weight`
with `pre` and `post` values.

It can perform smoother interpolation than
`cubic_interpolate()<class_@GlobalScope_method_cubic_interpolate>`{.interpreted-text
role="ref"} by the time values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_db_to_linear}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **db_to_linear**(db:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_db_to_linear>`{.interpreted-text
role="ref"}

Converts from decibels to linear energy (audio).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_deg_to_rad}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **deg_to_rad**(deg:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_deg_to_rad>`{.interpreted-text role="ref"}

Converts an angle expressed in degrees to radians.

    var r = deg_to_rad(180) # r is 3.141593

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_ease}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ease**(x:
`float<class_float>`{.interpreted-text role="ref"}, curve:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_ease>`{.interpreted-text role="ref"}

Returns an \"eased\" value of `x` based on an easing function defined
with `curve`. This easing function is based on an exponent. The `curve`
can be any floating-point number, with specific values leading to the
following behaviors:

``` text
- Lower than -1.0 (exclusive): Ease in-out
- -1.0: Linear
- Between -1.0 and 0.0 (exclusive): Ease out-in
- 0.0: Constant
- Between 0.0 to 1.0 (exclusive): Ease out
- 1.0: Linear
- Greater than 1.0 (exclusive): Ease in
```

\`ease() curve values cheatsheet
\<https://raw.githubusercontent.com/godotengine/godot-docs/master/img/ease_cheatsheet.png\>\`\_\_

See also
`smoothstep()<class_@GlobalScope_method_smoothstep>`{.interpreted-text
role="ref"}. If you need to perform more advanced transitions, use
`Tween.interpolate_value()<class_Tween_method_interpolate_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_error_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**error_string**(error: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_error_string>`{.interpreted-text
role="ref"}

Returns a human-readable name for the given
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} code.

    print(OK)                              # Prints 0
    print(error_string(OK))                # Prints "OK"
    print(error_string(ERR_BUSY))          # Prints "Busy"
    print(error_string(ERR_OUT_OF_MEMORY)) # Prints "Out of memory"

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_exp}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **exp**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_exp>`{.interpreted-text role="ref"}

The natural exponential function. It raises the mathematical constant
*e* to the power of `x` and returns it.

\*e\* has an approximate value of 2.71828, and can be obtained with
`exp(1)`.

For exponents to other bases use the method
`pow()<class_@GlobalScope_method_pow>`{.interpreted-text role="ref"}.

    var a = exp(2) # Approximately 7.39

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_floor}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **floor**(x:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_floor>`{.interpreted-text role="ref"}

Rounds `x` downward (towards negative infinity), returning the largest
whole number that is not more than `x`. Supported types:
`int<class_int>`{.interpreted-text role="ref"},
`float<class_float>`{.interpreted-text role="ref"},
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"},
`Vector4<class_Vector4>`{.interpreted-text role="ref"},
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}.

    var a = floor(2.99) # a is 2.0
    a = floor(-2.99)    # a is -3.0

See also `ceil()<class_@GlobalScope_method_ceil>`{.interpreted-text
role="ref"},
`round()<class_@GlobalScope_method_round>`{.interpreted-text
role="ref"}, and
`snapped()<class_@GlobalScope_method_snapped>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For better type safety, use
`floorf()<class_@GlobalScope_method_floorf>`{.interpreted-text
role="ref"},
`floori()<class_@GlobalScope_method_floori>`{.interpreted-text
role="ref"},
`Vector2.floor()<class_Vector2_method_floor>`{.interpreted-text
role="ref"},
`Vector3.floor()<class_Vector3_method_floor>`{.interpreted-text
role="ref"}, or
`Vector4.floor()<class_Vector4_method_floor>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_floorf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **floorf**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_floorf>`{.interpreted-text role="ref"}

Rounds `x` downward (towards negative infinity), returning the largest
whole number that is not more than `x`.

A type-safe version of
`floor()<class_@GlobalScope_method_floor>`{.interpreted-text
role="ref"}, returning a `float<class_float>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_floori}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **floori**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_floori>`{.interpreted-text role="ref"}

Rounds `x` downward (towards negative infinity), returning the largest
whole number that is not more than `x`.

A type-safe version of
`floor()<class_@GlobalScope_method_floor>`{.interpreted-text
role="ref"}, returning an `int<class_int>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This function is *not* the same as `int(x)`, which rounds
towards 0.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_fmod}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fmod**(x:
`float<class_float>`{.interpreted-text role="ref"}, y:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_fmod>`{.interpreted-text role="ref"}

Returns the floating-point remainder of `x` divided by `y`, keeping the
sign of `x`.

    var remainder = fmod(7, 5.5) # remainder is 1.5

For the integer remainder operation, use the `%` operator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_fposmod}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fposmod**(x:
`float<class_float>`{.interpreted-text role="ref"}, y:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_fposmod>`{.interpreted-text role="ref"}

Returns the floating-point modulus of `x` divided by `y`, wrapping
equally in positive and negative.

    print(" (x)  (fmod(x, 1.5))   (fposmod(x, 1.5))")
    for i in 7:
        var x = i * 0.5 - 1.5
        print("%4.1f           %4.1f  | %4.1f" % [x, fmod(x, 1.5), fposmod(x, 1.5)])

Prints:

``` text
(x)  (fmod(x, 1.5))   (fposmod(x, 1.5))
-1.5           -0.0  |  0.0
-1.0           -1.0  |  0.5
-0.5           -0.5  |  1.0
0.0            0.0  |  0.0
0.5            0.5  |  0.5
1.0            1.0  |  1.0
1.5            0.0  |  0.0
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_hash}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hash**(variable:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_hash>`{.interpreted-text role="ref"}

Returns the integer hash of the passed `variable`.

::::: tabs
::: code-tab
gdscript

print(hash(\"a\")) \# Prints 177670
:::

::: code-tab
csharp

GD.Print(GD.Hash(\"a\")); // Prints 177670
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_instance_from_id}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**instance_from_id**(instance_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_@GlobalScope_method_instance_from_id>`{.interpreted-text
role="ref"}

Returns the `Object<class_Object>`{.interpreted-text role="ref"} that
corresponds to `instance_id`. All Objects have a unique instance ID. See
also
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var drink = \"water\"

func [ready]{#ready}():

:   var id = get_instance_id() var instance = instance_from_id(id)
    print(instance.foo) \# Prints \"water\"
:::

::: code-tab
csharp

public partial class MyNode : Node { public string Drink { get; set; } =
\"water\";

> public override void [Ready]{#ready}() { ulong id = GetInstanceId();
> var instance = (MyNode)InstanceFromId(Id); GD.Print(instance.Drink);
> // Prints \"water\" }

}
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_inverse_lerp}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**inverse_lerp**(from: `float<class_float>`{.interpreted-text
role="ref"}, to: `float<class_float>`{.interpreted-text role="ref"},
weight: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_inverse_lerp>`{.interpreted-text
role="ref"}

Returns an interpolation or extrapolation factor considering the range
specified in `from` and `to`, and the interpolated value specified in
`weight`. The returned value will be between `0.0` and `1.0` if `weight`
is between `from` and `to` (inclusive). If `weight` is located outside
this range, then an extrapolation factor will be returned (return value
lower than `0.0` or greater than `1.0`). Use
`clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text role="ref"}
on the result of
`inverse_lerp()<class_@GlobalScope_method_inverse_lerp>`{.interpreted-text
role="ref"} if this is not desired.

    # The interpolation ratio in the `lerp()` call below is 0.75.
    var middle = lerp(20, 30, 0.75)
    # middle is now 27.5.

    # Now, we pretend to have forgotten the original ratio and want to get it back.
    var ratio = inverse_lerp(20, 30, 27.5)
    # ratio is now 0.75.

See also `lerp()<class_@GlobalScope_method_lerp>`{.interpreted-text
role="ref"}, which performs the reverse of this operation, and
`remap()<class_@GlobalScope_method_remap>`{.interpreted-text role="ref"}
to map a continuous series of values to another.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_equal_approx**(a:
`float<class_float>`{.interpreted-text role="ref"}, b:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"}

Returns `true` if `a` and `b` are approximately equal to each other.

Here, \"approximately equal\" means that `a` and `b` are within a small
internal epsilon of each other, which scales with the magnitude of the
numbers.

Infinity values of the same sign are considered equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_is_finite}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finite**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_is_finite>`{.interpreted-text role="ref"}

Returns whether `x` is a finite value, i.e. it is not
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"}, positive infinity, or negative infinity. See also
`is_inf()<class_@GlobalScope_method_is_inf>`{.interpreted-text
role="ref"} and
`is_nan()<class_@GlobalScope_method_is_nan>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_is_inf}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_inf**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_is_inf>`{.interpreted-text role="ref"}

Returns `true` if `x` is either positive infinity or negative infinity.
See also
`is_finite()<class_@GlobalScope_method_is_finite>`{.interpreted-text
role="ref"} and
`is_nan()<class_@GlobalScope_method_is_nan>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_is_instance_id_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_instance_id_valid**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_@GlobalScope_method_is_instance_id_valid>`{.interpreted-text
role="ref"}

Returns `true` if the Object that corresponds to `id` is a valid object
(e.g. has not been deleted from memory). All Objects have a unique
instance ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_is_instance_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_instance_valid**(instance:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_is_instance_valid>`{.interpreted-text
role="ref"}

Returns `true` if `instance` is a valid Object (e.g. has not been
deleted from memory).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_is_nan}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_nan**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_is_nan>`{.interpreted-text role="ref"}

Returns `true` if `x` is a NaN (\"Not a Number\" or invalid) value. This
method is needed as
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} is not equal to itself, which means `x == NAN` can\'t be
used to check whether a value is a NaN.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_is_same}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_same**(a:
`Variant<class_Variant>`{.interpreted-text role="ref"}, b:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_is_same>`{.interpreted-text role="ref"}

Returns `true`, for value types, if `a` and `b` share the same value.
Returns `true`, for reference types, if the references of `a` and `b`
are the same.

    # Vector2 is a value type
    var vec2_a = Vector2(0, 0)
    var vec2_b = Vector2(0, 0)
    var vec2_c = Vector2(1, 1)
    is_same(vec2_a, vec2_a)  # true
    is_same(vec2_a, vec2_b)  # true
    is_same(vec2_a, vec2_c)  # false

    # Array is a reference type
    var arr_a = []
    var arr_b = []
    is_same(arr_a, arr_a)  # true
    is_same(arr_a, arr_b)  # false

These are `Variant<class_Variant>`{.interpreted-text role="ref"} value
types: `null`, `bool<class_bool>`{.interpreted-text role="ref"},
`int<class_int>`{.interpreted-text role="ref"},
`float<class_float>`{.interpreted-text role="ref"},
`String<class_String>`{.interpreted-text role="ref"},
`StringName<class_StringName>`{.interpreted-text role="ref"},
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"},
`Vector4<class_Vector4>`{.interpreted-text role="ref"},
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"},
`Rect2<class_Rect2>`{.interpreted-text role="ref"},
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"},
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"},
`Plane<class_Plane>`{.interpreted-text role="ref"},
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"},
`AABB<class_AABB>`{.interpreted-text role="ref"},
`Basis<class_Basis>`{.interpreted-text role="ref"},
`Projection<class_Projection>`{.interpreted-text role="ref"},
`Color<class_Color>`{.interpreted-text role="ref"},
`NodePath<class_NodePath>`{.interpreted-text role="ref"},
`RID<class_RID>`{.interpreted-text role="ref"},
`Callable<class_Callable>`{.interpreted-text role="ref"} and
`Signal<class_Signal>`{.interpreted-text role="ref"}.

These are `Variant<class_Variant>`{.interpreted-text role="ref"}
reference types: `Object<class_Object>`{.interpreted-text role="ref"},
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"},
`Array<class_Array>`{.interpreted-text role="ref"},
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"},
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
role="ref"},
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"},
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"},
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"},
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"},
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"},
`PackedVector4Array<class_PackedVector4Array>`{.interpreted-text
role="ref"}, and
`PackedColorArray<class_PackedColorArray>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_is_zero_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_zero_approx**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_is_zero_approx>`{.interpreted-text
role="ref"}

Returns `true` if `x` is zero or almost zero. The comparison is done
using a tolerance calculation with a small internal epsilon.

This function is faster than using
`is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} with one value as zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_lerp}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **lerp**(from:
`Variant<class_Variant>`{.interpreted-text role="ref"}, to:
`Variant<class_Variant>`{.interpreted-text role="ref"}, weight:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_lerp>`{.interpreted-text role="ref"}

Linearly interpolates between two values by the factor defined in
`weight`. To perform interpolation, `weight` should be between `0.0` and
`1.0` (inclusive). However, values outside this range are allowed and
can be used to perform *extrapolation*. If this is not desired, use
`clampf()<class_@GlobalScope_method_clampf>`{.interpreted-text
role="ref"} to limit `weight`.

Both `from` and `to` must be the same type. Supported types:
`int<class_int>`{.interpreted-text role="ref"},
`float<class_float>`{.interpreted-text role="ref"},
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Vector4<class_Vector4>`{.interpreted-text role="ref"},
`Color<class_Color>`{.interpreted-text role="ref"},
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"},
`Basis<class_Basis>`{.interpreted-text role="ref"},
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

    lerp(0, 4, 0.75) # Returns 3.0

See also
`inverse_lerp()<class_@GlobalScope_method_inverse_lerp>`{.interpreted-text
role="ref"} which performs the reverse of this operation. To perform
eased interpolation with
`lerp()<class_@GlobalScope_method_lerp>`{.interpreted-text role="ref"},
combine it with
`ease()<class_@GlobalScope_method_ease>`{.interpreted-text role="ref"}
or
`smoothstep()<class_@GlobalScope_method_smoothstep>`{.interpreted-text
role="ref"}. See also
`remap()<class_@GlobalScope_method_remap>`{.interpreted-text role="ref"}
to map a continuous series of values to another.

\*\*Note:\*\* For better type safety, use
`lerpf()<class_@GlobalScope_method_lerpf>`{.interpreted-text
role="ref"},
`Vector2.lerp()<class_Vector2_method_lerp>`{.interpreted-text
role="ref"},
`Vector3.lerp()<class_Vector3_method_lerp>`{.interpreted-text
role="ref"},
`Vector4.lerp()<class_Vector4_method_lerp>`{.interpreted-text
role="ref"}, `Color.lerp()<class_Color_method_lerp>`{.interpreted-text
role="ref"},
`Quaternion.slerp()<class_Quaternion_method_slerp>`{.interpreted-text
role="ref"}, `Basis.slerp()<class_Basis_method_slerp>`{.interpreted-text
role="ref"},
`Transform2D.interpolate_with()<class_Transform2D_method_interpolate_with>`{.interpreted-text
role="ref"}, or
`Transform3D.interpolate_with()<class_Transform3D_method_interpolate_with>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_lerp_angle}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **lerp_angle**(from:
`float<class_float>`{.interpreted-text role="ref"}, to:
`float<class_float>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_lerp_angle>`{.interpreted-text role="ref"}

Linearly interpolates between two angles (in radians) by a `weight`
value between 0.0 and 1.0.

Similar to `lerp()<class_@GlobalScope_method_lerp>`{.interpreted-text
role="ref"}, but interpolates correctly when the angles wrap around
`@GDScript.TAU<class_@GDScript_constant_TAU>`{.interpreted-text
role="ref"}. To perform eased interpolation with
`lerp_angle()<class_@GlobalScope_method_lerp_angle>`{.interpreted-text
role="ref"}, combine it with
`ease()<class_@GlobalScope_method_ease>`{.interpreted-text role="ref"}
or
`smoothstep()<class_@GlobalScope_method_smoothstep>`{.interpreted-text
role="ref"}.

    extends Sprite
    var elapsed = 0.0
    func _process(delta):
        var min_angle = deg_to_rad(0.0)
        var max_angle = deg_to_rad(90.0)
        rotation = lerp_angle(min_angle, max_angle, elapsed)
        elapsed += delta

\*\*Note:\*\* This function lerps through the shortest path between
`from` and `to`. However, when these two angles are approximately
`PI + k * TAU` apart for any integer `k`, it\'s not obvious which way
they lerp due to floating-point precision errors. For example,
`lerp_angle(0, PI, weight)` lerps counter-clockwise, while
`lerp_angle(0, PI + 5 * TAU, weight)` lerps clockwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_lerpf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **lerpf**(from:
`float<class_float>`{.interpreted-text role="ref"}, to:
`float<class_float>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_lerpf>`{.interpreted-text role="ref"}

Linearly interpolates between two values by the factor defined in
`weight`. To perform interpolation, `weight` should be between `0.0` and
`1.0` (inclusive). However, values outside this range are allowed and
can be used to perform *extrapolation*. If this is not desired, use
`clampf()<class_@GlobalScope_method_clampf>`{.interpreted-text
role="ref"} on the result of this function.

    lerpf(0, 4, 0.75) # Returns 3.0

See also
`inverse_lerp()<class_@GlobalScope_method_inverse_lerp>`{.interpreted-text
role="ref"} which performs the reverse of this operation. To perform
eased interpolation with
`lerp()<class_@GlobalScope_method_lerp>`{.interpreted-text role="ref"},
combine it with
`ease()<class_@GlobalScope_method_ease>`{.interpreted-text role="ref"}
or
`smoothstep()<class_@GlobalScope_method_smoothstep>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_linear_to_db}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **linear_to_db**(lin:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_linear_to_db>`{.interpreted-text
role="ref"}

Converts from linear energy to decibels (audio). Since volume is not
normally linear, this can be used to implement volume sliders that
behave as expected.

\*\*Example:\*\* Change the Master bus\'s volume through a
`Slider<class_Slider>`{.interpreted-text role="ref"} node, which ranges
from `0.0` to `1.0`:

    AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Master"), linear_to_db($Slider.value))

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_log}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **log**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_log>`{.interpreted-text role="ref"}

Returns the [natural
logarithm](https://en.wikipedia.org/wiki/Natural_logarithm) of `x` (base
[\[i\]e\[/i\]](https://en.wikipedia.org/wiki/E_(mathematical_constant)),
with *e* being approximately 2.71828). This is the amount of time needed
to reach a certain level of continuous growth.

\*\*Note:\*\* This is not the same as the \"log\" function on most
calculators, which uses a base 10 logarithm. To use base 10 logarithm,
use `log(x) / log(10)`.

    log(10) # Returns 2.302585

\*\*Note:\*\* The logarithm of `0` returns `-inf`, while negative values
return `-nan`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_max}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **max**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_@GlobalScope_method_max>`{.interpreted-text
role="ref"}

Returns the maximum of the given numeric values. This function can take
any number of arguments.

    max(1, 7, 3, -6, 5) # Returns 7

\*\*Note:\*\* When using this on vectors it will *not* perform
component-wise maximum, and will pick the largest value when compared
using `x < y`. To perform component-wise maximum, use
`Vector2.max()<class_Vector2_method_max>`{.interpreted-text role="ref"},
`Vector2i.max()<class_Vector2i_method_max>`{.interpreted-text
role="ref"}, `Vector3.max()<class_Vector3_method_max>`{.interpreted-text
role="ref"},
`Vector3i.max()<class_Vector3i_method_max>`{.interpreted-text
role="ref"}, `Vector4.max()<class_Vector4_method_max>`{.interpreted-text
role="ref"}, and
`Vector4i.max()<class_Vector4i_method_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_maxf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **maxf**(a:
`float<class_float>`{.interpreted-text role="ref"}, b:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_maxf>`{.interpreted-text role="ref"}

Returns the maximum of two `float<class_float>`{.interpreted-text
role="ref"} values.

    maxf(3.6, 24)   # Returns 24.0
    maxf(-3.99, -4) # Returns -3.99

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_maxi}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **maxi**(a:
`int<class_int>`{.interpreted-text role="ref"}, b:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_maxi>`{.interpreted-text role="ref"}

Returns the maximum of two `int<class_int>`{.interpreted-text
role="ref"} values.

    maxi(1, 2)   # Returns 2
    maxi(-3, -4) # Returns -3

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_min}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **min**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_@GlobalScope_method_min>`{.interpreted-text
role="ref"}

Returns the minimum of the given numeric values. This function can take
any number of arguments.

    min(1, 7, 3, -6, 5) # Returns -6

\*\*Note:\*\* When using this on vectors it will *not* perform
component-wise minimum, and will pick the smallest value when compared
using `x < y`. To perform component-wise minimum, use
`Vector2.min()<class_Vector2_method_min>`{.interpreted-text role="ref"},
`Vector2i.min()<class_Vector2i_method_min>`{.interpreted-text
role="ref"}, `Vector3.min()<class_Vector3_method_min>`{.interpreted-text
role="ref"},
`Vector3i.min()<class_Vector3i_method_min>`{.interpreted-text
role="ref"}, `Vector4.min()<class_Vector4_method_min>`{.interpreted-text
role="ref"}, and
`Vector4i.min()<class_Vector4i_method_min>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_minf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **minf**(a:
`float<class_float>`{.interpreted-text role="ref"}, b:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_minf>`{.interpreted-text role="ref"}

Returns the minimum of two `float<class_float>`{.interpreted-text
role="ref"} values.

    minf(3.6, 24)   # Returns 3.6
    minf(-3.99, -4) # Returns -4.0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_mini}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **mini**(a:
`int<class_int>`{.interpreted-text role="ref"}, b:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_mini>`{.interpreted-text role="ref"}

Returns the minimum of two `int<class_int>`{.interpreted-text
role="ref"} values.

    mini(1, 2)   # Returns 1
    mini(-3, -4) # Returns -4

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_move_toward}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **move_toward**(from:
`float<class_float>`{.interpreted-text role="ref"}, to:
`float<class_float>`{.interpreted-text role="ref"}, delta:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_move_toward>`{.interpreted-text
role="ref"}

Moves `from` toward `to` by the `delta` amount. Will not go past `to`.

Use a negative `delta` value to move away.

    move_toward(5, 10, 4)    # Returns 9
    move_toward(10, 5, 4)    # Returns 6
    move_toward(5, 10, 9)    # Returns 10
    move_toward(10, 5, -1.5) # Returns 11.5

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_nearest_po2}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **nearest_po2**(value:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_nearest_po2>`{.interpreted-text
role="ref"}

Returns the smallest integer power of 2 that is greater than or equal to
`value`.

    nearest_po2(3) # Returns 4
    nearest_po2(4) # Returns 4
    nearest_po2(5) # Returns 8

    nearest_po2(0)  # Returns 0 (this may not be expected)
    nearest_po2(-1) # Returns 0 (this may not be expected)

\*\*Warning:\*\* Due to its implementation, this method returns `0`
rather than `1` for values less than or equal to `0`, with an exception
for `value` being the smallest negative 64-bit integer
(`-9223372036854775808`) in which case the `value` is returned
unchanged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_pingpong}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pingpong**(value:
`float<class_float>`{.interpreted-text role="ref"}, length:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_pingpong>`{.interpreted-text role="ref"}

Wraps `value` between `0` and the `length`. If the limit is reached, the
next value the function returns is decreased to the `0` side or
increased to the `length` side (like a triangle wave). If `length` is
less than zero, it becomes positive.

    pingpong(-3.0, 3.0) # Returns 3.0
    pingpong(-2.0, 3.0) # Returns 2.0
    pingpong(-1.0, 3.0) # Returns 1.0
    pingpong(0.0, 3.0)  # Returns 0.0
    pingpong(1.0, 3.0)  # Returns 1.0
    pingpong(2.0, 3.0)  # Returns 2.0
    pingpong(3.0, 3.0)  # Returns 3.0
    pingpong(4.0, 3.0)  # Returns 2.0
    pingpong(5.0, 3.0)  # Returns 1.0
    pingpong(6.0, 3.0)  # Returns 0.0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_posmod}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **posmod**(x:
`int<class_int>`{.interpreted-text role="ref"}, y:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_posmod>`{.interpreted-text role="ref"}

Returns the integer modulus of `x` divided by `y` that wraps equally in
positive and negative.

    print("#(i)  (i % 3)   (posmod(i, 3))")
    for i in range(-3, 4):
        print("%2d       %2d  | %2d" % [i, i % 3, posmod(i, 3)])

Prints:

``` text
(i)  (i % 3)   (posmod(i, 3))
-3        0  |  0
-2       -2  |  1
-1       -1  |  2
 0        0  |  0
 1        1  |  1
 2        2  |  2
 3        0  |  0
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_pow}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pow**(base:
`float<class_float>`{.interpreted-text role="ref"}, exp:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_pow>`{.interpreted-text role="ref"}

Returns the result of `base` raised to the power of `exp`.

In GDScript, this is the equivalent of the `**` operator.

    pow(2, 5)   # Returns 32.0
    pow(4, 1.5) # Returns 8.0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_print}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **print**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_@GlobalScope_method_print>`{.interpreted-text
role="ref"}

Converts one or more arguments of any type to string in the best way
possible and prints them to the console.

::::: tabs
::: code-tab
gdscript

var a = \[1, 2, 3\] print(\"a\", \"b\", a) \# Prints \"ab\[1, 2, 3\]\"
:::

::: code-tab
csharp

Godot.Collections.Array a = \[1, 2, 3\]; GD.Print(\"a\", \"b\", a); //
Prints \"ab\[1, 2, 3\]\"
:::
:::::

\*\*Note:\*\* Consider using
`push_error()<class_@GlobalScope_method_push_error>`{.interpreted-text
role="ref"} and
`push_warning()<class_@GlobalScope_method_push_warning>`{.interpreted-text
role="ref"} to print error and warning messages instead of
`print()<class_@GlobalScope_method_print>`{.interpreted-text role="ref"}
or
`print_rich()<class_@GlobalScope_method_print_rich>`{.interpreted-text
role="ref"}. This distinguishes them from print messages used for
debugging purposes, while also displaying a stack trace when an error or
warning is printed. See also
`Engine.print_to_stdout<class_Engine_property_print_to_stdout>`{.interpreted-text
role="ref"} and
`ProjectSettings.application/run/disable_stdout<class_ProjectSettings_property_application/run/disable_stdout>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_print_rich}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**print_rich**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_@GlobalScope_method_print_rich>`{.interpreted-text role="ref"}

Converts one or more arguments of any type to string in the best way
possible and prints them to the console.

The following BBCode tags are supported: `b`, `i`, `u`, `s`, `indent`,
`code`, `url`, `center`, `right`, `color`, `bgcolor`, `fgcolor`.

URL tags only support URLs wrapped by a URL tag, not URLs with a
different title.

When printing to standard output, the supported subset of BBCode is
converted to ANSI escape codes for the terminal emulator to display.
Support for ANSI escape codes varies across terminal emulators,
especially for italic and strikethrough. In standard output, `code` is
represented with faint text but without any font change. Unsupported
tags are left as-is in standard output.

::::: tabs
::: code-tab
gdscript

print_rich(\"\[color=green\]\[b\]Hello world\![/b\]\[/color\]\") \#
Prints \"Hello world!\", in green with a bold font.
:::

::: code-tab
csharp

GD.PrintRich(\"\[color=green\]\[b\]Hello world\![/b\]\[/color\]\"); //
Prints \"Hello world!\", in green with a bold font.
:::
:::::

\*\*Note:\*\* Consider using
`push_error()<class_@GlobalScope_method_push_error>`{.interpreted-text
role="ref"} and
`push_warning()<class_@GlobalScope_method_push_warning>`{.interpreted-text
role="ref"} to print error and warning messages instead of
`print()<class_@GlobalScope_method_print>`{.interpreted-text role="ref"}
or
`print_rich()<class_@GlobalScope_method_print_rich>`{.interpreted-text
role="ref"}. This distinguishes them from print messages used for
debugging purposes, while also displaying a stack trace when an error or
warning is printed.

\*\*Note:\*\* Output displayed in the editor supports clickable
`[url=address]text[/url]` tags. The `[url]` tag\'s `address` value is
handled by
`OS.shell_open()<class_OS_method_shell_open>`{.interpreted-text
role="ref"} when clicked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_print_verbose}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**print_verbose**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_@GlobalScope_method_print_verbose>`{.interpreted-text
role="ref"}

If verbose mode is enabled
(`OS.is_stdout_verbose()<class_OS_method_is_stdout_verbose>`{.interpreted-text
role="ref"} returning `true`), converts one or more arguments of any
type to string in the best way possible and prints them to the console.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_printerr}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**printerr**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_@GlobalScope_method_printerr>`{.interpreted-text
role="ref"}

Prints one or more arguments to strings in the best way possible to
standard error line.

::::: tabs
::: code-tab
gdscript

printerr(\"prints to stderr\")
:::

::: code-tab
csharp

GD.PrintErr(\"prints to stderr\");
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_printraw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**printraw**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_@GlobalScope_method_printraw>`{.interpreted-text
role="ref"}

Prints one or more arguments to strings in the best way possible to the
OS terminal. Unlike
`print()<class_@GlobalScope_method_print>`{.interpreted-text
role="ref"}, no newline is automatically added at the end.

\*\*Note:\*\* The OS terminal is *not* the same as the editor\'s Output
dock. The output sent to the OS terminal can be seen when running Godot
from a terminal. On Windows, this requires using the `console.exe`
executable.

::::: tabs
::: code-tab
gdscript

\# Prints \"ABC\" to terminal. printraw(\"A\") printraw(\"B\")
printraw(\"C\")
:::

::: code-tab
csharp

// Prints \"ABC\" to terminal. GD.PrintRaw(\"A\"); GD.PrintRaw(\"B\");
GD.PrintRaw(\"C\");
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_prints}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**prints**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_@GlobalScope_method_prints>`{.interpreted-text
role="ref"}

Prints one or more arguments to the console with a space between each
argument.

::::: tabs
::: code-tab
gdscript

prints(\"A\", \"B\", \"C\") \# Prints \"A B C\"
:::

::: code-tab
csharp

GD.PrintS(\"A\", \"B\", \"C\"); // Prints \"A B C\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_printt}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**printt**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_@GlobalScope_method_printt>`{.interpreted-text
role="ref"}

Prints one or more arguments to the console with a tab between each
argument.

::::: tabs
::: code-tab
gdscript

printt(\"A\", \"B\", \"C\") \# Prints \"A B C\"
:::

::: code-tab
csharp

GD.PrintT(\"A\", \"B\", \"C\"); // Prints \"A B C\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_push_error}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_error**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_@GlobalScope_method_push_error>`{.interpreted-text role="ref"}

Pushes an error message to Godot\'s built-in debugger and to the OS
terminal.

::::: tabs
::: code-tab
gdscript

push_error(\"test error\") \# Prints \"test error\" to debugger and
terminal as an error.
:::

::: code-tab
csharp

GD.PushError(\"test error\"); // Prints \"test error\" to debugger and
terminal as an error.
:::
:::::

\*\*Note:\*\* This function does not pause project execution. To print
an error message and pause project execution in debug builds, use
`assert(false, "test error")` instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_push_warning}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_warning**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_@GlobalScope_method_push_warning>`{.interpreted-text
role="ref"}

Pushes a warning message to Godot\'s built-in debugger and to the OS
terminal.

::::: tabs
::: code-tab
gdscript

push_warning(\"test warning\") \# Prints \"test warning\" to debugger
and terminal as a warning.
:::

::: code-tab
csharp

GD.PushWarning(\"test warning\"); // Prints \"test warning\" to debugger
and terminal as a warning.
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_rad_to_deg}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **rad_to_deg**(rad:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_rad_to_deg>`{.interpreted-text role="ref"}

Converts an angle expressed in radians to degrees.

    rad_to_deg(0.523599) # Returns 30
    rad_to_deg(PI)       # Returns 180
    rad_to_deg(PI * 2)   # Returns 360

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_rand_from_seed}
::: rst-class
classref-method
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**rand_from_seed**(seed: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_rand_from_seed>`{.interpreted-text
role="ref"}

Given a `seed`, returns a
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
of size `2`, where its first element is the randomized
`int<class_int>`{.interpreted-text role="ref"} value, and the second
element is the same as `seed`. Passing the same `seed` consistently
returns the same array.

\*\*Note:\*\* \"Seed\" here refers to the internal state of the pseudo
random number generator, currently implemented as a 64 bit integer.

    var a = rand_from_seed(4)

    print(a[0]) # Prints 2879024997
    print(a[1]) # Prints 4

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_randf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **randf**()
`🔗<class_@GlobalScope_method_randf>`{.interpreted-text role="ref"}

Returns a random floating-point value between `0.0` and `1.0`
(inclusive).

::::: tabs
::: code-tab
gdscript

randf() \# Returns e.g. 0.375671
:::

::: code-tab
csharp

GD.Randf(); // Returns e.g. 0.375671
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_randf_range}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **randf_range**(from:
`float<class_float>`{.interpreted-text role="ref"}, to:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_randf_range>`{.interpreted-text
role="ref"}

Returns a random floating-point value between `from` and `to`
(inclusive).

::::: tabs
::: code-tab
gdscript

randf_range(0, 20.5) \# Returns e.g. 7.45315 randf_range(-10, 10) \#
Returns e.g. -3.844535
:::

::: code-tab
csharp

GD.RandRange(0.0, 20.5); // Returns e.g. 7.45315 GD.RandRange(-10.0,
10.0); // Returns e.g. -3.844535
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_randfn}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **randfn**(mean:
`float<class_float>`{.interpreted-text role="ref"}, deviation:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_randfn>`{.interpreted-text role="ref"}

Returns a
[normally-distributed](https://en.wikipedia.org/wiki/Normal_distribution),
pseudo-random floating-point value from the specified `mean` and a
standard `deviation`. This is also known as a Gaussian distribution.

\*\*Note:\*\* This method uses the [Box-Muller
transform](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform)
algorithm.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_randi}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **randi**()
`🔗<class_@GlobalScope_method_randi>`{.interpreted-text role="ref"}

Returns a random unsigned 32-bit integer. Use remainder to obtain a
random value in the interval `[0, N - 1]` (where N is smaller than
2\^32).

::::: tabs
::: code-tab
gdscript

randi() \# Returns random integer between 0 and 2\^32 - 1 randi() % 20
\# Returns random integer between 0 and 19 randi() % 100 \# Returns
random integer between 0 and 99 randi() % 100 + 1 \# Returns random
integer between 1 and 100
:::

::: code-tab
csharp

GD.Randi(); // Returns random integer between 0 and 2\^32 - 1 GD.Randi()
% 20; // Returns random integer between 0 and 19 GD.Randi() % 100; //
Returns random integer between 0 and 99 GD.Randi() % 100 + 1; // Returns
random integer between 1 and 100
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_randi_range}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **randi_range**(from:
`int<class_int>`{.interpreted-text role="ref"}, to:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_randi_range>`{.interpreted-text
role="ref"}

Returns a random signed 32-bit integer between `from` and `to`
(inclusive). If `to` is lesser than `from`, they are swapped.

::::: tabs
::: code-tab
gdscript

randi_range(0, 1) \# Returns either 0 or 1 randi_range(-10, 1000) \#
Returns random integer between -10 and 1000
:::

::: code-tab
csharp

GD.RandRange(0, 1); // Returns either 0 or 1 GD.RandRange(-10, 1000); //
Returns random integer between -10 and 1000
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_randomize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **randomize**()
`🔗<class_@GlobalScope_method_randomize>`{.interpreted-text role="ref"}

Randomizes the seed (or the internal state) of the random number
generator. The current implementation uses a number based on the
device\'s time.

\*\*Note:\*\* This function is called automatically when the project is
run. If you need to fix the seed to have consistent, reproducible
results, use `seed()<class_@GlobalScope_method_seed>`{.interpreted-text
role="ref"} to initialize the random number generator.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_remap}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **remap**(value:
`float<class_float>`{.interpreted-text role="ref"}, istart:
`float<class_float>`{.interpreted-text role="ref"}, istop:
`float<class_float>`{.interpreted-text role="ref"}, ostart:
`float<class_float>`{.interpreted-text role="ref"}, ostop:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_remap>`{.interpreted-text role="ref"}

Maps a `value` from range `[istart, istop]` to `[ostart, ostop]`. See
also `lerp()<class_@GlobalScope_method_lerp>`{.interpreted-text
role="ref"} and
`inverse_lerp()<class_@GlobalScope_method_inverse_lerp>`{.interpreted-text
role="ref"}. If `value` is outside `[istart, istop]`, then the resulting
value will also be outside `[ostart, ostop]`. If this is not desired,
use `clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on the result of this function.

    remap(75, 0, 100, -1, 1) # Returns 0.5

For complex use cases where multiple ranges are needed, consider using
`Curve<class_Curve>`{.interpreted-text role="ref"} or
`Gradient<class_Gradient>`{.interpreted-text role="ref"} instead.

\*\*Note:\*\* If `istart == istop`, the return value is undefined (most
likely NaN, INF, or -INF).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_rid_allocate_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rid_allocate_id**()
`🔗<class_@GlobalScope_method_rid_allocate_id>`{.interpreted-text
role="ref"}

Allocates a unique ID which can be used by the implementation to
construct an RID. This is used mainly from native extensions to
implement servers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_rid_from_int64}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **rid_from_int64**(base:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_rid_from_int64>`{.interpreted-text
role="ref"}

Creates an RID from a `base`. This is used mainly from native extensions
to build servers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_rotate_toward}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**rotate_toward**(from: `float<class_float>`{.interpreted-text
role="ref"}, to: `float<class_float>`{.interpreted-text role="ref"},
delta: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_rotate_toward>`{.interpreted-text
role="ref"}

Rotates `from` toward `to` by the `delta` amount. Will not go past `to`.

Similar to
`move_toward()<class_@GlobalScope_method_move_toward>`{.interpreted-text
role="ref"}, but interpolates correctly when the angles wrap around
`@GDScript.TAU<class_@GDScript_constant_TAU>`{.interpreted-text
role="ref"}.

If `delta` is negative, this function will rotate away from `to`, toward
the opposite angle, and will not go past the opposite angle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_round}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **round**(x:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_round>`{.interpreted-text role="ref"}

Rounds `x` to the nearest whole number, with halfway cases rounded away
from 0. Supported types: `int<class_int>`{.interpreted-text role="ref"},
`float<class_float>`{.interpreted-text role="ref"},
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"},
`Vector4<class_Vector4>`{.interpreted-text role="ref"},
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}.

    round(2.4) # Returns 2
    round(2.5) # Returns 3
    round(2.6) # Returns 3

See also `floor()<class_@GlobalScope_method_floor>`{.interpreted-text
role="ref"}, `ceil()<class_@GlobalScope_method_ceil>`{.interpreted-text
role="ref"}, and
`snapped()<class_@GlobalScope_method_snapped>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For better type safety, use
`roundf()<class_@GlobalScope_method_roundf>`{.interpreted-text
role="ref"},
`roundi()<class_@GlobalScope_method_roundi>`{.interpreted-text
role="ref"},
`Vector2.round()<class_Vector2_method_round>`{.interpreted-text
role="ref"},
`Vector3.round()<class_Vector3_method_round>`{.interpreted-text
role="ref"}, or
`Vector4.round()<class_Vector4_method_round>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_roundf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **roundf**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_roundf>`{.interpreted-text role="ref"}

Rounds `x` to the nearest whole number, with halfway cases rounded away
from 0.

A type-safe version of
`round()<class_@GlobalScope_method_round>`{.interpreted-text
role="ref"}, returning a `float<class_float>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_roundi}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **roundi**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_roundi>`{.interpreted-text role="ref"}

Rounds `x` to the nearest whole number, with halfway cases rounded away
from 0.

A type-safe version of
`round()<class_@GlobalScope_method_round>`{.interpreted-text
role="ref"}, returning an `int<class_int>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_seed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **seed**(base:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_seed>`{.interpreted-text role="ref"}

Sets the seed for the random number generator to `base`. Setting the
seed manually can ensure consistent, repeatable results for most random
functions.

::::: tabs
::: code-tab
gdscript

var my_seed = \"Godot Rocks\".hash() seed(my_seed) var a = randf() +
randi() seed(my_seed) var b = randf() + randi() \# a and b are now
identical
:::

::: code-tab
csharp

ulong mySeed = (ulong)GD.Hash(\"Godot Rocks\"); GD.Seed(mySeed); var a =
GD.Randf() + GD.Randi(); GD.Seed(mySeed); var b = GD.Randf() +
GD.Randi(); // a and b are now identical
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_sign}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **sign**(x:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_sign>`{.interpreted-text role="ref"}

Returns the same type of `Variant<class_Variant>`{.interpreted-text
role="ref"} as `x`, with `-1` for negative values, `1` for positive
values, and `0` for zeros. For `nan` values it returns 0.

Supported types: `int<class_int>`{.interpreted-text role="ref"},
`float<class_float>`{.interpreted-text role="ref"},
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"},
`Vector4<class_Vector4>`{.interpreted-text role="ref"},
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}.

    sign(-6.0) # Returns -1
    sign(0.0)  # Returns 0
    sign(6.0)  # Returns 1
    sign(NAN)  # Returns 0

    sign(Vector3(-6.0, 0.0, 6.0)) # Returns (-1, 0, 1)

\*\*Note:\*\* For better type safety, use
`signf()<class_@GlobalScope_method_signf>`{.interpreted-text
role="ref"},
`signi()<class_@GlobalScope_method_signi>`{.interpreted-text
role="ref"},
`Vector2.sign()<class_Vector2_method_sign>`{.interpreted-text
role="ref"},
`Vector2i.sign()<class_Vector2i_method_sign>`{.interpreted-text
role="ref"},
`Vector3.sign()<class_Vector3_method_sign>`{.interpreted-text
role="ref"},
`Vector3i.sign()<class_Vector3i_method_sign>`{.interpreted-text
role="ref"},
`Vector4.sign()<class_Vector4_method_sign>`{.interpreted-text
role="ref"}, or
`Vector4i.sign()<class_Vector4i_method_sign>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_signf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **signf**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_signf>`{.interpreted-text role="ref"}

Returns `-1.0` if `x` is negative, `1.0` if `x` is positive, and `0.0`
if `x` is zero. For `nan` values of `x` it returns 0.0.

    signf(-6.5) # Returns -1.0
    signf(0.0)  # Returns 0.0
    signf(6.5)  # Returns 1.0
    signf(NAN)  # Returns 0.0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_signi}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **signi**(x:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_signi>`{.interpreted-text role="ref"}

Returns `-1` if `x` is negative, `1` if `x` is positive, and `0` if `x`
is zero.

    signi(-6) # Returns -1
    signi(0)  # Returns 0
    signi(6)  # Returns 1

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_sin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sin**(angle_rad:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_sin>`{.interpreted-text role="ref"}

Returns the sine of angle `angle_rad` in radians.

    sin(0.523599)       # Returns 0.5
    sin(deg_to_rad(90)) # Returns 1.0

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_sinh}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sinh**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_sinh>`{.interpreted-text role="ref"}

Returns the hyperbolic sine of `x`.

    var a = log(2.0) # Returns 0.693147
    sinh(a) # Returns 0.75

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_smoothstep}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **smoothstep**(from:
`float<class_float>`{.interpreted-text role="ref"}, to:
`float<class_float>`{.interpreted-text role="ref"}, x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_smoothstep>`{.interpreted-text role="ref"}

Returns a smooth cubic Hermite interpolation between `0` and `1`.

For positive ranges (when `from <= to`) the return value is `0` when
`x <= from`, and `1` when `x >= to`. If `x` lies between `from` and
`to`, the return value follows an S-shaped curve that smoothly
transitions from `0` to `1`.

For negative ranges (when `from > to`) the function is mirrored and
returns `1` when `x <= to` and `0` when `x >= from`.

This S-shaped curve is the cubic Hermite interpolator, given by
`f(y) = 3*y^2 - 2*y^3` where `y = (x-from) / (to-from)`.

    smoothstep(0, 2, -5.0) # Returns 0.0
    smoothstep(0, 2, 0.5) # Returns 0.15625
    smoothstep(0, 2, 1.0) # Returns 0.5
    smoothstep(0, 2, 2.0) # Returns 1.0

Compared to `ease()<class_@GlobalScope_method_ease>`{.interpreted-text
role="ref"} with a curve value of `-1.6521`,
`smoothstep()<class_@GlobalScope_method_smoothstep>`{.interpreted-text
role="ref"} returns the smoothest possible curve with no sudden changes
in the derivative. If you need to perform more advanced transitions, use
`Tween<class_Tween>`{.interpreted-text role="ref"} or
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}.

\`Comparison between smoothstep() and ease(x, -1.6521) return values
\<https://raw.githubusercontent.com/godotengine/godot-docs/master/img/smoothstep_ease_comparison.png\>\`\_\_

\`Smoothstep() return values with positive, zero, and negative ranges
\<https://raw.githubusercontent.com/godotengine/godot-docs/master/img/smoothstep_range.webp\>\`\_\_

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_snapped}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **snapped**(x:
`Variant<class_Variant>`{.interpreted-text role="ref"}, step:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_snapped>`{.interpreted-text role="ref"}

Returns the multiple of `step` that is the closest to `x`. This can also
be used to round a floating-point number to an arbitrary number of
decimals.

The returned value is the same type of
`Variant<class_Variant>`{.interpreted-text role="ref"} as `step`.
Supported types: `int<class_int>`{.interpreted-text role="ref"},
`float<class_float>`{.interpreted-text role="ref"},
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"},
`Vector4<class_Vector4>`{.interpreted-text role="ref"},
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"}.

    snapped(100, 32)  # Returns 96
    snapped(3.14159, 0.01)  # Returns 3.14

    snapped(Vector2(34, 70), Vector2(8, 8))  # Returns (32, 72)

See also `ceil()<class_@GlobalScope_method_ceil>`{.interpreted-text
role="ref"},
`floor()<class_@GlobalScope_method_floor>`{.interpreted-text
role="ref"}, and
`round()<class_@GlobalScope_method_round>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For better type safety, use
`snappedf()<class_@GlobalScope_method_snappedf>`{.interpreted-text
role="ref"},
`snappedi()<class_@GlobalScope_method_snappedi>`{.interpreted-text
role="ref"},
`Vector2.snapped()<class_Vector2_method_snapped>`{.interpreted-text
role="ref"},
`Vector2i.snapped()<class_Vector2i_method_snapped>`{.interpreted-text
role="ref"},
`Vector3.snapped()<class_Vector3_method_snapped>`{.interpreted-text
role="ref"},
`Vector3i.snapped()<class_Vector3i_method_snapped>`{.interpreted-text
role="ref"},
`Vector4.snapped()<class_Vector4_method_snapped>`{.interpreted-text
role="ref"}, or
`Vector4i.snapped()<class_Vector4i_method_snapped>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_snappedf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **snappedf**(x:
`float<class_float>`{.interpreted-text role="ref"}, step:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_snappedf>`{.interpreted-text role="ref"}

Returns the multiple of `step` that is the closest to `x`. This can also
be used to round a floating-point number to an arbitrary number of
decimals.

A type-safe version of
`snapped()<class_@GlobalScope_method_snapped>`{.interpreted-text
role="ref"}, returning a `float<class_float>`{.interpreted-text
role="ref"}.

    snappedf(32.0, 2.5)  # Returns 32.5
    snappedf(3.14159, 0.01)  # Returns 3.14

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_snappedi}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **snappedi**(x:
`float<class_float>`{.interpreted-text role="ref"}, step:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_snappedi>`{.interpreted-text role="ref"}

Returns the multiple of `step` that is the closest to `x`.

A type-safe version of
`snapped()<class_@GlobalScope_method_snapped>`{.interpreted-text
role="ref"}, returning an `int<class_int>`{.interpreted-text
role="ref"}.

    snappedi(53, 16)  # Returns 48
    snappedi(4096, 100)  # Returns 4100

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_sqrt}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sqrt**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_sqrt>`{.interpreted-text role="ref"}

Returns the square root of `x`, where `x` is a non-negative number.

    sqrt(9)     # Returns 3
    sqrt(10.24) # Returns 3.2
    sqrt(-1)    # Returns NaN

\*\*Note:\*\* Negative values of `x` return NaN (\"Not a Number\"). In
C#, if you need negative inputs, use `System.Numerics.Complex`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_step_decimals}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **step_decimals**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_step_decimals>`{.interpreted-text
role="ref"}

Returns the position of the first non-zero digit, after the decimal
point. Note that the maximum return value is 10, which is a design
decision in the implementation.

    var n = step_decimals(5)       # n is 0
    n = step_decimals(1.0005)      # n is 4
    n = step_decimals(0.000000005) # n is 9

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_str}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **str**(\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_@GlobalScope_method_str>`{.interpreted-text
role="ref"}

Converts one or more arguments of any
`Variant<class_Variant>`{.interpreted-text role="ref"} type to a
`String<class_String>`{.interpreted-text role="ref"} in the best way
possible.

    var a = [10, 20, 30]
    var b = str(a)
    print(len(a)) # Prints 3 (the number of elements in the array).
    print(len(b)) # Prints 12 (the length of the string "[10, 20, 30]").

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_str_to_var}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**str_to_var**(string: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_@GlobalScope_method_str_to_var>`{.interpreted-text role="ref"}

Converts a formatted `string` that was returned by
`var_to_str()<class_@GlobalScope_method_var_to_str>`{.interpreted-text
role="ref"} to the original `Variant<class_Variant>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var data = \'{ \"a\": 1, \"b\": 2 }\' \# data is a String var dict =
str_to_var(data) \# dict is a Dictionary print(dict\[\"a\"\]) \# Prints
1
:::

::: code-tab
csharp

string data = \"{ \"a\": 1, \"b\": 2 }\"; // data is a string var dict =
GD.StrToVar(data).AsGodotDictionary(); // dict is a Dictionary
GD.Print(dict\[\"a\"\]); // Prints 1
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_tan}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tan**(angle_rad:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_tan>`{.interpreted-text role="ref"}

Returns the tangent of angle `angle_rad` in radians.

    tan(deg_to_rad(45)) # Returns 1

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_tanh}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **tanh**(x:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_tanh>`{.interpreted-text role="ref"}

Returns the hyperbolic tangent of `x`.

    var a = log(2.0) # Returns 0.693147
    tanh(a)          # Returns 0.6

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_type_convert}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**type_convert**(variant: `Variant<class_Variant>`{.interpreted-text
role="ref"}, type: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_type_convert>`{.interpreted-text
role="ref"}

Converts the given `variant` to the given `type`, using the
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} values. This method is generous with how it handles types,
it can automatically convert between array types, convert numeric
`String<class_String>`{.interpreted-text role="ref"}s to
`int<class_int>`{.interpreted-text role="ref"}, and converting most
things to `String<class_String>`{.interpreted-text role="ref"}.

If the type conversion cannot be done, this method will return the
default value for that type, for example converting
`Rect2<class_Rect2>`{.interpreted-text role="ref"} to
`Vector2<class_Vector2>`{.interpreted-text role="ref"} will always
return `Vector2.ZERO<class_Vector2_constant_ZERO>`{.interpreted-text
role="ref"}. This method will never show error messages as long as
`type` is a valid Variant type.

The returned value is a `Variant<class_Variant>`{.interpreted-text
role="ref"}, but the data inside and its type will be the same as the
requested type.

    type_convert("Hi!", TYPE_INT) # Returns 0
    type_convert("123", TYPE_INT) # Returns 123
    type_convert(123.4, TYPE_INT) # Returns 123
    type_convert(5, TYPE_VECTOR2) # Returns (0, 0)
    type_convert("Hi!", TYPE_NIL) # Returns null

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_type_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**type_string**(type: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_type_string>`{.interpreted-text
role="ref"}

Returns a human-readable name of the given `type`, using the
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} values.

    print(TYPE_INT) # Prints 2
    print(type_string(TYPE_INT)) # Prints "int"
    print(type_string(TYPE_STRING)) # Prints "String"

See also `typeof()<class_@GlobalScope_method_typeof>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_typeof}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **typeof**(variable:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_typeof>`{.interpreted-text role="ref"}

Returns the internal type of the given `variable`, using the
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} values.

    var json = JSON.new()
    json.parse('["a", "b", "c"]')
    var result = json.get_data()
    if result is Array:
        print(result[0]) # Prints "a"
    else:
        print("Unexpected result!")

See also
`type_string()<class_@GlobalScope_method_type_string>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_var_to_bytes}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**var_to_bytes**(variable: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_@GlobalScope_method_var_to_bytes>`{.interpreted-text
role="ref"}

Encodes a `Variant<class_Variant>`{.interpreted-text role="ref"} value
to a byte array, without encoding objects. Deserialization can be done
with
`bytes_to_var()<class_@GlobalScope_method_bytes_to_var>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If you need object serialization, see
`var_to_bytes_with_objects()<class_@GlobalScope_method_var_to_bytes_with_objects>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Encoding `Callable<class_Callable>`{.interpreted-text
role="ref"} is not supported and will result in an empty value,
regardless of the data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_var_to_bytes_with_objects}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**var_to_bytes_with_objects**(variable:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_var_to_bytes_with_objects>`{.interpreted-text
role="ref"}

Encodes a `Variant<class_Variant>`{.interpreted-text role="ref"} value
to a byte array. Encoding objects is allowed (and can potentially
include executable code). Deserialization can be done with
`bytes_to_var_with_objects()<class_@GlobalScope_method_bytes_to_var_with_objects>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Encoding `Callable<class_Callable>`{.interpreted-text
role="ref"} is not supported and will result in an empty value,
regardless of the data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_var_to_str}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**var_to_str**(variable: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_@GlobalScope_method_var_to_str>`{.interpreted-text role="ref"}

Converts a `Variant<class_Variant>`{.interpreted-text role="ref"}
`variable` to a formatted `String<class_String>`{.interpreted-text
role="ref"} that can then be parsed using
`str_to_var()<class_@GlobalScope_method_str_to_var>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var a = { \"a\": 1, \"b\": 2 } print(var_to_str(a))
:::

::: code-tab
csharp

var a = new Godot.Collections.Dictionary { \[\"a\"\] = 1, \[\"b\"\] = 2
}; GD.Print(GD.VarToStr(a));
:::
:::::

Prints:

``` text
{
    "a": 1,
    "b": 2
}
```

\*\*Note:\*\* Converting `Signal<class_Signal>`{.interpreted-text
role="ref"} or `Callable<class_Callable>`{.interpreted-text role="ref"}
is not supported and will result in an empty value for these types,
regardless of their data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_weakref}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **weakref**(obj:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_weakref>`{.interpreted-text role="ref"}

Returns a `WeakRef<class_WeakRef>`{.interpreted-text role="ref"}
instance holding a weak reference to `obj`. Returns an empty
`WeakRef<class_WeakRef>`{.interpreted-text role="ref"} instance if `obj`
is `null`. Prints an error and returns `null` if `obj` is neither
`Object<class_Object>`{.interpreted-text role="ref"}-derived nor `null`.

A weak reference to an object is not enough to keep the object alive:
when the only remaining references to a referent are weak references,
garbage collection is free to destroy the referent and reuse its memory
for something else. However, until the object is actually destroyed the
weak reference may return the object even if there are no strong
references to it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_wrap}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **wrap**(value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, min:
`Variant<class_Variant>`{.interpreted-text role="ref"}, max:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_wrap>`{.interpreted-text role="ref"}

Wraps the `Variant<class_Variant>`{.interpreted-text role="ref"} `value`
between `min` and `max`. `min` is *inclusive* while `max` is
*exclusive*. This can be used for creating loop-like behavior or
infinite surfaces.

Variant types `int<class_int>`{.interpreted-text role="ref"} and
`float<class_float>`{.interpreted-text role="ref"} are supported. If any
of the arguments is `float<class_float>`{.interpreted-text role="ref"},
this function returns a `float<class_float>`{.interpreted-text
role="ref"}, otherwise it returns an `int<class_int>`{.interpreted-text
role="ref"}.

    var a = wrap(4, 5, 10)
    # a is 9 (int)

    var a = wrap(7, 5, 10)
    # a is 7 (int)

    var a = wrap(10.5, 5, 10)
    # a is 5.5 (float)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_wrapf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **wrapf**(value:
`float<class_float>`{.interpreted-text role="ref"}, min:
`float<class_float>`{.interpreted-text role="ref"}, max:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_wrapf>`{.interpreted-text role="ref"}

Wraps the float `value` between `min` and `max`. `min` is *inclusive*
while `max` is *exclusive*. This can be used for creating loop-like
behavior or infinite surfaces.

    # Infinite loop between 5.0 and 9.9
    value = wrapf(value + 0.1, 5.0, 10.0)

    # Infinite rotation (in radians)
    angle = wrapf(angle + 0.1, 0.0, TAU)

    # Infinite rotation (in radians)
    angle = wrapf(angle + 0.1, -PI, PI)

\*\*Note:\*\* If `min` is `0`, this is equivalent to
`fposmod()<class_@GlobalScope_method_fposmod>`{.interpreted-text
role="ref"}, so prefer using that instead.
`wrapf()<class_@GlobalScope_method_wrapf>`{.interpreted-text role="ref"}
is more flexible than using the
`fposmod()<class_@GlobalScope_method_fposmod>`{.interpreted-text
role="ref"} approach by giving the user control over the minimum value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_@GlobalScope_method_wrapi}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **wrapi**(value:
`int<class_int>`{.interpreted-text role="ref"}, min:
`int<class_int>`{.interpreted-text role="ref"}, max:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_@GlobalScope_method_wrapi>`{.interpreted-text role="ref"}

Wraps the integer `value` between `min` and `max`. `min` is *inclusive*
while `max` is *exclusive*. This can be used for creating loop-like
behavior or infinite surfaces.

    # Infinite loop between 5 and 9
    frame = wrapi(frame + 1, 5, 10)

    # result is -2
    var result = wrapi(-6, -5, -1)
