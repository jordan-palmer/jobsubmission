import jobsubmission.JobSub 
from jobsubmission.JobSub import *

inFile="text.txt"
source = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/setup.sh"
#workdir = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT"
workdir = "/hadoop/data/jpalmer/outputfiles/TPCtopsimdata/"
command = "/scratch3/jpalmer/PhD/JP-LEDs2/BACCARAT/build.x86_64-slc6-gcc48-opt/bin/BaccMCTruth"
myfile = "/hadoop/data/jpalmer/outputfiles/TPCtopsimdata/lz_mdc2_TPCtop_100_5000_JP_1004367627.root"
#myfile = "lz_mdc3_Na22_JP_100_ALL_2.root"
errorfile = "errfile.txt"
logfile ="logfile.txt"
shellname = "LEDTEST"
jobdirname = "RootTOMCTruthNa22"
#source,"shelltest",command,myfile,workdir

x = jobsubmission.jobSubmitter(source,"TESTDIR", command, myfile, workdir)
jobsubmission.jobSubmitter.writeJobBash(x)
jobsubmission.jobSubmitter.jobSubmit(x,errorfile,logfile,"medium","4gb")
