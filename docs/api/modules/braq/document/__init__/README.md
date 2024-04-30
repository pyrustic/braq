###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/braq/document/__init__.py)

# Module Overview
> Module: **braq.document.\_\_init\_\_**

Braq Document class

## Classes
- [**Document**](/docs/api/modules/braq/document/__init__/class-Document.md): This class represents an editable model of a Braq document
    - [encoding\_mode](/docs/api/modules/braq/document/__init__/class-Document.md#properties-table); _getter, setter_
    - [obj\_builder](/docs/api/modules/braq/document/__init__/class-Document.md#properties-table); _getter, setter_
    - [schema](/docs/api/modules/braq/document/__init__/class-Document.md#properties-table); _getter, setter_
    - [spacing](/docs/api/modules/braq/document/__init__/class-Document.md#properties-table); _getter, setter_
    - [type\_ref](/docs/api/modules/braq/document/__init__/class-Document.md#properties-table); _getter, setter_
    - [build](/docs/api/modules/braq/document/__init__/class-Document.md#build): Decode and return the section whose header is provided
    - [build\_config](/docs/api/modules/braq/document/__init__/class-Document.md#build_config): Build a configuration dictionary from the document and return it
    - [clear](/docs/api/modules/braq/document/__init__/class-Document.md#clear): Clear the entire document
    - [embed](/docs/api/modules/braq/document/__init__/class-Document.md#embed): Embed a Python dict object into the document. Paradict will be used to encode the body to a string
    - [get](/docs/api/modules/braq/document/__init__/class-Document.md#get): Get the textual body of the section whose header is provided
    - [get\_lines](/docs/api/modules/braq/document/__init__/class-Document.md#get_lines): Get the body lines of the section whose header is provided
    - [list\_headers](/docs/api/modules/braq/document/__init__/class-Document.md#list_headers): Return the ordered list (a 'tuple' to be precise) of section's headers (strings)
    - [load\_from](/docs/api/modules/braq/document/__init__/class-Document.md#load_from): Load the document from a file by providing a path string or pathlib.Path object
    - [load\_schema](/docs/api/modules/braq/document/__init__/class-Document.md#load_schema): Load a schema file
    - [remove](/docs/api/modules/braq/document/__init__/class-Document.md#remove): Remove specific section(s) from this document
    - [render](/docs/api/modules/braq/document/__init__/class-Document.md#render): Render the entire document or a specific set of sections, i.e., return a textual Paradict string that may be stored in a file.
    - [save\_to](/docs/api/modules/braq/document/__init__/class-Document.md#save_to): Save the contents of this document to a specific file
    - [set](/docs/api/modules/braq/document/__init__/class-Document.md#set): Create or update a section by providing its header and the body
    - [validate](/docs/api/modules/braq/document/__init__/class-Document.md#validate): Validate this entire document or only specific section(s)

<p align="right"><a href="#braq-api-reference">Back to top</a></p>
