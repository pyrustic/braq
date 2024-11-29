from braq import misc


__all__ = ["parse", "parse_compact", "Parser", "is_header", "get_header"]


def parse(s, end_of_stream=None):
    """
    Iteratively parse a string

    [param]
    - s: either a text string, or a file-like object that supports .read()
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


def parse_compact(s, end_of_stream=None):
    """
    Parse and compact a Braq text stream

    [param]
    - stream: either a text string, UTF-8 binary, a sequence of or an iterator of lines
    - end_of_stream: string representing the end of stream

    [return]
    Returns the dict of sections (keys are headers and
    values are section's bodies. A section body is a text string)
    """
    sections = dict()
    for header, body in parse(s, end_of_stream=end_of_stream):
        if header not in sections:
            sections[header] = list()
        sections[header].extend(body)
    for header, body in sections.items():
        sections[header] = "\n".join(body).rstrip()
    return sections


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
        stream = self._ensure_stream(stream)
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
            misc.exhaust_iterator(body)
            while self._cached_header is not None:
                cached_header = self._cached_header
                self._cached_header = None
                body = self._iter_body(stream)
                yield cached_header, body
                misc.exhaust_iterator(body)

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

    def _ensure_stream(self, stream):
        if not isinstance(stream, str):
            stream = stream.read()
        stream = stream.splitlines(keepends=False)
        return iter(stream)

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
