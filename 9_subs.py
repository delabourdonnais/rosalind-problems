def get_subs(s, t):
    subs = []
    idx = 0
    while True:
        sub = s.find(t, idx)
        if sub == -1:
            break
        subs.append(sub+1)
        idx = sub + 1
    for sub in subs:
        print sub,
