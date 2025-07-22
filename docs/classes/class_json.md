github_url
:   hide

# JSON {#class_JSON}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Helper class for creating and parsing JSON data.

::: rst-class
classref-introduction-group
:::

## Description

The **JSON** class enables all data types to be converted to and from a
JSON string. This is useful for serializing data, e.g. to save to a file
or send over the network.

`stringify()<class_JSON_method_stringify>`{.interpreted-text role="ref"}
is used to convert any data type into a JSON string.

`parse()<class_JSON_method_parse>`{.interpreted-text role="ref"} is used
to convert any existing JSON data into a
`Variant<class_Variant>`{.interpreted-text role="ref"} that can be used
within Godot. If successfully parsed, use
`data<class_JSON_property_data>`{.interpreted-text role="ref"} to
retrieve the `Variant<class_Variant>`{.interpreted-text role="ref"}, and
use
`@GlobalScope.typeof()<class_@GlobalScope_method_typeof>`{.interpreted-text
role="ref"} to check if the Variant\'s type is what you expect. JSON
Objects are converted into a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}, but JSON
data can be used to store `Array<class_Array>`{.interpreted-text
role="ref"}s, numbers, `String<class_String>`{.interpreted-text
role="ref"}s and even just a boolean.

    var data_to_send = ["a", "b", "c"]
    var json_string = JSON.stringify(data_to_send)
    # Save data
    # ...
    # Retrieve data
    var json = JSON.new()
    var error = json.parse(json_string)
    if error == OK:
        var data_received = json.data
        if typeof(data_received) == TYPE_ARRAY:
            print(data_received) # Prints the array.
        else:
            print("Unexpected data")
    else:
        print("JSON Parse Error: ", json.get_error_message(), " in ", json_string, " at line ", json.get_error_line())

Alternatively, you can parse strings using the static
`parse_string()<class_JSON_method_parse_string>`{.interpreted-text
role="ref"} method, but it doesn\'t handle errors.

    var data = JSON.parse_string(json_string) # Returns null if parsing failed.

\*\*Note:\*\* Both parse methods do not fully comply with the JSON
specification:

- Trailing commas in arrays or objects are ignored, instead of causing a
  parser error.
- New line and tab characters are accepted in string literals, and are
  treated like their corresponding escape sequences `\n` and `\t`.
- Numbers are parsed using
  `String.to_float()<class_String_method_to_float>`{.interpreted-text
  role="ref"} which is generally more lax than the JSON specification.
- Certain errors, such as invalid Unicode sequences, do not cause a
  parser error. Instead, the string is cleaned up and an error is logged
  to the console.

::: rst-class
classref-reftable-group
:::

## Properties

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

## Property Descriptions

:::: {#class_JSON_property_data}
::: rst-class
classref-property
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **data** = `null`
`🔗<class_JSON_property_data>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_data**(value: `Variant<class_Variant>`{.interpreted-text
  role="ref"})
- `Variant<class_Variant>`{.interpreted-text role="ref"} **get_data**()

Contains the parsed JSON data in
`Variant<class_Variant>`{.interpreted-text role="ref"} form.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_JSON_method_from_native}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**from_native**(variant: `Variant<class_Variant>`{.interpreted-text
role="ref"}, full_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_JSON_method_from_native>`{.interpreted-text
role="ref"}

Converts a native engine type to a JSON-compliant value.

By default, objects are ignored for security reasons, unless
`full_objects` is `true`.

You can convert a native value to a JSON string like this:

    func encode_data(value, full_objects = false):
        return JSON.stringify(JSON.from_native(value, full_objects))

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSON_method_get_error_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_error_line**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_JSON_method_get_error_line>`{.interpreted-text
role="ref"}

Returns `0` if the last call to
`parse()<class_JSON_method_parse>`{.interpreted-text role="ref"} was
successful, or the line number where the parse failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSON_method_get_error_message}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_error_message**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_JSON_method_get_error_message>`{.interpreted-text
role="ref"}

Returns an empty string if the last call to
`parse()<class_JSON_method_parse>`{.interpreted-text role="ref"} was
successful, or the error message if it failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSON_method_get_parsed_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_parsed_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_JSON_method_get_parsed_text>`{.interpreted-text
role="ref"}

Return the text parsed by
`parse()<class_JSON_method_parse>`{.interpreted-text role="ref"}
(requires passing `keep_text` to
`parse()<class_JSON_method_parse>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSON_method_parse}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**parse**(json_text: `String<class_String>`{.interpreted-text
role="ref"}, keep_text: `bool<class_bool>`{.interpreted-text role="ref"}
= false) `🔗<class_JSON_method_parse>`{.interpreted-text role="ref"}

Attempts to parse the `json_text` provided.

Returns an `Error<enum_@GlobalScope_Error>`{.interpreted-text
role="ref"}. If the parse was successful, it returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} and the result can be retrieved using
`data<class_JSON_property_data>`{.interpreted-text role="ref"}. If
unsuccessful, use
`get_error_line()<class_JSON_method_get_error_line>`{.interpreted-text
role="ref"} and
`get_error_message()<class_JSON_method_get_error_message>`{.interpreted-text
role="ref"} to identify the source of the failure.

Non-static variant of
`parse_string()<class_JSON_method_parse_string>`{.interpreted-text
role="ref"}, if you want custom error handling.

The optional `keep_text` argument instructs the parser to keep a copy of
the original text. This text can be obtained later by using the
`get_parsed_text()<class_JSON_method_get_parsed_text>`{.interpreted-text
role="ref"} function and is used when saving the resource (instead of
generating new text from
`data<class_JSON_property_data>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSON_method_parse_string}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**parse_string**(json_string: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_JSON_method_parse_string>`{.interpreted-text
role="ref"}

Attempts to parse the `json_string` provided and returns the parsed
data. Returns `null` if parse failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSON_method_stringify}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **stringify**(data:
`Variant<class_Variant>`{.interpreted-text role="ref"}, indent:
`String<class_String>`{.interpreted-text role="ref"} = \"\", sort_keys:
`bool<class_bool>`{.interpreted-text role="ref"} = true, full_precision:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_JSON_method_stringify>`{.interpreted-text
role="ref"}

Converts a `Variant<class_Variant>`{.interpreted-text role="ref"} var to
JSON text and returns the result. Useful for serializing data to store
or send over the network.

\*\*Note:\*\* The JSON specification does not define integer or float
types, but only a *number* type. Therefore, converting a Variant to JSON
text will convert all numerical values to
`float<class_float>`{.interpreted-text role="ref"} types.

\*\*Note:\*\* If `full_precision` is `true`, when stringifying floats,
the unreliable digits are stringified in addition to the reliable digits
to guarantee exact decoding.

The `indent` parameter controls if and how something is indented; its
contents will be used where there should be an indent in the output.
Even spaces like `"   "` will work. `\t` and `\n` can also be used for a
tab indent, or to make a newline for each indent respectively.

\*\*Example output:\*\*

    ## JSON.stringify(my_dictionary)
    {"name":"my_dictionary","version":"1.0.0","entities":[{"name":"entity_0","value":"value_0"},{"name":"entity_1","value":"value_1"}]}

    ## JSON.stringify(my_dictionary, "\t")
    {
        "name": "my_dictionary",
        "version": "1.0.0",
        "entities": [
            {
                "name": "entity_0",
                "value": "value_0"
            },
            {
                "name": "entity_1",
                "value": "value_1"
            }
        ]
    }

    ## JSON.stringify(my_dictionary, "...")
    {
    ..."name": "my_dictionary",
    ..."version": "1.0.0",
    ..."entities": [
    ......{
    ........."name": "entity_0",
    ........."value": "value_0"
    ......},
    ......{
    ........."name": "entity_1",
    ........."value": "value_1"
    ......}
    ...]
    }

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSON_method_to_native}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**to_native**(json: `Variant<class_Variant>`{.interpreted-text
role="ref"}, allow_objects: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_JSON_method_to_native>`{.interpreted-text
role="ref"}

Converts a JSON-compliant value that was created with
`from_native()<class_JSON_method_from_native>`{.interpreted-text
role="ref"} back to native engine types.

By default, objects are ignored for security reasons, unless
`allow_objects` is `true`.

You can convert a JSON string back to a native value like this:

    func decode_data(string, allow_objects = false):
        return JSON.to_native(JSON.parse_string(string), allow_objects)
