import JobSubwreplace as job
from JobSubwreplace import *

source = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/setup.sh"  #environment you want to source
workdir = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT"    #working directory in this form!
command = "echo 'hello farm' >> "   #command you want to run
myfile = "HelloFarm.txt"   #input file
errorfile = "errfile_hello.txt"   #error file
logfile ="logfile_hello.txt"   #log file
jobdirname = "HelloFarmDir"  #direcory in which you want your job to run in 
jobname = "HelloFarm"   #jobname 
 
x = jobSubmitter(source,workdir,command,jobdirname,jobname,myfile)
jobSubmitter.writeJobBash(x,myfile)
jobSubmitter.jobSubmit(x,errorfile, logfile)
