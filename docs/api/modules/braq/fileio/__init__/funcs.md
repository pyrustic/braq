###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/braq/fileio/__init__/README.md) | [Source](/braq/fileio/__init__.py)

# Functions within module
> Module: [braq.fileio.\_\_init\_\_](/docs/api/modules/braq/fileio/__init__/README.md)

Here are functions exposed in the module:
- [read](#read)
- [read\_iter](#read_iter)
- [write](#write)

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
