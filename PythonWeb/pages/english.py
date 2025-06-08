import reflex as rx
from PythonWeb.routes import Route
from PythonWeb.components.navbar import navbar
from PythonWeb.views.header.header import header
from PythonWeb.views.links.links import links
from PythonWeb.components.footer import footer
from PythonWeb.styles.styles import *
from PythonWeb.constants import *
from PythonWeb.components.info_button import info_button
import PythonWeb.utils as utils
from PythonWeb.components.ant_components import language_button_index
from PythonWeb.state.PageState import PageState
from PythonWeb.routes import Route


@rx.page(
    route=Route.ENG.value,
    title=TEXT_TAB_TITLE,
    description=TEXT_ENG_HEADER,
    image=utils.avatar,
    meta=utils.eng_meta,
)
def eng() -> rx.Component:
    """English version of the main page."""
    return rx.box(
        utils.lang_en(),
        navbar(NAVBAR_ENG, live=PageState.is_live),
        rx.center(
            rx.vstack(
                header(
                    TEXT_ENG_TITULO,
                    TEXT_ENG_HEADER,
                    TEXT_ENG_COUNTRY,
                    TEXT_ENG_CONTACT,
                    PageState.is_live,
                    PageState.live_tittle,
                    "live",
                ),
                links("My Projects", projects),
                info_button("Certifications", certs),
                links("Social Networks", socials),
                align="center",
                max_width=MAX_WIDTH,
                spacing="6",
            ),
            width="100%",
            margin_y=Size.XLARGE,
        ),
        language_button_index(),
        footer(),
    )

