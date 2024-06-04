import os
import dotenv
from supabase import create_client, Client

class SupabaseAPI:

    dotenv.load_dotenv()
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def  featured(self) -> list:
        response = self.supabase.table('featured').select('*').execute()

        featured_data = []

        if len(response.data) > 0:
            for featured_items in response.data:
                featured_data.append(featured_items)
        #print(featured_data)
        return featured_data