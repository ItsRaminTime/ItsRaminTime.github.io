import os
from subprocess import call

list = [name for name in os.listdir("/Users/raminahmari/Downloads/GPCR-Visualizer/Interactions/Single Frame") if os.path.isdir(os.path.join("/Users/raminahmari/Downloads/GPCR-Visualizer/Interactions/Single Frame", name))]

for code in list:
    print(code)
    call(["wget", "https://files.rcsb.org/view/%s.pdb" % code])