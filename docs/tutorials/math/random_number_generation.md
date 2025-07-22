# Random number generation {#doc_random_number_generation}

Many games rely on randomness to implement core game mechanics. This
page guides you through common types of randomness and how to implement
them in Godot.

After giving you a brief overview of useful functions that generate
random numbers, you will learn how to get random elements from arrays,
dictionaries, and how to use a noise generator in GDScript. Lastly,
we\'ll take a look at cryptographically secure random number generation
and how it differs from typical random number generation.

:::: note
::: title
Note
:::

Computers cannot generate \"true\" random numbers. Instead, they rely on
[pseudorandom number
generators](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
(PRNGs).

Godot internally uses the [PCG Family](https://www.pcg-random.org/) of
pseudorandom number generators.
::::

## Global scope versus RandomNumberGenerator class

Godot exposes two ways to generate random numbers: via *global scope*
methods or using the `class_RandomNumberGenerator`{.interpreted-text
role="ref"} class.

Global scope methods are easier to set up, but they don\'t offer as much
control.

RandomNumberGenerator requires more code to use, but allows creating
multiple instances, each with their own seed and state.

This tutorial uses global scope methods, except when the method only
exists in the RandomNumberGenerator class.

## The randomize() method

:::: note
::: title
Note
:::

Since Godot 4.0, the random seed is automatically set to a random value
when the project starts. This means you don\'t need to call
`randomize()` in `_ready()` anymore to ensure that results are random
across project runs. However, you can still use `randomize()` if you
want to use a specific seed number, or generate it using a different
method.
::::

In global scope, you can find a `randomize()
<class_@GlobalScope_method_randomize>`{.interpreted-text role="ref"}
method. **This method should be called only once when your project
starts to initialize the random seed.** Calling it multiple times is
unnecessary and may impact performance negatively.

Putting it in your main scene script\'s `_ready()` method is a good
choice:

:::: tabs
.. code-tab:: gdscript GDScript

func [ready]{#ready}():

:   randomize()

::: code-tab
csharp
:::

public override void [Ready]{#ready}() { GD.Randomize(); }
::::

You can also set a fixed random seed instead using `seed()
<class_@GlobalScope_method_seed>`{.interpreted-text role="ref"}. Doing
so will give you *deterministic* results across runs:

:::: tabs
.. code-tab:: gdscript GDScript

func [ready]{#ready}():

:   seed(12345) \# To use a string as a seed, you can hash it to a
    number. seed(\"Hello world\".hash())

::: code-tab
csharp
:::

public override void [Ready]{#ready}() { GD.Seed(12345); // To use a
string as a seed, you can hash it to a number. GD.Seed(\"Hello
world\".Hash()); }
::::

When using the RandomNumberGenerator class, you should call
`randomize()` on the instance since it has its own seed:

:::: tabs
.. code-tab:: gdscript GDScript

var random = RandomNumberGenerator.new() random.randomize()

::: code-tab
csharp
:::

var random = new RandomNumberGenerator(); random.Randomize();
::::

## Getting a random number

Let\'s look at some of the most commonly used functions and methods to
generate random numbers in Godot.

The function
`randi() <class_@GlobalScope_method_randi>`{.interpreted-text
role="ref"} returns a random number between `0` and `2^32 - 1`. Since
the maximum value is huge, you most likely want to use the modulo
operator (`%`) to bound the result between 0 and the denominator:

:::: tabs
.. code-tab:: gdscript GDScript

\# Prints a random integer between 0 and 49. print(randi() % 50)

\# Prints a random integer between 10 and 60. print(randi() % 51 + 10)

::: code-tab
csharp
:::

// Prints a random integer between 0 and 49. GD.Print(GD.Randi() % 50);

// Prints a random integer between 10 and 60. GD.Print(GD.Randi() % 51 +
10);
::::

`randf() <class_@GlobalScope_method_randf>`{.interpreted-text
role="ref"} returns a random floating-point number between 0 and 1. This
is useful to implement a
`doc_random_number_generation_weighted_random_probability`{.interpreted-text
role="ref"} system, among other things.

`randfn() <class_@GlobalScope_method_randfn>`{.interpreted-text
role="ref"} returns a random floating-point number following a [normal
distribution](https://en.wikipedia.org/wiki/Normal_distribution). This
means the returned value is more likely to be around the mean (0.0 by
default), varying by the deviation (1.0 by default):

:::: tabs
.. code-tab:: gdscript GDScript

\# Prints a random floating-point number from a normal distribution with
a mean 0.0 and deviation 1.0. print(randfn(0.0, 1.0))

::: code-tab
csharp
:::

// Prints a random floating-point number from a normal distribution with
a mean 0.0 and deviation 1.0. GD.Print(GD.Randfn(0.0, 1.0));
::::

`randf_range() <class_@GlobalScope_method_randf_range>`{.interpreted-text
role="ref"} takes two arguments `from` and `to`, and returns a random
floating-point number between `from` and `to`:

:::: tabs
.. code-tab:: gdscript GDScript

\# Prints a random floating-point number between -4 and 6.5.
print(randf_range(-4, 6.5))

::: code-tab
csharp
:::

// Prints a random floating-point number between -4 and 6.5.
GD.Print(GD.RandRange(-4.0, 6.5));
::::

`randi_range() <class_@GlobalScope_method_randi_range>`{.interpreted-text
role="ref"} takes two arguments `from` and `to`, and returns a random
integer between `from` and `to`:

:::: tabs
.. code-tab:: gdscript GDScript

\# Prints a random integer between -10 and 10. print(randi_range(-10,
10))

::: code-tab
csharp
:::

// Prints a random integer number between -10 and 10.
GD.Print(GD.RandRange(-10, 10));
::::

## Get a random array element

We can use random integer generation to get a random element from an
array, or use the
`Array.pick_random<class_Array_method_pick_random>`{.interpreted-text
role="ref"} method to do it for us:

:::: tabs
.. code-tab:: gdscript GDScript

var [fruits]{#fruits} = \[\"apple\", \"orange\", \"pear\", \"banana\"\]

func [ready]{#ready}():

:   

    for i in range(100):

    :   \# Pick 100 fruits randomly. print(get_fruit())

    for i in range(100):

    :   \# Pick 100 fruits randomly, this time using the
        [Array.pick_random()]{.title-ref} \# helper method. This has the
        same behavior as [get_fruit()]{.title-ref}.
        print([fruits.pick_random]{#fruits.pick_random}())

func get_fruit():

:   var random_fruit = [fruits]{#fruits}\[randi() %
    [fruits.size]{#fruits.size}()\] \# Returns \"apple\", \"orange\",
    \"pear\", or \"banana\" every time the code runs. \# We may get the
    same fruit multiple times in a row. return random_fruit

::: code-tab
csharp
:::

// Use Godot\'s Array type instead of a BCL type so we can use
[PickRandom()]{.title-ref} on it. private
Godot.Collections.Array\<string\> [fruits]{#fruits} = \[\"apple\",
\"orange\", \"pear\", \"banana\"\];

public override void [Ready]{#ready}() { for (int i = 0; i \< 100; i++)
{ // Pick 100 fruits randomly. GD.Print(GetFruit()); }

> for (int i = 0; i \< 100; i++) { // Pick 100 fruits randomly, this
> time using the [Array.PickRandom()]{.title-ref} // helper method. This
> has the same behavior as [GetFruit()]{.title-ref}.
> GD.Print([fruits.PickRandom]{#fruits.pickrandom}()); }

}

public string GetFruit() { string randomFruit =
[fruits]{#fruits}\[GD.Randi() % [fruits.Size]{#fruits.size}()\]; //
Returns \"apple\", \"orange\", \"pear\", or \"banana\" every time the
code runs. // We may get the same fruit multiple times in a row. return
randomFruit; }
::::

To prevent the same fruit from being picked more than once in a row, we
can add more logic to the above method. In this case, we can\'t use
`Array.pick_random<class_Array_method_pick_random>`{.interpreted-text
role="ref"} since it lacks a way to prevent repetition:

:::: tabs
.. code-tab:: gdscript GDScript

var [fruits]{#fruits} = \[\"apple\", \"orange\", \"pear\", \"banana\"\]
var [last_fruit]{#last_fruit} = \"\"

func [ready]{#ready}():

:   \# Pick 100 fruits randomly. for i in range(100): print(get_fruit())

func get_fruit():

:   var random_fruit = [fruits]{#fruits}\[randi() %
    [fruits.size]{#fruits.size}()\] while random_fruit ==
    [last_fruit]{#last_fruit}: \# The last fruit was picked. Try again
    until we get a different fruit. random_fruit =
    [fruits]{#fruits}\[randi() % [fruits.size]{#fruits.size}()\]

    \# Note: if the random element to pick is passed by reference, \#
    such as an array or dictionary, \# use [\_last_fruit =
    random_fruit.duplicate()]{.title-ref} instead.
    [last_fruit]{#last_fruit} = random_fruit

    \# Returns \"apple\", \"orange\", \"pear\", or \"banana\" every time
    the code runs. \# The function will never return the same fruit more
    than once in a row. return random_fruit

::: code-tab
csharp
:::

private string\[\] [fruits]{#fruits} = \[\"apple\", \"orange\",
\"pear\", \"banana\"\]; private string [lastFruit]{#lastfruit} = \"\";

public override void [Ready]{#ready}() { for (int i = 0; i \< 100; i++)
{ // Pick 100 fruits randomly. GD.Print(GetFruit()); } }

public string GetFruit() { string randomFruit =
[fruits]{#fruits}\[GD.Randi() % [fruits.Length]{#fruits.length}\]; while
(randomFruit == [lastFruit]{#lastfruit}) { // The last fruit was picked.
Try again until we get a different fruit. randomFruit =
[fruits]{#fruits}\[GD.Randi() % [fruits.Length]{#fruits.length}\]; }

> [lastFruit]{#lastfruit} = randomFruit;
>
> // Returns \"apple\", \"orange\", \"pear\", or \"banana\" every time
> the code runs. // The function will never return the same fruit more
> than once in a row. return randomFruit;

}
::::

This approach can be useful to make random number generation feel less
repetitive. Still, it doesn\'t prevent results from \"ping-ponging\"
between a limited set of values. To prevent this, use the `shuffle bag
<doc_random_number_generation_shuffle_bags>`{.interpreted-text
role="ref"} pattern instead.

## Get a random dictionary value

We can apply similar logic from arrays to dictionaries as well:

:::: tabs
.. code-tab:: gdscript GDScript

var [metals]{#metals} = {

:   \"copper\": {\"quantity\": 50, \"price\": 50}, \"silver\":
    {\"quantity\": 20, \"price\": 150}, \"gold\": {\"quantity\": 3,
    \"price\": 500},

}

func [ready]{#ready}():

:   

    for i in range(20):

    :   print(get_metal())

func get_metal():

:   var random_metal = [metals.values]{#metals.values}()\[randi() %
    metals.size()\] \# Returns a random metal value dictionary every
    time the code runs. \# The same metal may be selected multiple times
    in succession. return random_metal

::: code-tab
csharp
:::

private Godot.Collections.Dictionary\<string,
Godot.Collections.Dictionary\<string, int\>\> [metals]{#metals} = new()
{ {\"copper\", new Godot.Collections.Dictionary\<string,
int\>{{\"quantity\", 50}, {\"price\", 50}}}, {\"silver\", new
Godot.Collections.Dictionary\<string, int\>{{\"quantity\", 20},
{\"price\", 150}}}, {\"gold\", new Godot.Collections.Dictionary\<string,
int\>{{\"quantity\", 3}, {\"price\", 500}}}, };

public override void [Ready]{#ready}() { for (int i = 0; i \< 20; i++) {
GD.Print(GetMetal()); } }

public Godot.Collections.Dictionary\<string, int\> GetMetal() { var (\_,
randomMetal) = [metals.ElementAt]{#metals.elementat}((int)(GD.Randi() %
[metals.Count]{#metals.count})); // Returns a random metal value
dictionary every time the code runs. // The same metal may be selected
multiple times in succession. return randomMetal; }
::::

## Weighted random probability {#doc_random_number_generation_weighted_random_probability}

The `randf() <class_@GlobalScope_method_randf>`{.interpreted-text
role="ref"} method returns a floating-point number between 0.0 and 1.0.
We can use this to create a \"weighted\" probability where different
outcomes have different likelihoods:

:::: tabs
.. code-tab:: gdscript GDScript

func [ready]{#ready}():

:   

    for i in range(100):

    :   print(get_item_rarity())

func get_item_rarity():

:   var random_float = randf()

    if random_float \< 0.8:

    :   \# 80% chance of being returned. return \"Common\"

    elif random_float \< 0.95:

    :   \# 15% chance of being returned. return \"Uncommon\"

    else:

    :   \# 5% chance of being returned. return \"Rare\"

::: code-tab
csharp
:::

public override void [Ready]{#ready}() { for (int i = 0; i \< 100; i++)
{ GD.Print(GetItemRarity()); } }

public string GetItemRarity() { float randomFloat = GD.Randf();

> if (randomFloat \< 0.8f) { // 80% chance of being returned. return
> \"Common\"; } else if (randomFloat \< 0.95f) { // 15% chance of being
> returned. return \"Uncommon\"; } else { // 5% chance of being
> returned. return \"Rare\"; }

}
::::

You can also get a weighted random *index* using the
`rand_weighted() <class_RandomNumberGenerator_method_rand_weighted>`{.interpreted-text
role="ref"} method on a RandomNumberGenerator instance. This returns a
random integer between 0 and the size of the array that is passed as a
parameter. Each value in the array is a floating-point number that
represents the *relative* likelihood that it will be returned as an
index. A higher value means the value is more likely to be returned as
an index, while a value of `0` means it will never be returned as an
index.

For example, if `[0.5, 1, 1, 2]` is passed as a parameter, then the
method is twice as likely to return `3` (the index of the value `2`) and
twice as unlikely to return `0` (the index of the value `0.5`) compared
to the indices `1` and `2`.

Since the returned value matches the array\'s size, it can be used as an
index to get a value from another array as follows:

:::: tabs
.. code-tab:: gdscript GDScript

\# Prints a random element using the weighted index that is returned by
[rand_weighted()]{.title-ref}. \# Here, \"apple\" will be returned twice
as rarely as \"orange\" and \"pear\". \# \"banana\" is twice as common
as \"orange\" and \"pear\", and four times as common as \"apple\". var
fruits = \[\"apple\", \"orange\", \"pear\", \"banana\"\] var
probabilities = \[0.5, 1, 1, 2\];

var random = RandomNumberGenerator.new()
print(fruits\[random.rand_weighted(probabilities)\])

::: code-tab
csharp
:::

// Prints a random element using the weighted index that is returned by
[RandWeighted()]{.title-ref}. // Here, \"apple\" will be returned twice
as rarely as \"orange\" and \"pear\". // \"banana\" is twice as common
as \"orange\" and \"pear\", and four times as common as \"apple\".
string\[\] fruits = \[\"apple\", \"orange\", \"pear\", \"banana\"\];
float\[\] probabilities = \[0.5f, 1, 1, 2\];

var random = new RandomNumberGenerator();
GD.Print(fruits\[random.RandWeighted(probabilities)\]);
::::

## \"Better\" randomness using shuffle bags {#doc_random_number_generation_shuffle_bags}

Taking the same example as above, we would like to pick fruits at
random. However, relying on random number generation every time a fruit
is selected can lead to a less *uniform* distribution. If the player is
lucky (or unlucky), they could get the same fruit three or more times in
a row.

You can accomplish this using the *shuffle bag* pattern. It works by
removing an element from the array after choosing it. After multiple
selections, the array ends up empty. When that happens, you reinitialize
it to its default value:

:::: tabs
.. code-tab:: gdscript GDScript

var [fruits]{#fruits} = \[\"apple\", \"orange\", \"pear\", \"banana\"\]
\# A copy of the fruits array so we can restore the original value into
[fruits]{.title-ref}. var [fruits_full]{#fruits_full} = \[\]

func [ready]{#ready}():

:   [fruits_full]{#fruits_full} =
    [fruits.duplicate]{#fruits.duplicate}()
    [fruits.shuffle]{#fruits.shuffle}()

    for i in 100:

    :   print(get_fruit())

func get_fruit():

:   

    if [fruits.is_empty]{#fruits.is_empty}():

    :   \# Fill the fruits array again and shuffle it. [fruits]{#fruits}
        = [fruits_full.duplicate]{#fruits_full.duplicate}()
        [fruits.shuffle]{#fruits.shuffle}()

    \# Get a random fruit, since we shuffled the array, \# and remove it
    from the [\_fruits]{.title-ref} array. var random_fruit =
    [fruits.pop_front]{#fruits.pop_front}() \# Returns \"apple\",
    \"orange\", \"pear\", or \"banana\" every time the code runs,
    removing it from the array. \# When all fruit are removed, it
    refills the array. return random_fruit

::: code-tab
csharp
:::

private Godot.Collections.Array\<string\> [fruits]{#fruits} =
\[\"apple\", \"orange\", \"pear\", \"banana\"\]; // A copy of the fruits
array so we can restore the original value into [fruits]{.title-ref}.
private Godot.Collections.Array\<string\> [fruitsFull]{#fruitsfull};

public override void [Ready]{#ready}() { [fruitsFull]{#fruitsfull} =
[fruits.Duplicate]{#fruits.duplicate}();
[fruits.Shuffle]{#fruits.shuffle}();

> for (int i = 0; i \< 100; i++) { GD.Print(GetFruit()); }

}

public string GetFruit() { if([fruits.Count]{#fruits.count} == 0) { //
Fill the fruits array again and shuffle it. [fruits]{#fruits} =
[fruitsFull.Duplicate]{#fruitsfull.duplicate}();
[fruits.Shuffle]{#fruits.shuffle}(); }

> // Get a random fruit, since we shuffled the array, string randomFruit
> = [fruits]{#fruits}\[0\]; // and remove it from the
> [\_fruits]{.title-ref} array. [fruits.RemoveAt]{#fruits.removeat}(0);
> // Returns \"apple\", \"orange\", \"pear\", or \"banana\" every time
> the code runs, removing it from the array. // When all fruit are
> removed, it refills the array. return randomFruit;

}
::::

When running the above code, there is a chance to get the same fruit
twice in a row. Once we picked a fruit, it will no longer be a possible
return value unless the array is now empty. When the array is empty, we
reset it back to its default value, making it possible to have the same
fruit again, but only once.

## Random noise

The random number generation shown above can show its limits when you
need a value that *slowly* changes depending on the input. The input can
be a position, time, or anything else.

To achieve this, you can use random *noise* functions. Noise functions
are especially popular in procedural generation to generate
realistic-looking terrain. Godot provides
`class_fastnoiselite`{.interpreted-text role="ref"} for this, which
supports 1D, 2D and 3D noise. Here\'s an example with 1D noise:

:::: tabs
.. code-tab:: gdscript GDScript

var [noise]{#noise} = FastNoiseLite.new()

func [ready]{#ready}():

:   \# Configure the FastNoiseLite instance.
    [noise.noise_type]{#noise.noise_type} =
    FastNoiseLite.NoiseType.TYPE_SIMPLEX_SMOOTH
    [noise.seed]{#noise.seed} = randi()
    [noise.fractal_octaves]{#noise.fractal_octaves} = 4
    [noise.frequency]{#noise.frequency} = 1.0 / 20.0

    for i in 100:

    :   \# Prints a slowly-changing series of floating-point numbers \#
        between -1.0 and 1.0.
        print([noise.get_noise_1d]{#noise.get_noise_1d}(i))

::: code-tab
csharp
:::

private FastNoiseLite [noise]{#noise} = new FastNoiseLite();

public override void [Ready]{#ready}() { // Configure the FastNoiseLite
instance. [noise.NoiseType]{#noise.noisetype} =
FastNoiseLite.NoiseTypeEnum.SimplexSmooth; [noise.Seed]{#noise.seed} =
(int)GD.Randi(); [noise.FractalOctaves]{#noise.fractaloctaves} = 4;
[noise.Frequency]{#noise.frequency} = 1.0f / 20.0f;

> for (int i = 0; i \< 100; i++) {
> GD.Print([noise.GetNoise1D]{#noise.getnoise1d}(i)); }

}
::::

## Cryptographically secure pseudorandom number generation

So far, the approaches mentioned above are **not** suitable for
*cryptographically secure* pseudorandom number generation (CSPRNG). This
is fine for games, but this is not sufficient for scenarios where
encryption, authentication or signing is involved.

Godot offers a `class_Crypto`{.interpreted-text role="ref"} class for
this. This class can perform asymmetric key encryption/decryption,
signing/verification, while also generating cryptographically secure
random bytes, RSA keys, HMAC digests, and self-signed
`class_X509Certificate`{.interpreted-text role="ref"}s.

The downside of
`CSPRNG (Cryptographically secure pseudorandom number generation)`{.interpreted-text
role="abbr"} is that it\'s much slower than standard pseudorandom number
generation. Its API is also less convenient to use. As a result,
`CSPRNG (Cryptographically secure pseudorandom number generation)`{.interpreted-text
role="abbr"} should be avoided for gameplay elements.

Example of using the Crypto class to generate 2 random integers between
`0` and `2^32 - 1` (inclusive):

    var crypto := Crypto.new()
    # Request as many bytes as you need, but try to minimize the amount
    # of separate requests to improve performance.
    # Each 32-bit integer requires 4 bytes, so we request 8 bytes.
    var byte_array := crypto.generate_random_bytes(8)

    # Use the ``decode_u32()`` method from PackedByteArray to decode a 32-bit unsigned integer
    # from the beginning of `byte_array`. This method doesn't modify `byte_array`.
    var random_int_1 := byte_array.decode_u32(0)
    # Do the same as above, but with an offset of 4 bytes since we've already decoded
    # the first 4 bytes previously.
    var random_int_2 := byte_array.decode_u32(4)

    prints("Random integers:", random_int_1, random_int_2)

::: seealso
See `class_PackedByteArray`{.interpreted-text role="ref"}\'s
documentation for other methods you can use to decode the generated
bytes into various types of data, such as integers or floats.
:::
