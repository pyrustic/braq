Back to [All Modules](https://github.com/pyrustic/braq/blob/master/docs/modules/README.md#readme)

# Module Overview

**braq**
 
No description

> **Classes:** &nbsp; [Parser](https://github.com/pyrustic/braq/blob/master/docs/modules/content/braq/content/classes/Parser.md#class-parser) &nbsp;&nbsp; [Section](https://github.com/pyrustic/braq/blob/master/docs/modules/content/braq/content/classes/Section.md#class-section)
>
> **Functions:** &nbsp; [check\_header](#check_header) &nbsp;&nbsp; [get\_header](#get_header) &nbsp;&nbsp; [iter\_parse](#iter_parse) &nbsp;&nbsp; [iter\_read](#iter_read) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [write](#write)
>
> **Constants:** &nbsp; None

# All Functions
[check\_header](#check_header) &nbsp;&nbsp; [get\_header](#get_header) &nbsp;&nbsp; [iter\_parse](#iter_parse) &nbsp;&nbsp; [iter\_read](#iter_read) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [write](#write)

## check\_header
No description



**Signature:** (line)





**Return Value:** None

[Back to Top](#module-overview)


## get\_header
No description



**Signature:** (line)





**Return Value:** None

[Back to Top](#module-overview)


## iter\_parse
Stream is either a text string, a sequence of or an iterator of lines
Usage:
```
for header, body in parse(stream):
    print(header)  # string
    for line in body:  # iterator
        print(line)
```
Note that stream might be binary text encoded with UTF-8



**Signature:** (stream, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


## iter\_read
Iteratively read a file. This generator yields a 2-tuple made
of a header string and an iterator to iterate over the body line by line.



**Signature:** (src, end\_of\_stream=None)

|Parameter|Description|
|---|---|
|src|is either a path string, a pathlib.Path instance, or a file object which might expose binary text encoded with UTF-8|
|end\_of\_stream|a character or string to indicate the end of the stream|





**Return Value:** Yields a 2-tuple made of a header string and a body iterator to iterate
over the body line by line

[Back to Top](#module-overview)


## parse
parse and flatten.
returns the dict of sections (keys are headers and
values are section's bodies. a section body is a text string



**Signature:** (stream, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


## read
Read a file then flatten its contents (concatenate sections with same header).



**Signature:** (src, end\_of\_stream=None)

|Parameter|Description|
|---|---|
|src|is either a path string, a pathlib.Path instance, or a file object which might expose binary text encoded with UTF-8|
|end\_of\_stream|a character or string to indicate the end of the stream|





**Return Value:** returns the dict of sections where keys are headers and
values are section's bodies. A section body is a text string

[Back to Top](#module-overview)


## render
Render sections, i.e., transform the sequence of sections
into a Braq text document (string)



**Signature:** (\*sections, spacing=1)

|Parameter|Description|
|---|---|
|sections|Section objects or header-body tuples. Note that a body is either a text string or a sequence of lines|
|spacing|number of empty lines between two sections, defaults to 1|





**Return Value:** A string representing a Braq text document

[Back to Top](#module-overview)


## write
Write to a file



**Signature:** (\*sections, dest=None, spacing=1)

|Parameter|Description|
|---|---|
|\*sections|sections objects or header-body 2-tuples|
|dest|is either a path string, a pathlib.Path instance|
|spacing|number of lines between two sections, defaults to 1|





**Return Value:** None

[Back to Top](#module-overview)


