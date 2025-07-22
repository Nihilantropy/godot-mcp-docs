github_url
:   hide

# TextureLayeredRD {#class_TextureLayeredRD}

**Inherits:** `TextureLayered<class_TextureLayered>`{.interpreted-text
role="ref"} **\<** `Texture<class_Texture>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`Texture2DArrayRD<class_Texture2DArrayRD>`{.interpreted-text
role="ref"},
`TextureCubemapArrayRD<class_TextureCubemapArrayRD>`{.interpreted-text
role="ref"},
`TextureCubemapRD<class_TextureCubemapRD>`{.interpreted-text role="ref"}

Abstract base class for layered texture RD types.

::: rst-class
classref-introduction-group
:::

## Description

Base class for
`Texture2DArrayRD<class_Texture2DArrayRD>`{.interpreted-text
role="ref"},
`TextureCubemapRD<class_TextureCubemapRD>`{.interpreted-text role="ref"}
and
`TextureCubemapArrayRD<class_TextureCubemapArrayRD>`{.interpreted-text
role="ref"}. Cannot be used directly, but contains all the functions
necessary for accessing the derived resource types.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TextureLayeredRD_property_texture_rd_rid}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **texture_rd_rid**
`🔗<class_TextureLayeredRD_property_texture_rd_rid>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_rd_rid**(value: `RID<class_RID>`{.interpreted-text
  role="ref"})
- `RID<class_RID>`{.interpreted-text role="ref"}
  **get_texture_rd_rid**()

The RID of the texture object created on the
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.
