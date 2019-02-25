#============================================================================#                                                                  
#JobSub class                  -  Updated : Jordan Palmer : 24-02-19         #                                                                                
#============================================================================#                                                                              
# This is the main jobSubmitter class. Edit your own version of this if      #
# you wish; however, make sure you update the version in your python         #
# path.                                                                      #
# Documentation : http://www.pp.rhul.ac.uk/~jpalmer/jobsubmissions/index.html#
#----------------------------------------------------------------------------#
# __init__ : Constructor which creates directories                           #                                                                       
# writeJobBash: Function that writes a shell script to be run on the farm    #                                                                              
# jobSubmit: Submits job to the farm using qsub                              #
#============================================================================#

import os
import subprocess as sub

class jobSubmitter(object):
    
    def __init__(self, source, jobName, cmd, inFile, workDir = "./", jobDirName=None):
        # Constructer - set member variables here
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
       
        if not os.path.exists(self.jobDirName):
            os.makedirs(self.jobDirName)
        shScript = "/shellScripts"
        if not os.path.exists(self.jobDirName + shScript):
            os.makedirs(self.jobDirName + shScript)
        self.jobScript = self.jobDirName + shScript + "/" + self.jobName + ".sh"
        inputfiles = "/inputFiles"
        if not os.path.exists(self.jobDirName+inputfiles):
            os.makedirs(self.jobDirName+inputfiles)
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
        print "-------------------------------------------------------------"

    def writeJobBash(self):
        #Function that writes a shell script to a file which will be qsubbed. Includes running on the node!
        f = open(self.jobScript, "w+")
        MainString = "#!/bin/sh \necho \"PBS Job ID  = \"$PBS_JOBID \nsource {0} \necho sourced config \nJOBDIR=/data/$USER/job_$PBS_JOBID \nmkdir -p $JOBDIR \ncd $JOBDIR \necho This is the directory = $PWD \ntrap \"cp $JOBDIR/* {1}/. ; rm -rf $JOBDIR; exit;\" SIGTERM SIGINT SIGHUP \n{2} {3} \necho \"job finished\" \ndate \necho \"we are in =\" $PWD \ncp $JOBDIR/* {4}/. \necho {4}\nif [ $? != 0 ]; then \n\techo \"copy failed\" \n\texit 1 \nfi \nrm -rf $JOBDIR \nif [ $? == 0 ]; then \n\t echo \"tidied up files on node\" \nfi" 
        f.write(MainString.format(self.source, self.jobDirName, self.cmd, self.inFile, self.jobDirName))
        
    def jobSubmit(self,err_file = None ,log_file = None, queue = "medium", memory = "4GB", shellScript = None):
        #Function to qsub jobs 
        print "-------------------------------------------------------------"
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
            sub.call(["qsub", "-q", queue, "-l", "pvmem="+memory, "-o", self.err_outFiles, "-jo e", self.jobScript])
            print "Job submitted"
        else :
            print "Job submitted with seperate log and error files"
            sub.call(["qsub", "-q", queue, "-l", "pvmem="+memory, "-o", self.err_outFiles + "/" + log_file, "-e", self.err_outFiles + "/" + err_file, shellScript])

