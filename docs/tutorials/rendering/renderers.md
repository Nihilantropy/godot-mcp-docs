# Renderers {#doc_renderers}

::: seealso
This page gives an overview of Godot\'s renderers, focusing on the
differences between their rendering features. For more technical details
on the renderers, see
`doc_internal_rendering_architecture`{.interpreted-text role="ref"}.
:::

## Introduction

Godot 4 includes three renderers:

- **Forward+**. The most advanced renderer, suited for desktop platforms
  only. Used by default on desktop platforms. This renderer uses
  **Vulkan**, **Direct3D 12**, or **Metal** as the rendering driver, and
  it uses the **RenderingDevice** backend.
- **Mobile**. Fewer features, but renders simple scenes faster. Suited
  for mobile and desktop platforms. Used by default on mobile platforms.
  This renderer uses **Vulkan**, **Direct3D 12**, or **Metal** as the
  rendering driver, and it uses the **RenderingDevice** backend.
- **Compatibility**, sometimes called **GL Compatibility**. The least
  advanced renderer, suited for low-end desktop and mobile platforms.
  Used by default on the web platform. This renderer uses **OpenGL** as
  the rendering driver.

### Renderers, rendering drivers, and RenderingDevice

![](img/renderers_rendering_layers.webp)

The *renderer*, or *rendering method*, determines which features are
available. Most of the time, this is the only thing you need to think
about. Godot\'s renderers are **Forward+**, **Mobile**, and
**Compatibility**.

The *rendering driver* tells the GPU what to do, using a graphics API.
Godot can use the **OpenGL**, **Vulkan**, **Direct3D 12**, and **Metal**
rendering drivers. Not every GPU supports every rendering driver, and
therefore not every GPU supports all renderers. Vulkan, Direct3D 12, and
Metal are modern, low-level graphics APIs, and requires newer hardware.
OpenGL is an older graphics API that runs on most hardware.

RenderingDevice is a *rendering backend*, an abstraction layer between
the renderer and the rendering driver. It is used by the Forward+ and
Mobile renderers, and these renderers are sometimes called
\"RenderingDevice-based renderers\".

## Choosing a renderer

Choosing a renderer is a complex question, and depends on your hardware
and the which platforms you are developing for. As a starting point:

Choose **Forward+** if:

> - You are developing for desktop.
> - You have relatively new hardware which supports Vulkan, Direct3D 12,
>   or Metal.
> - You are developing a 3D game.
> - You want to use the most advanced rendering features.

Choose **Mobile** if:

> - You are developing for newer mobile devices, desktop XR, or desktop.
> - You have relatively new hardware which supports Vulkan, Direct3D 12,
>   or Metal.
> - You are developing a 3D game.
> - You want to use advanced rendering features, subject to the
>   limitations of mobile hardware.

Choose **Compatibility** if:

> - You are developing for older mobile devices, older desktop devices,
>   or standalone XR. The Compatibility renderer supports the widest
>   range of hardware.
> - You are developing for web. In this case, Compatibility is the only
>   choice.
> - You have older hardware which does not support Vulkan. In this case,
>   Compatibility is the only choice.
> - You are developing a 2D game, or a 3D game which does not need
>   advanced rendering features.
> - You want the best performance possible on all devices and don\'t
>   need advanced rendering features.

Keep in mind every game is unique, and this is only a starting point.
For example, you might choose to use the Compatibility renderer even
though you have the latest GPU, so you can support the widest range of
hardware. Or you might want to use the Forward+ renderer for a 2D game,
so you can advanced features like compute shaders.

### Switching between renderers

In the editor, you can always switch between renderers by clicking on
the renderer name in the upper-right corner of the editor.

Switching between renderers may require some manual tweaks to your
scene, lighting, and environment, since each renderer is different. In
general, switching between the Mobile and Forward+ renderers will
require fewer adjustments than switching between the Compatibility
renderer and the Forward+ or Mobile renderers.

Since Godot 4.4, when using Forward+ or Mobile, if Vulkan is not
supported, the engine will fall back to Direct3D 12 and vice versa. If
the attempted fallback driver is not supported either, the engine will
then fall back to Compatibility when the RenderingDevice backend is not
supported. This allows the project to run anyway, but it may look
different than the intended appearance due to the more limited renderer.
This behavior can be disabled in the project settings by unchecking
`Rendering > Rendering Device > Fallback to OpenGL 3<class_ProjectSettings_property_rendering/rendering_device/fallback_to_opengl3>`{.interpreted-text
role="ref"}.

## Feature comparison

This is not a complete list of the features of each renderer. If a
feature is not listed here, it is available in all renderers, though it
may be much faster on some renderers. For a list of *all* features in
Godot, see `doc_list_of_features`{.interpreted-text role="ref"}.

Hardware with RenderingDevice support is hardware which can run Vulkan,
Direct3D 12, or Metal.

### Overall comparison

+--------------+-----------------+-----------------+-----------------+
| Feature      | Compatibility   | Mobile          | Forward+        |
+==============+=================+=================+=================+
| **Required** | Older or        | Newer or        | Newer or        |
| **hardware** | low-end.        | high-end.       | high-end.       |
|              |                 | Requires        | Requires        |
|              |                 | Vulkan,         | Vulkan,         |
|              |                 | Direct3D 12, or | Direct3D 12, or |
|              |                 | Metal support.  | Metal support.  |
+--------------+-----------------+-----------------+-----------------+
| Runs on new  | ✔️ Yes. \| ✔️   |                 |                 |
| hardware     | Yes. \| ✔️ Yes. |                 |                 |
|              | \|              |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| Runs on old  | ✔️ Yes. \| ✔️ Yes |                 |                 |
| and low-end  | , but slower th |                 |                 |
| hardware     | an \| ✔️ Yes, bu |                 |                 |
|              | t slowest of \| |                 |                 |
|              |                 |                 |                 |
|              | :   |           |                 |                 |
|              |  Compatibility. |                 |                 |
|              |       \| all    |                 |                 |
|              |                 |                 |                 |
|              |      renderers. |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| Runs on      | ✔️ Yes. \| ❌ N  |                 |                 |
| hardware     | o. \| ❌ No. \| |                 |                 |
| without      |                 |                 |                 |
| Ren          | :               |                 |                 |
| deringDevice |  |              |                 |                 |
| support      |              \| |                 |                 |
|              |                 |                 |                 |
|              |  |              |                 |                 |
|              |              \| |                 |                 |
|              |                 |                 |                 |
|              |  |              |                 |                 |
|              |              \| |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| **Target     | Mobile, low-end | Mobile,         | Desktop.        |
| platforms**  | desktop, web.   | desktop.        |                 |
+--------------+-----------------+-----------------+-----------------+
| Desktop      | ✔️ Yes. \| ✔️   |                 |                 |
|              | Yes. \| ✔️ Yes. |                 |                 |
|              | \|              |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| Mobile       | ✔️ Yes (         |                 |                 |
|              | low-end). \| ✔️  |                 |                 |
|              | Yes (high-end). |                 |                 |
|              |  \| ⚠️ Supported |                 |                 |
|              | , but poorly \| |                 |                 |
|              |                 |                 |                 |
|              | :               |                 |                 |
|              |  |              |                 |                 |
|              |              \| |                 |                 |
|              |                 |                 |                 |
|              |      optimized. |                 |                 |
|              |       Use       |                 |                 |
|              |       Mobile or |                 |                 |
|              |                 |                 |                 |
|              |  |              |                 |                 |
|              |              \| |                 |                 |
|              |                 |                 |                 |
|              |   Compatibility |                 |                 |
|              |       instead.  |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| XR           | ✔️ Yes.         |                 |                 |
|              | Recommended for |                 |                 |
|              | \| ✔️ Yes.      |                 |                 |
|              | Recommended for |                 |                 |
|              | \| ⚠️           |                 |                 |
|              | Supported, but  |                 |                 |
|              | poorly \|       |                 |                 |
|              | standalone      |                 |                 |
|              | headsets. \|    |                 |                 |
|              | desktop         |                 |                 |
|              | headsets. \|    |                 |                 |
|              | optimized. Use  |                 |                 |
|              | Mobile or \| \| |                 |                 |
|              | Compatibility   |                 |                 |
|              | instead.        |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| Web          | ✔️ Yes. \| ❌   |                 |                 |
|              | No. \| ❌ No.   |                 |                 |
|              | \|              |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| 2D Games     | ✔️ Yes.          |                 |                 |
|              | \| ✔️ Yes, but \ |                 |                 |
|              | | ✔️ Yes, but \| |                 |                 |
|              |                 |                 |                 |
|              | :               |                 |                 |
|              | | Compatibility |                 |                 |
|              |       is        |                 |                 |
|              |       usually   |                 |                 |
|              |       \|        |                 |                 |
|              |                 |                 |                 |
|              |   Compatibility |                 |                 |
|              |       is        |                 |                 |
|              |       usually   |                 |                 |
|              |     | good      |                 |                 |
|              |       enough    |                 |                 |
|              |       for 2D.   |                 |                 |
|              |       \| good   |                 |                 |
|              |       enough    |                 |                 |
|              |       for 2D.   |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| 3D Games     | ✔️ Yes. \| ✔️   |                 |                 |
|              | Yes. \| ✔️ Yes. |                 |                 |
|              | \|              |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| **Feature    | 2D and core 3D  | Most rendering  | All rendering   |
| set**        | features.       | features.       | features.       |
+--------------+-----------------+-----------------+-----------------+
| 2D rendering | ✔️ Yes. \| ✔️ Ye  |                 |                 |
| features     | s. \| ✔️ Yes. \| |                 |                 |
|              |                 |                 |                 |
|              | :               |                 |                 |
|              |  |              |                 |                 |
|              |              \| |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| Core 3D      | ✔️ Yes. \| ✔️ Ye  |                 |                 |
| rendering    | s. \| ✔️ Yes. \| |                 |                 |
| features     |                 |                 |                 |
|              | :               |                 |                 |
|              |  |              |                 |                 |
|              |              \| |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| Advanced     | ❌ No.          | ⚠️ Yes, limited |                 |
| rendering    |                 | by \| ✔️ Yes.   |                 |
| features     |                 | All rendering   |                 |
|              |                 | \| mobile       |                 |
|              |                 | hardware. \|    |                 |
|              |                 | features are    |                 |
|              |                 | supported.      |                 |
+--------------+-----------------+-----------------+-----------------+
| New features | ⚠️ Some new     |                 |                 |
|              | rendering \| ✔️ |                 |                 |
|              | Most new        |                 |                 |
|              | rendering \| ✔️ |                 |                 |
|              | All new         |                 |                 |
|              | features are \| |                 |                 |
|              | features are    |                 |                 |
|              | added to \|     |                 |                 |
|              | features are    |                 |                 |
|              | added to \|     |                 |                 |
|              | added to        |                 |                 |
|              | Forward+. As    |                 |                 |
|              | the             |                 |                 |
|              | Compatibility.  |                 |                 |
|              | Features \|     |                 |                 |
|              | Mobile. Mobile  |                 |                 |
|              | usually \|      |                 |                 |
|              | focus of new    |                 |                 |
|              | development,    |                 |                 |
|              | are added after |                 |                 |
|              | Mobile \| gets  |                 |                 |
|              | new features as |                 |                 |
|              | \| Forward+     |                 |                 |
|              | gets features   |                 |                 |
|              | and Forward+.   |                 |                 |
|              | \| Forward+     |                 |                 |
|              | does. \| first. |                 |                 |
+--------------+-----------------+-----------------+-----------------+
| Rendering    | Low base cost,  | Medium base     | Highest base    |
| cost         | but high        | cost, and       | cost, and low   |
|              | scaling cost.   | medium scaling  | scaling cost.   |
|              |                 | cost.           |                 |
+--------------+-----------------+-----------------+-----------------+
| Rendering    | OpenGL.         | Vulkan,         | Vulkan,         |
| driver       |                 | Direct3D 12, or | Direct3D 12, or |
|              |                 | Metal.          | Metal.          |
+--------------+-----------------+-----------------+-----------------+

### Lights and shadows

See `doc_lights_and_shadows`{.interpreted-text role="ref"} for more
information.

+----------------+----------------+----------------+----------------+
| Feature        | Compatibility  | Mobile         | Forward+       |
+================+================+================+================+
| Lighting       | Forward        | Forward        | Clustered      |
| approach       |                |                | Forward        |
+----------------+----------------+----------------+----------------+
| Maximum        | 8 per mesh.    | 8 per mesh,    | 512 per        |
| OmniLights     | Can be         | 256 per view.  | cluster. Can   |
|                | increased.     |                | be increased.  |
+----------------+----------------+----------------+----------------+
| Maximum        | 8 per mesh.    | 8 per mesh,    | 512 per        |
| SpotLights     | Can be         | 256 per view.  | cluster. Can   |
|                | increased.     |                | be increased.  |
+----------------+----------------+----------------+----------------+
| Maximum        | 8              | 8              | 8              |
| Dir            |                |                |                |
| ectionalLights |                |                |                |
+----------------+----------------+----------------+----------------+
| PCSS for       | ❌ Not         | ✔️ S            |                |
| OmniLight and  | supported.     | upported. \| ✔ |                |
| SpotLight      |                | ️ Supported. \| |                |
|                |                |                |                |
|                |                | :   |          |                |
+----------------+----------------+----------------+----------------+
| PCSS for       | ❌ Not         | ❌ Not         | ✔️ Supported.  |
| Di             | supported.     | supported.     | \|             |
| rectionalLight |                |                |                |
+----------------+----------------+----------------+----------------+
| Light          | ❌ Not         | ✔️ S            |                |
| projector      | supported.     | upported. \| ✔ |                |
| textures       |                | ️ Supported. \| |                |
|                |                |                |                |
|                |                | :   |          |                |
+----------------+----------------+----------------+----------------+

### Global Illumination

See `doc_introduction_to_global_illumination`{.interpreted-text
role="ref"} for more information.

  -----------------------------------------------------------------------
  Feature           Compatibility     Mobile            Forward+
  ----------------- ----------------- ----------------- -----------------
  ReflectionProbe   ✔️ Supported, 2                     
                    per \| ✔️                           
                    Supported, 8 per                    
                    \| ✔️ Supported,                    
                    unlimited. \|                       
                    mesh. \| mesh. \|                   

  LightmapGI        ⚠️ Rendering of                     
                    baked \| ✔️                         
                    Supported. \| ✔️                    
                    Supported. \|                       
                    lightmaps is                        
                    supported. \| \|                    
                    Baking requires                     
                    hardware \| \|                      
                    with                                
                    RenderingDevice                     
                    \| \| support. \|                   
                    \|                                  

  VoxelGI           ❌ Not supported. ❌ Not supported. ✔️ Supported. \|

  Screen-Space      ❌ Not supported. ❌ Not supported. ✔️ Supported. \|
  Indirect Lighting                                     
  (SSIL)                                                

  Signed Distance   ❌ Not supported. ❌ Not supported. ✔️ Supported. \|
  Field Global                                          
  Illumination                                          
  (SDFGI)                                               
  -----------------------------------------------------------------------

### Environment and post-processing

See `doc_environment_and_post_processing`{.interpreted-text role="ref"}
for more information.

+----------------+----------------+----------------+----------------+
| Feature        | Compatibility  | Mobile         | Forward+       |
+================+================+================+================+
| Fog (Depth and | ✔️ Supported.  |                |                |
| Height)        | \| ✔️          |                |                |
|                | Supported. \|  |                |                |
|                | ✔️ Supported.  |                |                |
|                | \|             |                |                |
+----------------+----------------+----------------+----------------+
| Volumetric Fog | ❌ Not         | ❌ Not         | ✔️ Supported.  |
|                | supported.     | supported.     | \|             |
+----------------+----------------+----------------+----------------+
| Tonemapping    | ✔️ Supported.  |                |                |
|                | \| ✔️          |                |                |
|                | Supported. \|  |                |                |
|                | ✔️ Supported.  |                |                |
|                | \|             |                |                |
+----------------+----------------+----------------+----------------+
| Screen-Space   | ❌ Not         | ❌ Not         | ✔️ Supported.  |
| Reflections    | supported.     | supported.     | \|             |
+----------------+----------------+----------------+----------------+
| Screen-Space   | ❌ Not         | ❌ Not         | ✔️ Supported.  |
| Ambient        | supported.     | supported.     | \|             |
| Occlusion      |                |                |                |
| (SSAO)         |                |                |                |
+----------------+----------------+----------------+----------------+
| Screen-Space   | ❌ Not         | ❌ Not         | ✔️ Supported.  |
| Indirect       | supported.     | supported.     | \|             |
| Lighting       |                |                |                |
| (SSIL)         |                |                |                |
+----------------+----------------+----------------+----------------+
| Signed         | ❌ Not         | ❌ Not         | ✔️ Supported.  |
| Distance Field | supported.     | supported.     | \|             |
| Global         |                |                |                |
| Illumination   |                |                |                |
| (SDFGI)        |                |                |                |
+----------------+----------------+----------------+----------------+
| Glow           | ✔️ Supported.  |                |                |
|                | \| ✔️          |                |                |
|                | Supported. \|  |                |                |
|                | ✔️ Supported.  |                |                |
|                | \|             |                |                |
+----------------+----------------+----------------+----------------+
| Adjustments    | ✔️ Supported.  |                |                |
|                | \| ✔️          |                |                |
|                | Supported. \|  |                |                |
|                | ✔️ Supported.  |                |                |
|                | \|             |                |                |
+----------------+----------------+----------------+----------------+
| Custom         | ✔️ Sup          |                |                |
| p              | ported. \| ✔️ S |                |                |
| ost-processing | upported. \| ✔ |                |                |
| with           | ️ Supported. \| |                |                |
| fullscreen     |                |                |                |
| quad           | :   |          |                |                |
|                |                |                |                |
|                |             \| |                |                |
+----------------+----------------+----------------+----------------+
| Custom         | ❌ Not         | ✔️ S            |                |
| p              | supported.     | upported. \| ✔ |                |
| ost-processing |                | ️ Supported. \| |                |
| with           |                |                |                |
| Com            |                | :   |          |                |
| positorEffects |                |                |                |
+----------------+----------------+----------------+----------------+

### Antialiasing

See `doc_3d_antialiasing`{.interpreted-text role="ref"} for more
information.

+------------+-----------------+-----------------+-----------------+
| Feature    | Compatibility   | Mobile          | Forward+        |
+============+=================+=================+=================+
| MSAA 3D    | ✔️ Supported.   |                 |                 |
|            | \| ✔️           |                 |                 |
|            | Supported. \|   |                 |                 |
|            | ✔️ Supported.   |                 |                 |
|            | \|              |                 |                 |
+------------+-----------------+-----------------+-----------------+
| MSAA 2D    | ❌ Not          | ✔️ Supported.   |                 |
|            | supported.      | \| ✔️           |                 |
|            |                 | Supported. \|   |                 |
+------------+-----------------+-----------------+-----------------+
| TAA        | ❌ Not          | ❌ Not          | ✔️ Supported.   |
|            | supported.      | supported.      | \|              |
+------------+-----------------+-----------------+-----------------+
| FSR2       | ❌ Not          | ❌ Not          | ✔️ Supported.   |
|            | supported.      | supported.      | \|              |
+------------+-----------------+-----------------+-----------------+
| FXAA       | ❌ Not          | ✔️ Supported.   |                 |
|            | supported.      | \| ✔️           |                 |
|            |                 | Supported. \|   |                 |
+------------+-----------------+-----------------+-----------------+
| SSAA       | ✔️ Supported.   |                 |                 |
|            | \| ✔️           |                 |                 |
|            | Supported. \|   |                 |                 |
|            | ✔️ Supported.   |                 |                 |
|            | \|              |                 |                 |
+------------+-----------------+-----------------+-----------------+
| Sc         | ❌ Not          | ✔               |                 |
| reen-space | supported.      | ️ Supported. \|  |                 |
| roughness  |                 | ✔️ Supported. \| |                 |
| limiter    |                 |                 |                 |
|            |                 | :   |           |                 |
+------------+-----------------+-----------------+-----------------+

### StandardMaterial features

See `doc_standard_material_3d`{.interpreted-text role="ref"} for more
information.

  ----------------------------------------------------------------------
  Feature          Compatibility     Mobile            Forward+
  ---------------- ----------------- ----------------- -----------------
  Sub-surface      ❌ Not supported. ❌ Not supported. ✔️ Supported. \|
  scattering                                           

  ----------------------------------------------------------------------

### Shader features

See `doc_shading_reference`{.interpreted-text role="ref"} for more
information.

+----------------+----------------+----------------+----------------+
| Feature        | Compatibility  | Mobile         | Forward+       |
+================+================+================+================+
| Screen texture | ✔️ Supported.  |                |                |
|                | \| ✔️          |                |                |
|                | Supported. \|  |                |                |
|                | ✔️ Supported.  |                |                |
|                | \|             |                |                |
+----------------+----------------+----------------+----------------+
| Depth texture  | ✔️ Sup          |                |                |
|                | ported. \| ✔️ S |                |                |
|                | upported. \| ✔ |                |                |
|                | ️ Supported. \| |                |                |
|                |                |                |                |
|                | :   |          |                |                |
|                |                |                |                |
|                |             \| |                |                |
+----------------+----------------+----------------+----------------+
| No             | ❌ Not         | ❌ Not         | ✔️ Supported.  |
| rmal/Roughness | supported.     | supported.     | \|             |
| texture        |                |                |                |
+----------------+----------------+----------------+----------------+
| Compute        | ❌ Not         | ⚠️ Supported,  |                |
| shaders        | supported.     | but comes \|   |                |
|                |                | ✔️ Supported.  |                |
|                |                | \| with a      |                |
|                |                | performance \| |                |
|                |                | penalty on     |                |
|                |                | older          |                |
|                |                | devices.\|     |                |
+----------------+----------------+----------------+----------------+

### Other features

+----------------+----------------+----------------+----------------+
| Feature        | Compatibility  | Mobile         | Forward+       |
+================+================+================+================+
| Variable rate  | ❌ Not         | ✔️ S            |                |
| shading        | supported.     | upported. \| ✔ |                |
|                |                | ️ Supported. \| |                |
|                |                |                |                |
|                |                | :   |          |                |
+----------------+----------------+----------------+----------------+
| Decals         | ❌ Not         | ✔️ Supported.  |                |
|                | supported.     | \| ✔️          |                |
|                |                | Supported. \|  |                |
+----------------+----------------+----------------+----------------+
| Depth of field | ❌ Not         | ✔️ Supported.  |                |
| blur           | supported.     | \| ✔️          |                |
|                |                | Supported. \|  |                |
+----------------+----------------+----------------+----------------+
| Adaptive and   | ❌ Not         | ✔️ S            |                |
| Mailbox VSync  | supported.     | upported. \| ✔ |                |
| modes          |                | ️ Supported. \| |                |
|                |                |                |                |
|                |                | :   |          |                |
+----------------+----------------+----------------+----------------+
| 2D HDR         | ❌ Not         | ✔️ Supported.  |                |
| Viewport       | supported.     | \| ✔️          |                |
|                |                | Supported. \|  |                |
+----------------+----------------+----------------+----------------+
| R              | ❌ Not         | ✔️ S            |                |
| enderingDevice | supported.     | upported. \| ✔ |                |
| access         |                | ️ Supported. \| |                |
|                |                |                |                |
|                |                | :   |          |                |
+----------------+----------------+----------------+----------------+
