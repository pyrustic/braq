"""FileDoc class for creating model for textual Paradict data file"""
import os.path
import braq
from contextlib import contextmanager
from braq.document import Document
from paradict import CONFIG_MODE


__all__ = ["FileDoc"]


class FileDoc(Document):
    """File-based Braq document"""
    def __init__(self, path, *, autosave=True, schema=None,
                 type_ref=None, obj_builder=None,
                 lazy_loading=True, spacing=1,
                 encoding_mode=CONFIG_MODE):
        """
        Init

        [param]
        - path: path string or a pathlib.Path instance
        - autosave: bool to tell whether data should be saved to disk right after modification
        - schema: a Python dict that serves as schema to validate the sections
        of the document. It is a dictionary of dictionaries, with root keys
        representing a section header.
        - type_ref: optional TypeRef object
        - obj_builder: function that accepts a paradict.box.Obj container and
        returns a fresh new Python object
        - lazy_loading: boolean to tell whether the model should be built right at the initialization of the object or when it is needed.
        - spacing: number of blank lines to place between two adjacent sections
        - encoding_mode: either "d" or "c", to indicate if Python dicts should be
        encoded with the paradict.DATA_MODE or paradict.CONFIG_MODE. By default,
        a document's encoding mode is set to paradict.CONFI_MODE
        """
        super().__init__(schema=schema, type_ref=type_ref,
                         obj_builder=obj_builder, spacing=spacing,
                         encoding_mode=encoding_mode)
        self._sections = None
        self._path = path
        self._autosave = autosave
        self._lazy_loading = lazy_loading
        if lazy_loading:
            self.load()

    @property
    def path(self):
        return self._path

    @property
    def autosave(self):
        return self._autosave

    @autosave.setter
    def autosave(self, val):
        self._autosave = val

    @property
    def lazy_loading(self):
        return self._lazy_loading

    def get(self, header):
        self._ensure_sections()
        return super().get(header)

    def get_lines(self, header):
        self._ensure_sections()
        return super().get_lines(header)

    def set(self, header, body=None):
        self._ensure_sections()
        super().set(header, body)
        if self._autosave:
            self.save()

    def build(self, header, skip_comments=True):
        """
        Decode and return the section whose header is provided

        [param]
        - header: the string header of the section
        - skip_comments: boolean to tell whether comments should be ignored or not
        """
        self._ensure_sections()
        return super().build(header, skip_comments=skip_comments)

    def build_config(self, *headers, skip_comments=True, on_error=None):
        self._ensure_sections()
        return super().build_config(*headers, skip_comments=skip_comments,
                                    on_error=on_error)

    def embed(self, header, body):
        self._ensure_sections()
        r = super().embed(header, body)
        if self._autosave:
            self.save()
        return r

    @contextmanager
    def edit_model(self, autosave=True):
        """
        Context manager to edit the model of the document and save to disk only at the end
        of the context. Note that when the autosave argument is set to False, the model
        isn't saved at the end of the context
        """
        self._ensure_sections()
        cached_global_autosave = self._autosave
        self._autosave = False
        yield
        self._autosave = cached_global_autosave
        if autosave:
            self.save()

    def list_headers(self):
        """
        Return the ordered list (a 'tuple' to be precise)
        of section's headers (strings)
        """
        self._ensure_sections()
        return super().list_headers()

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
        self._ensure_sections()
        return super().render(*headers)

    def save_to(self, path):
        """Save the document to a new file.
        Here, path is either a path string
        or a pathlib.Path object"""
        self._ensure_sections()
        return super().save_to(path)

    def remove(self, *headers):
        """remove specific sections from both the document model and the linked file"""
        self._ensure_sections()
        super().remove(*headers)
        if self._autosave:
            self.save()

    def load(self):
        """load the document from the linked file"""
        if not os.path.isfile(self._path):
            self._sections = dict()
            return False
        self._sections = braq.read(self._path)
        return True

    def save(self):
        """Save the document in the linked file. Return a confirmation bool"""
        if self._sections is None:
            return False
        s = list()
        for header, body in self._sections.items():
            s.append((header, body))
        braq.write(*s, dst=self._path, spacing=self._spacing)
        return True

    def clear(self):
        """Clear the entire document"""
        self._ensure_sections()
        super().clear()
        if self._autosave:
            self.save()

    def _ensure_sections(self):
        if self._sections is None:
            self.load()
