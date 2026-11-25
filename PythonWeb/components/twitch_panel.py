import reflex as rx
from PythonWeb.styles.styles import card_style, card_title_style, card_body_style
from PythonWeb.styles.colors import Colors as Color
from PythonWeb.state.PageState import PageState


def twitch_panel(live_text: str) -> rx.Component:
    """Aviso de directo en Twitch (un único enlace, sin anidar)."""
    return rx.link(
        rx.hstack(
            rx.image(src="/twitch_norm.svg", width="3em", height="3em", alt="Logo de Twitch",
                     class_name="shake"),
            rx.vstack(
                rx.text(f"{PageState.live_user} {live_text}", style=card_title_style,
                        color=Color.PRIMARY.value),
                rx.text(PageState.live_tittle, style=card_body_style),
                spacing="1",
            ),
            align="center",
            spacing="4",
        ),
        href=f"https://www.twitch.tv/{PageState.live_user}",
        is_external=True,
        style=dict(card_style, border=f"1px solid {Color.PRIMARY.value}"),
        class_name="card",
    )
