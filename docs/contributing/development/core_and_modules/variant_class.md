# Variant class {#doc_variant_class}

## About

Variant is the most important datatype in Godot. A Variant takes up only
24 bytes on 64-bit platforms (20 bytes on 32-bit platforms) and can
store almost any engine datatype inside of it. Variants are rarely used
to hold information for long periods of time, instead they are used
mainly for communication, editing, serialization and generally moving
data around.

A Variant can:

- Store almost any datatype.
- Perform operations between many variants (GDScript uses Variant as its
  atomic/native datatype).
- Be hashed, so it can be compared quickly to other variants.
- Be used to convert safely between datatypes.
- Be used to abstract calling methods and their arguments (Godot exports
  all its functions through variants).
- Be used to defer calls or move data between threads.
- Be serialized as binary and stored to disk, or transferred via
  network.
- Be serialized to text and use it for printing values and editable
  settings.
- Work as an exported property, so the editor can edit it universally.
- Be used for dictionaries, arrays, parsers, etc.

Basically, thanks to the Variant class, writing Godot itself was a much,
much easier task, as it allows for highly dynamic constructs not common
of C++ with little effort. Become a friend of Variant today.

:::: note
::: title
Note
:::

All types within Variant except Nil and Object **cannot** be `null` and
must always store a valid value. These types within Variant are
therefore called *non-nullable* types.

One of the Variant types is *Nil* which can only store the value `null`.
Therefore, it is possible for a Variant to contain the value `null`,
even though all Variant types excluding Nil and Object are non-nullable.
::::

### References

- [core/variant/variant.h](https://github.com/godotengine/godot/blob/master/core/variant/variant.h)

## List of variant types

These types are available in Variant:

  --------------------------------------------------------------------------
  Type                                           Notes
  ---------------------------------------------- ---------------------------
  Nil (can only store `null`)                    Nullable type

  `class_bool`{.interpreted-text role="ref"}     

  `class_int`{.interpreted-text role="ref"}      

  `class_float`{.interpreted-text role="ref"}    

  `class_string`{.interpreted-text role="ref"}   

  `class_vector2`{.interpreted-text role="ref"}  

  `class_vector2i`{.interpreted-text role="ref"} 

  `class_rect2`{.interpreted-text role="ref"}    2D counterpart of AABB

  `class_rect2i`{.interpreted-text role="ref"}   

  `class_vector3`{.interpreted-text role="ref"}  

  `class_vector3i`{.interpreted-text role="ref"} 

  `class_transform2d`{.interpreted-text          
  role="ref"}                                    

  `class_vector4`{.interpreted-text role="ref"}  

  `class_vector4i`{.interpreted-text role="ref"} 

  `class_plane`{.interpreted-text role="ref"}    

  `class_quaternion`{.interpreted-text           
  role="ref"}                                    

  `class_aabb`{.interpreted-text role="ref"}     3D counterpart of Rect2

  `class_basis`{.interpreted-text role="ref"}    

  `class_transform3d`{.interpreted-text          
  role="ref"}                                    

  `class_projection`{.interpreted-text           
  role="ref"}                                    

  `class_color`{.interpreted-text role="ref"}    

  `class_stringname`{.interpreted-text           
  role="ref"}                                    

  `class_nodepath`{.interpreted-text role="ref"} 

  `class_rid`{.interpreted-text role="ref"}      

  `class_object`{.interpreted-text role="ref"}   Nullable type

  `class_callable`{.interpreted-text role="ref"} 

  `class_signal`{.interpreted-text role="ref"}   

  `class_dictionary`{.interpreted-text           
  role="ref"}                                    

  `class_array`{.interpreted-text role="ref"}    

  `class_packedbytearray`{.interpreted-text      
  role="ref"}                                    

  `class_packedint32array`{.interpreted-text     
  role="ref"}                                    

  `class_packedint64array`{.interpreted-text     
  role="ref"}                                    

  `class_packedfloat32array`{.interpreted-text   
  role="ref"}                                    

  `class_packedfloat64array`{.interpreted-text   
  role="ref"}                                    

  `class_packedstringarray`{.interpreted-text    
  role="ref"}                                    

  `class_packedvector2array`{.interpreted-text   
  role="ref"}                                    

  `class_packedvector3array`{.interpreted-text   
  role="ref"}                                    

  `class_packedcolorarray`{.interpreted-text     
  role="ref"}                                    

  `class_packedvector4array`{.interpreted-text   
  role="ref"}                                    
  --------------------------------------------------------------------------

## Containers: Array and Dictionary

Both `class_array`{.interpreted-text role="ref"} and
`class_dictionary`{.interpreted-text role="ref"} are implemented using
variants. A Dictionary can match any datatype used as key to any other
datatype. An Array just holds an array of Variants. Of course, a Variant
can also hold a Dictionary or an Array inside, making it even more
flexible.

Modifications to a container will modify all references to it. A Mutex
should be created to lock it if
`multi-threaded access <doc_using_multiple_threads>`{.interpreted-text
role="ref"} is desired.

### References

- [core/variant/dictionary.h](https://github.com/godotengine/godot/blob/master/core/variant/dictionary.h)
- [core/variant/array.h](https://github.com/godotengine/godot/blob/master/core/variant/array.h)
