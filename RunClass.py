import jobsubmission.JobSub 
from jobsubmission.JobSub import *

inFile="text.txt"
source = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/setup.sh"
workdir = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/outputfiles/Na22data"
command = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/build.x86_64-slc6-gcc48-opt/bin/BaccMCTruth"
myfile = "lz_mdc3_Na22_JP_100_ALL_2.root"
errorfile = "errfile.txt"
logfile ="logfile.txt"
shellname = "LEDTEST"
jobdirname = "RootTOMCTruthNa22"

x = jobsubmission.jobSubmitter(source,workdir,command,"RootToMCTruthNa22",myfile)
jobsubmission.jobSubmitter.writeJobBash(x)
jobsubmission.jobSubmitter.jobSubmit(x,errorfile,logfile,"long","8gb")
