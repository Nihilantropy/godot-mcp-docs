github_url
:   hide

# RandomNumberGenerator {#class_RandomNumberGenerator}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides methods for generating pseudo-random numbers.

::: rst-class
classref-introduction-group
:::

## Description

RandomNumberGenerator is a class for generating pseudo-random numbers.
It currently uses [PCG32](https://www.pcg-random.org/).

\*\*Note:\*\* The underlying algorithm is an implementation detail and
should not be depended upon.

To generate a random float number (within a given range) based on a
time-dependent seed:

    var rng = RandomNumberGenerator.new()
    func _ready():
        var my_random_number = rng.randf_range(-10.0, 10.0)

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Random number generation <../tutorials/math/random_number_generation>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_RandomNumberGenerator_property_seed}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **seed** = `0`
`🔗<class_RandomNumberGenerator_property_seed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_seed**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_seed**()

Initializes the random number generator state based on the given seed
value. A given seed will give a reproducible sequence of pseudo-random
numbers.

\*\*Note:\*\* The RNG does not have an avalanche effect, and can output
similar random streams given similar seeds. Consider using a hash
function to improve your seed quality if they\'re sourced externally.

\*\*Note:\*\* Setting this property produces a side effect of changing
the internal
`state<class_RandomNumberGenerator_property_state>`{.interpreted-text
role="ref"}, so make sure to initialize the seed *before* modifying the
`state<class_RandomNumberGenerator_property_state>`{.interpreted-text
role="ref"}:

\*\*Note:\*\* The default value of this property is pseudo-random, and
changes when calling
`randomize()<class_RandomNumberGenerator_method_randomize>`{.interpreted-text
role="ref"}. The `0` value documented here is a placeholder, and not the
actual default seed.

    var rng = RandomNumberGenerator.new()
    rng.seed = hash("Godot")
    rng.state = 100 # Restore to some previously saved state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RandomNumberGenerator_property_state}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **state** = `0`
`🔗<class_RandomNumberGenerator_property_state>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_state**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_state**()

The current state of the random number generator. Save and restore this
property to restore the generator to a previous state:

    var rng = RandomNumberGenerator.new()
    print(rng.randf())
    var saved_state = rng.state # Store current state.
    print(rng.randf()) # Advance internal state.
    rng.state = saved_state # Restore the state.
    print(rng.randf()) # Prints the same value as previously.

\*\*Note:\*\* Do not set state to arbitrary values, since the random
number generator requires the state to have certain qualities to behave
properly. It should only be set to values that came from the state
property itself. To initialize the random number generator with
arbitrary input, use
`seed<class_RandomNumberGenerator_property_seed>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* The default value of this property is pseudo-random, and
changes when calling
`randomize()<class_RandomNumberGenerator_method_randomize>`{.interpreted-text
role="ref"}. The `0` value documented here is a placeholder, and not the
actual default state.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RandomNumberGenerator_method_rand_weighted}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**rand_weighted**(weights:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_RandomNumberGenerator_method_rand_weighted>`{.interpreted-text
role="ref"}

Returns a random index with non-uniform weights. Prints an error and
returns `-1` if the array is empty.

:::: tabs
::: code-tab
gdscript

var rng = RandomNumberGenerator.new()

var my_array = \[\"one\", \"two\", \"three\", \"four\"\] var weights =
PackedFloat32Array(\[0.5, 1, 1, 2\])

\# Prints one of the four elements in [my_array]{.title-ref}. \# It is
more likely to print \"four\", and less likely to print \"one\".
print(my_array\[rng.rand_weighted(weights)\])
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RandomNumberGenerator_method_randf}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **randf**()
`🔗<class_RandomNumberGenerator_method_randf>`{.interpreted-text
role="ref"}

Returns a pseudo-random float between `0.0` and `1.0` (inclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RandomNumberGenerator_method_randf_range}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **randf_range**(from:
`float<class_float>`{.interpreted-text role="ref"}, to:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_RandomNumberGenerator_method_randf_range>`{.interpreted-text
role="ref"}

Returns a pseudo-random float between `from` and `to` (inclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RandomNumberGenerator_method_randfn}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **randfn**(mean:
`float<class_float>`{.interpreted-text role="ref"} = 0.0, deviation:
`float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_RandomNumberGenerator_method_randfn>`{.interpreted-text
role="ref"}

Returns a
[normally-distributed](https://en.wikipedia.org/wiki/Normal_distribution),
pseudo-random floating-point number from the specified `mean` and a
standard `deviation`. This is also known as a Gaussian distribution.

\*\*Note:\*\* This method uses the [Box-Muller
transform](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform)
algorithm.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RandomNumberGenerator_method_randi}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **randi**()
`🔗<class_RandomNumberGenerator_method_randi>`{.interpreted-text
role="ref"}

Returns a pseudo-random 32-bit unsigned integer between `0` and
`4294967295` (inclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RandomNumberGenerator_method_randi_range}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **randi_range**(from:
`int<class_int>`{.interpreted-text role="ref"}, to:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RandomNumberGenerator_method_randi_range>`{.interpreted-text
role="ref"}

Returns a pseudo-random 32-bit signed integer between `from` and `to`
(inclusive).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RandomNumberGenerator_method_randomize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **randomize**()
`🔗<class_RandomNumberGenerator_method_randomize>`{.interpreted-text
role="ref"}

Sets up a time-based seed for this **RandomNumberGenerator** instance.
Unlike the `@GlobalScope<class_@GlobalScope>`{.interpreted-text
role="ref"} random number generation functions, different
**RandomNumberGenerator** instances can use different seeds.
