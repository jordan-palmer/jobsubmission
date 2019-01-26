import os
import subprocess as sub

class jobSubmitter(object):

    def __init__(self,sourceDir,workDir,cmd,jobName):
        #Constructer - set member variables here
        self.sourceDir = sourceDir
        self.workDir = wowrkDir
        self.cmd = cmd
        self.jobName = jobName

    def writeJobBash(self,inFile):
        #Function that writes a shell script to a file which will be qsubbed 
        f = open(self.jobName,"w+")
        line1 = "#!/bin/bash"
        line2 = "cd" + " " + self.workDir
        line3 = "source" + " " + self.sourceDir
        line4 = "echo sourced config"
        line5 = "cd" + " " + cmdDir
        line6 = "../" + self.cmd + " " + inFile
        #This line writes the lines in a column 
        f.write('%s\n%s\n%s\n%s\n%s\n%s\n'%(line1,line2,line3,line4,line5,line6))


    def jobSubmit(err_file, log_file):
        #Function to qsub jobs 
        os.system("chmod +x" + " " + self.jobName)
        sub.call(["qsub","-q","long","-l","pvmem=8gb","-o",log_file,"-e",err_file, self.jobName])
        #sub.call(["./"+jobName])


jobName = "jobname8_testlocal.sh" 
writeJobBash("","","run.mac","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/setup.sh",jobName)

jobSubmit("c_err","d_log", jobName)


        
    
