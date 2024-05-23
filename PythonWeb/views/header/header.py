import reflex as rx
from PythonWeb.styles.styles import *
from PythonWeb.components.link_icon import link_icon
from PythonWeb.components.info_text import info_text
from PythonWeb.styles.colors import Colors as Color
from PythonWeb.styles.colors import Fonts as Fonts
from PythonWeb.constants import *

def header () -> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.avatar(name="Víctor Jiménez",
                  border_color=Color.CONTENT.value,
                  border_width='3px',
                  src="avatar.png",
                  alt="Avatar de Víctor Jiménez",
                  fallback='VJ',
                  variant="solid",
                  high_contrast=False,
                  radius="full",
                  size='8'),
        rx.vstack(
        rx.heading("Víctor Jiménez",
                   font_size=Size.XLARGE.value,
                   margin_bottom="-15px",
                   margin_top="5px",
                   color=Color.PRIMARY.value,
                   font_family=Fonts.JETBRAINS_MONO.value,
                   font_weight="700"),
        rx.text(TEXTO_TITULO,
                font_size=Size.MEDIUM.value,
                color=TextColor.WHITE.value),
            rx.hstack(
                rx.flex(
                    info_text(
                        "Zafra, Badajoz, Extremadura", "España"),
                ),
            ),
            rx.hstack(rx.text("Contacto: ", font_size=Size.MEDIUM.value, color=TextColor.WHITE.value),
                link_icon("mailto:vmjimenezs02@educarex.es", "mail"),
                link_icon("https://t.me/p3sc4", "send"),
                color=Color.PRIMARY.value,
            ),
        ),
        spacing = '5'
        ),
        rx.text(TEXTO_HEADER,
                font_size=Size.LARGE.value,
                color=TextColor.WHITE.value),
        align_items="start",
        spacing='5',
        font_family=Fonts.JETBRAINS_MONO.value,
    )