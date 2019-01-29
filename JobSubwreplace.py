import os
import subprocess as sub
from random import randint


class jobSubmitter(object):

    def __init__(self,source,workDir,cmd,jobName,inFile):
        #Constructer - set member variables here
        self.source = source
        self.workDir = workDir
        self.cmd = cmd
        self.jobName = jobName
        self.inFile = inFile
        
        #set up file system - by default all in-files in relation to workDir and all outputs placed into newly created directory                                                   
        self.jobDir = self.workDir + "/" + self.jobName #jobDir = new directory for output                                                                                 
        sub.call(["echo", self.jobDir])
        if not os.path.exists(self.jobDir):
            os.makedirs(self.jobDir)
        shScript = "/shellScripts"
        if not os.path.exists(self.jobDir + shScript):
            os.makedirs(self.jobDir+"Dir" + shScript)
        self.jobScript = self.jobDir+"Dir" + shScript + "/" + self.jobName + ".sh"

    def random_with_N_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    def searchReplace(self, ToReplace, Replacement, filetoedit, extension):
        #temp1 = str(random_with_N_digits(3))                            
        os.chdir(self.workDir)
        dotchar = filetoedit.rfind(".")
        length = len(filetoedit)
        charnum = length - dotchar
        z = ""
        for i in range(dotchar,length,1):
            z = z + filetoedit[i]
        print z      
        if extension == "date":
            date = strftime("-%Y-%d-%m-%H:%M:%S", gmtime())
            tempfile = filetoedit.replace(z,date+z)   
        elif extension == "rand":
            tempfile = filetoedit.replace(z,random_with_N_digits(3)+z)
        else:
            tempfile = filetoedit.replace(z,extension+z)
        
        print tempfile
        f1 = open(self.inFile, 'r')
        f2 = open(tempfile, 'w')
        for line in f1:
            f2.write(line.replace(ToReplace, Replacement))
            #f1.close()
            #f2.close()
        return tempfile

    def writeJobBash(self, shellName, filetorun):
        #Function that writes a shell script to a file which will be qsubbed 
#        filetouse = self.searchReplace("/Bacc/source/set LEDPhotons TPCtop 1 1000","/Bacc/source/set LEDPhotons TPCtop 2 1000")
        #newinfile = open(filetouse,"r")
        f = open(shellName,"w+")
        line1 = "#!/bin/bash"
        line2 = "cd" + " " + self.workDir
        line3 = "source" + " " + self.source
        line4 = "echo sourced config"
        line5 = self.cmd + " " + filetorun#self.inFile
        #This line writes the lines in a column 
        f.write('%s\n%s\n%s\n%s\n%s\n'%(line1,line2,line3,line4,line5))


    def jobSubmit(self,err_file, log_file):
        #Function to qsub jobs 
        os.system("chmod +x" + " " + self.jobName)
        sub.call(["qsub","-q","long","-l","pvmem=8gb","-o",log_file,"-e",err_file, self.jobName])
        #sub.call(["./"+jobName])




#inFile = "test.txt"
#SearchReplace("test","message")

#jobName = "jobname8_testlocal.sh" 
#writeJobBash("","","run.mac","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/setup.sh",jobName)

#jobSubmit("c_err","d_log", jobName)


#inFile = "text.txt"

    
