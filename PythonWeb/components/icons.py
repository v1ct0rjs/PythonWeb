import reflex as rx
from PythonWeb.styles.colors import Colors as Color


def mask_icon(src: str, size: str = "1.5em", color: str = Color.PRIMARY.value) -> rx.Component:
    """Pinta un SVG monocromo con el color indicado usando CSS mask."""
    return rx.box(
        width=size,
        height=size,
        min_width=size,
        background_color=color,
        style={
            "mask": f"url({src}) no-repeat center / contain",
            "-webkit-mask": f"url({src}) no-repeat center / contain",
        },
    )


def accent_icon(icon: str, icon_path: str | None = None, size: str = "1.5em") -> rx.Component:
    """Icono en color de acento: SVG propio (mask), imagen o icono Lucide."""
    if icon_path and icon_path.endswith(".svg"):
        return mask_icon(icon_path, size)
    if icon_path:
        return rx.image(src=icon_path, width=size, height=size, alt="", object_fit="contain")
    return rx.icon(tag=icon, size=22, color=Color.PRIMARY.value, min_width="22px")


def icon_link(url: str, label: str, icon: str | None = None, src: str | None = None) -> rx.Component:
    """Icono enlazado (redes/contacto) con etiqueta accesible."""
    content = mask_icon(src, "20px") if src else rx.icon(tag=icon, size=20, color=Color.PRIMARY.value)
    return rx.link(
        content,
        href=url,
        is_external=True,
        aria_label=label,
        title=label,
        opacity="0.85",
        _hover={"opacity": "1"},
    )
