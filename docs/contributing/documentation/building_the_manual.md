# Building the manual with Sphinx {#doc_building_the_manual}

This page explains how to build a local copy of the Godot manual using
the Sphinx docs engine. This allows you to have local HTML files and
build the documentation as a PDF, EPUB, or LaTeX file, for example.

Before you get started, make sure that you have:

- [Git](https://git-scm.com/)
- [make](https://www.gnu.org/software/make/) (unless you\'re using
  Windows)
- [Python](https://www.python.org/) 3

:::: note
::: title
Note
:::

Python 3 should come with the `pip3` command. You may need to write
`python3 -m pip` (Unix) or `py -m pip` (Windows) instead of `pip3`. If
both approaches fail, [make sure that you have pip3
installed](https://pip.pypa.io/en/stable/installation/).
::::

1.  *(Optional)* Set up a virtual environment. Virtual environments
    prevent potential conflicts between the Python packages in
    `requirements.txt` and other Python packages that are installed on
    your system.

    a.  Create the virtual environment:

        ::::: tabs
        ::: group-tab
        Windows

        ``` pwsh
        py -m venv godot-docs-venv
        ```
        :::

        ::: group-tab
        Other platforms

        ``` sh
        python3 -m venv godot-docs-venv
        ```
        :::
        :::::

    b.  Activate the virtual environment:

        ::::: tabs
        ::: group-tab
        Windows

        ``` pwsh
        godot-docs-venv\Scripts\activate.bat
        ```
        :::

        ::: group-tab
        Other platforms

        ``` sh
        source godot-docs-venv/bin/activate
        ```
        :::
        :::::

    c.  *(Optional)* Update pre-installed packages:

        ::::: tabs
        ::: group-tab
        Windows

        ``` pwsh
        py -m pip install --upgrade pip setuptools
        ```
        :::

        ::: group-tab
        Other platforms

        ``` sh
        pip3 install --upgrade pip setuptools
        ```
        :::
        :::::

2.  Clone the docs repo:

    ``` sh
    git clone https://github.com/godotengine/godot-docs.git
    ```

3.  Change directory into the docs repo:

    ``` sh
    cd godot-docs
    ```

4.  Install the required packages:

    ``` sh
    pip3 install -r requirements.txt
    ```

5.  Build the docs:

    ``` sh
    make html
    ```

    :::: note
    ::: title
    Note
    :::

    On Windows, that command will run `make.bat` instead of GNU Make (or
    an alternative).
    ::::

    Alternatively, you can build the documentation by running the
    sphinx-build program manually:

    ``` sh
    sphinx-build -b html ./ _build/html
    ```

The compilation will take some time as the `classes/` folder contains
hundreds of files. See
`doc_building_the_manual:performance`{.interpreted-text role="ref"}.

You can then browse the documentation by opening
`_build/html/index.html` in your web browser.

## Dealing with errors

If you run into errors, you may try the following command:

``` sh
make SPHINXBUILD=~/.local/bin/sphinx-build html
```

If you get a `MemoryError` or `EOFError`, you can remove the `classes/`
folder and run `make` again. This will drop the class references from
the final HTML documentation, but will keep the rest intact.

:::: important
::: title
Important
:::

If you delete the `classes/` folder, do not use `git add .` when working
on a pull request or the whole `classes/` folder will be removed when
you commit. See
[#3157](https://github.com/godotengine/godot-docs/issues/3157) for more
detail.
::::

## Hints for performance {#doc_building_the_manual:performance}

### RAM usage

Building the documentation requires at least 8 GB of RAM to run without
disk swapping, which slows it down. If you have at least 16 GB of RAM,
you can speed up compilation by running:

::::: tabs
::: group-tab
Windows

``` pwsh
set SPHINXOPTS=-j2 && make html
```
:::

::: group-tab
Other platforms

``` sh
make html SPHINXOPTS=-j2
```
:::
:::::

You can use `-j auto` to use all available CPU threads, but this can use
a lot of RAM if you have a lot of CPU threads. For instance, on a system
with 32 CPU threads, `-j auto` (which corresponds to `-j 32` here) can
require 20+ GB of RAM for Sphinx alone.

### Specifying a list of files

:::: warning
::: title
Warning
:::

This section will not work on Windows, since the repository is using a
simplified `make.bat` script instead of the real GNU Make program. If
you would like to get a Linux terminal on your system, consider using
[Windows Subsystem for Linux
(WSL)](https://learn.microsoft.com/en-us/windows/wsl/).
::::

You can specify a list of files to build, which can greatly speed up
compilation:

``` sh
make html FILELIST='classes/class_node.rst classes/class_resource.rst'
```

The list of files can also be provided by the `git` command. This way
you can automatically get the names of all files that have changed since
the last commit (`sed` is used to put them on the same line).

``` sh
make html FILELIST="$(git diff HEAD --name-only | sed -z 's/\n/ /g')"
```

You can replace `HEAD` with `master` to return all files changed from
the `master` branch:

``` sh
make html FILELIST="$(git diff master --name-only | sed -z 's/\n/ /g')"
```

If any images were modified, the output will contain some warnings about
them, but the build will proceed correctly.
