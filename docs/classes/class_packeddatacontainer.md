github_url
:   hide

# PackedDataContainer {#class_PackedDataContainer}

**Deprecated:** Use
`@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>`{.interpreted-text
role="ref"} or
`FileAccess.store_var()<class_FileAccess_method_store_var>`{.interpreted-text
role="ref"} instead. To enable data compression, use
`PackedByteArray.compress()<class_PackedByteArray_method_compress>`{.interpreted-text
role="ref"} or
`FileAccess.open_compressed()<class_FileAccess_method_open_compressed>`{.interpreted-text
role="ref"}.

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Efficiently packs and serializes `Array<class_Array>`{.interpreted-text
role="ref"} or `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**PackedDataContainer** can be used to efficiently store data from
untyped containers. The data is packed into raw bytes and can be saved
to file. Only `Array<class_Array>`{.interpreted-text role="ref"} and
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} can be
stored this way.

You can retrieve the data by iterating on the container, which will work
as if iterating on the packed data itself. If the packed container is a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}, the data
can be retrieved by key names (`String<class_String>`{.interpreted-text
role="ref"}/`StringName<class_StringName>`{.interpreted-text role="ref"}
only).

    var data = { "key": "value", "another_key": 123, "lock": Vector2() }
    var packed = PackedDataContainer.new()
    packed.pack(data)
    ResourceSaver.save(packed, "packed_data.res")

    var container = load("packed_data.res")
    for key in container:
        prints(key, container[key])

Prints:

``` text
key value
lock (0, 0)
another_key 123
```

Nested containers will be packed recursively. While iterating, they will
be returned as
`PackedDataContainerRef<class_PackedDataContainerRef>`{.interpreted-text
role="ref"}.

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

:::: {#class_PackedDataContainer_method_pack}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**pack**(value: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_PackedDataContainer_method_pack>`{.interpreted-text
role="ref"}

Packs the given container into a binary representation. The `value` must
be either `Array<class_Array>`{.interpreted-text role="ref"} or
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}, any other
type will result in invalid data error.

\*\*Note:\*\* Subsequent calls to this method will overwrite the
existing data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedDataContainer_method_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedDataContainer_method_size>`{.interpreted-text
role="ref"}

Returns the size of the packed container (see
`Array.size()<class_Array_method_size>`{.interpreted-text role="ref"}
and `Dictionary.size()<class_Dictionary_method_size>`{.interpreted-text
role="ref"}).
