# Dictionary-Objecter

this class takes a python dictionary object and starting a loop over all its keys, then takes every key and value to set it as attribute with `setattr()` to **it self**

it uses **Recursion** to support nested dictionaryes

the method will add an underscore *('_')* to any key starts with a digit, and replace every space *(' ')* with underscore *('_')*
