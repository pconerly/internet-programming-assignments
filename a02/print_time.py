
from datetime import *

def print_time():
    monthBuff = ""
    dayBuff = ""
    theDate = datetime.today()
    if theDate.month < 10:
        monthBuff = '0'
    if theDate.day < 10:
        dayBuff = '0'
    today = '%d/%s%d/%s%d'%(theDate.year,monthBuff,theDate.month,dayBuff,theDate.day)    

    print "Today's date: %s" % today

print_time()
