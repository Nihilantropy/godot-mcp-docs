github_url
:   hide

# XRFaceTracker {#class_XRFaceTracker}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `XRTracker<class_XRTracker>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A tracked face.

::: rst-class
classref-introduction-group
:::

## Description

An instance of this object represents a tracked face and its
corresponding blend shapes. The blend shapes come from the [Unified
Expressions](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/unified-blendshapes)
standard, and contain extended details and visuals for each blend shape.
Additionally the [Tracking Standard
Comparison](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/compatibility/overview)
page documents the relationship between Unified Expressions and other
standards.

As face trackers are turned on they are registered with the
`XRServer<class_XRServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `XR documentation index <../tutorials/xr/index>`{.interpreted-text
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

:::: {#enum_XRFaceTracker_BlendShapeEntry}
::: rst-class
classref-enumeration
:::
::::

enum **BlendShapeEntry**:
`🔗<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text role="ref"}

:::: {#class_XRFaceTracker_constant_FT_EYE_LOOK_OUT_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_LOOK_OUT_RIGHT** = `0`

Right eye looks outwards.

:::: {#class_XRFaceTracker_constant_FT_EYE_LOOK_IN_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_LOOK_IN_RIGHT** = `1`

Right eye looks inwards.

:::: {#class_XRFaceTracker_constant_FT_EYE_LOOK_UP_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_LOOK_UP_RIGHT** = `2`

Right eye looks upwards.

:::: {#class_XRFaceTracker_constant_FT_EYE_LOOK_DOWN_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_LOOK_DOWN_RIGHT** = `3`

Right eye looks downwards.

:::: {#class_XRFaceTracker_constant_FT_EYE_LOOK_OUT_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_LOOK_OUT_LEFT** = `4`

Left eye looks outwards.

:::: {#class_XRFaceTracker_constant_FT_EYE_LOOK_IN_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_LOOK_IN_LEFT** = `5`

Left eye looks inwards.

:::: {#class_XRFaceTracker_constant_FT_EYE_LOOK_UP_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_LOOK_UP_LEFT** = `6`

Left eye looks upwards.

:::: {#class_XRFaceTracker_constant_FT_EYE_LOOK_DOWN_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_LOOK_DOWN_LEFT** = `7`

Left eye looks downwards.

:::: {#class_XRFaceTracker_constant_FT_EYE_CLOSED_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_CLOSED_RIGHT** = `8`

Closes the right eyelid.

:::: {#class_XRFaceTracker_constant_FT_EYE_CLOSED_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_CLOSED_LEFT** = `9`

Closes the left eyelid.

:::: {#class_XRFaceTracker_constant_FT_EYE_SQUINT_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_SQUINT_RIGHT** = `10`

Squeezes the right eye socket muscles.

:::: {#class_XRFaceTracker_constant_FT_EYE_SQUINT_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_SQUINT_LEFT** = `11`

Squeezes the left eye socket muscles.

:::: {#class_XRFaceTracker_constant_FT_EYE_WIDE_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_WIDE_RIGHT** = `12`

Right eyelid widens beyond relaxed.

:::: {#class_XRFaceTracker_constant_FT_EYE_WIDE_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_WIDE_LEFT** = `13`

Left eyelid widens beyond relaxed.

:::: {#class_XRFaceTracker_constant_FT_EYE_DILATION_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_DILATION_RIGHT** = `14`

Dilates the right eye pupil.

:::: {#class_XRFaceTracker_constant_FT_EYE_DILATION_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_DILATION_LEFT** = `15`

Dilates the left eye pupil.

:::: {#class_XRFaceTracker_constant_FT_EYE_CONSTRICT_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_CONSTRICT_RIGHT** = `16`

Constricts the right eye pupil.

:::: {#class_XRFaceTracker_constant_FT_EYE_CONSTRICT_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_CONSTRICT_LEFT** = `17`

Constricts the left eye pupil.

:::: {#class_XRFaceTracker_constant_FT_BROW_PINCH_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_PINCH_RIGHT** = `18`

Right eyebrow pinches in.

:::: {#class_XRFaceTracker_constant_FT_BROW_PINCH_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_PINCH_LEFT** = `19`

Left eyebrow pinches in.

:::: {#class_XRFaceTracker_constant_FT_BROW_LOWERER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_LOWERER_RIGHT** = `20`

Outer right eyebrow pulls down.

:::: {#class_XRFaceTracker_constant_FT_BROW_LOWERER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_LOWERER_LEFT** = `21`

Outer left eyebrow pulls down.

:::: {#class_XRFaceTracker_constant_FT_BROW_INNER_UP_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_INNER_UP_RIGHT** = `22`

Inner right eyebrow pulls up.

:::: {#class_XRFaceTracker_constant_FT_BROW_INNER_UP_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_INNER_UP_LEFT** = `23`

Inner left eyebrow pulls up.

:::: {#class_XRFaceTracker_constant_FT_BROW_OUTER_UP_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_OUTER_UP_RIGHT** = `24`

Outer right eyebrow pulls up.

:::: {#class_XRFaceTracker_constant_FT_BROW_OUTER_UP_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_OUTER_UP_LEFT** = `25`

Outer left eyebrow pulls up.

:::: {#class_XRFaceTracker_constant_FT_NOSE_SNEER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NOSE_SNEER_RIGHT** = `26`

Right side face sneers.

:::: {#class_XRFaceTracker_constant_FT_NOSE_SNEER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NOSE_SNEER_LEFT** = `27`

Left side face sneers.

:::: {#class_XRFaceTracker_constant_FT_NASAL_DILATION_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NASAL_DILATION_RIGHT** = `28`

Right side nose canal dilates.

:::: {#class_XRFaceTracker_constant_FT_NASAL_DILATION_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NASAL_DILATION_LEFT** = `29`

Left side nose canal dilates.

:::: {#class_XRFaceTracker_constant_FT_NASAL_CONSTRICT_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NASAL_CONSTRICT_RIGHT** = `30`

Right side nose canal constricts.

:::: {#class_XRFaceTracker_constant_FT_NASAL_CONSTRICT_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NASAL_CONSTRICT_LEFT** = `31`

Left side nose canal constricts.

:::: {#class_XRFaceTracker_constant_FT_CHEEK_SQUINT_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_CHEEK_SQUINT_RIGHT** = `32`

Raises the right side cheek.

:::: {#class_XRFaceTracker_constant_FT_CHEEK_SQUINT_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_CHEEK_SQUINT_LEFT** = `33`

Raises the left side cheek.

:::: {#class_XRFaceTracker_constant_FT_CHEEK_PUFF_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_CHEEK_PUFF_RIGHT** = `34`

Puffs the right side cheek.

:::: {#class_XRFaceTracker_constant_FT_CHEEK_PUFF_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_CHEEK_PUFF_LEFT** = `35`

Puffs the left side cheek.

:::: {#class_XRFaceTracker_constant_FT_CHEEK_SUCK_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_CHEEK_SUCK_RIGHT** = `36`

Sucks in the right side cheek.

:::: {#class_XRFaceTracker_constant_FT_CHEEK_SUCK_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_CHEEK_SUCK_LEFT** = `37`

Sucks in the left side cheek.

:::: {#class_XRFaceTracker_constant_FT_JAW_OPEN}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_JAW_OPEN** = `38`

Opens jawbone.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_CLOSED}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_CLOSED** = `39`

Closes the mouth.

:::: {#class_XRFaceTracker_constant_FT_JAW_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_JAW_RIGHT** = `40`

Pushes jawbone right.

:::: {#class_XRFaceTracker_constant_FT_JAW_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_JAW_LEFT** = `41`

Pushes jawbone left.

:::: {#class_XRFaceTracker_constant_FT_JAW_FORWARD}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_JAW_FORWARD** = `42`

Pushes jawbone forward.

:::: {#class_XRFaceTracker_constant_FT_JAW_BACKWARD}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_JAW_BACKWARD** = `43`

Pushes jawbone backward.

:::: {#class_XRFaceTracker_constant_FT_JAW_CLENCH}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_JAW_CLENCH** = `44`

Flexes jaw muscles.

:::: {#class_XRFaceTracker_constant_FT_JAW_MANDIBLE_RAISE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_JAW_MANDIBLE_RAISE** = `45`

Raises the jawbone.

:::: {#class_XRFaceTracker_constant_FT_LIP_SUCK_UPPER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_SUCK_UPPER_RIGHT** = `46`

Upper right lip part tucks in the mouth.

:::: {#class_XRFaceTracker_constant_FT_LIP_SUCK_UPPER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_SUCK_UPPER_LEFT** = `47`

Upper left lip part tucks in the mouth.

:::: {#class_XRFaceTracker_constant_FT_LIP_SUCK_LOWER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_SUCK_LOWER_RIGHT** = `48`

Lower right lip part tucks in the mouth.

:::: {#class_XRFaceTracker_constant_FT_LIP_SUCK_LOWER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_SUCK_LOWER_LEFT** = `49`

Lower left lip part tucks in the mouth.

:::: {#class_XRFaceTracker_constant_FT_LIP_SUCK_CORNER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_SUCK_CORNER_RIGHT** = `50`

Right lip corner folds into the mouth.

:::: {#class_XRFaceTracker_constant_FT_LIP_SUCK_CORNER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_SUCK_CORNER_LEFT** = `51`

Left lip corner folds into the mouth.

:::: {#class_XRFaceTracker_constant_FT_LIP_FUNNEL_UPPER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_FUNNEL_UPPER_RIGHT** = `52`

Upper right lip part pushes into a funnel.

:::: {#class_XRFaceTracker_constant_FT_LIP_FUNNEL_UPPER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_FUNNEL_UPPER_LEFT** = `53`

Upper left lip part pushes into a funnel.

:::: {#class_XRFaceTracker_constant_FT_LIP_FUNNEL_LOWER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_FUNNEL_LOWER_RIGHT** = `54`

Lower right lip part pushes into a funnel.

:::: {#class_XRFaceTracker_constant_FT_LIP_FUNNEL_LOWER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_FUNNEL_LOWER_LEFT** = `55`

Lower left lip part pushes into a funnel.

:::: {#class_XRFaceTracker_constant_FT_LIP_PUCKER_UPPER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_PUCKER_UPPER_RIGHT** = `56`

Upper right lip part pushes outwards.

:::: {#class_XRFaceTracker_constant_FT_LIP_PUCKER_UPPER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_PUCKER_UPPER_LEFT** = `57`

Upper left lip part pushes outwards.

:::: {#class_XRFaceTracker_constant_FT_LIP_PUCKER_LOWER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_PUCKER_LOWER_RIGHT** = `58`

Lower right lip part pushes outwards.

:::: {#class_XRFaceTracker_constant_FT_LIP_PUCKER_LOWER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_PUCKER_LOWER_LEFT** = `59`

Lower left lip part pushes outwards.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_UPPER_UP_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_UPPER_UP_RIGHT** = `60`

Upper right part of the lip pulls up.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_UPPER_UP_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_UPPER_UP_LEFT** = `61`

Upper left part of the lip pulls up.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_LOWER_DOWN_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_LOWER_DOWN_RIGHT** = `62`

Lower right part of the lip pulls up.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_LOWER_DOWN_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_LOWER_DOWN_LEFT** = `63`

Lower left part of the lip pulls up.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_UPPER_DEEPEN_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_UPPER_DEEPEN_RIGHT** = `64`

Upper right lip part pushes in the cheek.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_UPPER_DEEPEN_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_UPPER_DEEPEN_LEFT** = `65`

Upper left lip part pushes in the cheek.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_UPPER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_UPPER_RIGHT** = `66`

Moves upper lip right.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_UPPER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_UPPER_LEFT** = `67`

Moves upper lip left.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_LOWER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_LOWER_RIGHT** = `68`

Moves lower lip right.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_LOWER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_LOWER_LEFT** = `69`

Moves lower lip left.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_CORNER_PULL_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_CORNER_PULL_RIGHT** = `70`

Right lip corner pulls diagonally up and out.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_CORNER_PULL_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_CORNER_PULL_LEFT** = `71`

Left lip corner pulls diagonally up and out.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_CORNER_SLANT_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_CORNER_SLANT_RIGHT** = `72`

Right corner lip slants up.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_CORNER_SLANT_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_CORNER_SLANT_LEFT** = `73`

Left corner lip slants up.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_FROWN_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_FROWN_RIGHT** = `74`

Right corner lip pulls down.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_FROWN_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_FROWN_LEFT** = `75`

Left corner lip pulls down.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_STRETCH_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_STRETCH_RIGHT** = `76`

Mouth corner lip pulls out and down.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_STRETCH_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_STRETCH_LEFT** = `77`

Mouth corner lip pulls out and down.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_DIMPLE_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_DIMPLE_RIGHT** = `78`

Right lip corner is pushed backwards.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_DIMPLE_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_DIMPLE_LEFT** = `79`

Left lip corner is pushed backwards.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_RAISER_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_RAISER_UPPER** = `80`

Raises and slightly pushes out the upper mouth.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_RAISER_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_RAISER_LOWER** = `81`

Raises and slightly pushes out the lower mouth.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_PRESS_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_PRESS_RIGHT** = `82`

Right side lips press and flatten together vertically.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_PRESS_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_PRESS_LEFT** = `83`

Left side lips press and flatten together vertically.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_TIGHTENER_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_TIGHTENER_RIGHT** = `84`

Right side lips squeeze together horizontally.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_TIGHTENER_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_TIGHTENER_LEFT** = `85`

Left side lips squeeze together horizontally.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_OUT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_OUT** = `86`

Tongue visibly sticks out of the mouth.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_UP}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_UP** = `87`

Tongue points upwards.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_DOWN** = `88`

Tongue points downwards.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_RIGHT** = `89`

Tongue points right.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_LEFT** = `90`

Tongue points left.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_ROLL}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_ROLL** = `91`

Sides of the tongue funnel, creating a roll.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_BLEND_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_BLEND_DOWN** = `92`

Tongue arches up then down inside the mouth.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_CURL_UP}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_CURL_UP** = `93`

Tongue arches down then up inside the mouth.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_SQUISH}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_SQUISH** = `94`

Tongue squishes together and thickens.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_FLAT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_FLAT** = `95`

Tongue flattens and thins out.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_TWIST_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_TWIST_RIGHT** = `96`

Tongue tip rotates clockwise, with the rest following gradually.

:::: {#class_XRFaceTracker_constant_FT_TONGUE_TWIST_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_TONGUE_TWIST_LEFT** = `97`

Tongue tip rotates counter-clockwise, with the rest following gradually.

:::: {#class_XRFaceTracker_constant_FT_SOFT_PALATE_CLOSE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_SOFT_PALATE_CLOSE** = `98`

Inner mouth throat closes.

:::: {#class_XRFaceTracker_constant_FT_THROAT_SWALLOW}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_THROAT_SWALLOW** = `99`

The Adam\'s apple visibly swallows.

:::: {#class_XRFaceTracker_constant_FT_NECK_FLEX_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NECK_FLEX_RIGHT** = `100`

Right side neck visibly flexes.

:::: {#class_XRFaceTracker_constant_FT_NECK_FLEX_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NECK_FLEX_LEFT** = `101`

Left side neck visibly flexes.

:::: {#class_XRFaceTracker_constant_FT_EYE_CLOSED}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_CLOSED** = `102`

Closes both eye lids.

:::: {#class_XRFaceTracker_constant_FT_EYE_WIDE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_WIDE** = `103`

Widens both eye lids.

:::: {#class_XRFaceTracker_constant_FT_EYE_SQUINT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_SQUINT** = `104`

Squints both eye lids.

:::: {#class_XRFaceTracker_constant_FT_EYE_DILATION}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_DILATION** = `105`

Dilates both pupils.

:::: {#class_XRFaceTracker_constant_FT_EYE_CONSTRICT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_EYE_CONSTRICT** = `106`

Constricts both pupils.

:::: {#class_XRFaceTracker_constant_FT_BROW_DOWN_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_DOWN_RIGHT** = `107`

Pulls the right eyebrow down and in.

:::: {#class_XRFaceTracker_constant_FT_BROW_DOWN_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_DOWN_LEFT** = `108`

Pulls the left eyebrow down and in.

:::: {#class_XRFaceTracker_constant_FT_BROW_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_DOWN** = `109`

Pulls both eyebrows down and in.

:::: {#class_XRFaceTracker_constant_FT_BROW_UP_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_UP_RIGHT** = `110`

Right brow appears worried.

:::: {#class_XRFaceTracker_constant_FT_BROW_UP_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_UP_LEFT** = `111`

Left brow appears worried.

:::: {#class_XRFaceTracker_constant_FT_BROW_UP}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_BROW_UP** = `112`

Both brows appear worried.

:::: {#class_XRFaceTracker_constant_FT_NOSE_SNEER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NOSE_SNEER** = `113`

Entire face sneers.

:::: {#class_XRFaceTracker_constant_FT_NASAL_DILATION}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NASAL_DILATION** = `114`

Both nose canals dilate.

:::: {#class_XRFaceTracker_constant_FT_NASAL_CONSTRICT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_NASAL_CONSTRICT** = `115`

Both nose canals constrict.

:::: {#class_XRFaceTracker_constant_FT_CHEEK_PUFF}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_CHEEK_PUFF** = `116`

Puffs both cheeks.

:::: {#class_XRFaceTracker_constant_FT_CHEEK_SUCK}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_CHEEK_SUCK** = `117`

Sucks in both cheeks.

:::: {#class_XRFaceTracker_constant_FT_CHEEK_SQUINT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_CHEEK_SQUINT** = `118`

Raises both cheeks.

:::: {#class_XRFaceTracker_constant_FT_LIP_SUCK_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_SUCK_UPPER** = `119`

Tucks in the upper lips.

:::: {#class_XRFaceTracker_constant_FT_LIP_SUCK_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_SUCK_LOWER** = `120`

Tucks in the lower lips.

:::: {#class_XRFaceTracker_constant_FT_LIP_SUCK}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_SUCK** = `121`

Tucks in both lips.

:::: {#class_XRFaceTracker_constant_FT_LIP_FUNNEL_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_FUNNEL_UPPER** = `122`

Funnels in the upper lips.

:::: {#class_XRFaceTracker_constant_FT_LIP_FUNNEL_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_FUNNEL_LOWER** = `123`

Funnels in the lower lips.

:::: {#class_XRFaceTracker_constant_FT_LIP_FUNNEL}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_FUNNEL** = `124`

Funnels in both lips.

:::: {#class_XRFaceTracker_constant_FT_LIP_PUCKER_UPPER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_PUCKER_UPPER** = `125`

Upper lip part pushes outwards.

:::: {#class_XRFaceTracker_constant_FT_LIP_PUCKER_LOWER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_PUCKER_LOWER** = `126`

Lower lip part pushes outwards.

:::: {#class_XRFaceTracker_constant_FT_LIP_PUCKER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_LIP_PUCKER** = `127`

Lips push outwards.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_UPPER_UP}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_UPPER_UP** = `128`

Raises the upper lips.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_LOWER_DOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_LOWER_DOWN** = `129`

Lowers the lower lips.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_OPEN}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_OPEN** = `130`

Mouth opens, revealing teeth.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_RIGHT** = `131`

Moves mouth right.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_LEFT** = `132`

Moves mouth left.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_SMILE_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_SMILE_RIGHT** = `133`

Right side of the mouth smiles.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_SMILE_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_SMILE_LEFT** = `134`

Left side of the mouth smiles.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_SMILE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_SMILE** = `135`

Mouth expresses a smile.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_SAD_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_SAD_RIGHT** = `136`

Right side of the mouth expresses sadness.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_SAD_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_SAD_LEFT** = `137`

Left side of the mouth expresses sadness.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_SAD}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_SAD** = `138`

Mouth expresses sadness.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_STRETCH}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_STRETCH** = `139`

Mouth stretches.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_DIMPLE}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_DIMPLE** = `140`

Lip corners dimple.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_TIGHTENER}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_TIGHTENER** = `141`

Mouth tightens.

:::: {#class_XRFaceTracker_constant_FT_MOUTH_PRESS}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MOUTH_PRESS** = `142`

Mouth presses together.

:::: {#class_XRFaceTracker_constant_FT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} **FT_MAX** = `143`

Represents the size of the
`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRFaceTracker_property_blend_shapes}
::: rst-class
classref-property
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **blend_shapes** = `PackedFloat32Array()`
`🔗<class_XRFaceTracker_property_blend_shapes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_shapes**(value:
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"})
- `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} **get_blend_shapes**()

The array of face blend shape weights with indices corresponding to the
`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"} enum.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRFaceTracker_method_get_blend_shape}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_blend_shape**(blend_shape:
`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRFaceTracker_method_get_blend_shape>`{.interpreted-text
role="ref"}

Returns the requested face blend shape weight.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRFaceTracker_method_set_blend_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_blend_shape**(blend_shape:
`BlendShapeEntry<enum_XRFaceTracker_BlendShapeEntry>`{.interpreted-text
role="ref"}, weight: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_XRFaceTracker_method_set_blend_shape>`{.interpreted-text
role="ref"}

Sets a face blend shape weight.
