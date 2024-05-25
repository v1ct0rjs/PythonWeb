import reflex as rx
from PythonWeb.components.navbar import navbar
from PythonWeb.views.header.header import header
from PythonWeb.views.links.links import links
from PythonWeb.components.footer import footer
from PythonWeb.styles.styles import *
from PythonWeb.constants import *
from PythonWeb.components.info_button import info_button

def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang = 'es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links('Mis Proyectos', proyectos),
                info_button('Certificaciones', certificados),
                links('Redes Sociales', enlaces),

                align="center",
                max_width=MAX_WIDTH,
                spacing='6',
                ),
            widht="100%",
            margin_y=Size.XLARGE,
        ),
        footer()
    )

app = rx.App(
    style=BASE_STYLE,
    stylesheets=GFONTS,
    head_components=[
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={GTAG}"),
        rx.script(
            """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-QFHWGRCS3T');
            """),
        ],
)
title = "V1cT0r's Portfolio"
description = TEXTO_HEADER
preview = "/assets/preview.png"

meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:title", "content": str(title)},
    {"name": "og:description", "content": str(description)},
    {"name": "og:image", "content": str(preview)},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@vmjimsan"},
]

app.add_page(index,
             title = title,
             description = description,
             image = "/assets/avatar.png",
             meta = meta)