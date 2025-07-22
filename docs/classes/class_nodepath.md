github_url
:   hide

# NodePath {#class_NodePath}

A pre-parsed scene tree path.

::: rst-class
classref-introduction-group
:::

## Description

The **NodePath** built-in `Variant<class_Variant>`{.interpreted-text
role="ref"} type represents a path to a node or property in a hierarchy
of nodes. It is designed to be efficiently passed into many built-in
methods (such as
`Node.get_node()<class_Node_method_get_node>`{.interpreted-text
role="ref"},
`Object.set_indexed()<class_Object_method_set_indexed>`{.interpreted-text
role="ref"},
`Tween.tween_property()<class_Tween_method_tween_property>`{.interpreted-text
role="ref"}, etc.) without a hard dependence on the node or property
they point to.

A node path is represented as a `String<class_String>`{.interpreted-text
role="ref"} composed of slash-separated (`/`) node names and
colon-separated (`:`) property names (also called \"subnames\"). Similar
to a filesystem path, `".."` and `"."` are special node names. They
refer to the parent node and the current node, respectively.

The following examples are paths relative to the current node:

    ^"A"     # Points to the direct child A.
    ^"A/B"   # Points to A's child B.
    ^"."     # Points to the current node.
    ^".."    # Points to the parent node.
    ^"../C"  # Points to the sibling node C.
    ^"../.." # Points to the grandparent node.

A leading slash means the path is absolute, and begins from the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}:

    ^"/root"            # Points to the SceneTree's root Window.
    ^"/root/Title"      # May point to the main scene's root node named "Title".
    ^"/root/Global"     # May point to an autoloaded node or scene named "Global".

Despite their name, node paths may also point to a property:

    ^":position"           # Points to this object's position.
    ^":position:x"         # Points to this object's position in the x axis.
    ^"Camera3D:rotation:y" # Points to the child Camera3D and its y rotation.
    ^"/root:size:x"        # Points to the root Window and its width.

In some situations, it\'s possible to omit the leading `:` when pointing
to an object\'s property. As an example, this is the case with
`Object.set_indexed()<class_Object_method_set_indexed>`{.interpreted-text
role="ref"} and
`Tween.tween_property()<class_Tween_method_tween_property>`{.interpreted-text
role="ref"}, as those methods call
`get_as_property_path()<class_NodePath_method_get_as_property_path>`{.interpreted-text
role="ref"} under the hood. However, it\'s generally recommended to keep
the `:` prefix.

Node paths cannot check whether they are valid and may point to nodes or
properties that do not exist. Their meaning depends entirely on the
context in which they\'re used.

You usually do not have to worry about the **NodePath** type, as strings
are automatically converted to the type when necessary. There are still
times when defining node paths is useful. For example, exported
**NodePath** properties allow you to easily select any node within the
currently edited scene. They are also automatically updated when moving,
renaming or deleting nodes in the scene tree editor. See also
`@GDScript.@export_node_path<class_@GDScript_annotation_@export_node_path>`{.interpreted-text
role="ref"}.

See also `StringName<class_StringName>`{.interpreted-text role="ref"},
which is a similar type designed for optimized strings.

\*\*Note:\*\* In a boolean context, a **NodePath** will evaluate to
`false` if it is empty (`NodePath("")`). Otherwise, a **NodePath** will
always evaluate to `true`.

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- [2D Role Playing Game (RPG)
  Demo](https://godotengine.org/asset-library/asset/2729)

::: rst-class
classref-reftable-group
:::

## Constructors

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Operators

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_NodePath_constructor_NodePath}
::: rst-class
classref-constructor
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **NodePath**()
`🔗<class_NodePath_constructor_NodePath>`{.interpreted-text role="ref"}

Constructs an empty **NodePath**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**NodePath**(from: `NodePath<class_NodePath>`{.interpreted-text
role="ref"})

Constructs a **NodePath** as a copy of the given **NodePath**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**NodePath**(from: `String<class_String>`{.interpreted-text role="ref"})

Constructs a **NodePath** from a
`String<class_String>`{.interpreted-text role="ref"}. The created path
is absolute if prefixed with a slash (see
`is_absolute()<class_NodePath_method_is_absolute>`{.interpreted-text
role="ref"}).

The \"subnames\" optionally included after the path to the target node
can point to properties, and can also be nested.

The following strings can be valid node paths:

    # Points to the Sprite2D node.
    "Level/RigidBody2D/Sprite2D"

    # Points to the Sprite2D node and its "texture" resource.
    # get_node() would retrieve the Sprite2D, while get_node_and_resource()
    # would retrieve both the Sprite2D node and the "texture" resource.
    "Level/RigidBody2D/Sprite2D:texture"

    # Points to the Sprite2D node and its "position" property.
    "Level/RigidBody2D/Sprite2D:position"

    # Points to the Sprite2D node and the "x" component of its "position" property.
    "Level/RigidBody2D/Sprite2D:position:x"

    # Points to the RigidBody2D node as an absolute path beginning from the SceneTree.
    "/root/Level/RigidBody2D"

\*\*Note:\*\* In GDScript, it\'s also possible to convert a constant
string into a node path by prefixing it with `^`. `^"path/to/node"` is
equivalent to `NodePath("path/to/node")`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NodePath_method_get_as_property_path}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_as_property_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NodePath_method_get_as_property_path>`{.interpreted-text
role="ref"}

Returns a copy of this node path with a colon character (`:`) prefixed,
transforming it to a pure property path with no node names (relative to
the current node).

::::: tabs
::: code-tab
gdscript

\# node_path points to the \"x\" property of the child node named
\"position\". var node_path = \^\"position:x\"

\# property_path points to the \"position\" in the \"x\" axis of this
node. var property_path = node_path.get_as_property_path()
print(property_path) \# Prints \":position:x\"
:::

::: code-tab
csharp

// nodePath points to the \"x\" property of the child node named
\"position\". var nodePath = new NodePath(\"position:x\");

// propertyPath points to the \"position\" in the \"x\" axis of this
node. NodePath propertyPath = nodePath.GetAsPropertyPath();
GD.Print(propertyPath); // Prints \":position:x\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_get_concatenated_names}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_concatenated_names**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NodePath_method_get_concatenated_names>`{.interpreted-text
role="ref"}

Returns all node names concatenated with a slash character (`/`) as a
single `StringName<class_StringName>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_get_concatenated_subnames}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_concatenated_subnames**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NodePath_method_get_concatenated_subnames>`{.interpreted-text
role="ref"}

Returns all property subnames concatenated with a colon character (`:`)
as a single `StringName<class_StringName>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var node_path = \^\"Sprite2D:texture:resource_name\"
print(node_path.get_concatenated_subnames()) \# Prints
\"texture:resource_name\"
:::

::: code-tab
csharp

var nodePath = new NodePath(\"Sprite2D:texture:resource_name\");
GD.Print(nodePath.GetConcatenatedSubnames()); // Prints
\"texture:resource_name\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_get_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_name**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NodePath_method_get_name>`{.interpreted-text
role="ref"}

Returns the node name indicated by `idx`, starting from 0. If `idx` is
out of bounds, an error is generated. See also
`get_subname_count()<class_NodePath_method_get_subname_count>`{.interpreted-text
role="ref"} and
`get_name_count()<class_NodePath_method_get_name_count>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var sprite_path = NodePath(\"../RigidBody2D/Sprite2D\")
print(sprite_path.get_name(0)) \# Prints \"..\"
print(sprite_path.get_name(1)) \# Prints \"RigidBody2D\"
print(sprite_path.get_name(2)) \# Prints \"Sprite\"
:::

::: code-tab
csharp

var spritePath = new NodePath(\"../RigidBody2D/Sprite2D\");
GD.Print(spritePath.GetName(0)); // Prints \"..\"
GD.Print(spritePath.GetName(1)); // Prints \"PathFollow2D\"
GD.Print(spritePath.GetName(2)); // Prints \"Sprite\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_get_name_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_name_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NodePath_method_get_name_count>`{.interpreted-text role="ref"}

Returns the number of node names in the path. Property subnames are not
included.

For example, `"../RigidBody2D/Sprite2D:texture"` contains 3 node names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_get_subname}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_subname**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NodePath_method_get_subname>`{.interpreted-text
role="ref"}

Returns the property name indicated by `idx`, starting from 0. If `idx`
is out of bounds, an error is generated. See also
`get_subname_count()<class_NodePath_method_get_subname_count>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var path_to_name = NodePath(\"Sprite2D:texture:resource_name\")
print(path_to_name.get_subname(0)) \# Prints \"texture\"
print(path_to_name.get_subname(1)) \# Prints \"resource_name\"
:::

::: code-tab
csharp

var pathToName = new NodePath(\"Sprite2D:texture:resource_name\");
GD.Print(pathToName.GetSubname(0)); // Prints \"texture\"
GD.Print(pathToName.GetSubname(1)); // Prints \"resource_name\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_get_subname_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_subname_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NodePath_method_get_subname_count>`{.interpreted-text
role="ref"}

Returns the number of property names (\"subnames\") in the path. Each
subname in the node path is listed after a colon character (`:`).

For example, `"Level/RigidBody2D/Sprite2D:texture:resource_name"`
contains 2 subnames.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_hash}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hash**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NodePath_method_hash>`{.interpreted-text
role="ref"}

Returns the 32-bit hash value representing the node path\'s contents.

\*\*Note:\*\* Node paths with equal hash values are *not* guaranteed to
be the same, as a result of hash collisions. Node paths with different
hash values are guaranteed to be different.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_is_absolute}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_absolute**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NodePath_method_is_absolute>`{.interpreted-text
role="ref"}

Returns `true` if the node path is absolute. Unlike a relative path, an
absolute path is represented by a leading slash character (`/`) and
always begins from the `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"}. It can be used to reliably access nodes from the root node
(e.g. `"/root/Global"` if an autoload named \"Global\" exists).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NodePath_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the node path has been constructed from an empty
`String<class_String>`{.interpreted-text role="ref"} (`""`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_method_slice}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**slice**(begin: `int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"} = 2147483647)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_NodePath_method_slice>`{.interpreted-text
role="ref"}

Returns the slice of the **NodePath**, from `begin` (inclusive) to `end`
(exclusive), as a new **NodePath**.

The absolute value of `begin` and `end` will be clamped to the sum of
`get_name_count()<class_NodePath_method_get_name_count>`{.interpreted-text
role="ref"} and
`get_subname_count()<class_NodePath_method_get_subname_count>`{.interpreted-text
role="ref"}, so the default value for `end` makes it slice to the end of
the **NodePath** by default (i.e. `path.slice(1)` is a shorthand for
`path.slice(1, path.get_name_count() + path.get_subname_count())`).

If either `begin` or `end` are negative, they will be relative to the
end of the **NodePath** (i.e. `path.slice(0, -2)` is a shorthand for
`path.slice(0, path.get_name_count() + path.get_subname_count() - 2)`).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_NodePath_operator_neq_NodePath}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_NodePath_operator_neq_NodePath>`{.interpreted-text role="ref"}

Returns `true` if two node paths are not equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NodePath_operator_eq_NodePath}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_NodePath_operator_eq_NodePath>`{.interpreted-text role="ref"}

Returns `true` if two node paths are equal, that is, they are composed
of the same node names and subnames in the same order.
