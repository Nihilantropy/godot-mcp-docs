github_url
:   hide

# SkinReference {#class_SkinReference}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A reference-counted holder object for a skeleton RID used in the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

An internal object containing a mapping from a
`Skin<class_Skin>`{.interpreted-text role="ref"} used within the context
of a particular `MeshInstance3D<class_MeshInstance3D>`{.interpreted-text
role="ref"} to refer to the skeleton\'s
`RID<class_RID>`{.interpreted-text role="ref"} in the RenderingServer.

See also
`MeshInstance3D.get_skin_reference()<class_MeshInstance3D_method_get_skin_reference>`{.interpreted-text
role="ref"} and
`RenderingServer.instance_attach_skeleton()<class_RenderingServer_method_instance_attach_skeleton>`{.interpreted-text
role="ref"}.

Note that despite the similar naming, the skeleton RID used in the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
does not have a direct one-to-one correspondence to a
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} node.

In particular, a `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} node with no
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
children may be unknown to the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}.

On the other hand, a `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} with multiple
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
nodes which each have different
`MeshInstance3D.skin<class_MeshInstance3D_property_skin>`{.interpreted-text
role="ref"} objects may have multiple SkinReference instances (and
hence, multiple skeleton `RID<class_RID>`{.interpreted-text
role="ref"}s).

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

:::: {#class_SkinReference_method_get_skeleton}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_skeleton**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkinReference_method_get_skeleton>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} owned by this
SkinReference, as returned by
`RenderingServer.skeleton_create()<class_RenderingServer_method_skeleton_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkinReference_method_get_skin}
::: rst-class
classref-method
:::
::::

`Skin<class_Skin>`{.interpreted-text role="ref"} **get_skin**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_SkinReference_method_get_skin>`{.interpreted-text
role="ref"}

Returns the `Skin<class_Skin>`{.interpreted-text role="ref"} connected
to this SkinReference. In the case of
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
with no
`MeshInstance3D.skin<class_MeshInstance3D_property_skin>`{.interpreted-text
role="ref"} assigned, this will reference an internal default
`Skin<class_Skin>`{.interpreted-text role="ref"} owned by that
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}.

Note that a single `Skin<class_Skin>`{.interpreted-text role="ref"} may
have more than one **SkinReference** in the case that it is shared by
meshes across multiple `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} nodes.
