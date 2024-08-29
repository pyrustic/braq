###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/braq/__init__/README.md) | [Source](/braq/__init__.py)

# Class FileDoc
> Module: [braq.\_\_init\_\_](/docs/api/modules/braq/__init__/README.md)
>
> Class: **FileDoc**
>
> Inheritance: [braq.document.Document](/docs/api/modules/braq/document/class-Document.md)

File-based Braq document

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| attachments\_dir | _getter, setter_ | No docstring. |
| autosave | _getter, setter_ | No docstring. |
| bin\_to\_text | _getter, setter_ | No docstring. |
| encoding\_mode | _getter, setter_ | No docstring. |
| obj\_builder | _getter, setter_ | No docstring. |
| path | _getter_ | No docstring. |
| root\_dir | _getter, setter_ | No docstring. |
| schema | _getter, setter_ | No docstring. |
| spacing | _getter, setter_ | No docstring. |
| type\_ref | _getter, setter_ | No docstring. |

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [build](#build)
- [build\_config](#build_config)
- [clear](#clear)
- [embed](#embed)
- [get](#get)
- [get\_lines](#get_lines)
- [is\_valid](#is_valid)
- [list\_headers](#list_headers)
- [load](#load)
- [load\_from](#load_from)
- [load\_schema](#load_schema)
- [remove](#remove)
- [render](#render)
- [save](#save)
- [save\_to](#save_to)
- [set](#set)
- [validate](#validate)
- [\_ensure\_sections](#_ensure_sections)

## \_\_init\_\_
Init

```python
def __init__(self, path, *, autosave=True, schema=None, type_ref=None, obj_builder=None, spacing=1, encoding_mode='c', bin_to_text=False, root_dir=None, attachments_dir='attachments'):
    ...
```

| Parameter | Description |
| --- | --- |
| path | path string or a pathlib.Path instance |
| autosave | bool to tell whether data should be saved to disk right after modification |
| schema | a Python dict that serves as schema to validate the sections of the document. It is a dictionary of dictionaries, with root keys representing a section header. |
| type\_ref | optional TypeRef object |
| obj\_builder | function that accepts a paradict.box.Obj container and returns a fresh new Python object |
| spacing | number of blank lines to place between two adjacent sections |
| encoding\_mode | either "d" or "c", to indicate if Python dicts should be encoded with the paradict.DATA_MODE or paradict.CONFIG_MODE. By default, a document's encoding mode is set to paradict.CONFI_MODE |

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## build
Decode and return the section whose header is provided

```python
def build(self, header, skip_comments=True):
    ...
```

| Parameter | Description |
| --- | --- |
| header | the string header of the section |
| skip\_comments | boolean to tell whether comments should be ignored or not |

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## build\_config
Build a configuration dictionary from the document and return it

```python
def build_config(self, *headers, skip_comments=True):
    ...
```

| Parameter | Description |
| --- | --- |
| headers | Headers of sections meant to be part of the config. Not providing headers implies that the entire document can be treated as config data |
| skip\_comments | boolean to tell whether comments should be ignored or not |

### Value to return
Returns a dictionary whose keys are headers and values are dictionaries representing the Paradict-compatible bodies of sections. The value is None when the body failed to be converted into dictionary with Paradict

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## clear
Clear the entire document

```python
def clear(self):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## embed
Embed a Python dict object into the document. Paradict will be used
to encode the body to a string

```python
def embed(self, header, body):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## get
Get the textual body of the section whose header is provided

```python
def get(self, header):
    ...
```

| Parameter | Description |
| --- | --- |
| header | the header (str) of the section |

### Value to return
Return a string or None if this section doesn't exist

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## get\_lines
Get the body lines of the section whose header is provided

```python
def get_lines(self, header):
    ...
```

| Parameter | Description |
| --- | --- |
| header | the header (str) of the section |

### Value to return
Return a list of strings or None if this section doesn't exist

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## is\_valid
Validate this entire document or only specific section(s).
Note that if the schema is missing or the schema isn't a dictionary,
a ValidationError will be raised

```python
def is_valid(self, *headers):
    ...
```

| Parameter | Description |
| --- | --- |
| \*headers | headers to validate. If you ignore this parameter, the entire document will be checked against the schema. |

### Value to return
Return true if the document is valid. Raise an exception if the schema is missing

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## list\_headers
Return the ordered list (a 'tuple' to be precise)
of section's headers (strings)

```python
def list_headers(self):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## load
load the document from the linked file

```python
def load(self):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## load\_from
Load the document from a file by providing
a path string or pathlib.Path object.
Note that this will override previous contents in the document

```python
def load_from(self, path):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## load\_schema
Load a schema file

```python
def load_schema(self, src):
    ...
```

| Parameter | Description |
| --- | --- |
| src | either a path, a pathlib.Path object, or a file like object |

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## remove
remove specific sections from both the document model and the linked file

```python
def remove(self, headers):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## render
Render the entire document or a specific set of sections, i.e.,
return a textual Paradict string that may be stored in a file.

```python
def render(self, *headers):
    ...
```

| Parameter | Description |
| --- | --- |
| \*headers | Headers of sections to render. Omitting this will render the entire document |

### Value to return
Returns a string that contains sections (each made of square-brackets delimited header
and the associated body)

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## save
Save the document in the linked file. Return a confirmation bool

```python
def save(self):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## save\_to
Save the document to a new file.
Here, path is either a path string
or a pathlib.Path object

```python
def save_to(self, path):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## set
Create or update a section by providing its header and the body

```python
def set(self, header, body=None):
    ...
```

| Parameter | Description |
| --- | --- |
| header | the header (str) of the section |
| body | the body of the section, either a string or a list of string (lines) |

### Value to return
Return the body as a string

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## validate
Validate this entire document or only specific section(s).
Might raise a ValidationError

```python
def validate(self, *headers):
    ...
```

| Parameter | Description |
| --- | --- |
| \*headers | headers to validate. If you ignore this parameter, the entire document will be checked against the schema. |

### Exceptions table
ValidationError

| Exception | Circumstance |
| --- | --- |


<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## \_ensure\_sections
No docstring

```python
def _ensure_sections(self):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>
