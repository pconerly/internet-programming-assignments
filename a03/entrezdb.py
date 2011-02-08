from Bio import Entrez

Entrez.email = 'pconerly@gmail.com'
#handle = Entrez.esearch(db="protein", retmax=10, term="cerevisiae")


for edb in ['protein', 'gene', 'nucleotide']:
    handle = Entrez.esearch(db=edb, retmax=10, term='"Saccharomyces cerevisiae"[porgn:__txid4932]')
    record = Entrez.read(handle)
    print edb, "search============="
    print 'count', record["Count"]
    print 'idlist', record["IdList"]


