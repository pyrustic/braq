import pathlib
import written
from braq.section import render
from braq.parser import iter_parse


def iter_read(src, end_of_stream=None):
    """src is either a path string, a pathlib.Path instance, or a file object.
    Note that the file object might expose binary text encoded with UTF-8"""
    if isinstance(src, pathlib.Path):
        src = str(pathlib.Path(src).resolve())
    if isinstance(src, str):
        with open(src, "r", encoding="utf-8") as file:
            yield from iter_parse(file, end_of_stream=end_of_stream)
    else:
        yield from iter_parse(src, end_of_stream=end_of_stream)


def read(src, end_of_stream=None):
    """read and flatten.
    returns the dict of sections (keys are headers and
    values are section's bodies. a section body is a text string"""
    sections = dict()
    for header, body in iter_read(src, end_of_stream=end_of_stream):
        if header not in sections:
            sections[header] = list()
        sections[header].extend(body)
    for header, body in sections.items():
        sections[header] = "\n".join(body).rstrip()
    return sections


def write(*sections, dest=None, spacing=1):
    r = render(*sections, spacing=spacing)
    written.write(r, dest)
    #with open(dest, "w", encoding="utf-8") as file:
    #    file.write(r)
