github_url
:   hide

# HeightMapShape3D {#class_HeightMapShape3D}

**Inherits:** `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D height map shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 3D heightmap shape, intended for use in physics. Usually used to
provide a shape for a
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"}. This type is most commonly used for terrain with vertices
placed in a fixed width grid. Due to the nature of the heightmap, it
cannot be used to model overhangs or caves, which would require multiple
vertices at the same vertical location. Holes can be punched through the
collision by assigning
`@GDScript.NAN<class_@GDScript_constant_NAN>`{.interpreted-text
role="ref"} to the height of the desired vertices (this is supported in
both GodotPhysics3D and Jolt Physics). You could then insert meshes with
their own separate collision to provide overhangs, caves, and so on.

\*\*Performance:\*\* **HeightMapShape3D** is faster to check collisions
against than
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"}, but it is significantly slower than primitive shapes like
`BoxShape3D<class_BoxShape3D>`{.interpreted-text role="ref"}.

A heightmap collision shape can also be built by using an
`Image<class_Image>`{.interpreted-text role="ref"} reference:

:::: tabs
::: code-tab
gdscript

var heightmap_texture =
ResourceLoader.load(\"res://heightmap_image.exr\") var heightmap_image =
heightmap_texture.get_image() heightmap_image.convert(Image.FORMAT_RF)

var height_min = 0.0 var height_max = 10.0

update_map_data_from_image(heightmap_image, height_min, height_max)
:::
::::

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

:::: {#class_HeightMapShape3D_property_map_data}
::: rst-class
classref-property
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **map_data** = `PackedFloat32Array(0, 0, 0, 0)`
`🔗<class_HeightMapShape3D_property_map_data>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_map_data**(value:
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"})
- `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} **get_map_data**()

Height map data. The array\'s size must be equal to
`map_width<class_HeightMapShape3D_property_map_width>`{.interpreted-text
role="ref"} multiplied by
`map_depth<class_HeightMapShape3D_property_map_depth>`{.interpreted-text
role="ref"}.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HeightMapShape3D_property_map_depth}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **map_depth** = `2`
`🔗<class_HeightMapShape3D_property_map_depth>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_map_depth**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_map_depth**()

Number of vertices in the depth of the height map. Changing this will
resize the
`map_data<class_HeightMapShape3D_property_map_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HeightMapShape3D_property_map_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **map_width** = `2`
`🔗<class_HeightMapShape3D_property_map_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_map_width**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_map_width**()

Number of vertices in the width of the height map. Changing this will
resize the
`map_data<class_HeightMapShape3D_property_map_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_HeightMapShape3D_method_get_max_height}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_max_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_HeightMapShape3D_method_get_max_height>`{.interpreted-text
role="ref"}

Returns the largest height value found in
`map_data<class_HeightMapShape3D_property_map_data>`{.interpreted-text
role="ref"}. Recalculates only when
`map_data<class_HeightMapShape3D_property_map_data>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HeightMapShape3D_method_get_min_height}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_min_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_HeightMapShape3D_method_get_min_height>`{.interpreted-text
role="ref"}

Returns the smallest height value found in
`map_data<class_HeightMapShape3D_property_map_data>`{.interpreted-text
role="ref"}. Recalculates only when
`map_data<class_HeightMapShape3D_property_map_data>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HeightMapShape3D_method_update_map_data_from_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_map_data_from_image**(image:
`Image<class_Image>`{.interpreted-text role="ref"}, height_min:
`float<class_float>`{.interpreted-text role="ref"}, height_max:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_HeightMapShape3D_method_update_map_data_from_image>`{.interpreted-text
role="ref"}

Updates
`map_data<class_HeightMapShape3D_property_map_data>`{.interpreted-text
role="ref"} with data read from an
`Image<class_Image>`{.interpreted-text role="ref"} reference.
Automatically resizes heightmap
`map_width<class_HeightMapShape3D_property_map_width>`{.interpreted-text
role="ref"} and
`map_depth<class_HeightMapShape3D_property_map_depth>`{.interpreted-text
role="ref"} to fit the full image width and height.

The image needs to be in either
`Image.FORMAT_RF<class_Image_constant_FORMAT_RF>`{.interpreted-text
role="ref"} (32 bit),
`Image.FORMAT_RH<class_Image_constant_FORMAT_RH>`{.interpreted-text
role="ref"} (16 bit), or
`Image.FORMAT_R8<class_Image_constant_FORMAT_R8>`{.interpreted-text
role="ref"} (8 bit).

Each image pixel is read in as a float on the range from `0.0` (black
pixel) to `1.0` (white pixel). This range value gets remapped to
`height_min` and `height_max` to form the final height value.

\*\*Note:\*\* Using a heightmap with 16-bit or 32-bit data, stored in
EXR or HDR format is recommended. Using 8-bit height data, or a format
like PNG that Godot imports as 8-bit, will result in a terraced terrain.
