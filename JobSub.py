import os
import subprocess as sub

class jobSubmitter(object):
    
    def __init__(self,source,jobName,cmd,inFile,workDir = "./",jobDirName = None):
        #Constructer - set member variables here
        self.source = source
        self.workDir = workDir
        self.cmd = cmd
        
        if(jobDirName == None):
            self.jobDirName = self.workDir + "/" + jobName
        else:
            self.jobDirName =  jobDirName
        
        self.jobName = jobName
       
        
        self.inFile = inFile

        self.tempfile = inFile

        #self.jobDirName = self.workDir + "/" + self.jobName #jobDir = new directory for output
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

        print "source: " + self.source 
        print "jobName:  " + self.jobName 
        print "cmd: " + self.cmd 
        print "inFile:  " + self.inFile 
        print "workDir " + self.workDir 
        print "jobDirName:  " + self.jobDirName
        print "----------------------------------------------------"
    def writeJobBash(self):
        #Function that writes a shell script to a file which will be qsubbed 
        f = open(self.jobScript,"w+")
        
        
        

# prepare cleanup trap
        


        line1 = "#!/bin/bash"
        line2 =  "echo \"PBS Job ID  = \"$PBS_JOBID"
        line3 = "source" + " " + self.source              #"cd" + " " + self.workDir
        line4 = "echo sourced config"
        line5 = "JOBDIR=/data/$USER/job_$PBS_JOBID"
        line6 = "mkdir -p $JOBDIR"
        line7 = "cd $JOBDIR"
        line8 = "trap \"cp $JOBDIR/* " + self.jobDirName + "/. ; rm -rf $JOBDIR; exit;\" SIGTERM SIGINT SIGHUP"
        line9 =  self.workDir+"/" + self.cmd + " " + self.inFile
        line10 = "echo \"job finished\""
        line11 = "date"
        line12 = "cp $JOBDIR/* " + self.jobDirName + "/."
        line13 = "if [ $? != 0 ]; then"
        line14 = "\techo \"copy failed\""
        line15 = "\texit 1"
        line16 = "fi"
        # clean up temporary files
        line17 = "rm -rf $JOBDIR"
        line18 = "if [ $? == 0 ]; then"
        line19 = "\t echo \"tidied up files on node\""
        line20 = "fi"

        #This line writes the lines in a column 
        f.write('%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n'%(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,line20))


    def jobSubmit(self,err_file = None ,log_file = None, queue = "medium", memory = "4GB", shellScript = None):
        #Function to qsub jobs 
        print "-----------------------------------"
        if(err_file == None):
            err_File = self.jobName + "_err"
        
        if(log_file == None):
            log_file = self.jobName + "_log"

        if(shellScript == None):
            shellScript = self.jobScript
        
        
        print err_file +"\t" + log_file + "\t" + queue + "\t" + memory 
        print shellScript
        os.system("chmod +x" + " " + self.jobScript)
        
        if(err_file == log_file):
            sub.call(["qsub","-q",queue,"-l","pvmem="+memory,"-o",self.err_outFiles,"-jo e", self.jobScript])
            print "Job submitted"
        else :
            print "Job submitted with seperate log and error files"
            sub.call(["qsub","-q",queue,"-l","pvmem="+memory,"-o",self.err_outFiles + "/" + log_file,"-e", self.err_outFiles + "/" + err_file, shellScript])
        #sub.call(["./"+jobName])
        
    

    def jobCleanUp():
        sub.call(["rm",self.jobScript])

#jobName = "jobname8_testlocal.sh" 
#writeJobBash("","","run.mac","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/","/cvmfs/lz.opensciencegrid.org/DER/release-8.1.5/x86_64-slc6-gcc48-opt/setup.sh",jobName)

#jobSubmit("c_err","d_log", jobName)


        
    
