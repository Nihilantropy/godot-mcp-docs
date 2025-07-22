# Upgrading from Godot 4.3 to Godot 4.4 {#doc_upgrading_to_godot_4.4}

For most games and apps made with 4.3 it should be relatively safe to
migrate to 4.4. This page intends to cover everything you need to pay
attention to when migrating your project.

## Breaking changes

If you are migrating from 4.3 to 4.4, the breaking changes listed here
might affect you. Changes are grouped by areas/systems.

This article indicates whether each breaking change affects GDScript and
whether the C# breaking change is *binary compatible* or *source
compatible*:

- **Binary compatible** - Existing binaries will load and execute
  successfully without recompilation, and the run-time behavior won\'t
  change.
- **Source compatible** - Source code will compile successfully without
  changes when upgrading Godot.

### Core

  Change                                                                     GDScript Compatible                                                               C# Binary Compatible                                                                                                C# Source Compatible   Introduced
  -------------------------------------------------------------------------- --------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------- ---------------------- -------------
  **FileAccess**                                                                                                                                                                                                                                                                                          
  Method `open_encrypted` adds a new `iv` optional parameter                 `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -98918\`\_
  Method `store_8` changes return type from `void` to `bool`                 `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_16` changes return type from `void` to `bool`                `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_32` changes return type from `void` to `bool`                `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_64` changes return type from `void` to `bool`                `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_buffer` changes return type from `void` to `bool`            `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_csv_line` changes return type from `void` to `bool`          `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_double` changes return type from `void` to `bool`            `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_float` changes return type from `void` to `bool`             `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_half` changes return type from `void` to `bool`              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_line` changes return type from `void` to `bool`              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_pascal_string` changes return type from `void` to `bool`     `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_real` changes return type from `void` to `bool`              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_string` changes return type from `void` to `bool`            `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  Method `store_var` changes return type from `void` to `bool`               `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-78289\`\_
  **OS**                                                                                                                                                                                                                                                                                                  
  Method `execute_with_pipe` adds a new `blocking` optional parameter        `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -94434\`\_
  Method `read_string_from_stdin` adds a new `buffer_size` parameter[^1]     `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `✔️ (This API does not break compatibility. A compatibility method was added.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \`G   H-91201\`\_
  **RegEx**                                                                                                                                                                                                                                                                                               
  Method `compile` adds a new `show_error` optional parameter                `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -95212\`\_
  Method `create_from_string` adds a new `show_error` optional parameter     `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -95212\`\_
  **Semaphore**                                                                                                                                                                                                                                                                                           
  Method `post` adds a new `count` optional parameter                        `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -93605\`\_
  **TranslationServer**                                                                                                                                                                                                                                                                                   
  Method `standardize_locale` adds a new `add_defaults` optional parameter   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -98972\`\_

### GUI nodes

  Change                                                                                    GDScript Compatible                                                               C# Binary Compatible                                                   C# Source Compatible                                                   Introduced
  ----------------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------
  **RichTextLabel**                                                                                                                                                                                                                                                                                                         
  Method `push_meta` adds a new `tooltip` optional parameter                                `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                   ️with compat\| \`GH                                                     -99481\`\_
  Method `set_table_column_expand` adds a new `shrink` optional parameter                   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                   ️with compat\| \`GH                                                     -101482\`\_
  **GraphEdit**                                                                                                                                                                                                                                                                                                             
  Method `connect_node` adds a new `keep_alive` optional parameter                          `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                   ️with compat\| \`GH                                                     -97449\`\_
  Signal `frame_rect_changed` changes `new_rect` parameter type from `Vector2` to `Rect2`   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-102796](https://github.com/godotengine/godot/pull/102796)

### Physics

  Change                                                                GDScript Compatible                                                               C# Binary Compatible   C# Source Compatible   Introduced
  --------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------- ---------------------- ------------
  **SoftBody3D**                                                                                                                                                                                        
  Method `set_point_pinned` adds a new `insert_at` optional parameter   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔   ️with compat\| \`GH     -94684\`\_

### Rendering

  Change                                                                                                  GDScript Compatible                                                               C# Binary Compatible                                                                                                C# Source Compatible   Introduced
  ------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------- ---------------------- --------------
  **CPUParticles2D**                                                                                                                                                                                                                                                                                                                   
  Method `restart` adds a new `keep_seed` optional parameter                                              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -92089\`\_
  **CPUParticles3D**                                                                                                                                                                                                                                                                                                                   
  Method `restart` adds a new `keep_seed` optional parameter                                              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -92089\`\_
  **GPUParticles2D**                                                                                                                                                                                                                                                                                                                   
  Method `restart` adds a new `keep_seed` optional parameter                                              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -92089\`\_
  **GPUParticles3D**                                                                                                                                                                                                                                                                                                                   
  Method `restart` adds a new `keep_seed` optional parameter                                              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -92089\`\_
  **RenderingDevice**                                                                                                                                                                                                                                                                                                                  
  Method `draw_list_begin` adds a new `breadcrumb` optional parameter                                     `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -90993\`\_
  Method `draw_list_begin` removes many parameters                                                        `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `✔️ (This API does not break compatibility. A compatibility method was added.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \`G   H-98670\`\_
  Method `index_buffer_create` adds a new `enable_device_address` optional parameter                      `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -100062\`\_
  Method `uniform_buffer_create` adds a new `enable_device_address` optional parameter                    `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -100062\`\_
  Method `vertex_buffer_create` adds a new `enable_device_address` optional parameter                     `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -100062\`\_
  **RenderingServer**                                                                                                                                                                                                                                                                                                                  
  Method `multimesh_allocate_data` adds a new `use_indirect` optional parameter                           `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                                                                ️with compat\| \`GH     -99455\`\_
  **Shader**                                                                                                                                                                                                                                                                                                                           
  Method `get_default_texture_parameter` changes return type from `Texture2D` to `Texture`                `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ❌\| \`                GH-95126\`\_
  Method `set_default_texture_parameter` changes `texture` parameter type from `Texture2D` to `Texture`   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ✔️\| \`G               H-95126\`\_
  **VisualShaderNodeCubemap**                                                                                                                                                                                                                                                                                                          
  Property `cube_map` changes type from `Cubemap` to `TextureLayered`                                     `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ❌\| \`                GH-95126\`\_
  **VisualShaderNodeTexture2DArray**                                                                                                                                                                                                                                                                                                   
  Property `texture_array` changes type from `Texture2DArray` to `TextureLayered`                         `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                                                             ❌\| \`                GH-95126\`\_

:::: note
::: title
Note
:::

In C#, the enum `RenderingDevice.StorageBufferUsage` breaks
compatibility because of the way the bindings generator detects the enum
prefix. New members where added in
[GH-100062](https://github.com/godotengine/godot/pull/100062) to the
enum that caused the enum members to be renamed.
::::

### Navigation

  Change                                                         GDScript Compatible                                                               C# Binary Compatible   C# Source Compatible   Introduced
  -------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------- ---------------------- -------------
  **NavigationServer2D**                                                                                                                                                                         
  Method `query_path` adds a new `callback` optional parameter   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔   ️with compat\| \`GH     -100129\`\_
  **NavigationServer3D**                                                                                                                                                                         
  Method `query_path` adds a new `callback` optional parameter   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔   ️with compat\| \`GH     -100129\`\_

### Editor plugins

  Change                                                                                                            GDScript Compatible                                                               C# Binary Compatible                                                   C# Source Compatible                                                   Introduced
  ----------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------
  **EditorInterface**                                                                                                                                                                                                                                                                                                                               
  Method `open_scene_from_path` adds a new `set_inherited` optional parameter                                       `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                   ️with compat\| \`GH                                                     -90057\`\_
  Method `popup_node_selector` adds a new `current_value` optional parameter                                        `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                   ️with compat\| \`GH                                                     -94323\`\_
  Method `popup_property_selector` adds a new `current_value` optional parameter                                    `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                   ️with compat\| \`GH                                                     -94323\`\_
  **EditorSceneFormatImporter**                                                                                                                                                                                                                                                                                                                     
  Method `_get_import_flags` removed                                                                                `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-101531](https://github.com/godotengine/godot/pull/101531)
  **EditorTranslationParserPlugin**                                                                                                                                                                                                                                                                                                                 
  Method `_parse_file` changes return type to `Array` and removes `msgids` and `msgids_context_plural` parameters   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-99297](https://github.com/godotengine/godot/pull/99297)

:::: note
::: title
Note
:::

The method `_get_import_flags` was never used by the engine. It was
removed despite the compatibility breakage as there\'s no way for users
to rely on this affecting engine behavior.
::::

## Behavior changes

### Core

:::: note
::: title
Note
:::

The `Curve` resource now enforces its value range, so `min_value` and
`max_value` need to be changed if any of the points fall outside of the
default `[0, 1]` range.
::::

### Rendering

:::: note
::: title
Note
:::

The `VisualShaderNodeVec4Constant` shader node had its input type
changed to `Vector4`. Users need to recreate the values in their
constants.
::::

### CSG

:::: note
::: title
Note
:::

The CSG implementation now uses Emmett Lalish\'s
[Manifold](https://github.com/elalish/manifold) library
([GH-94321](https://github.com/godotengine/godot/pull/94321)). The new
implementation is more consistent with manifold definitions and fixes a
number of bugs and stability issues. As a result, non-manifold meshes
are no longer supported. You can use `MeshInstance3D` for rendering
non-manifold geometry, such as quads or planes.
::::

### Android

:::: note
::: title
Note
:::

Android sensor events are no longer enabled by default
([GH-94799](https://github.com/godotengine/godot/pull/94799)). Projects
that use sensor events can enable them as needed in Project Settings
under **Input Devices \> Sensors**.
::::

[^1]: Default buffer size in 4.3 is `1024`.
