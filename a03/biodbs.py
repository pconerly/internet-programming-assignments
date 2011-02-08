from Bio import Entrez

Entrez.email = 'pconerly@gmail.com'


#finds all DBs
record = Entrez.read(Entrez.einfo())
print record['DbList']

