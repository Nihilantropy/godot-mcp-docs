github_url
:   hide

# PhysicsDirectSpaceState2DExtension {#class_PhysicsDirectSpaceState2DExtension}

**Inherits:**
`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides virtual methods that can be overridden to create custom
`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"} implementations.

::: rst-class
classref-introduction-group
:::

## Description

This class extends
`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"} by providing additional virtual methods that can be
overridden. When these methods are overridden, they will be called
instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of
`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
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

:::: {#class_PhysicsDirectSpaceState2DExtension_private_method__cast_motion}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_cast_motion**(shape_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}, motion:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, margin:
`float<class_float>`{.interpreted-text role="ref"}, collision_mask:
`int<class_int>`{.interpreted-text role="ref"}, collide_with_bodies:
`bool<class_bool>`{.interpreted-text role="ref"}, collide_with_areas:
`bool<class_bool>`{.interpreted-text role="ref"}, closest_safe:
`float*`, closest_unsafe: `float*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectSpaceState2DExtension_private_method__cast_motion>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState2DExtension_private_method__collide_shape}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_collide_shape**(shape_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}, motion:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, margin:
`float<class_float>`{.interpreted-text role="ref"}, collision_mask:
`int<class_int>`{.interpreted-text role="ref"}, collide_with_bodies:
`bool<class_bool>`{.interpreted-text role="ref"}, collide_with_areas:
`bool<class_bool>`{.interpreted-text role="ref"}, results: `void*`,
max_results: `int<class_int>`{.interpreted-text role="ref"},
result_count: `int32_t*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectSpaceState2DExtension_private_method__collide_shape>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState2DExtension_private_method__intersect_point}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_intersect_point**(position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
canvas_instance_id: `int<class_int>`{.interpreted-text role="ref"},
collision_mask: `int<class_int>`{.interpreted-text role="ref"},
collide_with_bodies: `bool<class_bool>`{.interpreted-text role="ref"},
collide_with_areas: `bool<class_bool>`{.interpreted-text role="ref"},
results: `PhysicsServer2DExtensionShapeResult*`, max_results:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectSpaceState2DExtension_private_method__intersect_point>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState2DExtension_private_method__intersect_ray}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_intersect_ray**(from: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, to: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
collision_mask: `int<class_int>`{.interpreted-text role="ref"},
collide_with_bodies: `bool<class_bool>`{.interpreted-text role="ref"},
collide_with_areas: `bool<class_bool>`{.interpreted-text role="ref"},
hit_from_inside: `bool<class_bool>`{.interpreted-text role="ref"},
result: `PhysicsServer2DExtensionRayResult*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectSpaceState2DExtension_private_method__intersect_ray>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState2DExtension_private_method__intersect_shape}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_intersect_shape**(shape_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}, motion:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, margin:
`float<class_float>`{.interpreted-text role="ref"}, collision_mask:
`int<class_int>`{.interpreted-text role="ref"}, collide_with_bodies:
`bool<class_bool>`{.interpreted-text role="ref"}, collide_with_areas:
`bool<class_bool>`{.interpreted-text role="ref"}, result:
`PhysicsServer2DExtensionShapeResult*`, max_results:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectSpaceState2DExtension_private_method__intersect_shape>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState2DExtension_private_method__rest_info}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_rest_info**(shape_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}, motion:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, margin:
`float<class_float>`{.interpreted-text role="ref"}, collision_mask:
`int<class_int>`{.interpreted-text role="ref"}, collide_with_bodies:
`bool<class_bool>`{.interpreted-text role="ref"}, collide_with_areas:
`bool<class_bool>`{.interpreted-text role="ref"}, rest_info:
`PhysicsServer2DExtensionShapeRestInfo*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectSpaceState2DExtension_private_method__rest_info>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsDirectSpaceState2DExtension_method_is_body_excluded_from_query}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_body_excluded_from_query**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsDirectSpaceState2DExtension_method_is_body_excluded_from_query>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
