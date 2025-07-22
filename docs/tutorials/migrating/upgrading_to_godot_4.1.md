# Upgrading from Godot 4.0 to Godot 4.1 {#doc_upgrading_to_godot_4.1}

For most games and apps made with 4.0, it should be relatively safe to
migrate to 4.1. This page intends to cover everything you need to pay
attention to when migrating your project.

## Breaking changes

If you are migrating from 4.0 to 4.1, the breaking changes listed here
might affect you. Changes are grouped by areas/systems.

:::: warning
::: title
Warning
:::

The GDExtension API completely breaks compatibility in 4.1, so it\'s not
included in the table below. See the
`updating_your_gdextension_for_godot_4_1`{.interpreted-text role="ref"}
section for more information.
::::

This article indicates whether each breaking change affects GDScript and
whether the C# breaking change is *binary compatible* or *source
compatible*:

- **Binary compatible** - Existing binaries will load and execute
  successfully without recompilation, and the runtime behavior won\'t
  change.
- **Source compatible** - Source code will compile successfully without
  changes when upgrading Godot.

### Core

  Change                                                                                       GDScript Compatible                                                               C# Binary Compatible   C# Source Compatible   Introduced
  -------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------- ---------------------- --------------
  **Basis**                                                                                                                                                                                                                    
  Method `looking_at` adds a new `use_model_front` optional parameter                          `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️\| \|✔               ️\| \`GH                -76082\`\_
  **Object**                                                                                                                                                                                                                   
  Method `get_meta_list` changes return type from `PackedStringArray` to `Array[StringName]`   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                ❌\| \`                GH-76418\`\_
  **Transform3D**                                                                                                                                                                                                              
  Method `looking_at` adds a new `use_model_front` optional parameter                          `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️\| \|✔               ️\| \`GH                -76082\`\_
  **UndoRedo**                                                                                                                                                                                                                 
  Method `create_action` adds a new `backward_undo_ops` optional parameter                     `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔   ️\| \`GH                -76688\`\_
  **WorkerThreadPool**                                                                                                                                                                                                         
  Method `wait_for_task_completion` changes return type from `void` to `Error`                 `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                ✔️\| \`G               H-77143\`\_

### Animation

  Change                                                                                         GDScript Compatible                                                               C# Binary Compatible                                                   C# Source Compatible                                                   Introduced
  ---------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------------- -------------------------------------------------------------
  **AnimationNode**                                                                                                                                                                                                                                                                                                              
  Method `_process` adds a new `test_only` parameter                                             `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-75759](https://github.com/godotengine/godot/pull/75759)
  Method `blend_input` adds a new `test_only` optional parameter                                 `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                   ️\| \`GH                                                                -75759\`\_
  Method `blend_node` adds a new `test_only` optional parameter                                  `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                   ️\| \`GH                                                                -75759\`\_
  **AnimationNodeStateMachinePlayback**                                                                                                                                                                                                                                                                                          
  Method `get_travel_path` changes return type from `PackedStringArray` to `Array[StringName]`   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                ❌\| \`                                                                GH-76418\`\_

### 2D nodes

  Change                         GDScript Compatible                                                    C# Binary Compatible                                                   C# Source Compatible                                                   Introduced
  ------------------------------ ---------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------------- -------------------------------------------------------------
  **PathFollow2D**                                                                                                                                                                                                                                    
  Property `lookahead` removed   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-72842](https://github.com/godotengine/godot/pull/72842)

### 3D nodes

+-------------+-------------+-------------+-------------+------------+
| Change      | GDScript    | C# Binary   | C# Source   | Introduced |
|             | Compatible  | Compatible  | Compatible  |            |
+=============+=============+=============+=============+============+
| **G         |             |             |             |            |
| eometry3D** |             |             |             |            |
+-------------+-------------+-------------+-------------+------------+
| Method      | `✔️ (Thi     | ✔️ with     | |           | -76418\`\_ |
| `segm       | s API does  | compat\|    |             |            |
| ent_interse | not break c | \|❌        |        \`GH |            |
| cts_convex` | ompatibilit |             |             |            |
| changes     | y.)`{.inter |             |             |            |
| `planes`    | preted-text |             |             |            |
| parameter   | r           |             |             |            |
| type from   | ole="abbr"} |             |             |            |
| untyped     | \|          |             |             |            |
| `Array` to  |             |             |             |            |
| `Ar         |             |             |             |            |
| ray[Plane]` |             |             |             |            |
+-------------+-------------+-------------+-------------+------------+
| **MeshI     |             |             |             |            |
| nstance3D** |             |             |             |            |
+-------------+-------------+-------------+-------------+------------+
| Method      | `✔️ (Thi     | ✔️ with     | ️\| \`GH     | -72152\`\_ |
| `c          | s API does  | compat\|    |             |            |
| reate_multi | not break c | \|✔         |             |            |
| ple_convex_ | ompatibilit |             |             |            |
| collisions` | y.)`{.inter |             |             |            |
| adds a new  | preted-text |             |             |            |
| `settings`  | r           |             |             |            |
| optional    | ole="abbr"} |             |             |            |
| parameter   | \|          |             |             |            |
+-------------+-------------+-------------+-------------+------------+
| **Node3D**  |             |             |             |            |
+-------------+-------------+-------------+-------------+------------+
| Method      | `✔️ (Thi     | ✔️ with     | ️\| \`GH     | -76082\`\_ |
| `look_at`   | s API does  | compat\|    |             |            |
| adds a new  | not break c | \|✔         |             |            |
| `use_m      | ompatibilit |             |             |            |
| odel_front` | y.)`{.inter |             |             |            |
| optional    | preted-text |             |             |            |
| parameter   | r           |             |             |            |
|             | ole="abbr"} |             |             |            |
|             | \|          |             |             |            |
+-------------+-------------+-------------+-------------+------------+
| Method      | `✔️ (Thi     | ✔️ with     | ️\| \`GH     | -76082\`\_ |
| `           | s API does  | compat\|    |             |            |
| look_at_fro | not break c | \|✔         |             |            |
| m_position` | ompatibilit |             |             |            |
| adds a new  | y.)`{.inter |             |             |            |
| `use_m      | preted-text |             |             |            |
| odel_front` | r           |             |             |            |
| optional    | ole="abbr"} |             |             |            |
| parameter   | \|          |             |             |            |
+-------------+-------------+-------------+-------------+------------+

### GUI nodes

  Change                                                                         GDScript Compatible                                                               C# Binary Compatible   C# Source Compatible   Introduced
  ------------------------------------------------------------------------------ --------------------------------------------------------------------------------- ---------------------- ---------------------- ------------
  **CodeEdit**                                                                                                                                                                                                   
  Method `add_code_completion_option` adds a new `location` optional parameter   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔   ️\| \`GH                -75746\`\_
  **RichTextLabel**                                                                                                                                                                                              
  Method `push_list` adds a new `bullet` optional parameter                      `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔   ️\| \`GH                -75017\`\_
  Method `push_paragraph` adds a new `justification_flags` optional parameter    `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔   ️\| \`GH                -75250\`\_
  Method `push_paragraph` adds a new `tab_stops` optional parameter              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔   ️\| \`GH                -76401\`\_
  **Tree**                                                                                                                                                                                                       
  Method `edit_selected` adds a new `force_edit` optional parameter              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔   ️\| \`GH                -76794\`\_

### Physics

  Change                                                                                            GDScript Compatible                                                    C# Binary Compatible                                                   C# Source Compatible                                                   Introduced
  ------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------------- -------------------------------------------------------------
  **Area2D**                                                                                                                                                                                                                                                                                                             
  Property `priority` changes type from `float` to `int`                                            `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-72749](https://github.com/godotengine/godot/pull/72749)
  **Area3D**                                                                                                                                                                                                                                                                                                             
  Property `priority` changes type from `float` to `int`                                            `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-72749](https://github.com/godotengine/godot/pull/72749)
  **PhysicsDirectSpaceState2D**                                                                                                                                                                                                                                                                                          
  Method `collide_shape` changes return type from `Array[PackedVector2Array]` to `Array[Vector2]`   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-75260](https://github.com/godotengine/godot/pull/75260)
  **PhysicsDirectSpaceState3D**                                                                                                                                                                                                                                                                                          
  Method `collide_shape` changes return type from `Array[PackedVector3Array]` to `Array[Vector3]`   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-75260](https://github.com/godotengine/godot/pull/75260)

### Rendering

+-------------+-------------+-------------+-------------+-------------+
| Change      | GDScript    | C# Binary   | C# Source   | Introduced  |
|             | Compatible  | Compatible  | Compatible  |             |
+=============+=============+=============+=============+=============+
| **RDS       |             |             |             |             |
| haderFile** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Method      | `✔️ (Thi     | ❌\| \|     | ❌\| \`     | G           |
| `get_ve     | s API does  |             |             | H-76418\`\_ |
| rsion_list` | not break c |             |             |             |
| changes     | ompatibilit |             |             |             |
| return type | y.)`{.inter |             |             |             |
| from        | preted-text |             |             |             |
| `PackedS    | r           |             |             |             |
| tringArray` | ole="abbr"} |             |             |             |
| to          | \|          |             |             |             |
| `Array[S    |             |             |             |             |
| tringName]` |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Render    |             |             |             |             |
| ingDevice** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Method      | `✔️ (Thi     | ✔️ with     | |           | -76418\`\_  |
| `draw_      | s API does  | compat\|    |             |             |
| list_begin` | not break c | \|❌        |        \`GH |             |
| changes     | ompatibilit |             |             |             |
| `storag     | y.)`{.inter |             |             |             |
| e_textures` | preted-text |             |             |             |
| parameter   | r           |             |             |             |
| type from   | ole="abbr"} |             |             |             |
| untyped     | \|          |             |             |             |
| `Array` to  |             |             |             |             |
| `           |             |             |             |             |
| Array[RID]` |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Render    |             |             |             |             |
| ingServer** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Method      | `✔️ (Thi     | ❌\| \|     | ❌\| \`     | G           |
| `           | s API does  |             |             | H-76418\`\_ |
| global_shad | not break c |             |             |             |
| er_paramete | ompatibilit |             |             |             |
| r_get_list` | y.)`{.inter |             |             |             |
| changes     | preted-text |             |             |             |
| return type | r           |             |             |             |
| from        | ole="abbr"} |             |             |             |
| `PackedS    | \|          |             |             |             |
| tringArray` |             |             |             |             |
| to          |             |             |             |             |
| `Array[S    |             |             |             |             |
| tringName]` |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Su        |             |             |             |             |
| rfaceTool** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Method      | `✔️ (Thi     | ✔️ with     | |           | -76418\`\_  |
| `add_tr     | s API does  | compat\|    |             |             |
| iangle_fan` | not break c | \|❌        |        \`GH |             |
| changes     | ompatibilit |             |             |             |
| `tangents`  | y.)`{.inter |             |             |             |
| parameter   | preted-text |             |             |             |
| type from   | r           |             |             |             |
| untyped     | ole="abbr"} |             |             |             |
| `Array` to  | \|          |             |             |             |
| `Ar         |             |             |             |             |
| ray[Plane]` |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

### Navigation

  Change                                                                                                              GDScript Compatible                                                               C# Binary Compatible                                                   C# Source Compatible                                                   Introduced
  ------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------------- -------------------------------------------------------------
  **NavigationAgent2D**                                                                                                                                                                                                                                                                                                                               
  Method `set_velocity` replaced with `velocity` property                                                             `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                ❌\| \`                                                                GH-69988\`\_
  Property `time_horizon` split into `time_horizon_agents` and `time_horizon_obstacles`                               `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  **NavigationAgent3D**                                                                                                                                                                                                                                                                                                                               
  Property `agent_height_offset` renamed to `path_height_offset`                                                      `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  Property `ignore_y` removed                                                                                         `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  Method `set_velocity` replaced with `velocity` property                                                             `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                ❌\| \`                                                                GH-69988\`\_
  Property `time_horizon` split into `time_horizon_agents` and `time_horizon_obstacles`                               `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  **NavigationObstacle2D**                                                                                                                                                                                                                                                                                                                            
  Property `estimate_radius` removed                                                                                  `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  Method `get_rid` renamed to `get_agent_rid`                                                                         `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  **NavigationObstacle3D**                                                                                                                                                                                                                                                                                                                            
  Property `estimate_radius` removed                                                                                  `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  Method `get_rid` renamed to `get_agent_rid`                                                                         `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  **NavigationServer2D**                                                                                                                                                                                                                                                                                                                              
  Method `agent_set_callback` renamed to `agent_set_avoidance_callback`                                               `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  Method `agent_set_target_velocity` removed                                                                          `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  Method `agent_set_time_horizon` split into `agent_set_time_horizon_agents` and `agent_set_time_horizon_obstacles`   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  **NavigationServer3D**                                                                                                                                                                                                                                                                                                                              
  Method `agent_set_callback` renamed to `agent_set_avoidance_callback`                                               `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  Method `agent_set_target_velocity` removed                                                                          `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)
  Method `agent_set_time_horizon` split into `agent_set_time_horizon_agents` and `agent_set_time_horizon_obstacles`   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-69988](https://github.com/godotengine/godot/pull/69988)

### Networking

  Change                                                                                   GDScript Compatible                                                               C# Binary Compatible   C# Source Compatible   Introduced
  ---------------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------- ---------------------- -------------
  **WebRTCPeerConnectionExtension**                                                                                                                                                                                        
  Method `_create_data_channel` changes return type from `Object` to `WebRTCDataChannel`   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                ✔️\| \`G               H-78237\`\_

### Editor plugins

  Change                                                                          GDScript Compatible                                                               C# Binary Compatible                                                   C# Source Compatible                                                   Introduced
  ------------------------------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------------------------------------------------------- ---------------------------------------------------------------------- -------------------------------------------------------------
  **AnimationTrackEditPlugin**                                                                                                                                                                                                                                                                                    
  Type `AnimationTrackEditPlugin` removed                                         `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-76413](https://github.com/godotengine/godot/pull/76413)
  **EditorInterface**                                                                                                                                                                                                                                                                                             
  Type `EditorInterface` changes inheritance from `Node` to `Object`              `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                ❌\| \`                                                                GH-76176\`\_
  Method `set_movie_maker_enabled` replaced with `movie_maker_enabled` property   `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                ❌\| \`                                                                GH-76176\`\_
  Method `is_movie_maker_enabled` replaced with `movie_maker_enabled` property    `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ❌\| \|                                                                ❌\| \`                                                                GH-76176\`\_
  **EditorResourcePreviewGenerator**                                                                                                                                                                                                                                                                              
  Method `_generate` adds a new `metadata` parameter                              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-64628](https://github.com/godotengine/godot/pull/64628)
  Method `_generate_from_path` adds a new `metadata` parameter                    `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}              `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   `❌ (This API breaks compatibility.)`{.interpreted-text role="abbr"}   [GH-64628](https://github.com/godotengine/godot/pull/64628)
  **EditorUndoRedoManager**                                                                                                                                                                                                                                                                                       
  Method `create_action` adds a new `backward_undo_ops` optional parameter        `✔️ (This API does not break compatibility.)`{.interpreted-text role="abbr"} \|   ✔️ with compat\| \|✔                                                   ️\| \`GH                                                                -76688\`\_

## Behavior changes

In 4.1 some behavior changes have been introduced, which might require
you to adjust your project.

  Change                                                                                                                                                                                                                                           Introduced
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------
  **SubViewportContainer**                                                                                                                                                                                                                         
  When input events should reach SubViewports and their children, `SubViewportContainer.mouse_filter` now needs to be `MOUSE_FILTER_STOP` or `MOUSE_FILTER_PASS`. See [GH-79271](https://github.com/godotengine/godot/issues/79271) for details.   [GH-57894](https://github.com/godotengine/godot/pull/57894)
  Multiple layered `SubViewportContainer` nodes, that should all receive mouse input events, now need to be replaced by `Area2D` nodes. See [GH-79128](https://github.com/godotengine/godot/issues/79128) for details.                             [GH-57894](https://github.com/godotengine/godot/pull/57894)
  **Viewport**                                                                                                                                                                                                                                     
  `Viewport` nodes, that have Physics Picking enabled, now automatically set InputEvents as handled. See [GH-79897](https://github.com/godotengine/godot/issues/79897) for workarounds.                                                            [GH-77595](https://github.com/godotengine/godot/pull/77595)

## Updating your GDExtension for 4.1 {#updating_your_gdextension_for_godot_4_1}

In order to fix a serious bug, in Godot 4.1 we had to break binary
compatibility in a big way and source compatibility in a small way.

This means that GDExtensions made for Godot 4.0 will need to be
recompiled for Godot 4.1 (using the `4.1` branch of godot-cpp), with a
small change to their source code.

In Godot 4.0, your \"entry_symbol\" function looks something like this:

``` cpp
GDExtensionBool GDE_EXPORT example_library_init(const GDExtensionInterface *p_interface, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
    godot::GDExtensionBinding::InitObject init_obj(p_interface, p_library, r_initialization);

    init_obj.register_initializer(initialize_example_module);
    init_obj.register_terminator(uninitialize_example_module);
    init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

    return init_obj.init();
}
```

However, for Godot 4.1, it should look like:

``` cpp
GDExtensionBool GDE_EXPORT example_library_init(GDExtensionInterfaceGetProcAddress p_get_proc_address, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization) {
    godot::GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);

    init_obj.register_initializer(initialize_example_module);
    init_obj.register_terminator(uninitialize_example_module);
    init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

    return init_obj.init();
}
```

There are two small changes:

1.  The first argument changes from
    `const GDExtensionInterface *p_interface` to
    `GDExtensionInterfaceGetProcAddress p_get_proc_address`
2.  The constructor for the [init_obj]{.title-ref} variable now receives
    `p_get_proc_address` as its first parameter

You also need to add an extra `compatibility_minimum` line to your
`.gdextension` file, so that it looks something like:

    [configuration]

    entry_symbol = "example_library_init"
    compatibility_minimum = 4.1

This lets Godot know that your GDExtension has been updated and is safe
to load in Godot 4.1.
