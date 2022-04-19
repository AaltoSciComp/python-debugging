
The Python Debugger
===================

Python is an interpreted language. Thus, the runtime is reading the source code line-by-line and executing it. The runtime offers a service, where you can register a function that is called whenever a specific line is executed. Similarly other call backs can be registered for e.g. exception handlers. On top of these services, one can build a *debugger*, which sets up a nice user-interface to study the executing python routines.

The Python debugger, pdb, can be used to inspect the state of the program
while it's running. Pdb is a standard Python library, so you don't need to
install it.

The most common way of using it is running ``pdp.set_trace()`` in your script.
(Since version 3.7: You can simply use the built-in ``breakpoint()``.)

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

Python has stopped on line 16 of ``examples/divide_by_zero_with_pdp.py``. You can
now look at the values of any variables, run Python functions and even change
the program state before continuing.

Here are some useful pdb commands:

  - Show current location
    
    - **list** Print a few lines of code around the current position.
    - **where** Print the current position and the functions that were called
      to get there (same as the stack trace printed when an exception is raised).

  - Work with breakpoints
    
    - **break** ``[([filename:]lineno | function) [, condition]]`` Set a new breakpoint to a specific line or function. With the optional condition statement, the program is stopped only if the condition evaluates True.
    - **break** List all breaks
    - **disable #** disables a breakpoint
    - **clear #** removes a breakpoint

  - Continue execution
    
    - **next** Execute the current line and move to the next one.
    - **until** Execute until you reach next line (useful in loops)
    - **step** If the line contains a function, move into it. Otherwise execute
      the current line.
    - **continue:** Run until the next breakpoint

  - Move point of view 
    
    - **up** Move to the function that called this one (up the stack).
    - **down** Move to the function called from this one (down the stack).

  - Print variables
    
    - **p variable** Print the value of an expression (you can also run ``print(variable)``)
    - **display variable** Display the value of the expression if it changed

It is also possible to modify variable values within the program:

.. code-block::
   
   % python examples/divide_by_zero_with_pdp.py
   > /u/54/sjjamsa/unix/debugCourse/python-debugging/examples/divide_by_zero_with_pdp.py(8)<module>()
   -> def sum(numbers):
   (Pdb) b 18, denom==0
   Breakpoint 1 at /u/54/sjjamsa/unix/debugCourse/python-debugging/examples/divide_by_zero_with_pdp.py:18
   (Pdb) c
   > /u/54/sjjamsa/unix/debugCourse/python-debugging/examples/divide_by_zero_with_pdp.py(18)calc_average()
   -> return enum / denom
   (Pdb) p denom
   0
   (Pdb) denom=1.0
   (Pdb) p denom
   1.0
   (Pdb) c
   [3.0, 3.5, 4.0, 0.0]

      
      
Watching variables
~~~~~~~~~~~~~~~~~~

Debuggers can often watch a specific variable for changes but, ``pdb`` does not have that feature. Instead, You can use  `Watchpoints <https://pypi.org/project/watchpoints/>`_, which  implements a variable monitor.

The package is available from PyPi:

.. code-block:: console

    $ pip install watchpoints


Afterwards you can use it fairly simply:

.. code-block:: python

    from watchpoints import watch
    watch(myVariable)

The file ``examples/divide_by_zero_with_watchpoints.py`` serves as an example:
    
.. code-block:: console

   python examples/divide_by_zero_with_watchpoints.py


Watchpoints have further features, such as:

- Watching the **variable** holding an object
- Watching the **object** stored in some variable
- Conditional watchpoints
- Integrates with pdb: ``watch.config(pdb=True)``

   
    
Pdb in various environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~
    

pdb with iPython: ipdb
----------------------

You can turn on automatic calling of the pdb debugger after an exception:

.. code-block:: console

    $ ipython --pdb examples/divide_by_zero.py


There is also a magic command to enable pdb:


.. code-block:: python

    %pdb

To run a script with the debugger, use ``-d``. The debugger will stop at the first line of the script.

.. code-block:: python

    %run -d examples/divide_by_zero.py



pdb with jupyter
----------------

Internally, jupyter uses ipdb, so many things works as in normal command line ``ipython``.

- The ``%pdb``-magical command enables automatics start of ``ipdb`` in case of an Exception. 
- Alternatively, you can use the ``%debug`` magic command to initiate ``ipdb`` in post-mortem after the Exception has been printed.



pdb with spyder
---------------


The ipdb is `available also in spyder <https://docs.spyder-ide.org/5/panes/debugging.html>`_.



Alternatives for pdb
~~~~~~~~~~~~~~~~~~~~

 * `pdb++ <https://pypi.org/project/pdbpp/>`_ is meant to be a drop-in replacement for pdb
 * `Pudb <https://pypi.org/project/pudb/>`_ strives to provide all the niceties of modern GUI-based debuggers in a more lightweight and keyboard-friendly package. 
 * PyCharm has its own `debugger <https://www.jetbrains.com/pycharm/features/debugger.html>`_.

If you do use ``print()``, it may not immediately print out your debug message. You may need to use the optional parameter ``flush=True`` to ``print()``. Alternatively, setting the `environment variable <https://docs.python.org/3/using/cmdline.html#environment-variables>`_ ``PYTHONUNBUFFERED`` to a non-empty string may be enough to force immediate output.

