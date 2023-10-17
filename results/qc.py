import time
from glob import glob
for f in glob("*/*"):
    c = 0
    for l in open(f):
        c+=1

    if f.startswith("spider") and c != 1034:
        print(f, c)
    elif f.startswith("others"):
        if ("prompt_9" in f or "prompt_10" in f):
            if c != 2470:
                print(f, c)
        else:
            if c != 3034:
                print(f, c)
