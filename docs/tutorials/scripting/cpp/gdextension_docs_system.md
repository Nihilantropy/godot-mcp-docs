# Adding documentation {#doc_godot_cpp_docs_system}

:::: note
::: title
Note
:::

Adding documentation for GDExtensions is only possible for Godot 4.3 and
later. The support can be integrated into your project regardless
because the snippet will check if you use the appropriate godot-cpp
version. If you set the `compatibility_minimum` to 4.2 and you load a
project with the extension through a 4.2 editor, the documentation page
for that class will be empty. The extension itself will still work.
::::

The GDExtension documentation system works in a similar manner to the
built-in engine documentation. It uses a series of XML files (one per
class) to document the exposed constructors, properties, methods,
constants, signals, and theme items of each class.

:::: note
::: title
Note
:::

We are assuming you are using the project files explained in the
`example project <doc_godot_cpp_getting_started>`{.interpreted-text
role="ref"} with the following structure:
::::

``` none
gdextension_cpp_example/  # GDExtension directory
|
+--demo/                  # game example/demo to test the extension
|   |
|   +--main.tscn
|   |
|   +--bin/
|       |
|       +--gdexample.gdextension
|
+--godot-cpp/             # C++ bindings
|
+--src/                   # source code of the extension we are building
|   |
|   +--register_types.cpp
|   +--register_types.h
|   +--gdexample.cpp
|   +--gdexample.h
```

Inside the Godot demo project directory of your GDExtension directory,
run the following terminal command:

``` none
# Replace "godot" with the full path to a Godot editor binary
# if Godot is not installed in your `PATH`.
godot --doctool ../ --gdextension-docs
```

This command calls upon the Godot editor binary to generate
documentation via the `--doctool` and `--gdextension-docs` commands. The
`../` addition is to let Godot know where the GDExtension SConstruct
file is located. By calling this command, Godot generates a
`doc_classes` directory inside the project directory in which it
generates XML files for the GDExtension classes. Those files can then be
edited to add information about member variables, methods, signals, and
more.

To add the now edited documentation to the GDExtension and let the
editor load it, you need to add the following lines to your SConstruct
file:

``` py
if env["target"] in ["editor", "template_debug"]:
try:
    doc_data = env.GodotCPPDocData("src/gen/doc_data.gen.cpp", source=Glob("doc_classes/*.xml"))
    sources.append(doc_data)
except AttributeError:
    print("Not including class reference as we're targeting a pre-4.3 baseline.")
```

The if-statement checks if we are compiling the GDExtension library with
the `editor` and `template_debug` flags. SCons then tries to load all
the XML files inside the `doc_classes` directory and appends them to the
`sources` variable which already includes all the source files of your
extension. If it fails it means we are currently trying to compile the
library when the `godot_cpp` is set to a version before 4.3.

After loading the extension in a 4.3 Godot editor or later and open the
documentation of your extension class either by
`Ctrl + Click`{.interpreted-text role="kbd"} in the script editor or the
Editor help dialog you will see something like this:

![image](img/gdextension_docs_generation.webp)

## Documentation styling

To style specific parts of text you can use BBCode tags similarly to how
they can be used in
`RichTextLabels <doc_bbcode_in_richtextlabel>`{.interpreted-text
role="ref"}. You can set text as bold, italic, underlined, colored,
codeblocks etc. by embedding them in tags like this:

``` none
[b]this text will be shown as bold[/b]
```

Currently they supported tags for the GDExtension documentation system
are:

+------------------------------------------+---------------------------+
| Tag                                      | Example                   |
+------------------------------------------+---------------------------+
| | **b**                                  | `[b]{text}[/b]`           |
| | Makes `{text}` use the bold (or bold   |                           |
|   italics) font of `RichTextLabel`.      |                           |
+------------------------------------------+---------------------------+
| | **i**                                  | `[i]{text}[/i]`           |
| | Makes `{text}` use the italics (or     |                           |
|   bold italics) font of `RichTextLabel`. |                           |
+------------------------------------------+---------------------------+
| | **u**                                  | `[u]{text}[/u]`           |
| | Makes `{text}` underlined.             |                           |
+------------------------------------------+---------------------------+
| | **s**                                  | `[s]{text}[/s]`           |
| | Makes `{text}` strikethrough.          |                           |
+------------------------------------------+---------------------------+
| | **kbd**                                | `[kbd]{text}[/kbd]`       |
| | Makes `{text}` use a grey beveled      |                           |
|   background, indicating a keyboard      |                           |
|   shortcut.                              |                           |
+------------------------------------------+---------------------------+
| | **code**                               | `[code]{text}[/code]`     |
| | Makes inline `{text}` use the mono     |                           |
|   font and styles the text color and     |                           |
|   background like code.                  |                           |
+------------------------------------------+---------------------------+
| | **codeblocks**                         | | `[codeblocks]`          |
| | Makes multiline `{text}` use the mono  | | `[gdscript]`            |
|   font and styles the text color and     | | `{text}`                |
|   background like code.                  | | `[/gdscript]`           |
| | The addition of the `[gdscript]` tag   | | `[/codeblocks]`         |
|   highlights the GDScript specific       |                           |
|   syntax.                                |                           |
+------------------------------------------+---------------------------+
| | **center**                             | `[center]{text}[/center]` |
| | Makes `{text}` horizontally centered.  |                           |
| | Same as `[p align=center]`.            |                           |
+------------------------------------------+---------------------------+
| | **url**                                | | `[url]{link}[/url]`     |
| | Creates a hyperlink (underlined and    | | `                       |
|   clickable text). Can contain optional  | [url={link}]{text}[/url]` |
|   `{text}` or display `{link}` as is.    |                           |
+------------------------------------------+---------------------------+
| | **img**                                | | `[img]{path}[/img]`     |
| | Inserts an image from the `{path}`     | | `[                      |
|   (can be any valid                      | img={width}]{path}[/img]` |
|   `class_Texture2D`{.interpreted-text    | | `[img={widt             |
|   role="ref"} resource).                 | h}x{height}]{path}[/img]` |
| | If `{width}` is provided, the image    | | `[i                     |
|   will try to fit that width maintaining | mg={valign}]{path}[/img]` |
|   the aspect ratio.                      | | `[im                    |
| | If both `{width}` and `{height}` are   | g {options}]{path}[/img]` |
|   provided, the image will be scaled to  |                           |
|   that size.                             |                           |
| | Add `%` to the end of `{width}` or     |                           |
|   `{height}` value to specify it as      |                           |
|   percentages of the control width       |                           |
|   instead of pixels.                     |                           |
| | If `{valign}` configuration is         |                           |
|   provided, the image will try to align  |                           |
|   to the surrounding text, see           |                           |
|   `doc_bbcode_in_richtextlabel_imag      |                           |
| e_and_table_alignment`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
| | Supports configuration options, see    |                           |
|   `doc_bbcode_in_richte                  |                           |
| xtlabel_image_options`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
+------------------------------------------+---------------------------+
| | **color**                              | `[color={c                |
| | Changes the color of `{text}`. Color   | ode/name}]{text}[/color]` |
|   must be provided by a common name (see |                           |
|   `doc_bbcode_in_richt                   |                           |
| extlabel_named_colors`{.interpreted-text |                           |
|   role="ref"}) or using the HEX format   |                           |
|   (e.g. `#ff00ff`, see                   |                           |
|   `doc_bbcode_in_ric                     |                           |
| htextlabel_hex_colors`{.interpreted-text |                           |
|   role="ref"}).                          |                           |
+------------------------------------------+---------------------------+

## Publishing documentation online

You may want to publish an online reference for your GDExtension,
similar to this website. The most important step is to build
reStructuredText (`.rst`) files from your XML class reference:

``` bash
# You need a version.py file, so download it first.
curl -sSLO https://raw.githubusercontent.com/godotengine/godot/refs/heads/master/version.py

# Edit version.py according to your project before proceeding.
# Then, run the rst generator. You'll need to have Python installed for this command to work.
curl -sSL https://raw.githubusercontent.com/godotengine/godot/master/doc/tools/make_rst.py | python3 - -o "docs/classes" -l "en" doc_classes
```

Your `.rst` files will now be available in `docs/classes/`. From here,
you can use any documentation builder that supports reStructuredText
syntax to create a website from them.

[godot-docs](https://github.com/godotengine/godot-docs) uses
[Sphinx](https://www.sphinx-doc.org/en/master/). You can use the
repository as a basis to build your own documentation system. The
following guide describes the basic steps, but they are not exhaustive:
You will need a bit of personal insight to make it work.

1.  Add [godot-docs](https://github.com/godotengine/godot-docs) as a
    submodule to your `docs/` folder.
2.  Copy over its `conf.py`, `index.rst`, `.readthedocs.yaml` files into
    `/docs/`. You may later decide to copy over and edit more of
    godot-docs\' files, like `_templates/layout.html`.
3.  Modify these files according to your project. This mostly involves
    adjusting paths to point to the `godot-docs` subfolder, as well as
    strings to reflect it\'s your project rather than Godot you\'re
    building the docs for.
4.  Create an account on [readthedocs.org](http://readthedocs.org).
    Import your project, and modify its base `.readthedocs.yaml` file
    path to `/docs/.readthedocs.yaml`.

Once you have completed all these steps, your documentation should be
available at `<repo-name>.readthedocs.io`.
