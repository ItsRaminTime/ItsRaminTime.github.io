import json
data = json.load(open("../table.json"))
codes = [x["pdb"] for x in data]

for code in codes:
	from subprocess import call
	call(["wget", "https://files.rcsb.org/view/%s.pdb" % code])
