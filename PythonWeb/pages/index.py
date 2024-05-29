import reflex as rx
from PythonWeb.components.navbar import navbar
from PythonWeb.views.header.header import header
from PythonWeb.views.links.links import links
from PythonWeb.components.footer import footer
from PythonWeb.styles.styles import *
from PythonWeb.constants import *
from PythonWeb.components.info_button import info_button
import PythonWeb.utils as utils
from PythonWeb.components.ant_components import float_button
from PythonWeb.api.api import hello

class IndexState(rx.State):
    @rx.var
    def say_hello(Self) -> str:
        return hello()


@rx.page(
    title=TEXT_TAB_TITLE,
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
                rx.text(IndexState.say_hello, color="white"),
                header(TEXTO_TITULO, TEXTO_HEADER, TEXTO_PAIS, TEXTO_CONTACTO),
                links('Mis Proyectos', proyectos),
                info_button('Certificaciones', certificados),
                links('Redes Sociales', enlaces),
                float_button(),
                align="center",
                max_width=MAX_WIDTH,
                spacing='6',
            ),
            widht="100%",
            margin_y=Size.XLARGE,
        ),
        footer()
    )
