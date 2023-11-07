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
