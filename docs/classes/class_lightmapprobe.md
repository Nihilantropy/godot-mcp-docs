github_url
:   hide

# LightmapProbe {#class_LightmapProbe}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Represents a single manually placed probe for dynamic object lighting
with `LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**LightmapProbe** represents the position of a single manually placed
probe for dynamic object lighting with
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}. Lightmap
probes affect the lighting of
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"}-derived nodes that have their
`GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>`{.interpreted-text
role="ref"} set to
`GeometryInstance3D.GI_MODE_DYNAMIC<class_GeometryInstance3D_constant_GI_MODE_DYNAMIC>`{.interpreted-text
role="ref"}.

Typically, `LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}
probes are placed automatically by setting
`LightmapGI.generate_probes_subdiv<class_LightmapGI_property_generate_probes_subdiv>`{.interpreted-text
role="ref"} to a value other than
`LightmapGI.GENERATE_PROBES_DISABLED<class_LightmapGI_constant_GENERATE_PROBES_DISABLED>`{.interpreted-text
role="ref"}. By creating **LightmapProbe** nodes before baking
lightmaps, you can add more probes in specific areas for greater detail,
or disable automatic generation and rely only on manually placed probes
instead.

\*\*Note:\*\* **LightmapProbe** nodes that are placed after baking
lightmaps are ignored by dynamic objects. You must bake lightmaps again
after creating or modifying **LightmapProbe**s for the probes to be
effective.
