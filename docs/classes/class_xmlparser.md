github_url
:   hide

# XMLParser {#class_XMLParser}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides a low-level interface for creating parsers for XML files.

::: rst-class
classref-introduction-group
:::

## Description

Provides a low-level interface for creating parsers for
[XML](https://en.wikipedia.org/wiki/XML) files. This class can serve as
base to make custom XML parsers.

To parse XML, you must open a file with the
`open()<class_XMLParser_method_open>`{.interpreted-text role="ref"}
method or a buffer with the
`open_buffer()<class_XMLParser_method_open_buffer>`{.interpreted-text
role="ref"} method. Then, the
`read()<class_XMLParser_method_read>`{.interpreted-text role="ref"}
method must be called to parse the next nodes. Most of the methods take
into consideration the currently parsed node.

Here is an example of using **XMLParser** to parse an SVG file (which is
based on XML), printing each element and its attributes as a dictionary:

::::: tabs
::: code-tab
gdscript

var parser = XMLParser.new() parser.open(\"path/to/file.svg\") while
parser.read() != ERR_FILE_EOF: if parser.get_node_type() ==
XMLParser.NODE_ELEMENT: var node_name = parser.get_node_name() var
attributes_dict = {} for idx in range(parser.get_attribute_count()):
attributes_dict\[parser.get_attribute_name(idx)\] =
parser.get_attribute_value(idx) print(\"The \", node_name, \" element
has the following attributes: \", attributes_dict)
:::

::: code-tab
csharp

var parser = new XmlParser(); parser.Open(\"path/to/file.svg\"); while
(parser.Read() != Error.FileEof) { if (parser.GetNodeType() ==
XmlParser.NodeType.Element) { var nodeName = parser.GetNodeName(); var
attributesDict = new Godot.Collections.Dictionary(); for (int idx = 0;
idx \< parser.GetAttributeCount(); idx++) {
attributesDict\[parser.GetAttributeName(idx)\] =
parser.GetAttributeValue(idx); } GD.Print(\$\"The {nodeName} element has
the following attributes: {attributesDict}\"); } }
:::
:::::

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

## Enumerations

:::: {#enum_XMLParser_NodeType}
::: rst-class
classref-enumeration
:::
::::

enum **NodeType**: `🔗<enum_XMLParser_NodeType>`{.interpreted-text
role="ref"}

:::: {#class_XMLParser_constant_NODE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`NodeType<enum_XMLParser_NodeType>`{.interpreted-text role="ref"}
**NODE_NONE** = `0`

There\'s no node (no file or buffer opened).

:::: {#class_XMLParser_constant_NODE_ELEMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`NodeType<enum_XMLParser_NodeType>`{.interpreted-text role="ref"}
**NODE_ELEMENT** = `1`

An element node type, also known as a tag, e.g. `<title>`.

:::: {#class_XMLParser_constant_NODE_ELEMENT_END}
::: rst-class
classref-enumeration-constant
:::
::::

`NodeType<enum_XMLParser_NodeType>`{.interpreted-text role="ref"}
**NODE_ELEMENT_END** = `2`

An end of element node type, e.g. `</title>`.

:::: {#class_XMLParser_constant_NODE_TEXT}
::: rst-class
classref-enumeration-constant
:::
::::

`NodeType<enum_XMLParser_NodeType>`{.interpreted-text role="ref"}
**NODE_TEXT** = `3`

A text node type, i.e. text that is not inside an element. This includes
whitespace.

:::: {#class_XMLParser_constant_NODE_COMMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`NodeType<enum_XMLParser_NodeType>`{.interpreted-text role="ref"}
**NODE_COMMENT** = `4`

A comment node type, e.g. `<!--A comment-->`.

:::: {#class_XMLParser_constant_NODE_CDATA}
::: rst-class
classref-enumeration-constant
:::
::::

`NodeType<enum_XMLParser_NodeType>`{.interpreted-text role="ref"}
**NODE_CDATA** = `5`

A node type for CDATA (Character Data) sections, e.g.
`<![CDATA[CDATA section]]>`.

:::: {#class_XMLParser_constant_NODE_UNKNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`NodeType<enum_XMLParser_NodeType>`{.interpreted-text role="ref"}
**NODE_UNKNOWN** = `6`

An unknown node type.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XMLParser_method_get_attribute_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_attribute_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_get_attribute_count>`{.interpreted-text
role="ref"}

Returns the number of attributes in the currently parsed element.

\*\*Note:\*\* If this method is used while the currently parsed node is
not
`NODE_ELEMENT<class_XMLParser_constant_NODE_ELEMENT>`{.interpreted-text
role="ref"} or
`NODE_ELEMENT_END<class_XMLParser_constant_NODE_ELEMENT_END>`{.interpreted-text
role="ref"}, this count will not be updated and will still reflect the
last element.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_get_attribute_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_attribute_name**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_get_attribute_name>`{.interpreted-text
role="ref"}

Returns the name of an attribute of the currently parsed element,
specified by the `idx` index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_get_attribute_value}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_attribute_value**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_get_attribute_value>`{.interpreted-text
role="ref"}

Returns the value of an attribute of the currently parsed element,
specified by the `idx` index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_get_current_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_current_line**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_get_current_line>`{.interpreted-text
role="ref"}

Returns the current line in the parsed file, counting from 0.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_get_named_attribute_value}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_named_attribute_value**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_get_named_attribute_value>`{.interpreted-text
role="ref"}

Returns the value of an attribute of the currently parsed element,
specified by its `name`. This method will raise an error if the element
has no such attribute.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_get_named_attribute_value_safe}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_named_attribute_value_safe**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_get_named_attribute_value_safe>`{.interpreted-text
role="ref"}

Returns the value of an attribute of the currently parsed element,
specified by its `name`. This method will return an empty string if the
element has no such attribute.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_get_node_data}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_node_data**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_get_node_data>`{.interpreted-text role="ref"}

Returns the contents of a text node. This method will raise an error if
the current parsed node is of any other type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_get_node_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_node_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_get_node_name>`{.interpreted-text role="ref"}

Returns the name of a node. This method will raise an error if the
currently parsed node is a text node.

\*\*Note:\*\* The content of a
`NODE_CDATA<class_XMLParser_constant_NODE_CDATA>`{.interpreted-text
role="ref"} node and the comment string of a
`NODE_COMMENT<class_XMLParser_constant_NODE_COMMENT>`{.interpreted-text
role="ref"} node are also considered names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_get_node_offset}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_node_offset**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_get_node_offset>`{.interpreted-text
role="ref"}

Returns the byte offset of the currently parsed node since the beginning
of the file or buffer. This is usually equivalent to the number of
characters before the read position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_get_node_type}
::: rst-class
classref-method
:::
::::

`NodeType<enum_XMLParser_NodeType>`{.interpreted-text role="ref"}
**get_node_type**()
`🔗<class_XMLParser_method_get_node_type>`{.interpreted-text role="ref"}

Returns the type of the current node. Compare with
`NodeType<enum_XMLParser_NodeType>`{.interpreted-text role="ref"}
constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_has_attribute}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_attribute**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XMLParser_method_has_attribute>`{.interpreted-text role="ref"}

Returns `true` if the currently parsed element has an attribute with the
`name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_XMLParser_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the currently parsed element is empty, e.g.
`<element />`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_open}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**open**(file: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_XMLParser_method_open>`{.interpreted-text role="ref"}

Opens an XML `file` for parsing. This method returns an error code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_open_buffer}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**open_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_XMLParser_method_open_buffer>`{.interpreted-text role="ref"}

Opens an XML raw `buffer` for parsing. This method returns an error
code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_read}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**read**() `🔗<class_XMLParser_method_read>`{.interpreted-text
role="ref"}

Parses the next node in the file. This method returns an error code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_seek}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**seek**(position: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_XMLParser_method_seek>`{.interpreted-text role="ref"}

Moves the buffer cursor to a certain offset (since the beginning) and
reads the next node there. This method returns an error code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XMLParser_method_skip_section}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**skip_section**()
`🔗<class_XMLParser_method_skip_section>`{.interpreted-text role="ref"}

Skips the current section. If the currently parsed node contains more
inner nodes, they will be ignored and the cursor will go to the closing
of the current element.
