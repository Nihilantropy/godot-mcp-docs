# Contributing to the documentation {#doc_contributing_to_the_documentation}

This guide explains how to contribute to Godot\'s documentation, be it
by writing or reviewing pages.

::: seealso
If you want to translate pages or the class reference from English to
other languages, read
`doc_editor_and_docs_localization`{.interpreted-text role="ref"}.
:::

## Getting started

To modify or create pages in the reference manual, you need to edit
`.rst` files in the [godot-docs GitHub
repository](https://github.com/godotengine/godot-docs). Modifying those
pages in a pull request triggers a rebuild of the online documentation
upon merging.

::: seealso
For details on Git usage and the pull request workflow, please refer to
the `doc_pr_workflow`{.interpreted-text role="ref"} page. Most of what
it describes regarding the main godotengine/godot repository is also
valid for the docs repository.
:::

:::: warning
::: title
Warning
:::

The class reference\'s source files are in the [Godot engine
repository](https://github.com/godotengine/godot). We generate the
`Class Reference <doc_class_reference>`{.interpreted-text role="ref"}
section of this documentation from them. If you want to update the
description of a class, its methods, or properties, read
`doc_updating_the_class_reference`{.interpreted-text role="ref"}.
::::

## What is the Godot documentation

The Godot documentation is intended as a comprehensive reference manual
for the Godot game engine. It is not meant to contain step-by-step
tutorials, except for two game creation tutorials in the Getting Started
section.

We strive to write factual content in an accessible and well-written
language. To contribute, you should also read:

1.  `doc_docs_writing_guidelines`{.interpreted-text role="ref"}. There,
    you will find rules and recommendations to write in a way that
    everyone understands.
2.  `doc_content_guidelines`{.interpreted-text role="ref"}. They explain
    the principles we follow to write the documentation and the kind of
    content we accept.

## Contributing changes

**Pull requests should use the** `master` **branch by default.** Only
make pull requests against other branches (e.g. `3.6` or `4.2`) if your
changes only apply to that specific version of Godot. After a pull
request is merged into `master`, it will usually be cherry-picked into
the current stable branch by documentation maintainers.

Though less convenient to edit than a wiki, this Git repository is where
we write the documentation. Having direct access to the source files in
a revision control system is a plus to ensure our documentation quality.

### Editing existing pages

To edit an existing page, locate its `.rst` source file and open it in
your favorite text editor. You can then commit the changes, push them to
your fork, and make a pull request. **Note that the pages in**
`classes/` **should not be edited here.** They are automatically
generated from Godot\'s [XML class
reference](https://github.com/godotengine/godot/tree/master/doc/classes).
See `doc_updating_the_class_reference`{.interpreted-text role="ref"} for
details.

::: seealso
To build the manual and test changes on your computer, see
`doc_building_the_manual`{.interpreted-text role="ref"}.
:::

## Editing pages online

You can edit the documentation online by clicking the **Edit on GitHub**
link in the top-right of every page.

Doing so takes you to the GitHub text editor. You need to have a GitHub
account and to log in to use it. Once logged in, you can propose change
like so:

1.  Click the **Edit on GitHub** button.
2.  On the GitHub page you\'re taken to, make sure the current branch is
    \"master\". Click the pencil icon in the top-right corner near the
    **Raw**, **Blame**, and **Delete** buttons. It has the tooltip
    \"Fork this project and edit the file\".
3.  Edit the text in the text editor.
4.  Click \"Commit changes\...\", summarize the changes you made and
    make sure to replace the placeholder \"Update file.rst\" by a short,
    but clear one-line description, as this is the commit title. Click
    the button **Propose changes**.
5.  On the following screens, click the **Create pull request** button
    until you see a message like *Username wants to merge 1 commit into
    godotengine:master from Username:patch-1*.

:::: note
::: title
Note
:::

If there are more commits than your own in the pull request it is likely
that your branch was created using the wrong origin, due to \"master\"
not being the current branch in step 2. You will need to rebase your
branch to \"master\" or create a new branch.
::::

Another contributor will review your changes and merge them into the
docs if they\'re good. They may also make changes or ask you to do so
before merging.

## Adding new pages

Before adding a new page, please ensure that it fits in the
documentation:

1.  Look for [existing
    issues](https://github.com/godotengine/godot-docs/issues) or open a
    new one to see if the page is necessary.
2.  Ensure there isn\'t a page that already covers the topic.
3.  Read our `doc_content_guidelines`{.interpreted-text role="ref"}.

To add a new page, create a `.rst` file with a meaningful name in the
section you want to add a file to, e.g. `tutorials/3d/light_baking.rst`.

You should then add your page to the relevant \"toctree\" (table of
contents, e.g. `tutorials/3d/index.rst`). Add your new filename to the
list on a new line, using a relative path and no extension, e.g. here
`light_baking`.

### Titles

Always begin pages with their title and a Sphinx reference name:

    .. _doc_insert_your_title_here:

    Insert your title here
    ======================

The reference `_doc_insert_your_title_here` and the title should match.

The reference allows linking to this page using the `:ref:` format, e.g.
`` :ref:`doc_insert_your_title_here ``\` would link to the above example
page (note the lack of leading underscore in the reference).

Write your titles like plain sentences, without capitalizing each word:

- **Good:** Understanding signals in Godot
- **Bad:** Understanding Signals In Godot

Only proper nouns, projects, people, and node class names should have
their first letter capitalized.

### Sphinx and reStructuredText syntax

Check Sphinx\'s [reST
Primer](https://www.sphinx-doc.org/en/stable/rest.html) and the
[official reference](https://docutils.sourceforge.net/rst.html) for
details on the syntax.

Sphinx uses specific reST comments to do specific operations, like
defining the table of contents (`.. toctree::`) or cross-referencing
pages. Check the [official Sphinx
documentation](https://www.sphinx-doc.org/en/stable/index.html) for more
details. To learn how to use Sphinx directives like `.. note::` or
`.. seealso::`, check out the [Sphinx directives
documentation](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html).

### Adding images and attachments

To add images, please put them in an `img/` folder next to the `.rst`
file with a meaningful name and include them in your page with:

``` rst
.. image:: img/image_name.webp
```

Alternatively, you can use the [figure]{.title-ref} directive, which
gives the image a contrasting border and allows centering it on the
page.

``` rst
.. figure:: img/image_name.webp
    :align: center
```

You can also include attachments as support material for a tutorial, by
placing them into a `files/` folder next to the `.rst` file, and using
this inline markup:

``` rst
:download:`file_name.zip <files/file_name.zip>`
```

Consider using the [godot-docs-project-starters
\<https://github.com/godotengine/godot-docs-project-starters\>]{.title-ref}
repository for hosting support materials, such as project templates and
asset packs. You can use a direct link to the generated archive from
that repository with the regular link markup:

``` rst
`file_name.zip <https://github.com/godotengine/godot-docs-project-starters/releases/download/latest-4.x/file_name.zip>`_
```

## License

This documentation and every page it contains is published under the
terms of the [Creative Commons Attribution 3.0 license (CC BY
3.0)](https://creativecommons.org/licenses/by/3.0/), with attribution to
\"Juan Linietsky, Ariel Manzur and the Godot community\".

By contributing to the documentation on the GitHub repository, you agree
that your changes are distributed under this license.
