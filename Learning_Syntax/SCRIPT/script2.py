from script1 import *

print(__name__) # This time around reversed
'''
It will first run print in script1 as it was imported, which will output
the module/file name "script1"

Then after

It will run print in this module/file which will print "__main__"
'''