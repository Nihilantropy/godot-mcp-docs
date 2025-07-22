# KDevelop {#doc_configuring_an_ide_kdevelop}

[KDevelop](https://www.kdevelop.org) is a free, open source IDE for all
desktop platforms.

## Importing the project

- From the KDevelop\'s main screen select **Open Project**.

<figure class="figure-w480 align-center">
<img src="img/kdevelop_newproject.png"
alt="img/kdevelop_newproject.png" />
<figcaption>KDevelop's main screen.</figcaption>
</figure>

- Navigate to the Godot root folder and select it.
- On the next screen, choose **Custom Build System** for the **Project
  Manager**.

<figure class="figure-w480 align-center">
<img src="img/kdevelop_custombuild.png"
alt="img/kdevelop_custombuild.png" />
</figure>

- After the project has been imported, open the project configuration by
  right-clicking on it in the **Projects** panel and selecting **Open
  Configuration..** option.

<figure class="figure-w480 align-center">
<img src="img/kdevelop_openconfig.png"
alt="img/kdevelop_openconfig.png" />
</figure>

- Under **Language Support** open the **Includes/Imports** tab and add
  the following paths:

  ``` none
  .  // A dot, to indicate the root of the Godot project
  core/
  core/os/
  core/math/
  drivers/
  platform/<your_platform>/  // Replace <your_platform> with a folder
                                corresponding to your current platform
  ```

<figure class="figure-w480 align-center">
<img src="img/kdevelop_addincludes.png"
alt="img/kdevelop_addincludes.png" />
</figure>

- Apply the changes.

- Under **Custom Build System** add a new build configuration with the
  following settings:

    ------------- ---------------------------------------------------------
    Build         *blank*
    Directory     

    Enable        **True**

    Executable    **scons**

    Arguments     See
                  `doc_introduction_to_the_buildsystem`{.interpreted-text
                  role="ref"} for a full list of arguments.
    ------------- ---------------------------------------------------------

<figure class="figure-w480 align-center">
<img src="img/kdevelop_buildconfig.png"
alt="img/kdevelop_buildconfig.png" />
</figure>

- Apply the changes and close the configuration window.

## Debugging the project

- Select **Run \> Configure Launches\...** from the top menu.

<figure class="figure-w480 align-center">
<img src="img/kdevelop_configlaunches.png"
alt="img/kdevelop_configlaunches.png" />
</figure>

- Click **Add** to create a new launch configuration.
- Select **Executable** option and specify the path to your executable
  located in the `<Godot root directory>/bin` folder. The name depends
  on your build configuration, e.g. `godot.linuxbsd.editor.dev.x86_64`
  for 64-bit LinuxBSD platform with `platform=editor` and
  `dev_build=yes`.

<figure class="figure-w480 align-center">
<img src="img/kdevelop_configlaunches2.png"
alt="img/kdevelop_configlaunches2.png" />
</figure>

If you run into any issues, ask for help in one of [Godot\'s community
channels](https://godotengine.org/community).
