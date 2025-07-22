github_url
:   hide

# Node3DGizmo {#class_Node3DGizmo}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"}

Abstract class to expose editor gizmos for
`Node3D<class_Node3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This abstract class helps connect the
`Node3D<class_Node3D>`{.interpreted-text role="ref"} scene with the
editor-specific
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} class.

\*\*Node3DGizmo\*\* by itself has no exposed API, refer to
`Node3D.add_gizmo()<class_Node3D_method_add_gizmo>`{.interpreted-text
role="ref"} and pass it an
`EditorNode3DGizmo<class_EditorNode3DGizmo>`{.interpreted-text
role="ref"} instance.
