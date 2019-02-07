import os
import subprocess as sub

class jobSubmitter(object):

    def __init__(self,source,workDir,cmd,jobName,inFile):
        #Constructer - set member variables here
        self.source = source
        self.workDir = workDir
        self.cmd = cmd
        self.jobName = jobName
        self.inFile = inFile

        self.jobDir = self.workDir + "/" + self.jobName #jobDir = new directory for output
        sub.call(["echo", self.jobDir])

        if not os.path.exists(self.jobDir):
            os.makedirs(self.jobDir)
        shScript = "/shellScripts"
        if not os.path.exists(self.jobDir + shScript):
            os.makedirs(self.jobDir + shScript)

        self.jobScript = self.jobDir + shScript + "/" + self.jobName + ".sh"
    
    def writeJobBash(self):
        #Function that writes a shell script to a file which will be qsubbed 
        f = open(self.jobScript,"w+")
        line1 = "#!/bin/bash"
        line2 = "cd" + " " + self.workDir
        line3 = "source" + " " + self.source
        line4 = "echo sourced config"
        line5 =  self.cmd + " " + self.inFile
        #This line writes the lines in a column 
        f.write('%s\n%s\n%s\n%s\n%s\n'%(line1,line2,line3,line4,line5))


    def jobSubmit(self,err_file, log_file, length, memory):
        #Function to qsub jobs 
        os.system("chmod +x" + " " + self.jobName)
        sub.call(["qsub","-q",length,"-l","pvmem="+memory,"-o",log_file,"-e",err_file, self.jobScript])
        #sub.call(["./"+jobName])

    def jobCleanUp():
        sub.call(["rm",self.jobScript])

#jobName = "jobname8_testlocal.sh" 
#writeJobBash("","","run.mac","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/setup.sh",jobName)

#jobSubmit("c_err","d_log", jobName)


        
    
