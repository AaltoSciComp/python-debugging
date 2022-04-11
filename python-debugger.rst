
The Python Debugger
===================

Python is an interpreted language. Thus, the runtime is reading the source code line-by-line and executing it. The runtime offers a service, where you can register a function that is called whenever a specific line is executed. Similarly other call backs can be registered for e.g. exception handlerers. On top of these services, one can build a *debugger*, which sets up a nice user-interface to study the executing python routines.

The Python debugger, pdb, can be used to inspect the state of the program
while it's running. Pdb is a standard Python library, so you don't need to
install it.

The most common way of using it is running `pdp.set_trace()` in your script.
(Since version 3.7: You can simply use the built-in `breakpoint()`.)

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
----------------------

You can turn on automatic calling of the pdb debugger after an exception:

.. code-block:: console

    $ ipython --pdb examples/divide_by_zero_with_pdp.py


There is also a magic command to enable pdb:


.. code-block:: python

    %pdb






pdb with jupyter
----------------

Use the *%debug* magic command to initiate ipdb



pdb with spyder
---------------


The ipdb is `available also in spyder <https://docs.spyder-ide.org/5/panes/debugging.html>`_.



Alternatives for pdb
--------------------

 * https://pypi.org/project/pudb/
 * PyCharm has its own `debugger <https://www.jetbrains.com/pycharm/features/debugger.html>`_.
 * If you do use `print()`, it may not immediately print out your debug message. you may need to use the optional parameter `flush=True` to `print()`. Alternatively, setting the `environment variable <https://docs.python.org/3/using/cmdline.html#environment-variables>`_ `PYTHONUNBUFFERED` to a non-empty string may be enough to force immediate output.

