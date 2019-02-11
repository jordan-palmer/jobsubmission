Installation
============
Cloning the Git Repository
--------------------------
We would recommend that you create a directory named *yourname-packages* and enter said directory using the commands:

.. code-block:: console

     mkdir yourname-packages

.. code-block:: console

     cd yourname-packages


In order to obtain the neccessary files, do:

.. code-block:: console

     git clone git@github.com:quarkyjordan/JobSubmission.git

Now, type **ls** to make sure the git clone has worked. In order to make this package visible from anywhere in your workspace, add the line:


.. code-block:: bash
   
   export PYTHONPATH=/path/to/dir:$PYTHONPATH
     

into your **.profile** or **bashrc** file. To open these files do:

.. code-block:: console

   emacs -nw ~/.profile

or 

.. code-block:: console

   emacs -nw ~/.bashrc

Now, you should be ready to go!

Please follow the contact information if any of this doesn't work.
