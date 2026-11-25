import reflex as rx
from PythonWeb.styles.styles import navbar_style, nav_link_style, MONO
from PythonWeb.styles.colors import Colors as Color, TextColor
from PythonWeb.constants import URL_TWITCH


def nav_link(text: str, href: str) -> rx.Component:
    return rx.link(text, href=href, style=nav_link_style)


def navbar(t: dict, home: str, live=False) -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text(t["nav_brand"], display=rx.breakpoints(initial="none", lg="block")),
            rx.text("~/v1ct0r", display=rx.breakpoints(initial="block", lg="none")),
            href=home,
            color=Color.PRIMARY.value,
            font_weight="600",
            font_size="1.05em",
        ),
        rx.spacer(),
        rx.hstack(
            nav_link(t["nav_projects"], "#proyectos"),
            nav_link(t["nav_certs"], "#certificaciones"),
            nav_link(t["nav_contact"], "#contacto"),
            spacing="5",
            display=rx.breakpoints(initial="none", sm="flex"),
        ),
        rx.cond(
            live,
            rx.link(
                rx.image(src="/twitch.svg", width="1.8em", height="1.8em", alt="Twitch en directo",
                         class_name="blink"),
                href=URL_TWITCH,
                is_external=True,
            ),
        ),
        rx.link(
            rx.hstack(rx.icon("languages", size=16), rx.text(t["lang_label"]), spacing="1", align="center"),
            href=t["lang_href"],
            title=t["lang_title"],
            aria_label=t["lang_title"],
            font_size="0.85em",
            font_family=MONO,
            padding="0.3em 0.7em",
            border=f"1px solid {Color.BORDER.value}",
            border_radius="6px",
            color=TextColor.BODY.value,
            _hover={"border_color": Color.PRIMARY.value, "color": TextColor.PRIMARY.value},
        ),
        align="center",
        spacing="5",
        style=navbar_style,
    )
