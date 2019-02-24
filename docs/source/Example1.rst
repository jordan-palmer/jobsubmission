Example 1
=========

Example 1 is a simple python script which runs a command of your choice. This works in exactly the same way as the **HelloFarm.py** example.

1. Change the variables at the top of the file.

2. Go to the command line and do:

.. code-block:: console

   python RunClass.py

If everything has worked successfully, you would expect to see a new directory created inside your **WorkDir** with the specified name (in the example this is **TESTDIRNa**). Inside that directory there should be three more sub directories namely, **eoFiles**, **shellScripts**, and **inputFiles**. When the job has finished running, the program will copy the oytput files from the node into the correct directories. If, inside the job directory, there is no output file then something has gone wrong. Check the log file and error file inside the **eoFiles** directory to help discover the problem.    