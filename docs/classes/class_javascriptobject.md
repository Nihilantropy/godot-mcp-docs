github_url
:   hide

# JavaScriptObject {#class_JavaScriptObject}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A wrapper class for web native JavaScript objects.

::: rst-class
classref-introduction-group
:::

## Description

JavaScriptObject is used to interact with JavaScript objects retrieved
or created via
`JavaScriptBridge.get_interface()<class_JavaScriptBridge_method_get_interface>`{.interpreted-text
role="ref"},
`JavaScriptBridge.create_object()<class_JavaScriptBridge_method_create_object>`{.interpreted-text
role="ref"}, or
`JavaScriptBridge.create_callback()<class_JavaScriptBridge_method_create_callback>`{.interpreted-text
role="ref"}.

    extends Node

    var _my_js_callback = JavaScriptBridge.create_callback(myCallback) # This reference must be kept
    var console = JavaScriptBridge.get_interface("console")

    func _init():
        var buf = JavaScriptBridge.create_object("ArrayBuffer", 10) # new ArrayBuffer(10)
        print(buf) # Prints [JavaScriptObject:OBJECT_ID]
        var uint8arr = JavaScriptBridge.create_object("Uint8Array", buf) # new Uint8Array(buf)
        uint8arr[1] = 255
        prints(uint8arr[1], uint8arr.byteLength) # Prints "255 10"

        # Prints "Uint8Array(10) [ 0, 255, 0, 0, 0, 0, 0, 0, 0, 0 ]" in the browser's console.
        console.log(uint8arr)

        # Equivalent of JavaScriptBridge: Array.from(uint8arr).forEach(myCallback)
        JavaScriptBridge.get_interface("Array").from(uint8arr).forEach(_my_js_callback)

    func myCallback(args):
        # Will be called with the parameters passed to the "forEach" callback
        # [0, 0, [JavaScriptObject:1173]]
        # [255, 1, [JavaScriptObject:1173]]
        # ...
        # [0, 9, [JavaScriptObject:1180]]
        print(args)

\*\*Note:\*\* Only available in the Web platform.
