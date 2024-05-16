from enum import Enum
import reflex as rx
#constantes de estilo
MAX_WIDTH = '600px'


# Sizes

class Spacer(Enum):
    SMALL = '0.5em'
    MEDIUM = '1em'
    LARGE = '2em'
    XLARGE = '5em'

# Styles

BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Spacer.SMALL.value,
        "border_radius": Spacer.MEDIUM.value,
    }
}