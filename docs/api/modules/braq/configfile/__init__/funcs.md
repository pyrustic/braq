###### Braq API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/braq/configfile/__init__/README.md) | [Source](/braq/configfile/__init__.py)

# Functions within module
> Module: [braq.configfile.\_\_init\_\_](/docs/api/modules/braq/configfile/__init__/README.md)

Here are functions exposed in the module:
- [dump\_config](#dump_config)
- [load\_config](#load_config)

## dump\_config
Dump a dict to a config file. It will override the dest path.
The data should be a dict whose keys are header strings and values are dicts

```python
def dump_config(data, path, *, type_ref=None, spacing=1, encoding_mode='c', bin_to_text=False, skip_comments=False, root_dir=None, attachments_dir='attachments'):
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
