# JobSubmission
COLLABORATORS, PLEASE UPDATE
Python job submission scripts
Things to include
Python scripts

- add small wait if qsub called multiple times
- clean up function that removes all new .sh and .C files in the case of a break
- Make it so someone can run an executable command with different sets of arguments in one go


1. git clone repository 
2. include this line in .profile or .bashrc 
    export PYTHONPATH=/path/to/dir:$PYTHONPATH
3. recommend mkdir yourname-packages, so you have 
    export PYTHONPATH=/path/to/yourname-packages:$PYTHONPATH
4. Now, one can access the package anywhere! Simply add 
    import jobsubmission.JobSub
    from jobsubmission.JobSub import *
  to your python script. 
5. to make an object of the jobSubmitter class, now do:
    x = jobsubmission.jobSubmitter(par1,par2,....)
    
Documentation:

http://www.pp.rhul.ac.uk/~jpalmer/jobsubmissions/index.html

