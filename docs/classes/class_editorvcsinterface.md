github_url
:   hide

# EditorVCSInterface {#class_EditorVCSInterface}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Version Control System (VCS) interface, which reads and writes to the
local VCS in use.

::: rst-class
classref-introduction-group
:::

## Description

Defines the API that the editor uses to extract information from the
underlying VCS. The implementation of this API is included in VCS
plugins, which are GDExtension plugins that inherit
**EditorVCSInterface** and are attached (on demand) to the singleton
instance of **EditorVCSInterface**. Instead of performing the task
themselves, all the virtual functions listed below are calling the
internally overridden functions in the VCS plugins to provide a
plug-n-play experience. A custom VCS plugin is supposed to inherit from
**EditorVCSInterface** and override each of these virtual functions.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Version control systems <../tutorials/best_practices/version_control_systems>`{.interpreted-text
  role="doc"}

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

## Enumerations

:::: {#enum_EditorVCSInterface_ChangeType}
::: rst-class
classref-enumeration
:::
::::

enum **ChangeType**:
`🔗<enum_EditorVCSInterface_ChangeType>`{.interpreted-text role="ref"}

:::: {#class_EditorVCSInterface_constant_CHANGE_TYPE_NEW}
::: rst-class
classref-enumeration-constant
:::
::::

`ChangeType<enum_EditorVCSInterface_ChangeType>`{.interpreted-text
role="ref"} **CHANGE_TYPE_NEW** = `0`

A new file has been added.

:::: {#class_EditorVCSInterface_constant_CHANGE_TYPE_MODIFIED}
::: rst-class
classref-enumeration-constant
:::
::::

`ChangeType<enum_EditorVCSInterface_ChangeType>`{.interpreted-text
role="ref"} **CHANGE_TYPE_MODIFIED** = `1`

An earlier added file has been modified.

:::: {#class_EditorVCSInterface_constant_CHANGE_TYPE_RENAMED}
::: rst-class
classref-enumeration-constant
:::
::::

`ChangeType<enum_EditorVCSInterface_ChangeType>`{.interpreted-text
role="ref"} **CHANGE_TYPE_RENAMED** = `2`

An earlier added file has been renamed.

:::: {#class_EditorVCSInterface_constant_CHANGE_TYPE_DELETED}
::: rst-class
classref-enumeration-constant
:::
::::

`ChangeType<enum_EditorVCSInterface_ChangeType>`{.interpreted-text
role="ref"} **CHANGE_TYPE_DELETED** = `3`

An earlier added file has been deleted.

:::: {#class_EditorVCSInterface_constant_CHANGE_TYPE_TYPECHANGE}
::: rst-class
classref-enumeration-constant
:::
::::

`ChangeType<enum_EditorVCSInterface_ChangeType>`{.interpreted-text
role="ref"} **CHANGE_TYPE_TYPECHANGE** = `4`

An earlier added file has been typechanged.

:::: {#class_EditorVCSInterface_constant_CHANGE_TYPE_UNMERGED}
::: rst-class
classref-enumeration-constant
:::
::::

`ChangeType<enum_EditorVCSInterface_ChangeType>`{.interpreted-text
role="ref"} **CHANGE_TYPE_UNMERGED** = `5`

A file is left unmerged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_EditorVCSInterface_TreeArea}
::: rst-class
classref-enumeration
:::
::::

enum **TreeArea**:
`🔗<enum_EditorVCSInterface_TreeArea>`{.interpreted-text role="ref"}

:::: {#class_EditorVCSInterface_constant_TREE_AREA_COMMIT}
::: rst-class
classref-enumeration-constant
:::
::::

`TreeArea<enum_EditorVCSInterface_TreeArea>`{.interpreted-text
role="ref"} **TREE_AREA_COMMIT** = `0`

A commit is encountered from the commit area.

:::: {#class_EditorVCSInterface_constant_TREE_AREA_STAGED}
::: rst-class
classref-enumeration-constant
:::
::::

`TreeArea<enum_EditorVCSInterface_TreeArea>`{.interpreted-text
role="ref"} **TREE_AREA_STAGED** = `1`

A file is encountered from the staged area.

:::: {#class_EditorVCSInterface_constant_TREE_AREA_UNSTAGED}
::: rst-class
classref-enumeration-constant
:::
::::

`TreeArea<enum_EditorVCSInterface_TreeArea>`{.interpreted-text
role="ref"} **TREE_AREA_UNSTAGED** = `2`

A file is encountered from the unstaged area.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorVCSInterface_private_method__checkout_branch}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_checkout_branch**(branch_name:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__checkout_branch>`{.interpreted-text
role="ref"}

Checks out a `branch_name` in the VCS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__commit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_commit**(msg: `String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__commit>`{.interpreted-text
role="ref"}

Commits the currently staged changes and applies the commit `msg` to the
resulting commit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__create_branch}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_create_branch**(branch_name:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__create_branch>`{.interpreted-text
role="ref"}

Creates a new branch named `branch_name` in the VCS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__create_remote}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_create_remote**(remote_name:
`String<class_String>`{.interpreted-text role="ref"}, remote_url:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__create_remote>`{.interpreted-text
role="ref"}

Creates a new remote destination with name `remote_name` and points it
to `remote_url`. This can be an HTTPS remote or an SSH remote.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__discard_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_discard_file**(file_path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__discard_file>`{.interpreted-text
role="ref"}

Discards the changes made in a file present at `file_path`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__fetch}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_fetch**(remote: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__fetch>`{.interpreted-text
role="ref"}

Fetches new changes from the `remote`, but doesn\'t write changes to the
current working directory. Equivalent to `git fetch`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__get_branch_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
**\_get_branch_list**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__get_branch_list>`{.interpreted-text
role="ref"}

Gets an instance of an `Array<class_Array>`{.interpreted-text
role="ref"} of `String<class_String>`{.interpreted-text role="ref"}s
containing available branch names in the VCS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__get_current_branch_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_current_branch_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__get_current_branch_name>`{.interpreted-text
role="ref"}

Gets the current branch name defined in the VCS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__get_diff}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_get_diff**(identifier:
`String<class_String>`{.interpreted-text role="ref"}, area:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__get_diff>`{.interpreted-text
role="ref"}

Returns an array of `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} items (see
`create_diff_file()<class_EditorVCSInterface_method_create_diff_file>`{.interpreted-text
role="ref"},
`create_diff_hunk()<class_EditorVCSInterface_method_create_diff_hunk>`{.interpreted-text
role="ref"},
`create_diff_line()<class_EditorVCSInterface_method_create_diff_line>`{.interpreted-text
role="ref"},
`add_line_diffs_into_diff_hunk()<class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk>`{.interpreted-text
role="ref"} and
`add_diff_hunks_into_diff_file()<class_EditorVCSInterface_method_add_diff_hunks_into_diff_file>`{.interpreted-text
role="ref"}), each containing information about a diff. If `identifier`
is a file path, returns a file diff, and if it is a commit identifier,
then returns a commit diff.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__get_line_diff}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_get_line_diff**(file_path:
`String<class_String>`{.interpreted-text role="ref"}, text:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__get_line_diff>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} items (see
`create_diff_hunk()<class_EditorVCSInterface_method_create_diff_hunk>`{.interpreted-text
role="ref"}), each containing a line diff between a file at `file_path`
and the `text` which is passed in.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__get_modified_files_data}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_get_modified_files_data**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__get_modified_files_data>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} items (see
`create_status_file()<class_EditorVCSInterface_method_create_status_file>`{.interpreted-text
role="ref"}), each containing the status data of every modified file in
the project folder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__get_previous_commits}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_get_previous_commits**(max_commits:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__get_previous_commits>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} items (see
`create_commit()<class_EditorVCSInterface_method_create_commit>`{.interpreted-text
role="ref"}), each containing the data for a past commit.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__get_remotes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
**\_get_remotes**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__get_remotes>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`String<class_String>`{.interpreted-text role="ref"}s, each containing
the name of a remote configured in the VCS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__get_vcs_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_vcs_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__get_vcs_name>`{.interpreted-text
role="ref"}

Returns the name of the underlying VCS provider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__initialize}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_initialize**(project_path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__initialize>`{.interpreted-text
role="ref"}

Initializes the VCS plugin when called from the editor. Returns whether
or not the plugin was successfully initialized. A VCS project is
initialized at `project_path`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__pull}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_pull**(remote: `String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__pull>`{.interpreted-text
role="ref"}

Pulls changes from the remote. This can give rise to merge conflicts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__push}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_push**(remote: `String<class_String>`{.interpreted-text role="ref"},
force: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__push>`{.interpreted-text
role="ref"}

Pushes changes to the `remote`. If `force` is `true`, a force push will
override the change history already present on the remote.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__remove_branch}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_remove_branch**(branch_name:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__remove_branch>`{.interpreted-text
role="ref"}

Remove a branch from the local VCS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__remove_remote}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_remove_remote**(remote_name:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__remove_remote>`{.interpreted-text
role="ref"}

Remove a remote from the local VCS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__set_credentials}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_credentials**(username: `String<class_String>`{.interpreted-text
role="ref"}, password: `String<class_String>`{.interpreted-text
role="ref"}, ssh_public_key_path:
`String<class_String>`{.interpreted-text role="ref"},
ssh_private_key_path: `String<class_String>`{.interpreted-text
role="ref"}, ssh_passphrase: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__set_credentials>`{.interpreted-text
role="ref"}

Set user credentials in the underlying VCS. `username` and `password`
are used only during HTTPS authentication unless not already mentioned
in the remote URL. `ssh_public_key_path`, `ssh_private_key_path`, and
`ssh_passphrase` are only used during SSH authentication.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__shut_down}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_shut_down**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__shut_down>`{.interpreted-text
role="ref"}

Shuts down VCS plugin instance. Called when the user either closes the
editor or shuts down the VCS plugin through the editor UI.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__stage_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_stage_file**(file_path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__stage_file>`{.interpreted-text
role="ref"}

Stages the file present at `file_path` to the staged area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_private_method__unstage_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_unstage_file**(file_path: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorVCSInterface_private_method__unstage_file>`{.interpreted-text
role="ref"}

Unstages the file present at `file_path` from the staged area to the
unstaged area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_method_add_diff_hunks_into_diff_file}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**add_diff_hunks_into_diff_file**(diff_file:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"},
diff_hunks: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\])
`🔗<class_EditorVCSInterface_method_add_diff_hunks_into_diff_file>`{.interpreted-text
role="ref"}

Helper function to add an array of `diff_hunks` into a `diff_file`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**add_line_diffs_into_diff_hunk**(diff_hunk:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"},
line_diffs: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\])
`🔗<class_EditorVCSInterface_method_add_line_diffs_into_diff_hunk>`{.interpreted-text
role="ref"}

Helper function to add an array of `line_diffs` into a `diff_hunk`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_method_create_commit}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**create_commit**(msg: `String<class_String>`{.interpreted-text
role="ref"}, author: `String<class_String>`{.interpreted-text
role="ref"}, id: `String<class_String>`{.interpreted-text role="ref"},
unix_timestamp: `int<class_int>`{.interpreted-text role="ref"},
offset_minutes: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_EditorVCSInterface_method_create_commit>`{.interpreted-text
role="ref"}

Helper function to create a commit
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} item. `msg`
is the commit message of the commit. `author` is a single human-readable
string containing all the author\'s details, e.g. the email and name
configured in the VCS. `id` is the identifier of the commit, in
whichever format your VCS may provide an identifier to commits.
`unix_timestamp` is the UTC Unix timestamp of when the commit was
created. `offset_minutes` is the timezone offset in minutes, recorded
from the system timezone where the commit was created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_method_create_diff_file}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**create_diff_file**(new_file: `String<class_String>`{.interpreted-text
role="ref"}, old_file: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorVCSInterface_method_create_diff_file>`{.interpreted-text
role="ref"}

Helper function to create a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} for storing
old and new diff file paths.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_method_create_diff_hunk}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**create_diff_hunk**(old_start: `int<class_int>`{.interpreted-text
role="ref"}, new_start: `int<class_int>`{.interpreted-text role="ref"},
old_lines: `int<class_int>`{.interpreted-text role="ref"}, new_lines:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_EditorVCSInterface_method_create_diff_hunk>`{.interpreted-text
role="ref"}

Helper function to create a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} for storing
diff hunk data. `old_start` is the starting line number in old file.
`new_start` is the starting line number in new file. `old_lines` is the
number of lines in the old file. `new_lines` is the number of lines in
the new file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_method_create_diff_line}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**create_diff_line**(new_line_no: `int<class_int>`{.interpreted-text
role="ref"}, old_line_no: `int<class_int>`{.interpreted-text
role="ref"}, content: `String<class_String>`{.interpreted-text
role="ref"}, status: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorVCSInterface_method_create_diff_line>`{.interpreted-text
role="ref"}

Helper function to create a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} for storing
a line diff. `new_line_no` is the line number in the new file (can be
`-1` if the line is deleted). `old_line_no` is the line number in the
old file (can be `-1` if the line is added). `content` is the diff text.
`status` is a single character string which stores the line origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_method_create_status_file}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**create_status_file**(file_path:
`String<class_String>`{.interpreted-text role="ref"}, change_type:
`ChangeType<enum_EditorVCSInterface_ChangeType>`{.interpreted-text
role="ref"}, area:
`TreeArea<enum_EditorVCSInterface_TreeArea>`{.interpreted-text
role="ref"})
`🔗<class_EditorVCSInterface_method_create_status_file>`{.interpreted-text
role="ref"}

Helper function to create a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} used by
editor to read the status of a file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorVCSInterface_method_popup_error}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_error**(msg: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorVCSInterface_method_popup_error>`{.interpreted-text
role="ref"}

Pops up an error message in the editor which is shown as coming from the
underlying VCS. Use this to show VCS specific error messages.
