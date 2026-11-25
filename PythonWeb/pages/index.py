import reflex as rx
from PythonWeb.constants import TEXT_TAB_TITLE, TEXTO_HEADER
from PythonWeb.routes import Route
from PythonWeb.views.home import home
import PythonWeb.utils as utils


@rx.page(
    title=TEXT_TAB_TITLE,
    description=TEXTO_HEADER,
    image=utils.avatar,
    meta=utils.index_meta,
)
def index() -> rx.Component:
    return home("es", Route.INDEX.value)
