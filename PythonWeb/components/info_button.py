import reflex as rx
from PythonWeb.components.no_link_button import no_link_button
from PythonWeb.components.title import title
from PythonWeb.styles.styles import *
from PythonWeb.state.PageState import PageState

def info_button(titulo: str, enlaces: list) -> rx.Component:
    componentes = [title(titulo)]
    for enlace in enlaces:
        componentes.append(
            no_link_button(
                enlace['title'],
                enlace['subtitle'],
                icon_path=enlace['icon_path']
            )
        )
    return rx.vstack(*componentes, align="start", width="100%")


def twitch_info_panel(titulo: str, info: str, img_path: str, alt='') -> rx.Component:
    return rx.box(
        rx.link(
        rx.hstack(
            rx.image(
                src=img_path,
                width=Size.XXLARGE.value,
                height=Size.XXLARGE.value,
                margin=Size.MEDIUM.value,
                alt=alt,
                class_name="shake",
                ),
                rx.vstack(
                    rx.text(f'{PageState.live_user} {titulo}',
                            style=button_title_style,
                            color=Color.PRIMARY.value,
                            margin_left=Size.MEDIUM.value
                            ),
                    rx.text(info,
                            style=button_body_style,
                            color=Color.PRIMARY.value,
                            margin_left=Size.MEDIUM.value
                            ),
                    spacing='0',

                    ),
                href=f"https://www.twitch.tv/{PageState.live_user}",
                is_external=True,
            ),
            href=f"https://www.twitch.tv/{PageState.live_user}",
            is_external=True),
            width="100%",
            align_items="center",
        style=no_button_style,
    )

def github_info():
    pass