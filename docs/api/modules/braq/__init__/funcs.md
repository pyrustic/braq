###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/braq/__init__/README.md) | [Source](/src/braq/__init__.py)

# Functions within module
> Module: [braq.\_\_init\_\_](/docs/api/modules/braq/__init__/README.md)

Here are functions exposed in the module:
- [decode](#decode)
- [get\_header](#get_header)
- [is\_header](#is_header)
- [parse](#parse)
- [render](#render)

## decode
Parse and compact a Braq text stream into a dict

```python
def decode(s, end_of_stream=None):
    ...
```

| Parameter | Description |
| --- | --- |
| s | either a text string, or a text file-like object |
| end\_of\_stream | string representing the end of stream |

### Value to return
Returns the dict of sections where keys are headers and
values are bodies. A section body is a list of lines)

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## get\_header
Extract and return the header from a line string

```python
def get_header(line):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## is\_header
Return a boolean to tell whether a string is a header line or not

```python
def is_header(line):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## parse
Iteratively parse a source of text

```python
def parse(s, end_of_stream=None):
    ...
```

| Parameter | Description |
| --- | --- |
| s | either a text string, or a text file-like object |
| end\_of\_stream | string representing the end of stream |

### Value to return
Yield header and body for each section until end of stream.
The header is a string and the body is an iterator that yield each line (string)
of the body.

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
| sections | List of Section objects, or list of header-body tuples, or a braq dictionary (keys are strings representing headers, and values represent bodies). Note that a body is either a text string or a sequence of lines |
| spacing | number of empty lines between two sections, defaults to 1 |

### Value to return
A string representing a Braq text document

<p align="right"><a href="#braq-api-reference">Back to top</a></p>
