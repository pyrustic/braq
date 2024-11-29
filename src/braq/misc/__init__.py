def exhaust_iterator(iterator):
    """Exhaust an iterator by iterating over it"""
    for _ in iterator:
        pass


def compact_body(body):  # apparently we won't need this... as we do body.rstrip() not .strip()
    # ensure lines
    lines = body.splitlines(keepends=False) if isinstance(body, str) else body
    # remove leading empty/space lines
    while lines and not lines[0].strip():
        lines.pop(0)
    # remove trailing empty/space lines
    while lines and not lines[-1].strip():
        lines.pop()
    return lines
