allow_comments
:   False

# Building from source {#doc_compiling_index}

Godot prides itself on being very easy to build, by C++ project
standards.
`Godot uses the SCons build system <doc_faq_why_scons>`{.interpreted-text
role="ref"}, and after the initial setup compiling the engine for your
current platform should be as easy as running:

``` shell
scons
```

But you will probably need to use at least some of the available options
to configure the build to match your specific needs, be it a custom
engine fork, a lightweight build stripped of extra modules, or an
executable targeting engine development.

The articles below should help you navigate configuration options
available, as well as prerequisites required to compile Godot exactly
the way you need.

**Basics of building Godot**

Let\'s start with basics, and learn how to get Godot\'s source code, and
then which options to use to compile it regardless of your target
platform.

::: {#toc-devel-compiling .toctree maxdepth="1"}
getting_source introduction_to_the_buildsystem
:::

**Building for target platforms**

Below you can find instructions for compiling the engine for your
specific target platform. Note that Godot supports cross-compilation,
which means you can compile it for a target platform that doesn\'t match
your current platform (say, target Linux while being on Windows). The
guides will try their best to cover all possible situations.

::: {#toc-devel-compiling-platforms .toctree maxdepth="1"}
compiling_for_windows compiling_for_linuxbsd compiling_for_macos
compiling_for_android compiling_for_ios cross-compiling_for_ios_on_linux
compiling_for_web
:::

**Other compilation targets and options**

Some additional universal compilation options require further setup.
Namely, while Godot does have C#/.NET support as a part of its main
codebase, it does not get compiled by default to reduce the executable
size for users who don\'t need C# for their projects.

Articles below explain how to configure the buildsystem for cases like
this, and also cover some optimization techniques.

::: {#toc-devel-compiling-options .toctree maxdepth="1"}
compiling_with_dotnet compiling_with_script_encryption_key
optimizing_for_size
:::
