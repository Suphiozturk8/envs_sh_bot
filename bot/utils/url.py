
import re


def is_valid_envs_url(url: str) -> bool:
    pattern = re.compile(
        r"^https?://envs\.sh(/.+)$", re.IGNORECASE
    )
    return bool(pattern.match(url))
