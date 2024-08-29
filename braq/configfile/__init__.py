"""load_config and dump_config for Braq documents only containing config"""
import paradict
from paradict import CONFIG_MODE
from braq.filedoc import FileDoc
from braq.fileio import write


# TODO: test this and improve the docstring
def load_config(path, *, type_ref=None,
                obj_builder=None, skip_comments=True,
                root_dir=None, attachments_dir="attachments"):
    """Load a config file as a dict whose keys are headers and values are dicts"""
    file_doc = FileDoc(path, type_ref=type_ref,
                       obj_builder=obj_builder, root_dir=root_dir,
                       attachments_dir=attachments_dir)
    return file_doc.build_config(skip_comments=skip_comments)


# TODO test this and improve the docstring
def dump_config(data, path, *, type_ref=None,
                spacing=1, encoding_mode=CONFIG_MODE,
                bin_to_text=False, skip_comments=False, root_dir=None,
                attachments_dir="attachments"):
    """Dump a dict to a config file. It will override the dest path.
    The data should be a dict whose keys are header strings and values are dicts"""
    sections = list()
    for header, body in data:
        body = paradict.encode(body, mode=encoding_mode, type_ref=type_ref,
                               skip_comments=skip_comments, bin_to_text=bin_to_text,
                               root_dir=root_dir, attachments_dir=attachments_dir)
        sections.append((header, body))
    write(sections, dst=path, spacing=spacing)
