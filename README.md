[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI package version](https://img.shields.io/pypi/v/braq)](https://pypi.org/project/braq)
[![Downloads](https://static.pepy.tech/badge/braq)](https://pepy.tech/project/braq)

<!-- Cover -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/assets/braq/cover.png" alt="Cover image" width="650">
    <p align="center">
    Braq document with 3 sections of which the last is executable
    </p>
</div>

<!-- Intro Text -->
# Braq
<b>The most obvious way to section a document</b>

This project is part of the [Pyrustic Open Ecosystem](https://pyrustic.github.io).

## Table of contents
- [Overview](#overview)
- [Parse a document](#parse-a-document)
    - [Parse a document iteratively](#parse-a-document-iteratively)
- [Read a file](#read-a-file)
    - [Read a file iteratively](#read-a-file-iteratively)
- [Render a document](#render-a-document)
- [Write to file](#write-to-file)
- [The Section class](#the-section-class)
- [The Parser class](#the-parser-class)
- [Misc functions](#misc-functions)
- [Miscellaneous](#miscellaneous)
- [Testing and contributing](#testing-and-contributing)
- [Installation](#installation)


# Overview
**Braq** (pronounced `/ˈbɹæk/`) is a human-readable data format whose reference parser is an eponymous lightweight [Python](https://www.python.org/) library available on [PyPI](#installation).

> Along with [Paradict](https://github.com/pyrustic/paradict), Braq is a spin-off of [Jesth](https://github.com/pyrustic/jesth).


A Braq document is made up of **sections**, each defined by a **header** surrounded by square brackets (hence the name Braq) and a **body** which is just lines of text. 

Instead of interpreting the lines that make sections, the Braq parser lays low and lets the programmer decide what to do with them.

Because of this parsing policy, a single Braq document can contain an **eclectic set of sections** such as notes, JSON string, help text, server configs, [prompts](https://github.com/f/awesome-chatgpt-prompts) for a chatbot, [directed graph](https://en.wikipedia.org/wiki/Directed_graph), [ascii artwork](https://en.wikipedia.org/wiki/ASCII_art), and more.

> The doc generator used for [Pyrustic](https://pyrustic.github.io) projects consumes docstrings written in Braq.


<p align="right"><a href="#readme">Back to top</a></p>

# Parse a document
The library exposes the `parse` function which takes as input the text stream to be parsed, then returns a **dictionary** whose keys and values are strings representing headers and bodies respectively.

> Sections sharing the same header are concatenated !
> The header of an unnamed section is an empty string.

```python
import braq

text = """\
this is the unnamed section at
the top of this document...

[section 1]
this is section 1"""

d = braq.parse(text)

# check headers
assert tuple(d.keys()) == ("", "section 1")
# check the body of 'section 1'
assert d["section 1"] == "this is section 1"
```

## Parse a document iteratively
A document can be parsed line by line as following:

```python
import braq

text = """\
this is the unnamed section

[section 1]
this is section 1"""

for header, body in braq.iter_parse(text):
    if header:
        print("[" + header + "]")
    for line in body:
        print(line)
```

Output:

```text
this is the unnamed section

[section 1]
this is section 1
```


<p align="right"><a href="#readme">Back to top</a></p>

# Read a file
The library exposes the `read` function which takes as input the path to a file to parse, then returns a dictionary whose keys and values are strings representing headers and bodies respectively.

> Sections sharing the same header are concatenated !

```python
import braq

path = "/home/alex/braqfile.txt"

r = braq.read(path)
assert tuple(r.keys()) == ("", "section 1")
```

## Read a file iteratively
A large text file can be parsed line by line as following:

```python
import braq

path = "/home/alex/braqfile.txt"

for header, body in braq.iter_read(path):
    if header:
        print("[" + header + "]")
    for line in body:
        print(line)
```
Output:

```text
this is the unnamed section

[section 1]
this is section 1
```

<p align="right"><a href="#readme">Back to top</a></p>

# Render a document
Rendering a document involves transforming Python objects representing sections into Braq text which is a string that can be displayed on the screen or stored in a file.

The library exposes the `render` function which accepts as input a sequence of sections (either header-body tuples or `Section` objects) and returns a Braq document.

```python
import braq

section_1 = braq.Section("section 1", "line a\nline b")
section_2 = "section 2", "line c\nline d"
section_3 = "section 3", ("line e", "line f")

r = braq.render(section_1, section_2, section_3)

print(r)
```

Output:

```text
[section 1]
line a
line b

[section 2]
line c
line d

[section 3]
line e
line f
```

> The render function also accepts the `spacing` argument which defaults to 1 and represents the number of lines of spacing between two adjacent sections.


<p align="right"><a href="#readme">Back to top</a></p>

# Write to file
Following is a snippet for writting a Braq document to a file:

```python
import braq

# sections
section_1 = braq.Section("", "welcome")
section_2 = braq.Section("section 2")
section_3 = "section 3", ("line a", "line b")
# path to file
path = "/home/alex/braqfile.txt"
# write to file
r = braq.write(section_1, section_2, section_3, dest=path)
```
The contents of the Braq file:
```text
welcome

[section 2]

[section 3]
line a
line b
```

<p align="right"><a href="#readme">Back to top</a></p>

# The Section class
The `Section` class is an abstraction representing a Braq section. It exposes the `header` and `body` properties and renders itself when its `__str__` method is called implicitly.

```python
import braq

header, body = "my header", ("line a", "line b")
section = braq.Section(header, body)

assert section.header == "my header"
assert section.body == "line a\nline b"
assert str(section) == """\
[my header]
line a
line b"""
```


<p align="right"><a href="#readme">Back to top</a></p>

# The Parser class
The `iter_parse` function under the hood uses the `Parser` class to parse Braq documents.


```python
import braq

doc = """\
welcome

[section 1]
line a
line b"""

parser = braq.Parser()
for header, body in parser.parse(doc):
    if header:
        print("[" + header + "]")
    for line in body:
        print(line)
```

Output:

```text
welcome

[section 1]
line a
line b
```


<p align="right"><a href="#readme">Back to top</a></p>

# Misc functions
The `check_header` function accepts a line of text as input and then returns a boolean to indicate whether this line is a header or not.

```python
import braq

line_1 = "[my header]"
line_2 = "[this isn't a header] at all"
assert braq.check_header(line_1) is True
assert braq.check_header(line_2) is False
```

The `get_header` function accepts a line of text as input and returns a string if the line is a header. Otherwise, `None` is returned.

```python
import braq

line_1 = "[my header]"
line_2 = "[this isn't a header] at all"
assert braq.get_header(line_1) == "my header"
assert braq.get_header(line_2) is None
```

<p align="right"><a href="#readme">Back to top</a></p>

# Miscellaneous
Collection of miscellaneous notes.

## Cover image
The beautiful cover image is generated with [Carbon](https://carbon.now.sh/about).

<p align="right"><a href="#readme">Back to top</a></p>

# Testing and contributing
Feel free to **open an issue** to report a bug, suggest some changes, show some useful code snippets, or discuss anything related to this project. You can also directly email [me](https://pyrustic.github.io/#contact).

## Setup your development environment
Following are instructions to setup your development environment

```bash
# create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# clone the project then change into its directory
git clone https://github.com/pyrustic/braq.git
cd braq

# install the package locally (editable mode)
pip install -e .

# run tests
python -m unittest discover -f -s tests -t .

# deactivate the virtual environment
deactivate
```

<p align="right"><a href="#readme">Back to top</a></p>

# Installation
**Braq** is **cross-platform**. It is built on [Ubuntu](https://ubuntu.com/download/desktop) and should work on **Python 3.5** or **newer**.

## Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

## Install for the first time

```bash
pip install braq
```

## Upgrade the package
```bash
pip install braq --upgrade --upgrade-strategy eager
```

## Deactivate the virtual environment
```bash
deactivate
```

<p align="right"><a href="#readme">Back to top</a></p>

# About the author
Hello world, I'm Alex, a tech enthusiast ! Feel free to get in touch with [me](https://pyrustic.github.io/#contact) !

<br>
<br>
<br>

[Back to top](#readme)
