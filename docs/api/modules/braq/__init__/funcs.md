###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/braq/__init__/README.md) | [Source](/braq/__init__.py)

# Functions within module
> Module: [braq.\_\_init\_\_](/docs/api/modules/braq/__init__/README.md)

Here are functions exposed in the module:
- [check\_header](#check_header)
- [dump\_config](#dump_config)
- [get\_header](#get_header)
- [load\_config](#load_config)
- [parse](#parse)
- [parse\_iter](#parse_iter)
- [read](#read)
- [read\_iter](#read_iter)
- [render](#render)
- [write](#write)

## check\_header
Return a boolean to tell whether a string is a header line or not

```python
def check_header(line):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## dump\_config
Dump a dict to a config file. It will override the dest path.
The data should be a dict whose keys are header strings and values are dicts

```python
def dump_config(data, path, *, type_ref=None, spacing=1, encoding_mode='c', bin_to_text=False, skip_comments=False, root_dir=None, attachments_dir='attachments'):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## get\_header
Extract and return the header from a line string

```python
def get_header(line):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## load\_config
Load a config file as a dict whose keys are headers and values are dicts

```python
def load_config(path, *, type_ref=None, obj_builder=None, skip_comments=True, root_dir=None, attachments_dir='attachments'):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## parse
Parse and flatten a Braq text stream

```python
def parse(stream, end_of_stream=None):
    ...
```

| Parameter | Description |
| --- | --- |
| stream | either a text string, UTF-8 binary, a sequence of or an iterator of lines |
| end\_of\_stream | string representing the end of stream |

### Value to return
Returns the dict of sections (keys are headers and
values are section's bodies. a section body is a text string

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## parse\_iter
Iteratively parse a stream

```python
def parse_iter(stream, end_of_stream=None):
    ...
```

| Parameter | Description |
| --- | --- |
| stream | either a text string, UTF-8 binary, a sequence of or an iterator of lines |
| end\_of\_stream | string representing the end of stream |

### Value to return
Yield header and body for each section until end of stream.
The header is a string and the body is an iterator that yield each line (string)
of the body.

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## read
Read a file then flatten its contents (concatenate sections with same header).

```python
def read(filename, end_of_stream=None):
    ...
```

| Parameter | Description |
| --- | --- |
| filename | is either a path string, a pathlib.Path instance, or a file object which might expose binary text encoded with UTF-8 |
| end\_of\_stream | string to indicate the end of the stream |

### Value to return
returns the dict of sections where keys are headers and
values are section's bodies. A section body is a text string

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## read\_iter
Iteratively read a file. This generator yields a 2-tuple made
of a header string and an iterator to iterate over the body line by line.

```python
def read_iter(filename, end_of_stream=None):
    ...
```

| Parameter | Description |
| --- | --- |
| filename | is either a path string, a pathlib.Path instance, or a file object which might expose binary text encoded with UTF-8 |
| end\_of\_stream | string to indicate the end of the stream |

### Value to return
Yields a 2-tuple made of a header string and a body iterator to iterate
over the body line by line

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## render
Render sections, i.e., transform the sequence of sections
into a Braq text document (string)

```python
def render(sections, spacing=1):
    ...
```

| Parameter | Description |
| --- | --- |
| sections | Section objects or header-body tuples. Note that a body is either a text string or a sequence of lines |
| spacing | number of empty lines between two sections, defaults to 1 |

### Value to return
A string representing a Braq text document

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## write
Write to a file

```python
def write(sections, dst=None, spacing=1):
    ...
```

| Parameter | Description |
| --- | --- |
| \*sections | sections objects or header-body 2-tuples |
| dst | is either a path string, a pathlib.Path instance |
| spacing | number of lines between two sections, defaults to 1 |

<p align="right"><a href="#braq-api-reference">Back to top</a></p>
