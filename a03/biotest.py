from Bio import Entrez

Entrez.email = 'pconerly@gmail.com'
handle = Entrez.esearch(db="nucleotide", retmax=10, term="Opuntia")
record = Entrez.read(handle)
print record["Count"]
print record["IdList"]
print


#finds all DBs
#record = Entrez.read(Entrez.einfo())
#print record['DbList']

for i in range(3):
    spechandle = Entrez.efetch(db="nucleotide", id=record['IdList'][i], rettype='gb')
    print i, spechandle.read()
    print


