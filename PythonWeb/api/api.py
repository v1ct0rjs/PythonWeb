import PythonWeb.constants as constants
from .TwitchAPI import TwitchAPI

TwitchAPI = TwitchAPI()
async def repo() -> str:
    return constants.URL_GITHUB

async def live(user: str) -> bool:
    return TwitchAPI.live(user)