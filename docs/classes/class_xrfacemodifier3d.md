github_url
:   hide

# XRFaceModifier3D {#class_XRFaceModifier3D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node for driving standard face meshes from
`XRFaceTracker<class_XRFaceTracker>`{.interpreted-text role="ref"}
weights.

::: rst-class
classref-introduction-group
:::

## Description

This node applies weights from an
`XRFaceTracker<class_XRFaceTracker>`{.interpreted-text role="ref"} to a
mesh with supporting face blend shapes.

The [Unified
Expressions](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/unified-blendshapes)
blend shapes are supported, as well as ARKit and SRanipal blend shapes.

The node attempts to identify blend shapes based on name matching. Blend
shapes should match the names listed in the [Unified Expressions
Compatibility](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/compatibility/overview)
chart.

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
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRFaceModifier3D_property_face_tracker}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**face_tracker** = `&"/user/face_tracker"`
`🔗<class_XRFaceModifier3D_property_face_tracker>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_face_tracker**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_face_tracker**()

The `XRFaceTracker<class_XRFaceTracker>`{.interpreted-text role="ref"}
path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRFaceModifier3D_property_target}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **target** =
`NodePath("")`
`🔗<class_XRFaceModifier3D_property_target>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_target**()

The `NodePath<class_NodePath>`{.interpreted-text role="ref"} of the face
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}.
