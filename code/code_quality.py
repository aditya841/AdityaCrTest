import glob
import sys
import command_level
import traceback

def scan_folder(dir_path):
    try:
        total_comments_counter = 0
        total_non_comments_counter = 0
        print "Got the path. Scanning Dir....."        
        file_list = glob.glob(dir_path + "\*.py")
        for file1 in file_list:            
            pyfileob = command_level.PyCodeFile(open(file1, 'rU'))
            print file1.split('\\')[-1]
            print "Comments: " + str(pyfileob.comments())
            print "Ratio(Comments / Non_Comments): " + str(pyfileob.ratio())
            print 
            total_comments_counter+= pyfileob.comments()
            total_non_comments_counter+= pyfileob.non_comments()

        print "Totals: "
        print total_comments_counter
        print total_non_comments_counter
    except:
        print "Error in scan folder"
        print traceback.print_exc()
