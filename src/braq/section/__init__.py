
__all__ = ["Section", "render"]


class Section:

    def __init__(self, header, body=None):
        """
        Init

        [param]
        - header: the header (str) of the section
        - body: the body of the section, either a string or a list of string (lines)
        """
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
        """Body as string"""
        return self._body

    @body.setter
    def body(self, val):
        """Set the body (string or a list of strings representing lines)"""
        self._body = _ensure_body(val)

    def __str__(self):
        """A section object can be rendered"""
        return render((self, ))

    def __iter__(self):
        """A section object can be expanded into two items, the header, and the string body"""
        yield self._header
        yield self._body


def _ensure_body(body):
    """Convert non-string body into a string"""
    if not body:
        return ""
    if isinstance(body, str):
        return body.rstrip()
    return "\n".join(body).rstrip()
    

def render(sections, spacing=1):
    """
    Render sections, i.e., transform the sequence of sections
    into a Braq text document (string)

    [param]
    - sections: Section objects or header-body tuples.
    Note that a body is either a text string or a sequence of lines
    - spacing: number of empty lines between two sections, defaults to 1

    [return]
    A string representing a Braq text document
    """
    r = list()
    for i, section in enumerate(sections):
        if isinstance(section, Section):
            section = section.header, section.body
        header, body = section
        if header or (header == "" and i != 0):
            r.append("[" + header + "]")
        if isinstance(body, str):
            body = body.splitlines(keepends=False)
        if body:
            r.extend(body)
        if i < len(sections) - 1:
            r.extend([""]*spacing)
    return "\n".join(r)
