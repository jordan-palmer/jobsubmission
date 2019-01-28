import JobSub as job
from JobSub import *

#sourceDir,workDir,cmd,jobName,inFile
inFile="text.txt"
source = "/scratch1/darkmatter/ds20k/g4ds10_reBuild_1218/configDarkSide.sh"
#source = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/setup.sh"
workdir = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT"
command = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/build.x86_64-slc6-gcc48-opt/bin/BACCARATExecutable"
myfile = "LEDTEST.mac"
errorfile = "errfile.txt"
logfile ="logfile.txt"

x = jobSubmitter(source,workdir,command,"PythonTEST",myfile)
jobSubmitter.writeJobBash(x)
jobSubmitter.jobSubmit(x,errorfile,logfile)
#jobSubmitter.searRep(x,"test","message")

#source1 = "/scratch1/darkmatter/ds20k/g4ds10_reBuild_1218/configDarkSide.sh"
#wkDir = "/scratch1/darkmatter/ds20k/g4ds10_reBuild_1218/Linux-g++"
#cmd = "g4ds"
#myfile1 = "run.mac"

#y = jobSubmitter(source1,wkDir,cmd,"TestJob5", myfile1)
#jobSubmitter.writeJobBash(y)
#jobSubmitter.jobSubmit(y,errorfile,logfile) 
