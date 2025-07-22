github_url
:   hide

# SkeletonProfileHumanoid {#class_SkeletonProfileHumanoid}

**Inherits:** `SkeletonProfile<class_SkeletonProfile>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A humanoid `SkeletonProfile<class_SkeletonProfile>`{.interpreted-text
role="ref"} preset.

::: rst-class
classref-introduction-group
:::

## Description

A `SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}
as a preset that is optimized for the human form. This exists for
standardization, so all parameters are read-only.

A humanoid skeleton profile contains 54 bones divided in 4 groups:
`"Body"`, `"Face"`, `"LeftHand"`, and `"RightHand"`. It is structured as
follows:

``` text
Root
└─ Hips
    ├─ LeftUpperLeg
    │  └─ LeftLowerLeg
    │     └─ LeftFoot
    │        └─ LeftToes
    ├─ RightUpperLeg
    │  └─ RightLowerLeg
    │     └─ RightFoot
    │        └─ RightToes
    └─ Spine
        └─ Chest
            └─ UpperChest
                ├─ Neck
                │   └─ Head
                │       ├─ Jaw
                │       ├─ LeftEye
                │       └─ RightEye
                ├─ LeftShoulder
                │  └─ LeftUpperArm
                │     └─ LeftLowerArm
                │        └─ LeftHand
                │           ├─ LeftThumbMetacarpal
                │           │  └─ LeftThumbProximal
                │           │    └─ LeftThumbDistal
                │           ├─ LeftIndexProximal
                │           │  └─ LeftIndexIntermediate
                │           │    └─ LeftIndexDistal
                │           ├─ LeftMiddleProximal
                │           │  └─ LeftMiddleIntermediate
                │           │    └─ LeftMiddleDistal
                │           ├─ LeftRingProximal
                │           │  └─ LeftRingIntermediate
                │           │    └─ LeftRingDistal
                │           └─ LeftLittleProximal
                │              └─ LeftLittleIntermediate
                │                └─ LeftLittleDistal
                └─ RightShoulder
                   └─ RightUpperArm
                      └─ RightLowerArm
                         └─ RightHand
                            ├─ RightThumbMetacarpal
                            │  └─ RightThumbProximal
                            │     └─ RightThumbDistal
                            ├─ RightIndexProximal
                            │  └─ RightIndexIntermediate
                            │     └─ RightIndexDistal
                            ├─ RightMiddleProximal
                            │  └─ RightMiddleIntermediate
                            │     └─ RightMiddleDistal
                            ├─ RightRingProximal
                            │  └─ RightRingIntermediate
                            │     └─ RightRingDistal
                            └─ RightLittleProximal
                               └─ RightLittleIntermediate
                                 └─ RightLittleDistal
```

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Retargeting 3D Skeletons <../tutorials/assets_pipeline/retargeting_3d_skeletons>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

