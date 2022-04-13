============
Introduction
============

The four steps of debugging
---------------------------

1. Identify the bug

   - Get a report from user or find an example input that exhibits the problem
   - Find the faulty line or piece of logic

2. Isolate

   - Confirm that you have found the problem
   - Could be e.g. a unit test or a minimal (non)working example

3. Fix

   - Replacing the erroneous code with correct code

4. Test

   - Check that the bug is fixed and no new bugs were introduced.

In this course we are concentrating on the Identifying phase. It is expected, that as soon as you identify the bug, it is more or less obvious how it should be fixed.

Debugging is the art of identifying inconsistency between the expected and actual operation
-------------------------------------------------------------------------------------------

A problem exists whenever the user expects the system to operate differently from how it actually operates. The issue may lay either in the expectations or in the system.

Sometimes a program does do what the programmer intents it to do, but the user expects some other behaviour. Then the bug is in the user interface (UI), in the application programming interface (API) or in the documentation. For scientific computation this is most often encountered when starting to use a new library or software.

However, we concentrate on the common and basic problem of how to fix your own code. Here the inconsistency is usually between what you mean the computer to do and what you tell the computer to do.
The key to success is to have sufficiently deep understanding of what your code and the programming language does, to simulate in your mind the program.

This is all just a complicated way to say, that to debug Python successfully, you need to know the python language and some details of the underlying runtime.



Thus, we first recapitulate a few key features of the python language. We say a few words on how to avoid problems. After that we take a look at the python specific tools to help analyze a python program. 

