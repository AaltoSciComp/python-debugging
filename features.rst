======================================
Python features relevant for debugging
======================================

Python is an interpreted language
---------------------------------

 - Python is interpreted

   - There is no compilation phase, just syntax checking, then runtime
   - You can pre-process in IDE or a separate linting tool. A few more words on this later.

 - Syntax errors are easy to spot. They raise an exception immediately when you try to run the code.

   - Indentation problems are most common. Many text editors can show you different types of white space (tabs, spaces...)
   - Parenthesis and quotation mark mismatch as well




Datatypes -- strongly and dynamically typed
-------------------------------------------
 - Python is a strongly, but dynamically typed language:

   - Strong: The type of a runtime object does not change automatically.
   - Dynamic: Runtime objects have a specific type instead of variables having a type.

     - Since there are no types for variables, there is no way to force a specific type e.g. for a argument of a function.

 - Python feels like a weakly typed language, that is you can usually pass a variable to a function, and it (often) just works. This is achieved with duck-typing and sometimes with operator overloading

   - If the object has the expected methods and instance variables of the expected type, then it is generally of a compatible type. (duck-typing)
   - Operators and methods can be overwritten in a derived class.
   - For example, does it matter if an object is a sequence or a mapping, as long as you can index it conveniently?

     .. code-block:: python

	x_list = [    'a',     'b',     'c' ]
	y_dict = { 0 :'a',  1 :'b',  2 :'c' }
	x_list[1]    # 'b'
	y_dict[1]    # 'b'

     - This leads to errors:

       - what happens with ``x_list[0:2]`` and ``y_dict[0:2]``?
       - what happens with ``y_dict.keys()`` and ``x_list.keys()``?

   - You can give `type hints <https://docs.python.org/3/library/typing.html>`_ about what types are expected, but it is only documentation, not enforced by the runtime.

     .. code-block:: python
	
	def square( x: float) -> float:
	   return x**2

Scoping
-------

Python resolves variables using the LEGB rule or the **L**\ ocal, **E**\ nclosing, **G**\ lobal, **B**\ uilt-in rule.

 - Setting a name defined in a higher scope defines a new one.

   .. code-block:: python

      x = 2

      def set_x():
         x = 1

      set_x()
      print(x)# output: 2

   - If you wish to set the value of a variable from outer scope or a global variable within a function or loop, you can use the keywords ``nonlocal`` and ``global``.

 - Class variables have a similar effect. Derived classes share the class variables of the base class, unless re-defined.


Mutable vs immutable datatypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- An example: A list can be mutated in a function:

  .. code-block:: python

        def alternate(values):
           ''' Return a copy of a list with every second
           element inverted
           '''
           for i in range(0, len(values), 2):
              values[i] = -values[i]
           return values

        l = [1,2,3,4]
        alternated_l = alternate(l)
        print(l) # [ -1, 2, -3, 4 ]



- Not all variables can be  `mutated <https://docs.python.org/3/reference/datamodel.html>`_:

  - Mutable types are passed by reference
  - Mutable types are bound to a new name on assignment
  - Immutable types are passed by value
  - Immutable types are copied on assignment
    
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

- This applies also with numpy arrays. Remember, that normal assignment in numpy is not a copy, but a new name for the same data.

Functions can have default arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Default arguments are evaluated only once.

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

     - ``append_to`` is stored as long as the function ``append_to_list`` is stored
       
       - The values are stored in the ``__defaults__`` attribute of the function.
       - Take special care with functions with default values calling functions with default values. Best practice is often to use None as the default value and then fill in the default value in the function body.

- This is similar to the bugs one may encounter due to the late-binding behaviour in python closures. In a closure, an outer function returns a function, and the returned function uses a variable from the outer function. 
     - The variables referenced from the outer functions scope are stored in the ``__closure__`` attribute of the returned function. However, these variables are looked up only at the time when the returned function is executed. There are subtle effects in play here.
       
Memory management
-----------------

Python has automatic memory management. Unreachable runtime objects may be automatically removed from memory. However, this garbage collection is not guaranteed to happen.

 - You cannot rely on the finalizer method ``__del__()`` to be executed
 - The ``del``-statement only reduces the reference count of objects.
 - if you are running out of memory:

   - Size of an object can be checked with ``sys.getsizeof()``
   - Build in module ``gc`` provides an interface to the Garbage collector

Dependency issues
-----------------

Python looks for packages in

  1. First in user's own Python packages (in $HOME/.local/lib/python...)
  2. Then system directories (like /usr/local in Linux)

The exact list of folders your python is searching is defined in ``sys.path``.
     
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

Virtual environments
~~~~~~~~~~~~~~~~~~~~

Virtual environments make dependency management easier.
They essentially force Python to look for packages in
one place. This way you always know what packages your
software needs, and when you get stuck with dependency
problems, you can remove the environment and reinstall.

Examples of virtual environment managers for Python:

 - `Pipenv <https://pipenv.pypa.io/en/latest/>`_

 - `Virtualenv <https://virtualenv.pypa.io/en/latest/>`_

   - Subset of virtualenv is offered in the standard module `venv <https://docs.python.org/3/library/venv.html>`_
   
 - `Conda <https://docs.conda.io/>`_

   - `Mamba <https://anaconda.org/conda-forge/mamba>`_ is a fast drop-in replacement, if it takes too long to install packages with Conda.

   - To use pip with conda, always run

     .. code-block:: console

        $ conda install pip

Working with packaged python code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can inspect the source code of installed packages with an editor. The file location you can get from the variable ``__file__``:


.. code-block:: python
   
   import pdb
   print(pdb.__file__) # /u/54/sjjamsa/unix/conda/miniconda3/envs/sphinx/lib/python3.10/pdb.py




If you download the source code, (e.g. with git), you can install the package so that changes to source code do not require re-installing the package:

.. code-block:: console
   
   $ cd my_package_folder
   $ pip install -e ./


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

Whenever Python encounters an error (un-caught exception, to be exact), it prints a
trace-back like the one above. It's best to start
reading of from bottom.

The last line shows the error that was encountered,
and often some useful additional information. In this
case all we get is "division by zero", which is good
to know but does not tell us exactly what's wrong.

The two lines above give us the line where the problem
is. Usually there are several lines in libraries we
did not write ourselves, so keep reading until you
find one you can edit.

Maybe you can figure out the problem, but will later use a debugger to figure it out.


