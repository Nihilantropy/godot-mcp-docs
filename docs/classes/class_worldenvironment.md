github_url
:   hide

::: {.meta keywords="background, sky"}
:::

# WorldEnvironment {#class_WorldEnvironment}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Default environment properties for the entire scene (post-processing
effects, lighting and background settings).

::: rst-class
classref-introduction-group
:::

## Description

The **WorldEnvironment** node is used to configure the default
`Environment<class_Environment>`{.interpreted-text role="ref"} for the
scene.

The parameters defined in the **WorldEnvironment** can be overridden by
an `Environment<class_Environment>`{.interpreted-text role="ref"} node
set on the current `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"}. Additionally, only one **WorldEnvironment** may be
instantiated in a given scene at a time.

The **WorldEnvironment** allows the user to specify default lighting
parameters (e.g. ambient lighting), various post-processing effects
(e.g. SSAO, DOF, Tonemapping), and how to draw the background (e.g.
solid color, skybox). Usually, these are added in order to improve the
realism/color balance of the scene.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Environment and post-processing <../tutorials/3d/environment_and_post_processing>`{.interpreted-text
  role="doc"}
- [3D Material Testers
  Demo](https://godotengine.org/asset-library/asset/2742)
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

:::: {#class_WorldEnvironment_property_camera_attributes}
::: rst-class
classref-property
:::
::::

`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
**camera_attributes**
`🔗<class_WorldEnvironment_property_camera_attributes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_camera_attributes**(value:
  `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"})
- `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"} **get_camera_attributes**()

The default `CameraAttributes<class_CameraAttributes>`{.interpreted-text
role="ref"} resource to use if none set on the
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorldEnvironment_property_compositor}
::: rst-class
classref-property
:::
::::

`Compositor<class_Compositor>`{.interpreted-text role="ref"}
**compositor**
`🔗<class_WorldEnvironment_property_compositor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_compositor**(value:
  `Compositor<class_Compositor>`{.interpreted-text role="ref"})
- `Compositor<class_Compositor>`{.interpreted-text role="ref"}
  **get_compositor**()

The default `Compositor<class_Compositor>`{.interpreted-text role="ref"}
resource to use if none set on the
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorldEnvironment_property_environment}
::: rst-class
classref-property
:::
::::

`Environment<class_Environment>`{.interpreted-text role="ref"}
**environment**
`🔗<class_WorldEnvironment_property_environment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_environment**(value:
  `Environment<class_Environment>`{.interpreted-text role="ref"})
- `Environment<class_Environment>`{.interpreted-text role="ref"}
  **get_environment**()

The `Environment<class_Environment>`{.interpreted-text role="ref"}
resource used by this **WorldEnvironment**, defining the default
properties.
