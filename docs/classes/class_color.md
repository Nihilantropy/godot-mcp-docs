github_url
:   hide

# Color {#class_Color}

A color represented in RGBA format.

::: rst-class
classref-introduction-group
:::

## Description

A color represented in RGBA format by a red
(`r<class_Color_property_r>`{.interpreted-text role="ref"}), green
(`g<class_Color_property_g>`{.interpreted-text role="ref"}), blue
(`b<class_Color_property_b>`{.interpreted-text role="ref"}), and alpha
(`a<class_Color_property_a>`{.interpreted-text role="ref"}) component.
Each component is a 32-bit floating-point value, usually ranging from
`0.0` to `1.0`. Some properties (such as
`CanvasItem.modulate<class_CanvasItem_property_modulate>`{.interpreted-text
role="ref"}) may support values greater than `1.0`, for overbright or
HDR (High Dynamic Range) colors.

Colors can be created in various ways: By the various **Color**
constructors, by static methods such as
`from_hsv()<class_Color_method_from_hsv>`{.interpreted-text role="ref"},
and by using a name from the set of standardized colors based on [X11
color names](https://en.wikipedia.org/wiki/X11_color_names) with the
addition of
`TRANSPARENT<class_Color_constant_TRANSPARENT>`{.interpreted-text
role="ref"}. GDScript also provides
`@GDScript.Color8()<class_@GDScript_method_Color8>`{.interpreted-text
role="ref"}, which uses integers from `0` to `255` and doesn\'t support
overbright colors.

Color data may be stored in many color spaces and encodings. The
`srgb_to_linear()<class_Color_method_srgb_to_linear>`{.interpreted-text
role="ref"} and
`linear_to_srgb()<class_Color_method_linear_to_srgb>`{.interpreted-text
role="ref"} methods can convert between nonlinear sRGB encoding and
linear RGB encoding.

\*\*Note:\*\* In a boolean context, a Color will evaluate to `false` if
it is equal to `Color(0, 0, 0, 1)` (opaque black). Otherwise, a Color
will always evaluate to `true`.

\`Color constants cheatsheet
\<https://raw.githubusercontent.com/godotengine/godot-docs/master/img/color_constants.png\>\`\_\_

:::: note
::: title
Note
:::

There are notable differences when using this API with C#. See
`doc_c_sharp_differences`{.interpreted-text role="ref"} for more
information.
::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- [2D GD Paint Demo](https://godotengine.org/asset-library/asset/2768)
- [Tween Interpolation
  Demo](https://godotengine.org/asset-library/asset/2733)
- [GUI Drag And Drop
  Demo](https://godotengine.org/asset-library/asset/2767)

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Constructors

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Operators

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Color_constant_ALICE_BLUE}
::: rst-class
classref-constant
:::
::::

**ALICE_BLUE** = `Color(0.9411765, 0.972549, 1, 1)`
`🔗<class_Color_constant_ALICE_BLUE>`{.interpreted-text role="ref"}

Alice blue color.

:::: {#class_Color_constant_ANTIQUE_WHITE}
::: rst-class
classref-constant
:::
::::

**ANTIQUE_WHITE** = `Color(0.98039216, 0.92156863, 0.84313726, 1)`
`🔗<class_Color_constant_ANTIQUE_WHITE>`{.interpreted-text role="ref"}

Antique white color.

:::: {#class_Color_constant_AQUA}
::: rst-class
classref-constant
:::
::::

**AQUA** = `Color(0, 1, 1, 1)`
`🔗<class_Color_constant_AQUA>`{.interpreted-text role="ref"}

Aqua color.

:::: {#class_Color_constant_AQUAMARINE}
::: rst-class
classref-constant
:::
::::

**AQUAMARINE** = `Color(0.49803922, 1, 0.83137256, 1)`
`🔗<class_Color_constant_AQUAMARINE>`{.interpreted-text role="ref"}

Aquamarine color.

:::: {#class_Color_constant_AZURE}
::: rst-class
classref-constant
:::
::::

**AZURE** = `Color(0.9411765, 1, 1, 1)`
`🔗<class_Color_constant_AZURE>`{.interpreted-text role="ref"}

Azure color.

:::: {#class_Color_constant_BEIGE}
::: rst-class
classref-constant
:::
::::

**BEIGE** = `Color(0.9607843, 0.9607843, 0.8627451, 1)`
`🔗<class_Color_constant_BEIGE>`{.interpreted-text role="ref"}

Beige color.

:::: {#class_Color_constant_BISQUE}
::: rst-class
classref-constant
:::
::::

**BISQUE** = `Color(1, 0.89411765, 0.76862746, 1)`
`🔗<class_Color_constant_BISQUE>`{.interpreted-text role="ref"}

Bisque color.

:::: {#class_Color_constant_BLACK}
::: rst-class
classref-constant
:::
::::

**BLACK** = `Color(0, 0, 0, 1)`
`🔗<class_Color_constant_BLACK>`{.interpreted-text role="ref"}

Black color. In GDScript, this is the default value of any color.

:::: {#class_Color_constant_BLANCHED_ALMOND}
::: rst-class
classref-constant
:::
::::

**BLANCHED_ALMOND** = `Color(1, 0.92156863, 0.8039216, 1)`
`🔗<class_Color_constant_BLANCHED_ALMOND>`{.interpreted-text role="ref"}

Blanched almond color.

:::: {#class_Color_constant_BLUE}
::: rst-class
classref-constant
:::
::::

**BLUE** = `Color(0, 0, 1, 1)`
`🔗<class_Color_constant_BLUE>`{.interpreted-text role="ref"}

Blue color.

:::: {#class_Color_constant_BLUE_VIOLET}
::: rst-class
classref-constant
:::
::::

**BLUE_VIOLET** = `Color(0.5411765, 0.16862746, 0.8862745, 1)`
`🔗<class_Color_constant_BLUE_VIOLET>`{.interpreted-text role="ref"}

Blue violet color.

:::: {#class_Color_constant_BROWN}
::: rst-class
classref-constant
:::
::::

**BROWN** = `Color(0.64705884, 0.16470589, 0.16470589, 1)`
`🔗<class_Color_constant_BROWN>`{.interpreted-text role="ref"}

Brown color.

:::: {#class_Color_constant_BURLYWOOD}
::: rst-class
classref-constant
:::
::::

**BURLYWOOD** = `Color(0.87058824, 0.72156864, 0.5294118, 1)`
`🔗<class_Color_constant_BURLYWOOD>`{.interpreted-text role="ref"}

Burlywood color.

:::: {#class_Color_constant_CADET_BLUE}
::: rst-class
classref-constant
:::
::::

**CADET_BLUE** = `Color(0.37254903, 0.61960787, 0.627451, 1)`
`🔗<class_Color_constant_CADET_BLUE>`{.interpreted-text role="ref"}

Cadet blue color.

:::: {#class_Color_constant_CHARTREUSE}
::: rst-class
classref-constant
:::
::::

**CHARTREUSE** = `Color(0.49803922, 1, 0, 1)`
`🔗<class_Color_constant_CHARTREUSE>`{.interpreted-text role="ref"}

Chartreuse color.

:::: {#class_Color_constant_CHOCOLATE}
::: rst-class
classref-constant
:::
::::

**CHOCOLATE** = `Color(0.8235294, 0.4117647, 0.11764706, 1)`
`🔗<class_Color_constant_CHOCOLATE>`{.interpreted-text role="ref"}

Chocolate color.

:::: {#class_Color_constant_CORAL}
::: rst-class
classref-constant
:::
::::

**CORAL** = `Color(1, 0.49803922, 0.3137255, 1)`
`🔗<class_Color_constant_CORAL>`{.interpreted-text role="ref"}

Coral color.

:::: {#class_Color_constant_CORNFLOWER_BLUE}
::: rst-class
classref-constant
:::
::::

**CORNFLOWER_BLUE** = `Color(0.39215687, 0.58431375, 0.92941177, 1)`
`🔗<class_Color_constant_CORNFLOWER_BLUE>`{.interpreted-text role="ref"}

Cornflower blue color.

:::: {#class_Color_constant_CORNSILK}
::: rst-class
classref-constant
:::
::::

**CORNSILK** = `Color(1, 0.972549, 0.8627451, 1)`
`🔗<class_Color_constant_CORNSILK>`{.interpreted-text role="ref"}

Cornsilk color.

:::: {#class_Color_constant_CRIMSON}
::: rst-class
classref-constant
:::
::::

**CRIMSON** = `Color(0.8627451, 0.078431375, 0.23529412, 1)`
`🔗<class_Color_constant_CRIMSON>`{.interpreted-text role="ref"}

Crimson color.

:::: {#class_Color_constant_CYAN}
::: rst-class
classref-constant
:::
::::

**CYAN** = `Color(0, 1, 1, 1)`
`🔗<class_Color_constant_CYAN>`{.interpreted-text role="ref"}

Cyan color.

:::: {#class_Color_constant_DARK_BLUE}
::: rst-class
classref-constant
:::
::::

**DARK_BLUE** = `Color(0, 0, 0.54509807, 1)`
`🔗<class_Color_constant_DARK_BLUE>`{.interpreted-text role="ref"}

Dark blue color.

:::: {#class_Color_constant_DARK_CYAN}
::: rst-class
classref-constant
:::
::::

**DARK_CYAN** = `Color(0, 0.54509807, 0.54509807, 1)`
`🔗<class_Color_constant_DARK_CYAN>`{.interpreted-text role="ref"}

Dark cyan color.

:::: {#class_Color_constant_DARK_GOLDENROD}
::: rst-class
classref-constant
:::
::::

**DARK_GOLDENROD** = `Color(0.72156864, 0.5254902, 0.043137256, 1)`
`🔗<class_Color_constant_DARK_GOLDENROD>`{.interpreted-text role="ref"}

Dark goldenrod color.

:::: {#class_Color_constant_DARK_GRAY}
::: rst-class
classref-constant
:::
::::

**DARK_GRAY** = `Color(0.6627451, 0.6627451, 0.6627451, 1)`
`🔗<class_Color_constant_DARK_GRAY>`{.interpreted-text role="ref"}

Dark gray color.

:::: {#class_Color_constant_DARK_GREEN}
::: rst-class
classref-constant
:::
::::

**DARK_GREEN** = `Color(0, 0.39215687, 0, 1)`
`🔗<class_Color_constant_DARK_GREEN>`{.interpreted-text role="ref"}

Dark green color.

:::: {#class_Color_constant_DARK_KHAKI}
::: rst-class
classref-constant
:::
::::

**DARK_KHAKI** = `Color(0.7411765, 0.7176471, 0.41960785, 1)`
`🔗<class_Color_constant_DARK_KHAKI>`{.interpreted-text role="ref"}

Dark khaki color.

:::: {#class_Color_constant_DARK_MAGENTA}
::: rst-class
classref-constant
:::
::::

**DARK_MAGENTA** = `Color(0.54509807, 0, 0.54509807, 1)`
`🔗<class_Color_constant_DARK_MAGENTA>`{.interpreted-text role="ref"}

Dark magenta color.

:::: {#class_Color_constant_DARK_OLIVE_GREEN}
::: rst-class
classref-constant
:::
::::

**DARK_OLIVE_GREEN** = `Color(0.33333334, 0.41960785, 0.18431373, 1)`
`🔗<class_Color_constant_DARK_OLIVE_GREEN>`{.interpreted-text
role="ref"}

Dark olive green color.

:::: {#class_Color_constant_DARK_ORANGE}
::: rst-class
classref-constant
:::
::::

**DARK_ORANGE** = `Color(1, 0.54901963, 0, 1)`
`🔗<class_Color_constant_DARK_ORANGE>`{.interpreted-text role="ref"}

Dark orange color.

:::: {#class_Color_constant_DARK_ORCHID}
::: rst-class
classref-constant
:::
::::

**DARK_ORCHID** = `Color(0.6, 0.19607843, 0.8, 1)`
`🔗<class_Color_constant_DARK_ORCHID>`{.interpreted-text role="ref"}

Dark orchid color.

:::: {#class_Color_constant_DARK_RED}
::: rst-class
classref-constant
:::
::::

**DARK_RED** = `Color(0.54509807, 0, 0, 1)`
`🔗<class_Color_constant_DARK_RED>`{.interpreted-text role="ref"}

Dark red color.

:::: {#class_Color_constant_DARK_SALMON}
::: rst-class
classref-constant
:::
::::

**DARK_SALMON** = `Color(0.9137255, 0.5882353, 0.47843137, 1)`
`🔗<class_Color_constant_DARK_SALMON>`{.interpreted-text role="ref"}

Dark salmon color.

:::: {#class_Color_constant_DARK_SEA_GREEN}
::: rst-class
classref-constant
:::
::::

**DARK_SEA_GREEN** = `Color(0.56078434, 0.7372549, 0.56078434, 1)`
`🔗<class_Color_constant_DARK_SEA_GREEN>`{.interpreted-text role="ref"}

Dark sea green color.

:::: {#class_Color_constant_DARK_SLATE_BLUE}
::: rst-class
classref-constant
:::
::::

**DARK_SLATE_BLUE** = `Color(0.28235295, 0.23921569, 0.54509807, 1)`
`🔗<class_Color_constant_DARK_SLATE_BLUE>`{.interpreted-text role="ref"}

Dark slate blue color.

:::: {#class_Color_constant_DARK_SLATE_GRAY}
::: rst-class
classref-constant
:::
::::

**DARK_SLATE_GRAY** = `Color(0.18431373, 0.30980393, 0.30980393, 1)`
`🔗<class_Color_constant_DARK_SLATE_GRAY>`{.interpreted-text role="ref"}

Dark slate gray color.

:::: {#class_Color_constant_DARK_TURQUOISE}
::: rst-class
classref-constant
:::
::::

**DARK_TURQUOISE** = `Color(0, 0.80784315, 0.81960785, 1)`
`🔗<class_Color_constant_DARK_TURQUOISE>`{.interpreted-text role="ref"}

Dark turquoise color.

:::: {#class_Color_constant_DARK_VIOLET}
::: rst-class
classref-constant
:::
::::

**DARK_VIOLET** = `Color(0.5803922, 0, 0.827451, 1)`
`🔗<class_Color_constant_DARK_VIOLET>`{.interpreted-text role="ref"}

Dark violet color.

:::: {#class_Color_constant_DEEP_PINK}
::: rst-class
classref-constant
:::
::::

**DEEP_PINK** = `Color(1, 0.078431375, 0.5764706, 1)`
`🔗<class_Color_constant_DEEP_PINK>`{.interpreted-text role="ref"}

Deep pink color.

:::: {#class_Color_constant_DEEP_SKY_BLUE}
::: rst-class
classref-constant
:::
::::

**DEEP_SKY_BLUE** = `Color(0, 0.7490196, 1, 1)`
`🔗<class_Color_constant_DEEP_SKY_BLUE>`{.interpreted-text role="ref"}

Deep sky blue color.

:::: {#class_Color_constant_DIM_GRAY}
::: rst-class
classref-constant
:::
::::

**DIM_GRAY** = `Color(0.4117647, 0.4117647, 0.4117647, 1)`
`🔗<class_Color_constant_DIM_GRAY>`{.interpreted-text role="ref"}

Dim gray color.

:::: {#class_Color_constant_DODGER_BLUE}
::: rst-class
classref-constant
:::
::::

**DODGER_BLUE** = `Color(0.11764706, 0.5647059, 1, 1)`
`🔗<class_Color_constant_DODGER_BLUE>`{.interpreted-text role="ref"}

Dodger blue color.

:::: {#class_Color_constant_FIREBRICK}
::: rst-class
classref-constant
:::
::::

**FIREBRICK** = `Color(0.69803923, 0.13333334, 0.13333334, 1)`
`🔗<class_Color_constant_FIREBRICK>`{.interpreted-text role="ref"}

Firebrick color.

:::: {#class_Color_constant_FLORAL_WHITE}
::: rst-class
classref-constant
:::
::::

**FLORAL_WHITE** = `Color(1, 0.98039216, 0.9411765, 1)`
`🔗<class_Color_constant_FLORAL_WHITE>`{.interpreted-text role="ref"}

Floral white color.

:::: {#class_Color_constant_FOREST_GREEN}
::: rst-class
classref-constant
:::
::::

**FOREST_GREEN** = `Color(0.13333334, 0.54509807, 0.13333334, 1)`
`🔗<class_Color_constant_FOREST_GREEN>`{.interpreted-text role="ref"}

Forest green color.

:::: {#class_Color_constant_FUCHSIA}
::: rst-class
classref-constant
:::
::::

**FUCHSIA** = `Color(1, 0, 1, 1)`
`🔗<class_Color_constant_FUCHSIA>`{.interpreted-text role="ref"}

Fuchsia color.

:::: {#class_Color_constant_GAINSBORO}
::: rst-class
classref-constant
:::
::::

**GAINSBORO** = `Color(0.8627451, 0.8627451, 0.8627451, 1)`
`🔗<class_Color_constant_GAINSBORO>`{.interpreted-text role="ref"}

Gainsboro color.

:::: {#class_Color_constant_GHOST_WHITE}
::: rst-class
classref-constant
:::
::::

**GHOST_WHITE** = `Color(0.972549, 0.972549, 1, 1)`
`🔗<class_Color_constant_GHOST_WHITE>`{.interpreted-text role="ref"}

Ghost white color.

:::: {#class_Color_constant_GOLD}
::: rst-class
classref-constant
:::
::::

**GOLD** = `Color(1, 0.84313726, 0, 1)`
`🔗<class_Color_constant_GOLD>`{.interpreted-text role="ref"}

Gold color.

:::: {#class_Color_constant_GOLDENROD}
::: rst-class
classref-constant
:::
::::

**GOLDENROD** = `Color(0.85490197, 0.64705884, 0.1254902, 1)`
`🔗<class_Color_constant_GOLDENROD>`{.interpreted-text role="ref"}

Goldenrod color.

:::: {#class_Color_constant_GRAY}
::: rst-class
classref-constant
:::
::::

**GRAY** = `Color(0.74509805, 0.74509805, 0.74509805, 1)`
`🔗<class_Color_constant_GRAY>`{.interpreted-text role="ref"}

Gray color.

:::: {#class_Color_constant_GREEN}
::: rst-class
classref-constant
:::
::::

**GREEN** = `Color(0, 1, 0, 1)`
`🔗<class_Color_constant_GREEN>`{.interpreted-text role="ref"}

Green color.

:::: {#class_Color_constant_GREEN_YELLOW}
::: rst-class
classref-constant
:::
::::

**GREEN_YELLOW** = `Color(0.6784314, 1, 0.18431373, 1)`
`🔗<class_Color_constant_GREEN_YELLOW>`{.interpreted-text role="ref"}

Green yellow color.

:::: {#class_Color_constant_HONEYDEW}
::: rst-class
classref-constant
:::
::::

**HONEYDEW** = `Color(0.9411765, 1, 0.9411765, 1)`
`🔗<class_Color_constant_HONEYDEW>`{.interpreted-text role="ref"}

Honeydew color.

:::: {#class_Color_constant_HOT_PINK}
::: rst-class
classref-constant
:::
::::

**HOT_PINK** = `Color(1, 0.4117647, 0.7058824, 1)`
`🔗<class_Color_constant_HOT_PINK>`{.interpreted-text role="ref"}

Hot pink color.

:::: {#class_Color_constant_INDIAN_RED}
::: rst-class
classref-constant
:::
::::

**INDIAN_RED** = `Color(0.8039216, 0.36078432, 0.36078432, 1)`
`🔗<class_Color_constant_INDIAN_RED>`{.interpreted-text role="ref"}

Indian red color.

:::: {#class_Color_constant_INDIGO}
::: rst-class
classref-constant
:::
::::

**INDIGO** = `Color(0.29411766, 0, 0.50980395, 1)`
`🔗<class_Color_constant_INDIGO>`{.interpreted-text role="ref"}

Indigo color.

:::: {#class_Color_constant_IVORY}
::: rst-class
classref-constant
:::
::::

**IVORY** = `Color(1, 1, 0.9411765, 1)`
`🔗<class_Color_constant_IVORY>`{.interpreted-text role="ref"}

Ivory color.

:::: {#class_Color_constant_KHAKI}
::: rst-class
classref-constant
:::
::::

**KHAKI** = `Color(0.9411765, 0.9019608, 0.54901963, 1)`
`🔗<class_Color_constant_KHAKI>`{.interpreted-text role="ref"}

Khaki color.

:::: {#class_Color_constant_LAVENDER}
::: rst-class
classref-constant
:::
::::

**LAVENDER** = `Color(0.9019608, 0.9019608, 0.98039216, 1)`
`🔗<class_Color_constant_LAVENDER>`{.interpreted-text role="ref"}

Lavender color.

:::: {#class_Color_constant_LAVENDER_BLUSH}
::: rst-class
classref-constant
:::
::::

**LAVENDER_BLUSH** = `Color(1, 0.9411765, 0.9607843, 1)`
`🔗<class_Color_constant_LAVENDER_BLUSH>`{.interpreted-text role="ref"}

Lavender blush color.

:::: {#class_Color_constant_LAWN_GREEN}
::: rst-class
classref-constant
:::
::::

**LAWN_GREEN** = `Color(0.4862745, 0.9882353, 0, 1)`
`🔗<class_Color_constant_LAWN_GREEN>`{.interpreted-text role="ref"}

Lawn green color.

:::: {#class_Color_constant_LEMON_CHIFFON}
::: rst-class
classref-constant
:::
::::

**LEMON_CHIFFON** = `Color(1, 0.98039216, 0.8039216, 1)`
`🔗<class_Color_constant_LEMON_CHIFFON>`{.interpreted-text role="ref"}

Lemon chiffon color.

:::: {#class_Color_constant_LIGHT_BLUE}
::: rst-class
classref-constant
:::
::::

**LIGHT_BLUE** = `Color(0.6784314, 0.84705883, 0.9019608, 1)`
`🔗<class_Color_constant_LIGHT_BLUE>`{.interpreted-text role="ref"}

Light blue color.

:::: {#class_Color_constant_LIGHT_CORAL}
::: rst-class
classref-constant
:::
::::

**LIGHT_CORAL** = `Color(0.9411765, 0.5019608, 0.5019608, 1)`
`🔗<class_Color_constant_LIGHT_CORAL>`{.interpreted-text role="ref"}

Light coral color.

:::: {#class_Color_constant_LIGHT_CYAN}
::: rst-class
classref-constant
:::
::::

**LIGHT_CYAN** = `Color(0.8784314, 1, 1, 1)`
`🔗<class_Color_constant_LIGHT_CYAN>`{.interpreted-text role="ref"}

Light cyan color.

:::: {#class_Color_constant_LIGHT_GOLDENROD}
::: rst-class
classref-constant
:::
::::

**LIGHT_GOLDENROD** = `Color(0.98039216, 0.98039216, 0.8235294, 1)`
`🔗<class_Color_constant_LIGHT_GOLDENROD>`{.interpreted-text role="ref"}

Light goldenrod color.

:::: {#class_Color_constant_LIGHT_GRAY}
::: rst-class
classref-constant
:::
::::

**LIGHT_GRAY** = `Color(0.827451, 0.827451, 0.827451, 1)`
`🔗<class_Color_constant_LIGHT_GRAY>`{.interpreted-text role="ref"}

Light gray color.

:::: {#class_Color_constant_LIGHT_GREEN}
::: rst-class
classref-constant
:::
::::

**LIGHT_GREEN** = `Color(0.5647059, 0.93333334, 0.5647059, 1)`
`🔗<class_Color_constant_LIGHT_GREEN>`{.interpreted-text role="ref"}

Light green color.

:::: {#class_Color_constant_LIGHT_PINK}
::: rst-class
classref-constant
:::
::::

**LIGHT_PINK** = `Color(1, 0.7137255, 0.75686276, 1)`
`🔗<class_Color_constant_LIGHT_PINK>`{.interpreted-text role="ref"}

Light pink color.

:::: {#class_Color_constant_LIGHT_SALMON}
::: rst-class
classref-constant
:::
::::

**LIGHT_SALMON** = `Color(1, 0.627451, 0.47843137, 1)`
`🔗<class_Color_constant_LIGHT_SALMON>`{.interpreted-text role="ref"}

Light salmon color.

:::: {#class_Color_constant_LIGHT_SEA_GREEN}
::: rst-class
classref-constant
:::
::::

**LIGHT_SEA_GREEN** = `Color(0.1254902, 0.69803923, 0.6666667, 1)`
`🔗<class_Color_constant_LIGHT_SEA_GREEN>`{.interpreted-text role="ref"}

Light sea green color.

:::: {#class_Color_constant_LIGHT_SKY_BLUE}
::: rst-class
classref-constant
:::
::::

**LIGHT_SKY_BLUE** = `Color(0.5294118, 0.80784315, 0.98039216, 1)`
`🔗<class_Color_constant_LIGHT_SKY_BLUE>`{.interpreted-text role="ref"}

Light sky blue color.

:::: {#class_Color_constant_LIGHT_SLATE_GRAY}
::: rst-class
classref-constant
:::
::::

**LIGHT_SLATE_GRAY** = `Color(0.46666667, 0.53333336, 0.6, 1)`
`🔗<class_Color_constant_LIGHT_SLATE_GRAY>`{.interpreted-text
role="ref"}

Light slate gray color.

:::: {#class_Color_constant_LIGHT_STEEL_BLUE}
::: rst-class
classref-constant
:::
::::

**LIGHT_STEEL_BLUE** = `Color(0.6901961, 0.76862746, 0.87058824, 1)`
`🔗<class_Color_constant_LIGHT_STEEL_BLUE>`{.interpreted-text
role="ref"}

Light steel blue color.

:::: {#class_Color_constant_LIGHT_YELLOW}
::: rst-class
classref-constant
:::
::::

**LIGHT_YELLOW** = `Color(1, 1, 0.8784314, 1)`
`🔗<class_Color_constant_LIGHT_YELLOW>`{.interpreted-text role="ref"}

Light yellow color.

:::: {#class_Color_constant_LIME}
::: rst-class
classref-constant
:::
::::

**LIME** = `Color(0, 1, 0, 1)`
`🔗<class_Color_constant_LIME>`{.interpreted-text role="ref"}

Lime color.

:::: {#class_Color_constant_LIME_GREEN}
::: rst-class
classref-constant
:::
::::

**LIME_GREEN** = `Color(0.19607843, 0.8039216, 0.19607843, 1)`
`🔗<class_Color_constant_LIME_GREEN>`{.interpreted-text role="ref"}

Lime green color.

:::: {#class_Color_constant_LINEN}
::: rst-class
classref-constant
:::
::::

**LINEN** = `Color(0.98039216, 0.9411765, 0.9019608, 1)`
`🔗<class_Color_constant_LINEN>`{.interpreted-text role="ref"}

Linen color.

:::: {#class_Color_constant_MAGENTA}
::: rst-class
classref-constant
:::
::::

**MAGENTA** = `Color(1, 0, 1, 1)`
`🔗<class_Color_constant_MAGENTA>`{.interpreted-text role="ref"}

Magenta color.

:::: {#class_Color_constant_MAROON}
::: rst-class
classref-constant
:::
::::

**MAROON** = `Color(0.6901961, 0.1882353, 0.3764706, 1)`
`🔗<class_Color_constant_MAROON>`{.interpreted-text role="ref"}

Maroon color.

:::: {#class_Color_constant_MEDIUM_AQUAMARINE}
::: rst-class
classref-constant
:::
::::

**MEDIUM_AQUAMARINE** = `Color(0.4, 0.8039216, 0.6666667, 1)`
`🔗<class_Color_constant_MEDIUM_AQUAMARINE>`{.interpreted-text
role="ref"}

Medium aquamarine color.

:::: {#class_Color_constant_MEDIUM_BLUE}
::: rst-class
classref-constant
:::
::::

**MEDIUM_BLUE** = `Color(0, 0, 0.8039216, 1)`
`🔗<class_Color_constant_MEDIUM_BLUE>`{.interpreted-text role="ref"}

Medium blue color.

:::: {#class_Color_constant_MEDIUM_ORCHID}
::: rst-class
classref-constant
:::
::::

**MEDIUM_ORCHID** = `Color(0.7294118, 0.33333334, 0.827451, 1)`
`🔗<class_Color_constant_MEDIUM_ORCHID>`{.interpreted-text role="ref"}

Medium orchid color.

:::: {#class_Color_constant_MEDIUM_PURPLE}
::: rst-class
classref-constant
:::
::::

**MEDIUM_PURPLE** = `Color(0.5764706, 0.4392157, 0.85882354, 1)`
`🔗<class_Color_constant_MEDIUM_PURPLE>`{.interpreted-text role="ref"}

Medium purple color.

:::: {#class_Color_constant_MEDIUM_SEA_GREEN}
::: rst-class
classref-constant
:::
::::

**MEDIUM_SEA_GREEN** = `Color(0.23529412, 0.7019608, 0.44313726, 1)`
`🔗<class_Color_constant_MEDIUM_SEA_GREEN>`{.interpreted-text
role="ref"}

Medium sea green color.

:::: {#class_Color_constant_MEDIUM_SLATE_BLUE}
::: rst-class
classref-constant
:::
::::

**MEDIUM_SLATE_BLUE** = `Color(0.48235294, 0.40784314, 0.93333334, 1)`
`🔗<class_Color_constant_MEDIUM_SLATE_BLUE>`{.interpreted-text
role="ref"}

Medium slate blue color.

:::: {#class_Color_constant_MEDIUM_SPRING_GREEN}
::: rst-class
classref-constant
:::
::::

**MEDIUM_SPRING_GREEN** = `Color(0, 0.98039216, 0.6039216, 1)`
`🔗<class_Color_constant_MEDIUM_SPRING_GREEN>`{.interpreted-text
role="ref"}

Medium spring green color.

:::: {#class_Color_constant_MEDIUM_TURQUOISE}
::: rst-class
classref-constant
:::
::::

**MEDIUM_TURQUOISE** = `Color(0.28235295, 0.81960785, 0.8, 1)`
`🔗<class_Color_constant_MEDIUM_TURQUOISE>`{.interpreted-text
role="ref"}

Medium turquoise color.

:::: {#class_Color_constant_MEDIUM_VIOLET_RED}
::: rst-class
classref-constant
:::
::::

**MEDIUM_VIOLET_RED** = `Color(0.78039217, 0.08235294, 0.52156866, 1)`
`🔗<class_Color_constant_MEDIUM_VIOLET_RED>`{.interpreted-text
role="ref"}

Medium violet red color.

:::: {#class_Color_constant_MIDNIGHT_BLUE}
::: rst-class
classref-constant
:::
::::

**MIDNIGHT_BLUE** = `Color(0.09803922, 0.09803922, 0.4392157, 1)`
`🔗<class_Color_constant_MIDNIGHT_BLUE>`{.interpreted-text role="ref"}

Midnight blue color.

:::: {#class_Color_constant_MINT_CREAM}
::: rst-class
classref-constant
:::
::::

**MINT_CREAM** = `Color(0.9607843, 1, 0.98039216, 1)`
`🔗<class_Color_constant_MINT_CREAM>`{.interpreted-text role="ref"}

Mint cream color.

:::: {#class_Color_constant_MISTY_ROSE}
::: rst-class
classref-constant
:::
::::

**MISTY_ROSE** = `Color(1, 0.89411765, 0.88235295, 1)`
`🔗<class_Color_constant_MISTY_ROSE>`{.interpreted-text role="ref"}

Misty rose color.

:::: {#class_Color_constant_MOCCASIN}
::: rst-class
classref-constant
:::
::::

**MOCCASIN** = `Color(1, 0.89411765, 0.70980394, 1)`
`🔗<class_Color_constant_MOCCASIN>`{.interpreted-text role="ref"}

Moccasin color.

:::: {#class_Color_constant_NAVAJO_WHITE}
::: rst-class
classref-constant
:::
::::

**NAVAJO_WHITE** = `Color(1, 0.87058824, 0.6784314, 1)`
`🔗<class_Color_constant_NAVAJO_WHITE>`{.interpreted-text role="ref"}

Navajo white color.

:::: {#class_Color_constant_NAVY_BLUE}
::: rst-class
classref-constant
:::
::::

**NAVY_BLUE** = `Color(0, 0, 0.5019608, 1)`
`🔗<class_Color_constant_NAVY_BLUE>`{.interpreted-text role="ref"}

Navy blue color.

:::: {#class_Color_constant_OLD_LACE}
::: rst-class
classref-constant
:::
::::

**OLD_LACE** = `Color(0.99215686, 0.9607843, 0.9019608, 1)`
`🔗<class_Color_constant_OLD_LACE>`{.interpreted-text role="ref"}

Old lace color.

:::: {#class_Color_constant_OLIVE}
::: rst-class
classref-constant
:::
::::

**OLIVE** = `Color(0.5019608, 0.5019608, 0, 1)`
`🔗<class_Color_constant_OLIVE>`{.interpreted-text role="ref"}

Olive color.

:::: {#class_Color_constant_OLIVE_DRAB}
::: rst-class
classref-constant
:::
::::

**OLIVE_DRAB** = `Color(0.41960785, 0.5568628, 0.13725491, 1)`
`🔗<class_Color_constant_OLIVE_DRAB>`{.interpreted-text role="ref"}

Olive drab color.

:::: {#class_Color_constant_ORANGE}
::: rst-class
classref-constant
:::
::::

**ORANGE** = `Color(1, 0.64705884, 0, 1)`
`🔗<class_Color_constant_ORANGE>`{.interpreted-text role="ref"}

Orange color.

:::: {#class_Color_constant_ORANGE_RED}
::: rst-class
classref-constant
:::
::::

**ORANGE_RED** = `Color(1, 0.27058825, 0, 1)`
`🔗<class_Color_constant_ORANGE_RED>`{.interpreted-text role="ref"}

Orange red color.

:::: {#class_Color_constant_ORCHID}
::: rst-class
classref-constant
:::
::::

**ORCHID** = `Color(0.85490197, 0.4392157, 0.8392157, 1)`
`🔗<class_Color_constant_ORCHID>`{.interpreted-text role="ref"}

Orchid color.

:::: {#class_Color_constant_PALE_GOLDENROD}
::: rst-class
classref-constant
:::
::::

**PALE_GOLDENROD** = `Color(0.93333334, 0.9098039, 0.6666667, 1)`
`🔗<class_Color_constant_PALE_GOLDENROD>`{.interpreted-text role="ref"}

Pale goldenrod color.

:::: {#class_Color_constant_PALE_GREEN}
::: rst-class
classref-constant
:::
::::

**PALE_GREEN** = `Color(0.59607846, 0.9843137, 0.59607846, 1)`
`🔗<class_Color_constant_PALE_GREEN>`{.interpreted-text role="ref"}

Pale green color.

:::: {#class_Color_constant_PALE_TURQUOISE}
::: rst-class
classref-constant
:::
::::

**PALE_TURQUOISE** = `Color(0.6862745, 0.93333334, 0.93333334, 1)`
`🔗<class_Color_constant_PALE_TURQUOISE>`{.interpreted-text role="ref"}

Pale turquoise color.

:::: {#class_Color_constant_PALE_VIOLET_RED}
::: rst-class
classref-constant
:::
::::

**PALE_VIOLET_RED** = `Color(0.85882354, 0.4392157, 0.5764706, 1)`
`🔗<class_Color_constant_PALE_VIOLET_RED>`{.interpreted-text role="ref"}

Pale violet red color.

:::: {#class_Color_constant_PAPAYA_WHIP}
::: rst-class
classref-constant
:::
::::

**PAPAYA_WHIP** = `Color(1, 0.9372549, 0.8352941, 1)`
`🔗<class_Color_constant_PAPAYA_WHIP>`{.interpreted-text role="ref"}

Papaya whip color.

:::: {#class_Color_constant_PEACH_PUFF}
::: rst-class
classref-constant
:::
::::

**PEACH_PUFF** = `Color(1, 0.85490197, 0.7254902, 1)`
`🔗<class_Color_constant_PEACH_PUFF>`{.interpreted-text role="ref"}

Peach puff color.

:::: {#class_Color_constant_PERU}
::: rst-class
classref-constant
:::
::::

**PERU** = `Color(0.8039216, 0.52156866, 0.24705882, 1)`
`🔗<class_Color_constant_PERU>`{.interpreted-text role="ref"}

Peru color.

:::: {#class_Color_constant_PINK}
::: rst-class
classref-constant
:::
::::

**PINK** = `Color(1, 0.7529412, 0.79607844, 1)`
`🔗<class_Color_constant_PINK>`{.interpreted-text role="ref"}

Pink color.

:::: {#class_Color_constant_PLUM}
::: rst-class
classref-constant
:::
::::

**PLUM** = `Color(0.8666667, 0.627451, 0.8666667, 1)`
`🔗<class_Color_constant_PLUM>`{.interpreted-text role="ref"}

Plum color.

:::: {#class_Color_constant_POWDER_BLUE}
::: rst-class
classref-constant
:::
::::

**POWDER_BLUE** = `Color(0.6901961, 0.8784314, 0.9019608, 1)`
`🔗<class_Color_constant_POWDER_BLUE>`{.interpreted-text role="ref"}

Powder blue color.

:::: {#class_Color_constant_PURPLE}
::: rst-class
classref-constant
:::
::::

**PURPLE** = `Color(0.627451, 0.1254902, 0.9411765, 1)`
`🔗<class_Color_constant_PURPLE>`{.interpreted-text role="ref"}

Purple color.

:::: {#class_Color_constant_REBECCA_PURPLE}
::: rst-class
classref-constant
:::
::::

**REBECCA_PURPLE** = `Color(0.4, 0.2, 0.6, 1)`
`🔗<class_Color_constant_REBECCA_PURPLE>`{.interpreted-text role="ref"}

Rebecca purple color.

:::: {#class_Color_constant_RED}
::: rst-class
classref-constant
:::
::::

**RED** = `Color(1, 0, 0, 1)`
`🔗<class_Color_constant_RED>`{.interpreted-text role="ref"}

Red color.

:::: {#class_Color_constant_ROSY_BROWN}
::: rst-class
classref-constant
:::
::::

**ROSY_BROWN** = `Color(0.7372549, 0.56078434, 0.56078434, 1)`
`🔗<class_Color_constant_ROSY_BROWN>`{.interpreted-text role="ref"}

Rosy brown color.

:::: {#class_Color_constant_ROYAL_BLUE}
::: rst-class
classref-constant
:::
::::

**ROYAL_BLUE** = `Color(0.25490198, 0.4117647, 0.88235295, 1)`
`🔗<class_Color_constant_ROYAL_BLUE>`{.interpreted-text role="ref"}

Royal blue color.

:::: {#class_Color_constant_SADDLE_BROWN}
::: rst-class
classref-constant
:::
::::

**SADDLE_BROWN** = `Color(0.54509807, 0.27058825, 0.07450981, 1)`
`🔗<class_Color_constant_SADDLE_BROWN>`{.interpreted-text role="ref"}

Saddle brown color.

:::: {#class_Color_constant_SALMON}
::: rst-class
classref-constant
:::
::::

**SALMON** = `Color(0.98039216, 0.5019608, 0.44705883, 1)`
`🔗<class_Color_constant_SALMON>`{.interpreted-text role="ref"}

Salmon color.

:::: {#class_Color_constant_SANDY_BROWN}
::: rst-class
classref-constant
:::
::::

**SANDY_BROWN** = `Color(0.95686275, 0.6431373, 0.3764706, 1)`
`🔗<class_Color_constant_SANDY_BROWN>`{.interpreted-text role="ref"}

Sandy brown color.

:::: {#class_Color_constant_SEA_GREEN}
::: rst-class
classref-constant
:::
::::

**SEA_GREEN** = `Color(0.18039216, 0.54509807, 0.34117648, 1)`
`🔗<class_Color_constant_SEA_GREEN>`{.interpreted-text role="ref"}

Sea green color.

:::: {#class_Color_constant_SEASHELL}
::: rst-class
classref-constant
:::
::::

**SEASHELL** = `Color(1, 0.9607843, 0.93333334, 1)`
`🔗<class_Color_constant_SEASHELL>`{.interpreted-text role="ref"}

Seashell color.

:::: {#class_Color_constant_SIENNA}
::: rst-class
classref-constant
:::
::::

**SIENNA** = `Color(0.627451, 0.32156864, 0.1764706, 1)`
`🔗<class_Color_constant_SIENNA>`{.interpreted-text role="ref"}

Sienna color.

:::: {#class_Color_constant_SILVER}
::: rst-class
classref-constant
:::
::::

**SILVER** = `Color(0.7529412, 0.7529412, 0.7529412, 1)`
`🔗<class_Color_constant_SILVER>`{.interpreted-text role="ref"}

Silver color.

:::: {#class_Color_constant_SKY_BLUE}
::: rst-class
classref-constant
:::
::::

**SKY_BLUE** = `Color(0.5294118, 0.80784315, 0.92156863, 1)`
`🔗<class_Color_constant_SKY_BLUE>`{.interpreted-text role="ref"}

Sky blue color.

:::: {#class_Color_constant_SLATE_BLUE}
::: rst-class
classref-constant
:::
::::

**SLATE_BLUE** = `Color(0.41568628, 0.3529412, 0.8039216, 1)`
`🔗<class_Color_constant_SLATE_BLUE>`{.interpreted-text role="ref"}

Slate blue color.

:::: {#class_Color_constant_SLATE_GRAY}
::: rst-class
classref-constant
:::
::::

**SLATE_GRAY** = `Color(0.4392157, 0.5019608, 0.5647059, 1)`
`🔗<class_Color_constant_SLATE_GRAY>`{.interpreted-text role="ref"}

Slate gray color.

:::: {#class_Color_constant_SNOW}
::: rst-class
classref-constant
:::
::::

**SNOW** = `Color(1, 0.98039216, 0.98039216, 1)`
`🔗<class_Color_constant_SNOW>`{.interpreted-text role="ref"}

Snow color.

:::: {#class_Color_constant_SPRING_GREEN}
::: rst-class
classref-constant
:::
::::

**SPRING_GREEN** = `Color(0, 1, 0.49803922, 1)`
`🔗<class_Color_constant_SPRING_GREEN>`{.interpreted-text role="ref"}

Spring green color.

:::: {#class_Color_constant_STEEL_BLUE}
::: rst-class
classref-constant
:::
::::

**STEEL_BLUE** = `Color(0.27450982, 0.50980395, 0.7058824, 1)`
`🔗<class_Color_constant_STEEL_BLUE>`{.interpreted-text role="ref"}

Steel blue color.

:::: {#class_Color_constant_TAN}
::: rst-class
classref-constant
:::
::::

**TAN** = `Color(0.8235294, 0.7058824, 0.54901963, 1)`
`🔗<class_Color_constant_TAN>`{.interpreted-text role="ref"}

Tan color.

:::: {#class_Color_constant_TEAL}
::: rst-class
classref-constant
:::
::::

**TEAL** = `Color(0, 0.5019608, 0.5019608, 1)`
`🔗<class_Color_constant_TEAL>`{.interpreted-text role="ref"}

Teal color.

:::: {#class_Color_constant_THISTLE}
::: rst-class
classref-constant
:::
::::

**THISTLE** = `Color(0.84705883, 0.7490196, 0.84705883, 1)`
`🔗<class_Color_constant_THISTLE>`{.interpreted-text role="ref"}

Thistle color.

:::: {#class_Color_constant_TOMATO}
::: rst-class
classref-constant
:::
::::

**TOMATO** = `Color(1, 0.3882353, 0.2784314, 1)`
`🔗<class_Color_constant_TOMATO>`{.interpreted-text role="ref"}

Tomato color.

:::: {#class_Color_constant_TRANSPARENT}
::: rst-class
classref-constant
:::
::::

**TRANSPARENT** = `Color(1, 1, 1, 0)`
`🔗<class_Color_constant_TRANSPARENT>`{.interpreted-text role="ref"}

Transparent color (white with zero alpha).

:::: {#class_Color_constant_TURQUOISE}
::: rst-class
classref-constant
:::
::::

**TURQUOISE** = `Color(0.2509804, 0.8784314, 0.8156863, 1)`
`🔗<class_Color_constant_TURQUOISE>`{.interpreted-text role="ref"}

Turquoise color.

:::: {#class_Color_constant_VIOLET}
::: rst-class
classref-constant
:::
::::

**VIOLET** = `Color(0.93333334, 0.50980395, 0.93333334, 1)`
`🔗<class_Color_constant_VIOLET>`{.interpreted-text role="ref"}

Violet color.

:::: {#class_Color_constant_WEB_GRAY}
::: rst-class
classref-constant
:::
::::

**WEB_GRAY** = `Color(0.5019608, 0.5019608, 0.5019608, 1)`
`🔗<class_Color_constant_WEB_GRAY>`{.interpreted-text role="ref"}

Web gray color.

:::: {#class_Color_constant_WEB_GREEN}
::: rst-class
classref-constant
:::
::::

**WEB_GREEN** = `Color(0, 0.5019608, 0, 1)`
`🔗<class_Color_constant_WEB_GREEN>`{.interpreted-text role="ref"}

Web green color.

:::: {#class_Color_constant_WEB_MAROON}
::: rst-class
classref-constant
:::
::::

**WEB_MAROON** = `Color(0.5019608, 0, 0, 1)`
`🔗<class_Color_constant_WEB_MAROON>`{.interpreted-text role="ref"}

Web maroon color.

:::: {#class_Color_constant_WEB_PURPLE}
::: rst-class
classref-constant
:::
::::

**WEB_PURPLE** = `Color(0.5019608, 0, 0.5019608, 1)`
`🔗<class_Color_constant_WEB_PURPLE>`{.interpreted-text role="ref"}

Web purple color.

:::: {#class_Color_constant_WHEAT}
::: rst-class
classref-constant
:::
::::

**WHEAT** = `Color(0.9607843, 0.87058824, 0.7019608, 1)`
`🔗<class_Color_constant_WHEAT>`{.interpreted-text role="ref"}

Wheat color.

:::: {#class_Color_constant_WHITE}
::: rst-class
classref-constant
:::
::::

**WHITE** = `Color(1, 1, 1, 1)`
`🔗<class_Color_constant_WHITE>`{.interpreted-text role="ref"}

White color.

:::: {#class_Color_constant_WHITE_SMOKE}
::: rst-class
classref-constant
:::
::::

**WHITE_SMOKE** = `Color(0.9607843, 0.9607843, 0.9607843, 1)`
`🔗<class_Color_constant_WHITE_SMOKE>`{.interpreted-text role="ref"}

White smoke color.

:::: {#class_Color_constant_YELLOW}
::: rst-class
classref-constant
:::
::::

**YELLOW** = `Color(1, 1, 0, 1)`
`🔗<class_Color_constant_YELLOW>`{.interpreted-text role="ref"}

Yellow color.

:::: {#class_Color_constant_YELLOW_GREEN}
::: rst-class
classref-constant
:::
::::

**YELLOW_GREEN** = `Color(0.6039216, 0.8039216, 0.19607843, 1)`
`🔗<class_Color_constant_YELLOW_GREEN>`{.interpreted-text role="ref"}

Yellow green color.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Color_property_a}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **a** = `1.0`
`🔗<class_Color_property_a>`{.interpreted-text role="ref"}

The color\'s alpha component, typically on the range of 0 to 1. A value
of 0 means that the color is fully transparent. A value of 1 means that
the color is fully opaque.

\*\*Note:\*\* The alpha channel is always stored with linear encoding,
regardless of the color space of the other color channels. The
`linear_to_srgb()<class_Color_method_linear_to_srgb>`{.interpreted-text
role="ref"} and
`srgb_to_linear()<class_Color_method_srgb_to_linear>`{.interpreted-text
role="ref"} methods do not affect the alpha channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_a8}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **a8** = `255`
`🔗<class_Color_property_a8>`{.interpreted-text role="ref"}

Wrapper for `a<class_Color_property_a>`{.interpreted-text role="ref"}
that uses the range 0 to 255, instead of 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_b}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **b** = `0.0`
`🔗<class_Color_property_b>`{.interpreted-text role="ref"}

The color\'s blue component, typically on the range of 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_b8}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **b8** = `0`
`🔗<class_Color_property_b8>`{.interpreted-text role="ref"}

Wrapper for `b<class_Color_property_b>`{.interpreted-text role="ref"}
that uses the range 0 to 255, instead of 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_g}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **g** = `0.0`
`🔗<class_Color_property_g>`{.interpreted-text role="ref"}

The color\'s green component, typically on the range of 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_g8}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **g8** = `0`
`🔗<class_Color_property_g8>`{.interpreted-text role="ref"}

Wrapper for `g<class_Color_property_g>`{.interpreted-text role="ref"}
that uses the range 0 to 255, instead of 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_h}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **h** = `0.0`
`🔗<class_Color_property_h>`{.interpreted-text role="ref"}

The HSV hue of this color, on the range 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_ok_hsl_h}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ok_hsl_h** = `0.0`
`🔗<class_Color_property_ok_hsl_h>`{.interpreted-text role="ref"}

The OKHSL hue of this color, on the range 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_ok_hsl_l}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ok_hsl_l** = `0.0`
`🔗<class_Color_property_ok_hsl_l>`{.interpreted-text role="ref"}

The OKHSL lightness of this color, on the range 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_ok_hsl_s}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **ok_hsl_s** = `0.0`
`🔗<class_Color_property_ok_hsl_s>`{.interpreted-text role="ref"}

The OKHSL saturation of this color, on the range 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_r}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **r** = `0.0`
`🔗<class_Color_property_r>`{.interpreted-text role="ref"}

The color\'s red component, typically on the range of 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_r8}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **r8** = `0`
`🔗<class_Color_property_r8>`{.interpreted-text role="ref"}

Wrapper for `r<class_Color_property_r>`{.interpreted-text role="ref"}
that uses the range 0 to 255, instead of 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_s}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **s** = `0.0`
`🔗<class_Color_property_s>`{.interpreted-text role="ref"}

The HSV saturation of this color, on the range 0 to 1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_property_v}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **v** = `0.0`
`🔗<class_Color_property_v>`{.interpreted-text role="ref"}

The HSV value (brightness) of this color, on the range 0 to 1.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constructor Descriptions

:::: {#class_Color_constructor_Color}
::: rst-class
classref-constructor
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **Color**()
`🔗<class_Color_constructor_Color>`{.interpreted-text role="ref"}

Constructs a default **Color** from opaque black. This is the same as
`BLACK<class_Color_constant_BLACK>`{.interpreted-text role="ref"}.

\*\*Note:\*\* In C#, this constructs a **Color** with all of its
components set to `0.0` (transparent black).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Color<class_Color>`{.interpreted-text role="ref"} **Color**(from:
`Color<class_Color>`{.interpreted-text role="ref"}, alpha:
`float<class_float>`{.interpreted-text role="ref"})

Constructs a **Color** from the existing color, with
`a<class_Color_property_a>`{.interpreted-text role="ref"} set to the
given `alpha` value.

::::: tabs
::: code-tab
gdscript

var red = Color(Color.RED, 0.2) \# 20% opaque red.
:::

::: code-tab
csharp

var red = new Color(Colors.Red, 0.2f); // 20% opaque red.
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Color<class_Color>`{.interpreted-text role="ref"} **Color**(from:
`Color<class_Color>`{.interpreted-text role="ref"})

Constructs a **Color** as a copy of the given **Color**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Color<class_Color>`{.interpreted-text role="ref"} **Color**(code:
`String<class_String>`{.interpreted-text role="ref"})

Constructs a **Color** either from an HTML color code or from a
standardized color name. The supported color names are the same as the
constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Color<class_Color>`{.interpreted-text role="ref"} **Color**(code:
`String<class_String>`{.interpreted-text role="ref"}, alpha:
`float<class_float>`{.interpreted-text role="ref"})

Constructs a **Color** either from an HTML color code or from a
standardized color name, with `alpha` on the range of 0.0 to 1.0. The
supported color names are the same as the constants.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Color<class_Color>`{.interpreted-text role="ref"} **Color**(r:
`float<class_float>`{.interpreted-text role="ref"}, g:
`float<class_float>`{.interpreted-text role="ref"}, b:
`float<class_float>`{.interpreted-text role="ref"})

Constructs a **Color** from RGB values, typically between 0.0 and 1.0.
`a<class_Color_property_a>`{.interpreted-text role="ref"} is set to 1.0.

::::: tabs
::: code-tab
gdscript

var color = Color(0.2, 1.0, 0.7) \# Similar to [Color8(51, 255, 178,
255)]{.title-ref}
:::

::: code-tab
csharp

var color = new Color(0.2f, 1.0f, 0.7f); // Similar to [Color.Color8(51,
255, 178, 255)]{.title-ref}
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-constructor
:::

`Color<class_Color>`{.interpreted-text role="ref"} **Color**(r:
`float<class_float>`{.interpreted-text role="ref"}, g:
`float<class_float>`{.interpreted-text role="ref"}, b:
`float<class_float>`{.interpreted-text role="ref"}, a:
`float<class_float>`{.interpreted-text role="ref"})

Constructs a **Color** from RGBA values, typically between 0.0 and 1.0.

::::: tabs
::: code-tab
gdscript

var color = Color(0.2, 1.0, 0.7, 0.8) \# Similar to [Color8(51, 255,
178, 204)]{.title-ref}
:::

::: code-tab
csharp

var color = new Color(0.2f, 1.0f, 0.7f, 0.8f); // Similar to
[Color.Color8(51, 255, 178, 255, 204)]{.title-ref}
:::
:::::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Color_method_blend}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **blend**(over:
`Color<class_Color>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_blend>`{.interpreted-text
role="ref"}

Returns a new color resulting from overlaying this color over the given
color. In a painting program, you can imagine it as the `over` color
painted over this color (including alpha).

::::: tabs
::: code-tab
gdscript

var bg = Color(0.0, 1.0, 0.0, 0.5) \# Green with alpha of 50% var fg =
Color(1.0, 0.0, 0.0, 0.5) \# Red with alpha of 50% var blended_color =
bg.blend(fg) \# Brown with alpha of 75%
:::

::: code-tab
csharp

var bg = new Color(0.0f, 1.0f, 0.0f, 0.5f); // Green with alpha of 50%
var fg = new Color(1.0f, 0.0f, 0.0f, 0.5f); // Red with alpha of 50%
Color blendedColor = bg.Blend(fg); // Brown with alpha of 75%
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_clamp}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **clamp**(min:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(0, 0, 0, 0),
max: `Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1,
1))
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_clamp>`{.interpreted-text
role="ref"}

Returns a new color with all components clamped between the components
of `min` and `max`, by running
`@GlobalScope.clamp()<class_@GlobalScope_method_clamp>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_darkened}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **darkened**(amount:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_darkened>`{.interpreted-text
role="ref"}

Returns a new color resulting from making this color darker by the
specified `amount` (ratio from 0.0 to 1.0). See also
`lightened()<class_Color_method_lightened>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var green = Color(0.0, 1.0, 0.0) var darkgreen = green.darkened(0.2) \#
20% darker than regular green
:::

::: code-tab
csharp

var green = new Color(0.0f, 1.0f, 0.0f); Color darkgreen =
green.Darkened(0.2f); // 20% darker than regular green
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_from_hsv}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **from_hsv**(h:
`float<class_float>`{.interpreted-text role="ref"}, s:
`float<class_float>`{.interpreted-text role="ref"}, v:
`float<class_float>`{.interpreted-text role="ref"}, alpha:
`float<class_float>`{.interpreted-text role="ref"} = 1.0)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_from_hsv>`{.interpreted-text
role="ref"}

Constructs a color from an [HSV
profile](https://en.wikipedia.org/wiki/HSL_and_HSV). The hue (`h`),
saturation (`s`), and value (`v`) are typically between 0.0 and 1.0.

::::: tabs
::: code-tab
gdscript

var color = Color.from_hsv(0.58, 0.5, 0.79, 0.8)
:::

::: code-tab
csharp

var color = Color.FromHsv(0.58f, 0.5f, 0.79f, 0.8f);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_from_ok_hsl}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **from_ok_hsl**(h:
`float<class_float>`{.interpreted-text role="ref"}, s:
`float<class_float>`{.interpreted-text role="ref"}, l:
`float<class_float>`{.interpreted-text role="ref"}, alpha:
`float<class_float>`{.interpreted-text role="ref"} = 1.0)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_from_ok_hsl>`{.interpreted-text
role="ref"}

Constructs a color from an [OK HSL
profile](https://bottosson.github.io/posts/colorpicker/). The hue (`h`),
saturation (`s`), and lightness (`l`) are typically between 0.0 and 1.0.

::::: tabs
::: code-tab
gdscript

var color = Color.from_ok_hsl(0.58, 0.5, 0.79, 0.8)
:::

::: code-tab
csharp

var color = Color.FromOkHsl(0.58f, 0.5f, 0.79f, 0.8f);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_from_rgba8}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **from_rgba8**(r8:
`int<class_int>`{.interpreted-text role="ref"}, g8:
`int<class_int>`{.interpreted-text role="ref"}, b8:
`int<class_int>`{.interpreted-text role="ref"}, a8:
`int<class_int>`{.interpreted-text role="ref"} = 255)
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_from_rgba8>`{.interpreted-text
role="ref"}

Returns a **Color** constructed from red (`r8`), green (`g8`), blue
(`b8`), and optionally alpha (`a8`) integer channels, each divided by
`255.0` for their final value.

    var red = Color.from_rgba8(255, 0, 0)             # Same as Color(1, 0, 0).
    var dark_blue = Color.from_rgba8(0, 0, 51)        # Same as Color(0, 0, 0.2).
    var my_color = Color.from_rgba8(306, 255, 0, 102) # Same as Color(1.2, 1, 0, 0.4).

\*\*Note:\*\* Due to the lower precision of
`from_rgba8()<class_Color_method_from_rgba8>`{.interpreted-text
role="ref"} compared to the standard **Color** constructor, a color
created with
`from_rgba8()<class_Color_method_from_rgba8>`{.interpreted-text
role="ref"} will generally not be equal to the same color created with
the standard **Color** constructor. Use
`is_equal_approx()<class_Color_method_is_equal_approx>`{.interpreted-text
role="ref"} for comparisons to avoid issues with floating-point
precision error.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_from_rgbe9995}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**from_rgbe9995**(rgbe: `int<class_int>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_from_rgbe9995>`{.interpreted-text
role="ref"}

Decodes a **Color** from an RGBE9995 format integer. See
`Image.FORMAT_RGBE9995<class_Image_constant_FORMAT_RGBE9995>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_from_string}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **from_string**(str:
`String<class_String>`{.interpreted-text role="ref"}, default:
`Color<class_Color>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_from_string>`{.interpreted-text
role="ref"}

Creates a **Color** from the given string, which can be either an HTML
color code or a named color (case-insensitive). Returns `default` if the
color cannot be inferred from the string.

If you want to create a color from String in a constant expression, use
the equivalent constructor instead (i.e. `Color("color string")`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_get_luminance}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_luminance**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_get_luminance>`{.interpreted-text
role="ref"}

Returns the light intensity of the color, as a value between 0.0 and 1.0
(inclusive). This is useful when determining light or dark color. Colors
with a luminance smaller than 0.5 can be generally considered dark.

\*\*Note:\*\*
`get_luminance()<class_Color_method_get_luminance>`{.interpreted-text
role="ref"} relies on the color being in the linear color space to
return an accurate relative luminance value. If the color is in the sRGB
color space, use
`srgb_to_linear()<class_Color_method_srgb_to_linear>`{.interpreted-text
role="ref"} to convert it to the linear color space first.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_hex}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **hex**(hex:
`int<class_int>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_hex>`{.interpreted-text role="ref"}

Returns the **Color** associated with the provided `hex` integer in
32-bit RGBA format (8 bits per channel). This method is the inverse of
`to_rgba32()<class_Color_method_to_rgba32>`{.interpreted-text
role="ref"}.

In GDScript and C#, the `int<class_int>`{.interpreted-text role="ref"}
is best visualized with hexadecimal notation (`"0x"` prefix, making it
`"0xRRGGBBAA"`).

::::: tabs
::: code-tab
gdscript

var red = Color.hex(0xff0000ff) var dark_cyan = Color.hex(0x008b8bff)
var my_color = Color.hex(0xbbefd2a4)
:::

::: code-tab
csharp

var red = new Color(0xff0000ff); var dark_cyan = new Color(0x008b8bff);
var my_color = new Color(0xbbefd2a4);
:::
:::::

If you want to use hex notation in a constant expression, use the
equivalent constructor instead (i.e. `Color(0xRRGGBBAA)`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_hex64}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **hex64**(hex:
`int<class_int>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_hex64>`{.interpreted-text
role="ref"}

Returns the **Color** associated with the provided `hex` integer in
64-bit RGBA format (16 bits per channel). This method is the inverse of
`to_rgba64()<class_Color_method_to_rgba64>`{.interpreted-text
role="ref"}.

In GDScript and C#, the `int<class_int>`{.interpreted-text role="ref"}
is best visualized with hexadecimal notation (`"0x"` prefix, making it
`"0xRRRRGGGGBBBBAAAA"`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_html}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **html**(rgba:
`String<class_String>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_html>`{.interpreted-text role="ref"}

Returns a new color from `rgba`, an HTML hexadecimal color string.
`rgba` is not case-sensitive, and may be prefixed by a hash sign (`#`).

`rgba` must be a valid three-digit or six-digit hexadecimal color
string, and may contain an alpha channel value. If `rgba` does not
contain an alpha channel value, an alpha channel value of 1.0 is
applied. If `rgba` is invalid, returns an empty color.

::::: tabs
::: code-tab
gdscript

var blue = Color.html(\"#0000ff\") \# blue is Color(0.0, 0.0, 1.0, 1.0)
var green = Color.html(\"#0F0\") \# green is Color(0.0, 1.0, 0.0, 1.0)
var col = Color.html(\"663399cc\") \# col is Color(0.4, 0.2, 0.6, 0.8)
:::

::: code-tab
csharp

var blue = Color.FromHtml(\"#0000ff\"); // blue is Color(0.0, 0.0, 1.0,
1.0) var green = Color.FromHtml(\"#0F0\"); // green is Color(0.0, 1.0,
0.0, 1.0) var col = Color.FromHtml(\"663399cc\"); // col is Color(0.4,
0.2, 0.6, 0.8)
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_html_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**html_is_valid**(color: `String<class_String>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_html_is_valid>`{.interpreted-text
role="ref"}

Returns `true` if `color` is a valid HTML hexadecimal color string. The
string must be a hexadecimal value (case-insensitive) of either 3, 4, 6
or 8 digits, and may be prefixed by a hash sign (`#`). This method is
identical to
`String.is_valid_html_color()<class_String_method_is_valid_html_color>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

Color.html_is_valid(\"#55aaFF\") \# Returns true
Color.html_is_valid(\"#55AAFF20\") \# Returns true
Color.html_is_valid(\"55AAFF\") \# Returns true
Color.html_is_valid(\"#F2C\") \# Returns true

Color.html_is_valid(\"#AABBC\") \# Returns false
Color.html_is_valid(\"#55aaFF5\") \# Returns false
:::

::: code-tab
csharp

Color.HtmlIsValid(\"#55AAFF\"); // Returns true
Color.HtmlIsValid(\"#55AAFF20\"); // Returns true
Color.HtmlIsValid(\"55AAFF\"); // Returns true
Color.HtmlIsValid(\"#F2C\"); // Returns true

Color.HtmlIsValid(\"#AABBC\"); // Returns false
Color.HtmlIsValid(\"#55aaFF5\"); // Returns false
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_inverted}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **inverted**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_inverted>`{.interpreted-text
role="ref"}

Returns the color with its `r<class_Color_property_r>`{.interpreted-text
role="ref"}, `g<class_Color_property_g>`{.interpreted-text role="ref"},
and `b<class_Color_property_b>`{.interpreted-text role="ref"} components
inverted (`(1 - r, 1 - g, 1 - b, a)`).

::::: tabs
::: code-tab
gdscript

var black = Color.WHITE.inverted() var color = Color(0.3, 0.4, 0.9) var
inverted_color = color.inverted() \# Equivalent to [Color(0.7, 0.6,
0.1)]{.title-ref}
:::

::: code-tab
csharp

var black = Colors.White.Inverted(); var color = new Color(0.3f, 0.4f,
0.9f); Color invertedColor = color.Inverted(); // Equivalent to [new
Color(0.7f, 0.6f, 0.1f)]{.title-ref}
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_is_equal_approx}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_equal_approx**(to:
`Color<class_Color>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_is_equal_approx>`{.interpreted-text
role="ref"}

Returns `true` if this color and `to` are approximately equal, by
running
`@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>`{.interpreted-text
role="ref"} on each component.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_lerp}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **lerp**(to:
`Color<class_Color>`{.interpreted-text role="ref"}, weight:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_lerp>`{.interpreted-text role="ref"}

Returns the linear interpolation between this color\'s components and
`to`\'s components. The interpolation factor `weight` should be between
0.0 and 1.0 (inclusive). See also
`@GlobalScope.lerp()<class_@GlobalScope_method_lerp>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var red = Color(1.0, 0.0, 0.0) var aqua = Color(0.0, 1.0, 0.8)

red.lerp(aqua, 0.2) \# Returns Color(0.8, 0.2, 0.16) red.lerp(aqua, 0.5)
\# Returns Color(0.5, 0.5, 0.4) red.lerp(aqua, 1.0) \# Returns
Color(0.0, 1.0, 0.8)
:::

::: code-tab
csharp

var red = new Color(1.0f, 0.0f, 0.0f); var aqua = new Color(0.0f, 1.0f,
0.8f);

red.Lerp(aqua, 0.2f); // Returns Color(0.8f, 0.2f, 0.16f) red.Lerp(aqua,
0.5f); // Returns Color(0.5f, 0.5f, 0.4f) red.Lerp(aqua, 1.0f); //
Returns Color(0.0f, 1.0f, 0.8f)
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_lightened}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **lightened**(amount:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_lightened>`{.interpreted-text
role="ref"}

Returns a new color resulting from making this color lighter by the
specified `amount`, which should be a ratio from 0.0 to 1.0. See also
`darkened()<class_Color_method_darkened>`{.interpreted-text role="ref"}.

::::: tabs
::: code-tab
gdscript

var green = Color(0.0, 1.0, 0.0) var light_green = green.lightened(0.2)
\# 20% lighter than regular green
:::

::: code-tab
csharp

var green = new Color(0.0f, 1.0f, 0.0f); Color lightGreen =
green.Lightened(0.2f); // 20% lighter than regular green
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_linear_to_srgb}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **linear_to_srgb**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_linear_to_srgb>`{.interpreted-text
role="ref"}

Returns the color converted to the
[sRGB](https://en.wikipedia.org/wiki/SRGB) color space. This method
assumes the original color is in the linear color space. See also
`srgb_to_linear()<class_Color_method_srgb_to_linear>`{.interpreted-text
role="ref"} which performs the opposite operation.

\*\*Note:\*\* The color\'s `a<class_Color_property_a>`{.interpreted-text
role="ref"}lpha channel is not affected. The alpha channel is always
stored with linear encoding, regardless of the color space of the other
color channels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_srgb_to_linear}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **srgb_to_linear**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_srgb_to_linear>`{.interpreted-text
role="ref"}

Returns the color converted to the linear color space. This method
assumes the original color already is in the sRGB color space. See also
`linear_to_srgb()<class_Color_method_linear_to_srgb>`{.interpreted-text
role="ref"} which performs the opposite operation.

\*\*Note:\*\* The color\'s `a<class_Color_property_a>`{.interpreted-text
role="ref"}lpha channel is not affected. The alpha channel is always
stored with linear encoding, regardless of the color space of the other
color channels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_to_abgr32}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **to_abgr32**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_to_abgr32>`{.interpreted-text
role="ref"}

Returns the color converted to a 32-bit integer in ABGR format (each
component is 8 bits). ABGR is the reversed version of the default RGBA
format.

::::: tabs
::: code-tab
gdscript

var color = Color(1, 0.5, 0.2) print(color.to_abgr32()) \# Prints
4281565439
:::

::: code-tab
csharp

var color = new Color(1.0f, 0.5f, 0.2f); GD.Print(color.ToAbgr32()); //
Prints 4281565439
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_to_abgr64}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **to_abgr64**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_to_abgr64>`{.interpreted-text
role="ref"}

Returns the color converted to a 64-bit integer in ABGR format (each
component is 16 bits). ABGR is the reversed version of the default RGBA
format.

::::: tabs
::: code-tab
gdscript

var color = Color(1, 0.5, 0.2) print(color.to_abgr64()) \# Prints
-225178692812801
:::

::: code-tab
csharp

var color = new Color(1.0f, 0.5f, 0.2f); GD.Print(color.ToAbgr64()); //
Prints -225178692812801
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_to_argb32}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **to_argb32**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_to_argb32>`{.interpreted-text
role="ref"}

Returns the color converted to a 32-bit integer in ARGB format (each
component is 8 bits). ARGB is more compatible with DirectX.

::::: tabs
::: code-tab
gdscript

var color = Color(1, 0.5, 0.2) print(color.to_argb32()) \# Prints
4294934323
:::

::: code-tab
csharp

var color = new Color(1.0f, 0.5f, 0.2f); GD.Print(color.ToArgb32()); //
Prints 4294934323
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_to_argb64}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **to_argb64**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_to_argb64>`{.interpreted-text
role="ref"}

Returns the color converted to a 64-bit integer in ARGB format (each
component is 16 bits). ARGB is more compatible with DirectX.

::::: tabs
::: code-tab
gdscript

var color = Color(1, 0.5, 0.2) print(color.to_argb64()) \# Prints
-2147470541
:::

::: code-tab
csharp

var color = new Color(1.0f, 0.5f, 0.2f); GD.Print(color.ToArgb64()); //
Prints -2147470541
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_to_html}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**to_html**(with_alpha: `bool<class_bool>`{.interpreted-text role="ref"}
= true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_to_html>`{.interpreted-text
role="ref"}

Returns the color converted to an HTML hexadecimal color
`String<class_String>`{.interpreted-text role="ref"} in RGBA format,
without the hash (`#`) prefix.

Setting `with_alpha` to `false`, excludes alpha from the hexadecimal
string, using RGB format instead of RGBA format.

::::: tabs
::: code-tab
gdscript

var white = Color(1, 1, 1, 0.5) var with_alpha = white.to_html() \#
Returns \"ffffff7f\" var without_alpha = white.to_html(false) \# Returns
\"ffffff\"
:::

::: code-tab
csharp

var white = new Color(1, 1, 1, 0.5f); string withAlpha = white.ToHtml();
// Returns \"ffffff7f\" string withoutAlpha = white.ToHtml(false); //
Returns \"ffffff\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_to_rgba32}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **to_rgba32**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_to_rgba32>`{.interpreted-text
role="ref"}

Returns the color converted to a 32-bit integer in RGBA format (each
component is 8 bits). RGBA is Godot\'s default format. This method is
the inverse of `hex()<class_Color_method_hex>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var color = Color(1, 0.5, 0.2) print(color.to_rgba32()) \# Prints
4286526463
:::

::: code-tab
csharp

var color = new Color(1, 0.5f, 0.2f); GD.Print(color.ToRgba32()); //
Prints 4286526463
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_method_to_rgba64}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **to_rgba64**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Color_method_to_rgba64>`{.interpreted-text
role="ref"}

Returns the color converted to a 64-bit integer in RGBA format (each
component is 16 bits). RGBA is Godot\'s default format. This method is
the inverse of `hex64()<class_Color_method_hex64>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

var color = Color(1, 0.5, 0.2) print(color.to_rgba64()) \# Prints
-140736629309441
:::

::: code-tab
csharp

var color = new Color(1, 0.5f, 0.2f); GD.Print(color.ToRgba64()); //
Prints -140736629309441
:::
:::::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Operator Descriptions

:::: {#class_Color_operator_neq_Color}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator !=**(right:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_neq_Color>`{.interpreted-text role="ref"}

Returns `true` if the colors are not exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Color_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_mul_Color}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator**\*(right:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_mul_Color>`{.interpreted-text role="ref"}

Multiplies each component of the **Color** by the components of the
given **Color**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_mul_float}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator**\*(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_mul_float>`{.interpreted-text role="ref"}

Multiplies each component of the **Color** by the given
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_mul_int}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator**\*(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_mul_int>`{.interpreted-text role="ref"}

Multiplies each component of the **Color** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_sum_Color}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator +**(right:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_sum_Color>`{.interpreted-text role="ref"}

Adds each component of the **Color** with the components of the given
**Color**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_dif_Color}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator -**(right:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_dif_Color>`{.interpreted-text role="ref"}

Subtracts each component of the **Color** by the components of the given
**Color**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_div_Color}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator /**(right:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_div_Color>`{.interpreted-text role="ref"}

Divides each component of the **Color** by the components of the given
**Color**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_div_float}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator /**(right:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_div_float>`{.interpreted-text role="ref"}

Divides each component of the **Color** by the given
`float<class_float>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_div_int}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator /**(right:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_div_int>`{.interpreted-text role="ref"}

Divides each component of the **Color** by the given
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_eq_Color}
::: rst-class
classref-operator
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **operator ==**(right:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_eq_Color>`{.interpreted-text role="ref"}

Returns `true` if the colors are exactly equal.

\*\*Note:\*\* Due to floating-point precision errors, consider using
`is_equal_approx()<class_Color_method_is_equal_approx>`{.interpreted-text
role="ref"} instead, which is more reliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_idx_int}
::: rst-class
classref-operator
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **operator
\[\]**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Color_operator_idx_int>`{.interpreted-text role="ref"}

Access color components using their index. `[0]` is equivalent to
`r<class_Color_property_r>`{.interpreted-text role="ref"}, `[1]` is
equivalent to `g<class_Color_property_g>`{.interpreted-text role="ref"},
`[2]` is equivalent to `b<class_Color_property_b>`{.interpreted-text
role="ref"}, and `[3]` is equivalent to
`a<class_Color_property_a>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_unplus}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator unary+**()
`🔗<class_Color_operator_unplus>`{.interpreted-text role="ref"}

Returns the same value as if the `+` was not there. Unary `+` does
nothing, but sometimes it can make your code more readable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Color_operator_unminus}
::: rst-class
classref-operator
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **operator unary-**()
`🔗<class_Color_operator_unminus>`{.interpreted-text role="ref"}

Inverts the given color. This is equivalent to `Color.WHITE - c` or
`Color(1 - c.r, 1 - c.g, 1 - c.b, 1 - c.a)`. Unlike with
`inverted()<class_Color_method_inverted>`{.interpreted-text role="ref"},
the `a<class_Color_property_a>`{.interpreted-text role="ref"} component
is inverted, too.
