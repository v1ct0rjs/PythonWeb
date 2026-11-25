from enum import Enum
import reflex as rx
from .colors import Colors as Color
from .colors import TextColor as TextColor
from .colors import Fonts as Fonts

MAX_WIDTH = '1100px'
MONO = f"'{Fonts.JETBRAINS_MONO.value}', ui-monospace, monospace"
SANS = f"'{Fonts.INTER.value}', system-ui, sans-serif"


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


BASE_STYLE = {
    "font_family": SANS,
    "color": TextColor.BODY.value,
    "background_color": Color.BACKGROUND.value,
    rx.link: {
        "text_decoration": "none",
        "color": "inherit",
        "_hover": {"text_decoration": "none"},
    },
}

# --- Tarjetas ---------------------------------------------------------------

card_style = dict(
    display="block",
    width="100%",
    height="100%",
    background_color=Color.SURFACE.value,
    border=f"1px solid {Color.BORDER.value}",
    border_radius="12px",
    padding="1.1em 1.2em",
)

card_title_style = dict(
    font_family=MONO,
    font_weight="600",
    font_size="1.05em",
    color=TextColor.BODY.value,
)

card_body_style = dict(
    font_size="0.92em",
    line_height="1.5",
    color=TextColor.MUTED.value,
)

tag_style = dict(
    font_family=MONO,
    font_size="0.72em",
    padding="0.15em 0.6em",
    border_radius="999px",
    color=TextColor.PRIMARY.value,
    background_color="rgba(29, 211, 176, 0.08)",
    border="1px solid rgba(29, 211, 176, 0.3)",
    white_space="nowrap",
)

# --- Botones de acción -------------------------------------------------------

_cta_base = dict(
    display="inline-flex",
    align_items="center",
    gap="0.5em",
    font_family=MONO,
    font_weight="600",
    font_size="0.9em",
    padding="0.6em 1.1em",
    border_radius="8px",
    transition="background-color .2s ease, color .2s ease",
)

cta_primary_style = dict(
    _cta_base,
    background_color=Color.PRIMARY.value,
    color=TextColor.BLACK.value,
    border=f"1px solid {Color.PRIMARY.value}",
    _hover=dict(background_color=Color.SECONDARY.value, color=TextColor.BLACK.value),
)

cta_secondary_style = dict(
    _cta_base,
    background_color="transparent",
    color=TextColor.PRIMARY.value,
    border=f"1px solid {Color.PRIMARY.value}",
    _hover=dict(background_color="rgba(29, 211, 176, 0.1)", color=TextColor.PRIMARY.value),
)

# --- Navbar -----------------------------------------------------------------

navbar_style = dict(
    position="sticky",
    top="0",
    z_index="999",
    width="100%",
    padding="0.75em 1.25em",
    background_color="rgba(0, 0, 0, 0.75)",
    backdrop_filter="blur(8px)",
    border_bottom=f"1px solid {Color.BORDER.value}",
    font_family=MONO,
)

nav_link_style = dict(
    font_size="0.9em",
    color=TextColor.MUTED.value,
    _hover=dict(color=TextColor.PRIMARY.value),
)

# --- Secciones --------------------------------------------------------------

section_style = dict(
    width="100%",
    scroll_margin_top="5em",
    spacing="4",
    align="start",
)

subheading_style = dict(
    font_family=MONO,
    font_size="0.85em",
    text_transform="uppercase",
    letter_spacing="0.08em",
    color=TextColor.MUTED.value,
)
