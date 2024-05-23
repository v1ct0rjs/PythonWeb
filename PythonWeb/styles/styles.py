from enum import Enum
import reflex as rx
from .colors import Colors as Color
from .colors import TextColor as TextColor
from .colors import Fonts as Fonts

#constantes de estilo
MAX_WIDTH = '600px'


# Sizes

class Size(Enum):
    ZERO = '0'
    SMALL = '0.5em'
    MEDIUM = '0.8em'
    LARGE = '1em'
    MLARGE = '1.5em'
    XLARGE = '2em'
    XXLARGE = '4em'
    BIG = '6em'
    XBIG = '8em'

# Styles

BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
        "color": TextColor.BLACK.value,
        "background_color": Color.PRIMARY.value,
        "_hover": {
            "background_color": Color.WHITE.value,
        }
    },
    rx.link: {
        "text_decoration": "none",
        "color": "inherit",
        "_hover": {},
    }
}

button_title_style = dict(
    font_size=Size.MLARGE.value,
    color=TextColor.BLACK.value,
    font_family=Fonts.JETBRAINS_MONO.value,
)

button_body_style = dict(
    font_size=Size.LARGE.value,
    color=TextColor.CONTENT.value,
    font_family=Fonts.JETBRAINS_MONO.value,
)

head_stile = dict(
    width='100%',
    padding=Size.MEDIUM.value,
    color=Color.PRIMARY.value,
)

navbar_style = dict(
    position="sticky",
    #background="linear-gradient(to bottom, " + Color.CONTENT.value + ", transparent)",
    background=Color.BACKGROUND.value,
    padding_x=Size.SMALL.value,
    padding_y=Size.SMALL.value,
    z_index="999",
    top="0",
    font_family=Fonts.UBUNTU_SANS_MONO.value,
    font_weight="600",
)

no_button_style = dict(
        width="100%",
        height="100%",
        display="block",
        padding=Size.SMALL.value,
        border_radius=Size.SMALL.value,
        color=TextColor.BLACK.value,
        background_color=Color.BACKGROUND.value,
        border="4px",
        border_color=Color.PRIMARY.value,
        border_style="solid",
)
