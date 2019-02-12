import os
import subprocess as sub

class jobSubmitter(object):

    def __init__(self,source,jobName,cmd,inFile,workDir = "./",jobDirName = False):
        #Constructer - set member variables here
        self.source = source
        self.workDir = workDir
        self.cmd = cmd
        
        if(jobDirName == False):
            self.jobDirName = jobName
        else:
            self.jobDirName = jobDirName
        self.jobName = jobName
       
        
        self.inFile = inFile

        self.tempfile = inFile

        self.jobDirName = self.workDir + "/" + self.jobName #jobDir = new directory for output
        #sub.call(["echo", self.jobDir])
        if not os.path.exists(self.jobDirName):
            os.makedirs(self.jobDirName)
        
        shScript = "/shellScripts"
        if not os.path.exists(self.jobDirName + shScript):
            os.makedirs(self.jobDirName + shScript)
        self.jobScript = self.jobDirName + shScript + "/" + self.jobName + ".sh"

        inputfiles = "/inputFiles"
        if not os.path.exists(self.jobDirName+inputfiles):
            os.makedirs(self.jobDirName+inputfiles)
        self.inputFilesDir = self.jobDirName+inputfiles
#        sub.call(["cp","./"+inFile+"/",self.inputFilesDir])                                                                                                                                               

        eoFiles = "/eoFiles"
        if not os.path.exists(self.jobDirName+eoFiles):
            os.makedirs(self.jobDirName+eoFiles)
        self.err_outFiles = self.jobDirName+eoFiles

        print "created submmitter object"

        print self.source + " " + self.jobName + " " + self.cmd + " " + self.inFile + " " + self.workDir + " " + self.jobDirName
        sub.call(["echo","testing"])
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


    def jobSubmit(self,err_file = False ,log_file = False, queue = "medium", memory = "4GB", shellScript = False):
        #Function to qsub jobs 
        print "entered function"
        if(err_file == False):
            err_File = self.jobName + "_err"
        
        if(log_file == False):
            log_file = self.jobName + "_log"

        if(shellScript == False):
            shellScript = self.jobScript
        
        print "here"
        print err_file +"\t" + log_file + "\t" + queue + "\t" + memory 
        print self.jobScript
        os.system("chmod +x" + " " + self.jobScript)
        
        if(err_file == log_file):
            sub.call(["qsub","-q",queue,"-l","pvmem="+memory,"-o",self.err_outFiles,"-jo e", self.jobScript])
            print "will now submit job"
        else :
            print "will now submit job with seperate log and error files"
            sub.call(["qsub","-q",queue,"-l","pvmem="+memory,"-o",self.err_outFiles + "/" + log_file,"-e", self.err_outFiles + "/" + err_file, shellScript])
        #sub.call(["./"+jobName])
        
    

    def jobCleanUp():
        sub.call(["rm",self.jobScript])

#jobName = "jobname8_testlocal.sh" 
#writeJobBash("","","run.mac","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/setup.sh",jobName)

#jobSubmit("c_err","d_log", jobName)


        
    
