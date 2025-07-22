github_url
:   hide

# JavaClassWrapper {#class_JavaClassWrapper}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Provides access to the Java Native Interface.

::: rst-class
classref-introduction-group
:::

## Description

The JavaClassWrapper singleton provides a way for the Godot application
to send and receive data through the [Java Native
Interface](https://developer.android.com/training/articles/perf-jni)
(JNI).

\*\*Note:\*\* This singleton is only available in Android builds.

    var LocalDateTime = JavaClassWrapper.wrap("java.time.LocalDateTime")
    var DateTimeFormatter = JavaClassWrapper.wrap("java.time.format.DateTimeFormatter")

    var datetime = LocalDateTime.now()
    var formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")

    print(datetime.format(formatter))

\*\*Warning:\*\* When calling Java methods, be sure to check
`get_exception()<class_JavaClassWrapper_method_get_exception>`{.interpreted-text
role="ref"} to check if the method threw an exception.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Integrating with Android APIs <../tutorials/platform/android/javaclasswrapper_and_androidruntimeplugin>`{.interpreted-text
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

:::: {#class_JavaClassWrapper_method_get_exception}
::: rst-class
classref-method
:::
::::

`JavaObject<class_JavaObject>`{.interpreted-text role="ref"}
**get_exception**()
`🔗<class_JavaClassWrapper_method_get_exception>`{.interpreted-text
role="ref"}

Returns the Java exception from the last call into a Java class. If
there was no exception, it will return `null`.

\*\*Note:\*\* This method only works on Android. On every other
platform, this method will always return `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaClassWrapper_method_wrap}
::: rst-class
classref-method
:::
::::

`JavaClass<class_JavaClass>`{.interpreted-text role="ref"}
**wrap**(name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_JavaClassWrapper_method_wrap>`{.interpreted-text role="ref"}

Wraps a class defined in Java, and returns it as a
`JavaClass<class_JavaClass>`{.interpreted-text role="ref"}
`Object<class_Object>`{.interpreted-text role="ref"} type that Godot can
interact with.

When wrapping inner (nested) classes, use `$` instead of `.` to separate
them. For example,
`JavaClassWrapper.wrap("android.view.WindowManager$LayoutParams")` wraps
the **WindowManager.LayoutParams** class.

\*\*Note:\*\* This method only works on Android. On every other
platform, this method does nothing and returns an empty
`JavaClass<class_JavaClass>`{.interpreted-text role="ref"}.
