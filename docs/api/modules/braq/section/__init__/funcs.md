###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/braq/section/__init__/README.md) | [Source](/braq/section/__init__.py)

# Functions within module
> Module: [braq.section.\_\_init\_\_](/docs/api/modules/braq/section/__init__/README.md)

Here are functions exposed in the module:
- [render](#render)

## render
Render sections, i.e., transform the sequence of sections
into a Braq text document (string)

```python
def render(*sections, spacing=1):
    ...
```

| Parameter | Description |
| --- | --- |
| sections | Section objects or header-body tuples. Note that a body is either a text string or a sequence of lines |
| spacing | number of empty lines between two sections, defaults to 1 |

### Value to return
A string representing a Braq text document

<p align="right"><a href="#braq-api-reference">Back to top</a></p>
