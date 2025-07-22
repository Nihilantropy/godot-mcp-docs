# Idle and Physics Processing {#doc_idle_and_physics_processing}

Games run in a loop. Each frame, you need to update the state of your
game world before drawing it on screen. Godot provides two virtual
methods in the Node class to do so:
`Node._process() <class_Node_private_method__process>`{.interpreted-text
role="ref"} and
`Node._physics_process() <class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}. If you define either or both in a script, the engine will
call them automatically.

There are two types of processing available to you:

1.  **Idle processing** allows you to run code that updates a node every
    frame, as often as possible.
2.  **Physics processing** happens at a fixed rate, 60 times per second
    by default. This is independent of your game\'s actual framerate,
    and keeps physics running smoothly. You should use it for anything
    that involves the physics engine, like moving a body that collides
    with the environment.

You can activate idle processing by defining the `_process()` method in
a script. You can turn it off and back on by calling `Node.set_process()
<class_Node_method_set_process>`{.interpreted-text role="ref"}.

The engine calls this method every time it draws a frame:

:::: tabs
.. code-tab:: gdscript GDScript

func [process]{#process}(delta):

:   \# Do something\... pass

::: code-tab
csharp
:::

public override void [Process]{#process}(double delta) { // Do
something\... }
::::

Keep in mind that the frequency at which the engine calls `_process()`
depends on your application\'s framerate, which varies over time and
across devices.

The function\'s `delta` parameter is the time elapsed in seconds since
the previous call to `_process()`. Use this parameter to make
calculations independent of the framerate. For example, you should
always multiply a speed value by `delta` to animate a moving object.

Physics processing works with a similar virtual function:
`_physics_process()`. Use it for calculations that must happen before
each physics step, like moving a character that collides with the game
world. As mentioned above, `_physics_process()` runs at fixed time
intervals as much as possible to keep the physics interactions stable.
You can change the interval between physics steps in the Project
Settings, under Physics -\> Common -\> Physics Fps. By default, it\'s
set to run 60 times per second.

The engine calls this method before every physics step:

:::: tabs
.. code-tab:: gdscript GDScript

func [physics_process]{#physics_process}(delta):

:   \# Do something\... pass

::: code-tab
csharp
:::

public override void [PhysicsProcess]{#physicsprocess}(double delta) {
// Do something\... }
::::

The function `_process()` is not synchronized with physics. Its rate
depends on hardware and game optimization. It also runs after the
physics step in single-threaded games.

You can see the `_process()` function at work by creating a scene with a
single Label node, with the following script attached to it:

:::: tabs
.. code-tab:: gdscript GDScript

extends Label

var time = 0

func [process]{#process}(delta):

:   time += delta text = str(time) \# \'text\' is a built-in Label
    property.

::: code-tab
csharp
:::

using Godot;

public partial class CustomLabel : Label { private double [time]{#time};

> public override void [Process]{#process}(double delta) { [time]{#time}
> += delta; Text = [time.ToString]{#time.tostring}(); // \'Text\' is a
> built-in Label property. }

}
::::

When you run the scene, you should see a counter increasing each frame.
