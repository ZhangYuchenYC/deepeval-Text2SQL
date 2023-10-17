import json
from glob import glob

"""
def problematic(j, n):
    question = j["question"]
    query = j["sql"]

    ls = [l.split("=>")[0].strip() for l in j["prompt"].split("Translate text to SQL:")[-1].strip().split("\n")]
    ls2 = [l.split("=>")[1].strip() for l in j["prompt"].split("Translate text to SQL:")[-1].strip().split("\n")]
    
    c1, c2 = 0, 0
    for l in ls:
        if l.strip() != question.strip():
            c1 += 1
    for l in ls2:
        if l.strip() != query.strip():
            c2 += 1
    if c1 != n-1 or c2 != n:
        return True
    return False

for pt, el in [(3,2), (4,6), (5,2), (6,6), (7,2), (8,6)]:

    for f in glob("others*/*_%s_*"%pt):
        good_js = []
        appeared = {}
        c=0
        for l in open(f):
            try:
                j = json.loads(l)
            except:
                print(f)
            if problematic(j, el):
                c+=1
            else:
                good_js.append(j)

        print(f, c)
        #if c != 0:
        #    with open(f, "w") as fout:
        #        for j in good_js:
        #            print(json.dumps(j), file=fout)
"""

for f in glob("others*/*"):
    print(f)
    good_js = []
    q_appeared = {}

    c=0
    for l in open(f):
        j = json.loads(l)
        question = j["question"]
        sql = j["sql"]

        if question not in q_appeared:
            q_appeared[question] = 1
            good_js.append(j)
    print(f, len(good_js))

    with open(f, "w") as fout:
        for j in good_js:
            print(json.dumps(j), file=fout)
