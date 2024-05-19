from enum import Enum
import reflex as rx
from .colors import Colors as Color
from .colors import TextColor as TextColor

#constantes de estilo
MAX_WIDTH = '600px'


# Sizes

class Size(Enum):
    SMALL = '0.5em'
    MEDIUM = '0.8em'
    LARGE = '1em'
    MLARGE = '1.5em'
    XLARGE = '2em'

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
        "background_color": Color.DARKORANGE.value,
        "_hover": {
            "background_color": Color.CONTENT.value,
        }
    },
    rx.link: {
        "text_decoration": "none",
        "color": "inherit",
        "_hover": {},
    }
}

button_title_style = dict(
    font_size=Size.LARGE.value
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.GREY.value
)

head_stile = dict(
    width='100%',
    padding=Size.MEDIUM.value,
)

