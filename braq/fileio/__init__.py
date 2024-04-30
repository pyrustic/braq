import pathlib
import written
from braq.section import render
from braq.parser import parse_iter


__all__ = ["read_iter", "read", "write"]


def read_iter(filename, end_of_stream=None):
    """
    Iteratively read a file. This generator yields a 2-tuple made
    of a header string and an iterator to iterate over the body line by line.

    [param]
    - filename: is either a path string, a pathlib.Path instance, or a file object which
    might expose binary text encoded with UTF-8
    - end_of_stream: string to indicate the end of the stream

    [return]
    Yields a 2-tuple made of a header string and a body iterator to iterate
    over the body line by line

    [usage]
    ```python
    for header, body in Parser.parse(stream):
        print(header)  # string
        for line in body:  # iterator
            print(line)
    ```
    """
    if isinstance(filename, pathlib.Path):
        filename = str(pathlib.Path(filename).resolve())
    if isinstance(filename, str):
        with open(filename, "r", encoding="utf-8") as file:
            yield from parse_iter(file, end_of_stream=end_of_stream)
    else:
        yield from parse_iter(filename, end_of_stream=end_of_stream)


def read(filename, end_of_stream=None):
    """
    Read a file then flatten its contents (concatenate sections with same header).

    [param]
    - filename: is either a path string, a pathlib.Path instance, or a file object which
    might expose binary text encoded with UTF-8
    - end_of_stream: string to indicate the end of the stream

    [return]
    returns the dict of sections where keys are headers and
    values are section's bodies. A section body is a text string"""
    sections = dict()
    for header, body in read_iter(filename, end_of_stream=end_of_stream):
        if header not in sections:
            sections[header] = list()
        sections[header].extend(body)
    for header, body in sections.items():
        sections[header] = "\n".join(body).rstrip()
    return sections


def write(*sections, dst=None, spacing=1):
    """
    Write to a file

    [param]
    - *sections: sections objects or header-body 2-tuples
    - dst: is either a path string, a pathlib.Path instance
    - spacing: number of lines between two sections, defaults to 1
    """
    r = render(*sections, spacing=spacing)
    written.write(r, dst)
