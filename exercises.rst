=========   
Exercises
=========

You can try the debugger and tools on your own code, or do the following artificial exercises:

Ex 1. Install double pendulum
=============================

The exercises 1. & 2. will be using the following repository:
https://github.com/AaltoSciComp/double-pendulum

This code shows a double pendulum in action. A gui is needed for it to run, but the required libraries are available for Linux, Windows, Mac, ...


- Try running the code without installation:

  .. code-block:: console
		
     $ git clone https://github.com/AaltoSciComp/double-pendulum.git
     $ cd double-pendulum/
     $ python double-pendulum

  This step includes a learning goal: Recognize a missing python package, ``pygame`` in this case. You can install the package manually with ``pip``, or let the automatic installation system install it in the next phase.

- Install the source code as a package.

  .. code-block:: console
		
     $ git checkout pip_installable
     $ pip install -e ./
     $ double-pendulum

  or if you need to install with the ``--user``

  .. code-block:: console
		
     $ git checkout pip_installable
     $ pip install --user -e ./
     $ alias double-pendulum=$( python3 -c "import site; print(site.USER_BASE)" )/bin/double-pendulum # This is for bash/zsh shells. For C-family of shells, drop the "=". 
     $ double-pendulum
   
     - Confirm that editing the files has immediate effect. Add a ``print()`` or a ``break()`` statement in the ``main()``-function in ``double-pendulum/doublependulum/dp.py``.
   

Ex 2. Fix the broken pendulum
=============================

The pendulum is broken. Find the corrupted line. You may need to know, that the code uses four generalized coordinates: two for the angles of the hands (``t``) and two for the angular velocities of the hands (``w``). Try finding where the angle goes to zero.

- First get the broken version:

  .. code-block:: console
		
     $ git checkout broken_pendulum




- Here is one way to start the debugger:
   
  .. code-block:: console
		
     $ python -m pdb doublependulum/dp.py

  - You may wish to set a breakpoint on line 205 of dp.py and start exploring from there.

Ex 3. Defend!
=============

.. code-block:: console
		
   $ git clone https://github.com/AaltoSciComp/python-debugging.git

   
- Add an assertion to ``examples/divide_by_zero.py``

  - How is this better than the divide by zero Exception?

- Add typehints and expand the documentation in ``examples/indexing.py``.
