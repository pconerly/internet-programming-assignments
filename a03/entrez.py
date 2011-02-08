from Bio import Entrez

Entrez.email = 'pconerly@gmail.com'
#handle = Entrez.esearch(db="protein", retmax=10, term="cerevisiae")
handle = Entrez.esearch(db="protein", retmax=10, term='"Saccharomyces cerevisiae"[porgn:__txid4932]')
record = Entrez.read(handle)
print 'count', record["Count"]
print 'idlist', record["IdList"]
print 'translation stack', record["TranslationStack"]
print 'return start', record["RetStart"]
print 'term', record["TranslationStack"][0]["Term"]
print 'query translation', record["QueryTranslation"]
print record


#finds all DBs
#record = Entrez.read(Entrez.einfo())
#print record['DbList']

for i in range(1):
    spechandle = Entrez.efetch(db="protein", id=record['IdList'][i], rettype='gb', retmode='xml')
    print i#, spechandle.read()
    print
    for j in range(10):
        h = Entrez.parse(spechandle)
        print h
    print "========================================================"
    print spechandle.read()

    #spechandle = Entrez.efetch(db="protein", id=record['IdList'][i], rettype='gb', retmode='text')
    #print i, spechandle.read()
    print



