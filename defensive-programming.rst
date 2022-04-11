=====================
Defensive Programming
=====================

Reporting (un)expected state
----------------------------

- Assertions check for user defined conditions and raise an exception if the condition is False. `The syntax is <https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement>`_:

  .. code-block:: python

     assert expression0
		  
     assert expression1, expression2

     # Which is eqvivalent to:

     if __debug__:
         if not expression0: raise AssertionError
     
     if __debug__:
         if not expression1: raise AssertionError(expression2)

     

- Raising Exceptions

  In a more complex case you could `raise a custom exception <https://docs.python.org/3/tutorial/errors.html>`_ that carries the exact meaning you wish to transfer:

.. code-block:: python

   class mySpecialError(Exception):
	""" This error is raised in a special situation.  """
	pass

   if myValue < myLimit:
        raise mySpecialError()
	
- `Use loggers to easily turn on and off your debug writes <https://docs.python.org/3/howto/logging.html#logging-basic-tutorial>`_.

  - The basic idea of loggers is to provide a framework that makes it convenient to choose the current verbosity of the program depending on simple centralized run-time setting.
  - The logger framework can do formatting of the messages, such as including the time.


  
Checks while writing
--------------------
  
- Using On-line linting and IDEs

  - `Pylint <https://pylint.pycqa.org/en/latest/intro.html>`_ is an off-line tool that can check your code for formatting and for certain logical errors that could hint at hidden problems.

  
Divide and conquer
------------------

- Separate objects and clear interfaces
- Unit testing

Document well
-------------

- You can give `type hints <https://docs.python.org/3/library/typing.html>`_ about what types are expected, but it is only documentation, not enforced by the runtime.
