import reflex as rx
from PythonWeb.styles.styles import *
from PythonWeb.components.link_icon import link_icon
from PythonWeb.components.info_text import info_text
from PythonWeb.styles.colors import Colors as Color
from PythonWeb.styles.colors import Fonts as Fonts
from PythonWeb.components.info_button import *
from PythonWeb.model.Live import Live

def header (titulo: str, header: str, country: str, contact: str, cola='', live=Live(is_live=False, live_tittle='', live_user='')) -> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.avatar(
                  name="Víctor Jiménez",
                  border_color=Color.CONTENT.value,
                  border_width='3px',
                  src="/avatar.png",
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
        rx.text(titulo,
                font_size=Size.MEDIUM.value,
                color=TextColor.WHITE.value),
            rx.hstack(
                rx.flex(
                    info_text(
                        "Zafra, Badajoz, Extremadura", country),
                ),
            ),
            rx.hstack(rx.text(contact, font_size=Size.MEDIUM.value, color=TextColor.WHITE.value),
                link_icon("mailto:vmjimenezs02@educarex.es", "mail"),
                link_icon("https://t.me/p3sc4", "send"),
                color=Color.PRIMARY.value,
            ),
        ),
        spacing = '5'
        ),
        rx.cond(
            live.is_live,
            twitch_info_panel(cola, live.live_tittle, "/twitch_norm.svg", "Logo de Twitch"),

        ),
        rx.text(header,
                font_size=Size.LARGE.value,
                color=TextColor.WHITE.value),
        align_items="start",
        spacing='5',
        font_family=Fonts.JETBRAINS_MONO.value,
    )