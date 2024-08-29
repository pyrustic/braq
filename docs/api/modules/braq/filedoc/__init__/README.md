###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/braq/filedoc/__init__.py)

# Module Overview
> Module: **braq.filedoc.\_\_init\_\_**

FileDoc class for creating model for textual Paradict data file

## Classes
- [**FileDoc**](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md): File-based Braq document
    - [attachments\_dir](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [autosave](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [bin\_to\_text](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [encoding\_mode](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [obj\_builder](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [path](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter_
    - [root\_dir](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [schema](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [spacing](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [type\_ref](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [build](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#build): Decode and return the section whose header is provided
    - [build\_config](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#build_config): Build a configuration dictionary from the document and return it
    - [clear](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#clear): Clear the entire document
    - [embed](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#embed): Embed a Python dict object into the document. Paradict will be used to encode the body to a string
    - [get](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#get): Get the textual body of the section whose header is provided
    - [get\_lines](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#get_lines): Get the body lines of the section whose header is provided
    - [is\_valid](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#is_valid): Validate this entire document or only specific section(s). Note that if the schema is missing or the schema isn't a dictionary, ...
    - [list\_headers](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#list_headers): Return the ordered list (a 'tuple' to be precise) of section's headers (strings)
    - [load](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#load): load the document from the linked file
    - [load\_from](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#load_from): Load the document from a file by providing a path string or pathlib.Path object. Note that this will override previous contents ...
    - [load\_schema](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#load_schema): Load a schema file
    - [remove](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#remove): remove specific sections from both the document model and the linked file
    - [render](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#render): Render the entire document or a specific set of sections, i.e., return a textual Paradict string that may be stored in a file.
    - [save](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#save): Save the document in the linked file. Return a confirmation bool
    - [save\_to](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#save_to): Save the document to a new file. Here, path is either a path string or a pathlib.Path object
    - [set](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#set): Create or update a section by providing its header and the body
    - [validate](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#validate): Validate this entire document or only specific section(s). Might raise a ValidationError
    - [\_ensure\_sections](/docs/api/modules/braq/filedoc/__init__/class-FileDoc.md#_ensure_sections): No docstring.

<p align="right"><a href="#braq-api-reference">Back to top</a></p>
