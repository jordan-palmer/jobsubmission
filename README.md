# JobSubmission
Python job submission scripts
Things to include
Python scripts

- add small wait if qsub called multiple times
- function that searches for a string and replaces all instances of it (can be called multiple times) string_replace(stringtobereplaced, replacementstring, macro) would need to produce new macro everytime this happens so qsub works on it
- function that produces new directories
- clean up function that removes all new .sh and .C files in the case of a break
- Make it so someone can run an executable command with different sets of arguments in one go
- Make new dir for macros, .sh scripts etc
