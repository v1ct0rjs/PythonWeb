import PythonWeb.constants as constants
from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI


TwitchAPI = TwitchAPI()
SUPABASE_API = SupabaseAPI()
async def repo() -> str:
    return constants.URL_GITHUB

async def live(user: str) -> dict:

    return TwitchAPI.live(user)

async def featured() -> list:
    return SUPABASE_API.featured()