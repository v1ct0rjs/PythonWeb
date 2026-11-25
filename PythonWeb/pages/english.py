import reflex as rx
from PythonWeb.constants import TEXT_TAB_TITLE, TEXT_ENG_HEADER
from PythonWeb.routes import Route
from PythonWeb.views.home import home
import PythonWeb.utils as utils


@rx.page(
    route=Route.ENG.value,
    title=TEXT_TAB_TITLE,
    description=TEXT_ENG_HEADER,
    image=utils.avatar,
    meta=utils.eng_meta,
)
def eng() -> rx.Component:
    """English version of the main page."""
    return home("en", Route.ENG.value)
