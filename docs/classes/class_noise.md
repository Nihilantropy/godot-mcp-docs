github_url
:   hide

# Noise {#class_Noise}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `FastNoiseLite<class_FastNoiseLite>`{.interpreted-text
role="ref"}

Abstract base class for noise generators.

::: rst-class
classref-introduction-group
:::

## Description

This class defines the interface for noise generation libraries to
inherit from.

A default
`get_seamless_image()<class_Noise_method_get_seamless_image>`{.interpreted-text
role="ref"} implementation is provided for libraries that do not provide
seamless noise. This function requests a larger image from the
`get_image()<class_Noise_method_get_image>`{.interpreted-text
role="ref"} method, reverses the quadrants of the image, then uses the
strips of extra width to blend over the seams.

Inheriting noise classes can optionally override this function to
provide a more optimal algorithm.

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

## Method Descriptions

:::: {#class_Noise_method_get_image}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"} **get_image**(width:
`int<class_int>`{.interpreted-text role="ref"}, height:
`int<class_int>`{.interpreted-text role="ref"}, invert:
`bool<class_bool>`{.interpreted-text role="ref"} = false, in_3d_space:
`bool<class_bool>`{.interpreted-text role="ref"} = false, normalize:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Noise_method_get_image>`{.interpreted-text
role="ref"}

Returns an `Image<class_Image>`{.interpreted-text role="ref"} containing
2D noise values.

\*\*Note:\*\* With `normalize` set to `false`, the default
implementation expects the noise generator to return values in the range
`-1.0` to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Noise_method_get_image_3d}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\]
**get_image_3d**(width: `int<class_int>`{.interpreted-text role="ref"},
height: `int<class_int>`{.interpreted-text role="ref"}, depth:
`int<class_int>`{.interpreted-text role="ref"}, invert:
`bool<class_bool>`{.interpreted-text role="ref"} = false, normalize:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Noise_method_get_image_3d>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`Image<class_Image>`{.interpreted-text role="ref"}s containing 3D noise
values for use with
`ImageTexture3D.create()<class_ImageTexture3D_method_create>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* With `normalize` set to `false`, the default
implementation expects the noise generator to return values in the range
`-1.0` to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Noise_method_get_noise_1d}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_noise_1d**(x:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Noise_method_get_noise_1d>`{.interpreted-text
role="ref"}

Returns the 1D noise value at the given (x) coordinate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Noise_method_get_noise_2d}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_noise_2d**(x:
`float<class_float>`{.interpreted-text role="ref"}, y:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Noise_method_get_noise_2d>`{.interpreted-text
role="ref"}

Returns the 2D noise value at the given position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Noise_method_get_noise_2dv}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_noise_2dv**(v:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Noise_method_get_noise_2dv>`{.interpreted-text
role="ref"}

Returns the 2D noise value at the given position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Noise_method_get_noise_3d}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_noise_3d**(x:
`float<class_float>`{.interpreted-text role="ref"}, y:
`float<class_float>`{.interpreted-text role="ref"}, z:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Noise_method_get_noise_3d>`{.interpreted-text
role="ref"}

Returns the 3D noise value at the given position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Noise_method_get_noise_3dv}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_noise_3dv**(v:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Noise_method_get_noise_3dv>`{.interpreted-text
role="ref"}

Returns the 3D noise value at the given position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Noise_method_get_seamless_image}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**get_seamless_image**(width: `int<class_int>`{.interpreted-text
role="ref"}, height: `int<class_int>`{.interpreted-text role="ref"},
invert: `bool<class_bool>`{.interpreted-text role="ref"} = false,
in_3d_space: `bool<class_bool>`{.interpreted-text role="ref"} = false,
skirt: `float<class_float>`{.interpreted-text role="ref"} = 0.1,
normalize: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Noise_method_get_seamless_image>`{.interpreted-text
role="ref"}

Returns an `Image<class_Image>`{.interpreted-text role="ref"} containing
seamless 2D noise values.

\*\*Note:\*\* With `normalize` set to `false`, the default
implementation expects the noise generator to return values in the range
`-1.0` to `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Noise_method_get_seamless_image_3d}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Image<class_Image>`{.interpreted-text role="ref"}\]
**get_seamless_image_3d**(width: `int<class_int>`{.interpreted-text
role="ref"}, height: `int<class_int>`{.interpreted-text role="ref"},
depth: `int<class_int>`{.interpreted-text role="ref"}, invert:
`bool<class_bool>`{.interpreted-text role="ref"} = false, skirt:
`float<class_float>`{.interpreted-text role="ref"} = 0.1, normalize:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Noise_method_get_seamless_image_3d>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
`Image<class_Image>`{.interpreted-text role="ref"}s containing seamless
3D noise values for use with
`ImageTexture3D.create()<class_ImageTexture3D_method_create>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* With `normalize` set to `false`, the default
implementation expects the noise generator to return values in the range
`-1.0` to `1.0`.
