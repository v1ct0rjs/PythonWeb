import reflex as rx
from PythonWeb.api.api import live, featured
from PythonWeb.model.Live import Live

USER = "v1ct0rdev"

class PageState(rx.State):
    live: Live = Live(is_live=False, live_tittle='', live_user='')
    featured_data: list = []

    async def check_live(self):
        self.live = await live(USER)



    async def check_featured(self):
        self.featured_data = await featured()
