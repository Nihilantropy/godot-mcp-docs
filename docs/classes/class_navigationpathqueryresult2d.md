github_url
:   hide

# NavigationPathQueryResult2D {#class_NavigationPathQueryResult2D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents the result of a 2D pathfinding query.

::: rst-class
classref-introduction-group
:::

## Description

This class stores the result of a 2D navigation path query from the
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using NavigationPathQueryObjects <../tutorials/navigation/navigation_using_navigationpathqueryobjects>`{.interpreted-text
  role="doc"}

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

## Enumerations

:::: {#enum_NavigationPathQueryResult2D_PathSegmentType}
::: rst-class
classref-enumeration
:::
::::

enum **PathSegmentType**:
`🔗<enum_NavigationPathQueryResult2D_PathSegmentType>`{.interpreted-text
role="ref"}

:::: {#class_NavigationPathQueryResult2D_constant_PATH_SEGMENT_TYPE_REGION}
::: rst-class
classref-enumeration-constant
:::
::::

`PathSegmentType<enum_NavigationPathQueryResult2D_PathSegmentType>`{.interpreted-text
role="ref"} **PATH_SEGMENT_TYPE_REGION** = `0`

This segment of the path goes through a region.

:::: {#class_NavigationPathQueryResult2D_constant_PATH_SEGMENT_TYPE_LINK}
::: rst-class
classref-enumeration-constant
:::
::::

`PathSegmentType<enum_NavigationPathQueryResult2D_PathSegmentType>`{.interpreted-text
role="ref"} **PATH_SEGMENT_TYPE_LINK** = `1`

This segment of the path goes through a link.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_NavigationPathQueryResult2D_property_path}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **path** = `PackedVector2Array()`
`🔗<class_NavigationPathQueryResult2D_property_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_path**()

The resulting path array from the navigation query. All path array
positions are in global coordinates. Without customized query parameters
this is the same path as returned by
`NavigationServer2D.map_get_path()<class_NavigationServer2D_method_map_get_path>`{.interpreted-text
role="ref"}.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryResult2D_property_path_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **path_length** =
`0.0`
`🔗<class_NavigationPathQueryResult2D_property_path_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_path_length**()

Returns the length of the path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryResult2D_property_path_owner_ids}
::: rst-class
classref-property
:::
::::

`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
**path_owner_ids** = `PackedInt64Array()`
`🔗<class_NavigationPathQueryResult2D_property_path_owner_ids>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_owner_ids**(value:
  `PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
  role="ref"})
- `PackedInt64Array<class_PackedInt64Array>`{.interpreted-text
  role="ref"} **get_path_owner_ids**()

The `ObjectID`s of the `Object<class_Object>`{.interpreted-text
role="ref"}s which manage the regions and links each point of the path
goes through.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryResult2D_property_path_rids}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**path_rids** = `[]`
`🔗<class_NavigationPathQueryResult2D_property_path_rids>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_rids**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
  **get_path_rids**()

The `RID<class_RID>`{.interpreted-text role="ref"}s of the regions and
links that each point of the path goes through.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationPathQueryResult2D_property_path_types}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**path_types** = `PackedInt32Array()`
`🔗<class_NavigationPathQueryResult2D_property_path_types>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_path_types**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_path_types**()

The type of navigation primitive (region or link) that each point of the
path goes through.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NavigationPathQueryResult2D_method_reset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **reset**()
`🔗<class_NavigationPathQueryResult2D_method_reset>`{.interpreted-text
role="ref"}

Reset the result object to its initial state. This is useful to reuse
the object across multiple queries.
