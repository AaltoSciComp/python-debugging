.. Debugging Python documentation master file, created by
   sphinx-quickstart on Wed Jan 19 17:12:23 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. contents:: Table of Contents
	          :depth: 4
   
Debugging Python
================

.. toctree::
   :maxdepth: 4
   :caption: Contents:
	     

Introduction
------------
	     
The four steps of debugging
***************************

1. Identify the bug
   
   - Get a report from user or find an example input that exhibits the problem
   - Find the faulty line or piece of logic

2. Isolate

   - Confirm that you have found the problem
   - Could be e.g. a unit test or a minimal (non)working example

3. Fix

   - Replacing the erronous code with correct code

4. Test

   - Check that the bug is fixed and no new bugs were introduced.
   
In this course we are concentrating on the Identifying phase. It is expected, that as soon as you identify the bug, it is more or less obvious how it should be fixed. 

Debugging is the art of identifying inconsistency between the expected and actual operation
*******************************************************************************************

A problem exists whenever the user expects the system to operate differently from how it actually operates. The issue may lay either in the expectations or in the system.

Sometimes a program does do what the programmer intents it to do, but the user expects some other behaviour. Then the bug is in the user interface (UI), in the application programming interface (API) or in the documentation. For scientific computation this is most often encountered when starting to use a new library or software.

However, we concentrate on the common and basic problem of how to fix your own code. Here the inconsistency is usually between what you mean the computer to do and what you tell the computer to do.
The key to success is to have sufficiently deep understanding of what your code and the programming language does, to simulate in your mind the program.

This is all just a complicated way to say, that to debug Python succesfully, you need to know the python language and some details of the underlying runtime.



Thus, we first recapitulate a few key features of the python language. After that we take a look at the python specific tools to help analyse a python program. We conclude with a few words on how to avoid problems.

	     
Python features relevant for debugging
--------------------------------------

Datatypes -- weakly and dynamically typed
*****************************************
 - Python is weakly typed language in the sence that there is no way to force a specific type e.g. for a function argument.
 - If the object has the expected methods and instance variables of the expected type, then it is generally of a compatible type. (duck-typing) 
 - Operators and methods can be overwritten.



Syntax errors
*************

 - Python is interpretted
   
   - There is no compilation phase, just syntax checking, then runtime
     
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

     append_to will is stored as long as the function append_to_list stays in scope

     - Take special care whith functions with default values calling functions with default values. Best practice is often to use None as the default value and then fill in the default value in the function body.
   

Mutable vs immutable datatypes as function arguments
++++++++++++++++++++++++++++++++++++++++++++++++++++

 - There is no way for the computer to automatically check if you are giving a sane input in terms of argument types
 - https://docs.python.org/3/reference/datamodel.html
 - Mutable types are passed by reference
 - Immutable types are passed by value
 - How do you know if a type is mutable or not?

   - numbers are immutable (e.g. Float)
   - immutable sequences. 

     - String
     - Tuples (The objects referenced in a Tuple may be mutable.)
     - Byte

   - immutable sets:
      - Frozen set

   - mutable: lists, dictionaries, most objects

   - The contents of a mutable datatype cannot be changed; a new one must be always created:

     .. code-block:: python

		     x = 5
		     id(x)      # 123456
		     x = x + 1
		     id(x)      # 123777

		     y = ['foo']
		     id(y)      # 234567
		     y.append('bar')
		     id(y)      # 234567


     
Garbage collecting
******************

garbage collection is not guaranteed to happen

 - You cannot rely on the finalizer __del__() to be executed
 - del only reduces the reference count


Dependency issues
*****************

Python looks for packages in

  1. First in users own Python packages (in $HOME/.local/lib/python...)
  2. Then system directories (like /usr/local in Linux)

The same is true when uninstalling packages with pip.
So if you're not sure where a package is, uninstall it
at least twice.


There are many ways to install a package and these don't always work together.

 - System package manager (apt, ...)

   .. code-block:: console

      $ apt install python-scipy

 - System level pip

   .. code-block:: console

      $ pip install scipy

   - Don't mix pip with system installers. They don't track each others packages, but do install in the same place.

 - User level pip

   .. code-block:: console

      $ pip install --user scipy

   - Don't need to be admin
   - These will be checked first when importing

Virtual environments make dependency management easier.
They essentially force Python to look for packages in
one place. This way you always know what packages your
software needs, and when you get stuck with dependency
problems, you can remove the environment and reinstall.

Examples of virtual environment managers for Python:

 - Pipenv

 - Virtualenv

 - Conda / Mamba

   - To use pip with conda, always run

     .. code-block:: console

        $ conda install pip

Inspecting the source code of packages
++++++++++++++++++++++++++++++++++++++

Add contents here

Error Messages
--------------

Try running

.. code-block:: console

    $ python examples/divide_by_zero.py

This will throw an error:

.. code-block:: console

    Traceback (most recent call last):
    File "examples/divide_by_zero.py", line 32, in <module>
      averages = conditional_averages(numbers)
    File "examples/divide_by_zero.py", line 24, in conditional_averages
      average = calc_average(copy)
    File "examples/divide_by_zero.py", line 14, in calc_average
      return enum / denom
    ZeroDivisionError: division by zero

Whenever Python encounters an error, it prints a
traceback like the one above. It's best to start
reading of from bottom.

The last line shows the error that was encountered,
and often some useful additional information. In this
case all we get is "division by zero", which is good
to know but does not tell us exactly what's wrong.

The two lines above give us the line where the problem
is. Usually there are several lines in libraries we
did not write ourselves, so keep reading until you
find one you can edit.

Maybe you can figure out the problem, but will use a debugger to figure it out
in the next section.



The Python Debugger
-------------------

The Python debugger, pdb, can be used to inspect the state of the program
while it's running. Pdb is a standard Python library, so you don't need to
install it.

The most common way of using it is running `pdp.set_trace()` in your script.

.. code-block:: python

    import pdb

    ...

    pdp.set_trace()

When Python reaches this line, it will pause and open a pdb prompt:

.. code-block:: console

    $ python examples/divide_by_zero_with_pdp.py
    > /u/24/rantahj1/unix/src/python-debugging/examples/divide_by_zero.py(16)calc_average()
    -> return enum / denom
    (Pdb)

Python has stopped on line 16 of `examples/divide_by_zero_with_pdp.py`. You can
now look at the values of any variables, run Python functions and even change
the program state before continuing.

Here are some useful pdb commands:

  - **list:** Print a few lines of code around the current position.
  - **where:** Print the current position and the functions that were called
    to get there (same as the stack trace printed when an exception is raised).
  - **next:** Execute the current line and move to the next one.
  - **step:** If the line contains a function, move into it. Otherwise execute
    the current line.
  - **continue:** Run until the next `pdb.set_trace`
  - **up**: Move to the function that called this one (up the stack).
  - **down**: Move to the function called from this one (down the stack).
  - **p variable:** Print the value of a variable (you can also run
    `print(variable)`)
  - **b #**
  - **b**
  - **until #**


pdb with iPython: ipdb
**********************

Add content here


pdb with jupyter
****************

Use the *%debug* magic command to initiate ipdb



pdb with spyder
***************

Add content here



Alternatives for pdb
********************

 * https://pypi.org/project/pudb/





Defensive Programming
---------------------

- Assertions

- Raising Exceptions

- Using On-line linting and IDEs

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
