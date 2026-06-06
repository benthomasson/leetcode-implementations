"""License Key Formatting - LeetCode Solution."""


def license_key_formatting(s: str, k: int) -> str:
    """Reformat a license key so every group has exactly k chars (except possibly the first).

    Args:
        s: License key string with alphanumeric chars and dashes.
        k: Required group size.

    Returns:
        Reformatted license key with uppercase letters and groups of size k.
    """
    cleaned = s.replace("-", "").upper()
    first = len(cleaned) % k
    parts = []
    if first:
        parts.append(cleaned[:first])
    for i in range(first, len(cleaned), k):
        parts.append(cleaned[i:i + k])
    return "-".join(parts)
