from supabase import create_client, Client

from backend.config import settings

async def get_supabase() -> Client:
    """Get Supabase client instance."""
    return create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

# Usage example:
# client = await get_supabase()
# data = await client.table('videos').select("*").execute()