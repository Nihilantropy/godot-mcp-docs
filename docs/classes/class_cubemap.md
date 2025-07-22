github_url
:   hide

# Cubemap {#class_Cubemap}

**Inherits:**
`ImageTextureLayered<class_ImageTextureLayered>`{.interpreted-text
role="ref"} **\<**
`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Six square textures representing the faces of a cube. Commonly used as a
skybox.

::: rst-class
classref-introduction-group
:::

## Description

A cubemap is made of 6 textures organized in layers. They are typically
used for faking reflections in 3D rendering (see
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}).
It can be used to make an object look as if it\'s reflecting its
surroundings. This usually delivers much better performance than other
reflection methods.

This resource is typically used as a uniform in custom shaders. Few core
Godot methods make use of **Cubemap** resources.

To create such a texture file yourself, reimport your image files using
the Godot Editor import presets. To create a Cubemap from code, use
`ImageTextureLayered.create_from_images()<class_ImageTextureLayered_method_create_from_images>`{.interpreted-text
role="ref"} on an instance of the Cubemap class.

The expected image order is X+, X-, Y+, Y-, Z+, Z- (in Godot\'s
coordinate system, so Y+ is \"up\" and Z- is \"forward\"). You can use
one of the following templates as a base:

- [2×3 cubemap template (default layout
  option)](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_2x3.webp)
- [3×2 cubemap
  template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_3x2.webp)
- [1×6 cubemap
  template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_1x6.webp)
- [6×1 cubemap
  template](https://raw.githubusercontent.com/godotengine/godot-docs/master/tutorials/assets_pipeline/img/cubemap_template_6x1.webp)

\*\*Note:\*\* Godot doesn\'t support using cubemaps in a
`PanoramaSkyMaterial<class_PanoramaSkyMaterial>`{.interpreted-text
role="ref"}. To use a cubemap as a skybox, convert the default
`PanoramaSkyMaterial<class_PanoramaSkyMaterial>`{.interpreted-text
role="ref"} to a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}
using the **Convert to ShaderMaterial** resource dropdown option, then
replace its code with the following:

``` text
shader_type sky;

uniform samplerCube source_panorama : filter_linear, source_color, hint_default_black;
uniform float exposure : hint_range(0, 128) = 1.0;

void sky() {
    // If importing a cubemap from another engine, you may need to flip one of the `EYEDIR` components below
    // by replacing it with `-EYEDIR`.
    vec3 eyedir = vec3(EYEDIR.x, EYEDIR.y, EYEDIR.z);
    COLOR = texture(source_panorama, eyedir).rgb * exposure;
}
```

After replacing the shader code and saving, specify the imported Cubemap
resource in the Shader Parameters section of the ShaderMaterial in the
inspector.

Alternatively, you can use [this
tool](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html)
to convert a cubemap to an equirectangular sky map and use
`PanoramaSkyMaterial<class_PanoramaSkyMaterial>`{.interpreted-text
role="ref"} as usual.

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

:::: {#class_Cubemap_method_create_placeholder}
::: rst-class
classref-method
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**create_placeholder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Cubemap_method_create_placeholder>`{.interpreted-text
role="ref"}

Creates a placeholder version of this resource
(`PlaceholderCubemap<class_PlaceholderCubemap>`{.interpreted-text
role="ref"}).
