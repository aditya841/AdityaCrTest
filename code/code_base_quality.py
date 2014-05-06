import sys
import os
import code_quality

try:
    print "Starting the program"    
    if os.path.isdir(sys.argv[1]):        
        code_quality.scan_folder(sys.argv[1])
    else:
        print "It is not a directory"
except IndexError:
    print "You did not provide any directory"
    sys.exit(1)
except:
    print sys.exc_info()[0]
