# Introduction to Godot {#doc_introduction_to_godot}

This article is here to help you figure out whether Godot might be a
good fit for you. We will introduce some broad features of the engine to
give you a feel for what you can achieve with it and answer questions
such as \"what do I need to know to get started?\".

This is by no means an exhaustive overview. We will introduce many more
features in this getting started series.

## What is Godot?

Godot is a general-purpose 2D and 3D game engine designed to support all
sorts of projects. You can use it to create games or applications you
can then release on desktop or mobile, as well as on the web.

You can also create console games with it, although you either need
strong programming skills or a developer to port the game for you.

:::: note
::: title
Note
:::

The Godot team can\'t provide an open source console export due to the
licensing terms imposed by console manufacturers. Regardless of the
engine you use, though, releasing games on consoles is always a lot of
work. You can read more on that here: `doc_consoles`{.interpreted-text
role="ref"}.
::::

## What can the engine do?

Godot was initially developed in-house by an Argentinian game studio.
Its development started in 2001, and the engine was rewritten and
improved tremendously since its open source release in 2014.

Some examples of games created with Godot include Cassette Beasts, PVKK,
and Usagi Shima. As for applications, the open source pixel art drawing
program Pixelorama is powered by Godot, and so is the voxel RPG creator
RPG in a Box. You can find many more examples in the [Official
Showcase](https://godotengine.org/showcase/).

<figure class="align-center">
<img src="img/introduction_usagi_shima.webp"
alt="img/introduction_usagi_shima.webp" />
<figcaption>Usagi Shima</figcaption>
</figure>

<figure class="align-center">
<img src="img/introduction_cassette_beasts.webp"
alt="img/introduction_cassette_beasts.webp" />
<figcaption>Cassette Beasts</figcaption>
</figure>

<figure class="align-center">
<img src="img/introduction_pvkk.webp"
alt="img/introduction_pvkk.webp" />
<figcaption>PVKK: Planetenverteidigungskanonenkommandant</figcaption>
</figure>

<figure class="align-center">
<img src="img/introduction_rpg_in_a_box.webp"
alt="img/introduction_rpg_in_a_box.webp" />
<figcaption>RPG in a Box</figcaption>
</figure>

## How does it work and look?

Godot comes with a fully-fledged game editor with integrated tools to
answer the most common needs. It includes a code editor, an animation
editor, a tilemap editor, a shader editor, a debugger, a profiler, and
more.

![image](img/introduction_editor.webp)

The team strives to offer a feature-rich game editor with a consistent
user experience. While there is always room for improvement, the user
interface keeps getting refined.

Of course, if you prefer, you can work with external programs. We
officially support importing 3D scenes designed in
[Blender](https://www.blender.org/) and maintain plugins to code in
[VSCode](https://github.com/godotengine/godot-vscode-plugin) and
[Emacs](https://github.com/godotengine/emacs-gdscript-mode) for GDScript
and C#. We also support Visual Studio for C# on Windows.

![image](img/introduction_vscode.png)

## Programming languages

Let\'s talk about the available programming languages.

You can code your games using
`GDScript <doc_gdscript>`{.interpreted-text role="ref"}, a
Godot-specific and tightly integrated language with a lightweight
syntax, or `C# <doc_c_sharp>`{.interpreted-text role="ref"}, which is
popular in the games industry. These are the two main scripting
languages we support.

With the GDExtension technology, you can also write gameplay or
high-performance algorithms in C or C++ without recompiling the engine.
You can use this technology to integrate third-party libraries and other
Software Development Kits (SDK) in the engine.

Of course, you can also directly add modules and features to the engine,
as it\'s completely free and open source.

## What do I need to know to use Godot? {#doc_introduction_learning_programming}

Godot is a feature-packed game engine. With its thousands of features,
there is a lot to learn. To make the most of it, you need good
programming foundations. While we try to make the engine accessible, you
will benefit a lot from knowing how to think like a programmer first.

Godot relies on the object-oriented programming paradigm. Being
comfortable with concepts such as classes and objects will help you code
efficiently in it.

If you are entirely new to programming, we recommend following the [CS50
open courseware](https://cs50.harvard.edu/x) from Harvard University.
It\'s a great free course that will teach you everything you need to
know to be off to a good start. It will save you countless hours and
hurdles learning any game engine afterward.

:::: note
::: title
Note
:::

In CS50, you will learn multiple programming languages. Don\'t be afraid
of that: programming languages have many similarities. The skills you
learn with one language transfer well to others.
::::

We will provide you with more Godot-specific learning resources in
`doc_learning_new_features`{.interpreted-text role="ref"}.

In the next part, you will get an overview of the engine\'s essential
concepts.
