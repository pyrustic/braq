Back to [All Modules](https://github.com/pyrustic/braq/blob/master/docs/modules/README.md#readme)

# Module Overview

**braq.fileio**
 
No description

> **Classes:** &nbsp; None
>
> **Functions:** &nbsp; [iter\_read](#iter_read) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [write](#write)
>
> **Constants:** &nbsp; None

# All Functions
[iter\_read](#iter_read) &nbsp;&nbsp; [read](#read) &nbsp;&nbsp; [write](#write)

## iter\_read
src is either a path string, a pathlib.Path instance, or a file object.
Note that the file object might expose binary text encoded with UTF-8



**Signature:** (src, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


## read
read and flatten.
returns the dict of sections (keys are headers and
values are section's bodies. a section body is a text string



**Signature:** (src, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


## write
No description



**Signature:** (\*sections, dest=None, spacing=1)





**Return Value:** None

[Back to Top](#module-overview)


