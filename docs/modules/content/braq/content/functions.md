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
    for header, body in parse(stream):
        print(header)  # string
        for line in body:  # iterator
            print(line)
Note that stream might be binary text encoded with UTF-8



**Signature:** (stream, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


## iter\_read
src is either a path string, a pathlib.Path instance, or a file object.
Note that the file object might expose binary text encoded with UTF-8



**Signature:** (src, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


## parse
parse and flatten.
returns the dict of sections (keys are headers and
values are section's bodies. a section body is a text string



**Signature:** (stream, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


## read
read and flatten.
returns the dict of sections (keys are headers and
values are section's bodies. a section body is a text string



**Signature:** (src, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


## render
sections are either Section objects or header-body tuples
Note that a body is either a text string or a sequence of lines



**Signature:** (\*sections, spacing=1)





**Return Value:** None

[Back to Top](#module-overview)


## write
No description



**Signature:** (\*sections, dest=None, spacing=1)





**Return Value:** None

[Back to Top](#module-overview)


