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

Syntax errors
*************

 - Directly raise an error
 - Indentation problems most common
   - Many text editors can show you different types of white space (tabs, spaces...)

Scoping
*******

 - Setting a name defined in a higher scope defines a new one.

   .. code-block:: python

      x = 2

      def set_x():
         x = 1

      set_x()
      print(x)# output: 2

 - Lists:

   - Mutated in a function

     .. code-block:: python

        def alternate(values):
           ''' Return a copy of a list with every second
           element inverted
           '''
           for i in range(0:2:len(values)):
              values[i] = -values[i]
           return values

        l = [1,2,3,4]
        alternated_l = alternate(l)
        print(l) # [1,-2, 3,-4]

   - As a default argument (default arguments are evaluated only once...)

     .. code-block:: python

        def append_to_list(value, append_to=[]):
           ''' Add a value to a list. If no list if given,
           create a new one.
           '''
           append_to.append(value)
           return append_to

        l = append_to_list(1) # [1]
        print(l)

        l = append_to_list(2) # [1,2]


Dependency issues
*****************

There are many ways to install a package and these don't always work together.

Python looks for packages in

  1. Users own Python packages (in $HOME/.local/lib/python...)
  2. System directories (like /usr/local in Linux)


 - System package manager (apt, ...)

   .. code-block:: console

      apt install python-scipy

 - System level pip

   .. code-block:: console

      pip install scipy

   - Don't mix with apt or other system installers. They don't track each other.

 - User level pip

   .. code-block:: console

      pip install --user scipy

   - Don't need to be admin
   - These will be checked first when importing

 - conda / mamba

   .. code-block:: console

      conda install scipy

   - Easy to manage environments
   - Can install system libraries
   - To use pip, always run

     .. code-block:: console

        conda install pip


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


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
