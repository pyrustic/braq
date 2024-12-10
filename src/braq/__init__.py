from collections import UserDict, OrderedDict


__all__ = ["parse", "decode", "render",
           "is_header", "get_header",
           "Section", "Parser"]


def parse(s, end_of_stream=None):
    """
    Iteratively parse a source of text

    [param]
    - s: either a text string, or a text file-like object
    - end_of_stream: string representing the end of stream

    [return]
    Yield header and body for each section until end of stream.
    The header is a string and the body is an iterator that yield each line (string)
    of the body.

    [usage]
    ```python
    for header, body in parse(stream):
        print(header)  # string
        for line in body:  # iterator
            print(line)
    ```
    """
    parser = Parser(end_of_stream=end_of_stream)
    yield from parser.parse(s)


def decode(s, end_of_stream=None):
    """
    Parse and compact a Braq text stream into a dict

    [param]
    - s: either a text string, or a text file-like object
    - end_of_stream: string representing the end of stream

    [return]
    Returns the dict of sections where keys are headers and
    values are bodies. A section body is a list of lines)
    """
    sections = dict()
    for header, body in parse(s, end_of_stream=end_of_stream):
        if header not in sections:
            sections[header] = list()
        sections[header].extend(rstrip(tuple(body)))
    for header, body in sections.items():
        sections[header] = rstrip(body)
    return sections


def render(sections, spacing=1):
    """
    Render sections, i.e., transform the sequence of sections
    into a Braq text document (string)

    [param]
    - sections: List of Section objects, or list of header-body tuples,
        or a braq dictionary (keys are strings representing headers,
        and values represent bodies).
        Note that a body is either a text string or a sequence of lines
    - spacing: number of empty lines between two sections, defaults to 1

    [return]
    A string representing a Braq text document
    """
    r = list()
    if isinstance(sections, (dict, OrderedDict, UserDict)):
        sections = sections.items()
    for i, section in enumerate(sections):
        if not isinstance(section, Section):
            header, body = section
            section = Section(header, body)
        r.append(section.render(i))
        if i < len(sections) - 1:
            r.append("\n" * (spacing + 1))
            # r.extend([""]*spacing)
    return "".join(r)


class Section:

    def __init__(self, header, body=None):
        """
        Init

        [param]
        - header: the header (str) of the section
        - body: the body of the section, either a string or a list of string (lines)
        """
        self._header = header
        self._body = ensure_body(body)

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
        """Set the body (string or a list of strings representing lines)"""
        self._body = ensure_body(val)

    def __str__(self):
        """A section object can be rendered"""
        return self.render(0)

    def __iter__(self):
        """A section object can be expanded into two items, the header, and the string body"""
        yield self._header
        yield self._body

    def render(self, index=0):
        lines = list()
        if self._header or (self._header == "" and index != 0):
            header_line = "[" + self._header + "]"
            lines.append(header_line)
        lines.extend(self._body)
        return "\n".join(lines)


class Parser:

    def __init__(self, end_of_stream=None):
        """end_of_stream represents a non-empty string that will be
        used to indicate the end of the stream"""
        self._end_of_stream = end_of_stream
        self._cached_header = None
        self._opening_line = None
        self._active = False

    @property
    def end_of_stream(self):
        return self._end_of_stream

    @end_of_stream.setter
    def end_of_stream(self, val):
        self._end_of_stream = val

    def parse(self, stream):
        """
        Iteratively parse a stream

        [param]
        - stream: iterator, sequence of lines, text string or UTF-8 encoded binary

        [return]
        Yield header and body for each section until end of stream.
        The header is a string and the body is an iterator that yield each line (string)
        of the body.

        [usage]
        ```python
        for header, body in Parser().parse(stream):
            print(header)  # string
            for line in body:  # iterator
                print(line)
        ```
        """
        self._active = True
        stream = ensure_stream(stream)
        for line in stream:
            line = self._ensure_line(line)
            if not self._active or self._is_end_of_stream(line):  # end of stream
                return
            header = get_header(line)
            if header is None:
                self._opening_line = line
                header = ""
            body = self._iter_body(stream)
            yield header, body
            exhaust_iterator(body)
            while self._cached_header is not None:
                cached_header = self._cached_header
                self._cached_header = None
                body = self._iter_body(stream)
                yield cached_header, body
                exhaust_iterator(body)

    def _is_end_of_stream(self, line):
        if not self._end_of_stream:
            return False
        if line.rstrip() == self._end_of_stream:
            return True
        return False

    def _iter_body(self, stream):
        if self._opening_line is not None:
            yield self._opening_line
            self._opening_line = None
        for line in stream:
            line = self._ensure_line(line)
            if self._is_end_of_stream(line):  # end of stream
                self._active = False
                return
            header = get_header(line)
            if header is None:
                yield line
            else:
                self._cached_header = header
                return

    def _ensure_line(self, line):
        if not isinstance(line, str):
            line = line.decode("utf-8")
        return line.rstrip("\n")


def is_header(line):
    """Return a boolean to tell whether a string is a header line or not"""
    if not line.startswith("["):
        return False
    if line.rstrip().endswith("]"):
        return True
    return False


def get_header(line):
    """Extract and return the header from a line string"""
    if not line.startswith("["):
        return
    line = line.rstrip()
    if line.endswith("]"):
        return line[1:-1]


def ensure_stream(s):
    if isinstance(s, str):
        return iter(s.splitlines(keepends=False))
    return iterate_file(s)


def ensure_body(body):
    """Ensure that a body is a tuple of lines"""
    if not body:
        return list()
    if isinstance(body, str):
        body = body.splitlines(keepends=False)
    return rstrip(body)


def iterate_file(file):
    while True:
        line = file.readline()
        if not line:
            break
        yield line


def rstrip(lines):
    i = 0
    for line in reversed(lines):
        if line != "" and not line.isspace():
            break
        i += 1
    return lines[0:len(lines)-i]


def exhaust_iterator(iterator):
    """Exhaust an iterator by iterating over it"""
    for _ in iterator:
        pass
