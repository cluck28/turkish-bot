import secrets


def create_unique_id(prefix: str) -> str:
    return f"{prefix}_{secrets.token_hex(16)}"