from Bio import Entrez

from pygooglechart import SimpleLineChart
from pygooglechart import Axis

def parseseq(s):
    index = s.find('ORIGIN')
    aaseq = []
    #return index
    for c in s[index:]:
        if c.islower():
            aaseq.append(c)
    return aaseq

class region:
    def __init__(self, start, end, title):
        self.start = start
        self.end = end
        self.title = title

def parsesheet(s, key, title):
    index = s.find(key)
    regions = []
    while index != -1:
        print 'ping', index, len(s)
        s = s[index+1:]
        doubleindex = s.find("..")
        #find before number
        i = 1
        start = ''
        while s[doubleindex-i].isdigit():
            start = s[doubleindex-i] + start
            i += 1
        #find after number
        i = 2
        end = ''
        while s[doubleindex+i].isdigit():
            end = end + s[doubleindex+i]
            i += 1
        #find type
        titleindex = s.find(title + '="')
        if titleindex != -1:
            s = s[titleindex+len(title+'="'):]
            endquoteindex = s.find('"')
            regiontitle = s[0:endquoteindex]
            
        temp = region(start, end, regiontitle)
        regions.append(temp)
        index = s.find(key)
    print regions
    return regions

def makechart(aaseq, regions):
    hdph = dict()
    hdph['d'] = -3.5
    hdph['e'] = -3.5
    hdph['k'] = -3.9
    hdph['r'] = -4.5
    hdph['h'] = -3.2
    hdph['y'] = -1.3
    hdph['w'] = -0.9
    hdph['f'] = 2.8
    hdph['c'] = 2.5
    hdph['m'] = 1.9
    hdph['s'] = -0.8
    hdph['t'] = -0.7
    hdph['n'] = -3.5
    hdph['q'] = -3.5
    hdph['g'] = -0.4
    hdph['a'] = 1.8
    hdph['v'] = 4.2
    hdph['l'] = 3.8
    hdph['i'] = 4.5
    hdph['p'] = -1.6
    hdphseq = []
    for i in range(len(aaseq)):
        hdphseq.append(hdph[aaseq[i]])
    
    min_y = -5
    max_y = 5
    chart = SimpleLineChart(2, 2, y_range=[min_y, max_y])
    
    #chart.add_data([max_y]*2)
    chart.add_data(hdphseq)   
    #chart.add_data([min_y]*2)
    chart.set_axis_labels(Axis.BOTTOM, aaseq)
    
    chart.download('test.png')
    
    #print hdphseq
    return hdphseq


Entrez.email = 'pconerly@gmail.com'
handle = Entrez.esearch(db="protein", retmax=10, term="fluorescent")
record = Entrez.read(handle)
print record["Count"]
print record["IdList"]
print


#finds all DBs
#record = Entrez.read(Entrez.einfo())
#print record['DbList']

for i in range(1):
    spechandle = Entrez.efetch(db="protein", id=record['IdList'][i], rettype='gb', retmode='text')
    test = spechandle.read()
    print i, test 
    print "type is: ", type(test)
    aaseq = parseseq(test)
    print "origin index is", aaseq
    print "sheets are at", 
    regions = parsesheet(test, 'Region', 'region_name')
    for i in range(len(regions)):
        print regions[i].start, regions[i].end, regions[i].title

    makechart(aaseq, regions)


