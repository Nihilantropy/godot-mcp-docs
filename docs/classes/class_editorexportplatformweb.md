github_url
:   hide

# EditorExportPlatformWeb {#class_EditorExportPlatformWeb}

**Inherits:**
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Exporter for the Web.

::: rst-class
classref-introduction-group
:::

## Description

The Web exporter customizes how a web build is handled. In the editor\'s
\"Export\" window, it is created when adding a new \"Web\" preset.

\*\*Note:\*\* Godot on Web is rendered inside a `<canvas>` tag.
Normally, the canvas cannot be positioned or resized manually, but
otherwise acts as the main `Window<class_Window>`{.interpreted-text
role="ref"} of the application.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Exporting for the Web <../tutorials/export/exporting_for_web>`{.interpreted-text
  role="doc"}
- `Web documentation index <../tutorials/platform/web/index>`{.interpreted-text
  role="doc"}

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

:::: {#class_EditorExportPlatformWeb_property_custom_template/debug}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/debug**
`🔗<class_EditorExportPlatformWeb_property_custom_template/debug>`{.interpreted-text
role="ref"}

File path to the custom export template used for debug builds. If left
empty, the default template is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_custom_template/release}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_template/release**
`🔗<class_EditorExportPlatformWeb_property_custom_template/release>`{.interpreted-text
role="ref"}

File path to the custom export template used for release builds. If left
empty, the default template is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_html/canvas_resize_policy}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**html/canvas_resize_policy**
`🔗<class_EditorExportPlatformWeb_property_html/canvas_resize_policy>`{.interpreted-text
role="ref"}

Determines how the canvas should be resized by Godot.

- **None:** The canvas is not automatically resized.
- **Project:** The size of the canvas is dependent on the
  `ProjectSettings<class_ProjectSettings>`{.interpreted-text
  role="ref"}.
- **Adaptive:** The canvas is automatically resized to fit as much of
  the web page as possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_html/custom_html_shell}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**html/custom_html_shell**
`🔗<class_EditorExportPlatformWeb_property_html/custom_html_shell>`{.interpreted-text
role="ref"}

The custom HTML page that wraps the exported web build. If left empty,
the default HTML shell is used.

For more information, see the
`Customizing HTML5 Shell <../tutorials/platform/web/customizing_html5_shell>`{.interpreted-text
role="doc"} tutorial.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_html/experimental_virtual_keyboard}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**html/experimental_virtual_keyboard**
`🔗<class_EditorExportPlatformWeb_property_html/experimental_virtual_keyboard>`{.interpreted-text
role="ref"}

**Experimental:** This property may be changed or removed in future
versions.

If `true`, embeds support for a virtual keyboard into the web page,
which is shown when necessary on touchscreen devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_html/export_icon}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **html/export_icon**
`🔗<class_EditorExportPlatformWeb_property_html/export_icon>`{.interpreted-text
role="ref"}

If `true`, the project icon will be used as the favicon for this
application\'s web page.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_html/focus_canvas_on_start}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**html/focus_canvas_on_start**
`🔗<class_EditorExportPlatformWeb_property_html/focus_canvas_on_start>`{.interpreted-text
role="ref"}

If `true`, the canvas will be focused as soon as the application is
loaded, if the browser window is already in focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_html/head_include}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**html/head_include**
`🔗<class_EditorExportPlatformWeb_property_html/head_include>`{.interpreted-text
role="ref"}

Additional HTML tags to include inside the `<head>`, such as `<meta>`
tags.

\*\*Note:\*\* You do not need to add a `<title>` tag, as it is
automatically included based on the project\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_progressive_web_app/background_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**progressive_web_app/background_color**
`🔗<class_EditorExportPlatformWeb_property_progressive_web_app/background_color>`{.interpreted-text
role="ref"}

The background color used behind the web application.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_progressive_web_app/display}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**progressive_web_app/display**
`🔗<class_EditorExportPlatformWeb_property_progressive_web_app/display>`{.interpreted-text
role="ref"}

The [display
mode](https://developer.mozilla.org/en-US/docs/Web/Manifest/display/) to
use for this progressive web application. Different browsers and
platforms may not behave the same.

- **Fullscreen:** Displays the app in fullscreen and hides all of the
  browser\'s UI elements.
- **Standalone:** Displays the app in a separate window and hides all of
  the browser\'s UI elements.
- **Minimal UI:** Displays the app in a separate window and only shows
  the browser\'s UI elements for navigation.
- **Browser:** Displays the app as a normal web page.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_progressive_web_app/enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**progressive_web_app/enabled**
`🔗<class_EditorExportPlatformWeb_property_progressive_web_app/enabled>`{.interpreted-text
role="ref"}

If `true`, turns this web build into a [progressive web
application](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_progressive_web_app/ensure_cross_origin_isolation_headers}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**progressive_web_app/ensure_cross_origin_isolation_headers**
`🔗<class_EditorExportPlatformWeb_property_progressive_web_app/ensure_cross_origin_isolation_headers>`{.interpreted-text
role="ref"}

When enabled, the progressive web app will make sure that each request
has cross-origin isolation headers (COEP/COOP).

This can simplify the setup to serve the exported game.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_progressive_web_app/icon_144x144}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**progressive_web_app/icon_144x144**
`🔗<class_EditorExportPlatformWeb_property_progressive_web_app/icon_144x144>`{.interpreted-text
role="ref"}

File path to the smallest icon for this web application. If not defined,
defaults to the project icon.

\*\*Note:\*\* If the icon is not 144×144, it will be automatically
resized for the final build.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_progressive_web_app/icon_180x180}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**progressive_web_app/icon_180x180**
`🔗<class_EditorExportPlatformWeb_property_progressive_web_app/icon_180x180>`{.interpreted-text
role="ref"}

File path to the small icon for this web application. If not defined,
defaults to the project icon.

\*\*Note:\*\* If the icon is not 180×180, it will be automatically
resized for the final build.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_progressive_web_app/icon_512x512}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**progressive_web_app/icon_512x512**
`🔗<class_EditorExportPlatformWeb_property_progressive_web_app/icon_512x512>`{.interpreted-text
role="ref"}

File path to the largest icon for this web application. If not defined,
defaults to the project icon.

\*\*Note:\*\* If the icon is not 512×512, it will be automatically
resized for the final build.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_progressive_web_app/offline_page}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**progressive_web_app/offline_page**
`🔗<class_EditorExportPlatformWeb_property_progressive_web_app/offline_page>`{.interpreted-text
role="ref"}

The page to display, should the server hosting the page not be
available. This page is saved in the client\'s machine.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_progressive_web_app/orientation}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**progressive_web_app/orientation**
`🔗<class_EditorExportPlatformWeb_property_progressive_web_app/orientation>`{.interpreted-text
role="ref"}

The orientation to use when the web application is run through a mobile
device.

- **Any:** No orientation is forced.
- **Landscape:** Forces a horizontal layout (wider than it is taller).
- **Portrait:** Forces a vertical layout (taller than it is wider).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_threads/emscripten_pool_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**threads/emscripten_pool_size**
`🔗<class_EditorExportPlatformWeb_property_threads/emscripten_pool_size>`{.interpreted-text
role="ref"}

The number of threads that emscripten will allocate at startup. A
smaller value will allocate fewer threads and consume fewer system
resources, but you may run the risk of running out of threads in the
pool and needing to allocate more threads at run time which may cause a
deadlock.

\*\*Note:\*\* Some browsers have a hard cap on the number of threads
that can be allocated, so it is best to be cautious and keep this number
low.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_threads/godot_pool_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**threads/godot_pool_size**
`🔗<class_EditorExportPlatformWeb_property_threads/godot_pool_size>`{.interpreted-text
role="ref"}

Override for the default size of the
`WorkerThreadPool<class_WorkerThreadPool>`{.interpreted-text
role="ref"}. This setting is used when
`ProjectSettings.threading/worker_pool/max_threads<class_ProjectSettings_property_threading/worker_pool/max_threads>`{.interpreted-text
role="ref"} size is set to -1 (which it is by default). This size must
be smaller than
`threads/emscripten_pool_size<class_EditorExportPlatformWeb_property_threads/emscripten_pool_size>`{.interpreted-text
role="ref"} otherwise deadlocks may occur.

When using threads this size needs to be large enough to accommodate
features that rely on having a dedicated thread like
`ProjectSettings.physics/2d/run_on_separate_thread<class_ProjectSettings_property_physics/2d/run_on_separate_thread>`{.interpreted-text
role="ref"} or
`ProjectSettings.rendering/driver/threads/thread_model<class_ProjectSettings_property_rendering/driver/threads/thread_model>`{.interpreted-text
role="ref"}. In general, it is best to ensure that this is at least 4
and is at least 2 or 3 less than
`threads/emscripten_pool_size<class_EditorExportPlatformWeb_property_threads/emscripten_pool_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_variant/extensions_support}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**variant/extensions_support**
`🔗<class_EditorExportPlatformWeb_property_variant/extensions_support>`{.interpreted-text
role="ref"}

If `true` enables `GDExtension<class_GDExtension>`{.interpreted-text
role="ref"} support for this web build.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_variant/thread_support}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**variant/thread_support**
`🔗<class_EditorExportPlatformWeb_property_variant/thread_support>`{.interpreted-text
role="ref"}

If `true`, the exported game will support threads. It requires [a
\"cross-origin isolated\" website](https://web.dev/articles/coop-coep),
which may be difficult to set up and is limited for security reasons
(such as not being able to communicate with third-party websites).

If `false`, the exported game will not support threads. As a result, it
is more prone to performance and audio issues, but will only require to
be run on an HTTPS website.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_vram_texture_compression/for_desktop}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**vram_texture_compression/for_desktop**
`🔗<class_EditorExportPlatformWeb_property_vram_texture_compression/for_desktop>`{.interpreted-text
role="ref"}

If `true`, allows textures to be optimized for desktop through the
S3TC/BPTC algorithm.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatformWeb_property_vram_texture_compression/for_mobile}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**vram_texture_compression/for_mobile**
`🔗<class_EditorExportPlatformWeb_property_vram_texture_compression/for_mobile>`{.interpreted-text
role="ref"}

If `true` allows textures to be optimized for mobile through the
ETC2/ASTC algorithm.
