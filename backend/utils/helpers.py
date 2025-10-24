from datetime import datetime
from uuid import uuid4

def generate_id() -> str:
    """Generate a unique ID."""
    return str(uuid4())

def get_timestamp() -> str:
    """Get current timestamp in ISO format."""
    return datetime.utcnow().isoformat()