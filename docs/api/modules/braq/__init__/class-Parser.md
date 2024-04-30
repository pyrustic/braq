###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/braq/__init__/README.md) | [Source](/braq/__init__.py)

# Class Parser
> Module: [braq.\_\_init\_\_](/docs/api/modules/braq/__init__/README.md)
>
> Class: **Parser**
>
> Inheritance: `object`

No class docstring.

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| end\_of\_stream | _getter, setter_ | No docstring. |

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [parse](#parse)
- [\_ensure\_line](#_ensure_line)
- [\_ensure\_stream](#_ensure_stream)
- [\_is\_end\_of\_stream](#_is_end_of_stream)
- [\_iter\_body](#_iter_body)

## \_\_init\_\_
end_of_stream represents a non-empty string that will be
used to indicate the end of the stream

```python
def __init__(self, end_of_stream=None):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## parse
Iteratively parse a stream

```python
def parse(self, stream):
    ...
```

| Parameter | Description |
| --- | --- |
| stream | iterator, sequence of lines, text string or UTF-8 encoded binary |

### Value to return
Yield header and body for each section until end of stream.
The header is a string and the body is an iterator that yield each line (string)
of the body.

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## \_ensure\_line
No docstring

```python
def _ensure_line(self, line):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## \_ensure\_stream
No docstring

```python
def _ensure_stream(self, stream):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## \_is\_end\_of\_stream
No docstring

```python
def _is_end_of_stream(self, line):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## \_iter\_body
No docstring

```python
def _iter_body(self, stream):
    ...
```

<p align="right"><a href="#braq-api-reference">Back to top</a></p>
