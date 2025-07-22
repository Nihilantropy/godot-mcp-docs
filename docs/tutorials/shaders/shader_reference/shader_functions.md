# Built-in functions {#doc_shader_functions}

Godot supports a large number of built-in functions, conforming roughly
to the GLSL ES 3.0 specification.

:::: note
::: title
Note
:::

The following type aliases only used in documentation to reduce
repetitive function declarations. They can each refer to any of several
actual types.

  ----------------------------------------------------------------------------
  alias             actual types                           glsl documentation
                                                           alias
  ----------------- -------------------------------------- -------------------
  vec_type          float, vec2, vec3, or vec4             genType

  vec_int_type      int, ivec2, ivec3, or ivec4            genIType

  vec_uint_type     uint, uvec2, uvec3, or uvec4           genUType

  vec_bool_type     bool, bvec2, bvec3, or bvec4           genBType

  mat_type          mat2, mat3, or mat4                    mat

  gvec4_type        vec4, ivec4, or uvec4                  gvec4

  gsampler2D        sampler2D, isampler2D, or uSampler2D   gsampler2D

  gsampler2DArray   sampler2DArray, isampler2DArray, or    gsampler2DArray
                    uSampler2DArray                        

  gsampler3D        sampler3D, isampler3D, or uSampler3D   gsampler3D
  ----------------------------------------------------------------------------

If any of these are specified for multiple parameters, they must all be
the same type unless otherwise noted.
::::

::::: {#shading_componentwise}
:::: note
::: title
Note
:::

Many functions that accept one or more vectors or matrices perform the
described function on each component of the vector/matrix. Some
examples:

  Operation                             Equivalent Scalar Operation
  ------------------------------------- -----------------------------------------
  `sqrt(vec2(4, 64))`                   `vec2(sqrt(4), sqrt(64))`
  `min(vec2(3, 4), 1)`                  `vec2(min(3, 1), min(4, 1))`
  `min(vec3(1, 2, 3),vec3(5, 1, 3))`    `vec3(min(1, 5), min(2, 1), min(3, 3))`
  `pow(vec3(3, 8, 5 ), 2)`              `vec3(pow(3, 2), pow(8, 2), pow(5, 2))`
  `pow(vec3(3, 8, 5), vec3(1, 2, 4))`   `vec3(pow(3, 1), pow(8, 2), pow(5, 4))`

The [GLSL Language
Specification](http://www.opengl.org/registry/doc/GLSLangSpec.4.30.6.pdf)
says under section 5.10 Vector and Matrix Operations:

> With a few exceptions, operations are component-wise. Usually, when an
> operator operates on a vector or matrix, it is operating independently
> on each component of the vector or matrix, in a component-wise
> fashion. \[\...\] The exceptions are matrix multiplied by vector,
> vector multiplied by matrix, and matrix multiplied by matrix. These do
> not operate component-wise, but rather perform the correct linear
> algebraic multiply.
::::
:::::

These function descriptions are adapted and modified from [official
OpenGL documentation](https://registry.khronos.org/OpenGL-Refpages/gl4/)
originally published by Khronos Group under the [Open Publication
License](https://opencontent.org/openpub). Each function description
links to the corresponding official OpenGL documentation. Modification
history for this page can be found on
[GitHub](https://github.com/godotengine/godot-docs/blob/master/tutorials/shaders/shader_reference/shader_functions.rst).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-reftable-group
:::

## Trigonometric functions

+----------------------+----------------------+----------------------+
| > Return Type        | > Function           | Description / Return |
|                      |                      | value                |
+======================+======================+======================+
| `v                   | `radians             | Convert degrees to   |
| ec_type (Any of: flo | <shader_func_radians | radians.             |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"}         |                      |
|                      | degrees)             |                      |
+----------------------+----------------------+----------------------+
| `v                   | `degrees             | Convert radians to   |
| ec_type (Any of: flo | <shader_func_degrees | degrees.             |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"}         |                      |
|                      | radians)             |                      |
+----------------------+----------------------+----------------------+
| `v                   | `sin<shader_func_sin | Sine.                |
| ec_type (Any of: flo | >`{.interpreted-text |                      |
| at, vec2, vec3, vec4 | role="ref"}(`v       |                      |
| )`{.interpreted-text | ec_type (Any of: flo |                      |
| role="abbr"}         | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `cos<shader_func_cos | Cosine.              |
| ec_type (Any of: flo | >`{.interpreted-text |                      |
| at, vec2, vec3, vec4 | role="ref"}(`v       |                      |
| )`{.interpreted-text | ec_type (Any of: flo |                      |
| role="abbr"}         | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `tan<shader_func_tan | Tangent.             |
| ec_type (Any of: flo | >`{.interpreted-text |                      |
| at, vec2, vec3, vec4 | role="ref"}(`v       |                      |
| )`{.interpreted-text | ec_type (Any of: flo |                      |
| role="abbr"}         | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `a                   | Arc sine.            |
| ec_type (Any of: flo | sin<shader_func_asin |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `a                   | Arc cosine.          |
| ec_type (Any of: flo | cos<shader_func_acos |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| | `v                 | | `a                 | Arc tangent.         |
| ec_type (Any of: flo | tan<shader_func_atan |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text |   role="ref"}(`v     |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `v                 | at, vec2, vec3, vec4 |                      |
| ec_type (Any of: flo | )`{.interpreted-text |                      |
| at, vec2, vec3, vec4 |   role="abbr"}       |                      |
| )`{.interpreted-text |   y_over_x)          |                      |
|   role="abbr"}       | | `at                |                      |
|                      | an<shader_func_atan2 |                      |
|                      | >`{.interpreted-text |                      |
|                      |   role="ref"}(`v     |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} y,    |                      |
|                      |   `v                 |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} x)    |                      |
+----------------------+----------------------+----------------------+
| `v                   | `s                   | Hyperbolic sine.     |
| ec_type (Any of: flo | inh<shader_func_sinh |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `c                   | Hyperbolic cosine.   |
| ec_type (Any of: flo | osh<shader_func_cosh |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `t                   | Hyperbolic tangent.  |
| ec_type (Any of: flo | anh<shader_func_tanh |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `asi                 | Arc hyperbolic sine. |
| ec_type (Any of: flo | nh<shader_func_asinh |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `aco                 | Arc hyperbolic       |
| ec_type (Any of: flo | sh<shader_func_acosh | cosine.              |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `ata                 | Arc hyperbolic       |
| ec_type (Any of: flo | nh<shader_func_atanh | tangent.             |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+

::: rst-class
classref-descriptions-group
:::

### Trigonometric function descriptions

:::: {#shader_func_radians}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**radians**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} degrees) `🔗<shader_func_radians>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Converts a quantity specified in degrees into radians, with the
> formula `degrees * (PI / 180)`.
>
> param degrees
> :   The quantity, in degrees, to be converted to radians.
>
> return
> :   The input `degrees` converted to radians.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/radians.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_degrees}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**degrees**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} radians) `🔗<shader_func_degrees>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Converts a quantity specified in radians into degrees, with the
> formula `radians * (180 / PI)`
>
> param radians
> :   The quantity, in radians, to be converted to degrees.
>
> return
> :   The input `radians` converted to degrees.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/degrees.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_sin}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**sin**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} angle) `🔗<shader_func_sin>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the trigonometric sine of `angle`.
>
> param angle
> :   The quantity, in radians, of which to return the sine.
>
> return
> :   The sine of `angle`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sin.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_cos}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**cos**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} angle) `🔗<shader_func_cos>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the trigonometric cosine of `angle`.
>
> param angle
> :   The quantity, in radians, of which to return the cosine.
>
> return
> :   The cosine of `angle`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cos.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_tan}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**tan**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} angle) `🔗<shader_func_tan>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the trigonometric tangent of `angle`.
>
> param angle
> :   The quantity, in radians, of which to return the tangent.
>
> return
> :   The tangent of `angle`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tan.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_asin}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**asin**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_asin>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Arc sine, or inverse sine. Calculates the angle whose sine is `x` and
> is in the range `[-PI/2, PI/2]`. The result is undefined if `x < -1`
> or `x > 1`.
>
> param x
> :   The value whose arc sine to return.
>
> return
> :   The angle whose trigonometric sine is `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asin.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_acos}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**acos**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_acos>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Arc cosine, or inverse cosine. Calculates the angle whose cosine is
> `x` and is in the range `[0, PI]`.
>
> The result is undefined if `x < -1` or `x > 1`.
>
> param x
> :   The value whose arc cosine to return.
>
> return
> :   The angle whose trigonometric cosine is `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acos.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_atan}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**atan**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y_over_x) `🔗<shader_func_atan>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Calculates the arc tangent given a tangent value of `y/x`.
>
> :::: note
> ::: title
> Note
> :::
>
> Because of the sign ambiguity, the function cannot determine with
> certainty in which quadrant the angle falls only by its tangent value.
> If you need to know the quadrant, use
> `atan(vec_type y, vec_type x)<shader_func_atan2>`{.interpreted-text
> role="ref"}.
> ::::
>
> param y_over_x
> :   The fraction whose arc tangent to return.
>
> return
> :   The trigonometric arc-tangent of `y_over_x` and is in the range
>     `[-PI/2, PI/2]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_atan2}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**atan**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_atan2>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Calculates the arc tangent given a numerator and denominator. The
> signs of `y` and `x` are used to determine the quadrant that the angle
> lies in. The result is undefined if `x == 0`.
>
> Equivalent to
> `atan2() <class_@GlobalScope_method_atan2>`{.interpreted-text
> role="ref"} in GDScript.
>
> param y
> :   The numerator of the fraction whose arc tangent to return.
>
> param x
> :   The denominator of the fraction whose arc tangent to return.
>
> return
> :   The trigonometric arc tangent of `y/x` and is in the range
>     `[-PI, PI]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atan.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_sinh}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**sinh**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_sinh>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Calculates the hyperbolic sine using `(e^x - e^-x)/2`.
>
> param x
> :   The value whose hyperbolic sine to return.
>
> return
> :   The hyperbolic sine of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sinh.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_cosh}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**cosh**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_cosh>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Calculates the hyperbolic cosine using `(e^x + e^-x)/2`.
>
> param x
> :   The value whose hyperbolic cosine to return.
>
> return
> :   The hyperbolic cosine of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cosh.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_tanh}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**tanh**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_tanh>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Calculates the hyperbolic tangent using `sinh(x)/cosh(x)`.
>
> param x
> :   The value whose hyperbolic tangent to return.
>
> return
> :   The hyperbolic tangent of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/tanh.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_asinh}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**asinh**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_asinh>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Calculates the arc hyperbolic sine of `x`, or the inverse of `sinh`.
>
> param x
> :   The value whose arc hyperbolic sine to return.
>
> return
> :   The arc hyperbolic sine of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/asinh.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_acosh}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**acosh**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_acosh>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Calculates the arc hyperbolic cosine of `x`, or the non-negative
> inverse of `cosh`. The result is undefined if `x < 1`.
>
> param x
> :   The value whose arc hyperbolic cosine to return.
>
> return
> :   The arc hyperbolic cosine of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/acosh.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_atanh}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**atanh**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_atanh>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Calculates the arc hyperbolic tangent of `x`, or the inverse of
> `tanh`. The result is undefined if `abs(x) > 1`.
>
> param x
> :   The value whose arc hyperbolic tangent to return.
>
> return
> :   The arc hyperbolic tangent of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/atanh.xhtml>

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-reftable-group
:::

## Exponential and math functions

+----------------------+----------------------+----------------------+
| > Return Type        | Function             | Description / Return |
|                      |                      | value                |
+======================+======================+======================+
| `v                   | `pow<shader_func_pow | Power (undefined if  |
| ec_type (Any of: flo | >`{.interpreted-text | `x < 0` or if        |
| at, vec2, vec3, vec4 | role="ref"}(`v       | `x == 0` and         |
| )`{.interpreted-text | ec_type (Any of: flo | `y <= 0`).           |
| role="abbr"}         | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x,      |                      |
|                      | `v                   |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} y)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `exp<shader_func_exp | Base-e exponential.  |
| ec_type (Any of: flo | >`{.interpreted-text |                      |
| at, vec2, vec3, vec4 | role="ref"}(`v       |                      |
| )`{.interpreted-text | ec_type (Any of: flo |                      |
| role="abbr"}         | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `e                   | Base-2 exponential.  |
| ec_type (Any of: flo | xp2<shader_func_exp2 |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `log<shader_func_log | Natural (base-e)     |
| ec_type (Any of: flo | >`{.interpreted-text | logarithm.           |
| at, vec2, vec3, vec4 | role="ref"}(`v       |                      |
| )`{.interpreted-text | ec_type (Any of: flo |                      |
| role="abbr"}         | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `l                   | Base-2 logarithm.    |
| ec_type (Any of: flo | og2<shader_func_log2 |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `s                   | Square root.         |
| ec_type (Any of: flo | qrt<shader_func_sqrt |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `inversesqrt<sha     | Inverse square root. |
| ec_type (Any of: flo | der_func_inversesqrt |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| | `v                 | |                    | Absolute value       |
| ec_type (Any of: flo | `abs<shader_func_abs | (returns positive    |
| at, vec2, vec3, vec4 | >`{.interpreted-text | value if negative).  |
| )`{.interpreted-text |   role="ref"}(`v     |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `vec_in            | at, vec2, vec3, vec4 |                      |
| t_type (Any of: int, | )`{.interpreted-text |                      |
|  ivec2, ivec3, ivec4 |   role="abbr"} x)    |                      |
| )`{.interpreted-text | |                    |                      |
|   role="abbr"}       | `abs<shader_func_abs |                      |
|                      | >`{.interpreted-text |                      |
|                      |                      |                      |
|                      |  role="ref"}(`vec_in |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} x)    |                      |
+----------------------+----------------------+----------------------+
| `v                   | `s                   | Returns `1.0` if     |
| ec_type (Any of: flo | ign<shader_func_sign | positive, `-1.0` if  |
| at, vec2, vec3, vec4 | >`{.interpreted-text | negative, `0.0`      |
| )`{.interpreted-text | role="ref"}(`v       | otherwise.           |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `vec_in              | `s                   | Returns `1` if       |
| t_type (Any of: int, | ign<shader_func_sign | positive, `-1` if    |
|  ivec2, ivec3, ivec4 | >`{.interpreted-text | negative, `0`        |
| )`{.interpreted-text | role="ref"}(`vec_in  | otherwise.           |
| role="abbr"}         | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `flo                 | Rounds to the        |
| ec_type (Any of: flo | or<shader_func_floor | integer below.       |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `rou                 | Rounds to the        |
| ec_type (Any of: flo | nd<shader_func_round | nearest integer.     |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `roundEven<s         | Rounds to the        |
| ec_type (Any of: flo | hader_func_roundEven | nearest even         |
| at, vec2, vec3, vec4 | >`{.interpreted-text | integer.             |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `tru                 | Truncation.          |
| ec_type (Any of: flo | nc<shader_func_trunc |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `c                   | Rounds to the        |
| ec_type (Any of: flo | eil<shader_func_ceil | integer above.       |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `fra                 | Fractional (returns  |
| ec_type (Any of: flo | ct<shader_func_fract | `x - floor(x)`).     |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| | `v                 | |                    | Modulo (division     |
| ec_type (Any of: flo | `mod<shader_func_mod | remainder).          |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text |   role="ref"}(`v     |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `v                 | at, vec2, vec3, vec4 |                      |
| ec_type (Any of: flo | )`{.interpreted-text |                      |
| at, vec2, vec3, vec4 |   role="abbr"} x,    |                      |
| )`{.interpreted-text |   `v                 |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} y)    |                      |
|                      | |                    |                      |
|                      | `mod<shader_func_mod |                      |
|                      | >`{.interpreted-text |                      |
|                      |   role="ref"}(`v     |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} x,    |                      |
|                      |   float y)           |                      |
+----------------------+----------------------+----------------------+
| `v                   | `m                   | Fractional of `x`,   |
| ec_type (Any of: flo | odf<shader_func_modf | with `i` as integer  |
| at, vec2, vec3, vec4 | >`{.interpreted-text | part.                |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x, out  |                      |
|                      | `v                   |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} i)      |                      |
+----------------------+----------------------+----------------------+
| | `v                 | |                    | Lowest value between |
| ec_type (Any of: flo | `min<shader_func_min | `a` and `b`.         |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text |   role="ref"}(`v     |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `v                 | at, vec2, vec3, vec4 |                      |
| ec_type (Any of: flo | )`{.interpreted-text |                      |
| at, vec2, vec3, vec4 |   role="abbr"} a,    |                      |
| )`{.interpreted-text |   `v                 |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `vec_in            | at, vec2, vec3, vec4 |                      |
| t_type (Any of: int, | )`{.interpreted-text |                      |
|  ivec2, ivec3, ivec4 |   role="abbr"} b)    |                      |
| )`{.interpreted-text | |                    |                      |
|   role="abbr"}       | `min<shader_func_min |                      |
| | `vec_in            | >`{.interpreted-text |                      |
| t_type (Any of: int, |   role="ref"}(`v     |                      |
|  ivec2, ivec3, ivec4 | ec_type (Any of: flo |                      |
| )`{.interpreted-text | at, vec2, vec3, vec4 |                      |
|   role="abbr"}       | )`{.interpreted-text |                      |
| | `vec_uint_         |   role="abbr"} a,    |                      |
| type (Any of: float, |   float b)           |                      |
|  uvec2, uvec3, uvec4 | |                    |                      |
| )`{.interpreted-text | `min<shader_func_min |                      |
|   role="abbr"}       | >`{.interpreted-text |                      |
| | `vec_uint_         |                      |                      |
| type (Any of: float, |  role="ref"}(`vec_in |                      |
|  uvec2, uvec3, uvec4 | t_type (Any of: int, |                      |
| )`{.interpreted-text |  ivec2, ivec3, ivec4 |                      |
|   role="abbr"}       | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   `vec_in            |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} b)    |                      |
|                      | |                    |                      |
|                      | `min<shader_func_min |                      |
|                      | >`{.interpreted-text |                      |
|                      |                      |                      |
|                      |  role="ref"}(`vec_in |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   int b)             |                      |
|                      | |                    |                      |
|                      | `min<shader_func_min |                      |
|                      | >`{.interpreted-text |                      |
|                      |   ro                 |                      |
|                      | le="ref"}(`vec_uint_ |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   `vec_uint_         |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} b)    |                      |
|                      | |                    |                      |
|                      | `min<shader_func_min |                      |
|                      | >`{.interpreted-text |                      |
|                      |   ro                 |                      |
|                      | le="ref"}(`vec_uint_ |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   uint b)            |                      |
+----------------------+----------------------+----------------------+
| | `v                 | |                    | Highest value        |
| ec_type (Any of: flo | `max<shader_func_max | between `a` and `b`. |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text |   role="ref"}(`v     |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `v                 | at, vec2, vec3, vec4 |                      |
| ec_type (Any of: flo | )`{.interpreted-text |                      |
| at, vec2, vec3, vec4 |   role="abbr"} a,    |                      |
| )`{.interpreted-text |   `v                 |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `vec_in            | at, vec2, vec3, vec4 |                      |
| t_type (Any of: int, | )`{.interpreted-text |                      |
|  ivec2, ivec3, ivec4 |   role="abbr"} b)    |                      |
| )`{.interpreted-text | |                    |                      |
|   role="abbr"}       | `max<shader_func_max |                      |
| | `vec_in            | >`{.interpreted-text |                      |
| t_type (Any of: int, |   role="ref"}(`v     |                      |
|  ivec2, ivec3, ivec4 | ec_type (Any of: flo |                      |
| )`{.interpreted-text | at, vec2, vec3, vec4 |                      |
|   role="abbr"}       | )`{.interpreted-text |                      |
| | `vec_uint_         |   role="abbr"} a,    |                      |
| type (Any of: float, |   float b)           |                      |
|  uvec2, uvec3, uvec4 | |                    |                      |
| )`{.interpreted-text | `max<shader_func_max |                      |
|   role="abbr"}       | >`{.interpreted-text |                      |
| | `vec_uint_         |                      |                      |
| type (Any of: float, |  role="ref"}(`vec_in |                      |
|  uvec2, uvec3, uvec4 | t_type (Any of: int, |                      |
| )`{.interpreted-text |  ivec2, ivec3, ivec4 |                      |
|   role="abbr"}       | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   `vec_in            |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} b)    |                      |
|                      | |                    |                      |
|                      | `max<shader_func_max |                      |
|                      | >`{.interpreted-text |                      |
|                      |                      |                      |
|                      |  role="ref"}(`vec_in |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   int b)             |                      |
|                      | |                    |                      |
|                      | `max<shader_func_max |                      |
|                      | >`{.interpreted-text |                      |
|                      |   ro                 |                      |
|                      | le="ref"}(`vec_uint_ |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   `vec_uint_         |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} b)    |                      |
|                      | |                    |                      |
|                      | `max<shader_func_max |                      |
|                      | >`{.interpreted-text |                      |
|                      |   ro                 |                      |
|                      | le="ref"}(`vec_uint_ |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   uint b)            |                      |
+----------------------+----------------------+----------------------+
| | `v                 | | `cla               | Clamps `x` between   |
| ec_type (Any of: flo | mp<shader_func_clamp | `min` and `max`      |
| at, vec2, vec3, vec4 | >`{.interpreted-text | (inclusive).         |
| )`{.interpreted-text |   role="ref"}(`v     |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `v                 | at, vec2, vec3, vec4 |                      |
| ec_type (Any of: flo | )`{.interpreted-text |                      |
| at, vec2, vec3, vec4 |   role="abbr"} x,    |                      |
| )`{.interpreted-text |   `v                 |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `vec_in            | at, vec2, vec3, vec4 |                      |
| t_type (Any of: int, | )`{.interpreted-text |                      |
|  ivec2, ivec3, ivec4 |   role="abbr"} min,  |                      |
| )`{.interpreted-text |   `v                 |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `vec_in            | at, vec2, vec3, vec4 |                      |
| t_type (Any of: int, | )`{.interpreted-text |                      |
|  ivec2, ivec3, ivec4 |   role="abbr"} max)  |                      |
| )`{.interpreted-text | | `cla               |                      |
|   role="abbr"}       | mp<shader_func_clamp |                      |
| | `vec_uint_         | >`{.interpreted-text |                      |
| type (Any of: float, |   role="ref"}(`v     |                      |
|  uvec2, uvec3, uvec4 | ec_type (Any of: flo |                      |
| )`{.interpreted-text | at, vec2, vec3, vec4 |                      |
|   role="abbr"}       | )`{.interpreted-text |                      |
| | `vec_uint_         |   role="abbr"} x,    |                      |
| type (Any of: float, |   float min, float   |                      |
|  uvec2, uvec3, uvec4 |   max)               |                      |
| )`{.interpreted-text | | `cla               |                      |
|   role="abbr"}       | mp<shader_func_clamp |                      |
|                      | >`{.interpreted-text |                      |
|                      |                      |                      |
|                      |  role="ref"}(`vec_in |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} x,    |                      |
|                      |   `vec_in            |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} min,  |                      |
|                      |   `vec_in            |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} max)  |                      |
|                      | | `cla               |                      |
|                      | mp<shader_func_clamp |                      |
|                      | >`{.interpreted-text |                      |
|                      |                      |                      |
|                      |  role="ref"}(`vec_in |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} x,    |                      |
|                      |   int min, int max)  |                      |
|                      | | `cla               |                      |
|                      | mp<shader_func_clamp |                      |
|                      | >`{.interpreted-text |                      |
|                      |   ro                 |                      |
|                      | le="ref"}(`vec_uint_ |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} x,    |                      |
|                      |   `vec_uint_         |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} min,  |                      |
|                      |   `vec_uint_         |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} max)  |                      |
|                      | | `cla               |                      |
|                      | mp<shader_func_clamp |                      |
|                      | >`{.interpreted-text |                      |
|                      |   ro                 |                      |
|                      | le="ref"}(`vec_uint_ |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} x,    |                      |
|                      |   uint min, uint     |                      |
|                      |   max)               |                      |
+----------------------+----------------------+----------------------+
| | `v                 | |                    | Linear interpolate   |
| ec_type (Any of: flo | `mix<shader_func_mix | between `a` and `b`  |
| at, vec2, vec3, vec4 | >`{.interpreted-text | by `c`.              |
| )`{.interpreted-text |   role="ref"}(`v     |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `v                 | at, vec2, vec3, vec4 |                      |
| ec_type (Any of: flo | )`{.interpreted-text |                      |
| at, vec2, vec3, vec4 |   role="abbr"} a,    |                      |
| )`{.interpreted-text |   `v                 |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `v                 | at, vec2, vec3, vec4 |                      |
| ec_type (Any of: flo | )`{.interpreted-text |                      |
| at, vec2, vec3, vec4 |   role="abbr"} b,    |                      |
| )`{.interpreted-text |   `v                 |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} c)    |                      |
|                      | |                    |                      |
|                      | `mix<shader_func_mix |                      |
|                      | >`{.interpreted-text |                      |
|                      |   role="ref"}(`v     |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   `v                 |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} b,    |                      |
|                      |   float c)           |                      |
|                      | |                    |                      |
|                      | `mix<shader_func_mix |                      |
|                      | >`{.interpreted-text |                      |
|                      |   role="ref"}(`v     |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} a,    |                      |
|                      |   `v                 |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} b,    |                      |
|                      |   `vec_bool          |                      |
|                      | _type (Any of: bool, |                      |
|                      |  bvec2, bvec3, bvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} c)    |                      |
+----------------------+----------------------+----------------------+
| `v                   | `fma<shader_func_fma | Fused multiply-add   |
| ec_type (Any of: flo | >`{.interpreted-text | operation:           |
| at, vec2, vec3, vec4 | role="ref"}(`v       | `(a * b + c)`        |
| )`{.interpreted-text | ec_type (Any of: flo |                      |
| role="abbr"}         | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} a,      |                      |
|                      | `v                   |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} b,      |                      |
|                      | `v                   |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} c)      |                      |
+----------------------+----------------------+----------------------+
| | `v                 | | `s                 | `b < a ? 0.0 : 1.0`  |
| ec_type (Any of: flo | tep<shader_func_step |                      |
| at, vec2, vec3, vec4 | >`{.interpreted-text |                      |
| )`{.interpreted-text |   role="ref"}(`v     |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `v                 | at, vec2, vec3, vec4 |                      |
| ec_type (Any of: flo | )`{.interpreted-text |                      |
| at, vec2, vec3, vec4 |   role="abbr"} a,    |                      |
| )`{.interpreted-text |   `v                 |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} b)    |                      |
|                      | | `s                 |                      |
|                      | tep<shader_func_step |                      |
|                      | >`{.interpreted-text |                      |
|                      |   role="ref"}(float  |                      |
|                      |   a,                 |                      |
|                      |   `v                 |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} b)    |                      |
+----------------------+----------------------+----------------------+
| | `v                 | | `smoothstep<sh     | Hermite interpolate  |
| ec_type (Any of: flo | ader_func_smoothstep | between `a` and `b`  |
| at, vec2, vec3, vec4 | >`{.interpreted-text | by `c`.              |
| )`{.interpreted-text |   role="ref"}(`v     |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
| | `v                 | at, vec2, vec3, vec4 |                      |
| ec_type (Any of: flo | )`{.interpreted-text |                      |
| at, vec2, vec3, vec4 |   role="abbr"} a,    |                      |
| )`{.interpreted-text |   `v                 |                      |
|   role="abbr"}       | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} b,    |                      |
|                      |   `v                 |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} c)    |                      |
|                      | | `smoothstep<sh     |                      |
|                      | ader_func_smoothstep |                      |
|                      | >`{.interpreted-text |                      |
|                      |   role="ref"}(float  |                      |
|                      |   a, float b,        |                      |
|                      |   `v                 |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      |   role="abbr"} c)    |                      |
+----------------------+----------------------+----------------------+
| `vec_bool            | `isn                 | Returns `true` if    |
| _type (Any of: bool, | an<shader_func_isnan | scalar or vector     |
|  bvec2, bvec3, bvec4 | >`{.interpreted-text | component is `NaN`.  |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `vec_bool            | `isi                 | Returns `true` if    |
| _type (Any of: bool, | nf<shader_func_isinf | scalar or vector     |
|  bvec2, bvec3, bvec4 | >`{.interpreted-text | component is `INF`.  |
| )`{.interpreted-text | role="ref"}(`v       |                      |
| role="abbr"}         | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `vec_in              | `f                   | `float` to `int` bit |
| t_type (Any of: int, | loatBitsToInt<shader | copying, no          |
|  ivec2, ivec3, ivec4 | _func_floatBitsToInt | conversion.          |
| )`{.interpreted-text | >`{.interpreted-text |                      |
| role="abbr"}         | role="ref"}(`v       |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `vec_uint_           | `flo                 | `float` to `uint`    |
| type (Any of: float, | atBitsToUint<shader_ | bit copying, no      |
|  uvec2, uvec3, uvec4 | func_floatBitsToUint | conversion.          |
| )`{.interpreted-text | >`{.interpreted-text |                      |
| role="abbr"}         | role="ref"}(`v       |                      |
|                      | ec_type (Any of: flo |                      |
|                      | at, vec2, vec3, vec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `i                   | `int` to `float` bit |
| ec_type (Any of: flo | ntBitsToFloat<shader | copying, no          |
| at, vec2, vec3, vec4 | _func_intBitsToFloat | conversion.          |
| )`{.interpreted-text | >`{.interpreted-text |                      |
| role="abbr"}         | role="ref"}(`vec_in  |                      |
|                      | t_type (Any of: int, |                      |
|                      |  ivec2, ivec3, ivec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+
| `v                   | `uin                 | `uint` to `float`    |
| ec_type (Any of: flo | tBitsToFloat<shader_ | bit copying, no      |
| at, vec2, vec3, vec4 | func_uintBitsToFloat | conversion.          |
| )`{.interpreted-text | >`{.interpreted-text |                      |
| role="abbr"}         | ro                   |                      |
|                      | le="ref"}(`vec_uint_ |                      |
|                      | type (Any of: float, |                      |
|                      |  uvec2, uvec3, uvec4 |                      |
|                      | )`{.interpreted-text |                      |
|                      | role="abbr"} x)      |                      |
+----------------------+----------------------+----------------------+

::: rst-class
classref-descriptions-group
:::

### Exponential and math function descriptions

:::: {#shader_func_pow}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**pow**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y) `🔗<shader_func_pow>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Raises `x` to the power of `y`.
>
> The result is undefined if `x < 0` or if `x == 0` and `y <= 0`.
>
> param x
> :   The value to be raised to the power `y`.
>
> param y
> :   The power to which `x` will be raised.
>
> return
> :   The value of `x` raised to the `y` power.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/pow.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_exp}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**exp**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_exp>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Raises `e` to the power of `x`, or the the natural exponentiation.
>
> Equivalent to `pow(e, x)`.
>
> param x
> :   The value to exponentiate.
>
> return
> :   The natural exponentiation of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_exp2}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**exp2**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_exp2>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Raises `2` to the power of `x`.
>
> Equivalent to `pow(2.0, x)`.
>
> param x
> :   The value of the power to which `2` will be raised.
>
> return
> :   `2` raised to the power of x.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/exp2.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_log}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**log**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_log>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the natural logarithm of `x`, i.e. the value `y` which
> satisfies `x == pow(e, y)`. The result is undefined if `x <= 0`.
>
> param x
> :   The value of which to take the natural logarithm.
>
> return
> :   The natural logarithm of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_log2}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**log2**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_log2>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the base-2 logarithm of `x`, i.e. the value `y` which
> satisfies `x == pow(2, y)`. The result is undefined if `x <= 0`.
>
> param x
> :   The value of which to take the base-2 logarithm.
>
> return
> :   The base-2 logarithm of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/log2.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_sqrt}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**sqrt**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_sqrt>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the square root of `x`. The result is undefined if `x < 0`.
>
> param x
> :   The value of which to take the square root.
>
> return
> :   The square root of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sqrt.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_inversesqrt}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**inversesqrt**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_inversesqrt>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the inverse of the square root of `x`, or `1.0 / sqrt(x)`. The
> result is undefined if `x <= 0`.
>
> param x
> :   The value of which to take the inverse of the square root.
>
> return
> :   The inverse of the square root of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inversesqrt.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_abs}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**abs**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_abs>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**abs**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_abs>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the absolute value of `x`. Returns `x` if `x` is positive,
> otherwise returns `-1 * x`.
>
> param x
> :   The value of which to return the absolute.
>
> return
> :   The absolute value of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/abs.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_sign}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**sign**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_sign>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**sign**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_sign>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns `-1` if `x < 0`, `0` if `x == 0`, and `1` if `x > 0`.
>
> param x
> :   The value from which to extract the sign.
>
> return
> :   The sign of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/sign.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_floor}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**floor**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_floor>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns a value equal to the nearest integer that is less than or
> equal to `x`.
>
> param x
> :   The value to floor.
>
> return
> :   The nearest integer that is less than or equal to `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floor.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_round}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**round**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_round>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Rounds `x` to the nearest integer.
>
> :::: note
> ::: title
> Note
> :::
>
> Rounding of values with a fractional part of `0.5` is
> implementation-dependent. This includes the possibility that
> `round(x)` returns the same value as `roundEven(x)`for all values of
> `x`.
> ::::
>
> param x
> :   The value to round.
>
> return
> :   The rounded value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/round.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_roundEven}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**roundEven**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_roundEven>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Rounds `x` to the nearest integer. A value with a fractional part of
> `0.5` will always round toward the nearest even integer. For example,
> both `3.5` and `4.5` will round to `4.0`.
>
> param x
> :   The value to round.
>
> return
> :   The rounded value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/roundEven.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_trunc}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**trunc**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_trunc>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Truncates `x`. Returns a value equal to the nearest integer to `x`
> whose absolute value is not larger than the absolute value of `x`.
>
> param x
> :   The value to evaluate.
>
> return
> :   The truncated value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/trunc.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_ceil}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**ceil**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_ceil>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns a value equal to the nearest integer that is greater than or
> equal to `x`.
>
> param x
> :   The value to evaluate.
>
> return
> :   The ceiling-ed value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ceil.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_fract}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**fract**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_fract>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the fractional part of `x`.
>
> This is calculated as `x - floor(x)`.
>
> param x
> :   The value to evaluate.
>
> return
> :   The fractional part of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fract.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_mod}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**mod**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y) `🔗<shader_func_mod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**mod**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x, float y) `🔗<shader_func_mod>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the value of `x modulo y`. This is also sometimes called the
> remainder.
>
> This is computed as `x - y * floor(x/y)`.
>
> param x
> :   The value to evaluate.
>
> return
> :   The value of `x modulo y`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mod.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_modf}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**modf**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x, out
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} i) `🔗<shader_func_modf>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Separates a floating-point value `x` into its integer and fractional
> parts.
>
> The fractional part of the number is returned from the function. The
> integer part (as a floating-point quantity) is returned in the output
> parameter `i`.
>
> param x
> :   The value to separate.
>
> param out i
> :   A variable that receives the integer part of `x`.
>
> return
> :   The fractional part of the number.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/modf.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_min}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**min**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_min>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**min**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a, float b) `🔗<shader_func_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**min**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} a,
`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_min>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**min**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} a, int b) `🔗<shader_func_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**min**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} a,
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_min>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**min**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} a, uint b) `🔗<shader_func_min>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the minimum of two values `a` and `b`.
>
> Returns `b` if `b < a`, otherwise returns `a`.
>
> param a
> :   The first value to compare.
>
> param b
> :   The second value to compare.
>
> return
> :   The minimum value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/min.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_max}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**max**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_max>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**max**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a, float b) `🔗<shader_func_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**max**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} a,
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_max>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**max**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} a, uint b) `🔗<shader_func_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**max**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} a,
`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_max>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**max**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} a, int b) `🔗<shader_func_max>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the maximum of two values `a` and `b`.
>
> It returns `b` if `b > a`, otherwise it returns `a`.
>
> param a
> :   The first value to compare.
>
> param b
> :   The second value to compare.
>
> return
> :   The maximum value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/max.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_clamp}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**clamp**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} minVal,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} maxVal) `🔗<shader_func_clamp>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**clamp**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x, float minVal, float maxVal)
`🔗<shader_func_clamp>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**clamp**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} x,
`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} minVal,
`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} maxVal) `🔗<shader_func_clamp>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**clamp**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} x, int minVal, int maxVal)
`🔗<shader_func_clamp>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**clamp**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} x,
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} minVal,
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} maxVal) `🔗<shader_func_clamp>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**clamp**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} x, uint minVal, uint maxVal)
`🔗<shader_func_clamp>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the value of `x` constrained to the range `minVal` to
> `maxVal`.
>
> The returned value is computed as `min(max(x, minVal), maxVal)`.
>
> param x
> :   The value to constrain.
>
> param minVal
> :   The lower end of the range into which to constrain `x`.
>
> param maxVal
> :   The upper end of the range into which to constrain `x`.
>
> return
> :   The clamped value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/clamp.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_mix}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**mix**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} c) `🔗<shader_func_mix>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**mix**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b, float c) `🔗<shader_func_mix>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Performs a linear interpolation between `a` and `b` using `c` to
> weight between them.
>
> Computed as `a * (1 - c) + b * c`.
>
> Equivalent to
> `lerp() <class_@GlobalScope_method_lerp>`{.interpreted-text
> role="ref"} in GDScript.
>
> param a
> :   The start of the range in which to interpolate.
>
> param b
> :   The end of the range in which to interpolate.
>
> param c
> :   The value to use to interpolate between `a` and `b`.
>
> return
> :   The interpolated value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-method
:::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**mix**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b,
`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"} c) `🔗<shader_func_mix>`{.interpreted-text role="ref"}

> Selects either value `a` or value `b` based on the value of `c`. For a
> component of `c` that is false, the corresponding component of `a` is
> returned. For a component of `c` that is true, the corresponding
> component of `b` is returned. Components of `a` and `b` that are not
> selected are allowed to be invalid floating-point values and will have
> no effect on the results.
>
> If `a`, `b`, and `c` are vector types the operation is performed
> `component-wise <shading_componentwise>`{.interpreted-text
> role="ref"}. ie.
> `mix(vec2(42, 314), vec2(9.8, 6e23), bvec2(true, false)))` will return
> `vec2(9.8, 314)`.
>
> param a
> :   Value returned when `c` is false.
>
> param b
> :   Value returned when `c` is true.
>
> param c
> :   The value used to select between `a` and `b`.
>
> return
> :   The interpolated value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/mix.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_fma}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**fma**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} c) `🔗<shader_func_fma>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Performs, where possible, a fused multiply-add operation, returning
> `a * b + c`. In use cases where the return value is eventually
> consumed by a variable declared as precise:
>
> > - `fma()` is considered a single operation, whereas the expression
> >   `a * b + c` consumed by a variable declared as precise is
> >   considered two operations.
> > - The precision of `fma()` can differ from the precision of the
> >   expression `a * b + c`.
> > - `fma()` will be computed with the same precision as any other
> >   `fma()` consumed by a precise variable, giving invariant results
> >   for the same input values of a, b and c.
>
> Otherwise, in the absence of precise consumption, there are no special
> constraints on the number of operations or difference in precision
> between `fma()` and the expression `a * b + c`.
>
> param a
> :   The first value to be multiplied.
>
> param b
> :   The second value to be multiplied.
>
> param c
> :   The value to be added to the result.
>
> return
> :   The value of `a * b + c`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fma.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_step}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**step**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_step>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} **step**(float a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_step>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Generates a step function by comparing b to a.
>
> Equivalent to `if (b < a) { return 0.0; } else { return 1.0; }`. For
> element i of the return value, 0.0 is returned if b\[i\] \< a\[i\],
> and 1.0 is returned otherwise.
>
> param a
> :   The location of the edge of the step function.
>
> param b
> :   The value to be used to generate the step function.
>
> return
> :   `0.0` or `1.0`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/step.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_smoothstep}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**smoothstep**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} c) `🔗<shader_func_smoothstep>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} **smoothstep**(float a, float b,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} c) `🔗<shader_func_smoothstep>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Performs smooth Hermite interpolation between `0` and `1` when a \< c
> \< b. This is useful in cases where a threshold function with a smooth
> transition is desired.
>
> Smoothstep is equivalent to:
>
>     vec_type t;
>     t = clamp((c - a) / (b - a), 0.0, 1.0);
>     return t * t * (3.0 - 2.0 * t);
>
> Results are undefined if `a >= b`.
>
> param a
> :   The value of the lower edge of the Hermite function.
>
> param b
> :   The value of the upper edge of the Hermite function.
>
> param c
> :   The source value for interpolation.
>
> return
> :   The interpolated value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/smoothstep.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_isnan}
::: rst-class
classref-method
:::
::::

`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"}
**isnan**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_isnan>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> For each element i of the result, returns `true` if x\[i\] is positive
> or negative floating-point NaN (Not a Number) and false otherwise.
>
> param x
> :   The value to test for NaN.
>
> return
> :   `true` or `false`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isnan.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_isinf}
::: rst-class
classref-method
:::
::::

`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"}
**isinf**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_isinf>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> For each element i of the result, returns `true` if x\[i\] is positive
> or negative floating-point infinity and false otherwise.
>
> param x
> :   The value to test for infinity.
>
> return
> :   `true` or `false`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/isinf.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_floatBitsToInt}
::: rst-class
classref-method
:::
::::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**floatBitsToInt**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_floatBitsToInt>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the encoding of the floating-point parameters as `int`.
>
> The floating-point bit-level representation is preserved.
>
> param x
> :   The value whose floating-point encoding to return.
>
> return
> :   The floating-point encoding of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_floatBitsToUint}
::: rst-class
classref-method
:::
::::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**floatBitsToUint**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_floatBitsToUint>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Returns the encoding of the floating-point parameters as `uint`.
>
> The floating-point bit-level representation is preserved.
>
> param x
> :   The value whose floating-point encoding to return.
>
> return
> :   The floating-point encoding of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/floatBitsToInt.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_intBitsToFloat}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**intBitsToFloat**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_intBitsToFloat>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Converts a bit encoding to a floating-point value. Opposite of
> [floatBitsToInt\<shader_func_floatBitsToInt\>]{.title-ref}
>
> If the encoding of a `NaN` is passed in `x`, it will not signal and
> the resulting value will be undefined.
>
> If the encoding of a floating-point infinity is passed in parameter
> `x`, the resulting floating-point value is the corresponding (positive
> or negative) floating-point infinity.
>
> param x
> :   The bit encoding to return as a floating-point value.
>
> return
> :   A floating-point value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_uintBitsToFloat}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**uintBitsToFloat**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_uintBitsToFloat>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Converts a bit encoding to a floating-point value. Opposite of
> [floatBitsToUint\<shader_func_floatBitsToUint\>]{.title-ref}
>
> If the encoding of a `NaN` is passed in `x`, it will not signal and
> the resulting value will be undefined.
>
> If the encoding of a floating-point infinity is passed in parameter
> `x`, the resulting floating-point value is the corresponding (positive
> or negative) floating-point infinity.
>
> param x
> :   The bit encoding to return as a floating-point value.
>
> return
> :   A floating-point value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/intBitsToFloat.xhtml>

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-reftable-group
:::

## Geometric functions

::: rst-class
classref-descriptions-group
:::

### Geometric function descriptions

:::: {#shader_func_length}
::: rst-class
classref-method
:::
::::

float
**length**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_length>`{.interpreted-text role="ref"}

> Returns the length of the vector. ie.
> `sqrt(x[0] * x[0] + x[1] * x[1] + ... + x[n] * x[n])`
>
> param x
> :   The vector
>
> return
> :   The length of the vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/length.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_distance}
::: rst-class
classref-method
:::
::::

float
**distance**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_distance>`{.interpreted-text role="ref"}

> Returns the distance between the two points a and b.
>
> i.e., `length(b - a);`
>
> param a
> :   The first point.
>
> param b
> :   The second point.
>
> return
> :   The scalar distance between the points
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/distance.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_dot}
::: rst-class
classref-method
:::
::::

float
**dot**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} a,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} b) `🔗<shader_func_dot>`{.interpreted-text role="ref"}

> Returns the dot product of two vectors, `a` and `b`. i.e.,
> `a.x * b.x + a.y * b.y + ...`
>
> param a
> :   The first vector.
>
> param b
> :   The second vector.
>
> return
> :   The dot product.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dot.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_cross}
::: rst-class
classref-method
:::
::::

vec3 **cross**(vec3 a, vec3 b) `🔗<shader_func_cross>`{.interpreted-text
role="ref"}

> Returns the cross product of two vectors. i.e.:
>
>     vec2( a.y * b.z - b.y * a.z,
>           a.z * b.x - b.z * a.x,
>           a.x * b.z - b.x * a.y)
>
> param a
> :   The first vector.
>
> param b
> :   The second vector.
>
> return
> :   The cross product of `a` and `b`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/cross.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_normalize}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**normalize**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_normalize>`{.interpreted-text
role="ref"}

> Returns a vector with the same direction as `x` but with length `1.0`.
>
> param x
> :   The vector to normalize.
>
> return
> :   The normalized vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/normalize.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_reflect}
::: rst-class
classref-method
:::
::::

vec3 **reflect**(vec3 I, vec3 N)
`🔗<shader_func_reflect>`{.interpreted-text role="ref"}

> Calculate the reflection direction for an incident vector.
>
> For a given incident vector `I` and surface normal `N` reflect returns
> the reflection direction calculated as `I - 2.0 * dot(N, I) * N`.
>
> :::: note
> ::: title
> Note
> :::
>
> `N` should be normalized in order to achieve the desired result.
> ::::
>
> param I
> :   The incident vector.
>
> param N
> :   The normal vector.
>
> return
> :   The reflection vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/reflect.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_refract}
::: rst-class
classref-method
:::
::::

vec3 **refract**(vec3 I, vec3 N, float eta)
`🔗<shader_func_refract>`{.interpreted-text role="ref"}

> Calculate the refraction direction for an incident vector.
>
> For a given incident vector `I`, surface normal `N` and ratio of
> indices of refraction, `eta`, refract returns the refraction vector,
> `R`.
>
> `R` is calculated as:
>
>     k = 1.0 - eta * eta * (1.0 - dot(N, I) * dot(N, I));
>     if (k < 0.0)
>         R = genType(0.0);       // or genDType(0.0)
>     else
>         R = eta * I - (eta * dot(N, I) + sqrt(k)) * N;
>
> :::: note
> ::: title
> Note
> :::
>
> The input parameters I and N should be normalized in order to achieve
> the desired result.
> ::::
>
> param I
> :   The incident vector.
>
> param N
> :   The normal vector.
>
> param eta
> :   The ratio of indices of refraction.
>
> return
> :   The refraction vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/refract.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_faceforward}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**faceforward**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} N,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} I,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} Nref) `🔗<shader_func_faceforward>`{.interpreted-text
role="ref"}

> Returns a vector pointing in the same direction as another.
>
> Orients a vector to point away from a surface as defined by its
> normal. If `dot(Nref, I) < 0` faceforward returns `N`, otherwise it
> returns `-N`.
>
> param N
> :   The vector to orient.
>
> param I
> :   The incident vector.
>
> param Nref
> :   The reference vector.
>
> return
> :   The oriented vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/faceforward.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_matrixCompMult}
::: rst-class
classref-method
:::
::::

`mat_type (Any of: mat2, mat3, mat4)`{.interpreted-text role="abbr"}
**matrixCompMult**(`mat_type (Any of: mat2, mat3, mat4)`{.interpreted-text
role="abbr"} x, `mat_type (Any of: mat2, mat3, mat4)`{.interpreted-text
role="abbr"} y) `🔗<shader_func_matrixCompMult>`{.interpreted-text
role="ref"}

> Perform a `component-wise <shading_componentwise>`{.interpreted-text
> role="ref"} multiplication of two matrices.
>
> Performs a component-wise multiplication of two matrices, yielding a
> result matrix where each component, `result[i][j]` is computed as the
> scalar product of `x[i][j]` and `y[i][j]`.
>
> param x
> :   The first matrix multiplicand.
>
> param y
> :   The second matrix multiplicand.
>
> return
> :   The resultant matrix.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/matrixCompMult.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_outerProduct}
::: rst-class
classref-method
:::
::::

`mat_type (Any of: mat2, mat3, mat4)`{.interpreted-text role="abbr"}
**outerProduct**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} column,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} row) `🔗<shader_func_outerProduct>`{.interpreted-text
role="ref"}

> Calculate the outer product of a pair of vectors.
>
> Does a linear algebraic matrix multiply `column * row`, yielding a
> matrix whose number of rows is the number of components in `column`
> and whose number of columns is the number of components in `row`.
>
> param column
> :   The column vector for multiplication.
>
> param row
> :   The row vector for multiplication.
>
> return
> :   The outer product matrix.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/outerProduct.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_transpose}
::: rst-class
classref-method
:::
::::

`mat_type (Any of: mat2, mat3, mat4)`{.interpreted-text role="abbr"}
**transpose**(`mat_type (Any of: mat2, mat3, mat4)`{.interpreted-text
role="abbr"} m) `🔗<shader_func_transpose>`{.interpreted-text
role="ref"}

> Calculate the transpose of a matrix.
>
> param m
> :   The matrix to transpose.
>
> return
> :   A new matrix that is the transpose of the input matrix `m`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/transpose.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_determinant}
::: rst-class
classref-method
:::
::::

float
**determinant**(`mat_type (Any of: mat2, mat3, mat4)`{.interpreted-text
role="abbr"} m) `🔗<shader_func_determinant>`{.interpreted-text
role="ref"}

> Calculate the determinant of a matrix.
>
> param m
> :   The matrix.
>
> return
> :   The determinant of the input matrix `m`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/determinant.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_inverse}
::: rst-class
classref-method
:::
::::

`mat_type (Any of: mat2, mat3, mat4)`{.interpreted-text role="abbr"}
**inverse**(`mat_type (Any of: mat2, mat3, mat4)`{.interpreted-text
role="abbr"} m) `🔗<shader_func_inverse>`{.interpreted-text role="ref"}

> Calculate the inverse of a matrix.
>
> The values in the returned matrix are undefined if `m` is singular or
> poorly-conditioned (nearly singular).
>
> param m
> :   The matrix of which to take the inverse.
>
> return
> :   A new matrix which is the inverse of the input matrix `m`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/inverse.xhtml>

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-reftable-group
:::

## Comparison functions

::: rst-class
classref-descriptions-group
:::

### Comparison function descriptions

:::: {#shader_func_lessThan}
::: rst-class
classref-method
:::
::::

`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"}
**lessThan**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y) `🔗<shader_func_lessThan>`{.interpreted-text role="ref"}

> Performs a `component-wise<shading_componentwise>`{.interpreted-text
> role="ref"} less-than comparison of two vectors.
>
> param x
> :   The first vector to compare.
>
> param y
> :   The second vector to compare.
>
> return
> :   A boolean vector in which each element `i` is computed as
>     `x[i] < y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThan.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_greaterThan}
::: rst-class
classref-method
:::
::::

`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"}
**greaterThan**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y) `🔗<shader_func_greaterThan>`{.interpreted-text
role="ref"}

> Performs a `component-wise<shading_componentwise>`{.interpreted-text
> role="ref"} greater-than comparison of two vectors.
>
> param x
> :   The first vector to compare.
>
> param y
> :   The second vector to compare.
>
> return
> :   A boolean vector in which each element `i` is computed as
>     `x[i] > y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThan.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_lessThanEqual}
::: rst-class
classref-method
:::
::::

`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"}
**lessThanEqual**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y) `🔗<shader_func_lessThanEqual>`{.interpreted-text
role="ref"}

> Performs a `component-wise<shading_componentwise>`{.interpreted-text
> role="ref"} less-than-or-equal comparison of two vectors.
>
> param x
> :   The first vector to compare.
>
> param y
> :   The second vector to compare.
>
> return
> :   A boolean vector in which each element `i` is computed as
>     `x[i] <= y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/lessThanEqual.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_greaterThanEqual}
::: rst-class
classref-method
:::
::::

`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"}
**greaterThanEqual**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y) `🔗<shader_func_greaterThanEqual>`{.interpreted-text
role="ref"}

> Performs a `component-wise<shading_componentwise>`{.interpreted-text
> role="ref"} greater-than-or-equal comparison of two vectors.
>
> param x
> :   The first vector to compare.
>
> param y
> :   The second vector to compare.
>
> return
> :   A boolean vector in which each element `i` is computed as
>     `x[i] >= y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/greaterThanEqual.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_equal}
::: rst-class
classref-method
:::
::::

`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"}
**equal**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y) `🔗<shader_func_equal>`{.interpreted-text role="ref"}

> Performs a `component-wise<shading_componentwise>`{.interpreted-text
> role="ref"} equal-to comparison of two vectors.
>
> param x
> :   The first vector to compare.
>
> param y
> :   The second vector to compare.
>
> return
> :   A boolean vector in which each element `i` is computed as
>     `x[i] == y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/equal.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_notEqual}
::: rst-class
classref-method
:::
::::

`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"}
**notEqual**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x,
`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} y) `🔗<shader_func_notEqual>`{.interpreted-text role="ref"}

> Performs a `component-wise<shading_componentwise>`{.interpreted-text
> role="ref"} not-equal-to comparison of two vectors.
>
> param x
> :   The first vector for comparison.
>
> param y
> :   The second vector for comparison.
>
> return
> :   A boolean vector in which each element `i` is computed as
>     `x[i] != y[i]`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/notEqual.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_any}
::: rst-class
classref-method
:::
::::

bool
**any**(`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_any>`{.interpreted-text role="ref"}

> Returns `true` if any element of a boolean vector is `true`, `false`
> otherwise.
>
> Functionally equivalent to:
>
>     bool any(bvec x) {     // bvec can be bvec2, bvec3 or bvec4
>         bool result = false;
>         int i;
>         for (i = 0; i < x.length(); ++i) {
>             result |= x[i];
>         }
>         return result;
>     }
>
> param x
> :   The vector to be tested for truth.
>
> return
> :   True if any element of x is true and false otherwise.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/any.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_all}
::: rst-class
classref-method
:::
::::

bool
**all**(`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_all>`{.interpreted-text role="ref"}

> Returns `true` if all elements of a boolean vector are `true`, `false`
> otherwise.
>
> Functionally equivalent to:
>
>     bool all(bvec x)       // bvec can be bvec2, bvec3 or bvec4
>     {
>         bool result = true;
>         int i;
>         for (i = 0; i < x.length(); ++i)
>         {
>             result &= x[i];
>         }
>         return result;
>     }
>
> param x
> :   The vector to be tested for truth.
>
> return
> :   `true` if all elements of `x` are `true` and `false` otherwise.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/all.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_not}
::: rst-class
classref-method
:::
::::

`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"}
**not**(`vec_bool_type (Any of: bool, bvec2, bvec3, bvec4)`{.interpreted-text
role="abbr"} x) `🔗<shader_func_not>`{.interpreted-text role="ref"}

> Logically invert a boolean vector.
>
> param x
> :   The vector to be inverted.
>
> return
> :   A new boolean vector for which each element i is computed as
>     !x\[i\].
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/not.xhtml>

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-reftable-group
:::

## Texture functions

::: rst-class
classref-descriptions-group
:::

### Texture function descriptions

:::: {#shader_func_textureSize}
::: rst-class
classref-method
:::
::::

ivec2
**textureSize**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, int lod) `🔗<shader_func_textureSize>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

ivec2 **textureSize**(samplerCube s, int lod)
`🔗<shader_func_textureSize>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

ivec2 **textureSize**(samplerCubeArray s, int lod)
`🔗<shader_func_textureSize>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

ivec3
**textureSize**(`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`{.interpreted-text
role="abbr"} s, int lod) `🔗<shader_func_textureSize>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

ivec3
**textureSize**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s, int lod) `🔗<shader_func_textureSize>`{.interpreted-text
role="ref"}

> Retrieves the dimensions of a level of a texture.
>
> Returns the dimensions of level `lod` (if present) of the texture
> bound to sampler.
>
> The components in the return value are filled in, in order, with the
> width, height and depth of the texture. For the array forms, the last
> component of the return value is the number of layers in the texture
> array.
>
> param s
> :   The sampler to which the texture whose dimensions to retrieve is
>     bound.
>
> param lod
> :   The level of the texture for which to retrieve the dimensions.
>
> return
> :   The dimensions of level `lod` (if present) of the texture bound to
>     sampler.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureSize.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_textureQueryLod}
::: rst-class
classref-method
:::
::::

vec2
**textureQueryLod**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec2 p)
`🔗<shader_func_textureQueryLod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec2
**textureQueryLod**(`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`{.interpreted-text
role="abbr"} s, vec2 p)
`🔗<shader_func_textureQueryLod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec2
**textureQueryLod**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s, vec3 p)
`🔗<shader_func_textureQueryLod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec2 **textureQueryLod**(samplerCube s, vec3 p)
`🔗<shader_func_textureQueryLod>`{.interpreted-text role="ref"}

> :::: note
> ::: title
> Note
> :::
>
> Available only in the fragment shader.
> ::::
>
> Compute the level-of-detail that would be used to sample from a
> texture.
>
> The mipmap array(s) that would be accessed is returned in the x
> component of the return value. The computed level-of-detail relative
> to the base level is returned in the y component of the return value.
>
> If called on an incomplete texture, the result of the operation is
> undefined.
>
> param s
> :   The sampler to which the texture whose level-of-detail will be
>     queried is bound.
>
> param p
> :   The texture coordinates at which the level-of-detail will be
>     queried.
>
> return
> :   See description.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLod.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_textureQueryLevels}
::: rst-class
classref-method
:::
::::

int
**textureQueryLevels**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s) `🔗<shader_func_textureQueryLevels>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

int
**textureQueryLevels**(`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`{.interpreted-text
role="abbr"} s) `🔗<shader_func_textureQueryLevels>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

int
**textureQueryLevels**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s) `🔗<shader_func_textureQueryLevels>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

int **textureQueryLevels**(samplerCube s)
`🔗<shader_func_textureQueryLevels>`{.interpreted-text role="ref"}

> Compute the number of accessible mipmap levels of a texture.
>
> If called on an incomplete texture, or if no texture is associated
> with sampler, `0` is returned.
>
> param s
> :   The sampler to which the texture whose mipmap level count will be
>     queried is bound.
>
> return
> :   The number of accessible mipmap levels in the texture, or `0`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureQueryLevels.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_texture}
::: rst-class
classref-method
:::
::::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**texture**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec2 p \[, float bias\] )
`🔗<shader_func_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**texture**(`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`{.interpreted-text
role="abbr"} s, vec3 p \[, float bias\] )
`🔗<shader_func_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**texture**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s, vec3 p \[, float bias\] )
`🔗<shader_func_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec4 **texture**(samplerCube s, vec3 p \[, float bias\] )
`🔗<shader_func_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec4 **texture**(samplerCubeArray s, vec4 p \[, float bias\] )
`🔗<shader_func_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec4 **texture**(samplerExternalOES s, vec2 p \[, float bias\] )
`🔗<shader_func_texture>`{.interpreted-text role="ref"}

> Retrieves texels from a texture.
>
> Samples texels from the texture bound to `s` at texture coordinate
> `p`. An optional bias, specified in `bias` is included in the
> level-of-detail computation that is used to choose mipmap(s) from
> which to sample.
>
> For shadow forms, the last component of `p` is used as Dsub and the
> array layer is specified in the second to last component of `p`. (The
> second component of `p` is unused for 1D shadow lookups.)
>
> For non-shadow variants, the array layer comes from the last component
> of P.
>
> param s
> :   The sampler to which the texture from which texels will be
>     retrieved is bound.
>
> param p
> :   The texture coordinates at which texture will be sampled.
>
> param bias
> :   An optional bias to be applied during level-of-detail computation.
>
> return
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texture.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_textureProj}
::: rst-class
classref-method
:::
::::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureProj**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec3 p \[, float bias\] )
`🔗<shader_func_textureProj>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureProj**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec4 p \[, float bias\] )
`🔗<shader_func_textureProj>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureProj**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s, vec4 p \[, float bias\] )
`🔗<shader_func_textureProj>`{.interpreted-text role="ref"}

> Perform a texture lookup with projection.
>
> The texture coordinates consumed from `p`, not including the last
> component of `p`, are divided by the last component of `p`. The
> resulting 3rd component of `p` in the shadow forms is used as Dref.
> After these values are computed, the texture lookup proceeds as in
> texture.
>
> param s
> :   The sampler to which the texture from which texels will be
>     retrieved is bound.
>
> param p
> :   The texture coordinates at which texture will be sampled.
>
> param bias
> :   Optional bias to be applied during level-of-detail computation.
>
> return
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProj.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_textureLod}
::: rst-class
classref-method
:::
::::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureLod**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec2 p, float lod)
`🔗<shader_func_textureLod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureLod**(`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`{.interpreted-text
role="abbr"} s, vec3 p, float lod)
`🔗<shader_func_textureLod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureLod**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s, vec3 p, float lod)
`🔗<shader_func_textureLod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec4 **textureLod**(samplerCube s, vec3 p, float lod)
`🔗<shader_func_textureLod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec4 **textureLod**(samplerCubeArray s, vec4 p, float lod)
`🔗<shader_func_textureLod>`{.interpreted-text role="ref"}

> Performs a texture lookup at coordinate `p` from the texture bound to
> sampler with an explicit level-of-detail as specified in `lod`. `lod`
> specifies λbase and sets the partial derivatives as follows:
>
>     δu/δx=0, δv/δx=0, δw/δx=0
>     δu/δy=0, δv/δy=0, δw/δy=0
>
> param s
> :   The sampler to which the texture from which texels will be
>     retrieved is bound.
>
> param p
> :   The texture coordinates at which texture will be sampled.
>
> param lod
> :   The explicit level-of-detail.
>
> return
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureLod.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_textureProjLod}
::: rst-class
classref-method
:::
::::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureProjLod**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec3 p, float lod)
`🔗<shader_func_textureProjLod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureProjLod**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec4 p, float lod)
`🔗<shader_func_textureProjLod>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureProjLod**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s, vec4 p, float lod)
`🔗<shader_func_textureProjLod>`{.interpreted-text role="ref"}

> Performs a texture lookup with projection from an explicitly specified
> level-of-detail.
>
> The texture coordinates consumed from P, not including the last
> component of `p`, are divided by the last component of `p`. The
> resulting 3rd component of `p` in the shadow forms is used as Dref.
> After these values are computed, the texture lookup proceeds as in
> [textureLod\<shader_func_textureLod\>]{.title-ref}, with `lod` used to
> specify the level-of-detail from which the texture will be sampled.
>
> param s
> :   The sampler to which the texture from which texels will be
>     retrieved is bound.
>
> param p
> :   The texture coordinates at which texture will be sampled.
>
> param lod
> :   The explicit level-of-detail from which to fetch texels.
>
> return
> :   a texel
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjLod.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_textureGrad}
::: rst-class
classref-method
:::
::::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureGrad**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec2 p, vec2 dPdx, vec2 dPdy)
`🔗<shader_func_textureGrad>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureGrad**(`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`{.interpreted-text
role="abbr"} s, vec3 p, vec2 dPdx, vec2 dPdy)
`🔗<shader_func_textureGrad>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureGrad**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s, vec3 p, vec2 dPdx, vec2 dPdy)
`🔗<shader_func_textureGrad>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec4 **textureGrad**(samplerCube s, vec3 p, vec3 dPdx, vec3 dPdy)
`🔗<shader_func_textureGrad>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec4 **textureGrad**(samplerCubeArray s, vec3 p, vec3 dPdx, vec3 dPdy)
`🔗<shader_func_textureGrad>`{.interpreted-text role="ref"}

> 
>
> Performs a texture lookup at coordinate `p` from the texture bound to sampler with explicit texture coordinate gradiends as specified in `dPdx` and `dPdy`. Set:
>
> :   - `δs/δx=δp/δx` for a 1D texture, `δp.s/δx` otherwise
>     - `δs/δy=δp/δy` for a 1D texture, `δp.s/δy` otherwise
>     - `δt/δx=0.0` for a 1D texture, `δp.t/δx` otherwise
>     - `δt/δy=0.0` for a 1D texture, `δp.t/δy` otherwise
>     - `δr/δx=0.0` for a 1D or 2D texture, `δp.p/δx` otherwise
>     - `δr/δy=0.0` for a 1D or 2D texture, `δp.p/δy` otherwise
>
> For the cube version, the partial derivatives of `p` are assumed to be
> in the coordinate system used before texture coordinates are projected
> onto the appropriate cube face.
>
> param s
> :   The sampler to which the texture from which texels will be
>     retrieved is bound.
>
> param p
> :   The texture coordinates at which texture will be sampled.
>
> param dPdx
> :   The partial derivative of P with respect to window x.
>
> param dPdy
> :   The partial derivative of P with respect to window y.
>
> return
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGrad.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_textureProjGrad}
::: rst-class
classref-method
:::
::::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureProjGrad**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec3 p, vec2 dPdx, vec2 dPdy)
`🔗<shader_func_textureProjGrad>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureProjGrad**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec4 p, vec2 dPdx, vec2 dPdy)
`🔗<shader_func_textureProjGrad>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureProjGrad**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s, vec4 p, vec3 dPdx, vec3 dPdy)
`🔗<shader_func_textureProjGrad>`{.interpreted-text role="ref"}

> Perform a texture lookup with projection and explicit gradients.
>
> The texture coordinates consumed from `p`, not including the last
> component of `p`, are divided by the last component of `p`. After
> these values are computed, the texture lookup proceeds as in
> [textureGrad\<shader_func_textureGrad\>]{.title-ref}, passing `dPdx`
> and `dPdy` as gradients.
>
> param s
> :   The sampler to which the texture from which texels will be
>     retrieved is bound.
>
> param p
> :   The texture coordinates at which texture will be sampled.
>
> param dPdx
> :   The partial derivative of `p` with respect to window x.
>
> param dPdy
> :   The partial derivative of `p` with respect to window y.
>
> return
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureProjGrad.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_texelFetch}
::: rst-class
classref-method
:::
::::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**texelFetch**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, ivec2 p, int lod)
`🔗<shader_func_texelFetch>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**texelFetch**(`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`{.interpreted-text
role="abbr"} s, ivec3 p, int lod)
`🔗<shader_func_texelFetch>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**texelFetch**(`gsampler3D (Any of: sampler3D, isampler3D, uSampler3D)`{.interpreted-text
role="abbr"} s, ivec3 p, int lod)
`🔗<shader_func_texelFetch>`{.interpreted-text role="ref"}

> Performs a lookup of a single texel from texture coordinate `p` in the
> texture bound to sampler.
>
> param s
> :   The sampler to which the texture from which texels will be
>     retrieved is bound.
>
> param p
> :   The texture coordinates at which texture will be sampled.
>
> param lod
> :   Specifies the level-of-detail within the texture from which the
>     texel will be fetched.
>
> return
> :   A texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/texelFetch.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_textureGather}
::: rst-class
classref-method
:::
::::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureGather**(`gsampler2D (Any of: sampler2D, isampler2D, uSampler2D)`{.interpreted-text
role="abbr"} s, vec2 p \[, int comps\] )
`🔗<shader_func_textureGather>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`gvec4_type (Any of: vec4, ivec4, uvec4)`{.interpreted-text role="abbr"}
**textureGather**(`gsampler2DArray (Any of: sampler2DArray, isampler2DArray, uSampler2DArray)`{.interpreted-text
role="abbr"} s, vec3 p \[, int comps\] )
`🔗<shader_func_textureGather>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

vec4 **textureGather**(samplerCube s, vec3 p \[, int comps\] )
`🔗<shader_func_textureGather>`{.interpreted-text role="ref"}

> Gathers four texels from a texture.
>
> Returns the value:
>
>     vec4(Sample_i0_j1(p, base).comps,
>          Sample_i1_j1(p, base).comps,
>          Sample_i1_j0(p, base).comps,
>          Sample_i0_j0(p, base).comps);
>
> param s
> :   The sampler to which the texture from which texels will be
>     retrieved is bound.
>
> param p
> :   The texture coordinates at which texture will be sampled.
>
> param comps
> :   *optional* the component of the source texture (0 -\> x, 1 -\> y,
>     2 -\> z, 3 -\> w) that will be used to generate the resulting
>     vector. Zero if not specified.
>
> return
> :   The gathered texel.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/textureGather.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_dFdx}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**dFdx**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} p) `🔗<shader_func_dFdx>`{.interpreted-text role="ref"}

> :::: note
> ::: title
> Note
> :::
>
> Available only in the fragment shader.
> ::::
>
> Returns the partial derivative of `p` with respect to the window x
> coordinate using local differencing.
>
> Returns either `dFdxCoarse<shader_func_dFdxCoarse>`{.interpreted-text
> role="ref"} or `dFdxFine<shader_func_dfdxFine>`{.interpreted-text
> role="ref"}. The implementation may choose which calculation to
> perform based upon factors such as performance or the value of the API
> `GL_FRAGMENT_SHADER_DERIVATIVE_HINT` hint.
>
> :::: warning
> ::: title
> Warning
> :::
>
> Expressions that imply higher order derivatives such as
> `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives
> such as `dFdx(dFdy(n))`.
> ::::
>
> param p
>
> :   The expression of which to take the partial derivative.
>
>     :::: note
>     ::: title
>     Note
>     :::
>
>     It is assumed that the expression `p` is continuous and therefore
>     expressions evaluated via non-uniform control flow may be
>     undefined.
>     ::::
>
> return
> :   The partial derivative of `p`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/dFdx.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_dFdxCoarse}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**dFdxCoarse**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} p) `🔗<shader_func_dFdxCoarse>`{.interpreted-text
role="ref"}

> :::: note
> ::: title
> Note
> :::
>
> Available only in the fragment shader. Not available when using the
> Compatibility renderer.
> ::::
>
> Returns the partial derivative of `p` with respect to the window x
> coordinate.
>
> Calculates derivatives using local differencing based on the value of
> `p` for the current fragment\'s neighbors, and will possibly, but not
> necessarily, include the value for the current fragment. That is, over
> a given area, the implementation can compute derivatives in fewer
> unique locations than would be allowed for the corresponding
> `dFdxFine<shader_func_dFdxFine>`{.interpreted-text role="ref"}
> function.
>
> :::: warning
> ::: title
> Warning
> :::
>
> Expressions that imply higher order derivatives such as
> `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives
> such as `dFdx(dFdy(n))`.
> ::::
>
> param p
>
> :   The expression of which to take the partial derivative.
>
>     :::: note
>     ::: title
>     Note
>     :::
>
>     It is assumed that the expression `p` is continuous and therefore
>     expressions evaluated via non-uniform control flow may be
>     undefined.
>     ::::
>
> return
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_dFdxFine}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**dFdxFine**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} p) `🔗<shader_func_dFdxFine>`{.interpreted-text role="ref"}

> :::: note
> ::: title
> Note
> :::
>
> Available only in the fragment shader. Not available when using the
> Compatibility renderer.
> ::::
>
> Returns the partial derivative of `p` with respect to the window x
> coordinate.
>
> Calculates derivatives using local differencing based on the value of
> `p` for the current fragment and its immediate neighbor(s).
>
> :::: warning
> ::: title
> Warning
> :::
>
> Expressions that imply higher order derivatives such as
> `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives
> such as `dFdx(dFdy(n))`.
> ::::
>
> param p
>
> :   The expression of which to take the partial derivative.
>
>     :::: note
>     ::: title
>     Note
>     :::
>
>     It is assumed that the expression `p` is continuous and therefore
>     expressions evaluated via non-uniform control flow may be
>     undefined.
>     ::::
>
> return
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_dFdy}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**dFdy**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} p) `🔗<shader_func_dFdy>`{.interpreted-text role="ref"}

> :::: note
> ::: title
> Note
> :::
>
> Available only in the fragment shader.
> ::::
>
> Returns the partial derivative of `p` with respect to the window y
> coordinate using local differencing.
>
> Returns either `dFdyCoarse<shader_func_dFdyCoarse>`{.interpreted-text
> role="ref"} or `dFdyFine<shader_func_dfdyFine>`{.interpreted-text
> role="ref"}. The implementation may choose which calculation to
> perform based upon factors such as performance or the value of the API
> `GL_FRAGMENT_SHADER_DERIVATIVE_HINT` hint.
>
> :::: warning
> ::: title
> Warning
> :::
>
> Expressions that imply higher order derivatives such as
> `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives
> such as `dFdx(dFdy(n))`.
> ::::
>
> param p
>
> :   The expression of which to take the partial derivative.
>
>     :::: note
>     ::: title
>     Note
>     :::
>
>     It is assumed that the expression `p` is continuous and therefore
>     expressions evaluated via non-uniform control flow may be
>     undefined.
>     ::::
>
> return
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_dFdyCoarse}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**dFdyCoarse**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} p) `🔗<shader_func_dFdyCoarse>`{.interpreted-text
role="ref"}

> :::: note
> ::: title
> Note
> :::
>
> Available only in the fragment shader. Not available when using the
> Compatibility renderer.
> ::::
>
> Returns the partial derivative of `p` with respect to the window y
> coordinate.
>
> Calculates derivatives using local differencing based on the value of
> `p` for the current fragment\'s neighbors, and will possibly, but not
> necessarily, include the value for the current fragment. That is, over
> a given area, the implementation can compute derivatives in fewer
> unique locations than would be allowed for the corresponding dFdyFine
> and dFdyFine functions.
>
> :::: warning
> ::: title
> Warning
> :::
>
> Expressions that imply higher order derivatives such as
> `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives
> such as `dFdx(dFdy(n))`.
> ::::
>
> param p
>
> :   The expression of which to take the partial derivative.
>
>     :::: note
>     ::: title
>     Note
>     :::
>
>     It is assumed that the expression `p` is continuous and therefore
>     expressions evaluated via non-uniform control flow may be
>     undefined.
>     ::::
>
> return
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_dFdyFine}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**dFdyFine**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} p) `🔗<shader_func_dFdyFine>`{.interpreted-text role="ref"}

> :::: note
> ::: title
> Note
> :::
>
> Available only in the fragment shader. Not available when using the
> Compatibility renderer.
> ::::
>
> Returns the partial derivative of `p` with respect to the window y
> coordinate.
>
> Calculates derivatives using local differencing based on the value of
> `p` for the current fragment and its immediate neighbor(s).
>
> :::: warning
> ::: title
> Warning
> :::
>
> Expressions that imply higher order derivatives such as
> `dFdx(dFdx(n))` have undefined results, as do mixed-order derivatives
> such as `dFdx(dFdy(n))`.
> ::::
>
> param p
>
> :   The expression of which to take the partial derivative.
>
>     :::: note
>     ::: title
>     Note
>     :::
>
>     It is assumed that the expression `p` is continuous and therefore
>     expressions evaluated via non-uniform control flow may be
>     undefined.
>     ::::
>
> return
> :   The partial derivative of `p`.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/dFdx.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_fwidth}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**fwidth**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} p) `🔗<shader_func_fwidth>`{.interpreted-text role="ref"}

> Returns the sum of the absolute value of derivatives in x and y.
>
> Uses local differencing for the input argument `p`.
>
> Equivalent to `abs(dFdx(p)) + abs(dFdy(p))`.
>
> param p
> :   The expression of which to take the partial derivative.
>
> return
> :   The partial derivative.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_fwidthCoarse}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**fwidthCoarse**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} p) `🔗<shader_func_fwidthCoarse>`{.interpreted-text
role="ref"}

> :::: note
> ::: title
> Note
> :::
>
> Available only in the fragment shader. Not available when using the
> Compatibility renderer.
> ::::
>
> Returns the sum of the absolute value of derivatives in x and y.
>
> Uses local differencing for the input argument p.
>
> Equivalent to `abs(dFdxCoarse(p)) + abs(dFdyCoarse(p))`.
>
> param p
> :   The expression of which to take the partial derivative.
>
> return
> :   The partial derivative.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/fwidth.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_fwidthFine}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**fwidthFine**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} p) `🔗<shader_func_fwidthFine>`{.interpreted-text
role="ref"}

> :::: note
> ::: title
> Note
> :::
>
> Available only in the fragment shader. Not available when using the
> Compatibility renderer.
> ::::
>
> Returns the sum of the absolute value of derivatives in x and y.
>
> Uses local differencing for the input argument p.
>
> Equivalent to `abs(dFdxFine(p)) + abs(dFdyFine(p))`.
>
> param p
> :   The expression of which to take the partial derivative.
>
> return
> :   The partial derivative.
>
> <https://registry.khronos.org/OpenGL-Refpages/gl4/html/fwidth.xhtml>

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-reftable-group
:::

## Packing and unpacking functions

These functions convert floating-point numbers into various sized
integers and then pack those integers into a single 32bit unsigned
integer. The \'unpack\' functions perform the opposite operation,
returning the original floating-point numbers.

::: rst-class
classref-descriptions-group
:::

### Packing and unpacking function descriptions

:::: {#shader_func_packHalf2x16}
::: rst-class
classref-method
:::
::::

uint **packHalf2x16**(vec2 v)
`🔗<shader_func_packHalf2x16>`{.interpreted-text role="ref"}

> Converts two 32-bit floating-point quantities to 16-bit floating-point
> quantities and packs them into a single 32-bit integer.
>
> Returns an unsigned integer obtained by converting the components of a
> two-component floating-point vector to the 16-bit floating-point
> representation found in the OpenGL Specification, and then packing
> these two 16-bit integers into a 32-bit unsigned integer. The first
> vector component specifies the 16 least-significant bits of the
> result; the second component specifies the 16 most-significant bits.
>
> param v
> :   A vector of two 32-bit floating-point values that are to be
>     converted to 16-bit representation and packed into the result.
>
> return
> :   The packed value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packHalf2x16.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_unpackHalf2x16}
::: rst-class
classref-method
:::
::::

vec2 **unpackHalf2x16**(uint v)
`🔗<shader_func_unpackHalf2x16>`{.interpreted-text role="ref"}

> Inverse of `packHalf2x16<shader_func_packHalf2x16>`{.interpreted-text
> role="ref"}.
>
> Unpacks a 32-bit integer into two 16-bit floating-point values,
> converts them to 32-bit floating-point values, and puts them into a
> vector. The first component of the vector is obtained from the 16
> least-significant bits of `v`; the second component is obtained from
> the 16 most-significant bits of `v`.
>
> param v
> :   A single 32-bit unsigned integer containing 2 packed 16-bit
>     floating-point values.
>
> return
> :   Two unpacked floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackHalf2x16.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_packUnorm2x16}
::: rst-class
classref-method
:::
::::

uint **packUnorm2x16**(vec2 v)
`🔗<shader_func_packUnorm2x16>`{.interpreted-text role="ref"}

> Pack floating-point values into an unsigned integer.
>
> Converts each component of the normalized floating-point value v into
> 16-bit integer values and then packs the results into a 32-bit
> unsigned integer.
>
> The conversion for component c of `v` to fixed-point is performed as
> follows:
>
>     round(clamp(c, 0.0, 1.0) * 65535.0)
>
> The first component of the vector will be written to the least
> significant bits of the output; the last component will be written to
> the most significant bits.
>
> param v
> :   A vector of values to be packed into an unsigned integer.
>
> return
> :   Unsigned 32 bit integer containing the packed encoding of the
>     vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_unpackUnorm2x16}
::: rst-class
classref-method
:::
::::

vec2 **unpackUnorm2x16**(uint v)
`🔗<shader_func_unpackUnorm2x16>`{.interpreted-text role="ref"}

> Unpack floating-point values from an unsigned integer.
>
> Unpack single 32-bit unsigned integers into a pair of 16-bit unsigned
> integers. Then, each component is converted to a normalized
> floating-point value to generate the returned two-component vector.
>
> The conversion for unpacked fixed point value f to floating-point is
> performed as follows:
>
> > f / 65535.0
>
> The first component of the returned vector will be extracted from the
> least significant bits of the input; the last component will be
> extracted from the most significant bits.
>
> param v
> :   An unsigned integer containing packed floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_packSnorm2x16}
::: rst-class
classref-method
:::
::::

uint **packSnorm2x16**(vec2 v)
`🔗<shader_func_packSnorm2x16>`{.interpreted-text role="ref"}

> Packs floating-point values into an unsigned integer.
>
> Convert each component of the normalized floating-point value `v` into
> 16-bit integer values and then packs the results into a 32-bit
> unsigned integer.
>
> The conversion for component c of `v` to fixed-point is performed as
> follows:
>
>     round(clamp(c, -1.0, 1.0) * 32767.0)
>
> The first component of the vector will be written to the least
> significant bits of the output; the last component will be written to
> the most significant bits.
>
> param v
> :   A vector of values to be packed into an unsigned integer.
>
> return
> :   Unsigned 32 bit integer containing the packed encoding of the
>     vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_unpackSnorm2x16}
::: rst-class
classref-method
:::
::::

vec2 **unpackSnorm2x16**(uint v)
`🔗<shader_func_unpackSnorm2x16>`{.interpreted-text role="ref"}

> Unpacks floating-point values from an unsigned integer.
>
> Unpacks single 32-bit unsigned integers into a pair of 16-bit signed
> integers. Then, each component is converted to a normalized
> floating-point value to generate the returned two-component vector.
>
> The conversion for unpacked fixed point value f to floating-point is
> performed as follows:
>
> > clamp(f / 32727.0, -1.0, 1.0)
>
> The first component of the returned vector will be extracted from the
> least significant bits of the input; the last component will be
> extracted from the most significant bits.
>
> param v
> :   An unsigned integer containing packed floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_packUnorm4x8}
::: rst-class
classref-method
:::
::::

uint **packUnorm4x8**(vec4 v)
`🔗<shader_func_packUnorm4x8>`{.interpreted-text role="ref"}

> Packs floating-point values into an unsigned integer.
>
> Converts each component of the normalized floating-point value `v`
> into 16-bit integer values and then packs the results into a 32-bit
> unsigned integer.
>
> The conversion for component c of `v` to fixed-point is performed as
> follows:
>
>     round(clamp(c, 0.0, 1.0) * 255.0)
>
> The first component of the vector will be written to the least
> significant bits of the output; the last component will be written to
> the most significant bits.
>
> param v
> :   A vector of values to be packed into an unsigned integer.
>
> return
> :   Unsigned 32 bit integer containing the packed encoding of the
>     vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_unpackUnorm4x8}
::: rst-class
classref-method
:::
::::

vec4 **unpackUnorm4x8**(uint v)
`🔗<shader_func_unpackUnorm4x8>`{.interpreted-text role="ref"}

> Unpacks floating-point values from an unsigned integer.
>
> Unpacks single 32-bit unsigned integers into four 8-bit unsigned
> integers. Then, each component is converted to a normalized
> floating-point value to generate the returned four-component vector.
>
> The conversion for unpacked fixed point value f to floating-point is
> performed as follows:
>
> > f / 255.0
>
> The first component of the returned vector will be extracted from the
> least significant bits of the input; the last component will be
> extracted from the most significant bits.
>
> param v
> :   An unsigned integer containing packed floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_packSnorm4x8}
::: rst-class
classref-method
:::
::::

uint **packSnorm4x8**(vec4 v)
`🔗<shader_func_packSnorm4x8>`{.interpreted-text role="ref"}

> Packs floating-point values into an unsigned integer.
>
> Convert each component of the normalized floating-point value `v` into
> 16-bit integer values and then packs the results into a 32-bit
> unsigned integer.
>
> The conversion for component c of `v` to fixed-point is performed as
> follows:
>
>     round(clamp(c, -1.0, 1.0) * 127.0)
>
> The first component of the vector will be written to the least
> significant bits of the output; the last component will be written to
> the most significant bits.
>
> param v
> :   A vector of values to be packed into an unsigned integer.
>
> return
> :   Unsigned 32 bit integer containing the packed encoding of the
>     vector.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/packUnorm.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_unpackSnorm4x8}
::: rst-class
classref-method
:::
::::

vec4 **unpackSnorm4x8**(uint v)
`🔗<shader_func_unpackSnorm4x8>`{.interpreted-text role="ref"}

> Unpack floating-point values from an unsigned integer.
>
> Unpack single 32-bit unsigned integers into four 8-bit signed
> integers. Then, each component is converted to a normalized
> floating-point value to generate the returned four-component vector.
>
> The conversion for unpacked fixed point value f to floating-point is
> performed as follows:
>
> > clamp(f / 127.0, -1.0, 1.0)
>
> The first component of the returned vector will be extracted from the
> least significant bits of the input; the last component will be
> extracted from the most significant bits.
>
> param v
> :   An unsigned integer containing packed floating-point values.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/unpackUnorm.xhtml>

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-reftable-group
:::

## Bitwise functions

::: rst-class
classref-descriptions-group
:::

### Bitwise function descriptions

:::: {#shader_func_bitfieldExtract}
::: rst-class
classref-method
:::
::::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**bitfieldExtract**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} value, int offset, int bits)
`🔗<shader_func_bitfieldExtract>`{.interpreted-text role="ref"}

> Extracts a subset of the bits of `value` and returns it in the least
> significant bits of the result. The range of bits extracted is
> `[offset, offset + bits - 1]`.
>
> The most significant bits of the result will be set to zero.
>
> :::: note
> ::: title
> Note
> :::
>
> If bits is zero, the result will be zero.
> ::::
>
> :::: warning
> ::: title
> Warning
> :::
>
> The result will be undefined if:
>
> - offset or bits is negative.
> - if the sum of offset and bits is greater than the number of bits
>   used to store the operand.
> ::::
>
> param value
> :   The integer from which to extract bits.
>
> param offset
> :   The index of the first bit to extract.
>
> param bits
> :   The number of bits to extract.
>
> return
> :   Integer with the requested bits.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**bitfieldExtract**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} value, int offset, int bits)
`🔗<shader_func_bitfieldExtract>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Extracts a subset of the bits of `value` and returns it in the least
> significant bits of the result. The range of bits extracted is
> `[offset, offset + bits - 1]`.
>
> The most significant bits will be set to the value of
> `offset + base - 1` (i.e., it is sign extended to the width of the
> return type).
>
> :::: note
> ::: title
> Note
> :::
>
> If bits is zero, the result will be zero.
> ::::
>
> :::: warning
> ::: title
> Warning
> :::
>
> The result will be undefined if:
>
> - offset or bits is negative.
> - if the sum of offset and bits is greater than the number of bits
>   used to store the operand.
> ::::
>
> param value
> :   The integer from which to extract bits.
>
> param offset
> :   The index of the first bit to extract.
>
> param bits
> :   The number of bits to extract.
>
> return
> :   Integer with the requested bits.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldExtract.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_bitfieldInsert}
::: rst-class
classref-method
:::
::::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**bitfieldExtract**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} value, int offset, int bits)
`🔗<shader_func_bitfieldInsert>`{.interpreted-text role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**bitfieldInsert**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} base,
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} insert, int offset, int bits)
`🔗<shader_func_bitfieldInsert>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Inserts the `bits` least significant bits of `insert` into `base` at
> offset `offset`.
>
> The returned value will have bits \[offset, offset + bits + 1\] taken
> from \[0, bits - 1\] of `insert` and all other bits taken directly
> from the corresponding bits of base.
>
> :::: note
> ::: title
> Note
> :::
>
> If bits is zero, the result will be the original value of base.
> ::::
>
> :::: warning
> ::: title
> Warning
> :::
>
> The result will be undefined if:
>
> - offset or bits is negative.
> - if the sum of offset and bits is greater than the number of bits
>   used to store the operand.
> ::::
>
> param base
> :   The integer into which to insert `insert`.
>
> param insert
> :   The value of the bits to insert.
>
> param offset
> :   The index of the first bit to insert.
>
> param bits
> :   The number of bits to insert.
>
> return
> :   `base` with inserted bits.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldInsert.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_bitfieldReverse}
::: rst-class
classref-method
:::
::::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**bitfieldReverse**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} value) `🔗<shader_func_bitfieldReverse>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**bitfieldReverse**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} value) `🔗<shader_func_bitfieldReverse>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Reverse the order of bits in an integer.
>
> The bit numbered `n` will be taken from bit `(bits - 1) - n` of
> `value`, where bits is the total number of bits used to represent
> `value`.
>
> param value
> :   The value whose bits to reverse.
>
> return
> :   `value` but with its bits reversed.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitfieldReverse.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_bitCount}
::: rst-class
classref-method
:::
::::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**bitCount**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} value) `🔗<shader_func_bitCount>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**bitCount**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} value) `🔗<shader_func_bitCount>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Counts the number of 1 bits in an integer.
>
> param value
> :   The value whose bits to count.
>
> return
> :   The number of bits that are set to 1 in the binary representation
>     of `value`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/bitCount.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_findLSB}
::: rst-class
classref-method
:::
::::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**findLSB**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} value) `🔗<shader_func_findLSB>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**findLSB**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} value) `🔗<shader_func_findLSB>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Find the index of the least significant bit set to `1`.
>
> :::: note
> ::: title
> Note
> :::
>
> If `value` is zero, `-1` will be returned.
> ::::
>
> param value
> :   The value whose bits to scan.
>
> return
> :   The bit number of the least significant bit that is set to 1 in
>     the binary representation of value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findLSB.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_findMSB}
::: rst-class
classref-method
:::
::::

`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"}
**findMSB**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} value) `🔗<shader_func_findMSB>`{.interpreted-text
role="ref"}

::: rst-class
classref-method
:::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**findMSB**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} value) `🔗<shader_func_findMSB>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Find the index of the most significant bit set to 1.
>
> :::: note
> ::: title
> Note
> :::
>
> For signed integer types, the sign bit is checked first and then: -
> For positive integers, the result will be the bit number of the most
> significant bit that is set to 1. - For negative integers, the result
> will be the bit number of the most significant bit set to 0.
> ::::
>
> :::: note
> ::: title
> Note
> :::
>
> For a value of zero or negative 1, -1 will be returned.
> ::::
>
> param value
> :   The value whose bits to scan.
>
> return
> :   The bit number of the most significant bit that is set to 1 in the
>     binary representation of value.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/findMSB.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_imulExtended}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**imulExtended**(`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} x,
`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} y, out
`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} msb, out
`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} lsb) `🔗<shader_func_imulExtended>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Perform 32-bit by 32-bit signed multiplication to produce a 64-bit
> result.
>
> The 32 least significant bits of this product are returned in `lsb`
> and the 32 most significant bits are returned in `msb`.
>
> param x
> :   The first multiplicand.
>
> param y
> :   The second multiplicand.
>
> param msb
> :   The variable to receive the most significant word of the product.
>
> param lsb
> :   The variable to receive the least significant word of the product.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_umulExtended}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**umulExtended**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} x,
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} y, out
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} msb, out
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} lsb) `🔗<shader_func_umulExtended>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Perform 32-bit by 32-bit unsigned multiplication to produce a 64-bit
> result.
>
> The 32 least significant bits of this product are returned in `lsb`
> and the 32 most significant bits are returned in `msb`.
>
> param x
> :   The first multiplicand.
>
> param y
> :   The second multiplicand.
>
> param msb
> :   The variable to receive the most significant word of the product.
>
> param lsb
> :   The variable to receive the least significant word of the product.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/umulExtended.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_uaddCarry}
::: rst-class
classref-method
:::
::::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**uaddCarry**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} x,
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} y, out
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} carry) `🔗<shader_func_uaddCarry>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Add unsigned integers and generate carry.
>
> adds two 32-bit unsigned integer variables (scalars or vectors) and
> generates a 32-bit unsigned integer result, along with a carry output.
> The value carry is .
>
> param x
> :   The first operand.
>
> param y
> :   The second operand.
>
> param carry
> :   0 if the sum is less than 2^32^, otherwise 1.
>
> return
> :   `(x + y) % 2^32`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/uaddCarry.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_usubBorrow}
::: rst-class
classref-method
:::
::::

`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"}
**usubBorrow**(`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} x,
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} y, out
`vec_uint_type (Any of: float, uvec2, uvec3, uvec4)`{.interpreted-text
role="abbr"} borrow) `🔗<shader_func_usubBorrow>`{.interpreted-text
role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Subtract unsigned integers and generate borrow.
>
> param x
> :   The first operand.
>
> param y
> :   The second operand.
>
> param borrow
> :   `0` if `x >= y`, otherwise `1`.
>
> return
> :   The difference of `x` and `y` if non-negative, or 2^32^ plus that
>     difference otherwise.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/usubBorrow.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_ldexp}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**ldexp**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x, out
`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} exp) `🔗<shader_func_ldexp>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Assembles a floating-point number from a value and exponent.
>
> :::: warning
> ::: title
> Warning
> :::
>
> If this product is too large to be represented in the floating-point
> type, the result is undefined.
> ::::
>
> param x
> :   The value to be used as a source of significand.
>
> param exp
> :   The value to be used as a source of exponent.
>
> return
> :   `x * 2^exp`
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/ldexp.xhtml>

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#shader_func_frexp}
::: rst-class
classref-method
:::
::::

`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"}
**frexp**(`vec_type (Any of: float, vec2, vec3, vec4)`{.interpreted-text
role="abbr"} x, out
`vec_int_type (Any of: int, ivec2, ivec3, ivec4)`{.interpreted-text
role="abbr"} exp) `🔗<shader_func_frexp>`{.interpreted-text role="ref"}

> `Component-wise Function<shading_componentwise>`{.interpreted-text
> role="ref"}.
>
> Extracts `x` into a floating-point significand in the range
> `[0.5, 1.0)` and in integral exponent of two, such that:
>
>     x = significand * 2 ^ exponent
>
> For a floating-point value of zero, the significand and exponent are
> both zero.
>
> :::: warning
> ::: title
> Warning
> :::
>
> For a floating-point value that is an infinity or a floating-point
> NaN, the results are undefined.
> ::::
>
> param x
> :   The value from which significand and exponent are to be extracted.
>
> param exp
> :   The variable into which to place the exponent of `x`.
>
> return
> :   The significand of `x`.
>
> <https://www.khronos.org/registry/OpenGL-Refpages/gl4/html/frexp.xhtml>

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------
