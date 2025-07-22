# Class reference primer {#doc_class_reference_primer}

This page explains how to write the class reference. You will learn
where to write new descriptions for the classes, methods, and properties
for Godot\'s built-in node types.

::: seealso
To learn to submit your changes to the Godot project using the Git
version control system, see
`doc_updating_the_class_reference`{.interpreted-text role="ref"}.
:::

The reference for each class is contained in an XML file like the one
below:

``` xml
<class name="Node2D" inherits="CanvasItem" version="4.0">
    <brief_description>
        A 2D game object, inherited by all 2D-related nodes. Has a position, rotation, scale, and Z index.
    </brief_description>
    <description>
        A 2D game object, with a transform (position, rotation, and scale). All 2D nodes, including physics objects and sprites, inherit from Node2D. Use Node2D as a parent node to move, scale and rotate children in a 2D project. Also gives control of the node's render order.
    </description>
    <tutorials>
        <link title="Custom drawing in 2D">https://docs.godotengine.org/en/latest/tutorials/2d/custom_drawing_in_2d.html</link>
        <link title="All 2D Demos">https://github.com/godotengine/godot-demo-projects/tree/master/2d</link>
    </tutorials>
    <methods>
        <method name="apply_scale">
            <return type="void">
            </return>
            <argument index="0" name="ratio" type="Vector2">
            </argument>
            <description>
                Multiplies the current scale by the [code]ratio[/code] vector.
            </description>
        </method>
        [...]
        <method name="translate">
            <return type="void">
            </return>
            <argument index="0" name="offset" type="Vector2">
            </argument>
            <description>
                Translates the node by the given [code]offset[/code] in local coordinates.
            </description>
        </method>
    </methods>
    <members>
        <member name="global_position" type="Vector2" setter="set_global_position" getter="get_global_position">
            Global position.
        </member>
        [...]
        <member name="z_index" type="int" setter="set_z_index" getter="get_z_index" default="0">
            Z index. Controls the order in which the nodes render. A node with a higher Z index will display in front of others.
        </member>
    </members>
    <constants>
    </constants>
</class>
```

It starts with brief and long descriptions. In the generated docs, the
brief description is always at the top of the page, while the long
description lies below the list of methods, variables, and constants.
You can find methods, member variables, constants, and signals in
separate XML nodes.

For each, you want to learn how they work in Godot\'s source code. Then,
fill their documentation by completing or improving the text in these
tags:

- [\<brief_description\>]{.title-ref}
- [\<description\>]{.title-ref}
- [\<constant\>]{.title-ref}
- [\<method\>]{.title-ref} (in its [\<description\>]{.title-ref} tag;
  return types and arguments don\'t take separate documentation strings)
- [\<member\>]{.title-ref}
- [\<signal\>]{.title-ref} (in its [\<description\>]{.title-ref} tag;
  arguments don\'t take separate documentation strings)
- [\<constant\>]{.title-ref}

Write in a clear and simple language. Always follow the
`writing guidelines
<doc_docs_writing_guidelines>`{.interpreted-text role="ref"} to keep
your descriptions short and easy to read. **Do not leave empty lines**
in the descriptions: each line in the XML file will result in a new
paragraph, even if it is empty.

## How to edit class XML {#doc_class_reference_editing_xml}

Edit the file for your chosen class in `doc/classes/` to update the
class reference. The folder contains an XML file for each class. The XML
lists the constants and methods you will find in the class reference.
Godot generates and updates the XML automatically.

:::: note
::: title
Note
:::

For some modules in the engine\'s source code, you\'ll find the XML
files in the `modules/<module_name>/doc_classes/` directory instead.
::::

Edit it using your favorite text editor. If you use a code editor, make
sure that it doesn\'t change the indent style: you should use tabs for
the XML and four spaces inside BBCode-style blocks. More on that below.

To check that the modifications you\'ve made are correct in the
generated documentation, navigate to the `doc/` folder and run the
command `make rst`. This will convert the XML files to the online
documentation\'s format and output errors if anything\'s wrong.

Alternatively, you can build Godot and open the modified page in the
built-in code reference. To learn how to compile the engine, read the
`compilation
guide <toc-devel-compiling>`{.interpreted-text role="ref"}.

We recommend using a code editor that supports XML files like Vim, Atom,
Visual Studio Code, Notepad++, or another to comfortably edit the file.
You can also use their search feature to find classes and properties
quickly.

:::: tip
::: title
Tip
:::

If you use Visual Studio Code, you can install the [vscode-xml
extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml)
to get linting for class reference XML files.
::::

### Improve formatting with BBCode style tags {#doc_class_reference_bbcode}

Godot\'s XML class reference supports BBCode-like tags for linking as
well as formatting text and code. In the tables below you can find the
available tags, usage examples and the results after conversion to
reStructuredText.

#### Linking

Whenever you link to a member of another class, you need to specify the
class name. For links to the same class, the class name is optional and
can be omitted.

+----------------+--------------------+-------------------------------+
| Tag and        | Example            | Result                        |
| Description    |                    |                               |
+================+====================+===============================+
| | `[Class]`    | `Mov               | Move the                      |
| | Link to      | e the [Sprite2D].` | `clas                         |
|   class        |                    | s_Sprite2D`{.interpreted-text |
|                |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| | `[annotatio  | `See [annotation   | See                           |
| n Class.name]` |  @GDScript.@rpc].` | `@GDScript                    |
| | Link to      |                    | .@rpc <class_@GDScript_annota |
|   annotation   |                    | tion_@rpc>`{.interpreted-text |
|                |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| | `[constan    | `See [con          | See                           |
| t Class.name]` | stant Color.RED].` | `Color.RED <class_Color_con   |
| | Link to      |                    | stant_RED>`{.interpreted-text |
|   constant     |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| | `[enu        | `See [enum         | See                           |
| m Class.name]` |  Mesh.ArrayType].` | `Mesh.ArrayType <enum_Mesh_   |
| | Link to enum |                    | ArrayType>`{.interpreted-text |
|                |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| | `[membe      | `Get [memb         | Get                           |
| r Class.name]` | er Node2D.scale].` | `Nod                          |
| | Link to      |                    | e2D.scale <class_Node2D_prope |
|   member       |                    | rty_scale>`{.interpreted-text |
|                |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| | `[metho      | `Call [met         | Call                          |
| d Class.name]` | hod Node3D.hide].` | `N                            |
| | Link to      |                    | ode3D.hide() <class_Node3D_me |
|   method       |                    | thod_hide>`{.interpreted-text |
|                |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| | `[constructo | `Use [construc     | Use                           |
| r Class.name]` | tor Color.Color].` | `Colo                         |
| | Link to      |                    | r.Color <class_Color_construc |
|   built-in     |                    | tor_Color>`{.interpreted-text |
|   constructor  |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| | `[operato    | `Use [operator C   | Use                           |
| r Class.name]` | olor.operator *].` | `Color.op                     |
| | Link to      |                    | erator * <class_Color_operato |
|   built-in     |                    | r_mul_int>`{.interpreted-text |
|   operator     |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| | `[signa      | `Emit [sign        | Emit                          |
| l Class.name]` | al Node.renamed].` | `N                            |
| | Link to      |                    | ode.renamed <class_Node_signa |
|   signal       |                    | l_renamed>`{.interpreted-text |
|                |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| | `[theme_ite  | `See [theme_       | See                           |
| m Class.name]` | item Label.font].` | `L                            |
| | Link to      |                    | abel.font <class_Label_theme_ |
|   theme item   |                    | font_font>`{.interpreted-text |
|                |                    | role="ref"}.                  |
+----------------+--------------------+-------------------------------+
| |              | `Takes [param si   | Takes `size` for the size.    |
| `[param name]` | ze] for the size.` |                               |
| | Parameter    |                    |                               |
|   name (as     |                    |                               |
|   code)        |                    |                               |
+----------------+--------------------+-------------------------------+

:::: note
::: title
Note
:::

Currently only `class_@GDScript`{.interpreted-text role="ref"} has
annotations.
::::

#### Formatting text

+-------------------+---------------------------+---------------------+
| Tag and           | Example                   | Result              |
| Description       |                           |                     |
+===================+===========================+=====================+
| | `[br]`          | | `Line 1.[br]`           | | Line 1.           |
| | Line break      | | `Line 2.`               | | Line 2.           |
+-------------------+---------------------------+---------------------+
| | `[lb]` `[rb]`   | `[lb]b[rb]text[lb]/b[rb]` | \[b\]text\[/b\]     |
| | `[` and `]`     |                           |                     |
|   respectively    |                           |                     |
+-------------------+---------------------------+---------------------+
| | `[b]` `[/b]`    | `Do [b]n                  | Do **not** call     |
| | Bold            | ot[/b] call this method.` | this method.        |
+-------------------+---------------------------+---------------------+
| | `[i]` `[/i]`    | `Returns the              | Returns the         |
| | Italic          |  [i]global[/i] position.` | *global* position.  |
+-------------------+---------------------------+---------------------+
| | `[u]` `[/u]`    | `[u]Alw                   | <u>Always</         |
| | Underline       | ays[/u] use this method.` | u> use this method. |
+-------------------+---------------------------+---------------------+
| | `[s]` `[/s]`    | `[s]O                     | <s>Outdat           |
| | Strikethrough   | utdated information.[/s]` | ed information.</s> |
+-------------------+---------------------------+---------------------+
| | `[url]`         | | `[url]h                 | | <h                |
|   `[/url]`        | ttps://example.com[/url]` | ttps://example.com> |
| | Hyperlink       | | `[url=https://e         | | [Website](h       |
|                   | xample.com]Website[/url]` | ttps://example.com) |
+-------------------+---------------------------+---------------------+
| | `[center]`      | `[c                       | <center             |
|   `[/center]`     | enter]2 + 2 = 4[/center]` | >2 + 2 = 4</center> |
| | Horizontal      |                           |                     |
|   centering       |                           |                     |
+-------------------+---------------------------+---------------------+
| | `[kbd]`         | `Pr                       | Press               |
|   `[/kbd]`        | ess [kbd]Ctrl + C[/kbd].` | `Ctrl + C           |
| | Keyboard/mouse  |                           | `{.interpreted-text |
|   shortcut        |                           | role="kbd"}.        |
+-------------------+---------------------------+---------------------+
| | `[code]`        | `Re                       | Returns `true`.     |
|   `[/code]`       | turns [code]true[/code].` |                     |
| | Inline code     |                           |                     |
|   fragment        |                           |                     |
+-------------------+---------------------------+---------------------+

:::: note
::: title
Note
:::

1.  Some supported tags like `[color]` and `[font]` are not listed here
    because they are not recommended in the engine documentation.
2.  `[kbd]` disables BBCode until the parser encounters `[/kbd]`.
3.  `[code]` disables BBCode until the parser encounters `[/code]`.
::::

#### Formatting code blocks

There are two options for formatting code blocks:

1.  Use `[codeblock]` if you want to add an example for a specific
    language.
2.  Use `[codeblocks]`, `[gdscript]`, and `[csharp]` if you want to add
    the same example for both languages, GDScript and C#.

By default, `[codeblock]` highlights GDScript syntax. You can change it
using the `lang` attribute. Currently supported options are:

- `[codeblock lang=text]` disables syntax highlighting;
- `[codeblock lang=gdscript]` highlights GDScript syntax;
- `[codeblock lang=csharp]` highlights C# syntax (only in .NET version).

:::: note
::: title
Note
:::

`[codeblock]` disables BBCode until the parser encounters
`[/codeblock]`.
::::

:::: warning
::: title
Warning
:::

Use `[codeblock]` for pre-formatted code blocks. Since Godot 4.5,
**tabs** should be used for indentation.
::::

For example:

``` none
[codeblock]
func _ready():
    var sprite = get_node("Sprite2D")
    print(sprite.get_pos())
[/codeblock]
```

Will display as:

``` gdscript
func _ready():
    var sprite = get_node("Sprite2D")
    print(sprite.get_pos())
```

If you need to have different code version in GDScript and C#, use
`[codeblocks]` instead. If you use `[codeblocks]`, you also need to have
at least one of the language-specific tags, `[gdscript]` and `[csharp]`.

Always write GDScript code examples first! You can use this
[experimental code translation
tool](https://github.com/HaSa1002/codetranslator) to speed up your
workflow.

``` none
[codeblocks]
[gdscript]
func _ready():
    var sprite = get_node("Sprite2D")
    print(sprite.get_pos())
[/gdscript]
[csharp]
public override void _Ready()
{
    var sprite = GetNode("Sprite2D");
    GD.Print(sprite.GetPos());
}
[/csharp]
[/codeblocks]
```

The above will display as:

:::: tabs
.. code-tab:: gdscript GDScript

func [ready]{#ready}():

:   var sprite = get_node(\"Sprite2D\") print(sprite.get_pos())

::: code-tab
csharp
:::

public override void [Ready]{#ready}() { var sprite =
GetNode(\"Sprite2D\"); GD.Print(sprite.GetPos()); }
::::

#### Formatting notes and warnings

To denote important information, add a paragraph starting with
\"\[b\]Note:\[/b\]\" at the end of the description:

``` none
[b]Note:[/b] Only available when using the Vulkan renderer.
```

To denote crucial information that could cause security issues or loss
of data if not followed carefully, add a paragraph starting with
\"\[b\]Warning:\[/b\]\" at the end of the description:

``` none
[b]Warning:[/b] If this property is set to [code]true[/code], it allows clients to execute arbitrary code on the server.
```

In all the paragraphs described above, make sure the punctuation is part
of the BBCode tags for consistency.

### Marking API as deprecated/experimental

To mark an API as deprecated or experimental, you need to add the
corresponding XML attribute. The attribute value must be a message
explaining why the API is not recommended (BBCode markup is supported)
or an empty string (the default message will be used). If an API element
is marked as deprecated/experimental, then it is considered documented
even if the description is empty.

``` xml
<class name="Parallax2D" inherits="Node2D" experimental="This node is meant to replace [ParallaxBackground] and [ParallaxLayer]. The implementation may change in the future." xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../class.xsd">
    [...]
</class>

<constant name="RESPONSE_USE_PROXY" value="305" enum="ResponseCode" deprecated="Many clients ignore this response code for security reasons. It is also deprecated by the HTTP standard.">
    HTTP status code [code]305 Use Proxy[/code].
</constant>

<member name="auto_translate" type="bool" setter="set_auto_translate" getter="is_auto_translating" deprecated="Use [member Node.auto_translate_mode] instead.">
    Toggles if any text should automatically change to its translated version depending on the current locale.
</member>

<method name="get_method_call_mode" qualifiers="const" deprecated="Use [member AnimationMixer.callback_mode_method] instead.">
    <return type="int" enum="AnimationPlayer.AnimationMethodCallMode" />
    <description>
        Returns the call mode used for "Call Method" tracks.
    </description>
</method>
```
