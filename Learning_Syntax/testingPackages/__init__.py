# Define all prerequisites
'''In below code, the __all__ vairable is alist of stirng that indicate the names
that should be imported when using the '*' operator. The dot (.) before the module names
means that they are relative imports, which means that they are imported from the same package.'''


from . import apples as notApples
from . import oranges

__all__= [notApples, oranges]

'''
“Are the variables named module1 and module2?”
They’re names (variables) in the package namespace that reference module objects. 
After those imports run, module1 is a module object, not a plain string or number.

“What does the dot represent?”
The dot is relative import syntax: . = “this package”. 
(You use this inside __init__.py or another module that’s part of a package.)

“Are they actual files?”
Usually yes. Most commonly you have a layout like:
yourpackage/
  __init__.py     # contains your snippet
  module1.py      # this is the 'module1' submodule
  module2.py      # this is the 'module2' submodule

'''
