import csv

compound_dict = {}

with open('./L6810-Traditional Chinese Medicine Monomer Library-2910cpds.csv', encoding = 'utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        compound_dict[row['PubChem CID']] = row['Name']

def find_compound_name_by_cid(cid):
    return compound_dict.get(str(cid), None)