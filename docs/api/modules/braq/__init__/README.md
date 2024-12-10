###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/src/braq/__init__.py)

# Module Overview
> Module: **braq.\_\_init\_\_**

No docstring.

## Functions
- [**All functions**](/docs/api/modules/braq/__init__/funcs.md)
    - [decode](/docs/api/modules/braq/__init__/funcs.md#decode): Parse and compact a Braq text stream into a dict
    - [get\_header](/docs/api/modules/braq/__init__/funcs.md#get_header): Extract and return the header from a line string
    - [is\_header](/docs/api/modules/braq/__init__/funcs.md#is_header): Return a boolean to tell whether a string is a header line or not
    - [parse](/docs/api/modules/braq/__init__/funcs.md#parse): Iteratively parse a source of text
    - [render](/docs/api/modules/braq/__init__/funcs.md#render): Render sections, i.e., transform the sequence of sections into a Braq text document (string)

<p align="right"><a href="#braq-api-reference">Back to top</a></p>

## Classes
- [**Parser**](/docs/api/modules/braq/__init__/class-Parser.md): No docstring.
    - [end\_of\_stream](/docs/api/modules/braq/__init__/class-Parser.md#properties-table); _getter, setter_
    - [parse](/docs/api/modules/braq/__init__/class-Parser.md#parse): Iteratively parse a stream
    - [\_ensure\_line](/docs/api/modules/braq/__init__/class-Parser.md#_ensure_line): No docstring.
    - [\_is\_end\_of\_stream](/docs/api/modules/braq/__init__/class-Parser.md#_is_end_of_stream): No docstring.
    - [\_iter\_body](/docs/api/modules/braq/__init__/class-Parser.md#_iter_body): No docstring.
- [**Section**](/docs/api/modules/braq/__init__/class-Section.md): No docstring.
    - [body](/docs/api/modules/braq/__init__/class-Section.md#properties-table); _getter, setter_
    - [header](/docs/api/modules/braq/__init__/class-Section.md#properties-table); _getter, setter_
    - [render](/docs/api/modules/braq/__init__/class-Section.md#render): No docstring.

<p align="right"><a href="#braq-api-reference">Back to top</a></p>
