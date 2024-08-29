###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/braq/__init__.py)

# Module Overview
> Module: **braq.\_\_init\_\_**

No docstring.

## Fields
- [**All fields**](/docs/api/modules/braq/__init__/fields.md)
    - CONFIG\_MODE = `'c'`
    - DATA\_MODE = `'d'`

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## Functions
- [**All functions**](/docs/api/modules/braq/__init__/funcs.md)
    - [check\_header](/docs/api/modules/braq/__init__/funcs.md#check_header): Return a boolean to tell whether a string is a header line or not
    - [dump\_config](/docs/api/modules/braq/__init__/funcs.md#dump_config): Dump a dict to a config file. It will override the dest path. The data should be a dict whose keys are header strings and values...
    - [get\_header](/docs/api/modules/braq/__init__/funcs.md#get_header): Extract and return the header from a line string
    - [load\_config](/docs/api/modules/braq/__init__/funcs.md#load_config): Load a config file as a dict whose keys are headers and values are dicts
    - [parse](/docs/api/modules/braq/__init__/funcs.md#parse): Parse and flatten a Braq text stream
    - [parse\_iter](/docs/api/modules/braq/__init__/funcs.md#parse_iter): Iteratively parse a stream
    - [read](/docs/api/modules/braq/__init__/funcs.md#read): Read a file then flatten its contents (concatenate sections with same header).
    - [read\_iter](/docs/api/modules/braq/__init__/funcs.md#read_iter): Iteratively read a file. This generator yields a 2-tuple made of a header string and an iterator to iterate over the body line b...
    - [render](/docs/api/modules/braq/__init__/funcs.md#render): Render sections, i.e., transform the sequence of sections into a Braq text document (string)
    - [write](/docs/api/modules/braq/__init__/funcs.md#write): Write to a file

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## Classes
- [**Document**](/docs/api/modules/braq/__init__/class-Document.md): This class represents an editable model of a Braq document
    - [attachments\_dir](/docs/api/modules/braq/__init__/class-Document.md#properties-table); _getter, setter_
    - [bin\_to\_text](/docs/api/modules/braq/__init__/class-Document.md#properties-table); _getter, setter_
    - [encoding\_mode](/docs/api/modules/braq/__init__/class-Document.md#properties-table); _getter, setter_
    - [obj\_builder](/docs/api/modules/braq/__init__/class-Document.md#properties-table); _getter, setter_
    - [root\_dir](/docs/api/modules/braq/__init__/class-Document.md#properties-table); _getter, setter_
    - [schema](/docs/api/modules/braq/__init__/class-Document.md#properties-table); _getter, setter_
    - [spacing](/docs/api/modules/braq/__init__/class-Document.md#properties-table); _getter, setter_
    - [type\_ref](/docs/api/modules/braq/__init__/class-Document.md#properties-table); _getter, setter_
    - [build](/docs/api/modules/braq/__init__/class-Document.md#build): Decode and return the section whose header is provided
    - [build\_config](/docs/api/modules/braq/__init__/class-Document.md#build_config): Build a configuration dictionary from the document and return it
    - [clear](/docs/api/modules/braq/__init__/class-Document.md#clear): Clear the entire document
    - [embed](/docs/api/modules/braq/__init__/class-Document.md#embed): Embed a Python dict object into the document. Paradict will be used to encode the body to a string
    - [get](/docs/api/modules/braq/__init__/class-Document.md#get): Get the textual body of the section whose header is provided
    - [get\_lines](/docs/api/modules/braq/__init__/class-Document.md#get_lines): Get the body lines of the section whose header is provided
    - [is\_valid](/docs/api/modules/braq/__init__/class-Document.md#is_valid): Validate this entire document or only specific section(s). Note that if the schema is missing or the schema isn't a dictionary, ...
    - [list\_headers](/docs/api/modules/braq/__init__/class-Document.md#list_headers): Return the ordered list (a 'tuple' to be precise) of section's headers (strings)
    - [load\_from](/docs/api/modules/braq/__init__/class-Document.md#load_from): Load the document from a file by providing a path string or pathlib.Path object. Note that this will override previous contents ...
    - [load\_schema](/docs/api/modules/braq/__init__/class-Document.md#load_schema): Load a schema file
    - [remove](/docs/api/modules/braq/__init__/class-Document.md#remove): Remove specific section(s) from this document
    - [render](/docs/api/modules/braq/__init__/class-Document.md#render): Render the entire document or a specific set of sections, i.e., return a textual Paradict string that may be stored in a file.
    - [save\_to](/docs/api/modules/braq/__init__/class-Document.md#save_to): Save the contents of this document to a specific file
    - [set](/docs/api/modules/braq/__init__/class-Document.md#set): Create or update a section by providing its header and the body
    - [validate](/docs/api/modules/braq/__init__/class-Document.md#validate): Validate this entire document or only specific section(s). Might raise a ValidationError
- [**FileDoc**](/docs/api/modules/braq/__init__/class-FileDoc.md): File-based Braq document
    - [attachments\_dir](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [autosave](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [bin\_to\_text](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [encoding\_mode](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [obj\_builder](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [path](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter_
    - [root\_dir](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [schema](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [spacing](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [type\_ref](/docs/api/modules/braq/__init__/class-FileDoc.md#properties-table); _getter, setter_
    - [build](/docs/api/modules/braq/__init__/class-FileDoc.md#build): Decode and return the section whose header is provided
    - [build\_config](/docs/api/modules/braq/__init__/class-FileDoc.md#build_config): Build a configuration dictionary from the document and return it
    - [clear](/docs/api/modules/braq/__init__/class-FileDoc.md#clear): Clear the entire document
    - [embed](/docs/api/modules/braq/__init__/class-FileDoc.md#embed): Embed a Python dict object into the document. Paradict will be used to encode the body to a string
    - [get](/docs/api/modules/braq/__init__/class-FileDoc.md#get): Get the textual body of the section whose header is provided
    - [get\_lines](/docs/api/modules/braq/__init__/class-FileDoc.md#get_lines): Get the body lines of the section whose header is provided
    - [is\_valid](/docs/api/modules/braq/__init__/class-FileDoc.md#is_valid): Validate this entire document or only specific section(s). Note that if the schema is missing or the schema isn't a dictionary, ...
    - [list\_headers](/docs/api/modules/braq/__init__/class-FileDoc.md#list_headers): Return the ordered list (a 'tuple' to be precise) of section's headers (strings)
    - [load](/docs/api/modules/braq/__init__/class-FileDoc.md#load): load the document from the linked file
    - [load\_from](/docs/api/modules/braq/__init__/class-FileDoc.md#load_from): Load the document from a file by providing a path string or pathlib.Path object. Note that this will override previous contents ...
    - [load\_schema](/docs/api/modules/braq/__init__/class-FileDoc.md#load_schema): Load a schema file
    - [remove](/docs/api/modules/braq/__init__/class-FileDoc.md#remove): remove specific sections from both the document model and the linked file
    - [render](/docs/api/modules/braq/__init__/class-FileDoc.md#render): Render the entire document or a specific set of sections, i.e., return a textual Paradict string that may be stored in a file.
    - [save](/docs/api/modules/braq/__init__/class-FileDoc.md#save): Save the document in the linked file. Return a confirmation bool
    - [save\_to](/docs/api/modules/braq/__init__/class-FileDoc.md#save_to): Save the document to a new file. Here, path is either a path string or a pathlib.Path object
    - [set](/docs/api/modules/braq/__init__/class-FileDoc.md#set): Create or update a section by providing its header and the body
    - [validate](/docs/api/modules/braq/__init__/class-FileDoc.md#validate): Validate this entire document or only specific section(s). Might raise a ValidationError
    - [\_ensure\_sections](/docs/api/modules/braq/__init__/class-FileDoc.md#_ensure_sections): No docstring.
- [**Parser**](/docs/api/modules/braq/__init__/class-Parser.md): No docstring.
    - [end\_of\_stream](/docs/api/modules/braq/__init__/class-Parser.md#properties-table); _getter, setter_
    - [parse](/docs/api/modules/braq/__init__/class-Parser.md#parse): Iteratively parse a stream
    - [\_ensure\_line](/docs/api/modules/braq/__init__/class-Parser.md#_ensure_line): No docstring.
    - [\_ensure\_stream](/docs/api/modules/braq/__init__/class-Parser.md#_ensure_stream): No docstring.
    - [\_is\_end\_of\_stream](/docs/api/modules/braq/__init__/class-Parser.md#_is_end_of_stream): No docstring.
    - [\_iter\_body](/docs/api/modules/braq/__init__/class-Parser.md#_iter_body): No docstring.
- [**Section**](/docs/api/modules/braq/__init__/class-Section.md): No docstring.
    - [body](/docs/api/modules/braq/__init__/class-Section.md#properties-table); _getter, setter_
    - [header](/docs/api/modules/braq/__init__/class-Section.md#properties-table); _getter, setter_
- [**TypeRef**](/docs/api/modules/braq/__init__/class-TypeRef.md): This class represents a mechanism for customizing Python types allowed for (de)serializing data with Paradict classes and functi...
    - [adapters](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bin\_int\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bin\_int\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bin\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bin\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bool\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bool\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [comment\_id\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [comment\_id\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [comment\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [comment\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [complex\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [complex\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [date\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [date\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [datetime\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [datetime\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [dict\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [dict\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [float\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [float\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [grid\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [grid\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [hex\_int\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [hex\_int\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [int\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [int\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [list\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [list\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [obj\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [obj\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [oct\_int\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [oct\_int\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [set\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [set\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [str\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [str\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [time\_type](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [time\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [adapt](/docs/api/modules/braq/__init__/class-TypeRef.md#adapt): Checks the 'adapters' attribute to find out if there is an adapter function registered for the type of the data argument. Then, ...
    - [check](/docs/api/modules/braq/__init__/class-TypeRef.md#check): This function accepts as argument a Python type, and return its Paradict string type if it exists, else returns None
    - [\_create\_map](/docs/api/modules/braq/__init__/class-TypeRef.md#_create_map): No docstring.
    - [\_update\_types](/docs/api/modules/braq/__init__/class-TypeRef.md#_update_types): No docstring.

<p align="right"><a href="#braq-api-reference">Back to top</a></p>
