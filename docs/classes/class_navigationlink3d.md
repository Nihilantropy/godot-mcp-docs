github_url
:   hide

# NavigationLink3D {#class_NavigationLink3D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A link between two positions on
`NavigationRegion3D<class_NavigationRegion3D>`{.interpreted-text
role="ref"}s that agents can be routed through.

::: rst-class
classref-introduction-group
:::

## Description

A link between two positions on
`NavigationRegion3D<class_NavigationRegion3D>`{.interpreted-text
role="ref"}s that agents can be routed through. These positions can be
on the same
`NavigationRegion3D<class_NavigationRegion3D>`{.interpreted-text
role="ref"} or on two different ones. Links are useful to express
navigation methods other than traveling along the surface of the
navigation mesh, such as ziplines, teleporters, or gaps that can be
jumped across.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using NavigationLinks <../tutorials/navigation/navigation_using_navigationlinks>`{.interpreted-text
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

## Property Descriptions

:::: {#class_NavigationLink3D_property_bidirectional}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **bidirectional** =
`true`
`🔗<class_NavigationLink3D_property_bidirectional>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bidirectional**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_bidirectional**()

Whether this link can be traveled in both directions or only from
`start_position<class_NavigationLink3D_property_start_position>`{.interpreted-text
role="ref"} to
`end_position<class_NavigationLink3D_property_end_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_property_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `true`
`🔗<class_NavigationLink3D_property_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_enabled**()

Whether this link is currently active. If `false`,
`NavigationServer3D.map_get_path()<class_NavigationServer3D_method_map_get_path>`{.interpreted-text
role="ref"} will ignore this link.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_property_end_position}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **end_position**
= `Vector3(0, 0, 0)`
`🔗<class_NavigationLink3D_property_end_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_end_position**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_end_position**()

Ending position of the link.

This position will search out the nearest polygon in the navigation mesh
to attach to.

The distance the link will search is controlled by
`NavigationServer3D.map_set_link_connection_radius()<class_NavigationServer3D_method_map_set_link_connection_radius>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_property_enter_cost}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **enter_cost** =
`0.0` `🔗<class_NavigationLink3D_property_enter_cost>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enter_cost**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_enter_cost**()

When pathfinding enters this link from another regions navigation mesh
the
`enter_cost<class_NavigationLink3D_property_enter_cost>`{.interpreted-text
role="ref"} value is added to the path distance for determining the
shortest path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_property_navigation_layers}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **navigation_layers** =
`1`
`🔗<class_NavigationLink3D_property_navigation_layers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_navigation_layers**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_navigation_layers**()

A bitfield determining all navigation layers the link belongs to. These
navigation layers will be checked when requesting a path with
`NavigationServer3D.map_get_path()<class_NavigationServer3D_method_map_get_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_property_start_position}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**start_position** = `Vector3(0, 0, 0)`
`🔗<class_NavigationLink3D_property_start_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_start_position**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_start_position**()

Starting position of the link.

This position will search out the nearest polygon in the navigation mesh
to attach to.

The distance the link will search is controlled by
`NavigationServer3D.map_set_link_connection_radius()<class_NavigationServer3D_method_map_set_link_connection_radius>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_property_travel_cost}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **travel_cost** =
`1.0`
`🔗<class_NavigationLink3D_property_travel_cost>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_travel_cost**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_travel_cost**()

When pathfinding moves along the link the traveled distance is
multiplied with
`travel_cost<class_NavigationLink3D_property_travel_cost>`{.interpreted-text
role="ref"} for determining the shortest path.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NavigationLink3D_method_get_global_end_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_global_end_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationLink3D_method_get_global_end_position>`{.interpreted-text
role="ref"}

Returns the
`end_position<class_NavigationLink3D_property_end_position>`{.interpreted-text
role="ref"} that is relative to the link as a global position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_method_get_global_start_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_global_start_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationLink3D_method_get_global_start_position>`{.interpreted-text
role="ref"}

Returns the
`start_position<class_NavigationLink3D_property_start_position>`{.interpreted-text
role="ref"} that is relative to the link as a global position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_method_get_navigation_layer_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_navigation_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationLink3D_method_get_navigation_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`navigation_layers<class_NavigationLink3D_property_navigation_layers>`{.interpreted-text
role="ref"} bitmask is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_method_get_navigation_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_navigation_map**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationLink3D_method_get_navigation_map>`{.interpreted-text
role="ref"}

Returns the current navigation map `RID<class_RID>`{.interpreted-text
role="ref"} used by this link.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_method_get_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationLink3D_method_get_rid>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of this link
on the `NavigationServer3D<class_NavigationServer3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_method_set_global_end_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_global_end_position**(position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_NavigationLink3D_method_set_global_end_position>`{.interpreted-text
role="ref"}

Sets the
`end_position<class_NavigationLink3D_property_end_position>`{.interpreted-text
role="ref"} that is relative to the link from a global `position`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_method_set_global_start_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_global_start_position**(position:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_NavigationLink3D_method_set_global_start_position>`{.interpreted-text
role="ref"}

Sets the
`start_position<class_NavigationLink3D_property_start_position>`{.interpreted-text
role="ref"} that is relative to the link from a global `position`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_method_set_navigation_layer_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationLink3D_method_set_navigation_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`navigation_layers<class_NavigationLink3D_property_navigation_layers>`{.interpreted-text
role="ref"} bitmask, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationLink3D_method_set_navigation_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_map**(navigation_map:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationLink3D_method_set_navigation_map>`{.interpreted-text
role="ref"}

Sets the `RID<class_RID>`{.interpreted-text role="ref"} of the
navigation map this link should use. By default the link will
automatically join the `World3D<class_World3D>`{.interpreted-text
role="ref"} default navigation map so this function is only required to
override the default map.
