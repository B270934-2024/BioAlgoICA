import re
arg1="fastaseq.fasta"
print(f"{arg1}")
print(re.findall(r".fasta$",f"{arg1}"))
