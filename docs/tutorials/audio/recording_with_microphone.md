article_outdated
:   True

# Recording with microphone {#doc_recording_with_microphone}

Godot supports in-game audio recording for Windows, macOS, Linux,
Android and iOS.

A simple demo is included in the official demo projects and will be used
as support for this tutorial:
<https://github.com/godotengine/godot-demo-projects/tree/master/audio/mic_record>.

You will need to enable audio input in the
`Audio > Driver > Enable Input<class_ProjectSettings_property_audio/driver/enable_input>`{.interpreted-text
role="ref"} project setting, or you\'ll just get empty audio files.

## The structure of the demo

The demo consists of a single scene. This scene includes two major
parts: the GUI and the audio.

We will focus on the audio part. In this demo, a bus named `Record` with
the effect `Record` is created to handle the audio recording. An
`AudioStreamPlayer` named `AudioStreamRecord` is used for recording.

![image](img/record_bus.png)

![image](img/record_stream_player.png)

:::: tabs
.. code-tab:: gdscript GDScript

var effect var recording

func [ready]{#ready}():

:   \# We get the index of the \"Record\" bus. var idx =
    AudioServer.get_bus_index(\"Record\") \# And use it to retrieve its
    first effect, which has been defined \# as an \"AudioEffectRecord\"
    resource. effect = AudioServer.get_bus_effect(idx, 0)

::: code-tab
csharp
:::

private AudioEffectRecord [effect]{#effect}; private AudioStreamSample
[recording]{#recording};

public override void [Ready]{#ready}() { // We get the index of the
\"Record\" bus. int idx = AudioServer.GetBusIndex(\"Record\"); // And
use it to retrieve its first effect, which has been defined // as an
\"AudioEffectRecord\" resource. [effect]{#effect} =
(AudioEffectRecord)AudioServer.GetBusEffect(idx, 0); }
::::

The audio recording is handled by the
`class_AudioEffectRecord`{.interpreted-text role="ref"} resource which
has three methods:
`get_recording() <class_AudioEffectRecord_method_get_recording>`{.interpreted-text
role="ref"},
`is_recording_active() <class_AudioEffectRecord_method_is_recording_active>`{.interpreted-text
role="ref"}, and
`set_recording_active() <class_AudioEffectRecord_method_set_recording_active>`{.interpreted-text
role="ref"}.

:::: tabs
.. code-tab:: gdscript GDScript

func [on_record_button_pressed]{#on_record_button_pressed}():

:   

    if effect.is_recording_active():

    :   recording = effect.get_recording() \$PlayButton.disabled = false
        \$SaveButton.disabled = false effect.set_recording_active(false)
        \$RecordButton.text = \"Record\" \$Status.text = \"\"

    else:

    :   \$PlayButton.disabled = true \$SaveButton.disabled = true
        effect.set_recording_active(true) \$RecordButton.text = \"Stop\"
        \$Status.text = \"Recording\...\"

::: code-tab
csharp
:::

private void OnRecordButtonPressed() { if
([effect.IsRecordingActive]{#effect.isrecordingactive}()) {
[recording]{#recording} = [effect.GetRecording]{#effect.getrecording}();
GetNode\<Button\>(\"PlayButton\").Disabled = false;
GetNode\<Button\>(\"SaveButton\").Disabled = false;
[effect.SetRecordingActive]{#effect.setrecordingactive}(false);
GetNode\<Button\>(\"RecordButton\").Text = \"Record\";
GetNode\<Label\>(\"Status\").Text = \"\"; } else {
GetNode\<Button\>(\"PlayButton\").Disabled = true;
GetNode\<Button\>(\"SaveButton\").Disabled = true;
[effect.SetRecordingActive]{#effect.setrecordingactive}(true);
GetNode\<Button\>(\"RecordButton\").Text = \"Stop\";
GetNode\<Label\>(\"Status\").Text = \"Recording\...\"; } }
::::

At the start of the demo, the recording effect is not active. When the
user presses the `RecordButton`, the effect is enabled with
`set_recording_active(true)`.

On the next button press, as `effect.is_recording_active()` is `true`,
the recorded stream can be stored into the `recording` variable by
calling `effect.get_recording()`.

:::: tabs
.. code-tab:: gdscript GDScript

func [on_play_button_pressed]{#on_play_button_pressed}():

:   print(recording) print(recording.format) print(recording.mix_rate)
    print(recording.stereo) var data = recording.get_data()
    print(data.size()) \$AudioStreamPlayer.stream = recording
    \$AudioStreamPlayer.play()

::: code-tab
csharp
:::

private void OnPlayButtonPressed() { GD.Print([recording]{#recording});
GD.Print([recording.Format]{#recording.format});
GD.Print([recording.MixRate]{#recording.mixrate});
GD.Print([recording.Stereo]{#recording.stereo}); byte\[\] data =
[recording.Data]{#recording.data}; GD.Print(data.Length); var
audioStreamPlayer = GetNode\<AudioStreamPlayer\>(\"AudioStreamPlayer\");
audioStreamPlayer.Stream = [recording]{#recording};
audioStreamPlayer.Play(); }
::::

To playback the recording, you assign the recording as the stream of the
`AudioStreamPlayer` and call `play()`.

:::: tabs
.. code-tab:: gdscript GDScript

func [on_save_button_pressed]{#on_save_button_pressed}():

:   var save_path = \$SaveButton/Filename.text
    recording.save_to_wav(save_path) \$Status.text = \"Saved WAV file
    to: %sn(%s)\" % \[save_path,
    ProjectSettings.globalize_path(save_path)\]

::: code-tab
csharp
:::

private void OnSaveButtonPressed() { string savePath =
GetNode\<LineEdit\>(\"SaveButton/Filename\").Text;
[recording.SaveToWav]{#recording.savetowav}(savePath);
GetNode\<Label\>(\"Status\").Text = string.Format(\"Saved WAV file to:
{0}n({1})\", savePath, ProjectSettings.GlobalizePath(savePath)); }
::::

To save the recording, you call `save_to_wav()` with the path to a file.
In this demo, the path is defined by the user via a `LineEdit` input
box.
