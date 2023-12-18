Back to [All Modules](https://github.com/pyrustic/braq/blob/master/docs/modules/README.md#readme)

# Module Overview

**braq.parser**
 
No description

> **Classes:** &nbsp; [Parser](https://github.com/pyrustic/braq/blob/master/docs/modules/content/braq.parser/content/classes/Parser.md#class-parser)
>
> **Functions:** &nbsp; [check\_header](https://github.com/pyrustic/braq/blob/master/docs/modules/content/braq.parser/content/functions.md#check_header) &nbsp;&nbsp; [get\_header](https://github.com/pyrustic/braq/blob/master/docs/modules/content/braq.parser/content/functions.md#get_header) &nbsp;&nbsp; [iter\_parse](https://github.com/pyrustic/braq/blob/master/docs/modules/content/braq.parser/content/functions.md#iter_parse) &nbsp;&nbsp; [parse](https://github.com/pyrustic/braq/blob/master/docs/modules/content/braq.parser/content/functions.md#parse)
>
> **Constants:** &nbsp; None

# Class Parser
No description.

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|end_of_stream|getter|None||
|end_of_stream|setter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [parse](#parse) &nbsp;&nbsp; [\_ensure\_line](#_ensure_line) &nbsp;&nbsp; [\_ensure\_stream](#_ensure_stream) &nbsp;&nbsp; [\_is\_end\_of\_stream](#_is_end_of_stream) &nbsp;&nbsp; [\_iter\_body](#_iter_body)

## \_\_init\_\_
end_of_stream represents a non-empty string that will be
used to indicate the end of the stream



**Signature:** (self, end\_of\_stream=None)





**Return Value:** None

[Back to Top](#module-overview)


## parse
Stream is an iterator, a sequence of lines, or a text string
Usage:
    for header, body in Parser.parse(stream):
        print(header)  # string
        for line in body:  # iterator
            print(line)
Note that stream might be binary text encoded with UTF-8



**Signature:** (self, stream)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_line
No description



**Signature:** (self, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_stream
No description



**Signature:** (self, stream)





**Return Value:** None

[Back to Top](#module-overview)


## \_is\_end\_of\_stream
No description



**Signature:** (self, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_iter\_body
No description



**Signature:** (self, stream)





**Return Value:** None

[Back to Top](#module-overview)



