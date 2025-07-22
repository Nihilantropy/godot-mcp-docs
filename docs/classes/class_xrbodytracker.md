github_url
:   hide

# XRBodyTracker {#class_XRBodyTracker}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`XRPositionalTracker<class_XRPositionalTracker>`{.interpreted-text
role="ref"} **\<** `XRTracker<class_XRTracker>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A tracked body in XR.

::: rst-class
classref-introduction-group
:::

## Description

A body tracking system will create an instance of this object and add it
to the `XRServer<class_XRServer>`{.interpreted-text role="ref"}. This
tracking system will then obtain skeleton data, convert it to the Godot
Humanoid skeleton and store this data on the **XRBodyTracker** object.

Use `XRBodyModifier3D<class_XRBodyModifier3D>`{.interpreted-text
role="ref"} to animate a body mesh using body tracking data.

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

:::: {#enum_XRBodyTracker_BodyFlags}
::: rst-class
classref-enumeration
:::
::::

flags **BodyFlags**:
`🔗<enum_XRBodyTracker_BodyFlags>`{.interpreted-text role="ref"}

:::: {#class_XRBodyTracker_constant_BODY_FLAG_UPPER_BODY_SUPPORTED}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyFlags<enum_XRBodyTracker_BodyFlags>`{.interpreted-text role="ref"}
**BODY_FLAG_UPPER_BODY_SUPPORTED** = `1`

Upper body tracking supported.

:::: {#class_XRBodyTracker_constant_BODY_FLAG_LOWER_BODY_SUPPORTED}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyFlags<enum_XRBodyTracker_BodyFlags>`{.interpreted-text role="ref"}
**BODY_FLAG_LOWER_BODY_SUPPORTED** = `2`

Lower body tracking supported.

:::: {#class_XRBodyTracker_constant_BODY_FLAG_HANDS_SUPPORTED}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyFlags<enum_XRBodyTracker_BodyFlags>`{.interpreted-text role="ref"}
**BODY_FLAG_HANDS_SUPPORTED** = `4`

Hand tracking supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRBodyTracker_Joint}
::: rst-class
classref-enumeration
:::
::::

enum **Joint**: `🔗<enum_XRBodyTracker_Joint>`{.interpreted-text
role="ref"}

:::: {#class_XRBodyTracker_constant_JOINT_ROOT}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_ROOT** = `0`

Root joint.

:::: {#class_XRBodyTracker_constant_JOINT_HIPS}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_HIPS** = `1`

Hips joint.

:::: {#class_XRBodyTracker_constant_JOINT_SPINE}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_SPINE** = `2`

Spine joint.

:::: {#class_XRBodyTracker_constant_JOINT_CHEST}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_CHEST** = `3`

Chest joint.

:::: {#class_XRBodyTracker_constant_JOINT_UPPER_CHEST}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_UPPER_CHEST** = `4`

Upper chest joint.

:::: {#class_XRBodyTracker_constant_JOINT_NECK}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_NECK** = `5`

Neck joint.

:::: {#class_XRBodyTracker_constant_JOINT_HEAD}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_HEAD** = `6`

Head joint.

:::: {#class_XRBodyTracker_constant_JOINT_HEAD_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_HEAD_TIP** = `7`

Head tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_SHOULDER}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_SHOULDER** = `8`

Left shoulder joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_UPPER_ARM}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_UPPER_ARM** = `9`

Left upper arm joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_LOWER_ARM}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_LOWER_ARM** = `10`

Left lower arm joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_SHOULDER}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_SHOULDER** = `11`

Right shoulder joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_UPPER_ARM}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_UPPER_ARM** = `12`

Right upper arm joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_LOWER_ARM}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_LOWER_ARM** = `13`

Right lower arm joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_UPPER_LEG}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_UPPER_LEG** = `14`

Left upper leg joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_LOWER_LEG}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_LOWER_LEG** = `15`

Left lower leg joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_FOOT}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_FOOT** = `16`

Left foot joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_TOES}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_TOES** = `17`

Left toes joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_UPPER_LEG}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_UPPER_LEG** = `18`

Right upper leg joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_LOWER_LEG}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_LOWER_LEG** = `19`

Right lower leg joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_FOOT}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_FOOT** = `20`

Right foot joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_TOES}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_TOES** = `21`

Right toes joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_HAND}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_HAND** = `22`

Left hand joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_PALM}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_PALM** = `23`

Left palm joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_WRIST}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_WRIST** = `24`

Left wrist joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_THUMB_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_THUMB_METACARPAL** = `25`

Left thumb metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_THUMB_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_THUMB_PHALANX_PROXIMAL** = `26`

Left thumb phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_THUMB_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_THUMB_PHALANX_DISTAL** = `27`

Left thumb phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_THUMB_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_THUMB_TIP** = `28`

Left thumb tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_INDEX_FINGER_METACARPAL** = `29`

Left index finger metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_INDEX_FINGER_PHALANX_PROXIMAL** = `30`

Left index finger phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_INDEX_FINGER_PHALANX_INTERMEDIATE** = `31`

Left index finger phalanx intermediate joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_INDEX_FINGER_PHALANX_DISTAL** = `32`

Left index finger phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_INDEX_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_INDEX_FINGER_TIP** = `33`

Left index finger tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_MIDDLE_FINGER_METACARPAL** = `34`

Left middle finger metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_MIDDLE_FINGER_PHALANX_PROXIMAL** = `35`

Left middle finger phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_MIDDLE_FINGER_PHALANX_INTERMEDIATE** = `36`

Left middle finger phalanx intermediate joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_MIDDLE_FINGER_PHALANX_DISTAL** = `37`

Left middle finger phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_MIDDLE_FINGER_TIP** = `38`

Left middle finger tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_RING_FINGER_METACARPAL** = `39`

Left ring finger metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_RING_FINGER_PHALANX_PROXIMAL** = `40`

Left ring finger phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_RING_FINGER_PHALANX_INTERMEDIATE** = `41`

Left ring finger phalanx intermediate joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_RING_FINGER_PHALANX_DISTAL** = `42`

Left ring finger phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_RING_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_RING_FINGER_TIP** = `43`

Left ring finger tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_PINKY_FINGER_METACARPAL** = `44`

Left pinky finger metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_PINKY_FINGER_PHALANX_PROXIMAL** = `45`

Left pinky finger phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_PINKY_FINGER_PHALANX_INTERMEDIATE** = `46`

Left pinky finger phalanx intermediate joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_PINKY_FINGER_PHALANX_DISTAL** = `47`

Left pinky finger phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_PINKY_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_PINKY_FINGER_TIP** = `48`

Left pinky finger tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_HAND}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_HAND** = `49`

Right hand joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_PALM}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_PALM** = `50`

Right palm joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_WRIST}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_WRIST** = `51`

Right wrist joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_THUMB_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_THUMB_METACARPAL** = `52`

Right thumb metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_THUMB_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_THUMB_PHALANX_PROXIMAL** = `53`

Right thumb phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_THUMB_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_THUMB_PHALANX_DISTAL** = `54`

Right thumb phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_THUMB_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_THUMB_TIP** = `55`

Right thumb tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_INDEX_FINGER_METACARPAL** = `56`

Right index finger metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_INDEX_FINGER_PHALANX_PROXIMAL** = `57`

Right index finger phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_INDEX_FINGER_PHALANX_INTERMEDIATE** = `58`

Right index finger phalanx intermediate joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_INDEX_FINGER_PHALANX_DISTAL** = `59`

Right index finger phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_INDEX_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_INDEX_FINGER_TIP** = `60`

Right index finger tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_MIDDLE_FINGER_METACARPAL** = `61`

Right middle finger metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_MIDDLE_FINGER_PHALANX_PROXIMAL** = `62`

Right middle finger phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_MIDDLE_FINGER_PHALANX_INTERMEDIATE** = `63`

Right middle finger phalanx intermediate joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_MIDDLE_FINGER_PHALANX_DISTAL** = `64`

Right middle finger phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_MIDDLE_FINGER_TIP** = `65`

Right middle finger tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_RING_FINGER_METACARPAL** = `66`

Right ring finger metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_RING_FINGER_PHALANX_PROXIMAL** = `67`

Right ring finger phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_RING_FINGER_PHALANX_INTERMEDIATE** = `68`

Right ring finger phalanx intermediate joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_RING_FINGER_PHALANX_DISTAL** = `69`

Right ring finger phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_RING_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_RING_FINGER_TIP** = `70`

Right ring finger tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_PINKY_FINGER_METACARPAL** = `71`

Right pinky finger metacarpal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_PINKY_FINGER_PHALANX_PROXIMAL** = `72`

Right pinky finger phalanx proximal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_PINKY_FINGER_PHALANX_INTERMEDIATE** = `73`

Right pinky finger phalanx intermediate joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_PINKY_FINGER_PHALANX_DISTAL** = `74`

Right pinky finger phalanx distal joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_PINKY_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_PINKY_FINGER_TIP** = `75`

Right pinky finger tip joint.

:::: {#class_XRBodyTracker_constant_JOINT_LOWER_CHEST}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LOWER_CHEST** = `76`

Lower chest joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_SCAPULA}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_SCAPULA** = `77`

Left scapula joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_WRIST_TWIST}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_WRIST_TWIST** = `78`

Left wrist twist joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_SCAPULA}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_SCAPULA** = `79`

Right scapula joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_WRIST_TWIST}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_WRIST_TWIST** = `80`

Right wrist twist joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_FOOT_TWIST}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_FOOT_TWIST** = `81`

Left foot twist joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_HEEL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_HEEL** = `82`

Left heel joint.

:::: {#class_XRBodyTracker_constant_JOINT_LEFT_MIDDLE_FOOT}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_LEFT_MIDDLE_FOOT** = `83`

Left middle foot joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_FOOT_TWIST}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_FOOT_TWIST** = `84`

Right foot twist joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_HEEL}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_HEEL** = `85`

Right heel joint.

:::: {#class_XRBodyTracker_constant_JOINT_RIGHT_MIDDLE_FOOT}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_RIGHT_MIDDLE_FOOT** = `86`

Right middle foot joint.

:::: {#class_XRBodyTracker_constant_JOINT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}
**JOINT_MAX** = `87`

Represents the size of the
`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRBodyTracker_JointFlags}
::: rst-class
classref-enumeration
:::
::::

flags **JointFlags**:
`🔗<enum_XRBodyTracker_JointFlags>`{.interpreted-text role="ref"}

:::: {#class_XRBodyTracker_constant_JOINT_FLAG_ORIENTATION_VALID}
::: rst-class
classref-enumeration-constant
:::
::::

`JointFlags<enum_XRBodyTracker_JointFlags>`{.interpreted-text
role="ref"} **JOINT_FLAG_ORIENTATION_VALID** = `1`

The joint\'s orientation data is valid.

:::: {#class_XRBodyTracker_constant_JOINT_FLAG_ORIENTATION_TRACKED}
::: rst-class
classref-enumeration-constant
:::
::::

`JointFlags<enum_XRBodyTracker_JointFlags>`{.interpreted-text
role="ref"} **JOINT_FLAG_ORIENTATION_TRACKED** = `2`

The joint\'s orientation is actively tracked. May not be set if tracking
has been temporarily lost.

:::: {#class_XRBodyTracker_constant_JOINT_FLAG_POSITION_VALID}
::: rst-class
classref-enumeration-constant
:::
::::

`JointFlags<enum_XRBodyTracker_JointFlags>`{.interpreted-text
role="ref"} **JOINT_FLAG_POSITION_VALID** = `4`

The joint\'s position data is valid.

:::: {#class_XRBodyTracker_constant_JOINT_FLAG_POSITION_TRACKED}
::: rst-class
classref-enumeration-constant
:::
::::

`JointFlags<enum_XRBodyTracker_JointFlags>`{.interpreted-text
role="ref"} **JOINT_FLAG_POSITION_TRACKED** = `8`

The joint\'s position is actively tracked. May not be set if tracking
has been temporarily lost.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRBodyTracker_property_body_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`BodyFlags<enum_XRBodyTracker_BodyFlags>`{.interpreted-text
role="ref"}\] **body_flags** = `0`
`🔗<class_XRBodyTracker_property_body_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_body_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`BodyFlags<enum_XRBodyTracker_BodyFlags>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`BodyFlags<enum_XRBodyTracker_BodyFlags>`{.interpreted-text
  role="ref"}\] **get_body_flags**()

The type of body tracking data captured.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRBodyTracker_property_has_tracking_data}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_tracking_data** =
`false`
`🔗<class_XRBodyTracker_property_has_tracking_data>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_has_tracking_data**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_has_tracking_data**()

If `true`, the body tracking data is valid.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRBodyTracker_method_get_joint_flags}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JointFlags<enum_XRBodyTracker_JointFlags>`{.interpreted-text
role="ref"}\] **get_joint_flags**(joint:
`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRBodyTracker_method_get_joint_flags>`{.interpreted-text
role="ref"}

Returns flags about the validity of the tracking data for the given body
joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRBodyTracker_method_get_joint_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_joint_transform**(joint:
`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRBodyTracker_method_get_joint_transform>`{.interpreted-text
role="ref"}

Returns the transform for the given body joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRBodyTracker_method_set_joint_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_flags**(joint:
`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JointFlags<enum_XRBodyTracker_JointFlags>`{.interpreted-text
role="ref"}\])
`🔗<class_XRBodyTracker_method_set_joint_flags>`{.interpreted-text
role="ref"}

Sets flags about the validity of the tracking data for the given body
joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRBodyTracker_method_set_joint_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_transform**(joint:
`Joint<enum_XRBodyTracker_Joint>`{.interpreted-text role="ref"},
transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_XRBodyTracker_method_set_joint_transform>`{.interpreted-text
role="ref"}

Sets the transform for the given body joint.
