from glob import glob
for f in glob("*/*"):
    print(f, len([1 for l in open(f)]))
