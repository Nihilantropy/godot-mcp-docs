github_url
:   hide

# ModifierBoneTarget3D {#class_ModifierBoneTarget3D}

**Inherits:**
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

А node that dynamically copies the 3D transform of a bone in its parent
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This node selects a bone in a
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} and
attaches to it. This means that the **ModifierBoneTarget3D** node will
dynamically copy the 3D transform of the selected bone.

The functionality is similar to
`BoneAttachment3D<class_BoneAttachment3D>`{.interpreted-text
role="ref"}, but this node adopts the
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} cycle and is intended to be used as another
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"}\'s target.

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

:::: {#class_ModifierBoneTarget3D_property_bone}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bone** = `-1`
`🔗<class_ModifierBoneTarget3D_property_bone>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bone**()

The index of the attached bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ModifierBoneTarget3D_property_bone_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **bone_name** =
`""`
`🔗<class_ModifierBoneTarget3D_property_bone_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_bone_name**()

The name of the attached bone.
