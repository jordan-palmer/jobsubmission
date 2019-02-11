Farm Communication
==================

This chapter introduces the user to useful farm commands which allows the user to check and delete jobs.

To view all of the jobs running on the farm do: 

.. code-block:: console
   
   qstat

To only view your jobs, do: 

.. code-block:: console

   qstat -u yourusername

In order to kill one of your current jobs do the command above and copy and paste the number next **pbs2** assigned to your job, i.e: 


.. code-block:: console

   6508787.pbs2        yourjobname         yourusername      time:Q/R:length

and do:

.. code-block:: console

   qdel 6508787

