.. Debugging Python documentation master file, created by
   sphinx-quickstart on Wed Jan 19 17:12:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Debugging Python
================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Things about Python
-------------------

 - Syntax errors directly raise an error
   - Indentation
 - Scoping
   - Setting a name defined in a higher scope defines it in this one.
 - Lists:
   - As a default argument (default arguments are evaluated only once...)
   - Mutated in functions
 - Dependency issues!
   - Is the package in
     - system folders
     - pip folders
     - conda, pipenv, ...


Error Messages
--------------

 - A couple of examples
   - Main points: how to read the stack trace, find the line in your code


The Python Debugger
-------------------

 - Introduce pdp
 - Using ipdp (IPython debugger) in Jupyter



Defensive Programming
---------------------

- Assertions

- Raising Exceptions

- Handling Exceptions Programatically


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
