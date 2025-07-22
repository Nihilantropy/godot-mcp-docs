article_outdated
:   True

::: {.meta keywords="cheatsheet, cheat sheet, shortcut"}
:::

# Default editor shortcuts {#doc_default_key_mapping}

Many Godot editor functions can be executed with keyboard shortcuts.
This page lists functions which have associated shortcuts by default,
but many others are available for customization in editor settings as
well. To change keys associated with these and other actions navigate to
**Editor \> Editor Settings \> Shortcuts**.

While some actions are universal, a lot of shortcuts are specific to
individual tools. For this reason it is possible for some key
combinations to be assigned to more than one function. The correct
action will be performed depending on the context.

:::: note
::: title
Note
:::

While Windows and Linux builds of the editor share most of the default
settings, some shortcuts may differ for macOS version. This is done for
better integration of the editor into macOS ecosystem. Users fluent with
standard shortcuts on that OS should find Godot Editor\'s default key
mapping intuitive.
::::

## General editor actions

  ---------------------------------------------------------------------------------------------------------------------------------------
  Action name   Windows, Linux                               macOS                                       Editor setting
  ------------- -------------------------------------------- ------------------------------------------- --------------------------------
  Open 2D       `Ctrl + F1`{.interpreted-text role="kbd"}    `Cmd + Ctrl + 1`{.interpreted-text          `editor/editor_2d`
  Editor                                                     role="kbd"}                                 

  Open 3D       `Ctrl + F2`{.interpreted-text role="kbd"}    `Cmd + Ctrl + 2`{.interpreted-text          `editor/editor_3d`
  Editor                                                     role="kbd"}                                 

  Open Script   `Ctrl + F3`{.interpreted-text role="kbd"}    `Cmd + Ctrl + 3`{.interpreted-text          `editor/editor_script`
  Editor                                                     role="kbd"}                                 

  Search Help   `F1`{.interpreted-text role="kbd"}           `Opt + Space`{.interpreted-text role="kbd"} `editor/editor_help`

  Distraction   `Ctrl + Shift + F11`{.interpreted-text       `Cmd + Ctrl + D`{.interpreted-text          `editor/distraction_free_mode`
  Free Mode     role="kbd"}                                  role="kbd"}                                 

  Next Scene    `Ctrl + Tab`{.interpreted-text role="kbd"}   `Ctrl + Tab`{.interpreted-text role="kbd"}  `editor/next_tab`
  Tab                                                                                                    

  Previous      `Ctrl + Shift + Tab`{.interpreted-text       `Ctrl + Shift + Tab`{.interpreted-text      `editor/prev_tab`
  Scene Tab     role="kbd"}                                  role="kbd"}                                 

  Filter Files  `Ctrl + Alt + P`{.interpreted-text           `Opt + Cmd + P`{.interpreted-text           `editor/filter_files`
                role="kbd"}                                  role="kbd"}                                 

  Open Scene    `Ctrl + O`{.interpreted-text role="kbd"}     `Cmd + O`{.interpreted-text role="kbd"}     `editor/open_scene`

  Close Scene   `Ctrl + Shift + W`{.interpreted-text         `Cmd + W`{.interpreted-text role="kbd"}     `editor/close_scene`
                role="kbd"}                                                                              

  Reopen Closed `Ctrl + Shift + T`{.interpreted-text         `Cmd + Shift + T`{.interpreted-text         `editor/reopen_closed_scene`
  Scene         role="kbd"}                                  role="kbd"}                                 

  Save Scene    `Ctrl + S`{.interpreted-text role="kbd"}     `Cmd + S`{.interpreted-text role="kbd"}     `editor/save_scene`

  Save Scene As `Ctrl + Shift + S`{.interpreted-text         `Cmd + Shift + S`{.interpreted-text         `editor/save_scene_as`
                role="kbd"}                                  role="kbd"}                                 

  Save All      `Ctrl + Shift + Alt + S`{.interpreted-text   `Cmd + Shift + Opt + S`{.interpreted-text   `editor/save_all_scenes`
  Scenes        role="kbd"}                                  role="kbd"}                                 

  Quick Open    `Shift + Alt + O`{.interpreted-text          `Cmd + Ctrl + O`{.interpreted-text          `editor/quick_open`
                role="kbd"}                                  role="kbd"}                                 

  Quick Open    `Ctrl + Shift + O`{.interpreted-text         `Cmd + Shift + O`{.interpreted-text         `editor/quick_open_scene`
  Scene         role="kbd"}                                  role="kbd"}                                 

  Quick Open    `Ctrl + Alt + O`{.interpreted-text           `Opt + Cmd + O`{.interpreted-text           `editor/quick_open_script`
  Script        role="kbd"}                                  role="kbd"}                                 

  Undo          `Ctrl + Z`{.interpreted-text role="kbd"}     `Cmd + Z`{.interpreted-text role="kbd"}     `editor/undo`

  Redo          `Ctrl + Shift + Z`{.interpreted-text         `Cmd + Shift + Z`{.interpreted-text         `editor/redo`
                role="kbd"}                                  role="kbd"}                                 

  Quit          `Ctrl + Q`{.interpreted-text role="kbd"}     `Cmd + Q`{.interpreted-text role="kbd"}     `editor/file_quit`

  Quit to       `Ctrl + Shift + Q`{.interpreted-text         `Shift + Opt + Q`{.interpreted-text         `editor/quit_to_project_list`
  Project List  role="kbd"}                                  role="kbd"}                                 

  Take          `Ctrl + F12`{.interpreted-text role="kbd"}   `Cmd + F12`{.interpreted-text role="kbd"}   `editor/take_screenshot`
  Screenshot                                                                                             

  Toggle        `Shift + F11`{.interpreted-text role="kbd"}  `Cmd + Ctrl + F`{.interpreted-text          `editor/fullscreen_mode`
  Fullscreen                                                 role="kbd"}                                 

  Play          `F5`{.interpreted-text role="kbd"}           `Cmd + B`{.interpreted-text role="kbd"}     `editor/play`

  Pause Scene   `F7`{.interpreted-text role="kbd"}           `Cmd + Ctrl + Y`{.interpreted-text          `editor/pause_scene`
                                                             role="kbd"}                                 

  Stop          `F8`{.interpreted-text role="kbd"}           `Cmd + .`{.interpreted-text role="kbd"}     `editor/stop`

  Play Scene    `F6`{.interpreted-text role="kbd"}           `Cmd + R`{.interpreted-text role="kbd"}     `editor/play_scene`

  Play Custom   `Ctrl + Shift + F5`{.interpreted-text        `Cmd + Shift + R`{.interpreted-text         `editor/play_custom_scene`
  Scene         role="kbd"}                                  role="kbd"}                                 

  Expand Bottom `Shift + F12`{.interpreted-text role="kbd"}  `Shift + F12`{.interpreted-text role="kbd"} `editor/bottom_panel_expand`
  Panel                                                                                                  

  Command       `Ctrl + Shift + P`{.interpreted-text         `Cmd + Shift + P`{.interpreted-text         `editor/command_palette`
  Palette       role="kbd"}                                  role="kbd"}                                 
  ---------------------------------------------------------------------------------------------------------------------------------------

## Bottom panels

Only bottom panels that are always available have a default shortcut
assigned. Others must be manually bound in the Editor Settings if
desired.

  -------------------------------------------------------------------------------------------------------------------------------------
  Action name         Windows, Linux                 macOS                          Editor setting
  ------------------- ------------------------------ ------------------------------ ---------------------------------------------------
  Toggle Last Opened  `Ctrl + J`{.interpreted-text   `Ctrl + J`{.interpreted-text   `editor/toggle_last_opened_bottom_panel`
  Panel               role="kbd"}                    role="kbd"}                    

  Toggle Animation    `Alt + N`{.interpreted-text    `Alt + N`{.interpreted-text    `bottom_panels/toggle_animation_bottom_panel`
  Bottom Panel        role="kbd"}                    role="kbd"}                    

  Toggle Audio Bottom `Alt + A`{.interpreted-text    `Alt + A`{.interpreted-text    `bottom_panels/toggle_audio_bottom_panel`
  Panel               role="kbd"}                    role="kbd"}                    

  Toggle Debugger     `Alt + D`{.interpreted-text    `Alt + D`{.interpreted-text    `bottom_panels/toggle_debugger_bottom_panel`
  Bottom Panel        role="kbd"}                    role="kbd"}                    

  Toggle FileSystem   `Alt + F`{.interpreted-text    `Alt + F`{.interpreted-text    `bottom_panels/toggle_filesystem_bottom_panel`
  Bottom Panel        role="kbd"}                    role="kbd"}                    

  Toggle Output       `Alt + O`{.interpreted-text    `Alt + O`{.interpreted-text    `bottom_panels/toggle_output_bottom_panel`
  Bottom Panel        role="kbd"}                    role="kbd"}                    

  Toggle Shader       `Alt + S`{.interpreted-text    `Alt + S`{.interpreted-text    `bottom_panels/toggle_shader_editor_bottom_panel`
  Editor Bottom Panel role="kbd"}                    role="kbd"}                    
  -------------------------------------------------------------------------------------------------------------------------------------

## 2D / CanvasItem editor

  ---------------------------------------------------------------------------------------------------------------------------------------------------
  Action name     Windows, Linux                         macOS                                 Editor setting
  --------------- -------------------------------------- ------------------------------------- ------------------------------------------------------
  Zoom In         `Ctrl + =`{.interpreted-text           `Cmd + =`{.interpreted-text           `canvas_item_editor/zoom_plus`
                  role="kbd"}                            role="kbd"}                           

  Zoom Out        `Ctrl + -`{.interpreted-text           `Cmd + -`{.interpreted-text           `canvas_item_editor/zoom_minus`
                  role="kbd"}                            role="kbd"}                           

  Zoom Reset      `Ctrl + 0`{.interpreted-text           `Cmd + 0`{.interpreted-text           `canvas_item_editor/zoom_reset`
                  role="kbd"}                            role="kbd"}                           

  Pan View        `Space`{.interpreted-text role="kbd"}  `Space`{.interpreted-text role="kbd"} `canvas_item_editor/pan_view`

  Select Mode     `Q`{.interpreted-text role="kbd"}      `Q`{.interpreted-text role="kbd"}     `canvas_item_editor/select_mode`

  Move Mode       `W`{.interpreted-text role="kbd"}      `W`{.interpreted-text role="kbd"}     `canvas_item_editor/move_mode`

  Rotate Mode     `E`{.interpreted-text role="kbd"}      `E`{.interpreted-text role="kbd"}     `canvas_item_editor/rotate_mode`

  Scale Mode      `S`{.interpreted-text role="kbd"}      `S`{.interpreted-text role="kbd"}     `canvas_item_editor/scale_mode`

  Ruler Mode      `R`{.interpreted-text role="kbd"}      `R`{.interpreted-text role="kbd"}     `canvas_item_editor/ruler_mode`

  Use Smart Snap  `Shift + S`{.interpreted-text          `Shift + S`{.interpreted-text         `canvas_item_editor/use_smart_snap`
                  role="kbd"}                            role="kbd"}                           

  Use Grid Snap   `Shift + G`{.interpreted-text          `Shift + G`{.interpreted-text         `canvas_item_editor/use_grid_snap`
                  role="kbd"}                            role="kbd"}                           

  Multiply grid   `Num *`{.interpreted-text role="kbd"}  `Num *`{.interpreted-text role="kbd"} `canvas_item_editor/multiply_grid_step`
  step by 2                                                                                    

  Divide grid     `Num /`{.interpreted-text role="kbd"}  `Num /`{.interpreted-text role="kbd"} `canvas_item_editor/divide_grid_step`
  step by 2                                                                                    

  Always Show     `G`{.interpreted-text role="kbd"}      `G`{.interpreted-text role="kbd"}     `canvas_item_editor/show_grid`
  Grid                                                                                         

  Show Helpers    `H`{.interpreted-text role="kbd"}      `H`{.interpreted-text role="kbd"}     `canvas_item_editor/show_helpers`

  Show Guides     `Y`{.interpreted-text role="kbd"}      `Y`{.interpreted-text role="kbd"}     `canvas_item_editor/show_guides`

  Center          `F`{.interpreted-text role="kbd"}      `F`{.interpreted-text role="kbd"}     `canvas_item_editor/center_selection`
  Selection                                                                                    

  Frame Selection `Shift + F`{.interpreted-text          `Shift + F`{.interpreted-text         `canvas_item_editor/frame_selection`
                  role="kbd"}                            role="kbd"}                           

  Preview Canvas  `Ctrl + Shift + P`{.interpreted-text   `Cmd + Shift + P`{.interpreted-text   `canvas_item_editor/preview_canvas_scale`
  Scale           role="kbd"}                            role="kbd"}                           

  Insert Key      `Ins`{.interpreted-text role="kbd"}    `Ins`{.interpreted-text role="kbd"}   `canvas_item_editor/anim_insert_key`

  Insert Key      `Ctrl + Ins`{.interpreted-text         `Cmd + Ins`{.interpreted-text         `canvas_item_editor/anim_insert_key_existing_tracks`
  (Existing       role="kbd"}                            role="kbd"}                           
  Tracks)                                                                                      

  Make Custom     `Ctrl + Shift + B`{.interpreted-text   `Cmd + Shift + B`{.interpreted-text   `canvas_item_editor/skeleton_make_bones`
  Bones from      role="kbd"}                            role="kbd"}                           
  Nodes                                                                                        

  Clear Pose      `Shift + K`{.interpreted-text          `Shift + K`{.interpreted-text         `canvas_item_editor/anim_clear_pose`
                  role="kbd"}                            role="kbd"}                           
  ---------------------------------------------------------------------------------------------------------------------------------------------------

## 3D / Spatial editor {#doc_default_key_mapping_shortcuts_spatial_editor}

  --------------------------------------------------------------------------------------------------------------------------------------------------
  Action name              Windows, Linux                       macOS                               Editor setting
  ------------------------ ------------------------------------ ----------------------------------- ------------------------------------------------
  Toggle Freelook          `Shift + F`{.interpreted-text        `Shift + F`{.interpreted-text       `spatial_editor/freelook_toggle`
                           role="kbd"}                          role="kbd"}                         

  Freelook Left            `A`{.interpreted-text role="kbd"}    `A`{.interpreted-text role="kbd"}   `spatial_editor/freelook_left`

  Freelook Right           `D`{.interpreted-text role="kbd"}    `D`{.interpreted-text role="kbd"}   `spatial_editor/freelook_right`

  Freelook Forward         `W`{.interpreted-text role="kbd"}    `W`{.interpreted-text role="kbd"}   `spatial_editor/freelook_forward`

  Freelook Backwards       `S`{.interpreted-text role="kbd"}    `S`{.interpreted-text role="kbd"}   `spatial_editor/freelook_backwards`

  Freelook Up              `E`{.interpreted-text role="kbd"}    `E`{.interpreted-text role="kbd"}   `spatial_editor/freelook_up`

  Freelook Down            `Q`{.interpreted-text role="kbd"}    `Q`{.interpreted-text role="kbd"}   `spatial_editor/freelook_down`

  Freelook Speed Modifier  `Shift`{.interpreted-text            `Shift`{.interpreted-text           `spatial_editor/freelook_speed_modifier`
                           role="kbd"}                          role="kbd"}                         

  Freelook Slow Modifier   `Alt`{.interpreted-text role="kbd"}  `Opt`{.interpreted-text role="kbd"} `spatial_editor/freelook_slow_modifier`

  Select Mode              `Q`{.interpreted-text role="kbd"}    `Q`{.interpreted-text role="kbd"}   `spatial_editor/tool_select`

  Move Mode                `W`{.interpreted-text role="kbd"}    `W`{.interpreted-text role="kbd"}   `spatial_editor/tool_move`

  Rotate Mode              `E`{.interpreted-text role="kbd"}    `E`{.interpreted-text role="kbd"}   `spatial_editor/tool_rotate`

  Scale Mode               `R`{.interpreted-text role="kbd"}    `R`{.interpreted-text role="kbd"}   `spatial_editor/tool_scale`

  Use Local Space          `T`{.interpreted-text role="kbd"}    `T`{.interpreted-text role="kbd"}   `spatial_editor/local_coords`

  Use Snap                 `Y`{.interpreted-text role="kbd"}    `Y`{.interpreted-text role="kbd"}   `spatial_editor/snap`

  Snap Object to Floor     `PgDown`{.interpreted-text           `PgDown`{.interpreted-text          `spatial_editor/snap_to_floor`
                           role="kbd"}                          role="kbd"}                         

  Top View                 `Num 7`{.interpreted-text            `Num 7`{.interpreted-text           `spatial_editor/top_view`
                           role="kbd"}                          role="kbd"}                         

  Bottom View              `Alt + Num 7`{.interpreted-text      `Opt + Num 7`{.interpreted-text     `spatial_editor/bottom_view`
                           role="kbd"}                          role="kbd"}                         

  Front View               `Num 1`{.interpreted-text            `Num 1`{.interpreted-text           `spatial_editor/front_view`
                           role="kbd"}                          role="kbd"}                         

  Rear View                `Alt + Num 1`{.interpreted-text      `Opt + Num 1`{.interpreted-text     `spatial_editor/rear_view`
                           role="kbd"}                          role="kbd"}                         

  Right View               `Num 3`{.interpreted-text            `Num 3`{.interpreted-text           `spatial_editor/right_view`
                           role="kbd"}                          role="kbd"}                         

  Left View                `Alt + Num 3`{.interpreted-text      `Opt + Num 3`{.interpreted-text     `spatial_editor/left_view`
                           role="kbd"}                          role="kbd"}                         

  Switch                   `Num 5`{.interpreted-text            `Num 5`{.interpreted-text           `spatial_editor/switch_perspective_orthogonal`
  Perspective/Orthogonal   role="kbd"}                          role="kbd"}                         
  View                                                                                              

  Insert Animation Key     `K`{.interpreted-text role="kbd"}    `K`{.interpreted-text role="kbd"}   `spatial_editor/insert_anim_key`

  Focus Origin             `O`{.interpreted-text role="kbd"}    `O`{.interpreted-text role="kbd"}   `spatial_editor/focus_origin`

  Focus Selection          `F`{.interpreted-text role="kbd"}    `F`{.interpreted-text role="kbd"}   `spatial_editor/focus_selection`

  Align Transform with     `Ctrl + Alt + M`{.interpreted-text   `Opt + Cmd + M`{.interpreted-text   `spatial_editor/align_transform_with_view`
  View                     role="kbd"}                          role="kbd"}                         

  Align Rotation with View `Ctrl + Alt + F`{.interpreted-text   `Opt + Cmd + F`{.interpreted-text   `spatial_editor/align_rotation_with_view`
                           role="kbd"}                          role="kbd"}                         

  1 Viewport               `Ctrl + 1`{.interpreted-text         `Cmd + 1`{.interpreted-text         `spatial_editor/1_viewport`
                           role="kbd"}                          role="kbd"}                         

  2 Viewports              `Ctrl + 2`{.interpreted-text         `Cmd + 2`{.interpreted-text         `spatial_editor/2_viewports`
                           role="kbd"}                          role="kbd"}                         

  2 Viewports (Alt)        `Ctrl + Alt + 2`{.interpreted-text   `Opt + Cmd + 2`{.interpreted-text   `spatial_editor/2_viewports_alt`
                           role="kbd"}                          role="kbd"}                         

  3 Viewports              `Ctrl + 3`{.interpreted-text         `Cmd + 3`{.interpreted-text         `spatial_editor/3_viewports`
                           role="kbd"}                          role="kbd"}                         

  3 Viewports (Alt)        `Ctrl + Alt + 3`{.interpreted-text   `Opt + Cmd + 3`{.interpreted-text   `spatial_editor/3_viewports_alt`
                           role="kbd"}                          role="kbd"}                         

  4 Viewports              `Ctrl + 4`{.interpreted-text         `Cmd + 4`{.interpreted-text         `spatial_editor/4_viewports`
                           role="kbd"}                          role="kbd"}                         
  --------------------------------------------------------------------------------------------------------------------------------------------------

## Text editor {#doc_default_key_mapping_shortcuts_text_editor}

  ----------------------------------------------------------------------------------------------------------------------------------------------------------
  Action name   Windows, Linux                                macOS                                          Editor setting
  ------------- --------------------------------------------- ---------------------------------------------- -----------------------------------------------
  Cut           `Ctrl + X`{.interpreted-text role="kbd"}      `Cmd + X`{.interpreted-text role="kbd"}        `script_text_editor/cut`

  Copy          `Ctrl + C`{.interpreted-text role="kbd"}      `Cmd + C`{.interpreted-text role="kbd"}        `script_text_editor/copy`

  Paste         `Ctrl + V`{.interpreted-text role="kbd"}      `Cmd + V`{.interpreted-text role="kbd"}        `script_text_editor/paste`

  Select All    `Ctrl + A`{.interpreted-text role="kbd"}      `Cmd + A`{.interpreted-text role="kbd"}        `script_text_editor/select_all`

  Find          `Ctrl + F`{.interpreted-text role="kbd"}      `Cmd + F`{.interpreted-text role="kbd"}        `script_text_editor/find`

  Find Next     `F3`{.interpreted-text role="kbd"}            `Cmd + G`{.interpreted-text role="kbd"}        `script_text_editor/find_next`

  Find Previous `Shift + F3`{.interpreted-text role="kbd"}    `Cmd + Shift + G`{.interpreted-text            `script_text_editor/find_previous`
                                                              role="kbd"}                                    

  Find in Files `Ctrl + Shift + F`{.interpreted-text          `Cmd + Shift + F`{.interpreted-text            `script_text_editor/find_in_files`
                role="kbd"}                                   role="kbd"}                                    

  Replace       `Ctrl + R`{.interpreted-text role="kbd"}      `Opt + Cmd + F`{.interpreted-text role="kbd"}  `script_text_editor/replace`

  Replace in    `Ctrl + Shift + R`{.interpreted-text          `Cmd + Shift + R`{.interpreted-text            `script_text_editor/replace_in_files`
  Files         role="kbd"}                                   role="kbd"}                                    

  Undo          `Ctrl + Z`{.interpreted-text role="kbd"}      `Cmd + Z`{.interpreted-text role="kbd"}        `script_text_editor/undo`

  Redo          `Ctrl + Y`{.interpreted-text role="kbd"}      `Cmd + Y`{.interpreted-text role="kbd"}        `script_text_editor/redo`

  Move Up       `Alt + Up Arrow`{.interpreted-text            `Opt + Up Arrow`{.interpreted-text role="kbd"} `script_text_editor/move_up`
                role="kbd"}                                                                                  

  Move Down     `Alt + Down Arrow`{.interpreted-text          `Opt + Down Arrow`{.interpreted-text           `script_text_editor/move_down`
                role="kbd"}                                   role="kbd"}                                    

  Delete Line   `Ctrl + Shift + K`{.interpreted-text          `Cmd + Shift + K`{.interpreted-text            `script_text_editor/delete_line`
                role="kbd"}                                   role="kbd"}                                    

  Toggle        `Ctrl + K`{.interpreted-text role="kbd"}      `Cmd + K`{.interpreted-text role="kbd"}        `script_text_editor/toggle_comment`
  Comment                                                                                                    

  Fold/Unfold   `Alt + F`{.interpreted-text role="kbd"}       `Ctrl + Cmd + F`{.interpreted-text role="kbd"} `script_text_editor/toggle_fold_line`
  Line                                                                                                       

  Duplicate     `Ctrl + Alt + Down Arrow`{.interpreted-text   `Cmd + Shift + Down Arrow`{.interpreted-text   `script_text_editor/duplicate_lines`
  Lines         role="kbd"}                                   role="kbd"}                                    

  Duplicate     `Ctrl + Shift + D`{.interpreted-text          `Cmd + Shift + C`{.interpreted-text            `script_text_editor/duplicate_selection`
  Selection     role="kbd"}                                   role="kbd"}                                    

  Complete      `Ctrl + Space`{.interpreted-text role="kbd"}  `Ctrl + Space`{.interpreted-text role="kbd"}   `script_text_editor/complete_symbol`
  Symbol                                                                                                     

  Evaluate      `Ctrl + Shift + E`{.interpreted-text          `Cmd + Shift + E`{.interpreted-text            `script_text_editor/evaluate_selection`
  Selection     role="kbd"}                                   role="kbd"}                                    

  Trim Trailing `Ctrl + Alt + T`{.interpreted-text            `Opt + Cmd + T`{.interpreted-text role="kbd"}  `script_text_editor/trim_trailing_whitespace`
  Whitespace    role="kbd"}                                                                                  

  Uppercase     `Shift + F4`{.interpreted-text role="kbd"}    `Shift + F4`{.interpreted-text role="kbd"}     `script_text_editor/convert_to_uppercase`

  Lowercase     `Shift + F5`{.interpreted-text role="kbd"}    `Shift + F5`{.interpreted-text role="kbd"}     `script_text_editor/convert_to_lowercase`

  Capitalize    `Shift + F6`{.interpreted-text role="kbd"}    `Shift + F6`{.interpreted-text role="kbd"}     `script_text_editor/capitalize`

  Convert       `Ctrl + Shift + Y`{.interpreted-text          `Cmd + Shift + Y`{.interpreted-text            `script_text_editor/convert_indent_to_spaces`
  Indent to     role="kbd"}                                   role="kbd"}                                    
  Spaces                                                                                                     

  Convert       `Ctrl + Shift + I`{.interpreted-text          `Cmd + Shift + I`{.interpreted-text            `script_text_editor/convert_indent_to_tabs`
  Indent to     role="kbd"}                                   role="kbd"}                                    
  Tabs                                                                                                       

  Auto Indent   `Ctrl + I`{.interpreted-text role="kbd"}      `Cmd + I`{.interpreted-text role="kbd"}        `script_text_editor/auto_indent`

  Toggle        `Ctrl + Alt + B`{.interpreted-text            `Opt + Cmd + B`{.interpreted-text role="kbd"}  `script_text_editor/toggle_bookmark`
  Bookmark      role="kbd"}                                                                                  

  Go to Next    `Ctrl + B`{.interpreted-text role="kbd"}      `Cmd + B`{.interpreted-text role="kbd"}        `script_text_editor/goto_next_bookmark`
  Bookmark                                                                                                   

  Go to         `Ctrl + Shift + B`{.interpreted-text          `Cmd + Shift + B`{.interpreted-text            `script_text_editor/goto_previous_bookmark`
  Previous      role="kbd"}                                   role="kbd"}                                    
  Bookmark                                                                                                   

  Go to         `Ctrl + Alt + F`{.interpreted-text            `Ctrl + Cmd + J`{.interpreted-text role="kbd"} `script_text_editor/goto_function`
  Function      role="kbd"}                                                                                  

  Go to Line    `Ctrl + L`{.interpreted-text role="kbd"}      `Cmd + L`{.interpreted-text role="kbd"}        `script_text_editor/goto_line`

  Toggle        `F9`{.interpreted-text role="kbd"}            `Cmd + Shift + B`{.interpreted-text            `script_text_editor/toggle_breakpoint`
  Breakpoint                                                  role="kbd"}                                    

  Remove All    `Ctrl + Shift + F9`{.interpreted-text         `Cmd + Shift + F9`{.interpreted-text           `script_text_editor/remove_all_breakpoints`
  Breakpoints   role="kbd"}                                   role="kbd"}                                    

  Go to Next    `Ctrl + .`{.interpreted-text role="kbd"}      `Cmd + .`{.interpreted-text role="kbd"}        `script_text_editor/goto_next_breakpoint`
  Breakpoint                                                                                                 

  Go to         `Ctrl + ,`{.interpreted-text role="kbd"}      `Cmd + ,`{.interpreted-text role="kbd"}        `script_text_editor/goto_previous_breakpoint`
  Previous                                                                                                   
  Breakpoint                                                                                                 

  Contextual    `Alt + F1`{.interpreted-text role="kbd"}      `Opt + Shift + Space`{.interpreted-text        `script_text_editor/contextual_help`
  Help                                                        role="kbd"}                                    
  ----------------------------------------------------------------------------------------------------------------------------------------------------------

## Script editor

  -------------------------------------------------------------------------------------------------------------------------------------------------
  Action name  Windows, Linux                                 macOS                                          Editor setting
  ------------ ---------------------------------------------- ---------------------------------------------- --------------------------------------
  Find         `Ctrl + F`{.interpreted-text role="kbd"}       `Cmd + F`{.interpreted-text role="kbd"}        `script_editor/find`

  Find Next    `F3`{.interpreted-text role="kbd"}             `F3`{.interpreted-text role="kbd"}             `script_editor/find_next`

  Find         `Shift + F3`{.interpreted-text role="kbd"}     `Shift + F3`{.interpreted-text role="kbd"}     `script_editor/find_previous`
  Previous                                                                                                   

  Find in      `Ctrl + Shift + F`{.interpreted-text           `Cmd + Shift + F`{.interpreted-text            `script_editor/find_in_files`
  Files        role="kbd"}                                    role="kbd"}                                    

  Move Up      `Shift + Alt + Up Arrow`{.interpreted-text     `Shift + Opt + Up Arrow`{.interpreted-text     `script_editor/window_move_up`
               role="kbd"}                                    role="kbd"}                                    

  Move Down    `Shift + Alt + Down Arrow`{.interpreted-text   `Shift + Opt + Down Arrow`{.interpreted-text   `script_editor/window_move_down`
               role="kbd"}                                    role="kbd"}                                    

  Next Script  `Ctrl + Shift + .`{.interpreted-text           `Cmd + Shift + .`{.interpreted-text            `script_editor/next_script`
               role="kbd"}                                    role="kbd"}                                    

  Previous     `Ctrl + Shift + ,`{.interpreted-text           `Cmd + Shift + ,`{.interpreted-text            `script_editor/prev_script`
  Script       role="kbd"}                                    role="kbd"}                                    

  Reopen       `Ctrl + Shift + T`{.interpreted-text           `Cmd + Shift + T`{.interpreted-text            `script_editor/reopen_closed_script`
  Closed       role="kbd"}                                    role="kbd"}                                    
  Script                                                                                                     

  Save         `Ctrl + Alt + S`{.interpreted-text role="kbd"} `Opt + Cmd + S`{.interpreted-text role="kbd"}  `script_editor/save`

  Save All     `Ctrl + Shift + Alt + S`{.interpreted-text     `Cmd + Shift + Opt + S`{.interpreted-text      `script_editor/save_all`
               role="kbd"}                                    role="kbd"}                                    

  Soft Reload  `Ctrl + Shift + R`{.interpreted-text           `Cmd + Shift + R`{.interpreted-text            `script_editor/reload_script_soft`
  Script       role="kbd"}                                    role="kbd"}                                    

  History      `Alt + Left Arrow`{.interpreted-text           `Opt + Left Arrow`{.interpreted-text           `script_editor/history_previous`
  Previous     role="kbd"}                                    role="kbd"}                                    

  History Next `Alt + Right Arrow`{.interpreted-text          `Opt + Right Arrow`{.interpreted-text          `script_editor/history_next`
               role="kbd"}                                    role="kbd"}                                    

  Close        `Ctrl + W`{.interpreted-text role="kbd"}       `Cmd + W`{.interpreted-text role="kbd"}        `script_editor/close_file`

  Run          `Ctrl + Shift + X`{.interpreted-text           `Cmd + Shift + X`{.interpreted-text            `script_editor/run_file`
               role="kbd"}                                    role="kbd"}                                    

  Toggle       `Ctrl + \\`{.interpreted-text role="kbd"}      `Cmd + \\`{.interpreted-text role="kbd"}       `script_editor/toggle_scripts_panel`
  Scripts                                                                                                    
  Panel                                                                                                      

  Zoom In      `Ctrl + =`{.interpreted-text role="kbd"}       `Cmd + =`{.interpreted-text role="kbd"}        `script_editor/zoom_in`

  Zoom Out     `Ctrl + -`{.interpreted-text role="kbd"}       `Cmd + -`{.interpreted-text role="kbd"}        `script_editor/zoom_out`

  Reset Zoom   `Ctrl + 0`{.interpreted-text role="kbd"}       `Cmd + 0`{.interpreted-text role="kbd"}        `script_editor/reset_zoom`
  -------------------------------------------------------------------------------------------------------------------------------------------------

## Editor output

  -----------------------------------------------------------------------------------------------------------------
  Action name  Windows, Linux                         macOS                                 Editor setting
  ------------ -------------------------------------- ------------------------------------- -----------------------
  Copy         `Ctrl + C`{.interpreted-text           `Cmd + C`{.interpreted-text           `editor/copy_output`
  Selection    role="kbd"}                            role="kbd"}                           

  Clear Output `Ctrl + Shift + K`{.interpreted-text   `Cmd + Shift + K`{.interpreted-text   `editor/clear_output`
               role="kbd"}                            role="kbd"}                           
  -----------------------------------------------------------------------------------------------------------------

## Debugger

  ------------------------------------------------------------------------------------------
  Action name   Windows, Linux            macOS                     Editor setting
  ------------- ------------------------- ------------------------- ------------------------
  Step Into     `F11`{.interpreted-text   `F11`{.interpreted-text   `debugger/step_into`
                role="kbd"}               role="kbd"}               

  Step Over     `F10`{.interpreted-text   `F10`{.interpreted-text   `debugger/step_over`
                role="kbd"}               role="kbd"}               

  Continue      `F12`{.interpreted-text   `F12`{.interpreted-text   `debugger/continue`
                role="kbd"}               role="kbd"}               
  ------------------------------------------------------------------------------------------

## File dialog

  ---------------------------------------------------------------------------------------------------------------------------------
  Action name   Windows, Linux                          macOS                                   Editor setting
  ------------- --------------------------------------- --------------------------------------- -----------------------------------
  Go Back       `Alt + Left Arrow`{.interpreted-text    `Opt + Left Arrow`{.interpreted-text    `file_dialog/go_back`
                role="kbd"}                             role="kbd"}                             

  Go Forward    `Alt + Right Arrow`{.interpreted-text   `Opt + Right Arrow`{.interpreted-text   `file_dialog/go_forward`
                role="kbd"}                             role="kbd"}                             

  Go Up         `Alt + Up Arrow`{.interpreted-text      `Opt + Up Arrow`{.interpreted-text      `file_dialog/go_up`
                role="kbd"}                             role="kbd"}                             

  Refresh       `F5`{.interpreted-text role="kbd"}      `F5`{.interpreted-text role="kbd"}      `file_dialog/refresh`

  Toggle Hidden `Ctrl + H`{.interpreted-text            `Cmd + H`{.interpreted-text role="kbd"} `file_dialog/toggle_hidden_files`
  Files         role="kbd"}                                                                     

  Toggle        `Alt + F`{.interpreted-text role="kbd"} `Opt + F`{.interpreted-text role="kbd"} `file_dialog/toggle_favorite`
  Favorite                                                                                      

  Toggle Mode   `Alt + V`{.interpreted-text role="kbd"} `Opt + V`{.interpreted-text role="kbd"} `file_dialog/toggle_mode`

  Create Folder `Ctrl + N`{.interpreted-text            `Cmd + N`{.interpreted-text role="kbd"} `file_dialog/create_folder`
                role="kbd"}                                                                     

  Delete        `Del`{.interpreted-text role="kbd"}     `Cmd + BkSp`{.interpreted-text          `file_dialog/delete`
                                                        role="kbd"}                             

  Focus Path    `Ctrl + L`{.interpreted-text            `Cmd + Shift + G`{.interpreted-text     `file_dialog/focus_path`
                role="kbd"}                             role="kbd"}                             

  Move Favorite `Ctrl + Up Arrow`{.interpreted-text     `Cmd + Up Arrow`{.interpreted-text      `file_dialog/move_favorite_up`
  Up            role="kbd"}                             role="kbd"}                             

  Move Favorite `Ctrl + Down Arrow`{.interpreted-text   `Cmd + Down Arrow`{.interpreted-text    `file_dialog/move_favorite_down`
  Down          role="kbd"}                             role="kbd"}                             
  ---------------------------------------------------------------------------------------------------------------------------------

## FileSystem dock

  ---------------------------------------------------------------------------------------------------------
  Action name Windows, Linux                 macOS                            Editor setting
  ----------- ------------------------------ -------------------------------- -----------------------------
  Copy Path   `Ctrl + C`{.interpreted-text   `Cmd + C`{.interpreted-text      `filesystem_dock/copy_path`
              role="kbd"}                    role="kbd"}                      

  Duplicate   `Ctrl + D`{.interpreted-text   `Cmd + D`{.interpreted-text      `filesystem_dock/duplicate`
              role="kbd"}                    role="kbd"}                      

  Delete      `Del`{.interpreted-text        `Cmd + BkSp`{.interpreted-text   `filesystem_dock/delete`
              role="kbd"}                    role="kbd"}                      
  ---------------------------------------------------------------------------------------------------------

## Scene tree dock

  ---------------------------------------------------------------------------------------------------------------------------
  Action name Windows, Linux                          macOS                                  Editor setting
  ----------- --------------------------------------- -------------------------------------- --------------------------------
  Add Child   `Ctrl + A`{.interpreted-text            `Cmd + A`{.interpreted-text            `scene_tree/add_child_node`
  Node        role="kbd"}                             role="kbd"}                            

  Batch       `Ctrl + F2`{.interpreted-text           `Cmd + F2`{.interpreted-text           `scene_tree/batch_rename`
  Rename      role="kbd"}                             role="kbd"}                            

  Copy Node   `Ctrl + Shift + C`{.interpreted-text    `Cmd + Shift +  C`{.interpreted-text   `scene_tree/copy_node_path`
  Path        role="kbd"}                             role="kbd"}                            

  Delete      `Del`{.interpreted-text role="kbd"}     `Cmd + BkSp`{.interpreted-text         `scene_tree/delete`
                                                      role="kbd"}                            

  Force       `Shift + Del`{.interpreted-text         `Shift + Del`{.interpreted-text        `scene_tree/delete_no_confirm`
  Delete      role="kbd"}                             role="kbd"}                            

  Duplicate   `Ctrl + D`{.interpreted-text            `Cmd + D`{.interpreted-text            `scene_tree/duplicate`
              role="kbd"}                             role="kbd"}                            

  Move Up     `Ctrl + Up Arrow`{.interpreted-text     `Cmd + Up Arrow`{.interpreted-text     `scene_tree/move_up`
              role="kbd"}                             role="kbd"}                            

  Move Down   `Ctrl + Down Arrow`{.interpreted-text   `Cmd + Down Arrow`{.interpreted-text   `scene_tree/move_down`
              role="kbd"}                             role="kbd"}                            
  ---------------------------------------------------------------------------------------------------------------------------

## Animation track editor

  -------------------------------------------------------------------------------------------------------------------------------------------------
  Action name  Windows, Linux                           macOS                                   Editor setting
  ------------ ---------------------------------------- --------------------------------------- ---------------------------------------------------
  Duplicate    `Ctrl + D`{.interpreted-text role="kbd"} `Cmd + D`{.interpreted-text role="kbd"} `animation_editor/duplicate_selection`
  Selection                                                                                     

  Duplicate    `Ctrl + Shift + D`{.interpreted-text     `Cmd + Shift + D`{.interpreted-text     `animation_editor/duplicate_selection_transposed`
  Transposed   role="kbd"}                              role="kbd"}                             

  Delete       `Del`{.interpreted-text role="kbd"}      `Cmd + BkSp`{.interpreted-text          `animation_editor/delete_selection`
  Selection                                             role="kbd"}                             

  Go to Next   `Ctrl + Right Arrow`{.interpreted-text   `Cmd + Right Arrow`{.interpreted-text   `animation_editor/goto_next_step`
  Step         role="kbd"}                              role="kbd"}                             

  Go to        `Ctrl + Left Arrow`{.interpreted-text    `Cmd + Left Arrow`{.interpreted-text    `animation_editor/goto_prev_step`
  Previous     role="kbd"}                              role="kbd"}                             
  Step                                                                                          
  -------------------------------------------------------------------------------------------------------------------------------------------------

## TileMap editor

  --------------------------------------------------------------------------------------------------------------------
  Action name    Windows, Linux                 macOS                            Editor setting
  -------------- ------------------------------ -------------------------------- -------------------------------------
  Select         `S`{.interpreted-text          `S`{.interpreted-text            `tiles_editor/selection_tool`
                 role="kbd"}                    role="kbd"}                      

  Cut Selection  `Ctrl + X`{.interpreted-text   `Cmd + X`{.interpreted-text      `tiles_editor/cut`
                 role="kbd"}                    role="kbd"}                      

  Copy Selection `Ctrl + C`{.interpreted-text   `Cmd + C`{.interpreted-text      `tiles_editor/copy`
                 role="kbd"}                    role="kbd"}                      

  Paste          `Ctrl + V`{.interpreted-text   `Cmd + V`{.interpreted-text      `tiles_editor/paste`
  Selection      role="kbd"}                    role="kbd"}                      

  Delete         `Del`{.interpreted-text        `Cmd + BkSp`{.interpreted-text   `tiles_editor/delete`
  Selection      role="kbd"}                    role="kbd"}                      

  Cancel         `Esc`{.interpreted-text        `Esc`{.interpreted-text          `tiles_editor/cancel`
                 role="kbd"}                    role="kbd"}                      

  Paint          `D`{.interpreted-text          `D`{.interpreted-text            `tiles_editor/paint_tool`
                 role="kbd"}                    role="kbd"}                      

  Line           `L`{.interpreted-text          `L`{.interpreted-text            `tiles_editor/line_tool`
                 role="kbd"}                    role="kbd"}                      

  Rect           `R`{.interpreted-text          `R`{.interpreted-text            `tiles_editor/rect_tool`
                 role="kbd"}                    role="kbd"}                      

  Bucket         `B`{.interpreted-text          `B`{.interpreted-text            `tiles_editor/bucket_tool`
                 role="kbd"}                    role="kbd"}                      

  Picker         `P`{.interpreted-text          `P`{.interpreted-text            `tiles_editor/picker`
                 role="kbd"}                    role="kbd"}                      

  Eraser         `E`{.interpreted-text          `E`{.interpreted-text            `tiles_editor/eraser`
                 role="kbd"}                    role="kbd"}                      

  Flip           `C`{.interpreted-text          `C`{.interpreted-text            `tiles_editor/flip_tile_horizontal`
  Horizontally   role="kbd"}                    role="kbd"}                      

  Flip           `V`{.interpreted-text          `V`{.interpreted-text            `tiles_editor/flip_tile_vertical`
  Vertically     role="kbd"}                    role="kbd"}                      

  Rotate Left    `Z`{.interpreted-text          `Z`{.interpreted-text            `tiles_editor/rotate_tile_left`
                 role="kbd"}                    role="kbd"}                      

  Rotate Right   `X`{.interpreted-text          `X`{.interpreted-text            `tiles_editor/rotate_tile_right`
                 role="kbd"}                    role="kbd"}                      
  --------------------------------------------------------------------------------------------------------------------

## TileSet Editor

  ----------------------------------------------------------------------------------------------------------------
  Action name     Windows, Linux               macOS                        Editor setting
  --------------- ---------------------------- ---------------------------- --------------------------------------
  Next Coordinate `PgDown`{.interpreted-text   `PgDown`{.interpreted-text   `tileset_editor/next_shape`
                  role="kbd"}                  role="kbd"}                  

  Previous        `PgUp`{.interpreted-text     `PgUp`{.interpreted-text     `tileset_editor/previous_shape`
  Coordinate      role="kbd"}                  role="kbd"}                  

  Region Mode     `1`{.interpreted-text        `1`{.interpreted-text        `tileset_editor/editmode_region`
                  role="kbd"}                  role="kbd"}                  

  Collision Mode  `2`{.interpreted-text        `2`{.interpreted-text        `tileset_editor/editmode_collision`
                  role="kbd"}                  role="kbd"}                  

  Occlusion Mode  `3`{.interpreted-text        `3`{.interpreted-text        `tileset_editor/editmode_occlusion`
                  role="kbd"}                  role="kbd"}                  

  Navigation Mode `4`{.interpreted-text        `4`{.interpreted-text        `tileset_editor/editmode_navigation`
                  role="kbd"}                  role="kbd"}                  

  Bitmask Mode    `5`{.interpreted-text        `5`{.interpreted-text        `tileset_editor/editmode_bitmask`
                  role="kbd"}                  role="kbd"}                  

  Priority Mode   `6`{.interpreted-text        `6`{.interpreted-text        `tileset_editor/editmode_priority`
                  role="kbd"}                  role="kbd"}                  

  Icon Mode       `7`{.interpreted-text        `7`{.interpreted-text        `tileset_editor/editmode_icon`
                  role="kbd"}                  role="kbd"}                  

  Z Index Mode    `8`{.interpreted-text        `8`{.interpreted-text        `tileset_editor/editmode_z_index`
                  role="kbd"}                  role="kbd"}                  
  ----------------------------------------------------------------------------------------------------------------

## Project manager

  ------------------------------------------------------------------------------------------------------------------
  Action name     Windows, Linux                 macOS                            Editor setting
  --------------- ------------------------------ -------------------------------- ----------------------------------
  New Project     `Ctrl + N`{.interpreted-text   `Cmd + N`{.interpreted-text      `project_manager/new_project`
                  role="kbd"}                    role="kbd"}                      

  Import Project  `Ctrl + I`{.interpreted-text   `Cmd + I`{.interpreted-text      `project_manager/import_project`
                  role="kbd"}                    role="kbd"}                      

  Scan for        `Ctrl + S`{.interpreted-text   `Cmd + S`{.interpreted-text      `project_manager/scan_projects`
  Projects        role="kbd"}                    role="kbd"}                      

  Edit Project    `Ctrl + E`{.interpreted-text   `Cmd + E`{.interpreted-text      `project_manager/edit_project`
                  role="kbd"}                    role="kbd"}                      

  Run Project     `Ctrl + R`{.interpreted-text   `Cmd + R`{.interpreted-text      `project_manager/run_project`
                  role="kbd"}                    role="kbd"}                      

  Rename Project  `F2`{.interpreted-text         `Enter`{.interpreted-text        `project_manager/rename_project`
                  role="kbd"}                    role="kbd"}                      

  Remove Project  `Delete`{.interpreted-text     `Cmd + BkSp`{.interpreted-text   `project_manager/remove_project`
                  role="kbd"}                    role="kbd"}                      
  ------------------------------------------------------------------------------------------------------------------
