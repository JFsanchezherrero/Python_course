# Final integrative exercise

## Subset data
Create a subset some entries from chr1: 215 entries from 0 - 46 Mb

Using linux and the GRCh38 and Ensembl annotation v108, I subsetted some entries and generated a csv file.

```
head -10000 Homo_sapiens.GRCh38.108.chr.gtf \
		awk '{if ($3=="gene"){print $0}}' \
		awk '{print "chr1,"$4","$5","$7","$10","$14","$NF}' 
		sed 's/"//g' | sed 's/;//g' | sed 's/havana//' | sed 's/_tagene//' > chr1_annot.csv 
```

## Sort 
I sort the contents of the file in a numeric way using starting position for each entry.

```
# sort
sort -n -k2 -t, > chr1_annot.csv
```

## Add header
Then, I manually add a header to the csv file: `chr,start,stop,strand,ensembl_ID,gene_name,biotype`

As an example:
```
chr,start,stop,strand,ensembl_ID,gene_name,biotype
chr1,182696,184174,+,ENSG00000279928,DDX11L17,unprocessed_pseudogene
chr1,185217,195411,-,ENSG00000279457,WASH9P,unprocessed_pseudogene
chr1,187891,187958,-,ENSG00000273874,MIR6859-2,miRNA
chr1,257864,359681,-,ENSG00000228463,,transcribed_processed_pseudogene
chr1,266855,268655,+,ENSG00000286448,,lncRNA
chr1,516376,516479,-,ENSG00000278757,U6,snRNA
```


### example.py

#!/usr/bin/env python3
import sys
import pandas as pd

fasta_file = sys.argv[1]
annot_file = sys.argv[2]

with open(fasta_file,'r') as reader:
    contents_file = reader.readlines()

## read fasta
fasta_header = contents_file[0]
fasta_seq = "".join(contents_file[1:])
fasta_seq = fasta_seq.replace("\n","")

## read annot
annot_df = pd.read_csv(annot_file, header=0)

## select random entry
import random
rnd_el = random.choice(range(len(annot_df)))

start_pos = annot_df.loc[rnd_el,'start']
stop_pos = annot_df.loc[rnd_el,'stop']

print(fasta_seq[annot_df.loc[rnd_el,'start']:annot_df.loc[rnd_el,'stop']])

