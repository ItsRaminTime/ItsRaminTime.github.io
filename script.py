import json
data = json.load(open("receptor_protein_translator.json"))
codes = [x["pdb_code"] for x in data]

for code in codes:
	from subprocess import call
	call(["wget", "https://files.rcsb.org/view/%s.pdb" % code])
