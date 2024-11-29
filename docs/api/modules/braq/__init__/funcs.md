###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/braq/__init__/README.md) | [Source](/src/braq/__init__.py)

# Functions within module
> Module: [braq.\_\_init\_\_](/docs/api/modules/braq/__init__/README.md)

Here are functions exposed in the module:
- [get\_header](#get_header)
- [is\_header](#is_header)
- [parse](#parse)
- [parse\_compact](#parse_compact)
- [render](#render)

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
Iteratively parse a string

```python
def parse(s, end_of_stream=None):
    ...
```

| Parameter | Description |
| --- | --- |
| s | either a text string, or a file-like object that supports .read() |
| end\_of\_stream | string representing the end of stream |

### Value to return
Yield header and body for each section until end of stream.
The header is a string and the body is an iterator that yield each line (string)
of the body.

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## parse\_compact
Parse and compact a Braq text stream

```python
def parse_compact(s, end_of_stream=None):
    ...
```

| Parameter | Description |
| --- | --- |
| stream | either a text string, UTF-8 binary, a sequence of or an iterator of lines |
| end\_of\_stream | string representing the end of stream |

### Value to return
Returns the dict of sections (keys are headers and
values are section's bodies. A section body is a text string)

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
