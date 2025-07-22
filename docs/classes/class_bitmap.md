github_url
:   hide

# BitMap {#class_BitMap}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Boolean matrix.

::: rst-class
classref-introduction-group
:::

## Description

A two-dimensional array of boolean values, can be used to efficiently
store a binary matrix (every matrix element takes only one bit) and
query the values using natural cartesian coordinates.

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

:::: {#class_BitMap_method_convert_to_image}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**convert_to_image**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BitMap_method_convert_to_image>`{.interpreted-text role="ref"}

Returns an image of the same size as the bitmap and with an
`Format<enum_Image_Format>`{.interpreted-text role="ref"} of type
`Image.FORMAT_L8<class_Image_constant_FORMAT_L8>`{.interpreted-text
role="ref"}. `true` bits of the bitmap are being converted into white
pixels, and `false` bits into black.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_create}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create**(size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}) `🔗<class_BitMap_method_create>`{.interpreted-text
role="ref"}

Creates a bitmap with the specified size, filled with `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_create_from_image_alpha}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_from_image_alpha**(image:
`Image<class_Image>`{.interpreted-text role="ref"}, threshold:
`float<class_float>`{.interpreted-text role="ref"} = 0.1)
`🔗<class_BitMap_method_create_from_image_alpha>`{.interpreted-text
role="ref"}

Creates a bitmap that matches the given image dimensions, every element
of the bitmap is set to `false` if the alpha value of the image at that
position is equal to `threshold` or less, and `true` in other case.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_get_bit}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_bit**(x:
`int<class_int>`{.interpreted-text role="ref"}, y:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_BitMap_method_get_bit>`{.interpreted-text
role="ref"}

Returns bitmap\'s value at the specified position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_get_bitv}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_bitv**(position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_BitMap_method_get_bitv>`{.interpreted-text
role="ref"}

Returns bitmap\'s value at the specified position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_get_size}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **get_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_BitMap_method_get_size>`{.interpreted-text
role="ref"}

Returns bitmap\'s dimensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_get_true_bit_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_true_bit_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BitMap_method_get_true_bit_count>`{.interpreted-text
role="ref"}

Returns the number of bitmap elements that are set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_grow_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**grow_mask**(pixels: `int<class_int>`{.interpreted-text role="ref"},
rect: `Rect2i<class_Rect2i>`{.interpreted-text role="ref"})
`🔗<class_BitMap_method_grow_mask>`{.interpreted-text role="ref"}

Applies morphological dilation or erosion to the bitmap. If `pixels` is
positive, dilation is applied to the bitmap. If `pixels` is negative,
erosion is applied to the bitmap. `rect` defines the area where the
morphological operation is applied. Pixels located outside the `rect`
are unaffected by
`grow_mask()<class_BitMap_method_grow_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_opaque_to_polygons}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"}\] **opaque_to_polygons**(rect:
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}, epsilon:
`float<class_float>`{.interpreted-text role="ref"} = 2.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_BitMap_method_opaque_to_polygons>`{.interpreted-text
role="ref"}

Creates an `Array<class_Array>`{.interpreted-text role="ref"} of
polygons covering a rectangular portion of the bitmap. It uses a
marching squares algorithm, followed by Ramer-Douglas-Peucker (RDP)
reduction of the number of vertices. Each polygon is described as a
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} of its vertices.

To get polygons covering the whole bitmap, pass:

    Rect2(Vector2(), get_size())

`epsilon` is passed to RDP to control how accurately the polygons cover
the bitmap: a lower `epsilon` corresponds to more points in the
polygons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_resize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**resize**(new_size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}) `🔗<class_BitMap_method_resize>`{.interpreted-text
role="ref"}

Resizes the image to `new_size`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_set_bit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **set_bit**(x:
`int<class_int>`{.interpreted-text role="ref"}, y:
`int<class_int>`{.interpreted-text role="ref"}, bit:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_BitMap_method_set_bit>`{.interpreted-text role="ref"}

Sets the bitmap\'s element at the specified position, to the specified
value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_set_bit_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bit_rect**(rect: `Rect2i<class_Rect2i>`{.interpreted-text
role="ref"}, bit: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_BitMap_method_set_bit_rect>`{.interpreted-text role="ref"}

Sets a rectangular portion of the bitmap to the specified value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BitMap_method_set_bitv}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bitv**(position: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, bit: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_BitMap_method_set_bitv>`{.interpreted-text role="ref"}

Sets the bitmap\'s element at the specified position, to the specified
value.
