import pathlib
import written
from braq.section import render
from braq.parser import iter_parse


def iter_read(src, end_of_stream=None):
    """
    Iteratively read a file. This generator yields a 2-tuple made
    of a header string and an iterator to iterate over the body line by line.

    [parameters]
    - src: is either a path string, a pathlib.Path instance, or a file object which
    might expose binary text encoded with UTF-8
    - end_of_stream: a character or string to indicate the end of the stream

    [return]
    Yields a 2-tuple made of a header string and a body iterator to iterate
    over the body line by line
    """
    if isinstance(src, pathlib.Path):
        src = str(pathlib.Path(src).resolve())
    if isinstance(src, str):
        with open(src, "r", encoding="utf-8") as file:
            yield from iter_parse(file, end_of_stream=end_of_stream)
    else:
        yield from iter_parse(src, end_of_stream=end_of_stream)


def read(src, end_of_stream=None):
    """
    Read a file then flatten its contents (concatenate sections with same header).

    [parameters]
    - src: is either a path string, a pathlib.Path instance, or a file object which
    might expose binary text encoded with UTF-8
    - end_of_stream: a character or string to indicate the end of the stream

    [return]
    returns the dict of sections where keys are headers and
    values are section's bodies. A section body is a text string"""
    sections = dict()
    for header, body in iter_read(src, end_of_stream=end_of_stream):
        if header not in sections:
            sections[header] = list()
        sections[header].extend(body)
    for header, body in sections.items():
        sections[header] = "\n".join(body).rstrip()
    return sections


def write(*sections, dest=None, spacing=1):
    """
    Write to a file

    [parameters]
    - *sections: sections objects or header-body 2-tuples
    - dest: is either a path string, a pathlib.Path instance
    - spacing: number of lines between two sections, defaults to 1
    """
    r = render(*sections, spacing=spacing)
    written.write(r, dest)
