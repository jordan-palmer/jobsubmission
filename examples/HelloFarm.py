#=====================================================================#                                       
#HelloFarm                  -  Updated : Jordan Palmer : 24-02-19     #          
#=====================================================================#                                                                           
#Simple HelloFarm job submission script example.                      #                                                                   
# 1. Creates an object of the class (x)                               #                                                                                 
# 2. Writes a shell script                                            #                                                                         
# 3. Submits job on the farm                                          #                                                                                  
# Edit the variables below in the same format                         #
# This program writes 'Hello Farm' to a text file. This should be used#
# to test that your code runs                                         #                                                              
#=====================================================================#

import jobsubmission.JobSub as _job
#from jobsubmission.JobSub import *

source = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/setup.sh"  #environment you want to source
workdir = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT"    #working directory in this form!
command = "echo 'hello farm' >> "   #command you want to run, eg 'root -l' 
myfile = "HelloFarm.txt"   #input file, file you act command on
errorfile = "errfile_hello.txt"   #error file
logfile ="logfile_hello.txt"   #log file
jobname = "HelloFarm"   #jobname 
joblength = "short" #Sets the allocated time: long=500hours, medium=20hours, short=20mins
jobmemory = "500mb" #sets allocated memory. Make sure you choose the lowest memory possible!

_self = _job.jobSubmitter(source,"HELLOWORLD",command, myfile,workdir) #object of the class
_self.writeJobBash()
_self.jobSubmit(errorfile,logfile,joblength,jobmemory)
