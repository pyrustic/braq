

class Section:
    def __init__(self, header, body=None):
        self._header = header
        self._body = _ensure_body(body)

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, val):
        self._header = val

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, val):
        self._body = _ensure_body(val)

    def __str__(self):
        return render(self)


def _ensure_body(body):
    if not body:
        return ""
    if isinstance(body, str):
        return body
    return "\n".join(body)
    

def render(*sections, spacing=1):
    """sections are either Section objects or header-body tuples
    Note that a body is either a text string or a sequence of lines"""
    r = list()
    for i, section in enumerate(sections):
        if isinstance(section, Section):
            section = section.header, section.body
        header, body = section
        if header or (header == "" and i != 0):
            r.append("[" + header + "]")
        if isinstance(body, str):
            body = body.splitlines()
        if body:
            r.extend(body)
        if i < len(sections) - 1:
            r.extend([""]*spacing)
    return "\n".join(r)
