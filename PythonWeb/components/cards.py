import reflex as rx
from PythonWeb.styles.styles import (
    card_style, card_title_style, card_body_style, tag_style,
)
from PythonWeb.styles.colors import TextColor
from PythonWeb.components.icons import accent_icon, mask_icon


def tag(text: str) -> rx.Component:
    return rx.box(text, style=tag_style)


def project_card(project: dict, lang: str) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.hstack(
                accent_icon(project["icon"], project.get("icon_path")),
                rx.text(project["title"], style=card_title_style),
                rx.spacer(),
                rx.icon("arrow-up-right", size=18, color=TextColor.MUTED.value, class_name="card-arrow",
                        min_width="18px"),
                align="center",
                width="100%",
                spacing="3",
            ),
            rx.text(project["desc"][lang], style=card_body_style),
            rx.spacer(),
            rx.flex(*[tag(t) for t in project["tags"]], wrap="wrap", gap="0.4em"),
            spacing="3",
            align="start",
            height="100%",
        ),
        href=project["url"],
        is_external=True,
        style=card_style,
        class_name="card",
    )


def info_card(item: dict, lang: str, image_size: str = "3em") -> rx.Component:
    """Tarjeta compacta: certificaciones (sin enlace) o redes (con enlace)."""
    path = item["icon_path"]
    icon = mask_icon(path, "1.6em") if path.endswith(".svg") else rx.image(
        src=path, width=image_size, height=image_size, object_fit="contain", alt=item["title"])
    body = rx.hstack(
        icon,
        rx.vstack(
            rx.text(item["title"], style=card_title_style),
            rx.text(item["desc"][lang], style=card_body_style),
            spacing="0",
        ),
        align="center",
        spacing="4",
    )
    if "url" in item:
        return rx.link(body, href=item["url"], is_external=True, style=card_style, class_name="card")
    return rx.box(body, style=card_style)
