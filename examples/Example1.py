#=====================================================================#
#Example 1                  -  Updated : Jordan Palmer : 24-02-19     #
#=====================================================================#
#Simple job submission script example.                                #
# 1. Creates an object of the class (x)                               #
# 2. Writes a shell script                                            #
# 3. Submits job on the farm                                          #
# Edit the variables below in the same format                         #
#=====================================================================#

import jobsubmission.JobSub as _job
#from jobsubmission.JobSub import *

source = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/setup.sh" #Full path to environment you would like to source 
workdir = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT" #Working directory, where job directory will be created
command = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/build.x86_64-slc6-gcc48-opt/bin/BaccRootConverter" #command of job, i.e "./executable" , "root -l" 
myfile = "lz_mdc3_Na22_JP_100_1003951237.bin" #Target file you wish to act 'command' on
errorfile = "errfile.txt" #Name of error file
logfile = "logfile.txt" #name of log file

# 1
_self = _job.jobSubmitter(source,"EXAMPLE1",  
                          command, myfile, workdir)
# 2
_self.jobSubmitter.writeJobBash() 
# 3
_self.jobSubmit(errorfile,
                logfile,"medium","4gb")
