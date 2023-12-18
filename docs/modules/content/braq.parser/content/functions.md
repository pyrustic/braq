Back to [All Modules](https://github.com/pyrustic/braq/blob/master/docs/modules/README.md#readme)

# Module Overview

**braq.parser**
 
No description

> **Classes:** &nbsp; [Parser](https://github.com/pyrustic/braq/blob/master/docs/modules/content/braq.parser/content/classes/Parser.md#class-parser)
>
> **Functions:** &nbsp; [check\_header](#check_header) &nbsp;&nbsp; [get\_header](#get_header) &nbsp;&nbsp; [iter\_parse](#iter_parse) &nbsp;&nbsp; [parse](#parse)
>
> **Constants:** &nbsp; None

# All Functions
[check\_header](#check_header) &nbsp;&nbsp; [get\_header](#get_header) &nbsp;&nbsp; [iter\_parse](#iter_parse) &nbsp;&nbsp; [parse](#parse)

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


## parse
parse and flatten.
returns the dict of sections (keys are headers and
values are section's bodies. a section body is a text string



**Signature:** (stream, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


