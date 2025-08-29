# What is __Init__.py File in Python?
You can organize code into modules AND packages, packages are COLLECTIONS of modules. The __init__.py file is a Python file that is executed when a package is imported, so normally it will be executed once even when you import a package numerous times.

It is a special file used in Python to define packages and initialize their namespaces.
- It can contain an initialization code that runs when the package is imported
- Now technically without this file, Python won't recognize a directory as a package, however latest versions of Python does not require this, as it now occurs <u>implictly</u>.
## Nonetheless:
  - It marks the directory as a Python Package so that the interpreter can find the modules inside it. 
  - It can contain initialization code for the package, such as importing submodules, defining variables, or executing other code.
    
# Syntax of Importing and Using __Init__.py File
- To import a package or <u>module</u>, us the '<u>import</u>' keyword followed by the package or module name. For instance, importing module1 from the 'package' is done with:
  ```
  import mypackage.module1
  ```
---
- Alternatively, use 'from' followed by the **package/module name**, and 'import' for **specific functions, classes, or variables**. Example:
  ```
  from mypackage.Module1 import func1
  ```
---
- <span style="color: red;">Avoid using</span> the '*' operator to import all names form a package/module, as it may lead to ocnflicts and reduce code readability. For instance:
  ```
    from mypackage import *
  ```
Note that this method only imports names defined in the **init**.py file, excluding submodules. To include submdules, use **all** variables in **init**.py to specify the modules or names to import.