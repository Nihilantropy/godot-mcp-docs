github_url
:   hide

# ShaderGlobalsOverride {#class_ShaderGlobalsOverride}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node used to override global shader parameters\' values in a scene.

::: rst-class
classref-introduction-group
:::

## Description

Similar to how a
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text role="ref"}
node can be used to override the environment while a specific scene is
loaded, **ShaderGlobalsOverride** can be used to override global shader
parameters temporarily. Once the node is removed, the project-wide
values for the global shader parameters are restored. See the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
`global_shader_parameter_*` methods for more information.

\*\*Note:\*\* Only one **ShaderGlobalsOverride** can be used per scene.
If there is more than one **ShaderGlobalsOverride** node in the scene
tree, only the first node (in tree order) will be taken into account.

\*\*Note:\*\* All **ShaderGlobalsOverride** nodes are made part of a
`"shader_overrides_group"` group when they are added to the scene tree.
The currently active **ShaderGlobalsOverride** node also has a
`"shader_overrides_group_active"` group added to it. You can use this to
check which **ShaderGlobalsOverride** node is currently active.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Shading language <../tutorials/shaders/shader_reference/shading_language>`{.interpreted-text
  role="doc"}
