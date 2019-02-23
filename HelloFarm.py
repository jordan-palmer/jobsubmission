import jobsubmission.JobSub
from jobsubmission.JobSub import *

source = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/setup.sh"  #environment you want to source
workdir = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT"    #working directory in this form!
command = "echo 'hello farm' >> "   #command you want to run, eg 'root -l' 
myfile = "HelloFarm.txt"   #input file, file you act command on
errorfile = "errfile_hello.txt"   #error file
logfile ="logfile_hello.txt"   #log file
#jobdirname = "HelloFarmDir"  #directory in which you want your job to run in 
jobname = "HelloFarm"   #jobname 
joblength = "short" #Sets the allocated time: long=500hours, medium=20hours, short=20mins
jobmemory = "500mb" #sets allocated memory. Make sure you choose the lowest memory possible!

x = jobsubmission.jobSubmitter(source,"HELLOWORLD",command, myfile,workdir) #object of the class
jobsubmission.jobSubmitter.writeJobBash(x) #creates .sh script to be run on farm
jobsubmission.jobSubmitter.jobSubmit(x,errorfile,logfile,joblength,jobmemory) #qsubs on farm



#x = jobsubmission.jobSubmitter(source,"TESTDIR", command, myfile, workdir)
#jobsubmission.jobSubmitter.writeJobBash(x)
#jobsubmission.jobSubmitter.jobSubmit(x,errorfile,logfile,"medium","4gb") 
