import reflex as rx
from PythonWeb.api.api import live

USER = "dj_10tacle"

class PageState(rx.State):
    is_live: bool
    live_tittle: str
    live_user: str

    async def check_live(self):
        live_data = await live(USER)
        self.is_live = live_data["live"]
        self.live_user = live_data["user"]
        self.live_tittle = live_data["title"]
