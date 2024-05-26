import reflex as rx
from PythonWeb.components.navbar import navbar
from PythonWeb.views.header.header import header
from PythonWeb.views.links.links import links
from PythonWeb.components.footer import footer
from PythonWeb.styles.styles import *
from PythonWeb.constants import *
from PythonWeb.components.info_button import info_button
import PythonWeb.utils as utils


@rx.page(
    title=TEXTO_TITULO,
    description=TEXTO_HEADER,
    image=utils.avatar,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(NAVBAR_ESP),
        rx.center(
            rx.vstack(
                header(TEXTO_TITULO, TEXTO_HEADER, TEXTO_PAIS, TEXTO_CONTACTO),
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
