import sys  
import time  
import myModule
# Output example: [=======   ] 75%  
# width defines bar width  
# percent defines current percentage  
 
def progress(width, percent):  
    print "%s %d%%\r" % (('%%-%ds' % width) % (width * percent / 100 * '='), percent)
    if percent >= 100:  
        print  
        sys.stdout.flush()  
# Simulate doing something ...  
for i in xrange(100):  
    progress(100, (i + 1))  
    time.sleep(1) # Slow it down for demo  

