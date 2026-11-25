import reflex as rx
from PythonWeb.styles.styles import MONO, cta_primary_style, cta_secondary_style
from PythonWeb.styles.colors import Colors as Color, TextColor
from PythonWeb.components.icons import icon_link
from PythonWeb.components.twitch_panel import twitch_panel
from PythonWeb.constants import URL_GITHUB, URL_LINKEDIN, URL_EMAIL, URL_TELEGRAM


def header(t: dict, is_live) -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.avatar(
                name="Víctor Jiménez",
                src="/avatar.png",
                alt="Avatar de Víctor Jiménez",
                fallback="VJ",
                radius="full",
                size=rx.breakpoints(initial="8", md="9"),
                border=f"2px solid {Color.PRIMARY.value}",
                box_shadow="0 0 40px rgba(29, 211, 176, 0.25)",
            ),
            rx.vstack(
                rx.text("$ whoami", font_family=MONO, font_size="0.85em", color=TextColor.MUTED.value),
                rx.heading(
                    "Víctor Jiménez",
                    as_="h1",
                    font_family=MONO,
                    font_weight="700",
                    font_size=rx.breakpoints(initial="2em", sm="2.6em"),
                    line_height="1.1",
                    color=TextColor.PRIMARY.value,
                ),
                rx.text(t["role"], font_size="1.1em", font_weight="500", color=TextColor.BODY.value),
                rx.hstack(
                    rx.icon("map-pin", size=15),
                    rx.text(t["location"], font_size="0.9em"),
                    spacing="1",
                    align="center",
                    color=TextColor.MUTED.value,
                ),
                spacing="2",
                align=rx.breakpoints(initial="center", sm="start"),
                text_align=rx.breakpoints(initial="center", sm="left"),
            ),
            direction=rx.breakpoints(initial="column", sm="row"),
            align="center",
            gap="2em",
            width="100%",
        ),
        rx.text(t["bio"], font_size="1.05em", line_height="1.7", color=TextColor.MUTED.value,
                max_width="65ch"),
        rx.flex(
            rx.link(t["cta_projects"], rx.icon("arrow-down", size=16), href="#proyectos",
                    style=cta_primary_style),
            rx.link(t["cta_contact"], rx.icon("mail", size=16), href=URL_EMAIL, is_external=True,
                    style=cta_secondary_style),
            rx.hstack(
                icon_link(URL_GITHUB, "GitHub", src="/github.svg"),
                icon_link(URL_LINKEDIN, "LinkedIn", src="/linkedin.svg"),
                icon_link(URL_TELEGRAM, "Telegram", icon="send"),
                spacing="4",
                align="center",
                padding_left="0.5em",
            ),
            wrap="wrap",
            align="center",
            gap="1em",
        ),
        rx.cond(is_live, twitch_panel(t["live"])),
        spacing="6",
        width="100%",
        padding_top=rx.breakpoints(initial="1em", sm="3em"),
    )
