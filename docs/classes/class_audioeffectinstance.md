github_url
:   hide

# AudioEffectInstance {#class_AudioEffectInstance}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AudioEffectSpectrumAnalyzerInstance<class_AudioEffectSpectrumAnalyzerInstance>`{.interpreted-text
role="ref"}

Manipulates the audio it receives for a given effect.

::: rst-class
classref-introduction-group
:::

## Description

An audio effect instance manipulates the audio it receives for a given
effect. This instance is automatically created by an
`AudioEffect<class_AudioEffect>`{.interpreted-text role="ref"} when it
is added to a bus, and should usually not be created directly. If
necessary, it can be fetched at run-time with
`AudioServer.get_bus_effect_instance()<class_AudioServer_method_get_bus_effect_instance>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`{.interpreted-text
  role="doc"}

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

:::: {#class_AudioEffectInstance_private_method__process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_process**(src_buffer: `const void*`, dst_buffer: `AudioFrame*`,
frame_count: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectInstance_private_method__process>`{.interpreted-text
role="ref"}

Called by the `AudioServer<class_AudioServer>`{.interpreted-text
role="ref"} to process this effect. When
`_process_silence()<class_AudioEffectInstance_private_method__process_silence>`{.interpreted-text
role="ref"} is not overridden or it returns `false`, this method is
called only when the bus is active.

\*\*Note:\*\* It is not useful to override this method in GDScript or
C#. Only GDExtension can take advantage of it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AudioEffectInstance_private_method__process_silence}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_process_silence**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffectInstance_private_method__process_silence>`{.interpreted-text
role="ref"}

Override this method to customize the processing behavior of this effect
instance.

Should return `true` to force the
`AudioServer<class_AudioServer>`{.interpreted-text role="ref"} to always
call
`_process()<class_AudioEffectInstance_private_method__process>`{.interpreted-text
role="ref"}, even if the bus has been muted or cannot otherwise be
heard.
