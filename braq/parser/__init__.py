from braq import misc


def iter_parse(stream, end_of_stream=None):
    """
    Stream is either a text string, a sequence of or an iterator of lines
    Usage:
        for header, body in parse(stream):
            print(header)  # string
            for line in body:  # iterator
                print(line)
    Note that stream might be binary text encoded with UTF-8
    """
    parser = Parser(end_of_stream=end_of_stream)
    yield from parser.parse(stream)


def parse(stream, end_of_stream=None):
    """parse and flatten.
    returns the dict of sections (keys are headers and
    values are section's bodies. a section body is a text string"""
    sections = dict()
    for header, body in iter_parse(stream, end_of_stream=end_of_stream):
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
        Stream is an iterator, a sequence of lines, or a text string
        Usage:
            for header, body in Parser.parse(stream):
                print(header)  # string
                for line in body:  # iterator
                    print(line)
        Note that stream might be binary text encoded with UTF-8
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
        if isinstance(stream, str):
            stream = stream.splitlines(keepends=False)
        return iter(stream)

    def _ensure_line(self, line):
        if not isinstance(line, str):
            line = line.decode("utf-8")
        return line.rstrip("\n")


def check_header(line):
    if not line.startswith("["):
        return False
    if line.rstrip().endswith("]"):
        return True
    return False


def get_header(line):
    if not line.startswith("["):
        return None
    line = line.rstrip()
    if line.endswith("]"):
        return line[1:-1]
