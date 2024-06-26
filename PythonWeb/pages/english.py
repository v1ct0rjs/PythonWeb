import reflex as rx
from PythonWeb.components.navbar import navbar
from PythonWeb.views.header.header import header
from PythonWeb.views.links.links import links
from PythonWeb.components.footer import footer
from PythonWeb.styles.styles import *
from PythonWeb.constants import *
from PythonWeb.components.info_button import info_button
import PythonWeb.utils as utils
from PythonWeb.routes import Route
from PythonWeb.components.ant_components import FloatButtonIdex as float_button_index
from PythonWeb.state.PageState import PageState
@rx.page(
    route=Route.ENG.value,
    title=TEXT_TAB_TITLE,
    description=utils.eng_description,
    image=utils.avatar,
    meta=utils.eng_meta,
    on_load=[PageState.check_live, PageState.check_featured]
)
def eng() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(NAVBAR_ENG, live=PageState.is_live),
        rx.center(
            rx.vstack(
                header(TEXT_ENG_TITULO, TEXT_ENG_HEADER, TEXT_ENG_COUNTRY, TEXT_ENG_CONTACT, PageState.is_live, PageState.live_tittle, "is in live"),
                links('Projects', projects),
                info_button('Certifications', certs),
                links('Social Networks', socials),
                float_button_index(),
                align="center",
                max_width=MAX_WIDTH,
                spacing='6',
            ),
            widht="100%",
            margin_y=Size.XLARGE,
        ),
        footer()
    )
