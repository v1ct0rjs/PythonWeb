import reflex as rx
from PythonWeb.api.api import live

USER = "dj_10tacle"

class PageState(rx.State):
    is_live: bool

    async def check_live(self) -> bool:
        self.is_live = await live(USER)

