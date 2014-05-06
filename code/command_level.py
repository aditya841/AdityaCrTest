import sys
import traceback

class PyCodeFile:    
    def __init__(self, file_object):
        try:
            self.lines_counter = 0
            self.comments_counter = 0                       
            for line in file_object:                
                strip_line = line.strip()
                if len(strip_line) > 0 and strip_line[0] == '#':
                    self.comments_counter+=1
                self.lines_counter+=1            
        except:
            print "Error in PyCodeFile"
            print traceback.print_exc()
        return None
            
    def comments(self):
        return self.comments_counter

    def non_comments(self):
        return self.lines_counter - self.comments_counter

    def ratio(self):
        try:            
            return self.comments() * 1.0 / self.non_comments()
        except ZeroDivisionError:
            return "No non comments line"
