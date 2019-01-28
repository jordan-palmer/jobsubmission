import os
import subprocess as sub

class jobSubmitter(object):

    def __init__(self,sourceDir,workDir,cmd,jobName,inFile):
        #Constructer - set member variables here
        self.sourceDir = sourceDir
        self.workDir = workDir
        self.cmd = cmd
        self.jobName = jobName
        self.inFile = inFile

    def searRep(self, ToReplace, Replacement, filetoedit):
        #temp1 = str(random_with_N_digits(3))                            
        os.chdir(self.workDir)
        ToReplace = str(ToReplace)
        Replacement = str(Replacement)
#        it = str(filetoedit.replace(".*
        temp = str(filetoedit.replace(".mac","2.mac"))
        f1 = open(self.inFile, 'r')
        f2 = open(temp, 'w')
        for line in f1:
            f2.write(line.replace(ToReplace, Replacement))
            #f1.close()
            #f2.close()
        return temp

    def writeJobBash(self):
        #Function that writes a shell script to a file which will be qsubbed 
        filetouse = self.searRep("/Bacc/source/set LEDPhotons TPCtop 1 1000","/Bacc/source/set LEDPhotons TPCtop 2 1000")
        #newinfile = open(filetouse,"r")
        f = open(self.jobName,"w+")
        line1 = "#!/bin/bash"
        line2 = "cd" + " " + self.workDir
        line3 = "source" + " " + self.sourceDir
        line4 = "echo sourced config"
        line5 = "cd" + " " + self.workDir
        line6 = "./" + self.cmd + " " + filetouse
        #This line writes the lines in a column 
        f.write('%s\n%s\n%s\n%s\n%s\n%s\n'%(line1,line2,line3,line4,line5,line6))


    def jobSubmit(self,err_file, log_file):
        #Function to qsub jobs 
        os.system("chmod +x" + " " + self.jobName)
        sub.call(["qsub","-q","long","-l","pvmem=8gb","-o",log_file,"-e",err_file, self.jobName])
        #sub.call(["./"+jobName])

    def random_with_N_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

            



#inFile = "test.txt"
#SearchReplace("test","message")

#jobName = "jobname8_testlocal.sh" 
#writeJobBash("","","run.mac","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/setup.sh",jobName)

#jobSubmit("c_err","d_log", jobName)


#inFile = "text.txt"

    
