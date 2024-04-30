###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/braq/parser/__init__/README.md) | [Source](/braq/parser/__init__.py)

# Functions within module
> Module: [braq.parser.\_\_init\_\_](/docs/api/modules/braq/parser/__init__/README.md)

Here are functions exposed in the module:
- [check\_header](#check_header)
- [get\_header](#get_header)
- [parse](#parse)
- [parse\_iter](#parse_iter)

## check\_header
Return a boolean to tell whether a string is a header line or not

```python
def check_header(line):
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
