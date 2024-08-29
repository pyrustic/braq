"""Braq Document class"""
from paradict.typeref import TypeRef
from paradict import validator, encode, decode, CONFIG_MODE
from braq.errors import ValidationError
from braq import errors
import braq


__all__ = ["Document"]


class Document:
    """This class represents an editable model of a Braq document"""
    def __init__(self, init_text="", *, schema=None,
                 type_ref=None, obj_builder=None,
                 spacing=1, encoding_mode=CONFIG_MODE,
                 bin_to_text=True, root_dir=None,
                 attachments_dir="attachments"):
        """
        Init

        [param]
        - init_text: Braq text for initializing the model

        - schema: a Python dict that serves as schema to validate the sections
            of the document. It is a dictionary of dictionaries, with root keys
            representing a section header.

        - type_ref: optional TypeRef object

        - obj_builder: function that accepts a paradict.box.Obj container and
            returns a fresh new Python object

        - spacing: number of blank lines to place between two adjacent sections

        - encoding_mode: either "d" (paradict.DATA_MODE) or "c" (paradict.CONFIG_MODE) to
            indicate if Python dicts should be encoded in the data or config mode.
            By default, a document's encoding mode is set to paradict.CONFIG_MODE

        - bin_to_text: boolean to text whether Paradict binary values should be converted
            into base16 strings or stored as attachments

        - root_dir: root directory in which the attachments folder is expected to be

        - attachments_dir: directory in which attachments should be saved. This is a path
            that is relative to the root directory. Only slashes are allowed as separator.
        """
        self._sections = braq.parse(init_text)
        self._schema = schema
        self._type_ref = type_ref if type_ref else TypeRef()
        self._obj_builder = obj_builder
        self._spacing = spacing
        self._encoding_mode = encoding_mode
        self._bin_to_text = bin_to_text
        self._root_dir = root_dir
        self._attachments_dir = attachments_dir

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, val):
        self._schema = val

    @property
    def spacing(self):
        return self._spacing

    @spacing.setter
    def spacing(self, val):
        self._spacing = val

    @property
    def obj_builder(self):
        return self._obj_builder

    @obj_builder.setter
    def obj_builder(self, val):
        self._obj_builder = val

    @property
    def encoding_mode(self):
        return self._encoding_mode

    @encoding_mode.setter
    def encoding_mode(self, val):
        self._encoding_mode = val

    @property
    def type_ref(self):
        return self._type_ref

    @type_ref.setter
    def type_ref(self, val):
        self._type_ref = val if val else TypeRef()

    @property
    def root_dir(self):
        return self._root_dir

    @root_dir.setter
    def root_dir(self, val):
        self._root_dir = val

    @property
    def bin_to_text(self):
        return self._bin_to_text

    @bin_to_text.setter
    def bin_to_text(self, val):
        self._bin_to_text = val

    @property
    def attachments_dir(self):
        return self._attachments_dir

    @attachments_dir.setter
    def attachments_dir(self, val):
        self._attachments_dir = val

    def get(self, header):
        """
        Get the textual body of the section whose header is provided

        [param]
        - header: the header (str) of the section

        [return]
        Return a string or None if this section doesn't exist
        """
        return self._sections.get(header)

    def get_lines(self, header):
        """
        Get the body lines of the section whose header is provided

        [param]
        - header: the header (str) of the section

        [return]
        Return a list of strings or None if this section doesn't exist
        """
        body = self._sections.get(header)
        if body is None:
            return
        return body.splitlines(keepends=False)

    def set(self, header, body):
        """
        Create or update a section by providing its header and the body

        [param]
        - header: the header (str) of the section
        - body: the body of the section, either a string or a list of string (lines)

        [return]
        Return the body as a string
        """
        if not isinstance(body, str):
            body = "\n".join(body)
        self._sections[header] = body.rstrip()
        return body

    def build(self, header, skip_comments=True):
        """
        Decode and return the section whose header is provided

        [param]
        - header: the string header of the section
        - skip_comments: boolean to tell whether comments should be ignored or not

        [return]
        Return the body as a Python dictionary built with Paradict
        """
        body = self._sections.get(header)
        if body is None:
            return
        body = decode(body, obj_builder=self._obj_builder,
                      skip_comments=skip_comments, root_dir=self._root_dir,
                      type_ref=self._type_ref)
        return body

    def build_config(self, *headers, skip_comments=True):
        """Build a configuration dictionary from the document and return it

        [param]
        - headers: Headers of sections meant to be part of the config.
        Not providing headers implies that the entire document can be treated as config data
        - skip_comments: boolean to tell whether comments should be ignored or not

        [return]
        Returns a dictionary whose keys are headers and values are dictionaries representing the Paradict-compatible bodies of sections. The value is None when the body failed to be converted into dictionary with Paradict
        """
        headers = headers if headers else self.list_headers()
        config = dict()
        for header in headers:
            config[header] = self.build(header, skip_comments=skip_comments)
        return config

    def embed(self, header, body):
        """Embed a Python dict object into the document. Paradict will be used
        to encode the body to a string"""
        if type(body) not in self._type_ref.dict_types:
            msg = "Only a dictionary can be embedded"
            raise errors.Error(msg)
        body = encode(body, mode=self._encoding_mode,
                      type_ref=self._type_ref,
                      skip_comments=False,
                      root_dir=self._root_dir,
                      bin_to_text=self._bin_to_text,
                      attachments_dir=self._attachments_dir)
        self._sections[header] = body
        return body

    def list_headers(self):
        """
        Return the ordered list (a 'tuple' to be precise)
        of section's headers (strings)
        """
        return tuple(self._sections.keys())

    def render(self, *headers):
        """
        Render the entire document or a specific set of sections, i.e.,
        return a textual Paradict string that may be stored in a file.

        [param]
        - *headers: Headers of sections to render.
        Omitting this will render the entire document

        [return]
        Returns a string that contains sections (each made of square-brackets delimited header
        and the associated body)
        """
        sections = list()
        cache = set()
        headers = headers if headers else self.list_headers()
        for header in headers:
            if header in cache:
                continue
            else:
                cache.add(header)
            if header not in self._sections:
                continue
            sections.append((header, self._sections.get(header)))
        return braq.render(sections, spacing=self._spacing)

    def load_schema(self, src):
        """
        Load a schema file

        [param]
        - src: either a path, a pathlib.Path object, or a file like object
        """
        r = braq.read(src)
        self._schema = dict()
        for header, body in r.items():
            body = decode(body, type_ref=self._type_ref, obj_builder=self._obj_builder,
                          skip_comments=True, root_dir=self._root_dir)
            self._schema[header] = body

    def is_valid(self, *headers):
        """
        Validate this entire document or only specific section(s).
        Note that if the schema is missing or the schema isn't a dictionary,
        a ValidationError will be raised

        [param]
        - *headers: headers to validate. If you ignore this parameter, the entire document will
        be checked against the schema.

        [return]
        Return true if the document is valid. Raise an exception if the schema is missing
        """
        if self._schema is None:
            msg = "Missing schema"
            raise ValidationError(msg)
        if type(self._schema) not in self._type_ref.dict_types:
            msg = "The schema must be a dictionary whose keys represent the section headers"
            raise ValidationError(msg)
        headers = headers if headers else self.list_headers()
        for header in headers:
            if header not in self._schema:
                continue
            if not validator.is_valid(self.build(header, skip_comments=True),
                                      self._schema.get(header)):
                return False
        return True

    def validate(self, *headers):
        """
        Validate this entire document or only specific section(s).
        Might raise a ValidationError

        [param]
        - *headers: headers to validate. If you ignore this parameter, the entire document will
        be checked against the schema.

        [except]
        - ValidationError
        """
        if self._schema is None:
            msg = "Missing schema"
            raise ValidationError(msg)
        if type(self._schema) not in self._type_ref.dict_types:
            msg = "The schema must be a dictionary whose keys represent the section headers"
            raise ValidationError(msg)
        headers = headers if headers else self.list_headers()
        for header in headers:
            if header not in self._schema:
                continue
            validator.validate(self.build(header, skip_comments=True),
                               self._schema.get(header))

    def load_from(self, path):
        """Load the document from a file by providing
        a path string or pathlib.Path object.
        Note that this will override previous contents in the document"""
        self._sections = braq.read(path)

    def save_to(self, path):
        """
        Save the contents of this document to a specific file

        [param]
        - path: path to filename. Path may be a pathlib.Path instance
        """
        if not path:
            return False
        sections = list()
        for header, body in self._sections.items():
            sections.append((header, body))
        braq.write(sections, dst=path, spacing=self._spacing)
        return True

    def remove(self, headers):
        """
        Remove specific section(s) from this document

        [param]
        - *headers: the headers of the sections to remove
        """
        for header in headers:
            try:
                del self._sections[header]
            except KeyError as e:
                pass

    def clear(self):
        """Clear the entire document"""
        self._sections = dict()
