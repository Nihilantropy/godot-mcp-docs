github_url
:   hide

# BoneConstraint3D {#class_BoneConstraint3D}

**Inherits:**
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `AimModifier3D<class_AimModifier3D>`{.interpreted-text
role="ref"},
`ConvertTransformModifier3D<class_ConvertTransformModifier3D>`{.interpreted-text
role="ref"},
`CopyTransformModifier3D<class_CopyTransformModifier3D>`{.interpreted-text
role="ref"}

A node that may modify Skeleton3D\'s bone with associating the two
bones.

::: rst-class
classref-introduction-group
:::

## Description

Base class of
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} that modifies the bone set in
`set_apply_bone()<class_BoneConstraint3D_method_set_apply_bone>`{.interpreted-text
role="ref"} based on the transform of the bone retrieved by
`get_reference_bone()<class_BoneConstraint3D_method_get_reference_bone>`{.interpreted-text
role="ref"}.

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

## Method Descriptions

:::: {#class_BoneConstraint3D_method_clear_setting}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_setting**()
`🔗<class_BoneConstraint3D_method_clear_setting>`{.interpreted-text
role="ref"}

Clear all settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_get_amount}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_amount**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BoneConstraint3D_method_get_amount>`{.interpreted-text
role="ref"}

Returns the apply amount of the setting at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_get_apply_bone}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_apply_bone**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BoneConstraint3D_method_get_apply_bone>`{.interpreted-text
role="ref"}

Returns the apply bone of the setting at `index`. This bone will be
modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_get_apply_bone_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_apply_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BoneConstraint3D_method_get_apply_bone_name>`{.interpreted-text
role="ref"}

Returns the apply bone name of the setting at `index`. This bone will be
modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_get_reference_bone}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_reference_bone**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BoneConstraint3D_method_get_reference_bone>`{.interpreted-text
role="ref"}

Returns the reference bone of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_get_reference_bone_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_reference_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BoneConstraint3D_method_get_reference_bone_name>`{.interpreted-text
role="ref"}

Returns the reference bone name of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_get_setting_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_setting_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BoneConstraint3D_method_get_setting_count>`{.interpreted-text
role="ref"}

Returns the number of settings in the modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_set_amount}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_amount**(index: `int<class_int>`{.interpreted-text role="ref"},
amount: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_BoneConstraint3D_method_set_amount>`{.interpreted-text
role="ref"}

Sets the apply amount of the setting at `index` to `amount`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_set_apply_bone}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_apply_bone**(index: `int<class_int>`{.interpreted-text
role="ref"}, bone: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_BoneConstraint3D_method_set_apply_bone>`{.interpreted-text
role="ref"}

Sets the apply bone of the setting at `index` to `bone`. This bone will
be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_set_apply_bone_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_apply_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"}, bone_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_BoneConstraint3D_method_set_apply_bone_name>`{.interpreted-text
role="ref"}

Sets the apply bone of the setting at `index` to `bone_name`. This bone
will be modified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_set_reference_bone}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_reference_bone**(index: `int<class_int>`{.interpreted-text
role="ref"}, bone: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_BoneConstraint3D_method_set_reference_bone>`{.interpreted-text
role="ref"}

Sets the reference bone of the setting at `index` to `bone`.

This bone will be only referenced and not modified by this modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_set_reference_bone_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_reference_bone_name**(index: `int<class_int>`{.interpreted-text
role="ref"}, bone_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_BoneConstraint3D_method_set_reference_bone_name>`{.interpreted-text
role="ref"}

Sets the reference bone of the setting at `index` to `bone_name`.

This bone will be only referenced and not modified by this modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneConstraint3D_method_set_setting_count}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_setting_count**(count: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_BoneConstraint3D_method_set_setting_count>`{.interpreted-text
role="ref"}

Sets the number of settings in the modifier.
