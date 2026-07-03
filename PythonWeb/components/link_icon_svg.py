

from PythonWeb.styles.styles import *

def link_icon_svg(url: str, src: str, alt: str = "") -> rx.Component:
    return rx.link(
        rx.box(
            width="20px",
            height="20px",
            background_color=Color.PRIMARY.value,
            style={
                "mask": f"url({src}) no-repeat center / contain",
                "-webkit-mask": f"url({src}) no-repeat center / contain",
            },
            aria_label=alt,
        ),
        href=url,
        is_external=True,
    )