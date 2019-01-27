import JobSub as job
from JobSub import *

#sourceDir,workDir,cmd,jobName,inFile
inFile="text.txt"
source = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/setup.sh"
workdir = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/"
command = "build.x86_64-slc6-gcc48-opt/bin/BACCARATExecutable"
myfile = "LEDTEST.mac"
errorfile = "errfile.txt"
logfile ="logfile.txt"

x = jobSubmitter(source,workdir,command,"PythonTEST",myfile)
jobSubmitter.writeJobBash(x)
jobSubmitter.jobSubmit(x,errorfile,logfile)
#jobSubmitter.searRep(x,"test","message")