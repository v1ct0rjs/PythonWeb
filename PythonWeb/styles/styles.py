from enum import Enum
import reflex as rx
#constantes de estilo
MAX_WIDTH = '600px'


# Sizes

class Size(Enum):
    SMALL = '0.5em'
    MEDIUM = '0.8em'
    LARGE = '1em'
    XLARGE = '2em'

# Styles

BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
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
    font_size=Size.MEDIUM.value
)

head_stile = dict(
    size='8',
    width='100%',
    padding=Size.MEDIUM.value
)

