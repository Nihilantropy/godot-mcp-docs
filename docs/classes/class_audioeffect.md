github_url
:   hide

# AudioEffect {#class_AudioEffect}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AudioEffectAmplify<class_AudioEffectAmplify>`{.interpreted-text
role="ref"},
`AudioEffectCapture<class_AudioEffectCapture>`{.interpreted-text
role="ref"},
`AudioEffectChorus<class_AudioEffectChorus>`{.interpreted-text
role="ref"},
`AudioEffectCompressor<class_AudioEffectCompressor>`{.interpreted-text
role="ref"},
`AudioEffectDelay<class_AudioEffectDelay>`{.interpreted-text
role="ref"},
`AudioEffectDistortion<class_AudioEffectDistortion>`{.interpreted-text
role="ref"}, `AudioEffectEQ<class_AudioEffectEQ>`{.interpreted-text
role="ref"},
`AudioEffectFilter<class_AudioEffectFilter>`{.interpreted-text
role="ref"},
`AudioEffectHardLimiter<class_AudioEffectHardLimiter>`{.interpreted-text
role="ref"},
`AudioEffectLimiter<class_AudioEffectLimiter>`{.interpreted-text
role="ref"},
`AudioEffectPanner<class_AudioEffectPanner>`{.interpreted-text
role="ref"},
`AudioEffectPhaser<class_AudioEffectPhaser>`{.interpreted-text
role="ref"},
`AudioEffectPitchShift<class_AudioEffectPitchShift>`{.interpreted-text
role="ref"},
`AudioEffectRecord<class_AudioEffectRecord>`{.interpreted-text
role="ref"},
`AudioEffectReverb<class_AudioEffectReverb>`{.interpreted-text
role="ref"},
`AudioEffectSpectrumAnalyzer<class_AudioEffectSpectrumAnalyzer>`{.interpreted-text
role="ref"},
`AudioEffectStereoEnhance<class_AudioEffectStereoEnhance>`{.interpreted-text
role="ref"}

Base class for audio effect resources.

::: rst-class
classref-introduction-group
:::

## Description

The base `Resource<class_Resource>`{.interpreted-text role="ref"} for
every audio effect. In the editor, an audio effect can be added to the
current bus layout through the Audio panel. At run-time, it is also
possible to manipulate audio effects through
`AudioServer.add_bus_effect()<class_AudioServer_method_add_bus_effect>`{.interpreted-text
role="ref"},
`AudioServer.remove_bus_effect()<class_AudioServer_method_remove_bus_effect>`{.interpreted-text
role="ref"}, and
`AudioServer.get_bus_effect()<class_AudioServer_method_get_bus_effect>`{.interpreted-text
role="ref"}.

When applied on a bus, an audio effect creates a corresponding
`AudioEffectInstance<class_AudioEffectInstance>`{.interpreted-text
role="ref"}. The instance is directly responsible for manipulating the
sound, based on the original audio effect\'s properties.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`{.interpreted-text
  role="doc"}
- [Audio Microphone Record
  Demo](https://godotengine.org/asset-library/asset/2760)

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

:::: {#class_AudioEffect_private_method__instantiate}
::: rst-class
classref-method
:::
::::

`AudioEffectInstance<class_AudioEffectInstance>`{.interpreted-text
role="ref"} **\_instantiate**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_AudioEffect_private_method__instantiate>`{.interpreted-text
role="ref"}

Override this method to customize the
`AudioEffectInstance<class_AudioEffectInstance>`{.interpreted-text
role="ref"} created when this effect is applied on a bus in the
editor\'s Audio panel, or through
`AudioServer.add_bus_effect()<class_AudioServer_method_add_bus_effect>`{.interpreted-text
role="ref"}.

    extends AudioEffect

    @export var strength = 4.0

    func _instantiate():
        var effect = CustomAudioEffectInstance.new()
        effect.base = self

        return effect

\*\*Note:\*\* It is recommended to keep a reference to the original
**AudioEffect** in the new instance. Depending on the implementation
this allows the effect instance to listen for changes at run-time and be
modified accordingly.
