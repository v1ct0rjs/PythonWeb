import reflex as rx
from PythonWeb.api.api import live, featured

USER = "v1ct0rdev"

class PageState(rx.State):
    is_live: bool
    live_tittle: str
    live_user: str
    featured_data: list

    # async def check_live(self):
    #     live_data = await live(USER)
    #     self.is_live = live_data["live"]
    #     self.live_user = live_data["user"]
    #     self.live_tittle = live_data["title"]
    #
    #
    # async def check_featured(self):
    #     self.featured_data = await featured()
