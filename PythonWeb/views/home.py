import reflex as rx
from PythonWeb.components.navbar import navbar
from PythonWeb.components.footer import footer
from PythonWeb.views.header.header import header
from PythonWeb.views.sections import projects_section, certs_section, socials_section
from PythonWeb.styles.styles import MAX_WIDTH
from PythonWeb.state.PageState import PageState
from PythonWeb.constants import TEXTS
import PythonWeb.utils as utils


def home(lang: str, home_route: str) -> rx.Component:
    """Página principal común a ambos idiomas."""
    t = TEXTS[lang]
    return rx.box(
        utils.lang_script(lang),
        navbar(t, home_route, live=PageState.is_live),
        rx.vstack(
            header(t, PageState.is_live),
            projects_section(t, lang),
            certs_section(t, lang),
            socials_section(t, lang),
            spacing="9",
            width="100%",
            max_width=MAX_WIDTH,
            margin_x="auto",
            padding_x=rx.breakpoints(initial="1em", sm="1.5em"),
            padding_y="2em",
        ),
        footer(),
    )
