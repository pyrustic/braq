Back to [All Modules](https://github.com/pyrustic/braq/blob/master/docs/modules/README.md#readme)

# Module Overview

**braq.section**
 
No description

> **Classes:** &nbsp; [Section](https://github.com/pyrustic/braq/blob/master/docs/modules/content/braq.section/content/classes/Section.md#class-section)
>
> **Functions:** &nbsp; [\_ensure\_body](#_ensure_body) &nbsp;&nbsp; [render](#render)
>
> **Constants:** &nbsp; None

# All Functions
[\_ensure\_body](#_ensure_body) &nbsp;&nbsp; [render](#render)

## \_ensure\_body
No description



**Signature:** (body)





**Return Value:** None

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


