github_url
:   hide

# ResourceImporterScene {#class_ResourceImporterScene}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports a glTF, FBX, COLLADA, or Blender 3D scene.

::: rst-class
classref-introduction-group
:::

## Description

See also
`ResourceImporterOBJ<class_ResourceImporterOBJ>`{.interpreted-text
role="ref"}, which is used for OBJ models that can be imported as an
independent `Mesh<class_Mesh>`{.interpreted-text role="ref"} or a scene.

Additional options (such as extracting individual meshes or materials to
files) are available in the **Advanced Import Settings** dialog. This
dialog can be accessed by double-clicking a 3D scene in the FileSystem
dock or by selecting a 3D scene in the FileSystem dock, going to the
Import dock and choosing **Advanced**.

\*\*Note:\*\* **ResourceImporterScene** is *not* used for
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}s, such as
`.tscn` and `.scn` files.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Importing 3D scenes <../tutorials/assets_pipeline/importing_3d_scenes/index>`{.interpreted-text
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

:::: {#class_ResourceImporterScene_property__subresources}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_subresources** = `{}`
`🔗<class_ResourceImporterScene_property__subresources>`{.interpreted-text
role="ref"}

Contains properties for the scene\'s subresources. This is an internal
option which is not visible in the Import dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_animation/fps}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **animation/fps** =
`30`
`🔗<class_ResourceImporterScene_property_animation/fps>`{.interpreted-text
role="ref"}

The number of frames per second to use for baking animation curves to a
series of points with linear interpolation. It\'s recommended to
configure this value to match the value you\'re using as a baseline in
your 3D modeling software. Higher values result in more precise
animation with fast movement changes, at the cost of higher file sizes
and memory usage. Thanks to interpolation, there is usually not much
benefit in going above 30 FPS (as the animation will still appear smooth
at higher rendering framerates).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_animation/import}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **animation/import** =
`true`
`🔗<class_ResourceImporterScene_property_animation/import>`{.interpreted-text
role="ref"}

If `true`, import animations from the 3D scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_animation/import_rest_as_RESET}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**animation/import_rest_as_RESET** = `false`
`🔗<class_ResourceImporterScene_property_animation/import_rest_as_RESET>`{.interpreted-text
role="ref"}

If `true`, adds an `Animation<class_Animation>`{.interpreted-text
role="ref"} named `RESET`, containing the
`Skeleton3D.get_bone_rest()<class_Skeleton3D_method_get_bone_rest>`{.interpreted-text
role="ref"} from `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} nodes. This can be useful to extract an animation in the
reference pose.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_animation/remove_immutable_tracks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**animation/remove_immutable_tracks** = `true`
`🔗<class_ResourceImporterScene_property_animation/remove_immutable_tracks>`{.interpreted-text
role="ref"}

If `true`, remove animation tracks that only contain default values.
This can reduce output file size and memory usage with certain 3D
scenes, depending on the contents of their animation tracks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_animation/trimming}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **animation/trimming**
= `false`
`🔗<class_ResourceImporterScene_property_animation/trimming>`{.interpreted-text
role="ref"}

If `true`, trim the beginning and end of animations if there are no
keyframe changes. This can reduce output file size and memory usage with
certain 3D scenes, depending on the contents of their animation tracks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_import_script/path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**import_script/path** = `""`
`🔗<class_ResourceImporterScene_property_import_script/path>`{.interpreted-text
role="ref"}

Path to an import script, which can run code after the import process
has completed for custom processing. See [Using import scripts for
automation](../tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html#using-import-scripts-for-automation)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_materials/extract}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **materials/extract** =
`0`
`🔗<class_ResourceImporterScene_property_materials/extract>`{.interpreted-text
role="ref"}

Material extraction mode.

- `0 (Keep Internal)`, materials are not extracted.
- `1 (Extract Once)`, materials are extracted once and reused on
  subsequent import.
- `2 (Extract and Overwrite)`, materials are extracted and overwritten
  on every import.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_materials/extract_format}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**materials/extract_format** = `0`
`🔗<class_ResourceImporterScene_property_materials/extract_format>`{.interpreted-text
role="ref"}

Extracted material file format.

- `0 (Text)`, text file format (`*.tres`).
- `1 (Binary)`, binary file format (`*.res`).
- `2 (Material)`, binary file format (`*.material`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_materials/extract_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**materials/extract_path** = `""`
`🔗<class_ResourceImporterScene_property_materials/extract_path>`{.interpreted-text
role="ref"}

Path extracted materials are saved to. If empty, source scene path is
used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_meshes/create_shadow_meshes}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**meshes/create_shadow_meshes** = `true`
`🔗<class_ResourceImporterScene_property_meshes/create_shadow_meshes>`{.interpreted-text
role="ref"}

If `true`, enables the generation of shadow meshes on import. This
optimizes shadow rendering without reducing quality by welding vertices
together when possible. This in turn reduces the memory bandwidth
required to render shadows. Shadow mesh generation currently doesn\'t
support using a lower detail level than the source mesh (but shadow
rendering will make use of LODs when relevant).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_meshes/ensure_tangents}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**meshes/ensure_tangents** = `true`
`🔗<class_ResourceImporterScene_property_meshes/ensure_tangents>`{.interpreted-text
role="ref"}

If `true`, generate vertex tangents using
[Mikktspace](http://www.mikktspace.com/) if the input meshes don\'t have
tangent data. When possible, it\'s recommended to let the 3D modeling
software generate tangents on export instead on relying on this option.
Tangents are required for correct display of normal and height maps,
along with any material/shader features that require tangents.

If you don\'t need material features that require tangents, disabling
this can reduce output file size and speed up importing if the source 3D
file doesn\'t contain tangents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_meshes/force_disable_compression}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**meshes/force_disable_compression** = `false`
`🔗<class_ResourceImporterScene_property_meshes/force_disable_compression>`{.interpreted-text
role="ref"}

If `true`, mesh compression will not be used. Consider enabling if you
notice blocky artifacts in your mesh normals or UVs, or if you have
meshes that are larger than a few thousand meters in each direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_meshes/generate_lods}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**meshes/generate_lods** = `true`
`🔗<class_ResourceImporterScene_property_meshes/generate_lods>`{.interpreted-text
role="ref"}

If `true`, generates lower detail variants of the mesh which will be
displayed in the distance to improve rendering performance. Not all
meshes benefit from LOD, especially if they are never rendered from far
away. Disabling this can reduce output file size and speed up importing.
See [Mesh level of detail
(LOD)](../tutorials/3d/mesh_lod.html#doc-mesh-lod) for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_meshes/light_baking}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **meshes/light_baking** =
`1`
`🔗<class_ResourceImporterScene_property_meshes/light_baking>`{.interpreted-text
role="ref"}

Configures the meshes\'
`GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>`{.interpreted-text
role="ref"} in the 3D scene. If set to **Static Lightmaps**, sets the
meshes\' GI mode to Static and generates UV2 on import for
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} baking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_meshes/lightmap_texel_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**meshes/lightmap_texel_size** = `0.2`
`🔗<class_ResourceImporterScene_property_meshes/lightmap_texel_size>`{.interpreted-text
role="ref"}

Controls the size of each texel on the baked lightmap. A smaller value
results in more precise lightmaps, at the cost of larger lightmap sizes
and longer bake times.

\*\*Note:\*\* Only effective if
`meshes/light_baking<class_ResourceImporterScene_property_meshes/light_baking>`{.interpreted-text
role="ref"} is set to **Static Lightmaps**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_nodes/apply_root_scale}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**nodes/apply_root_scale** = `true`
`🔗<class_ResourceImporterScene_property_nodes/apply_root_scale>`{.interpreted-text
role="ref"}

If `true`,
`nodes/root_scale<class_ResourceImporterScene_property_nodes/root_scale>`{.interpreted-text
role="ref"} will be applied to the descendant nodes, meshes, animations,
bones, etc. This means that if you add a child node later on within the
imported scene, it won\'t be scaled. If `false`,
`nodes/root_scale<class_ResourceImporterScene_property_nodes/root_scale>`{.interpreted-text
role="ref"} will multiply the scale of the root node instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_nodes/import_as_skeleton_bones}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**nodes/import_as_skeleton_bones** = `false`
`🔗<class_ResourceImporterScene_property_nodes/import_as_skeleton_bones>`{.interpreted-text
role="ref"}

Treat all nodes in the imported scene as if they are bones within a
single `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}. Can
be used to guarantee that imported animations target skeleton bones
rather than nodes. May also be used to assign the `"Root"` bone in a
`BoneMap<class_BoneMap>`{.interpreted-text role="ref"}. See
`Retargeting 3D Skeletons <../tutorials/assets_pipeline/retargeting_3d_skeletons>`{.interpreted-text
role="doc"} for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_nodes/root_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **nodes/root_name**
= `""`
`🔗<class_ResourceImporterScene_property_nodes/root_name>`{.interpreted-text
role="ref"}

Override for the root node name. If empty, the root node will use what
the scene specifies, or the file name if the scene does not specify a
root name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_nodes/root_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **nodes/root_scale**
= `1.0`
`🔗<class_ResourceImporterScene_property_nodes/root_scale>`{.interpreted-text
role="ref"}

The uniform scale to use for the scene root. The default value of `1.0`
will not perform any rescaling. See
`nodes/apply_root_scale<class_ResourceImporterScene_property_nodes/apply_root_scale>`{.interpreted-text
role="ref"} for details of how this scale is applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_nodes/root_script}
::: rst-class
classref-property
:::
::::

`Script<class_Script>`{.interpreted-text role="ref"}
**nodes/root_script** = `null`
`🔗<class_ResourceImporterScene_property_nodes/root_script>`{.interpreted-text
role="ref"}

If set to a valid script, attaches the script to the root node of the
imported scene. If the type of the root node is not compatible with the
script, the root node will be replaced with a type that is compatible
with the script. This setting can also be used on other non-mesh nodes
in the scene to attach scripts to them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_nodes/root_type}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **nodes/root_type**
= `""`
`🔗<class_ResourceImporterScene_property_nodes/root_type>`{.interpreted-text
role="ref"}

Override for the root node type. If empty, the root node will use what
the scene specifies, or `Node3D<class_Node3D>`{.interpreted-text
role="ref"} if the scene does not specify a root type. Using a node type
that inherits from `Node3D<class_Node3D>`{.interpreted-text role="ref"}
is recommended. Otherwise, you\'ll lose the ability to position the node
directly in the 3D editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_nodes/use_name_suffixes}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**nodes/use_name_suffixes** = `true`
`🔗<class_ResourceImporterScene_property_nodes/use_name_suffixes>`{.interpreted-text
role="ref"}

If `true`, will use suffixes in the names of imported objects such as
nodes and resources to determine types and properties, such as `-noimp`
to skip import of a node or animation, `-alpha` to enable alpha
transparency on a material, and `-vcol` to enable vertex colors on a
material. Disabling this makes editor-imported files more similar to the
original files, and more similar to files imported at runtime. See
`Node type customization using name suffixes <../tutorials/assets_pipeline/importing_3d_scenes/node_type_customization>`{.interpreted-text
role="doc"} for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_nodes/use_node_type_suffixes}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**nodes/use_node_type_suffixes** = `true`
`🔗<class_ResourceImporterScene_property_nodes/use_node_type_suffixes>`{.interpreted-text
role="ref"}

If `true`, will use suffixes in the node names to determine the node
type, such as `-col` for collision shapes. This is only used when
`nodes/use_name_suffixes<class_ResourceImporterScene_property_nodes/use_name_suffixes>`{.interpreted-text
role="ref"} is `true`. Disabling this makes editor-imported files more
similar to the original files, and more similar to files imported at
runtime. See
`Node type customization using name suffixes <../tutorials/assets_pipeline/importing_3d_scenes/node_type_customization>`{.interpreted-text
role="doc"} for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterScene_property_skins/use_named_skins}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**skins/use_named_skins** = `true`
`🔗<class_ResourceImporterScene_property_skins/use_named_skins>`{.interpreted-text
role="ref"}

If checked, use named `Skin<class_Skin>`{.interpreted-text role="ref"}s
for animation. The
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
node contains 3 properties of relevance here: a skeleton
`NodePath<class_NodePath>`{.interpreted-text role="ref"} pointing to the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} node
(usually `..`), a mesh, and a skin:

- The `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} node
  contains a list of bones with names, their pose and rest, a name and a
  parent bone.
- The mesh is all of the raw vertex data needed to display a mesh. In
  terms of the mesh, it knows how vertices are weight-painted and uses
  some internal numbering often imported from 3D modeling software.
- The skin contains the information necessary to bind this mesh onto
  this Skeleton3D. For every one of the internal bone IDs chosen by the
  3D modeling software, it contains two things. Firstly, a matrix known
  as the Bind Pose Matrix, Inverse Bind Matrix, or IBM for short.
  Secondly, the `Skin<class_Skin>`{.interpreted-text role="ref"}
  contains each bone\'s name (if
  `skins/use_named_skins<class_ResourceImporterScene_property_skins/use_named_skins>`{.interpreted-text
  role="ref"} is `true`), or the bone\'s index within the
  `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} list (if
  `skins/use_named_skins<class_ResourceImporterScene_property_skins/use_named_skins>`{.interpreted-text
  role="ref"} is `false`).

Together, this information is enough to tell Godot how to use the bone
poses in the `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} node to render the mesh from each
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}.
Note that each `MeshInstance3D<class_MeshInstance3D>`{.interpreted-text
role="ref"} may share binds, as is common in models exported from
Blender, or each
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"} may
use a separate `Skin<class_Skin>`{.interpreted-text role="ref"} object,
as is common in models exported from other tools such as Maya.
