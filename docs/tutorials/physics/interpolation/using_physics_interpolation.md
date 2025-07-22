# Using physics interpolation {#doc_using_physics_interpolation}

How do we incorporate physics interpolation into a Godot game? Are there
any caveats?

We have tried to make the system as easy to use as possible, and many
existing games will work with few changes. That said there are some
situations which require special treatment, and these will be described.

## Turn on the physics interpolation setting

The first step is to turn on physics interpolation in
`Project Settings > Physics > Common > Physics Interpolation<class_ProjectSettings_property_physics/common/physics_interpolation>`{.interpreted-text
role="ref"} You can now run your game.

It is likely that nothing looks hugely different, particularly if you
are running physics at 60 TPS or a multiple of it. However, quite a bit
more is happening behind the scenes.

:::: tip
::: title
Tip
:::

To convert an existing game to use interpolation, it is highly
recommended that you temporarily set
`Project Settings > Physics > Common > Physics Tick per Second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"} to a low value such as `10`, which will make interpolation
problems more obvious.
::::

## Move (almost) all game logic from [process]{#process} to [physics_process]{#physics_process}

The most fundamental requirement for physics interpolation (which you
may be doing already) is that you should be moving and performing game
logic on your objects within `_physics_process` (which runs at a physics
tick) rather than `_process` (which runs on a rendered frame). This
means your scripts should typically be doing the bulk of their
processing within `_physics_process`, including responding to input and
AI.

Setting the transform of objects only within physics ticks allows the
automatic interpolation to deal with transforms *between* physics ticks,
and ensures the game will run the same whatever machine it is run on. As
a bonus, this also reduces CPU usage if the game is rendering at high
FPS, since AI logic (for example) will no longer run on every rendered
frame.

:::: note
::: title
Note
:::

If you attempt to set the transform of interpolated objects *outside*
the physics tick, the calculations for the interpolated position will be
incorrect, and you will get jitter. This jitter may not be visible on
your machine, but it *will* occur for some players. For this reason,
setting the transform of interpolated objects should be avoided outside
of the physics tick. Godot will attempt to produce warnings in the
editor if this case is detected.
::::

:::: tip
::: title
Tip
:::

This is only a *soft rule*. There are some occasions where you might
want to teleport objects outside of the physics tick (for instance when
starting a level, or respawning objects). Still, in general, you should
be applying transforms from the physics tick.
::::

## Ensure that all indirect movement happens during physics ticks

Consider that in Godot, nodes can be moved not just directly in your own
scripts, but also by automatic methods such as tweening, animation, and
navigation. All these methods should also have their timing set to
operate on the physics tick rather than each frame (\"idle\"), **if**
you are using them to move objects (*these methods can also be used to
control properties that are not interpolated*).

:::: note
::: title
Note
:::

Also consider that nodes can be moved not just by moving themselves, but
also by moving parent nodes in the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}. The movement
of parents should therefore also only occur during physics ticks.
::::

## Choose a physics tick rate

When using physics interpolation, the rendering is decoupled from
physics, and you can choose any value that makes sense for your game.
You are no longer limited to values that are multiples of the user\'s
monitor refresh rate (for stutter-free gameplay if the target FPS is
reached).

As a rough guide:

  -----------------------------------------------------------------------
  Low tick rates (10-30)  Medium tick rates       High tick rates (60+)
                          (30-60)                 
  ----------------------- ----------------------- -----------------------
  Better CPU performance  Good physics behavior   Good with fast physics
                          in complex scenes       

  Add some delay to input Good for first person   Good for racing games
                          games                   

  Simple physics                                  
  behaviour                                       
  -----------------------------------------------------------------------

:::: note
::: title
Note
:::

You can always change the tick rate as you develop, it is as simple as
changing the project setting.
::::

## Call `reset_physics_interpolation()` when teleporting objects

Most of the time, interpolation is what you want between two physics
ticks. However, there is one situation in which it may *not* be what you
want. That is when you are initially placing objects, or moving them to
a new location. Here, you don\'t want a smooth motion between where the
object was (e.g. the origin) and the initial position - you want an
instantaneous move.

The solution to this is to call the
`Node.reset_physics_interpolation<class_Node_method_reset_physics_interpolation>`{.interpreted-text
role="ref"} function. What this function does under the hood is set the
internally stored *previous transform* of the object to be equal to the
*current transform*. This ensures that when interpolating between these
two equal transforms, there will be no movement.

Even if you forget to call this, it will usually not be a problem in
most situations (especially at high tick rates). This is something you
can easily leave to the polishing phase of your game. The worst that
will happen is seeing a streaking motion for a frame or so when you move
them - you will know when you need it!

There are actually two ways to use `reset_physics_interpolation()`:

*Standing start (e.g. player)*

1)  Set the initial transform
2)  Call `reset_physics_interpolation()`

The previous and current transforms will be identical, resulting in no
initial movement.

*Moving start (e.g. bullet)*

1)  Set the initial transform
2)  Call `reset_physics_interpolation()`
3)  Immediately set the transform expected after the first tick of
    motion

The previous transform will be the starting position, and the current
transform will act as though a tick of simulation has already taken
place. This will immediately start moving the object, instead of having
a tick delay standing still.

:::: important
::: title
Important
:::

Make sure you set the transform and call `reset_physics_interpolation()`
in the correct order as shown above, otherwise you will see unwanted
\"streaking\".
::::

## Testing and debugging tips

Even if you intend to run physics at 60 TPS, in order to thoroughly test
your interpolation and get the smoothest gameplay, it is highly
recommended to temporarily set the physics tick rate to a low value such
as 10 TPS.

The gameplay may not work perfectly, but it should enable you to more
easily see cases where you should be calling
`Node.reset_physics_interpolation<class_Node_method_reset_physics_interpolation>`{.interpreted-text
role="ref"}, or where you should be using your own custom interpolation
on e.g. a `Camera3D<class_Camera3D>`{.interpreted-text role="ref"}. Once
you have these cases fixed, you can set the physics tick rate back to
the desired setting.

The other great advantage to testing at a low tick rate is you can often
notice other game systems that are synchronized to the physics tick and
creating glitches which you may want to work around. Typical examples
include setting animation blend values, which you may decide to set in
`_process()` and interpolate manually.
